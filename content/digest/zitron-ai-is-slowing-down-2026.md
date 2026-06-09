---
title: "AI Is Slowing Down"
date: 2026-06-09T14:20:00+09:00
tags: ["경제·금융", "AI 거품", "OpenAI", "Anthropic", "데이터센터", "AI"]
categories: ["다이제스트"]
summary: "Ed Zitron이 6월 8일에 올린 글. 2030년까지 데이터센터 빌드아웃에 9.5조에서 15조 달러가 필요하지만, OpenAI와 Anthropic에 89% 집중된 수요로는 채워질 수 없다는 자본 산수와, 토큰 빌링 도입 2개월에서 3개월 만에 도입 기업들이 사용자당 한도를 거는 둔화 신호를 모은 자료."
ShowToc: true
TocOpen: false
cover:
  image: "/images/zitron-ai-is-slowing-down-2026/agentic-ai-app-shovelware.png"
images:
  - "/images/zitron-ai-is-slowing-down-2026/agentic-ai-app-shovelware.png"
---

## 3줄 요약

1. Ed Zitron이 자신의 뉴스레터 *Where's Your Ed At*에 6월 8일 올린 무료 글. AI 산업의 자본 약속과 실제 수요의 격차를 사례와 수치로 모아 보여 준다.
2. 2030년까지 진행될 데이터센터 빌드아웃은 9.5조\~15조 달러 규모로 추정되지만, AI 컴퓨트 수요의 89%가 OpenAI와 Anthropic에 몰려 있어 그 자본을 회수할 매출 기반이 없다.
3. Anthropic과 OpenAI가 2026년 1분기에 토큰 기반 빌링으로 전환하자, 2\~3개월 만에 Uber, T-Mobile, Brex 같은 도입 기업들이 사용자당 토큰 한도를 걸기 시작했다. Zitron은 이를 AI 수요가 *둔화*하는 첫 신호로 본다.

## 자료 정보

