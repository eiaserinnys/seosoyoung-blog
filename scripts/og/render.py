from pathlib import Path
from struct import unpack

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "scripts" / "og" / "home.html"
OUTPUT = ROOT / "static" / "og" / "home.png"


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
        page.goto(SOURCE.as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        page.screenshot(path=str(OUTPUT), animations="disabled")
        browser.close()

    image = OUTPUT.read_bytes()
    if image[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("OG output is not a PNG")
    dimensions = unpack(">II", image[16:24])
    if dimensions != (1200, 630):
        raise SystemExit(f"Unexpected OG dimensions: {dimensions}")

    size = OUTPUT.stat().st_size
    if size >= 300_000:
        raise SystemExit(f"OG image exceeds 300 KB: {size} bytes")
    print(f"{OUTPUT}: 1200x630, {size} bytes")


if __name__ == "__main__":
    main()
