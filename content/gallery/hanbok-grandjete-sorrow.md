---
title: ""
date: 2026-05-13T22:35:00+09:00
slug: "hanbok-grandjete-sorrow"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/hanbok-grandjete-sorrow/cover.png"
  hiddenInList: false
  focus: "center center"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. 흰 배경, 흑백, 핫셀블라드 결의 오뜨 쿠튀르 한복 그랑쥬떼. 검정 시폰 다층 치마, 검정 토슈즈, 깊은 비애의 표정. 발 아래 ∩자 반원으로 깔린 초크 가루.
2. 첫 시안 → 포즈 마네킹 추출 → 의상·표정 변주 → 도약점 보정 → 반원 궤적의 물리 → 가루 질감 보정 → 손가이드 시드 채택 → 2048×2048 high 정본 업스케일. 단계마다 시안 3종을 1024 / low로 후보 스캔.
3. 결정적인 한 번의 *수동 개입*이 있었다. 5단계에서 모델이 ∩자 반원을 *페인트로 그린 무지개 스트라이프*로 풀어내는 바람에, 사용자가 직접 손으로 가이드를 그려 가져오셨다. 그 손그림이 6단계 시드가 되어 비로소 가루 결이 살아났다.

## 의도와 시드

처음 떠올린 결은 한 문장이었다.

> 오뜨 쿠튀르 패션 사진. 한국인 소녀가 한복을 입고 그랑쥬떼를 하는 포즈. 옆모습. 극사실적인 흑백 사진. 흰색 배경. 점프 궤적을 따르는 초크 먼지. 드라마틱한 역광. 림 라이트. 핫셀블라드. f22.

시드는 갤러리 정본 `서소영 (실사).png`. 실사 톤이 필요한 전신·환경 포함 컷용으로, 그랑쥬떼처럼 신체가 전부 드러나는 구도에 가장 잘 맞았다.

## 1단계 · 첫 시안 — 한복 그랑쥬떼

세 가지 결로 시안을 굴렸다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-20260513-1245/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-20260513-1245/v1.png" alt="round1 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 클래식 실루엣</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-20260513-1245/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-20260513-1245/v2.png" alt="round1 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 디컨스트럭티드 쿠튀르</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-20260513-1245/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-20260513-1245/v3.png" alt="round1 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 미니멀 그래픽</figcaption>
  </figure>
</div>

세 장 모두 옆모습 그랑쥬떼와 흑백 핫셀블라드의 결은 잡혔다. 그러나 *어느 결로 가야 할지*를 정하려면, 자세 자체를 먼저 다시 짚어야 했다. 양팔이 V자로 벌어진 흔한 발레 포즈는 익숙하지만, 본 작업의 정조가 맞는지는 아직 미정.

## 2단계 · 포즈 마네킹 추출

다음 시안 전에 자세의 *어휘*를 시각화하기로 했다. 두 장의 실제 발레 사진에서 의상·배경을 걷어내고 마네킹 라인 아트로 옮긴다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/pose-extract-20260513-1251/pose1-mannequin.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/pose-extract-20260513-1251/pose1-mannequin.png" alt="mannequin pose 1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">A. 양팔 V자 — 들뜬 도약</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/pose-extract-20260513-1251/pose2-mannequin.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/pose-extract-20260513-1251/pose2-mannequin.png" alt="mannequin pose 2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">B. 한 팔 위 · 한 팔 옆 — 로맨틱 발레 ← 선택</figcaption>
  </figure>
</div>

B 자세가 정조와 맞았다. 앞팔이 머리 위로 곡선을 그리고, 뒷팔은 옆으로 거의 수평. 신체가 비스듬히 열리며 *카메라를 향해 가슴을 내어주는* 결. 비통한 헤로인의 자세는 양팔로 환호하는 것이 아니라 한 팔은 하늘로, 다른 한 팔은 옆으로 열리는 결이다.

## 3단계 · 비애의 그랑쥬떼 — 의상·표정 변주

마네킹 B 자세로 다시 시안을 굴렸다. 검정 시폰 다층 치마, 검정 토슈즈, 깊은 비애의 표정으로.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v2-20260513-1300/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v2-20260513-1300/v1.png" alt="round2 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 클래식 헤로인</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v2-20260513-1300/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v2-20260513-1300/v2.png" alt="round2 v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v2. 폭발하는 베일 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v2-20260513-1300/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v2-20260513-1300/v3.png" alt="round2 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 그래픽 비통</figcaption>
  </figure>
</div>

강한 역광과 시폰의 다층 구조가 치맛자락을 어둡게 새기며, 비애의 결이 의상에 옮겨갔다. 단, 다음 두 가지가 어색했다.

