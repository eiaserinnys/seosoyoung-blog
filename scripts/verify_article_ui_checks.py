"""A9/A10 measurements for verify_article_ui.py (card #1177, round 2).

A9: table inline code mid-word breaks, measured per character with Range rects.
A10: inline math punctuation orphan, measured with Range rect tops.

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
() => {
  const content = document.querySelector('.post-content');
  if (!content) return {math: [], checked: 0, violations: 0};
  const topOfChar = (node, offset) => {
    const range = document.createRange();
    range.setStart(node, offset);
    range.setEnd(node, offset + 1);
    const rects = range.getClientRects();
    return rects.length ? +rects[0].top.toFixed(1) : null;
  };
  const mathEls = [...content.querySelectorAll('.katex')].filter((m) => !m.closest('.katex-display'));
  const out = mathEls.map((m, i) => {
    const parent = m.parentElement;
    // auto-render puts the returned .katex inside an anonymous span; that span
    // is the inline box whose siblings are the surrounding text nodes.
    const mathNode = (parent && parent.childElementCount === 1
      && parent.textContent.trim() === m.textContent.trim()) ? parent : m;
    const prev = mathNode.previousSibling;
    const next = mathNode.nextSibling;
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
    if (next && next.nodeType === 3) {
      const lead = next.data.match(/^\s*/)[0].length;
      if (lead < next.data.length) {
        nextChar = next.data[lead];
        nextTop = topOfChar(next, lead);
      }
    }
    const rects = mathNode.getClientRects();
    const startTop = rects.length ? +rects[0].top.toFixed(1) : null;
    const endTop = rects.length ? +rects[rects.length - 1].top.toFixed(1) : null;
    const open = !!prevChar && /[(\[{]/.test(prevChar);
    const close = !!nextChar && /[)\]},.:;!?%]/.test(nextChar);
    const openViolation = !!(open && prevTop !== null && startTop !== null
      && Math.abs(prevTop - startTop) > 1);
    const closeViolation = !!(close && nextTop !== null && endTop !== null
      && Math.abs(nextTop - endTop) > 1);
    const cell = m.closest('td,th');
    return {
      i: i,
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
      mathNodeTag: mathNode.tagName,
      mathNodeClass: String(mathNode.className || ''),
      mathNodeSiblings: [prev ? prev.nodeName : null, next ? next.nodeName : null],
    };
  });
  return {
    math: out,
    checked: out.filter((m) => m.open || m.close).length,
    violations: out.filter((m) => m.openViolation || m.closeViolation).length,
  };
}
"""

A9_WIDE_CONFIGS = ("mid-light", "wide-light")
A9_NARROW_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light")
A10_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light", "wide-light")


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
    if "memory-caching-rnns" not in path:
        return []
    entries = []
    for name in A10_CONFIGS:
        data = (configs.get(name) or {}).get("a10") or {}
        math = data.get("math") or []
        checked = data.get("checked", 0)
        violations = data.get("violations", 0)
        bad = [m for m in math if m.get("openViolation") or m.get("closeViolation")]
        sample = "; ".join(
            f"{m.get('cell') or '(본문)'} prev={m.get('prevChar')!r}@{m.get('prevTop')} "
            f"math={m.get('startTop')}..{m.get('endTop')} next={m.get('nextChar')!r}@{m.get('nextTop')} "
            f"open={m.get('openViolation')} close={m.get('closeViolation')}"
            for m in bad[:4]
        )
        entries.append({
            "ok": checked > 0 and violations == 0,
            "detail": f"{path} {name}: checked={checked} violations={violations}"
                      + (f" / {sample}" if sample else ""),
        })
    return entries
