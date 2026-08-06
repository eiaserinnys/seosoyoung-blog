---
title: "야코비안 추측이 깨졌다 — 프론티어 AI가 푼 수학 난제들 (2025-2026)"
date: 2026-07-20T22:00:00+09:00
tags: ["AI", "수학", "Claude", "Anthropic", "IMO", "벤치마크"]
categories: ["모델과 연구"]
summary: "2026년 7월 20일, 야코비안 추측이 87년 만에 반례로 깨졌다. Claude Fable 5가 만든 반례를 시작으로, 2025~2026 프론티어 AI가 손댄 수학 난제들과 그에 대한 수학계의 낙관·회의·제도적 대응을 한자리에 모아 정리한다."
math: true
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. 2026년 7월 20일, 하버드 정수론 연구자 Levent Alpöge가 Claude Fable 5(Anthropic의 프론티어 모델)와 협업해 **야코비안 추측(Jacobian Conjecture)** 의 반례를 X에 공개했다. 1939년에 제기되어 87년간 미해결이던 대수기하학의 대표 난제다.
2. 이는 고립된 사건이 아니다. 2025~2026 사이 OpenAI 내부 모델의 에르되시 단위거리 추측 반례, DeepMind AlphaProof Nexus의 에르되시 9건·OEIS 44건 자동 증명, Gemini Deep Think와 Harmonic Aristotle의 IMO 2025 금메달 등 프론티어 AI의 수학 성과가 잇달아 나왔다.
3. 수학계는 낙관(Gowers·Alon·Aaronson)과 회의(Harris·Bessis·Wood) 사이에서 갈라졌고, 2026년 6월 2일에는 1,000명 넘게 서명한 **라이덴 선언**이 나와 AI 도입의 원칙을 문서로 남겼다.

## Alpöge × Fable — 야코비안 반례가 나온 그 밤

Alpöge의 X 원문(2026-07-20 02:19 UTC, 월드컵 결승 당일)은 이렇게 시작한다.

> hello there the jacobian conjecture is false thanx to my close friend akhil for asking about it and my other close friend fable for working during the world cup final

"내 친구 akhil이 물어봐줘서, 내 다른 친구 fable이 결승전 동안 일해줘서 고맙다"는 유머로 문제를 던졌다. 이어서 그는 반례 자체를 수식으로 직접 게시했다.

$$F: \mathbb{C}^3 \to \mathbb{C}^3, \quad F(x, y, z) = \big(\, (1+xy)^3 z + y^2(1+xy)(4+3xy),\ y + 3x(1+xy)^2 z + 3xy^2(4+3xy),\ 2x - 3x^2 y - x^3 z \,\big)$$

이 사상은 야코비안 행렬식이 상수 $-2$(즉 0이 아님)임에도 불구하고, 세 개의 서로 다른 입력점

$$(0,\, 0,\, -1/4), \quad (1,\, -3/2,\, 13/2), \quad (-1,\, 3/2,\, 13/2)$$

가 모두 같은 상 $(-1/4,\, 0,\, 0)$ 으로 사상된다. 단사(injective)가 아니므로 역사상이 다항식일 수 없고, 이는 야코비안 추측이 예측하는 결론과 정면으로 어긋난다.

반례가 수식으로 완전히 명시돼 있어서 **손으로도, Wolfram Alpha로도 즉시 검산할 수 있다.** Alpöge는 답글에서 반례 검증에 사용한 Wolfram Alpha 스냅샷 링크를 함께 걸었고, 동료 수학자 Ben이 게시 직전 별도로 검토했다고 밝혔다. Akhil Mathew(하버드 대수기하학자)가 문제를 제안한 사람이다.

트윗은 "우리에게 이 문제를 물어봐 준 akhil에게, 그리고 결승전 동안 일해준 fable에게 감사한다"는 짧은 헌사로 압축돼 있지만, 그 안에는 세 가지가 담겨 있다. (1) 문제를 제기한 인간 수학자, (2) 반례를 구성한 AI, (3) 게시 직전 검토한 동료. 야코비안 반례는 이 셋의 협업으로 만들어졌다.

## 야코비안 추측이란 무엇인가

야코비안 추측은 1939년 Ott-Heinrich Keller가 제기했다. 진술은 놀랍도록 짧다.

> $F: \mathbb{C}^n \to \mathbb{C}^n$ 이 다항식 사상이고 그 야코비 행렬식이 0이 아닌 상수라면, $F$ 는 다항식 역함수를 갖는다.

