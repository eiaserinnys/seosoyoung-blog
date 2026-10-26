#!/usr/bin/env python3
"""Report article titles containing characters missing from their selected OG font."""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path

import yaml
from fontTools import unicodedata
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[2]
FONT_PATHS = {
    "sc": ROOT / "assets/fonts/NotoSansSC-Bold.ttf",
    "noto": ROOT / "assets/fonts/NotoSans-Bold.ttf",
    "jp": ROOT / "assets/fonts/PretendardJP-Bold.ttf",
}


def select_font(title: str) -> str:
    scripts = {unicodedata.script(char) for char in title}
    has_han = "Hani" in scripts
    has_hangul_or_kana = bool(scripts & {"Hang", "Hira", "Kana"})
    has_letterlike = any(0x2100 <= ord(char) <= 0x214F for char in title)
    if has_han and not has_hangul_or_kana:
        return "sc"
    if not has_han and not has_hangul_or_kana and has_letterlike:
        return "noto"
    return "jp"


def read_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f"YAML front matter not found: {path}")
    metadata = yaml.safe_load(parts[1]) or {}
    title = metadata.get("title")
    if not isinstance(title, str):
        raise ValueError(f"string title not found: {path}")
    return title


def unicode_cmap(path: Path) -> set[int]:
    font = TTFont(path, lazy=True)
    try:
        return {
            codepoint
            for table in font["cmap"].tables
            if table.isUnicode()
            for codepoint in table.cmap
        }
    finally:
        font.close()


def article_files(single_file: Path | None) -> list[Path]:
    if single_file is not None:
        return [single_file.resolve()]
    return sorted(
        path
        for section in (ROOT / "content/posts", ROOT / "content/digest")
        for path in section.rglob("*.md")
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "file",
        nargs="?",
        type=Path,
        help="check one Markdown file instead of all posts and digests",
    )
    args = parser.parse_args()

    cmaps = {key: unicode_cmap(path) for key, path in FONT_PATHS.items()}
    checked = 0
    selected = Counter()
    failures: list[str] = []
    for path in article_files(args.file):
        title = read_title(path)
        font_key = select_font(title)
        selected[font_key] += 1
        checked += 1
        missing = sorted({ord(char) for char in title if ord(char) not in cmaps[font_key]})
        if missing:
            label = FONT_PATHS[font_key].name
            points = ", ".join(f"U+{codepoint:04X} {chr(codepoint)!r}" for codepoint in missing)
            failures.append(f"{path.relative_to(ROOT)} [{label}]: {points}")

    if failures:
        print("\n".join(f"FAIL {failure}" for failure in failures))
        print(f"{len(failures)} of {checked} titles contain missing glyphs")
        return 1

    counts = ", ".join(f"{key}={selected[key]}" for key in ("sc", "noto", "jp"))
    print(f"PASS {checked} titles have complete cmap coverage ({counts})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
