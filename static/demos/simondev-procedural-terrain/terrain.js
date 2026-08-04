import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import GUI from 'https://cdn.jsdelivr.net/npm/lil-gui@0.19.2/+esm';
import { fragmentShader, vertexShader } from './terrain-shaders.js';

export const TRICK_INVENTORY = Object.freeze([
  { id: 1, label: '하이트맵 기초', control: 'frequency + amplitude' },
  { id: 2, label: 'fBM과 pow 재조형', control: 'octaves + lacunarity + gain + reshapePower' },
  { id: 3, label: 'Ridged noise', control: 'noiseType: ridged' },
  { id: 4, label: 'Voronoi noise', control: 'noiseType: voronoi' },
  { id: 5, label: 'fBM × 선택 노이즈', control: 'featureFbm' },
  { id: 6, label: '미분 기반 침식', control: 'erosion + erosionStrength' },
  { id: 7, label: '테라스', control: 'terrace + terraceSteps' },
  { id: 8, label: '저주파 테라스 + 풍화 fBM', control: 'combinedPreset' },
  { id: 9, label: '거리 안개', control: 'distanceFog' },
  { id: 10, label: 'Crytek 높이 안개', control: 'heightFog + fogDensity' },
  { id: 11, label: '소광 / 산란 분리', control: 'scatterSeparated' },
]);

const settings = {
  frequency: 0.48,
  amplitude: 11.5,
  octaves: 6,
  lacunarity: 2.03,
  gain: 0.49,
  reshapePower: 2.8,
  noiseType: 'ridged',
  featureFbm: true,
  erosion: true,
  erosionStrength: 2.1,
  terrace: true,
  terraceSteps: 9,
  combinedPreset: true,
  distanceFog: true,
  heightFog: true,
  fogDensity: 0.22,
  scatterSeparated: true,
  autoFlight: true,
};

const PRESETS = Object.freeze({
  Basic: {
    frequency: 0.34, amplitude: 8.5, octaves: 1, reshapePower: 1,
    noiseType: 'value', featureFbm: false, erosion: false, terrace: false,
    combinedPreset: false, distanceFog: true, heightFog: false, scatterSeparated: false,
  },
  fBM: {
    frequency: 0.36, amplitude: 10, octaves: 6, reshapePower: 3,
    noiseType: 'value', featureFbm: true, erosion: false, terrace: false,
    combinedPreset: false, distanceFog: true, heightFog: false, scatterSeparated: false,
  },
  Ridged: {
    frequency: 0.45, amplitude: 10.5, octaves: 6, reshapePower: 2.2,
    noiseType: 'ridged', featureFbm: true, erosion: false, terrace: false,
    combinedPreset: false, distanceFog: true, heightFog: false, scatterSeparated: false,
  },
  Voronoi: {
    frequency: 0.4, amplitude: 8.8, octaves: 5, reshapePower: 1.65,
    noiseType: 'voronoi', featureFbm: true, erosion: false, terrace: false,
    combinedPreset: false, distanceFog: true, heightFog: false, scatterSeparated: false,
  },
  Layered: {
    frequency: 0.46, amplitude: 11, octaves: 6, reshapePower: 2.7,
    noiseType: 'value', featureFbm: true, erosion: true, erosionStrength: 2.2,
    terrace: true, terraceSteps: 9, combinedPreset: true,
    distanceFog: true, heightFog: false, scatterSeparated: false,
  },
  Full: {
    frequency: 0.48, amplitude: 11.5, octaves: 6, lacunarity: 2.03, gain: 0.49,
    reshapePower: 2.65, noiseType: 'value', featureFbm: true,
    erosion: true, erosionStrength: 2.1, terrace: true, terraceSteps: 9,
    combinedPreset: true, distanceFog: true, heightFog: true,
    fogDensity: 0.22, scatterSeparated: true,
  },
});

const noiseModes = { value: 0, ridged: 1, voronoi: 2 };
const loading = document.querySelector('#loading');
const errorPanel = document.querySelector('#error');
const canvas = document.querySelector('#terrain');