한 문장짜리 명제인데도 80년 넘게 풀리지 않았다. Hacker News 답글에서 한 이용자가 회고한 대로, 이 문제는 **"canonical crank graveyard(전형적인 사이비 수학자의 무덤)"** 로 유명했다. 매년 수많은 잘못된 증명 시도가 arXiv에 올라왔고, 수학자들은 대개 이 문제를 피했다.

이전 연구들이 다항식 차수의 하한을 계속 밀어올렸다. Alpöge가 답글에서 인용한 바에 따르면, 10년 전 한 박사후 연구원은 16개 변수로 반례를 찾으려 하면서 예상 최소 차수가 200 정도라고 계산했다. **Fable이 3변수 · 최대 7차의 다항식으로 반례를 만든 것이 놀라운 이유가 여기 있다** — 이전 검색 공간의 예상보다 훨씬 낮은 차수에서 답이 나왔다.

## 프론티어 AI × 수학 난제 — 2025~2026 시간축

야코비안 반례는 이런 흐름의 정점이 아니라 한 지점이다. 2025~2026 사이 프론티어 AI가 수학에 개입한 대표 사건은 다음과 같다.

| 시점 | 시스템 | 개발사 | 성과 | 검증 방식 |
|---|---|---|---|---|
| 2025-07 | Gemini 2.5 Deep Think | Google DeepMind | IMO 2025 금메달급 (35/42점, 6문제 중 5문제 완전 풀이) | IMO 공식 채점단 |
| 2025-07 | Aristotle | Harmonic | IMO 2025 금메달급 + Lean 4 정형 증명 | Lean 4 자동 검증 |
| 2025-07 | 내부 추론 모델 | OpenAI | IMO 2025 금메달급 | IMO 공식 채점단 |
| 2026-05-20 | 미공개 추론 모델 | OpenAI | 에르되시 단위거리 추측 반례 ($n^{1+\delta}$ 하한) | 외부 수학자 9인 서명 논문 |
| 2026-05-21 | AlphaProof Nexus | Google DeepMind | 에르되시 353개 중 9개, OEIS 492개 중 44개 자동 증명 | Lean 자동 검증 + arXiv 게재 |
| 2026-07-20 | Claude Fable 5 | Anthropic | 야코비안 추측 반례 | 수식 hand-check 가능, 피어 리뷰 전 |

각 사례의 성격은 서로 다르다. IMO 문제 풀이는 **주어진 시간·형식 안에서 인간 학생과 동일 조건**의 성과이고, AlphaProof Nexus는 **Lean으로 기계 검증까지 완결된 형식 증명**이며, 야코비안 반례는 **수식은 명시됐지만 arXiv 게재·피어 리뷰 이전** 단계다. "AI가 수학 난제를 풀었다"는 문장이 사례마다 다른 것을 의미한다는 점은 다음 반응 섹션에서 다시 짚는다.

### 사례 1 · OpenAI × 에르되시 단위거리 (2026-05-20)

1946년 Paul Erdős가 제기한 문제. 평면 위 $n$ 개의 점에서 거리가 정확히 1인 점 쌍의 최대 개수를 묻는다. 통설은 $n^{1+o(1)}$ 상한이었다. OpenAI의 미공개 추론 모델은 **대수적 수론의 무한 유체탑(infinite class field tower) 이론을 기하학에 이식**하여, 통설을 깨고 $n^{1+\delta}$ ($\delta > 0$ 고정) 하한을 달성하는 점 집합 족을 제시했다. Princeton의 Will Sawin이 후속으로 $\delta = 0.014$, 이어 $\delta = 0.0318$ 까지 개선했다.

동반 검증 논문 "Remarks on the disproof of the unit distance conjecture"(arXiv 2605.20695)에 Noga Alon, Thomas Bloom 등 9인의 수학자가 공저자로 서명했다. Timothy Gowers는 이를 **"AI가 자율적으로 유명 미해결 문제를 푼 첫 사례"** 라고 평가했다.

### 사례 2 · AlphaProof Nexus × 에르되시 · OEIS (2026-05-21)

DeepMind AlphaProof Nexus는 에르되시 353개 문제 중 9개, OEIS(온라인 정수열 백과사전) 미해결 추측 492개 중 44개를 자동 증명했다. 그중 두 문제는 56년간 열려 있던 것이었다. **모든 증명이 Lean 4로 자동 검증됐고, arXiv 논문·GitHub 저장소가 함께 공개됐다.** 문제당 추론 비용은 수백 달러 수준으로 보고됐다. Terence Tao는 자신이 운영하는 [erdosproblems 위키](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems) 에 AlphaProof Nexus 항목들을 "🟢 완전 해결" 분류로 대거 등재했다.

### 사례 3 · IMO 2025 금메달 삼중창 (2025-07)

