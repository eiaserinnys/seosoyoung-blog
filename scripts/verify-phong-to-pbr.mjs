import { access, readFile } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const repoRoot = fileURLToPath(new URL('../', import.meta.url));
const demoRoot = path.join(repoRoot, 'static', 'demos', 'phong-to-pbr');
const requiredFiles = [
  'index.html',
  'styles.css',
  'app.js',
  'mode-specs.js',
  'pbr-math.js',
  'pbr-glsl.js',
  'environment.js',
  'renderer.js',
  'ui.js',
  'shaders/analytic.js',
  'shaders/material.js',
  'shaders/pipeline.js',
  'shaders/studio.js',
];
const expectedModes = [
  'compare',
  'ggx-d',
  'fresnel',
  'smith-g',
  'metalness',
  'normal',
  'ibl',
  'pipeline',
  'studio',
];
const MODE_IDS_WITH_AXES = ['ggx-d', 'fresnel'];
const failures = [];
const check = (condition, message) => {
  if (!condition) failures.push(message);
};
const close = (actual, expected, tolerance, message) => {
  check(Math.abs(actual - expected) <= tolerance, `${message}: ${actual} != ${expected}`);
};

const missing = [];
for (const name of requiredFiles) {
  try {
    await access(path.join(demoRoot, name));
  } catch {
    missing.push(name);
  }
}
if (missing.length) {
  failures.push(`missing demo files: ${missing.join(', ')}`);
}

