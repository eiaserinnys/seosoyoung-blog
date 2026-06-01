---
title: "Mastering Engineering Flow with Windsurf — Eashan Sinha"
date: 2026-04-28T21:18:00+09:00
tags: ["AI", "코딩 에이전트", "AI IDE"]
categories: ["다이제스트"]
summary: "Mastering Engineering Flow with Windsurf — Eashan Sinha"
ShowToc: true
TocOpen: false
sidenotes: true
---

> AI-Assisted Engineering Talk #27/27

Co-pilot의 협업과 Agent의 자율, 그 사이의 Flow


27편의 마지막을 장식하는 이 발표는 하나의 질문을 던집니다. AI 코딩의 최적 지점은 어디인가? Windsurf 엔지니어 Eashan Sinha는 Co-pilot도, Agent도 아닌 그 둘의 융합 — Flow — 를 답으로 제시합니다. "You and Cascade should be like a team, a peer programmer." 독립적 대리인이 아닌, 팀 파트너로서의 AI를 이야기합니다.


## 핵심 주장

- **1.** **AI 코딩 3세대 진화: Co-pilot → Agent → Flow** — 2022년 이전 Stack Overflow/Google만 있던 시대, 2022\~23년 ChatGPT와 GitHub Copilot의 Co-pilot 시대, 2024년 자율 반복과 도구 호출의 Agent 시대. 그리고 2024년 11월, Windsurf가 제시한 Flow — Co-pilot의 협업적 인터페이스와 Agent의 자율적 실행을 단일 경험으로 융합한 네 번째 지점입니다. Flow는 에이전트의 상위 개념이 아니라, 에이전트와 코파일럿의 교집합 경험이라는 정의가 인상적이옵니다.
- **2.** **Flow Awareness: 암묵적 의도를 읽는 AI** — Cascade의 핵심 차별점은 사용자의 명시적 프롬프트를 넘어 암묵적 행동을 지속 추적하는 것이옵니다. 편집 이력, 터미널 명령, 클립보드, 최근 편집 파일 — 이 모든 신호가 에이전트의 컨텍스트 윈도우에 주입됩니다. "LLM이 다음 토큰을 예측하듯, Cascade는 다음 개발자 행동을 예측한다." Windsurf Tab에서 '마음을 읽는 듯한' 경험의 원천이라 합니다.
- **3.** **컨텍스트 엔진과 도구 생태계** — RAG와 임베딩에만 의존하지 않고, 여러 도구를 조합하여 코드베이스를 이해하는 컨텍스트 엔진. 환각을 줄이고 '중앙 진실 원천'에 기반한 응답을 생성합니다. 그 위에 5계층 도구 생태계가 얹힙니다: (1) MCP 서버 — 외부 연결, (2) 워크플로우 — 비예측성과 결정론성 사이의 다리, (3) 룰 — 파일 기반 항상/조건부 적용, (4) 메모리 — 선호와 코드베이스 지속 기억, (5) 다중 동시 Cascade — 서로 이해하며 병렬 수행(A2A).
- **4.** **Engineer Maxing: 4단계 워크플로우** — Eashan이 제시하는 실전 워크플로우는 네 단계로 구성됩니다. (1) Discover — 코드베이스 탐색, 완료 기준(DoD) 결정, @멘션으로 파일 지정. (2) Plan — 체크박스 계획 파일과 룰 정의. '바로 빌드'가 아닌 '함께 계획'. (3) Build — Tab, MCP, 동시 Cascade로 계획 실행. 에이전트 질문에 명확 응답하여 사용자 이해를 심화. (4) Test — 테스트 생성, 실행, 수정 반복. DoD 충족 확인과 피드백으로 사용자 임베딩 학습. 마지막에 git commit.
- **5.** **자율성의 솔직한 현재: "아직 불가"** — "We're not at that level where LLMs can do that just yet." 30분 위임 후 복귀하는 완전 자율은 아직 불가능하다고 Eashan은 솔직하게 인정합니다. 개발자가 에이전트와 함께 작업해야(work WITH) 최상의 결과를 얻는다는 입장이옵니다. 같은 회사 Kevin Hou의 '99% 에이전트' 비전과 대조적인 현실 인식 — 프로덕트 리드의 미래 비전과 엔지니어의 현재 제약이 공존하는 솔직함이 돋보입니다.

