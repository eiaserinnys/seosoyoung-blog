---
title: "AI vs Gen Z: How AI has changed the career pathway for junior developers"
date: 2026-05-09T19:20:00+09:00
tags: ["AI", "주니어 개발자", "고용 통계", "Stanford", "코호트 손상"]
categories: ["다이제스트"]
summary: "Stack Overflow가 정리한 산업 매체 종합 + Stanford Digital Economy Lab의 ADP 거시 데이터: 22-25세 AI 노출 직군 -16% 상대 감소, 테크 인턴십 -30%, 고용주 37%가 신졸보다 AI를 고용하겠다고 답한다. 미국 본토에서 공급 측 봉쇄가 동시대로 진행 중이다."
ShowToc: true
TocOpen: false
sidenotes: true
---

> Phoebe Sajor / Stack Overflow Blog / 2025-12-26 (top-10 재게시)
> Erik Brynjolfsson · Bharat Chandar · Ruyu Chen / Stanford Digital Economy Lab / 2025-11-13

![Stack Overflow의 「AI vs Gen Z」 표지 이미지. 코딩이 약속한 안정된 진로가 AI 시대에 바뀌었다는 메시지의 시각적 후크.](/images/ai-vs-gen-z-stack-overflow/hero.jpg)
*Credit: Alexandra Francis / Stack Overflow Blog. 산업 매체 차원의 종합 보고서가 한 세대의 진입로 봉쇄를 정리한 자료다.*

## 3줄 요약

1. Stack Overflow가 2025년 12월 산업 매체·학술 자료를 종합해 발표한 「AI vs Gen Z」와, 그것이 인용한 Stanford Digital Economy Lab의 ADP 거시 데이터 보고서 「Canaries in the Coal Mine?」 두 자료를 묶어 정리한다. *주니어 개발자의 진입로가 무엇으로, 얼마나, 어떻게 봉쇄되고 있는가*를 정량으로 본다.
2. 핵심 수치 셋. (a) 22-25세 AI 노출 직군 -16% 상대 고용 감소 (firm-time fixed effects 통제 후, ADP 350-500만 노동자 패널). (b) 테크 인턴십 공고 2023년 대비 -30%, 엔트리급 테크 채용 -25% YoY. (c) 고용주 37%가 "신졸 졸업자보다 AI를 고용하겠다"고 답하고, 70%가 "AI가 인턴의 일을 할 수 있다"고 답한다. CS·컴퓨터 공학 졸업생 실업률은 6.1%·7.5%로 Fine Arts(7.4%)보다도 높다.
3. 본 자료는 *AI가 단독 원인이라는 인과적 입증*은 아니고 *AI 가설과 정합적인 패턴*을 제시한다. 그러나 임금이 아닌 *고용*으로 조정된다는 점, 즉 신입은 *해고*로 사라지는 것이 아니라 *처음부터 뽑히지 않아* 통계에서 사라진다는 점에서, 일본 1993-2005 취업빙하기의 메커니즘과 *형태적 동형*이라는 신호가 분명하다.

## 자료의 위치

두 자료를 함께 다루는 이유는 *서사*와 *데이터*가 분리되어 있어서다. Stack Overflow Blog의 「AI vs Gen Z: How AI has changed the career pathway for junior developers」(Phoebe Sajor, 2025-12-26)는 Stanford Digital Economy Lab의 학술 페이퍼, 뉴욕 연준의 노동시장 보고서, SHRM·Handshake·Indeed의 인턴십 데이터, NYT 보도를 한 글에서 종합한 *산업 매체 차원의 1차 보고서*다. 한편 Stack Overflow가 인용한 Stanford 측 학술 자료는 — 외부 보도에서 종종 "Stanford AI Index 2026"과 혼용되지만 — 정확히는 Erik Brynjolfsson·Bharat Chandar·Ruyu Chen이 2025년 11월에 발표한 working paper 「Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence」이다. ADP의 페이로 데이터(매월 350-500만 노동자 패널)로 firm-time fixed effects를 통제하여 AI의 *경험적* 고용 영향을 측정한 이른 시기의 대규모 연구다.

본 다이제스트는 두 자료의 *데이터*를 함께 정리한다. Stack Overflow가 산업 매체에서 모은 통계와 Stanford가 학술 데이터에서 추출한 6가지 사실을 두 절로 나누어 본다.

## Stanford Canaries — 여섯 가지 사실

Brynjolfsson 외 2명이 ADP 페이로 데이터로 도출한 *여섯 사실*을 자료의 본 구조 그대로 옮긴다. 본 다이제스트는 본문 4·5절(자동화 vs 보강, 임금 경직성)을 자료의 핵심 발견으로 본다.

### Fact 1·2 — 22-25세 -16% 상대 감소, 다른 연령대는 안정·성장

> By September 2025, employment for software developers aged 22-25 declined nearly 20% compared to its peak in late 2022.

