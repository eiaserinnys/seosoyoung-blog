export const vertexShader = /* glsl */ `
precision highp float;

uniform float uTime;
uniform float uFrequency;
uniform float uAmplitude;
uniform float uOctaves;
uniform float uLacunarity;
uniform float uGain;
uniform float uReshapePower;
uniform float uNoiseMode;
uniform float uFeatureFbm;
uniform float uErosionEnabled;
uniform float uErosionStrength;
uniform float uTerraceEnabled;
uniform float uTerraceSteps;
uniform float uCombinedPreset;
uniform float uGridSpacing;

varying vec3 vWorldPosition;
varying vec3 vWorldNormal;
varying float vHeight;

vec2 hash22(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * vec3(0.1031, 0.1030, 0.0973));
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.xx + p3.yz) * p3.zy);
}

float hash21(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

float valueNoise(vec2 p) {
  vec2 cell = floor(p);
  vec2 f = fract(p);
  vec2 smoothF = f * f * (3.0 - 2.0 * f);
  float a = hash21(cell);
  float b = hash21(cell + vec2(1.0, 0.0));
  float c = hash21(cell + vec2(0.0, 1.0));
  float d = hash21(cell + vec2(1.0, 1.0));
  return mix(mix(a, b, smoothF.x), mix(c, d, smoothF.x), smoothF.y) * 2.0 - 1.0;
}

float voronoiNoise(vec2 p) {
  vec2 cell = floor(p);
  vec2 f = fract(p);
  float nearest = 8.0;

  for (int y = -1; y <= 1; y++) {
    for (int x = -1; x <= 1; x++) {
      vec2 neighbour = vec2(float(x), float(y));
      vec2 point = hash22(cell + neighbour);
      nearest = min(nearest, length(neighbour + point - f));
    }
  }

  float cellSurface = smoothstep(0.12, 0.68, clamp(nearest * 1.45, 0.0, 1.0));
  return cellSurface * 2.0 - 1.0;
}

float terrainNoise(vec2 p) {
  float base = valueNoise(p);
  if (uNoiseMode < 0.5) return base;
  if (uNoiseMode < 1.5) return 1.0 - 2.0 * abs(base);
  return voronoiNoise(p);
}

float fbmValue(vec2 p) {
  float sum = 0.0;
  float weight = 1.0;
  float weightSum = 0.0;
  vec2 samplePoint = p * uFrequency;

  float octaveLimit = (uNoiseMode > 0.5 && uFeatureFbm < 0.5) ? 1.0 : uOctaves;
  float sampleFrequency = uFrequency;
  float nyquistFrequency = 0.5 / max(uGridSpacing, 0.0001);
  for (int octave = 0; octave < 8; octave++) {
    if (float(octave) >= octaveLimit) break;
    float bandWeight = 1.0 - smoothstep(nyquistFrequency * 0.82, nyquistFrequency, sampleFrequency);
    sum += terrainNoise(samplePoint) * weight * bandWeight;
    weightSum += weight * bandWeight;
    samplePoint = samplePoint * uLacunarity + vec2(17.1, 9.2);
    sampleFrequency *= uLacunarity;
    weight *= uGain;
  }

  return sum / max(weightSum, 0.0001);
}

float reshape(float rawHeight) {
  float normalized = clamp(rawHeight * 0.5 + 0.5, 0.0, 1.0);
  return pow(normalized, uReshapePower);
}

float baseHeight(vec2 p) {
  return reshape(fbmValue(p));
}

float broadHeight(vec2 p) {
  return reshape(terrainNoise(p * uFrequency));
}

float erodedHeight(vec2 p) {
  float detailed = baseHeight(p);
  if (uErosionEnabled < 0.5) return detailed;

  float epsilon = 0.11;
  float dx = broadHeight(p + vec2(epsilon, 0.0)) - broadHeight(p - vec2(epsilon, 0.0));
  float dz = broadHeight(p + vec2(0.0, epsilon)) - broadHeight(p - vec2(0.0, epsilon));
  float slope = length(vec2(dx, dz)) / (2.0 * epsilon);
  float weathering = exp(-slope * uErosionStrength * 3.5);
  float broadShape = broadHeight(p);
  return mix(broadShape, detailed, clamp(weathering, 0.08, 1.0));
}

float terrace(float heightValue, float steps) {
  float scaled = clamp(heightValue, 0.0, 0.9999) * steps;
  float shelf = floor(scaled);
  float local = fract(scaled);
  float shortRamp = smoothstep(0.76, 0.96, local);
  return (shelf + shortRamp) / steps;
}

float lowFrequencyTerraces(vec2 p) {
  vec2 samplePoint = p * uFrequency * 0.34;
  float sum = 0.0;
  float weight = 1.0;
  float weightSum = 0.0;

  for (int octave = 0; octave < 4; octave++) {
    sum += valueNoise(samplePoint) * weight;
    weightSum += weight;
    samplePoint = samplePoint * 2.03 + vec2(11.7, 4.3);
    weight *= 0.49;
  }

  float shaped = pow(clamp(sum / weightSum * 0.5 + 0.5, 0.0, 1.0), 2.35);
  return terrace(shaped, max(uTerraceSteps, 2.0));
}

float finalHeight(vec2 p) {
  float result = erodedHeight(p);

  if (uCombinedPreset > 0.5) {
    float largeForm = lowFrequencyTerraces(p);
    result = clamp(mix(largeForm, result, 0.46), 0.0, 1.0);
  } else if (uTerraceEnabled > 0.5) {
    result = terrace(result, max(uTerraceSteps, 2.0));
  }

  return result;
}

void main() {
  vec2 terrainPosition = position.xz + vec2(uTime * 0.002, 0.0);
  float heightValue = finalHeight(terrainPosition);
  float heightX = finalHeight(terrainPosition + vec2(uGridSpacing, 0.0));
  float heightZ = finalHeight(terrainPosition + vec2(0.0, uGridSpacing));
  float gradientX = (heightX - heightValue) * uAmplitude / uGridSpacing;
  float gradientZ = (heightZ - heightValue) * uAmplitude / uGridSpacing;
  vec3 localNormal = normalize(vec3(-gradientX, 1.0, -gradientZ));
  vec3 displaced = vec3(position.x, (heightValue - 0.28) * uAmplitude, position.z);
  vec4 worldPosition = modelMatrix * vec4(displaced, 1.0);
  vWorldPosition = worldPosition.xyz;
  vWorldNormal = normalize(mat3(modelMatrix) * localNormal);
  vHeight = heightValue;
  gl_Position = projectionMatrix * viewMatrix * worldPosition;
}
`;

