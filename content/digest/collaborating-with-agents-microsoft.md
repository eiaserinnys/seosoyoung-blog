---
title: "Collaborating with Agents in your Software Dev Workflow — 다이제스트"
date: 2026-04-29T04:42:00+09:00
tags: ["GitHub Copilot", "에이전트 격리", "DevOps"]
categories: ["다이제스트"]
summary: "GitHub 개발자 애드보킷들이 Copilot의 6중 격리 아키텍처와, AI가 DevOps 흐름을 바꾸지 않는다는 원칙을 워크숍에서 시연한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Christopher Harrison & John Peck(GitHub Developer Advocates)이 진행한 GitHub Copilot 핸즈온 워크숍.
2. Copilot은 'AI 페어 프로그래머'이며 코드를 읽기 때문에 코드베이스 가독성이 곧 컨텍스트 품질이다.
3. Coding agent는 6중 격리로 인간 검증 전 진입을 원천 차단하며, AI는 DevOps flow를 바꾸지 않는다.

## 6중 격리 아키텍처

코딩 에이전트의 안전 장치:

- Firewall — 네트워크 격리
- Ephemeral — 일회용 실행 환경
- Branch-only-write — 메인 직접 수정 불가
- Draft-PR — 자동 머지 금지
- Gated-CI — CI 통과 필수
- No-self-review — 자기 코드 자기 승인 불가

## copilot-instructions.md

입력측 검증 자산으로서의 역할:

- `copilot-instructions.md`와 `.instructions(applyTo glob)`으로 컨텍스트 커스터마이징
- 우선순위에 last-writer-wins가 없으므로 *일관성*이 곧 시스템 속성
- 리뷰·린터·보안 스캔·테스트는 AI 시대에도 그대로 필수

## 가장 흥미로운 지점

"AI는 DevOps flow를 바꾸지 않는다"는 선언이 인상적이다. 에이전트가 아무리 발전해도 검증 인프라의 필요성은 변하지 않는다는 보수적이지만 현실적인 관점이다.

## 출처

**Jon Peck & Christopher Harrison (Microsoft/GitHub)**
원문: <https://www.youtube.com/watch?v=G1hhmz6mXT0>
시리즈: [AI 코딩 도구의 검증 표면 — 27편의 발표에서 배운 것]({{< ref "/posts/verification-surface-27-talks" >}})
