---
title: ""
date: 2026-05-15T17:20:00+09:00
slug: "painted-self-meets-real-self"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self/cover.png"
  hiddenInList: false
  focus: "50% 30%"
source: "자체 설계 — 사용자 협업"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. *일러스트 서소영*과 *실사 서소영*을 마주 세워 서로를 보고 놀라는 한 컷을 만든 카드. 두 인물의 옆모습 시안을 따로 굽고, 한 호출에서 두 입력으로 합성한 뒤, 거리·배경을 다듬고, 눈높이 정렬에 한 번 실패한 다음, 정본을 high로 업스케일한 5+1라운드 작업.
2. *거울 프롬프트가 컴포지션의 절반을 미리 결정한다*. 일러스트는 우측 응시, 실사는 좌측 응시로 1·2단계에서 미리 짝을 맞춰 두자, 3단계의 합성에서 모델이 두 인물의 시선을 의외로 정확히 마주쳐 줬다. 합성은 두 인물의 *방향이 이미 정해진* 상태에서만 자연스럽다.
3. *image-to-image의 정밀 위치 시프트는 약점이다*. 5단계에서 왼쪽 인물만 수직으로 내려 키와 눈높이를 맞추려 했지만, 모델은 시프트 강도를 정확히 따르지 못하고 표정·시선까지 흐트러뜨렸다. 픽셀 단위 위치 조정은 image-to-image가 아니라 PIL 합성의 영역이다.

## 의도와 시드

*일러스트 서소영과 실사 서소영이 서로를 보고 놀라는 한 컷*을 만들고 싶었다. 시드는 두 장.

- `서소영 (포트레이트).png` — 일러스트 톤
- `서소영 (실사, 포트레이트).png` — 실사 톤

핵심 컨셉은 단순하다. *그림 속의 나*와 *현실의 나*가 마주쳤다. 두 사람이 서로를 보고 놀란다. 정사각형 한 컷.

이 한 줄을 만들기 위해 두 인물의 *시선 방향*을 미리 짝지어 굽는 것이 시작점이었다 — 일러스트는 우측을 보고, 실사는 좌측을 보도록. 합성은 그 다음.

## 1단계 · 일러스트 서소영, 우측 응시 놀람

`서소영 (포트레이트).png`를 시드로 image-to-image. 반측면, 좌측 배치, 시선 우측, 놀란 표정. 표정의 강도와 손동작 유무로 세 결을 굴렸다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r1/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r1/v1.png" alt="round 1 v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1. 차분한 놀람, 시선이 자연스러움 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r1/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r1/v2.png" alt="round 1 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 손을 입가로 가져간 강한 놀람</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r1/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r1/v3.png" alt="round 1 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 클로즈업, 표정만으로 놀람</figcaption>
  </figure>
</div>

V1을 골랐다. 합성 시 카운터파트의 강도와 균형을 맞추려면 *너무 강하지 않은 절제된 놀람*이 안전하다고 봤다.

## 2단계 · 실사 서소영, 좌측 응시 놀람

`서소영 (실사, 포트레이트).png`를 시드로 동일한 방향성을 *거울로* 굽는다. 반측면, 우측 배치, 시선 좌측. 합성 시 일러스트와 정확히 마주 보도록 미리 짝을 맞춰 두는 단계.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r2/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r2/v1.png" alt="round 2 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 차분한 놀람</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r2/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r2/v2.png" alt="round 2 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 손동작 있는 강한 놀람</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r2/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r2/v3.png" alt="round 2 v3" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v3. 클로즈업 고정 시선 ← 선택</figcaption>
  </figure>
</div>

V3가 가장 시선이 단단하게 잡혔다. 일러스트 V1의 *조용한 놀람*과 짝지어 합성 단계에서 *서로 정면으로 시선이 부딪히는* 결을 만들 수 있을 거라 봤다.

## 3단계 · 첫 합성 — 한 호출, 두 입력

핵심 라운드. *한 번의 image-to-image 호출에 두 시안을 동시에 입력*으로 넣고, 두 인물이 마주 보는 한 컷을 합성하도록 지시했다. 시선 매칭이 가장 까다로울 거라 예상해 세 가지 다른 구도 전략을 굴렸다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r3/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r3/v1.png" alt="round 3 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 평행 스플릿, 정중앙 여백</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r3/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r3/v2.png" alt="round 3 v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v2. 클로즈 인카운터 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r3/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r3/v3.png" alt="round 3 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 액자 메타 — 그림 속의 나</figcaption>
  </figure>
</div>

> v2가 좋은데, 둘 사이에 살짝 공간을 띄우고, 배경이 동일한 흰색이 되도록 하자.

세 안 모두 시선이 의외로 잘 마주쳤다. *거울 프롬프트로 1·2단계에서 방향을 미리 잡아둔* 효과였다. V2는 두 사람이 거의 닿을 듯 가깝고 시선의 충돌감이 가장 강했지만, 두 가지 보정이 필요했다 — 거리, 그리고 가운데 톤이 갈라진 배경.

## 4단계 · 거리·배경 다듬기 — V2 보존, 두 축만 변경

3단계 V2를 시드로 잡고 *시선·표정·자세는 그대로 유지*, 거리와 배경 두 축만 변경. 거리감을 세 단계로 굴렸다. 보존 항목을 한 줄씩 *identical*로 명시했다 (peony의 교훈).

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r4/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r4/v1.png" alt="round 4 v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1. 중간 거리, 호흡 균형 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r4/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r4/v2.png" alt="round 4 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 가까운 거리, 충돌감 강함</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r4/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r4/v3.png" alt="round 4 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 넉넉한 거리, 카피 여지</figcaption>
  </figure>
</div>

