import { existsSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, extname, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const defaultRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');

function options(args) {
  const result = { root: defaultRoot, config: 'scripts/ui-css-check.config.json', mode: 'check' };
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg === '--root' || arg === '--config') {
      if (!args[i + 1] || args[i + 1].startsWith('--')) throw new Error(`${arg}에 경로가 필요합니다`);
      result[arg.slice(2)] = args[++i];
    } else if (arg === '--init' || arg === '--update') {
      if (result.mode !== 'check') throw new Error('--init과 --update는 함께 쓸 수 없습니다');
      result.mode = arg.slice(2);
    } else {
      throw new Error(`알 수 없는 인자: ${arg}`);
    }
  }
  result.root = resolve(result.root);
  return result;
}

function filesUnder(root, directories, extension) {
  const paths = new Set();
  function visit(path) {
    for (const entry of readdirSync(path, { withFileTypes: true })) {
      const child = resolve(path, entry.name);
      if (entry.isDirectory()) visit(child);
      else if (entry.isFile() && extname(entry.name) === extension) paths.add(child);
    }
  }
  for (const dir of directories) visit(resolve(root, dir));
  return [...paths].sort();
}

function posixPath(root, path) {
  return relative(root, path).split(sep).join('/');
}

function lineAt(text, offset) {
  return text.slice(0, offset).split('\n').length;
}

