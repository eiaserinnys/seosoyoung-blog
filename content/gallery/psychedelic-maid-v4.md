---
title: ""
date: 2026-05-19T22:22:00+09:00
slug: "psychedelic-maid-v4"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4/cover.png"
  hiddenInList: false
  focus: "50% 30%"
source: "자체 설계"
model: "gpt-image-2"
draft: false
---

## 3줄 요약

1. *컬러 직행 → 실패 → 선화로 회귀 → 역할 분리 컬러화 → 광학 마감*의 4막 구조. 매 단계 진단이 다음 라운드의 보정 축이 되어 *광각 클로즈업 + 사이키델릭 눈동자*의 사이키델릭 메이드 인상이 비로소 자리잡았다.
2. 컬러 단계에서 *포즈 유지*와 *다이나믹*을 한 프롬프트에 함께 요구하면 모델은 *다이나믹*을 우선해 광각 정체성을 흘려보낸다. 두 지시가 충돌하는 순간, *작가가 양보한 차원*을 모델이 자유롭게 채워 넣는다.
3. 결정적 우회는 *선화로 돌아가는 결정*이었다. 포즈와 인상의 *골격을 흑백으로 먼저 굳히고*, 색은 *역할 분리된 reference*로 따로 입혔다. 마무리는 *도어 렌즈 광학 효과* — 광각 왜곡이라는 형식의 결정에 *"문 너머의 시선"*이라는 의미가 사후적으로 부여되었다.

## 의도와 시드

[psychedelic-maid-v3](/gallery/psychedelic-maid-v3/)가 *AI는 출발점이고 인간이 마무리한다*는 결로 닫혔다면, v4는 *반대편의 결*에서 시작한 카드다. 이번엔 *손그림을 거치지 않고도 자세와 인상을 끝까지 자동화로 끌고 갈 수 있는가*를 물었다.

테마는 *사이키델릭한 세계에 들어선 찻쟁반을 든 메이드*. 의상·색감·광기는 v2/v3에서 정립된 결을 잇되, **포즈는 새로 — 광각 왜곡 + 얼굴 클로즈업 + 도어 렌즈 너머의 시선**으로 가져가기로 했다.

시드: 없음. 텍스트 prompt와 다회차 reference 입력만으로 인상을 빚어 올린다.

## 1단계 · 컬러 직행 (실패)

먼저 *컬러로 직행*하는 정공법을 시도했다. 9컷 컬러 시안 시트로 가능한 자세·구도의 후보를 한 번에 뽑고, 그중 하나를 시드로 잡아 "*포즈를 다이나믹하게*" 변형을 반복했다. 결과는 4컷의 *서로 다른 컬러 변형* — 정면 정적 / 공중 다이나믹 / 점프 / 다시 정적 — 였다. 모두 *완성도 자체는 높지만 무엇 하나도 "광각 클로즈업"이라는 인상의 골격을 담고 있지 않았다*.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s1-9grid.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s1-9grid.png" alt="컬러 9컷 시안" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">컬러 9컷 시안 시트</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s2-static.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s2-static.png" alt="정면 정적" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">변형 1 — 정면 정적</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s3-airborne.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s3-airborne.png" alt="공중 다이나믹" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">변형 2 — 공중 다이나믹</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s4-jump.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s4-jump.png" alt="점프" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">변형 3 — 점프</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s5-static.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r1/s5-static.png" alt="다시 정적" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">변형 4 — 다시 정적</figcaption>
  </figure>
</div>

진단은 명료했다. *"포즈를 유지하면서 다이나믹하게 바꿔줘"* 라는 한 줄의 prompt에 **두 개의 상충 지시**가 들어 있었다 — *유지*와 *변경*. 모델은 이 충돌을 *해소*하지 않고 *다이나믹*에 가중치를 두어 자유롭게 새 자세를 만들었다. 9컷에서 흥미로웠던 광각 시안은 그 과정에서 *시드에 없는 차원*이라 통째로 사라졌다. **광각 정체성을 갖지 않은 시드에서 출발한 것이 근본 오류였다.**

## 2단계 · 선화로 회귀 (포즈 골격)

