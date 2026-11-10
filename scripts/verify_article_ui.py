#!/usr/bin/env python3
"""서재 글 화면 시각 검수 스크립트 (6가지 뷰포트·테마 캡처 및 배치·대비·표·도식·alt 측정).

사용법:
  python3 -P scripts/verify_article_ui.py <build_dir> <out_dir> [--path /digest/roguelike-wikipedia/]
"""
import argparse
import json
import socket
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

CONFIGS = [
    ("wide-light", 1440, 900, 1, "light"),
    ("wide-dark", 1440, 900, 1, "dark"),
    ("mid-light", 1024, 800, 1, "light"),
    ("narrow-light", 375, 812, 2, "light"),
    ("narrow-dark", 375, 812, 2, "dark"),
    ("min360-light", 360, 740, 2, "light"),
]

MEASURE_JS = r"""
() => {
  const r = (el) => { if (!el) return null; const b = el.getBoundingClientRect();
    return {x: +b.left.toFixed(1), y: +(b.top + scrollY).toFixed(1), w: +b.width.toFixed(1), h: +b.height.toFixed(1), right: +b.right.toFixed(1)}; };
  const parseRGB = (s) => { const m = s.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return {r:p[0], g:p[1], b:p[2], a: p.length > 3 ? p[3] : 1}; };
  const lum = (c) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
  const blend = (fg, bg) => ({r: fg.r * fg.a + bg.r * (1 - fg.a), g: fg.g * fg.a + bg.g * (1 - fg.a), b: fg.b * fg.a + bg.b * (1 - fg.a), a: 1});
  const ratio = (a, b) => { const la = lum(a), lb = lum(b); return +((Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05)).toFixed(2); };
  const bgOf = (el) => { let layers = []; let e = el;
    while (e && e.nodeType === 1) { const c = parseRGB(getComputedStyle(e).backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; } e = e.parentElement; }
    let base = {r: 255, g: 255, b: 255, a: 1}; if (!layers.length || layers[layers.length - 1].a < 1) base = parseRGB(getComputedStyle(document.documentElement).backgroundColor) || base;
    for (let i = layers.length - 1; i >= 0; i--) base = blend(layers[i], base); return base; };
  const textInfo = (el, label) => { if (!el) return {label, missing: true}; const cs = getComputedStyle(el); const fg = parseRGB(cs.color); const bg = bgOf(el);
    return {label, fontSize: cs.fontSize, fontWeight: cs.fontWeight, lineHeight: cs.lineHeight, family: cs.fontFamily.split(',')[0], color: cs.color, contrast: ratio(blend(fg, bg), bg)}; };

  const content = document.querySelector('.post-content');
  const out = {};
  out.viewport = {w: innerWidth, h: innerHeight};
  out.theme = document.documentElement.dataset.theme || '(none)';
  out.docScrollWidth = document.documentElement.scrollWidth;
  out.bodyScrollWidth = document.body.scrollWidth;
  out.horizontalOverflow = document.documentElement.scrollWidth > innerWidth;
  out.content = r(content);

  const wide = [];
  content.querySelectorAll('*').forEach((el) => { const b = el.getBoundingClientRect(); if (b.width === 0) return;
    if (el.closest('.table-scroll') && !el.classList.contains('table-scroll')) return;
    if (b.right > innerWidth + 0.5 || b.left < -0.5) wide.push({tag: el.tagName, cls: el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className, left: b.left, right: b.right}); });
  out.elementsBeyondViewport = wide.slice(0, 20);

  const cover = document.querySelector('.entry-cover img');
  out.cover = cover ? {complete: cover.complete, natural: [cover.naturalWidth, cover.naturalHeight], rect: r(cover), alt: cover.getAttribute('alt')} : null;
  out.header = {title: r(document.querySelector('.post-title')), lead: r(document.querySelector('.post-lead')), meta: r(document.querySelector('.post-meta')), cover: r(document.querySelector('.entry-cover'))};

  out.images = [...content.querySelectorAll('img')].map((img) => {
    const p = img.closest('p'); let cap = p ? p.nextElementSibling : null; let capInP = false;
    const emSame = p ? p.querySelector('em') : null; if (emSame) { cap = emSame; capInP = true; }
    const capRect = cap ? r(cap) : null; const ir = r(img);
    return {src: img.src.split('/').pop(), complete: img.complete, natural: [img.naturalWidth, img.naturalHeight], alt: img.getAttribute('alt'), rect: ir,
      parentTag: img.parentElement.tagName, captionTag: cap ? cap.tagName : null, captionInSameP: capInP,
      captionText: cap ? cap.textContent.slice(0, 40) : null, captionRect: capRect,
      captionAlign: cap ? getComputedStyle(cap).textAlign : null,
      captionFont: cap ? getComputedStyle(cap).fontSize : null,
      gapImgToCaption: capRect && ir ? +(capRect.y - (ir.y + ir.h)).toFixed(1) : null,
      leftDiff: capRect && ir ? +(capRect.x - ir.x).toFixed(1) : null,
      contentLeftDiff: ir ? +(ir.x - r(content).x).toFixed(1) : null,
      contentRightDiff: ir ? +(r(content).right - ir.right).toFixed(1) : null};
  });

  const fig = content.querySelector('figure.blog-diagram');
  if (fig) {
    const svgs = [...fig.querySelectorAll('svg')];
    out.diagram = {figure: r(fig), childTags: [...fig.children].map((c) => c.tagName + (c.className && c.className.baseVal ? '.' + c.className.baseVal : '')),
      pInsideFigure: fig.querySelectorAll('p').length, brInsideFigure: fig.querySelectorAll('br').length,
      parentTag: fig.parentElement.tagName, prevTag: fig.previousElementSibling && fig.previousElementSibling.tagName,
      strayPAround: [fig.previousElementSibling, fig.nextElementSibling].filter((e) => e && e.tagName === 'P' && !e.textContent.trim()).length,
      figcaption: textInfo(fig.querySelector('figcaption'), 'figcaption'), figcaptionRect: r(fig.querySelector('figcaption')), svgs: []};
    svgs.forEach((svg) => {
      const cs = getComputedStyle(svg); const vb = svg.viewBox.baseVal; const rect = svg.getBoundingClientRect();
      const scale = rect.width / (vb.width || 1);
      const info = {cls: svg.className.baseVal, display: cs.display, rect: r(svg), viewBox: [vb.width, vb.height], scale: +scale.toFixed(3),
        dashedCount: svg.querySelectorAll('line[stroke-dasharray], path[stroke-dasharray]').length, texts: []};
      if (cs.display !== 'none') {
        const rects = [...svg.querySelectorAll('rect')].filter((x) => x.getAttribute('x') !== null).map((x) => ({x: +x.getAttribute('x'), y: +x.getAttribute('y'), w: +x.getAttribute('width'), h: +x.getAttribute('height')}));
        svg.querySelectorAll('text').forEach((t) => {
          const bb = t.getBBox(); const tx = +t.getAttribute('x'), ty = +t.getAttribute('y');
          const box = rects.filter((b) => tx >= b.x && tx <= b.x + b.w && ty >= b.y && ty <= b.y + b.h).sort((a, b) => a.w * a.h - b.w * b.h)[0];
          const tcs = getComputedStyle(t);
          info.texts.push({text: t.textContent, fontPx: +(parseFloat(t.getAttribute('font-size')) * scale).toFixed(2),
            fill: tcs.fill, family: tcs.fontFamily.split(',')[0],
            bbox: [+bb.x.toFixed(1), +bb.y.toFixed(1), +bb.width.toFixed(1), +bb.height.toFixed(1)],
            box: box || null,
            rightPad: box ? +((box.x + box.w) - (bb.x + bb.width)).toFixed(1) : null,
            leftPad: box ? +(bb.x - box.x).toFixed(1) : null,
            topPad: box ? +(bb.y - box.y).toFixed(1) : null,
            bottomPad: box ? +((box.y + box.h) - (bb.y + bb.height)).toFixed(1) : null});
        });
        info.svgBg = getComputedStyle(svg).backgroundColor;
      }
      out.diagram.svgs.push(info);
    });
  }

  out.tables = [...content.querySelectorAll('table')].map((t, i) => {
    const wrap = t.closest('.table-scroll'); const th = t.querySelector('thead th'); const td = t.querySelector('tbody td');
    const colWidths = [...t.querySelectorAll('tbody tr:first-child td')].map((c) => Math.round(c.getBoundingClientRect().width));
    const maxLinesPerCell = Math.max(...[...t.querySelectorAll('td')].map((c) => Math.round((c.getBoundingClientRect().height - 16) / parseFloat(getComputedStyle(c).lineHeight))));
    return {i: i + 1, cols: t.querySelectorAll('thead th').length, rows: t.querySelectorAll('tbody tr').length,
      wrapper: wrap ? wrap.className : null, wrapClient: wrap ? wrap.clientWidth : null, wrapScroll: wrap ? wrap.scrollWidth : null,
      tableRect: r(t), wrapRect: r(wrap), th: textInfo(th, 'th'), td: textInfo(td, 'td'),
      colWidths, maxLinesPerCell,
      firstColWidths: [...t.querySelectorAll('tbody tr td:first-child')].slice(0, 3).map((c) => +c.getBoundingClientRect().width.toFixed(1)),
      maxCellHeight: Math.max(...[...t.querySelectorAll('td')].map((c) => c.getBoundingClientRect().height))};
  });

  const notes = [...document.querySelectorAll('aside.sidenote')];
  const markers = [...content.querySelectorAll('sup[id^="fnref"], a.footnote-ref')].filter((m) => m.tagName === 'SUP' || !m.closest('sup'));
  out.footnoteMarkers = markers.length;
  out.footnotesSection = (() => { const f = document.querySelector('.footnotes'); if (!f) return null; const cs = getComputedStyle(f);
    return {display: cs.display, visibility: cs.visibility, rect: r(f), items: f.querySelectorAll('li').length, text: textInfo(f.querySelector('li p') || f.querySelector('li'), 'footnote li')}; })();
  out.sidenotes = notes.map((n, i) => { const m = markers[i]; const nr = r(n); const mr = m ? r(m) : null;
    return {i: i + 1, rect: nr, markerY: mr ? mr.y : null, offsetFromMarker: mr ? +(nr.y - mr.y).toFixed(1) : null,
      gapFromContent: +(nr.x - r(content).right).toFixed(1), beyondViewport: nr.right > innerWidth, text: textInfo(n, 'sidenote')}; });
  out.sidenoteOverlaps = [];
  for (let i = 1; i < notes.length; i++) { const a = notes[i - 1].getBoundingClientRect(), b = notes[i].getBoundingClientRect();
    out.sidenoteOverlaps.push(+(b.top - a.bottom).toFixed(1)); }

  const bodyP = [...content.querySelectorAll(':scope > p')].find((p) => p.textContent.length > 100);
  out.textSamples = [textInfo(bodyP, 'body p'), textInfo(content.querySelector('h2'), 'h2'),
    textInfo(content.querySelector('p > em'), 'caption em'), textInfo(content.querySelector('code'), 'inline code'),
    textInfo(document.querySelector('.post-meta'), 'post-meta'), textInfo(content.querySelector('ol li'), 'summary li')];
  out.bodyPWidth = bodyP ? r(bodyP).w : null;
  return out;
}
"""


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def settle(page):
    h = page.evaluate("document.documentElement.scrollHeight")
    y = 0
    while y < h:
        page.evaluate(f"window.scrollTo(0, {y})")
        page.wait_for_timeout(120)
        y += 600
        h = page.evaluate("document.documentElement.scrollHeight")
    page.wait_for_load_state("networkidle")
    page.evaluate("Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))")
    page.evaluate("document.fonts.ready")
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1500)


