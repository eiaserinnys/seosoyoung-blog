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
A16_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light", "phablet-light", "tablet-light", "tablet820-light", "mid-light", "wide-light", "wide-dark", "narrow-dark")
ROW_WIDTH_TOL = 0.5
DIAGRAM_MIN_EFF_PX = 10.9
DIAGRAM_MOBILE_MAX_SCALE = 1.15
DIAGRAM_HEADER_RIGHT_TOL = 1.5
DIAGRAM_SWATCH_GAP_TOL = 1.5
DIAGRAM_ITEM_GAP_TOL = 2.0

A16_JS = r"""
() => {
  const content = document.querySelector('.post-content');
  if (!content) return {figs: []};
  const figs = [...content.querySelectorAll('figure.blog-diagram')];
  const out = figs.map((fig, fi) => {
    const visibleSvgs = [...fig.querySelectorAll('svg')].filter(
      (s) => getComputedStyle(s).display !== 'none'
    );
    const svg = visibleSvgs[0];
    if (!svg) {
      return {fig: fi + 1, visibleSvgCount: 0, pInside: fig.querySelectorAll('p').length,
              brInside: fig.querySelectorAll('br').length};
    }
    const r = svg.getBoundingClientRect();
    const vb = svg.viewBox.baseVal;
    const scale = r.width / (vb.width || 1);
    const texts = [...svg.querySelectorAll('text')].map((t) => {
      const b = t.getBBox();
      const fs = parseFloat(getComputedStyle(t).fontSize);
      return {
        text: t.textContent.trim(),
        fs,
        eff: +(fs * scale).toFixed(2),
        x: b.x,
        y: b.y,
        w: b.width,
        h: b.height,
        r: +(b.x + b.width).toFixed(1),
        fill: getComputedStyle(t).fill,
        anchor: t.getAttribute('text-anchor') || 'start',
      };
    });
    const rects = [...svg.querySelectorAll('rect')]
      .map((rc) => ({
        x: +rc.getAttribute('x') || 0,
        y: +rc.getAttribute('y') || 0,
        w: +rc.getAttribute('width'),
        h: +rc.getAttribute('height'),
        fill: rc.getAttribute('fill'),
        stroke: rc.getAttribute('stroke'),
      }))
      .filter((rc) => !(rc.w === vb.width && rc.h === vb.height));
    const outside = texts
      .filter((t) => t.x < -0.5 || t.y < -0.5 || t.x + t.w > vb.width + 0.5 || t.y + t.h > vb.height + 0.5)
      .map((t) => ({text: t.text, tb: [+t.x.toFixed(1), +t.y.toFixed(1), +t.w.toFixed(1), +t.h.toFixed(1)]}));
    const ov = [];
    for (let i = 0; i < texts.length; i++) {
      for (let j = i + 1; j < texts.length; j++) {
        const a = texts[i], b = texts[j];
        const ix = Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x);
        const iy = Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y);
        if (ix > 0.5 && iy > 0.5) ov.push([a.text, b.text, +ix.toFixed(1), +iy.toFixed(1)]);
      }
    }
    const cross = [];
    texts.forEach((t) => rects.forEach((rc) => {
      const inside = (px, py) => px >= rc.x - 0.5 && px <= rc.x + rc.w + 0.5
                              && py >= rc.y - 0.5 && py <= rc.y + rc.h + 0.5;
      const strictIn = (px, py) => px > rc.x + 0.5 && px < rc.x + rc.w - 0.5
                                && py > rc.y + 0.5 && py < rc.y + rc.h - 0.5;
      const inCount = [strictIn(t.x, t.y), strictIn(t.x + t.w, t.y),
                       strictIn(t.x, t.y + t.h), strictIn(t.x + t.w, t.y + t.h)].filter(Boolean).length;
      const outCount = [!inside(t.x, t.y), !inside(t.x + t.w, t.y),
                        !inside(t.x, t.y + t.h), !inside(t.x + t.w, t.y + t.h)].filter(Boolean).length;
      if (inCount > 0 && outCount > 0) {
        cross.push({text: t.text, rect: [rc.x, rc.y, rc.w, rc.h],
                    tb: [+t.x.toFixed(1), +t.y.toFixed(1), +t.w.toFixed(1), +t.h.toFixed(1)]});
      }
    }));
    const boxRects = rects.filter((rc) => rc.w > 40 && rc.h > 24);
    const headerRules = [...svg.querySelectorAll('line')].filter((l) => {
      const x1 = +l.getAttribute('x1'), x2 = +l.getAttribute('x2');
      const y1 = +l.getAttribute('y1'), y2 = +l.getAttribute('y2');
      if (y1 !== y2 || (x2 - x1) <= vb.width * 0.8) return false;
      return !boxRects.some((rc) => y1 > rc.y + 1 && y1 < rc.y + rc.h - 1
                                 && x1 >= rc.x - 1 && x2 <= rc.x + rc.w + 1);
    });
    let headerRow = null;
    if (headerRules.length > 0) {
      const hr = headerRules[0];
      const rx1 = +hr.getAttribute('x1'), rx2 = +hr.getAttribute('x2'), ry = +hr.getAttribute('y1');
      const items = [...svg.querySelectorAll('text, rect')]
        .map((e) => ({tag: e.tagName.toLowerCase(), t: (e.textContent || '').trim().slice(0, 24), b: e.getBBox()}))
        .filter((e) => e.b.width > 0 && e.b.y + e.b.height <= ry + 1 && !(e.b.width >= vb.width - 1))
        .map((e) => ({tag: e.tag, t: e.t, x: +e.b.x.toFixed(1), r: +(e.b.x + e.b.width).toFixed(1),
                      w: +e.b.width.toFixed(1), cy: +(e.b.y + e.b.height / 2).toFixed(1)}))
        .sort((a, b) => a.x - b.x);
      const rightEdge = items.length ? Math.max(...items.map((it) => it.r)) : null;
      const rightDiff = rightEdge !== null ? +(rx2 - rightEdge).toFixed(1) : null;
      const swatchGaps = [];
      const itemGaps = [];
      for (let i = 0; i < items.length - 1; i++) {
        if (items[i].tag === 'rect' && items[i + 1].tag === 'text') {
          swatchGaps.push(+(items[i + 1].x - items[i].r).toFixed(1));
          if (i + 2 < items.length && items[i + 2].tag === 'rect') {
            itemGaps.push(+(items[i + 2].x - items[i + 1].r).toFixed(1));
          }
        }
      }
      headerRow = {rule: [rx1, rx2, ry], items, rightEdge, rightDiff, swatchGaps, itemGaps};
    }
    const effs = texts.map((t) => t.eff);
    return {
      fig: fi + 1,
      visibleSvgCount: visibleSvgs.length,
      pInside: fig.querySelectorAll('p').length,
      brInside: fig.querySelectorAll('br').length,
      cls: svg.getAttribute('class'),
      vb: [vb.width, vb.height],
      rendered: [+r.width.toFixed(1), +r.height.toFixed(1)],
      scale: +scale.toFixed(3),
      minEff: effs.length ? Math.min(...effs) : null,
      maxEff: effs.length ? Math.max(...effs) : null,
      textCount: texts.length,
      small: texts.filter((t) => t.eff < 10.9).map((t) => [t.text, t.eff]),
      outside,
      ov,
      cross,
      headerRow,
      caption: fig.querySelector('figcaption') ? fig.querySelector('figcaption').textContent.trim() : null,
    };
  });
  return {figs: out};
}
"""


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
        return [{"ok": True, "na": True, "detail": f"{path}: 수식 측정 없음 (A10 해당 없음)"}]
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
        return [{"ok": True, "na": True, "detail": f"{path}: 수식 측정 없음 (A11 해당 없음)"}]
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


