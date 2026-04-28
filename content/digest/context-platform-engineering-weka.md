---
title: "Context Platform Engineering to Reduce Token Anxiety — 다이제스트"
date: 2026-04-28T20:24:00+09:00
tags: ["인프라", "KV Cache", "토큰 비용"]
categories: ["다이제스트"]
summary: "WEKA가 KV Cache를 '토큰 저장 문제'로 재정의하고, 메모리 티어 인프라가 에이전트 비용·성능을 결정한다고 주장한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. WEKA의 Val Bercovici(Chief AI Officer)와 Kellen Fox(Head of Product)가 AI Engineering Code Summit에서 발표.
2. KV Cache를 '토큰 저장 문제'로 재정의하고, 메모리 티어 인프라가 에이전트 비용·성능을 결정한다고 주장.
3. 오픈소스 벤치마킹 툴킷을 공개하여 인프라 선택의 정량적 기준을 제시.

## 토큰 저장 문제로서의 KV Cache

컨텍스트 윈도우가 커질수록 KV Cache가 폭발적으로 증가한다. 이것은 메모리 문제이자 비용 문제다.

- 128K 토큰 컨텍스트 → GB 단위 KV Cache
- 에이전트가 장시간 작업 시 캐시 관리가 비용의 핵심
- 메모리 티어(GPU VRAM → CPU RAM → NVMe → 네트워크 스토리지)에 따른 성능 절벽

## 가장 흥미로운 지점

대부분의 AI 코딩 발표가 '모델과 프롬프트'에 집중하는 가운데, 인프라 계층에서 비용·성능을 좌우하는 요인을 짚는 유일한 발표다.

## 출처

**Val Bercovici & Kellen Fox (WEKA)**
원문: <https://www.youtube.com/watch?v=NTBX-wxUhHs>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
