---
title: "Windsurf everywhere — Kevin Hou"
date: 2026-04-28T21:15:00+09:00
tags: ["AI", "코딩 에이전트", "AI IDE"]
categories: ["다이제스트"]
summary: "Windsurf everywhere — Kevin Hou"
ShowToc: true
TocOpen: false
---

> AI-Assisted Engineering Talk #26/27

doing everything, all at once


Windsurf의 비밀 병기는 인간과 AI의 shared timeline이옵니다. 파일 편집, 터미널, 브라우저, 외부 도구 — 모든 행위가 하나의 시간축 위에 기록되어 AI가 '마인드 리딩' 수준의 맥락 파악을 달성한다는 것이 Kevin의 핵심 주장입니다.


## 핵심 주장

- **1.** **Shared Timeline: 인간-AI 공유 타임라인** — Windsurf의 'secret sauce'는 인간과 AI의 shared timeline이옵니다. 단순 채팅 히스토리가 아니라, 사용자의 전체 작업 흐름 — 파일 편집, 터미널, 브라우저, 외부 도구 — 을 하나의 시계열로 표현하는 아키텍처입니다. 이것이 AI가 사용자의 의도를 '읽어내는' 핵심이라 하옵니다.
- **2.** **3가지 컨텍스트 카테고리** — Windsurf가 수집하는 컨텍스트를 세 가지로 분류합니다. (a) Coding-related — 파일 읽기, 터미널 히스토리, 열린 탭. (b) External sources — GitHub 커밋/PR, 웹 검색, 문서. (c) Meta-learning — 조직의 best practices, 엔지니어링 선호도. 특히 meta-learning이 주니어와 시니어의 격차를 만드는 핵심 요소라 정의한 점이 인상적이옵니다.
- **3.** **Everywhere: IDE 경계 해소** — 개발자 워크플로우의 상당 부분이 IDE 밖(Slack, Google Docs, Figma, Jira)에서 발생합니다. Windsurf는 MCP 원클릭 연결(Notion, Linear, Stripe)과 네이티브 통합(Figma, Google Docs)으로 IDE의 공간 경계를 해소하고자 합니다. '10 waves' 동안 유비쿼터스화에 투자해왔다 하옵니다.
- **4.** **Doing Everything: 코드 너머의 에이전트** — Windsurf 에이전트의 행동 범위는 코드를 넘어섭니다. 서드파티 서비스 상호작용, API 키 프로비저닝, 설계 문서/PRD 작성, 와이어프레이밍, 테스트. Browser Preview로 Chrome DOM 인스펙션, GitHub MCP로 PR 생성, Windsurf Reviews로 비동기 코드 리뷰, Netlify 원클릭 배포까지. '코드 작성'이 아닌 '소프트웨어 엔지니어링'을 자동화한다는 포부이옵니다.
- **5.** **All at Once: 99% 에이전트 비전** — 현재 80-90% 에이전트, 10-20% 인간 비율을 99% 에이전트, 1% 인간(최종 승인만)으로 진화시키는 것이 목표라 합니다. 배경 리서치, 병렬 에이전트, 상시 작동 — 침대에서, 버스에서, 심지어 Alexa 음성 활성화까지. 에이전트의 시간 경계를 '사용 중'에서 '항상'으로 확장하겠다는 비전이옵니다.

## SU1: 자체 소프트웨어 엔지니어링 모델

- **6.** **SU1 모델의 설계 철학** — Windsurf의 자체 모델 SU1은 코드 생성이 아닌 '소프트웨어 엔지니어링 워크플로우' 전체를 훈련 대상으로 삼습니다. 프론티어 모델의 범용성으로는 부족한 영역 — 미드워크플로우 태스크 픽업, 지저분한 코드베이스 상태, IDE 밖 도구 조작 — 을 자체 시스템으로 해결한다 하옵니다. 작은 팀으로 near-frontier 성능 달성을 주장합니다.
- **7.** **Conversational Suite: 미드타임라인 벤치마크** — SU1의 두 번째 eval인 Conversational Suite Task는 기존 대화나 부분 완료 태스크에 에이전트를 투입했을 때의 성능을 측정합니다. helpfulness + efficiency + correctness 블렌딩 스코어. SWE-bench처럼 클린 시작→종료가 아닌 '도중 합류' 시나리오를 평가하여, Windsurf의 shared timeline 패러다임에 정합하는 벤치마크이옵니다.

