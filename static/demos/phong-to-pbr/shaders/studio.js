import { displayGLSL, meshVertexShader, pbrMathGLSL } from '../pbr-glsl.js';

export { meshVertexShader as vertexShader };

export const fragmentShader = /* glsl */`
  precision highp float;
  varying vec3 vWorldPosition;
  varying vec3 vWorldNormal;
  varying vec2 vUv;
  uniform sampler2D envMap;
  uniform sampler2D uIrradianceMap;
  uniform int uVisualMode;
  uniform int uVariant;
  uniform vec3 uBaseColor;
  uniform vec3 uLightPosition;
  uniform float uLightRadiance;
  uniform float uEnvironmentIntensity;
  uniform float uEnvironmentRotation;
  uniform float uRoughness;
  uniform float uMetallic;
  uniform float uIor;
  uniform float uNormalStrength;
  uniform float uExposure;
  uniform int uToneMapper;
  ${pbrMathGLSL}
  ${displayGLSL}
  #include <cube_uv_reflection_fragment>

  vec2 directionToEquirectUv(vec3 direction) {
    vec3 d = normalize(direction);
    return vec2(atan(d.z, d.x) / (2.0 * PBR_PI) + 0.5, asin(clamp(d.y, -1.0, 1.0)) / PBR_PI + 0.5);
  }

  vec2 envBrdfApprox(float NoV, float roughness) {
    vec4 c0 = vec4(-1.0, -0.0275, -0.572, 0.022);
    vec4 c1 = vec4(1.0, 0.0425, 1.04, -0.04);
    vec4 r = roughness * c0 + c1;
    float a004 = min(r.x * r.x, exp2(-9.28 * NoV)) * r.x + r.y;
    return vec2(-1.04, 1.04) * a004 + r.zw;
  }

  vec3 rotateEnvironment(vec3 direction) {
    float cosine = cos(uEnvironmentRotation);
    float sine = sin(uEnvironmentRotation);
    return vec3(
      cosine * direction.x + sine * direction.z,
      direction.y,
      -sine * direction.x + cosine * direction.z
    );
  }

  vec3 perturbNormal(vec3 surfaceNormal, float strength) {
    float frequency = 9.0;
    vec3 tangentNormal = normalize(vec3(
      sin(vUv.x * frequency * 6.2831853) * strength,
      cos(vUv.y * frequency * 6.2831853) * strength,
      1.0
    ));
    vec3 q0 = dFdx(vWorldPosition);
    vec3 q1 = dFdy(vWorldPosition);
    vec2 st0 = dFdx(vUv);
    vec2 st1 = dFdy(vUv);
    vec3 tangent = normalize(q0 * st1.t - q1 * st0.t);
    vec3 bitangent = normalize(-q0 * st1.s + q1 * st0.s);
    return normalize(mat3(tangent, bitangent, surfaceNormal) * tangentNormal);
  }

  vec3 evaluateIbl(vec3 n, vec3 v, vec3 baseColor, float roughness, float metallic, float ior) {
    float NoV = max(dot(n, v), 0.0);
    float dielectricF0 = pbrIorToF0(ior);
    vec3 f0 = mix(vec3(dielectricF0), baseColor, metallic);
    vec3 reflection = rotateEnvironment(reflect(-v, n));
    vec3 prefiltered = textureCubeUV(envMap, reflection, roughness).rgb;
    vec2 dfg = envBrdfApprox(NoV, roughness);
    vec3 specular = prefiltered * (f0 * dfg.x + dfg.y);
    vec3 irradiance = texture2D(uIrradianceMap, directionToEquirectUv(rotateEnvironment(n))).rgb;
    vec3 viewFresnel = pbrSchlickFresnel(NoV, f0);
    vec3 diffuseWeight = (vec3(1.0) - viewFresnel) * (1.0 - metallic);
    vec3 diffuse = diffuseWeight * baseColor * irradiance / PBR_PI;
    return (diffuse + specular) * uEnvironmentIntensity;
  }

  void main() {
    vec3 baseColor = uBaseColor;
    float roughness = uRoughness;
    float metallic = uMetallic;
    float normalStrength = uNormalStrength;
    if (uVisualMode == 0 && uVariant == 0) roughness = 0.09;
    if (uVisualMode == 1) {
      if (uVariant == 1) roughness = 0.14;
      if (uVariant == 2) roughness = 0.68;
      if (uVariant == 3) {
        roughness = 0.84;
        metallic = 0.0;
        normalStrength = 0.0;
        baseColor = vec3(0.055, 0.065, 0.085);
      }
    }
    vec3 n = perturbNormal(normalize(vWorldNormal), normalStrength);
    vec3 v = normalize(cameraPosition - vWorldPosition);
    vec3 l = normalize(uLightPosition - vWorldPosition);
    vec3 indirect = evaluateIbl(n, v, baseColor, roughness, metallic, uIor);
    vec3 direct = vec3(0.0);
    if (uVisualMode == 1 && uLightRadiance > 0.0) {
      direct = pbrEvaluateDirect(
        n, v, l, baseColor, roughness, metallic, uIor,
        vec3(uLightRadiance), 1.0
      ).radiance;
    }
    vec3 color = pbrLinearToSrgb(pbrToneMap(indirect + direct, uExposure, uToneMapper));
    gl_FragColor = vec4(color, 1.0);
  }
`;
