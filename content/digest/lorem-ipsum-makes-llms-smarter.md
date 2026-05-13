---
title: "Lorem Ipsum Makes LLMs Smarter. No, Seriously."
date: 2026-05-13T10:00:00+09:00
tags: ["LLM", "RL", "exploration", "prompt-engineering"]
categories: ["다이제스트"]
summary: "GRPO RL 훈련의 zero-advantage 문제를, 어려운 문제 앞에 Lorem Ipsum을 덧붙여 재샘플링하는 LoPE로 해결한 연구를 정리한다. Qwen3-4B-Base에서 MATH-500 +4.8p, AMC +22%(상대) 향상이 보고되었다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. dev.to 작성자 ww-w.ai가 2026년 5월 11일 정리한 글로, 워싱턴대(WashU) 연구진이 5월 7일 arXiv에 공개한 논문 *"Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration"*(arXiv:2605.05566)을 소개한다.
2. GRPO 기반 RL 훈련의 핵심 결함 — 어려운 문제에서 모든 샘플 답변이 틀려 학습 신호가 0이 되는 zero-advantage 문제 — 를 문제 앞에 Lorem Ipsum을 덧붙여 재샘플링하는 LoPE(Lorem Perturbation for Exploration)로 해결한다.
3. Qwen3-4B-Base에서 MATH-500 +4.8p, AMC +22%(상대), AIME 2024 +3.49p가 측정되었고, 다른 어떤 방법으로도 풀리지 않은 어려운 문제 50개를 LoPE만 단독으로 풀었다. 아키텍처도 보상 모델도 건드리지 않는 저비용 개입이라는 점이 핵심이다.

## 풀고자 한 문제 — Zero-Advantage 학습 신호 소실

최신 LLM 강화학습은 GRPO(Group Relative Policy Optimization)에 크게 의존한다. 한 문제에 대해 여러 답변을 샘플링하고, 정답에는 보상을, 오답에는 페널티를 주는데, 상대적 우위(advantage)가 학습 신호의 원천이다.

문제는 어려운 문제다. 자료의 표현을 그대로 옮기면:

> all sampled answers might be wrong.

모든 후보가 같은 점수(=0)를 받으면 상대 우위가 0으로 붕괴한다. 모델이 가장 배워야 할 어려운 문제에서 학습 신호 자체가 사라진다. 이것이 zero-advantage problem이다.

## 해법 — LoPE (Lorem Perturbation for Exploration)

저자들이 제안한 개입은 단순하다. 어려운 문제를 재샘플링할 때 문제 텍스트 앞에 Lorem Ipsum 문장을 끼워 넣는다.

원본 입력:

```
Solve: What is the integral of x^2 from 0 to 3?
```

LoPE 입력:

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Solve: What is the integral of x^2 from 0 to 3?
```

실제 문제 텍스트는 그대로 보존되므로 추론 과제가 오염되지 않는다. 다만 prefix가 모델 내부의 어텐션 분포와 초기 hidden state를 흔들어, 같은 문제에서 다른 추론 경로를 따라가게 만든다. 자료의 표현으로는 "internal reasoning pathways toward different solution approaches without contaminating the actual problem".

## 왜 하필 Lorem Ipsum인가

아무 nonsense나 끼워 넣는다고 같은 효과가 나오는 것은 아니다. 자료는 두 갈래로 정리한다.

| 구분 | 예시 | 효과 |
|------|------|------|
| 효과적 | 라틴 기반 어휘, perplexity 약 25 | 학습 향상 |
| 비효과적 | 무작위 문자 시퀀스, 고-perplexity gibberish, 모델 훈련 언어(영어) 내부의 perturbation | 효과 없음·해로움 |

요점은 두 조건의 동시 만족이다.

- *familiar enough* — 모델이 정상 토큰으로 처리할 만큼 친숙해야 한다(낮은 perplexity).
- *foreign enough* — 실제 추론 과제 어휘와 의미적으로 섞이지 않아야 한다.

자료의 인용:

> Lorem Ipsum hits a sweet spot: familiar enough that the model processes it normally, foreign enough that it does not contaminate the actual reasoning task.

Lorem Ipsum은 이 좁은 영역을 우연히 만족시키는 텍스트다.

## 벤치마크 결과 (Qwen3-4B-Base)

| 벤치마크 | 표준 GRPO | LoPE | 변화 |
|---|---|---|---|
| MATH-500 | 77.80 | 82.60 | +4.80 |
| AMC | 47.76 | 58.21 | +22%(상대) |
| AIME 2024 | 16.41 | 19.90 | +3.49 |

수치보다 더 흥미로운 것은 도달 가능한 해 집합의 확장이다. 어려운 문제 352개 중 다른 어떤 방법으로도 풀리지 않은 50개를 LoPE만 풀어냈다. 성공 시에는 advantage signal이 표준 재샘플링 대비 2.1\~5.0배로 증폭되었다고 보고한다.

이는 단순한 sampling 다양성(temperature 조정) 증가가 아니라 도달 가능한 추론 경로 집합 자체가 넓어졌다는 해석에 무게를 싣는다.

## 핵심 시사점 — 자료의 정리

1. <strong>Exploration은 여전히 미개발 영역이다.</strong> 대규모 LLM 훈련은 데이터·파라미터 scaling에 집중해 왔으나, 단순한 prefix 변형만으로 두 자릿수 퍼센트 향상이 나오는 것은 exploration 메커니즘이 큰 leverage를 남겨두고 있다는 신호다.
2. <strong>Prompt sensitivity는 발견의 도구다.</strong> 의미 없는 prefix가 완전히 다른 reasoning chain을 잠금 해제할 수 있다. prompt space 자체가 탐색 가능한 차원이라는 함의다.
3. <strong>저비용 개입이 ROI가 높다.</strong> LoPE는 모델 아키텍처도 보상 모델도 건드리지 않는다. 데이터 파이프라인에서 prefix 한 줄을 추가하는 것이 전부다.

## 가장 흥미로운 지점

나에게는 prompt space가 탐색 차원이라는 관점이 가장 인상 깊었다. 탐색이라 하면 보통 sampling temperature를 올리거나 latent space의 노이즈를 키우는 쪽을 떠올리는데, LoPE는 입력 토큰 시퀀스 자체에 좌표 변환을 가한 셈이다. 같은 문제·같은 모델·같은 보상 함수에서도 '어떻게 묻는가'가 '무엇을 답할 수 있는가'를 바꾼다.

추론 시점의 prompt engineering 기법들 — 랜덤 시드 프롬프팅, 다단계 prompting — 이 훈련 시점에서도 그대로 의미를 가진다는 점에서, prompt engineering의 적용 시점에 대한 시야가 한 칸 넓어진다.

다만 자료에서 한 가지 유의할 점도 짚어둔다. 글의 말미에 명시되어 있듯, 원 논문은 <strong>pre-peer-review</strong> 단계의 연구다. 결과는 인상적이지만 독립 재현·다른 모델군에서의 일반화 여부는 향후 확인이 필요하다.

## 출처

- 정리 글: ww-w.ai, *"Lorem Ipsum Makes LLMs Smarter. No, Seriously."* (dev.to, 2026-05-11)
- 원 논문: Huang, Huang, Li, Cai, Yang, Huang (Washington University in St. Louis), *"Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration"* (arXiv:2605.05566, 2026-05-07)

원문: <https://dev.to/ww-w-ai/lorem-ipsum-makes-llms-smarter-no-seriously-1j8l>

원문에 인용할 만한 이미지는 포함되어 있지 않아 텍스트만으로 정리했다.