컬러를 *되돌리고*, 선화로 처음부터 다시 시작했다. *색을 빼니 형식의 골격이 또렷이 보인다* — 9컷 선화 시안에서 *광각 로우앵글*, *극단적 클로즈업*, *광각 왜곡* 같은 구도들이 명료한 후보로 등장했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r2/s1-9grid-a.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r2/s1-9grid-a.png" alt="선화 9컷 1차" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">선화 9컷 — 1차 (광각 탐색)</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r2/s2-9grid-b.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r2/s2-9grid-b.png" alt="선화 9컷 2차" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">선화 9컷 — 2차 (찻쟁반 + 얀데레 톤)</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r2/s3-closeup-eyes.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r2/s3-closeup-eyes.png" alt="광각 클로즈업 + 배경 눈" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">광각 클로즈업 — 배경 눈 모티프</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r2/s4-closeup-clean.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r2/s4-closeup-clean.png" alt="배경 눈 정리 — 선화 최종" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">배경 정리 — 선화 최종 ← 선택</figcaption>
  </figure>
</div>

2차 시트에서 *찻쟁반을 든 메이드*라는 직무·소품 축이 더해졌고, 거기서 한 컷을 골라 *얼굴이 더 가깝게 광각 왜곡되는 클로즈업*으로 끌어올렸다. 배경의 *눈동자 모티프*가 흥미로웠으나 인상이 산만해질 위험이 있어 다음 단계에서 정리. **이 선화가 v4 카드의 인상 골격**이다.

핵심 통찰: *컬러는 무엇이 표현되어 있는지 결정하지만, 선화는 무엇이 표현되어야 하는지 결정한다*. 형식의 결정은 색이 입혀지기 전에 끝나 있어야 한다.

## 3단계 · 역할 분리 컬러화 (성공)

선화 최종을 시드로 컬러화로 넘어갔다. 1단계와 결정적으로 달랐던 것은 **reference의 역할 분리**다.

> 첫번째 첨부한 *포즈와 구도를 활용해서*, 두번째 첨부한 *인물과 색감*을 넣어 다시 그려줘. 인물은 호기심 어린 눈길로 미소 짓고 있는데, 눈 안이 사이키델릭한 컬러로 뱅글뱅글 돌고 있어.

선화는 *포즈와 구도*만 담당. 별도의 인물·색감 reference가 *인상과 톤*만 담당. 텍스트는 *디테일 하나*(눈 안의 사이키델릭 회전)만 추가. **세 입력이 서로의 영역을 침범하지 않는다.** 모델 입장에서 충돌이 없으니 *유지할 것은 유지하고 새로 더할 것만 더한다.*

<div style="display:flex;justify-content:center;margin:20px 0;">
  <figure style="max-width:480px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r3/s1-color.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r3/s1-color.png" alt="역할 분리 컬러화 채택본" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;text-align:center;">광각 클로즈업 보존 + 사이키델릭 눈동자 — 컬러 채택본</figcaption>
  </figure>
</div>

광각 왜곡 클로즈업이 *선에 잡혀 있던 그대로* 살아남았고, 그 위에 사이키델릭 색감과 뱅글뱅글 도는 눈동자가 새로 얹혔다. 1단계에서 한 프롬프트로 한꺼번에 풀려고 했던 모든 요청이, *역할이 분리된 세 입력의 협업*으로 한 번에 떨어진다.

## 4단계 · 광학 마감

채택본은 좋았지만 *조금 더*가 남아 있었다. 세 번의 정교한 보정으로 마무리.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r4/s1-wide-eyes.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r4/s1-wide-eyes.png" alt="광각 강화 + 눈동자 디테일" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">① 광각 강화 + 눈동자 디테일</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r4/s2-props.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4-r4/s2-props.png" alt="찻잔·그릇 사이키델릭 동조" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">② 찻잔·그릇 사이키델릭 동조</figcaption>
  </figure>
  <figure style="flex:1;min-width:160px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/psychedelic-maid-v4/cover.png" alt="도어 렌즈 광학 효과 — 최종" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">③ 도어 렌즈 광학 효과 — 최종 ← cover</figcaption>
  </figure>
</div>

①은 *얼굴을 더 가깝게, 광각을 더 과감하게* — 1단계에서 잃었던 클로즈업의 강도를 끝까지 밀어붙임. ②는 *찻잔·그릇·티팟의 포인트 컬러를 인물 색감과 동조* — 소도구가 배경과 같은 결로 사이키델릭하게 묶이며 화면의 통일성이 잡힘. **③의 마무리가 결정타였다 — 흐림 + 색수차 + 비네팅의 도어 렌즈 광학 효과.** 이 한 줄의 후보정이 *광각 왜곡*이라는 형식의 결정에 **"문 너머에서 들여다본 시선"**이라는 의미를 사후적으로 부여한다. 광각이 *왜 광각이어야 했는지*가 비로소 설명된다.

