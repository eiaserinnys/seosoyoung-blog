import { displayGLSL, pbrMathGLSL, screenVertexShader } from '../pbr-glsl.js';

export { screenVertexShader as vertexShader };

export const fragmentShader = /* glsl */`
  precision highp float;
  varying vec2 vUv;
  uniform int uMode;
  uniform vec2 uResolution;
  uniform float uRoughness;
  uniform float uHalfAngle;
  uniform float uIor;
  uniform float uViewAngle;
  uniform float uLightRadiance;
  uniform float uExposure;
  uniform int uToneMapper;
  uniform float uShowIncorrect;
  ${pbrMathGLSL}
  ${displayGLSL}

  float lineMask(float y, float target, float width) {
    return 1.0 - smoothstep(width, width * 2.0, abs(y - target));
  }

  vec3 grid(vec2 uv) {
    vec2 fine = abs(fract(uv * vec2(8.0, 5.0)) - 0.5);
    float lines = 1.0 - smoothstep(0.46, 0.49, max(fine.x, fine.y));
    return mix(vec3(0.025, 0.032, 0.05), vec3(0.055, 0.066, 0.09), lines * 0.55);
  }

  vec3 drawGgx() {
    vec2 uv = vUv;
    float alpha = uRoughness * uRoughness;
    float theta = uv.x * 1.553343;
    float D = pbrGgxD(cos(theta), alpha);
    float peak = pbrGgxD(1.0, alpha);
    float normalized = clamp(D / peak, 0.0, 1.0);
    float curveY = 0.12 + 0.76 * normalized;
    vec3 color = grid(uv);
    float fill = smoothstep(curveY, curveY - 0.012, uv.y);
    color = mix(color, vec3(0.06, 0.25, 0.34), fill * 0.55);
    color = mix(color, vec3(0.35, 0.9, 1.0), lineMask(uv.y, curveY, 0.006));
    float markerX = clamp(uHalfAngle / 89.0, 0.0, 1.0);
    color = mix(color, vec3(1.0, 0.55, 0.2), lineMask(uv.x, markerX, 0.0025));
    return color;
  }

  vec3 drawFresnel() {
    vec2 uv = vUv;
    float angle = uv.x * 1.553343;
    float f0 = pbrIorToF0(uIor);
    float F = pbrSchlickFresnel(cos(angle), vec3(f0)).r;
    float curveY = 0.1 + F * 0.8;
    vec3 color = grid(uv);
    float fill = smoothstep(curveY, curveY - 0.015, uv.y);
    color = mix(color, vec3(0.22, 0.12, 0.33), fill * 0.66);
    color = mix(color, vec3(0.98, 0.58, 0.94), lineMask(uv.y, curveY, 0.006));
    float markerX = clamp(uViewAngle / 89.0, 0.0, 1.0);
    color = mix(color, vec3(1.0, 0.72, 0.3), lineMask(uv.x, markerX, 0.0025));
    float currentF = pbrSchlickFresnel(cos(radians(uViewAngle)), vec3(f0)).r;
    float markerY = 0.1 + currentF * 0.8;
    float point = 1.0 - smoothstep(0.008, 0.022, distance(uv, vec2(markerX, markerY)));
    return mix(color, vec3(1.0), point);
  }

  vec3 lightBlob(vec2 uv, vec2 center, vec3 color, float power) {
    float distanceSquared = dot(uv - center, uv - center);
    return color * power * exp(-distanceSquared * 18.0);
  }

  vec3 drawPipeline() {
    vec2 uv = vUv;
    bool incorrectSide = uv.x > 0.5 && uShowIncorrect > 0.5;
    vec2 localUv = vec2(fract(uv.x * 2.0), uv.y);
    vec3 baseSrgb = mix(vec3(0.05, 0.07, 0.13), vec3(0.58, 0.24, 0.08), smoothstep(0.05, 0.95, localUv.y));
    vec3 baseLinear = pbrSrgbToLinear(baseSrgb);
    vec3 warm = lightBlob(localUv, vec2(0.3, 0.62), vec3(1.0, 0.18, 0.03), uLightRadiance);
    vec3 cool = lightBlob(localUv, vec2(0.72, 0.44), vec3(0.04, 0.28, 1.0), uLightRadiance * 0.82);
    vec3 ambient = vec3(0.025, 0.035, 0.08);
    if (!incorrectSide) {
      vec3 linearHdr = baseLinear * (ambient + warm + cool);
      return pbrLinearToSrgb(pbrToneMap(linearHdr, uExposure, uToneMapper));
    }
    vec3 wrong = baseSrgb * (
      pbrLinearToSrgb(ambient) + pbrLinearToSrgb(warm) + pbrLinearToSrgb(cool)
    ) * uExposure;
    return clamp(wrong, 0.0, 1.0);
  }

  void main() {
    vec3 color = uMode == 0 ? drawGgx() : (uMode == 1 ? drawFresnel() : drawPipeline());
    float divider = smoothstep(0.0, 1.5 / max(uResolution.x, 1.0), abs(vUv.x - 0.5));
    if (uMode == 2) color = mix(vec3(0.72, 0.75, 0.84), color, divider);
    gl_FragColor = vec4(color, 1.0);
  }
`;