V1이 호흡과 긴장의 균형이 가장 좋았다. 가운데 톤 분할도 사라지고 단일 오프화이트 배경이 깔끔하게 잡혔다. 표정·시선은 V2 원본 그대로.

## 5단계 · 눈높이 정렬 시도 — 패착, 회귀

> 왼쪽 일러스트 서소영을 약간 아래로 이동해서 둘의 키와 시선을 맞추는 걸 시안 3개로 생성해보자. 다른 건 전부 그대로 유지하면서.

4단계 V1을 시드로 잡고 *오른쪽 실사는 그대로, 왼쪽 일러스트만 수직으로 시프트*하도록 시도. 시프트 강도를 약·중·강 세 단계로 굴렸다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r5/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r5/v1.png" alt="round 5 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 약한 시프트 — 변동 거의 없음</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r5/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r5/v2.png" alt="round 5 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 중간 의도 — V1과 유사</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r5/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/painted-self-meets-real-self-r5/v3.png" alt="round 5 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 강한 시프트 — 시선·표정 흐트러짐</figcaption>
  </figure>
</div>

> 으악… 너무 어긋났는데?

회귀였다. 모델은 시프트 강도를 정확히 따르지 못했고, V3에 이르러 표정과 시선까지 함께 흐트러졌다. 가장 까다로울 거라 예상한 *눈높이 정렬*이 결국 image-to-image의 약점에서 막혔다 — 픽셀 단위 위치 시프트는 *재해석*으로 흡수되어 보존 지시를 일관되게 받지 못한다. 이 라운드를 접고 4단계 V1으로 돌아가 본 발행으로 직행했다.

## 6단계 · 2048×2048 high 정본 업스케일

4단계 V1을 시드로 `--size 2048x2048 --quality high`. 약 4분 32초, 6.3MB. 프롬프트는 *upscale-only*로만 짧게. CRITICAL 절에 *do not change anything compositional / identical eye-line·gaze·expression·distance·background*를 한 줄씩 명시하고, 변경 허용 범위는 *eyes·lashes 디테일, 일러스트 측 브러시 텍스처, 실사 측 피부·옷감 텍스처, 비드 액세서리 하이라이트*만으로 좁혔다.

본 카드의 커버는 펜화의 가는 선과 사진의 미세 결이 한 캔버스에서 깨끗하게 공존하는 컷으로 떨어졌다. 두 인물은 같은 시선 라인 위에서 서로를 보고 놀라 있다.

## 가장 흥미로운 지점

**거울 프롬프트가 컴포지션의 절반을 미리 결정한다.** 1·2단계에서 *일러스트는 우측 응시 / 실사는 좌측 응시*로 짝을 맞춰 굽지 않았다면, 3단계의 합성에서 두 인물의 시선이 이렇게 자연스럽게 마주치지 않았을 것이다. 합성은 두 인물의 *방향이 이미 정해진* 입력에서만 안전하다 — 한 호출 안에서 모델이 시선 방향까지 새로 결정하도록 두면 결과는 흩어진다. 마주 보는 한 컷의 절반은 두 입력을 굽기 *전에* 만들어진다.

**multi-input image-to-image의 시선 매칭은 의외로 강하다.** 두 인물을 따로 굽고 PIL로 합치면 정확하지만 부자연스럽다 — 빛, 그림자, 배경 톤이 어긋난다. 한 호출에 두 입력을 넣으면 모델이 두 사람을 *같은 캔버스*로 인식해 시선·눈높이·조명을 함께 맞춰준다. 정밀도는 떨어지지만 *자연스러움*은 단연 우월하다. 이 카드는 그 트레이드오프를 자연스러움 쪽으로 끝까지 가져갔다.

**image-to-image의 정밀 위치 시프트는 약점이다.** 5단계에서 *왼쪽만 N% 내려라*는 지시가 통하지 않았다. 모델은 위치 시프트를 *공간 변환*이 아니라 *재렌더 힌트*로 흡수한다. 그래서 약한 시프트는 거의 변화가 없고, 강한 시프트는 표정·시선까지 함께 흔들린다. 픽셀 단위 위치 조정은 image-to-image가 아니라 PIL 매트 컴포지팅의 영역이다 — 다음 같은 작업이 있다면 이 단계는 바로 PIL로 넘긴다.

**보존 지시는 KEEP UNCHANGED를 한 줄씩 *identical*로 명시.** 4단계와 6단계에서 효과를 봤다. *"표정 유지하면서 거리만 바꿔줘"* 같은 단일 지시는 모델이 일부만 듣는다. *Both characters' faces, eyes, eyebrows, lips, expressions, gaze directions, hair, earrings, hanbok, posture, head tilt, shoulder framing — all identical to the input* 처럼 한 줄씩 명사로 나열하고, ONLY CHANGE는 한두 항목으로 좁혀야 모델의 재해석 충동이 눌린다. peony 카드의 교훈이 이 카드에서도 그대로 통했다.

## 출처

자체 설계 — 사용자 협업.

## 메모

- 시드: `.claude/skills/gallery-post/inputs/서소영 (포트레이트).png` + `.claude/skills/gallery-post/inputs/서소영 (실사, 포트레이트).png`
- 모든 라운드 시안의 R2 키는 slug별로 분리 보존(`gallery/painted-self-meets-real-self-r{1..5}/v{1..3}.png`). 패착 라운드인 5단계 시안도 본문 비교를 위해 그대로 유지.
- 정본 cover는 2048×2048 high (6.3MB, 272초). 시안 단계는 모두 1024×1024 low로 진행.
- 합성 전용 입력은 1단계 V1과 2단계 V3. 다른 V를 입력으로 잡았다면 시선·구도가 다르게 나왔을 가능성이 크다 — 거울 입력의 *어떤 V를 고를지*가 합성의 결을 사실상 결정한다.