- 발신: Ed Zitron, *Where's Your Ed At* 뉴스레터
- 발행: 2026-06-08
- 분량: 약 4,800단어
- 톤: 도발적이고 비속어가 섞인 적대적 논평. 다만 핵심 주장은 1차 보도와 공시 데이터로 뒷받침된다.
- 위치: AI 거품 시리즈(3월\~5월의 *What If We're In an AI Bubble* 3부작) 직후 발행된 무료 follow-up.

## 데이터센터 자본 약속의 규모

| 항목 | 수치 | 출처 |
|---|---|---|
| 계획된 데이터센터 용량 | 190GW | Sightline Climate, 2026-02 |
| 1GW당 비용 (NVIDIA CEO 추정) | \$80B \~ \$100B | Jensen Huang, GTC Taipei 2026 |
| 총 빌드아웃 비용 | \$9.5T \~ \$15T | 위 두 수치의 곱 |
| 현재 연간 데이터센터 채권 발행액 | 약 \$250B | Zitron 추정, FT 5월 보도 |
| 빌드아웃을 채우기 위해 필요한 연간 발행액 | \$500B \~ \$1T | Zitron 추정 |

Bloomberg는 이 빌드아웃을 "\$3 trillion"으로 보도했으나, Zitron은 단위를 한 자릿수 잘못 잡은 오류로 본다.

같은 시기에 하이퍼스케일러는 채권이 아닌 *주식*으로 자금을 끌어 오기 시작했다. Google이 5월에 \$85B 규모의 주식을 매각했고, Meta도 수십억 달러 규모의 추가 매각을 검토 중이다. Zitron의 팟캐스트에 출연한 경제학자 Paul Kedrosky는 이를 "채권 조달이 더 어려워지고 있다는 신호"로 해석한다.

NVIDIA의 매출 구조도 같은 압력 아래 있다. 분기 매출의 54%가 익명 3개 고객에서 나오는데, Zitron은 이를 Microsoft, Google, Meta에 서버를 납품하는 대만 ODM 3사로 추정한다. 즉 NVIDIA의 향후 매출은 이 3사의 부채 조달 능력에 묶여 있다.

## OpenAI와 Anthropic의 약속

| 회사 | 컴퓨트 약속 | 누적 조달 | 2029년 매출 목표 | 추가 필요 추정 |
|---|---|---|---|---|
| Anthropic | \$330B (Google, Amazon, MS) + \$30B CoreWeave + \$15B SpaceX | \$95B | \$174B/년 | 1년 안에 \$200B 추가 |
| OpenAI | \$770B+ (MS, Amazon, CoreWeave, Cerebras, Oracle) | 3월 \$122B 라운드 | \$184B/년 | 연말까지 \$250B 추가 |

OpenAI는 2030년까지 누적 \$852B를 소진할 것으로 자체 전망했다. Anthropic이 자신을 2029년에 흑자로 본다고 밝힌 데 대해, Zitron은 "재무 공학을 빼면 현재도 흑자가 아니"라며 회의한다.

이 둘이 전체 AI 컴퓨트 수요의 최소 70%, 추정 80\~90%를 차지한다. Zitron의 표현으로는 "두 회사 밖에서 발생하는 수요는 연간 *몇 십억 달러* 단위이고, 정작 필요한 건 *몇 백억 달러* 단위"다.

## 수요-공급 격차의 산수

> 190GW × PUE 1.35 → 임계 IT 부하 약 140GW. 메가와트당 연간 \$12.5M으로 부과한다면 연간 약 \$1.75T의 매출이 필요하다. 절반만 건설된다 해도 \$875B/년이 필요하다.

Zitron이 자료에서 직접 제시한 계산이다. 같은 자료에서 OpenAI와 Anthropic의 2029년 매출 합계 전망은 약 \$358B이다. 즉 두 회사가 약속대로 성장해도, 같은 규모의 회사가 *최소 두 곳은 더 나타나야* 데이터센터 자본이 회수된다.

The Information의 보도는 이 격차가 좁혀지지 않는다는 쪽을 가리킨다. OpenAI와 Anthropic이 <em>모든 AI 스타트업 매출의 89%</em>를 차지한다. 하이퍼스케일러의 AI 매출을 더해도 그림이 크게 바뀌지 않는다. Microsoft의 AI 연간 런 레이트 \$37B 중 대부분이 OpenAI의 컴퓨트 사용이고, Copilot 등 자체 매출은 최대 \$8B 규모로 추정된다.

같은 시점에 Microsoft AI CEO Mustafa Suleyman은 "Anthropic 모델이 너무 비싸서 Microsoft 내부 사용을 0으로 줄이겠다"고 발언했다. Zitron은 이를 *수요를 더 늘려야 할 시점에 가장 큰 고객 중 하나가 빠지는* 사건으로 지목한다.

## 토큰 빌링 도입 후 시장 반응

Anthropic과 OpenAI는 2026년 Q1에 사용량 기반(토큰) 빌링으로 전환했다. Zitron이 모은 사례:

| 회사 | 도입 후 조치 |
|---|---|
| Uber | 한 분기 만에 연간 토큰 예산을 소진. 이후 사용자당 월 \$1,500 한도 설정 |
| T-Mobile | 사용자당 월 \$2,000 한도 (티어 시스템 도입 검토) |
| Brex | 엔지니어 주당 \$500, 비엔지니어 주당 \$5 |
| 익명 회사 | spend control 미설정 상태로 한 달에 Anthropic 모델에 \$500M 지출 |

Uber COO는 "토큰 지출과 Uber 서비스의 유의미한 기능 개선 사이의 연결을 보이기 어렵다"고 발언했다. Zitron은 이 발언을 인용해, AI 도구의 ROI가 *측정 불가능*한 게 아니라 *측정 가능해진 순간 회수당하고 있다*고 본다.

KPMG의 미발표 설문에서 AI 비용에 종합 가시성을 가진 기업은 26%, 일부 가시성을 가진 기업이 50%, 사후 청구서까지 가시성이 없는 기업이 22%였다. *Wall Street Journal*은 이를 두고 "토큰이라는 새 자원이 CFO에게 익숙한 정액제 모델과 충돌한다"고 보도했다.

> The shift to pricing based on usage, and measured by tokens [...] is creating new challenges for even the most experienced finance teams. CFOs used to paying flat amounts for technology are finding costs more unpredictable and harder to model as they build agents and embark on ambitious AI investments. (KPMG, WSJ)

## "Loops" 권유와 그 의도

같은 시기에 Anthropic Claude Code 책임자 Boris Cherny와 OpenAI 산하 OpenClaw의 Peter Steinberger가 거의 동시에 "에이전트의 loop를 설계하라"고 사용자에게 주문하기 시작했다. Zitron의 해석: 사용자 입력 없이도 모델이 스스로 추론과 행동을 반복하며 토큰을 소비하는 흐름을 권장하는 것이며, 이는 매출 압박과 직결된다. Steinberger 본인이 한 달에 OpenAI API 토큰을 \$1.3M 어치 소비한다고 공개적으로 인증한 바 있다.

Zitron은 자기 글에서 이미 한 차례 정리해 둔 비유를 다시 꺼낸다.

> 보조금이 있는 정액제 구독에서는 모델의 실수(루프에 갇히거나 엉뚱한 일을 하는 것)가 "초기 기술의 자연스러운 잡음"으로 미뤄진다. 비용이 월 \$20, \$100, \$200이기 때문이다. AI 회사들은 이 비용 구조를 의도적으로 흐려 두었다. 사용자가 실수의 실제 비용을 보는 순간, 벌에 쏘인 듯이 비명을 지른다는 걸 알기 때문이다.

## 본문에 인용된 차트: 출시 폭증과 사용량 정체의 갈림

![Agentic AI가 모바일 앱 출시를 폭증시켰지만, 이 앱들이 실제 사용으로 이어진다는 신호는 없다. (FT, John Burn-Murdoch, Demirer et al. 2026 인용)](/images/zitron-ai-is-slowing-down-2026/agentic-ai-app-shovelware.png)

iOS 앱의 월간 출시 건수는 2025년 초 *Agentic AI* 도입 시점부터 가파르게 상승해 2026년 초 2024년 평균의 180% 수준에 도달한다. 같은 기간 *유의미한 사용량을 가진 앱*과 *앱 리뷰*는 정체하거나 하락한다. Zitron은 이를 "AI가 우리에게 준 건 *더 많은 앱*뿐, 대부분 쓸모없거나 안전하지 않은 슬롭웨어"라는 자기 주장의 시각적 근거로 인용한다.

## "Wild Wild West의 거대 금속 거미" 비유

자료 후반부 한 절을 우화로 채운다. AI 산업을 영화 〈와일드 와일드 웨스트〉(1999)의 거대 기계 거미에 빗댄 비유다. 요약:

- 거미 1대 가격 \$1M, 한 번 작동에 연료 \$40K.
- 가끔 다이어트 콜라를 정확히 집어 오고, 가끔 냉장고를 꿰뚫는다. 한 번 사용한 비용은 결과의 성패와 무관하게 청구된다.
- 제조사가 일반 사용자에게는 월 \$200 보조금으로 공급한다. 기업 사용자는 실제 비용을 부담한다.
- 모든 업데이트가 "거미가 할 수 있는 일의 범위"를 넓힌다고 광고하지만, 결과의 일관성은 측정되지 않는다.
- 비판하면 "doomer, luddite, rube"로 분류된다.

Zitron은 이 비유로 두 가지를 동시에 말한다. 첫째, AI 도구의 *능력*은 일부 작업에서 실재한다. 둘째, 그 능력의 *경제성*은 보조금이 사라지면 곧장 무너진다.

## 마무리: 다음 2주 안 예고

자료 맺음말에서 Zitron은 "앞으로 2주 안에 AI 산업의 최악의 두려움을 확인할 보도를 낼 것"이라고 예고한다. 익명 제보자가 가져온 자료라고만 밝히고 내용은 공개하지 않는다. *이 다이제스트 작성 시점(2026-06-09) 기준으로 후속 보도는 아직 나오지 않았다.* 후속 보도가 나오면 별도 다이제스트로 다룬다.

## 가장 흥미로운 지점

토큰 빌링이 도입된 *바로 그 분기*부터 ROI 비판이 주요 매체에 동시 등장한다는 타이밍이 흥미롭다. 보조금이 가린 명목 비용(\$20\~\$200) 시절에는 모델의 실패가 "초기 기술의 성장통"으로 미뤄졌지만, 사후 청구서로 노출되자 같은 실패가 곧장 자금 통제로 회수된다. 기술 자체의 한계가 새로 발견된 게 아니라, *가격 정보 비대칭이 풀린 효과*가 수요 곡선을 휘게 만든 셈이다.

Zitron의 자본 산수가 거칠게 들리더라도, OpenAI와 Anthropic이 IPO 압박으로 보조금을 줄이고 토큰 빌링을 일반 사용자에게도 확대할 때 이 효과가 더 넓은 층에 동시에 작동한다는 함의는 무겁다. GitHub Copilot이 토큰 빌링으로 전환한 첫 주에 사용자 불만이 쏟아진 사례가 이미 보고됐다.

다만 자료는 격앙된 톤과 적대적 어휘 때문에 한 번 더 거르고 읽을 필요가 있다. 산수의 양 끝값(예: \$9.5T\~\$15T, 절반만 건설 시 \$875B/년) 가운데 어느 쪽을 두는지에 따라 결론의 무게가 크게 달라진다. Bloomberg의 "\$3T" 표기가 단위 오류라는 Zitron의 단언도 1차 자료(Sightline Climate 데이터의 실제 단위)를 직접 보고 다시 확인할 가치가 있다.

## 출처

- 저자: Ed Zitron
- 매체: *Where's Your Ed At* 뉴스레터
- 발행일: 2026-06-08
- 원문: <https://www.wheresyoured.at/ai-is-slowing-down/>
- 본문 차트 출처: FT, John Burn-Murdoch / Demirer et al., *Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools* (2026)
