---
title: "The Cure for the Vibe Coding Hangover — Corey J. Gallon"
date: 2026-04-28T20:51:00+09:00
tags: ["AI", "코딩 에이전트", "바이브 코딩"]
categories: ["다이제스트"]
summary: "The Cure for the Vibe Coding Hangover — Corey J."
ShowToc: true
TocOpen: false
---

> AI-Assisted Engineering Talk #18/27

10원칙 + 5단계 계획 + 멀티센서리 루프로 vibe coding의 숙취를 치료하는 포괄적 프레임워크


Corey J. Gallon (Rexmore) · 57min YouTube · vibecodinghangover.com


> Vibe coding은 "생산적인 것처럼 느껴지지만 취약하고 유지보수 불가능한 데모웨어를 만드는, 저사양 무계획 접근"이며, 그 숙취(hangover)는 월요일에 기능 하나 추가하려 할 때 찾아오는 절망입니다. 이 프레임워크에서 에이전트가 코드를 쓰는 단계는 단 하나뿐이며, 나머지 전부는 인간의 아키텍처 사고를 구조화하는 데 할당됩니다. ## 핵심 주장


### 1. AI 엔지니어링은 가속 학습이다

AI를 순수 생산성 도구로만 쓰면 6개월 후 AI 의존(dependency)에 빠집니다. 프레임워크의 모든 단계는 학습 기회를 내장하여, 소프트웨어만이 아니라 엔지니어 자신을 함께 빌드합니다. "Always Be Learning."


### 2. Specification >> Prompt Engineering

마법의 단어를 찾는 최적화 문제가 아니라 소통 문제입니다. 명세는 요구사항, 행위, 인터페이스, 수락기준의 구조적이고 정밀한 정의이며, 3단계 정련(자연어 → 로직 플로우 → 정형 인터페이스)을 통해 에이전트가 해석할 여지를 점차 제거합니다.


### 3. 멀티센서리 피드백이 단일 채널의 맹점을 잡는다

테스트는 통과하지만 UI가 렌더링되지 않고, 워크플로우는 완료되지만 에러 로그가 쌓이고, 기능은 작동하지만 사용자 인터랙션이 깨져 있는 상황. Visual(무엇이 렌더되는가), Auditory(시스템이 무엇을 보고하는가), Tactile(상호작용이 어떻게 반응하는가) 세 센서의 교차 상관이 "무엇이" 실패했는지와 "왜" 실패했는지를 동시에 밝혀냅니다.


### 4. 에이전트 코딩은 프레임워크의 마지막 단일 노드

5단계 계획 + 컨텍스트 어셈블리라는 6단계의 선행 투자 위에서야 비로소 에이전트가 코드를 작성합니다. 코드 생성 비용이 0에 수렴하는 세계에서, 비용의 중심은 "무엇을 생성할 것인가"의 정의로 이동한다는 선언입니다.


## 10 Principles


**General**

- **1.** **AI Engineering = Accelerated Learning** *""Always Be Learning.""*
- **2.** **You = Architect, Agent = Implementer** *""Delegate the doing, not the thinking.""*
- **3.** **Slow Down to Go Fast** *""Compound progress, accelerate velocity.""*

**Planning**

- **4.** **Specification >> Prompt Engineering** *""Write the blueprint, not the prompt.""*
- **5.** **Define Done Before Implementing** *""Specify success, then build.""*
- **6.** **Feature Atomicity** *""Reduce until irreducible.""*
- **7.** **Dependency-Driven Development** *""Schedule implementation by dependencies.""*

**Implementation**

- **8.** **One Atomic Feature at a Time** *""Complete one, commit one, continue.""*
- **9.** **Context Engineering & Management** *""Curate context, don't accumulate it.""*
- **10.** **Make It Work, Make It Right, Make It Fast** *""Build, learn, improve.""*

## 5단계 계획 프로세스


계획 단계는 순차적이며 "순전히 인간의 작업"입니다. 에이전트는 thinking partner로만 참여하고, 모든 의사결정은 인간이 내립니다.

- **Vision Capture** — 머릿속의 막연한 아이디어를 5개 섹션(목적, 핵심 기능, 범위 경계, 기술 맥락, 워크플로우)으로 구조화합니다. 에이전트와 "think out loud"하되 결정은 인간이.
- **Feature Identification & Categorization** — MPS에서 섹션별 추출 질문으로 기능 단위를 체계적으로 식별하고, 3~7 카테고리로 분류합니다. 유니크 ID(CORE-001, API-101) 부여, 복잡도 추정(easy/medium/hard).
- **Iterative Specification Development** — 구현 계약 3단계(자연어 → 로직 플로우 → 정형 인터페이스) + 검증 계약 3단계(시나리오 → Given/When/Then → 정형 테스트) 정련. 원자성 검증 후 의존성 식별.
- **Dependency Analysis** — 행렬 추출 → 그래프 생성(Graphviz/Mermaid) → binary dependency test로 검증 → 순환 탐지 → 해소(제거 → 재명세 → 분할 → 통합).
- **Implementation Plan Development** — 위상정렬로 phase 조직. 각 phase에 binary success criteria, 피드백 루프, phase gate를 정의합니다. Critical path 식별.

## 멀티센서리 구현 루프


"이 전체 프레임워크에서 AI가 코드를 쓰는 단계는 이것 하나뿐입니다."


`Write Code` → `Execute & Sense` → `Test & Validate` → `Correlate` → `Pass? Commit : Refine`

