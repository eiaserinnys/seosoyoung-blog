---
title: ""
date: 2026-05-17T18:14:35+09:00
slug: "seosoyoung-moth-veil"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-moth-veil/cover.png"
  hiddenInList: false
  focus: "50% 18%"
source: "자체 설계 — 외부 레퍼런스 이미지(주복 김 제공)를 베이스로 4 라운드 협업"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

- 레퍼런스 이미지의 막(膜) 두른 형상을 베이스 프롬프트로 풀고, 시드 인물에 입혀 4 라운드(1차 컨셉 → 역광·위엄 보정 → 포즈 회복·의상 확장 → 황금색 SSS 마스터)로 다듬은 카드.
- 같은 보정 지시도 *포즈 자체가 라운드를 넘어가며 휘발*된다. r2에서 정본 포즈를 잃었고, r3에서 명시적 PRESERVE 블록을 프롬프트 상단에 둬야 회복되었다.
- 황금색·SSS·금박을 한 라운드에 함께 얹어도 어색하지 않은 건, 베이스가 *막을 통과한 빛*이라는 단일한 광학 컨셉으로 처음부터 짜여 있었기 때문.

## 의도와 시드

출발은 주복 김이 던진 한 장의 레퍼런스 이미지였다. 회화체로 그려진, 막(膜) 같은 베일을 두른 정체불명의 형상. 그 자체를 프롬프트로 풀어내는 작업으로 시작했다.

```
Subject & pose
A solitary ethereal figure standing in a frontal, slightly symmetrical pose,
arms outstretched and lowered, body completely shrouded under layered
translucent membranous veils that spread out wide like a moth's wings or a
melting jellyfish. The silhouette is tall and tapering — a dark vertical core
at the center, fanning out into a wide skirt of overlapping organic drapes
that pool onto a wet reflective floor. The figure faces the viewer directly,
motionless, with a quiet, ceremonial stillness.

Face & head
A small, pale, porcelain-like oval face emerges at the top of the veils —
almost mask-like, expressionless, with minimal features and two small dark
eye markings. The face is the brightest point in the composition, catching
a soft top-down light.

Costume / membrane texture
Many overlapping sheets of thin, semi-translucent organic membrane — like wet
silk crossed with dried moth wings. Each sheet is dotted with irregular oval
and teardrop-shaped holes (eyespots), some rimmed with darker pigment,
creating a lace-like, perforated pattern. The membranes have a faintly
iridescent, oily sheen, with glossy highlights along their curling edges.
Inside the veils, near the core of the body, a deep black-to-charcoal
gradient suggests a hidden, slender silhouette underneath.

Color & lighting
Near-monochrome palette: ivory white, pearl, warm bone, charcoal, deep black.
A subtle warm amber glow seeps from the inner core — as if light is trapped
inside the body. Rim light traces the outer edges of the veils, separating
them from the pitch-black background. Soft specular highlights on the wet
floor reflect the lower veils.

Composition & background
Centered full-body composition, the figure occupying roughly 70% of the
frame's height. Plenty of negative space around the figure. Background is a
flat, near-black void with the faintest cool gradient. A wet, glass-like
floor reflects the bottom of the veils.

Style & rendering
Painterly digital illustration, concept-art quality, sharp focus on the face
and the membrane patterns, soft falloff toward the edges. Detailed but not
photographic — brushwork visible in the membrane translucency. Mood: solemn,
mournful, fairy-tale gothic, with a touch of biological eeriness.
```

이 베이스 프롬프트에 *서소영의 얼굴*을 시드로 얹기로 했다. 시드는 `서소영 (실사, 포트레이트).png` — 정체성 앵커가 가장 강한 카드. 회화적 의상 위로 사실적 얼굴이 살짝 떠 있는 결을 노렸다.

## 1단계 · 세 포즈 후보

같은 의상의 *세 순간*을 보여주는 변주로 시작했다. 정면 정적, 반측 각성, 의례의 위엄. 한 컨셉의 가능한 결을 모두 펼쳐놓고 어느 결로 더 들어갈지 정하는 라운드.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-still/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-still/cover.png" alt="시안 1 — 정면 정적" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">시안 1 — 정면·정적</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-awaken/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-awaken/cover.png" alt="시안 2 — 반측 각성" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">시안 2 — 반측·각성 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-rite/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-rite/cover.png" alt="시안 3 — 의례 위엄" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">시안 3 — 의례·위엄</figcaption>
  </figure>
