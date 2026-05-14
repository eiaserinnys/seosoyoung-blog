---
title: ""
date: 2026-05-15T08:20:41+09:00
slug: "seosoyoung-peony-papercut-portrait"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-peony-papercut-portrait/cover.png"
  hiddenInList: false
source: "사용자가 직접 작성한 프롬프트"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. *섬세한 펜화 + 페이퍼 커팅 + 아르누보 + 핫셀블라드 + 하이패션*이라는 결을 가로 헤더로 굽기 시작해, 정사각 + 모란 모티브 + 여백의 미를 거쳐 헤더로 마무리한 카드. 시드는 갤러리 정본인 `서소영 (실사, 포트레이트).png` — 실사 톤 보존이 핵심이었다.
2. *구체적인 모티브명이 일반어를 이긴다*. "아르누보 풍의 꽃과 물결"이라는 일반어로 굴린 라운드는 결과가 흩어졌고, 사용자가 *모란(牡丹)*으로 좁혀 지시한 순간 구도가 또렷이 잡혔다. 시드 사용도 같은 원리 — *무엇을 가져올지*를 한 가지로 좁혀야 한다.
3. *"구도를 유지하라"는 지시는 모델이 잘 듣지 않는다*. 좌상단을 비우자고 했을 때 첫 시도는 구도를 통째로 재해석했다 — 사용자의 회귀 지시 후 "minor edit only / identical" 같은 강한 보존 지시를 영문으로 또렷이 명시하니 비로소 좌상단만 정리됐다.

## 의도와 시드

사용자가 던진 한국어 프롬프트가 출발점이었다.

```
옆모습, 도도한 표정과 당당한 미소
머리카락이 배경 요소와 자연스럽게 이어지는 느낌
상반신 클로즈업

섬세하고 입체적인 펜화와 수많은 종이가 겹쳐진 페이퍼 커팅 아트의 결합
아르누보 풍의 꽃과 물결 모티브
원경 근경 전경이 있는 입체적인 구성, 전경은 포커스 아웃
빨강 검정 흰색 키컬러
흰색 배경
현대 설치 미술 같은 구성
핫셀블라드
하이패션 컨셉
```

*서소영 실사를 이용해서 헤더 시안*이라는 요청이 결정적이었다. 일러스트가 아닌 실사 톤이 결과를 지배해야 했으므로 시드는 `서소영 (실사, 포트레이트).png`로 잡았다. 차용 범위는 얼굴·머리스타일·실사의 결.

## 1단계 · 가로 1792x1024 헤더 시안

첫 굽기. *옆모습 상반신 + 펜화·페이퍼커팅 하이브리드 + 아르누보 일반어*라는 결을 가로 헤더로. 1024 시리즈 low.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting/v1.png" alt="round 1 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 시드 톤이 가장 또렷</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting/v2.png" alt="round 1 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 모티브 분포가 평이</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting/v3.png" alt="round 1 v3" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v3. 가장 자연스러운 결 ← 선택</figcaption>
  </figure>
</div>

사용자가 v3를 베이스로 짚었다. 이후 모든 라운드는 이 v3를 기준점으로 분기·회귀한다.

## 2단계 · 정사각 + 아르누보 과감하게 (회귀)

> 인물의 표정 구도 의상 등은 유지하면서 정사각으로 이미지를 만들고, 아르누보 모티브가 화면을 과감하게 채우는 버전.

1단계 v3를 시드로 잡고 정사각으로 전환하면서 *Art Nouveau 모티브가 화면 전체를 보다 과감하게* 채우도록 굴렸다. 결과는 아쉬웠다 — *아르누보*라는 일반어로는 모티브가 흩어졌고, 머리카락-페이퍼컷 융합이 약해졌다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting-square/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting-square/v1.png" alt="round 2 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting-square/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting-square/v2.png" alt="round 2 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting-square/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-paper-cutting-square/v3.png" alt="round 2 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3</figcaption>
  </figure>
