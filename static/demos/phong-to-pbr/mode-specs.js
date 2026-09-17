const range = (id, label, min, max, step, value) => ({ id, label, type: 'range', min, max, step, value });
const select = (id, label, value, options) => ({ id, label, type: 'select', value, options });
const checkbox = (id, label, value) => ({ id, label, type: 'checkbox', value });
const color = (id, label, value) => ({ id, label, type: 'color', value });

export const MODE_IDS = Object.freeze([
  'compare',
  'ggx-d',
  'fresnel',
  'smith-g',
  'metalness',
  'normal',
  'ibl',
  'pipeline',
  'studio',
]);

export const COMMON_LIMIT = '교육용 단일 산란 모델입니다. 불투명, 등방성, 단일 레이어 표면만 다루며 Unity와 Unreal의 버전별 구현을 완전히 재현하지 않습니다.';

export const RENDER_DEFAULTS = Object.freeze({
  legacyModel: 'blinn-phong',
  shininess: 64,
  roughness: 0.4,
  halfAngle: 24,
  ior: 1.5,
  viewAngle: 55,
  geometryEnabled: true,
  baseColor: '#b86b42',
  metallic: 0,
  normalStrength: 0,
  normalFrequency: 10,
  environmentIntensity: 1,
  environmentRotation: 0,
  lightAngle: 38,
  lightRadiance: 6,
  exposure: 1,
  toneMapper: 'aces',
  showIncorrect: true,
});

