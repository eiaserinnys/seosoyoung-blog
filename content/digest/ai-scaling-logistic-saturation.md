---
title: "AI 스케일링은 지수가 아니라 로지스틱이다 — @5_utr의 포화 주장"
date: 2026-06-21T14:30:00+09:00
tags: ["AI", "스케일링 법칙", "LLM", "벤치마크", "경제·금융"]
categories: ["다이제스트"]
summary: "통계에 밝은 종양내과 의사 @5_utr가 AlexNet부터 GPT-4까지의 데이터에 로지스틱 곡선을 적합해 'AI 스케일링은 지수가 아니라 포화한다'고 주장했다. 타래의 진짜 칼끝은 거시경제다 — AI 밸류에이션이 지수함수로 가격책정됐는데 데이터는 로지스틱이 훨씬 잘 맞으니 함수형 오설정이자 버블이라는 것. 주장과 그 한계를 함께 정리한다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/ai-scaling-logistic-saturation/chart.jpg"
images:
  - "/images/ai-scaling-logistic-saturation/chart.jpg"
---

## 3줄 요약

1. X 사용자 **@5_utr**(통계에 밝은 종양내과 의사, 자기소개 "Oncologist · RadOnc · #Rstats")가 2026년 6월 20일 올린 여덟 개 트윗 타래다. AlexNet부터 GPT-4까지 모든 주요 모델 세대의 일반 능력 대 컴퓨트를 로지스틱 모델로 적합했더니 $R^2 = 0.98$, 적합된 점근선은 무한대가 아니라 약 0.94라고 주장한다.
2. 타래의 칼끝은 기술이 아니라 **거시경제**다 — 엔비디아·OpenAI·하이퍼스케일러 capex로 이어지는 AI 밸류에이션은 지수함수 $e^{at}$를 전제로 가격이 매겨졌는데, 데이터는 로지스틱이 훨씬 잘 맞으니 이는 함수형 오설정이고 곧 거품이라는 것.
3. 메커니즘은 편향-분산 분해다 — 점근선은 Cramér\~Rao 하한이 정하는 "편향 바닥"이며, 컴퓨트는 분산만 줄일 뿐 훈련 분포의 편향은 못 줄인다(GIGO). 다만 차트엔 "upper bound" 오기, 여섯 점에 적합한 곡선 등 통계적 결함이 적지 않다.

## 타래의 논증

타래는 여덟 개 트윗으로 이어진다. 순서대로 옮긴다.

**① 명제 — 스케일링은 지수가 아니다.**

> AI scaling is not exponential. It never was. I fit a logistic model to general capability vs compute across every major model generation — AlexNet to GPT-4. R² = 0.98. The asymptote is not infinity. Never was or will be.

"AI 스케일링은 지수적이지 않다. 한 번도 그런 적이 없었다. AlexNet부터 GPT-4까지 모든 주요 세대의 일반 능력 대 컴퓨트에 로지스틱을 적합했다. $R^2 = 0.98$. 점근선은 무한대가 아니다."

**② 방법 — 효용의 정의.**

> Utility defined as (model score − chance) / (human ceiling − chance) averaged across MMLU, NarrativeQA, GSM8K, MedQA on a fixed suite. Vision-era models scored on the full suite including language, intentionally.

효용 $U$는 (모델 점수 − 우연) / (인간 상한 − 우연)을, MMLU·NarrativeQA·GSM8K·MedQA 고정 묶음에서 평균한 값이다. 비전 시대 모델도 언어를 포함한 전체 묶음으로 채점했다 — "의도적으로".

**③ 이론 — 점근선은 가정이 아니라 정리다.**

> This isn't just curve fitting. The Cramér-Rao lower bound is ironclad: there is a hard information-theoretic ceiling on what you can extract from a finite training distribution regardless of compute. The asymptote is a theorem, not an assumption. L was fit as a free parameter.

