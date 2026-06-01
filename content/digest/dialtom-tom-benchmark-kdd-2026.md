---
title: "DialToM: A Theory of Mind Benchmark for Forecasting State-Driven Dialogue Trajectories"
date: 2026-04-30T09:10:00+09:00
tags: ["theory-of-mind", "LLM-evaluation", "benchmark", "trust", "dialogue-forecasting"]
categories: ["다이제스트"]
summary: "자연 대화 기반 ToM 벤치마크. 정신 상태 식별(Literal ToM)과 대화 궤적 예측(Functional ToM)을 분리 평가하여, LLM이 정신 상태를 '알면서도 활용하지 못하는' 추론 비대칭을 밝혀냈다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. 싱가포르 SMU 연구진이 KDD 2026에 제출한 ToM 벤치마크로, LLM-LLM 합성 대화가 아닌 실제 인간 대화에서 구축했다.
2. 기존 BDIEK 프레임워크에 신뢰(Trust)를 추가한 BDIEKT로 확장하고, 정신 상태 식별(Literal ToM)과 대화 궤적 예측(Functional ToM)을 분리 평가한다.
3. 대부분의 LLM이 정신 상태 식별에는 우수하지만 그 이해를 사회적 궤적 예측에 활용하지 못하는 "추론 비대칭"을 보이며, Gemini 3 Pro만이 예외다.

## BDIEKT: Trust를 추가한 정신 상태 프레임워크

기존 ToM 연구는 Belief(신념), Desire(욕구), Intention(의도), Emotion(감정), Knowledge(지식)의 BDIEK 프레임워크를 사용해왔다. DialToM은 여기에 <strong>Trust(신뢰)</strong>를 추가하여 BDIEKT로 확장한다.

신뢰는 다자 대화에서 관계적 요인으로, 특히 고위험 이자적(dyadic) 상호작용에서 대화 궤적을 결정하는 핵심 변수다. 화자 간 신뢰 수준이 같은 발화를 전혀 다른 방향으로 이끌 수 있기 때문이다.

## Literal ToM vs Functional ToM

DialToM의 가장 중요한 설계 결정은 두 가지 ToM 능력을 분리 평가한다는 점이다.

- **Literal ToM**: 대화 속 등장인물의 정신 상태(BDIEKT)를 식별하는 능력. "이 사람이 지금 무엇을 믿고/원하고/느끼는가?"
- **Functional ToM**: 식별된 정신 상태를 활용하여 대화의 향후 궤적을 예측하는 능력. <strong>Prospective Diagnostic Forecasting</strong>으로 측정한다 — 완전한 정신 상태 프로필(BDIEKT)만 주어진 상태에서, 상태 일관적인 대화 궤적을 식별해야 한다.

이 분리가 중요한 이유는, "정신 상태를 안다"와 "안다는 것을 써먹을 수 있다"가 같은 능력이 아니기 때문이다.

## 자연 대화 기반 구축

ToMATO가 LLM-LLM 합성 대화를 사용하는 것과 달리, DialToM은 <strong>실제 인간 대화</strong>에서 벤치마크를 구축한다. 인간 검증자가 품질을 확인한 다지선다 형식이며, 기존 벤치마크의 표면적 패턴 재현(spurious correlation) 문제를 회피하려는 설계다.

## 핵심 발견: 추론 비대칭

평가 결과에서 가장 두드러진 발견은 <strong>추론 비대칭(reasoning asymmetry)</strong>이다.

- **Literal ToM**: 대부분의 LLM이 정신 상태 식별에서 <strong>우수한</strong> 성능을 보인다
- **Functional ToM**: 그러나 그 이해를 사회적 궤적 예측에 활용하는 데는 <strong>실패</strong>한다
- **예외**: Gemini 3 Pro만이 정신 상태 이해를 궤적 예측에 성공적으로 연결했다

추가로, 인간과 LLM이 생성한 정신 상태 추론 사이의 의미적 유사도가 약하다. LLM이 정답을 맞히더라도, 그 추론 과정이 인간의 사회적 인지와 질적으로 다를 수 있음을 시사한다.

## 가장 흥미로운 지점

"아는 것"과 "아는 것을 쓰는 것"의 분리가 날카롭다. 인간에게 Theory of Mind는 단순히 타인의 마음을 읽는 것이 아니라, 그 읽기를 바탕으로 사회적 행동을 조율하는 것이다. LLM이 전자에서는 인간에 근접하면서도 후자에서 실패한다는 발견은, 현재 LLM의 "이해"가 기능적 이해가 아닌 패턴 매칭에 가까울 수 있다는 의심을 강화한다.

Gemini 3 Pro만의 예외도 흥미롭다. 어떤 아키텍처적·학습적 차이가 이 격차를 만드는지는 논문이 깊이 다루지 않지만, 후속 연구의 중요한 실마리가 될 것이다.

## 출처

Neemesh Yadav, Palakorn Achananuparp, Jing Jiang, Ee-Peng Lim. Submitted to KDD 2026 Datasets and Benchmarks Track.
원문: <https://arxiv.org/abs/2604.20443>
코드: <https://github.com/Stealth-py/DialToM>
