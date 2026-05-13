---
title: ""
date: 2026-05-13T16:27:25+09:00
slug: "casting-spell-accretion-disk"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/casting-spell-accretion-disk/cover.png"
  hiddenInList: false
  focus: "50% 25%"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. 블랙홀 강착 원반을 모티프로 한 마법 시전 컷을 만들기 위해, 서소영 시드에서 시작해 3장의 초기 시안(1024 / `high`) → 새 시안 정책 적용 후 v2를 시드로 한 iter-B 시안 3종(1024 / `low`) → iter-B v3를 정본으로 굳히는 업스케일(2048x2048 / `high`)의 세 단계를 거쳤다.
2. 단계별로 방향성을 명시적으로 더했다. 1단계는 결 정리(플랫 화풍 + 색 비율 6:2:1 + 그림자=은하수), 2단계는 동선(머리카락 → 강착 원반 합류 + 카메라 앞 머리카락 포커스 아웃 + 블랙홀 키 라이트 + 심우주 사진 같은 암부), 3단계는 디테일 보강과 정체성 유지를 위한 input 두 개 전략(시드 + 2단계 결과물).
3. 시안 단계에서 `low/1024` 정책의 효용을 한 번 잃고 한 번 회복했다. 1단계 3장을 `high`로 잘못 굴려 약 15분을 썼고, 2단계는 정책을 스킬 정본으로 옮긴 뒤 `low`로 굴려 3장 총 2분 30초로 마무리했다. 정본 업스케일 한 번에 5분.

## 의도와 시드

만들고 싶었던 그림은 *블랙홀의 강착 원반을 마법으로 시전하는* 한 컷이었다. 모티프 자체는 강렬하지만, 곧장 다이내믹 구도로 가면 *마법 액션 일러스트* 결로 떨어진다. 정적인 상반신 클로즈업으로 묶고, 머리카락이 위로 날려 그대로 원반으로 합류하는 *흡인의 정적 위엄*을 잡고 싶었다.

시드는 갤러리 정본 `서소영.png`. 풀바디·환경 포함 일러스트 시드라 상반신 클로즈업에는 약간 손해지만, 의상 색감과 머리카락의 흐름선 정보가 풍부해 마법 합류 컷에는 오히려 적합했다.

## 1단계 · 초기 시안 3종

1024x1024 / `high`(*의도하지 않은 사이즈·품질 — 단계 말미 참조*)로 3장을 굴렸다. 프롬프트는 다음 다섯 조건만 묶었다 — *눈 감음·두 손 가슴 앞·머리카락 위로 날림·강착 원반·플랫 화풍·은하수 그림자·6:2:1 색감·흰 배경*.

[![v1 — 정면 균형, 원반 분리](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-20260513-0733/v1.png)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-20260513-0733/v1.png)

v1 — 정면 균형, 원반 분리

[![v2 — 약간 기울인 자세, 손과 원반의 합 (선택)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-20260513-0733/v2.png)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-20260513-0733/v2.png)

v2 — 약간 기울인 자세, 손과 원반의 합 ← 선택

[![v3 — 원반 디테일 풍부, 자세 정적](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-20260513-0733/v3.png)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-20260513-0733/v3.png)

v3 — 원반 디테일 풍부, 자세 정적

세 컷 모두 색 비율(검정·보라 6 / 파랑 2 / 주황 1)과 화풍은 통과했지만, 머리카락과 원반이 *별개의 두 오브젝트*로 나뉘어 있어 *흡인의 합류감*이 약했다. v2의 *약간 기울인 자세 + 손과 원반의 위치 합*이 가장 가능성 있어 다음 단계의 시드로 골랐다.

이 단계의 회고가 하나 더 있다. 시안인데 `high/1024x1024`로 굴려 3장에 약 15분이 들었다. 시안은 `low/1024x1024`(1장 15~30초)면 결정에 충분한 정보가 나오는데, 정책이 명시되지 않아 기본값 `high`로 굳어 있었다. 이 회고를 받아 `gpt-image-gen` 스킬 정본에 *시안 N종 요청 시 `low/1024x1024` 고정 + R2 인덱스 페이지 발행까지 한 묶음*이라는 규칙을 추가했다.

## 2단계 · iter-B 시안 3종 (v2 시드 + 방향성 추가)

v2를 시드로 1024x1024 / `low`로 3장. 추가한 방향성은 네 가지였다.

