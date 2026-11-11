#!/usr/bin/env python3
"""서재 글 화면 시각 검수 스크립트 (폭·테마 캡처, A1~A13 측정, 각주 왕복, 창 크기 시나리오).

사용법:
  PLAYWRIGHT_BROWSERS_PATH="$HOME/.cache/ms-playwright" \
    python3 -P scripts/verify_article_ui.py <build_dir> <out_dir> \
      [--path /digest/roguelike-wikipedia/] [--path /digest/paradox-of-tragedy-three-aesthetics-papers/]

--path를 여러 번 주면 글마다 <out_dir>/<slug>/ 아래에 산출하고, <out_dir>/metrics.json에
전체 A1~A13 판정을 모은다. 분석 비콘(umami) 요청은 연결이 없는 환경에서 load 이벤트를
막으므로 차단한다. 화면과 무관하다.
"""
import argparse
import json
import re
import socket
import struct
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_article_ui_checks import (
    A10_CONFIGS, A10_JS, A11_JS, A9_JS, a9_checks, a10_checks, a11_checks, a12_checks,
    a13_checks, resized_sidenotes_ok, sidenote_presence_ok, summarize_checks,
)

CONFIGS = [
    ("wide-light", 1440, 900, 1, "light"),
    ("wide-dark", 1440, 900, 1, "dark"),
    ("mid-light", 1024, 800, 1, "light"),
    ("narrow-light", 375, 812, 2, "light"),
    ("narrow-dark", 375, 812, 2, "dark"),
    ("min360-light", 360, 740, 2, "light"),
    ("min390-light", 390, 844, 2, "light"),
    ("min414-light", 414, 896, 2, "light"),
]

DEFAULT_PATHS = [
    "/digest/roguelike-wikipedia/",
    "/digest/memory-caching-rnns/",
    "/digest/pixellab-ai-pixel-art-generator/",
    "/digest/compozy-agent-os/",
    "/digest/skillopt-text-space-optimizer-2026/",
    "/digest/oist-quantum-spins-centimeter-object/",
    "/digest/combining-llms-cofailure-ceiling/",
    "/digest/qwenputer-riscv-cpu/",
    "/digest/it3-periodic-table-z172/",
    "/digest/ai-agents-unmapped-maya-site/",
    "/gallery/seosoyoung-russian-avant-garde-poster/",
]

MATH_PATHS = [
    "/digest/memory-caching-rnns/",
    "/digest/skillopt-text-space-optimizer-2026/",
    "/digest/oist-quantum-spins-centimeter-object/",
    "/digest/combining-llms-cofailure-ceiling/",
    "/digest/qwenputer-riscv-cpu/",
    "/digest/it3-periodic-table-z172/",
]

RESIZE_SCENARIOS = [
    ("1440-1100-600-1440", [1440, 1100, 600, 1440]),
    ("1440-375-1440", [1440, 375, 1440]),
    ("340-375", [340, 375]),
]

TOC_GAP = 32
TOC_GAP_TOL = 1
MIN_TABLE_COLS = 3
MAX_SQUEEZE_TEST_COLS = 5
SHORT_CELL_WIDTH_LIMIT = 100