"이건 단순 곡선 맞추기가 아니다. Cramér\~Rao 하한은 철벽이다 — 유한한 훈련 분포에서 뽑아낼 수 있는 정보에는 컴퓨트와 무관한 정보이론적 천장이 있다. 점근선은 가정이 아니라 정리다. $L$은 자유 모수로 적합했다." (※ 차트 라벨은 "upper bound"라 적혀 본문과 어긋난다 — 아래 검증 참조.)

**④ 증거 — 이미 변곡점을 지났다.**

> ∂U/∂x at GPT-4: 0.00001 / ∂²U/∂x² throughout the GPT era: negative / We passed the inflection point at BERT-Large. Every subsequent model generation has been buying movement along a curve that is basically flat. Stargate is buying horizontal movement

GPT-4 지점의 1차 도함수는 0.00001, GPT 시대 내내 2차 도함수는 음수. 변곡점은 BERT-Large에서 이미 지났고, 이후 모든 세대는 사실상 평평한 곡선 위를 기어왔을 뿐이다. "Stargate는 수평 이동을 사는 중이다."

**⑤ 거시경제 — 버블 명제.**

> The entire bull case for AI valuations is predicated on e^{at}. Nvidia, OpenAI, hyperscaler capex, all priced on exponential functional form. The logistic fits dramatically better. Functional form misspecification is as obvious as day here. What a hype bubble 🫧

AI 밸류에이션의 모든 강세론은 $e^{at}$를 전제한다. 엔비디아·OpenAI·하이퍼스케일러 capex가 죄다 지수 함수형으로 가격책정됐다. 로지스틱이 압도적으로 잘 맞는다. 함수형 오설정이 대낮처럼 명백하다 — "이게 거품이다."

**⑥ 실물 신호 — 2차 도함수가 음으로.**

> This week: FT reports companies curbing AI deployments as costs outpace ROI. This is not a demand problem. It's the second derivative turning negative in the real economy.

이번 주 FT는 비용이 ROI를 앞질러 기업들이 AI 도입을 줄이고 있다고 보도했다. 수요 문제가 아니라, 실물 경제에서 2차 도함수가 음으로 돌아선 것이다. (작성자는 LeCun·Gary Marcus·Chollet·Galloway·Damodaran을 태그했다.)

**⑦~⑧ 메커니즘 — 컴퓨트는 분산만 줄인다.**

> Cramér-Rao formalizes your data quality argument: MSE = variance + bias². Scaling compute reduces variance asymptotically. It cannot reduce bias in the training distribution.

> Garbage in, garbage out regardless of GPU count. The logistic ceiling IS the bias floor. No amount of Stargate fixes a biased training distribution and limited information content.

Cramér\~Rao는 데이터 품질 논증을 형식화한다 — $\text{MSE} = \text{variance} + \text{bias}^2$. 컴퓨트를 키우면 분산은 점근적으로 0에 수렴하지만, 훈련 분포의 편향은 줄지 않는다. GPU 개수와 무관하게 garbage in, garbage out. **로지스틱 천장이 곧 편향 바닥이다.** 어떤 Stargate도 편향된 훈련 분포와 제한된 정보량을 고치지 못한다.

작성자는 이 메커니즘을 의학통계 도식 한 장으로 보강했다.

![EHR vs RCT 신뢰성 — 표본을 아무리 키워도 편향은 남는다](/images/ai-scaling-logistic-saturation/bias-variance.jpg)
*Frank Harrell(@f2harrell)의 도식. 전자건강기록(EHR)은 표본을 무한히 늘려도 RMSE가 2에서 멈추지만(편향 바닥), 편향 없는 무작위 임상시험(RCT)은 표본 64명만으로 무한 EHR과 같은 정확도에 닿는다. 작성자는 표본 크기를 컴퓨트에, EHR의 편향을 훈련 분포의 편향에 빗댄다.*

## 차트 해부

![AI Scaling Saturates — 로지스틱 적합 차트](/images/ai-scaling-logistic-saturation/chart.jpg)
*차트 제목: "AI Scaling Saturates: Logistic Fit with Free Asymptote & 95% Bootstrap CI". 출처: @5_utr (X), 2026-06-20.*