def clip_shot(page, path, el_selector=None, rect=None, pad=24, nth=0):
    if el_selector:
        rect = page.evaluate(
            """([s, n]) => { const e = document.querySelectorAll(s)[n]; if (!e) return null; const b = e.getBoundingClientRect();
            return {x: b.left + scrollX, y: b.top + scrollY, w: b.width, h: b.height}; }""",
            [el_selector, nth],
        )
    if not rect:
        return None
    vw = page.viewport_size["width"]
    x = max(0, rect["x"] - pad)
    y = max(0, rect["y"] - pad)
    w = min(vw - x, rect["w"] + pad * 2)
    page.screenshot(path=str(path), full_page=True, clip={"x": x, "y": y, "width": w, "height": rect["h"] + pad * 2})
    return str(path)


def viewport_shot(page, selector, path, nth=0):
    loc = page.locator(selector).nth(nth)
    loc.scroll_into_view_if_needed()
    page.evaluate(
        "([s, n]) => { const e = document.querySelectorAll(s)[n]; window.scrollTo(0, e.getBoundingClientRect().top + scrollY - 16); }",
        [selector, nth],
    )
    page.wait_for_timeout(200)
    page.screenshot(path=str(path))


def main():
    parser = argparse.ArgumentParser(description="Verify blog article UI/UX across 6 states")
    parser.add_argument("build_dir", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--path", default="/digest/roguelike-wikipedia/")
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    port = free_port()
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1", "--directory", str(args.build_dir)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1.0)
    url = f"http://127.0.0.1:{port}{args.path}"
    report = {"url": url, "configs": {}, "interactions": {}, "tables_375": {}}

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for name, w, h, dpr, scheme in CONFIGS:
                ctx = browser.new_context(
                    viewport={"width": w, "height": h},
                    device_scale_factor=dpr,
                    color_scheme=scheme,
                    is_mobile=(w < 500),
                    has_touch=(w < 500),
                )
                page = ctx.new_page()
                failed = []
                page.on("requestfailed", lambda req: failed.append(req.url))
                page.on("response", lambda res: failed.append(f"{res.status} {res.url}") if res.status >= 400 else None)
                page.goto(url, wait_until="load")
                settle(page)
                m = page.evaluate(MEASURE_JS)
                m["failedRequests"] = failed
                d = args.out_dir / name
                d.mkdir(exist_ok=True)
                page.screenshot(path=str(d / "full.png"), full_page=True)
                page.screenshot(path=str(d / "first-screen.png"))
                shots = {}
                if page.locator("figure.blog-diagram").count() > 0:
                    if w < 500:
                        viewport_shot(page, "figure.blog-diagram", d / "diagram.png")
                        shots["diagram"] = str(d / "diagram.png")
                    else:
                        shots["diagram"] = clip_shot(page, d / "diagram.png", "figure.blog-diagram")
                t_count = page.locator(".post-content table").count()
                for i in range(t_count):
                    shots[f"table{i+1}"] = clip_shot(page, d / f"table{i+1}.png", ".post-content table", nth=i)
                img_count = page.locator(".post-content p:has(> img)").count()
                for i in range(img_count):
                    rect = page.evaluate(
                        """(n) => { const p = document.querySelectorAll('.post-content p:has(> img)')[n]; if (!p) return null;
                        const a = p.getBoundingClientRect(); const c = p.nextElementSibling; const b = c ? c.getBoundingClientRect() : a;
                        return {x: Math.min(a.left, b.left) + scrollX, y: a.top + scrollY, w: Math.max(a.right, b.right) - Math.min(a.left, b.left), h: b.bottom - a.top}; }""",
                        i,
                    )
                    shots[f"image{i+2}"] = clip_shot(page, d / f"image{i+2:02d}.png", rect=rect)
                if m["sidenotes"]:
                    for s in m["sidenotes"]:
                        rr = {"x": m["content"]["x"], "y": s["rect"]["y"] - 80, "w": s["rect"]["right"] - m["content"]["x"], "h": s["rect"]["h"] + 160}
                        shots[f"sidenote{s['i']}"] = clip_shot(page, d / f"sidenote{s['i']}.png", rect=rr, pad=16)
                elif page.locator(".footnotes").count() > 0:
                    shots["footnotes"] = clip_shot(page, d / "footnotes.png", ".footnotes")
                m["shots"] = shots
                report["configs"][name] = m
                ctx.close()

            # 375 폭 표 키 큰 뷰포트 단발 캡처 및 측정
            t375_dir = args.out_dir / "tables-375"
            t375_dir.mkdir(exist_ok=True)
            ctx_t = browser.new_context(viewport={"width": 375, "height": 4800}, device_scale_factor=1, is_mobile=True, has_touch=True, color_scheme="light")
            page_t = ctx_t.new_page()
            page_t.add_init_script(
                "document.addEventListener('DOMContentLoaded', () => { const s = document.createElement('style'); s.textContent = 'html{scroll-behavior:auto!important}'; document.head.appendChild(s); });"
            )
            page_t.goto(url, wait_until="load")
            page_t.evaluate("document.fonts.ready")
            page_t.wait_for_timeout(1200)
            t_count = page_t.locator(".post-content .table-scroll").count()
            for i in range(t_count):
                el = page_t.locator(".post-content .table-scroll").nth(i)
                box = el.bounding_box()
                page_t.evaluate(f"window.scrollTo(0, {box['y']} + scrollY - 20)")
                page_t.wait_for_timeout(200)
                box = el.bounding_box()
                th = min(box["height"] + 40, 4800 - max(0, box["y"] - 20))
                page_t.screenshot(path=str(t375_dir / f"375-table{i+1}.png"), clip={"x": 0, "y": max(0, box["y"] - 20), "width": 375, "height": th})
                report["tables_375"][f"table{i+1}"] = {
                    "height": round(box["height"]),
                    "overflowing": page_t.evaluate(f"document.querySelectorAll('.post-content .table-scroll')[{i}].classList.contains('is-overflowing')"),
                    "colWidths": page_t.evaluate(f"[...document.querySelectorAll('.post-content table')[{i}].querySelectorAll('tbody tr:first-child td')].map(c => Math.round(c.getBoundingClientRect().width))"),
                    "maxLinesPerCell": page_t.evaluate(f"Math.max(...[...document.querySelectorAll('.post-content table')[{i}].querySelectorAll('td')].map(c => Math.round((c.getBoundingClientRect().height - 16) / parseFloat(getComputedStyle(c).lineHeight))))"),
                }
            ctx_t.close()
            browser.close()
    finally:
        server.terminate()
        server.wait(timeout=5)

    (args.out_dir / "metrics.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    (args.out_dir / "tables-375" / "tables-375.json").write_text(json.dumps(report["tables_375"], ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", args.out_dir / "metrics.json")


if __name__ == "__main__":
    main()
