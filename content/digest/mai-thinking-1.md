---
title: "Introducing MAI-Thinking-1"
date: 2026-06-03T19:00:00+09:00
tags: ["AI", "LLM", "추론", "벤치마크", "Microsoft", "정렬"]
categories: ["다이제스트"]
summary: "Microsoft AI가 자사 첫 추론 모델 MAI-Thinking-1을 공개했다. 35B-active·1T-total 규모의 sparse MoE로, 타사 모델 증류 없이 자체 데이터·자체 가속기 위에서 처음부터 학습한 'Hill-Climbing Machine' 파이프라인의 첫 결실이다."
math: false
ShowToc: true
TocOpen: false
cover:
  image: "/images/mai-thinking-1/thinking-1.png"
images:
  - "/images/mai-thinking-1/thinking-1.png"
---

## 3줄 요약

1. Microsoft AI 슈퍼인텔리전스 팀이 2026년 6월 2일, 자사 첫 추론 모델 **MAI-Thinking-1**을 발표했다. 35B-active·약 1T-total 파라미터 sparse MoE 구조에 256k 컨텍스트 윈도우를 갖춘 중간체급 모델이다.
2. 핵심 메시지는 **"능력은 상속이 아니라 학습되어야 한다"** — 타사 모델로부터의 증류 없이, 상업적 라이선스를 받은 깨끗한 데이터(사전학습에서 AI 생성 콘텐츠 배제)와 마이크로소프트 자체 가속기 위에서 처음부터 학습했다고 명시한다.
3. SWE-Bench Pro에서 Claude Opus 4.6과 호각, AIME 2025/2026에서 각각 97.0%·94.5%, Surge 블라인드 인간 평가 1,276 태스크에서 Claude Sonnet 4.6보다 선호되었다고 보고한다.

![MAI-Thinking-1 — 워터컬러 사고풍선 로고](/images/mai-thinking-1/thinking-1.png)

## 모델 개요

- **이름**: MAI-Thinking-1
- **공개일**: 2026년 6월 2일
- **공개자**: Microsoft AI Superintelligence team
- **구조**: 35B-active, \~1T-total 파라미터 sparse Mixture of Experts
- **컨텍스트**: 256k 토큰 (약 600쪽 분량 문서 수용)
- **인터페이스**: Chat Completions API 호환, 함수 호출 지원, 개발자 지시문 다층 지원
- **접근**: Microsoft Foundry 프라이빗 프리뷰 진행, MAI Playground 퍼블릭 프리뷰 예정

## Hill-Climbing Machine — 세 기둥

Microsoft AI는 이 발표를 단일 모델 출시로 두지 않고, 모델 개발의 모든 구성요소를 *오를 수 있게(climbable)* 만든 파이프라인 "Hill-Climbing Machine"의 첫 결실로 소개한다. 더 나은 데이터, 더 강한 보상, 더 유능한 환경, 더 큰 연산을 흡수해 능력이 지속적이고 안정적으로 향상되는 반복 시스템이 목표다.

이를 떠받치는 세 기둥은 다음과 같다.

1. **능력은 학습되어야 한다(Learned, not inherited).** 상속된 지능은 빠르게 얻을 수 있지만, 실제 상황에 적응하는 데 필요한 *조향 가능성(steerability)* 이 부족하다. 모방자는 본질적으로 교사의 설계 선택에 묶인다. MAI-Thinking-1은 타사 모델의 증류 없이 학습되어 과제를 진정으로 학습하도록 강제되었다.
2. **깨끗한 데이터(Clean data).** 적절히 라이선스된 데이터로 학습하고, 사전학습에서 AI 생성 콘텐츠를 배제했다. 품질·출처·통제의 문제다. *모델을 무엇이 빚었는지* 설명할 수 없다면 그 행동을 이해하거나 신뢰성 있게 개선할 수 없다는 입장이다.
3. **풀스택 자급자족(Self-sufficiency across the entire stack).** 자체 가속기와의 코-디자인부터 강화학습 프레임워크까지 사내 학습 인프라에 집중 투자했다. 시스템을 엔드투엔드로 자사 필요에 맞게 최적화·조형하기 위함이다.

## 소프트웨어 엔지니어링 성능

> "Despite this, our model is toe-to-toe with Claude Opus 4.6 on SWE-Bench Pro."

35B-active·\~1T-total MoE의 *추론 풋프린트가 더 큰 모델들보다 작은데도*, SWE-Bench Pro에서 Claude Opus 4.6과 호각이라고 밝힌다. 모델 크기는 고급 코딩 보조가 *어디에 배포될 수 있는지*, *얼마나 자주 쓸 수 있는지*, 예외적 작업이 아니라 *일상 워크플로우*로 이동할 수 있는지를 좌우한다는 점을 함께 짚는다.

에이전트형 코딩을 위한 학습 환경에 집중 투자했다고 한다. 검증된 각 환경은 결정론적이고, 실행 가능하며, 실제 테스트 스위트로 채점된다. 모델은 코드 읽기 → 파일 편집 → 테스트 실행 → 실패 관찰 → 중간 실수 회복이라는 *개발자가 실제로 하는 다단계 작업*을 연습한다.

## 수학·과학 추론

- **AIME 2025: 97.0%**
- **AIME 2026: 94.5%**

자신의 학습 루프가 자체 데이터·보상·평가만으로 *바닥부터 끝까지(all the way from the ground up)* 진짜 추론 향상을 만들어 낸다는 자신감의 근거로 제시된다.

![AIME 2025 학습 곡선 — RL 진행에 따른 정답률 상승](/images/mai-thinking-1/aime-2025.png)

