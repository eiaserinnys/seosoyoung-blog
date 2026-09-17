import { displayGLSL, meshVertexShader, pbrMathGLSL } from '../pbr-glsl.js';

export { meshVertexShader as vertexShader };

export const fragmentShader = /* glsl */`
  precision highp float;
  varying vec3 vWorldPosition;
  varying vec3 vWorldNormal;
  varying vec2 vUv;
  uniform int uVisualMode;
  uniform int uVariant;
  uniform int uLegacyModel;
  uniform float uShininess;
  uniform vec3 uBaseColor;
  uniform vec3 uLightPosition;
  uniform vec3 uLightDirection;
  uniform vec3 uViewDirection;
  uniform float uLightRadiance;
  uniform float uRoughness;
  uniform float uMetallic;
  uniform float uIor;
  uniform float uNormalStrength;
  uniform float uNormalFrequency;
  uniform float uGeometryEnabled;
  ${pbrMathGLSL}
  ${displayGLSL}

  vec3 perturbNormal(vec3 surfaceNormal, float strength) {
    float waveX = sin(vUv.x * uNormalFrequency * 6.2831853);
    float waveY = cos(vUv.y * uNormalFrequency * 6.2831853);
    vec3 tangentNormal = normalize(vec3(waveX * strength, waveY * strength, 1.0));
    vec3 q0 = dFdx(vWorldPosition);
    vec3 q1 = dFdy(vWorldPosition);
    vec2 st0 = dFdx(vUv);
    vec2 st1 = dFdy(vUv);
    vec3 tangent = normalize(q0 * st1.t - q1 * st0.t);
    vec3 bitangent = normalize(-q0 * st1.s + q1 * st0.s);
    mat3 tbn = mat3(tangent, bitangent, surfaceNormal);
    return normalize(tbn * tangentNormal);
  }

  vec3 legacyLight(vec3 n, vec3 v, vec3 l) {
    float NoL = max(dot(n, l), 0.0);
    vec3 h = normalize(v + l);
    float phongDot = max(dot(reflect(-l, n), v), 0.0);
    float blinnDot = max(dot(n, h), 0.0);
    float lobe = pow(uLegacyModel == 0 ? phongDot : blinnDot, max(1.0, uShininess));
    vec3 diffuse = uBaseColor / PBR_PI;
    vec3 specular = vec3(0.7) * lobe;
    return (diffuse + specular) * vec3(uLightRadiance) * NoL;
  }

  void main() {
    vec3 geometricNormal = normalize(vWorldNormal);
    float normalStrength = (uVisualMode == 3 && uVariant == 0) ? 0.0 : uNormalStrength;
    vec3 n = perturbNormal(geometricNormal, normalStrength);
    vec3 v = uVisualMode == 1 ? normalize(uViewDirection) : normalize(cameraPosition - vWorldPosition);
    vec3 l = uVisualMode == 1 ? normalize(uLightDirection) : normalize(uLightPosition - vWorldPosition);
    float metallic = uMetallic;
    if (uVisualMode == 2) {
      if (uVariant == 0) metallic = 0.0;
      if (uVariant == 2) metallic = 1.0;
    }
    float geometryEnabled = uVisualMode == 1 && uVariant == 0 ? 0.0 : uGeometryEnabled;
    PbrDirectResult pbr = pbrEvaluateDirect(
      n, v, l, uBaseColor, uRoughness, metallic, uIor,
      vec3(uLightRadiance), geometryEnabled
    );
    vec3 hdr = pbr.radiance;
    if (uVisualMode == 0 && uVariant == 0) hdr = legacyLight(n, v, l);
    vec3 color = pbrLinearToSrgb(pbrToneMap(hdr, 1.0, 2));
    gl_FragColor = vec4(color, 1.0);
  }
`;
