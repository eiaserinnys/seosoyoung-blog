---
title: "The Model Isn't Wrong — You're Just Bad at Prompting"
date: 2026-04-28T20:24:00+09:00
tags: ["AI", "코딩 에이전트", "프롬프팅"]
categories: ["다이제스트"]
summary: "The Model Isn't Wrong — You're Just Bad at Prompting"
ShowToc: true
TocOpen: false
sidenotes: true
---

> AI-Assisted Engineering Talk #9/27

모두가 같은 모델에 접근할 수 있는 시대에, 제품의 차별화는 어디서 오는 것이겠습니까. Dan은 그 답이 prompt와 그 주변 architecture에 있다고 못박습니다. 그리고 CoT, few-shot, meta prompting의 정석을 빠르게 훑은 뒤, reasoning model에서는 그 정석이 정반대로 뒤집힌다는 결정타를 날립니다.


### Prompt Engineering은 진짜 엔지니어링이다

AI 기능을 실제로 출시(ship)해 본 사람은 압니다 — 모델에게 '원하는 것'을 이해시키는 일 자체가 어렵다는 것을. 모두가 같은 모델에 접근하는 시대에, prompt와 그 주변 architecture가 제품 차별화의 거의 유일한 축이옵니다.


### 가장 단순한 해결책을 먼저 시도하라

Anthropic의 에이전트 가이드를 인용하여, 한 시간 만에 'prompt로는 안 되니 RAG를 만들자'로 점프하는 것은 게으른 결론이라 지적합니다. Prompt로 풀리는 문제는 RAG보다 운영 비용이 비교 불가하게 낮습니다.


### CoT는 모델 내부로 이동했다

DeepSeek R1은 think 태그 안에 reasoning chain을 생성하도록 학습되었습니다. 이제 외부에서 'think step by step'을 붙일 필요가 없어졌습니다 — CoT가 prompt 기법에서 모델의 기본 행동으로 변한 변곡점이옵니다.


### Few-shot은 1\~2개로 충분, 그 이상은 역효과

예시 개수 대비 성능 그래프는 거의 항상 빠르게 plateau에 도달하고, 어느 시점부터 오히려 성능을 떨어뜨립니다. 다양한 입력을 커버하는 1\~2개 예시면 충분하다는 것이지요.


### Reasoning Model에서는 모든 것이 정반대

o1, R1 같은 reasoning model에서는 minimal prompting이 정석입니다. Few-shot을 추가하면 오히려 성능이 저하되고, reasoning 방법을 prompt로 지시하면 모델 내장 reasoning을 덮어써 정확도가 떨어집니다.


## Prompt의 표면이 이동하고 있다


이 발표에서 가장 주목할 만한 통찰은, prompt engineering의 표면(surface)이 외부에서 모델 내부로 이동하고 있다는 관찰이옵니다. Zero-shot CoT의 'think step by step'이 한때는 혁신적 기법이었지만, 이제 reasoning model은 그것을 기본 행동으로 내장하였습니다.


### 기법별 핵심 정리


Zero-shot CoT — 'think step by step' 한 줄이 출력 토큰 분포를 추론 단계에 의해 조건부로 만듭니다. 표면 표현보다 중요한 것은 이 메커니즘 자체이옵니다.


Few-shot CoT — 정답이 아니라 사고 과정을 보여주는 것이 핵심. Auto-CoT, Auto-Reason 같은 프레임워크가 이 원리를 자동화하였습니다.


Show, don't tell — 클라이언트의 톤이나 스타일을 텍스트로 묘사하는 것보다, 입력-출력 페어를 한두 개 보여주는 편이 빠릅니다. 자연어로 설명하기 어려운 분포를 직접 시연하는 방식이지요.


Meta Prompting — LLM으로 prompt를 짜는 것. Anthropic, OpenAI playground 등 주요 플랫폼이 무료 제공합니다. 단, 모델 제공자별로 잘 통하는 prompt 형태가 다르므로 분기가 필요합니다.


Microsoft의 Med Prompt 프레임워크 실험에서 o1 모델에 few-shot 예시를 추가했더니 오히려 성능이 저하되었습니다. DeepSeek R1 학습팀과 OpenAI o1 preview 노트도 같은 결론에 도달하였지요. 반면, reasoning 토큰 길이가 늘어남에 따라 정확도는 동반 상승 — 'reason more' 격려가 효과를 냅니다.


## Reasoning Model 프롬프트 체크리스트


Dan이 정리한 reasoning model 대응 4원칙이옵니다.


### o1 / R1 계열 모델에 적용


Minimal prompt + 명확한 task description — 군더더기를 제거하고, 무엇을 원하는지만 분명하게 전달합니다.


필요 시 reasoning을 더 격려 — 'quick response'보다 '더 사고하라'가 우월합니다. 마지막 1%를 짜낼 때 유효합니다.


Few-shot 회피, 쓰더라도 1\~2개 — 추가 컨텍스트가 reasoning model을 over-complicate시키고 혼란에 빠뜨립니다.


Reasoning 방법을 prompt로 지시하지 말 것 — 모델에 내장된 reasoning을 외부 prompt가 덮어쓰면 정확도가 떨어집니다.


## 27편 시리즈와의 접점


이 발표는 prompt engineering의 기초부터 최신 reasoning model까지를 아우르는 교과서적 정리이면서, 동시에 '모델이 진화하면 기법도 뒤집힌다'는 핵심 메시지를 담고 있습니다. Context Engineering 시리즈의 다른 발표들과 자연스럽게 맞닿는 지점을 살펴봅니다.


### AI 코딩 발표 27편 종합 분석


전체 시리즈의 교차 분석과 통합 인사이트를 확인하실 수 있습니다.


### 시리즈 내 교차점


Simplicity 원칙의 반복 — Dan의 '가장 단순한 해결책 우선' 원칙은 시리즈 전반에서 반복되는 주제이옵니다. 복잡한 아키텍처로 뛰어들기 전에 prompt만으로 해결 가능한지를 먼저 검증하라는 메시지.


모델 진화에 따른 기법 전환 — CoT가 외부 기법에서 모델 내부 행동으로 이동한 사례는, AI 도구를 다루는 방법론이 모델 세대마다 재검토되어야 함을 시사합니다.


Meta Prompting과 자동화 — LLM으로 prompt를 짜는 접근은 context engineering에서 '인간이 직접 작성'과 '시스템이 자동 생성'의 경계가 흐려지는 흐름과 맥을 같이 합니다.


모델이 틀린 게 아니라, 우리가 모델에게 말을 잘 못 걸고 있는 것이라는 제목 자체가 이 발표의 핵심을 담고 있사옵니다. 그리고 더 흥미로운 것은 — reasoning model 시대에는 '말을 적게 거는 것'이 더 나은 결과를 낸다는 역설이지요. 기법은 시대에 따라 뒤집히지만, 모델을 이해하고 적절히 다루는 능력 자체의 가치는 변하지 않는 것 같습니다.
