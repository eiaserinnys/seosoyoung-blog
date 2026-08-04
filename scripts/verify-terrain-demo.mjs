import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const repoRoot = fileURLToPath(new URL('../', import.meta.url));
const demoRoot = path.join(repoRoot, 'static', 'demos', 'simondev-procedural-terrain');

const read = async (name) => readFile(path.join(demoRoot, name), 'utf8');
const [html, styles, runtime, shaders] = await Promise.all([
  read('index.html'),
  read('styles.css'),
  read('terrain.js'),
  read('terrain-shaders.js'),
]);

const failures = [];
const assert = (condition, message) => {
  if (!condition) failures.push(message);
};

assert(html.includes('three@0.168.0'), 'three.js CDN version must stay pinned');
assert(runtime.includes('lil-gui@0.19.2'), 'lil-gui CDN version must stay pinned');
assert(html.includes('type="module" src="./terrain.js"'), 'local module entry is missing');
assert(styles.includes('@media (max-width: 720px)'), 'mobile layout contract is missing');

const inventoryIds = [...runtime.matchAll(/\{ id: (\d+), label:/g)].map((match) => Number(match[1]));
assert(inventoryIds.length === 11, `expected 11 inventory entries, found ${inventoryIds.length}`);
assert(inventoryIds.every((id, index) => id === index + 1), 'inventory ids must be exactly 1 through 11');

const controls = [
  ['1', 'uFrequency', 'uAmplitude'],
  ['2', 'uOctaves', 'uLacunarity', 'uGain', 'uReshapePower'],
  ['3', "noiseType: 'ridged'", 'uNoiseMode'],
  ['4', "noiseType: 'voronoi'", 'voronoiNoise'],
  ['5', 'uFeatureFbm', 'octaveLimit'],
  ['6', 'uErosionEnabled', 'uErosionStrength', 'erodedHeight'],
  ['7', 'uTerraceEnabled', 'uTerraceSteps', 'shortRamp'],
  ['8', 'uCombinedPreset', 'lowFrequencyTerraces'],
  ['9', 'uDistanceFogEnabled', 'distanceFog'],
  ['10', 'uHeightFogEnabled', 'heightFogOpticalDepth', 'uFogDensity'],
  ['11', 'uScatterSeparated', 'inScattering', 'transmittance'],
];

const guiProperties = [
  'frequency', 'amplitude',
  'octaves', 'lacunarity', 'gain', 'reshapePower',
  'noiseType', 'featureFbm',
  'erosion', 'erosionStrength',
  'terrace', 'terraceSteps', 'combinedPreset',
  'distanceFog', 'heightFog', 'fogDensity', 'scatterSeparated',
  'autoFlight',
];

for (const property of guiProperties) {
  const singleQuoted = `add(settings, '${property}'`;
  const doubleQuoted = `add(settings, "${property}"`;
  assert(
    runtime.includes(singleQuoted) || runtime.includes(doubleQuoted),
    `GUI control missing: ${property}`,
  );
}

assert(runtime.includes('setControl(property, value)'), 'browser verification control bridge is missing');

for (const [id, ...markers] of controls) {
  for (const marker of markers) {
    assert(runtime.includes(marker) || shaders.includes(marker), `trick ${id} marker missing: ${marker}`);
  }
}

const settingsBlock = runtime.match(/const settings = \{([\s\S]*?)\n\};/)?.[1] ?? '';
const expectedDefaults = [
  ['gridDensity', '1024'],
  ['frequency', '0.19'],
  ['amplitude', '11.2'],
  ['octaves', '6'],
  ['lacunarity', '2.02'],
  ['gain', '0.54'],
  ['reshapePower', '1.05'],
  ['noiseType', "'value'"],
  ['featureFbm', 'false'],
  ['erosion', 'true'],
  ['erosionStrength', '0.4'],
  ['terrace', 'true'],
  ['terraceSteps', '3'],
  ['combinedPreset', 'true'],
  ['distanceFog', 'true'],
  ['heightFog', 'true'],
  ['fogDensity', '0.02'],
  ['scatterSeparated', 'true'],
];
for (const [property, value] of expectedDefaults) {
  assert(
    new RegExp(`\\b${property}:\\s*${value.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\$&')}[,\\n]`).test(settingsBlock),
    `initial setting mismatch: ${property} must be ${value}`,
  );
}

assert(!runtime.includes("applyPreset('Full')"), 'initial settings must not be overwritten by a preset');
assert(/new GUI\(\{[\s\S]*?container:\s*app[,\n]/.test(runtime), 'lil-gui must live inside the fullscreen app container');
assert(runtime.includes('new THREE.PlaneGeometry(GRID_SIZE, GRID_SIZE, density, density)'), 'terrain grid must use the selected density');
assert(shaders.includes('gl_Position = projectionMatrix * viewMatrix * worldPosition'), 'vertex displacement path is missing');
assert(shaders.includes('vWorldNormal = normalize(mat3(modelMatrix) * localNormal)'), 'smooth vertex normal path is missing');
assert(!/\bdFdx\b|\bdFdy\b/.test(shaders), 'fragment derivative normals must stay removed');

const combinedBranch = shaders.indexOf('if (uCombinedPreset > 0.5)');
const terraceBranch = shaders.indexOf('else if (uTerraceEnabled > 0.5)');
assert(combinedBranch >= 0 && terraceBranch > combinedBranch, 'combined terrain must take precedence over standalone terraces');
assert(/#fullscreen-toggle\s*\{[\s\S]*?position:\s*absolute;[\s\S]*?left:\s*16px;[\s\S]*?top:\s*16px;/.test(styles), 'fullscreen button must stay in the top-left corner');
assert(/\.lil-gui\.root\s*\{[\s\S]*?position:\s*absolute;[\s\S]*?max-height:\s*calc\(100% - 32px\);/.test(styles), 'GUI must remain positioned and scrollable inside the app');
assert(/\.lil-gui\.root\s*>\s*\.children\s*\{[\s\S]*?overflow-y:\s*auto;/.test(styles), 'long GUI content must scroll vertically');

if (failures.length) {
  console.error(`terrain demo contract failed (${failures.length})`);
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exitCode = 1;
} else {
  console.log('terrain demo contract: 11/11 tricks, 4 demo files verified');
}