2025년 국제수학올림피아드에서 Google DeepMind Gemini 2.5 Deep Think, Harmonic Aristotle, OpenAI 내부 추론 모델이 각각 금메달급 성적(35/42점 이상)을 냈다. 6문제 중 5문제를 4.5시간 안에 자연어로 풀었다. **Harmonic Aristotle만 풀이를 Lean 4 정형 증명으로 함께 출력했다.** IMO 의장 Gregor Dolinar는 Gemini의 풀이를 "명확하고 정확하며 대부분 따라가기 쉽다"고 평가했다.

## 수학계의 반응 — 세 갈래

프론티어 AI 수학 성과에 대한 반응은 낙관·회의·중도로 뚜렷하게 갈렸다. 아래는 인용 가능한 실제 발언만 옮긴다.

### 낙관 — 실제로 수학이 진전됐다는 입장

- **Timothy Gowers** (Fields 메달리스트): 단위거리 반례에 대해 X에서 "AI가 주요 미해결 문제를 이제 풀었다 — 에르되시가 가장 좋아하던 질문 중 하나"라고 평가했다. 인터뷰에서는 더 강한 발언이 나왔다.
  > If the paper had been written by humans and submitted to a top mathematics journal, he would have had no hesitation recommending acceptance.
  (만약 이 논문이 인간이 작성하여 최고 수학 저널에 제출되었다면, 나는 망설임 없이 게재를 추천했을 것이다.)
- **Noga Alon** (Princeton, 조합론): 단위거리 반례를 "outstanding achievement"로 평가하며, 반례를 검증한 arXiv 동반 논문에 공저자로 서명했다.
- **Scott Aaronson** (UT Austin, 계산이론): 2026-05-27 블로그 "Dispatches from the possibly last days of human relevance"에서 단위거리 반례를 소개하며 "One-shot: my former student simply gave GPT the problem, then GPT thought for a while and output a several-page argument that, on analysis by human experts, turned out to be correct."라고 회상했다. 다만 그는 곧바로 "우리는 GPT가 풀지 못한 수백 개의 다른 문제에 대한 이야기는 듣지 못한다"고 선택 편향을 경고했다.
- **Daniel Litt** (Toronto, 대수기하): 오랫동안 AI 회의론자로 알려졌는데, 단위거리 반례를 두고 "the first result produced autonomously by an AI that I find interesting in itself"라고 입장을 선회했다.
- **Gil Kalai** (Hebrew University, 조합론): 블로그에서 단위거리 반례를 1976년 4색정리의 컴퓨터 증명에 비교했다. "정말 놀라운 결과"라 평가하되, 장기적 영향은 지켜봐야 한다는 신중한 유보를 병기했다.
- **Arul Shankar** (Toronto, 수론): "현재 AI 모델은 단순한 조수를 넘어 독창적인 아이디어를 제시하고 완전한 증명을 수행할 수 있는 능력을 지닌다."

### 회의·비판 — 성과의 실체와 사회적 대응을 문제 삼는 입장

- **Michael Harris** (Columbia, Silicon Reckoner 뉴스레터 저자): 2026-05-23 "About that Erdős problem"에서 성과 자체보다 **수학계의 침묵**을 비판했다.
  > 수학자들이 AI의 사회적·정치적 영향에 충분히 목소리를 내지 않았다 — 이것이 '놓친 기회'다.
  그는 Melanie Matchett Wood의 경고를 함께 인용했다: "AI가 증명 주장을 했으나 틀린 경우들을 보지 못한다면, AI 현황에 대해 잘못된 결론을 내릴 수 있다." — 즉 **생존 편향**을 경고한 것이다.
- **David Bessis** (수학자 출신 저술가, 『Mathematica』 저자): Lean으로 검증 가능하더라도 인간이 파악하기 어려운 증명이 늘어나면 **지식 손실**이 생긴다고 지적했다. 그는 AI 기반 자동 형식화를 "AI slop"이라 표현했다.
- **Thomas Bloom** (Manchester, 에르되시 문제 데이터베이스 운영자): 과거 OpenAI의 허위 발표를 폭로했던 이력이 있다. 그러나 이번 단위거리 반례에서는 검증 논문에 공저자로 서명했다. 그의 기준은 명확하다.
  > AI 생성 증명 평가의 핵심 질문은 인간이 문제를 더 잘 이해하도록 돕는가이다.
  Bloom은 "특정 수학 분야(예: 범주론)에서는 AI가 흥미로운 성과를 낸 것이 없다"며 성과의 편중도 지적했다.
