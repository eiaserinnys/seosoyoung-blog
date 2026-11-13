#!/usr/bin/env python3
"""글 머리 정렬 검수 (카드 #1296): 넓은 화면에서 메타 줄과 제목 사이 틈(gap)과
제목·요약 마지막 줄 baseline, 좁은 화면 불변을 기준 빌드와 고친 빌드에서 견준다.

사용법:
  PLAYWRIGHT_BROWSERS_PATH="$HOME/.cache/ms-playwright" \
    python3 -P scripts/verify_post_header.py \
      --after <고친 빌드> --before <기준 빌드> --out <캡처 폴더> --sample 60

표본: 각 빌드의 digest/*/index.html 중 post-lead 가 있는 글을 날짜 내림차순 n편
(세라피엘 header_gap_survey.py 의 고르기 방식)에 고정 글 세 편(긴 제목·짧은 요약,
요약 없음, 갤러리)을 더한다.
폭: 넓은 폭 1440·1200·1024, 좁은 폭 820·360.

실패 조건(카드 #1296 기준본 계약 1~6):
1) before 표본의 1440px gap 이 모두 60px 미만(문제 글을 못 잡음)
2) after 넓은 폭에서 표본 전체 gap 최대 - 최소 > 1px
3) after 넓은 폭에서 요약 있는 글의 제목 마지막 줄과 요약 마지막 줄 baseline 차 > 1px
4) after 넓은 폭에서 메타 left 와 제목 left 차 > 1px, 메타 right > 요약 left,
   메타 높이가 before 보다 1px 넘게 큼(줄바꿈)
5) before 에서 제목이 밀리지 않았던 글(gap 이 before 표본 최솟값+1px 이하)과 갤러리 글은
   넓은 폭에서 좌표가 before 와 1px 넘게 다름
6) 좁은 폭에서 표본 전체의 좌표가 before 와 1px 넘게 다름

조건 5의 메타 너비는 견주지 않는다. 조건 4가 메타 오른쪽이 요약 왼쪽을 넘지 못하게 하므로
감싸개(1/8 칸) 안에서 메타 상자는 좁아질 수밖에 없고, 메타에는 배경과 테두리가 없어
상자 너비는 화면에 보이지 않는다. 대신 메타 안 글의 합집합 범위와 top/left/height 를 견준다.
"""
import argparse
import re
import socket
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import Error as PlaywrightError, sync_playwright

WIDE_WIDTHS = (1440, 1200, 1024)
NARROW_WIDTHS = (820, 360)
CAPTURE_WIDTHS = (1440, 1024, 820, 360)

FIXED_PATHS = [
    "/digest/coding-agents-change-sde-forever/",
    "/digest/marc-andreessen-ai-native-startups/",
    "/gallery/seosoyoung-loose-watercolor-drift/",
]
GALLERY_PATH = FIXED_PATHS[-1]

TIME_RE = re.compile(r"<time class=mono datetime=(\d{4}-\d{2}-\d{2})")

