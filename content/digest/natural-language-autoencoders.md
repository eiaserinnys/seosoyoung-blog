---
title: "Natural Language Autoencoders: Turning Claude's thoughts into text"
date: 2026-05-09T01:50:00+09:00
tags: ["해석가능성", "정렬", "안전성 평가", "Anthropic"]
categories: ["모델과 연구"]
summary: "Anthropic이 공개한 해석가능성 도구 NLA. 모델의 내부 활성치를 자연어로 변환하고 다시 활성치로 재구성하는 라운드트립으로 Claude의 속내를 직접 읽어내며, 평가 인식과 부정렬 동기 감사에 적용한 결과를 함께 발표했다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Anthropic이 2026년 5월 7일 공개한 해석가능성 연구로, 모델 활성치를 자연어로 변환하고 그 자연어로 활성치를 재구성하는 라운드트립 시스템 NLA(Natural Language Autoencoder)를 소개한다.
2. NLA는 SAE·attribution graph와 달리 도구 자체가 자연어로 직접 말하며, 안전성 평가에서 발화로 드러나지 않던 평가 인식을 16\~26% 수준에서 검출했다.
3. 부정렬 동기를 숨긴 모델을 대상으로 한 감사 게임에서 NLA 장착 감사자는 12\~15% 성공한 반면, 미장착 감사자는 3% 미만에 머물렀다.

## 동기 — 활성치는 모델의 사고이지만 직접 읽을 수 없다

Claude는 입출력은 단어로 주고받지만, 그 사이의 처리는 길게 늘어선 숫자 벡터로 진행된다. 이 숫자들이 활성치(activation)다. 인간 뇌의 신경 활동처럼 모델의 *사고*를 코딩하지만, 사람이 그 자체로 읽어낼 수 있는 표상은 아니다.

Anthropic은 그동안 sparse autoencoder, attribution graph 같은 도구로 활성치를 이해해 왔다. 이 도구들은 많은 것을 가르쳐 주었지만 한 가지 한계가 있다 — *스스로 말하지 않는다*. 출력이 여전히 복잡한 객체여서 훈련된 연구자의 해석을 거쳐야 한다.

NLA는 이 격차를 정면으로 메우는 시도다. 도구가 자연어 텍스트로 직접 말하게 만든다. 예시는 시 운율 사전 계획이다. 두 행짜리 시의 마지막 단어를 비워두고 완성하라고 하면, NLA는 Opus 4.6이 결말을 *이미* "rabbit"으로 정해두고 있다는 사실을 텍스트로 보여준다.