function makeUniforms() {
  return {
    uTime: { value: 0 },
    uFrequency: { value: settings.frequency },
    uAmplitude: { value: settings.amplitude },
    uOctaves: { value: settings.octaves },
    uLacunarity: { value: settings.lacunarity },
    uGain: { value: settings.gain },
    uReshapePower: { value: settings.reshapePower },
    uNoiseMode: { value: noiseModes[settings.noiseType] },
    uFeatureFbm: { value: Number(settings.featureFbm) },
    uErosionEnabled: { value: Number(settings.erosion) },
    uErosionStrength: { value: settings.erosionStrength },
    uTerraceEnabled: { value: Number(settings.terrace) },
    uTerraceSteps: { value: settings.terraceSteps },
    uCombinedPreset: { value: Number(settings.combinedPreset) },
    uDistanceFogEnabled: { value: Number(settings.distanceFog) },
    uHeightFogEnabled: { value: Number(settings.heightFog) },
    uFogDensity: { value: settings.fogDensity },
    uScatterSeparated: { value: Number(settings.scatterSeparated) },
    uSkyColor: { value: new THREE.Color('#8ca9b0') },
  };
}

function syncUniforms(uniforms) {
  uniforms.uFrequency.value = settings.frequency;
  uniforms.uAmplitude.value = settings.amplitude;
  uniforms.uOctaves.value = settings.featureFbm || settings.noiseType === 'value' ? settings.octaves : 1;
  uniforms.uLacunarity.value = settings.lacunarity;
  uniforms.uGain.value = settings.gain;
  uniforms.uReshapePower.value = settings.reshapePower;
  uniforms.uNoiseMode.value = noiseModes[settings.noiseType];
  uniforms.uFeatureFbm.value = Number(settings.featureFbm);
  uniforms.uErosionEnabled.value = Number(settings.erosion);
  uniforms.uErosionStrength.value = settings.erosionStrength;
  uniforms.uTerraceEnabled.value = Number(settings.terrace);
  uniforms.uTerraceSteps.value = settings.terraceSteps;
  uniforms.uCombinedPreset.value = Number(settings.combinedPreset);
  uniforms.uDistanceFogEnabled.value = Number(settings.distanceFog);
  uniforms.uHeightFogEnabled.value = Number(settings.heightFog);
  uniforms.uFogDensity.value = settings.fogDensity;
  uniforms.uScatterSeparated.value = Number(settings.scatterSeparated);
}

function createGui(uniforms) {
  const gui = new GUI({ title: '11 TERRAIN TRICKS', width: 328 });
  const controllers = [];
  const track = (controller) => {
    controllers.push(controller);
    controller.onChange(() => syncUniforms(uniforms));
    return controller;
  };

  const presetActions = {};
  const applyPreset = (name) => {
    Object.assign(settings, PRESETS[name]);
    syncUniforms(uniforms);
    controllers.forEach((controller) => controller.updateDisplay());
    document.body.dataset.preset = name.toLowerCase();
  };

  Object.keys(PRESETS).forEach((name) => {
    presetActions[name] = () => applyPreset(name);
  });

  const presets = gui.addFolder('PRESETS');
  Object.keys(PRESETS).forEach((name) => presets.add(presetActions, name));

  const basic = gui.addFolder('1 · 하이트맵 기초');
  track(basic.add(settings, 'frequency', 0.08, 1.2, 0.01).name('주파수'));
  track(basic.add(settings, 'amplitude', 2, 18, 0.1).name('진폭'));

  const fbm = gui.addFolder('2 · fBM + pow 재조형');
  track(fbm.add(settings, 'octaves', 1, 8, 1).name('옥타브'));
  track(fbm.add(settings, 'lacunarity', 1.4, 3.2, 0.01).name('라쿠나리티'));
  track(fbm.add(settings, 'gain', 0.2, 0.78, 0.01).name('게인'));
  track(fbm.add(settings, 'reshapePower', 0.5, 5, 0.05).name('pow 지수 k'));

  const noise = gui.addFolder('3–5 · Ridged / Voronoi');
  track(noise.add(settings, 'noiseType', {
    'Value · 기본': 'value',
    'Ridged · 바위 능선': 'ridged',
    'Voronoi · 셀 곰보': 'voronoi',
  }).name('3–4 · 노이즈'));
  track(noise.add(settings, 'featureFbm').name('5 · 선택 노이즈 fBM'));

  const erosion = gui.addFolder('6 · 미분 기반 침식');
  track(erosion.add(settings, 'erosion').name('풍화 켜기'));
  track(erosion.add(settings, 'erosionStrength', 0, 5, 0.05).name('풍화 강도'));

  const terraces = gui.addFolder('7–8 · 테라스와 조합');
  track(terraces.add(settings, 'terrace').name('7 · 테라스'));
  track(terraces.add(settings, 'terraceSteps', 2, 18, 1).name('계단 수'));
  track(terraces.add(settings, 'combinedPreset').name('8 · 저주파+풍화 합성'));

  const fog = gui.addFolder('9–11 · 대기');
  track(fog.add(settings, 'distanceFog').name('9 · 거리 안개'));
  track(fog.add(settings, 'heightFog').name('10 · 높이 안개'));
  track(fog.add(settings, 'fogDensity', 0.02, 0.55, 0.005).name('높이 안개 밀도'));
  track(fog.add(settings, 'scatterSeparated').name('11 · 소광/산란 분리'));

  const cameraFolder = gui.addFolder('CAMERA');
  track(cameraFolder.add(settings, 'autoFlight').name('완만한 자동 비행'));

  presets.open();
  basic.open();
  if (window.matchMedia('(max-width: 720px)').matches) gui.close();
  return { gui, applyPreset };
}

