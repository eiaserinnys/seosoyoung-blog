#!/usr/bin/env python3
"""
발행 전 마크다운 인라인 마크업 깨짐 린트.

goldmark(Hugo)가 CJK 인접 강조 구분자를 닫지 못해 raw `**`/`*`/`_`가
그대로 출력되는 부류를 소스 단계에서 잡는다. 취소선(물결표) 부류는
hugo.toml에서 strikethrough=false로 엔진 레벨에서 막았으므로 참고용으로만 경고한다.

사용:
  python3 scripts/lint_md.py content/posts/some-post.md [more.md ...]
  python3 scripts/lint_md.py            # content/posts, content/digest 전체

종료 코드: 위험 패턴이 하나라도 있으면 1.
"""
import re
import sys
import pathlib

# 코드펜스(```...```)와 인라인 코드(`...`)는 강조 규칙이 적용되지 않으므로 제거한 뒤 검사한다.
FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")

HANGUL = r"가-힣"

# 위험: 닫는 강조 구분자 바로 뒤에 한글이 공백 없이 붙는 경우.
# goldmark는 이 run을 right-flanking으로 보지 못해 닫지 못하고 raw로 출력한다.
BOLD_CJK = re.compile(rf"\*\*[^*\n]+\*\*[{HANGUL}]")
ITALIC_STAR_CJK = re.compile(rf"(?<!\*)\*[^*\n]+\*[{HANGUL}]")
ITALIC_US_CJK = re.compile(rf"(?<!_)_[^_\n]+_[{HANGUL}]")
# 참고: 물결표 두 개 이상(strikethrough 꺼져 있으면 무해하지만 이식성 위해 경고)
TILDE_PAIR = re.compile(r"~[^~\n]*~")


def strip_code(text: str) -> str:
    text = FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    text = INLINE_CODE.sub(" ", text)
    return text


def lint_file(path: pathlib.Path):
    raw = path.read_text(encoding="utf-8")
    body = strip_code(raw)
    problems = []
    for lineno, line in enumerate(body.splitlines(), 1):
        for label, rx, hard in (
            ("bold+CJK: **…**한글 → <strong>…</strong> 사용", BOLD_CJK, True),
            ("italic+CJK: *…*한글 → <em>…</em> 사용", ITALIC_STAR_CJK, True),
            ("italic+CJK: _…_한글 → <em>…</em> 사용", ITALIC_US_CJK, True),
        ):
            if rx.search(line):
                problems.append((lineno, "ERROR", label, line.strip()[:80]))
        # 물결표는 strikethrough=false 전제에서 경고만
        if len(TILDE_PAIR.findall(line)) >= 1 and line.count("~") >= 2:
            problems.append((lineno, "warn", "물결표 다수: 취소선 오인 소지(설정으로 차단됨)", line.strip()[:80]))
    return problems


def main() -> int:
    args = sys.argv[1:]
    if args:
        files = [pathlib.Path(a) for a in args]
    else:
        root = pathlib.Path(__file__).resolve().parent.parent
        files = sorted(
            list((root / "content" / "posts").glob("*.md"))
            + list((root / "content" / "digest").glob("*.md"))
        )
    had_error = False
    for f in files:
        if not f.exists():
            print(f"[skip] {f} (없음)")
            continue
        for lineno, level, label, snippet in lint_file(f):
            mark = "❌" if level == "ERROR" else "⚠️"
            if level == "ERROR":
                had_error = True
            print(f"{mark} {f}:{lineno} [{level}] {label}\n     …{snippet}…")
    if had_error:
        print("\n강조 깨짐 위험 패턴 발견. <strong>/<em> 태그로 교체 후 재검사.")
        return 1
    print(f"[ok] {len(files)}개 파일 검사, 강조 깨짐 위험 없음.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
