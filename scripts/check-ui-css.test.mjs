import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { afterEach, test } from 'node:test';

const checker = resolve('scripts/check-ui-css.mjs');
const roots = [];
const ruleIds = [
  'color-literal', 'font-literal', 'radius-literal', 'spacing-literal',
  'selection-outside-policy', 'outline-none', 'tw-text-arbitrary', 'tw-rounded-arbitrary',
];

afterEach(() => {
  for (const root of roots.splice(0)) rmSync(root, { recursive: true, force: true });
});

function fixture() {
  const root = mkdtempSync(join(tmpdir(), 'ui-css-check-'));
  roots.push(root);
  mkdirSync(join(root, 'src'), { recursive: true });
  const config = {
    cssRoots: ['src'], tsxRoots: ['src'], tsxExclude: ['.test.', '/e2e/', '.stories.'],
    tokenFiles: ['src/tokens.css'], selectionPolicyFiles: ['src/selection.css'],
    baseline: 'baseline.json',
    rules: Object.fromEntries(ruleIds.map(id => [id, { enabled: true, hint: `대신 ${id} 토큰` }])),
  };
  writeFileSync(join(root, 'config.json'), JSON.stringify(config));
  return {
    root,
    write(path, contents) { writeFileSync(join(root, path), contents); },
    run(...args) {
      return spawnSync(process.execPath, [checker, '--root', root, '--config', 'config.json', ...args], { encoding: 'utf8' });
    },
    baseline() { return JSON.parse(readFileSync(join(root, 'baseline.json'), 'utf8')); },
  };
}

test('기준치와 같으면 규칙별 합계를 출력하고 통과한다', () => {
  const f = fixture();
  f.write('src/a.css', '.a { color: #fff; padding: 4px; }');
  assert.equal(f.run('--init').status, 0);
  const result = f.run();
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /color-literal.*1/);
  assert.match(result.stdout, /spacing-literal.*1/);
});

test('리터럴이 늘면 원본 줄과 hint를 출력하고 실패한다', () => {
  const f = fixture();
  f.write('src/a.css', '.a {\n  padding: 2px;\n}\n');
  assert.equal(f.run('--init').status, 0);
  f.write('src/a.css', '.a {\n  padding: 2px;\n  padding: 13px;\n}\n');
  const result = f.run();
  assert.equal(result.status, 1);
  assert.match(result.stdout, /spacing-literal.*src\/a\.css.*1.*2/);
  assert.match(result.stdout, /src\/a\.css:3: padding: 13px/);
  assert.match(result.stdout, /대신 spacing-literal 토큰/);
  assert.match(result.stdout, /PR 설명/);
});

test('새 CSS와 TSX 파일은 기준치 0에서 세며 임의값을 각각 센다', () => {
  const f = fixture();
  assert.equal(f.run('--init').status, 0);
  f.write('src/new.css', '.a { margin: 4px; }');
  f.write('src/new.tsx', '<div className="text-[13px] rounded-[5px] rounded-tl-[4px]" />');
  f.write('src/ignored.test.tsx', '<div className="text-[15px]" />');
  const result = f.run();
  assert.equal(result.status, 1);
  assert.match(result.stdout, /spacing-literal.*src\/new\.css.*0.*1/);
  assert.match(result.stdout, /tw-text-arbitrary.*src\/new\.tsx.*0.*1/);
  assert.match(result.stdout, /tw-rounded-arbitrary.*src\/new\.tsx.*0.*2/);
  assert.doesNotMatch(result.stdout, /ignored\.test/);
});

test('여러 줄 주석과 토큰 및 선택 정책 파일은 해당 규칙에서 제외한다', () => {
  const f = fixture();
  f.write('src/a.css', '/* color: #123;\n padding: 20px; */\n.a { color: #123; user-select: none; }');
  f.write('src/tokens.css', '.a { color: #fff; font-size: 12px; margin: 5px; user-select: none; }');
  f.write('src/selection.css', '.a { user-select: none; -webkit-user-select: text; color: #fff; }');
  assert.equal(f.run('--init').status, 0);
  const b = f.baseline();
  assert.equal(b['color-literal']['src/a.css'], 1);
  assert.equal(b['color-literal']['src/selection.css'], 1);
  assert.equal(b['color-literal']['src/tokens.css'], undefined);
  assert.equal(b['spacing-literal']?.['src/a.css'], undefined);
  assert.equal(b['selection-outside-policy']['src/tokens.css'], 1);
  assert.equal(b['selection-outside-policy']['src/selection.css'], undefined);
});

