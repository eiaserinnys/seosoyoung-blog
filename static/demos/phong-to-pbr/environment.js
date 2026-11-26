import * as THREE from 'three';

const PI = Math.PI;
const TAU = PI * 2;
const SUN_DIRECTION = normalize([0.42, 0.72, 0.55]);

function normalize(vector) {
  const length = Math.hypot(...vector);
  return vector.map((value) => value / length);
}

function cross(a, b) {
  return [
    a[1] * b[2] - a[2] * b[1],
    a[2] * b[0] - a[0] * b[2],
    a[0] * b[1] - a[1] * b[0],
  ];
}

function addScaled(a, b, scale) {
  return [a[0] + b[0] * scale, a[1] + b[1] * scale, a[2] + b[2] * scale];
}

function dot(a, b) {
  return a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
}

function uvToDirection(u, v) {
  const longitude = (u - 0.5) * TAU;
  const latitude = (v - 0.5) * PI;
  const cosLatitude = Math.cos(latitude);
  return [
    Math.cos(longitude) * cosLatitude,
    Math.sin(latitude),
    Math.sin(longitude) * cosLatitude,
  ];
}

export function sampleEnvironment(direction) {
  const y = Math.max(-1, Math.min(1, direction[1]));
  const sky = Math.max(0, y);
  const ground = Math.max(0, -y);
  const horizon = Math.exp(-Math.abs(y) * 5.5);
  const sunDot = Math.max(0, dot(direction, SUN_DIRECTION));
  const sun = 34 * sunDot ** 420 + 3.6 * sunDot ** 38;
  const coolSky = [0.12 + 0.2 * sky, 0.2 + 0.35 * sky, 0.34 + 0.68 * sky];
  const warmHorizon = [0.88, 0.3, 0.09].map((channel) => channel * horizon * 0.72);
  const darkGround = [0.06, 0.045, 0.035].map((channel) => channel * (0.45 + ground));
  const sunColor = [1, 0.71, 0.34].map((channel) => channel * sun);
  return coolSky.map((channel, index) => channel + warmHorizon[index] + darkGround[index] + sunColor[index]);
}

function makeFloatTexture(width, height, sampler) {
  const data = new Float32Array(width * height * 4);
  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      const direction = uvToDirection((x + 0.5) / width, (y + 0.5) / height);
      const color = sampler(direction);
      const offset = (y * width + x) * 4;
      data[offset] = color[0];
      data[offset + 1] = color[1];
      data[offset + 2] = color[2];
      data[offset + 3] = 1;
    }
  }
  const texture = new THREE.DataTexture(data, width, height, THREE.RGBAFormat, THREE.FloatType);
  texture.colorSpace = THREE.LinearSRGBColorSpace;
  texture.magFilter = THREE.LinearFilter;
  texture.minFilter = THREE.LinearFilter;
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.ClampToEdgeWrapping;
  texture.needsUpdate = true;
  return texture;
}

function radicalInverse(bits) {
  let value = bits;
  value = ((value << 16) | (value >>> 16)) >>> 0;
  value = (((value & 0x55555555) << 1) | ((value & 0xaaaaaaaa) >>> 1)) >>> 0;
  value = (((value & 0x33333333) << 2) | ((value & 0xcccccccc) >>> 2)) >>> 0;
  value = (((value & 0x0f0f0f0f) << 4) | ((value & 0xf0f0f0f0) >>> 4)) >>> 0;
  value = (((value & 0x00ff00ff) << 8) | ((value & 0xff00ff00) >>> 8)) >>> 0;
  return value * 2.3283064365386963e-10;
}

function cosineSample(index, count) {
  const u = (index + 0.5) / count;
  const v = radicalInverse(index);
  const radius = Math.sqrt(u);
  const phi = TAU * v;
  return [radius * Math.cos(phi), radius * Math.sin(phi), Math.sqrt(Math.max(0, 1 - u))];
}

function tangentFrame(normal) {
  const up = Math.abs(normal[1]) < 0.999 ? [0, 1, 0] : [1, 0, 0];
  const tangent = normalize(cross(up, normal));
  const bitangent = cross(normal, tangent);
  return [tangent, bitangent];
}

export function integrateDiffuseIrradiance(normal, sampleCount = 64) {
  const [tangent, bitangent] = tangentFrame(normal);
  const sum = [0, 0, 0];
  for (let index = 0; index < sampleCount; index += 1) {
    const local = cosineSample(index, sampleCount);
    let direction = addScaled(normal.map((value) => value * local[2]), tangent, local[0]);
    direction = addScaled(direction, bitangent, local[1]);
    const radiance = sampleEnvironment(normalize(direction));
    for (let channel = 0; channel < 3; channel += 1) sum[channel] += radiance[channel];
  }
  return sum.map((value) => PI * value / sampleCount);
}

export function createEnvironment(renderer) {
  const source = makeFloatTexture(256, 128, sampleEnvironment);
  source.mapping = THREE.EquirectangularReflectionMapping;
  const irradiance = makeFloatTexture(48, 24, (normal) => integrateDiffuseIrradiance(normal));
  const generator = new THREE.PMREMGenerator(renderer);
  generator.compileEquirectangularShader();
  const pmremTarget = generator.fromEquirectangular(source);
  generator.dispose();
  return {
    source,
    irradiance,
    pmrem: pmremTarget.texture,
    dispose() {
      source.dispose();
      irradiance.dispose();
      pmremTarget.dispose();
    },
  };
}
