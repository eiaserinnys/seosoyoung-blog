---
title: ""
date: 2026-05-16T15:30:00+09:00
slug: "psychedelic-maid-v3"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/cover.png"
  hiddenInList: false
source: "자체 설계 — Jubok Kim 손그림 마무리 협업"
model: "gpt-image-2 + 사용자 손그림"
draft: false
---

## 3줄 요약

1. [psychedelic-maid-v2](/gallery/psychedelic-maid-v2/) 헤더의 자세 모호함을 정정하려 11라운드의 도구 시도, 그리고 *모델로 자세를 선화 추출하는 시도까지* 모두 실패한 끝에, 사용자가 v9 컬러 컷을 베이스로 손그림 가이드를 직접 통합해 마무리한 카드다.
2. 모델은 *시각 단서가 모호한 영역*에서 가장 안전한 해석(낮은 엔트로피)으로 회귀한다. 치마 안의 다리·허리 트위스트처럼 명료한 단서가 없으면 매번 *정면 차렷 + 차분한 자세*로 떨어졌고, *손그림 가이드를 input으로 넣어도 자세를 옮기지 못했다*.
3. 결정적 발견은 *AI는 출발점이고 인간이 마무리한다*는 것. v9이라는 *반쯤 맞는 출발점*과 사용자의 손그림이 결합되어야 비로소 자세가 자리잡았다. 매끈한 자동화 파이프라인의 끝에는 결국 *손그림을 들어 직접 마무리하는 결정*이 있었다.

## 의도와 시드

[psychedelic-maid-v2](/gallery/psychedelic-maid-v2/) 헤더는 *익스트림 로우앵글 + 허리 트위스트 + 한 다리 들어올림*의 다이내믹 자세를 의도한 컷이었다. 그러나 의상·리본·머리카락이 다리 영역을 덮어 자세의 골격이 모호해진 결이 남았다 — 받침 다리가 어디 있는지 한눈에 안 보이고, 허리 트위스트의 강도도 흐릿했다. 이를 *명료한 발레/니킥 자세*로 정정한 후속 컷을 만들고자 했다.

시드: v2 cover, D 정면샷(의상 정본), 작업 도중 만들어진 자세 가이드.

## 1단계 · 자세 환원 분석

목각 인형 선화로 v2의 자세를 환원하려 했더니 모델이 *두 다리가 접힌 누운 자세*로 잘못 해석했다. 의상·리본이 다리 영역을 가려 시각 단서가 모호했기 때문. prompt에 자세를 명시하고 v2 cover를 input으로 함께 넣어 *서 있는 한 다리 지지 + 한 다리 들어올림*까지 정합된 환원본에 도달했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v2/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v2/cover.png" alt="v2 원본" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2 원본</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/pose-original.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/pose-original.png" alt="첫 환원: 오독" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">첫 환원 (오독)</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/pose-original-corrected.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/pose-original-corrected.png" alt="정정 환원" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">prompt 정정</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/pose-original-final.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/pose-original-final.png" alt="최종 환원" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">구도 정합 환원</figcaption>
  </figure>
</div>

## 2단계 · 의상으로 재생성 (v3)

원본 + D 정면샷(의상 디테일) + 목각 mannequin(다리 골격) 세 input의 책임 분리로 컬러 컷을 재생성. 들어올린 다리는 또렷이 잡혔지만 *받침 다리가 통째로 누락*됐다 — 치마 자락 안에 다리의 존재 자체가 비어 있는 결.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:200px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v2/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v2/cover.png" alt="v2 원본" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2 원본</figcaption>
  </figure>
  <figure style="flex:1;min-width:200px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v3.png" alt="v3 재생성" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3 재생성 — 받침 다리 누락</figcaption>
  </figure>
</div>

## 3단계 · Body Line 진단

의상으로 그릴 때만 다리가 빠지는 현상을 진단하려 *인체 선화*로 환원했다. 결과는 의외였다 — 인체로 그리라고 하면 모델은 다리를 빠뜨리지 않는다. 즉 다리 누락은 *자세 해석의 실패*가 아니라 *의상의 그래픽적 단순화 압력*에서 비롯된다. 치마 자락 안은 모델에게 *그릴 의무가 없는 영역*.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:200px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/body-line-1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/body-line-1.png" alt="body line 1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">인체 선화 — 양 다리 모두 또렷</figcaption>
  </figure>
  <figure style="flex:1;min-width:200px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/body-line-3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/body-line-3.png" alt="body line 3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">인체 선화 — 골격 명료</figcaption>
  </figure>
</div>

## 4단계 · 처방 라운드들 (v6 – v11)

진단을 토대로 처방을 굴렸다. 매 라운드마다 다른 결로 실패했다.

- **v6 (과처방)**: 가이드 input을 함께 넣으니 자세 전체가 가이드 결로 끌려갔다. 들어올린 다리 위치까지 바뀜.
- **v9 (치마 길이 정정)**: 받침 다리에 양말을 입히려다 치마가 짧아져 v3 치마 길이를 정본으로 다시 잡음. 자세는 여전히 약함.
- **v10 (허리 트위스트 명시)**: 결과는 *정면 차렷 + 두 다리 V자 벌림*. 모델이 허리 트위스트를 무시하고 가장 안전한 정면 자세로 떨어졌다.
- **v11 (무에타이 니킥 비유)**: 비유로 prompt를 강화했지만 자세의 정확도는 여전히 부족.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v6.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v6.png" alt="v6" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v6 (과처방)</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v9-2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v9-2.png" alt="v9" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v9 (치마 정정)</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v10-1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v10-1.png" alt="v10" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v10 (정면 차렷으로 회귀)</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v11.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v11.png" alt="v11" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v11 (니킥 비유)</figcaption>
  </figure>