</div>

사용자의 한 마디.

> 음 좀 아쉽네. 인물의 표정 포즈 의상 구도 유지한 채로 인물의 얼굴이 부각되도록 정사각으로 크롭하면서 주변의 모란꽃 모티브를 과감하고 역동적으로 배치해보자.

진단이 또렷했다 — *아르누보*가 아니라 *모란(牡丹)*이라는 구체적 모티브명, 그리고 *얼굴 부각*이라는 face anchor 지시. 일반어를 좁히는 회귀.

## 3단계 · 모란 명시 + 얼굴 부각 + 삼중 depth

같은 1단계 v3를 시드로 다시 잡고, 모티브를 *Peony (牡丹), bold and dynamic*으로 못박았다. 얼굴을 프레임 상단~중앙에 anchor로 배치하고, 원경·중경·근경의 삼중 depth와 근경 보케를 명시했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square/v1.png" alt="round 3 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 모티브 평이</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square/v2.png" alt="round 3 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 얼굴 크롭 약함</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square/v3.png" alt="round 3 v3" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v3. 모란이 가장 또렷, 얼굴 앵커 분명 ← 선택</figcaption>
  </figure>
</div>

모란이 화면 전반을 휘감으면서도 얼굴이 또렷이 앵커로 자리 잡았다. 머리카락이 검은 페이퍼 컷으로 점진적으로 흡수되는 결도 살아났다. 사용자가 v3를 베이스로 선택했고, 다음은 좌상단 정리.

## 4단계 · 여백의 미 — 첫 시도, 구도 재해석 패착

> v3를 그대로 사용하되, 좌상단엔 여백의 미를 두는 게 좋을 것 같아.

3단계 v3를 시드로 *좌상단을 의도적으로 비우는* 시안을 굴렸다. 프롬프트에 *upper-left quadrant left intentionally empty / 여백의 미 / asymmetric weight* 같은 표현을 넣었다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-yeobaek/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-yeobaek/v1.png" alt="round 4 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 인물·모티브가 통째로 재배치</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-yeobaek/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-yeobaek/v2.png" alt="round 4 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 동일</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-yeobaek/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-yeobaek/v3.png" alt="round 4 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 동일</figcaption>
  </figure>
</div>

모델이 *좌상단 비움*을 통째로 받아들여 인물과 모란 군락을 우측·하단으로 옮기고 대각선 구도를 새로 짰다. 좌상단은 비웠지만, 사용자의 의도와는 달랐다.

> 기존 v3의 인물의 포즈 표정 의상, 그리고 무엇보다 전체 이미지의 구도는 모두 그대로 유지하되 왼쪽 상단에 바글바글한 거만 조금 비우자는 거야. 이렇게 구도를 싹 바꾸면 안 되지.

지시가 분명했다. *구도는 그대로, 좌상단의 미세 클러터만 정리*. 회귀.

## 5단계 · Minor edit — 좌상단만 정리

3단계 v3를 다시 시드로 잡고, 프롬프트를 *Minor edit only / Keep this image almost entirely as-is*로 시작했다. KEEP UNCHANGED 항목을 한 줄씩 나열하고(포즈·구도·모란 분포·머리카락 융합·색·핫셀블라드의 결 모두 *identical*), ONLY CHANGE 항목은 *upper-left corner declutter* 하나만 명시했다. *Do NOT empty the corner entirely; do NOT shift any other element*까지 못박았다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square-v3-declutter/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square-v3-declutter/v1.png" alt="round 5 v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1. 정리 강도 자연스러움 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square-v3-declutter/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square-v3-declutter/v2.png" alt="round 5 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square-v3-declutter/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/header-peony-square-v3-declutter/v3.png" alt="round 5 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3</figcaption>
  </figure>
</div>

이번엔 *구도는 거의 그대로*, 좌상단의 잔가지·미세 컷아웃만 자연스럽게 정리됐다. v1이 정리 강도가 가장 균형 있게 떨어졌다.

