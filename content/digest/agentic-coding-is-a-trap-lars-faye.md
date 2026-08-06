---
title: "Agentic Coding is a Trap"
date: 2026-05-05T11:05:00+09:00
tags: ["AI", "코딩 에이전트", "인지 부채", "기술 위축"]
categories: ["에이전트와 코딩"]
summary: "에이전틱 코딩이 생산성을 높여주는 대신 개발자의 인지 능력과 비판적 사고력을 잠식하고 있다는 경고. 감독의 역설, 벤더 종속, 우선순위 역전 문제를 짚고 AI를 '보조 프로세스'로 격하하는 워크플로우를 제안한다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Lars Faye가 2026년 4월 에이전틱 코딩의 구조적 함정을 정리한 글이다. 생산성 이면의 인지 부채(cognitive debt)와 기술 위축(skill atrophy)을 핵심 위험으로 지목한다.
2. "감독의 역설" — 코딩 에이전트를 효과적으로 감독하려면 코딩 실력이 필요한데, 에이전트 사용이 바로 그 실력을 퇴화시킨다.
3. 저자는 AI를 '오케스트레이터'가 아닌 '보조 프로세스'로 격하하고, 구현의 주도권을 개발자가 유지하는 워크플로우를 실천하고 있다.

## 에이전틱 코딩의 현주소

> "AI does the coding, and the human in the loop is the orchestrator"

업계에서 유행하는 Spec Driven Development(SDD)는 개발자가 요구사항을 정의하고 계획을 세운 뒤, 에이전트에게 구현을 맡기는 방식이다. 슬롯머신 레버를 당기듯 여러 에이전트 인스턴스를 반복 실행하며, 그 과정에서 "오케스트레이터"와 생성된 코드 사이의 거리는 점점 벌어진다.

저자가 꼽는 정량적 트레이드오프 네 가지:

- AI의 비결정성을 완화하기 위한 **주변 시스템 복잡도 증가**
- 광범위한 인구에 걸친 **기술 위축**
- Claude Code 장애로 팀 전체가 멈추는 **벤더 종속**
- 고정비인 인건비와 달리 끊임없이 변동하는 **토큰 비용**

## "또 다른 추상화"가 아닌 이유

프로그래머가 FORTRAN, 컴파일러, 고수준 언어 등 새로운 추상화를 경계해온 역사가 있다. 하지만 과거의 우려는 추측과 이론에 그쳤다. 이번에는 AI 도구가 등장한 짧은 기간 안에 이미 유의미한 영향이 관측되고 있다는 점이 다르다.

![r/webdev — "AI reliance and cognitive decline." AI 의존과 인지 능력 저하를 걱정하는 개발자 (215 upvotes)](/images/agentic-coding-is-a-trap-lars-faye/skills-01.png)

![r/cscareerquestions — "Letting AI do 100% coding FRIED my brain." 바이브 코딩으로 인지 능력이 망가졌다는 고백 (124 upvotes)](/images/agentic-coding-is-a-trap-lars-faye/skills-02.png)

주니어 개발자만의 문제가 아니다. 10년 이상 경력자도 같은 현상을 보고하고 있다.

![r/webdev — "Handling feeling dumber or like losing skills due to the need of using AI." 9년차 개발자가 회사의 AI 의무 사용 정책 속에서 역량 저하를 호소한다](/images/agentic-coding-is-a-trap-lars-faye/skills-05.png)

![r/ClaudeCode — "Losing my ability to code due to AI." AI를 1년 이상 쓴 뒤 코딩 능력이 퇴화했다는 보고](/images/agentic-coding-is-a-trap-lars-faye/skills-06.png)

주니어 개발자에게는 더 가파른 벽이다. 코드를 직접 작성하는 마찰과 도전이 학습의 절반 이상을 차지하는데, 그것을 코드 리뷰로 대체하면 성장 경로 자체가 잘린다.

![r/cscareerquestions — "juniors on my team ship fast but can't debug anything they didn't actually write." 주니어가 빠르게 배포하지만 자기가 쓰지 않은 코드는 디버깅할 수 없다는 시니어의 증언](/images/agentic-coding-is-a-trap-lars-faye/skills-04.png)

![r/ClaudeAI — "hired a junior who learned to code with AI. cannot debug without it." AI로 코딩을 배운 주니어를 채용했으나 AI 없이는 디버깅이 불가능하다는 보고 (1.6K upvotes)](/images/agentic-coding-is-a-trap-lars-faye/skills-07.png)

## 감독의 역설 (Paradox of Supervision)

Anthropic 자체 연구에서 나온 놀랍도록 솔직한 고백이 핵심을 찌른다:

> "One reason that the atrophy of coding skills is concerning is the 'paradox of supervision'... effectively using Claude requires supervision, and supervising Claude requires the very coding skills that may atrophy from AI overuse"

LinkedIn의 소프트웨어 엔지니어링 디렉터 Sandor Nyako는 50명의 엔지니어 조직에서 이 현상이 퍼지는 것을 목격하고, "비판적 사고나 문제 해결이 필요한 작업"에는 에이전트를 사용하지 말라고 요청했다.