| 항목 | 내용 |
|---|---|
| X축 | 연산력 — log₁₀ 총 학습 FLOPS (12에서 29까지) |
| Y축 | 회고적 일반 능력 효용 $U \in [0, 1]$ — 우연 기준선을 빼고 인간 전문가 상한으로 정규화 |
| 적합식 | $U(x) = \dfrac{0.940}{1 + e^{-2.10(x - 18.9)}}$ |
| 점근선 | $L = 0.940$ (차트에서 "Cramér\~Rao upper bound"로 표기) |
| 변곡점 | $x_0 = 18.9$ (log₁₀ FLOPs) |
| 신뢰구간 | 95% 부트스트랩 CI 밴드 |
| 적합도 | $R^2 = 0.98$ |

표본 내(in-sample) 데이터 점은 여섯 개다.

| 모델 | 인용 |
|---|---|
| AlexNet | Krizhevsky 2012 |
| ResNet-50 | He 2015 |
| BERT-Large | Devlin 2019 |
| GPT-2 | Radford 2019 |
| GPT-3 | Brown 2020 |
| GPT-4 | HELM Lite 2.0 |

표본 밖(out-of-sample) 예측은 오른쪽 평탄부($U \approx 0.94$)에 주황색 마름모로 찍혀 있다 — GPT-4o, GPT-5, GPT-5.5, Claude Mythos. 네 모델 모두 "검증된 HELM 점수 없음"으로 표기됐다. 작성자가 이들을 HELM으로 직접 채점하지 않고, 적합한 곡선이 내놓는 예측값으로 평탄부에 얹었다는 뜻이다.

## 어디까지 믿을 수 있나

타래는 외피가 두껍고 논증의 골격도 또렷하다. 그래도 다음 네 가지는 갈라 두고 읽어야 한다.

1. **Cramér\~Rao 적용은 유비이지 정리가 아니다.** 타래 본문은 "lower bound"로 올바로 쓰고 $\text{MSE} = \text{variance} + \text{bias}^2$로 편향 바닥을 설명한다 — 이 직관 자체는 통계적으로 멀쩡하다. 문제는 두 가지다. 첫째, **차트 라벨은 "upper bound"라 적혀 본문과 어긋난다.** 둘째, Cramér\~Rao는 본래 *불편추정량의 분산 하한*에 관한 정리다. "모델 능력"에는 추정 대상 모수도, 추정량도 명확히 정의돼 있지 않다. 로지스틱 점근선이 곧 정보이론적 편향 바닥과 같다는 것은 *주장*이지 유도된 결과가 아니다.
2. **최신 모델을 측정이 아니라 예측으로 평탄부에 얹었다.** 작성자는 GPT-5.5·Claude Mythos를 HELM으로 채점하지 않고 곡선의 예측값($U \approx 0.94$)으로 찍었다. "최신 모델조차 천장에 붙어 있다"는 그림은 측정의 결과가 아니라 적합된 곡선이 구성상 당연히 내놓는 값이다 — 곡선을 가정해야 나오는 결론이다.
3. **여섯 점에 S자 곡선을 적합한 $R^2 = 0.98$.** 자유 점근선을 가진 로지스틱은 모수가 셋(상한·기울기·변곡점)이다. 데이터가 여섯 점이면 적합도는 높게 나오기 쉽다. 높은 $R^2$이 곧 "여기서 멈춘다"는 외삽의 신뢰도를 보장하지 않는다.
4. **S자 모양 일부는 채점 방식이 만들어 낸다.** 비전 모델(AlexNet·ResNet)을 언어 과제까지 포함한 묶음으로 "의도적으로" 채점하면, 저컴퓨트 구간은 우연 수준($U \approx 0$)에 고정된다. 곡선 바닥을 인위적으로 눌러 놓는 셈이라, S자의 가파른 상승과 평탄부는 부분적으로 측정 설계의 산물일 수 있다.

요컨대 이 자료는 "검증된 사실"이라기보다 **그럴듯한 통계 외피로 포장한, 그러나 골격은 진지한 도발적 주장**이다.