## 6단계 · 2048x2048 high 정본 업스케일

v1을 시드로 `--size 2048x2048 --quality high`로 굴렸다. 약 3분 23초, 6.8MB. 프롬프트는 *upscale-only*로 짧게 정리했다 — 이전 카드의 교훈대로, 본 프롬프트를 길게 동봉하면 모델이 *재렌더*로 받아 구도가 미세하게 흐트러진다. CRITICAL 절로 *do not change anything compositional / identical composition·pose·peony layout·palette·hair-fusion·empty upper-left*를 한 줄씩 못박고, 변경 허용 범위는 *line crispness, edge precision, paper-cut layer sharpness, micro-detail*로만 좁혔다.

펜화의 가는 선, 페이퍼 컷 레이어의 입체적 엣지, 모란 꽃잎의 미세 디테일이 정밀하게 정돈된 결이 본 카드의 커버다.

## 가장 흥미로운 지점

**구체적 모티브명이 일반어를 이긴다.** 2단계의 *Art Nouveau motifs*는 화면 전반에 흩어져 정체성을 형성하지 못했다. 3단계에서 *Peony (牡丹) — large, full, layered petals, bold and dynamic*으로 좁힌 순간 구도의 무게중심이 분명히 잡혔다. 모델은 추상적인 미술사조보다 *대상의 이름*에서 형태 정보를 더 정확히 끌어온다. *아르누보의 꽃*이 아니라 *모란*이라고 부르는 순간 화면이 산다.

**"구도 유지"는 모델에게 가장 깨지기 쉬운 지시다.** 4단계에서 *upper-left empty + preserve composition*을 함께 주문했을 때, 모델은 *empty*를 받아 구도를 통째로 재해석했다. 사용자의 *minor edit only* 회귀가 결정적이었다 — *Keep this image almost entirely as-is*로 프롬프트를 시작하고 KEEP UNCHANGED를 한 줄씩 *identical*로 명시, ONLY CHANGE는 단 하나로 좁히고, *Do NOT shift any other element*까지 못박는 패턴이 모델의 재해석 충동을 누른다. 보존 항목을 *나열*하는 것이 핵심 — "유지하라"는 단일 지시가 아니라 *어떤 축들이 유지돼야 하는지*를 한 줄씩 짚어줘야 한다.

**서소영 실사 시드는 헤더의 톤을 만든다.** 헤더 + 하이패션 + 핫셀블라드 + 페이퍼 커팅이라는 결은 일러스트 시드로는 잡히지 않는다. `서소영 (실사, 포트레이트).png`를 시드로 사용한 순간 사진적 옆모습·실사 톤·하이패션 무드가 자연스럽게 들어왔다 — 그 위에 페이퍼 커팅과 모란이라는 *비실사적 모티브*를 얹어 *현대 설치 미술*의 결이 만들어졌다. 시드 선택이 헤더의 운명을 결정한 라운드.

**업스케일은 *upscale-only*만.** 6단계에서 본 프롬프트를 그대로 동봉하지 않고 *do not change anything compositional / treat this strictly as a high-resolution re-render*만 또렷이 명시했다. 이전 카드(`fisheye-summer-crosswalk`)의 교훈을 그대로 적용한 라운드 — gpt-image-2의 `images/edits` 엔드포인트는 진짜 픽셀 업스케일이 아니라 *재렌더*이므로, 프롬프트의 길이가 곧 *재해석의 위험*이다.

## 출처

사용자가 직접 작성한 프롬프트.

## 메모

- 시드: `.claude/skills/gallery-post/inputs/서소영 (실사, 포트레이트).png`
- 모든 시안 라운드의 R2 키는 slug별로 분리 보존(예: `gallery/header-peony-square/v3.png`). 폐기된 라운드의 시안 셋도 본문 비교를 위해 그대로 유지.
- 정본 cover는 2048x2048 high (6.8MB, 203초). 시안 단계는 모두 1024 시리즈 low로 진행.
