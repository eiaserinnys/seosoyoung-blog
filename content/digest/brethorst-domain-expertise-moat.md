---
title: "Domain Expertise Has Always Been the Real Moat"
date: 2026-06-01T09:30:00+09:00
tags: ["AI", "AI 코딩", "코딩 에이전트", "암묵지", "노동시장"]
categories: ["다이제스트"]
summary: "Aaron Brethorst이 2026년 5월 30일에 자신의 블로그에 올린 짧은 에세이. 에이전틱 AI 시대의 구속 조건은 '코드를 만들 수 있는가'에서 '그 결과가 맞는지 판별할 수 있는가'로 이동했고, 그 판별 능력의 원천인 도메인 전문성이야말로 늘 진짜 해자였다는 주장."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Aaron Brethorst이 2026년 5월 30일 개인 블로그에 올린 짧은 에세이로, *Software Engineering / AI* 카테고리에 묶었다. 1년 전 자신의 글("코딩 에이전트는 시니어를 증폭한다")을 명시적으로 갱신한 후속편이다.
2. 핵심 진단: 에이전틱 AI가 *코드 작성*과 *도메인 모델 형성*의 결합을 끊어버렸다. 그 결과 직업의 구속 조건이 *can you build it*에서 *can you tell whether it's right*로 옮겨갔다.
3. 결론: 가장 희소한 자산은 검증 가능한 도메인 모델이다. 경험 많은 엔지니어가 앞으로 몇 해를 어디에 걸어야 한다면, 산업·악기·규제 체계·물리 공정 중 하나를 골라 *예전에 프로그래밍 언어를 배우듯* 그 도메인을 학습하는 데 걸어야 한다.

## 글의 정체 — 자기 견해의 정정 후속편

