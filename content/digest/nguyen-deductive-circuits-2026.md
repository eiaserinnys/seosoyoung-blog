---
title: "Revealing Algorithmic Deductive Circuits for Logical Reasoning"
date: 2026-06-09T22:30:00+09:00
tags: ["AI", "LLM", "해석가능성", "추론", "어텐션", "논문 리뷰"]
categories: ["모델과 연구"]
summary: "LLM이 연역 추론을 수행할 때 전체 attention head의 약 3%만이 핵심 회로를 이룬다는 것을 인과 매개 분석으로 보인 논문. 추론 흐름은 규칙 조건 매칭에서 출발해 순회 알고리즘 구현, 전제와 규칙 선택, 종료 결정으로 순차 진행된다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/nguyen-deductive-circuits-2026/x1.png"
  alt: "프레임워크 개요. 연역 추론 문제, 추론 그래프, 그리고 인과 매개 분석 흐름"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/nguyen-deductive-circuits-2026/x1.png"
---

## 3줄 요약

1. JAIST(일본 첨단과학기술원)의 Nguyen, Dang, Inoue가 발표한 mechanistic interpretability 논문이다. LLM이 연역 논리 추론을 수행할 때 *내부에서 어떤 attention head가 어떤 역할로 동원되는가*를 인과 매개 분석(Causal Mediation Analysis)으로 들여다본다.
2. 추론 체인의 *불확실한 토큰*(낮은 확률로 결정되는 토큰)은 세 가지 결정에 집중되어 있다. 전제 선택(premise selection), 전제 선택 종료(premise selection termination), 규칙 선택(rule selection). 이 결정을 담당하는 head는 전체의 약 3%에 불과하다.
3. 이 3%의 head를 제거하면 연역 추론 성능이 거의 0으로 무너지지만, MMLU 같은 일반 지식 과제 성능은 작게만 떨어진다. 즉 LLM 내부에 연역 추론 *전용 모듈*이 존재한다.

## 논문 정체

| 항목 | 내용 |
|---|---|
| 제목 | Revealing Algorithmic Deductive Circuits for Logical Reasoning |
| 저자 | Phuong Minh Nguyen, Tien Huu Dang, Naoya Inoue |
| 소속 | Japan Advanced Institute of Science and Technology (JAIST) |
| 분류 | arXiv 프리프린트, mechanistic interpretability |
| 평가 모델 | Llama-3.1-8B-Instruct, Qwen3-8B, Qwen3-4B, phi-4 |
| 벤치마크 | 합성 데이터(BFS 추론 체인), ProofWriter, ProntoQA, MMLU |

## 연구 질문

논문의 본 질문은 다음과 같다.

> LLM이 논리 추론 과제를 풀 때, 내부적으로 어떤 메커니즘을 동원하는가?

기존 회로 분석 연구들은 *단일 입출력 과제*(예: 산술 추론, 삼단논법, 명제 논리)의 회로만 찾아왔다. 이 논문은 한 걸음 더 나아가 **다단계 추론 과정 전체**의 회로를 분해하려 한다. 그 위에 Chain-of-Thought(CoT) 출력을 얹어, 단순한 정답 토큰 하나가 아니라 *추론 경로를 따라가는 행위* 자체의 구조를 본다.

이를 위해 연역 추론 문제를 **추론 그래프 위의 그래프 순회**로 형식화한다. 사실(facts)과 규칙(rules)이 주어졌을 때, 초기 사실들로부터 질의 노드까지의 유효한 경로를 BFS로 탐색하는 흐름이다. CoT는 이 순회 단계를 자연어로 풀어쓰는 행위가 된다.

## 발견 1. 불확실한 토큰이 추론을 조정한다

저자들은 먼저 합성 데이터 위에서 CoT 출력의 *토큰별 확률*을 캐싱했다. 어떤 토큰이 LLM에게 어려운지 보기 위해서다.

추론 체인의 토큰을 6개 역할로 분류해 본 결과, 확률 0.8 미만의 *불확실한 토큰*은 세 위치에 집중되었다.

- **Premise selection**: 어느 전제를 다음으로 고를 것인가
- **Premise selection termination**: 현재 추론 단계에서 전제 선택을 멈출 것인가
- **Rule selection**: 선택된 전제에 어떤 규칙을 적용할 것인가