MEASURE_JS = r"""
() => {
  const r = (el) => { if (!el) return null; const b = el.getBoundingClientRect();
    return {x: +b.left.toFixed(1), y: +(b.top + scrollY).toFixed(1), w: +b.width.toFixed(1), h: +b.height.toFixed(1), right: +b.right.toFixed(1)}; };
  const parseRGB = (s) => { const m = s.match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return {r:p[0], g:p[1], b:p[2], a: p.length > 3 ? p[3] : 1}; };
  const lum = (c) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
  const blend = (fg, bg) => ({r: fg.r * fg.a + bg.r * (1 - fg.a), g: fg.g * fg.a + bg.g * (1 - fg.a), b: fg.b * fg.a + bg.b * (1 - fg.a), a: 1});
  const ratio = (a, b) => { const la = lum(a), lb = lum(b); return +((Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05)).toFixed(2); };
  const bgOf = (el) => { let layers = []; let e = el;
    while (e && e.nodeType === 1) { const c = parseRGB(getComputedStyle(e).backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; } e = e.parentElement; }
    let base = {r: 255, g: 255, b: 255, a: 1}; if (!layers.length || layers[layers.length - 1].a < 1) base = parseRGB(getComputedStyle(document.documentElement).backgroundColor) || base;
    for (let i = layers.length - 1; i >= 0; i--) base = blend(layers[i], base); return base; };
  const textInfo = (el, label) => { if (!el) return {label, missing: true}; const cs = getComputedStyle(el); const fg = parseRGB(cs.color); const bg = bgOf(el);
    return {label, fontSize: cs.fontSize, fontWeight: cs.fontWeight, lineHeight: cs.lineHeight, family: cs.fontFamily.split(',')[0], color: cs.color, contrast: ratio(blend(fg, bg), bg)}; };

  const content = document.querySelector('.post-content');
  const out = {};
  out.viewport = {w: innerWidth, h: innerHeight};
  out.theme = document.documentElement.dataset.theme || '(none)';
  out.docScrollWidth = document.documentElement.scrollWidth;
  out.bodyScrollWidth = document.body.scrollWidth;
  out.horizontalOverflow = document.documentElement.scrollWidth > innerWidth;
  out.content = r(content);

  const toc = document.querySelector('.toc');
  const first = content ? content.firstElementChild : null;
  out.tocGap = (toc && first) ? +(first.getBoundingClientRect().top - toc.getBoundingClientRect().bottom).toFixed(1) : null;
  out.tocOpen = toc ? toc.hasAttribute('open') : null;
  out.firstContent = {tag: first ? first.tagName : null, className: first ? String(first.className || '') : null, rect: r(first)};

  const wide = [];
  content.querySelectorAll('*').forEach((el) => { const b = el.getBoundingClientRect(); if (b.width === 0) return;
    if (el.closest('.table-scroll') && !el.classList.contains('table-scroll')) return;
    if (b.right > innerWidth + 0.5 || b.left < -0.5) wide.push({tag: el.tagName, cls: el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className, left: b.left, right: b.right}); });
  out.elementsBeyondViewport = wide.slice(0, 20);

  const cover = document.querySelector('.entry-cover img');
  out.cover = cover ? {complete: cover.complete, natural: [cover.naturalWidth, cover.naturalHeight], rect: r(cover), alt: cover.getAttribute('alt')} : null;
  out.header = {title: r(document.querySelector('.post-title')), lead: r(document.querySelector('.post-lead')), meta: r(document.querySelector('.post-meta')), cover: r(document.querySelector('.entry-cover'))};

  out.images = [...content.querySelectorAll('img')].map((img) => {
    const p = img.closest('p'); let cap = p ? p.nextElementSibling : null; let capInP = false;
    const emSame = p ? p.querySelector('em') : null; if (emSame) { cap = emSame; capInP = true; }
    const capRect = cap ? r(cap) : null; const ir = r(img);
    return {src: img.src.split('/').pop(), complete: img.complete, natural: [img.naturalWidth, img.naturalHeight], alt: img.getAttribute('alt'), rect: ir,
      parentTag: img.parentElement.tagName, captionTag: cap ? cap.tagName : null, captionInSameP: capInP,
      captionText: cap ? cap.textContent.slice(0, 40) : null, captionRect: capRect,
      captionAlign: cap ? getComputedStyle(cap).textAlign : null,
      captionFont: cap ? getComputedStyle(cap).fontSize : null,
      gapImgToCaption: capRect && ir ? +(capRect.y - (ir.y + ir.h)).toFixed(1) : null,
      leftDiff: capRect && ir ? +(capRect.x - ir.x).toFixed(1) : null,
      contentLeftDiff: ir ? +(ir.x - r(content).x).toFixed(1) : null,
      contentRightDiff: ir ? +(r(content).right - ir.right).toFixed(1) : null};
  });

  const probe = document.createElement('span');
  probe.style.color = 'var(--rule)';
  document.body.appendChild(probe);
  out.ruleColor = getComputedStyle(probe).color;
  probe.remove();

  // 같은 flex/grid 줄에 놓인 이미지를 묶으려고 가장 가까운 격자 조상을 행 키로 준다.
  const rowHosts = new Map();
  const rowKeyOf = (img) => {
    let e = img.parentElement;
    while (e && e !== content) {
      const d = getComputedStyle(e).display;
      if (d === 'flex' || d === 'inline-flex' || d === 'grid' || d === 'inline-grid') {
        if (!rowHosts.has(e)) rowHosts.set(e, rowHosts.size);
        return rowHosts.get(e);
      }
      e = e.parentElement;
    }
    return null;
  };
  out.postImages = [...content.querySelectorAll('img')]
    .filter((img) => img.getBoundingClientRect().width > 0)
    .map((img) => {
      const b = img.getBoundingClientRect();
      const cs = getComputedStyle(img);
      return {src: img.src.split('/').pop(), x: +b.left.toFixed(1), y: +(b.top + scrollY).toFixed(1),
        w: +b.width.toFixed(1), h: +b.height.toFixed(1), boxShadow: cs.boxShadow,
        borderWidths: [parseFloat(cs.borderTopWidth), parseFloat(cs.borderRightWidth),
          parseFloat(cs.borderBottomWidth), parseFloat(cs.borderLeftWidth)],
        borderColors: [cs.borderTopColor, cs.borderRightColor, cs.borderBottomColor, cs.borderLeftColor],
        outline: {width: parseFloat(cs.outlineWidth), style: cs.outlineStyle,
          color: cs.outlineColor, offset: parseFloat(cs.outlineOffset)},
        rowKey: rowKeyOf(img)};
    });

  const fig = content.querySelector('figure.blog-diagram');
  if (fig) {
    const svgs = [...fig.querySelectorAll('svg')];
    out.diagram = {figure: r(fig), childTags: [...fig.children].map((c) => c.tagName + (c.className && c.className.baseVal ? '.' + c.className.baseVal : '')),
      pInsideFigure: fig.querySelectorAll('p').length, brInsideFigure: fig.querySelectorAll('br').length,
      parentTag: fig.parentElement.tagName, prevTag: fig.previousElementSibling && fig.previousElementSibling.tagName,
      strayPAround: [fig.previousElementSibling, fig.nextElementSibling].filter((e) => e && e.tagName === 'P' && !e.textContent.trim()).length,
      figcaption: textInfo(fig.querySelector('figcaption'), 'figcaption'), figcaptionRect: r(fig.querySelector('figcaption')), svgs: []};
    svgs.forEach((svg) => {
      const cs = getComputedStyle(svg); const vb = svg.viewBox.baseVal; const rect = svg.getBoundingClientRect();
      const scale = rect.width / (vb.width || 1);
      const info = {cls: svg.className.baseVal, display: cs.display, rect: r(svg), viewBox: [vb.width, vb.height], scale: +scale.toFixed(3),
        dashedCount: svg.querySelectorAll('line[stroke-dasharray], path[stroke-dasharray]').length, texts: []};
      if (cs.display !== 'none') {
        const rects = [...svg.querySelectorAll('rect')].filter((x) => x.getAttribute('x') !== null).map((x) => ({x: +x.getAttribute('x'), y: +x.getAttribute('y'), w: +x.getAttribute('width'), h: +x.getAttribute('height')}));
        svg.querySelectorAll('text').forEach((t) => {
          const bb = t.getBBox(); const tx = +t.getAttribute('x'), ty = +t.getAttribute('y');
          const box = rects.filter((b) => tx >= b.x && tx <= b.x + b.w && ty >= b.y && ty <= b.y + b.h).sort((a, b) => a.w * a.h - b.w * b.h)[0];
          const tcs = getComputedStyle(t);
          info.texts.push({text: t.textContent, fontPx: +(parseFloat(t.getAttribute('font-size')) * scale).toFixed(2),
            fill: tcs.fill, family: tcs.fontFamily.split(',')[0],
            bbox: [+bb.x.toFixed(1), +bb.y.toFixed(1), +bb.width.toFixed(1), +bb.height.toFixed(1)],
            box: box || null,
            rightPad: box ? +((box.x + box.w) - (bb.x + bb.width)).toFixed(1) : null,
            leftPad: box ? +(bb.x - box.x).toFixed(1) : null,
            topPad: box ? +(bb.y - box.y).toFixed(1) : null,
            bottomPad: box ? +((box.y + box.h) - (bb.y + bb.height)).toFixed(1) : null});
        });
        info.svgBg = getComputedStyle(svg).backgroundColor;
      }
      out.diagram.svgs.push(info);
    });
  }

  out.tables = [...content.querySelectorAll('table')].map((t, i) => {
    const wrap = t.closest('.table-scroll');
    const th = t.querySelector('thead th');
    const td = t.querySelector('tbody td');
    const rows = [...t.querySelectorAll('tr')];
    let cols = 0;
    rows.forEach((row) => { let count = 0; [...row.children].forEach((cell) => { count += cell.colSpan || 1; }); if (count > cols) cols = count; });
    const overflowBefore = wrap ? wrap.classList.contains('is-overflowing') : null;
    const style = getComputedStyle(t);
    if (wrap) wrap.classList.remove('is-overflowing');
    const oldWidth = t.style.getPropertyValue('width');
    const oldPriority = t.style.getPropertyPriority('width');
    t.style.setProperty('width', 'max-content');
    const maxContentWidth = +t.getBoundingClientRect().width.toFixed(1);
    if (oldWidth) t.style.setProperty('width', oldWidth, oldPriority); else t.style.removeProperty('width');
    if (wrap && overflowBefore) wrap.classList.add('is-overflowing');

    const firstBodyCell = t.querySelector('tbody td') || t.querySelector('td');
    const firstCellStyle = firstBodyCell ? getComputedStyle(firstBodyCell) : null;
    const codeMetrics = [...t.querySelectorAll('td code, th code')].map((c) => {
      const cs = getComputedStyle(c);
      const lineHeight = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.4;
      const b = c.getBoundingClientRect();
      return {text: c.textContent.trim().slice(0, 48), lines: lineHeight > 0 ? +(b.height / lineHeight).toFixed(2) : null};
    });
    const colWidths = [...t.querySelectorAll('tbody tr:first-child td')].map((c) => Math.round(c.getBoundingClientRect().width));
    const maxLinesPerCell = Math.max(...[...t.querySelectorAll('td')].map((c) => Math.round((c.getBoundingClientRect().height - 16) / parseFloat(getComputedStyle(c).lineHeight))));
    return {i: i + 1, cols, headerCols: t.querySelectorAll('thead th').length, rows: rows.length,
      wrapper: wrap ? wrap.className : null, wrapClient: wrap ? wrap.clientWidth : null, wrapScroll: wrap ? wrap.scrollWidth : null,
      wrapping: wrap ? wrap.classList.contains('is-overflowing') : null, overflowing: overflowBefore,
      wrapDelta: wrap ? wrap.scrollWidth - wrap.clientWidth : null,
      tableRect: r(t), wrapRect: r(wrap), th: textInfo(th, 'th'), td: textInfo(td, 'td'),
      colWidths, maxLinesPerCell,
      firstColWidths: [...t.querySelectorAll('tbody tr td:first-child')].slice(0, 3).map((c) => +c.getBoundingClientRect().width.toFixed(1)),
      maxCellHeight: Math.max(...[...t.querySelectorAll('td')].map((c) => c.getBoundingClientRect().height)),
      maxContentWidth, fontSize: parseFloat(style.fontSize),
      firstCellMinWidth: firstCellStyle ? firstCellStyle.minWidth : null,
      firstCellWidth: firstBodyCell ? +firstBodyCell.getBoundingClientRect().width.toFixed(1) : null,
      firstCellText: firstBodyCell ? firstBodyCell.textContent.trim().slice(0, 24) : null,
      hasInlineCode: codeMetrics.length > 0, codeMetrics};
  });

  const markers = [...content.querySelectorAll('sup[id^="fnref"], a.footnote-ref')].filter((m) => m.tagName === 'SUP' || !m.closest('sup'));
  const normalizeKey = (value) => {
    let key = String(value || '').trim();
    if (key.charAt(0) === '#') key = key.slice(1);
    try { key = decodeURIComponent(key); } catch (error) {}
    return key.replace(/^fnref[:\-]/, '').replace(/^fn[:\-]/, '');
  };
  const markerKey = (marker) => {
    const link = marker.matches('a[href^="#fn"]') ? marker : marker.querySelector('a[href^="#fn"]');
    return (link && normalizeKey(link.getAttribute('href'))) || normalizeKey(marker.id);
  };
  const markerByKey = {};
  markers.forEach((marker) => { const key = markerKey(marker); if (key && !(key in markerByKey)) markerByKey[key] = marker; });

  const notes = [...document.querySelectorAll('aside.sidenote')];
  out.footnoteMarkers = markers.length;
  out.footnotesSection = (() => { const f = document.querySelector('.footnotes'); if (!f) return null; const cs = getComputedStyle(f);
    return {display: cs.display, visibility: cs.visibility, rect: r(f), items: f.querySelectorAll('li').length, text: textInfo(f.querySelector('li p') || f.querySelector('li'), 'footnote li')}; })();
  out.sidenotes = notes.map((n, i) => {
    const num = n.querySelector('.sidenote-num');
    const key = n.dataset.footnoteKey || '';
    const marker = markerByKey[key] || markers[i];
    const markerLink = marker ? (marker.matches('a') ? marker : marker.querySelector('a[href^="#fn"]')) : null;
    const nr = r(n);
    const text = n.textContent.trim();
    const numText = num ? num.textContent.trim() : null;
    return {i: i + 1, rect: nr, markerY: marker ? r(marker).y : null,
      offsetFromMarker: marker ? +(nr.y - r(marker).y).toFixed(1) : null,
      gapFromContent: +(nr.x - r(content).right).toFixed(1), beyondViewport: nr.right > innerWidth, text: textInfo(n, 'sidenote'),
      numberText: numText,
      numberIsFirst: !!num && (n.firstElementChild === num || (n.firstElementChild && n.firstElementChild.firstElementChild === num)),
      startsWithNumber: !!numText && text.startsWith(numText),
      markerText: markerLink ? markerLink.textContent.trim() : (marker ? marker.textContent.trim() : null)};
  });
  out.sidenoteOverlaps = [];
  for (let i = 1; i < notes.length; i++) { const a = notes[i - 1].getBoundingClientRect(), b = notes[i].getBoundingClientRect();
    out.sidenoteOverlaps.push(+(b.top - a.bottom).toFixed(1)); }

  const bodyP = [...content.querySelectorAll(':scope > p')].find((p) => p.textContent.length > 100);
  out.textSamples = [textInfo(bodyP, 'body p'), textInfo(content.querySelector('h2'), 'h2'),
    textInfo(content.querySelector('p > em'), 'caption em'), textInfo(content.querySelector('code'), 'inline code'),
    textInfo(document.querySelector('.post-meta'), 'post-meta'), textInfo(content.querySelector('ol li'), 'summary li')];
  out.bodyPWidth = bodyP ? r(bodyP).w : null;
  return out;
}
"""

