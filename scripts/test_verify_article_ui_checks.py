"""Exercise the math layout checks against passing and failing rendered content."""

import unittest

from playwright.sync_api import sync_playwright

from verify_article_ui_checks import (
    A10_JS, A11_JS, A15_JS, A16_JS, a11_checks, a12_checks, a13_checks, a14_checks, a15_checks,
    a16_checks, resized_sidenotes_ok, sidenote_presence_ok, strict_lightbox_checks, summarize_checks,
)


def lightbox_row(src="image.png"):
    big = {"y": 27.0, "w": 1200.0, "h": 800.0, "natural": [2400, 1600], "complete": True, "src": src}
    before = {"open": False, "rootOverflow": "", "activeInLightbox": False, "activeSrc": None}
    opened = {"open": True, "rootOverflow": "hidden", "big": big, "vw": 1440, "vh": 900,
              "box": {"w": 1317.6, "h": 831.0},
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

    def test_zero_target_checks_are_na(self):
        from verify_article_ui import path_checks

        names = ("min360-light", "narrow-light", "min390-light", "min414-light",
                 "wide-light", "mid-light", "wide-dark", "narrow-dark",
                 "phablet-light", "tablet-light", "tablet820-light")

        def config(width):
            return {"tocGap": 32, "tables": [], "sidenotes": [], "footnoteMarkers": 0,
                    "footnotesSection": None, "docScrollWidth": width,
                    "viewport": {"w": width}, "a9": {"codes": []}, "quotes": None,
                    "postImages": [], "diagrams": {"figs": []}}

        configs = {name: config(360 if name == "min360-light" else 1440) for name in names}
        report = {"path": "/digest/x/", "configs": configs, "resize": {}, "heightResize": [],
                  "lightbox": {}}
        summary, checks = path_checks(report)
        for key in ("A2", "A3", "A7", "A8", "A10", "A11", "A20"):
            self.assertEqual(len(checks[key]), 1, key)
            self.assertTrue(checks[key][0]["na"], key)
            self.assertTrue(checks[key][0]["ok"], key)
            self.assertEqual(summary[key]["checked"], 0, key)
            self.assertEqual(summary[key]["na"], 1, key)
            self.assertTrue(summary[key]["pass"], key)
        self.assertFalse(summarize_checks([])["pass"])

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

    def test_lightbox_no_slight_overflow(self):
        def row(width, whole=False):
            record = lightbox_row()
            record["opened"].update({"vw": 375, "vh": 812, "wideMode": not whole,
                                     "box": {"w": 352.5, "h": 789.5},
                                     "inView": whole, "inViewX": True,
                                     "overlayScrollableX": True})
            record["opened"]["big"] = dict(record["opened"]["big"], w=float(width), x=0.0,
                                           right=float(width))
            return record

        def verdict(record):
            entries = a14_checks("/posts/x/", {"narrow-light": {"applicable": True, "rows": [record]}})
            return entries[0]["ok"], entries[0]["detail"]

        # 375 화면에서 512px로 열면 바탕 안쪽 폭(352.5px)보다 조금 넓은 채 오른쪽이 잘린다.
        ok, detail = verdict(row(512))
        self.assertFalse(ok)
        self.assertIn("noSlightOverflow", detail)
        # 바탕 안쪽 폭의 1.5배 넘게 열고 가로로 밀 수 있으면 통과한다.
        ok, detail = verdict(row(1058))
        self.assertTrue(ok, detail)
        # 바탕 안쪽 폭 안에 통째로 들어오는 폭은 그대로 통과한다.
        ok, detail = verdict(row(352, whole=True))
        self.assertTrue(ok, detail)

    def test_a14_width_rule_uses_overlay_box(self):
        record = lightbox_row("wide-box.png")
        record["img"]["width"] = 720.0
        record["opened"]["big"] = dict(record["opened"]["big"], natural=[1600, 800],
                                       w=1317.6, h=658.8)
        entries = a14_checks("/digest/x/", {"wide-light": {"applicable": True, "rows": [record]}})
        self.assertTrue(entries[0]["ok"], entries[0]["detail"])

        # 예전 96vw 상수(1382.4px)로 연 폭은 바탕 안쪽 폭 규칙과 어긋난다.
        record["opened"]["big"] = dict(record["opened"]["big"], w=1382.4, h=691.2)
        entries = a14_checks("/digest/x/", {"wide-light": {"applicable": True, "rows": [record]}})
        self.assertFalse(entries[0]["ok"])
        self.assertIn("wide.expectedWidth", entries[0]["detail"])

    def test_strict_lightbox_checks(self):
        def strict_row(**overrides):
            overlay = {"clientW": 1404, "clientH": 885, "scrollW": 1404, "scrollH": 885,
                       "leftGap": 55.2, "rightGap": 55.2, "right": 1440}
            before = {"open": False, "scrollY": 1200.0, "bodyFirstX": 16.0}
            closed = {"open": False, "scrollY": 1200.0, "bodyFirstX": 16.0}
            opened = {"open": True, "vw": 1440, "vh": 900, "wideMode": False,
                      "scrollMode": False, "screenLeftGap": 55.2, "screenRightGap": 55.2,
                      "overlay": dict(overlay)}
            opened.update(overrides)
            return {"img": {"src": "x.png"}, "opened": opened, "before": before,
                    "afterEsc": dict(closed), "afterOutsideClick": dict(closed)}

        def verdict(row):
            entries = strict_lightbox_checks("/digest/x/", {"wide-light": {"applicable": True, "rows": [row]}})
            return (all(entry["ok"] for entry in entries),
                    " | ".join(entry["detail"] for entry in entries))

        ok, detail = verdict(strict_row())
        self.assertTrue(ok, detail)

        overflow = strict_row()
        overflow["opened"]["overlay"]["scrollW"] = 1448
        ok, detail = verdict(overflow)
        self.assertFalse(ok)
        self.assertIn("scrollW=1448 clientW=1404", detail)

        off_center = strict_row()
        off_center["opened"]["overlay"]["rightGap"] = 60.2
        ok, detail = verdict(off_center)
        self.assertFalse(ok)
        self.assertIn("gapDiff=5.0", detail)

        wide_tall = strict_row(wideMode=True)
        wide_tall["opened"]["overlay"].update({"scrollW": 2900, "scrollH": 900})
        ok, detail = verdict(wide_tall)
        self.assertFalse(ok)
        self.assertIn("wide", detail)

        wide_ok = strict_row(wideMode=True)
        wide_ok["opened"]["overlay"].update({"scrollW": 2900, "scrollH": 885})
        ok, detail = verdict(wide_ok)
        self.assertTrue(ok, detail)

        resized = strict_row()
        resized["afterResize"] = dict(strict_row()["opened"], vw=1024, overlay=dict(
            strict_row()["opened"]["overlay"], clientW=988, scrollW=1028))
        ok, detail = verdict(resized)
        self.assertFalse(ok)
        self.assertIn("afterResize", detail)

        error = {"img": {"src": "x.png"}, "error": "Timeout 15000ms exceeded"}
        ok, detail = verdict(error)
        self.assertFalse(ok)

        entries = strict_lightbox_checks("/digest/x/", {"wide-light": {"applicable": False,
                                                                       "reason": "확대할 그림이 없다"}})
        self.assertEqual(len(entries), 1)
        self.assertTrue(entries[0]["na"])

    def test_strict_lightbox_window_closed_and_thumb_checks(self):
        def strict_row(**overrides):
            overlay = {"clientW": 1404, "clientH": 885, "scrollW": 1404, "scrollH": 885,
                       "leftGap": 55.2, "rightGap": 55.2, "right": 1440}
            before = {"open": False, "scrollY": 1200.0, "bodyFirstX": 16.0}
            closed = {"open": False, "scrollY": 1200.0, "bodyFirstX": 16.0}
            opened = {"open": True, "vw": 1440, "vh": 900, "wideMode": False,
                      "scrollMode": False, "screenLeftGap": 55.2, "screenRightGap": 55.2,
                      "overlay": dict(overlay)}
            opened.update(overrides)
            return {"img": {"src": "x.png"}, "opened": opened, "before": before,
                    "afterEsc": dict(closed), "afterOutsideClick": dict(closed)}

        def verdict(row, page_thumb=None, thumb_eligible=False):
            data = {"applicable": True, "rows": [row]}
            if page_thumb is not None:
                data["pageThumb"] = page_thumb
            if thumb_eligible:
                data["thumbEligible"] = True
            entries = strict_lightbox_checks("/digest/x/", {"wide-light": data})
            return (all(entry["ok"] for entry in entries),
                    " | ".join(entry["detail"] for entry in entries))

        ok, detail = verdict(strict_row())
        self.assertTrue(ok, detail)

        window = strict_row()
        window["opened"]["screenRightGap"] = 67.2
        ok, detail = verdict(window)
        self.assertFalse(ok)
        self.assertIn("winDiff=12.0", detail)

        strip = strict_row()
        strip["opened"]["overlay"]["right"] = 1428
        ok, detail = verdict(strip)
        self.assertFalse(ok)
        self.assertIn("rightDiff=12", detail)

        moved = strict_row()
        moved["afterEsc"]["scrollY"] = 1210.0
        ok, detail = verdict(moved)
        self.assertFalse(ok)
        self.assertIn("[afterEsc]", detail)
        self.assertIn("diff=10.0", detail)

        shifted = strict_row()
        shifted["afterOutsideClick"]["bodyFirstX"] = 17.5
        ok, detail = verdict(shifted)
        self.assertFalse(ok)
        self.assertIn("[afterOutsideClick]", detail)
        self.assertIn("bodyFirstX=17.5", detail)

        page_thumb = {"normal": 6, "hover": 8, "active": 8}
        wide = strict_row(wideMode=True)
        wide["wideThumb"] = dict(page_thumb)
        ok, detail = verdict(wide, page_thumb=page_thumb, thumb_eligible=True)
        self.assertTrue(ok, detail)

        thin = strict_row(wideMode=True)
        thin["wideThumb"] = {"normal": 6, "hover": 6, "active": 8}
        ok, detail = verdict(thin, page_thumb=page_thumb, thumb_eligible=True)
        self.assertFalse(ok)
        self.assertIn("wideThumb", detail)

        missing = strict_row(wideMode=True)
        ok, detail = verdict(missing, page_thumb=page_thumb, thumb_eligible=True)
        self.assertFalse(ok)
        self.assertIn("썸 두께 측정값 없음", detail)

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

    def test_a15_counts_opening_quote_after_closing_paren(self):
        # 닫는 소괄호 뒤 여는 따옴표 + 한글 조사는 뒤집힌 닫는 따옴표다.
        self.page.set_content(
            '<div class="post-content"><p>‘J-커브(J-Curve)‘를 “가(나)“를 만났다</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 2)
        # 올바른 닫는 따옴표는 세지 않는다.
        self.page.set_content(
            '<div class="post-content"><p>‘J-커브(J-Curve)’를 “가(나)”를 만났다</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 0)

    def test_a15_counts_flipped_quote_after_inline_tag(self):
        # **강조**"의가 렌더된 “강조“의는 앞의 여는 따옴표가 아직 닫히지 않았다.
        self.page.set_content('<div class="post-content"><p>“강조“의 말</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 1)
        self.page.set_content('<div class="post-content"><p>‘강조‘의 말</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 1)
        # 닫는 인라인 태그 뒤에 뒤집힌 닫는 따옴표도 센다(태그는 글 추출에서 빠진다).
        self.page.set_content(
            '<div class="post-content"><p>“<strong>언제 효력이 발생하는가</strong>“의</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 1)
        # 앞선 여는 따옴표가 없으면 정당한 여는 따옴표다.
        self.page.set_content(
            '<div class="post-content"><p><strong>말했다</strong>“안녕”이라고</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 0)

    def test_a15_counts_flipped_quote_after_any_character_but_not_doubled_openers(self):
        # 짝 없는 여는 따옴표 뒤 여는 부호+한글은 앞 글자가 무엇이든 센다.
        self.page.set_content('<div class="post-content"><p>“지난주 매출이 얼마였지?“라고</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 1)
        # 곧은 따옴표를 겹쳐 쓴 자리는 둘째 부호가 여는 자리이므로 세지 않는다.
        self.page.set_content('<div class="post-content"><p>““나라면 이렇게””</p></div>')
        self.assertEqual(self.page.evaluate(A15_JS)["hitCount"], 0)

    def test_a11_overflowing_display_math_needs_hint(self):
        self.page.set_viewport_size({"width": 800, "height": 600})
        self.page.set_content("""<style>
          .post-content { width: 300px }
          .katex-display { width: 200px; overflow: hidden }
          .katex-display .katex { display: inline-block; width: 400px }
        </style><div class="post-content"><div class="katex-display"><span class="katex">x</span></div></div>""")
        measured = self.page.evaluate(A11_JS)
        self.assertGreater(measured["displays"][0]["over"], 1)
        config = {"min360-light": {"a11": {"bounds": [{"over": 0}],
                                           "displays": measured["displays"], "tables": []}}}
        entries = [e for e in a11_checks("/posts/x/", config) if "displayMath" in e["detail"]]
        self.assertFalse(entries[0]["ok"], "힌트 없는 넘침 블록 수식은 실패해야 한다")
        # 가로 스크롤과 넘침 그림자 힌트를 갖추면 통과한다.
        self.page.evaluate("""() => {
          const d = document.querySelector('.katex-display');
          d.style.overflowX = 'auto';
          d.style.backgroundImage = 'linear-gradient(to right, #fff, transparent)';
        }""")
        measured = self.page.evaluate(A11_JS)
        config["min360-light"]["a11"]["displays"] = measured["displays"]
        entries = [e for e in a11_checks("/posts/x/", config) if "displayMath" in e["detail"]]
        self.assertTrue(entries[0]["ok"])

    def test_settle_waits_only_for_visible_images_and_is_bounded(self):
        import time

        from verify_article_ui import settle

        self.page.set_viewport_size({"width": 375, "height": 400})
        self.page.set_content("""
          <div style="height: 1600px"></div>
          <p><img id="below" loading="lazy" alt=""
                  src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40'%3E%3Crect width='40' height='40'/%3E%3C/svg%3E"
                  style="width: 40px; height: 40px"></p>
          <div style="display: none"><img id="hidden" alt="hidden" src="data:image/gif;base64,R0lGODlhAQABAAAAACw="></div>
        """)
        # display:none 안의 이미지는 화면에 그려지지 않으므로 끝없이 기다리면 안 된다.
        self.page.evaluate("""() => {
          const img = document.getElementById('hidden');
          Object.defineProperty(img, 'complete', { get: () => false });
        }""")
        started = time.monotonic()
        settle(self.page, image_timeout_ms=3000)
        self.assertLess(time.monotonic() - started, 20)
        self.assertTrue(self.page.evaluate("document.getElementById('below').complete"))

        # 화면에 그려지는 이미지가 끝내 로드되지 않아도 한도 안에 돌아온다.
        page = self.browser.new_page(viewport={"width": 375, "height": 400})
        try:
            page.set_content('<p style="margin: 0"><img id="pending" alt="" '
                             'style="width: 40px; height: 40px"></p>')
            page.evaluate("""() => {
              const img = document.getElementById('pending');
              Object.defineProperty(img, 'complete', { get: () => false });
            }""")
            started = time.monotonic()
            settle(page, image_timeout_ms=300)
            self.assertLess(time.monotonic() - started, 10)
        finally:
            page.close()

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

    def test_six_col_table_must_fit_at_820_and_above(self):
        from verify_article_ui import path_checks

        names = ("min360-light", "narrow-light", "min390-light", "min414-light",
                 "wide-light", "mid-light", "wide-dark", "narrow-dark",
                 "phablet-light", "tablet-light", "tablet820-light")

        def make_configs(wide_max_content, wide_overflowing):
            out = {}
            for name in names:
                is_wide = name in ("tablet820-light", "mid-light", "wide-light")
                wrap = 712 if name == "tablet820-light" else (720 if is_wide else 323)
                max_content = wide_max_content if is_wide else 694
                overflowing = wide_overflowing if is_wide else True
                out[name] = {
                    "tocGap": 32,
                    "tables": [{
                        "i": 1, "cols": 6, "overflowing": overflowing,
                        "maxContentWidth": max_content, "wrapClient": wrap,
                        "tableRect": {"w": max(wrap, max_content) if overflowing else wrap, "h": 300},
                    }],
                    "sidenotes": [], "footnoteMarkers": 0, "footnotesSection": None,
                    "docScrollWidth": 1440, "viewport": {"w": 1440},
                    "a9": {"codes": []}, "quotes": None, "postImages": [], "diagrams": {"figs": []},
                }
            return out

        bad_summary, _ = path_checks({
            "path": "/digest/x/", "configs": make_configs(896, True), "resize": {}, "heightResize": [],
            "lightbox": {},
        })
        self.assertFalse(bad_summary["A7"]["pass"])

        good_summary, _ = path_checks({
            "path": "/digest/x/", "configs": make_configs(712, False), "resize": {}, "heightResize": [],
            "lightbox": {},
        })
        self.assertTrue(good_summary["A7"]["pass"])


if __name__ == '__main__':
    unittest.main()

class NewArticleChecksTest(unittest.TestCase):
    def test_a21_diagram_text_ratio(self):
        from verify_article_ui_checks import a21_checks
        good = {str(w): [100.0, 120.0] for w in (360, 375, 390, 414)}
        self.assertTrue(all(e['ok'] for e in a21_checks('/x/', good)))
        good['390'][0] = 101
        self.assertFalse(all(e['ok'] for e in a21_checks('/x/', good)))

    def test_a22_table_header(self):
        from verify_article_ui_checks import a22_checks
        row = {'kind': 'overflow', 'width': 375, 'topDiff': 0.5, 'edges': [0.5, -0.5],
               'afterScrollEdges': [0.5], 'afterScrollTop': 0, 'afterResizeEdges': [0.5],
               'afterResizeTop': 0, 'hiddenAfter': True,
               'inert': True, 'tabSafe': True}
        self.assertTrue(a22_checks('/x/', [row])[0]['ok'])
        row['afterScrollEdges'] = [2]
        self.assertFalse(a22_checks('/x/', [row])[0]['ok'])

    def test_a23_wrapped_table(self):
        from verify_article_ui_checks import a23_checks
        self.assertTrue(a23_checks('/x/', [{'lines': 5, 'overflowing': True, 'scroll': 900, 'client': 720}])[0]['ok'])
        self.assertFalse(a23_checks('/x/', [{'lines': 6, 'overflowing': True, 'scroll': 900, 'client': 720}])[0]['ok'])
        self.assertFalse(a23_checks('/x/', [{'lines': 2, 'overflowing': False, 'scroll': 800, 'client': 720}])[0]['ok'])

    def test_a24_image_reservation(self):
        from verify_article_ui_checks import a24_checks
        row = {'width': 600, 'height': 300, 'attrWidth': 1200, 'attrHeight': 600, 'anchorShift': 1, 'loaded': True, 'complete': False}
        self.assertTrue(a24_checks('/x/', [row])[0]['ok'])
        row['anchorShift'] = 3
        self.assertFalse(a24_checks('/x/', [row])[0]['ok'])
        row['anchorShift'] = 0
        row['height'] = 10
        self.assertFalse(a24_checks('/x/', [row])[0]['ok'])

class RevisedChecksTest(unittest.TestCase):
    def test_a5_independent_expected_overflow(self):
        from verify_article_ui_checks import a5_overflow_checks
        passing = {'index': 1, 'cols': 5, 'isOverflowing': True, 'natural': False,
                   'squeezed': False, 'longCell': True, 'maxContentWidth': 1200, 'wrapClient': 720}
        self.assertTrue(a5_overflow_checks('/x/', passing)[0]['ok'])
        failing = dict(passing, isOverflowing=False)
        self.assertFalse(a5_overflow_checks('/x/', failing)[0]['ok'])
        failing = dict(passing, longCell=False)
        self.assertFalse(a5_overflow_checks('/x/', failing)[0]['ok'])

    def test_a17_vertical_sticky_does_not_hide_body_horizontal_failure(self):
        from verify_article_ui_checks import a17_checks
        row = {'index': 1, 'cols': 3, 'overflowing': False, 'sticky': False,
               'wrapClient': 720, 'firstCellWidth': 100, 'fontSize': 18,
               'firstCellPosition': 'sticky', 'bodyCellPosition': 'static'}
        self.assertTrue(a17_checks('/x/', {'wide-light': {'sticky': [row]}})[0]['ok'])
        row['bodyCellPosition'] = 'sticky'
        self.assertFalse(a17_checks('/x/', {'wide-light': {'sticky': [row]}})[0]['ok'])

class RevisedBrowserChecksTest(unittest.TestCase):
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

    def test_a11_ignores_only_hidden_header_clone(self):
        self.page.set_content('''<style>.post-content{width:300px} table{width:200px;table-layout:fixed} th{padding:8px 16px}
          .katex{display:inline-block;width:30px}</style><div class="post-content">
          <table><thead><tr><th><span class="katex">x</span></th></tr></thead></table>
          <div class="table-header-clone" hidden><table><thead><tr><th>
          <span class="katex">x</span></th></tr></thead></table></div></div>''')
        self.assertEqual(len(self.page.evaluate(A11_JS)['bounds']), 1)
        self.page.locator('.table-header-clone').evaluate('e => e.hidden=false')
        self.page.locator('.table-header-clone .katex').evaluate("e => e.style.width='400px'")
        result = self.page.evaluate(A11_JS)['bounds']
        self.assertEqual(len(result), 2)
        self.assertGreater(result[1]['over'], 1)

    def test_a5_measures_long_cell_without_reading_overflow_class(self):
        from verify_article_ui import STATE_JS
        from verify_article_ui_checks import a5_overflow_checks
        self.page.set_content('''<style>.table-scroll{width:260px} table{width:100%;border-collapse:collapse;
          font:16px/24px sans-serif} td,th{padding:4px 8px;vertical-align:top}</style>
          <div class="post-content"><div class="table-scroll"><table><thead><tr><th>A</th><th>B</th><th>C</th></tr></thead>
          <tbody><tr><td>one</td><td>words words words words words words words words words words words words words words words words</td><td>end</td></tr></tbody></table></div></div>''')
        state = self.page.evaluate(STATE_JS)['tables'][0]
        self.assertTrue(state['longCell'])
        self.assertGreater(state['maxContentWidth'], state['wrapClient'])
        self.assertFalse(a5_overflow_checks('/x/', state)[0]['ok'])
        self.page.locator('.table-scroll').evaluate("e => e.classList.add('is-overflowing')")
        state = self.page.evaluate(STATE_JS)['tables'][0]
        self.assertTrue(a5_overflow_checks('/x/', state)[0]['ok'])

    def test_expanded_four_column_table_keeps_short_first_column_readable(self):
        from pathlib import Path
        css = Path('assets/css/30-post.css').read_text(encoding='utf-8')
        js = Path('assets/js/post.js').read_text(encoding='utf-8')
        self.page.set_viewport_size({'width': 375, 'height': 812})
        self.page.set_content('''<style>*, *::before, *::after{box-sizing:border-box}:root{--space-1:8px;--space-2:16px;--space-3:24px;
          --line:1px;--line-strong:2px;--bg:white;--rule:#ccc;--rule-strong:#333;--ink-2:#333;
          --topbar-height:64px} .post-content{width:335px;font-size:18px}</style>
          <div class="post-content"><table><thead><tr><th>모델</th><th>메모리</th><th>함수</th><th>갱신</th></tr></thead>
          <tbody><tr><td>SWLA</td><td>길고 긴 메모리 설명이 여러 줄로 자주 줄바꿈되도록 충분히 길게 반복합니다 길고 긴 메모리 설명이 여러 줄로 자주 줄바꿈되도록 반복합니다</td><td>목적 함수에 대한 설명</td><td>갱신 규칙을 설명합니다</td></tr>
          <tr><td>Titans (LMM)</td><td>심층 신경망</td><td>회귀 손실</td><td>가중치 감쇠</td></tr></tbody></table></div>''')
        self.page.add_style_tag(content=css)
        self.page.evaluate(js)
        wrapper = self.page.locator('.table-scroll')
        self.assertIn('is-expanded', wrapper.get_attribute('class'))
        width = wrapper.locator('tbody td').first.evaluate('e => e.getBoundingClientRect().width')
        self.assertLessEqual(width, 100)