test('var만 쓰는 선언은 세지 않고 혼합된 실제 리터럴은 센다', () => {
  const f = fixture();
  f.write('src/a.css', `.a {
    color: rgb(var(--rgb)); font-size: var(--size); font-family: var(--font);
    border-radius: var(--radius); padding: var(--space); margin: 0; gap: 0px;
    padding-inline: var(--space) 4px; border-top-left-radius: var(--radius) 2em;
    border-bottom-right-radius: 999px; background: rgb(0 0 0) #fff;
  }`);
  assert.equal(f.run('--init').status, 0);
  const b = f.baseline();
  assert.equal(b['color-literal']['src/a.css'], 1);
  assert.equal(b['spacing-literal']['src/a.css'], 1);
  assert.equal(b['radius-literal']['src/a.css'], 1);
  assert.equal(b['font-literal']?.['src/a.css'], undefined);
});

test('--update는 감소분만 반영하고 0을 지우며 늘어난 수는 올리지 않는다', () => {
  const f = fixture();
  f.write('src/a.css', '.a { color: #fff; padding: 2px; margin: 4px; }');
  assert.equal(f.run('--init').status, 0);
  f.write('src/a.css', '.a { color: #fff; background: #000; padding: 2px; }');
  const update = f.run('--update');
  assert.equal(update.status, 0, update.stderr);
  const b = f.baseline();
  assert.equal(b['color-literal']['src/a.css'], 1);
  assert.equal(b['spacing-literal']['src/a.css'], 1);
  assert.equal(f.run().status, 1);
  f.write('src/a.css', '.a { color: var(--color); }');
  const decreased = f.run();
  assert.equal(decreased.status, 0);
  assert.match(decreased.stdout, /기준치를 낮출 수 있다: node scripts\/check-ui-css\.mjs --update/);
  assert.equal(f.run('--update').status, 0);
  const after = f.baseline();
  assert.equal(after['spacing-literal']?.['src/a.css'], undefined);
  assert.equal(after['color-literal']?.['src/a.css'], undefined);
  assert.equal(f.run().status, 0);
});

test('규칙별 선언과 오류 처리를 검사한다', () => {
  const f = fixture();
  f.write('src/a.css', `.a {
    font-size: 1rem; font-family: Arial; outline: none; outline-style: none;
    -webkit-user-select: none; padding: 3px 4px; color: hsl(0 0% 0%);
  }`);
  assert.equal(f.run('--init').status, 0);
  const b = f.baseline();
  assert.equal(b['font-literal']['src/a.css'], 2);
  assert.equal(b['outline-none']['src/a.css'], 2);
  assert.equal(b['selection-outside-policy']['src/a.css'], 1);
  assert.equal(b['spacing-literal']['src/a.css'], 1);
  assert.equal(b['color-literal']['src/a.css'], 1);
  rmSync(join(f.root, 'baseline.json'));
  assert.equal(f.run().status, 2);
});

test('색 함수와 hex는 선언별로 세고 토큰을 쓰는 함수와 상속 글꼴은 제외한다', () => {
  const f = fixture();
  f.write('src/a.css', `.a {
    color: #abc #abcd #aabbcc #aabbccdd;
    background: rgb(1 2 3) rgba(1, 2, 3, 1) hsl(0 0% 0%) hsla(0, 0%, 0%, 1);
    border-color: oklch(0 0 0) oklab(0 0 0) lab(0 0 0) lch(0 0 0) color(srgb 0 0 0);
    fill: rgb(var(--rgb)); stroke: color(srgb var(--channels));
    font-family: inherit !important;
    outline: 0px;
  }`);
  assert.equal(f.run('--init').status, 0);
  const b = f.baseline();
  assert.equal(b['color-literal']['src/a.css'], 3);
  assert.equal(b['font-literal']?.['src/a.css'], undefined);
  assert.equal(b['outline-none']['src/a.css'], 1);
  assert.equal(f.run('--init').status, 2);
});

test('둥근 모서리 임의값은 토큰을 제외하고 센다', () => {
  const f = fixture();
  f.write('src/a.tsx', '<div className="rounded-[var(--radius-lg)] rounded-t-[--radius] rounded-[8px] rounded-tl-[4px]" />');
  assert.equal(f.run('--init').status, 0);
  assert.equal(f.baseline()['tw-rounded-arbitrary']['src/a.tsx'], 2);
});

test('font 줄임 속성의 직접 크기는 세고 상속과 토큰은 제외한다', () => {
  const f = fixture();
  f.write('src/a.css', '.a { font: 400 16px/24px sans-serif; font: 600 1rem/1.5 sans-serif; font: inherit; font: var(--v3-type-body); }');
  assert.equal(f.run('--init').status, 0);
  assert.equal(f.baseline()['font-literal']['src/a.css'], 2);
});
