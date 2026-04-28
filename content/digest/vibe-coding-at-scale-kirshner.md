---
title: "Vibe Coding at Scale — 다이제스트"
date: 2026-04-28T21:06:00+09:00
tags: ["VS Code", "엔터프라이즈", "커스터마이징"]
categories: ["다이제스트"]
summary: "VS Code 팀의 Harald Kirshner가 vibe coding의 3단계 성숙도 모델(YOLO→Structured→Spec-Driven)과 VS Code 커스터마이징 레이어를 제시한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Harald Kirshner(VS Code 팀)가 ~15분간 VS Code의 AI 커스터마이징 기능을 라이브 시연.
2. Vibe coding의 3단계 성숙도 모델(YOLO → Structured → Spec-Driven)을 제시한다.
3. VS Code 커스터마이징 레이어(Chat Modes, Instructions, Prompts, MCP)가 입력측 검증 표면의 조직적 표준화 메커니즘으로 기능한다.

## 3단계 성숙도 모델

- **YOLO**: 아무 규칙 없이 에이전트에게 던짐
- **Structured**: Rules, instructions로 품질 가이드
- **Spec-Driven**: 명세가 코드의 상위 소스

## VS Code 커스터마이징 레이어

- **Chat Modes**: 에이전트의 행동 모드 커스터마이징
- **Instructions**: 프로젝트별·파일별 지시사항
- **Prompts**: 재사용 가능한 프롬프트 템플릿
- **MCP**: 외부 도구·데이터 연결

## 가장 흥미로운 지점

Vibe Coding 카테고리의 마지막 영상으로, 개인이 아닌 조직·규모 차원을 추가한다. 다만 governance/compliance/audit 등 전통적 엔터프라이즈 차원은 미다룸.

## 출처

**Harald Kirshner (VS Code)**
원문: <https://www.youtube.com/watch?v=i1uPAN6uW4s>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
