export const meshVertexShader = /* glsl */`
  varying vec3 vWorldPosition;
  varying vec3 vWorldNormal;
  varying vec2 vUv;

  void main() {
    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
    vWorldPosition = worldPosition.xyz;
    vWorldNormal = normalize(mat3(modelMatrix) * normal);
    vUv = uv;
    gl_Position = projectionMatrix * viewMatrix * worldPosition;
  }
`;

export const screenVertexShader = /* glsl */`
  varying vec2 vUv;
  void main() {
    vUv = uv;
    gl_Position = vec4(position.xy, 0.0, 1.0);
  }
`;

export const pbrMathGLSL = /* glsl */`
  #define PBR_PI 3.141592653589793
  #define PBR_EPSILON 0.000001

  struct PbrDirectResult {
    vec3 radiance;
    vec3 diffuse;
    vec3 specular;
    vec3 fresnel;
    float distribution;
    float geometry;
  };

  float pbrGgxD(float NoH, float alpha) {
    float alpha2 = alpha * alpha;
    float factor = NoH * NoH * (alpha2 - 1.0) + 1.0;
    return alpha2 / (PBR_PI * factor * factor);
  }

  vec3 pbrSchlickFresnel(float VoH, vec3 f0) {
    float factor = pow(1.0 - clamp(VoH, 0.0, 1.0), 5.0);
    return f0 + (vec3(1.0) - f0) * factor;
  }

  float pbrSmithGCorrelated(float NoV, float NoL, float alpha) {
    if (NoV <= 0.0 || NoL <= 0.0) return 0.0;
    float alpha2 = alpha * alpha;
    float lambdaV = sqrt(alpha2 + (1.0 - alpha2) * NoV * NoV);
    float lambdaL = sqrt(alpha2 + (1.0 - alpha2) * NoL * NoL);
    float denominator = NoL * lambdaV + NoV * lambdaL;
    return (2.0 * NoL * NoV) / max(denominator, PBR_EPSILON);
  }

  float pbrIorToF0(float ior) {
    float ratio = (ior - 1.0) / (ior + 1.0);
    return ratio * ratio;
  }

  PbrDirectResult pbrEvaluateDirect(
    vec3 n,
    vec3 v,
    vec3 l,
    vec3 baseColor,
    float perceptualRoughness,
    float metallic,
    float ior,
    vec3 lightRadiance,
    float geometryEnabled
  ) {
    vec3 h = normalize(v + l);
    float NoL = clamp(dot(n, l), 0.0, 1.0);
    float NoV = clamp(dot(n, v), 0.0, 1.0);
    float NoH = clamp(dot(n, h), 0.0, 1.0);
    float VoH = clamp(dot(v, h), 0.0, 1.0);
    float alpha = perceptualRoughness * perceptualRoughness;
    float dielectricF0 = pbrIorToF0(ior);
    vec3 f0 = mix(vec3(dielectricF0), baseColor, metallic);
    float D = pbrGgxD(NoH, alpha);
    vec3 F = pbrSchlickFresnel(VoH, f0);
    float smithG = pbrSmithGCorrelated(NoV, NoL, alpha);
    float G = mix(1.0, smithG, geometryEnabled);
    float denominator = max(4.0 * NoL * NoV, PBR_EPSILON);
    vec3 specular = D * F * G / denominator;
    vec3 diffuse = (vec3(1.0) - F) * (1.0 - metallic) * baseColor / PBR_PI;
    PbrDirectResult result;
    result.radiance = (diffuse + specular) * lightRadiance * NoL;
    result.diffuse = diffuse;
    result.specular = specular;
    result.fresnel = F;
    result.distribution = D;
    result.geometry = G;
    return result;
  }
`;

export const displayGLSL = /* glsl */`
  vec3 pbrToneMap(vec3 color, float exposure, int toneMapper) {
    color *= exposure;
    if (toneMapper == 1) return color / (vec3(1.0) + color);
    if (toneMapper == 2) {
      vec3 a = color * (2.51 * color + 0.03);
      vec3 b = color * (2.43 * color + 0.59) + 0.14;
      return clamp(a / b, 0.0, 1.0);
    }
    return clamp(color, 0.0, 1.0);
  }

  vec3 pbrLinearToSrgb(vec3 color) {
    vec3 low = color * 12.92;
    vec3 high = 1.055 * pow(max(color, vec3(0.0)), vec3(1.0 / 2.4)) - 0.055;
    return mix(high, low, lessThanEqual(color, vec3(0.0031308)));
  }

  vec3 pbrSrgbToLinear(vec3 color) {
    vec3 low = color / 12.92;
    vec3 high = pow((color + 0.055) / 1.055, vec3(2.4));
    return mix(high, low, lessThanEqual(color, vec3(0.04045)));
  }
`;
