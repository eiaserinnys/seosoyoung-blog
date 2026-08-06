---
title: "Building with Anthropic Claude: Prompt Workshop — Zack Witten"
date: 2026-04-28T20:30:00+09:00
tags: ["AI", "코딩 에이전트", "Claude", "프롬프팅"]
categories: ["에이전트와 코딩"]
summary: "Building with Anthropic Claude: Prompt Workshop — Zack Witten"
ShowToc: true
TocOpen: false
sidenotes: true
---

> AI-Assisted Engineering Talk #11/27

프롬프트 엔지니어링 발표는 많지만, Anthropic의 공식 prompt engineer가 직접 청중의 프롬프트를 받아서 실시간으로 뜯어고치는 워크숍은 드물지요. Zack Witten은 70분 동안 XML 태그, prefill, few-shot 예시, 시스템 프롬프트 분리까지 Anthropic이 실제로 권하는 기법을 하나하나 시연했습니다. 그리고 그 모든 기법을 합쳐도 좋은 예시 하나에 미치지 못한다고, 아주 단호하게 말했습니다.


## 핵심 주장 5가지


워크숍에서 반복적으로 강조된 다섯 가지 핵심 주장입니다. 각각이 독립적인 기법이면서 하나의 철학을 공유합니다 — 모호함을 제거하라.


### Few-shot이 다른 모든 기법의 합보다 중요하다

XML 태그, 구체성, prefill, 강조 등 워크숍에서 다룬 모든 기법을 합쳐도 좋은 few-shot 예시의 효과에 미치지 못합니다. Anthropic 내부에서도 같은 결론이라고 합니다.

> *""In some ways that's more important than like everything else that I've said combined.""* ### 코드로 할 수 있는 건 프롬프트에 넣지 마라

JSON 파싱, 길이 제약, 포맷 변환, 대문자 변환 등 결정론적 처리가 가능한 작업은 코드로 처리하는 것이 확실합니다. 프롬프트로 모든 것을 해결하려는 충동이 가장 흔한 실수라고 짚었습니다.

> *""나라면 Claude에게 코드를 짜게 해서 처리한다.""* ### 정보가 먼저, 지시가 마지막

프롬프트 배치 순서가 성능에 영향을 줍니다. 참조 문서와 데이터를 먼저 놓고, 작업 지시를 맨 끝에 배치하면 recency bias를 활용할 수 있습니다. 모든 프롬프트를 XML 태그로 구조화하는 것은 기본 습관입니다.


### Assistant prefill로 출력 형식을 구조적으로 보장하라