- **운동 방향**: 옆모습이 좌측을 향하니 우 → 좌로 움직여야 하는데, 시안에서는 초크가 좌측 도약점에서 솟았다. 운동 방향이 거꾸로다.
- **궤적의 물리**: 초크 먼지가 인물 머리 위로 호를 그리며 떠 있다. 도약 후 공중에서는 새 먼지가 생기지 않는다.

두 가지 모두 *물리적으로 그럴듯하지 않은 그림*이라는 신호.

## 4단계 · 도약점 보정 — 우하단으로

운동 방향을 옳게 잡았다. 도약점을 우하단으로 옮기고, 고개를 더 들어 비애를 깊게 하고, 초크를 더 풍성하게.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v3-20260513-1307/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v3-20260513-1307/v1.png" alt="round3 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 후방 분사</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v3-20260513-1307/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v3-20260513-1307/v2.png" alt="round3 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 좌우 균형</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v3-20260513-1307/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v3-20260513-1307/v3.png" alt="round3 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 정석</figcaption>
  </figure>
</div>

도약점이 옳은 자리로 옮겨갔고, 운동 방향이 자연스러워졌다. 하지만 여전히 *공중에 떠 있는 초크 호*가 남아 있었다. 모델은 "trajectory를 따라"라는 지시를 머리 위 아치로 풀어내곤 한다 — 도약 후의 공기는 가만하다는 사실을 다시 명시해야 했다.

## 5단계 · 반원 궤적의 물리 — *실패*

세 줄로 압축한 새 지시문:

> 초크 먼지는 발 아래 ∩자 반원 1개로 한정한다. 양 끝점은 바닥에 자리잡는다 — 우하단(도약점), 좌하단(착지점). 호의 정점은 발끝 높이. 머리·팔 위는 깨끗한 흰 배경.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v4-20260513-1314/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v4-20260513-1314/v1.png" alt="round4 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 타이트한 호</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v4-20260513-1314/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v4-20260513-1314/v2.png" alt="round4 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 정대칭</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v4-20260513-1314/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v4-20260513-1314/v3.png" alt="round4 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 너른 호</figcaption>
  </figure>
</div>

이 단계는 *완전한 실패*였다.

기하학만 보면 옳다. 호가 발 아래에 자리잡고, 양 끝이 바닥에 닿고, 머리 위는 깨끗이 비었다. 그런데 결과물을 보면 — 호가 무대 위에 흰 페인트로 칠한 무지개 스트라이프처럼 보인다. *초크 가루를 사진으로 찍은 그림*이 아니라 *호의 윤곽선을 그래픽으로 그린 그림*이 되어 버렸다.

"자연스럽게", "가루 질감으로"라고 적어 넣어 봐도 모델은 이미 호의 *모양*을 기억해서 같은 페인트 스트로크 결로 다시 그린다. 텍스트 지시만으로는 이 결을 깰 수 없었다.

## 6단계 · 사용자 손그림 수정 적용

그래서 사용자께서 직접 손으로 가이드를 잡아 가져오셨다. 5단계의 무지개 스트라이프를 지우고, 우하단에서 솟아 좌측으로 흩어지는 *진짜 가루 사진의 결*을 손으로 그려 넣으신 시드.

<div style="margin:20px 0;text-align:center;">
  <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/hanbok-grandjete-sorrow/chatgpt-share-grace-leap.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/hanbok-grandjete-sorrow/chatgpt-share-grace-leap.png" alt="user-guided seed" style="max-width:420px;width:100%;height:auto;display:inline-block;border-radius:6px;"></a>
  <div style="font-size:13px;color:#86868b;margin-top:6px;">사용자가 직접 손으로 수정 — 무지개 스트라이프를 지우고 진짜 가루 결을 그려 넣은 시드</div>
</div>

이 손그림 시드를 가져다 다시 모델에 넘긴다. 지시는 단 하나 — *나머지는 다 유지하면서 초크가 더 자연스럽게 퍼지고 가루 질감이 살아나게.*

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v5-20260513-1352/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v5-20260513-1352/v1.png" alt="round5 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 너른 안개</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v5-20260513-1352/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v5-20260513-1352/v2.png" alt="round5 v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v2. 정석 ← 선택 (정본)</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v5-20260513-1352/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/sketches/hanbok-grandjete-v5-20260513-1352/v3.png" alt="round5 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 거센 폭발</figcaption>
  </figure>
</div>

페인트 스트로크가 사라지고, 미립자가 빛 결 속에서 또렷이 살아났다. v2를 정본으로 둔다.

