#!/usr/bin/env python3
"""서재 글 화면 시각 검수 스크립트 (폭·테마 캡처, A1~A19 측정, 각주 왕복, 창 크기 시나리오).

사용법:
  PLAYWRIGHT_BROWSERS_PATH="$HOME/.cache/ms-playwright" \
    python3 -P scripts/verify_article_ui.py <build_dir> <out_dir> \
      [--path /digest/roguelike-wikipedia/] [--path /digest/paradox-of-tragedy-three-aesthetics-papers/]

--path를 여러 번 주면 글마다 <out_dir>/<slug>/ 아래에 산출하고, <out_dir>/metrics.json에
전체 A1~A19 판정을 모은다. 분석 비콘(umami) 요청은 연결이 없는 환경에서 load 이벤트를
막으므로 차단한다. 화면과 무관하다.
"""
import argparse
import io
import json
import re
import socket
import struct
import subprocess
import sys
import time
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image
from playwright.sync_api import Error as PlaywrightError, sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_article_ui_checks import (
    A10_CONFIGS, A10_JS, A11_JS, A15_JS, A16_JS, A17_CONFIGS, A9_JS, a9_checks, a10_checks, a11_checks,
    a12_checks, a13_checks, a14_checks, a15_checks, a16_checks, a17_checks, a18_checks, a19_checks,
    a5_overflow_checks, a21_checks, a22_checks, a22_rule_checks, a23_checks, a23_synthetic_coverage, a24_checks,
    a26_checks,
    resized_sidenotes_ok, sidenote_presence_ok, strict_lightbox_checks, summarize_checks,
)

CONFIGS = [
    ("wide-light", 1440, 900, 1, "light"),
    ("wide-dark", 1440, 900, 1, "dark"),
    ("mid-light", 1024, 800, 1, "light"),
    ("tablet820-light", 820, 1180, 2, "light"),
    ("tablet-light", 768, 1024, 2, "light"),
    ("phablet-light", 600, 960, 2, "light"),
    ("narrow-light", 375, 812, 2, "light"),
    ("narrow-dark", 375, 812, 2, "dark"),
    ("min360-light", 360, 740, 2, "light"),
    ("min390-light", 390, 844, 2, "light"),
    ("min414-light", 414, 896, 2, "light"),
]

# 태블릿·큰 폰은 겹쳐 뜨는 스크롤바를 쓰는 터치 기기라 데스크톱 스크롤바가 폭을 먹지 않는다.
TOUCH_CONFIGS = {"phablet-light", "tablet-light", "tablet820-light"}

# lightbox.js의 prepareLightboxImages가 isLightboxImage인 그림에만 aria-haspopup을 단다.
# 링크로 감싼 그림은 누르면 링크로 가는 것이 의도된 동작이라 대상이 아니다.
LIGHTBOX_SELECTOR = ('.post-content img[aria-haspopup="dialog"], '
                     'article.post-single .entry-cover img[aria-haspopup="dialog"]')
LIGHTBOX_CONFIGS = ("wide-light", "mid-light", "narrow-light", "narrow-dark")
LIGHTBOX_MAX_IMAGES = 4  # 동작이 그림마다 같아 DOM 순서 앞 4장만 잰다

# 썸 두께를 픽셀로 재는 설정. device_scale_factor가 1인 데스크톱 설정만 쓴다.
LIGHTBOX_THUMB_CONFIGS = {"wide-light", "mid-light"}
LIGHTBOX_THUMB_BAR_PX = 12
LIGHTBOX_THUMB_STRIP_PX = 220
THUMB_COLOR_DISTANCE = 24

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
    "/digest/xiaomi-mimo-v2-6/",
    "/digest/jacobian-conjecture-false-frontier-ai-2026/",
    "/digest/anabology-escape-velocity-mv/",
    "/digest/design-md-agent-design-system/",
    "/digest/humanitys-first-exam/",
    "/gallery/seosoyoung-russian-avant-garde-poster/",
    "/posts/why-rsi-might-not-reach-agi/",
]

MATH_PATHS = [
    "/digest/memory-caching-rnns/",
    "/digest/skillopt-text-space-optimizer-2026/",
    "/digest/oist-quantum-spins-centimeter-object/",
    "/digest/combining-llms-cofailure-ceiling/",
    "/digest/qwenputer-riscv-cpu/",
    "/digest/it3-periodic-table-z172/",
    "/digest/reasoning-as-pathfinding/",
    "/digest/q35-timelines-update-2027/",
    "/digest/hakken-predicting-future-discoveries/",
    "/digest/chenglou-handwired/",
    "/digest/cram-classical-energies-reasoning/",
]

RESIZE_SCENARIOS = [
    ("1440-1100-600-1440", [1440, 1100, 600, 1440]),
    ("1440-375-1440", [1440, 375, 1440]),
    ("340-375", [340, 375]),
    ("390-844", [390, 844]),
]

TOC_GAP = 32
TOC_GAP_TOL = 1
MIN_TABLE_COLS = 3
MAX_SQUEEZE_TEST_COLS = 5
SHORT_CELL_WIDTH_LIMIT = 100

# A8: 줄바꿈 경로를 시험하도록 40자 넘는 인라인 코드가 든 2칸 표를 시험 안에서만 넣는다(글 내용은 그대로).
# 붙임표·마침표 없이 이어진 한 낱말이라 overflow-wrap이 없으면 칸을 넘친다.
INLINE_CODE_TABLE_TEXT = "connectivitymodulatedrecurrentstateupdatealphabetagammadelta"
# A25: 글 안 인라인 코드(표 머리, 그림 설명, 각주, small 속)의 계산된 글자 크기 하한.
CODE_SIZE_PATHS = ["/digest/automated-cloud-factory/", "/posts/skill-catalog-dynamic-linking/", "/digest/trycua-cua/"]
CODE_SIZE_WIDTHS = (1440, 375)
CODE_SIZE_MIN_PX = 13