export const fragmentShader = /* glsl */ `
precision highp float;

uniform vec3 uSkyColor;
uniform float uDistanceFogEnabled;
uniform float uHeightFogEnabled;
uniform float uFogDensity;
uniform float uScatterSeparated;

varying vec3 vWorldPosition;
varying vec3 vWorldNormal;
varying float vHeight;

float heightFogOpticalDepth(vec3 ray, float distanceToSurface) {
  float falloff = 0.24;
  float fogFloor = -3.0;
  float densityAtCamera = exp(-falloff * (cameraPosition.y - fogFloor));
  float verticalChange = falloff * ray.y * distanceToSurface;
  float integral;

  if (abs(verticalChange) < 0.001) {
    integral = densityAtCamera * distanceToSurface;
  } else {
    integral = densityAtCamera * (1.0 - exp(-verticalChange)) / verticalChange;
    integral *= distanceToSurface;
  }

  return max(integral * uFogDensity, 0.0);
}

void main() {
  vec3 normal = normalize(vWorldNormal);
  if (normal.y < 0.0) normal *= -1.0;

  float slope = 1.0 - clamp(normal.y, 0.0, 1.0);
  vec3 lowRock = vec3(0.10, 0.135, 0.15);
  vec3 highRock = vec3(0.42, 0.45, 0.45);
  vec3 snow = vec3(0.96, 0.98, 0.96);
  vec3 groundColor = mix(lowRock, highRock, smoothstep(0.12, 0.68, vHeight));
  float gentleSlope = 1.0 - smoothstep(0.30, 0.86, slope);
  float snowLine = smoothstep(0.14, 0.38, vHeight) * gentleSlope;
  float highAltitudeSnow = smoothstep(0.20, 0.45, vHeight);
  snowLine = max(snowLine, highAltitudeSnow * mix(0.64, 0.96, gentleSlope));
  groundColor = mix(groundColor, snow, snowLine);

  vec3 lightDirection = normalize(vec3(-0.48, 0.74, 0.46));
  float diffuse = max(dot(normal, lightDirection), 0.0);
  float halfLambert = diffuse * 0.66 + 0.34;
  float rim = pow(1.0 - max(dot(normal, normalize(cameraPosition - vWorldPosition)), 0.0), 3.0);
  vec3 color = groundColor * halfLambert + vec3(0.09, 0.15, 0.17) * rim * 0.35;

  vec3 cameraRay = vWorldPosition - cameraPosition;
  float distanceToSurface = length(cameraRay);
  vec3 rayDirection = cameraRay / max(distanceToSurface, 0.0001);

  if (uHeightFogEnabled > 0.5) {
    float opticalDepth = heightFogOpticalDepth(rayDirection, distanceToSurface);
    float transmittance = exp(-opticalDepth);

    if (uScatterSeparated > 0.5) {
      float sunFacing = pow(max(dot(-rayDirection, lightDirection), 0.0), 6.0);
      vec3 inScattering = uSkyColor * (1.0 - transmittance) * (0.72 + 0.38 * sunFacing);
      color = color * transmittance + inScattering;
    } else {
      color = mix(color, uSkyColor, 1.0 - transmittance);
    }
  }

  if (uDistanceFogEnabled > 0.5) {
    float distanceFog = 1.0 - exp(-distanceToSurface * distanceToSurface * 0.00072);
    color = mix(color, uSkyColor, clamp(distanceFog, 0.0, 0.92));
  }

  color *= 1.0 - smoothstep(0.76, 1.0, distance(vWorldPosition.xz, vec2(0.0)) / 30.0) * 0.08;
  gl_FragColor = vec4(color, 1.0);
}
`;
