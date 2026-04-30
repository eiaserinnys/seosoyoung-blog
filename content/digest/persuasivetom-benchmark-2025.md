---
title: "PersuasiveToM: A Benchmark for Evaluating Machine Theory of Mind in Persuasive Dialogues"
date: 2026-04-30T09:06:00+09:00
tags: ["Theory-of-Mind", "LLM-evaluation", "benchmark", "persuasion", "BDI-model"]
categories: ["다이제스트"]
summary: "설득 대화 시나리오에서 LLM의 Theory of Mind을 BDI 프레임워크로 평가하는 벤치마크. GPT-4o조차 피설득자의 동적 욕구 추적에서 인간 대비 17%p, 설득자 의도 추론에서 32%p 뒤처진다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. PersuasiveToM은 <strong>신념-욕구-의도</strong>(BDI) 프레임워크를 설득 대화에 적용해, ToM Reasoning과 ToM Application 두 축으로 LLM의 마음 이론을 평가한다.
2. 설득자의 정적 목표 vs 피설득자의 동적 욕구라는 역할 비대칭이 평가의 핵심 난이도를 결정하며, LLM은 정적 속성은 잘 읽지만 동적 심리 변화 추적에서 급감한다.
3. CoT 프롬프팅은 전략 예측에서만 소폭 효과가 있을 뿐 정신 상태 추론에서는 일관된 개선이 없다.

## 기존 ToM 벤치마크의 한계

대부분의 기존 ToM 벤치마크는 물리적 세계에 대한 정보 추론에 집중한다. Sally-Anne 테스트의 핵심은 "물건이 어디에 있는가"다. FANToM은 대화 맥락으로 확장했지만, 여전히 물리적 정보의 비대칭을 다룬다.

PersuasiveToM은 한 단계 더 나아가 **심리적 상태**(psychological states)의 추론을 평가한다. "상대가 이 제안에 대해 어떤 태도를 갖고 있는가", "대화가 진행되면서 그 태도가 어떻게 변하는가"가 핵심 질문이다.

## 벤치마크 설계

### BDI 프레임워크 적용

Bratman(1987)의 <strong>신념-욕구-의도</strong>(Belief-Desire-Intention) 모델을 기반으로 세 가지 추론 과제를 설계한다.

- **Desire Reasoning**: 설득자의 목표와 피설득자의 변화하는 욕구를 추적
- **Belief Reasoning**: 각 참여자가 상대의 태도를 어떻게 인식하는지 추론
- **Intention Reasoning**: Cialdini의 설득 원칙(상호성, 희소성, 합의, 권위, 일관성, 호감)에 매핑된 의도를 식별

여기에 ToM Application 과제 두 가지가 추가된다.

- **Strategy Prediction**: 다음에 사용할 설득 전략 예측
- **Judgement**: 주어진 전략이 효과적인지 판단

### 역할 비대칭의 핵심

설득 대화의 독특한 구조는 <strong>역할 비대칭</strong>에 있다. 설득자의 목표는 대화 내내 정적이다(예: "Alice를 식물원 투어에 참여시키기"). 반면 피설득자의 욕구는 대화 진행에 따라 거부\~중립\~수용으로 동적 변화한다. 이 비대칭이 LLM에게 차별적 난이도를 부여한다.

### 데이터 규모

525개 대화 인스턴스, 35개 도메인(생활, 교육, 기술 등), 평균 4.9턴, 약 18,000개 질문.

## 실험 결과

8개 LLM을 대상으로 한 평가 결과(표에서 발췌):

| 과제 | GPT-4o | 인간 | 격차 |
|------|--------|------|------|
| 설득자 Desire | 95.6% | 100% | -4.4%p |
| 피설득자 Desire | 67.7% | 84.6% | **-16.9%p** |
| 설득자 Belief | 89.5% | 92.3% | -2.8%p |
| 피설득자 Belief | 81.7% | 87.9% | -6.2%p |
| 설득자 Intention | 46.3% | 78.1% | **-31.8%p** |
| Strategy Prediction | 73.6% | 86.8% | -13.2%p |
| Judgement | 96.4% | 98.0% | -1.6%p |

### 패턴 분석

**정적 vs 동적**: 설득자의 정적 욕구는 96%까지 맞추지만, 피설득자의 동적 욕구는 68%로 급감한다. LLM은 "변하지 않는 것"은 잘 읽지만, "변해가는 것"을 추적하는 데 근본적 한계가 있다.

**의도 추론의 바닥**: 설득자의 의도 추론은 모든 모델에서 \~46%로, 랜덤(16.7%)보다는 높지만 인간(78%)에 크게 못 미친다. LLM이 설득 이론(Cialdini 원칙)을 내재화하지 못했음을 시사한다.

**CoT의 한계**: CoT는 Strategy Prediction에서만 소폭 개선(GPT-4o 기준 73.6%\~76.9%)을 보이고, 나머지 과제에서는 일관된 효과가 없다. 오히려 중간 추론 단계에서 오류가 누적되어 최종 판단을 오도하는 경우가 관찰된다.

**Judgement의 높은 성능**: 전략 효과성 판단(96.4%)은 인간(98%)에 근접한다. 이는 "사후 판단"은 쉽지만 "사전 예측"은 어렵다는 비대칭을 보여준다.

## 가장 흥미로운 지점

"설득자의 의도 추론"이 가장 어렵다는 결과가 인상적이다. 설득자가 왜 그 말을 했는지, 어떤 심리적 지렛대를 사용하려 했는지를 파악하는 것이야말로 ToM의 고차원적 활용이다. LLM이 여기서 인간의 절반 수준에 그친다는 것은, 현재 모델들이 "상대를 움직이려는 의도"를 읽는 데 근본적으로 약하다는 것을 의미한다.

## 출처

Fangxu Yu, Lai Jiang, Shenyi Huang, Zhen Wu, Xinyu Dai. Nanjing University, SJTU, UCSD. 2025.
원문: <https://arxiv.org/abs/2502.21017>
코드: <https://github.com/Yu-Fangxu/PersuasiveToM>