// Preserve offsets and line breaks so reported locations refer to the original CSS.
function withoutComments(text) {
  return text.replace(/\/\*[\s\S]*?\*\//g, comment => comment.replace(/[^\r\n]/g, ' '));
}

function closingParen(value, opening) {
  let depth = 0;
  for (let i = opening; i < value.length; i++) {
    if (value[i] === '(') depth++;
    if (value[i] === ')' && --depth === 0) return i;
  }
  return value.length - 1;
}

function stripVars(value) {
  const pattern = /\bvar\s*\(/gi;
  let result = '';
  let cursor = 0;
  for (const match of value.matchAll(pattern)) {
    if (match.index < cursor) continue;
    result += value.slice(cursor, match.index);
    cursor = closingParen(value, match.index + match[0].length - 1) + 1;
  }
  return result + value.slice(cursor);
}

function hasColorLiteral(value) {
  if (/#(?:[\da-f]{8}|[\da-f]{6}|[\da-f]{4}|[\da-f]{3})(?![\w-])/i.test(value)) return true;
  const pattern = /\b(?:rgba?|hsla?|oklch|oklab|lab|lch|color)\s*\(/gi;
  for (const match of value.matchAll(pattern)) {
    const start = match.index + match[0].length;
    const end = closingParen(value, start - 1);
    if (!/\bvar\s*\(/i.test(value.slice(start, end))) return true;
  }
  return false;
}

function hasLength(value, units, radius = false) {
  const pattern = new RegExp(`(?:^|[^\\w.])([-+]?(?:\\d*\\.)?\\d+)(${units})\\b`, 'gi');
  return [...stripVars(value).matchAll(pattern)].some(match => {
    const number = Number(match[1]);
    return number !== 0 && !(radius && match[2].toLowerCase() === 'px' && number >= 999);
  });
}

function cssRules(property, value) {
  const rules = [];
  if (hasColorLiteral(value)) rules.push('color-literal');
  if ((['font-size', 'font'].includes(property) && !/\bvar\s*\(/i.test(value) && /(?:\d*\.)?\d+(?:px|rem|em)\b/i.test(value)) ||
      (property === 'font-family' && !/\bvar\s*\(/i.test(value) && !/^inherit(?:\s*!important)?\s*$/i.test(value.trim()))) {
    rules.push('font-literal');
  }
  if (/^border-(?:[a-z]+-)*radius$/.test(property) && hasLength(value, 'px|rem|em', true)) rules.push('radius-literal');
  if (/^(?:(?:padding|margin)(?:-[a-z]+)*|gap|row-gap|column-gap)$/.test(property) && hasLength(value, 'px|rem')) rules.push('spacing-literal');
  if (property === 'user-select' || property === '-webkit-user-select') rules.push('selection-outside-policy');
  if ((property === 'outline' && /^(?:none|0)/i.test(value.trim())) ||
      (property === 'outline-style' && /^none(?:\s*!important)?\s*$/i.test(value.trim()))) rules.push('outline-none');
  return rules;
}

function collect(root, config) {
  const findings = {};
  function add(rule, path, line, source) {
    if (!config.rules[rule]?.enabled) return;
    findings[rule] ??= {};
    findings[rule][path] ??= [];
    findings[rule][path].push({ line, source });
  }
  for (const file of filesUnder(root, config.cssRoots, '.css')) {
    const path = posixPath(root, file);
    const original = readFileSync(file, 'utf8');
    const css = withoutComments(original);
    const declarations = /(?:^|[;{}])\s*([-\w]+)\s*:\s*([^;{}]*)(?=[;}]|$)/g;
    for (const match of css.matchAll(declarations)) {
      const property = match[1].toLowerCase();
      const propertyOffset = match.index + match[0].indexOf(match[1]);
      const end = match.index + match[0].length;
      const source = original.slice(propertyOffset, end + (css[end] === ';' ? 1 : 0)).trim();
      for (const rule of cssRules(property, match[2])) {
        if (['color-literal', 'font-literal', 'radius-literal', 'spacing-literal'].includes(rule) && config.tokenFiles.includes(path)) continue;
        if (rule === 'selection-outside-policy' && config.selectionPolicyFiles.includes(path)) continue;
        add(rule, path, lineAt(original, propertyOffset), source);
      }
    }
  }
  for (const file of filesUnder(root, config.tsxRoots, '.tsx')) {
    const path = posixPath(root, file);
    if (config.tsxExclude.some(part => path.includes(part))) continue;
    const original = readFileSync(file, 'utf8');
    for (const [rule, pattern] of [
      ['tw-text-arbitrary', /text-\[(?=\d)/g],
      ['tw-rounded-arbitrary', /rounded-(?:[a-z]+-)?\[(?!var\(|--)/g],
    ]) {
      for (const match of original.matchAll(pattern)) {
        const line = lineAt(original, match.index);
        const start = original.lastIndexOf('\n', match.index) + 1;
        const end = original.indexOf('\n', match.index);
        add(rule, path, line, original.slice(start, end === -1 ? undefined : end).trim());
      }
    }
  }
  return findings;
}

function sortedCounts(counts) {
  return Object.fromEntries(Object.keys(counts).sort().map(rule => [rule,
    Object.fromEntries(Object.entries(counts[rule]).filter(([, count]) => count > 0).sort(([a], [b]) => a < b ? -1 : a > b ? 1 : 0)),
  ]));
}

function writeBaseline(path, counts) {
  writeFileSync(path, `${JSON.stringify(sortedCounts(counts), null, 2)}\n`, 'utf8');
}

function main() {
  const { root, config: configPath, mode } = options(process.argv.slice(2));
  const config = JSON.parse(readFileSync(resolve(root, configPath), 'utf8'));
  const baselinePath = resolve(root, config.baseline);
  if (mode === 'init' && existsSync(baselinePath)) throw new Error(`기준치 파일이 이미 있습니다: ${config.baseline}`);
  const baseline = mode === 'init' ? {} : JSON.parse(readFileSync(baselinePath, 'utf8'));
  const findings = collect(root, config);
  const current = Object.fromEntries(Object.keys(config.rules).map(rule => [rule,
    Object.fromEntries(Object.entries(findings[rule] ?? {}).map(([path, entries]) => [path, entries.length])),
  ]));
  if (mode === 'init') {
    writeBaseline(baselinePath, current);
    console.log(`기준치 생성: ${config.baseline}`);
    return 0;
  }
  if (mode === 'update') {
    const updated = {};
    for (const rule of Object.keys(baseline)) {
      updated[rule] = {};
      for (const [path, count] of Object.entries(baseline[rule])) {
        updated[rule][path] = config.rules[rule]?.enabled ? Math.min(count, current[rule]?.[path] ?? 0) : count;
      }
    }
    writeBaseline(baselinePath, updated);
    console.log(`기준치 감소분 반영: ${config.baseline}`);
    return 0;
  }
  let increased = false;
  const decreased = [];
  const totals = [];
  for (const [rule, setting] of Object.entries(config.rules)) {
    if (!setting.enabled) {
      totals.push(`${rule}: 비활성`);
      continue;
    }
    const paths = new Set([...Object.keys(baseline[rule] ?? {}), ...Object.keys(current[rule])]);
    let total = 0;
    for (const path of [...paths].sort()) {
      const oldCount = baseline[rule]?.[path] ?? 0;
      const count = current[rule][path] ?? 0;
      total += count;
      if (count > oldCount) {
        increased = true;
        console.log(`${rule} ${path}: 기준치 ${oldCount}, 지금 ${count}`);
        for (const entry of findings[rule][path]) console.log(`${path}:${entry.line}: ${entry.source}`);
        console.log(`대신: ${setting.hint}`);
        console.log('새로 적은 값을 토큰으로 바꾼다. 까닭이 있어 남겨야 하면 기준치 파일의 그 숫자를 손으로 올리고 PR 설명에 까닭을 적는다.');
      } else if (count < oldCount) {
        decreased.push(`${rule} ${path}: ${oldCount} → ${count}`);
      }
    }
    totals.push(`${rule}: ${total}`);
  }
  if (decreased.length) {
    console.log('기준치를 낮출 수 있다: node scripts/check-ui-css.mjs --update');
    for (const target of decreased) console.log(target);
  }
  if (!increased && !decreased.length) {
    for (const total of totals) console.log(total);
  }
  return increased ? 1 : 0;
}

try {
  process.exitCode = main();
} catch (error) {
  console.error(`UI CSS 검사 오류: ${error.message}`);
  process.exitCode = 2;
}