def a16_checks(path, configs):
    has_figs = any(((cfg or {}).get("diagrams") or {}).get("figs") for cfg in configs.values())
    if not has_figs:
        return [{"ok": True, "na": True, "detail": f"{path}: 인라인 도표 0건 (A16 해당 없음)"}]
    entries = []
    for name in A16_CONFIGS:
        figs = (((configs.get(name) or {}).get("diagrams")) or {}).get("figs") or []
        if not figs:
            continue
        all_swatch = []
        all_item = []
        for f in figs:
            dom_ok = (f.get("visibleSvgCount") == 1
                      and f.get("pInside", 0) == 0
                      and f.get("brInside", 0) == 0)
            min_eff = f.get("minEff")
            small = f.get("small") or []
            outside = f.get("outside") or []
            ov = f.get("ov") or []
            cross = f.get("cross") or []
            hr = f.get("headerRow")
            hr_diff = hr.get("rightDiff") if hr else None
            hr_ok = hr is None or (hr_diff is not None and abs(hr_diff) <= DIAGRAM_HEADER_RIGHT_TOL)
            cls = f.get("cls") or ""
            scale = f.get("scale")
            mobile_scale_ok = ("diagram-svg-mobile" not in cls.split()) or (
                scale is not None and scale <= DIAGRAM_MOBILE_MAX_SCALE)
            ok = (dom_ok and min_eff is not None and min_eff >= DIAGRAM_MIN_EFF_PX
                  and mobile_scale_ok
                  and not small and not outside and not ov and not cross and hr_ok)
            entries.append({
                "ok": ok,
                "detail": (
                    f"{path} {name} fig{f.get('fig')} ({f.get('cls')}): "
                    f"eff={min_eff}..{f.get('maxEff')} small={len(small)} "
                    f"outside={len(outside)} ov={len(ov)} cross={len(cross)} "
                    f"headerRightDiff={hr_diff} scale={scale}"
                ),
            })
            if hr:
                all_swatch.extend(hr.get("swatchGaps") or [])
                all_item.extend(hr.get("itemGaps") or [])
        if len(all_swatch) >= 2:
            spread = round(max(all_swatch) - min(all_swatch), 1)
            entries.append({
                "ok": spread <= DIAGRAM_SWATCH_GAP_TOL,
                "detail": f"{path} {name} legend swatchGaps={all_swatch} spread={spread}px "
                          f"(기준 <= {DIAGRAM_SWATCH_GAP_TOL}px)",
            })
        if len(all_item) >= 2:
            spread = round(max(all_item) - min(all_item), 1)
            entries.append({
                "ok": spread <= DIAGRAM_ITEM_GAP_TOL,
                "detail": f"{path} {name} legend itemGaps={all_item} spread={spread}px "
                          f"(기준 <= {DIAGRAM_ITEM_GAP_TOL}px)",
            })
    return entries


