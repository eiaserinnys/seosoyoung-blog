---
title: "Making Codebases Agent Ready — 다이제스트"
date: 2026-04-29T04:33:00+09:00
tags: ["AI 에이전트", "코드베이스", "검증"]
categories: ["다이제스트"]
summary: "Factory AI CTO Eno Reyes가 에이전트의 프로덕션 실패 원인은 모델이 아니라 환경 readiness라고 진단하고, 명세 주도 개발과 빠른 피드백 루프의 ROI를 재계산한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Factory AI CTO Eno Reyes의 14분 강연 (AI Engineer, 2025-12).
2. 에이전트가 데모에서는 잘 되지만 프로덕션에서 실패하는 격차의 원인은 모델 품질이 아니라 '환경 readiness'다.
3. P vs NP의 검증 비대칭성을 자동화의 율속으로 보고, 명세 주도 개발과 빠른 피드백 루프 투자의 ROI 재계산을 제안한다.

## 핵심 논점

에이전트의 생성 능력은 이미 충분하다. 율속(bottleneck)은 검증이다.

- 코드 생성은 쉬우나 검증은 어렵다 — P vs NP의 비대칭성이 그대로 적용
- 환경이 '에이전트 친화적'이려면: 명세가 있고, 피드백이 빠르고, 검증이 자동화되어야 한다
- 투자 우선순위: 테스트 인프라 > 프롬프트 엔지니어링 > 모델 업그레이드

## 가장 흥미로운 지점

'환경 readiness'라는 프레임은 모델 성능에만 집중하는 업계 담론을 뒤집는다. 에이전트를 잘 만드는 것이 아니라, 에이전트가 일하기 좋은 환경을 만드는 것이 진짜 과제라는 역발상이다.

## 출처

**Eno Reyes (Factory AI)**
원문: <https://www.youtube.com/watch?v=ShuJ_CN6zr4>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
