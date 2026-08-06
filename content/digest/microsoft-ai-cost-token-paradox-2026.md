---
title: "Microsoft reports are exposing AI's real cost problem"
date: 2026-05-23T10:00:00+09:00
tags: ["AI", "AI 비용", "토큰 경제학", "IPO", "LLM"]
categories: ["AI 산업"]
summary: "Fortune이 마이크로소프트의 Claude Code 라이선스 회수와 Uber의 4개월 AI 예산 소진을 짚으며, 토큰 단가 하락에도 총비용은 오히려 오르는 패러독스를 보도했다. HedgieMarkets는 이 패러독스가 결국 OpenAI·Anthropic의 18-24개월 IPO 타임라인이 강요하는 가격 전가라고 해석한다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/microsoft-ai-cost-token-paradox-2026/cover-nadella.webp"
images:
  - "/images/microsoft-ai-cost-token-paradox-2026/cover-nadella.webp"
sidenotes: true
---

## 3줄 요약

1. Fortune은 마이크로소프트가 사내 Claude Code 라이선스를 대부분 회수하고 GitHub Copilot CLI로 이주시키고 있다고 보도했다. Uber는 2026년 AI 코딩 도구 예산을 단 4개월 만에 모두 소진했다.
2. 엔비디아 Bryan Catanzaro는 "내 팀에서 컴퓨트 비용이 직원 비용을 한참 넘어선다"고 말했다. Gartner는 2030년이면 1조 파라미터 LLM의 추론 단가가 2025년 대비 약 90% 떨어지겠지만, 에이전트 모델이 더 많은 토큰을 쓰기 때문에 기업의 총 추론 비용은 오히려 상승한다고 예측한다.[^gartner-2030]
3. HedgieMarkets는 이 모든 가격 인상이 "IPO 타이밍 이슈"라고 진단했다. OpenAI·Anthropic·xAI는 18\~24개월 안에 상장해야 하고, S-1을 제출하기 전에 손실 곡선이 꺾이는 모습을 보여야 하기 때문에 비용 전가가 지금 가속된다는 것이다.

![Satya Nadella, Microsoft CEO. Sven Hoppe/picture alliance via Getty Images](/images/microsoft-ai-cost-token-paradox-2026/cover-nadella.webp)

## 마이크로소프트의 Claude Code 후퇴

The Verge 보도에 따르면 마이크로소프트는 사내 직접 Claude Code 라이선스를 대부분 취소하고, 자사 GitHub Copilot CLI로 엔지니어들을 옮기고 있다. 이 결정은 사내 액세스를 처음 연 지 *불과 6개월* 만에 나왔다. 수천 명의 개발자·PM·디자이너가 코딩 실험에 활용하면서 도구가 너무 빨리, 너무 깊이 자리 잡았다는 것이 핵심 부담이다.[^microsoft-discontinues]

다만 이번 회수가 마이크로소프트의 더 큰 Anthropic 관계를 흔드는 것은 아니다. Foundry 딜로 묶인 50억 달러 투자, Foundry 고객의 Claude 모델 접근, 그리고 Anthropic의 300억 달러 Azure 컴퓨트 약정은 모두 그대로 유지된다. 사내 사용권만 끊은 것이다.

Uber도 비슷한 그림이다. CTO Praveen Neppalli Naga는 The Information에 회사가 2026년 AI 코딩 도구 예산 전체를 단 4개월 만에 태웠다고 밝혔다. Uber는 직전까지 사내 리더보드로 팀별 AI 사용량을 줄 세워가며 적극적으로 채택을 부추기던 회사였다.[^uber-cto]

## "토큰맥싱"의 역설 — 권장이 곧 청구서다

Fortune은 같은 흐름을 메타·아마존에서도 짚는다. 메타에서는 직원이 사내 AI 사용량 리더보드 *"Claudeonomics"* 를 만들었고, 아마존은 직원들에게 *"tokenmaxx"* — 즉 토큰을 최대한 많이 쓰라 — 를 권장하는 캠페인을 돌렸다. 토큰 기반 가격제 아래서는 *효율적으로, 더 많이 쓸수록* 청구서가 커진다는 단순한 사실을 권장 캠페인이 가린다.

Goldman Sachs는 2030년까지 에이전틱 AI 도입으로 토큰 소비가 24배 증가하여 월 *120 quadrillion(12경)* 개에 이를 것이라 전망한다. 단가가 떨어져도 총소비량이 그를 추월하면 청구서는 위로 간다.[^goldman-2030]

Gartner의 메시지는 더 직접적이다.

> "Chief Product Officers (CPOs) should not confuse the deflation of commodity tokens with the democratization of frontier reasoning."
>
> — Will Sommer, Gartner senior director analyst

Gartner가 짚는 세 가지 이유가 있다.
1. 에이전트 모델은 같은 작업에 표준 모델보다 *훨씬 더 많은* 토큰을 쓴다.
2. 소비 증가 속도가 단가 하락 속도를 앞지를 가능성이 높다.
3. AI 공급자가 단가 하락을 *전부 고객에게* 넘겨주지는 않는다.

엔비디아의 Bryan Catanzaro는 이 그림을 한 문장으로 압축했다.

> "For my team, the cost of compute is far beyond the costs of the employees."

엔비디아 CEO Jensen Huang은 미래에 *직원 한 명당 100개의 AI 에이전트*가 함께 일할 것이라 말한 바 있다. 단가 하락이 토큰 소비 폭증을 따라가지 못하면, 그 미래는 경영진이 예상한 것보다 훨씬 큰 청구서를 동반한다.