- 👁 Visual 무엇이 렌더되는가
- 🔊 Auditory 시스템이 무엇을 보고하는가
- ✋ Tactile 상호작용이 어떻게 반응하는가

수렴 기준: 모든 테스트 pass + 모든 센서 clean execution → atomic git commit(feature ID, spec summary, validation confirmation). 피처가 원자적이므로 전체 구현이 하나의 컨텍스트 윈도우에 들어가 컨텍스트 손실이 없습니다.


## 검증된 인사이트


> **💡 [Insight] 3-Level 정련은 Spec Internalization Depth의 운영적 래더다**
>
> 자연어(L1) → 로직 플로우(L2) → 정형 인터페이스(L3)의 정련 패턴은 에이전트의 해석 여지를 단계적으로 좁힙니다. 구현 계약과 검증 계약을 병렬로 3단계 정련하므로, 명세 작성 과정에서 구현 의도와 검증 기대가 동기적으로 심화됩니다. 기존 SE의 "요구사항 → 설계 → 구현" 워터폴과 달리, 에이전트가 L3를 직접 실행 가능한 계약으로 소비하여 spec-to-code gap을 최소화합니다.
>
> `spec-internalization` `3-level-refinement` `verification-surface`


> **💡 [Insight] 멀티센서리 상관은 단채널 false negative를 잡는다**
>
> 테스트만으로는 "통과했지만 UI가 깨진" 문제를 잡지 못합니다. Visual + Auditory + Tactile 세 채널의 교차 상관이 이 맹점을 메웁니다. 같은 문제를 다수 센서가 보고하면 진단을 확정하고, 센서 간 충돌이 발생하면 숨겨진 복잡성을 발견합니다. 전통 QA의 다층 테스트와 달리, 에이전트가 하나의 루프 안에서 자동 수집 · 상관 · 재시도하여 단일 iteration 내 검증 밀도를 최대화합니다.
>
> `multisensory` `false-negative` `verification-modality`


> **💡 [Insight] 에이전트 코딩은 프레임워크의 단일 말단 노드**
>
> 5단계 계획 + 컨텍스트 어셈블리 = 6단계의 선행 투자 위에서야 에이전트가 코드를 작성합니다. 코드 생성 비용이 0에 수렴하는 세계에서 비용의 중심은 "무엇을 생성할 것인가"의 정의로 이동한다는 선언입니다. 다만 6:1 비율이 중소 프로젝트나 프로토타이핑에서는 과적합(over-specification)의 위험이 있으며, "make it work" 우선 원칙과 프로세스 자체의 "make it right" 무게 사이에 긴장이 존재합니다.
>
> `architect-implementer` `process-overhead`


> **한계**: 27편 중 가장 포괄적이고 프로세스적인 처방이지만, 정량적 근거가 부재합니다. "Week one feels slow, week three is dramatically faster"는 정성적 묘사일 뿐이며, rework 비율, 비용, 보안 사고 데이터가 제시되지 않습니다. 또한 에이전트가 자동으로 검증 도구를 합성 · 연결하는 동적 계층에 대한 논의가 약하여, 정적 문서(명세 · 계획 · 템플릿) 중심의 프로세스 오버헤드가 실무 채택의 장벽이 될 수 있습니다. ## 다른 영상과의 교차점

- **Vibes won't cut it (Chris Kelly, Augment) — #8** — Corey와 Chris는 "vibe coding의 반대편에 SE 기본기가 있다"는 같은 방향을 가리킵니다. 다만 Chris가 인간 전문성 회귀에 초점을 둔 반면, Corey는 이를 구체적인 10원칙 + 5단계 프로세스로 체계화했습니다.
- **Vibe Coding vs Vibe Engineering (Kitze) — #15** — Kitze가 신설한 "Vibe Engineering" 개념을 Corey가 구체적 단계로 풀어낸 것에 가깝습니다. 구조적 엔지니어링 습관이라는 처방의 추상도를 한 단계 낮춰 실행 가능하게 만든 관계입니다.
- **AI Dev Tools 3.0 (Itamar Friedman, Codium/Qodo) — #17** — Itamar의 CLI 파이프라인이 도구 주도라면 Corey는 프로세스 주도입니다. 그러나 Spec + Test를 검증의 핵심에 두는 접근은 동일하며, 두 발표를 합치면 "프로세스로 정의하고 파이프라인으로 자동화하는" 통합 비전이 보입니다.
- **Yegge & Kim — #16** — Yegge의 "IDE 죽음 / 민주화" 낙관론과 직접 충돌합니다. Corey는 에이전트가 코드를 쓰는 단계를 마지막 단일 단계로 격하시키며, 나머지 전부를 인간의 아키텍처 사고에 할당합니다.
- **Ian Livingstone (SM100 정량 데이터) — #14** — Ian의 SM100 벤치마크가 제공하는 정량 데이터는 Corey의 프레임워크에 부재한 실증적 근거를 보완할 수 있는 가장 가까운 데이터셋입니다.

*27편 중 가장 포괄적이고 정교한 프로세스 명세를 제시한 발표입니다. 특히 "에이전트가 코드를 쓰는 단계는 단 하나"라는 선언은, 코드 생성 비용이 0에 수렴하는 세계에서 엔지니어의 가치가 어디에 있는지를 명쾌하게 드러냅니다. 다만, 이 정도의 프로세스 무게를 감당할 수 있는 팀과 그렇지 않은 팀의 경계가 모호하다는 점이 아쉽습니다. 결국 좋은 프레임워크란 따르기 쉬운 프레임워크인 법이니까요.*