GRID_IMAGES_JS = r"""
() => {
  const content = document.querySelector('.post-content');
  if (!content) return [];
  const isRowHost = (el) => {
    const d = getComputedStyle(el).display;
    return d === 'flex' || d === 'inline-flex' || d === 'grid' || d === 'inline-grid';
  };
  return [...content.querySelectorAll('img')].filter((img) => {
    if (img.getBoundingClientRect().width <= 0) return false;
    let e = img.parentElement;
    while (e && e !== content) {
      if (isRowHost(e)) return true;
      e = e.parentElement;
    }
    return false;
  }).map((img) => {
    const b = img.getBoundingClientRect();
    return {src: img.src.split('/').pop(), x: +(b.left + scrollX).toFixed(1),
      y: +(b.top + scrollY).toFixed(1), w: +b.width.toFixed(1), h: +b.height.toFixed(1)};
  });
}
"""

STATE_JS = r"""
() => {
  const tables = [...document.querySelectorAll('.post-content .table-scroll')].map((wrap, i) => {
    const table = wrap.querySelector('table');
    const was = wrap.classList.contains('is-overflowing');
    wrap.classList.remove('is-overflowing');
    const rows = [...table.querySelectorAll('tr')];
    let cols = 0;
    rows.forEach((row) => { let count = 0; [...row.children].forEach((cell) => { count += cell.colSpan || 1; }); if (count > cols) cols = count; });
    const natural = wrap.scrollWidth > wrap.clientWidth + 1 || table.scrollWidth > wrap.clientWidth + 1;
    const fontSize = parseFloat(getComputedStyle(table).fontSize);
    let squeezed = false;
    if (!natural && cols >= 3 && cols <= 5 && wrap.clientWidth / cols < fontSize * 8) {
      const oldWidth = table.style.getPropertyValue('width');
      const oldPriority = table.style.getPropertyPriority('width');
      table.style.setProperty('width', 'max-content');
      const maxContent = table.getBoundingClientRect().width;
      if (oldWidth) table.style.setProperty('width', oldWidth, oldPriority); else table.style.removeProperty('width');
      squeezed = maxContent > wrap.clientWidth + 1;
    }
    wrap.classList.toggle('is-overflowing', was);
    return {index: i + 1, cols, isOverflowing: was, expected: natural || squeezed,
      natural, squeezed, wrapClient: wrap.clientWidth, wrapScroll: wrap.scrollWidth,
      tableWidth: +table.getBoundingClientRect().width.toFixed(1),
      tableHeight: +table.getBoundingClientRect().height.toFixed(1)};
  });
  const sidenotes = [...document.querySelectorAll('aside.sidenote')].map((n, i) => ({
    index: i + 1,
    numberText: (n.querySelector('.sidenote-num') || {}).textContent
      ? n.querySelector('.sidenote-num').textContent.trim() : null,
  }));
  const footnotes = document.querySelector('.footnotes');
  const content = document.querySelector('.post-content');
  const toc = document.querySelector('.toc');
  const first = content ? content.firstElementChild : null;
  return {width: innerWidth, tables, sidenoteCount: sidenotes.length,
    numberedSidenotes: sidenotes.filter((n) => n.numberText).length,
    sidenotes,
    footnotesDisplay: footnotes ? getComputedStyle(footnotes).display : null,
    horizontalOverflow: document.documentElement.scrollWidth > innerWidth,
    tocGap: (toc && first) ? +(first.getBoundingClientRect().top - toc.getBoundingClientRect().bottom).toFixed(1) : null};
}
"""

