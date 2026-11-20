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
  const codes = [...document.querySelectorAll('.post-content table :not(pre) > code')].filter(c => !c.closest('.table-header-clone')).map((c, i) => {
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
  const loneCharCells = [];
  wrappers.forEach((wrap, ti) => {
    const table = wrap.querySelector(':scope > table');
    if (!table) return;
    [...table.querySelectorAll('th, td')].forEach((cell) => {
      const items = [];
      const walker = document.createTreeWalker(cell, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT);
      let node;
      while ((node = walker.nextNode())) {
        if (node.nodeType === Node.ELEMENT_NODE) {
          if (node.classList.contains('katex')) {
            const html = node.querySelector('.katex-html');
            const text = (html ? html.textContent : node.textContent).replace(/\s+/g, '');
            const rect = node.getBoundingClientRect();
            if (text && rect.width > 0 && rect.height > 0) {
              items.push({top: rect.top, bottom: rect.bottom, text});
            }
          }
          continue;
        }
        const parent = node.parentElement;
        if (!parent || parent.closest('.katex, script, style, svg')) continue;
        for (let k = 0; k < node.data.length; k++) {
          const ch = node.data[k];
          if (!ch.trim()) continue;
          const range = document.createRange();
          range.setStart(node, k);
          range.setEnd(node, k + 1);
          const rects = range.getClientRects();
          if (!rects.length) continue;
          items.push({top: rects[0].top, bottom: rects[0].bottom, text: ch});
        }
      }
      const lines = [];
      for (const item of items) {
        const mid = (item.top + item.bottom) / 2;
        const line = lines.find((l) => Math.abs(mid - l.mid) <= 9);
        if (line) {
          line.text += item.text;
        } else {
          lines.push({mid, text: item.text});
        }
      }
      if (lines.length > 1) {
        const lone = lines
          .filter((l) => l.text.length === 1 && !/[가-힣ㄱ-ㅎㅏ-ㅣ.,:;!?()\[\]]/.test(l.text))
          .map((l) => l.text);
        if (lone.length) {
          loneCharCells.push({
            table: ti + 1,
            text: cell.textContent.trim().slice(0, 48),
            lines: lines.map((l) => l.text),
            lone,
          });
        }
      }
    });
  });
  return {codes: codes, loneCharCells: loneCharCells};
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
    .filter((k) => !k.closest('.katex-display') && !k.closest('.table-header-clone[hidden]'));
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
    const allKatex = [...table.querySelectorAll('.katex')].filter((k) => !k.closest('.katex-display'));
    const isMathTable = wrap.classList.contains('is-math-table');
    const maxLines = allKatex.length ? Math.max(...allKatex.map((k) => k.getClientRects().length)) : 0;
    const overflowing = wrap.classList.contains('is-overflowing') && !wrap.classList.contains('is-expanded');
    return {i: i + 1, hasMath: allKatex.length > 0, isMathTable, overflowing, maxLines};
  }).filter((table) => table.hasMath);
  const displays = [...content.querySelectorAll('.katex-display')].map((k, i) => {
    const style = getComputedStyle(k);
    return {
      i: i + 1,
      clientW: k.clientWidth,
      scrollW: k.scrollWidth,
      over: +(k.scrollWidth - k.clientWidth).toFixed(2),
      overflowX: style.overflowX,
      backgroundImage: style.backgroundImage,
      tex: (k.querySelector('annotation') || {}).textContent || '',
    };
  });
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
    let singleOpen = false;
    let doubleOpen = false;
    for (let i = 0; i < text.length; i++) {
      const ch = text[i];
      const prev = text[i - 1] || '';
      const next = text[i + 1] || '';
      // 여는 따옴표가 한글 조사와 이어지는데 바로 앞이 닫는 소괄호이거나, 같은 블록에 아직 닫히지 않은
      // 같은 종류의 여는 따옴표가 앞에 있으면 닫는 따옴표가 뒤집힌 것이다. 바로 앞이 같은 여는 부호인
      // 자리는 겹쳐 쓴 여는 부호이므로 후처리와 같이 세지 않는다.
      const sameKindOpen = ch === '‘' ? singleOpen : ch === '“' ? doubleOpen : false;
      if ((ch === '‘' || ch === '“') && /[가-힣]/.test(next)
          && (prev === ')' || (sameKindOpen && prev !== ch))) {
        hitCount++;
        if (hits.length < 20) hits.push(text.slice(Math.max(0, i - 20), i + 21));
        // 뒤집힌 부호는 앞의 여는 따옴표를 닫는 자리이므로 상태를 닫는다.
        if (ch === '‘') singleOpen = false; else doubleOpen = false;
        continue;
      }
      if (ch === '‘') { singleOpen = true; continue; }
      if (ch === '’') { singleOpen = false; continue; }
      if (ch === '“') { doubleOpen = true; continue; }
      if (ch === '”') { doubleOpen = false; continue; }
      if (ch !== '"') continue;
      if (doubleOpen || /[가-힣]/.test(prev) || /[가-힣]/.test(next)) {
        hitCount++;
        if (hits.length < 20) hits.push(text.slice(Math.max(0, i - 20), i + 21));
        // 곧은 큰따옴표가 닫는 자리였으면 앞의 여는 따옴표를 닫는다.
        doubleOpen = false;
      }
    }
  }
  return {blocks: order.length, hitCount, hits};
}
"""

A9_WIDE_CONFIGS = ("tablet-light", "mid-light", "wide-light")
A9_NARROW_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light")
A9_LONE_CHAR_CONFIGS = ("min360-light", "narrow-light", "min390-light")
WIDE_TABLE_MAX_CELL_LINES = 6
WIDE_CODE_SHORT_LEN = 24
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
DIAGRAM_BOX_PAD_RATIO_MAX = 1.45

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
    const boxPads = boxRects.filter((rc) => rc.stroke).map((rc) => {
      const inside = texts.filter((t) => t.x >= rc.x - 0.5 && t.x + t.w <= rc.x + rc.w + 0.5
                                      && t.y >= rc.y - 0.5 && t.y + t.h <= rc.y + rc.h + 0.5);
      const insideRects = boxRects.filter((other) => other !== rc
                                      && other.x >= rc.x - 0.5 && other.x + other.w <= rc.x + rc.w + 0.5
                                      && other.y >= rc.y - 0.5 && other.y + other.h <= rc.y + rc.h + 0.5);
      if (!inside.length || insideRects.length > 0) return null;
      const top = Math.min(...inside.map((t) => t.y));
      const bottom = Math.max(...inside.map((t) => t.y + t.h));
      const topGap = +(top - rc.y).toFixed(1);
      const bottomGap = +((rc.y + rc.h) - bottom).toFixed(1);
      const lo = Math.max(1, Math.min(topGap, bottomGap));
      const hi = Math.max(topGap, bottomGap);
      return {
        box: [rc.x, rc.y, rc.w, rc.h],
        first: inside[0].text.slice(0, 24),
        topGap,
        bottomGap,
        padRatio: +(hi / lo).toFixed(2),
      };
    }).filter(Boolean);
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
      boxPads,
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


def _code_split_bad(code):
    lines = code.get("lines") or 1
    text = (code.get("text") or "").strip()
    return bool(code.get("midWord")) or (lines > 1 and len(text) <= WIDE_CODE_SHORT_LEN) or lines > 2


def _a9_detail(path, name, codes, tables=None):
    bad = [c for c in codes if _code_split_bad(c)]
    max_lines = max(((c.get("lines") or 1) for c in codes), default=0)
    sample = "; ".join(
        f"table {c.get('table')} {c.get('text')!r} lines={c.get('lines')} breaks={_midword_breaks(c)}"
        for c in bad[:5]
    )
    table_part = ""
    if tables is not None:
        cell_lines = [f"t{t.get('i')}={t.get('maxLinesPerCell')}" for t in tables]
        table_part = f" maxLinesPerCell=[{', '.join(cell_lines)}]"
    return (
        f"{path} {name}: code={len(codes)} maxCodeLines={max_lines} badCode={len(bad)} "
        f"overflowing={sum(1 for c in codes if c.get('overflowing'))}{table_part}"
        + (f" / {sample}" if sample else "")
    )


def a9_checks(path, configs):
    entries = []
    for name in A9_WIDE_CONFIGS:
        cfg = configs.get(name) or {}
        codes = (cfg.get("a9") or {}).get("codes") or []
        tables = cfg.get("tables") or []
        bad_tables = [t for t in tables if (t.get("maxLinesPerCell") or 0) > WIDE_TABLE_MAX_CELL_LINES]
        entries.append({
            "ok": not any(_code_split_bad(c) for c in codes) and not bad_tables,
            "detail": _a9_detail(path, name, codes, tables),
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
    lone_by_cell = {}
    for name in A9_LONE_CHAR_CONFIGS:
        for cell in (((configs.get(name) or {}).get("a9") or {}).get("loneCharCells") or []):
            key = (cell.get("table"), cell.get("text"))
            rec = lone_by_cell.setdefault(key, {
                "table": cell.get("table"),
                "text": cell.get("text"),
                "lines": cell.get("lines"),
                "lone": cell.get("lone"),
                "configs": [],
            })
            rec["configs"].append(name)
    for rec in lone_by_cell.values():
        entries.append({
            "ok": False,
            "detail": (f"{path} {','.join(rec['configs'])} table {rec['table']} "
                       f"{rec['text']!r}: 한글 아닌 한 글자 단독 줄 {rec['lone']} lines={rec['lines']}"),
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
            # 못 줄이는 블록 수식은 넘치되 가로 스크롤과 넘침 그림자 힌트를 갖춰야 통과한다.
            over = [item for item in displays if item["over"] > 1]
            bad_disp = [item for item in over
                        if item.get("overflowX") not in ("auto", "scroll")
                        or (item.get("backgroundImage") or "none") == "none"]
            entries.append({"ok": not bad_disp,
                            "detail": f"{path} {name}: displayMath={len(displays)} over={len(over)} "
                                      f"noHint={len(bad_disp)} examples={bad_disp[:4]}"})
        for table in data.get("tables") or []:
            if not table.get("isMathTable"):
                continue
            max_lines = table.get("maxLines", 1)
            entries.append({"ok": max_lines <= 1,
                            "detail": f"{path} {name}: math table {table['i']} maxLines={max_lines}"})
    wide = ((configs.get("wide-light") or {}).get("a11") or {})
    side_bounds = [item for item in wide.get("bounds", []) if item.get("side")]
    if side_bounds:
        bad = [item for item in side_bounds if item["over"] > 1]
        entries.append({"ok": not bad, "detail": f"{path} wide-light: side math={len(side_bounds)} "
                                                 f"over={len(bad)} examples={bad[:4]}"})
    tables = wide.get("tables") or []
    for table in tables:
        max_lines = table.get("maxLines", 1)
        lines_ok = (max_lines <= 1) if table.get("isMathTable") else True
        entries.append({"ok": not table["overflowing"] and lines_ok,
                        "detail": f"{path} wide-light: math table {table['i']} overflowing={table['overflowing']}"
                                  + (f" maxLines={max_lines}" if table.get("isMathTable") else "")})
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
    # 바탕의 실제 안쪽 폭보다 넓게 열었다면 그 폭의 1.5배 이상이어야 한다. 조금만 넓게
    # 열려 일부만 잘리는 상태는 만들지 않는다.
    box = opened.get("box") or {}
    width_limit = float(box.get("w") or (float(opened.get("vw") or 0) * 0.96))
    big_w = float(big.get("w") or 0)
    no_slight_overflow = big_w <= width_limit + 1 or big_w >= width_limit * 1.5 - 2
    in_view_ok = bool(opened.get("inView")) or (
        bool(opened.get("scrollMode")) and bool(opened.get("inViewX"))
        and big.get("y") is not None and big["y"] >= 0
        and bool(opened.get("overlayScrollable"))) or (
        # 좁은 화면에서 높이에 맞춰 연 그림은 화면보다 넓다. 왼쪽 끝에서 시작하고 가로로 밀 수 있으면 된다.
        bool(opened.get("wideMode")) and big.get("x") is not None and big["x"] >= -0.5
        and big.get("y") is not None and big["y"] >= 0
        and bool(opened.get("overlayScrollableX")))
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
        ("noSlightOverflow", no_slight_overflow),
    ]
    return [name for name, ok in conditions if not ok]


def _a14_state_geometry(row):
    """연 그림의 원래 본문 폭과 바탕 안쪽 상자로부터, 규칙이 내는 열림 폭과 새 규칙 적용 여부를 셈한다."""
    meta = row.get("img") or {}
    opened = row.get("opened") or {}
    big = opened.get("big") or {}
    natural = big.get("natural") or [0, 0]
    rendered = meta.get("width")
    box = opened.get("box") or {}
    box_width = box.get("w")
    box_height = box.get("h")
    if not (natural[0] and natural[1] and rendered and box_width and box_height):
        return None
    ratio = natural[1] / natural[0]
    height_limit = min(box_height * 0.88, box_height * 0.94 - float(opened.get("captionH") or 0))
    fit = min(natural[0], box_width, height_limit / ratio)
    height_fit = min(natural[0], height_limit / ratio)
    expected = (min(max(rendered, min(natural[0], box_width)), box_width)
                if fit < rendered - 1 else fit)
    return {
        "rendered": rendered,
        "fit": fit,
        "heightFit": height_fit,
        "expectedWidth": expected,
        # 반올림 경계에서 판정이 흔들리지 않게 5px 여유를 둔다.
        # lightbox.js와 같이 높이에 맞춘 폭이 바탕 안쪽 폭의 1.5배 이상일 때만 새 규칙이다.
        "newRule": fit < rendered * 1.5 - 5 and height_fit >= box_width * 1.5,
    }


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
            geo = _a14_state_geometry(row)
            if geo and name in ("narrow-light", "narrow-dark") and geo["newRule"]:
                panned = row.get("panned") or {}
                panned_big = panned.get("big") or {}
                vw = opened.get("vw") or 0
                failed += [name_ for name_, ok in (
                    ("narrow.width>=1.5x", (big.get("w") or 0) >= geo["rendered"] * 1.5 - 1),
                    ("narrow.leftEdge", big.get("x") is not None and big["x"] >= -0.5),
                    ("narrow.panToEnd", panned_big.get("right") is not None
                     and panned_big["right"] <= vw + 0.5
                     and bool(panned.get("overlayScrollableX"))),
                ) if not ok]
            if geo and name == "wide-light":
                failed += [name_ for name_, ok in (
                    ("wide.expectedWidth", abs((big.get("w") or 0) - geo["expectedWidth"]) <= 2),
                ) if not ok]
            entries.append({
                "ok": not failed,
                "detail": f"{path} {name} {meta.get('src')}: big={big.get('w')}x{big.get('h')} "
                          f"body={geo and round(geo['rendered'], 1)} "
                          f"in {opened.get('vw')}x{opened.get('vh')} "
                          f"scrollMode={bool(opened.get('scrollMode'))} "
                          f"wideMode={bool(opened.get('wideMode'))} failed={failed or '없음'}",
            })
    return entries


LIGHTBOX_THUMB_STATES = ("normal", "hover", "active")


def _lightbox_thumb_values(thumb):
    """썸 두께 측정값이 보통·올림·누름 모두 숫자로 있으면 돌려준다. 아니면 None."""
    if not isinstance(thumb, dict) or thumb.get("error"):
        return None
    values = {}
    for state in LIGHTBOX_THUMB_STATES:
        value = thumb.get(state)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return None
        values[state] = value
    return values


def strict_lightbox_checks(path, lightbox):
    """--strict-lightbox: 연 상태마다 바탕 넘침과 화면 정렬을 잰다.

    wide가 아니면 가로 넘침이 없고(scrollWidth <= clientWidth + 1) 바탕 안 좌우 틈 차이와
    창 기준 좌우 틈 차이가 1px 이하이며, wide면 세로 넘침이 없어야 한다. 열린 모든 상태에서
    바탕 오른쪽 끝이 window.innerWidth와 1px 안이어야 하고, 닫은 뒤 scrollY와 본문 첫 요소 x가
    연 앞과 1px 안으로 같아야 한다. 데스크톱 wide 가로 막대 썸 두께는 같은 상태의 페이지 세로
    막대 썸 두께와 같아야 한다. 처음 연 상태(opened)와 창 크기를 바꾼 뒤(afterResize)를 본다.
    """
    entries = []
    for name, data in (lightbox or {}).items():
        if not (data or {}).get("applicable"):
            continue
        page_thumb = _lightbox_thumb_values((data or {}).get("pageThumb"))
        for row in data.get("rows") or []:
            src = (row.get("img") or {}).get("src")
            if row.get("error"):
                entries.append({"ok": False,
                                "detail": f"{path} {name} {src}: 열지 못함 error={row['error']}"})
                continue
            for state in ("opened", "afterResize"):
                measured = row.get(state)
                if not measured:
                    continue
                if not measured.get("open"):
                    entries.append({"ok": False,
                                    "detail": f"{path} {name} {src} [{state}]: 열린 상태가 아님"})
                    continue
                overlay = measured.get("overlay") or {}
                client_w = overlay.get("clientW")
                client_h = overlay.get("clientH")
                scroll_w = overlay.get("scrollW")
                scroll_h = overlay.get("scrollH")
                left_gap = overlay.get("leftGap")
                right_gap = overlay.get("rightGap")
                overlay_right = overlay.get("right")
                vw = measured.get("vw")
                if None in (client_w, client_h, scroll_w, scroll_h, left_gap, right_gap,
                            overlay_right, vw):
                    entries.append({"ok": False,
                                    "detail": f"{path} {name} {src} [{state}]: 바탕 측정값 없음 {overlay!r}"})
                    continue
                right_diff = abs(overlay_right - vw)
                if measured.get("wideMode"):
                    ok = scroll_h <= client_h + 1 and right_diff <= 1
                    entries.append({
                        "ok": ok,
                        "detail": (f"{path} {name} {src} [{state}] wide {vw}x{measured.get('vh')}: "
                                   f"scrollH={scroll_h} clientH={client_h} "
                                   f"overlayRight={overlay_right} vw={vw} rightDiff={round(right_diff, 2)}"),
                    })
                else:
                    screen_left = measured.get("screenLeftGap")
                    screen_right = measured.get("screenRightGap")
                    if None in (screen_left, screen_right):
                        entries.append({"ok": False,
                                        "detail": f"{path} {name} {src} [{state}]: 창 기준 틈 측정값 없음"})
                        continue
                    gap_diff = abs(left_gap - right_gap)
                    win_diff = abs(screen_left - screen_right)
                    ok = scroll_w <= client_w + 1 and gap_diff <= 1 and win_diff <= 1 and right_diff <= 1
                    mode = "scroll" if measured.get("scrollMode") else "fit"
                    entries.append({
                        "ok": ok,
                        "detail": (f"{path} {name} {src} [{state}] {mode} {vw}x{measured.get('vh')}: "
                                   f"scrollW={scroll_w} clientW={client_w} "
                                   f"leftGap={left_gap} rightGap={right_gap} gapDiff={round(gap_diff, 2)} "
                                   f"screenLeftGap={screen_left} screenRightGap={screen_right} "
                                   f"winDiff={round(win_diff, 2)} "
                                   f"overlayRight={overlay_right} vw={vw} rightDiff={round(right_diff, 2)}"),
                    })
            if not (row.get("opened") or {}).get("open"):
                continue
            before = row.get("before") or {}
            base_y = before.get("scrollY")
            base_x = before.get("bodyFirstX")
            if base_y is None or base_x is None:
                entries.append({"ok": False,
                                "detail": f"{path} {name} {src}: 연 앞 scrollY/본문 x 측정값 없음"})
            else:
                for state in ("afterEsc", "afterOutsideClick"):
                    closed = row.get(state) or {}
                    closed_y = closed.get("scrollY")
                    closed_x = closed.get("bodyFirstX")
                    if closed_y is None or closed_x is None:
                        entries.append({"ok": False,
                                        "detail": f"{path} {name} {src} [{state}]: 닫은 뒤 측정값 없음"})
                        continue
                    y_diff = abs(closed_y - base_y)
                    x_diff = abs(closed_x - base_x)
                    entries.append({
                        "ok": y_diff <= 1 and x_diff <= 1,
                        "detail": (f"{path} {name} {src} [{state}]: scrollY={closed_y} (연 앞 {base_y}) "
                                   f"diff={round(y_diff, 2)} bodyFirstX={closed_x} (연 앞 {base_x}) "
                                   f"diff={round(x_diff, 2)}"),
                    })
            opened = row.get("opened") or {}
            if opened.get("wideMode") and (data or {}).get("thumbEligible"):
                wide_values = _lightbox_thumb_values(row.get("wideThumb"))
                if page_thumb is None or wide_values is None:
                    entries.append({
                        "ok": False,
                        "detail": (f"{path} {name} {src} wide: 썸 두께 측정값 없음 "
                                   f"page={data.get('pageThumb')!r} wide={row.get('wideThumb')!r}"),
                    })
                else:
                    same = all(wide_values[s] == page_thumb[s] for s in LIGHTBOX_THUMB_STATES)
                    entries.append({
                        "ok": same,
                        "detail": (f"{path} {name} {src} wide: pageThumb={page_thumb} "
                                   f"wideThumb={wide_values}"),
                    })
    if not entries:
        return [{"ok": True, "na": True,
                 "detail": f"{path}: 확대해 잰 그림 0건 (strict-lightbox 해당 없음)"}]
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
            box_pads = f.get("boxPads") or []
            bad_pads = [b for b in box_pads if (b.get("padRatio") or 1) > DIAGRAM_BOX_PAD_RATIO_MAX]
            ok = (dom_ok and min_eff is not None and min_eff >= DIAGRAM_MIN_EFF_PX
                  and mobile_scale_ok
                  and not small and not outside and not ov and not cross and not bad_pads and hr_ok)
            entries.append({
                "ok": ok,
                "detail": (
                    f"{path} {name} fig{f.get('fig')} ({f.get('cls')}): "
                    f"eff={min_eff}..{f.get('maxEff')} small={len(small)} "
                    f"outside={len(outside)} ov={len(ov)} cross={len(cross)} "
                    f"badPads={len(bad_pads)} headerRightDiff={hr_diff} scale={scale}"
                    + (f" padFailures={bad_pads[:3]}" if bad_pads else "")
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


# A17: 넘치는 표 첫 열 고정(post.js의 is-sticky-first). 여유 폭 기준은 post.js와 같다.
# 2칸 표는 고정하지 않는다(post.js의 cols >= 3 조건).
MIN_COLUMN_EM = 8
MIN_TABLE_COLS = 3
A17_CONFIGS = ("min360-light", "narrow-light", "min390-light", "min414-light", "narrow-dark", "wide-light")


def a5_overflow_checks(path, row):
    candidate = (not row['natural'] and not row['squeezed'] and row['cols'] >= 3
                 and row['longCell'] and row['maxContentWidth'] > row['wrapClient'] + 1)
    expected = row['natural'] or row['squeezed'] or candidate
    rejected = (candidate and not row['isOverflowing'] and row.get('minimumMaxColumn') is not None
                and row['minimumMaxColumn'] > row['minimumVisible'] + 1)
    return [{'ok': row['isOverflowing'] == expected or rejected,
             'detail': f"{path} table {row['index']}: overflowing={row['isOverflowing']} "
                       f"natural={row['natural']} squeezed={row['squeezed']} candidate={candidate} "
                       f"minimum={row.get('minimumMaxColumn')}/{row.get('minimumVisible')}"}]


def a17_checks(path, configs):
    entries = []
    tables = 0
    for name in A17_CONFIGS:
        for row in ((configs.get(name) or {}).get("sticky") or []):
            tables += 1
            width = row.get("firstCellWidth")
            wrap = row.get("wrapClient") or 0
            font = row.get("fontSize")
            room = None if width is None else wrap - width
            need = None if font is None else font * MIN_COLUMN_EM
            cols = row.get("cols")
            expected = (bool(row.get("overflowing")) and cols is not None and cols >= MIN_TABLE_COLS
                        and width is not None and wrap > 0 and need is not None and room >= need)
            bg = row.get("firstCellBg") or {}
            body = row.get("bodyBg") or {}
            bg_same = (bg.get("a") == 1 and body.get("a") is not None
                       and (bg.get("r"), bg.get("g"), bg.get("b"))
                       == (body.get("r"), body.get("g"), body.get("b")))
            if expected:
                head_left = row.get("firstLeftDiff")
                body_left = row.get("bodyLeftDiff")
                scroll_left = row.get("scrollLeft")
                max_scroll = row.get("maxScroll")
                at_end = (scroll_left is not None and max_scroll is not None
                          and abs(scroll_left - max_scroll) <= 1)
                ok = (bool(row.get("sticky"))
                      and head_left is not None and body_left is not None
                      and abs(head_left) <= 1 and abs(body_left) <= 1 and at_end and bg_same)
                detail = (f"{path} {name} table {row.get('index')} ({cols}칸): sticky={row.get('sticky')} "
                          f"expected=True room={room}px need={need}px "
                          f"headLeftDiff={row.get('firstLeftDiff')} bodyLeftDiff={row.get('bodyLeftDiff')} "
                          f"scroll={scroll_left}/{max_scroll} bg={bg} bodyBg={body}")
            else:
                must_stick_390 = (name == "min390-light" and bool(row.get("overflowing"))
                                  and cols is not None and cols >= MIN_TABLE_COLS)
                ok = (not must_stick_390 and not row.get("sticky")
                      and row.get("bodyCellPosition") == "static")
                detail = (f"{path} {name} table {row.get('index')} ({cols}칸): sticky={row.get('sticky')} "
                          f"expected=False bodyPosition={row.get('bodyCellPosition')} "
                          f"overflowing={row.get('overflowing')} room={room}px need={need}px"
                          + (" (390px 넘치는 3칸+ 표는 첫 열 고정 필수)" if must_stick_390 else ""))
            entries.append({"ok": ok, "detail": detail})
    if not tables:
        entries.append({"ok": True, "na": True, "detail": f"{path}: A17 대상 폭 표 0건 (A17 해당 없음)"})
    return entries


def a18_checks(path, configs):
    """A18: 고정 표 첫 열과 둘째 열의 그려진 가로 괘선 y 목록이 같은지, 표 맨 아래 줄이 두 열 모두에 있는지.

    측정값(configs[name]["seams"])은 verify_article_ui.py가 rest/end 스크린샷에서 만든다.
    """
    entries = []
    tables = 0
    for name in A17_CONFIGS:
        for rec in ((configs.get(name) or {}).get("seams") or []):
            tables += 1
            states = rec.get("states") or {}
            bad = [state for state in ("rest", "end") if not (states.get(state) or {}).get("ok")]
            lines = sum(len((states.get(state) or {}).get("a") or [])
                        + len((states.get(state) or {}).get("strongA") or [])
                        for state in ("rest", "end"))
            if bad:
                bits = []
                for state in bad:
                    s = states.get(state) or {}
                    bits.append(f"{state}: a={str(s.get('a'))[:200]} b={str(s.get('b'))[:200]} "
                                f"strongA={s.get('strongA')} strongB={s.get('strongB')} "
                                f"bottomA={s.get('bottomA')} bottomB={s.get('bottomB')} "
                                f"reason={s.get('reason')}")
                detail = (f"{path} {name} table {rec.get('table')} ({rec.get('text')}): "
                          f"괘선 어긋남 {'; '.join(bits)}")
                entries.append({"ok": False, "detail": detail})
            else:
                entries.append({"ok": True,
                                "detail": f"{path} {name} table {rec.get('table')}: "
                                          f"rest+end 괘선 {lines}줄 일치, 표 맨 아래 줄 확인"})
    if not tables:
        entries.append({"ok": True, "na": True, "detail": f"{path}: A18 대상 고정 표 0건 (A18 해당 없음)"})
    return entries


def a19_checks(path, rows):
    """A19: 창 높이만 바뀐 뒤에도 밀어 둔 넘치는 표의 scrollLeft와 두 클래스가 그대로인지."""
    entries = []
    for row in rows or []:
        before = row.get("before") or {}
        after = row.get("after") or {}
        pushed = (before.get("scrollLeft") or 0) > 1
        kept = (after.get("scrollLeft") is not None and before.get("scrollLeft") is not None
                and abs(after["scrollLeft"] - before["scrollLeft"]) <= 1)
        same_classes = (after.get("overflowing") == before.get("overflowing")
                        and after.get("sticky") == before.get("sticky"))
        ok = pushed and kept and same_classes
        detail = (f"{path} narrow-light table {row.get('table')} ({row.get('text')}): "
                  f"높이만 변경 전 scrollLeft={before.get('scrollLeft')}/{before.get('max')} "
                  f"overflowing={before.get('overflowing')} sticky={before.get('sticky')} → "
                  f"후 scrollLeft={after.get('scrollLeft')}/{after.get('max')} "
                  f"overflowing={after.get('overflowing')} sticky={after.get('sticky')}"
                  f"{'' if pushed else ' (밀리지 않아 판정 불가)'}")
        entries.append({"ok": ok, "detail": detail})
    if not entries:
        entries.append({"ok": True, "na": True, "detail": f"{path}: A19 대상 넘치는 표 0건 (A19 해당 없음)"})
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


def a21_checks(path, samples, diagram_counts):
    widths = ('360', '375', '390', '414')
    arrays = [samples.get(width, []) for width in widths]
    if not any(diagram_counts.get(width, 0) for width in widths):
        return [{'ok': True, 'na': True,
                 'detail': f'{path}: 모바일 도식 0건 (A21 해당 없음)'}]
    if not all(arrays) or len({len(a) for a in arrays}) != 1:
        return [{'ok': False,
                 'detail': f'{path}: 모바일 도식 글자 목록이 비었거나 폭마다 길이가 다름 {arrays}'}]
    entries = []
    for i, values in enumerate(zip(*arrays)):
        low, high = min(values), max(values)
        entries.append({'ok': low > 0 and high / low <= 1.005,
                        'detail': f'{path} SVG text {i}: {values}'})
    return entries


def a22_checks(path, rows):
    entries = []
    for row in rows:
        edges = row['edges'] + row['afterScrollEdges'] + row['afterResizeEdges']
        ok = (all(abs(row[k]) <= 1 for k in ('topDiff', 'afterScrollTop', 'afterResizeTop')) and all(row[k] for k in ('edges', 'afterScrollEdges', 'afterResizeEdges'))
              and all(abs(x) <= 1 for x in edges)
              and row['hiddenAfter'] and row['inert'] and row['tabSafe'])
        entries.append({'ok': ok, 'detail': f'{path} A22 {row}'})
    return entries


def a22_rule_checks(path, rows):
    return [{'ok': bool(row['top'] and row['bottom'] and row['beforeThickness'] > 0
                        and row['afterThickness'] > 0
                        and abs(row['beforeThickness'] - row['afterThickness']) <= 1),
             'detail': f"{path} A22 rule {row}"} for row in rows]


def a23_synthetic_coverage(reports):
    return any(row.get('synthetic') for report in reports.values() for row in report.get('synthetic', []))


def a23_checks(path, rows):
    entries = []
    for row in rows:
        if row['cols'] < 3:
            continue
        ok = (not (row['natural'] or row['squeezed']) or not row['expanded'])
        if row['expanded']:
            ok = (ok and row['overflowing'] and row['maxColumn'] <= row['visible'] + 1
                  and row['lines'] < row['linesBefore'])
        if not row['overflowing']:
            ok = ok and row['scroll'] <= row['client'] + 1
        if 'expectedOverflow' in row:
            ok = ok and row['expanded'] == row['expectedOverflow']
        if row.get('synthetic'):
            ok = ok and row['expanded'] and row['maxContentWidth'] > 3 * row['client']
        entries.append({'ok': bool(ok), 'detail': f'{path} A23 {row}'})
    return entries


def a24_checks(path, rows):
    entries = []
    for row in rows:
        width, height = row.get('attrWidth'), row.get('attrHeight')
        ok = (bool(width and height) and row.get('loaded') and not row.get('complete')
              and abs(row['height'] - row['width'] * height / width) <= 1
              and row.get('anchorShift') is not None and abs(row['anchorShift']) <= 2)
        entries.append({'ok': bool(ok), 'detail': f'{path} A24 {row}'})
    return entries


def a26_checks(path, configs):
    """375px에서 넘치는 3칸 이상 표는 첫 열이 고정되고, 둘째 열부터 각 열의 글 폭이 남는 폭 안에 들어온다."""
    narrow = configs.get('narrow-light') or {}
    tables = narrow.get('tables') or []
    targets = [t for t in tables
               if bool(t.get('overflowing')) and (t.get('cols') or 0) >= 3]
    if not targets:
        return [{'ok': True, 'na': True,
                 'detail': f'{path}: 375px 넘치는 3칸 이상 표 0건 (A26 해당 없음)'}]
    entries = []
    for t in targets:
        sticky = bool(t.get('sticky'))
        need_widths = t.get('colNeedWidths') or []
        visible = t.get('visibleWidth')
        if visible is None:
            wrap_client = t.get('wrapClient') or 0
            first_w = t.get('firstCellWidth') or 0
            visible = round(wrap_client - (first_w if sticky else 0))
        headers = t.get('colHeaders') or []
        rest_needs = need_widths[1:]
        max_need = max(rest_needs) if rest_needs else 0
        over_cols = [
            f"{idx + 2}열({headers[idx + 1] if idx + 1 < len(headers) else ''}={w}px>{visible}px)"
            for idx, w in enumerate(rest_needs)
            if w > visible + 1
        ]
        ok = sticky and bool(rest_needs) and not over_cols
        entries.append({'ok': bool(ok),
                        'detail': f"{path} 375 table {t.get('i')} ({t.get('cols')}칸): "
                                  f"sticky={sticky} visible={visible}px maxNeed={max_need}px "
                                  f"colNeedWidths={need_widths} over={over_cols} headers={headers}"})
    return entries