MEASURE_JS = r"""
() => {
  const rect = (el) => { if (!el) return null; const b = el.getBoundingClientRect();
    return {top: +b.top.toFixed(2), left: +b.left.toFixed(2), width: +b.width.toFixed(2),
      height: +b.height.toFixed(2), right: +b.right.toFixed(2), bottom: +b.bottom.toFixed(2)}; };
  // 높이 0 인라인 블록의 top 은 그 줄의 baseline 이다. 끝에 붙여 마지막 줄,
  // 줄이 넘쳐 높이가 바뀌면 앞에 붙여 첫 줄 baseline 과 줄 수로 마지막 줄을 구한다.
  const baseline = (el) => {
    if (!el) return null;
    const lineHeight = parseFloat(getComputedStyle(el).lineHeight);
    const height0 = el.getBoundingClientRect().height;
    const makeProbe = () => {
      const probe = document.createElement('span');
      probe.style.cssText = 'display:inline-block;width:0;height:0;margin:0;padding:0;border:0;line-height:0;vertical-align:baseline';
      return probe;
    };
    const end = makeProbe();
    el.appendChild(end);
    let y = end.getBoundingClientRect().top;
    const height1 = el.getBoundingClientRect().height;
    end.remove();
    if (Math.abs(height1 - height0) > 0.5 && lineHeight > 0) {
      const start = makeProbe();
      el.insertBefore(start, el.firstChild);
      const startTop = start.getBoundingClientRect().top;
      start.remove();
      const lines = Math.round(height0 / lineHeight);
      y = startTop + Math.max(0, lines - 1) * lineHeight;
    }
    return +y.toFixed(2);
  };
  const textExtent = (el) => {
    if (!el) return null;
    const range = document.createRange();
    range.selectNodeContents(el);
    const rects = [...range.getClientRects()].filter((r) => r.width > 0 || r.height > 0);
    if (!rects.length) return null;
    return {left: +Math.min(...rects.map((r) => r.left)).toFixed(2),
      top: +Math.min(...rects.map((r) => r.top)).toFixed(2),
      right: +Math.max(...rects.map((r) => r.right)).toFixed(2),
      bottom: +Math.max(...rects.map((r) => r.bottom)).toFixed(2)};
  };
  const meta = document.querySelector('.post-meta');
  const title = document.querySelector('.post-title');
  const lead = document.querySelector('.post-lead');
  const metaRect = rect(meta);
  const titleRect = rect(title);
  const leadRect = rect(lead);
  return {
    meta: metaRect,
    title: titleRect,
    lead: leadRect,
    metaText: textExtent(meta),
    gap: (metaRect && titleRect) ? +(titleRect.top - metaRect.bottom).toFixed(2) : null,
    titleBaseline: baseline(title),
    leadBaseline: baseline(lead),
    sideBySide: (titleRect && leadRect) ? (leadRect.left >= titleRect.right - 1) : null,
  };
}
"""


def free_port():
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


def serve(build_dir):
    port = free_port()
    proc = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1", "--directory", str(build_dir)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1.0)
    return proc, port


def pick_sample(build_dir, count):
    rows = []
    for page in (build_dir / "digest").glob("*/index.html"):
        html = page.read_text(encoding="utf-8", errors="ignore")
        match = TIME_RE.search(html)
        if match and "post-lead" in html:
            rows.append((match.group(1), "/digest/" + page.parent.name + "/"))
    rows.sort(key=lambda row: row[0], reverse=True)
    paths = [path for _, path in rows[:count]]
    for path in FIXED_PATHS:
        if path not in paths:
            paths.append(path)
    return paths


def settle(page):
    page.evaluate("() => document.fonts.ready.then(() => true)")
    page.wait_for_timeout(80)


def open_page(context, port, path):
    page = context.new_page()
    page.set_default_navigation_timeout(30000)
    page.goto(f"http://127.0.0.1:{port}{path}", wait_until="domcontentloaded")
    settle(page)
    return page


def measure_build(build_dir, paths, errors):
    proc, port = serve(build_dir)
    data = {path: {} for path in paths}
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                for width in WIDE_WIDTHS + NARROW_WIDTHS:
                    context = browser.new_context(viewport={"width": width, "height": 900})
                    context.route("**umami**", lambda route: route.abort())
                    for path in paths:
                        page = None
                        try:
                            page = open_page(context, port, path)
                            if not (build_dir / path.strip("/") / "index.html").exists():
                                errors.append(f"{build_dir.name}: 글 없음 {path}")
                                continue
                            data[path][width] = page.evaluate(MEASURE_JS)
                        except PlaywrightError as exc:
                            errors.append(f"{build_dir.name} {width} {path}: {exc}")
                        finally:
                            if page is not None:
                                page.close()
                    context.close()
            finally:
                browser.close()
    finally:
        proc.terminate()
        proc.wait(timeout=5)
    return data