OVERFLOW_JS = r"""
() => [...document.querySelectorAll('.post-content .table-scroll')].map((w, i) => {
  const t = w.querySelector('table');
  return {index: i + 1, overflowing: w.classList.contains('is-overflowing'),
    tableWidth: +t.getBoundingClientRect().width.toFixed(1)};
})
"""

ACTIVE_JS = r"""
() => {
  const a = document.activeElement;
  if (!a) return {tag: null};
  const b = a.getBoundingClientRect();
  const num = a.querySelector ? a.querySelector('.sidenote-num') : null;
  return {tag: a.tagName, id: a.id, className: String(a.className || ''),
    isSidenote: a.matches('aside.sidenote'), sidenoteNumber: num ? num.textContent.trim() : null,
    top: +b.top.toFixed(1), inViewport: b.top >= -1 && b.bottom <= innerHeight + 1,
    hash: location.hash};
}
"""

BACKREF_JS = r"""
() => {
  const marker = document.querySelector('.post-content sup[id^="fnref"]');
  const a = document.activeElement;
  const b = marker ? marker.getBoundingClientRect() : null;
  return {activeTag: a ? a.tagName : null, activeId: a ? a.id : null,
    markerTop: b ? +b.top.toFixed(1) : null,
    markerInViewport: b ? (b.top >= -1 && b.bottom <= innerHeight + 1) : null,
    hash: location.hash};
}
"""


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def settle(page):
    h = page.evaluate("document.documentElement.scrollHeight")
    y = 0
    while y < h:
        page.evaluate(f"window.scrollTo(0, {y})")
        page.wait_for_timeout(40)
        y += 1400
        h = page.evaluate("document.documentElement.scrollHeight")
    page.wait_for_load_state("networkidle")
    page.evaluate("Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))")
    page.evaluate("document.fonts.ready")
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1000)


