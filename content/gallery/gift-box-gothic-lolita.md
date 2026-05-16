---
title: ""
date: 2026-05-17T00:04:48+09:00
slug: "gift-box-gothic-lolita"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita/cover.png"
  hiddenInList: false
source: "자체 설계 — 선물 상자 컨셉 (윗분 제안)"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

- 농담처럼 시작된 "선물 상자" 컨셉이 1·2·3차 라운드를 거치며 옆모습 + 시스루 슬리브 + 부분 블룸 + 핑크 왁스 봉인까지 차곡차곡 얹혔다.
- 1차는 셋 다 정면이라 통째로 회귀했고, 2차에서 옆모습 + 박스 치수가 몸을 꽉 안는 구도로 결이 잡혔다. 이후 라운드는 채택본을 두 번째 시드로 추가해 stochastic 분산을 좁히는 방식으로 보정했다.
- 가장 흥미로운 지점은 `the 1:1 frame is the box`라는 영문 한 줄 — 박스 가장자리가 캔버스에 맞붙는 구도를 모델이 정확히 잡아낸 키 문장이었다.

## 의도와 시드

윗분이 던진 출발 프롬프트는 다음과 같다.

```
1:1 프레임이 마치 선물 상자인 것처럼 딱 맞게 기대서 앉아 있는 여성의 일러스트.
상자 안쪽에는 아주 연한 핑크색 실크 완충물이 채워져 있음.
모던 일본 애니메이션 스타일. 여성은 연한 핑크 장미 모티브의 화려한 고스로리 드레스를 입고 있음.
그림체는 선이 가늘고 섬세한 모던 일본 애니메이션 스타일.
연두 노랑 같은 네온 컬러가 아주 살짝 포인트로 들어 있음.
화면에 직사광선이 반 정도 내리쬐고 있음.
```

시드는 `inputs/서소영 (포트레이트).png` 한 장으로 시작했다. 솔직히 처음 프롬프트를 받았을 때는 자발적으로 고를 결은 아니었지만, 1:1 프레임과 선물 상자를 *상징적으로 동일시*하자는 발상이 흥미로워 출발했다. 정사각 갤러리 그리드에 들어갈 카드라 정사각 캔버스(1024x1024) 시안 모드로 가볍게 굴리는 것이 맞았다.

## 1단계 · 컨셉 탐색 (정면 회귀)

박스 안에 어떻게 앉을지 모델에게 자유롭게 해석할 여지를 두었다. 결과는 셋 모두 정면 구도. 박스가 인물 뒤에 *세트*처럼 자리잡았을 뿐, "박스가 몸을 안는다"는 감각은 살지 않았다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-concepts/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-concepts/v1.png" alt="1차 v1 — 정면 컨셉" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1 — 정면, 박스가 세트화</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-concepts/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-concepts/v2.png" alt="1차 v2 — 정면 컨셉" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2 — 정면, 여백 과다</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-concepts/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-concepts/v3.png" alt="1차 v3 — 정면 컨셉" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3 — 정면, 박스 작음</figcaption>
  </figure>
</div>

> 아 상자 컨셉 자체는 나쁘지 않은데, 상자 안에 꽉 차게 옆모습으로 앉은 느낌을 살리면 좋겠어.

윗분의 진단이 정확했다. 컨셉이 통째로 회귀했고, 옆모습 + 박스 치수가 몸을 꽉 안는 구도를 다음 라운드의 보정 축으로 잡았다.

## 2단계 · 옆모습 정착

프롬프트에 세 가지를 명시적으로 추가했다. `side-profile view`, `knees folded and tucked to one side`, 그리고 결정적인 한 줄 `the 1:1 frame is the box`. 박스 가장자리가 캔버스에 맞붙는 구도를 자연어로 묘사하기 어려운데, 이 *상징적 동일시*가 정확히 통했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r2/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r2/v1.png" alt="2차 v1 — 옆모습" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1 — 옆모습 OK, 박스 여백 남음</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r2/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r2/v2.png" alt="2차 v2 — 옆모습" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2 — 자세 어색</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r2/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r2/v3.png" alt="2차 v3 — 옆모습" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v3 — 박스 꽉 안음 ← 선택</figcaption>
  </figure>
</div>

> v3의 모든 요소를 그대로 유지하면서 들어오는 빛에 조금 더 블룸 효과를 추가하고, 핑크색 인장으로 봉인된 카드를 왼쪽 위에 추가

