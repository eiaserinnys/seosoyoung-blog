"""Exercise the math layout checks against passing and failing rendered content."""

import unittest

from playwright.sync_api import sync_playwright

from verify_article_ui_checks import (
    A10_JS, A11_JS, a12_checks, a13_checks, resized_sidenotes_ok, sidenote_presence_ok,
    summarize_checks,
)


class ArticleUiChecksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.page = self.browser.new_page()

    def tearDown(self):
        self.page.close()

    def test_hangul_and_math_overflow(self):
        self.page.set_content("""<style>
          p { width: 100px; margin: 0; font: 16px/24px monospace; word-break: keep-all }
          .lead { display: inline-block; width: 20px }
          .katex { display: inline-block; width: 80px }
          .math-nowrap { white-space: nowrap }
          .math-nowrap .katex { white-space: normal }
        </style><div class="post-content"><p><span class="lead"></span><span><span class="katex">x</span></span>가</p></div>""")
        before = self.page.evaluate(A10_JS)
        self.assertEqual(before["hangulChecked"], 1)
        self.assertEqual(before["hangulViolations"], 1)

        self.page.evaluate("""() => {
          const p = document.querySelector('p');
          const unit = p.querySelector('.katex').parentElement;
          const wrap = document.createElement('span');
          wrap.className = 'math-nowrap';
          p.insertBefore(wrap, unit);
          wrap.append(unit, unit.nextSibling);
        }""")
        after = self.page.evaluate(A10_JS)
        self.assertEqual(after["hangulChecked"], 1)
        self.assertEqual(after["hangulViolations"], 0)

        self.page.locator('.katex').evaluate("el => el.style.width = '140px'")
        self.assertGreater(self.page.evaluate(A11_JS)["bounds"][0]["over"], 1)
        self.page.locator('.katex').evaluate("el => el.style.width = '80px'")
        self.assertLessEqual(self.page.evaluate(A11_JS)["bounds"][0]["over"], 1)

    def test_sidenote_counts_allow_articles_without_footnotes(self):
        without = {"footnoteMarkers": 0, "sidenotes": []}
        missing = {"footnoteMarkers": 1, "sidenotes": []}
        final = {"sidenoteCount": 0, "numberedSidenotes": 0}
        self.assertTrue(sidenote_presence_ok(without))
        self.assertFalse(sidenote_presence_ok(missing))
        self.assertTrue(resized_sidenotes_ok(final, without))
        self.assertFalse(resized_sidenotes_ok(final, {"sidenotes": [1]}))

    def test_sidenote_math_bounds_and_adjacent_text(self):
        self.page.set_content("""<style>
          aside { width: 100px; font: 16px/24px monospace }
          .lead { display: inline-block; width: 20px }
          .katex { display: inline-block; width: 80px }
          .math-nowrap { white-space: nowrap }
        </style><div class="post-content"></div><aside class="sidenote"><p><span class="lead"></span><span><span class="katex">x</span></span>Cf의</p></aside>""")
        self.assertEqual(self.page.evaluate(A10_JS)["checked"], 0)
        before = self.page.evaluate(A10_JS, True)
        self.assertEqual(before["checked"], 1)
        self.assertEqual(before["violations"], 1)
        self.page.evaluate("""() => {
          const p = document.querySelector('aside p');
          const unit = p.querySelector('.katex').parentElement;
          const wrap = document.createElement('span');
          wrap.className = 'math-nowrap';
          p.insertBefore(wrap, unit);
          wrap.append(unit, unit.nextSibling);
        }""")
        self.assertEqual(self.page.evaluate(A10_JS, True)["violations"], 0)
        self.page.locator('.katex').evaluate("el => el.style.width = '140px'")
        self.assertGreater(self.page.evaluate(A11_JS, True)["bounds"][0]["over"], 1)
        self.page.locator('.katex').evaluate("el => el.style.width = '60px'")
        self.assertLessEqual(self.page.evaluate(A11_JS, True)["bounds"][0]["over"], 1)
        self.page.locator('aside p').evaluate("el => el.innerHTML = '<span><span class=\"katex\">x</span></span> Cf'")
        self.assertEqual(self.page.evaluate(A10_JS, True)["checked"], 0)

    def test_post_image_hairline(self):
        base = {"ruleColor": "rgb(228, 228, 225)"}
        with_line = dict(base, postImages=[{"src": "image06.png",
                                            "boxShadow": "rgb(228, 228, 225) 0px 0px 0px 1px"}])
        without_line = dict(base, postImages=[{"src": "image06.png", "boxShadow": "none"}])
        self.assertTrue(all(entry["ok"] for entry in a12_checks("/digest/x/", {"wide-light": with_line})))
        self.assertFalse(any(entry["ok"] for entry in a12_checks("/digest/x/", {"wide-light": without_line})))

    def test_post_image_checks_na_without_images(self):
        configs = {"wide-light": {"ruleColor": "rgb(228, 228, 225)", "postImages": []}}
        for check in (a12_checks, a13_checks):
            entries = check("/digest/x/", configs)
            self.assertEqual(len(entries), 1)
            self.assertTrue(entries[0]["ok"])
            self.assertTrue(entries[0]["na"])
            summary = summarize_checks(entries)
            self.assertEqual(summary["checked"], 0)
            self.assertEqual(summary["na"], 1)
            self.assertEqual(summary["failed"], 0)
            self.assertTrue(summary["pass"])

    def test_post_image_gap_and_row_widths(self):
        rule = "rgb(228, 228, 225)"
        shadow = f"{rule} 0px 0px 0px 1px"
        outline = {"width": 2.0, "style": "solid", "color": "rgb(201, 122, 78)", "offset": -2.0}

        def image(src, **extra):
            record = {"src": src, "w": 100.0, "h": 100.0, "boxShadow": shadow,
                      "borderWidths": [0.0, 0.0, 0.0, 0.0],
                      "borderColors": ["rgb(0, 0, 0)"] * 4,
                      "outline": {"width": 0.0, "style": "none",
                                  "color": "rgb(0, 0, 0)", "offset": 0.0},
                      "rowKey": None}
            record.update(extra)
            return record

        fixed = [
            image("v2-rays-from-gaze.png", rowKey=0, outline=outline),
            image("v1-diagonal-reach.png", rowKey=0),
        ]
        fixed_configs = {"wide-light": {"ruleColor": rule, "postImages": fixed}}
        self.assertTrue(all(entry["ok"] for entry in a13_checks("/gallery/x/", fixed_configs)))

        broken = [
            image("v2-rays-from-gaze.png", rowKey=0, outline=outline),
            image("v1-diagonal-reach.png", rowKey=0,
                  borderWidths=[2.0, 2.0, 2.0, 2.0],
                  borderColors=["rgba(0, 0, 0, 0)"] * 4),
        ]
        broken_configs = {"wide-light": {"ruleColor": rule, "postImages": broken}}
        self.assertTrue(any(not entry["ok"] for entry in a13_checks("/gallery/x/", broken_configs)))


if __name__ == '__main__':
    unittest.main()
