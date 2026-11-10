"""A9/A10/A11 measurements for verify_article_ui.py (card #1177).

A9: table inline code mid-word breaks, measured per character with Range rects.
A10: inline math punctuation orphan, measured with Range rect tops.
A11: math bounds and wide table overflow.

Both measurements run identically on the 9b8f1de build and the new build.
A10 does not depend on `.math-nowrap`; it reads the rendered math box that
KaTeX auto-render leaves in place.
"""

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
  return {bounds, tables};
}
"""

A9_WIDE_CONFIGS = ("mid-light", "wide-light")
A9_NARROW_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light")
A10_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light", "wide-light")
A11_NARROW_CONFIGS = ("min360-light", "narrow-light", "min414-light")


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
