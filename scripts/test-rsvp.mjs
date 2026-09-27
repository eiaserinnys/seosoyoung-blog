import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import vm from "node:vm";
import test from "node:test";

const scriptPath = fileURLToPath(new URL("../assets/js/rsvp.js", import.meta.url));
const source = readFileSync(scriptPath, "utf8");
const marker = '  document.addEventListener("keydown", handleKeys);\n';
assert.ok(source.includes(marker), "RSVP initialization hook should remain available");

function loadReader(texts) {
  const content = {};
  const paragraph = {
    parentElement: content,
    matches(selector) {
      return selector.startsWith("address,blockquote");
    }
  };
  const textNodes = texts.map((text) => {
    const nodeValue = typeof text === "string" ? text : text.nodeValue;
    const parentElement = typeof text === "string" ? paragraph : {
      parentElement: paragraph,
      nodeValue,
      matches: (selector) => text.math && selector === ".katex"
    };
    return { nodeValue, parentElement };
  });
  const meta = { appendChild() {} };
  const article = {
    querySelector(selector) {
      return selector === ".post-content" ? content : selector === ".post-meta" ? meta : null;
    }
  };
  content.parentElement = article;

  class FakeRange {
    setStart(node, offset) {
      this.startContainer = node;
      this.startOffset = offset;
    }
    setEnd(node, offset) {
      this.endContainer = node;
      this.endOffset = offset;
    }
    selectNodeContents(node) {
      this.setStart(node, 0);
      this.setEnd(node, node.nodeValue.length);
    }
  }

  class FakeHighlight {
    constructor() {
      this.ranges = [];
    }
    add(range) {
      this.ranges.push(range);
    }
    clear() {
      this.ranges = [];
    }
  }

  const highlights = new Map();
  const document = {
    querySelector() {
      return article;
    },
    createTreeWalker() {
      let index = 0;
      return { nextNode: () => textNodes[index++] || null };
    },
    createRange: () => new FakeRange(),
    createElement: () => ({ addEventListener() {}, classList: { add() {} } }),
    createTextNode: (nodeValue) => ({ nodeValue }),
    addEventListener() {}
  };
  const context = {
    document,
    NodeFilter: { SHOW_TEXT: 4 },
    window: { CSS: { highlights }, Highlight: FakeHighlight }
  };
  vm.createContext(context);
  const instrumentedSource = source.replace(
    marker,
    `  globalThis.__rsvpTest = { collectTokens, initHighlights, updateHighlights, getSentenceStarts: () => sentenceStarts };\n${marker}`
  );
  vm.runInContext(instrumentedSource, context);
  return { api: context.__rsvpTest, highlights, textNodes };
}

test("omits both parenthesis styles while preserving suffixes, brackets, and quotes", () => {
  const reader = loadReader([
    "미시카 칼로프(Mishka ",
    "Kharlov)는 [위키]이고, “별칭”（설명）이다."
  ]);
  const originalText = reader.textNodes.map((node) => node.nodeValue);
  const tokens = reader.api.collectTokens();

  assert.deepEqual(Array.from(tokens, (token) => token.text), [
    "미시카",
    "칼로프는",
    "[위키]이고,",
    "“별칭”이다."
  ]);
  assert.deepEqual(reader.textNodes.map((node) => node.nodeValue), originalText);
});

test("hidden punctuation does not affect sentence starts or token count", () => {
  const reader = loadReader(["첫 문장(숨긴다. 계속) 끝. 둘째(English) 문장!"]);
  const tokens = reader.api.collectTokens();

  assert.deepEqual(Array.from(tokens, (token) => token.text), ["첫", "문장", "끝.", "둘째", "문장!"]);
  assert.deepEqual(Array.from(reader.api.getSentenceStarts()), [0, 3]);
  assert.deepEqual(Array.from(tokens, (token) => token.sentenceStart), [0, 0, 0, 3, 3]);
});

test("omits inline math inside parentheses and keeps the adjacent suffix", () => {
  const reader = loadReader(["식(", { nodeValue: "x²", math: true }, ")는 값."]);
  const tokens = reader.api.collectTokens();

  assert.deepEqual(Array.from(tokens, (token) => token.text), ["식는", "값."]);
  assert.equal(tokens.some((token) => token.isMath), false);
});

test("word highlighting maps each visible fragment back to the original text", () => {
  const reader = loadReader(["미시카 칼로프(Mishka ", "Kharlov)는 [위키]이고, “별칭”（설명）이다."]);
  const tokens = reader.api.collectTokens();
  const token = tokens.find((item) => item.text === "칼로프는");

  assert.ok(token);
  assert.deepEqual(Array.from(token.highlightRanges, (range) =>
    range.startContainer.nodeValue.slice(range.startOffset, range.endOffset)
  ), ["칼로프", "는"]);
  reader.api.initHighlights();
  reader.api.updateHighlights(token);
  assert.equal(reader.highlights.get("rsvp-word").ranges.length, 2);
});