if (!missing.length) {
  const [html, styles, app, specsSource, mathSource, glsl, environment, renderer, analyticShader] = await Promise.all([
    readFile(path.join(demoRoot, 'index.html'), 'utf8'),
    readFile(path.join(demoRoot, 'styles.css'), 'utf8'),
    readFile(path.join(demoRoot, 'app.js'), 'utf8'),
    readFile(path.join(demoRoot, 'mode-specs.js'), 'utf8'),
    readFile(path.join(demoRoot, 'pbr-math.js'), 'utf8'),
    readFile(path.join(demoRoot, 'pbr-glsl.js'), 'utf8'),
    readFile(path.join(demoRoot, 'environment.js'), 'utf8'),
    readFile(path.join(demoRoot, 'renderer.js'), 'utf8'),
    readFile(path.join(demoRoot, 'shaders', 'analytic.js'), 'utf8'),
  ]);
  const cacheBust = `?verify=${Date.now()}`;
  const math = await import(`${pathToFileURL(path.join(demoRoot, 'pbr-math.js')).href}${cacheBust}`);
  const specs = await import(`${pathToFileURL(path.join(demoRoot, 'mode-specs.js')).href}${cacheBust}`);

  check(html.includes('three@0.168.0'), 'Three.js CDN version must stay pinned to 0.168.0');
  check(html.includes('type="module" src="./app.js"'), 'local module entry is missing');
  check(styles.includes('@media (max-width: 600px)'), '360px mobile layout contract is missing');
  check(styles.includes('overflow-x: hidden'), 'horizontal overflow guard is missing');
  check(app.includes("params.get('mode') ?? 'studio'"), 'studio must be the explicit missing-query default');
  check(app.includes('IntersectionObserver'), 'lazy WebGL initialization is missing');
  check(app.includes('visibilitychange'), 'Page Visibility lifecycle is missing');
  check(renderer.includes('requestRender'), 'event-driven render scheduler is missing');
  check(renderer.includes('new ResizeObserver'), 'canvas resize observer is missing');
  check(renderer.includes('resizeObserver?.disconnect()'), 'canvas resize observer cleanup is missing');
  check(!renderer.includes('setAnimationLoop'), 'continuous renderer loop is forbidden');
  check(renderer.includes('WEBGL_lose_context'), 'released iframes must explicitly lose their WebGL context');
  check(renderer.includes('BroadcastChannel'), 'cross-iframe context handoff is missing');
  check(environment.includes('PMREMGenerator'), 'actual Three.js PMREM prefilter is missing');
  check(environment.includes('fromEquirectangular'), 'equirectangular PMREM input is missing');
  check(environment.includes('integrateDiffuseIrradiance'), 'diffuse numerical convolution is missing');
  check(specsSource.includes('Three.js PMREM 근사'), 'PMREM approximation disclosure is missing');
  check(specsSource.includes('정확한 GGX 적분이 아닙니다'), 'exact-integral disclaimer is missing');
  check(specsSource.includes('거시 그림자'), 'Smith G macro-shadow disclaimer is missing');
  check(specsSource.includes('불투명, 등방성, 단일 레이어'), 'material scope disclaimer is missing');
  check(!/[·―—]/.test([html, specsSource, mathSource].join('\n')), 'forbidden UI punctuation is present');
  check(styles.includes('input[type="range"]:focus-visible'), 'range focus-visible style is missing');
  check(![mathSource, specsSource].join('\n').includes(' × '), 'dot products must not use the vector cross-product symbol');
  check(mathSource.includes('const PBR_EPSILON'), 'single denominator epsilon is missing');
  check(glsl.includes('float alpha = perceptualRoughness * perceptualRoughness;'), 'GLSL r→alpha mapping drifted');
  check(glsl.includes('pbrSmithGCorrelated'), 'shared GLSL Smith G function is missing');
  check(glsl.includes('pbrEvaluateDirect'), 'shared GLSL direct-light path is missing');
  check(analyticShader.includes('float divider = smoothstep('), 'pipeline divider must not cover both comparison panels');
  check(!analyticShader.includes('pow(normalized'), 'normalized GGX graph must use a linear y axis');
  check(renderer.includes('cameraRight'), 'Smith specimens must stay side by side in camera space');
  check(renderer.includes('uEnvironmentRotation'), 'environment rotation renderer uniform is missing');
  check(specsSource.match(/range\('environmentRotation'/g)?.length === 2, 'ibl and studio must both expose environment rotation');

  check(Array.isArray(specs.MODE_IDS), 'MODE_IDS must be exported');
  check(JSON.stringify(specs.MODE_IDS) === JSON.stringify(expectedModes), 'mode IDs or order drifted');
  check(Object.keys(specs.MODE_SPECS).length === expectedModes.length, 'mode inventory must be exactly 9');
  for (const id of expectedModes) {
    const spec = specs.MODE_SPECS[id];
    check(Boolean(spec), `mode spec missing: ${id}`);
    check(Boolean(spec?.title && spec?.question && spec?.limits), `mode copy incomplete: ${id}`);
    check(Array.isArray(spec?.controls) && spec.controls.length > 0, `mode controls missing: ${id}`);
    check(Boolean(spec?.badge?.label && spec?.badge?.value), `mode badge missing: ${id}`);
  }
  check(MODE_IDS_WITH_AXES.every((id) => specs.MODE_SPECS[id].axes?.x && specs.MODE_SPECS[id].axes?.y), 'D/F graph axes are missing');

  close(math.roughnessToAlpha(0.5), 0.25, 1e-12, 'r=0.5 alpha');
  close(math.roughnessToAlpha(1), 1, 1e-12, 'r=1 alpha');
  close(math.iorToF0(1.5), 0.04, 1e-12, 'IOR 1.5 F0');
  close(math.ggxDistribution(1, 1), 1 / Math.PI, 1e-12, 'GGX alpha=1 normal peak');
  const alphaMin = math.roughnessToAlpha(math.MIN_ROUGHNESS);
  close(
    math.ggxDistribution(1, alphaMin),
    1 / (Math.PI * alphaMin * alphaMin),
    1e-6,
    'minimum roughness GGX peak must not be epsilon-clamped',
  );
  close(math.ggxDistribution(0, alphaMin), alphaMin * alphaMin / Math.PI, 1e-12, 'GGX horizon');
  close(math.schlickFresnel(1, 0.04), 0.04, 1e-12, 'Schlick normal incidence');
  close(math.schlickFresnel(0, 0.04), 1, 1e-12, 'Schlick grazing');
  close(math.smithGCorrelated(1, 1, alphaMin), 1, 1e-12, 'Smith normal incidence');
  close(math.smithGCorrelated(0, 0.5, alphaMin), 0, 1e-12, 'Smith grazing limit');
  const fresnelMetrics = math.modeMetrics('fresnel', { roughness: 0.4, halfAngle: 24, viewAngle: 60, ior: 1.5 });
  check(fresnelMetrics[1][1] === '0.500', 'Fresnel readout must use viewAngle, not shared halfAngle');
  const smithMetrics = math.modeMetrics('smith-g', { roughness: 0.4, halfAngle: 24, viewAngle: 60 });
  check(smithMetrics[1][1] === '0.500', 'Smith readout must use viewAngle, not shared halfAngle');

  const roughnesses = [math.MIN_ROUGHNESS, 0.1, 0.25, 0.5, 0.8, 1];
  const dots = [0, 1e-6, 0.01, 0.5, 1];
  const metallics = [0, 0.5, 1];
  const iors = [1, 1.5, 2.5];
  let numericCases = 0;
  for (const roughness of roughnesses) {
    for (const noV of dots) {
      for (const noL of dots) {
        for (const metallic of metallics) {
          for (const ior of iors) {
            const result = math.evaluateDirectLight({
              roughness,
              noV,
              noL,
              noH: Math.min(1, Math.sqrt((noV + noL) * 0.5)),
              voH: Math.min(1, Math.sqrt(Math.max(noV, noL))),
              metallic,
              ior,
              baseColor: [0.82, 0.31, 0.12],
              lightRadiance: [7, 6, 5],
            });
            const values = [result.D, result.G, ...result.F, ...result.specular, ...result.diffuse, ...result.radiance];
            check(values.every(Number.isFinite), `non-finite direct-light sample: ${JSON.stringify({ roughness, noV, noL, metallic, ior })}`);
            check(values.every((value) => value >= 0), `negative direct-light sample: ${JSON.stringify({ roughness, noV, noL, metallic, ior })}`);
            if (noL === 0) close(Math.max(...result.radiance), 0, 1e-12, 'NoL=0 radiance');
            numericCases += 1;
          }
        }
      }
    }
  }
  check(numericCases === 1350, `numeric grid changed: ${numericCases}`);
}

if (failures.length) {
  console.error(`phong-to-pbr contract failed (${failures.length})`);
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exitCode = 1;
} else {
  console.log('phong-to-pbr contract: 9/9 modes, 1,350 numeric cases, 13 demo files verified');
}