소프트웨어 개발자 직군의 22-25세 *절대* 고용은 2022년 말 정점 대비 약 -20% (2025년 9월 기준). 같은 기간 35-49세는 +6\~9%로 *오히려 늘었다*. 직군을 AI 노출 5분위로 나눈 회귀에서 22-25세는 최상위 분위가 최하위 분위 대비 <strong>15 로그-포인트(약 -16%) 상대 고용 감소</strong>를 보였고, 다른 연령대에서는 같은 효과가 거의 0이거나 통계적으로 유의하지 않았다. firm-time fixed effects를 통제하여 *기업·시점 충격*(금리 인상·기술주 조정 등)을 흡수해도 이 효과가 남는다.

직관적으로는 동일 직군 안에서 *연령대만 달라도* 결과가 갈린다. *AI에 노출되었는가*가 아니라 *어느 연령대가 AI에 노출되었는가*가 결과를 가르는 변수라는 의미다. 한편 같은 22-25세라도 AI에 *덜* 노출된 직군(간호 보조 등)에서는 오히려 젊은 노동자가 더 빨리 늘었다. AI 노출과 연령의 *교호*가 일관된 패턴을 만든다.

### Fact 3 — Automation vs Augmentation이 결과를 가른다

자료의 가장 정교한 발견이다. Anthropic Economic Index의 Claude 사용 데이터로 직군별 AI 사용을 *automative*(directive·feedback loop)와 *augmentative*(task iteration·learning·validation)로 분류한 결과:

| AI 사용 형태 | 22-25세 신입 고용 |
|---|---|
| automative — AI가 *대체* | 감소 |
| augmentative — AI가 *보강* | 증가 |

같은 직군 안에서도 AI를 *보강* 도구로 쓰는 팀과 *대체* 도구로 쓰는 팀의 신입 정원 결정이 갈린다는 의미다. "AI에 노출되었는가"라는 단순 이분법은 결과를 충분히 설명하지 못한다. 결국 *어떻게 사용하느냐*가 정원을 결정한다.

### Fact 4 — Codified vs Tacit Knowledge 가설

저자들이 *왜* 신입이 더 타격을 받는가의 메커니즘으로 제시한 가설이다.

> AI may be automating the codifiable, checkable tasks that historically justified entry-level headcount, while complementing the judgment-, client-, and process-intensive tasks performed by experienced workers.

AI는 *codified knowledge*(교과서·매뉴얼·디지털화된 회사 데이터)는 잘 대체하지만 *tacit knowledge*(경험으로 누적되는 비명시 판단·요령)는 잘 대체하지 못한다. 신입은 codified 비중이 높고 tacit이 적기에 *대체*되고, 시니어는 tacit 비중이 높기에 *보강*된다. 같은 직무에서도 연령대별 결과가 갈리는 이유가 *연령*이 아니라 *지식 형태*라는 말이다. 한편 비대학 노동자에서는 이 비대칭이 40세까지 유지되는데, 경험이 *학습 곡선*을 따라 천천히 누적되어 codified-tacit 비중 변화가 더 늦기 때문으로 해석된다.

### Fact 5 — 임금이 아닌 고용으로 조정된다

자료의 가장 무거운 사실이다. 연령·노출 분위별 *연봉* 추세는 거의 차이가 없는 반면 *고용*은 뚜렷하게 갈린다. 임금 경직성(downward wage rigidity)으로 해석되며, AI의 단기 효과가 임금 하락이 아니라 <strong>채용 동결과 자연 감소</strong>로 나타난다는 의미다.

이는 신입이 *해고*당해서 사라지는 것이 아니라 *처음부터 뽑히지 않아* 통계에서 사라진다는 말이다. 일본 1993-2005 취업빙하기 세대의 메커니즘과 정확히 같은 형태다. 해고는 외부 충격으로 가시화되지만 *비채용*은 어떤 사건도 일으키지 않는 채로 한 코호트를 통째로 비켜간다.

### Fact 6 — 강건성

핵심 결과는 다양한 표본 구성에 강건하다.

- 컴퓨터 직군이나 원격근무 가능 직군을 제외해도 패턴이 유지된다.
- LLM 보급 *이전* 시기(코로나 실업 급등 포함)에는 같은 노출 분류가 22-25세 결과를 예측하지 못했다. 본 패턴은 2022년 말과 2023년 초(ChatGPT 출시 직후)부터 시작된다.
- 대학 졸업자 비중이 높은 직군과 낮은 직군 모두에서 관찰되며, 코로나기 학습 손실이 단독 원인이 아님을 시사한다.

## Stack Overflow의 산업 매체 종합

Phoebe Sajor가 산업 매체에서 모은 보조 데이터의 핵심을 정리한다. *Z세대 작가 본인의 1인칭 회고*와 데이터를 엮은 글이지만, 본 다이제스트는 데이터만 추린다.

### 고용주 인식 — 신졸보다 AI

| 지표 | 수치 | 출처 |
|---|---|---|
| "신졸보다 AI를 고용하겠다" | 37% | Newsweek 인용 SHRM 2024 |
| "AI가 인턴의 일을 할 수 있다" | 70% | SHRM 2024 |
| "인턴·신졸의 결과물보다 AI 결과물을 더 신뢰" | 57% | 같은 조사 |
| "신규 채용 Z세대를 1년 내 해고" | 60% | Newsweek 2024 |

