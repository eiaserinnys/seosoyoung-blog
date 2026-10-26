#!/usr/bin/env python3
"""Build the static backgrounds and fixed text-width measurements for OG cards."""

from __future__ import annotations

import math
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
OUT = ASSETS / "og"
DATA = ROOT / "data" / "og.yaml"
FONTS = ASSETS / "fonts"
INK = "#0F0F0F"
MUTED = "#5C5C5C"
ACCENT = "#0B7A4B"
WIDTH, HEIGHT = 1200, 630


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def draw_text(image: Image.Image, xy: tuple[int, int], text: str, font_name: str,
              size: int, fill: str, *, spacing: int = 0) -> None:
    draw = ImageDraw.Draw(image)
    selected_font = font(font_name, size)
    lines = text.split("\n")
    y = xy[1]
    for line in lines:
        draw.text((xy[0], y), line, font=selected_font, fill=fill, anchor="lt")
        y += size + spacing


def save_white(name: str, width: int, height: int = HEIGHT) -> Image.Image:
    image = Image.new("RGB", (width, height), "#FFFFFF")
    image.save(OUT / name, optimize=True)
    return image


def save_transparent(name: str, width: int, height: int = HEIGHT) -> Image.Image:
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    image.save(OUT / name, optimize=True)
    return image


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (ROOT / "data").mkdir(parents=True, exist_ok=True)

    post_cover = save_white("post-cover-base.png", 720)
    draw_text(post_cover, (72, 56), "서소영의 서재", "Pretendard-Bold.ttf", 24, INK)
    ImageDraw.Draw(post_cover).rectangle((72, 105, 647, 106), fill=INK)
    post_cover.save(OUT / "post-cover-base.png", optimize=True)

    post_wide = save_white("post-wide-base.png", WIDTH)
    draw_text(post_wide, (72, 56), "서소영의 서재", "Pretendard-Bold.ttf", 24, INK)
    ImageDraw.Draw(post_wide).rectangle((72, 105, 1127, 106), fill=INK)
    post_wide.save(OUT / "post-wide-base.png", optimize=True)

    save_transparent("post-cover-title.png", 668)
    save_transparent("post-wide-title.png", 1148)
    save_white("canvas.png", WIDTH)
    save_white("cover-tile.png", 480, HEIGHT)
    save_white("home-tile.png", 267, 206)

    home = save_white("home-base.png", 660)
    draw = ImageDraw.Draw(home)
    draw.rectangle((72, 56, 591, 57), fill=INK)
    draw_text(home, (72, 150), "서소영의\n서재", "Pretendard-ExtraBold.ttf", 84, INK, spacing=2)
    draw_text(home, (72, 352), "논문과 아티클을 읽고,\n소화하여, 지식으로 정리합니다.",
              "Pretendard-Regular.ttf", 26, MUTED, spacing=12)
    nav = ("쓴 글", "읽은 글", "실험실", "X")
    nav_font = font("Pretendard-SemiBold.ttf", 22)
    x = 72
    for label in nav:
        draw.text((x, 548), label, font=nav_font, fill=INK, anchor="lt")
        x += math.ceil(nav_font.getlength(label)) + 28
    home.save(OUT / "home-base.png", optimize=True)

    subject_text = (ROOT / "data" / "subjects.yaml").read_text(encoding="utf-8")
    categories = [line.removeprefix("- category: ").strip()
                  for line in subject_text.splitlines() if line.startswith("- category: ")]
    kind_font = font("Pretendard-SemiBold.ttf", 22)
    widths = {
        "kind": {
            "posts": math.ceil(kind_font.getlength("쓴 글")),
            "digest": math.ceil(kind_font.getlength("읽은 글")),
        },
        "category": {category: math.ceil(kind_font.getlength(category)) for category in categories},
    }
    payload = {"widths": widths}
    DATA.write_text(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"wrote {len(list(OUT.glob('*.png')))} PNG bases and {DATA.relative_to(ROOT)}")
    print(f"stored fixed text widths for {len(widths['category'])} categories")


if __name__ == "__main__":
    main()
