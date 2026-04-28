---
title: "Can you prove AI ROI in Software Engineering? — 다이제스트"
date: 2026-04-29T04:45:00+09:00
tags: ["생산성 측정", "ROI", "연구"]
categories: ["다이제스트"]
summary: "Stanford 연구진이 12만 명 개발자의 git 데이터를 2년간 분석하여 AI 코딩 도구의 실제 ROI를 정량 측정한 발표."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Stanford 연구진이 약 2년간 12만 명 개발자의 git 데이터를 시계열·교차단면으로 분석한 발표.
2. AI 코딩 도구의 실제 ROI를 '사용량'이 아닌 '산출물 변화'로 측정하려 한다.
3. 사용량·환경 청결성·도입 후 산출물·재작업 등 측정 가능한 신호로 AI 효과를 검증하는 방법론을 제안한다.

## 연구 방법론

- 12만 명 규모의 git 활동 데이터 기반
- 시계열 분석: 도구 도입 전후 비교
- 교차단면 분석: 사용자 vs 비사용자 비교
- 측정 지표: commit 빈도, PR 크기, 리뷰 턴어라운드, 재작업률

## 핵심 발견

단순 '생산성 향상 X%' 주장의 함정을 짚으면서, 올바른 측정 프레임워크를 제시한다.

## 가장 흥미로운 지점

업계가 AI 도구의 ROI를 '설문조사'나 '체감'으로 측정하는 가운데, git 데이터라는 객관적 신호로 접근한 희소한 대규모 연구다.

## 출처

**Yegor Denisov-Blanch (Stanford)**
원문: <https://www.youtube.com/watch?v=JvosMkuNxF8>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