function showFailure(error) {
  console.error('[terrain-demo] initialization failed', error);
  loading.classList.add('is-hidden');
  errorPanel.hidden = false;
}

function init() {
  if (!canvas.getContext('webgl2') && !canvas.getContext('webgl')) {
    throw new Error('WebGL is unavailable');
  }

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, window.innerWidth < 720 ? 1.35 : 1.8));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.08;
  renderer.setClearColor('#8ca9b0');
  renderer.debug.checkShaderErrors = true;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color('#8ca9b0');
  const camera = new THREE.PerspectiveCamera(48, 1, 0.1, 140);
  camera.position.set(23, 14, 23);

  const controls = new OrbitControls(camera, canvas);
  controls.target.set(0, 1.8, 0);
  controls.enableDamping = true;
  controls.dampingFactor = 0.055;
  controls.minDistance = 9;
  controls.maxDistance = 58;
  controls.maxPolarAngle = Math.PI * 0.48;
  controls.addEventListener('start', () => { settings.autoFlight = false; });

  const uniforms = makeUniforms();
  const material = new THREE.ShaderMaterial({
    uniforms,
    vertexShader,
    fragmentShader,
    side: THREE.DoubleSide,
  });
  const geometry = new THREE.PlaneGeometry(48, 48, 256, 256);
  geometry.rotateX(-Math.PI / 2);
  const terrain = new THREE.Mesh(geometry, material);
  scene.add(terrain);

  const { gui, applyPreset } = createGui(uniforms);
  applyPreset('Full');

  const resize = () => {
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    renderer.setSize(width, height, false);
    camera.aspect = width / Math.max(height, 1);
    camera.updateProjectionMatrix();
  };
  const observer = new ResizeObserver(resize);
  observer.observe(canvas);
  resize();

  const clock = new THREE.Clock();
  let elapsed = 0;
  const renderFrame = () => {
    const delta = Math.min(clock.getDelta(), 0.05);
    elapsed += delta;
    uniforms.uTime.value = elapsed;

    if (settings.autoFlight) {
      const radius = 32;
      camera.position.x = Math.cos(elapsed * 0.055) * radius;
      camera.position.z = Math.sin(elapsed * 0.055) * radius;
      camera.position.y = 13.5 + Math.sin(elapsed * 0.11) * 1.5;
    }

    controls.update();
    renderer.render(scene, camera);
    if (!window.__terrainDemo?.ready) {
      loading.classList.add('is-hidden');
      window.__terrainDemo.ready = true;
      window.dispatchEvent(new CustomEvent('terrain-demo-ready'));
    }
  };
  renderer.setAnimationLoop(renderFrame);

  window.__terrainDemo = {
    ready: false,
    inventory: TRICK_INVENTORY,
    settings,
    applyPreset,
    setSettings(patch) {
      Object.assign(settings, patch);
      syncUniforms(uniforms);
      gui.controllersRecursive().forEach((controller) => controller.updateDisplay());
    },
    setControl(property, value) {
      const controller = gui.controllersRecursive().find((entry) => entry.property === property);
      if (!controller) throw new Error(`Unknown terrain control: ${property}`);
      controller.setValue(value);
    },
    getControlInventory() {
      return gui.controllersRecursive().map((controller) => controller.property);
    },
    setCamera(position, target = [0, 1.8, 0]) {
      camera.position.fromArray(position);
      controls.target.fromArray(target);
      controls.update();
    },
    pause() {
      renderer.setAnimationLoop(null);
    },
    renderOnce() {
      renderFrame();
    },
    resume() {
      clock.getDelta();
      renderer.setAnimationLoop(renderFrame);
    },
    renderer,
  };

  window.addEventListener('beforeunload', () => {
    renderer.setAnimationLoop(null);
    observer.disconnect();
    gui.destroy();
    geometry.dispose();
    material.dispose();
    renderer.dispose();
  }, { once: true });
}

try {
  init();
} catch (error) {
  showFailure(error);
}
