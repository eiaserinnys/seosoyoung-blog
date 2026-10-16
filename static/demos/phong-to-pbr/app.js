import { createDefaultState, MODE_IDS, MODE_SPECS } from './mode-specs.js';
import { LabRenderer } from './renderer.js';
import { createLabUi, showFatalError } from './ui.js';

const params = new URLSearchParams(window.location.search);
const mode = params.get('mode') ?? 'studio';

if (!MODE_IDS.includes(mode)) {
  const message = `알 수 없는 mode “${mode}”입니다. 사용할 수 있는 값: ${MODE_IDS.join(', ')}`;
  showFatalError(message);
  window.__PBR_LAB__ = { ready: false, mode, error: message };
} else {
  startLab(mode, MODE_SPECS[mode]);
}

function startLab(activeMode, spec) {
  let state = createDefaultState(spec);
  let renderer = null;
  let isIntersecting = false;
  let releaseTimer = 0;
  let lastRenderCount = 0;
  let ready = false;
  let contextState = 'deferred';

  const ui = createLabUi(spec, activeMode, state, {
    onChange(id, value) {
      state = { ...state, [id]: value };
      ui.renderState(state);
      if (renderer) renderer.updateState(state);
      else if (isIntersecting && !document.hidden) activate();
    },
    onReset() {
      state = createDefaultState(spec);
      ui.renderState(state);
      if (renderer) renderer.updateState(state);
      else if (isIntersecting && !document.hidden) activate();
    },
    onFullscreen() {
      if (document.fullscreenElement) document.exitFullscreen?.();
      else ui.lab.requestFullscreen?.();
    },
  });

  function release(reason = 'released') {
    window.clearTimeout(releaseTimer);
    releaseTimer = 0;
    if (renderer) {
      lastRenderCount = renderer.renderCount;
      renderer.dispose();
      renderer = null;
      ui.replaceCanvas();
    }
    contextState = reason;
  }

  function scheduleRelease() {
    window.clearTimeout(releaseTimer);
    releaseTimer = window.setTimeout(() => {
      if (!isIntersecting || document.hidden) release('released-offscreen');
    }, 1400);
  }

  function activate() {
    if (renderer || !isIntersecting || document.hidden) return;
    window.clearTimeout(releaseTimer);
    releaseTimer = 0;
    ui.showLoading(contextState.startsWith('released') ? 'WebGL 컨텍스트를 다시 여는 중입니다' : undefined);
    contextState = 'initializing';
    try {
      renderer = new LabRenderer(ui.canvas, activeMode, state, {
        onFrame(frame) {
          lastRenderCount = frame.renderCount;
          ready = true;
          contextState = 'active';
          ui.showReady();
        },
        onYield() {
          if (!isIntersecting || document.hidden) release('released-for-peer');
        },
      });
    } catch (error) {
      contextState = 'error';
      ui.showError(`WebGL을 시작하지 못했습니다: ${error.message}`);
      console.error('[PBR Lab] WebGL initialization failed', error);
    }
  }

  const observer = 'IntersectionObserver' in window
    ? new IntersectionObserver(([entry]) => {
      isIntersecting = entry.isIntersecting;
      if (isIntersecting) {
        renderer?.setVisible(true);
        activate();
      } else {
        renderer?.setVisible(false);
        scheduleRelease();
      }
    }, { rootMargin: '220px 0px', threshold: 0.01 })
    : null;

  if (observer) observer.observe(ui.viewport);
  else {
    isIntersecting = true;
    activate();
  }

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      renderer?.setVisible(false);
      release('released-hidden');
    } else if (isIntersecting) {
      activate();
    }
  });

  window.addEventListener('pagehide', () => {
    observer?.disconnect();
    release('released-pagehide');
  }, { once: true });

  const bridge = {
    get ready() { return ready; },
    get mode() { return activeMode; },
    get renderCount() { return renderer?.renderCount ?? lastRenderCount; },
    get contextState() { return contextState; },
    getState() { return { ...state }; },
    setControl(id, value) {
      const control = spec.controls.find((candidate) => candidate.id === id);
      if (!control) throw new Error(`Unknown control: ${id}`);
      let normalized = value;
      if (control.type === 'range') normalized = Math.max(control.min, Math.min(control.max, Number(value)));
      if (control.type === 'checkbox') normalized = Boolean(value);
      state = { ...state, [id]: normalized };
      ui.renderState(state);
      if (renderer) renderer.updateState(state);
      else if (isIntersecting && !document.hidden) activate();
      return { ...state };
    },
    reset() {
      state = createDefaultState(spec);
      ui.renderState(state);
      renderer?.updateState(state);
      return { ...state };
    },
  };
  window.__PBR_LAB__ = bridge;
}