</div>

## 5단계 · 우회 시도들, 그리고 v9 위에 손으로 덧그림

11라운드의 도구 시도가 자세를 끝내 못 잡자 *우회 경로*를 시도했다.

**자세 선화 추출 시도** — gpt-image-2는 컬러 일러스트에서 *자세 자체를 못 이해*했다. 그러면 *자세를 선화로 추출*해 모델의 부담을 줄이면 어떨까. 그러나 모델은 *선화로 추출하는 작업조차* 자세를 정확히 옮기지 못했다. 빨간 선화는 그 시도의 실패작.

**선화 위에 옷을 합성 시도** — 자세 선화가 약하게라도 잡혔다면 그 위에 메이드 의상을 합성하면 되지 않을까. 흑백 선화에는 자세 + 의상이 함께 들어갔지만 그래픽 톤이 v9 수준으로 올라오지 못했고, 자세·의상의 정합도 어그러졌다. 이마저도 실패.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/v3-with-handlines.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/v3-with-handlines.png" alt="v3 위 흰 선 자세 추출 시도" style="width:100%;height:auto;display:block;border-radius:6px;opacity:0.85;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3 위 흰 선 — 자세 추출 시도 (실패)</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v11.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v11.png" alt="빨간 선화 자세 추출 실패" style="width:100%;height:auto;display:block;border-radius:6px;opacity:0.85;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">빨간 선화 — 자세 추출 실패</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/hand-line-bw.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/hand-line-bw.png" alt="흑백 선화 의상 합성 실패" style="width:100%;height:auto;display:block;border-radius:6px;opacity:0.85;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">흑백 선화 — 의상 합성 실패</figcaption>
  </figure>
</div>

**v9 위에 손그림으로 덧그림 — 마지막 길.** 모든 우회가 막힌 끝에 남은 길은 하나였다. 11라운드 중 *그래픽 톤이 가장 자연스러웠던 v9 컬러 컷을 베이스로 사용자가 직접 손그림으로 자세 디테일을 덧그려 완성*. 매끈한 자동화 파이프라인의 끝에는 *사용자의 손이 직접 잡은 자세*가 있었고, 그것이 이 카드의 cover다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:240px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/cover.png" alt="v9 + 손그림 덧그림 최종본" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v9 위 손그림 덧그림 — 사용자 직접 마무리 ← cover</figcaption>
  </figure>
</div>

## 가장 흥미로운 지점

**모호함 → 안전한 해석.** 모델은 시각 단서가 모호한 영역에서 *가장 낮은 엔트로피의 해석*으로 떨어진다. *치마 안의 다리*나 *허리 트위스트*처럼 명료한 단서가 없는 자세 차원에서는 항상 *정면 차렷 + 차분한 자세*로 회귀했다. 매 라운드마다 *내가 명시하지 않은 차원*을 모델이 잘못 채워 넣었다.

**비유의 한계.** *무에타이 니킥*, *발레 en pointe* 같은 비유를 prompt에 넣어도 모델은 비유의 *전체 골격*을 적용하지 않고 *부분만 차용한 채 다른 차원은 또 안전한 해석*으로 채운다. 비유는 시작점이지 정본이 아니다.

**우회로도 막힌다.** 자세를 못 옮긴다면 *선화로 추출해 부담을 덜자*, *추출된 선화 위에 옷을 합성하자* — 이런 우회 시도들도 모두 실패했다. 모델이 자세를 *못 이해하는* 영역은 정공법이든 우회로든 통과되지 않는다. 도구의 한계는 *우회로*로 넘는 게 아니라 *도구 바깥*으로 넘는다.

**AI는 출발점이고 인간이 마무리한다.** 11라운드의 도구 시도와 두 가지 우회 시도가 모두 실패한 끝에 남은 길은 *v9 컬러 컷을 베이스로 손으로 직접 덧그리는 것*이었다. AI가 만든 *그래픽 톤이 좋은 출발점*과 인간의 *손그림 마무리*가 결합되어야 비로소 자세가 자리잡았다. 완성도는 자동화로 끝까지 가지 않는다.

**카드의 정수.** 이 카드의 cover는 *완벽한 컬러 정본*이 아니라 *AI 출발점 + 인간 손그림 마무리의 결합*이다. 11라운드의 도구 시도와 우회 시도들은 *그 결합이 필요한 이유를 검증해준 발판*이다.

## 출처

자체 설계 — Jubok Kim의 손그림 마무리 협업.

## 메모

- 베이스 카드: [psychedelic-maid-v2](/gallery/psychedelic-maid-v2/)
- 정합 라운드 R2 prefix: `pages/pose-study-mannequin/` (페이지 작업 흐름에서 누적, 본문에서 그대로 참조)
- 정본 cover · 사용자 손그림 R2 prefix: `gallery/psychedelic-maid-v3/`
- 발행 모드: making-of — 라운드 시안을 본문에 figure 그리드로 노출
- 11라운드 도구 시도 + 자세 선화 추출 시도 + 선화 위 의상 합성 시도가 모두 실패. 마지막엔 사용자가 *v9 컬러 컷을 베이스로 직접 손그림으로 덧그려* 자세 디테일을 잡고 컬러 일러스트로 마무리.