def element_shot(page, selector, path, nth=0):
    page.locator(selector).nth(nth).screenshot(path=str(path))
    return str(path)


def wait_for_sidenote_settle(page):
    # full-page 캡처가 일으킨 reflow 뒤 sidenote.js가 노드를 다시 그린다(120ms 디바운스).
    # 다음 요소 캡처가 분리된 노드를 잡지 않게 재배치가 끝날 때까지 기다린다.
    if page.locator("aside.sidenote").count():
        page.wait_for_timeout(400)


def padded_element_shot(page, selector, path, nth=0, pad=8):
    # 본문 폭을 꽉 채운 이미지는 요소 캡처 경계에서 box-shadow 1px 선이 잘린다.
    # 요소 상자를 사방 pad만큼 넓혀 찍고 페이지 범위로 자른다.
    page.locator(selector).nth(nth).scroll_into_view_if_needed()
    box = page.evaluate(
        """([s, n]) => {
          const el = document.querySelectorAll(s)[n];
          const b = el.getBoundingClientRect();
          return {x: b.left + scrollX, y: b.top + scrollY, w: b.width, h: b.height,
                  docW: document.documentElement.scrollWidth,
                  docH: document.documentElement.scrollHeight};
        }""",
        [selector, nth],
    )
    x = max(0.0, box["x"] - pad)
    y = max(0.0, box["y"] - pad)
    width = min(box["docW"], box["x"] + box["w"] + pad) - x
    height = min(box["docH"], box["y"] + box["h"] + pad) - y
    # clip은 페이지 좌표라 full_page와 함께 줘야 뷰포트 밖 영역까지 찍힌다.
    page.screenshot(path=str(path), full_page=True,
                    clip={"x": x, "y": y, "width": width, "height": height})
    wait_for_sidenote_settle(page)
    return str(path)


def padded_box_shot(page, box, path, pad=8):
    # 격자(flex/grid) 안 이미지는 페이지 좌표 상자로 받아 사방 pad만큼 넓혀 찍는다.
    doc = page.evaluate(
        "() => ({w: document.documentElement.scrollWidth, h: document.documentElement.scrollHeight})"
    )
    x = max(0.0, box["x"] - pad)
    y = max(0.0, box["y"] - pad)
    width = min(doc["w"], box["x"] + box["w"] + pad) - x
    height = min(doc["h"], box["y"] + box["h"] + pad) - y
    page.screenshot(path=str(path), full_page=True,
                    clip={"x": x, "y": y, "width": width, "height": height})
    wait_for_sidenote_settle(page)
    return str(path)


def png_size(path):
    with open(path, "rb") as handle:
        head = handle.read(24)
    return list(struct.unpack(">II", head[16:24]))


def table_state(page, index):
    return page.evaluate(
        """(n) => {
          const wrapper = document.querySelectorAll('.post-content .table-scroll')[n];
          const table = wrapper.querySelector('table');
          const rect = table.getBoundingClientRect();
          return {overflowing: wrapper.classList.contains('is-overflowing'),
                  width: +rect.width.toFixed(1), height: +rect.height.toFixed(1)};
        }""",
        index,
    )


def apply_table_state(page, tables):
    # 요소 캡처가 일으키는 resize가 overflow 판정을 바꿀 수 있다.
    # 캡처 직전에는 측정 시점의 표 상태로 되돌려, 캡처와 metrics를 같은 상태로 맞춘다.
    page.evaluate(
        """(states) => {
          document.querySelectorAll('.post-content .table-scroll').forEach((wrapper, i) => {
            const want = !!(states[i] && states[i].overflowing);
            wrapper.classList.toggle('is-overflowing', want);
          });
        }""",
        [{"overflowing": table["overflowing"]} for table in tables if table["wrapper"]],
    )