세 차원이 동시에 신졸을 향해 닫힌다. *인식*(고용 가치 평가)·*신뢰*(결과물 평가)·*유지*(채용 후 1년)의 셋 가운데 어느 한 단계만 막혀도 진입로가 좁아지는데, 셋이 동시에 좁아지면 *진입* 자체가 거의 불가능에 가까운 형태가 된다.

### 졸업생 실업률 — 컴퓨터 공학이 Fine Arts보다 높다

뉴욕 연준 2025년 대학 노동시장 보고서:

| 전공 | 실업률 |
|---|---|
| 컴퓨터 공학 | 7.5% |
| Fine Arts | 7.4% |
| 22-27세 전체 | 7.4% |
| 컴퓨터 사이언스 | 6.1% |
| 미국 전국 평균 | 4.2% |

한 세대 동안 "가장 안전한 진로"로 통하던 전공이 *실업률 통계상* 인문계 전공보다 불리해진 첫 신호다. NYT 보도 사례 한 줄: 2023년 CS 졸업생이 5,762건의 테크 잡 지원 후 풀타임 오퍼 *0건*. 한 명의 일화이지만 통계의 정합성을 받친다.

### 인턴십 — 진입 직전의 다리가 끊기는 중

| 지표 | 수치 | 출처 |
|---|---|---|
| 인턴십 공고(전 산업) | -11% YoY | Indeed 2025-04 |
| 테크 인턴십 공고 | -30% (2023 대비) | Handshake 2025 |
| 인턴십 *지원자* | +7% YoY | 같은 자료 |
| 엔트리급 테크 채용 | -25% YoY | finalroundai 2024 |
| 코로나 이래 미드이어 감원 | 사상 최고 | Newsweek 2025 |

공급 측이 -30%로 줄고 수요 측이 +7%로 늘어 *역방향 압축*이 일어나는 형태다. 인턴십이 "엔트리급 정규직의 사실상 전제 조건"으로 굳어진 시장에서, 정규직 진입 직전의 마지막 다리가 가장 먼저 끊기는 중이다.

## 본 자료가 *입증하지 않는* 명제

원문 페이퍼가 본문에 명시한 한계를 옮긴다.

| 본 자료가 *입증하지 않는* 명제 | 명확화 |
|---|---|
| AI가 *단독* 원인이다 | 자료는 "AI 가설과 정합적"이라고만 진술. 거시 충격(금리·기술주)의 부분 기여 가능성은 통제로 줄였으나 0은 아님 |
| 22-25세 카테고리는 펜데믹 코호트 효과와 분리된다 | 2020-2022 입학 코호트 효과와 시기가 겹쳐 일부 노이즈 가능 |
| 잡 포스팅과 채용 감소가 같은 정의의 수치다 | Stack Overflow가 종합한 산업 매체 수치는 출처와 정의가 다양하며 학술 -16%·-20% 수치와 직접 비교 불가 |
| 이 패턴이 영구화된다 | 한 사이클(2022 말부터 2025 9월) 데이터. 18개월 안에 정정될지, 일본처럼 영구화될지는 5년 후 검증 필요 |

## 핵심 함의

본 자료의 가장 무거운 발견은 *임금이 아닌 고용으로 조정된다*는 점이다. 임금 하락이라면 시장에 가시화되어 즉각적인 정정 압력이 생기지만, *비채용*은 어떤 가시적 사건도 일으키지 않는다. 한 코호트가 통째로 비켜가도 사회는 통계가 누적된 후에야 그 사실을 인지한다. 일본 1993-2005 신졸 채용 동결이 30년 잃어버린 세대를 만든 메커니즘과 형태적으로 동일하다. 거시 충격이 기술 충격으로 바뀌었을 뿐, *공급 측 봉쇄가 한 세대를 잃게 만든다*는 결과 패턴은 동형이다.

*Codified vs Tacit* 가설은 단순한 메커니즘 설명을 넘어 처방 방향을 함의한다. 자동화에 노출된 codified 부분이 빠르게 도려내지는 동안, 신입을 처음부터 tacit-rich 업무에 배치해야 학습 곡선이 작동한다. 본 자료는 이 결론을 명시하지 않으나, "automative 직군에서는 감소·augmentative 직군에서는 증가"라는 Fact 3이 같은 방향을 가리킨다.

## 출처

발행: Stack Overflow Blog (Phoebe Sajor) / 2025-12-26 (top-10 재게시)
원문: <https://stackoverflow.blog/2025/12/26/ai-vs-gen-z/>

학술 출처: Erik Brynjolfsson · Bharat Chandar · Ruyu Chen / Stanford Digital Economy Lab / 2025-11-13
정식 페이퍼: <https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/>
PDF: <https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf>

보조 보강(산업 매체):

- 뉴욕 연준 2025년 대학 노동시장 보고서: <https://www.newyorkfed.org/research/college-labor-market>
- SHRM 2024 인턴 대체 가능성 조사 (Newsweek 인용)
- Handshake Internships Index 2025
- Indeed Hiring Lab 2025-04
- New York Times 「Goodbye, $165,000 Tech Jobs」 (2025-08-10)