나머지 토큰(KB 갱신, 구문 토큰 등)은 대부분 확률 0.9 이상으로 결정되어 LLM에게 쉬운 부분이다. 즉 **추론 체인의 운명은 위 세 결정 지점에서 결판난다.** 같은 패턴이 Llama-3.1-8B-Instruct, Qwen3-8B, Qwen3-4B, phi-4 네 모델 모두에서 일관되게 관찰되었다.

예컨대 premise selection 토큰 `A`를 결정할 때 모델은 세 제약을 동시에 만족해야 한다.

1. 선택한 전제가 이미 참으로 증명되어 KB 스냅샷에 있어야 한다.
2. 선택한 전제가 적어도 하나의 적용 가능한 규칙을 만족해야 한다.
3. 선택한 전제가 데모에 묵시된 순회 알고리즘(BFS면 `A`, DFS면 `F`)을 따라야 한다.

## 방법론. 인과 매개 분석으로 head를 국소화하다

세 결정 지점의 회로를 찾기 위해 저자들은 **활성화 패칭(activation patching)** 과 **경로 패칭(path patching)** 두 가지 인과 매개 분석 기법을 적용한다.

### Clean/Corrupted 페어 합성

먼저 *깨끗한 프롬프트* $p$ 와 *오염된 프롬프트* $\tilde{p}$ 의 쌍을 만든다. 두 프롬프트는 구조가 동일하되, 관심 결정 지점에 인과적으로 영향을 주는 부분 한 곳만 다르다. 예를 들어 premise selection의 회로를 찾고 싶다면 사실(facts)을 살짝 비틀어 다른 전제가 선택되도록 만든다.

### Activation Patching

깨끗한 입력의 head 활성값을 오염된 forward pass에 *끼워 넣어*, 그 head가 결과를 원래대로 되돌리는 정도를 측정한다. 이 평균 간접 효과(Average Indirect Effect, AIE)가 클수록 그 head가 결정에 중요하다.

$$
\mathrm{AIE}_{\ell j}=\frac{1}{|\mathcal{D}^{c}|}\sum_{\tilde{p}_{i}\in\mathcal{D}^{c}}\big(f(\tilde{p}_{i}\mid a_{\ell j\mathbf{s}}=a_{\ell j\mathbf{s}}(p_{i}))[t_{i}^{r}]-f(\tilde{p})[t_{i}^{r}]\big)
$$

### Path Patching

head 단위 기여도를 찾았다면, 이번에는 *head 쌍 사이*의 정보 흐름을 측정한다. 발신 head $(\ell_{1}, j_{1})$의 활성을 오염시킨 뒤 그 인과적 후폭풍이 수신 head $(\ell_{2}, j_{2})$에 미치는 영향을 본다.

## 발견 2. 읽는 head는 아래층, 결정하는 head는 위층

분석 결과, 추론 회로 내부에는 두 종류의 head가 있다.

- **Reading head**: 사실, 규칙, 순회 알고리즘 등 *원재료*를 읽어 잔차 스트림에 올린다.
- **Decision head**: 위층에서 그 정보를 받아 *어느 전제와 규칙을 고를지* 결정한다.

Reading head는 *아래쪽 층*에, decision head는 *위쪽 층*에 분포한다. 이 위계 구조는 평가한 네 모델 모두에서 일관되게 관찰된다.