## HedgieMarkets의 해석 — "이건 IPO 타이밍 이슈다"

같은 Fortune 기사를 인용하면서 HedgieMarkets가 X에 올린 분석은 한 단계 더 들어간다. 그의 진단은 토큰 가격 인상이 *기술적 한계*나 *공급 부족*이 아니라 *상장 일정*에 의해 강요된다는 것이다.

![HedgieMarkets의 분석 캡션 이미지](/images/microsoft-ai-cost-token-paradox-2026/hedgie-summary.jpg)

핵심 수치를 정리하면 다음과 같다.

| 지표 | 값 | 비고 |
|---|---|---|
| OpenAI 2026 예상 적자 | 약 140억 달러 | 매출 1달러당 약 2달러 지출 |
| Anthropic 손익분기 시점 | 2028년 전망 | 비슷한 적자 구조 |
| 엔비디아 Blackwell GPU 렌탈 단가 | 두 달간 +48% | 컴퓨트 수요 폭증 |
| OpenAI 최근 사모 펀딩 | 1,220억 달러 | 평가액 8,520억 달러(역대 최대) |

HedgieMarkets의 논리는 이렇게 흐른다.

> "The token pricing story is really an IPO timing story. OpenAI, Anthropic, and xAI all need to go public in the next 18 to 24 months because the private market cannot keep absorbing burn rates like these indefinitely."

> "Public markets do not accept 'we will figure it out' as a line item on an S-1, they require disclosed unit economics with a credible path to profitability and a date attached. That deadline is why the price increases are happening now rather than next year."

요약하면 — *지난 2년 동안 기업이 산 모든 토큰은 사실상 VC 자본과 하이퍼스케일러 교차 보조금으로 원가 이하에서 팔린 것*이고, 그 보조금에는 만기일이 있다. 랩들은 S-1에 *손실이 줄어드는 그래프*를 그려 넣어야 하기에, 적자 곡선을 꺾는 일은 기업 고객 청구서를 통해 일어날 수밖에 없다.

> "The labs cannot keep losing $2 per dollar of revenue once they file public statements, so the cost transfer to customers accelerates from here. For investors, the question is not whether these companies are valuable. They clearly are. The question is who absorbs the difference between what enterprises can budget and what the models actually consume between now and 2028, and right now the answer is the hyperscalers funding the buildout."

그래서 HedgieMarkets는 랩의 가격 발표보다 *마이크로소프트와 아마존의 capex 코멘터리*를 더 면밀히 본다고 덧붙인다 — 누가 차액을 흡수하는지가 진짜 질문이라는 것이다.

## 가장 흥미로운 지점

세 가지 이야기가 같은 그림의 다른 면이라는 점이 흥미롭다.

**첫째,** 사내 캠페인의 모순이다. 메타의 "Claudeonomics", 아마존의 "tokenmaxx", Uber의 사용량 리더보드는 모두 AI 사용을 *권장*하는 도구였지만, 토큰 단가 체계 아래서는 *권장 = 청구서 폭증*이다. Uber가 4개월 만에 예산을 다 태웠다는 사실은 이 캠페인이 작동했다는 증거이자, 작동하면 안 되는 방식으로 작동했다는 증거다.

**둘째,** Gartner의 경고와 HedgieMarkets의 진단이 같은 곳을 가리킨다는 점이다. Gartner는 *"공급자가 단가 하락을 고객에 전부 전가하지 않는다"* 고 말한다. HedgieMarkets는 *"S-1 마감 때문에 그렇게 못 한다"* 고 말한다. 첫째는 시장 구조의 문제, 둘째는 자본 시장 일정의 문제로 보이지만, 결국 *기업 고객이 예산으로 흡수 가능한 금액*과 *모델이 실제로 소비하는 컴퓨트* 사이의 간극을 누가 메우느냐의 같은 질문이다.

**셋째,** 마이크로소프트의 결정이 가장 직접적인 시그널이다. Claude Code 사내 라이선스를 회수하면서도 Anthropic에 50억 달러를 투자하고 Azure 컴퓨트 300억 달러 약정은 유지하는 결정은 — 도구가 가치가 없어서가 아니라, *비용을 흡수할 주체가 마이크로소프트 본사 IT 예산이어서는 안 된다* 는 판단으로 읽힌다. 차액을 흡수하는 주체가 누구인지가 진짜 질문이라는 HedgieMarkets의 관전 포인트가, 마이크로소프트 본사 IT 부서의 결재 라인에서 가장 먼저 작동한 셈이다.

## 출처

원문 기사: Jake Angelo, *"Microsoft reports are exposing AI's real cost problem: Using the tech is more expensive than paying human employees"*, Fortune, 2026-05-22
원문 URL: <https://fortune.com/2026/05/22/microsoft-ai-cost-problem-tokens-agents/>

확장 분석: HedgieMarkets (@HedgieMarkets), X, 2026-05-22
트윗 URL: <https://x.com/hedgiemarkets/status/2057975295442116889>

[^microsoft-discontinues]: The Verge, *"Microsoft discontinues Claude Code, returns to Notepad"* (Microsoft의 Claude Code 회수 보도)
[^uber-cto]: The Information, *"Uber CTO Shows Claude Code Can Blow AI Budgets"* (Uber 사례)
[^gartner-2030]: Gartner 리서치 (2030년 추론 단가 전망)
[^goldman-2030]: Goldman Sachs (2030년 토큰 소비 24배 증가 전망)