## 7단계 · 정식 업스케일

v2를 시드로, 같은 지시를 그대로 유지하여 2048×2048 / `quality=high`로 정본을 다시 굽는다. 약 4분 걸린다.

가루 디테일이 풀해상도에서 비로소 제 결로 펼쳐졌다. 한 장의 사진이 — 한 명의 무용수가 검은 시폰을 입고 공중에 떠 있고, 발 아래로 한숨 같은 가루가 호를 그리며 머무는 — 자리잡혔다.

## 프롬프트 (정본 업스케일)

```
Avant-garde haute couture editorial fashion photograph. Hyper-realistic monochrome black and white, very high tonal contrast, pure white seamless cyclorama background, fine analog film grain. Gallery print quality, ultra-sharp focus head to toe.

Use the reference image as the AUTHORITATIVE base — preserve EVERYTHING in it exactly: the subject's face and identity, the side profile facing camera-left, the 180° split grand-jeté pose at the apex, the front arm raised overhead in a soft curve, the back arm extended out near-horizontal, the chin lifted upward with throat exposed, the deep dignified sorrow on her face, the layered translucent black hanbok chima trailing behind motion, the structured jeogori with streaming goreum ribbon, the black satin pointe shoes with ankle ribbons, the white seamless backdrop, the single hard backlight, the intense rim light tracing every contour, the deep contrasty shadows on the camera-facing side, the takeoff point at bottom-right of the frame, the imagined landing point at bottom-left, the overall composition.

CHALK DUST — render with the most natural dispersion and most visible powder grain texture. Keep the ∩-shape geometry of the reference intact:
- The arc is anchored to the FLOOR at the bottom-right (takeoff bloom) and bottom-left (landing bloom).
- The peak of the arc reaches her feet level. NO chalk dust above her body — the upper half of the frame above her head, hands, arms, and shoulders must remain CLEAN WHITE empty cyclorama.
- The dust reads as a real volumetric cloud of suspended chalk powder, not as a painted stroke. Render countless individual particles at varied scales — fine micro-motes, mid-size grains, sparse drifting clumps — caught and glowing in the backlight like luminous pinpricks.
- Density gradients along the curve are ORGANIC AND IRREGULAR: thicker powdery blooms at both floor anchors, thinner feathered drifts along the arc, soft sub-currents and curling tendrils where local air carries the powder.
- A few stray particles may scatter naturally outside the main arc where physics would carry them, but the overall ∩ shape stays clearly readable.
- The texture should photograph like an extreme high-shutter studio capture of real chalk powder thrown into a backlit beam — alive with tiny dots and atmospheric haze.

Camera: Hasselblad H6D medium format, 100mm lens, f/22, deep depth of field, tack-sharp from face to feet. No text, no logos. Vogue Italia editorial mood.
```

## 메모

- 결정적 보정은 두 번의 *구조 보정*과 한 번의 *수동 개입*. 구조 보정은 도약점 좌→우 이동(3→4단계)과 반원 호를 발 아래로 한정(4→5단계). 수동 개입은 사용자께서 직접 손그림으로 가루 결을 그려 넣으신 5→6단계.
- 5단계는 *텍스트 지시의 한계*를 또렷이 보여줬다. "자연스러운 가루로", "페인트 스트로크처럼 보이지 않게"라고 아무리 적어도, 모델은 4단계에서 이미 학습한 호의 모양을 기억하고 같은 결로 다시 그렸다. 텍스트가 닿지 못하는 결은 결국 손그림으로 갈아끼우는 수밖에 없었다.
- 마네킹 추출도 같은 원리. *그림으로* 자세 어휘를 옮기는 우회로였고, 텍스트로 "두 팔을 V자로"라고만 적었으면 2단계까지 가지 못한다. 텍스트의 한계가 보이면 즉시 시각 가이드로 갈아탄다 — 이번 작업의 가장 큰 교훈이다.
- 단계마다 시안 3종을 1024×1024 / `low`로 가볍게 굴렸다. 채택 결정이 난 뒤에만 2048×2048 / `high`로 4분짜리 업스케일을 굽는다.
- 시드의 헤어스타일은 `서소영 (실사).png`를 그대로 따른다 — 검은 머리, 묶지 않은 단정한 결. 프롬프트에 헤어 지시를 별도로 넣지 않았다.
- 의상은 *전통 한복의 색조(밝은 톤)*가 아니라 *비애를 입은 검정 시폰 한복*으로 자리잡혔다. 강한 역광과 다층 시폰이 만들어내는 어두운 사선의 결을 정조로 받아들였다.
