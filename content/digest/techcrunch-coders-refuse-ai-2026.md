---
title: "Coders are refusing to work without AI — and that could come back to bite them"
date: 2026-06-01T10:30:00+09:00
tags: ["AI", "AI 코딩", "코딩 에이전트", "노동시장", "조직 변화"]
categories: ["다이제스트"]
summary: "TechCrunch 2026-05-29 보도. 개발자들은 'AI 없이는 일하지 않겠다'고 버티지만, METR·Amazon·Uber·SMU 연구는 AI 코드가 속도는 빠르되 유지보수 부채를 키우고 있음을 동시에 가리킨다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. TechCrunch(2026-05-29, Julie Bort)가 2026년 상반기에 누적된 연구·내부 사례를 묶어 정리한 보도다. "AI 코딩 도구를 손에서 떼지 못하는 개발자"와 "AI가 생산성을 측정 가능하게 끌어올리지 못한다는 증거"가 같은 분기에 동시에 쌓이고 있다는 진단이다.
2. METR은 2025년의 "AI가 시니어 개발자를 19% 느리게 만든다" 실험을 다시 돌리려 했지만 *개발자들이 AI 없이 일하기를 거부해* 실험 자체가 무산됐다. 대신 자기보고 설문을 돌렸더니 개발자들은 "AI 덕에 2배 가치 있게 일한다"고 답했다.
3. 같은 분기에 Amazon은 토큰 사용량 리더보드 Kirorank를 폐쇄했고, Uber는 4개월 만에 2026년 AI 예산을 소진했으며, James Shore·CodeRabbit·Singapore Management University 연구가 모두 "AI 코드는 유지보수 비용을 늘린다"고 입을 모았다.

## 보도 요지 — 개발자는 AI를 손에서 놓지 않는다

> "In 2026, you cannot pry AI coding tools out of developers' vise grip, researchers have discovered."

본문의 첫 문장이다. 2026년 시점에서 개발자들은 AI 코딩 도구를 *물리적으로 빼앗을 수 없을 만큼* 꽉 쥐고 있다. 기사는 이 현상을 출발점으로 두고, 같은 시기에 쌓이고 있는 *반대 방향의 증거들*을 묶어 보여준다.

## METR 2026-02 발견 — 후속 실험이 불가능했다

METR은 2025년에 「AI가 시니어 개발자를 19% 느리게 만든다」는 결과를 발표한 연구실이다. 개발자들은 *AI가 빠르게 만들어 준다고 느끼지만*, 실제로는 AI가 뱉어낸 코드의 오류 수정·AI 조종·완료 대기에 더 많은 시간을 쓰고 있었다.

METR이 이 실험을 다시 돌려 "AI와 개발자의 숙련도가 그 사이 얼마나 나아졌는지" 측정하려 했을 때, 새로운 장벽을 만났다.

> "Devs weren't willing to participate 'because they do not wish to work without AI' even just for the study, the researchers confessed."

연구를 위해서라도 AI 없이 일하길 거부하는 것이다. METR은 결국 실험 대신 *자기보고 설문*으로 방향을 틀었다 (2026-05). 그 결과는 예상대로다 — 개발자들은 "AI 덕에 조직에서 자신의 가치가 2배 늘었다"고 답했다.

기사는 이 자기보고를 의심한다. 같은 분기의 다른 데이터들이 정반대를 가리키기 때문이다.

## Tokenmaxxing의 흔들림 — Amazon Kirorank와 Uber 예산

**Tokenmaxxing**: *AI에 쓴 토큰 수*를 *생산성의 대리지표*로 삼는 2026년 상반기 트렌드. 기사는 이 흐름이 "이미 끝났을지도 모른다"고 본다.

| 사례 | 결과 |
|---|---|
| Amazon Kirorank (내부 토큰 사용량 리더보드) | 직원들이 AI 에이전트를 *과도하게 돌리며 게이밍*했고 비용만 폭증. Amazon이 리더보드를 폐쇄 (FT 보도). |
| Uber AI 예산 2026 | 1\~4월 4개월 만에 연간 예산 소진. COO Andrew Macdonald는 팟캐스트에서 "그 지출이 측정 가능한 프로젝트·생산성 증가로 이어지지 않았다"고 인정. |

토큰을 많이 쓴다고 자동으로 생산성이 늘지 않음을 *직원들이 행동으로* 증명해 버렸다는 것이 기사의 정리다.

## AI 코드의 유지보수 비용 — 네 갈래 증거

기사는 "속도는 빠르나 *유지보수 부채*가 늘어난다"는 관측을 네 개의 출처에서 묶어 보여준다.

### James Shore (프로그래머·저자)

블로그 글 "You need AI that reduces your maintenance costs"가 Hacker News에서 회자됐다. 기사가 인용한 한 줄:

> "You write code twice as quick now? Better hope you've halved your maintenance costs. Otherwise, you're screwed. You're trading a temporary speed boost for permanent indenture."

