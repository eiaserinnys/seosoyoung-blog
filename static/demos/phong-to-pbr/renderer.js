import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { createEnvironment } from './environment.js';
import { hexToLinearRgb } from './pbr-math.js';
import * as analyticShader from './shaders/analytic.js';
import * as materialShader from './shaders/material.js';
import * as studioShader from './shaders/studio.js';

const ANALYTIC_MODES = new Map([['ggx-d', 0], ['fresnel', 1], ['pipeline', 2]]);
const MATERIAL_MODES = new Map([['compare', 0], ['smith-g', 1], ['metalness', 2], ['normal', 3]]);
const TONE_MAPPERS = Object.freeze({ none: 0, reinhard: 1, aces: 2 });

function makeUniforms(state) {
  const color = hexToLinearRgb(state.baseColor);
  return {
    uResolution: { value: new THREE.Vector2(1, 1) },
    uMode: { value: 0 },
    uVisualMode: { value: 0 },
    uVariant: { value: 0 },
    uLegacyModel: { value: state.legacyModel === 'phong' ? 0 : 1 },
    uShininess: { value: state.shininess },
    uBaseColor: { value: new THREE.Vector3(...color) },
    uLightPosition: { value: new THREE.Vector3(4, 5, 3) },
    uLightDirection: { value: new THREE.Vector3(0.5, 0.7, 0.5).normalize() },
    uViewDirection: { value: new THREE.Vector3(0, 0, 1) },
    uLightRadiance: { value: state.lightRadiance },
    uEnvironmentIntensity: { value: state.environmentIntensity },
    uEnvironmentRotation: { value: THREE.MathUtils.degToRad(state.environmentRotation) },
    uRoughness: { value: state.roughness },
    uHalfAngle: { value: state.halfAngle },
    uMetallic: { value: state.metallic },
    uIor: { value: state.ior },
    uViewAngle: { value: state.viewAngle },
    uNormalStrength: { value: state.normalStrength },
    uNormalFrequency: { value: state.normalFrequency },
    uGeometryEnabled: { value: Number(state.geometryEnabled) },
    uExposure: { value: state.exposure },
    uToneMapper: { value: TONE_MAPPERS[state.toneMapper] },
    uShowIncorrect: { value: Number(state.showIncorrect) },
  };
}

function updateUniforms(uniforms, state) {
  const color = hexToLinearRgb(state.baseColor);
  const angle = THREE.MathUtils.degToRad(state.lightAngle);
  uniforms.uLegacyModel.value = state.legacyModel === 'phong' ? 0 : 1;
  uniforms.uShininess.value = state.shininess;
  uniforms.uBaseColor.value.set(...color);
  uniforms.uLightPosition.value.set(Math.sin(angle) * 5.5, 3.8, Math.cos(angle) * 5.5);
  uniforms.uLightDirection.value.set(Math.sin(angle), 0.7, Math.cos(angle)).normalize();
  const viewAngle = THREE.MathUtils.degToRad(state.viewAngle);
  uniforms.uViewDirection.value.set(Math.sin(viewAngle), 0, Math.cos(viewAngle));
  uniforms.uLightRadiance.value = state.lightRadiance;
  uniforms.uEnvironmentIntensity.value = state.environmentIntensity;
  uniforms.uEnvironmentRotation.value = THREE.MathUtils.degToRad(state.environmentRotation);
  uniforms.uRoughness.value = state.roughness;
  uniforms.uHalfAngle.value = state.halfAngle;
  uniforms.uMetallic.value = state.metallic;
  uniforms.uIor.value = state.ior;
  uniforms.uViewAngle.value = state.viewAngle;
  uniforms.uNormalStrength.value = state.normalStrength;
  uniforms.uNormalFrequency.value = state.normalFrequency;
  uniforms.uGeometryEnabled.value = Number(state.geometryEnabled);
  uniforms.uExposure.value = state.exposure;
  uniforms.uToneMapper.value = TONE_MAPPERS[state.toneMapper];
  uniforms.uShowIncorrect.value = Number(state.showIncorrect);
}

function materialFrom(shader, uniforms, envMap = null) {
  const material = new THREE.ShaderMaterial({
    uniforms,
    vertexShader: shader.vertexShader,
    fragmentShader: shader.fragmentShader,
    extensions: { derivatives: true },
  });
  if (envMap) material.envMap = envMap;
  return material;
}

