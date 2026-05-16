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

1. [psychedelic-maid-v2](/gallery/psychedelic-maid-v2/) 헤더의 자세 모호함(받침 다리 누락·허리 트위스트의 어색함)을 정정하려 11라운드의 도구 시도와 사용자의 손그림 가이드까지 거쳤지만 모델은 끝내 자세를 정확히 옮기지 못했고, 결국 *처음 v3 컬러 컷*을 그대로 cover로 받아들인 카드다.
2. 모델은 *시각 단서가 모호한 영역*에서 가장 안전한 해석(낮은 엔트로피)으로 회귀한다. 치마 안의 다리·허리 트위스트처럼 명료한 단서가 없으면 매번 *정면 차렷 + 차분한 자세*로 떨어졌다.
3. 결정적 발견은 *완벽함을 포기하는 결정*이다 — 자세의 모호함을 받아들이고 *그래픽 톤*을 우선시하면, 가장 자연스러운 마무리는 *원본 v3 그 자체*였다. 손그림 가이드는 정점이 아니라 *그 결정을 가능하게 한 검증 도구*가 됐다.

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

## 5단계 · 사용자 손그림 가이드, 그리고 v3 채택

11라운드 끝에 사용자가 직접 자세를 그렸다. 먼저 v3 컬러 위에 흰 선으로 받침 다리·자세 보정을 표시한 가이드, 이어 흑백 선화로 *발레/니킥 자세 + 메이드 의상 + 허리 트위스트*를 정합한 정본 가이드, 그리고 빨간 선화로 정점화한 시각적 결정본.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/v3-with-handlines.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/v3-with-handlines.png" alt="v3 위에 손가이드" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3 위 손그림 가이드 (흰 선)</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/hand-line-bw.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v3/hand-line-bw.png" alt="흑백 선화" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">흑백 선화 — 정본 가이드</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v11.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v11.png" alt="빨간 선화 결정본" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">(가이드를 prompt에 다시 넣어도 모델은 못 옮겼다)</figcaption>
  </figure>
</div>

그러나 *손그림 가이드를 prompt에 또 넣어 굴려도* 모델은 자세를 정확히 옮기지 못했다. 손그림은 *모델을 가르치는 도구*로는 한계가 있었다. 11라운드의 도구 시도와 손그림 가이드까지 모두 통과한 뒤, *결정*에 도달했다 — 자세의 모호함을 받아들이고, 가장 *그래픽적으로 자연스러운 결*인 *원본 v3 컬러 컷*을 그대로 cover로 굳히는 것.

손그림 가이드는 *정점*이 아니라 *그 결정을 검증한 도구*였다 — *AI가 못 옮긴다*는 사실을 정확히 확인시켜준 마지막 시도. 그리고 v3을 받아들이게 한 발판.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:200px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/pose-study-mannequin/regen-v3.png" alt="v3 — 채택본" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v3 컬러 컷 — 최종 채택 ← cover</figcaption>
  </figure>
</div>

## 가장 흥미로운 지점

**모호함 → 안전한 해석.** 모델은 시각 단서가 모호한 영역에서 *가장 낮은 엔트로피의 해석*으로 떨어진다. *치마 안의 다리*나 *허리 트위스트*처럼 명료한 단서가 없는 자세 차원에서는 항상 *정면 차렷 + 차분한 자세*로 회귀했다. 매 라운드마다 *내가 명시하지 않은 차원*을 모델이 잘못 채워 넣었다.

**비유의 한계.** *무에타이 니킥*, *발레 en pointe* 같은 비유를 prompt에 넣어도 모델은 비유의 *전체 골격*을 적용하지 않고 *부분만 차용한 채 다른 차원은 또 안전한 해석*으로 채운다. 비유는 시작점이지 정본이 아니다.

**손그림은 가이드이지 정본이 아니다.** 11라운드를 굴려도 못 잡힌 자세를 사용자가 손그림으로 잡았지만, *그 손그림을 prompt에 다시 넣어도 모델은 옮기지 못했다*. 손그림은 *모델을 정정하는 도구*가 아니라 *모델의 한계를 검증하는 도구*에 가까웠다.

**완벽함을 포기하는 결정.** 결정적 마무리는 *자세를 완벽히 정합하는 것*이 아니라 *그 모호함을 받아들이는 것*이었다. 그래픽 톤·색감·리본의 흐름이 살아있는 *원본 v3*이 자세의 작은 어색함을 덮을 만큼 매력적이었기 때문. 11라운드를 거친 끝에서야 *처음 결과를 받아들이는 결정*에 도달했다.

**카드의 정수.** 이 카드의 cover는 *완벽한 컬러 정본*이 아니라 *AI가 자세를 끝내 옮기지 못했음에도 그래픽 톤이 충분히 강해 받아들여진 결*이다. 11라운드의 시도와 손그림 가이드는 *그 결정의 무게를 만들어준 발판*이다.

## 출처

자체 설계 — Jubok Kim의 손그림 마무리 협업.

## 메모

- 베이스 카드: [psychedelic-maid-v2](/gallery/psychedelic-maid-v2/)
- 정합 라운드 R2 prefix: `pages/pose-study-mannequin/` (페이지 작업 흐름에서 누적, 본문에서 그대로 참조)
- 정본 cover · 사용자 손그림 R2 prefix: `gallery/psychedelic-maid-v3/`
- 발행 모드: making-of — 라운드 시안을 본문에 figure 그리드로 노출
- 사용자가 직접 자세를 손그림으로 그렸지만 모델은 이를 prompt input으로 받고도 정합에 실패. 11라운드 후 *v3 원본을 받아들이는 결정*으로 마무리.