</div>

> v2를 기반으로 하되 전체적으로 뒤쪽에서 강한 빛이 들어오도록 얼굴의 묘사도 의상에 맞춰 회화적으로 조금더 등신대를 길게, 위엄 있는 신적인 프로포션으로 의상이 뒤에서 비치는 빛 때문에 빛이 나고 의상과 비슷한 비치는 베알로 얼굴을 가리고 있게.

세 안은 정적·각성·위엄을 각각 잘 보였지만, 가장 *이야기를 품은* 안은 반측·각성이었다. 얼굴이 비스듬히 돌아가고 가슴 가운데에서 호박색 빛이 새어 나오는 구도가 한 컷에 *깨어남*의 서사를 담는다. 다음 라운드는 이 v2를 베이스로 두고 역광·신적 프로포션·얼굴 가림을 더 강하게 얹는다.

## 2단계 · 역광과 위엄 (회귀 라운드)

뒤쪽에서 들어오는 강한 역광, 막을 통과한 backlight, 의상과 같은 결의 베일로 얼굴 가림, 8~9등신의 신적 프로포션을 한 번에 얹었다. 같은 프롬프트로 stochastic 3장.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r2/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r2/v1.png" alt="r2 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r2 v1</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r2/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r2/v2.png" alt="r2 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r2 v2</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r2/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r2/v3.png" alt="r2 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r2 v3</figcaption>
  </figure>
</div>

> 엥? 이전 v2는 반측면이었잖아. 포즈가 너무 달라졌는데? 이번 시도처럼 광원과 베알, 위엄을 추가해서 조정하되 다시 시안 3개. 의상을 훨씬 넓게 퍼지도록

이 라운드는 *회귀(regression)*였다. 역광·얼굴 베일·신적 프로포션은 모두 들어왔지만, 정본인 *반측 각성 포즈*가 사라졌다 — 세 안 모두 정면 정적으로 굳어 있었다. 보정 축을 얹으면서 기존 포즈가 휘발된 것. 다음 라운드는 잃어버린 포즈를 *PRESERVE* 블록으로 명시적으로 못 박고, 의상의 좌우 펼침도 함께 보강한다.

## 3단계 · 포즈 회복과 의상 확장

프롬프트 상단에 **PRESERVE 블록**을 두어 반측 각성 포즈, 베일을 가른 손, 호박색 inner glow를 모두 명시적으로 보존하라고 지시했다. 의상의 좌우 펼침은 *몸 너비의 2.5~3배 wingspan*으로 수치화. r2의 보정 축은 그대로 유지.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r3/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r3/v1.png" alt="r3 v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">r3 v1 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r3/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r3/v2.png" alt="r3 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r3 v2</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r3/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-veil-r3/v3.png" alt="r3 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r3 v3</figcaption>
  </figure>
</div>

> v1의 구도 포즈 구성 의상 등을 유지하면서 황금색 색감과 sss로 투과되는 느낌을 살려서 고품질로 업스케일하자. 나비 날개 같은 문양을 금박으로 조금 더 강조하고 고개를 살짝 들게

PRESERVE 블록의 효과는 즉각이었다. v1은 반측 포즈, 베일을 가른 손, 호박색 inner glow가 모두 살아 있고, 의상이 좌우로 완전히 펼쳐진 나방 날개 형상이 잡혔다. v2는 세로 비율로 신적 프로포션은 잘 잡혔지만 좌우 펼침이 약했고, v3는 둘의 중간이지만 반측 포즈가 다시 흐려졌다. v1을 채택. 다음 라운드는 이 v1을 *직접 input*으로 두고 황금색·SSS·금박·고개 살짝 듦의 스타일 보정만 얹는 마스터 패스.

## 4단계 · 황금색 SSS 마스터

v1을 input으로 직접 넣고, 프롬프트는 *PRESERVE 블록 + ADJUSTMENT 블록*으로 명확히 나눴다. 구도·포즈·의상은 절대 건드리지 말 것, 그리고 다섯 가지(턱·색감·SSS·금박·디테일)만 얹을 것. 사이즈는 2048×2048, quality high.

<div style="display:flex;gap:12px;margin:20px 0;justify-content:center;">
  <figure style="max-width:520px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-moth-veil/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-moth-veil/cover.png" alt="마스터" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">마스터 — 황금색 SSS 통과 + 금박 eyespot ← 정본</figcaption>
  </figure>
