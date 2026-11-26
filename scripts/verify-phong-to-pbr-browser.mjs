import { createServer } from 'node:http';
import { createRequire } from 'node:module';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { MODE_IDS, MODE_SPECS } from '../static/demos/phong-to-pbr/mode-specs.js';

const require = createRequire(import.meta.url);
const playwrightModule = process.env.PLAYWRIGHT_MODULE ?? 'playwright';
const playwright = require(playwrightModule);
const playwrightPackage = require.resolve(path.join(playwrightModule, 'package.json'));
const utilsBundle = path.join(path.dirname(playwrightPackage), '..', 'playwright-core', 'lib', 'utilsBundle.js');
const { PNG } = require(utilsBundle);
const repoRoot = fileURLToPath(new URL('../', import.meta.url));
const staticRoot = path.join(repoRoot, 'static');
const screenshotRoot = path.resolve(process.argv[2] ?? path.join(tmpdir(), 'phong-to-pbr-screenshots'));
const mimeTypes = new Map([
  ['.css', 'text/css; charset=utf-8'],
  ['.html', 'text/html; charset=utf-8'],
  ['.js', 'text/javascript; charset=utf-8'],
  ['.png', 'image/png'],
]);

function serveStatic(request, response) {
  const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
  let filename = path.resolve(staticRoot, pathname.replace(/^\/+/, ''));
  if (pathname.endsWith('/')) filename = path.join(filename, 'index.html');
  if (!filename.startsWith(`${staticRoot}${path.sep}`)) {
    response.writeHead(403).end('Forbidden');
    return;
  }
  readFile(filename).then((body) => {
    response.writeHead(200, { 'content-type': mimeTypes.get(path.extname(filename)) ?? 'application/octet-stream' });
    response.end(body);
  }).catch(() => response.writeHead(404).end('Not found'));
}

function listen(server) {
  return new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => resolve(server.address().port));
  });
}

async function waitForFrame(page, count, label) {
  await page.waitForFunction((previous) => window.__PBR_LAB__.renderCount > previous, count, { timeout: 25000 }).catch((error) => {
    throw new Error(`${label}: ${error.message}`);
  });
}

function meanPixelDelta(leftBuffer, rightBuffer) {
  const left = PNG.sync.read(leftBuffer);
  const right = PNG.sync.read(rightBuffer);
  if (left.width !== right.width || left.height !== right.height) return 1;
  let delta = 0;
  for (let index = 0; index < left.data.length; index += 4) {
    delta += Math.abs(left.data[index] - right.data[index]);
    delta += Math.abs(left.data[index + 1] - right.data[index + 1]);
    delta += Math.abs(left.data[index + 2] - right.data[index + 2]);
  }
  return delta / (left.width * left.height * 3 * 255);
}

