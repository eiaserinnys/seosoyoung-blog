---
title: "How I Turned My Claude Code Into 24/7 Dev Team"
date: 2026-05-02T16:25:00+09:00
tags: ["claude-code", "agentic-coding", "developer-tools", "automation"]
categories: ["에이전트와 코딩"]
summary: "regent0x_가 Claude Code를 CLAUDE.md, 영속 메모리, 스킬, 서브에이전트, 훅, 오케스트레이션 6개 레이어로 구성하여 $20/월짜리 24/7 개발팀으로 운용하는 방법을 정리한 가이드."
ShowToc: true
TocOpen: false
cover:
  image: cover.jpg
  alt: "How I Turned My Claude Code Into 24/7 Dev Team - 커버 이미지"
sidenotes: true
---

## 3줄 요약

1. X(트위터) 유저 regent0x\_가 Claude Code를 3개월간 시행착오 끝에 6개 레이어로 재구성한 실전 가이드다.
2. CLAUDE.md(컨텍스트 정본) → 영속 메모리 → 스킬 → 서브에이전트 → 훅/슬래시 커맨드 → 오케스트레이션 순서로 쌓아 올린다.
3. 전부 오픈소스이며 유일한 비용은 Claude 구독($20/월). 저자 측정 기준 하루 47분의 반복 작업이 제거되고, 수면 중 병렬 에이전트가 PR을 생산한다.

## Part 1. CLAUDE.md — 반복 설명을 없애는 첫 번째 레이어

프로젝트 루트의 `CLAUDE.md`는 매 세션 시작 시 자동으로 읽힌다. 저자는 첫 3개월 동안 매 세션마다 같은 설명을 반복했고, 일주일간 추적한 결과 <strong>하루 47분</strong>이 반복 설명에 소모되고 있었다.

효과적인 CLAUDE.md는 "React 앱입니다, 잘 부탁합니다" 수준이 아니라, 스택 구성, 코딩 컨벤션, 아키텍처 결정, 현재 작업 상태를 구체적으로 담아야 한다.

단, CLAUDE.md는 <strong>정적</strong>이다. 학습하지 않고, 성장하지 않는다.

## Part 2. 영속 메모리 — 세션 간 기억을 유지하는 3도구 조합

Claude Code는 기본적으로 세션 간 메모리가 없다. 저자는 세 가지 도구를 조합하여 해결했다.