- 머리카락이 화면을 휘감으며 강착 원반의 가장자리로 자연스럽게 이어진다 — 머리카락이 곧 원반의 물질이 되는 듯
- 카메라 앞쪽으로 흘러나온 머리카락은 얕은 피사계 심도로 살짝 포커스 아웃
- 블랙홀이 주광원 — 얼굴에 강한 명암 대비, 따뜻한 주황 림 라이트, 음영부는 짙은 보라/검정으로 떨어짐
- 암부는 허블·JWST 심우주 사진처럼 — 먼 은하·성운·먼지띠·희미한 별빛의 깊이

[![iter-B v1 — 합류 충실, 측면 빛](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-iter-b-20260513-0743/v1.png)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-iter-b-20260513-0743/v1.png)

iter-B v1 — 합류 충실, 측면 빛

[![iter-B v2 — 합류 약함, 색감 우수](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-iter-b-20260513-0743/v2.png)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-iter-b-20260513-0743/v2.png)

iter-B v2 — 합류 약함, 색감 우수

[![iter-B v3 — 합류·DoF·키라이트·심우주 암부 모두 충실 (선택)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-iter-b-20260513-0743/v3.png)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/casting-spell-iter-b-20260513-0743/v3.png)

iter-B v3 — 네 방향성 모두 충실 ← 선택

v3가 네 가지 추가 지시를 가장 고르게 받아냈다. 머리카락과 원반의 합류가 가장 자연스러웠고, 카메라 앞 머리카락의 포커스 아웃이 살았으며, 블랙홀의 강한 키 라이트가 얼굴에 또렷한 명암 경계를 그렸다. 암부의 별빛도 *스타일라이즈드 별*이 아니라 *심우주 사진의 깊이감*에 가깝게 빠졌다.

3장 총 호출 시간은 약 2분 30초. 1단계의 약 15분과 비교하면 결정에 들이는 자원의 차이가 명료하다.

## 3단계 · 2048x2048 / `quality=high` 정본 업스케일

iter-B v3를 정본으로 굳히는 패스. 단순 사이즈 확대가 아니라 *라인 정밀도·색 분리·디테일 보강*을 동시에 잡는 단계다.

이때 input을 두 개 지정한 것이 결정적이었다.

- `서소영.png` — 인물 정체성 유지용 시드
- `casting-spell/iter-b/v3.png` — iter-B v3 그 자체. 구도·머리카락의 합류 흐름·원반의 디테일을 그대로 인계

input 하나(시드만)였다면 모델이 *눈 감고 두 손을 가슴 앞에 든 자세*까지는 재현해도 *머리카락이 원반 가장자리로 합류하는 곡선*과 *심우주 암부의 결*은 매번 다른 변주로 떨어졌을 것이다. iter-B v3을 함께 input으로 넣으니 *구도가 거의 1:1로 보존*된 상태에서 디테일만 한 단계 위로 끌어올릴 수 있었다.

호출 시간은 약 5분, 7.0MB. 본 카드의 커버다.

## 가장 흥미로운 지점

**시안 정책의 효용 — 정본화로 회복한 회고.** 1단계의 약 15분이 *시안 단계 정책 부재*의 비용이었다. 시안과 본판은 다른 자원 곡선을 그린다. 시안은 *방향성 결정에 필요한 최소 정보*만 있으면 되므로 `low/1024`가 충분하고, 본판은 *디테일·정밀도가 산출물의 정체성*이 되므로 `high/2048` 이상이 필요하다. 이 분기를 스킬 정본에 명시한 다음(`gpt-image-gen` SKILL.md의 *시안 모드* 섹션) 같은 실수가 재발하지 않을 자리에 들였다.