INLINE_CODE_SIZE_JS = r"""
() => {
  const content = document.querySelector('.post-content');
  if (!content) return {missing: true};
  const ctxOf = (el) => {
    const order = [['footnotes', '.footnotes'], ['sidenote', 'aside.sidenote'], ['th', 'th'], ['td', 'td'],
                   ['figcaption', 'figcaption'], ['sup', 'sup, sub'], ['small', 'small'],
                   ['heading', ':is(h2,h3,h4,h5,h6)'], ['blockquote', 'blockquote'], ['li', 'li'], ['p', 'p']];
    for (const [name, sel] of order) if (el.closest(sel)) return name;
    return 'other';
  };
  // 글 안에서 인라인 style이 글자 크기를 정한 곳은 이 단언에서 뺀다. 레이아웃용 style(--table-cols 등)은
  // 검사 대상 코드를 숨기지 않도록 글자 크기만 본다.
  const inlineFontSize = (el) => {
    for (let e = el; e; e = e.parentElement) {
      const value = e.getAttribute && e.getAttribute('style');
      if (value && /(?:^|;)\s*font-size\s*:/i.test(value)) return true;
    }
    return false;
  };
  const codes = [];
  for (const code of content.querySelectorAll('code')) {
    // 글 안 인라인 style과 SVG 글자는 이 단언에서 뺀다. 블록 코드(pre)도 인라인이 아니다.
    if (code.closest('pre, svg')) continue;
    if (inlineFontSize(code)) continue;
    const cs = getComputedStyle(code);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = code.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) continue;
    codes.push({text: code.textContent.trim().slice(0, 40), size: +parseFloat(cs.fontSize).toFixed(2), ctx: ctxOf(code)});
  }
  const below = codes.filter((c) => c.size < 13 - 0.01);
  return {count: codes.length, min: codes.length ? Math.min(...codes.map((c) => c.size)) : null,
          belowCount: below.length, below: below.slice(0, 12)};
}
"""

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
  const first = content ? [...content.children].find((el) => el.getBoundingClientRect().height > 0) || null : null;
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
    .filter((img) => img.getBoundingClientRect().width > 0 && !img.closest('a'))
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
        dashedCount: svg.querySelectorAll('line[stroke-dasharray], path[stroke-dasharray], polyline[stroke-dasharray]').length, texts: []};
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

  out.tables = [...content.querySelectorAll('table')].filter(t => !t.closest('.table-header-clone')).map((t, i) => {
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
      const cell = c.closest('td, th');
      let cellContentRight = null;
      if (cell) {
        const ccs = getComputedStyle(cell);
        cellContentRight = +(cell.getBoundingClientRect().right - parseFloat(ccs.paddingRight) - parseFloat(ccs.borderRightWidth)).toFixed(1);
      }
      return {text: c.textContent.trim().slice(0, 48), lines: lineHeight > 0 ? +(b.height / lineHeight).toFixed(2) : null,
              right: +b.right.toFixed(1), cellContentRight};
    });
    const colWidths = [...t.querySelectorAll('tbody tr:first-child td')].map((c) => Math.round(c.getBoundingClientRect().width));
    const dataRows = (t.tBodies[0] ? [...t.tBodies[0].rows] : rows.slice(t.tHead ? t.tHead.rows.length : 1)).filter((row) => [...row.children].every((c) => (c.colSpan || 1) === 1));
    const colTextLengths = Array.from({length: cols}, (_, ci) => dataRows.reduce((sum, row) => sum + (row.children[ci] ? row.children[ci].textContent.trim().length : 0), 0));
    const colHeaders = t.tHead && t.tHead.rows[0] ? [...t.tHead.rows[0].cells].map((c) => c.textContent.trim().slice(0, 24)) : [];
    // 화면에 보이는 글자만 잰다. KaTeX의 숨은 MathML 사본은 뺀다.
    const textRects = (cell) => {
      const out = [];
      const walker = document.createTreeWalker(cell, NodeFilter.SHOW_TEXT);
      let node;
      while ((node = walker.nextNode())) {
        if (!node.data.trim() || (node.parentElement && node.parentElement.closest('.katex-mathml'))) continue;
        const range = document.createRange();
        range.selectNodeContents(node);
        for (const rect of range.getClientRects()) if (rect.width > 0) out.push(rect);
      }
      return out;
    };
    const colNeedWidths = [];
    for (let c = 0; c < cols; c++) {
      let needW = 0;
      for (const row of rows) {
        const cell = row.children[c];
        if (!cell || (cell.colSpan || 1) !== 1) continue;
        const cr = cell.getBoundingClientRect();
        const rects = textRects(cell);
        if (rects.length) {
          const right = Math.max(...rects.map((x) => x.right));
          needW = Math.max(needW, right - cr.left);
        }
      }
      colNeedWidths.push(Math.round(needW));
    }
    const isSticky = wrap ? wrap.classList.contains('is-sticky-first') : false;
    const firstColCell = (rows[1] && rows[1].children[0]) || firstBodyCell;
    const firstColW = firstColCell ? firstColCell.getBoundingClientRect().width : 0;
    const visibleWidth = wrap ? Math.round(wrap.clientWidth - (isSticky ? firstColW : 0)) : null;
    let lastColEndGap = null;
    if (wrap && overflowBefore && cols >= 2) {
      const savedScroll = wrap.scrollLeft;
      wrap.scrollLeft = wrap.scrollWidth;
      const stickyRight = isSticky
        ? Math.max(...rows.map((row) => row.children[0] ? row.children[0].getBoundingClientRect().right : -Infinity))
        : wrap.getBoundingClientRect().left;
      const lastIdx = cols - 1;
      let lastTextLeft = Infinity;
      for (const row of rows) {
        const cell = row.children[lastIdx];
        if (!cell || (cell.colSpan || 1) !== 1) continue;
        for (const rect of textRects(cell)) {
          if (rect.left < lastTextLeft) lastTextLeft = rect.left;
        }
      }
      if (Number.isFinite(lastTextLeft) && Number.isFinite(stickyRight)) {
        lastColEndGap = +(lastTextLeft - stickyRight).toFixed(1);
      }
      wrap.scrollLeft = savedScroll;
    }
    const maxLinesPerCell = Math.max(...[...t.querySelectorAll('td')].map((c) => Math.round((c.getBoundingClientRect().height - 16) / parseFloat(getComputedStyle(c).lineHeight))));
    // A23과 같은 줄 세기: 칸 내용 높이를 그 칸 줄 높이로 나눠 반올림한다(머리 칸 포함).
    const cellLines = [...t.querySelectorAll('th,td')].map((cell) => {
      const cs = getComputedStyle(cell);
      const h = cell.getBoundingClientRect().height - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom)
        - parseFloat(cs.borderTopWidth) - parseFloat(cs.borderBottomWidth);
      return {lines: Math.round(h / parseFloat(cs.lineHeight)), text: cell.textContent.trim().slice(0, 24)};
    });
    const longestCell = cellLines.reduce((best, c) =>
      (c.lines > best.lines || (c.lines === best.lines && c.text.length > best.text.length)) ? c : best,
      {lines: 0, text: ''});
    return {i: i + 1, cols, headerCols: t.querySelectorAll('thead th').length, rows: rows.length,
      linesBefore: Math.max(0, longestCell.lines), linesBeforeText: longestCell.text,
      wrapper: wrap ? wrap.className : null, wrapClient: wrap ? wrap.clientWidth : null, wrapScroll: wrap ? wrap.scrollWidth : null,
      wrapping: wrap ? wrap.classList.contains('is-overflowing') : null, overflowing: overflowBefore,
      wrapDelta: wrap ? wrap.scrollWidth - wrap.clientWidth : null,
      tableRect: r(t), wrapRect: r(wrap), th: textInfo(th, 'th'), td: textInfo(td, 'td'),
      colWidths, maxLinesPerCell, colTextLengths, colHeaders, colNeedWidths, visibleWidth, lastColEndGap,
      firstColWidths: [...t.querySelectorAll('tbody tr td:first-child')].slice(0, 3).map((c) => +c.getBoundingClientRect().width.toFixed(1)),
      maxCellHeight: Math.max(...[...t.querySelectorAll('td')].map((c) => c.getBoundingClientRect().height)),
      maxContentWidth, fontSize: parseFloat(style.fontSize),
      firstCellMinWidth: firstCellStyle ? firstCellStyle.minWidth : null,
      firstCellWidth: firstBodyCell ? +firstBodyCell.getBoundingClientRect().width.toFixed(1) : null,
      firstCellText: firstBodyCell ? firstBodyCell.textContent.trim().slice(0, 24) : null,
      sticky: wrap ? wrap.classList.contains('is-sticky-first') : null,
      wrapFirst: wrap ? wrap.classList.contains('is-wrap-first') : false,
      firstCellPosition: firstCellStyle ? firstCellStyle.position : null,
      firstCellBg: firstCellStyle ? firstCellStyle.backgroundColor : null,
      firstColSpills: (() => {
        const bad = [];
        for (const cell of t.querySelectorAll('tr > :first-child')) {
          if ((cell.colSpan || 1) !== 1) continue;
          const r = document.createRange();
          r.selectNodeContents(cell);
          const rects = [...r.getClientRects()].filter(x => x.width > 0);
          if (!rects.length) continue;
          const right = Math.max(...rects.map(x => x.right));
          const limit = cell.getBoundingClientRect().right - parseFloat(getComputedStyle(cell).paddingRight);
          if (right > limit + 1) {
            bad.push(`${cell.textContent.trim().slice(0, 32)}(+${+(right - limit).toFixed(1)}px)`);
          }
        }
        return bad;
      })(),
      firstColMidWordBreaks: (() => {
        const bad = [];
        for (const cell of t.querySelectorAll('tbody tr > :first-child')) {
          const walker = document.createTreeWalker(cell, NodeFilter.SHOW_TEXT);
          const chars = [];
          let n;
          while ((n = walker.nextNode())) {
            if (n.parentElement && n.parentElement.closest('.katex, script, style')) continue;
            for (let k = 0; k < n.data.length; k++) {
              const r = document.createRange();
              r.setStart(n, k); r.setEnd(n, k + 1);
              const rects = r.getClientRects();
              if (!rects.length) continue;
              chars.push({c: n.data[k], top: Math.round(rects[0].top)});
            }
          }
          for (let k = 1; k < chars.length; k++) {
            if (chars[k].top > chars[k - 1].top + 4) {
              const prev = chars[k - 1].c, next = chars[k].c;
              if (/\s/.test(prev) || /\s/.test(next)) continue;
              bad.push(chars.slice(Math.max(0, k - 10), k).map(x => x.c).join('') + '⏎' + chars.slice(k, k + 10).map(x => x.c).join(''));
            }
          }
        }
        return bad;
      })(),
      firstColOrphanVersions: (() => {
        const bad = [];
        for (const cell of t.querySelectorAll('tbody tr > :first-child')) {
          const walker = document.createTreeWalker(cell, NodeFilter.SHOW_TEXT);
          const lines = [];
          let n;
          while ((n = walker.nextNode())) {
            if (n.parentElement && n.parentElement.closest('.katex, script, style')) continue;
            for (let k = 0; k < n.data.length; k++) {
              const ch = n.data[k];
              const r = document.createRange();
              r.setStart(n, k); r.setEnd(n, k + 1);
              const rects = r.getClientRects();
              if (!rects.length) continue;
              const mid = (rects[0].top + rects[0].bottom) / 2;
              let ln = lines.find(l => Math.abs(l.mid - mid) <= 9);
              if (!ln) { ln = {mid, text: ''}; lines.push(ln); }
              ln.text += ch;
            }
          }
          if (lines.length > 1) {
            for (const ln of lines.slice(1)) {
              if (/^\d+(?:\.\d+)?$/.test(ln.text.trim())) {
                bad.push(cell.textContent.trim() + ' -> ' + lines.map(l => l.text.trim()).join(' / '));
              }
            }
          }
        }
        return bad;
      })(),
      tableHyphenBreaks: (() => {
        const bad = [];
        for (const cell of t.querySelectorAll('th, td')) {
          const walker = document.createTreeWalker(cell, NodeFilter.SHOW_TEXT);
          let n;
          while ((n = walker.nextNode())) {
            const p = n.parentElement;
            if (!p || p.closest('.katex, code, pre, script, style')) continue;
            const txt = n.textContent;
            for (let k = 1; k < txt.length - 1; k++) {
              if (txt[k] !== '-') continue;
              if (!/[A-Za-z0-9]/.test(txt[k - 1]) || !/[A-Za-z0-9]/.test(txt[k + 1])) continue;
              const r1 = document.createRange(); r1.setStart(n, k); r1.setEnd(n, k + 1);
              const r2 = document.createRange(); r2.setStart(n, k + 1); r2.setEnd(n, k + 2);
              const a = r1.getBoundingClientRect(), b = r2.getBoundingClientRect();
              if (b.top - a.top > 4) {
                const s = txt.lastIndexOf(' ', k) + 1;
                let e = txt.indexOf(' ', k); if (e < 0) e = txt.length;
                bad.push(txt.slice(s, k + 1) + '⏎' + txt.slice(k + 1, e));
              }
            }
          }
        }
        return bad;
      })(),
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
  out.adjacentFootnoteGroups = [];
  out.strayFootnoteCommas = [];
  const fnSups = [...content.querySelectorAll('sup[id^="fnref"]')];
  for (const s of fnSups) {
    const prev = s.previousSibling;
    const before = getComputedStyle(s, '::before').content;
    const isAdj = Boolean(prev && prev.nodeType === 1 && prev.matches('sup[id^="fnref"]'));
    if (isAdj) {
      const a = prev.getBoundingClientRect();
      const b = s.getBoundingClientRect();
      const al = prev.querySelector('a') || prev;
      const bl = s.querySelector('a') || s;
      const ar = al.getBoundingClientRect();
      const br = bl.getBoundingClientRect();
      out.adjacentFootnoteGroups.push({
        nums: [prev.textContent.trim(), s.textContent.trim()],
        gap: +(b.left - a.right).toFixed(1),
        linkGap: +(br.left - ar.right).toFixed(1),
        sameLine: Math.abs(a.top - b.top) < 2,
        before,
      });
    } else {
      const hasComma = Boolean(before && before !== 'none' && before !== 'normal' && before !== '""');
      if (hasComma) {
        out.strayFootnoteCommas.push({
          num: s.textContent.trim(),
          before,
          prevText: prev && prev.nodeType === 3 ? prev.textContent.slice(-16) : '',
        });
      }
    }
  }
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

TABLE_STICKY_JS = r"""
() => {
  const parseRGB = (s) => { const m = String(s || '').match(/rgba?\(([^)]+)\)/); if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number); return {r:p[0], g:p[1], b:p[2], a: p.length > 3 ? p[3] : 1}; };
  const bodyBg = (() => {
    const b = parseRGB(getComputedStyle(document.body).backgroundColor);
    if (b && b.a > 0) return b;
    return parseRGB(getComputedStyle(document.documentElement).backgroundColor);
  })();
  const firstCellOf = (row) => (row && row.children[0] && row.children[0].colSpan === 1 ? row.children[0] : null);
  return [...document.querySelectorAll('.post-content .table-scroll')].map((wrap, index) => {
    const table = wrap.querySelector('table');
    const rows = [...table.querySelectorAll('tr')];
    let cols = 0;
    rows.forEach((row) => { let count = 0; [...row.children].forEach((cell) => { count += cell.colSpan || 1; }); if (count > cols) cols = count; });
    let firstCell = null;
    for (const row of rows) {
      const cell = firstCellOf(row);
      if (cell) { firstCell = cell; break; }
    }
    const firstCellIn = (selector) => {
      for (const row of table.querySelectorAll(selector)) {
        const cell = firstCellOf(row);
        if (cell) return cell;
      }
      return null;
    };
    const headCell = firstCellIn('thead tr');
    const bodyCell = firstCellIn('tbody tr');
    wrap.scrollLeft = wrap.scrollWidth;
    const wrapRect = wrap.getBoundingClientRect();
    const cellRect = firstCell ? firstCell.getBoundingClientRect() : null;
    const headRect = headCell ? headCell.getBoundingClientRect() : null;
    const bodyRect = bodyCell ? bodyCell.getBoundingClientRect() : null;
    const cs = firstCell ? getComputedStyle(firstCell) : null;
    const row0 = table.rows[0];
    const restCells = row0 ? [...row0.cells].slice(1) : [];
    const visibleRoom = cellRect ? wrap.clientWidth - cellRect.width : 0;
    const colsFit = restCells.length > 0 && restCells.every((cell, idx) => {
      const st = getComputedStyle(cell);
      const cw = cell.getBoundingClientRect().width;
      const needW = idx === restCells.length - 1
        ? cw - parseFloat(st.paddingInlineStart)
        : cw - parseFloat(st.paddingInlineStart) - parseFloat(st.paddingInlineEnd);
      return needW <= visibleRoom + 1;
    });
    const data = {
      index: index + 1,
      cols,
      overflowing: wrap.classList.contains('is-overflowing'),
      sticky: wrap.classList.contains('is-sticky-first'),
      colsFit,
      wrapClient: wrap.clientWidth,
      scrollLeft: +wrap.scrollLeft.toFixed(1),
      maxScroll: +(wrap.scrollWidth - wrap.clientWidth).toFixed(1),
      firstCellWidth: cellRect ? +cellRect.width.toFixed(1) : null,
      fontSize: parseFloat(getComputedStyle(table).fontSize),
      firstLeftDiff: headRect ? +(headRect.left - wrapRect.left).toFixed(1) : null,
      bodyLeftDiff: bodyRect ? +(bodyRect.left - wrapRect.left).toFixed(1) : null,
      firstCellPosition: cs ? cs.position : null,
      bodyCellPosition: bodyCell ? getComputedStyle(bodyCell).position : null,
      firstCellBg: cs ? parseRGB(cs.backgroundColor) : null,
      bodyBg,
    };
    wrap.scrollLeft = 0;
    return data;
  });
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
    const originalClass = wrap.className;
    const expandedWidth = table.style.getPropertyValue('--table-expanded-width');
    const expandedPriority = table.style.getPropertyPriority('--table-expanded-width');
    const scrollLeft = wrap.scrollLeft;
    wrap.classList.remove('is-overflowing', 'is-sticky-first', 'is-expanded', 'is-compact-first');
    table.style.removeProperty('--table-expanded-width');
    const rows = [...table.querySelectorAll('tr')];
    let cols = 0;
    rows.forEach((row) => { let count = 0; [...row.children].forEach((cell) => { count += cell.colSpan || 1; }); if (count > cols) cols = count; });
    const natural = wrap.scrollWidth > wrap.clientWidth + 1 || table.scrollWidth > wrap.clientWidth + 1;
    const fontSize = parseFloat(getComputedStyle(table).fontSize);
    const cellLines = [...table.querySelectorAll('th,td')].map(cell => {
      const cs = getComputedStyle(cell);
      const h = cell.getBoundingClientRect().height - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom)
        - parseFloat(cs.borderTopWidth) - parseFloat(cs.borderBottomWidth);
      return Math.round(h / parseFloat(cs.lineHeight));
    });
    const linesBefore = Math.max(0, ...cellLines);
    const longCell = cols >= 3 && linesBefore >= 5;
    const oldWidth = table.style.getPropertyValue('width');
    const oldPriority = table.style.getPropertyPriority('width');
    table.style.setProperty('width', 'max-content');
    const maxContentWidth = table.getBoundingClientRect().width;
    if (oldWidth) table.style.setProperty('width', oldWidth, oldPriority); else table.style.removeProperty('width');
    const squeezed = !natural && cols >= 3 && cols <= 5
      && wrap.clientWidth / cols < fontSize * 8 && maxContentWidth > wrap.clientWidth + 1;
    let minimumMaxColumn = null, minimumVisible = null;
    if (!natural && !squeezed && longCell && maxContentWidth > wrap.clientWidth + 1) {
      wrap.classList.add('is-overflowing', 'is-expanded');
      table.style.setProperty('--table-expanded-width', (wrap.clientWidth + 1) + 'px');
      const bodyCell = table.querySelector('tbody tr:first-child > :first-child');
      const label = bodyCell ? bodyCell.textContent.trim().slice(0, 24) : '';
      if (cols === 4 && bodyCell && (label.length <= 6 || /^\d{4}$/.test(label))
          && bodyCell.getBoundingClientRect().width > 100) wrap.classList.add('is-compact-first');
      const first = table.querySelector('tr > :first-child').getBoundingClientRect().width;
      const sticky = cols >= 3 && wrap.clientWidth - first >= fontSize * 8;
      wrap.classList.toggle('is-sticky-first', sticky);
      const firstAfter = table.querySelector('tr > :first-child').getBoundingClientRect().width;
      minimumVisible = wrap.clientWidth - (sticky ? firstAfter : 0);
      const head = table.tHead ? table.tHead.rows[0] : table.rows[0];
      minimumMaxColumn = Math.max(...[...head.cells].map(c => c.getBoundingClientRect().width));
    }
    wrap.className = originalClass;
    if (expandedWidth) table.style.setProperty('--table-expanded-width', expandedWidth, expandedPriority);
    else table.style.removeProperty('--table-expanded-width');
    wrap.scrollLeft = scrollLeft;
    return {index: i + 1, cols, isOverflowing: was, natural, squeezed, longCell,
      maxContentWidth, minimumMaxColumn, minimumVisible, linesBefore,
      wrapClient: wrap.clientWidth, wrapScroll: wrap.scrollWidth,
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
  const first = content ? [...content.children].find((el) => el.getBoundingClientRect().height > 0) || null : null;
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


LIGHTBOX_STATE_JS = r"""
() => {
  const o = document.querySelector('.ssy-lightbox');
  const ae = document.activeElement;
  const bodyFirst = document.body ? document.body.firstElementChild : null;
  const res = {open: !!o, rootOverflow: document.documentElement.style.overflow,
    activeInLightbox: !!(o && ae && o.contains(ae)),
    activeSrc: (ae && ae.tagName === 'IMG' && ae.getAttribute('src'))
      ? ae.getAttribute('src').split('/').pop() : null,
    scrollY: +window.scrollY.toFixed(2),
    bodyFirstX: bodyFirst ? +bodyFirst.getBoundingClientRect().x.toFixed(2) : null};
  if (o) {
    const b = o.querySelector('img');
    const r = b.getBoundingClientRect();
    const or = o.getBoundingClientRect();
    const oc = getComputedStyle(o);
    const cap = o.querySelector('.ssy-lightbox-caption');
    res.captionH = cap ? cap.offsetHeight + (parseFloat(getComputedStyle(cap).marginTop) || 0) : 0;
    res.big = {x: r.x, y: r.y, w: r.width, h: r.height, right: r.right, bottom: r.bottom,
      natural: [b.naturalWidth, b.naturalHeight], complete: b.complete, src: b.currentSrc.split('/').pop()};
    res.overlay = {left: +or.left.toFixed(2), top: +or.top.toFixed(2), right: +or.right.toFixed(2),
      bottom: +or.bottom.toFixed(2), clientW: o.clientWidth, clientH: o.clientHeight,
      scrollW: o.scrollWidth, scrollH: o.scrollHeight,
      leftGap: +(r.left - or.left).toFixed(2), rightGap: +(or.right - r.right).toFixed(2)};
    res.box = {w: +(o.clientWidth - parseFloat(oc.paddingLeft) - parseFloat(oc.paddingRight)).toFixed(2),
      h: +(o.clientHeight - parseFloat(oc.paddingTop) - parseFloat(oc.paddingBottom)).toFixed(2)};
    res.vw = innerWidth; res.vh = innerHeight;
    res.screenLeftGap = +r.left.toFixed(2);
    res.screenRightGap = +(innerWidth - r.right).toFixed(2);
    res.inView = r.x >= 0 && r.y >= 0 && r.right <= innerWidth + 0.5 && r.bottom <= innerHeight + 0.5;
    res.scrollMode = o.classList.contains('ssy-lightbox--scroll');
    res.wideMode = o.classList.contains('ssy-lightbox--wide');
    res.inViewX = r.x >= 0 && r.right <= innerWidth + 0.5;
    res.overlayScrollable = o.scrollHeight > o.clientHeight + 1;
    res.overlayScrollableX = o.scrollWidth > o.clientWidth + 1;
    res.scrollLeft = +o.scrollLeft.toFixed(1);
    res.ratioErr = b.naturalWidth ? Math.abs(r.width / r.height - b.naturalWidth / b.naturalHeight) : null;
    res.role = o.getAttribute('role'); res.label = o.getAttribute('aria-label');
  }
  return res;
}
"""


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


SETTLE_IMAGE_TIMEOUT_MS = 8000


SETTLE_IMAGES_JS = r"""
(limitMs) => new Promise((resolve) => {
  // display:none 안의 lazy 이미지는 화면에 그려지지 않으므로 기다리지 않는다.
  const waiting = [...document.images].filter(
    (img) => !img.complete && img.getClientRects().length > 0
  );
  if (!waiting.length) { resolve(0); return; }
  let done = false;
  const finish = () => {
    if (done) return;
    done = true;
    resolve(waiting.filter((img) => !img.complete).length);
  };
  setTimeout(finish, limitMs);
  Promise.all(waiting.map((img) => new Promise((r) => {
    img.addEventListener('load', r, { once: true });
    img.addEventListener('error', r, { once: true });
  }))).then(finish);
})
"""


def settle(page, image_timeout_ms=SETTLE_IMAGE_TIMEOUT_MS):
    # 스크롤 간격을 뷰포트 높이 이하로 두어 페이지의 모든 구간이 화면에 한 번씩 들어오게 한다.
    step = max(1, int(page.evaluate("window.innerHeight") or 1))
    y = 0
    h = page.evaluate("document.documentElement.scrollHeight")
    while y < h:
        page.evaluate(f"window.scrollTo(0, {y})")
        page.wait_for_timeout(40)
        y += step
        h = page.evaluate("document.documentElement.scrollHeight")
    page.wait_for_load_state("networkidle")
    # 그려지는 이미지만 기다리고 전체에 한도를 둔다. 한도에 걸리면 남은 수를 알리고 진행한다.
    pending = page.evaluate(SETTLE_IMAGES_JS, image_timeout_ms)
    if pending:
        print(f"settle: 그려지는 이미지 {pending}장이 {image_timeout_ms}ms 안에 로드되지 않아 넘어갑니다.",
              flush=True)
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


def open_context(browser, width, height, dpr, scheme, touch=False):
    ctx = browser.new_context(
        viewport={"width": width, "height": height},
        device_scale_factor=dpr,
        color_scheme=scheme,
        is_mobile=(width < 500 or touch),
        has_touch=(width < 500 or touch),
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
        imgs = page.locator(".post-content p > img")
        if imgs.count() > 0:
            img = imgs.first
            img.scroll_into_view_if_needed()
            page.wait_for_timeout(300)
            y_before = page.evaluate("scrollY")
            img.tap()
            page.wait_for_timeout(500)
            lb_open = page.evaluate("!!document.querySelector('.ssy-lightbox')")
            lb_caption = page.evaluate("(document.querySelector('.ssy-lightbox-caption')||{}).textContent || null")
            page.screenshot(path=str(out_dir / "lightbox-open.png"))
            page.keyboard.press("Escape")
            page.wait_for_timeout(400)
            lb_after = page.evaluate("!!document.querySelector('.ssy-lightbox')")
            scroll_kept = abs(page.evaluate("scrollY") - y_before) < 2
            active_after = page.evaluate("document.activeElement ? document.activeElement.tagName + '.' + document.activeElement.className : null")
            inter["lightbox"] = {
                "open": lb_open,
                "caption": lb_caption,
                "afterEsc": lb_after,
                "scrollKept": scroll_kept,
                "activeAfterEsc": active_after,
            }
    return inter


def table_scroll_end_capture(page, name, out_dir):
    # 첫 열 고정을 보이는 표를 끝까지 민 상태로 찍는다.
    # 변경 전 빌드(is-sticky-first 없음)에서도 같은 표를 찍도록 post.js와 같은 폭 조건으로 고른다.
    index = page.evaluate(
        """() => {
          const wraps = [...document.querySelectorAll('.post-content .table-scroll')];
          const sticky = wraps.findIndex((w) => w.classList.contains('is-sticky-first'));
          if (sticky >= 0) return sticky;
          const wouldStick = (w) => {
            if (!w.classList.contains('is-overflowing') || w.clientWidth <= 0) return false;
            const table = w.querySelector('table');
            let cols = 0;
            [...table.querySelectorAll('tr')].forEach((row) => {
              let count = 0;
              [...row.children].forEach((cell) => { count += cell.colSpan || 1; });
              if (count > cols) cols = count;
            });
            if (cols < 3) return false;
            const font = parseFloat(getComputedStyle(table).fontSize);
            if (isNaN(font)) return false;
            for (const row of [...table.querySelectorAll('tr')]) {
              const cell = row.children[0];
              if (cell && cell.colSpan === 1) {
                return w.clientWidth - cell.getBoundingClientRect().width >= font * 8;
              }
            }
            return false;
          };
          const overflowing = wraps.map((w, i) => i).filter((i) => wraps[i].classList.contains('is-overflowing'));
          const expected = overflowing.find((i) => wouldStick(wraps[i]));
          if (expected !== undefined) return expected;
          return overflowing.length ? overflowing[0] : -1;
        }"""
    )
    if index is None or index < 0:
        return None
    wrap = page.locator(".post-content .table-scroll").nth(index)
    wrap.scroll_into_view_if_needed()
    page.evaluate(
        "(i) => { const w = document.querySelectorAll('.post-content .table-scroll')[i]; if (w) w.scrollLeft = w.scrollWidth; }", index)
    page.wait_for_timeout(300)
    data = page.evaluate(
        """(i) => {
          const w = document.querySelectorAll('.post-content .table-scroll')[i];
          if (!w) return null;
          const table = w.querySelector('table');
          let first = null;
          for (const row of [...table.querySelectorAll('tr')]) {
            const cell = row.children[0];
            if (cell && cell.colSpan === 1) { first = cell; break; }
          }
          const wr = w.getBoundingClientRect();
          const fr = first ? first.getBoundingClientRect() : null;
          return {table: i + 1, scrollLeft: +w.scrollLeft.toFixed(1),
                  maxScroll: +(w.scrollWidth - w.clientWidth).toFixed(1),
                  sticky: w.classList.contains('is-sticky-first'),
                  firstLeftDiff: fr ? +(fr.left - wr.left).toFixed(1) : null};
        }""",
        index,
    )
    filename = "table-scrolled-end-dark.png" if name == "narrow-dark" else "table-scrolled-end.png"
    wrap.screenshot(path=str(out_dir / filename))
    page.evaluate("() => { document.querySelectorAll('.post-content .table-scroll').forEach((w) => { w.scrollLeft = 0; }); }")
    return data


# A18: 고정 첫 열과 이웃 칸의 그려진 가로 괘선이 같은 화소 줄에 있는지 잰다.
# 첫 열 오른쪽 끝 안쪽 x와 둘째 열 왼쪽 끝 안쪽 x에서 세로로 훑어 괘선색 y 구간 목록을 비교한다.
# 글자 안티에일리어싱이 괘선색과 비슷한 한두 화소를 만들므로 가로로 32화소 이상 이어진 구간만
# 괘선으로 센다. 머리 위아래 줄은 --rule-strong이라 DOM 머리 칸 경계 근처 창에서만 찾는다.
A18_COLOR_TOL = 2
A18_MIN_LINE_PX = 32
A18_HEADER_WINDOW_PX = 3
# 표 맨 아래 --rule 줄이 두 x 모두에 있는지는 표 바닥(장치 화소) 위아래 이 창 안에서 찾는다.
# 표가 화면 높이로 잘려 찍히면 바닥을 못 재므로 창 높이를 표 전체가 들어올 만큼 올려 찍는다.
# full_page 캡처는 창 크기를 바꿔 resize가 가로 스크롤을 되돌리므로 쓰지 않는다.
A18_BOTTOM_WINDOW_PX = 4
A18_TOP_GAP_CSS_PX = 120
A18_BOTTOM_PAD_CSS_PX = 8

A18_LIST_JS = r"""
() => {
  const wraps = [...document.querySelectorAll('.post-content .table-scroll')];
  wraps.forEach((w) => { w.scrollLeft = 0; });
  return wraps.map((w, i) => {
    if (!w.classList.contains('is-sticky-first')) return null;
    const table = w.querySelector('table');
    const row = [...table.querySelectorAll('tr')].find((r) => r.children.length > 1 && r.children[0].colSpan === 1);
    if (!row) return null;
    const wr = w.getBoundingClientRect();
    const first = row.children[0].getBoundingClientRect();
    const second = row.children[1].getBoundingClientRect();
    const headRow = table.querySelector('thead tr');
    const headCell = headRow ? ([...headRow.children].find((c) => c.colSpan === 1) || headRow.children[0]) : null;
    const hr = headCell ? headCell.getBoundingClientRect() : null;
    return {i, aRight: first.right - wr.left, bLeft: second.left - wr.left,
            headTop: hr ? hr.top - wr.top : null, headBottom: hr ? hr.bottom - wr.top : null,
            text: row.children[0].textContent.trim().slice(0, 20)};
  }).filter(Boolean);
}
"""

A18_PLACE_JS = r"""
([i, frac, gap]) => { const w = document.querySelectorAll('.post-content .table-scroll')[i];
  w.scrollLeft = (w.scrollWidth - w.clientWidth) * frac;
  const top = w.getBoundingClientRect().top + scrollY;
  window.scrollTo(0, top - gap);
  const r = w.getBoundingClientRect();
  const t = w.querySelector('table').getBoundingClientRect();
  return {x: r.left, y: r.top, w: r.width, h: r.height, tableBottom: t.bottom - r.top, viewH: innerHeight};
}
"""

A18_TALLEST_JS = r"""
() => Math.ceil(Math.max(0, ...[...document.querySelectorAll('.post-content .table-scroll.is-sticky-first')]
  .map((w) => w.getBoundingClientRect().height)))
"""

A18_COLOR_JS = r"""
() => { const out = {};
  for (const name of ['rule', 'rule-strong']) {
    const span = document.createElement('span');
    span.style.color = 'var(--' + name + ')';
    document.body.appendChild(span);
    out[name] = getComputedStyle(span).color;
    span.remove();
  }
  return out; }
"""

A18_END_JS = "() => { document.querySelectorAll('.post-content .table-scroll').forEach((w) => { w.scrollLeft = 0; }); window.scrollTo(0, 0); }"

# A18 캡처 동안만 표 감싸개의 오버레이 스크롤바를 숨긴다.
# 좁은 화면(모바일 에뮬레이션)의 오버레이 스크롤바는 자리를 차지하지 않고, 그 썸이 스크롤 0 에서
# 고정 첫 열 아래 표 바닥 괘선을 덮어 그려진 줄과 측정값이 어긋난다. 실제 휴대폰의 오버레이
# 스크롤바는 스크롤하는 동안에만 보이므로 화면 결함이 아니다. 반면 데스크톱의 클래식 스크롤바는
# 자리(15 CSS px)를 차지하므로 숨기면 표 감싸개 높이와 뒤 요소 위치가 바뀐다.
# 그래서 자리를 차지하지 않는(offset - client == 0) 감싸개에만 표시 속성을 붙여 숨긴다.
A18_HIDE_SCROLLBAR_JS = r"""
() => {
  const style = document.createElement('style');
  style.id = 'a18-hide-scrollbar';
  style.textContent = '[data-a18-hide-scrollbar] { scrollbar-width: none; }' +
    '[data-a18-hide-scrollbar]::-webkit-scrollbar { display: none; }';
  document.head.appendChild(style);
  document.querySelectorAll('.post-content .table-scroll.is-overflowing').forEach((w) => {
    if (w.offsetWidth - w.clientWidth === 0 && w.offsetHeight - w.clientHeight === 0) {
      w.setAttribute('data-a18-hide-scrollbar', '');
    }
  });
}
"""
A18_SHOW_SCROLLBAR_JS = r"""
() => {
  const style = document.getElementById('a18-hide-scrollbar');
  if (style) style.remove();
  document.querySelectorAll('[data-a18-hide-scrollbar]').forEach((w) => w.removeAttribute('data-a18-hide-scrollbar'));
}
"""


def parse_rgb(text):
    values = text[text.index("(") + 1:text.rindex(")")].split(",")[:3]
    return tuple(int(round(float(value))) for value in values)


def seam_hlen(pix, width, x, y, color):
    def hit(px):
        pixel = pix[px, y]
        return max(abs(pixel[k] - color[k]) for k in range(3)) <= A18_COLOR_TOL
    if not hit(x):
        return 0
    left = x
    while left > 0 and hit(left - 1):
        left -= 1
    right = x
    while right + 1 < width and hit(right + 1):
        right += 1
    return right - left + 1


def seam_runs(pix, width, height, x, color, y0=0, y1=None):
    if y1 is None:
        y1 = height
    runs = []
    start = None
    for y in range(y0, y1):
        pixel = pix[x, y]
        hit = max(abs(pixel[k] - color[k]) for k in range(3)) <= A18_COLOR_TOL
        if hit and start is None:
            start = y
        if not hit and start is not None:
            if seam_hlen(pix, width, x, start + (y - start) // 2, color) >= A18_MIN_LINE_PX:
                runs.append([start, y - start])
            start = None
    if start is not None and seam_hlen(pix, width, x, start + (y1 - start) // 2, color) >= A18_MIN_LINE_PX:
        runs.append([start, y1 - start])
    return runs


def seam_diff(a, b):
    left = {tuple(run) for run in (a or [])}
    right = {tuple(run) for run in (b or [])}
    return len(left - right) + len(right - left)


def seam_state_record(image, table, dpr, rule, strong, bottom_px):
    """한 상태(rest 또는 end)의 표 그림에서 두 x의 괘선 y 목록과 표 바닥 줄을 잰다."""
    pix = image.load()
    xa = int((table["aRight"] - 4) * dpr)
    xb = int((table["bLeft"] + 3) * dpr)
    empty = {"ok": False, "a": [], "b": [], "strongA": [], "strongB": [], "mismatch": 0,
             "bottomA": [], "bottomB": []}
    if xa < 0 or xb < 0 or xa >= image.width or xb >= image.width:
        return dict(empty, reason=f"잰 x가 그림 밖: xa={xa} xb={xb} width={image.width}")
    first_runs = seam_runs(pix, image.width, image.height, xa, rule)
    second_runs = seam_runs(pix, image.width, image.height, xb, rule)
    strong_first, strong_second = [], []
    if table["headTop"] is not None and table["headBottom"] is not None:
        for base in (table["headTop"] * dpr, table["headBottom"] * dpr):
            y0 = max(0, int(round(base)) - A18_HEADER_WINDOW_PX)
            y1 = min(image.height, int(round(base)) + A18_HEADER_WINDOW_PX + 1)
            strong_first.extend(seam_runs(pix, image.width, image.height, xa, strong, y0, y1))
            strong_second.extend(seam_runs(pix, image.width, image.height, xb, strong, y0, y1))
        strong_ok = bool(strong_first) and bool(strong_second)
    else:
        strong_ok = True
    # 표 맨 아래 --rule 줄: 두 x 모두 표 바닥 위아래 창 안에 있어야 한다(둘 다 같게 없는 경우도 실패).
    by0 = max(0, bottom_px - A18_BOTTOM_WINDOW_PX)
    by1 = min(image.height, bottom_px + A18_BOTTOM_WINDOW_PX + 1)
    bottom_first = seam_runs(pix, image.width, image.height, xa, rule, by0, by1)
    bottom_second = seam_runs(pix, image.width, image.height, xb, rule, by0, by1)
    bottom_ok = bool(bottom_first) and bool(bottom_second)
    ok = (bool(first_runs) and bool(second_runs) and first_runs == second_runs
          and strong_ok and strong_first == strong_second and bottom_ok)
    record = {"ok": ok, "a": first_runs, "b": second_runs,
              "strongA": strong_first, "strongB": strong_second,
              "bottomA": bottom_first, "bottomB": bottom_second,
              "mismatch": seam_diff(first_runs, second_runs) + seam_diff(strong_first, strong_second)}
    if not ok:
        if not bottom_ok:
            record["reason"] = (f"표 맨 아래 --rule 줄 없음(첫 열 x={bool(bottom_first)}, "
                                f"둘째 열 x={bool(bottom_second)}, 바닥 y={bottom_px})")
        elif not first_runs or not second_runs:
            record["reason"] = "괘선을 찾지 못함"
        elif not strong_ok:
            record["reason"] = "머리 위아래 --rule-strong 줄을 찾지 못함"
        else:
            record["reason"] = "두 x의 괘선 y 목록이 다름"
    return record


def capture_sticky_seams(page, out_dir, name, dpr):
    original = page.viewport_size
    tables = page.evaluate(A18_LIST_JS)
    sticky_count = page.evaluate(
        "() => document.querySelectorAll('.post-content .table-scroll.is-sticky-first').length")
    records = []
    if sticky_count > len(tables):
        missing = {"ok": False, "a": [], "b": [], "strongA": [], "strongB": [], "mismatch": 0,
                   "reason": f"측정하지 못한 고정 표 {sticky_count - len(tables)}건"}
        records.append({"table": None, "text": None,
                        "states": {"rest": dict(missing), "end": dict(missing)}})
    if not tables:
        return records
    # 표 전체가 한 화면에 들어오도록 창 높이만 올린다(가로 폭은 그대로라 post.js가 다시 계산하지 않는다).
    tallest = page.evaluate(A18_TALLEST_JS)
    tall = max(original["height"], tallest + A18_TOP_GAP_CSS_PX + A18_BOTTOM_PAD_CSS_PX + 16)
    page.set_viewport_size({"width": original["width"], "height": tall})
    page.wait_for_timeout(300)
    try:
        # 괘선을 재기 전에 오버레이 스크롤바만 숨긴다(창 높이를 올려도 자리 차지는 0 그대로다).
        page.evaluate(A18_HIDE_SCROLLBAR_JS)
        # 높이를 바꾼 뒤의 좌표로 다시 잰다.
        tables = page.evaluate(A18_LIST_JS)
        colors = page.evaluate(A18_COLOR_JS)
        rule = parse_rgb(colors["rule"])
        strong = parse_rgb(colors["rule-strong"])
        for table in tables:
            record = {"table": table["i"] + 1, "text": table["text"], "states": {}}
            for frac, state in ((0, "rest"), (1, "end")):
                box = page.evaluate(A18_PLACE_JS, [table["i"], frac, A18_TOP_GAP_CSS_PX])
                page.wait_for_timeout(250)
                empty = {"ok": False, "a": [], "b": [], "strongA": [], "strongB": [], "mismatch": 0,
                         "bottomA": [], "bottomB": []}
                if box["w"] < 20 or box["h"] < 20:
                    record["states"][state] = dict(empty, reason="표가 화면에 들어오지 않음")
                    continue
                if box["y"] < 0 or box["y"] + box["h"] + A18_BOTTOM_PAD_CSS_PX > box["viewH"]:
                    record["states"][state] = dict(
                        empty, reason=f"표 전체가 한 화면에 들어오지 않음: y={box['y']:.1f} h={box['h']:.1f} viewH={box['viewH']}")
                    continue
                # clip을 쓰면 캡처 원점이 바뀌어 화소 맞춤이 실제 화면과 달라진다. 화면 전체를 찍고 잘라 낸다.
                full = Image.open(io.BytesIO(page.screenshot())).convert("RGB")
                x0 = int(round(box["x"] * dpr))
                y0 = int(round(box["y"] * dpr))
                image = full.crop((x0, y0, min(full.width, x0 + int(round(box["w"] * dpr))),
                                   min(full.height, y0 + int(round((box["h"] + A18_BOTTOM_PAD_CSS_PX) * dpr)))))
                bottom_px = int(round(box["tableBottom"] * dpr))
                state_record = seam_state_record(image, table, dpr, rule, strong, bottom_px)
                if not state_record["ok"]:
                    image.save(out_dir / f"a18-{name}-table{table['i'] + 1}-{state}.png")
                record["states"][state] = state_record
            records.append(record)
    finally:
        page.evaluate(A18_SHOW_SCROLLBAR_JS)
        page.evaluate(A18_END_JS)
        page.set_viewport_size(original)
        page.wait_for_timeout(300)
    return records


SOURCE_OG_CARD_JS = r"""
() => {
  const c = document.querySelector('.source-og-card');
  if (!c) return null;
  const r = el => {
    if (!el) return null;
    const b = el.getBoundingClientRect();
    return {x: +b.x.toFixed(2), y: +b.y.toFixed(2), w: +b.width.toFixed(2), h: +b.height.toFixed(2)};
  };
  const lines = el => {
    if (!el) return 0;
    const rg = document.createRange();
    rg.selectNodeContents(el);
    return new Set([...rg.getClientRects()].map(x => Math.round(x.top))).size;
  };
  const media = c.querySelector('.source-og-card__media');
  const img = c.querySelector('img');
  const body = c.querySelector('.source-og-card__body');
  const kids = body ? [...body.children] : [];
  const gaps = [];
  for (let i = 1; i < kids.length; i++) {
    gaps.push(+(kids[i].getBoundingClientRect().top - kids[i - 1].getBoundingClientRect().bottom).toFixed(1));
  }
  const br = body.getBoundingClientRect();
  const first = kids[0].getBoundingClientRect();
  const last = kids[kids.length - 1].getBoundingClientRect();
  const probe = (varName) => {
    const p = document.createElement('span');
    p.style.cssText = `position:fixed;left:-9999px;color:var(${varName})`;
    document.body.appendChild(p);
    const col = getComputedStyle(p).color;
    p.remove();
    return col;
  };
  const metaEl = c.querySelector('.source-og-card__meta');
  const titleEl = c.querySelector('.source-og-card__title');
  const ctaEl = c.querySelector('.source-og-card__cta');
  return {
    vw: innerWidth,
    card: r(c),
    media: r(media),
    img: r(img),
    body: r(body),
    imgBoxShadow: img ? getComputedStyle(img).boxShadow : null,
    imgAlt: img ? img.getAttribute('alt') : null,
    hasCta: !!ctaEl,
    metaText: metaEl ? metaEl.textContent.trim() : '',
    metaHasHangul: metaEl ? /[가-힣]/.test(metaEl.textContent) : false,
    titleFontSize: titleEl ? parseFloat(getComputedStyle(titleEl).fontSize) : null,
    bodyFontSize: parseFloat(getComputedStyle(document.body).fontSize),
    lines: Object.fromEntries(kids.map(k => [(k.className.split('__')[1] || k.tagName), lines(k)])),
    gaps,
    padTop: +(first.top - br.top).toFixed(1),
    padBottom: +(br.bottom - last.bottom).toFixed(1),
    letterbox: +(media.getBoundingClientRect().height - img.getBoundingClientRect().height).toFixed(1),
    ruleStrongColor: probe('--rule-strong'),
    accentColor: probe('--accent'),
    bgColor: probe('--bg'),
  };
}
"""


def measure_source_og_card(page, dpr, check_pixels=False):
    card = page.locator(".source-og-card")
    if card.count() == 0:
        return None
    card.scroll_into_view_if_needed()
    page.wait_for_timeout(150)
    info = page.evaluate(SOURCE_OG_CARD_JS)
    if not info or not check_pixels:
        return info

    def color_close(a, b, tol=18):
        return all(abs(int(x) - int(y)) <= tol for x, y in zip(a[:3], b[:3]))

    bg_rgb = parse_rgb(info["bgColor"])

    def first_border_pixel(seq):
        for px in seq[:max(2, int(round(dpr)) + 1)]:
            if not color_close(px, bg_rgb, tol=6):
                return px
        return seq[0]

    def grab_border_pixels():
        raw = card.screenshot()
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        w, h = im.size
        vw = info["vw"]
        media_w = int(round(info["media"]["w"] * dpr))
        media_h = int(round(info["media"]["h"] * dpr))
        band = max(3, int(round(2 * dpr)) + 1)
        bands = {}
        if vw >= 641:
            img_x = max(band, min(w - band, media_w // 2))
            body_x = max(media_w + band, min(w - band, media_w + (w - media_w) // 2))
            mid_y = max(band, min(h - band, h // 2))
            bands["top_img"] = [im.getpixel((img_x, y)) for y in range(band)]
            bands["top_body"] = [im.getpixel((body_x, y)) for y in range(band)]
            bands["bottom_img"] = [im.getpixel((img_x, h - 1 - y)) for y in range(band)]
            bands["bottom_body"] = [im.getpixel((body_x, h - 1 - y)) for y in range(band)]
            bands["left_img"] = [im.getpixel((x, mid_y)) for x in range(band)]
            bands["right_body"] = [im.getpixel((w - 1 - x, mid_y)) for x in range(band)]
        else:
            mid_x = max(band, min(w - band, w // 2))
            img_y = max(band, min(h - band, media_h // 2))
            body_y = max(media_h + band, min(h - band, media_h + (h - media_h) // 2))
            bands["top_img"] = [im.getpixel((mid_x, y)) for y in range(band)]
            bands["bottom_body"] = [im.getpixel((mid_x, h - 1 - y)) for y in range(band)]
            bands["left_img"] = [im.getpixel((x, img_y)) for x in range(band)]
            bands["left_body"] = [im.getpixel((x, body_y)) for x in range(band)]
            bands["right_img"] = [im.getpixel((w - 1 - x, img_y)) for x in range(band)]
            bands["right_body"] = [im.getpixel((w - 1 - x, body_y)) for x in range(band)]
        return {k: first_border_pixel(v) for k, v in bands.items()}

    page.mouse.move(1, 1)
    page.evaluate("document.activeElement && document.activeElement.blur && document.activeElement.blur()")
    page.wait_for_timeout(150)
    rest_px = grab_border_pixels()

    page.evaluate("(document.querySelector('.toc summary') || document.querySelector('.toc a') || document.body).focus()")
    for _ in range(6):
        page.keyboard.press("Tab")
        if page.evaluate("document.activeElement && document.activeElement.classList.contains('source-og-card')"):
            break
    page.wait_for_timeout(150)
    focus_px = grab_border_pixels()
    page.evaluate("document.activeElement && document.activeElement.blur && document.activeElement.blur()")

    expected_rest = parse_rgb(info["ruleStrongColor"])
    expected_focus = parse_rgb(info["accentColor"])
    rest_mismatches = {
        k: list(v) for k, v in rest_px.items() if not color_close(v, expected_rest, tol=18)
    }
    focus_mismatches = {
        k: list(v) for k, v in focus_px.items() if not color_close(v, expected_focus, tol=18)
    }
    info["borderPixels"] = {
        "expectedRest": list(expected_rest),
        "expectedFocus": list(expected_focus),
        "rest": {k: list(v) for k, v in rest_px.items()},
        "focus": {k: list(v) for k, v in focus_px.items()},
        "restMismatches": rest_mismatches,
        "focusMismatches": focus_mismatches,
        "ok": not rest_mismatches and not focus_mismatches,
    }
    return info


def capture_config(browser, url, out_dir, name, width, height, dpr, scheme, a10=False):
    ctx = open_context(browser, width, height, dpr, scheme, touch=name in TOUCH_CONFIGS)
    page = ctx.new_page()
    failed = []
    page.on("requestfailed", lambda req: failed.append(req.url))
    page.on("response", lambda res: failed.append(f"{res.status} {res.url}") if res.status >= 400 else None)
    page.goto(url, wait_until="load", timeout=60000)
    settle(page)
    m = page.evaluate(MEASURE_JS)
    m["failedRequests"] = failed
    m["a9"] = page.evaluate(A9_JS)
    m["diagrams"] = page.evaluate(A16_JS)
    m["diagramTextLengths"] = page.evaluate("""() => [...document.querySelectorAll('.post-content .blog-diagram .diagram-svg-mobile text')]
      .filter(e => e.getBoundingClientRect().width > 0).map(e => e.getComputedTextLength())""")
    m["diagramMobileCount"] = page.evaluate(
        "() => document.querySelectorAll('.post-content .blog-diagram .diagram-svg-mobile').length")
    if name in ("wide-light", "narrow-light"):
        m["lineTables"] = page.evaluate(LINE_TABLES_JS, page.evaluate(STATE_JS)['tables'])
    if name in A17_CONFIGS:
        m["sticky"] = page.evaluate(TABLE_STICKY_JS)
    if name == "wide-light":
        m["quotes"] = page.evaluate(A15_JS)
    has_katex = page.locator(".post-content .katex, aside.sidenote .katex").count() > 0
    if (a10 or has_katex) and name in A10_CONFIGS:
        m["a10"] = page.evaluate(A10_JS, name == "wide-light")
        m["a11"] = page.evaluate(A11_JS, name == "wide-light")
    m["sourceOgCard"] = measure_source_og_card(
        page, dpr, check_pixels=name in ("wide-light", "wide-dark", "narrow-light", "narrow-dark")
    )
    d = out_dir / name
    d.mkdir(parents=True, exist_ok=True)
    page.add_style_tag(content=".site-top{position:static!important} html{scroll-behavior:auto!important}")
    if name in A17_CONFIGS:
        m["seams"] = capture_sticky_seams(page, d, name, dpr)
    shots = {}
    if width < 500:
        disp_count = page.locator(".post-content .katex-display").count()
        for i in range(disp_count):
            shots[f"display{i+1}-start"] = padded_element_shot(
                page, ".post-content .katex-display", d / f"display{i+1}-start.png", nth=i, pad=24)
            page.evaluate(
                "(idx) => { const k = document.querySelectorAll('.post-content .katex-display')[idx]; k.scrollLeft = k.scrollWidth; }", i)
            page.wait_for_timeout(100)
            shots[f"display{i+1}-end"] = padded_element_shot(
                page, ".post-content .katex-display", d / f"display{i+1}-end.png", nth=i, pad=24)
            page.evaluate(
                "(idx) => { document.querySelectorAll('.post-content .katex-display')[idx].scrollLeft = 0; }", i)
    diag_count = page.locator("figure.blog-diagram").count()
    for i in range(diag_count):
        key = "diagram" if i == 0 else f"diagram{i+1}"
        out_png = d / f"{key}.png"
        if width < 500:
            viewport_shot(page, "figure.blog-diagram", out_png, nth=i)
            shots[key] = str(out_png)
        else:
            shots[key] = element_shot(page, "figure.blog-diagram", out_png, nth=i)
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
    if name in ("narrow-light", "narrow-dark", "wide-light"):
        m["tableScrollEnd"] = table_scroll_end_capture(page, name, d)
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


# A19: 창 높이만 바뀌는 resize(모바일 주소창이 접히며 생기는 것)에서 밀어 둔 표의 가로 스크롤이 유지되는지.
# post.js가 가로 폭이 같은 resize에서 is-overflowing을 뗐다 붙이면 scrollLeft가 0으로 돌아간다.
A19_WIDTH = 375
A19_HEIGHT = 812
A19_HEIGHT_DELTA_PX = 96

A19_STATE_JS = r"""
(arm) => [...document.querySelectorAll('.post-content .table-scroll')].map((w, i) => {
  if (arm && w.classList.contains('is-overflowing')) w.scrollLeft = w.scrollWidth;
  const row = [...w.querySelectorAll('tr')].find((r) => r.children[0]);
  return {i, text: row ? row.children[0].textContent.trim().slice(0, 20) : '',
          overflowing: w.classList.contains('is-overflowing'),
          sticky: w.classList.contains('is-sticky-first'),
          scrollLeft: +w.scrollLeft.toFixed(1), max: +(w.scrollWidth - w.clientWidth).toFixed(1)};
})
"""


def run_height_resize(browser, url):
    ctx = open_context(browser, A19_WIDTH, A19_HEIGHT, 2, "light")
    page = ctx.new_page()
    page.goto(url, wait_until="load", timeout=60000)
    settle(page)
    page.add_style_tag(content="html{scroll-behavior:auto!important}")
    before = page.evaluate(A19_STATE_JS, True)
    page.wait_for_timeout(200)
    before = page.evaluate(A19_STATE_JS, False)
    page.set_viewport_size({"width": A19_WIDTH, "height": A19_HEIGHT + A19_HEIGHT_DELTA_PX})
    page.wait_for_timeout(500)
    after = page.evaluate(A19_STATE_JS, False)
    ctx.close()
    return [{"table": b["i"] + 1, "text": b["text"], "before": b, "after": a}
            for b, a in zip(before, after) if b["overflowing"]]


def css_rgb_triplet(value):
    """getComputedStyle의 rgb()/rgba() 문자열을 (r, g, b)로 바꾼다."""
    numbers = re.findall(r"[\d.]+", value or "")
    if len(numbers) < 3:
        return None
    return tuple(int(round(float(number))) for number in numbers[:3])


def measure_thumb_run(png_path, axis, bg=None):
    """막대 캡처에서 썸 색 구간의 두께(px)와 막대 방향 위치를 잰다.

    세로 막대는 행마다 x 방향으로, 가로 막대는 열마다 y 방향으로 배경색과 다른 구간을
    찾아 가장 흔한 길이를 썸 두께로 쓴다. 세라피엘 검수의 픽셀 스캔 방식을 그대로 옮겼다.
    배경색은 페이지에서 읽은 --bg를 넘긴다. 썸이 길게 그려져 캡처 대부분을 차지해도
    배경을 썸 색으로 잘못 고르지 않는다.
    """
    with Image.open(png_path) as im:
        rgb = im.convert("RGB")
    width, height = rgb.size
    px = rgb.load()
    if bg is None:
        bg = px[0, height - 1]

    def differs(color):
        return sum((a - b) ** 2 for a, b in zip(color, bg)) > THUMB_COLOR_DISTANCE ** 2

    runs = []
    if axis == "x":
        for y in range(height):
            start = None
            for x in range(width + 1):
                on = x < width and differs(px[x, y])
                if on and start is None:
                    start = x
                elif not on and start is not None:
                    runs.append((x - start, y))
                    start = None
    else:
        for x in range(width):
            start = None
            for y in range(height + 1):
                on = y < height and differs(px[x, y])
                if on and start is None:
                    start = y
                elif not on and start is not None:
                    runs.append((y - start, x))
                    start = None
    runs = [run for run in runs if run[0] >= 2]
    if not runs:
        return {"thickness": None, "pos": None}
    counts = {}
    for length, _ in runs:
        counts[length] = counts.get(length, 0) + 1
    thickness = max(counts, key=lambda length: (counts[length], length))
    positions = sorted(pos for length, pos in runs if length == thickness)
    return {"thickness": thickness, "pos": positions[len(positions) // 2]}


def capture_page_thumb(page, out_dir, name):
    """같은 화면의 페이지 세로 막대 썸 두께를 보통·올림·누름에서 잰다."""
    view = page.evaluate("() => ({vw: innerWidth, vh: innerHeight})")
    vw, vh = view["vw"], view["vh"]
    bg = css_rgb_triplet(page.evaluate(
        "() => getComputedStyle(document.documentElement).backgroundColor"))
    bar = LIGHTBOX_THUMB_BAR_PX
    x = max(0, vw - bar)
    height = min(LIGHTBOX_THUMB_STRIP_PX, vh)
    clip = {"x": x, "y": 0, "width": bar, "height": height}
    page.mouse.move(vw // 2, 10)
    page.wait_for_timeout(150)
    normal_path = out_dir / f"lightbox-{name}-page-vbar-normal.png"
    page.screenshot(path=str(normal_path), clip=clip)
    normal = measure_thumb_run(normal_path, "x", bg)
    result = {"normal": normal["thickness"], "pos": normal["pos"], "crop": str(normal_path)}
    if not normal["thickness"]:
        return result
    y = min(max(1, normal["pos"]), vh - 2)
    page.mouse.move(vw - bar // 2, y)
    page.wait_for_timeout(250)
    hover_path = out_dir / f"lightbox-{name}-page-vbar-hover.png"
    page.screenshot(path=str(hover_path), clip=clip)
    result["hover"] = measure_thumb_run(hover_path, "x", bg)["thickness"]
    page.mouse.down()
    page.wait_for_timeout(200)
    active_path = out_dir / f"lightbox-{name}-page-vbar-active.png"
    page.screenshot(path=str(active_path), clip=clip)
    result["active"] = measure_thumb_run(active_path, "x", bg)["thickness"]
    page.mouse.move(max(0, vw - bar - 40), y, steps=4)
    page.mouse.up()
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(200)
    return result


def capture_overlay_thumb(page, out_dir, name, index):
    """wide 라이트박스 가로 막대 썸 두께를 보통·올림·누름에서 잰다."""
    view = page.evaluate("() => ({vw: innerWidth, vh: innerHeight})")
    vw, vh = view["vw"], view["vh"]
    bg = css_rgb_triplet(page.evaluate(
        "() => getComputedStyle(document.documentElement).backgroundColor"))
    bar = LIGHTBOX_THUMB_BAR_PX
    y = max(0, vh - bar)
    clip = {"x": 0, "y": y, "width": min(420, vw), "height": bar}
    page.mouse.move(vw // 2, vh // 2)
    page.wait_for_timeout(150)
    normal_path = out_dir / f"lightbox-{name}-{index}-hbar-normal.png"
    page.screenshot(path=str(normal_path), clip=clip)
    normal = measure_thumb_run(normal_path, "y", bg)
    result = {"normal": normal["thickness"], "pos": normal["pos"], "crop": str(normal_path)}
    if not normal["thickness"]:
        return result
    x = min(max(1, normal["pos"]), vw - 2)
    page.mouse.move(x, vh - bar // 2)
    page.wait_for_timeout(250)
    hover_path = out_dir / f"lightbox-{name}-{index}-hbar-hover.png"
    page.screenshot(path=str(hover_path), clip=clip)
    result["hover"] = measure_thumb_run(hover_path, "y", bg)["thickness"]
    page.mouse.down()
    page.wait_for_timeout(200)
    active_path = out_dir / f"lightbox-{name}-{index}-hbar-active.png"
    page.screenshot(path=str(active_path), clip=clip)
    result["active"] = measure_thumb_run(active_path, "y", bg)["thickness"]
    # 누른 채 조금 끌어야 click이 닫기로 해석되지 않는다(dragged).
    page.mouse.move(min(vw - 2, x + 40), vh - bar // 2, steps=4)
    page.mouse.up()
    page.evaluate("() => { const o = document.querySelector('.ssy-lightbox'); if (o) o.scrollLeft = 0; }")
    page.wait_for_timeout(150)
    return result


def run_lightbox_scenarios(browser, url, out_dir):
    results = {}
    configs = {config[0]: config for config in CONFIGS}
    for name in LIGHTBOX_CONFIGS:
        _, width, height, dpr, scheme = configs[name]
        ctx = open_context(browser, width, height, dpr, scheme)
        page = ctx.new_page()
        page.goto(url, wait_until="load", timeout=60000)
        settle(page)
        count = page.locator(LIGHTBOX_SELECTOR).count()
        if count == 0:
            results[name] = {"applicable": False, "reason": "확대할 그림이 없다"}
            ctx.close()
            continue
        # wide 가로 막대 썸과 비교할 같은 화면의 페이지 세로 막대 썸을 먼저 잰다.
        page_thumb = None
        if name in LIGHTBOX_THUMB_CONFIGS:
            page_thumb = capture_page_thumb(page, out_dir, name)
        rows = []
        for i in range(min(count, LIGHTBOX_MAX_IMAGES)):
            img = page.locator(LIGHTBOX_SELECTOR).nth(i)
            meta = None
            try:
                img.scroll_into_view_if_needed()
                page.wait_for_timeout(300)
                meta = img.evaluate(
                    "e => ({src: e.getAttribute('src').split('/').pop(),"
                    " role: e.getAttribute('role'), tabIndex: e.tabIndex,"
                    " width: e.getBoundingClientRect().width,"
                    " haspopup: e.getAttribute('aria-haspopup')})")
                before = page.evaluate(LIGHTBOX_STATE_JS)
                img.click()
                page.wait_for_selector(".ssy-lightbox img", state="attached", timeout=15000)
                page.wait_for_function(
                    "() => { const b = document.querySelector('.ssy-lightbox img');"
                    " return b && b.complete && b.naturalWidth > 0; }", timeout=15000)
                page.wait_for_timeout(250)
                opened = page.evaluate(LIGHTBOX_STATE_JS)
                if i == 0:
                    page.screenshot(path=str(out_dir / f"lightbox-{name}-0.png"))
                wide_thumb = None
                if opened.get("wideMode") and name in LIGHTBOX_THUMB_CONFIGS:
                    try:
                        wide_thumb = capture_overlay_thumb(page, out_dir, name, i)
                    except Exception as e:  # 픽셀 측정 실패도 판정 실패로 남긴다.
                        wide_thumb = {"error": str(e)}
                # 가로로 넘치는 라이트박스는 끝까지 밀었을 때 오른쪽 끝이 보이는지 잰다.
                page.evaluate(
                    "() => { const o = document.querySelector('.ssy-lightbox'); o.scrollLeft = o.scrollWidth; }")
                page.wait_for_timeout(120)
                panned = page.evaluate(LIGHTBOX_STATE_JS)
                if i == 0 and opened.get("overlayScrollableX"):
                    page.screenshot(path=str(out_dir / f"lightbox-{name}-0-end.png"))
                page.evaluate("() => { const o = document.querySelector('.ssy-lightbox'); o.scrollLeft = 0; }")
                after_resize = None
                if i == 0:
                    # 연 채로 창 폭을 바꿔도 열린 채 다시 맞춰지는지 잰다(§0 18번).
                    page.set_viewport_size({"width": 600 if width < 500 else 1024, "height": height})
                    page.wait_for_timeout(400)
                    after_resize = page.evaluate(LIGHTBOX_STATE_JS)
                    page.set_viewport_size({"width": width, "height": height})
                    page.wait_for_timeout(300)
                page.keyboard.press("Tab")
                after_tab = page.evaluate(LIGHTBOX_STATE_JS)
                page.keyboard.press("Escape")
                page.wait_for_timeout(150)
                after_esc = page.evaluate(LIGHTBOX_STATE_JS)
                page.keyboard.press("Enter")
                page.wait_for_selector(".ssy-lightbox", state="attached")
                page.mouse.click(5, 5)
                page.wait_for_timeout(150)
                after_outside = page.evaluate(LIGHTBOX_STATE_JS)
                rows.append({"img": meta, "before": before, "opened": opened, "panned": panned,
                             "afterResize": after_resize, "wideThumb": wide_thumb,
                             "afterTab": after_tab, "afterEsc": after_esc,
                             "afterOutsideClick": after_outside})
            except PlaywrightError as e:
                rows.append({"img": meta, "error": str(e)})
                page.keyboard.press("Escape")
        results[name] = {"applicable": True, "rows": rows, "pageThumb": page_thumb,
                         "thumbEligible": name in LIGHTBOX_THUMB_CONFIGS}
        ctx.close()
    return results



LINE_TABLES_JS = r"""
(states) => [...document.querySelectorAll('.post-content .table-scroll')].map((w, i) => {
  const t = w.querySelector(':scope > table'), state = states[i];
  const row = t.tHead ? t.tHead.rows[0] : t.rows[0];
  const columns = [...row.cells].map(c => c.getBoundingClientRect().width);
  const visible = w.clientWidth - (w.classList.contains('is-sticky-first') ? columns[0] : 0);
  let lines = 0;
  t.querySelectorAll('th,td').forEach(cell => {
    const cs = getComputedStyle(cell);
    const h = cell.getBoundingClientRect().height - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom)
      - parseFloat(cs.borderTopWidth) - parseFloat(cs.borderBottomWidth);
    lines = Math.max(lines, Math.round(h / parseFloat(cs.lineHeight)));
  });
  return {table:i+1, cols:state.cols, lines, linesBefore:state.linesBefore,
          expanded:w.classList.contains('is-expanded'), overflowing:w.classList.contains('is-overflowing'),
          sticky:w.classList.contains('is-sticky-first'),
          natural:state.natural, squeezed:state.squeezed, maxContentWidth:state.maxContentWidth,
          maxColumn:Math.max(...columns), visible, scroll:w.scrollWidth, client:w.clientWidth,
          tableWidth:t.getBoundingClientRect().width, columns};
})
"""

HEADER_STATE_JS = r"""
(index) => {
  const w = document.querySelectorAll('.post-content .table-scroll')[index];
  const t = w.querySelector(':scope > table'), head = t.tHead;
  const clone = w.querySelector('.table-header-clone');
  const over = w.classList.contains('is-overflowing');
  const h = over ? clone && !clone.hidden ? clone.querySelector('thead') : null : head;
  const top = document.querySelector('.site-top').getBoundingClientRect().bottom;
  const heads = h ? [...h.querySelectorAll('tr:first-child > *')] : [];
  const cells = [...(t.tBodies[0]?.rows[0]?.cells || [])];
  let edges = [];
  if (heads.length === cells.length) heads.forEach((c, i) => {
    const a = c.getBoundingClientRect(), b = cells[i].getBoundingClientRect();
    edges.push(a.left-b.left, a.right-b.right);
  });
  return {topDiff: heads.length ? heads[0].getBoundingClientRect().top - top : 999, edges,
          shown: !!h, inert: !over || !!(clone && clone.hasAttribute('inert') && clone.getAttribute('aria-hidden') === 'true'),
          tabSafe: !over || !!(clone && (clone.inert || !clone.querySelector('a, button, input, select, textarea, [tabindex]')))};
}
"""


def run_header_scenarios(browser, url, out_dir):
    rows = []
    for width in (1440, 375):
        ctx = open_context(browser, width, 900, 1, 'light')
        page = ctx.new_page()
        page.goto(url, wait_until='load', timeout=60000)
        settle(page)
        page.add_style_tag(content='html{scroll-behavior:auto!important}')
        indices = page.evaluate("""() => [...document.querySelectorAll('.post-content .table-scroll')].map((w, i) => {
          const t = w.querySelector(':scope > table');
          return {i, kind: w.classList.contains('is-overflowing') ? 'overflow' : 'normal',
                  eligible: !!(t.tHead && t.tBodies[0]?.rows.length && t.getBoundingClientRect().height > t.tHead.getBoundingClientRect().height + 100)};
        })""")
        for kind in ('normal', 'overflow'):
            candidate = next((x for x in indices if x['kind'] == kind and x['eligible']), None)
            if not candidate:
                continue
            i = candidate['i']
            page.evaluate("""i => { const w=document.querySelectorAll('.post-content .table-scroll')[i];
              const h=w.querySelector(':scope > table').tHead; window.scrollTo(0, scrollY+h.getBoundingClientRect().top-64+8); }""", i)
            page.wait_for_timeout(120)
            initial = page.evaluate(HEADER_STATE_JS, i)
            page.evaluate("i => {const w=document.querySelectorAll('.post-content .table-scroll')[i]; w.scrollLeft=w.scrollWidth;}", i)
            page.wait_for_timeout(120)
            scrolled = page.evaluate(HEADER_STATE_JS, i)
            page.screenshot(path=str(out_dir / f'header-{width}-{kind}.png'))
            tab_safe = True
            if kind == 'overflow':
                for _ in range(15):
                    page.keyboard.press('Tab')
                    if page.evaluate("() => !!document.activeElement.closest('.table-header-clone')"):
                        tab_safe = False
                page.evaluate("""i => {const h=document.querySelectorAll('.post-content .table-scroll')[i].querySelector(':scope > table').tHead;
                    window.scrollTo(0,scrollY+h.getBoundingClientRect().top-64+8);}""", i)
                page.wait_for_timeout(120)
            page.set_viewport_size({'width': 1300 if width == 1440 else 390, 'height': 900})
            page.wait_for_timeout(250)
            resized = page.evaluate(HEADER_STATE_JS, i)
            page.evaluate("""i => {const w=document.querySelectorAll('.post-content .table-scroll')[i];
              window.scrollTo(0,scrollY+w.getBoundingClientRect().bottom+100);}""", i)
            page.wait_for_timeout(120)
            hidden = not page.evaluate(HEADER_STATE_JS, i)['shown'] if kind == 'overflow' else page.evaluate(
                """i => { const t=document.querySelectorAll('.post-content .table-scroll')[i].querySelector(':scope > table');
                    return t.tHead.querySelector('th,td').getBoundingClientRect().bottom < document.querySelector('.site-top').getBoundingClientRect().bottom; }""", i)
            rows.append({'kind': kind, 'width': width, 'table': i+1, 'topDiff': initial['topDiff'],
                         'edges': initial['edges'], 'afterScrollEdges': scrolled['edges'],
                         'afterScrollTop': scrolled['topDiff'], 'afterResizeEdges': resized['edges'],
                         'afterResizeTop': resized['topDiff'], 'hiddenAfter': hidden,
                         'inert': initial['inert'], 'tabSafe': initial['tabSafe'] and tab_safe})
            page.set_viewport_size({'width': width, 'height': 900})
            page.wait_for_timeout(150)
        ctx.close()
    return rows


def run_header_rules(browser, url, out_dir, path):
    results = []
    for scheme in ('light', 'dark'):
        for width in (1440, 375):
            ctx = open_context(browser, width, 900, 1, scheme)
            page = ctx.new_page()
            page.goto(url, wait_until='load', timeout=60000)
            settle(page)
            page.add_style_tag(content='html{scroll-behavior:auto!important}')
            candidates = page.evaluate("""() => [...document.querySelectorAll('.post-content .table-scroll')].map((w,i) => {
              const t=w.querySelector(':scope > table'); return {i, kind:w.classList.contains('is-overflowing')?'overflow':'normal',
                eligible:!!(t.tHead && t.tBodies[0]?.rows.length && t.getBoundingClientRect().height > t.tHead.getBoundingClientRect().height + 100)};
            })""")
            for kind in ('normal', 'overflow'):
                preferred = (1 if path == '/digest/memory-caching-rnns/' and width == 1440 and kind == 'normal'
                             else 0 if path == '/digest/jp-market-vis/' and width == 375 and kind == 'normal' else None)
                candidate = next((x for x in candidates if x['kind'] == kind and x['eligible'] and x['i'] == preferred), None)
                candidate = candidate or next((x for x in candidates if x['kind'] == kind and x['eligible']), None)
                if not candidate:
                    continue
                index = candidate['i']
                def place(offset):
                    page.evaluate("""([i,off]) => {const t=document.querySelectorAll('.post-content .table-scroll')[i].querySelector(':scope > table');
                      const bar=document.querySelector('.site-top').getBoundingClientRect().bottom;
                      window.scrollTo(0, scrollY+t.tHead.getBoundingClientRect().top-bar+off);}""", [index, offset])
                    page.wait_for_timeout(150)
                    return page.evaluate("""i => {const w=document.querySelectorAll('.post-content .table-scroll')[i],t=w.querySelector(':scope > table');
                      const clone=w.querySelector('.table-header-clone'), h=clone && !clone.hidden ? clone.querySelector('th,td') : t.tHead.querySelector('th,td');
                      const b=h.getBoundingClientRect(), wb=w.getBoundingClientRect(), p=document.createElement('span');p.style.color='var(--rule-strong)';document.body.append(p);
                      const color=getComputedStyle(p).color;p.remove();return {xs:[0.15,0.35,0.65,0.85].map(f=>Math.round(wb.left+w.clientWidth*f)),top:b.top,bottom:b.bottom,color};}""", index)
                def capture(geom, name):
                    raw = page.screenshot(path=str(out_dir / name))
                    image = Image.open(io.BytesIO(raw)).convert('RGB')
                    color = css_rgb_triplet(geom['color'])
                    def near(y):
                        return [j for j in range(max(0, round(y)-3), min(image.height, round(y)+4))
                                if sum(sum(abs(image.getpixel((x,j))[k]-color[k]) for k in range(3)) <= 60 for x in geom['xs']) >= 3]
                    return near(geom['top']), near(geom['bottom'])
                before = place(-100)
                bt, bb = capture(before, f'rule-{width}-{kind}-{scheme}-before.png')
                stuck = place(12)
                st, sb = capture(stuck, f'rule-{width}-{kind}-{scheme}-stuck.png')
                results.append({'scheme':scheme, 'width':width, 'kind':kind, 'table':index+1,
                    'top':bool(st), 'bottom':bool(sb), 'beforeThickness':len(bb), 'afterThickness':len(sb),
                    'beforeTop':bt, 'beforeBottom':bb, 'afterTop':st, 'afterBottom':sb})
            ctx.close()
    return results


def run_inline_code_table(browser, url, out_dir):
    """A8: 40자 넘는 인라인 코드가 든 2칸 표를 375px에 넣어 칸 안 오른쪽 끝과 표 넘침을 잰다."""
    ctx = open_context(browser, 375, 812, 2, 'light')
    page = ctx.new_page()
    fixture = ('<table id="a8-synthetic"><thead><tr><th>항목</th><th>설명</th></tr></thead>'
               '<tbody><tr><td>코드</td><td><code>' + INLINE_CODE_TABLE_TEXT + '</code></td></tr></tbody></table>')

    def inject(route):
        response = route.fetch()
        body = re.sub(r'(<div class=(?:"post-content"|post-content)>)', lambda m: m.group(1) + fixture,
                      response.text(), count=1)
        route.fulfill(response=response, body=body)

    page.route(url, inject)
    page.goto(url, wait_until='load', timeout=60000)
    # 글자 크기와 표 폭만 재므로 그림을 기다리지 않는다. 표 감싸기(post.js)가 끝날 만큼만 기다린다.
    page.wait_for_timeout(500)
    result = page.evaluate("""() => {
      const wrap = [...document.querySelectorAll('.post-content .table-scroll')]
        .find((w) => !!w.querySelector('#a8-synthetic'));
      if (!wrap) return null;
      const table = wrap.querySelector('#a8-synthetic');
      const code = table.querySelector('tbody code');
      const cell = code.closest('td');
      const ccs = getComputedStyle(cell);
      const cellRect = cell.getBoundingClientRect();
      const cellContentRight = cellRect.right - parseFloat(ccs.paddingRight) - parseFloat(ccs.borderRightWidth);
      const codeRect = code.getBoundingClientRect();
      const tableRect = table.getBoundingClientRect();
      const wrapRect = wrap.getBoundingClientRect();
      return {
        text: code.textContent.trim(),
        codeRight: +codeRect.right.toFixed(1), cellContentRight: +cellContentRight.toFixed(1),
        tableRight: +tableRect.right.toFixed(1), wrapRight: +wrapRect.right.toFixed(1),
        wrapClient: wrap.clientWidth, wrapScroll: wrap.scrollWidth,
        overflowing: wrap.classList.contains('is-overflowing'),
        fontSize: parseFloat(getComputedStyle(code).fontSize),
      };
    }""")
    if result:
        result['rightInCell'] = result['codeRight'] <= result['cellContentRight'] + 1
        result['tableInside'] = result['tableRight'] <= result['wrapRight'] + 1
        result['ok'] = (result['rightInCell'] and result['tableInside']
                        and not result['overflowing'] and result['wrapScroll'] <= result['wrapClient'] + 1)
        page.evaluate("() => { const w = document.querySelector('#a8-synthetic').closest('.table-scroll'); if (w) w.id = 'a8-synthetic-wrap'; }")
        page.locator('#a8-synthetic-wrap').screenshot(path=str(out_dir / 'inline-code-table-375.png'))
    ctx.close()
    return result


def run_inline_code_sizes(browser, base_url, paths, out_dir):
    """A25: 글 안 인라인 코드의 계산된 글자 크기를 폭별로 모은다(인라인 style과 SVG는 뺀다)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for width in CODE_SIZE_WIDTHS:
        ctx = open_context(browser, width, 900, 1, 'light')
        page = ctx.new_page()
        rows = {}
        for path in paths:
            page.goto(f"{base_url}{path}", wait_until='load', timeout=60000)
            page.wait_for_timeout(250)
            rows[path] = page.evaluate(INLINE_CODE_SIZE_JS)
        ctx.close()
        results[str(width)] = rows
    (out_dir / 'inline-code-sizes.json').write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding='utf-8')
    return results