def capture_build(build_dir, out_dir, articles, tag):
    proc, port = serve(build_dir)
    saved = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                for width in CAPTURE_WIDTHS:
                    context = browser.new_context(viewport={"width": width, "height": 900})
                    context.route("**umami**", lambda route: route.abort())
                    for path in articles:
                        page = None
                        try:
                            page = open_page(context, port, path)
                            slug = path.strip("/").split("/")[-1]
                            target = out_dir / f"{tag}-{width}-{slug}.png"
                            page.locator(".post-header").screenshot(path=str(target))
                            saved.append(target)
                        except PlaywrightError as exc:
                            print(f"캡처 실패 {tag} {width} {path}: {exc}", file=sys.stderr)
                        finally:
                            if page is not None:
                                page.close()
                    context.close()
            finally:
                browser.close()
    finally:
        proc.terminate()
        proc.wait(timeout=5)
    return saved


def rect_diffs(before, after, fields):
    if before is None or after is None:
        return ["요소 없음"] if before is not after else []
    return [f"{field} {before[field]}→{after[field]}" for field in fields
            if abs(before[field] - after[field]) > 1.0]


def cell_verdict(path, width, before, after):
    issues = []
    before_lead, after_lead = before.get("lead"), after.get("lead")
    before_meta, after_meta = before.get("meta"), after.get("meta")
    after_title = after.get("title")
    if width in WIDE_WIDTHS:
        if after_lead and after.get("sideBySide") is False:
            issues.append("요약이 제목 오른쪽에 나란히 있지 않음")
        if after_meta and after_title and abs(after_meta["left"] - after_title["left"]) > 1.0:
            issues.append(f"메타 left {after_meta['left']} vs 제목 left {after_title['left']}")
        if after_meta and after_lead and after_meta["right"] > after_lead["left"] + 0.5:
            issues.append(f"메타 right {after_meta['right']} > 요약 left {after_lead['left']}")
        if after_meta and before_meta and after_meta["height"] > before_meta["height"] + 1.0:
            issues.append(f"메타 높이 {before_meta['height']}→{after_meta['height']} (줄바꿈)")
        if after_lead and after.get("titleBaseline") is not None and after.get("leadBaseline") is not None:
            diff = abs(after["titleBaseline"] - after["leadBaseline"])
            if diff > 1.0:
                issues.append(f"마지막 줄 baseline 차 {diff:.2f}px")
    return issues


