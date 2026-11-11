"""A9/A10/A11 measurements for verify_article_ui.py (card #1177).

A9: table inline code mid-word breaks, measured per character with Range rects.
A10: inline math punctuation orphan, measured with Range rect tops.
A11: math bounds and wide table overflow.

Both measurements run identically on the 9b8f1de build and the new build.
A10 does not depend on `.math-nowrap`; it reads the rendered math box that
KaTeX auto-render leaves in place.
"""
import re

A9_JS = r"""
() => {
  const wrappers = [...document.querySelectorAll('.post-content .table-scroll')];
  const codes = [...document.querySelectorAll('.post-content table :not(pre) > code')].map((c, i) => {
    const wrap = c.closest('.table-scroll');
    const cs = getComputedStyle(c);
    const cell = c.closest('td,th');
    const breaks = [];
    let lastTop = null;
    let prevChar = '';
    let skippedSpace = false;
    const walker = document.createTreeWalker(c, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      for (let k = 0; k < node.data.length; k++) {
        const ch = node.data[k];
        const range = document.createRange();
        range.setStart(node, k);
        range.setEnd(node, k + 1);
        const rects = range.getClientRects();
        if (!rects.length) continue;
        const top = Math.round(rects[0].top);
        if (!ch.trim()) {
          if (lastTop !== null) skippedSpace = true;
          continue;
        }
        if (lastTop !== null && top > lastTop + 4) {
          breaks.push({
            prev: prevChar,
            ch: ch,
            skippedSpace: skippedSpace,
            midWord: /[A-Za-z0-9_]/.test(prevChar) && /[A-Za-z0-9_]/.test(ch) && !skippedSpace,
          });
        }
        lastTop = top;
        prevChar = ch;
        skippedSpace = false;
      }
    }
    return {
      i: i,
      table: wrap ? wrappers.indexOf(wrap) + 1 : null,
      overflowing: wrap ? wrap.classList.contains('is-overflowing') : null,
      text: c.textContent.slice(0, 120),
      lines: c.getClientRects().length,
      overflowWrap: cs.overflowWrap,
      wordBreak: cs.wordBreak,
      cellWhiteSpace: cell ? getComputedStyle(cell).whiteSpace : null,
      breaks: breaks,
      midWord: breaks.filter((b) => b.midWord).length,
    };
  });
  return {codes: codes};
}
"""