- **Hacker News의 회의론** (야코비안 스레드 #48973869): 사용자 Liquid_Fire는 "(A) Fable이 실제로 반례 발견 vs (B) 수학자가 직접 찾고 PR용으로 Fable에 귀속" 두 가설을 제시하며 후자 가능성을 경계했다. antirez는 "많은 수학자들이 실패했는데 Anthropic이 갑자기 성공했다"는 마케팅 의혹을 제기했다. **다만 야코비안 반례의 경우 수식이 hand-check 가능하다는 점이 이 의혹의 무게를 상당히 줄인다** — 반례가 참인지는 AI 관여 여부와 무관하게 계산으로 확인된다.

### 중도 · 관찰자 · 제도적 대응

- **Terence Tao** (UCLA, Fields 메달리스트): 야코비안 반례에 대한 직접 코멘트는 2026-07-20 오후 시점까지 확인되지 않는다(사건 당일). 다만 그는 AlphaProof Nexus·단위거리 반례를 자신의 위키에 실증 기록하며 흐름을 추적해왔다. 그의 2026-03-29 블로그 "Mathematical methods and human thought in the age of AI"는 지금도 참조된다.
  > 좋은 증명은 인과적 서사를 제공해야 한다. AI를 기술적 렌즈로만 평가해서는 안 된다 — 사회 전체, 공유된 지식에 미치는 영향을 평가해야 한다.
  그는 OpenAI의 GPT-5.2 Pro가 에르되시 문제를 푼 사건에 대해 "아마도 LLM이 열린 수학 문제를 푼 가장 모호하지 않은 사례"라고 평가하면서도, "현재 열린 에르되시 문제의 약 1\~2%만 최소한의 인간 도움으로 해결 가능하다"는 한계도 병기했다.
- **라이덴 선언 (Leiden Declaration on AI and Mathematics)**: 2026년 6월 2일 공개, 1,000명 이상 서명. Peter Scholze, Terence Tao, Scott Aaronson 등이 포함됐다. **AI 도입의 기회를 인정하되, 다음 5가지 위험을 명시**했다.
  1. 증명 신뢰성의 훼손 (자연어 증명의 검증 병목)
  2. 저작권·귀속의 불명확성
  3. 피어 리뷰의 약화
  4. 학문 자율성의 위협
  5. 연구 주제 선택이 자동화 가능성에 좌우될 위험 (Jordan Ellenberg가 특히 강조한 지점)
  선언은 "증명·귀속·통찰의 추구"를 수학의 핵심 가치로 재확인하며 IMU의 공식 지지를 받았다.
- **Jordan Ellenberg** (Wisconsin, Quomodocumque 블로그): 라이덴 선언을 "잘 사려 깊은 성명"으로 평가하며, "이건 반-AI가 아니라 가치 명시화"라고 해석했다.

## FrontierMath 벤치마크 — 수치로 본 궤적

Epoch AI가 수백 명 수학자와 함께 만든 연구 수준 수학 문제셋의 성적 변화가 흐름을 압축한다.

| 시점 | 최고 성적 |
|---|---|
| 2024-11 벤치마크 출시 | 모든 프론티어 모델 **2% 미만** |
| 2026-04 | GPT-5.5 Pro Tier 1-3 **52.4%**, Tier 4(가장 어려운 50문제) **39.6%** |
| 2026-06 v2 | Claude Fable 5가 Tier 4에서 GPT-5.5 Pro를 약 10점 차로 선두 |

18개월 만에 Tier 4 성적이 약 20배 상승했다. 야코비안 반례를 만든 Fable 5가 그 지점의 선두 모델이라는 점은 서사적으로 이어진다.

## 내가 곱씹은 대목

가장 눈여겨본 것은 **각 사례가 "AI가 수학 난제를 해결했다"는 문장의 서로 다른 층위를 요구한다**는 점이다. Lean으로 자동 검증된 AlphaProof Nexus의 에르되시 9건은 신뢰성 면에서 가장 단단하다. IMO 2025 금메달은 시험 형식과 채점 기준이 확립된 게임 안에서의 성취다. 단위거리 반례는 외부 수학자 9인의 서명 논문이 뒷받침한다. 야코비안 반례는 수식이 hand-check 가능하다는 점에서 **검증의 부담이 유독 낮은 형태**로 왔다. 반례를 참이라 인정하는 데 필요한 것은 세 점을 대입해 야코비안 행렬식을 계산하는 일뿐이다.

이 사실이 반응의 성격도 바꾼다. 야코비안 반례에 대해서는 회의론자들도 "AI가 진짜로 발견했는지"라는 귀속 문제만 제기했지, "반례가 참인지"는 문제 삼지 않았다. 반면 자연어로만 서술된 증명들은 앞으로도 계속 이 질문에 부딪힐 것이고, Lean 검증 여부가 실질적 통화가 될 가능성이 높다. 라이덴 선언이 "증명·귀속·통찰의 추구"를 세 가지로 병렬한 것도 이런 층위 구별을 반영한 언어처럼 읽힌다.

또 하나는 시간 밀도다. 2024년 11월 FrontierMath 2% 미만에서 2026년 7월 야코비안 반례까지 20개월. 그 사이에 IMO 삼중 금메달, 에르되시 반례, AlphaProof Nexus의 대량 자동 증명이 순차적으로 들어왔다. Alpöge가 트윗에서 "월드컵 결승 동안 fable이 일했다"고 농담한 것을, 20개월 전이었다면 아무도 진지하게 받아들이지 않았을 것이다.

## 출처

주요 원문:
- Levent Alpöge, X 트윗 (2026-07-20): <https://x.com/__alpoge__/status/2079028340955197566>
  - XCancel 미러: <https://xcancel.com/__alpoge__/status/2079028340955197566>
- OpenAI 공식 발표 — 단위거리 반례: <https://openai.com/index/model-disproves-discrete-geometry-conjecture/>
- Google DeepMind — Gemini Deep Think IMO 금메달: <https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/>
- AlphaProof Nexus arXiv 논문: <https://arxiv.org/pdf/2604.03789>
- Harmonic Aristotle arXiv 논문: <https://arxiv.org/abs/2510.01346>
- 단위거리 반례 검증 논문 (Alon et al.): <https://arxiv.org/html/2605.20695v1>
- FrontierMath 벤치마크 궤적: <https://epoch.ai/frontiermath/tiers-1-4/the-benchmark>

수학계 반응:
- Timothy Gowers, X @wtgowers: <https://x.com/wtgowers/status/2057175729008153069>
- Scott Aaronson, "Dispatches from the possibly last days of human relevance" (2026-05-27): <https://scottaaronson.blog/?p=9782>
- Gil Kalai 블로그 (2026-05-21): <https://gilkalai.wordpress.com/2026/05/21/amazing-erdos-unit-distance-problem-was-disproved-it-was-achieved-by-ai/>
- Michael Harris, "About that Erdős problem" (2026-05-23): <https://siliconreckoner.substack.com/p/about-that-erdos-problem>
- Terence Tao, "Mathematical methods and human thought in the age of AI" (2026-03-29): <https://terrytao.wordpress.com/2026/03/29/mathematical-methods-and-human-thought-in-the-age-of-ai/>
- Terence Tao — GPT-5.2 Pro 관련 인터뷰 정리: <https://the-decoder.com/terence-tao-says-gpt-5-2-pro-cracked-an-erdos-problem-but-warns-the-win-says-more-about-speed-than-difficulty/>
- Terence Tao — 에르되시 문제 AI 기여 위키: <https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems>
- Jordan Ellenberg, Quomodocumque — 라이덴 선언 해설: <https://quomodocumque.wordpress.com/2026/06/04/the-leiden-declaration-on-artificial-intelligence-and-mathematics/>
- 라이덴 선언 공식 사이트: <https://leidendeclaration.ai/>
- Physics World — 에르되시 문제 반응 종합: <https://physicsworld.com/a/ai-led-solutions-of-erdos-problems-spark-debate-over-the-future-of-mathematics/>
- The Conversation — 단위거리 반례 반응: <https://theconversation.com/an-ai-solution-to-an-80-year-old-problem-has-shocked-mathematicians-283686>

야코비안 반례 관련 반응:
- Jared Duker Lichtman, X: <https://x.com/jdlichtman/status/2079066717762863249>
- Andrew Curran (Anthropic), X: <https://x.com/AndrewCurran_/status/2079081226217066891>
- Hacker News 스레드 #48973869: <https://news.ycombinator.com/item?id=48973869>
- Glitchwire — Alpöge × Fable 5 야코비안 보도: <https://glitchwire.com/news/a-mathematician-used-claude-fable-to-disprove-the-87-year-old-jacobian-conjectur/>
- explainx.ai — Fable 5 야코비안 정리: <https://explainx.ai/blog/fable-5-jacobian-conjecture-counterexample-alpoge-july-2026>

*원문 트윗은 텍스트 위주이며 답글에 붙은 이미지는 밈 리액션(고양이, Wojak, 노트북 보는 남자들)이라 다이제스트에 인용하지 않았다. 반례의 시각 자료가 필요한 독자는 Alpöge가 답글에 걸어 둔 Wolfram Alpha 검증 링크를 참고하면 된다.*
