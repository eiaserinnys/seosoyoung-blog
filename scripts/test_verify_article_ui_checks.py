"""Exercise the math layout checks against passing and failing rendered content."""

import unittest

from playwright.sync_api import sync_playwright

from verify_article_ui_checks import (
    A10_JS, A11_JS, A15_JS, A16_JS, a12_checks, a13_checks, a14_checks, a15_checks, a16_checks,
    resized_sidenotes_ok, sidenote_presence_ok, summarize_checks,
)


def lightbox_row(src="image.png"):
    big = {"y": 27.0, "w": 1200.0, "h": 800.0, "natural": [2400, 1600], "complete": True, "src": src}
    before = {"open": False, "rootOverflow": "", "activeInLightbox": False, "activeSrc": None}
    opened = {"open": True, "rootOverflow": "hidden", "big": big, "vw": 1440, "vh": 900,
              "inView": True, "ratioErr": 0.001, "role": "dialog", "label": "이미지 확대",
              "activeInLightbox": True, "activeSrc": src}
    after_esc = {"open": False, "rootOverflow": "", "activeInLightbox": False, "activeSrc": src}
    return {"img": {"src": src, "role": "button", "tabIndex": 0, "haspopup": "dialog"},
            "before": before, "opened": opened, "afterTab": dict(opened),
            "afterEsc": after_esc, "afterOutsideClick": dict(after_esc)}


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


    def test_lightbox_verdicts(self):
        path = "/posts/x/"
        good = {"wide-light": {"applicable": True, "rows": [lightbox_row()]}}
        entries = a14_checks(path, good)
        self.assertEqual(len(entries), 1)
        self.assertTrue(entries[0]["ok"])
        self.assertFalse(entries[0].get("na", False))

        scroll = lightbox_row()
        scroll["opened"].update({"inView": False, "scrollMode": True,
                                 "inViewX": True, "overlayScrollable": True})
        entries = a14_checks(path, {"wide-light": {"applicable": True, "rows": [scroll]}})
        self.assertEqual(len(entries), 1)
        self.assertTrue(entries[0]["ok"])

        bad = lightbox_row()
        bad["afterEsc"]["activeSrc"] = "other.png"
        self.assertFalse(a14_checks(path, {"wide-light": {"applicable": True, "rows": [bad]}})[0]["ok"])

        error = {"img": {"src": "x.png"}, "error": "Timeout 15000ms exceeded"}
        self.assertFalse(a14_checks(path, {"wide-light": {"applicable": True, "rows": [error]}})[0]["ok"])

        entries = a14_checks(path, {"wide-light": {"applicable": False, "reason": "확대할 그림이 없다"}})
        self.assertEqual(len(entries), 1)
        self.assertTrue(entries[0]["ok"])
        self.assertTrue(entries[0]["na"])

    def test_straight_quote_detector(self):
        self.page.set_content(
            '<div class="post-content"><p>“봐 줘"라고 <code>"코드"는</code> “맞다”고</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 1)
        self.page.set_content('<div class="post-content"><p>“봐 줘”라고</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 0)

    def test_straight_quote_checks(self):
        path = "/posts/x/"
        passing = {"wide-light": {"quotes": {"blocks": 2, "hitCount": 0, "hits": []}}}
        self.assertTrue(a15_checks(path, passing)[0]["ok"])
        failing = {"wide-light": {"quotes": {"blocks": 2, "hitCount": 1, "hits": ['“a"b']}}}
        self.assertFalse(a15_checks(path, failing)[0]["ok"])
        self.assertTrue(a15_checks(path, {"wide-light": {}})[0]["na"])

    def test_diagram_audit_and_header_row_checks(self):
        self.page.set_viewport_size({"width": 800, "height": 600})
        self.page.set_content("""<style>
          .post-content { width: 720px; }
          figure.blog-diagram { margin: 0; }
          svg { display: block; width: 100%; height: auto; font-family: monospace; }
        </style><div class="post-content">
          <figure class="blog-diagram">
            <svg class="diagram-svg-desktop" viewBox="0 0 720 120">
              <rect width="720" height="120" fill="#eee"/>
              <text x="24" y="30" font-size="12">단위: 백만 토큰</text>
              <rect x="560" y="20" width="10" height="10" fill="#333"/>
              <text id="leg1" x="576" y="30" font-size="12">옛</text>
              <rect id="sw2" x="668" y="20" width="10" height="10" fill="#c30"/>
              <text id="leg2" x="696" y="30" text-anchor="end" font-size="12">새</text>
              <line x1="24" y1="42" x2="696" y2="42" stroke="#999"/>
              <rect x="24" y="56" width="200" height="44" fill="#fff" stroke="#333"/>
              <text x="36" y="82" font-size="12">상자 안 텍스트</text>
            </svg>
          </figure>
        </div>""")
        self.page.evaluate("""() => {
          const b2 = document.getElementById('leg2').getBBox();
          document.getElementById('sw2').setAttribute('x', String(+(b2.x - 16).toFixed(1)));
        }""")
        measured = self.page.evaluate(A16_JS)
        self.assertEqual(len(measured["figs"]), 1)
        fig = measured["figs"][0]
        self.assertEqual(fig["outside"], [])
        self.assertEqual(fig["ov"], [])
        self.assertEqual(fig["cross"], [])
        self.assertAlmostEqual(fig["headerRow"]["rightDiff"], 0.0, delta=1.5)

        good_cfg = {"wide-light": {"diagrams": measured}}
        self.assertTrue(all(e["ok"] for e in a16_checks("/digest/x/", good_cfg)))

        # Unaligned header right edge should fail A16
        bad_fig = dict(fig, headerRow=dict(fig["headerRow"], rightDiff=25.8))
        bad_cfg = {"wide-light": {"diagrams": {"figs": [bad_fig]}}}
        self.assertFalse(all(e["ok"] for e in a16_checks("/digest/x/", bad_cfg)))

        # Uneven legend item gaps across multiple charts should fail A16
        fig_a = dict(fig, fig=1, headerRow=dict(fig["headerRow"], swatchGaps=[6.0], itemGaps=[16.0]))
        fig_b = dict(fig, fig=2, headerRow=dict(fig["headerRow"], swatchGaps=[6.0], itemGaps=[32.0]))
        uneven_cfg = {"wide-light": {"diagrams": {"figs": [fig_a, fig_b]}}}
        self.assertFalse(all(e["ok"] for e in a16_checks("/digest/x/", uneven_cfg)))

        # Mobile SVG must not be scaled beyond 1.15x; 1.143x is the largest expected fitting scale
        mobile_too_big = dict(fig, cls="diagram-svg-mobile", scale=1.6)
        mobile_bad_cfg = {"wide-light": {"diagrams": {"figs": [mobile_too_big]}}}
        self.assertFalse(all(e["ok"] for e in a16_checks("/digest/x/", mobile_bad_cfg)))
        mobile_ok = dict(fig, cls="diagram-svg-mobile", scale=1.143)
        mobile_ok_cfg = {"wide-light": {"diagrams": {"figs": [mobile_ok]}}}
        self.assertTrue(all(e["ok"] for e in a16_checks("/digest/x/", mobile_ok_cfg)))

        # Pages without diagrams should return NA
        na_entries = a16_checks("/digest/none/", {"wide-light": {"diagrams": {"figs": []}}})
        self.assertTrue(na_entries[0]["na"])


if __name__ == '__main__':
    unittest.main()