async function verifyRun(browser, baseUrl, viewport, mode) {
  const page = await browser.newPage({ viewport: viewport.size, deviceScaleFactor: 1 });
  const diagnostics = [];
  page.on('console', (message) => {
    const text = message.text();
    const isScreenshotReadback = text.includes('GL Driver Message') && text.includes('GPU stall due to ReadPixels');
    if (!isScreenshotReadback && (message.type() === 'warning' || message.type() === 'error')) {
      diagnostics.push(`${message.type()}: ${text}`);
    }
  });
  page.on('pageerror', (error) => diagnostics.push(`pageerror: ${error.message}`));
  page.on('requestfailed', (request) => diagnostics.push(`requestfailed: ${request.url()} ${request.failure()?.errorText}`));

  try {
    await page.goto(`${baseUrl}/demos/phong-to-pbr/?mode=${mode}`, { waitUntil: 'networkidle' });
    await page.waitForFunction(() => window.__PBR_LAB__?.ready === true, null, { timeout: 25000 });
    await page.waitForFunction(() => getComputedStyle(document.querySelector('#veil')).opacity === '0');
    await page.waitForTimeout(650);
    const initial = await page.evaluate(() => {
      const lab = window.__PBR_LAB__;
      return {
        state: lab.getState(),
        count: lab.renderCount,
        mode: lab.mode,
        context: lab.contextState,
      };
    });
    if (initial.mode !== mode || initial.context !== 'active') {
      throw new Error(`invalid initial bridge ${JSON.stringify(initial)}`);
    }
    const canvas = page.locator('#render-canvas');
    const initialPixels = await canvas.screenshot();

    const probe = MODE_SPECS[mode].probe;
    await page.evaluate(({ id, value }) => window.__PBR_LAB__.setControl(id, value), {
      id: probe.control,
      value: probe.value,
    });
    await waitForFrame(page, initial.count, `${mode} ${viewport.name} probe frame`);
    const changed = await page.evaluate(() => ({
      count: window.__PBR_LAB__.renderCount,
    }));
    const changedPixels = await canvas.screenshot();
    if (meanPixelDelta(changedPixels, initialPixels) < 0.00001) throw new Error('probe did not change WebGL canvas pixels');
    await page.waitForTimeout(700);
    const idleCount = await page.evaluate(() => window.__PBR_LAB__.renderCount);
    if (idleCount !== changed.count) throw new Error(`renderer did not become idle (${changed.count} to ${idleCount})`);

    if (mode === 'ibl' || mode === 'studio') {
      const rotationStart = await page.evaluate(() => ({
        count: window.__PBR_LAB__.renderCount,
      }));
      const rotationPixels = await canvas.screenshot();
      await page.evaluate(() => window.__PBR_LAB__.setControl('environmentRotation', 120));
      await waitForFrame(page, rotationStart.count, `${mode} ${viewport.name} environment rotation frame`);
      const rotatedPixels = await canvas.screenshot();
      if (meanPixelDelta(rotatedPixels, rotationPixels) < 0.00001) throw new Error('environment rotation did not change WebGL canvas pixels');
    }

    const beforeResetCount = await page.evaluate(() => window.__PBR_LAB__.renderCount);
    await page.evaluate(() => window.__PBR_LAB__.reset());
    await page.waitForFunction((count) => window.__PBR_LAB__.renderCount > count, beforeResetCount);
    const resetState = await page.evaluate(() => window.__PBR_LAB__.getState());
    if (JSON.stringify(resetState) !== JSON.stringify(initial.state)) throw new Error('reset state mismatch');
    const resetPixels = await canvas.screenshot();
    const resetDelta = meanPixelDelta(resetPixels, initialPixels);
    if (resetDelta > 0.0005) {
      await Promise.all([
        writeFile(path.join(screenshotRoot, `debug-${viewport.name}-${mode}-initial.png`), initialPixels),
        writeFile(path.join(screenshotRoot, `debug-${viewport.name}-${mode}-reset.png`), resetPixels),
      ]);
      throw new Error(`reset canvas delta too large: ${resetDelta}`);
    }
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
    if (overflow) throw new Error('horizontal overflow');

    await page.waitForTimeout(500);
    await page.locator('#lab').screenshot({ path: path.join(screenshotRoot, `${viewport.name}-${mode}.png`) });
    if (diagnostics.length) throw new Error(`browser diagnostics were not empty\n${diagnostics.join('\n')}`);
  } catch (error) {
    throw new Error(`${mode} ${viewport.name}: ${error.message}`);
  } finally {
    await page.close();
  }
}

async function verifyLifecycle(browser, baseUrl) {
  const page = await browser.newPage({ viewport: { width: 900, height: 700 } });
  try {
    await page.goto(`${baseUrl}/demos/phong-to-pbr/?mode=studio`, { waitUntil: 'networkidle' });
    await page.waitForFunction(() => window.__PBR_LAB__?.contextState === 'active');
    await page.evaluate(() => { document.body.style.paddingTop = '1800px'; });
    await page.waitForFunction(() => window.__PBR_LAB__.contextState === 'released-offscreen', null, { timeout: 5000 });
    await page.evaluate(() => { document.body.style.paddingTop = '0'; });
    await page.waitForFunction(() => window.__PBR_LAB__.contextState === 'active', null, { timeout: 25000 });
  } finally {
    await page.close();
  }
}

async function canvasDimensions(page) {
  return page.evaluate(() => {
    const canvas = document.querySelector('#render-canvas');
    return {
      cssWidth: canvas.clientWidth,
      cssHeight: canvas.clientHeight,
      bufferWidth: canvas.width,
      bufferHeight: canvas.height,
      count: window.__PBR_LAB__.renderCount,
    };
  });
}