A10_JS = r"""
(includeSide = false) => {
  const content = document.querySelector('.post-content');
  if (!content) return {math: [], checked: 0, violations: 0};
  const topOfChar = (node, offset) => {
    const range = document.createRange();
    range.setStart(node, offset);
    range.setEnd(node, offset + 1);
    const rects = range.getClientRects();
    return rects.length ? +rects[0].top.toFixed(1) : null;
  };
  const mathEls = [...content.querySelectorAll('.katex'),
    ...(includeSide ? document.querySelectorAll('aside.sidenote .katex') : [])]
    .filter((m) => !m.closest('.katex-display'));
  const out = mathEls.map((m, i) => {
    const parent = m.parentElement;
    // auto-render puts the returned .katex inside an anonymous span; that span
    // is the inline box whose siblings are the surrounding text nodes.
    const mathNode = (parent && parent.childElementCount === 1
      && parent.textContent.trim() === m.textContent.trim()) ? parent : m;
    const prev = mathNode.previousSibling;
    const next = mathNode.nextSibling;
    // Punctuation can have been split into a text node inside math-nowrap,
    // with the following Korean text still outside it in the earlier build.
    const following = [];
    let sibling = next;
    while (sibling && sibling.nodeType === Node.TEXT_NODE) {
      following.push(sibling);
      sibling = sibling.nextSibling;
    }
    const wrapper = mathNode.parentElement;
    if (!sibling && wrapper && wrapper.classList.contains('math-nowrap')) {
      sibling = wrapper.nextSibling;
      while (sibling && sibling.nodeType === Node.TEXT_NODE) {
        following.push(sibling);
        sibling = sibling.nextSibling;
      }
    }
    let hangulTop = null;
    let hangulChar = null;
    let seekingHangul = true;
    for (const node of following) {
      for (let offset = 0; offset < node.data.length && seekingHangul; offset++) {
        const ch = node.data[offset];
        if (/[)\]},.:;!?%]/.test(ch)) continue;
        if (/[ㄱ-ㆎ가-힣]/.test(ch)) {
          hangulChar = ch;
          hangulTop = topOfChar(node, offset);
        }
        seekingHangul = false;
      }
      if (!seekingHangul) break;
    }
    let prevChar = null;
    let prevTop = null;
    if (prev && prev.nodeType === 3) {
      const trimmed = prev.data.replace(/\s+$/, '');
      if (trimmed) {
        prevChar = trimmed[trimmed.length - 1];
        prevTop = topOfChar(prev, trimmed.length - 1);
      }
    }
    let nextChar = null;
    let nextTop = null;
    let nextAdjacent = false;
    if (next && next.nodeType === 3) {
      const lead = next.data.match(/^\s*/)[0].length;
      if (lead < next.data.length) {
        nextChar = next.data[lead];
        nextTop = topOfChar(next, lead);
        nextAdjacent = lead === 0;
      }
    }
    const rects = mathNode.getClientRects();
    const startTop = rects.length ? +rects[0].top.toFixed(1) : null;
    const endTop = rects.length ? +rects[rects.length - 1].top.toFixed(1) : null;
    const open = !!prevChar && /[(\[{]/.test(prevChar);
    const close = !!nextChar && (/[)\]},.:;!?%]/.test(nextChar)
      || (nextAdjacent && /[A-Za-z]/.test(nextChar)));
    const openViolation = !!(open && prevTop !== null && startTop !== null
      && Math.abs(prevTop - startTop) > 1);
    const closeViolation = !!(close && nextTop !== null && endTop !== null
      && Math.abs(nextTop - endTop) > 1);
    const hangulViolation = !!(hangulChar && hangulTop !== null && endTop !== null
      && Math.abs(hangulTop - endTop) > 1);
    const cell = m.closest('td,th');
    return {
      i: i,
      side: !!m.closest('aside.sidenote'),
      cell: cell ? cell.textContent.slice(0, 60) : null,
      prevChar: prevChar,
      nextChar: nextChar,
      prevTop: prevTop,
      nextTop: nextTop,
      startTop: startTop,
      endTop: endTop,
      open: open,
      close: close,
      openViolation: openViolation,
      closeViolation: closeViolation,
      hangulChar: hangulChar,
      hangulTop: hangulTop,
      hangulViolation: hangulViolation,
      mathNodeTag: mathNode.tagName,
      mathNodeClass: String(mathNode.className || ''),
      mathNodeSiblings: [prev ? prev.nodeName : null, next ? next.nodeName : null],
    };
  });
  return {
    math: out,
    checked: out.filter((m) => m.open || m.close || m.hangulChar).length,
    hangulChecked: out.filter((m) => m.hangulChar).length,
    hangulViolations: out.filter((m) => m.hangulViolation).length,
    violations: out.filter((m) => m.openViolation || m.closeViolation || m.hangulViolation).length,
  };
}
"""

A11_JS = r"""
(includeSide = false) => {
  const content = document.querySelector('.post-content');
  const blockSelector = 'p,li,td,th,blockquote,h1,h2,h3,h4,h5,h6,figcaption,dd,dt';
  const maths = [...content.querySelectorAll('.katex'),
    ...(includeSide ? document.querySelectorAll('aside.sidenote .katex') : [])]
    .filter((k) => !k.closest('.katex-display'));
  const bounds = maths.map((k, i) => {
    let unit = k;
    const parent = k.parentElement;
    if (parent && parent.tagName === 'SPAN' && !parent.className && parent.childNodes.length === 1) unit = parent;
    const outer = unit.parentElement && unit.parentElement.classList.contains('math-nowrap') ? unit.parentElement : unit;
    const side = k.closest('aside.sidenote');
    const block = side || outer.parentElement.closest(blockSelector) || content;
    const style = getComputedStyle(block);
    const right = block.getBoundingClientRect().right - parseFloat(style.paddingRight) - parseFloat(style.borderRightWidth);
    return {i, side: !!side, over: +(outer.getBoundingClientRect().right - right).toFixed(2),
      tex: (k.querySelector('annotation') || {}).textContent || '', block: block.tagName};
  });
  const tables = [...content.querySelectorAll('.table-scroll')].map((wrap, i) => {
    const table = wrap.querySelector('table');
    return {i: i + 1, hasMath: !!table.querySelector('.katex'), overflowing: wrap.classList.contains('is-overflowing')};
  }).filter((table) => table.hasMath);
  const displays = [...content.querySelectorAll('.katex-display')].map((k, i) => ({
    i: i + 1,
    clientW: k.clientWidth,
    scrollW: k.scrollWidth,
    over: +(k.scrollWidth - k.clientWidth).toFixed(2),
    tex: (k.querySelector('annotation') || {}).textContent || '',
  }));
  return {bounds, tables, displays};
}
"""