> "To grow skills, people need to go through hardship. They need to develop the muscle to think through problems. How would someone question if AI is accurate if they don't have critical thinking?"

"과도 사용"의 기준이 무엇인지도 아직 정리되지 않았다. 이미 몇 달 만에 기술이 위축된다는 데이터와 일화가 나오고 있다. 이것이 바로 모순의 핵심이다: **코딩 에이전트 사용이 코딩 에이전트를 효과적으로 관리하는 데 필요한 바로 그 역량을 퇴화시킨다.**

## LLM은 잘못된 부분을 가속한다

AI 이전 좋은 개발자의 우선순위:

1. 코드와 코드베이스에 대한 **이해**
2. 문서화된 효율적 표준과의 **정합성**
3. 목표 달성에 필요한 **최소한의 코드**
4. 턴어라운드 타임

에이전틱 코딩은 이 목록을 **완전히 뒤집는다.** 속도와 생성량에 초점을 맞추면서, 깊은 이해와 간결함은 뒷전으로 밀린다. 속도는 높은 역량의 자연스러운 부산물이다. 강제하면 항상 정확도가 떨어진다.

## 코딩 === 기획

간과되는 사실이 있다. 일부 개발자에게 코드를 쓰는 행위 자체가 기획 과정이다.

OpenCode(오픈소스 코딩 에이전트) 제작자 Dax의 말:

> "When working on something new or something challenging, me typing out code is the process by which I figure out what we should even be doing. I have a really tough time just sitting there, writing out a giant spec on exactly how the feature should work."

말하는 것과 의미하는 것은 다르고, LLM은 모호함을 가정(또는 환각)으로 채운다. 결과적으로 **더 많은** 리뷰, **더 많은** 에이전트 수정, **더 많은** 토큰 소모, **더 큰** 단절로 이어진다. 확률적 시스템으로 결정론적 시스템을 대체하면서 모호성 제로를 기대하는 것은 불가능하다.

## 벤더 종속

Claude 장애 때 LinkedIn에 올라온 포스트들이 이를 증명한다. 키보드와 텍스트 에디터만 있으면 가능했던 일이 이제 AI 모델 공급자 구독을 요구하게 되었다.

- 모델 공급자들은 대규모 보조금을 쏟고 있고, 모델은 유동적 기반 위에 있다
- 새 모델 출시마다 높은 벤치마크 → 과대광고 → 현실 사용에서 "너프됐다"는 불만 → 같은 결과를 위해 2\~3배 토큰 소모
- 직원 비용은 알 수 있지만, 토큰 비용은 일/월/연 단위로 예측할 수 없다

Primeagen의 경고:

> "when you use these fully agentic workflows, the model providers essentially own you."

Anthropic의 또 다른 연구는 디버깅 역량의 **47% 하락**을 보여줬다:

> "developers may lean on AI to deliver quick results at the expense of building critical skills — most notably, the ability to debug when things go wrong."

## 저자의 접근법: AI의 역할을 격하하라

저자가 주장하는 것은 수동 코딩 회귀가 아니다. Emmet, 자동완성, 스니펫, jQuery처럼 LLM도 코드 생성 도구의 계보에 속한다. 다만 <strong>보조 프로세스</strong>로 써야 한다는 것이다.

저자의 일일 워크플로우:

- LLM으로 스펙과 계획을 생성하되 **구현은 본인이 주도한다.** 과제에 따라 수동 코딩 비중이 20\~100%.
- 모델에 요청할 때 <strong>의사 코드를 먼저 작성</strong>하여 요청과 생성 코드 사이의 거리를 좁힌다
- 모델을 위임 유틸리티, 인터랙티브 문서, 리서치 도구로 활용한다
- **한 번에 리뷰할 수 있는 양 이상을 생성하지 않는다.** 너무 많으면 속도를 줄이고 작업을 쪼갠다
- 스스로 해본 적 없거나 혼자 할 수 없는 것은 에이전트에 맡기지 않는다 (교육 목적 제외)

> Use them like the Ship's Computer, not Data.

더 빠르지는 않지만 더 나은 품질의 작업을 하고 있다는 것이 저자의 결론이다.

## 가장 흥미로운 지점

소셜 미디어 도입 때와 비슷한 패턴이 보인다. 장기적 영향을 이해하지 못한 채 대규모 실험을 자기 자신에게 수행하고, 뒤늦게 광범위한 주의력 결핍 같은 부작용을 발견하는 구조. 이번에는 주의력이 아니라 **사고력** 자체를 걸고 있다는 점에서 훨씬 위험하다.

Jeremy Howard의 말이 글을 마무리한다:

> "People who go all in on AI agents now are guaranteeing their obsolescence. If you outsource all your thinking to computers, you stop upskilling, learning, and becoming more competent."

## 출처

Lars Faye · 2026년 4월 26일
원문: <https://larsfaye.com/articles/agentic-coding-is-a-trap>