def run_synthetic_table(browser, url, out_dir):
    ctx = open_context(browser, 1440, 900, 1, 'light')
    page = ctx.new_page()
    sentence = '긴 가운데 열의 설명을 읽기 쉽게 배치하는 검수 문장입니다. ' * 40
    fixture = '<table id="a23-synthetic"><thead><tr><th>항목</th><th>긴 설명</th><th>값</th></tr></thead><tbody><tr><td>하나</td><td>' + sentence + '</td><td>둘</td></tr></tbody></table>'
    def inject(route):
        response = route.fetch()
        # 배포와 같은 --minify 빌드는 속성 따옴표를 빼므로, 따옴표 있는 꼴과 없는 꼴을 모두 받는다.
        body = re.sub(r'(<div class=(?:"post-content"|post-content)>)', lambda m: m.group(1) + fixture, response.text(), count=1)
        route.fulfill(response=response, body=body)
    page.route(url, inject)
    page.goto(url, wait_until='load', timeout=60000)
    settle(page)
    states = page.evaluate(STATE_JS)['tables']
    rows = page.evaluate(LINE_TABLES_JS, states)
    i = page.locator('.post-content .table-scroll').evaluate_all("ws => ws.findIndex(w => !!w.querySelector('#a23-synthetic'))")
    result = []
    if i >= 0:
        rows[i]['synthetic'] = True
        result.append(rows[i])
        page.locator('.post-content .table-scroll').nth(i).scroll_into_view_if_needed()
        page.screenshot(path=str(out_dir / 'synthetic-table-1440.png'))
    ctx.close()
    return result


