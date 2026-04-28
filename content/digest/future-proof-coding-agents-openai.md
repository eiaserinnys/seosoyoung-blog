---
title: "Future-Proof Coding Agents — 다이제스트"
date: 2026-04-29T05:42:00+09:00
tags: ["OpenAI", "Codex", "SDK", "에이전트 아키텍처"]
categories: ["다이제스트"]
summary: "OpenAI Applied AI팀이 코딩 에이전트를 모델 업그레이드에서 살아남게 만드는 방법을 제시한다. 하네스 복잡성을 SDK에 위임하라는 것이 핵심."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. OpenAI Applied AI Startups팀의 Bill Chen & Brian Fioca의 발표.
2. 코딩 에이전트를 모델 업그레이드에서 살아남게 만드는 '미래 보존형(future-proof)' 아키텍처를 논한다.
3. 하네스(harness)의 복잡성을 SDK 벤더에게 위임하고 제품 차별화에 집중하라는 것이 핵심 메시지.

## Future-Proof 아키텍처

모델이 빠르게 업그레이드되는 환경에서:

- 하네스(프롬프트 체인, 도구 관리, 에러 핸들링)가 복잡할수록 모델 교체 비용 증가
- SDK(Codex)가 하네스를 추상화하면 모델 교체가 투명해짐
- 제품 팀은 차별화 로직에만 집중

## Codex = 모델+하네스 결합체

Codex를 SDK로 제공하여 '미래 보존형' 에이전트 아키텍처를 제안:

- 모델 업그레이드 시 하네스도 함께 최적화
- 벤더 종속 vs 미래 보존의 트레이드오프 존재

## 가장 흥미로운 지점

영상 24(Boris Cherny)의 "단순하게 만들라"와 정반대 접근처럼 보이지만, 실은 같은 목표(복잡성 회피)를 다른 수단으로 달성한다. Anthropic: 단순한 도구. OpenAI: SDK에 위임.

## 출처

**Bill Chen & Brian Fioca (OpenAI)**
원문: <https://www.youtube.com/watch?v=wVl6ZjELpBk>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