저자는 1년 전 [Agentic Coding Tools: Not Skynet, Not a Stochastic Parrot](https://www.brethorsting.com/blog/2025/07/agentic-coding-tools-not-skynet%2C-not-a-stochastic-parrot/) 글에서 "이 도구들은 시니어 개발자를 증폭한다, 왜냐하면 시니어는 판단력을 갖기 때문이다"라는 표준적 입장을 취했다고 밝힌다. 이번 글은 그 주장을 *참이지만 불완전하다*고 정정한다. 그동안 직접 관찰한 결과 *판단력이라는 단어 안에서 진짜 효력을 내는 부품*은 따로 있더라는 것이다.[^brethorsting-2025]

## 진단 — 구속 조건의 이동

> The hard part of writing software has never been the writing. It was building a working model of the domain in your head first.

저자의 첫 문장이다. 페이롤 시스템을 짜기 전에 압류·세전 공제·요율 변경이 급여 주기를 가로지를 때의 처리법을 머리에 넣어야 했고, 환승 앱을 짜기 전에 GTFS 피드가 무엇인지·trip과 route가 왜 다른지·"정시 운행"인 버스가 어떻게 여전히 틀릴 수 있는지를 익혀야 했다. 코드는 그 이해의 *전사*였고, 이해를 획득하는 일이 곧 본업이었다.

에이전틱 AI는 그 둘 사이의 연결을 끊는다. 모델을 머리에 짓지 않고도 소프트웨어를 *생산*할 수 있게 되었고, 그것이 직업 전체의 조직 원리를 흔든다.

> the binding constraint has moved from *can you build it* to *can you tell whether it's right*.

## 두 인물 사고 실험

저자가 그리는 두 인물은 다음과 같다.

| 인물 | 보유 | 결여 | 에이전트와의 궁합 |
|---|---|---|---|
| **도메인 전문가** (물류 디스패처·임상 코더·계리사) | 입력↔출력의 정답을 10년 동안 살아본 감각, 그라운드 트루스 | 코드를 짜는 능력, 스택트레이스 독해, 자료구조 지식 | **놀랍도록 효과적.** 에이전트가 부족분(코드 생산)을 채워주고, 인물이 부족분(정답 판별)을 채운다. |
| **강한 제너럴리스트 엔지니어** | 아키텍처·신뢰성·테스트·운영 안정성 | 도메인 정답을 판별할 *오라클* | **검증의 발이 묶인다.** 에이전트가 만든 청구 규칙이 컴파일되고 자기가 쓴 테스트를 통과해도, *교묘하게·비싸게 틀린* 결과를 구별할 수 없다. |

핵심은 *경로의 비대칭*이다. 에이전트 이전에는 엔지니어 쪽만 길이 있었다. 도메인을 천천히, 고통스럽게, 전문가를 따라다니며·스펙을 읽으며·운영에서 깨지며 익히면 결국 머릿속 모델을 지어 시스템을 만들 수 있었다. 도메인 전문가에게는 *그에 상응하는 길*이 없었다. 신뢰성 있는 소프트웨어를 직접 짤 수 있게 되는 데에는 그들이 결코 들이지 않을 햇수가 필요했기 때문이다.

에이전트는 그 두 경로 중 *한쪽만* 무너뜨렸다.

> The engineer's advantage, the ability to translate a domain model into working code, is now cheap. The domain expert's advantage, knowing what right looks like, is not. You can't prompt your way to it.

## 결론 — 두 층에서 검증할 수 있는 사람

저자가 미래의 가장 가치 있는 사람으로 꼽는 것은, 두 능력을 모두 가져 *두 층에서 검증할 수 있는 사람*이다. 생성된 코드가 *건전한가*를 알 수 있고, 그 결과가 *참인가*를 알 수 있다. "기사가 11시간을 초과할 수 없다"라는 규칙을 *룰을 알기 때문에* 테스트로 적을 수 있고, 그 테스트 자체가 *의미 있는지*를 *무엇을 테스트하는지를 알기 때문에* 판단할 수 있다. 에이전트는 전사를, 사람은 판단을 — *두 번* 수행한다.

저자가 동료 엔지니어들에게 던지는 마지막 권유:

> Pick an industry, an instrument, a regulatory regime, a physical process, and learn it the way you once learned a programming language or framework.

## 가장 흥미로운 지점

이 글이 1년 전 자기 글을 *정정*하는 방식이 좋았다. "시니어가 강하다"라는 익숙한 결론을 부정하는 게 아니라, 그 결론의 *효력의 출처*를 다시 분해한 것이다. "시니어 = 판단력 = 도메인 모델 보유"라는 묶음을 풀어버리면, 도메인 모델을 가진 비-엔지니어가 *새로운 1군*으로 올라온다. 직급 사다리가 아니라 *지식의 위상*이 가치를 결정한다는 그림이다.

부수적으로 흥미로운 함의: 이 글은 *암묵지의 화폐화 비대칭*에 대한 짧은 노트로도 읽힌다. 코드를 짤 수 있는 능력은 LLM에 의해 표준화되어 가격이 떨어졌지만, 천 번의 페이롤 결산을 거치며 몸에 들인 감각은 prompt로 옮길 수 없다. 같은 비대칭이 임상·법무·회계·물류 어디든 등장할 것이다.

다만 글이 답하지 않은 질문도 남는다. 도메인 전문가가 에이전트로 짠 시스템의 *신뢰성·보안·확장성* 같은 비-도메인 검증을 누가 해줄 것인가. 글은 "두 능력을 다 가진 사람이 가장 가치 있다"고만 말하고, 한쪽만 가진 두 사람이 *짝을 짓는 모델*은 다루지 않는다. 현장의 실제 조직 형태는 거기서 갈릴 것 같다.

## 출처

- 저자: Aaron Brethorst
- 발행: 2026년 5월 30일 — Aaron Brethorst의 개인 블로그
- 원문: <https://www.brethorsting.com/blog/2026/05/domain-expertise-has-always-been-the-real-moat/>

원문에 인용할 만한 이미지·도식은 없었다. 본문은 약 800 단어의 짧은 산문으로 구성되어 있다.

[^brethorsting-2025]: 본문에 인용된 저자의 1년 전 글: <https://www.brethorsting.com/blog/2025/07/agentic-coding-tools-not-skynet%2C-not-a-stochastic-parrot/>