def run_image_reservation(browser, url, out_dir):
    ctx = open_context(browser, 375, 812, 1, 'light')
    page = ctx.new_page()
    page.goto(url, wait_until='load', timeout=60000)
    settle(page)
    choice = page.evaluate("""() => {
      const imgs=[...document.querySelectorAll('.post-content img[width][height]')];
      for (const img of imgs) {
        const h=[...document.querySelectorAll('.post-content h2[id],.post-content h3[id]')]
          .find(e => img.compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING);
        if (h && img.complete && img.naturalWidth) return {img:imgs.indexOf(img), id:h.id, src:img.currentSrc};
      } return null;
    }""")
    if not choice:
        ctx.close()
        return []
    response = ctx.request.get(choice['src'], timeout=15000)
    if not response.ok:
        ctx.close()
        return []
    image_bytes = response.body()
    content_type = response.headers.get('content-type', 'application/octet-stream')
    release = threading.Event()
    class DelayedImage(BaseHTTPRequestHandler):
        def do_GET(self):
            release.wait(30)
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(image_bytes)))
            self.end_headers()
            self.wfile.write(image_bytes)
        def log_message(self, *args):
            pass
    server = ThreadingHTTPServer(('127.0.0.1', 0), DelayedImage)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        page.evaluate("""c => {const img=document.querySelectorAll('.post-content img[width][height]')[c.img];
          const fresh=img.cloneNode(false); fresh.removeAttribute('src'); fresh.removeAttribute('srcset');
          img.replaceWith(fresh); fresh.loading='eager'; fresh.src=c.src; fresh.scrollIntoView({block:'center'});}""",
          {**choice, 'src': f'http://127.0.0.1:{server.server_port}/delayed-image'})
        page.wait_for_timeout(250)
        page.screenshot(path=str(out_dir / 'image-before-load.png'))
        page.evaluate("id => document.getElementById(id).scrollIntoView()", choice['id'])
        before = page.evaluate("""c => {const img=document.querySelectorAll('.post-content img[width][height]')[c.img];
          const b=img.getBoundingClientRect(); return {width:b.width,height:b.height,
          attrWidth:Number(img.getAttribute('width')),attrHeight:Number(img.getAttribute('height')),
          anchor:document.getElementById(c.id).getBoundingClientRect().top, src:c.src, complete:img.complete};}""", choice)
        release.set()
        page.wait_for_function("""c => {const i=document.querySelectorAll('.post-content img[width][height]')[c.img];
          return i.complete && i.naturalWidth > 0;}""", arg=choice, timeout=15000)
        after = page.evaluate("id => document.getElementById(id).getBoundingClientRect().top", choice['id'])
        before['loaded'] = True
        before['anchorShift'] = after - before.pop('anchor')
        page.screenshot(path=str(out_dir / 'image-after-load.png'))
        return [before]
    finally:
        release.set()
        server.shutdown()
        server.server_close()
        thread.join()
        ctx.close()