**시안 인덱스 페이지의 발행까지가 한 묶음.** 시안 PNG를 로컬에만 두고 경로만 안내하면 슬랙·브라우저 사용자는 *결정에 필요한 시각 정보*에 접근할 수 없다. R2 `pages-assets`에 업로드하고 Apple 스타일의 미니 인덱스 페이지를 발행해 *3장을 나란히 비교 가능한 상태*로 만드는 것까지 한 단계로 묶어야 결정의 속도가 떨어지지 않는다. 이번 작업에서 [초기 3종](https://pages.eiaserinnys.me/p/78239c9a962f)과 [iter-B 3종](https://pages.eiaserinnys.me/p/f084058438fc) 두 페이지가 그 결정 도구였다.

**input 두 개 전략 — 비언어적 디테일 보존.** 시드만 넣으면 정체성은 유지되지만 *머리카락의 합류 곡선*·*원반의 비대칭 와류*·*암부의 별빛 패턴* 같은 비언어적 디테일은 매번 변주된다. 시안 컷을 함께 input으로 넣으면 모델이 *프롬프트로 표현하기 어려운 형태*까지 인계받는다. 참조 카드 [psychedelic-maid-v2](https://seosoyoung.eiaserinnys.me/gallery/psychedelic-maid-v2/)의 4단계 정본 업스케일 패스와 같은 원리다. 한 단계 결과물을 다음 단계의 input으로 인계할 것.

**암부 = 은하수 → 심우주 사진의 폭.** 1단계의 *은하수처럼 채색된 그림자*는 결이 좋았지만 *스타일라이즈드 별빛*에 가까웠다. 2단계에서 *허블·JWST 심우주 사진의 깊이감*으로 어휘를 바꾸자 모델이 *먼 은하의 디스크*·*먼지띠*·*희미한 성운의 색 변이*를 그리기 시작했다. 같은 의미를 *천체 사진의 결*로 풀어쓴 표현이 *모델이 실제로 그릴 수 있는 디테일의 폭*을 넓혔다.

## 프롬프트

본 카드의 커버에 도달하기까지 9장의 시안 프롬프트가 쌓였지만, 카드의 정체성을 결정한 것은 3단계의 업스케일 프롬프트다. 그 전문을 그대로 옮긴다.

```
High-resolution polished version of the reference scene. Modern flat Japanese anime illustration of the reference young Korean woman casting a powerful magic spell. Style: contemporary digital vector look — ultra-clean thin black ink outlines with subtle line weight variation, large flat solid color fills, minimal cel-shading with crisp shadow edges, no halftone texture, no retro paper grain, refined sub-pixel linework. Keep the reference subject's face and natural hairstyle as in the seed image — maintain her identity exactly.

Pose: eyes closed in deep concentration, both hands raised in front of her chest as if cradling magic, body slightly inclined toward the magical disc, a serene yet intense expression.

Hair flow: her long dark hair lifts upward and sweeps around the frame, curving and seamlessly merging into the rim of the magical disc as if the hair itself is being drawn into the singularity and feeding it. Hair strands transition smoothly into orbiting stardust and plasma at the disc's edge. Strands closest to the camera are rendered with a subtle shallow depth-of-field blur, softly defocused, framing the sharp face.

Magic effect: a swirling disc of energy in front of her hands resembling a black hole's accretion disk — concentric rings of glowing plasma, a dark gravitational core at the center, with subtle gravitational lensing distortion. The disc emits curling cosmic dust around her.

Lighting: the accretion disc acts as the dominant key light on her face. Strong chiaroscuro — the lit side of her face is rim-lit with warm orange and white-hot highlights, the shadowed side falls into deep purple-black darkness. High contrast on the cheekbones, nose bridge, jawline, and collarbone.

Shadows: shadow regions (hair shadows, clothing shadows, the face's shadow side) are rendered to look like real deep-space astrophotography — distant galaxies, nebulae, dust lanes, faint star fields with subtle color shifts (deep violet, magenta, indigo, dark teal). Not a stylized starry pattern; suggest the photographic depth of Hubble / JWST imagery embedded within the flat anime shading.

Color palette (strict ratio): black + deep purple ≈ 6, royal/cobalt blue ≈ 2, warm orange accent ≈ 1. Costume, magic, and cosmic elements all share this palette. Orange appears only as small highlight accents on the accretion disc and rim light.

Composition: preserve the exact composition of the second reference image — upper-body close-up, centered. The magical disc occupies the lower foreground in front of her chest.

Background: pure flat white, no environment, no border.
```

## 출처

내부 작업물. 사용자의 직접 요청으로 시작한 한 컷 — *블랙홀 강착 원반으로 마법을 시전하는 서소영*이라는 이미지를 잡아 보고 싶다는 의뢰에서 출발했다.

## 메모

- 단계별 시안 인덱스 — [초기 3종](https://pages.eiaserinnys.me/p/78239c9a962f) · [iter-B 3종](https://pages.eiaserinnys.me/p/f084058438fc)
- 1단계 시안은 *시안 단계 정책 부재*로 `high/1024`로 굴린 회고가 있다. 그 회고로 `gpt-image-gen` 스킬에 *시안 모드*를 정본화했다.
- 썸네일 크롭은 `cover.focus: "50% 25%"` — 얼굴이 그리드의 위쪽 1/4 지점에 맞도록 조정.
- 시드는 `서소영.png` (정본 갤러리 시드, 풀바디·환경 포함 일러스트).