# A17: 넘치는 표 첫 열 고정(post.js의 is-sticky-first). 폭 비율 기준은 post.js와 같다.
STICKY_FIRST_MAX_RATIO = 0.4
A17_CONFIGS = ("narrow-light", "narrow-dark")


def a17_checks(path, configs):
    entries = []
    tables = 0
    for name in A17_CONFIGS:
        for row in ((configs.get(name) or {}).get("sticky") or []):
            tables += 1
            width = row.get("firstCellWidth")
            wrap = row.get("wrapClient") or 0
            expected = (bool(row.get("overflowing")) and width is not None and wrap > 0
                        and width <= wrap * STICKY_FIRST_MAX_RATIO)
            bg = row.get("firstCellBg") or {}
            body = row.get("bodyBg") or {}
            bg_same = (bg.get("a") == 1 and body.get("a") is not None
                       and (bg.get("r"), bg.get("g"), bg.get("b"))
                       == (body.get("r"), body.get("g"), body.get("b")))
            if expected:
                left = row.get("firstLeftDiff")
                ok = bool(row.get("sticky")) and left is not None and abs(left) <= 1 and bg_same
                detail = (f"{path} {name} table {row.get('index')}: sticky={row.get('sticky')} "
                          f"expected=True firstCol={width}/{wrap}px firstLeftDiff={left} "
                          f"bg={bg} bodyBg={body}")
            else:
                ok = not row.get("sticky") and row.get("firstCellPosition") == "static"
                detail = (f"{path} {name} table {row.get('index')}: sticky={row.get('sticky')} "
                          f"expected=False position={row.get('firstCellPosition')} "
                          f"overflowing={row.get('overflowing')} firstCol={width}/{wrap}px")
            entries.append({"ok": ok, "detail": detail})
    for row in ((configs.get("wide-light") or {}).get("sticky") or []):
        if row.get("overflowing"):
            continue
        entries.append({"ok": not row.get("sticky"),
                        "detail": f"{path} wide-light table {row.get('index')}: "
                                  f"sticky={row.get('sticky')} overflowing=False"})
    if not tables:
        entries.append({"ok": True, "na": True, "detail": f"{path}: 375 폭 표 0건 (A17 해당 없음)"})
    return entries


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