async function waitForSynchronizedCanvas(page, previousCount, label) {
  await page.waitForFunction((count) => {
    const canvas = document.querySelector('#render-canvas');
    return window.__PBR_LAB__.renderCount > count
      && Math.abs(canvas.width - canvas.clientWidth) <= 1
      && Math.abs(canvas.height - canvas.clientHeight) <= 1;
  }, previousCount, { timeout: 25000 }).catch((error) => {
    throw new Error(`${label}: ${error.message}`);
  });
  return canvasDimensions(page);
}

function assertCanvasDimensionsMatch(dimensions, label) {
  const widthDelta = Math.abs(dimensions.bufferWidth - dimensions.cssWidth);
  const heightDelta = Math.abs(dimensions.bufferHeight - dimensions.cssHeight);
  if (widthDelta > 1 || heightDelta > 1) {
    throw new Error(`${label}: stale drawing buffer ${JSON.stringify(dimensions)}`);
  }
}

async function verifyResizeAndFullscreen(browser, baseUrl) {
  const page = await browser.newPage({ viewport: { width: 900, height: 700 }, deviceScaleFactor: 1 });
  try {
    await page.goto(`${baseUrl}/demos/phong-to-pbr/?mode=studio`, { waitUntil: 'networkidle' });
    await page.waitForFunction(() => window.__PBR_LAB__?.contextState === 'active');
    const initial = await canvasDimensions(page);
    assertCanvasDimensionsMatch(initial, 'initial canvas');

    await page.setViewportSize({ width: 720, height: 780 });
    const breakpoint = await waitForSynchronizedCanvas(page, initial.count, 'breakpoint resize frame');
    assertCanvasDimensionsMatch(breakpoint, 'breakpoint canvas');
    if (breakpoint.cssWidth === initial.cssWidth && breakpoint.cssHeight === initial.cssHeight) {
      throw new Error('breakpoint did not change the canvas CSS dimensions');
    }

    const beforeFullscreen = breakpoint;
    await page.locator('#fullscreen').click();
    await page.waitForFunction(() => document.fullscreenElement?.id === 'lab');
    const fullscreen = await waitForSynchronizedCanvas(page, beforeFullscreen.count, 'fullscreen enter frame');
    assertCanvasDimensionsMatch(fullscreen, 'fullscreen canvas');
    if (fullscreen.cssWidth === beforeFullscreen.cssWidth && fullscreen.cssHeight === beforeFullscreen.cssHeight) {
      throw new Error('fullscreen did not change the canvas CSS dimensions');
    }

    await page.locator('#fullscreen').click();
    await page.waitForFunction(() => document.fullscreenElement === null);
    const restored = await waitForSynchronizedCanvas(page, fullscreen.count, 'fullscreen exit frame');
    assertCanvasDimensionsMatch(restored, 'restored canvas');
  } finally {
    await page.close();
  }
}

const server = createServer(serveStatic);
let browser;

try {
  await mkdir(screenshotRoot, { recursive: true });
  const port = await listen(server);
  browser = await playwright.chromium.launch({
    executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE,
    headless: true,
    args: ['--ignore-certificate-errors', '--enable-unsafe-swiftshader'],
  });
  const baseUrl = `http://127.0.0.1:${port}`;
  const viewports = [
    { name: 'desktop', size: { width: 1100, height: 760 } },
    { name: 'mobile', size: { width: 360, height: 780 } },
  ].filter((viewport) => !process.env.PBR_VIEWPORTS || process.env.PBR_VIEWPORTS.split(',').includes(viewport.name));
  const modes = process.env.PBR_MODES ? process.env.PBR_MODES.split(',') : MODE_IDS;
  let checks = 0;
  for (const viewport of viewports) {
    for (const mode of modes) {
      await verifyRun(browser, baseUrl, viewport, mode);
      checks += 1;
    }
  }
  await verifyLifecycle(browser, baseUrl);
  await verifyResizeAndFullscreen(browser, baseUrl);
  console.log(`phong-to-pbr browser: ${checks}/${viewports.length * modes.length} pixel probes and screenshots, reset, idle, lifecycle, resize and fullscreen checks passed`);
  console.log(`screenshots: ${screenshotRoot}`);
} finally {
  await browser?.close();
  server.close();
}