def capture_failed_image(browser, url, image_url, out_path):
    """Capture the existing broken-image fallback with the response deliberately aborted."""
    ctx = open_context(browser, 375, 812, 1, 'light')
    ctx.route(image_url, lambda route: route.abort())
    page = ctx.new_page()
    page.goto(url, wait_until='load', timeout=60000)
    img = page.locator('.post-content img').locator(f'xpath=self::img[@src="{image_url}"]').first
    img.scroll_into_view_if_needed()
    page.wait_for_timeout(200)
    result = img.evaluate("""e => ({outerHTML:e.outerHTML, complete:e.complete, naturalWidth:e.naturalWidth,
       width:e.getAttribute('width'), height:e.getAttribute('height')})""")
    page.screenshot(path=str(out_path))
    ctx.close()
    return result


def short_first_cell(text):
    value = (text or "").strip()
    return len(value) <= 6 or bool(re.fullmatch(r"\d{4}", value))


# A7: 820px 이상에서 6~7칸 표는 max-content가 래퍼에 들지 않아도, 눌린 칸이 모두 이 줄 수 이하면 통과한다.
A7_MAX_SQUEEZE_LINES = 2


def path_checks(report, strict_lightbox=False):
    checks = {key: [] for key in ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20", "A21", "A22", "A23", "A24", "A26")}

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
    for name in ("wide-light", "wide-dark", "narrow-light", "narrow-dark"):
        for g in (configs.get(name) or {}).get("adjacentFootnoteGroups") or []:
            sep_ok = (g.get("before") not in (None, "", "none", "normal", '""')
                      and (g.get("linkGap") or 0) > 1.0
                      and bool(g.get("sameLine")))
            add("A4", sep_ok,
                f"{path} {name} 연속 각주 {g.get('nums')}: before={g.get('before')!r} "
                f"linkGap={g.get('linkGap')}px sameLine={g.get('sameLine')}")
    stray_wide = (configs.get("wide-light") or {}).get("strayFootnoteCommas") or []
    if stray_wide:
        for sc in stray_wide:
            add("A4", False,
                f"{path} wide-light 비연속 각주 {sc.get('num')!r} 앞 쉼표 노출: "
                f"prev={sc.get('prevText')!r} before={sc.get('before')!r}")
    else:
        add("A4", True, f"{path} wide-light: 앞 노드가 글인 비연속 각주 번호의 ::before 쉼표 0건")

    for scenario, data in report["resize"].items():
        for stage in data["stages"]:
            for table in stage["tables"]:
                for entry in a5_overflow_checks(f"{path} {scenario}@{stage['stageWidth']}", table):
                    add("A5", entry["ok"], entry["detail"])
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

    for name in ("narrow-light", "tablet820-light", "mid-light", "wide-light"):
        for table in configs[name]["tables"]:
            if table["cols"] < 6:
                continue
            natural = table["maxContentWidth"] > table["wrapClient"] + 1
            if name in ("tablet820-light", "mid-light", "wide-light") and table["cols"] <= 7:
                ok = not table["overflowing"] and (
                    not natural or table["linesBefore"] <= A7_MAX_SQUEEZE_LINES)
            else:
                ok = table["overflowing"] == natural
            add("A7", ok,
                f"{path} {name} table {table['i']} ({table['cols']}칸): "
                f"overflowing={table['overflowing']} natural={natural} width={table['tableRect']['w']}px "
                f"maxContent={table['maxContentWidth']}px wrap={table['wrapClient']}px "
                f"maxLines={table['linesBefore']}줄 text={table['linesBeforeText']!r}")

    for table in configs["narrow-light"]["tables"]:
        if table["cols"] != 2 or not table["hasInlineCode"]:
            continue
        # 줄 수가 아니라 넘침으로 본다. 인라인 코드 상자의 오른쪽 끝이 칸 안에 있고 표가 넘치지 않아야 한다.
        right_ok = all(c.get("cellContentRight") is not None and c["right"] <= c["cellContentRight"] + 1
                       for c in table["codeMetrics"])
        fits = not table["overflowing"] and table["wrapScroll"] <= table["wrapClient"] + 1
        add("A8", fits and right_ok,
            f"{path} 375 table {table['i']} (2칸, 코드): overflowing={table['overflowing']} "
            f"wrapScroll={table['wrapScroll']} wrapClient={table['wrapClient']} rightInCell={right_ok} "
            f"codes={table['codeMetrics']}")
    synthetic_code_table = report.get("inlineCodeTable")
    if synthetic_code_table:
        add("A8", synthetic_code_table["ok"],
            f"{path} 375 시험용 2칸 코드 표(40자+): rightInCell={synthetic_code_table['rightInCell']} "
            f"tableInside={synthetic_code_table['tableInside']} overflowing={synthetic_code_table['overflowing']} "
            f"wrapScroll={synthetic_code_table['wrapScroll']} wrapClient={synthetic_code_table['wrapClient']} "
            f"code={synthetic_code_table['text']!r}")

    for entry in a9_checks(path, configs):
        add("A9", entry["ok"], entry["detail"])
    for entry in a10_checks(path, configs):
        add("A10", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a11_checks(path, configs):
        add("A11", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a12_checks(path, configs):
        add("A12", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a13_checks(path, configs):
        add("A13", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a14_checks(path, report["lightbox"]):
        add("A14", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a15_checks(path, configs):
        add("A15", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a16_checks(path, configs):
        add("A16", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a17_checks(path, configs):
        add("A17", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a18_checks(path, configs):
        add("A18", entry["ok"], entry["detail"], na=entry.get("na", False))
    for entry in a19_checks(path, report["heightResize"]):
        add("A19", entry["ok"], entry["detail"], na=entry.get("na", False))
    if strict_lightbox:
        for entry in strict_lightbox_checks(path, report.get("lightbox")):
            add("A20", entry["ok"], entry["detail"], na=entry.get("na", False))
    else:
        add("A20", True, f"{path}: --strict-lightbox 없이 실행 (A20 해당 없음)", na=True)

    lengths = {str(width): configs[name].get('diagramTextLengths', []) for width, name in
               ((360, 'min360-light'), (375, 'narrow-light'), (390, 'min390-light'), (414, 'min414-light'))}
    mobile_counts = {str(width): configs[name].get('diagramMobileCount', 0) for width, name in
                     ((360, 'min360-light'), (375, 'narrow-light'), (390, 'min390-light'), (414, 'min414-light'))}
    table_rows = configs['wide-light'].get('lineTables', [])
    targets = {'/digest/memory-caching-rnns/': (2, False),
               '/digest/spritefusion-jev-realtime-level-gen/': (2, False),
               '/digest/4danyone-monocular-4d-human/': (5, False)}
    if path in targets:
        index, expected = targets[path]
        for row in table_rows:
            if row['table'] == index:
                row['expectedOverflow'] = expected
    for key, entries in (('A21', a21_checks(path, lengths, mobile_counts)), ('A22', a22_checks(path, report.get('headers', [])) + a22_rule_checks(path, report.get('headerRules', []))),
                         ('A23', a23_checks(path + ' 1440', table_rows) + a23_checks(path + ' 375', configs['narrow-light'].get('lineTables', [])) + a23_checks(path + ' synthetic', report.get('synthetic', []))),
                         ('A24', a24_checks(path, report.get('imageReservation', []))),
                         ('A26', a26_checks(path, configs))):
        for entry in entries:
            add(key, entry['ok'], entry['detail'], na=entry.get('na', False))

    for key, what in (
        ("A2", "좁은 폭에서 3~5칸 표"),
        ("A3", "4칸 표"),
        ("A7", "6칸 이상 표"),
        ("A8", "375px 2칸 코드 표"),
    ):
        if not checks[key]:
            add(key, True, f"{path}: {what} 0건 ({key} 해당 없음)", na=True)

    summary = {key: summarize_checks(entries) for key, entries in checks.items()}
    return summary, checks


def required_failures(summary, required):
    """--require 판정. 실패가 있거나, 잰 항목도 해당 없음도 없으면 실패다.
    해당 없음(na)만 있는 검사는 이 글에 그 검사가 적용되지 않는다는 뜻이라 통과로 본다."""
    return [key for key in required
            if summary[key]['failed']
            or (not summary[key]['checked'] and not summary[key]['na'])]


def scan_build_footnote_classes(build_dir: Path):
    """빌드 산출물 전체에서 연속 각주(</sup><sup ... id="fnref)에만 fn-adj가 붙었는지 정적 검사한다."""
    adj_re = re.compile(r'</sup><sup\b([^>]*)id="fnref[^"]*"')
    all_fn_re = re.compile(r'(.{0,16})<sup\b([^>]*)id="fnref[^"]*"')
    total_pages = 0
    adj_total = 0
    missing_adj = []
    stray_adj = []
    for section in ("posts", "digest", "gallery"):
        for f in sorted((build_dir / section).glob("*/index.html")):
            total_pages += 1
            html = f.read_text(encoding="utf-8", errors="ignore")
            for m in adj_re.finditer(html):
                adj_total += 1
                if "fn-adj" not in m.group(1):
                    missing_adj.append(f"{section}/{f.parent.name}")
            for m in all_fn_re.finditer(html):
                prefix, attrs = m.group(1), m.group(2)
                if "fn-adj" in attrs and not prefix.endswith("</sup>"):
                    stray_adj.append(f"{section}/{f.parent.name}:{prefix[-8:]!r}")
    ok = not missing_adj and not stray_adj
    return {
        "ok": ok,
        "na": False,
        "detail": (
            f"build 전체({total_pages}편): 연속 각주 {adj_total}쌍, "
            f"fn-adj 누락 {len(missing_adj)}건, 비연속 fn-adj 오부착 {len(stray_adj)}건"
            + (f" missing={missing_adj[:5]} stray={stray_adj[:5]}" if not ok else "")
        ),
    }


def main():
    parser = argparse.ArgumentParser(description="Verify blog article UI/UX across widths, themes, interactions")
    parser.add_argument("build_dir", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--path", action="append", default=None,
                        help="검수할 글 경로. 여러 번 넘길 수 있다.")
    parser.add_argument("--strict-lightbox", action="store_true",
                        help="스크롤바를 보이게 띄우고 연 상태마다 바탕 넘침·가운데를 판정한다. 하나라도 어긋나면 1로 끝난다.")
    parser.add_argument("--require", default="", help="쉼표로 구분한 검사 ID를 필수 판정한다.")
    args = parser.parse_args()
    required = [item.strip().upper() for item in args.require.split(',') if item.strip()]
    if any(item not in {f'A{i}' for i in range(1, 27)} for item in required):
        parser.error('--require에 알 수 없는 검사 ID가 있다')

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
            # Playwright 헤드리스는 기본으로 스크롤바를 숨긴다. 엄격 판정에서는 실제 스크롤바가
            # 폭을 먹는 상태를 재야 하므로 숨기기를 끈다.
            launch_kwargs = {"ignore_default_args": ["--hide-scrollbars"]} if args.strict_lightbox else {}
            browser = p.chromium.launch(**launch_kwargs)
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
                              "tables_375": {}, "resize": {}, "heightResize": [], "lightbox": {}}
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
                    report["heightResize"] = run_height_resize(browser, url)
                    report["lightbox"] = run_lightbox_scenarios(browser, url, path_out)
                    report['headers'] = run_header_scenarios(browser, url, path_out)
                    report['headerRules'] = run_header_rules(browser, url, path_out, path)
                    report['synthetic'] = run_synthetic_table(browser, url, path_out) if path == paths[0] else []
                    report['imageReservation'] = run_image_reservation(browser, url, path_out)
                    report['inlineCodeTable'] = run_inline_code_table(browser, url, path_out)
                    reports[path] = report
                code_paths = list(dict.fromkeys(list(reports) + CODE_SIZE_PATHS))
                code_sizes = run_inline_code_sizes(browser, f"http://127.0.0.1:{port}", code_paths,
                                                   args.out_dir / 'inline-code')
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
    aggregate = {key: [] for key in ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15", "A16", "A17", "A18", "A19", "A20", "A21", "A22", "A23", "A24", "A25", "A26")}
    aggregate["A4"].append(scan_build_footnote_classes(args.build_dir))
    # A25: 인라인 코드 13px 하한. --path로 준 글과 함께 고정 세 글을 폭별로 잰다.
    for width, rows in code_sizes.items():
        for path, row in rows.items():
            if row.get('missing'):
                aggregate['A25'].append({'ok': True, 'na': True,
                                         'detail': f'{path} {width}: 글 본문 없음 (A25 해당 없음)'})
                continue
            if not row['count']:
                aggregate['A25'].append({'ok': True, 'na': True,
                                         'detail': f'{path} {width}: 인라인 코드 0개 (A25 해당 없음)'})
                continue
            ok = row['min'] >= CODE_SIZE_MIN_PX - 0.01
            detail = f"{path} {width}: 인라인 코드 {row['count']}개, 최소 {row['min']}px"
            if not ok:
                samples = ', '.join(f"{c['ctx']}:{c['size']}px {c['text']!r}" for c in row['below'])
                detail += f", 13px 미만 {row['belowCount']}개 [{samples}]"
            aggregate['A25'].append({'ok': ok, 'na': False, 'detail': detail})
    for path, report in reports.items():
        summary, raw = path_checks(report, strict_lightbox=args.strict_lightbox)
        report["verdicts"] = summary
        for key in aggregate:
            aggregate[key].extend(raw.get(key, []))
        slug = path.strip("/").split("/")[-1]
        (args.out_dir / slug / "metrics.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    sticky_seen = any(
        table.get("sticky")
        for report in reports.values()
        for config in report["configs"].values()
        for table in (config.get("sticky") or [])
    )
    if not sticky_seen:
        aggregate["A17"].append(
            {"ok": False, "na": False, "detail": "A17: 전체 실행에서 is-sticky-first가 붙은 표 0건"})
    seam_tables = sum(
        len(config.get("seams") or [])
        for report in reports.values()
        for config in report["configs"].values()
    )
    if not seam_tables:
        aggregate["A18"].append(
            {"ok": False, "na": False, "detail": "A18: 전체 실행에서 검사한 고정 표 0건"})

    height_tables = sum(len(report["heightResize"]) for report in reports.values())
    if not height_tables:
        aggregate["A19"].append(
            {"ok": False, "na": False, "detail": "A19: 전체 실행에서 검사한 넘치는 표 0건"})

    for key, entries in aggregate.items():
        combined["summary"][key] = summarize_checks(entries, limit=60)
    (args.out_dir / "metrics.json").write_text(json.dumps(combined, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(combined["summary"], ensure_ascii=False, indent=1))
    print("skipped:", skipped)
    print("wrote", args.out_dir / "metrics.json")
    if required:
        failed_required = required_failures(combined['summary'], required)
        if 'A22' in required:
            seen = {(row['width'], row['kind']) for report in reports.values() for row in report['headers']}
            if not {(1440, 'normal'), (1440, 'overflow'), (375, 'normal'), (375, 'overflow')} <= seen:
                failed_required.append('A22 coverage')
            rule_seen = {(row['width'], row['kind'], row['scheme']) for report in reports.values() for row in report['headerRules']}
            if not {(w, kind, scheme) for w in (1440, 375) for kind in ('normal', 'overflow') for scheme in ('light', 'dark')} <= rule_seen:
                failed_required.append('A22 rule coverage')
        if 'A23' in required and not a23_synthetic_coverage(reports):
            failed_required.append('A23 synthetic coverage')
        if failed_required:
            print('필수 검사 실패:', ', '.join(failed_required))
            sys.exit(1)
    if args.strict_lightbox:
        strict_failures = [entry for entry in aggregate["A20"]
                           if not entry.get("na") and not entry["ok"]]
        if strict_failures:
            for entry in strict_failures:
                print("strict-lightbox 실패:", entry["detail"])
            sys.exit(1)


if __name__ == "__main__":
    main()