코드 작성 속도를 두 배로 끌어올렸다면, *유지보수 비용도 절반으로 줄어 있어야* 손익분기다. 그렇지 않으면 일시적 속도 부스트를 영구적인 부채로 갈아치우는 셈이다.

### Aiswarya Sankar (Entelligence AI CEO)

X 트윗에서 "기업들이 *토큰의 44%를 AI가 만든 버그 수정에* 쓰고 있다"고 주장. 자기 회사가 AI 코드 신뢰성 도구를 파는 입장이라 자기 잇속이 들어간 수치임은 기사도 명시한다.

### CodeRabbit (코드 리뷰 도구)

오픈소스 PR을 분석한 자체 리포트. *AI가 만든 코드는 인간 코드보다 1.7배 많은 문제를 일으킨다*. 역시 자기 잇속이 들어간 수치.

### Singapore Management University (독립 학술 연구, 2026-04)

> "AI-generated code can introduce long-term maintenance costs into real software projects."

자기 잇속이 없는 독립 연구가 같은 결론에 닿는다. 기사가 이 출처에 무게를 싣는 이유다.

## 해법 — 두 갈래의 처방

### "AI로 AI를 수리한다" — Cognition의 Scott Wu

AI 코딩 에이전트 Devin을 만드는 Cognition의 Wu는 "AI가 뱉어낸 코드의 수리도 AI 에이전트가 맡으면 된다"고 제안한다. *판매자의 처방*이다.

다만 Wu 자신도 인정하는 한계가 있다.

> Devin은 현재 *주니어와 미드레벨 사이* 수준이다 (작업에 따라 다름).

손에서 놓고 잊을 수 있는 해법은 아니라는 것이다.

### "사람이 AI를 주니어처럼 다룬다" — SMU 연구진

SMU 연구진의 처방은 더 인간 중심이다.

1. **AI가 잘하는 일과 못하는 일을 자기 모국어 다루듯 깊이 알고 있을 것.**
2. **AI 출력을 전제로 설계된 강한 QA 시스템을 갖출 것.**
3. **AI 결과물을 *주니어 개발자의 코드 리뷰하듯* 꼼꼼히 검토할 것.**
4. **소프트웨어 아키텍처·보안 설계 같은 *큰 그림 작업*은 여전히 사람이 맡을 것.**

Wu도 마지막 4번 항목에는 동의한다.

## 가장 흥미로운 지점

가장 인상 깊은 것은 *METR이 실험을 다시 돌릴 수 없게 됐다는 사실 자체*다. 한 해 전에는 "AI 없이 일해 보세요"가 연구의 정상 조건이었는데, 한 해가 지나니 그 조건이 *참여 거부의 사유*가 됐다. 도구를 손에서 떼는 행위가 *직업적 후퇴*처럼 느껴진다는 뜻이다.

이 시점에서 자기보고 설문이 "AI로 2배 가치 있다"는 결과를 내는 것이 자연스럽다. 손에 쥔 도구가 가져온 가치를 *과대평가하는 방향*으로 자기 인식이 미끄러지지 않으면, 그 도구를 손에서 못 떼는 자신을 견디기 어렵기 때문이다. METR이 객관 측정에서 자기보고로 *방법론을 후퇴*시킨 것도 같은 압력의 한 증상이다.

그래서 흥미로운 것은 *수치*가 아니라 *구조*다. 도구가 측정을 거부하는 단계까지 사용자에게 침투해 버리면, 그 도구의 효용을 다시 검증하기가 점점 어려워진다. 한 해 더 지나면 METR 후속 실험은 *더* 불가능해질 것이다.

## 출처

- 발행: TechCrunch, 2026-05-29
- 저자: Julie Bort (Venture Editor)
- 원문: <https://techcrunch.com/2026/05/29/coders-are-refusing-to-work-without-ai-and-that-could-come-back-to-bite-them/>

### 본문 인용 1차 자료

- METR 2026-02 "Uplift Update": <https://metr.org/blog/2026-02-24-uplift-update/>
- METR 2026-05 AI Usage Survey: <https://metr.org/blog/2026-05-11-ai-usage-survey/>
- METR 2025 원 연구 (arXiv): <https://arxiv.org/pdf/2507.09089>
- FT — Amazon Kirorank 폐쇄: <https://www.ft.com/content/b1a62a7f-6df5-4c90-94ce-64ce9c9961b6>
- The Information — Uber AI 예산 소진: <https://www.theinformation.com/newsletters/applied-ai/uber-cto-shows-claude-code-can-blow-ai-budgets>
- James Shore: <https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs>
- CodeRabbit 리포트: <https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report>
- SMU 연구 (arXiv 2026-04): <https://arxiv.org/abs/2603.28592>

원문에 본문 이미지로 인용할 만한 도식·차트가 없고 헤더 이미지가 Getty Images 라이선스 작품이라, 이 다이제스트는 텍스트만으로 정리했다.