A15_JS = r"""
() => {
  const content = document.querySelector('.post-content');
  if (!content) return {blocks: 0, hitCount: 0, hits: []};
  const skipSelector = 'pre, code, kbd, samp, script, style, .katex, .katex-display, math';
  const blockSelector = 'p, li, td, th, h1, h2, h3, h4, h5, h6, figcaption, dt, dd';
  const blocks = new Map();
  const order = [];
  const walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT);
  let node;
  while ((node = walker.nextNode())) {
    const parent = node.parentElement;
    if (!parent || parent.closest(skipSelector)) continue;
    const block = parent.closest(blockSelector) || content;
    if (!blocks.has(block)) { blocks.set(block, []); order.push(block); }
    blocks.get(block).push(node.data);
  }
  let hitCount = 0;
  const hits = [];
  for (const block of order) {
    const text = blocks.get(block).join('');
    let open = false;
    for (let i = 0; i < text.length; i++) {
      const ch = text[i];
      if (ch === '“') { open = true; continue; }
      if (ch === '”') { open = false; continue; }
      if (ch !== '"') continue;
      const prev = text[i - 1] || '';
      const next = text[i + 1] || '';
      if (open || /[가-힣]/.test(prev) || /[가-힣]/.test(next)) {
        hitCount++;
        if (hits.length < 20) hits.push(text.slice(Math.max(0, i - 20), i + 21));
      }
    }
  }
  return {blocks: order.length, hitCount, hits};
}
"""

A9_WIDE_CONFIGS = ("mid-light", "wide-light")
A9_NARROW_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light")
A10_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light", "wide-light")
A11_NARROW_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light")
A12_CONFIGS = ("wide-light", "wide-dark", "narrow-light", "narrow-dark")
A13_CONFIGS = A12_CONFIGS
ROW_WIDTH_TOL = 0.5


def sidenote_presence_ok(wide):
    return not wide["footnoteMarkers"] or bool(wide["sidenotes"])


def resized_sidenotes_ok(final, wide):
    return (final["sidenoteCount"] == len(wide["sidenotes"])
            and final["numberedSidenotes"] == final["sidenoteCount"])


def _midword_breaks(code):
    return [
        {"prev": b.get("prev"), "ch": b.get("ch"), "skippedSpace": b.get("skippedSpace")}
        for b in code.get("breaks", [])
        if b.get("midWord")
    ]


def _a9_detail(path, name, codes):
    bad = [c for c in codes if c.get("midWord")]
    sample = "; ".join(
        f"table {c.get('table')} {c.get('text')!r} breaks={_midword_breaks(c)}"
        for c in bad[:5]
    )
    return (
        f"{path} {name}: code={len(codes)} midWord={len(bad)} "
        f"overflowing={sum(1 for c in codes if c.get('overflowing'))}"
        + (f" / {sample}" if sample else "")
    )


def a9_checks(path, configs):
    entries = []
    for name in A9_WIDE_CONFIGS:
        codes = ((configs.get(name) or {}).get("a9") or {}).get("codes") or []
        entries.append({
            "ok": not any(c.get("midWord") for c in codes),
            "detail": _a9_detail(path, name, codes),
        })
    for name in A9_NARROW_CONFIGS:
        codes = [
            c
            for c in (((configs.get(name) or {}).get("a9") or {}).get("codes") or [])
            if c.get("overflowing")
        ]
        entries.append({
            "ok": not any(c.get("midWord") for c in codes),
            "detail": _a9_detail(path, name, codes),
        })
    return entries