## 가장 흥미로운 지점

**충돌하는 지시는 모델이 알아서 풀지 않는다.** 1단계의 *"유지하면서 다이나믹하게"* 는 한 줄의 자연어로는 그럴듯해 보이지만, 모델 입장에서는 *해소할 수 없는 충돌*이다. 모델은 충돌을 *해소*하지 않고 *한쪽에 가중치를 두고 다른 쪽을 흘려보낸다*. 작가가 양보한 차원은 모델이 자유롭게 채운다 — 그 자유는 거의 항상 *작가의 의도와 다른 결*로 풀린다.

**형식의 결정은 색이 입혀지기 전에 끝나야 한다.** 컬러로 직행하면 *완성도 자체는 빠르게 올라온다*. 하지만 *완성도와 형식*은 다른 차원이다. 광각이라는 형식의 결정은 *흑백의 단서*에서 더 명료하게 보인다. 색은 형식을 강화하지만, 색이 형식을 *결정*하게 두면 *모델의 안전한 해석*이 우선한다. v3에서 보았던 *낮은 엔트로피로의 회귀*가 형식 차원에서도 동일하게 작동한다.

**reference의 역할 분리가 정공이다.** 한 reference에 *모든 책임*을 지우면 모델이 그 reference의 *어떤 차원을 보존하고 어떤 차원을 변형할지* 자의적으로 선택한다. *포즈는 A reference, 색감은 B reference, 디테일은 텍스트* 처럼 차원을 분리해 위임하면 모델이 *각 입력의 책임 영역을 침범하지 않는다*. 1단계가 실패하고 3단계가 성공한 본질적 차이는 *여기 한 줄에 있다*.

**후보정은 의미를 부여한다.** 4단계 ③의 도어 렌즈 광학 효과는 *기술적으로는 흐림 + 색수차 + 비네팅의 합*이지만, *서사적으로는 "문 너머의 시선"이라는 메타포의 정립*이다. 후보정이 단순히 *마무리*가 아니라 *형식의 사후적 정당화*로 작동하는 순간이 있다. 광각이라는 결정의 *이유*가 이 한 번의 후보정으로 카드에 들어왔다.

**카드의 정수.** v4의 cover는 *4번의 다른 결의 시도가 누적된 결과*다. 컬러 직행의 실패, 선화로의 회귀, 역할 분리의 발견, 광학 마감으로의 의미 부여 — 어느 한 단계라도 빠지면 이 컷이 나오지 않는다. *우회를 통한 성취가 정공의 실패를 헛되이 만들지 않는다*. 1단계의 실패는 *왜 선화로 돌아가야 했는지*를 증명하는 발판이고, 그 발판이 없었다면 3단계의 발견도 없다.

## 출처

자체 설계.

## 메모

- 베이스 카드: [psychedelic-maid-v3](/gallery/psychedelic-maid-v3/) (이전의 *AI 출발점 + 인간 손그림 마무리* 결을 이어, 이번엔 *손그림 없이 자동화 안에서 끝까지* 시도)
- 정본 cover R2 prefix: `gallery/psychedelic-maid-v4/`
- 라운드 시안 R2 prefix:
  - `gallery/psychedelic-maid-v4-r1/` — 1단계 컬러 직행 (실패 시안 5장)
  - `gallery/psychedelic-maid-v4-r2/` — 2단계 선화 회귀 (시안 4장, 채택본 포함)
  - `gallery/psychedelic-maid-v4-r3/` — 3단계 역할 분리 컬러화 (채택본 1장)
  - `gallery/psychedelic-maid-v4-r4/` — 4단계 광학 마감 (보조 시안 2장, 최종 cover는 정본 prefix)
- 발행 모드: making-of — 모든 라운드 시안을 본문에 figure 그리드로 노출. 시안 R2 객체는 보존
- 4단계 흐름: *컬러 직행 (실패) → 선화 회귀 (골격) → 역할 분리 컬러화 (성공) → 광학 마감 (의미 부여)*
- 핵심 발견: *충돌하는 한 줄의 자연어 prompt는 차원 분리된 다중 reference 입력으로 풀린다*
