"""Exercise the math layout checks against passing and failing rendered content."""

import unittest

from playwright.sync_api import sync_playwright

from verify_article_ui_checks import A10_JS, A11_JS, resized_sidenotes_ok, sidenote_presence_ok


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


if __name__ == '__main__':
    unittest.main()
