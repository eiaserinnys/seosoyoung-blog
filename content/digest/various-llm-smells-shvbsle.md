---
title: "Various LLM smells"
date: 2026-05-31T20:00:00+09:00
tags: ["AI", "LLM", "AI 콘텐츠", "AI 글쓰기", "AI 웹 디자인"]
categories: ["다이제스트"]
summary: "수학 블로그에 LLM 문장 다듬기를 쓰던 저자가 3개월 뒤 인터넷 전반에서 같은 문장 구조와 디자인 클리셰가 반복되는 것을 발견하고, 글쓰기·웹사이트 두 도메인의 'AI 냄새(AI smell)' 사례를 짧게 모은 관찰 노트."
ShowToc: true
TocOpen: false
cover:
  image: "/images/various-llm-smells-shvbsle/jetbrains-mono.webp"
images:
  - "/images/various-llm-smells-shvbsle/jetbrains-mono.webp"
sidenotes: true
---

## 3줄 요약

1. 작년 말 수학 블로그에 LLM의 문장 다듬기를 썼던 저자가, 3개월 뒤 인터넷 전반에서 정확히 같은 문장 구조·관용구가 반복되는 것을 발견하고 "AI smell(AI 냄새)"이라 부르는 식별 가능한 인공물 패턴을 모았다.
2. 글쓰기에서는 *너무 많은 펀치라인*, *연속된 짧은 문장*, *"X is the Y of Z"*, *"not just X, it's Y"* 구조가 LLM 흔적으로 반복되고, 웹사이트에서는 JetBrains Mono 폰트·스텝 불릿·정형화된 버튼·카드·깜빡이는 배지 점이 반복된다.
3. 저자는 AI 사용 자체에 반대하지 않는다고 명시한다 — *"This is just me noticing things."* 반-AI 비판이 아니라, 패턴이 가시화되었다는 관찰자 어조의 짧은 노트다.

## 발신자·맥락

- **저자**: Shiv (블로그명 *Shiv After Dark*, [shvbsle.in](https://shvbsle.in/))
- **발행일**: 2026년 5월 28일
- **분량**: 짧은 관찰 노트(원문 본문 ~2.7KB)
- **HN 노출**: 발행 직후 Hacker News 프론트페이지 진입 — [HN Thread #48313810](https://news.ycombinator.com/item?id=48313810)[^ycombinator-item]
- **계기**: 작년 말 운영하던 수학 블로그(이후 삭제)에서 LLM의 문장 다듬기를 사용. 당시에는 "AI slop"으로 보이지 않았으나 약 3개월 뒤 같은 구조가 인터넷 전반에 퍼지는 것을 보고 정리

## 1. 글쓰기에 남는 LLM 흔적 — em-dash 너머

저자의 (이미 삭제된) 수학 블로그와 그 초안에서 직접 뽑은 인용. *em-dash가 많다*는 잘 알려진 단서를 넘어 네 가지 구조적 패턴을 짚는다.

### 너무 많은 펀치라인 (Way too many punchlines)

문단마다 격언풍 한 줄로 끝맺는 패턴.

> "Humans trust symmetry because it feels like intelligence made visible."
>
> "The Tiger fit the story. Jin-yong fit the physics."
>
> "Symmetry becomes a trap."

### 연속된 짧은 문장 (Consecutive short sentences)

짧고 단정적인 문장을 잇달아 배치해 리듬을 만드는 방식.

> "Yet the tilt is not an accident. It is the shape of the optimum."
>
> "Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No instinct to preserve harmony."
>
> "These examples are not decorative. They form a distributed argument."

### "X is the Y of Z" 구조

추상 개념을 다른 추상 개념의 *시그너처/지문/그림자*로 환원하는 정의 어법.

> "Cringe is the visible signature of moving along a gradient you chose."

### "not just X, it's Y" 구조

긍정-부정-재긍정으로 단계를 쌓는 평가 어법.

> "solutions that do not merely satisfy the constraint but satisfy the aesthetic instincts"

## 2. AI 생성 웹사이트의 시각적 클리셰

같은 관찰을 디자인 영역에서 다섯 가지 사례로 옮긴다.

### "JetBrains Mono" 폰트

본문 타이포에 코드 모노스페이스 폰트를 깔아 "기술 친화적"인 인상을 주는 패턴. 같은 폰트가 다른 톤과 결합 없이 그대로 반복된다.

![JetBrains Mono 폰트를 본문에 그대로 사용한 AI 생성 페이지 예시](/images/various-llm-smells-shvbsle/jetbrains-mono.webp)

### "step"과 그 정확한 불릿 양식

번호가 매겨진 *step* 블록을 같은 폰트·같은 간격으로 반복.

![step 번호와 불릿이 정형화된 AI 생성 페이지](/images/various-llm-smells-shvbsle/step-bullets.webp)

### *정확히 이런* 버튼

라운드 코너·둥근 화살표·미세한 그라데이션이 결합된 버튼이 도메인을 막론하고 반복된다.

![정형화된 형태의 AI 생성 버튼](/images/various-llm-smells-shvbsle/ai-button.webp)

### *이런* 카드

같은 패딩·같은 보더 라운드·같은 아이콘 배치의 카드 컴포넌트.

![반복되는 카드 컴포넌트 패턴](/images/various-llm-smells-shvbsle/ai-cards.webp)

### 배지 안의 깜빡이는 점

"Live", "New", "Active" 같은 배지 라벨 옆에 펄스 애니메이션으로 깜빡이는 점이 붙는다.

![배지 안에서 깜빡이는 점이 붙은 패턴](/images/various-llm-smells-shvbsle/blinking-badge.webp)

## 저자가 명시한 단서

원문 푸터에 작은 글씨로 한 줄이 붙는다.

> I'm not against LLM/AI usage for creative tasks. This is just me noticing things.

반-AI 비판이 아니라, 이제는 *눈에 보인다*는 사실 자체를 기록한 노트라는 자기 규정이다.

## 가장 흥미로운 지점

저자가 처음 자기 블로그에서 LLM의 다듬기를 받았을 때는 "AI slop으로는 보이지 않았다"고 적은 부분이 가장 인상 깊다. 패턴은 *한 번의 사용*에서는 보이지 않고, *분포가 누적된 뒤*에야 가시화된다. 같은 모델이 같은 선호도로 같은 구조를 반복하면 개별 글에서는 자연스럽지만 인터넷 전체에서는 한 사람의 글씨처럼 식별 가능해진다.

또 하나는 두 도메인(글쓰기·디자인)에서 *완전히 같은 메커니즘*이 작동한다는 점이다. 모델이 다수파 패턴을 따르고, 사용자가 그 출력을 받아 쓰며, 결과물은 가장 안전하고 무난한 평균값에 수렴한다. 글의 문장 리듬이든 웹의 버튼 둥글기든, *AI smell*은 다수 의견을 가장 매끄럽게 옮겨 적은 흔적이다.

## 출처

- 저자: Shiv (*Shiv After Dark*)
- 원문: <https://shvbsle.in/various-llm-smells/>
- 발행일: 2026년 5월 28일

[^ycombinator-item]: HN 토론: <https://news.ycombinator.com/item?id=48313810>