def a10_checks(path, configs):
    if not any((config or {}).get("a10") for config in configs.values()):
        return []
    entries = []
    for name in A10_CONFIGS:
        data = (configs.get(name) or {}).get("a10") or {}
        math = data.get("math") or []
        checked = data.get("checked", 0)
        violations = data.get("violations", 0)
        bad = [m for m in math if m.get("openViolation") or m.get("closeViolation") or m.get("hangulViolation")]
        sample = "; ".join(
            f"{m.get('cell') or '(본문)'} prev={m.get('prevChar')!r}@{m.get('prevTop')} "
            f"math={m.get('startTop')}..{m.get('endTop')} next={m.get('nextChar')!r}@{m.get('nextTop')} "
            f"hangul={m.get('hangulChar')!r}@{m.get('hangulTop')} "
            f"open={m.get('openViolation')} close={m.get('closeViolation')} hangulDrop={m.get('hangulViolation')}"
            for m in bad[:4]
        )
        entries.append({
            "ok": checked > 0 and violations == 0,
            "detail": f"{path} {name}: checked={checked} violations={violations} "
                      f"hangul={data.get('hangulChecked', 0)} hangulDrop={data.get('hangulViolations', 0)}"
                      + (f" / {sample}" if sample else ""),
        })
    return entries


def a11_checks(path, configs):
    if not any((config or {}).get("a11") for config in configs.values()):
        return []
    entries = []
    for name in A11_NARROW_CONFIGS:
        data = (configs.get(name) or {}).get("a11") or {}
        bounds = data.get("bounds") or []
        bad = [item for item in bounds if item["over"] > 1]
        entries.append({"ok": bool(bounds) and not bad,
                        "detail": f"{path} {name}: math={len(bounds)} over={len(bad)} "
                                  f"examples={bad[:4]}"})
        displays = data.get("displays") or []
        if displays:
            bad_disp = [item for item in displays if item["over"] > 1]
            entries.append({"ok": not bad_disp,
                            "detail": f"{path} {name}: displayMath={len(displays)} over={len(bad_disp)} "
                                      f"examples={bad_disp[:4]}"})
    wide = ((configs.get("wide-light") or {}).get("a11") or {})
    side_bounds = [item for item in wide.get("bounds", []) if item.get("side")]
    if side_bounds:
        bad = [item for item in side_bounds if item["over"] > 1]
        entries.append({"ok": not bad, "detail": f"{path} wide-light: side math={len(side_bounds)} "
                                                 f"over={len(bad)} examples={bad[:4]}"})
    tables = wide.get("tables") or []
    for table in tables:
        entries.append({"ok": not table["overflowing"],
                        "detail": f"{path} wide-light: math table {table['i']} overflowing={table['overflowing']}"})
    return entries


def _post_images(config):
    return (config or {}).get("postImages") or []


def _path_has_images(configs):
    return any(_post_images(config) for config in configs.values())


def _alpha(color):
    value = (color or "").strip().lower()
    if value == "transparent":
        return 0.0
    match = re.match(r"rgba?\(([^)]+)\)", value)
    if not match:
        return 1.0
    parts = [part for part in re.split(r"[,/ ]+", match.group(1).strip()) if part]
    return float(parts[3]) if len(parts) > 3 else 1.0


def _visible_width(image):
    widths = image.get("borderWidths") or [0, 0, 0, 0]
    return float(image.get("w") or 0) - float(widths[3]) - float(widths[1])


def a12_checks(path, configs):
    if not _path_has_images(configs):
        return [{"ok": True, "na": True, "detail": f"{path}: 본문 이미지 0건 (A12 해당 없음)"}]
    entries = []
    for name in A12_CONFIGS:
        config = configs.get(name) or {}
        rule = config.get("ruleColor") or ""
        for image in _post_images(config):
            shadow = image.get("boxShadow") or ""
            ok = bool(rule) and rule in shadow and "0px 0px 0px 1px" in shadow
            entries.append({
                "ok": ok,
                "detail": f"{path} {name} {image.get('src')}: boxShadow={shadow!r} rule={rule!r}",
            })
    return entries


def a13_checks(path, configs):
    if not _path_has_images(configs):
        return [{"ok": True, "na": True, "detail": f"{path}: 본문 이미지 0건 (A13 해당 없음)"}]
    entries = []
    for name in A13_CONFIGS:
        config = configs.get(name) or {}
        rule = config.get("ruleColor") or ""
        hairline = []
        for image in _post_images(config):
            shadow = image.get("boxShadow") or ""
            if not (rule and rule in shadow and "0px 0px 0px 1px" in shadow):
                continue
            hairline.append(image)
            widths = image.get("borderWidths") or [0, 0, 0, 0]
            colors = image.get("borderColors") or ["", "", "", ""]
            gaps = [
                f"{side} {width}px {color!r}"
                for side, width, color in zip(("top", "right", "bottom", "left"), widths, colors)
                if float(width) > 0 and _alpha(color) == 0
            ]
            entries.append({
                "ok": not gaps,
                "detail": f"{path} {name} {image.get('src')}: borderGaps={gaps or '없음'} "
                          f"outline={image.get('outline')!r}",
            })
        rows = {}
        for image in hairline:
            key = image.get("rowKey")
            if key is not None:
                rows.setdefault(key, []).append(image)
        for key in sorted(rows):
            row = rows[key]
            if len(row) < 2:
                continue
            widths = [_visible_width(image) for image in row]
            spread = max(widths) - min(widths)
            entries.append({
                "ok": spread <= ROW_WIDTH_TOL,
                "detail": f"{path} {name} row {key}: visibleWidths="
                          f"{[round(width, 1) for width in widths]} spread={spread:.1f}px "
                          f"(기준 <= {ROW_WIDTH_TOL}px)",
            })
    return entries


