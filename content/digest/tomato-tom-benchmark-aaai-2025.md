---
title: "ToMATO: Verbalizing the Mental States of Role-Playing LLMs for Benchmarking Theory of Mind"
date: 2026-04-30T09:05:00+09:00
tags: ["theory-of-mind", "LLM-evaluation", "benchmark", "false-belief", "information-asymmetry"]
categories: ["다이제스트"]
summary: "NTT 연구진이 역할극 LLM 간 정보 비대칭 대화를 활용하여 5개 정신 상태 범주와 거짓 신념을 다층적으로 평가하는 ToM 벤치마크를 제안한다. GPT-4o mini조차 인간 성능에 미치지 못한다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. NTT 연구진(Shinoda et al.)이 AAAI 2025에 발표한 Theory of Mind 벤치마크로, 역할극 LLM 간 대화에서 정보 비대칭을 이용해 거짓 신념 상황을 체계적으로 생성한다.
2. 기존 벤치마크가 신념(belief)에만 집중하던 한계를 넘어, 신념·의도·욕구·감정·지식 5개 정신 상태 범주를 1차/2차 수준에서 동시에 평가한다.
3. 9개 LLM을 테스트한 결과, GPT-4o mini도 인간 성능에 미달하며 특히 거짓 신념 이해와 성격 특성 변화에 대한 로버스트니스가 부족하다.

## 기존 ToM 벤치마크의 세 가지 한계

이 논문은 기존 ToM 벤치마크가 현실 시나리오와 괴리되는 세 가지 문제를 지적한다.

1. **제한된 정신 상태 범위**: 대부분의 벤치마크가 신념(belief)만 평가한다. 의도, 욕구, 감정, 지식 같은 다른 정신 상태는 무시된다.
2. **거짓 신념 탐색 부족**: Sally-Anne 스타일의 단순한 시나리오에 의존하며, 다양한 유형의 거짓 신념을 체계적으로 생성하지 못한다.
3. **성격 특성 무시**: 등장인물의 다양한 성격이 ToM 추론 난이도에 미치는 영향을 고려하지 않는다.

## LLM-LLM 대화로 벤치마크를 생성하는 방법

ToMATO의 핵심 아이디어는 두 LLM이 역할극으로 대화하되, 각 발화 전에 <strong>내면 생각(thought)을 언어화</strong>하도록 프롬프팅하는 것이다.

- 상대방의 생각은 숨기므로 <strong>정보 비대칭</strong>이 자연스럽게 발생한다
- 이 정보 비대칭이 거짓 신념 상황을 **체계적으로** 생성하는 핵심 메커니즘이다
- 언어화된 생각은 "이 캐릭터의 정신 상태는 무엇인가?"라는 질문의 정답으로 활용된다
- 15개 성격 특성 패턴을 LLM에 부여하여 발화와 사고의 다양성을 확보한다

결과적으로 5,400개 다지선다 문항, 753개 대화, 15개 성격 특성 패턴으로 구성된 벤치마크가 만들어졌다.

## 5개 정신 상태 범주

ToMATO는 다음 5개 범주를 1차(자신의 정신 상태)와 2차(타인이 무엇을 생각하는지에 대한 추론) 수준에서 평가한다.

- **Belief (신념)**: 세계에 대한 믿음
- **Intention (의도)**: 행동 계획
- **Desire (욕구)**: 원하는 바
- **Emotion (감정)**: 감정 상태
- **Knowledge (지식)**: 알고 있는 정보

## 주요 평가 결과

9개 LLM을 평가한 결과, 핵심 발견은 세 가지다.

1. **GPT-4o mini도 인간에 미달**: 가장 성능이 좋은 모델조차 인간 수준에 도달하지 못했다.
2. **거짓 신념에서 격차가 최대**: 정보 비대칭으로 생성된 거짓 신념 이해에서 인간 대비 성능 격차가 가장 크다. 기존 Sally-Anne 스타일보다 현실에 가까운 난이도를 제공한다.
3. **성격 특성 변화에 취약**: 캐릭터의 성격 특성이 바뀌면 LLM의 ToM 추론 정확도가 불안정해진다. 인간은 이런 변화에 상대적으로 강건하다.

## 가장 흥미로운 지점

"생각을 숨기면 거짓 신념이 자연스럽게 생긴다"는 설계가 인상적이다. 기존 벤치마크처럼 인위적으로 Sally-Anne 시나리오를 만들 필요 없이, 정보 비대칭이라는 단일 메커니즘만으로 다양한 유형의 거짓 신념이 출현한다. 이는 인간 사회에서 거짓 신념이 발생하는 방식과도 닮아 있다 — 우리가 타인의 내면을 볼 수 없기 때문에 오해가 생기는 것이다.

## 출처

Kazutoshi Shinoda, Nobukatsu Hojo, Kyosuke Nishida, Saki Mizuno, Keita Suzuki, Ryo Masumura, Hiroaki Sugiyama, Kuniko Saito (NTT). AAAI 2025.
원문: <https://arxiv.org/abs/2501.08838>
코드: <https://github.com/kykim0/ToMATO>