def viewport_shot(page, selector, path, nth=0):
    loc = page.locator(selector).nth(nth)
    loc.scroll_into_view_if_needed()
    page.evaluate(
        "([s, n]) => { const e = document.querySelectorAll(s)[n]; window.scrollTo(0, e.getBoundingClientRect().top + scrollY - 16); }",
        [selector, nth],
    )
    page.wait_for_timeout(200)
    page.screenshot(path=str(path))


def open_context(browser, width, height, dpr, scheme):
    ctx = browser.new_context(
        viewport={"width": width, "height": height},
        device_scale_factor=dpr,
        color_scheme=scheme,
        is_mobile=(width < 500),
        has_touch=(width < 500),
        reduced_motion="reduce",
    )
    # 분석 비콘은 연결 없는 환경에서 load 이벤트를 막는다. 화면과 무관하다.
    ctx.route("https://umami.eiaserinnys.me/**", lambda route: route.abort())
    return ctx


def footnote_roundtrip(page, name, out_dir):
    inter = {}
    page.evaluate("window.scrollTo(0, 0)")
    refs = page.locator(".post-content a.footnote-ref")
    if refs.count() == 0:
        return {"applicable": False, "reason": "본문에 각주 링크가 없다"}
    ref = refs.first
    ref.scroll_into_view_if_needed()
    ref.click()
    page.wait_for_timeout(1600)
    inter["afterRefClick"] = page.evaluate(ACTIVE_JS)
    page.screenshot(path=str(out_dir / "after-ref-click.png"))
    if name == "narrow-light":
        back = page.locator(".footnotes a.footnote-backref").first
        if back.count() and back.is_visible():
            back.click()
            page.wait_for_timeout(1600)
            inter["afterBackref"] = page.evaluate(BACKREF_JS)
            page.screenshot(path=str(out_dir / "after-backref.png"))
        else:
            inter["afterBackref"] = "backref not visible"
    return inter


def capture_config(browser, url, out_dir, name, width, height, dpr, scheme, a10=False):
    ctx = open_context(browser, width, height, dpr, scheme)
    page = ctx.new_page()
    failed = []
    page.on("requestfailed", lambda req: failed.append(req.url))
    page.on("response", lambda res: failed.append(f"{res.status} {res.url}") if res.status >= 400 else None)
    page.goto(url, wait_until="load", timeout=60000)
    settle(page)
    m = page.evaluate(MEASURE_JS)
    m["failedRequests"] = failed
    m["a9"] = page.evaluate(A9_JS)
    if a10:
        m["a10"] = page.evaluate(A10_JS, name == "wide-light")
        m["a11"] = page.evaluate(A11_JS, name == "wide-light")
    d = out_dir / name
    d.mkdir(parents=True, exist_ok=True)
    page.add_style_tag(content=".site-top{position:static!important} html{scroll-behavior:auto!important}")
    shots = {}
    if page.locator("figure.blog-diagram").count() > 0:
        if width < 500:
            viewport_shot(page, "figure.blog-diagram", d / "diagram.png")
            shots["diagram"] = str(d / "diagram.png")
        else:
            shots["diagram"] = element_shot(page, "figure.blog-diagram", d / "diagram.png")
    t_count = page.locator(".post-content .table-scroll").count()
    capture_states = []
    for i in range(t_count):
        apply_table_state(page, m["tables"])
        state_before = table_state(page, i)
        shot_path = d / f"table{i+1}.png"
        shots[f"table{i+1}"] = element_shot(page, ".post-content .table-scroll", shot_path, nth=i)
        state_after = table_state(page, i)
        capture_states.append({"i": i + 1, "before": state_before, "after": state_after,
                               "png": png_size(shot_path)})
    m["tableCaptureStates"] = capture_states
    img_count = page.locator(".post-content p:has(> img)").count()
    for i in range(img_count):
        shots[f"image{i+2}"] = padded_element_shot(page, ".post-content p:has(> img)", d / f"image{i+2:02d}.png", nth=i)
    if name in ("wide-light", "narrow-light"):
        for i, box in enumerate(page.evaluate(GRID_IMAGES_JS)):
            shots[f"grid-image{i+1}"] = padded_box_shot(page, box, d / f"grid-image{i+1:02d}.png")
    if m["sidenotes"]:
        for s in m["sidenotes"]:
            shots[f"sidenote{s['i']}"] = element_shot(page, "aside.sidenote", d / f"sidenote{s['i']}.png", nth=s["i"] - 1)
    elif page.locator(".footnotes").count() > 0:
        shots["footnotes"] = element_shot(page, ".footnotes", d / "footnotes.png")
    if name in ("narrow-light", "wide-light"):
        m["interaction"] = footnote_roundtrip(page, name, d)
    apply_table_state(page, m["tables"])
    m["overflowBeforeFullPage"] = page.evaluate(OVERFLOW_JS)
    page.evaluate("window.scrollTo(0, 0)")
    page.screenshot(path=str(d / "full.png"), full_page=True)
    m["overflowAfterFullPage"] = page.evaluate(OVERFLOW_JS)
    m["overflowStableAcrossFullPage"] = m["overflowBeforeFullPage"] == m["overflowAfterFullPage"]
    page.evaluate("window.scrollTo(0, 0)")
    page.screenshot(path=str(d / "first-screen.png"))
    m["shots"] = shots
    ctx.close()
    return m