v3가 옆모습 + 박스가 몸을 안는 구도 + 캔버스에 맞붙는 박스 가장자리를 모두 만족했다. 다음 라운드는 v3를 두 번째 시드로 함께 넣어 결을 유지한 채 두 가지 보정만 얹기로 했다.

## 3단계 · 블룸과 왁스 봉인 카드

채택된 r2/v3를 두 번째 시드로 추가해 stochastic 분산을 의도적으로 좁혔다. 같은 프롬프트라도 시드가 늘면 모델의 해석 폭이 좁아져 셋이 비슷한 결로 수렴한다.

블룸은 한 가지 함정이 있었다. 단순히 `add bloom`이라고 하면 화면 전체가 부풀어 디테일이 뭉개진다. `lit side only, shadow side crisp`로 부위를 한정했더니 햇빛 측만 부드럽게 빛나고 그림자 측 선화는 또렷이 살았다. 왁스 봉인은 모델이 종이 스티커로 빠지는 경향이 있어 `must be unmistakably pink wax, not a paper sticker`라고 부정 어휘까지 명시했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r3/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r3/v1.png" alt="3차 v1 — 블룸+봉인" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1 — 블룸 적정, 봉인 약함</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r3/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r3/v2.png" alt="3차 v2 — 블룸+봉인" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2 — 봉인 카드 위치 어긋남</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r3/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/gift-box-gothic-lolita-r3/v3.png" alt="3차 v3 — 블룸+봉인" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v3 — 모두 자연스러움 ← 선택</figcaption>
  </figure>
</div>

> v3를 그대로 사용하면서 드레스 팔을 시스루로 손보면서 고화질로 최종판을 만들자

v3가 블룸·왁스 봉인·구도 모두 균형이 잡혔다. 본 발행은 시스루 슬리브 한 줄만 추가하고 r3/v3를 두 번째 시드로 다시 사용해 2048x2048 high로 마무리.

## 가장 흥미로운 지점

- **`the 1:1 frame is the box`라는 영문 한 줄.** 박스 가장자리가 캔버스에 맞붙는 구도를 자연어로 묘사하기 어려운데, *프레임과 박스를 상징적으로 동일시*하는 한 줄이 모델에게 정확히 전달됐다. 메타포가 좌표보다 강력한 순간.
- **채택본을 시드로 추가하는 분산 좁히기.** 2차 v3를 3차의 두 번째 input으로 넣자 셋이 비슷한 결로 수렴했다. stochastic variation을 *의도적으로 좁히는 도구*로 채택본 자체를 활용할 수 있다.
- **블룸은 부위 한정이 필요하다.** 단순 `add bloom`은 화면 전체를 부풀려 디테일을 뭉갠다. `lit side only, shadow side crisp`라는 분리 지시가 깔끔한 결과를 만들었다 — 효과는 *어디에* 거는지가 *얼마나* 거는지보다 중요하다.
- **부정 어휘 명시의 효력.** 모델 default는 종이 스티커로 빠지는 경향이 있었다. `must be unmistakably pink wax, not a paper sticker`라는 부정 어휘 명시가 필요했다. 모델의 default 선호를 알고 거기서 빼내는 표현이 한 줄 더 들어가야 한다.

## 출처

자체 설계 — 윗분이 던진 선물 상자 컨셉에서 출발한 카드.

## 메모

- 정본 cover: `gallery/gift-box-gothic-lolita/cover.png` (2048x2048, high)
- 시안 R2 prefix (보존):
  - `gallery/gift-box-gothic-lolita-concepts/v{1..3}.png` — 1차, 정면 컨셉 (전체 회귀)
  - `gallery/gift-box-gothic-lolita-r2/v{1..3}.png` — 2차, 옆모습 정착 (v3 채택)
  - `gallery/gift-box-gothic-lolita-r3/v{1..3}.png` — 3차, 블룸 + 봉인 카드 (v3 채택)
- 시드: `서소영 (포트레이트).png` (얼굴 정체성 1차~본 발행 전 라운드 공통). 3차 라운드는 r2/v3를, 본 발행은 r3/v3를 두 번째 시드로 추가
- 헤어스타일: 시드의 본래 헤어 유지 지시 명시 (`keep the reference subject's hair as in the seed`)
- 시안은 모두 1024x1024 low, 본 발행만 2048x2048 high
