---
title: "FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions"
date: 2026-04-30T09:05:00+09:00
tags: ["Theory-of-Mind", "LLM-evaluation", "benchmark", "information-asymmetry"]
categories: ["다이제스트"]
summary: "정보 비대칭이 자연스럽게 발생하는 대화 맥락에서 LLM의 Theory of Mind을 스트레스 테스트한 EMNLP 2023 논문. 최선의 LLM도 인간과 큰 격차를 보이며, CoT와 파인튜닝으로도 해소되지 않는다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. FANToM은 기존의 Sally-Anne 류 수동적 내러티브 대신, 다자 대화에서 정보 비대칭이 자연스럽게 발생하는 맥락으로 LLM의 ToM을 평가한다.
2. 동일한 추론을 요구하되 형태가 다른 다중 질문 유형을 설계해, LLM이 진짜 이해하는지 표면적 패턴 매칭인지를 구분한다.
3. 최신 LLM은 인간 대비 현저히 낮은 성능을 보이며, Chain-of-Thought 추론이나 파인튜닝으로도 이 격차가 해소되지 않는다.

## 배경: 왜 새로운 ToM 벤치마크가 필요한가

기존 ToM 평가는 대부분 수동적 내러티브를 기반으로 한다. "Sally가 방을 나간 사이 Anne이 공을 옮겼다. Sally는 공이 어디에 있다고 생각하는가?" 같은 시나리오다. 이 형식은 두 가지 근본적 한계가 있다.

첫째, **상호작용성이 없다.** 실제 사회적 맥락에서 ToM은 대화의 흐름 속에서 실시간으로 작동한다. 누가 무슨 말을 들었고, 누가 그 자리에 없었는지를 대화 진행에 따라 추적해야 한다.

둘째, **표면적 패턴으로 정답을 맞출 수 있다.** 질문 형식이 단순하면, 모델이 ToM 추론 없이도 텍스트의 통계적 패턴만으로 답할 수 있다. 이것이 LLM의 ToM 능력에 대한 환상(illusory ToM)을 만든다.

## FANToM의 설계 원칙

FANToM은 심리학의 이론적 요건과 LLM 평가의 경험적 고려사항을 함께 반영했다.

**정보 비대칭 대화 맥락**: 여러 참여자가 대화하는 상황을 설정하되, 특정 참여자가 중간에 자리를 비우거나 합류하면서 자연스럽게 정보 비대칭이 발생한다. "이 사람은 이 대화를 들었지만, 저 사람은 듣지 못했다"는 상황이 내러티브 장치가 아닌 대화 흐름 자체에서 생성된다.

**다중 질문 유형(Multiple Question Types)**: 동일한 underlying reasoning을 요구하지만 형태가 다른 여러 질문을 설계한다. 한 형태에서 맞추고 다른 형태에서 틀리면, 그것은 진정한 ToM 추론이 아니라 표면적 패턴 매칭이다. 이를 "허상적(illusory) ToM"이라 부른다.

## 핵심 결과

논문의 핵심 결론은 명확하다. **현재 최선의 LLM도 FANToM에서 인간에 크게 못 미친다.**

- Chain-of-Thought(CoT) 추론을 적용해도 성능이 유의미하게 개선되지 않는다
- 파인튜닝을 해도 격차가 해소되지 않는다
- 특히 다중 질문 유형 간 일관성이 낮아, LLM의 ToM이 표면적 수준에 머물러 있음을 시사한다

이는 LLM이 "누가 무엇을 알고 있는가"를 진정으로 추론하기보다, 텍스트의 통계적 단서에 의존하고 있음을 의미한다.

## 가장 흥미로운 지점

FANToM의 가장 날카로운 기여는 "허상적 ToM"이라는 개념을 실험적으로 포착한 것이다. 한 질문 형태에서 정답을 맞추면 ToM이 있다고 착각하기 쉽지만, 같은 추론을 다른 형태로 물으면 틀린다면 그것은 진짜 이해가 아니다. 이 방법론은 ToM을 넘어 LLM의 다른 고차 인지 능력을 평가할 때도 적용할 수 있는 범용적인 원칙이다.

## 출처

Hyunwoo Kim, Melanie Sclar, Xuhui Zhou, Ronan Le Bras, Gunhee Kim, Yejin Choi, Maarten Sap. EMNLP 2023.
원문: <https://arxiv.org/abs/2310.15421>