def capture_tables_375(browser, url, out_dir):
    d = out_dir / "tables-375"
    d.mkdir(parents=True, exist_ok=True)
    ctx = open_context(browser, 375, 4800, 1, "light")
    page = ctx.new_page()
    page.goto(url, wait_until="load", timeout=60000)
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(1200)
    page.add_style_tag(content=".site-top{position:static!important} html{scroll-behavior:auto!important}")
    info = {}
    t_count = page.locator(".post-content .table-scroll").count()
    for i in range(t_count):
        el = page.locator(".post-content .table-scroll").nth(i)
        el.screenshot(path=str(d / f"375-table{i+1}.png"))
        info[f"table{i+1}"] = page.evaluate(
            """(index) => {
              const w = document.querySelectorAll('.post-content .table-scroll')[index];
              const t = w.querySelector('table');
              const rows = [...t.querySelectorAll('tr')];
              let cols = 0;
              rows.forEach((row) => { let count = 0; [...row.children].forEach((cell) => { count += cell.colSpan || 1; }); if (count > cols) cols = count; });
              return {height: Math.round(t.getBoundingClientRect().height),
                overflowing: w.classList.contains('is-overflowing'), wrapClient: w.clientWidth, wrapScroll: w.scrollWidth,
                cols, colWidths: [...t.querySelectorAll('tbody tr:first-child td')].map(c => Math.round(c.getBoundingClientRect().width)),
                maxLinesPerCell: Math.max(...[...t.querySelectorAll('td')].map(c => Math.round((c.getBoundingClientRect().height - 16) / parseFloat(getComputedStyle(c).lineHeight)))),
                codeLines: [...t.querySelectorAll('td code')].map(c => {
                  const cs = getComputedStyle(c); const lh = parseFloat(cs.lineHeight) || parseFloat(cs.fontSize) * 1.4;
                  return {text: c.textContent.trim().slice(0, 48), lines: lh > 0 ? +(c.getBoundingClientRect().height / lh).toFixed(2) : null};
                })};
            }""",
            i,
        )
    ctx.close()
    (d / "tables-375.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
    return info


def run_resize_scenarios(browser, url, out_dir):
    results = {}
    for scenario, widths in RESIZE_SCENARIOS:
        first_width = widths[0]
        ctx = open_context(browser, first_width, 900 if first_width >= 600 else 812, 1, "light")
        page = ctx.new_page()
        page.goto(url, wait_until="load", timeout=60000)
        settle(page)
        stages = []
        for stage_index, width in enumerate(widths):
            if page.viewport_size["width"] != width:
                page.set_viewport_size({"width": width, "height": 900 if width >= 600 else 812})
            page.wait_for_timeout(900)
            state = page.evaluate(STATE_JS)
            state["stageWidth"] = width
            page.screenshot(path=str(out_dir / f"resize-{scenario}-{stage_index}-{width}.png"))
            stages.append(state)
        ctx.close()
        results[scenario] = {"widths": widths, "stages": stages}
    return results


def short_first_cell(text):
    value = (text or "").strip()
    return len(value) <= 6 or bool(re.fullmatch(r"\d{4}", value))


def path_checks(report):
    checks = {key: [] for key in ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13")}

    def add(key, ok, detail, na=False):
        checks[key].append({"ok": bool(ok), "na": na, "detail": detail})

    configs = report["configs"]
    path = report["path"]

    for name in ("min360-light", "narrow-light", "min414-light", "wide-light"):
        metric = configs[name]
        if metric["tocGap"] is not None:
            add("A1", abs(metric["tocGap"] - TOC_GAP) <= TOC_GAP_TOL,
                f"{path} {name}: tocGap={metric['tocGap']}px (기준 {TOC_GAP}px)")

    for name in ("min360-light", "narrow-light", "min390-light", "min414-light"):
        for table in configs[name]["tables"]:
            if MIN_TABLE_COLS <= table["cols"] <= MAX_SQUEEZE_TEST_COLS:
                ok = table["overflowing"] or (table["maxContentWidth"] <= table["wrapClient"] + 1)
                add("A2", ok,
                    f"{path} {name} table {table['i']} ({table['cols']}칸): "
                    f"overflowing={table['overflowing']} maxContent={table['maxContentWidth']}px "
                    f"wrap={table['wrapClient']}px width={table['tableRect']['w']}px height={table['tableRect']['h']}px")

    for name in ("narrow-light", "wide-light"):
        for table in configs[name]["tables"]:
            if table["cols"] != 4:
                continue
            min_width = table["firstCellMinWidth"]
            add("A3", min_width in ("auto", "0px", "0"),
                f"{path} {name} table {table['i']} (4칸): minWidth={min_width} "
                f"width={table['firstCellWidth']}px text={table['firstCellText']!r}")
            if short_first_cell(table["firstCellText"]):
                add("A3", table["firstCellWidth"] is not None and table["firstCellWidth"] <= SHORT_CELL_WIDTH_LIMIT,
                    f"{path} {name} table {table['i']} (4칸, 짧은 첫 칸): "
                    f"width={table['firstCellWidth']}px (기준 <= {SHORT_CELL_WIDTH_LIMIT}px)")

    wide = configs["wide-light"]
    mid = configs["mid-light"]
    for note in wide["sidenotes"]:
        add("A4", note["numberText"] is not None and note["numberIsFirst"]
            and note["startsWithNumber"] and note["numberText"] == note["markerText"],
            f"{path} sidenote {note['i']}: num={note['numberText']!r} marker={note['markerText']!r} "
            f"first={note['numberIsFirst']} startsWith={note['startsWithNumber']}")
    add("A4", sidenote_presence_ok(wide), f"{path} 1440: markers={wide['footnoteMarkers']} sidenote={len(wide['sidenotes'])}")
    add("A4", len(mid["sidenotes"]) == 0 and (mid["footnotesSection"] is None or mid["footnotesSection"]["display"] != "none"),
        f"{path} 1024: sidenote={len(mid['sidenotes'])} "
        f"footnotesDisplay={(mid['footnotesSection'] or {}).get('display')}")

    for scenario, data in report["resize"].items():
        for stage in data["stages"]:
            for table in stage["tables"]:
                add("A5", table["isOverflowing"] == table["expected"],
                    f"{path} {scenario}@{stage['stageWidth']} table {table['index']} ({table['cols']}칸): "
                    f"is-overflowing={table['isOverflowing']} expected={table['expected']} "
                    f"width={table['tableWidth']}px")
        final = data["stages"][-1]
        if final["stageWidth"] == 1440:
            add("A5", resized_sidenotes_ok(final, wide),
                f"{path} {scenario} 1440 복귀: sidenote={final['sidenoteCount']} 번호={final['numberedSidenotes']}")
            fresh = {t["i"]: t for t in wide["tables"]}
            for table in final["tables"]:
                reference = fresh.get(table["index"])
                if reference:
                    add("A5", table["isOverflowing"] == reference["overflowing"],
                        f"{path} {scenario} 1440 복귀 table {table['index']}: "
                        f"is-overflowing={table['isOverflowing']} 새로 연 1440={reference['overflowing']}")

    add("A6", configs["min360-light"]["docScrollWidth"] <= configs["min360-light"]["viewport"]["w"],
        f"{path} 360: scrollWidth={configs['min360-light']['docScrollWidth']} "
        f"innerWidth={configs['min360-light']['viewport']['w']}")

    for name in ("narrow-light", "wide-light"):
        for table in configs[name]["tables"]:
            if table["cols"] < 6:
                continue
            natural = table["maxContentWidth"] > table["wrapClient"] + 1
            add("A7", table["overflowing"] == natural,
                f"{path} {name} table {table['i']} ({table['cols']}칸): "
                f"overflowing={table['overflowing']} natural={natural} width={table['tableRect']['w']}px "
                f"maxContent={table['maxContentWidth']}px wrap={table['wrapClient']}px")

    for table in configs["narrow-light"]["tables"]:
        if table["cols"] != 2 or not table["hasInlineCode"]:
            continue
        long_codes = [c for c in table["codeMetrics"] if len(c["text"]) >= 20]
        wrap_ok = all((c["lines"] or 0) >= 2 for c in long_codes)
        fits = not table["overflowing"] and table["wrapScroll"] <= table["wrapClient"] + 1
        add("A8", fits and wrap_ok,
            f"{path} 375 table {table['i']} (2칸, 코드): overflowing={table['overflowing']} "
            f"wrapScroll={table['wrapScroll']} wrapClient={table['wrapClient']} "
            f"codes={table['codeMetrics']}")

    for entry in a9_checks(path, configs):
        add("A9", entry["ok"], entry["detail"])
    for entry in a10_checks(path, configs):
        add("A10", entry["ok"], entry["detail"])
    for entry in a11_checks(path, configs):
        add("A11", entry["ok"], entry["detail"])
    for entry in a12_checks(path, configs):
        add("A12", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a13_checks(path, configs):
        add("A13", entry["ok"], entry["detail"], na=entry.get("na", False))

    summary = {key: summarize_checks(entries) for key, entries in checks.items()}
    return summary, checks


def main():
    parser = argparse.ArgumentParser(description="Verify blog article UI/UX across widths, themes, interactions")
    parser.add_argument("build_dir", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--path", action="append", default=None,
                        help="검수할 글 경로. 여러 번 넘길 수 있다.")
    args = parser.parse_args()

    paths = args.path or DEFAULT_PATHS
    args.out_dir.mkdir(parents=True, exist_ok=True)
    port = free_port()
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--bind", "127.0.0.1", "--directory", str(args.build_dir)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1.0)

    reports = {}
    skipped = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            try:
                for path in paths:
                    index = args.build_dir / path.strip("/") / "index.html"
                    if not index.exists():
                        skipped.append(path)
                        continue
                    slug = path.strip("/").split("/")[-1]
                    path_out = args.out_dir / slug
                    path_out.mkdir(parents=True, exist_ok=True)
                    url = f"http://127.0.0.1:{port}{path}"
                    report = {"url": url, "path": path, "configs": {}, "interactions": {},
                              "tables_375": {}, "resize": {}}
                    a10_path = path in MATH_PATHS
                    for name, w, h, dpr, scheme in CONFIGS:
                        report["configs"][name] = capture_config(
                            browser, url, path_out, name, w, h, dpr, scheme,
                            a10=a10_path and name in A10_CONFIGS,
                        )
                    report["interactions"]["narrow"] = report["configs"]["narrow-light"].get("interaction")
                    report["interactions"]["wide"] = report["configs"]["wide-light"].get("interaction")
                    report["tables_375"] = capture_tables_375(browser, url, path_out)
                    report["resize"] = run_resize_scenarios(browser, url, path_out)
                    reports[path] = report
            finally:
                browser.close()
    finally:
        server.terminate()
        server.wait(timeout=5)

    combined = {"generatedAt": datetime.now(timezone.utc).isoformat(),
                "buildDir": str(args.build_dir), "outDir": str(args.out_dir),
                "configs": [{"name": c[0], "width": c[1], "height": c[2], "dpr": c[3], "colorScheme": c[4]}
                            for c in CONFIGS],
                "skipped": skipped, "paths": reports, "summary": {}}
    aggregate = {key: [] for key in ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13")}
    for path, report in reports.items():
        summary, raw = path_checks(report)
        report["verdicts"] = summary
        for key in aggregate:
            aggregate[key].extend(raw[key])
        slug = path.strip("/").split("/")[-1]
        (args.out_dir / slug / "metrics.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    for key, entries in aggregate.items():
        combined["summary"][key] = summarize_checks(entries, limit=60)
    (args.out_dir / "metrics.json").write_text(json.dumps(combined, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(combined["summary"], ensure_ascii=False, indent=1))
    print("skipped:", skipped)
    print("wrote", args.out_dir / "metrics.json")


if __name__ == "__main__":
    main()