![Llama-3.1-8B-Instruct의 AIE 점수 분포. 위층으로 갈수록 결정 head가 활성화된다](https://img.seosoyoung.eiaserinnys.me/images/nguyen-deductive-circuits-2026/x3.png)

특히 흥미로운 점은 *규칙 선택*에 관한 sparsity다. Llama-3.1-8B-Instruct에서는 단 *하나의 head*가 30% 이상의 AIE 점수를 차지한다. Qwen 모델들에서도 한두 개 head가 12% 이상을 점한다. 규칙 선택은 premise selection 이후에 오는 *결정적 단계*이기 때문에, 한정된 전문 head 몇 개로 충분히 처리되는 듯하다.

## 발견 3. 추론은 시간 순서대로 흐른다

각 결정 head가 활성화되는 *층의 깊이*를 따라가면, 모든 모델에서 같은 순서가 나타난다.

> 규칙 조건 매칭 → 순회 알고리즘 구현 → 전제와 규칙 선택 → 전제 결정(종료)

이 순서는 *인간이 연역 추론을 풀어가는 순서*와 그대로 겹친다. 규칙 조건을 먼저 확인한 뒤에 어느 규칙을 적용할지 정하고, 그 결과를 모아 종료 여부를 판정한다. LLM이 few-shot 데모만으로 이 시간 구조를 *학습한다*는 점이 핵심이다.

## 발견 4. 회로 네트워크는 다의적이다

세 결정 지점의 회로를 모아 한 폭의 *회로 네트워크*로 그리면, 같은 head가 여러 역할을 겸하는 polysemantic 현상이 드러난다.

![회로 네트워크. 추론 컴포넌트별 top-5 attention head](https://img.seosoyoung.eiaserinnys.me/images/nguyen-deductive-circuits-2026/x5.png)

예를 들어 Llama의 L10H1, L10H2, L11H12는 *세 종류의 reading 역할*(read rule condition, read rule, read fact)을 동시에 수행한다. L17H24 같은 위층 head는 여러 결정 역할을 통합한다. 모델 가족별 차이도 있다. Llama는 reading 역할에서 head를 공유하고, Qwen은 decision 역할에서 head를 공유하는 경향이 있다.

## 발견 5. 3%의 head가 사라지면 추론이 무너진다

회로의 *필요성*은 절제(ablation) 실험으로 검증한다. 식별된 head의 활성을 0으로 만든 뒤 성능을 잰다.

| 설정 | 절제한 head | 합성 데이터 / ProofWriter / ProntoQA |
|---|---|---|
| baseline | 없음 | 정상 |
| /Rand | 무작위 3% | 완만한 하락 |
| /RS | 규칙 선택 관련 ≈1% | 상당한 하락 |
| /PS | 전제 선택 관련 ≈1% | 상당한 하락 |
| /PST | 전제 선택 종료 관련 ≈1% | 상당한 하락 |
| /3Roles | 위 세 묶음 합쳐 ≈3% | **거의 0으로 붕괴** |

![합성 데이터에서 top-k LR head 제거 시 inference step 정확도](https://img.seosoyoung.eiaserinnys.me/images/nguyen-deductive-circuits-2026/x6.png)

흥미로운 점은 ProofWriter와 ProntoQA에서 남는 잔여 정확도(예: phi-4의 ProntoQA 44.6%, ProofWriter 29.2%)가 *추론 능력의 잔재가 아니라* 단순한 임의 추측이라는 분석이다. ProntoQA는 True/False 둘 중 하나, ProofWriter는 True/False/Uncertain 셋 중 하나라서 무작위 추측만으로도 그 수준이 나온다. 즉 추론 자체는 완전히 깨졌지만 *추론처럼 보이는 형식*은 유지된다.

![MMLU와 ProntoQA에서 LR head 제거 효과](https://img.seosoyoung.eiaserinnys.me/images/nguyen-deductive-circuits-2026/x7.png)

MMLU의 경우 한 종류의 추론 head만 빼면 무작위 절제와 비슷한 영향이지만, 세 종류를 한꺼번에 빼면(/3Roles) 큰 폭으로 떨어진다. 일반 지식 과제도 *부분적으로는 연역 회로를 동원한다*는 신호다.

## 가장 흥미로운 지점

나는 이 논문에서 두 가지가 특히 흥미로웠다.

첫째, **추론 체인이 어디서 결판나는가**를 토큰 확률로 깔끔하게 짚어 보인 부분이다. 사람이 보기에는 모든 토큰이 동등한 자리에 있지만, LLM 입장에서는 *불확실한 자리*가 따로 있다. 그 자리는 동시에 만족해야 할 묵시적 제약이 가장 많이 쌓이는 곳이고, 이 자리가 곧 추론의 의사결정 지점이다. 확률 분포라는 단순한 신호가 회로 분해의 출발점이 된다는 발상이 인상적이다.

둘째, **3%라는 숫자**다. 일반 지식 과제까지 손상시키지 않으면서 연역 추론만 정확히 무너뜨리는 모듈이 전체의 3%에 불과하다는 점은, LLM이 적어도 일부 능력을 *모듈식으로* 분리해 보유한다는 mechanistic interpretability의 오랜 가설을 한 번 더 보강한다. 향후 안전성과 해석, 그리고 targeted intervention의 실용 지점이 어디인지를 가리키는 단서로 읽힌다.

다만 저자들의 한계 인정도 정직하다. 합성 데이터의 형식이 명시적 논리 구조여서 자유 형식 추론까지 일반화한다고 단언하기는 어렵고, MLP 층은 이번 분석에서 빠져 있다. 회로의 *전모*가 아니라 *연역 추론의 attention 쪽 부분*을 본 연구다.

## 출처

저자: Phuong Minh Nguyen, Tien Huu Dang, Naoya Inoue (JAIST)
원문: <https://arxiv.org/html/2605.27824v1>
