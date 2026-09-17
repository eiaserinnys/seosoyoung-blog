export const MIN_ROUGHNESS = 0.09;
export const PBR_EPSILON = 1e-6;
const PI = Math.PI;

export function clamp01(value) {
  return Math.min(1, Math.max(0, value));
}

export function roughnessToAlpha(roughness) {
  return roughness * roughness;
}

export function iorToF0(ior) {
  const ratio = (ior - 1) / (ior + 1);
  return ratio * ratio;
}

export function ggxDistribution(noH, alpha) {
  const clampedNoH = clamp01(noH);
  const alpha2 = alpha * alpha;
  const factor = clampedNoH * clampedNoH * (alpha2 - 1) + 1;
  return alpha2 / (PI * factor * factor);
}

export function schlickFresnel(voH, f0) {
  const factor = (1 - clamp01(voH)) ** 5;
  if (Array.isArray(f0)) return f0.map((channel) => channel + (1 - channel) * factor);
  return f0 + (1 - f0) * factor;
}

export function smithGCorrelated(noV, noL, alpha) {
  const clampedNoV = clamp01(noV);
  const clampedNoL = clamp01(noL);
  if (clampedNoV === 0 || clampedNoL === 0) return 0;
  const alpha2 = alpha * alpha;
  const lambdaV = Math.sqrt(alpha2 + (1 - alpha2) * clampedNoV * clampedNoV);
  const lambdaL = Math.sqrt(alpha2 + (1 - alpha2) * clampedNoL * clampedNoL);
  const denominator = clampedNoL * lambdaV + clampedNoV * lambdaL;
  return (2 * clampedNoL * clampedNoV) / Math.max(denominator, PBR_EPSILON);
}

function mixColor(a, b, amount) {
  return a.map((channel, index) => channel * (1 - amount) + b[index] * amount);
}

export function evaluateDirectLight({
  roughness,
  noV,
  noL,
  noH,
  voH,
  metallic,
  ior,
  baseColor,
  lightRadiance,
  geometryEnabled = true,
}) {
  const alpha = roughnessToAlpha(roughness);
  const dielectricF0 = iorToF0(ior);
  const f0 = mixColor([dielectricF0, dielectricF0, dielectricF0], baseColor, metallic);
  const D = ggxDistribution(noH, alpha);
  const F = schlickFresnel(voH, f0);
  const G = geometryEnabled ? smithGCorrelated(noV, noL, alpha) : 1;
  const denominator = Math.max(4 * clamp01(noL) * clamp01(noV), PBR_EPSILON);
  const specular = F.map((channel) => (D * channel * G) / denominator);
  const diffuse = baseColor.map((channel, index) => (
    ((1 - F[index]) * (1 - metallic) * channel) / PI
  ));
  const radiance = lightRadiance.map((channel, index) => (
    (diffuse[index] + specular[index]) * channel * clamp01(noL)
  ));
  return { alpha, D, F, G, f0, specular, diffuse, radiance };
}

export function srgbChannelToLinear(channel) {
  return channel <= 0.04045 ? channel / 12.92 : ((channel + 0.055) / 1.055) ** 2.4;
}

export function hexToLinearRgb(hex) {
  const normalized = hex.replace('#', '');
  const channels = [0, 2, 4].map((offset) => Number.parseInt(normalized.slice(offset, offset + 2), 16) / 255);
  return channels.map(srgbChannelToLinear);
}

export function modeMetrics(mode, state) {
  const roughness = state.roughness ?? 0.5;
  const alpha = roughnessToAlpha(roughness);
  const selectedAngle = mode === 'ggx-d' ? state.halfAngle : state.viewAngle;
  const angle = (selectedAngle ?? 45) * PI / 180;
  const baseColor = hexToLinearRgb(state.baseColor ?? '#b86b42');
  if (mode === 'ggx-d') {
    const noH = Math.cos(angle);
    return [['α = r²', alpha.toFixed(4)], ['N, H 내적', noH.toFixed(3)], ['실제 D', ggxDistribution(noH, alpha).toFixed(4)]];
  }
  if (mode === 'fresnel') {
    const f0 = iorToF0(state.ior);
    return [['F₀', f0.toFixed(4)], ['cos θ', Math.cos(angle).toFixed(3)], ['F', schlickFresnel(Math.cos(angle), f0).toFixed(4)]];
  }
  if (mode === 'smith-g') {
    const noV = Math.cos(angle);
    const G = smithGCorrelated(noV, 0.72, alpha);
    return [['α = r²', alpha.toFixed(4)], ['N, V 내적', noV.toFixed(3)], ['Smith G', G.toFixed(4)]];
  }
  if (mode === 'metalness') {
    const dielectricF0 = iorToF0(state.ior);
    const f0 = mixColor([dielectricF0, dielectricF0, dielectricF0], baseColor, state.metallic);
    return [['dielectric F₀', dielectricF0.toFixed(3)], ['평균 F₀', (f0.reduce((a, b) => a + b, 0) / 3).toFixed(3)], ['비금속 가중치 (1-m)', (1 - state.metallic).toFixed(2)]];
  }
  if (mode === 'normal') {
    const z = 1 / Math.sqrt(1 + state.normalStrength * state.normalStrength);
    return [['노멀 강도', state.normalStrength.toFixed(2)], ['패턴 빈도', state.normalFrequency.toFixed(0)], ['기준 Z 근사', z.toFixed(3)]];
  }
  if (mode === 'compare') return [['PBR α', alpha.toFixed(4)], ['legacy 지수', state.shininess.toFixed(0)], ['legacy', state.legacyModel]];
  if (mode === 'ibl') return [['PMREM roughness', roughness.toFixed(2)], ['환경 방향', `${state.environmentRotation.toFixed(0)}°`], ['환경 배수', `${state.environmentIntensity.toFixed(2)}×`]];
  if (mode === 'pipeline') return [['선형 radiance', state.lightRadiance.toFixed(1)], ['노출', `${state.exposure.toFixed(2)}×`], ['톤매퍼', state.toneMapper]];
  return [['α = r²', alpha.toFixed(4)], ['금속성', state.metallic.toFixed(2)], ['환경 방향', `${state.environmentRotation.toFixed(0)}°`]];
}