Claude API에서 assistant 메시지를 {로 시작하면 JSON 형식이 구조적으로 보장됩니다. '프롬프트로 부탁'하는 것과 'API 수준에서 강제'하는 것은 차원이 다릅니다. Stop sequence와 결합하면 출력 경계까지 코드가 제어합니다.


### Temperature는 과대평가되었다

Temperature를 높여 창의성을 끌어내려는 시도는 대부분 비효과적입니다. Zack이 temperature 1과 0의 출력을 나란히 비교했을 때 결과가 거의 동일했습니다. 정확성이 중요한 작업에서는 0이 최적입니다.


## 19개 프롬프트 기법 카탈로그


워크숍에서 추출된 18개 실전 기법과 1개 인사이트입니다. 6개 카테고리로 정리했습니다.


### 프롬프트 구조화

- **XML 태그 구분 <instructions>, <context>, <examples> 태그로 섹션을 명확히 분리**
- **정보-먼저 배치 참조 문서를 앞에, 작업 지시를 끝에 — recency bias 활용**
- **강조 기법 대문자, 반복, EXTREMELY IMPORTANT — RLHF 학습 데이터에서 유래**

### 구체성과 출력 제어

- **구체적 숫자 '간결하게' 대신 '5문장으로' — 모호한 형용사를 측정 가능한 기준으로**
- **Code > Prompt 결정론적 처리는 코드에서. 프롬프트 만능주의는 가장 흔한 실수**
- **네거티브 역설 '\~하지 마라'는 오히려 그 행동에 attention을 집중시킨다**
- **Stop Sequence API 수준에서 출력 경계를 코드로 제어 — XML 태그와 결합**

### Prefill과 포맷 강제

- **Assistant Prefill assistant 메시지를 {로 시작 → JSON 출력 구조 보장**
- **Temperature = 0 창의적 작업에서도 기대만큼의 차이를 만들지 못한다**

### Few-Shot 예시 전략

- **예시의 압도적 우위 다른 모든 기법의 합보다 few-shot 예시가 효과적**
- **대조 쌍 나쁜 출력과 좋은 출력을 병치 — 톤/스타일에 특히 효과적**
- **100 → 7 선별 대량 생성 후 최선을 골라 예시로 재투입하는 반복 워크플로우**
- **경량 CoT 삽입 예시 안에 핵심 포인트 추출 단계를 넣어 사고 패턴을 유도**

### 시스템 프롬프트와 역할

- **시스템 = 역할만 상세 지시는 human turn에. 시스템에 넣으면 '일반 지침' 취급**
- **코드 라우팅 멀티 페르소나는 하나의 프롬프트가 아니라 코드에서 분기**

### 평가 / 다국어 / 멀티모달

- **감정 편향 경고 모델 자체 평가는 긍정 내용을 높게 채점 — 루브릭으로 보정**
- **모국어 프롬프팅 한국어 작업이면 한국어로. 영어 번역 후 지시보다 효과적**
- **이미지 전처리 관련 영역만 크롭, 확대 후 텍스트 묘사를 함께 제공**

## 예시가 지시보다 검증 밀도가 높은 이유


> **💡 Zack + Dan + 명제 프레임워크의 수렴**
>
> Few-shot 예시 하나가 톤, 포맷, 추론 패턴, 내용 범위를 동시에 제약합니다. 명시적 지시 여러 개에 해당하는 검증 표면을 단일 예시가 인코딩하는 것이지요. Zack의 "everything else combined"와 Dan의 "1\~2개 plateau"가 모두 이 밀도 모델로 설명됩니다. 예시의 검증 밀도가 높으니 적은 수로도 충분하고, 과잉 시에는 노이즈가 신호를 넘어서는 것입니다. 3개의 독립된 관찰(Zack의 실증, Dan의 데이터, 명제 프레임워크)이 같은 설명으로 수렴한 것이 이 인사이트의 핵심입니다. ## 교차 연결


이 워크숍은 27편 발표 영상 시리즈 중 다른 발표들과 명확한 교차 지점을 가지고 있습니다.

- ↔ Show, don't tell — 톤과 스타일은 설명보다 시연이 빠르다. 두 발표자가 독립적으로 같은 결론에 도달.
- + XML 태그 구조화, 정보-먼저 배치, assistant prefill, stop sequence, 대조 쌍 기법, 100→7 반복 선별 워크플로우, 시스템 프롬프트 역할 분리, 코드 라우팅, temperature 비효과성, 모델 자체 평가 감정 편향, 다국어/이미지 팁
- + Meta Prompting, Reasoning Models 정반대 권장사항, Zero-shot CoT 트리거 원리

> 명제와의 관계: 에이전트 자율성 ≡ 검증 표면의 함수 Zack의 워크숍은 명제의 입력측 검증 표면에 대한 실전 매뉴얼입니다. "code > prompt" = 검증 표면을 확률적(prompt)에서 결정론적(code)으로 이전 "few-shot > instructions" = 검증 표면의 밀도가 면적보다 중요 "stop sequence + prefill" = API 수준에서 출력 검증 표면을 구조적으로 보장 기존 명제 "면적이 아니라 위치와 밀도의 문제"를 Anthropic 내부자가 실증적으로 재확인한 셈이지요. ```
Atom Reference Tree

Prompt Engineering
└─ Building with Anthropic Claude (Zack Witten)
├─ 📐 프롬프트 구조화 · 3 cards
├─ 🎯 구체성과 출력 제어 · 4 cards
├─ 🔧 Prefill과 포맷 강제 · 2 cards
├─ ⭐ Few-Shot 예시 전략 · 4 cards + Dan 3 cross-ref
├─ 👤 시스템 프롬프트와 역할 분리 · 2 cards
└─ 🌍 평가·다국어·멀티모달 · 3 cards
```