export const MODE_SPECS = Object.freeze({
  compare: {
    title: 'Phong에서 미세면으로',
    eyebrow: '01 / LEGACY → MICROFACET',
    badge: { label: 'PERCEPTUAL', value: 'α = r²' },
    question: '같은 빛인데 하이라이트를 계산하는 규칙이 달라지면 무엇이 보일까요?',
    limits: '왼쪽 Phong/Blinn-Phong은 경험적 lobe입니다. roughness와 shininess는 서로 동치인 값이 아닙니다.',
    stageLabels: ['PHONG / BLINN-PHONG', 'COOK-TORRANCE'],
    controls: [
      select('legacyModel', '왼쪽 모델', 'blinn-phong', [['Blinn-Phong', 'blinn-phong'], ['Phong', 'phong']]),
      range('shininess', 'legacy 지수', 4, 256, 1, 64),
      range('roughness', 'PBR roughness', 0.09, 1, 0.01, 0.32),
      range('lightAngle', '빛의 각도', 10, 80, 1, 38),
    ],
    probe: { control: 'roughness', value: 0.78 },
  },
  'ggx-d': {
    title: 'GGX가 펼치는 미세면',
    eyebrow: '02 / NORMAL DISTRIBUTION D',
    badge: { label: 'DISTRIBUTION', value: 'D / D(1)' },
    question: 'roughness 하나가 반사에 알맞게 기울어진 미세면의 비율을 어떻게 바꿀까요?',
    limits: '화면 색은 D / D(1)로 정규화한 분포 모양입니다. 재질의 최종 밝기가 아니며, 실제 D 값은 오른쪽 수치로 따로 표시합니다.',
    axes: { x: '미세면 반각 θh / 0° → 90°', y: 'D / D(1)' },
    stageLabels: ['정규화된 D 분포', '선택 각도'],
    controls: [
      range('roughness', 'perceptual roughness', 0.09, 1, 0.01, 0.32),
      range('halfAngle', '미세면 반각', 0, 89, 1, 24),
    ],
    probe: { control: 'roughness', value: 0.82 },
  },
  fresnel: {
    title: '비스듬할수록 강해지는 반사',
    eyebrow: '03 / SCHLICK FRESNEL F',
    badge: { label: 'DIELECTRIC', value: 'IOR → F₀' },
    question: '같은 표면도 정면과 가장자리에서 왜 다르게 반사될까요?',
    limits: '매끄러운 경계의 시점 데모에서는 cos θ=dot(N,V)로 읽습니다. Cook-Torrance 직접광 안의 Schlick 항은 dot(V,H)를 사용합니다.',
    axes: { x: '시선각 θ / 0° → 90°', y: 'F' },
    stageLabels: ['F₀ / 정면 반사', 'F / 현재 각도'],
    controls: [
      range('ior', '굴절률 IOR', 1, 2.5, 0.01, 1.5),
      range('viewAngle', '보는 각도', 0, 89, 1, 62),
    ],
    probe: { control: 'viewAngle', value: 84 },
  },
  'smith-g': {
    title: '서로 가리는 미세면',
    eyebrow: '04 / SMITH MASKING-SHADOWING G',
    badge: { label: 'VISIBILITY', value: '0 ≤ G ≤ 1' },
    question: '표면을 비스듬히 볼 때 모든 미세면이 정말 카메라와 빛에 열려 있을까요?',
    notice: '주의: G 끄기는 비교용 G=1이며 물리 재질이 아닙니다.',
    limits: '두 시편에는 같은 직교 시선 벡터와 같은 방향광을 적용합니다. G는 미세면 사이의 masking-shadowing이며 shadow map이나 물체가 바닥에 만드는 거시 그림자는 계산하지 않습니다.',
    stageLabels: ['G = 1 / 비교용', 'SMITH G / 적용'],
    controls: [
      range('roughness', 'roughness', 0.09, 1, 0.01, 0.48),
      range('viewAngle', '보는 각도', 0, 86, 1, 72),
      checkbox('geometryEnabled', '오른쪽에 Smith G 적용', true),
    ],
    probe: { control: 'viewAngle', value: 84 },
  },
  metalness: {
    title: '색이 이동하는 자리',
    eyebrow: '05 / METALNESS WORKFLOW',
    badge: { label: 'WORKFLOW', value: 'F₀ = mix' },
    question: 'baseColor는 언제 몸체색이고, 언제 반사색이 될까요?',
    limits: '균질한 실제 물질은 metallic 0 또는 1이 보통입니다. 중간값은 텍스처 경계와 재질 혼합을 관찰하기 위한 작가용 값입니다.',
    stageLabels: ['DIELECTRIC / 0', '조절값', 'METAL / 1'],
    controls: [
      color('baseColor', 'baseColor', '#b87333'),
      range('metallic', 'metallic', 0, 1, 0.01, 0.38),
      range('roughness', 'roughness', 0.09, 1, 0.01, 0.28),
      range('ior', 'dielectric IOR', 1, 2.5, 0.01, 1.5),
    ],
    probe: { control: 'metallic', value: 0.82 },
  },
  normal: {
    title: '기하는 그대로, 빛의 방향만',
    eyebrow: '06 / NORMAL PERTURBATION',
    badge: { label: 'SHADING', value: 'N → N′' },
    question: '표면을 실제로 울퉁불퉁하게 만들지 않고도 왜 요철이 보일까요?',
    limits: '절차적 tangent-space 무늬가 shading normal만 바꿉니다. 실루엣, self-occlusion, 높이, parallax는 바뀌지 않습니다.',
    stageLabels: ['기하 노멀', '변형된 셰이딩 노멀'],
    controls: [
      range('normalStrength', '노멀 강도', 0, 2, 0.01, 1),
      range('normalFrequency', '무늬 빈도', 2, 20, 1, 10),
      range('roughness', 'roughness', 0.09, 1, 0.01, 0.4),
    ],
    probe: { control: 'normalStrength', value: 1.75 },
  },
  ibl: {
    title: '환경 전체가 광원이 될 때',
    eyebrow: '07 / IMAGE-BASED LIGHTING',
    badge: { label: 'PREFILTER', value: 'PMREM LOD' },
    question: 'roughness가 올라가면 환경 반사는 어떤 방식으로 흐려질까요?',
    limits: '선형 HDR 환경을 Three.js PMREM 근사로 prefilter합니다. PMREM은 계산 가능한 실시간 커널이며 정확한 GGX 적분이 아닙니다. diffuse는 같은 환경을 cosine-weighted 수치적분합니다.',
    stageLabels: ['매끈한 기준 / r 0.09', '조절 roughness'],
    controls: [
      color('baseColor', 'baseColor', '#a66b45'),
      range('roughness', 'roughness', 0.09, 1, 0.01, 0.18),
      range('metallic', 'metallic', 0, 1, 0.01, 0.68),
      range('environmentIntensity', '환경 밝기', 0, 2.5, 0.01, 1.2),
      range('environmentRotation', '환경 방향', -180, 180, 1, 0),
    ],
    probe: { control: 'roughness', value: 0.8 },
  },
  pipeline: {
    title: '밝기는 마지막에 접는다',
    eyebrow: '08 / LINEAR → EXPOSURE → DISPLAY',
    badge: { label: 'PIPELINE', value: 'LINEAR FIRST' },
    question: '조명 합산과 화면 변환의 순서를 바꾸면 같은 수치가 왜 다른 색이 될까요?',
    notice: '주의: 오른쪽은 sRGB 공간에서 빛을 더하는 의도적 오산입니다.',
    limits: 'ACES는 full ACES가 아닌 fitted approximation입니다.',
    stageLabels: ['선형 HDR 파이프라인', 'sRGB 합산 / 잘못된 예'],
    controls: [
      range('lightRadiance', 'HDR 빛 세기', 1, 16, 0.1, 7),
      range('exposure', 'exposure', 0.2, 2.5, 0.01, 1),
      select('toneMapper', 'tone mapper', 'aces', [['ACES fitted', 'aces'], ['Reinhard', 'reinhard'], ['없음 (clip)', 'none']]),
      checkbox('showIncorrect', '오른쪽 오산 함께 보기', true),
    ],
    probe: { control: 'exposure', value: 1.85 },
  },
  studio: {
    title: 'PBR 재질 스튜디오',
    eyebrow: '09 / INTEGRATED SCENE',
    badge: { label: 'MICROFACET', value: 'D / F / G' },
    question: 'D, F, G와 재질 값, 환경광, 화면 변환을 한 장면에 합치면 어떻게 움직일까요?',
    limits: '직접광은 공통 single-scattering GGX+Smith+Schlick 경로, 간접광은 PMREM+split-sum 근사입니다. shadow map, 다중 산란 보상, clear coat, sheen, anisotropy, transmission, AO는 없습니다.',
    stageLabels: ['통합 시편', 'roughness 비교'],
    controls: [
      color('baseColor', 'baseColor', '#b7603b'),
      range('roughness', 'roughness', 0.09, 1, 0.01, 0.26),
      range('metallic', 'metallic', 0, 1, 0.01, 0.7),
      range('ior', 'dielectric IOR', 1, 2.5, 0.01, 1.5),
      range('normalStrength', '노멀 강도', 0, 1.5, 0.01, 0.45),
      range('lightRadiance', '직접광 radiance', 0, 12, 0.1, 6),
      range('environmentIntensity', '환경 밝기', 0, 2.5, 0.01, 1),
      range('environmentRotation', '환경 방향', -180, 180, 1, 0),
      range('exposure', 'exposure', 0.2, 2.5, 0.01, 1),
      select('toneMapper', 'tone mapper', 'aces', [['ACES fitted', 'aces'], ['Reinhard', 'reinhard'], ['없음 (clip)', 'none']]),
    ],
    probe: { control: 'metallic', value: 0.12 },
  },
});

export function createDefaultState(spec) {
  return {
    ...RENDER_DEFAULTS,
    ...Object.fromEntries(spec.controls.map((control) => [control.id, control.value])),
  };
}
