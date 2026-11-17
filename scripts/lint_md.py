#!/usr/bin/env python3
"""
발행 전 마크다운 인라인 마크업 깨짐 린트.

goldmark(Hugo)가 CJK 인접 강조 구분자를 닫지 못해 raw `**`/`*`/`_`가
그대로 출력되는 부류를 소스 단계에서 잡는다. 취소선(물결표) 부류는
hugo.toml에서 strikethrough=false로 엔진 레벨에서 막았으므로 참고용으로만 경고한다.

다이제스트 원문 형식 오타 두 가지도 잡는다.
- doubled-quote: 본문(코드·인라인 코드 제외, front matter 제외)에서 곧은 큰따옴표
  두 개가 인용 여는 자리에 겹친 자리. `content:"";` 같은 빈 문자열은 잡지 않는다.
- merged-heading: `>` 로 시작하는 줄 중간에 공백 뒤 `##`~`######` 와 공백이 와
  인용 줄과 제목이 한 줄에 붙은 자리.

사용:
  python3 scripts/lint_md.py content/posts/some-post.md [more.md ...]
  python3 scripts/lint_md.py            # content/posts, content/digest 전체
  python3 scripts/lint_md.py --rules doubled-quote,merged-heading   # 고른 규칙만

종료 코드: 실행한 규칙의 위험 패턴이 하나라도 있으면 1.
"""
import argparse
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

# 곧은 큰따옴표 두 개가 여는 자리에 겹친 자리. 뒤에 글자가 와야 여는 인용이고,
# 세미콜론·쉼표·닫는 괄호·따옴표·강조 부호가 바로 오면 빈 문자열이나 닫는 자리다.
DOUBLED_QUOTE = re.compile(r'""(?=[^\s"\'*`;:,.)\]}])')
# 인용 줄 끝에 제목이 붙은 자리(줄 머리의 `> ## 제목`은 정상이라 잡지 않는다).
MERGED_HEADING = re.compile(r"^>\s.*?\s#{2,6}\s")

RULES = (
    "bold-cjk", "italic-cjk-star", "italic-cjk-underscore", "tilde",
    "doubled-quote", "merged-heading",
)


def strip_code(text: str) -> str:
    text = FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    text = INLINE_CODE.sub(" ", text)
    return text


def front_matter_end(lines):
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                return index + 1
    return 0


def lint_file(path: pathlib.Path, rules):
    raw = path.read_text(encoding="utf-8")
    problems = []
    if rules & {"bold-cjk", "italic-cjk-star", "italic-cjk-underscore", "tilde"}:
        body = strip_code(raw)
        for lineno, line in enumerate(body.splitlines(), 1):
            for key, label, rx in (
                ("bold-cjk", "bold+CJK: **…**한글 → <strong>…</strong> 사용", BOLD_CJK),
                ("italic-cjk-star", "italic+CJK: *…*한글 → <em>…</em> 사용", ITALIC_STAR_CJK),
                ("italic-cjk-underscore", "italic+CJK: _…_한글 → <em>…</em> 사용", ITALIC_US_CJK),
            ):
                if key in rules and rx.search(line):
                    problems.append((lineno, "ERROR", label, line.strip()[:80]))
            # 물결표는 strikethrough=false 전제에서 경고만
            if "tilde" in rules and len(TILDE_PAIR.findall(line)) >= 1 and line.count("~") >= 2:
                problems.append((lineno, "warn", "물결표 다수: 취소선 오인 소지(설정으로 차단됨)", line.strip()[:80]))
    if rules & {"doubled-quote", "merged-heading"}:
        lines = raw.splitlines()
        start = front_matter_end(lines)
        body = strip_code("\n".join(lines[start:]))
        for offset, line in enumerate(body.splitlines()):
            lineno = start + offset + 1
            if "doubled-quote" in rules and DOUBLED_QUOTE.search(line):
                problems.append((lineno, "ERROR",
                                 'doubled-quote: 곧은 큰따옴표 두 겹("")이 인용 여는 자리에 겹침',
                                 line.strip()[:80]))
            if "merged-heading" in rules and MERGED_HEADING.match(line):
                problems.append((lineno, "ERROR",
                                 "merged-heading: 인용 줄에 제목이 붙음 → 인용 줄·빈 줄·제목 줄로 나눈다",
                                 line.strip()[:80]))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="발행 전 마크다운 형식 린트")
    parser.add_argument("files", nargs="*", help="검사할 파일. 없으면 content/posts·content/digest 전체")
    parser.add_argument("--rules", default=None,
                        help="검사할 규칙을 쉼표로 고른다: " + ", ".join(RULES))
    args = parser.parse_args()

    if args.rules:
        selected = [name.strip() for name in args.rules.split(",") if name.strip()]
        unknown = [name for name in selected if name not in RULES]
        if unknown:
            parser.error("알 수 없는 규칙: " + ", ".join(unknown))
        rules = set(selected)
    else:
        rules = set(RULES)

    files = [pathlib.Path(name) for name in args.files] if args.files else []
    if not files:
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
        for lineno, level, label, snippet in lint_file(f, rules):
            mark = "❌" if level == "ERROR" else "⚠️"
            if level == "ERROR":
                had_error = True
            print(f"{mark} {f}:{lineno} [{level}] {label}\n     …{snippet}…")
    if had_error:
        print("\n위험 패턴 발견. 해당 규칙 위반을 고친 뒤 재검사.")
        return 1
    print(f"[ok] {len(files)}개 파일 검사, 위험 패턴 없음.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
