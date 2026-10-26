#!/usr/bin/env python3
"""Check generated Open Graph metadata and the images used by key page types."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import argparse
import re
import sys


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = {}

    def handle_starttag(self, tag, attrs):
        if tag != "meta":
            return
        values = dict(attrs)
        key = values.get("property") or values.get("name")
        if key:
            self.values[key] = values.get("content", "")


def read_meta(page):
    parser = MetaParser()
    parser.feed(page.read_text(encoding="utf-8"))
    return parser.values


def jpeg_size(path):
    data = path.read_bytes()
    if data[:2] != b"\xff\xd8":
        raise AssertionError(f"not a JPEG: {path}")
    offset = 2
    while offset < len(data):
        if data[offset] != 0xFF:
            offset += 1
            continue
        marker = data[offset + 1]
        offset += 2
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            continue
        size = int.from_bytes(data[offset : offset + 2], "big")
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            height = int.from_bytes(data[offset + 3 : offset + 5], "big")
            width = int.from_bytes(data[offset + 5 : offset + 7], "big")
            return width, height
        offset += size
    raise AssertionError(f"JPEG dimensions not found: {path}")


def image_file(public, image_url):
    path = unquote(urlparse(image_url).path).lstrip("/")
    candidate = (public / path).resolve()
    candidate.relative_to(public.resolve())
    return candidate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("public", type=Path)
    args = parser.parse_args()
    public = args.public.resolve()

    pages = {
        "home": ("index.html", "home"),
        "digest index": ("digest/index.html", "home"),
        "topic": ("categories/모델과-연구/index.html", "home"),
        "new digest without per-article data": ("digest/jascha-anthropocene-advice/index.html", "article"),
        "post with cover": ("posts/can-everyone-make-with-ai/index.html", "article"),
        "digest with cover A": ("digest/moss-image-technical-report/index.html", "article"),
        "digest with cover B": ("digest/local-llm-12gb-vram-deepseek-qwen38-27b/index.html", "article"),
        "post without cover": ("digest/cactus-needle-26m/index.html", "article"),
        "gallery": ("gallery/seosoyoung-mspaint-doodle/index.html", "gallery"),
    }

    observed = {}
    failures = []
    for name, (relative, kind) in pages.items():
        page = public / relative
        if not page.is_file():
            failures.append(f"{name}: page not found: {page}")
            continue
        meta = read_meta(page)
        image = meta.get("og:image", "")
        if not image:
            failures.append(f"{name}: og:image is missing")
            continue
        observed[name] = (meta, image, kind)
        if not meta.get("og:image:alt"):
            failures.append(f"{name}: og:image:alt is missing")
        if meta.get("twitter:image") != image:
            failures.append(f"{name}: Twitter and Open Graph images differ")
        if meta.get("twitter:card") != "summary_large_image":
            failures.append(f"{name}: twitter:card is not summary_large_image")

        if kind in ("home", "article"):
            if meta.get("og:image:width") != "1200" or meta.get("og:image:height") != "630":
                failures.append(f"{name}: expected 1200x630 metadata")
            if not urlparse(image).path.startswith("/og/"):
                failures.append(f"{name}: expected a generated /og/ image")
            try:
                path = image_file(public, image)
                if not path.is_file():
                    failures.append(f"{name}: generated image is missing: {path}")
                elif jpeg_size(path) != (1200, 630):
                    failures.append(f"{name}: generated JPEG dimensions are {jpeg_size(path)}")
            except (AssertionError, ValueError) as error:
                failures.append(f"{name}: {error}")
        elif kind == "gallery":
            if urlparse(image).path.startswith("/og/"):
                failures.append("gallery: source image was replaced by a generated OG image")
            source = Path(__file__).resolve().parents[2] / "content/gallery/seosoyoung-mspaint-doodle.md"
            cover = re.search(r'(?m)^  image:\s*"([^"]+)"$', source.read_text(encoding="utf-8"))
            if not cover or image != cover.group(1):
                failures.append("gallery: og:image no longer matches cover.image")

    if "home" in observed:
        home_image = observed["home"][1]
        for name in ("digest index", "topic"):
            if name in observed and observed[name][1] != home_image:
                failures.append(f"{name}: expected the homepage OG image")

    og_data = (Path(__file__).resolve().parents[2] / "data/og.yaml").read_text(encoding="utf-8")
    if "titleLines:" in og_data or "jascha-anthropocene-advice:" in og_data:
        failures.append("per-article title data should not be required")

    article_images = [
        observed[name][1]
        for name in ("post with cover", "digest with cover A", "digest with cover B", "post without cover")
        if name in observed
    ]
    if len(article_images) != len(set(article_images)):
        failures.append("article pages should each have their own generated OG image")

    if failures:
        print("\n".join(f"FAIL {failure}" for failure in failures), file=sys.stderr)
        return 1
    print(f"PASS Open Graph output: {len(observed)} page types, 1200x630 generated JPEGs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