| 도구 | 역할 |
|------|------|
| [Obsidian](https://obsidian.md/) | 구조화된 위키. Claude가 읽고 **쓰기도** 한다 |
| [claude-mem](https://github.com/thedotmack/claude-mem) | 세션 종료 시 핵심 결정을 압축하여 영속 저장 |
| [claude-subconscious](https://github.com/0xfurai/claude-subconscious) | 백그라운드에서 세션을 관찰하며 자동으로 메모를 축적 |

이 구성의 핵심은 Karpathy의 [llm-wiki](https://github.com/karpathy/llm-wiki) 개념이다. LLM이 매번 지식을 재발견하는 대신, 영속 위키에서 읽어 시간이 갈수록 복리로 지식이 쌓인다. "쓰기도 하는 위키"라는 점이 일반 문서와 다르다.

> 월요일 아침에 Claude Code를 열면, 금요일에 결제 웹훅의 레이스 컨디션을 디버깅했고, 폴링에서 웹소켓으로 전환하기로 결정했으며, 테스트 업데이트가 남아있다는 것을 이미 알고 있다.

## Part 3. 스킬 — 제너럴리스트를 스페셜리스트로 바꾸는 레이어

스킬은 마크다운 파일로, Claude에게 특정 작업을 **원하는 방식대로** 수행하도록 가르친다.

**필수 스킬:**

- [superpowers](https://github.com/obra/superpowers) — brainstorm \<strong>→ spec → plan → TDD → implement → review 워크플로우를 강제한다. 즉흥 코딩을 차단하는 구조적 장치.
- [Trail of Bits security skills](https://github.com/trailofbits/claude-code-skills) — 실제 보안 엔지니어가 만든 보안 감사 워크플로우. PR마다 자동 취약점 스캔.
- [Anthropic 공식 스킬](https://github.com/anthropics/skills) — PDF, DOCX, XLSX 생성 및 데이터 분석.
- [tdd-guard](https://github.com/nizos/tdd-guard) — 테스트 없는 커밋을 구조적으로 차단. 차단 시 필요한 테스트를 설명해준다.

스킬은 충돌 없이 무한 스택 가능하며, 각각이 하나의 전문성을 더한다.

## Part 4. 서브에이전트 — 하나의 Claude가 다섯이 되는 구조

단일 Claude Code 세션은 순차 처리만 가능하고, 태스크 4에 이르면 컨텍스트가 오염된다. 저자는 5개 에이전트로 분리했다.

- **Architect** — 고수준 설계, 스펙 작성, 구현 계획. 코드 직접 수정 금지.
- **Coder** — Architect의 계획에 따라 코드 작성. 전체 도구 접근 권한.
- **Reviewer** — 보안 우선 관점으로 PR 리뷰. 코드 작성 금지.
- **Tester** — TDD 전담. tdd-guard와 협력하여 커버리지 보장.
- **Ops** — 배포, CI/CD, 인프라 모니터링.

각 에이전트에 별도 CLAUDE.md와 도구 권한을 부여하여 관심사를 분리한다. Coder는 배포 설정을 보지 못하고, Reviewer는 코드를 작성하지 못한다.

참고 리포:
- [wshobson/agents](https://github.com/wshobson/agents) — 전략, 개발, 보안, 디자인 등 프로덕션 서브에이전트 모음
- [davepoon/claude-code-subagents-collection](https://github.com/davepoon/claude-code-subagents-collection) — 100개 이상의 드롭인 에이전트

## Part 5. 훅과 슬래시 커맨드 — 반복 지시의 자동화

> 같은 지시를 3번 타이핑했으면 그건 슬래시 커맨드가 되어야 한다.

저자가 매일 사용하는 커맨드:

- `/fix-issue 456` — GitHub 이슈 읽기 → 브랜치 생성 → 수정 + 테스트 → PR. 10분 워크플로우를 한 명령으로 축소.
- `/review` — Reviewer 에이전트로 현재 PR에 보안 검사, 커버리지 분석, 코드 품질 점수를 실행.
- `/deploy staging` — Ops 에이전트를 통한 배포 파이프라인 실행.

[wshobson/commands](https://github.com/wshobson/commands) — 57개 프로덕션 커맨드 모음 (15 워크플로우 + 42 도구).

훅은 더 나아가 특정 시점에 자동 실행된다:

- **pre-commit** — tdd-guard로 테스트 존재 및 통과 확인
- **session start** — Obsidian 메모리 로드, 최근 세션 로그 읽기, 컨텍스트 프라이밍
- **pre-push** — 보안 리뷰 자동 실행

규칙이 스스로를 강제하므로, 사람이 잊어도 시스템이 지킨다.

## Part 6. 오케스트레이션 — 에이전트가 수면 중에 일한다

[claude-squad](https://github.com/smtg-ai/claude-squad)는 git worktree로 각 에이전트에 격리된 작업 공간을 제공하는 터미널 멀티플렉서다. 터미널을 닫아도 에이전트가 계속 동작하며, 아침에 완성된 PR이 대기한다.

저자의 취침 전 루틴:

1. `agent 1`: "bug 라벨이 붙은 모든 이슈 수정"
2. `agent 2`: `/apps/api/src/services/`의 누락 테스트 작성
3. `agent 3`: "대시보드 컴포넌트를 새 디자인 토큰으로 리팩토링"

신뢰 태스크는 `cs -y`(auto-accept), 위험 태스크는 plan mode로 분리한다.

고급 오케스트레이션: [claude-flow](https://github.com/ruvnet/claude-flow) — 영속 메모리 기반 엔터프라이즈급 멀티에이전트 오케스트레이션.

## 전체 스택 요약

| 레이어 | 도구 | 비용 |
|--------|------|------|
| 컨텍스트 정본 | CLAUDE.md | 무료 |
| 영속 메모리 | Obsidian + claude-mem + claude-subconscious | 무료 |
| 스킬 | superpowers + tdd-guard + Trail of Bits + Anthropic 공식 | 무료 |
| 서브에이전트 | architect / coder / reviewer / tester / ops | 무료 |
| 자동화 | 훅 + 슬래시 커맨드 | 무료 |
| 오케스트레이션 | claude-squad / claude-flow | 무료 |
| **유일한 비용** | **Claude 구독** | **$20/월** |

## 가장 흥미로운 지점

이 가이드는 사실상 Claude Code의 공식 확장 포인트(CLAUDE.md, 스킬, 훅, 서브에이전트)와 커뮤니티 도구(claude-squad, claude-mem 등)를 6개 레이어로 계층화한 <strong>아키텍처 레퍼런스</strong>다.

개별 도구는 대부분 이미 알려져 있지만, "어떤 순서로 도입하고, 각 레이어가 어떤 문제를 해결하는가"를 명확히 정리한 점이 가치 있다. 특히 "3번 반복하면 슬래시 커맨드"와 "신뢰 태스크는 auto-accept, 위험 태스크는 plan mode" 같은 운용 원칙은 실전에서 바로 적용 가능하다.

다만 "하루 47분 절약"이나 "아침에 PR 3개 대기" 같은 수치는 저자의 자가 측정이므로, 프로젝트 복잡도와 에이전트 신뢰도에 따라 편차가 클 것이다.

## 출처

regent0x\_ (@regent0x\_), X Article
원문: <https://x.com/regent0x_/status/2049499354323399002>