function addBackdrop(scene) {
  const floor = new THREE.Mesh(
    new THREE.CircleGeometry(6.5, 96),
    new THREE.MeshBasicMaterial({ color: '#0c1625' }),
  );
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -1.18;
  scene.add(floor);
  return floor;
}

function makeAnalyticScene(renderer, mode, state) {
  const scene = new THREE.Scene();
  const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
  const uniforms = makeUniforms(state);
  uniforms.uMode.value = ANALYTIC_MODES.get(mode);
  const material = materialFrom(analyticShader, uniforms);
  const plane = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material);
  scene.add(plane);
  return { scene, camera, controls: null, materials: [material], resources: [plane.geometry] };
}

function makeMaterialScene(renderer, mode, state) {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(38, 1, 0.1, 50);
  camera.position.set(0, 1.15, 7.2);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.target.set(0, 0.05, 0);
  controls.enableDamping = false;
  controls.minDistance = 4.5;
  controls.maxDistance = 11;
  if (mode === 'smith-g') controls.enableRotate = false;
  const visualMode = MATERIAL_MODES.get(mode);
  const variants = mode === 'metalness' ? [0, 1, 2] : [0, 1];
  const positions = variants.length === 3 ? [-2.05, 0, 2.05] : [-1.35, 1.35];
  const materials = [];
  const resources = [];
  const meshes = [];
  variants.forEach((variant, index) => {
    const uniforms = makeUniforms(state);
    uniforms.uVisualMode.value = visualMode;
    uniforms.uVariant.value = variant;
    const material = materialFrom(materialShader, uniforms);
    const geometry = new THREE.SphereGeometry(0.98, 96, 64);
    const sphere = new THREE.Mesh(geometry, material);
    sphere.position.set(positions[index], 0, 0);
    scene.add(sphere);
    meshes.push(sphere);
    materials.push(material);
    resources.push(geometry);
  });
  const floor = addBackdrop(scene);
  resources.push(floor.geometry, floor.material);
  const lamp = new THREE.Mesh(
    new THREE.SphereGeometry(0.055, 16, 12),
    new THREE.MeshBasicMaterial({ color: '#ffd8a3' }),
  );
  scene.add(lamp);
  resources.push(lamp.geometry, lamp.material);
  return { scene, camera, controls, materials, resources, meshes, lamp };
}

function makeStudioScene(renderer, mode, state) {
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(38, 1, 0.1, 60);
  camera.position.set(4.8, 2.7, 7.2);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.target.set(0.15, 0.1, 0);
  controls.enableDamping = false;
  controls.minDistance = 4;
  controls.maxDistance = 12;
  const environment = createEnvironment(renderer);
  const visualMode = mode === 'ibl' ? 0 : 1;
  const definitions = mode === 'ibl'
    ? [
      { geometry: new THREE.SphereGeometry(1.05, 96, 64), position: [-1.25, 0, 0], variant: 0 },
      { geometry: new THREE.SphereGeometry(1.05, 96, 64), position: [1.25, 0, 0], variant: 1 },
    ]
    : [
      { geometry: new THREE.TorusKnotGeometry(0.86, 0.28, 180, 32), position: [-0.75, 0.15, 0], variant: 0 },
      { geometry: new THREE.SphereGeometry(0.58, 72, 48), position: [1.45, 0.72, 0.1], variant: 1 },
      { geometry: new THREE.SphereGeometry(0.58, 72, 48), position: [1.45, -0.7, 0.1], variant: 2 },
      { geometry: new THREE.CylinderGeometry(2.6, 2.9, 0.35, 96), position: [0.15, -1.34, 0], variant: 3 },
    ];
  const materials = [];
  const resources = [];
  definitions.forEach((definition) => {
    const uniforms = makeUniforms(state);
    uniforms.uVisualMode.value = visualMode;
    uniforms.uVariant.value = definition.variant;
    uniforms.envMap = { value: environment.pmrem };
    uniforms.uIrradianceMap = { value: environment.irradiance };
    const material = materialFrom(studioShader, uniforms, environment.pmrem);
    const mesh = new THREE.Mesh(definition.geometry, material);
    mesh.position.set(...definition.position);
    scene.add(mesh);
    materials.push(material);
    resources.push(definition.geometry);
  });
  return { scene, camera, controls, materials, resources, environment };
}

