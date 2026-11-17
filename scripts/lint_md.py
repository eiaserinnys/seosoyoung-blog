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
  python3 scripts/lint_md.py            # content/posts, content/digest, content/gallery 전체
  python3 scripts/lint_md.py --rules doubled-quote,merged-heading   # 고른 규칙만

종료 코드: 실행한 규칙의 위험 패턴이 하나라도 있으면 1.
"""
import argparse
import re
import sys
import pathlib
import unicodedata

# 코드펜스(```...```)와 인라인 코드(`...`)는 강조 규칙이 적용되지 않으므로 제거한 뒤 검사한다.
FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")

HANGUL = r"가-힣"

ITALIC_US_CJK = re.compile(rf"(?<!_)_[^_\n]+_[{HANGUL}]")
# 참고: 물결표 두 개 이상(strikethrough 꺼져 있으면 무해하지만 이식성 위해 경고)
TILDE_PAIR = re.compile(r"~[^~\n]*~")

# 곧은 큰따옴표 두 개가 여는 자리에 겹친 자리. 뒤에 글자가 와야 여는 인용이고,
# 세미콜론·쉼표·닫는 괄호·따옴표·강조 부호가 바로 오면 빈 문자열이나 닫는 자리다.
DOUBLED_QUOTE = re.compile(r'""(?=[^\s"\'*`;:,.)\]}])')
# 인용 줄 끝에 제목이 붙은 자리(줄 머리의 `> ## 제목`은 정상이라 잡지 않는다).
MERGED_HEADING = re.compile(r"^>\s.*?\s#{2,6}\s")

RULES = (
    "emphasis-flanking", "italic-cjk-underscore", "tilde",
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


# CommonMark는 Unicode P와 S 범주를 문장부호로 취급한다.
def is_punctuation(char):
    return bool(char) and unicodedata.category(char)[0] in "PS"


def is_whitespace(char):
    return char in "\t\n\f\r" or unicodedata.category(char) == "Zs"


def emphasis_lines(raw):
    """본문의 짝 없는 별표가 있는 원문 줄 번호를 돌려준다."""
    lines = raw.splitlines(keepends=True)
    start = front_matter_end(lines)
    # 별표만 마스킹한다. 인접 글자는 flanking 판정에 그대로 필요하다.
    masked = list(raw)
    offset = sum(map(len, lines[:start]))
    for i in range(offset):
        if masked[i] != "\n":
            masked[i] = " "
    body = raw[offset:]
    # 코드와 태그를 먼저 가려 그 안의 $가 수식 구간을 열지 않게 한다.
    shadow = list(body)
    exclusions = (
        (r"(?ms)^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[ \t]*(?:\n|$)", 0),
        (r"(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)", re.S),
        (r"<[/!?A-Za-z][^>\n]*>", 0),
        (r"(?s:\$\$.*?\$\$|\\\[.*?\\\])|\\\([^\n]*?\\\)|(?<![\\$])\$(?!\$)[^\n]*?(?<!\\)\$", 0),
    )
    for pattern, flags in exclusions:
        for match in re.finditer(pattern, "".join(shadow), flags):
            for i in range(offset + match.start(), offset + match.end()):
                if masked[i] == "*":
                    masked[i] = "\0"
                if shadow[i - offset] != "\n":
                    shadow[i - offset] = " "
    # 목적지 안의 중첩 괄호를 포함해 URL은 별표 구분자로 보지 않는다.
    for match in re.finditer(r"\]\(", body):
        depth, pos = 1, match.end()
        while pos < len(body) and depth:
            if body[pos] == "\\":
                pos += 2
                continue
            if body[pos] == "(":
                depth += 1
            elif body[pos] == ")":
                depth -= 1
            pos += 1
        if depth == 0:
            for i in range(offset + match.start(), offset + pos):
                if masked[i] == "*":
                    masked[i] = "\0"
    for match in re.finditer(r"\\+\*", body):
        if (len(match.group()) - 1) % 2:
            masked[offset + match.end() - 1] = "\0"

    groups, group = [], []
    pos = 0
    for lineno, line in enumerate(lines, 1):
        length = len(line)
        text = "".join(masked[pos:pos + length])
        # 목록 기호와 수평선은 구분자가 아니다.
        if re.match(r"^ {0,3}(?:\*[ \t]*){3,}$", text.rstrip("\r\n")):
            text = text.replace("*", "\0")
        else:
            text = re.sub(r"^( {0,3})\*(?=[ \t])", r"\1\0", text)
        standalone = bool(re.match(r"^\s*(?:#{1,6}\s|>|[-+*]\s|\d+[.)]\s|\|)", line)) or "|" in line
        if not line.strip() or standalone:
            if group:
                groups.append(group)
                group = []
            if line.strip():
                groups.append([(lineno, text)])
        else:
            group.append((lineno, text))
        pos += length
    if group:
        groups.append(group)

    bad = set()
    for group in groups:
        text = "".join(line for _, line in group)
        line_at = []
        for lineno, line in group:
            line_at.extend([lineno] * len(line))
        runs = []
        for match in re.finditer(r"\*+", text):
            before = text[match.start() - 1] if match.start() else "\n"
            after = text[match.end()] if match.end() < len(text) else "\n"
            left = not is_whitespace(after) and (not is_punctuation(after) or is_whitespace(before) or is_punctuation(before))
            right = not is_whitespace(before) and (not is_punctuation(before) or is_whitespace(after) or is_punctuation(after))
            if left or right:
                runs.append({"length": len(match.group()), "open": left, "close": right,
                             "line": line_at[match.start()]})
        # CommonMark delimiter stack: first closer, nearest compatible opener;
        # delimiters between a matched pair cannot later cross that pair.
        active = []
        for run in runs:
            while run["close"] and run["length"]:
                opener_index = None
                for index in range(len(active) - 1, -1, -1):
                    opener = active[index]
                    odd_match = ((opener["close"] or run["open"])
                                 and (opener["length"] + run["length"]) % 3 == 0
                                 and (opener["length"] % 3 != 0 or run["length"] % 3 != 0))
                    if opener["open"] and not odd_match:
                        opener_index = index
                        break
                if opener_index is None:
                    break
                opener = active[opener_index]
                for removed in active[opener_index + 1:]:
                    bad.add(removed["line"])
                del active[opener_index + 1:]
                used = 2 if opener["length"] >= 2 and run["length"] >= 2 else 1
                opener["length"] -= used
                run["length"] -= used
                if not opener["length"]:
                    active.pop()
            if run["length"]:
                active.append(run)
        bad.update(run["line"] for run in active)
    return bad


def lint_file(path: pathlib.Path, rules):
    raw = path.read_text(encoding="utf-8")
    problems = []
    if rules & {"emphasis-flanking", "bold-cjk", "italic-cjk-star"}:
        lines = raw.splitlines()
        for lineno in sorted(emphasis_lines(raw)):
            problems.append((lineno, "ERROR", "emphasis-flanking: 짝 없는 * → <strong>/<em> 또는 \\* 사용",
                             lines[lineno - 1].strip()[:80]))
    if rules & {"italic-cjk-underscore", "tilde"}:
        body = strip_code(raw)
        for lineno, line in enumerate(body.splitlines(), 1):
            for key, label, rx in (
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
    parser.add_argument("files", nargs="*", help="검사할 파일. 없으면 content/posts·content/digest·content/gallery 전체")
    parser.add_argument("--rules", default=None,
                        help="검사할 규칙을 쉼표로 고른다: " + ", ".join(RULES))
    args = parser.parse_args()

    if args.rules:
        selected = [name.strip() for name in args.rules.split(",") if name.strip()]
        unknown = [name for name in selected if name not in RULES and name not in {"bold-cjk", "italic-cjk-star"}]
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
            + list((root / "content" / "gallery").glob("*.md"))
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
