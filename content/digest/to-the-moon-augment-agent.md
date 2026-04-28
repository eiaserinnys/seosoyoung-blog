---
title: "To the moon! Navigating deep context in legacy code — 다이제스트"
date: 2026-04-28T21:03:00+09:00
tags: ["AI 에이전트", "레거시 코드", "컨텍스트 엔진"]
categories: ["다이제스트"]
summary: "Augment Code가 Apollo 11 AGC 어셈블리를 '궁극의 레거시'로 시연하며, 컨텍스트 엔진이 코드를 '텍스트가 아닌 코드로' 다루어야 한다고 주장한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Forrest Brazeal과 Matt Ball(Augment Code)이 AI Engineer World's Fair 2025에서 발표한 15분 강연.
2. Apollo 11 AGC 어셈블리 코드를 '궁극의 레거시 코드'로 두고 Augment Agent로 1202 알람을 조사하고 P65 착륙 알고리즘을 자율로 구현해 보인다.
3. 핵심 메시지: 컨텍스트 엔진이 코드를 '텍스트가 아닌 코드로' 다루어야 모델이 레거시를 이해할 수 있다.

## 핵심 내용

Apollo 11의 어셈블리 코드라는 극단적 사례를 통해 컨텍스트 엔진의 필요성을 시연한다.

- AGC 어셈블리는 문서도 부족하고 문법도 현대와 완전히 다른 '궁극의 레거시'
- 단순 토큰 기반 처리로는 의미를 파악할 수 없음 — 코드의 구조·의존성·흐름을 이해해야
- Augment의 컨텍스트 엔진이 코드 그래프를 구축하여 에이전트에게 제공
- 1202 알람 조사 → P65 착륙 알고리즘 구현까지 자율 수행 시연

## 가장 흥미로운 지점

극단적 레거시(1960년대 어셈블리)를 시연 소재로 택한 것이 설득력을 높인다. 현대 코드도 3년만 지나면 레거시가 되는 현실에서, 컨텍스트 엔진의 가치를 가장 극적으로 보여주는 사례다.

## 출처

**Forrest Brazeal & Matt Ball (Augment Code)**
원문: <https://www.youtube.com/watch?v=6NIr_cYPglk>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
