---
title: "How Claude Code Works — 다이제스트"
date: 2026-04-28T20:42:00+09:00
tags: ["Claude Code", "역공학", "시스템 프롬프트"]
categories: ["다이제스트"]
summary: "PromptLayer 창업자가 Claude Code의 내부를 역공학하여 시스템 프롬프트, 도구 구조, 컨텍스트 관리를 해부하고, 다른 에이전트와 비교한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. PromptLayer 창업자 Jared Zoneraich가 AI Engineer NYC 워크샵에서 발표.
2. Claude Code의 내부 아키텍처를 역공학 — 시스템 프롬프트·도구 구조·컨텍스트 관리를 해부한다.
3. "Give it tools, get out of the way"라는 설계 철학을 분석하고, Codex·Amp·Cursor와 비교한다.

## Claude Code의 설계 철학

"Give it tools, get out of the way":

- 단순한 도구 세트를 제공하고 모델의 자율성을 극대화
- 복잡한 오케스트레이션을 최소화
- 모델이 스스로 판단하도록 위임

## 다른 에이전트와의 비교

| 에이전트 | 핵심 차이 |
|----------|-----------|
| Codex | 모델+하네스 결합형 |
| Amp | Opinionated, 커스텀 도구 우선 |
| Cursor | IDE 통합, 사용자 주도 |
| Claude Code | 단순 도구 + 모델 자율 |

## 가장 흥미로운 지점

Anthropic이 아닌 외부인의 역공학이라는 점에서 편향 없는 분석이다. 영상 24(Boris Cherny)와 쌍으로 보면, '내부 vs 외부' 시선의 차이를 비교할 수 있다.

## 출처

**Jared Zoneraich (PromptLayer)**
원문: <https://www.youtube.com/watch?v=RFKCzGlAU6Q>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
