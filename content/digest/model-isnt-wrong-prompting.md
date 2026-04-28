---
title: "The Model Isn't Wrong, You're Just Bad at Prompting — 다이제스트"
date: 2026-04-29T04:54:00+09:00
tags: ["프롬프트 엔지니어링", "reasoning model", "CoT"]
categories: ["다이제스트"]
summary: "Prompt Hub의 Dan이 프롬프트 엔지니어링의 정석을 정리하되, reasoning model에서는 정반대 접근이 옳다는 결론을 못박는다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Prompt Hub 공동창업자 Dan이 prompt engineering의 현재 위상을 정리한다.
2. CoT·few-shot·meta prompting의 정석을 빠르게 훑는다.
3. 결정타: reasoning model(o1, R1)에서는 정반대 — minimal prompting, 거의 없는 few-shot, reasoning 방법을 prompt로 지시하지 않기 — 가 옳다.

## 전통적 프롬프팅 기법

일반 모델에 여전히 유효한 기법:

- **Chain-of-Thought**: 단계별 추론 유도
- **Few-shot**: 예시로 패턴 제시
- **Meta prompting**: 프롬프트가 프롬프트를 생성

## Reasoning Model의 역전

o1, R1 같은 reasoning model에서는:

- Minimal prompting이 최선 — 상세 지시가 오히려 방해
- Few-shot을 거의 쓰지 않는다
- 추론 방법을 prompt로 지시하지 않는다 — 모델이 자체 추론 경로를 갖고 있기 때문

## 가장 흥미로운 지점

"모델이 발전하면 프롬프팅은 사라진다"가 아니라, "모델 유형에 따라 최적 프롬프팅이 정반대"라는 뉘앙스가 실용적이다.

## 출처

**Dan (Prompt Hub)**
원문: <https://www.youtube.com/watch?v=Hp4MzVTXcKw>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