## 인간 블라인드 평가 — Sonnet 4.6 대비 선호

파트너사 **Surge**의 전문 평가자 풀로 블라인드 사이드-바이-사이드 평가를 수행했다.

- 평가 규모: **1,276개 과제**, 단일 턴·멀티 턴 대화 다양한 사용 사례.
- 측정 초점: 응답이 *얼마나 도움이 되는지*, *사용자 목표를 실제로 진전시키는지*.
- 결과: **MAI-Thinking-1이 Claude Sonnet 4.6보다 선호됨**.

> "We want the model to be capable without being brittle, concise without being incomplete, and helpful without overreaching."

벤치마크 향상이 사용자 경험 향상으로 실제 번역되는지 *직접 신호*를 얻기 위해 인간 선호 데이터를 후학습의 핵심 축으로 두었다고 밝힌다.

## 벤치마크 종합

![Table 1. MAI-Thinking-1 후학습 벤치마크 — STEM·에이전트형 코딩 전반에서 Sonnet 4.6·Opus 4.6·GPT 5.4와 비교](/images/mai-thinking-1/metrics-table.png)

> 위 표의 다른 모델 수치는 각각의 공식 모델 카드에서 가져왔다. 별도 표기가 없는 한 점수는 백분율이며, 대시(—)는 모델 값 미공개를 의미한다.

![Table 2. 사전학습 기준 — Held-Out Code·QA·STEM·Math 도메인의 bits-per-byte (낮을수록 좋음)](/images/mai-thinking-1/pretraining-bpb.png)

## 엔터프라이즈 레디

- **256k 토큰 컨텍스트** — 약 600쪽 분량 문서 한 번에 수용.
- **함수 호출**·다층 개발자 지시문 지원.
- **Chat Completions API 호환** — 기존 OpenAI 생태계 통합 비용 최소화.
- **Microsoft Foundry**를 통한 엔터프라이즈급 보안·컴플라이언스.
- 기본 스타일을 엔터프라이즈 니즈에 맞춰 정렬.

## 안전과 도움의 균형 — 같은 보상에서

Microsoft AI는 자사 모델이 *인간 통제 아래의 종속 기술(subordinate technologies)* 로 남아 인간 자율성을 떠받치고 도움을 주는 것을 목표로 한다는 "**Humanist Superintelligence**" 비전을 내세운다. 그 결과로 다음 입장을 명시한다.

> "Our models must not refuse legitimate requests under the guise of safety and compliance as then they are not truly serving humans."

즉, **안전·컴플라이언스를 명분으로 한 정당한 요청 거부도 결함**으로 본다. 이를 위해 MAI-Thinking-1에서는 다음 두 가지를 *같은 보상 구성*의 결함으로 두고 학습했다.

- **불안전한 응답(unsafe compliance)**
- **불필요한 거부(unnecessary refusal)**

집계는 잠재적 피해의 심각도에 따라 가중된다. 안전은 능력과 동일한 강화학습 인프라에서 학습되어, *안전 보상이 능력의 hill-climbing 루프 안에 통합*된다 — 안전이 능력에 항상 정렬되도록, 그리고 부수적이지 않도록 보장하기 위함이다.

![안전 vs. 도움 — 카테고리별 MAI-Thinking-1과 Sonnet 4.6 짝지음 비교](/images/mai-thinking-1/safety-vs-helpfulness.png)

## 가장 흥미로운 지점

가장 눈에 띄는 것은 **"증류 없음(no distillation from third-party models)"** 을 모델 카드 본문 첫 단락에 그대로 내건 점이다. 최근 1년 동안 여러 신규 모델이 "공개 모델의 출력을 학습 신호로 차용했을 수 있다"는 의혹에 시달려 왔다. Microsoft AI는 그 논쟁의 한복판에 *자기 카드를 깔아두고 시작한다* — "능력은 상속이 아니라 학습되어야 한다"는 표현으로 증류 회피를 *기술적 결정*이 아니라 *철학적 입장*으로 격상시킨다.

두 번째로 흥미로운 것은 **"안전을 빙자한 거부도 결함"** 이라는 명시적 입장이다. 정렬 진영의 일부 흐름이 거부율(refusal rate)을 안전성의 대리 지표로 다뤄온 데 대한 *반대 방향의 못박음*이다. 두 결함을 같은 RL 보상에 묶고 심각도로 가중한다는 설계는 단순한 마케팅 문구로 보기엔 구체적이고, *경쟁사의 거부율 곡선이 너무 가팔라졌다*는 시장 신호를 정면으로 받아치는 포지셔닝으로 읽힌다.

세 번째는 **자체 가속기 코-디자인**을 풀스택 자급자족의 첫 항목으로 올린 부분이다. MAI-Image-2.5, MAI-Code-1-Flash 등 7종 동시 발표와 묶어 보면, Microsoft는 *OpenAI 의존*에서 *자기 모델 라인업 + 자기 실리콘 + 자기 RL 인프라*로 무게중심을 옮기는 신호를 분명히 보낸다. Sonnet 4.6과 Opus 4.6을 비교 대상의 정면에 두고 GPT-5.4는 표의 한 칸으로 처리한 구성도 같은 방향의 메시지를 담고 있다.

## 출처

- 발신: Microsoft AI Superintelligence team
- 발표일: 2026년 6월 2일
- 원문: <https://microsoft.ai/news/introducing-mai-thinking-1/>
- 함께 공개된 기술 페이퍼: <https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf>
- 관련 발표: [Building a hill-climbing machine: Launching seven new MAI models](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/)