def _a14_failed_conditions(row):
    opened = row["opened"]
    after_tab = row["afterTab"]
    after_esc = row["afterEsc"]
    after_outside = row["afterOutsideClick"]
    before = row["before"]
    src = (row.get("img") or {}).get("src")
    big = opened.get("big") or {}
    in_view_ok = bool(opened.get("inView")) or (
        bool(opened.get("scrollMode")) and bool(opened.get("inViewX"))
        and big.get("y") is not None and big["y"] >= 0
        and bool(opened.get("overlayScrollable")))
    conditions = [
        ("opened.open", bool(opened.get("open"))),
        ("opened.inView", in_view_ok),
        ("opened.ratioErr", opened.get("ratioErr") is not None and opened["ratioErr"] < 0.01),
        ("afterTab.open", bool(after_tab.get("open"))),
        ("afterTab.activeInLightbox", bool(after_tab.get("activeInLightbox"))),
        ("afterEsc.open", not after_esc.get("open")),
        ("afterEsc.activeSrc", after_esc.get("activeSrc") == src),
        ("afterEsc.rootOverflow", after_esc.get("rootOverflow") == before.get("rootOverflow")),
        ("afterOutsideClick.open", not after_outside.get("open")),
        ("afterOutsideClick.rootOverflow",
         after_outside.get("rootOverflow") == before.get("rootOverflow")),
    ]
    return [name for name, ok in conditions if not ok]


def a14_checks(path, lightbox):
    if not any((data or {}).get("applicable") for data in (lightbox or {}).values()):
        return [{"ok": True, "na": True, "detail": f"{path}: 확대할 그림 0건 (A14 해당 없음)"}]
    entries = []
    for name, data in (lightbox or {}).items():
        if not (data or {}).get("applicable"):
            continue
        for row in data.get("rows") or []:
            meta = row.get("img") or {}
            if row.get("error"):
                entries.append({"ok": False,
                                "detail": f"{path} {name} {meta.get('src')}: error={row['error']}"})
                continue
            failed = _a14_failed_conditions(row)
            opened = row["opened"]
            big = opened.get("big") or {}
            entries.append({
                "ok": not failed,
                "detail": f"{path} {name} {meta.get('src')}: big={big.get('w')}x{big.get('h')} "
                          f"in {opened.get('vw')}x{opened.get('vh')} "
                          f"scrollMode={bool(opened.get('scrollMode'))} failed={failed or '없음'}",
            })
    return entries


def a15_checks(path, configs):
    quotes = (configs.get("wide-light") or {}).get("quotes")
    if not quotes:
        return [{"ok": True, "na": True, "detail": f"{path}: 곧은 따옴표 측정 없음 (A15 해당 없음)"}]
    hits = quotes.get("hits") or []
    sample = "; ".join(repr(hit) for hit in hits[:3])
    return [{
        "ok": quotes.get("hitCount", 0) == 0,
        "detail": f"{path} wide-light: blocks={quotes.get('blocks', 0)} "
                  f"hitCount={quotes.get('hitCount', 0)}" + (f" / {sample}" if sample else ""),
    }]


def summarize_checks(entries, limit=40):
    graded = [entry for entry in entries if not entry.get("na")]
    na = [entry for entry in entries if entry.get("na")]
    failed = [entry for entry in graded if not entry["ok"]]
    return {
        "checked": len(graded),
        "na": len(na),
        "passed": len(graded) - len(failed),
        "failed": len(failed),
        "pass": bool(entries) and not failed,
        "failures": failed[:limit],
        "naDetails": [entry["detail"] for entry in na][:5],
    }