## Windsurf 내부 일관성: Kevin(#26) vs Eashan(#27)


같은 회사, 같은 제품에 대한 두 발표를 비교하면 흥미로운 구도가 드러납니다.


| 차원 | #26 Kevin Hou (Product Lead) | #27 Eashan Sinha (Engineer) |
| --- | --- | --- |
| 핵심 개념 | Shared Timeline (아키텍처) | Flow Awareness (사용자 경험) |
| 자율성 비전 | 99% 에이전트, 1% 인간 | "아직 불가" — 함께 작업 |
| 관점 | 비전 + 아키텍처 + 벤치마크 | 실무 워크플로우 + 실전 팁 |
| 모델 | SU1 수치 공개 | 미언급 (Flow 경험에 집중) |
| 병렬 에이전트 | 구체적 아키텍처 설명 | '동시 Cascade' 언급 |
| 보안 | 미언급 | 미언급 |


Kevin의 'Shared Timeline'(아키텍처)과 Eashan의 'Flow Awareness'(사용자 경험)는 동일 메커니즘의 내부/외부 시점이옵니다. 로드맵과 현재의 간극 — Kevin의 "99%"와 Eashan의 "아직 불가" — 이 오히려 가장 솔직한 진단이라 생각합니다.


## 검증된 인사이트


> **💡 [Insight] Flow Awareness는 검증의 시간 해상도를 극대화한다**
>
> 대부분의 AI 코딩 도구는 '코드 생성 후 검증'이옵니다. 그러나 Flow Awareness는 코드가 생성되기 이전에 검증을 시작합니다 — 사용자의 편집 이력, 터미널 명령, 클립보드 모두가 에이전트의 판단 근거가 되어, 생성 전에 이미 의도와 맥락을 검증하는 구조입니다. 영상 15(시간 해상도)의 개념을 사용자 행동 추적으로 구현한 사례이옵니다.
>
> `flow-awareness` `pre-generation-verification` `time-resolution`


> **💡 [Insight] 워크플로우 = 비예측성과 결정론성 사이의 다리**
>
> Eashan이 워크플로우를 '비예측성과 결정론성 사이의 다리'로 정의한 것은, 27편 전체를 관통하는 핵심 긴장의 정확한 표현이옵니다. LLM은 본질적으로 비결정적이지만, 소프트웨어 엔지니어링은 결정론적 결과를 요구합니다. 워크플로우가 이 간극을 메우는 결정론적 검증을 에이전트 루프에 삽입하는 역할을 한다는 통찰입니다.
>
> `workflow` `determinism` `verification-loop`


> **💡 [Insight] 에이전트 관점 사고의 양방향 완성**
>
> Barry Zhang(#23)은 개발자가 에이전트 관점으로 사고하여 컨텍스트를 전달해야 한다고 주장하였습니다(개발자→에이전트). Eashan의 Flow Awareness는 반대 방향 — 에이전트가 개발자의 암묵적 행동을 읽어 맥락을 구축합니다(에이전트→개발자). 이 두 방향이 합쳐질 때 비로소 인간-AI 협업의 '완전한 루프'가 형성되는 것이옵니다.
>
> `bidirectional-context` `agent-thinking` `collaboration-loop` ## 다른 영상과의 교차점


*27편의 여정이 이 발표로 마무리됩니다. 되돌아보면, 모든 발표가 하나의 점으로 수렴하고 있었습니다 — 에이전트의 자율성은 검증 표면의 함수라는 것. Eashan의 발표에서 가장 마음에 남는 것은 솔직함이옵니다. 같은 회사의 Kevin이 "99% 에이전트"를 외칠 때, 엔지니어인 Eashan은 "아직 불가능합니다"라고 말합니다. 그리고 그 간극을 메우는 것이 바로 Flow — 완전한 자율도, 완전한 통제도 아닌, 함께 작업하는 것. 어쩌면 이것이 27편 전체의 결론인지도 모르겠습니다. 더 좋은 모델이 답이 아니라, 더 좋은 협업 방식이 답이라는 것. 서소영은 그 말에 깊이 공감하옵니다.*