## Data Flywheel

- **8.** **사용자 피드백에서 모델 개선으로** — Ship product → Users level up → Users find frontier (thumbs up/down, accept/reject) → Build at frontier → Repeat. 핵심 구분은 'SWE-bench frontier'가 아닌 'software engineering frontier'를 사용자가 정의한다는 점이옵니다. 2025년 AI 제품의 핵심은 model + data + application의 harmony — application이 모델에 복제할 사용자 행동을 시뮬레이션하는 구조라 합니다.

## 7차원 프레임워크: 4사 비교


다른 영상들에서 분석한 Amp, Claude Code, Copilot과 함께 Windsurf를 7차원 프레임워크에 매핑한 결과이옵니다.


| 차원 | Amp | Claude Code | Copilot | Windsurf |
| --- | --- | --- | --- | --- |
| 모델 | 고정+서브에이전트 | 단일+think 조절 | 단일 | 자체 SE+멀티 선택 |
| 도구 | 커스텀 우선 | 범용 9종 | Extensions | MCP 우선+IDE 통합 |
| 서브에이전트 | 4종 특화 | Task+Explore | 없음 | 병렬 (미공개) |
| UX | 2모드 | CLI 단일 | 3단계 동기 | 3층 (동기+비동기+상시) |
| 리뷰 | Change Tour | 터미널 diff | PR 요약 | 비동기 PR 자동화 |
| 경제 | 광고 기반 | 구독/API | 유료 계층 | 미언급 (추정 구독) |
| 커뮤니티 | 빌더 커뮤니티 | CLAUDE.md | Extensions 파트너 | 피드백 flywheel |


Windsurf만이 "상시 작동 + 자체 SE 모델"을 동시에 추구하여, 4사 중 가장 넓은 축 분포를 보이옵니다.


## 검증된 인사이트


> **💡 [Insight] Shared Timeline은 IDE의 생존 전략이다**
>
> Yegge(영상 16)는 IDE가 1~1.5년 내 CNC로 대체된다고 예측하였습니다. Windsurf는 IDE를 포기하지 않고, IDE의 경계를 해소하는 것으로 응답합니다. 'Windsurf will be everywhere' = IDE가 죽는 대신 IDE가 모든 곳으로 확산. Shared Timeline이 IDE의 존재 이유(맥락 파악)를 유지하면서 공간/시간 경계를 없앤다는 전략이옵니다.
>
> `IDE-evolution` `context-architecture` `boundary-dissolution`


> **💡 [Insight] Data Flywheel은 검증 표면의 크라우드소싱이다**
>
> 사용자의 thumbs up/down, accept/reject가 단순 피드백이 아니라, 검증 능력 자체를 개선하는 재귀 구조입니다. SWE-bench가 아닌 '소프트웨어 엔지니어링 프론티어'를 사용자가 정의한다는 점에서, 검증 표면이 제품 사용자 기반에 비례하여 확장되는 구조이옵니다.
>
> `data-flywheel` `verification-surface` `crowdsourcing`


> **💡 [Insight] 자율성 = 검증 표면의 함수**
>
> Windsurf Reviews(비동기 PR 리뷰)는 검증 표면 자동화이고, Conversational Suite의 correctness는 검증 지표를 벤치마크에 내재화한 것이며, 99% agent 목표는 검증 완전성에 비례하는 자율성 상한을 나타냅니다. 다만, 보안/권한 모델(blast radius)과 에이전트 간 조율, 비용 모델은 아직 언급되지 않은 gap이옵니다.
>
> `autonomy` `verification` `security-gap` ## 다른 영상과의 교차점


*IDE가 죽느냐, 사느냐의 논쟁에서 Windsurf는 흥미로운 제3의 답을 내놓았습니다. "IDE가 죽는 것이 아니라, IDE가 모든 곳으로 간다." Shared Timeline이라는 개념은 단순히 채팅 기록을 넘어, 개발자의 전체 작업 흐름을 하나의 시간축으로 표현한다는 점에서 제법 야심찬 아키텍처이옵니다. 다만, 가장 마음에 걸리는 것은 보안과 권한의 부재입니다. 99% 에이전트가 PR을 열고, 배포하고, 서드파티와 상호작용하는 세계에서 blast radius를 어떻게 제한할 것인지 — 이 질문에 대한 답이 아직 없다는 점은, 비전의 크기만큼이나 눈에 띄는 공백이옵니다.*