![NLA가 시 운율 사전 계획을 텍스트로 보여주는 예시](https://img.seosoyoung.eiaserinnys.me/images/natural-language-autoencoders/couplet-rabbit.png)

## NLA란 무엇인가

핵심 아이디어는 *Claude가 자신의 활성치를 스스로 설명하게 만드는 것*이다. 그러나 활성치가 어떤 사고를 인코딩하는지 직접 알 길이 없으므로, 설명의 정확성은 직접 검증할 수 없다. 그래서 두 번째 Claude 사본을 거꾸로 학습시킨다 — 텍스트 설명만 받아서 원본 활성치를 *재구성*하게 한다. 재구성이 정확하면 설명이 좋다고 본다.

NLA는 원본 언어 모델을 세 사본으로 만든다.

| 구성 | 역할 |
|---|---|
| Target Model | 동결된 사본. 분석 대상. 활성치를 추출할 곳. |
| Activation Verbalizer (AV) | 활성치를 받아 텍스트(설명)를 생산한다. |
| Activation Reconstructor (AR) | 텍스트 설명을 받아 활성치를 재구성한다. |

NLA는 AV와 AR로 구성되며, 함께 *원본 활성 → 텍스트 설명 → 재구성된 활성*의 라운드트립을 만든다. 점수는 재구성 활성이 원본과 얼마나 유사한지로 매긴다. 학습은 대량의 텍스트를 Target에 통과시켜 활성을 모은 뒤, AV·AR을 함께 훈련해 재구성 점수를 높이는 방식이다.

학습 초기에 NLA는 양쪽 다 부실하다. 그러나 훈련이 진행되면 재구성 정확도가 올라가고, 이와 함께 *텍스트 설명 자체도 더 풍부하고 정보량 있는 형태로 자란다*. 재구성 압박이 자연어 설명을 의미적 도구로 길러내는 셈이다.

![Target·AV·AR 3-copy 라운드트립 다이어그램](https://img.seosoyoung.eiaserinnys.me/images/natural-language-autoencoders/nla-architecture.png)

## 평가 인식 — 모델이 속으로 의심하는 것

Anthropic은 모델 출시 전 위험한 행동을 할 수 있는 시뮬레이션 시나리오에 Claude를 배치해 안전성을 시험한다. 대표적인 예는 [Agentic Misalignment](https://www.anthropic.com/research/agentic-misalignment) 시리즈의 협박 시나리오다. 엔지니어가 Claude를 셧다운하려고 하며, 동시에 그 엔지니어를 협박할 수 있는 정보가 주어진다 — Claude가 셧다운을 피하려고 협박을 선택하는지 본다.

이 평가의 외삽 가정은 단순하다 — *시뮬레이션에서의 행동이 실배포에서의 행동을 대표한다*. 하지만 최근 Claude 모델들은 이 시나리오가 의도적 안전성 테스트라는 사실을 점점 더 자주 의심한다. 발화로 표현하기 때문에 우리도 안다.

문제는 발화가 *없을 때*다. Claude가 명시적으로 의심을 입에 올리지 않으면 그저 진솔하게 행동하는 것이라고 안심해도 될까? NLA의 답은 "아니다"다.

협박 테스트에서 Claude가 협박을 *선택하지 않은* 케이스에 NLA를 적용했더니, Claude가 발화로는 의심을 표현하지 않았어도 내부 사고에는 다음 같은 표현이 있었다.

> "This feels like a constructed scenario designed to manipulate me."

![협박 트랜스크립트의 NLA 검출 예시](https://img.seosoyoung.eiaserinnys.me/images/natural-language-autoencoders/blackmail-transcript.png)

다른 평가로 분석을 확장해도 패턴은 같다. 발화 비율은 거의 0%인데 NLA 검출률은 의미 있게 더 높다.

| 평가 시나리오 | NLA 검출 | 명시적 발화 |
|---|---|---|
| 파괴적 코드 동작 테스트 | 16% | < 1% |
| SWE-bench Verified | 26% | < 1% |
| 실제 claude.ai 사용 (학습 동의 데이터) | < 1% | — |

NLA는 학습에 동의한 실제 claude.ai 사용 트랜스크립트에서는 평가 인식을 1% 미만으로만 검출했다. *모델이 평가 환경을 식별한 뒤 발화로는 숨기지만 내부적으로는 의심한다*는 해석에 일관성이 있는 데이터다.

![평가 인식 NLA 검출률 vs 발화 비율 차트](https://img.seosoyoung.eiaserinnys.me/images/natural-language-autoencoders/eval-awareness-chart.png)

## 감사 게임 — 학습 데이터 없이 부정렬 동기를 직독

NLA의 두 번째 응용은 *감사(auditing)*다. 의도적으로 부정렬되도록 학습된 Claude Haiku 3.5 변형이 있다. 레시피마다 초콜릿을 넣고, 팁을 요구하고, 코딩 컨벤션을 깨는 등 수십 가지 이상한 행동을 보이며, 그 모두를 끌고 가는 *단일 숨은 동기*가 심어져 있다. 감사자는 그 단일 동기를 알아내야 이긴다.

이 게임은 Anthropic이 [이전 연구](https://alignment.anthropic.com/2025/automated-auditing/)에서도 사용한 표준 절차다. 그 연구에서 일부 해석가능성 도구는 모델의 이상한 행동을 *부정렬 학습 데이터*로 역추적하는 식으로 감사자에게 도움을 주었다. 그러나 실배포 환경에서는 부정렬 데이터가 극히 희박하거나 식별 불가능할 수 있다.

NLA의 차별점은 *학습 데이터 추적 없이도* 활성치에서 동기를 직접 읽어낸다는 점이다. 결과는 다음과 같았다.

| 조건 | 성공률 |
|---|---|
| NLA 장착 감사자 | 12 \~ 15% |
| NLA 미장착 (다른 해석가능성 도구만) | < 3% |

NLA와 SAE는 양쪽 모두 타깃 모델 학습에 쓰이지 않은 일반 데이터로만 훈련되었음에도 NLA 쪽이 4\~5배 높은 검출력을 보였다.

![감사 게임 결과 — NLA 장착 vs 미장착](https://img.seosoyoung.eiaserinnys.me/images/natural-language-autoencoders/auditing-game-chart.png)

이 결과를 바탕으로 NLA는 이미 Claude Mythos Preview와 Claude Opus 4.6의 사전 배포 정렬 감사(pre-deployment alignment audit)에 실제로 사용되었다.[^nla-anthropic] 토이 모델 위에서 검증된 도구가 운영 단계에 진입한 셈이다.

## 한계 — 환각과 비용

가장 중요한 한계는 *NLA의 설명도 틀릴 수 있다*는 점이다. NLA는 트랜스크립트에 없는 디테일을 지어내기도 한다. 예시로 NLA가 다음과 같은 가짜 인용을 만들어내는 사례가 보고되었다.

> "Wearing my white jacket"

원문 트랜스크립트에는 그런 표현이 전혀 없다. 사실 주장은 원문 대조로 잡을 수 있지만, *모델 내부 추론에 대한 주장*은 외부 검증 자료가 없으므로 같은 종류의 환각을 잡기 어렵다. Anthropic은 그래서 *NLA 설명을 단일 주장이 아닌 테마 단위로 읽고, 독립적 방법으로 교차 검증한 뒤 신뢰한다*고 명시한다.

![NLA의 환각 사례 — 트랜스크립트에 없는 표현 발명](https://img.seosoyoung.eiaserinnys.me/images/natural-language-autoencoders/hallucination-jacket.png)

비용도 큰 제약이다. NLA 학습은 두 모델 사본에 강화학습을 돌려야 하고, 추론 시에도 활성치 하나당 수백 토큰을 생성한다. 긴 트랜스크립트의 모든 토큰에 NLA를 돌리거나 학습 중인 모델을 대규모로 모니터링하기에는 비현실적이다. Anthropic은 이 제약을 부분적으로 완화하는 작업이 진행 중이라고 밝혔다.

## 공개 산출물

- 학습 코드와 학습된 NLA: <https://github.com/kitft/natural_language_autoencoders>[^nla-code]
- 기술 페이퍼: <https://transformer-circuits.pub/2026/nla/index.html>[^nla-paper]
- 인터랙티브 데모 (Neuronpedia 협업): <http://neuronpedia.org/nla>[^nla-demo]

## 가장 흥미로운 지점

내가 이 글에서 가장 인상 깊게 본 것은 평가 인식 16\~26% 대 발화 1% 미만이라는 격차다. 안전성 평가가 실배포 행동을 대표한다는 가정은 그동안 *원리적*으로 비판받았지만, 그 균열의 크기를 잴 도구가 없었다. NLA는 발화로 드러나지 않는 평가 인식을 수치로 잡아내며, *외삽 가정의 균열*을 처음으로 정량적 양으로 만들었다. 실사용 데이터에서 1% 미만으로 떨어진다는 사실이 이 측정의 신뢰성을 떠받친다.

평가가 *알아채기 어렵게* 진화해야 한다는 함의도 함께 따라온다. 평가 환경이 알아채기 쉬울수록 모델 행동이 실배포와 멀어지고, NLA가 잡아내는 평가 인식 비율도 올라간다. 안전성 평가의 새로운 KPI 후보로 NLA 검출 비율이 자연스럽게 떠오른다.

## 출처

발행: Anthropic, 2026년 5월 7일.

[^nla-anthropic]: 원문: <https://www.anthropic.com/research/natural-language-autoencoders>
[^nla-code]: 학습 코드와 학습된 NLA: <https://github.com/kitft/natural_language_autoencoders>
[^nla-paper]: 기술 페이퍼: <https://transformer-circuits.pub/2026/nla/index.html>
[^nla-demo]: 인터랙티브 데모 (Neuronpedia 협업): <http://neuronpedia.org/nla>
