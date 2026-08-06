#!/usr/bin/env python3
"""Verify the rendered library sidebar contract without third-party packages."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


def class_names(attributes: dict[str, str]) -> set[str]:
    return set(attributes.get("class", "").split())


def url_path(value: str) -> str:
    path = unquote(urlparse(value).path)
    return path if path.endswith("/") else f"{path}/"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.navigation_count = 0
        self.disclosure_count = 0
        self.current_links: list[str] = []
        self.taxonomy_links: dict[str, list[tuple[str, str, int]]] = {
            "categories": [],
            "series": [],
        }
        self._active_taxonomy: str | None = None
        self._active_href = ""
        self._active_text: list[str] = []
        self._active_count: int | None = None

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = {key: value or "" for key, value in attrs}
        classes = class_names(attributes)

        if attributes.get("data-library-navigation") == "true":
            self.navigation_count += 1
        if tag == "details" and "library-tree-disclosure" in classes:
            self.disclosure_count += 1
        if tag == "a" and attributes.get("aria-current") == "page":
            self.current_links.append(url_path(attributes.get("href", "")))

        taxonomy = attributes.get("data-library-taxonomy")
        if tag == "a" and taxonomy in self.taxonomy_links:
            self._active_taxonomy = taxonomy
            self._active_href = url_path(attributes.get("href", ""))
            self._active_text = []
            self._active_count = None
        elif (
            tag == "span"
            and self._active_taxonomy
            and "library-tree-count" in classes
        ):
            count = attributes.get("data-count", "")
            if count.isdigit():
                self._active_count = int(count)

    def handle_data(self, data: str) -> None:
        if self._active_taxonomy:
            self._active_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or not self._active_taxonomy:
            return
        label = " ".join(" ".join(self._active_text).split())
        count = self._active_count
        if count is None:
            raise AssertionError(f"taxonomy count missing for {self._active_href}")
        self.taxonomy_links[self._active_taxonomy].append(
            (self._active_href, label.removesuffix(f" {count}"), count)
        )
        self._active_taxonomy = None


class TermsParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.entries: list[tuple[str, str, int]] = []
        self._terms_depth = 0
        self._active_href: str | None = None
        self._active_text: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = {key: value or "" for key, value in attrs}
        if tag == "ul" and "terms-tags" in class_names(attributes):
            self._terms_depth = 1
            return
        if self._terms_depth:
            if tag == "ul":
                self._terms_depth += 1
            if tag == "a":
                self._active_href = url_path(attributes.get("href", ""))
                self._active_text = []

    def handle_data(self, data: str) -> None:
        if self._active_href is not None:
            self._active_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._active_href is not None:
            text = " ".join(" ".join(self._active_text).split())
            match = re.search(r"\s(\d+)$", text)
            if not match:
                raise AssertionError(f"taxonomy root count missing for {self._active_href}")
            count = int(match.group(1))
            self.entries.append((self._active_href, text[: match.start()], count))
            self._active_href = None
        elif tag == "ul" and self._terms_depth:
            self._terms_depth -= 1


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def parse_terms(path: Path) -> list[tuple[str, str, int]]:
    parser = TermsParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.entries


def direct_term_pages(public: Path, taxonomy: str) -> list[Path]:
    root = public / taxonomy
    return sorted(
        path
        for path in root.glob("*/index.html")
        if path.parent.name != "page"
    )


def first_single(public: Path, section: str) -> Path:
    for path in sorted((public / section).glob("*/index.html")):
        html = path.read_text(encoding="utf-8")
        if "post-single" in html:
            return path
    raise AssertionError(f"no rendered single page found in {section}")


def assert_navigation(path: Path, current_path: str | None = None) -> PageParser:
    parsed = parse_page(path)
    assert parsed.navigation_count == 1, (
        f"{path}: expected one library navigation, got {parsed.navigation_count}"
    )
    assert parsed.disclosure_count == 1, (
        f"{path}: expected one responsive disclosure, got {parsed.disclosure_count}"
    )
    if current_path:
        assert parsed.current_links == [current_path], (
            f"{path}: expected current link {current_path}, got {parsed.current_links}"
        )
    return parsed


def assert_no_navigation(path: Path) -> None:
    parsed = parse_page(path)
    assert parsed.navigation_count == 0, f"{path}: library navigation leaked"
    assert not parsed.current_links, f"{path}: current library link leaked"


def main() -> int:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("public", type=Path)
    args = argument_parser.parse_args()
    public = args.public.resolve()

    digest = assert_navigation(public / "digest" / "index.html", "/digest/")
    assert_navigation(public / "digest" / "page" / "2" / "index.html", "/digest/")
    assert_navigation(public / "posts" / "index.html")
    assert_navigation(public / "posts" / "page" / "2" / "index.html")

    category_pages = direct_term_pages(public, "categories")
    series_pages = direct_term_pages(public, "series")
    tag_pages = direct_term_pages(public, "tags")
    assert category_pages, "no category term pages rendered"
    assert series_pages, "no series term pages rendered"
    assert tag_pages, "no tag term pages rendered"

    for term_page in category_pages:
        category_path = f"/categories/{term_page.parent.name}/"
        assert_navigation(term_page, category_path)
        second_page = term_page.parent / "page" / "2" / "index.html"
        if second_page.exists():
            assert_navigation(second_page, category_path)
    for term_page in series_pages:
        series_path = f"/series/{term_page.parent.name}/"
        assert_navigation(term_page, series_path)

    expected_categories = sorted(parse_terms(public / "categories" / "index.html"))
    expected_series = sorted(parse_terms(public / "series" / "index.html"))
    assert sorted(digest.taxonomy_links["categories"]) == expected_categories, (
        "category names, links, or counts differ from Hugo taxonomy output"
    )
    assert sorted(digest.taxonomy_links["series"]) == expected_series, (
        "series names, links, or counts differ from Hugo taxonomy output"
    )

    assert_no_navigation(first_single(public, "digest"))
    assert_no_navigation(first_single(public, "posts"))
    assert_no_navigation(tag_pages[0])
    assert_no_navigation(public / "categories" / "index.html")
    assert_no_navigation(public / "series" / "index.html")
    assert_no_navigation(public / "gallery" / "index.html")
    assert_no_navigation(public / "index.html")

    print(
        "library sidebar contract passed: "
        f"{len(expected_categories)} categories, {len(expected_series)} series"
    )
    print(
        "categories: "
        + ", ".join(f"{label} {count}" for _, label, count in expected_categories)
    )
    print(
        "series: "
        + ", ".join(f"{label} {count}" for _, label, count in expected_series)
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as error:
        print(f"library sidebar contract failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
