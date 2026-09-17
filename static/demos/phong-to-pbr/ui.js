import { COMMON_LIMIT } from './mode-specs.js';
import { modeMetrics } from './pbr-math.js';

function formatValue(control, value) {
  if (control.type === 'checkbox') return value ? 'ON' : 'OFF';
  if (control.type === 'color') return String(value).toUpperCase();
  if (control.type === 'select') return control.options.find((option) => option[1] === value)?.[0] ?? value;
  const step = String(control.step);
  const decimals = step.includes('.') ? step.split('.')[1].length : 0;
  return Number(value).toFixed(Math.min(decimals, 2));
}

function setRangeFill(input) {
  const progress = (Number(input.value) - Number(input.min)) / (Number(input.max) - Number(input.min));
  input.style.setProperty('--fill', `${Math.max(0, Math.min(1, progress)) * 100}%`);
}

export function createLabUi(spec, mode, initialState, { onChange, onReset, onFullscreen }) {
  const lab = document.querySelector('#lab');
  const viewport = document.querySelector('#viewport');
  const veil = document.querySelector('#veil');
  const statusText = document.querySelector('#status-text');
  const controlsRoot = document.querySelector('#control-list');
  const metricsRoot = document.querySelector('#metrics');
  const canvasId = 'render-canvas';
  const inputs = new Map();
  const values = new Map();

  lab.classList.add(`mode-${mode}`);
  document.querySelector('#eyebrow').textContent = spec.eyebrow;
  document.querySelector('#title').textContent = spec.title;
  document.querySelector('#question').textContent = spec.question;
  document.querySelector('#badge-label').textContent = spec.badge.label;
  document.querySelector('#badge-value').textContent = spec.badge.value;
  document.querySelector('#limits').textContent = `${spec.limits} ${COMMON_LIMIT}`;
  const notice = document.querySelector('#notice');
  if (spec.notice) {
    notice.textContent = spec.notice;
    notice.hidden = false;
  }
  document.querySelector('#stage-labels').replaceChildren(...spec.stageLabels.map((label) => {
    const span = document.createElement('span');
    span.textContent = label;
    return span;
  }));
  if (spec.axes) {
    document.querySelector('#axis-x').textContent = spec.axes.x;
    document.querySelector('#axis-y').textContent = spec.axes.y;
    document.querySelector('#graph-axes').hidden = false;
  }

  function makeInput(control) {
    const input = document.createElement('input');
    input.id = `control-${control.id}`;
    input.type = control.type;
    if (control.type === 'range') {
      input.min = control.min;
      input.max = control.max;
      input.step = control.step;
    }
    return input;
  }

  for (const control of spec.controls) {
    const row = document.createElement('div');
    row.className = `control-row control-row--${control.type}`;
    const label = document.createElement('label');
    label.htmlFor = `control-${control.id}`;
    label.textContent = control.label;
    let input;
    if (control.type === 'select') {
      input = document.createElement('select');
      input.id = `control-${control.id}`;
      control.options.forEach(([text, value]) => input.add(new Option(text, value)));
    } else {
      input = makeInput(control);
    }
    const output = document.createElement('output');
    output.className = 'control-value';
    output.htmlFor = input.id;
    if (control.type !== 'checkbox') row.append(label, output, input);
    else row.append(label, input);
    const eventName = control.type === 'range' || control.type === 'color' ? 'input' : 'change';
    input.addEventListener(eventName, () => {
      let value = input.value;
      if (control.type === 'range') value = Number(value);
      if (control.type === 'checkbox') value = input.checked;
      output.value = formatValue(control, value);
      if (control.type === 'range') setRangeFill(input);
      onChange(control.id, value);
    });
    controlsRoot.append(row);
    inputs.set(control.id, input);
    values.set(control.id, output);
  }

  document.querySelector('#reset').addEventListener('click', onReset);
  document.querySelector('#fullscreen').addEventListener('click', onFullscreen);

  function renderState(state) {
    for (const control of spec.controls) {
      const input = inputs.get(control.id);
      const value = state[control.id];
      if (control.type === 'checkbox') input.checked = value;
      else input.value = value;
      values.get(control.id).value = formatValue(control, value);
      if (control.type === 'range') setRangeFill(input);
    }
    metricsRoot.replaceChildren(...modeMetrics(mode, state).map(([label, value]) => {
      const item = document.createElement('dl');
      item.className = 'metric';
      const term = document.createElement('dt');
      const description = document.createElement('dd');
      term.textContent = label;
      description.textContent = value;
      item.append(term, description);
      return item;
    }));
  }

  function replaceCanvas() {
    const previous = document.querySelector(`#${canvasId}`);
    const canvas = document.createElement('canvas');
    canvas.id = canvasId;
    canvas.setAttribute('aria-label', '실시간 WebGL 재질 렌더링');
    previous.replaceWith(canvas);
    return canvas;
  }

  renderState(initialState);
  return {
    lab,
    viewport,
    get canvas() { return document.querySelector(`#${canvasId}`); },
    renderState,
    replaceCanvas,
    showLoading(message = 'WebGL 렌더러를 준비하고 있습니다') {
      statusText.textContent = message;
      veil.classList.remove('is-hidden', 'is-error');
    },
    showReady() { veil.classList.add('is-hidden'); },
    showError(message) {
      statusText.textContent = message;
      veil.classList.add('is-error');
      veil.classList.remove('is-hidden');
      veil.querySelector('.loader')?.remove();
    },
  };
}

export function showFatalError(message) {
  document.querySelector('#title').textContent = '열 수 없는 실험입니다';
  document.querySelector('#question').textContent = message;
  document.querySelector('#control-list').replaceChildren();
  document.querySelector('#metrics').replaceChildren();
  const veil = document.querySelector('#veil');
  veil.classList.add('is-error');
  veil.querySelector('.loader')?.remove();
  document.querySelector('#status-text').textContent = message;
}