def main():
    parser = argparse.ArgumentParser(description="글 머리(메타·제목·요약) 정렬 전후 검수")
    parser.add_argument("--after", type=Path, required=True, help="고친 빌드 폴더")
    parser.add_argument("--before", type=Path, required=True, help="기준 빌드 폴더")
    parser.add_argument("--out", type=Path, required=True, help="대표 캡처 폴더")
    parser.add_argument("--sample", type=int, default=60, help="날짜 내림차순으로 고를 글 수")
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    paths = pick_sample(args.after, args.sample)
    errors = []
    print(f"표본 {len(paths)}편 (고정 글 {len(FIXED_PATHS)}편 포함), 폭 {WIDE_WIDTHS} 넓은 폭 / {NARROW_WIDTHS} 좁은 폭")

    before = measure_build(args.before, paths, errors)
    after = measure_build(args.after, paths, errors)

    failures = list(errors)
    cell_issues = {}
    for path in paths:
        for width in WIDE_WIDTHS + NARROW_WIDTHS:
            issues = cell_verdict(path, width, before[path].get(width, {}), after[path].get(width, {}))
            if issues:
                cell_issues[(path, width)] = issues

    before_gaps = {path: before[path].get(1440, {}).get("gap") for path in paths}
    if not any(gap is not None and gap >= 60 for gap in before_gaps.values()):
        failures.append("조건 1: before 표본의 1440px gap 이 모두 60px 미만이라 문제 글을 잡지 못함")

    for width in WIDE_WIDTHS:
        gaps = [after[path].get(width, {}).get("gap") for path in paths]
        if any(gap is None for gap in gaps):
            failures.append(f"조건 2: {width}px 에서 gap 을 못 잰 글 {sum(gap is None for gap in gaps)}편")
        elif max(gaps) - min(gaps) > 1.0:
            failures.append(f"조건 2: {width}px after gap 편차 {max(gaps) - min(gaps):.2f}px "
                            f"(최소 {min(gaps)}, 최대 {max(gaps)})")

    measured_gaps = [gap for gap in before_gaps.values() if gap is not None]
    min_gap = min(measured_gaps) if measured_gaps else 0.0
    unpushed = {path for path, gap in before_gaps.items() if gap is not None and gap <= min_gap + 1.0}
    stable = unpushed | {GALLERY_PATH}
    for path in sorted(stable):
        for width in WIDE_WIDTHS:
            cell = cell_issues.get((path, width), [])
            if cell:
                continue
            before_cell, after_cell = before[path].get(width, {}), after[path].get(width, {})
            diffs = rect_diffs(before_cell.get("title"), after_cell.get("title"),
                               ("top", "left", "width", "height"))
            diffs += rect_diffs(before_cell.get("lead"), after_cell.get("lead"),
                                ("top", "left", "width", "height"))
            before_meta, after_meta = before_cell.get("meta"), after_cell.get("meta")
            diffs += [f"메타 {item}" for item in rect_diffs(before_meta, after_meta, ("top", "left", "height"))]
            diffs += [f"메타 글 범위 {item}" for item in rect_diffs(
                before_cell.get("metaText"), after_cell.get("metaText"),
                ("top", "left", "right", "bottom"))]
            if diffs:
                cell_issues[(path, width)] = diffs

    for path in paths:
        for width in NARROW_WIDTHS:
            cell = cell_issues.get((path, width), [])
            if cell:
                continue
            before_cell, after_cell = before[path].get(width, {}), after[path].get(width, {})
            diffs = rect_diffs(before_cell.get("meta"), after_cell.get("meta"),
                               ("top", "left", "width", "height"))
            diffs += rect_diffs(before_cell.get("title"), after_cell.get("title"),
                                ("top", "left", "width", "height"))
            diffs += rect_diffs(before_cell.get("lead"), after_cell.get("lead"),
                                ("top", "left", "width", "height"))
            if diffs:
                cell_issues[(path, width)] = diffs

    condition_names = {
        "sideBySide": "넓은 폭 배치", "요약이 제목 오른쪽에": "넓은 폭 배치",
        "메타 left": "조건 4", "메타 right": "조건 4", "메타 높이": "조건 4",
        "마지막 줄 baseline": "조건 3",
    }
    for (path, width), issues in sorted(cell_issues.items()):
        for issue in issues:
            condition = "조건 6" if width in NARROW_WIDTHS else "조건 5"
            for prefix, name in condition_names.items():
                if issue.startswith(prefix):
                    condition = name
                    break
            failures.append(f"{condition}: {width}px {path}: {issue}")

    for path in paths:
        for width in WIDE_WIDTHS + NARROW_WIDTHS:
            before_gap = before[path].get(width, {}).get("gap")
            after_gap = after[path].get(width, {}).get("gap")
            issues = cell_issues.get((path, width), [])
            verdict = "ok" if not issues else "FAIL " + "; ".join(issues)
            print(f"{width:>4} {path} before-gap={before_gap} after-gap={after_gap} {verdict}")

    largest = max(paths, key=lambda path: before_gaps[path] if before_gaps.get(path) is not None else float("-inf"))
    print(f"before 최대 gap 글: {largest} ({before_gaps[largest]}px)")
    capture_articles = [largest, FIXED_PATHS[0], GALLERY_PATH]
    saved = capture_build(args.before, args.out, capture_articles, "before")
    saved += capture_build(args.after, args.out, capture_articles, "after")
    print(f"대표 캡처 {len(saved)}장 → {args.out}")

    print("실패 목록:")
    if failures:
        for index, failure in enumerate(failures, 1):
            print(f"  {index}. {failure}")
    else:
        print("  없음")

    print(f"요약: 글 {len(paths)}편 × 폭 {len(WIDE_WIDTHS + NARROW_WIDTHS)}개, 실패 {len(failures)}건, "
          f"판정 {'통과' if not failures else '실패'}")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