export class LabRenderer {
  constructor(canvas, mode, state, { onFrame, onYield }) {
    this.canvas = canvas;
    this.mode = mode;
    this.state = state;
    this.onFrame = onFrame;
    this.onYield = onYield;
    this.disposed = false;
    this.visible = true;
    this.pendingFrame = 0;
    this.renderCount = 0;
    this.instanceId = crypto.randomUUID();
    this.renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
    this.renderer.outputColorSpace = THREE.LinearSRGBColorSpace;
    this.renderer.toneMapping = THREE.NoToneMapping;
    this.renderer.setClearColor('#07111e', 1);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, window.innerWidth <= 600 ? 1.25 : 1.75));
    const setup = ANALYTIC_MODES.has(mode)
      ? makeAnalyticScene(this.renderer, mode, state)
      : (MATERIAL_MODES.has(mode) ? makeMaterialScene(this.renderer, mode, state) : makeStudioScene(this.renderer, mode, state));
    Object.assign(this, setup);
    this.controls?.addEventListener('change', () => {
      if (this.mode === 'smith-g') this.arrangeSmithSpecimens();
      this.requestRender();
    });
    this.resizeObserver = 'ResizeObserver' in window
      ? new ResizeObserver(() => this.requestRender())
      : null;
    this.resizeObserver?.observe(this.canvas);
    this.channel = 'BroadcastChannel' in window ? new BroadcastChannel('phong-to-pbr-contexts') : null;
    if (this.channel) {
      this.channel.onmessage = (event) => {
        if (event.data?.type === 'context-active' && event.data.id !== this.instanceId && !this.visible) this.onYield();
      };
      this.channel.postMessage({ type: 'context-active', id: this.instanceId });
    }
    this.updateState(state);
  }

  updateState(state) {
    this.state = state;
    this.materials.forEach((material) => updateUniforms(material.uniforms, state));
    if (this.lamp) this.lamp.position.copy(this.materials[0].uniforms.uLightPosition.value);
    if (this.mode === 'smith-g') {
      this.arrangeSmithSpecimens();
    }
    this.requestRender();
  }

  setVisible(visible) {
    this.visible = visible;
    if (visible) {
      this.channel?.postMessage({ type: 'context-active', id: this.instanceId });
      this.requestRender();
    }
  }

  arrangeSmithSpecimens() {
    this.camera.updateMatrixWorld();
    const cameraRight = new THREE.Vector3().setFromMatrixColumn(this.camera.matrixWorld, 0).normalize();
    this.meshes[0].position.copy(cameraRight).multiplyScalar(-1.35);
    this.meshes[1].position.copy(cameraRight).multiplyScalar(1.35);
  }

  requestRender() {
    if (this.disposed || !this.visible || document.hidden || this.pendingFrame) return;
    this.pendingFrame = requestAnimationFrame(() => {
      this.pendingFrame = 0;
      this.resize();
      this.renderer.render(this.scene, this.camera);
      this.renderCount += 1;
      this.onFrame({ renderCount: this.renderCount });
    });
  }

  resize() {
    const width = Math.max(1, this.canvas.clientWidth);
    const height = Math.max(1, this.canvas.clientHeight);
    const pixelRatio = this.renderer.getPixelRatio();
    if (this.canvas.width !== Math.floor(width * pixelRatio) || this.canvas.height !== Math.floor(height * pixelRatio)) {
      this.renderer.setSize(width, height, false);
    }
    if (this.camera.isPerspectiveCamera) {
      this.camera.aspect = width / height;
      this.camera.updateProjectionMatrix();
    }
    this.materials.forEach((material) => material.uniforms.uResolution?.value.set(width, height));
  }

  dispose() {
    if (this.disposed) return;
    this.disposed = true;
    if (this.pendingFrame) cancelAnimationFrame(this.pendingFrame);
    this.resizeObserver?.disconnect();
    this.controls?.dispose();
    this.materials.forEach((material) => material.dispose());
    this.resources.forEach((resource) => resource.dispose?.());
    this.environment?.dispose();
    this.channel?.close();
    this.renderer.dispose();
    this.renderer.getContext().getExtension('WEBGL_lose_context')?.loseContext();
  }
}