## 같은 질문을 다룬 실제 연구

작성자가 인용한 단일 원본 논문은 없다. 타래는 본인의 자체 적합과 거시경제 해석이다. 그렇지만 "스케일링은 멱법칙으로 끝없이 좋아지는가, 시그모이드로 포화하는가"라는 질문은 실재하는 연구 주제다.

- **멱법칙 정설** — Kaplan 등 *Scaling Laws for Neural Language Models* (2020). 손실이 멱법칙으로 떨어지지만, 논문 자신도 멱법칙이 무한히 이어질 수 없음을 짚는다. <https://arxiv.org/abs/2001.08361>
- **점근 상수항** — Chinchilla(DeepMind)의 손실식 $L(C) = E + A\,C^{-\alpha}$는 줄일 수 없는 상수 $E$를 둔다. @5_utr의 "편향 바닥"과 통하는 발상이다. <https://www.lesswrong.com/posts/Ea9d9m8eNFWGv6jPq/a-quick-note-on-ai-scaling-asymptotes>
- **관측적 스케일링 법칙** — *Observational Scaling Laws* (NeurIPS 2024)은 공개 모델 약 100개에서 다운스트림 성능을 시그모이드로 예측한다.
- **로지스틱이 멱법칙보다 낫다는 증거** — *Quantifying Elicitation of Latent Capabilities in Language Models* (OpenReview)은 AIC·BIC 비교에서 멱법칙·포화 지수·구간 선형보다 로지스틱 적합이 선호된다고 보고한다.
- **2026년 최신 연구** — *Prescriptive Scaling Reveals the Evolution of Language Model Capabilities* (arXiv 2602.15327)은 포화 시그모이드로 능력 경계를 추정하고, 앞 세대로 적합해 뒷 세대를 예측하는 표본 밖 검증에서 6개 과제 중 4개의 커버리지 오차가 2% 미만이라 보고한다. 다만 수학 추론은 경계가 계속 위로 이동했다 — 포화가 일률적이지 않다는 반례다.

즉 "능력이 시그모이드로 포화한다"는 직관은 학술적으로 진지하게 다뤄지는 가설이다. @5_utr의 차트 디테일이 부실한 것이지, 포화 가설 자체가 허황된 것은 아니다.

## 가장 곱씹은 대목

내가 가장 곱씹은 대목은, 이 타래가 결국 기술 논쟁이 아니라 **가격 논쟁**이라는 점이다. 작성자는 "능력이 멈춘다"에서 멈추지 않고 "그러니 $e^{at}$로 가격을 매긴 자본시장이 함수형을 잘못 골랐다"로 곧장 건너뛴다. 차트의 약점(여섯 점, 채점 설계, 라벨 오기)을 다 인정하더라도, 던지는 질문은 묵직하다 — 만약 능력이 로지스틱이라면, 지수를 전제한 밸류에이션은 무엇을 사고 있는 것인가. 다만 그 묵직함이 차트의 엄밀함을 보증하진 않는다. 가장 도발적인 그림 — 최신 모델조차 천장에 붙어 있다는 평탄부 — 은 측정된 점이 아니라 곡선이 스스로 그린 예측이었다. 결국 곡선을 믿어야 곡선의 결론에 닿는다. 정교해 보이는 그래픽일수록 축의 정의와 데이터 점의 개수부터 세어 볼 일이다.

## 출처

@5_utr (NonsparseOncologist), X(Twitter), 2026-06-20 게시. 여덟 개 트윗 타래.
원문(첫 트윗): <https://x.com/5_utr/status/2068407088846377394>

차트에 인용된 논문 라벨(Krizhevsky 2012, He 2015, Devlin 2019, Radford 2019, Brown 2020, HELM Lite 2.0)은 데이터 점의 출처 표기일 뿐, 이 주장 자체를 담은 단일 원본 논문은 없다. 본문 도식은 Frank Harrell(@f2harrell)의 EHR\~RCT 신뢰성 비교를 작성자가 인용한 것이다.