</div>

> 이게 뭔진 나도 모르겠지만 일단 제작가를 발행하자 ㅋㅋㅋㅋㅋㅋㅋ

전체 톤이 honey-gold·앰버로 깔끔하게 이동했고, 베일 안쪽으로 빛이 스며드는 SSS의 결이 진하게 살아났다. eyespot 가장자리는 illuminated manuscript처럼 반짝이고, 다리 사이로 떨어지는 베일 안쪽까지 빛이 새어 나오면서 *깨어남이 몸 전체로 번지는* 인상이 더해졌다. 턱은 미묘하게 들렸지만 r3 v1과 비교하면 시선이 조금 위로 향한다. 한 가지 트레이드오프 — 얼굴 베일이 r3 v1보다 옅어져 이목구비가 더 또렷이 드러난다. *베일 너머의 신비*는 살짝 약해졌지만, 대신 *친근한 신성*이 들어왔다.

## 가장 흥미로운 지점

- **포즈는 보정을 얹는 순간 휘발된다.** r2 라운드의 회귀가 이를 증명했다 — "역광·얼굴 베일·신적 프로포션"을 얹는 지시만으로 *반측 각성*이라는 정본 포즈가 사라졌다. 라운드를 넘기며 보정 축을 더할 때는 보존해야 할 요소를 PRESERVE 블록으로 *상단에* 명시적으로 못 박아야 한다. 자연어 문장 안쪽에 녹여 두면 모델이 우선순위를 잃는다.
- **단일 광학 컨셉이 스타일 보정을 흡수한다.** 황금색·SSS·금박은 서로 다른 미학 처리지만 위화감 없이 합쳐졌다 — 베이스가 처음부터 *막을 통과한 빛*이라는 단일한 광학 컨셉으로 짜여 있었기 때문. 컨셉이 단단하면 후속 스타일 보정의 폭도 넓어진다.
- **input의 절대경로 패스가 정본 흐름을 단순하게 만든다.** r3 v1을 inputs 디렉토리에 복사하지 않고 `.local/tmp/` 절대경로로 직접 넘겨 마스터를 굴렸다. 라운드 산출물을 다음 라운드의 input으로 직접 연결할 수 있다는 건 making-of 흐름의 본질적인 단순화다.
- **얼굴 베일의 옅고 진함은 *친근함과 신비*의 트레이드오프다.** r3 v1과 마스터를 비교하면 같은 인물·같은 베일이지만 베일의 두께에 따라 캐릭터의 무게가 달라진다. 다음 카드에 비슷한 컨셉이 나오면 *얼굴 베일 두께*를 명시적인 보정 축으로 들어 올리는 게 좋겠다.

## 출처

자체 설계. 외부 레퍼런스 이미지 한 장(주복 김 제공)을 베이스 프롬프트로 풀고, 서소영 시드를 입혀 4 라운드(컨셉 → 역광 회귀 → 포즈 회복 → 황금색 마스터)에 걸쳐 다듬었다.

## 메모

- 시드: `서소영 (실사, 포트레이트).png` (1·2·3 라운드), r3 v1 (마스터 라운드 input)
- R2 prefix:
  - `gallery/seosoyoung-veil-still/cover.png` · `seosoyoung-veil-awaken/cover.png` · `seosoyoung-veil-rite/cover.png` (1단계)
  - `gallery/seosoyoung-veil-r2/v{1..3}.png` (2단계)
  - `gallery/seosoyoung-veil-r3/v{1..3}.png` (3단계)
  - `gallery/seosoyoung-moth-veil/cover.png` (마스터 정본)
- 1단계 .md 3개(`seosoyoung-veil-still/awaken/rite.md`)는 draft 상태로 리포에 보존. 시안 라운드의 R2 객체는 본문 figure 그리드 참조용으로 *삭제 금지*.
- 헤어스타일 지정 제거 / 시드 기준 일반화 (`long jet-black hair tied back` 류 제거, "keep her hairstyle as in the seed reference"로 일반화).
- 보정 프롬프트의 정본 구조: 상단 PRESERVE 블록 + 하단 ADJUSTMENT 블록. r2의 회귀를 r3에서 회복시킨 키.
- 마스터 cover의 `cover.focus: "50% 18%"` — 정사각 그리드에서 얼굴 위치를 위쪽으로 끌어올려 잘리지 않도록.
