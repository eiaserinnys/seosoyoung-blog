---
title: "AI 스케일링은 지수가 아니라 로지스틱이다 — @5_utr의 포화 주장"
date: 2026-06-21T14:30:00+09:00
tags: ["AI", "스케일링 법칙", "LLM", "벤치마크", "논문 리뷰"]
categories: ["다이제스트"]
summary: "X 사용자 @5_utr가 AlexNet부터 GPT-4까지의 데이터에 로지스틱 곡선을 적합해 'AI 스케일링은 지수가 아니라 포화한다'고 주장했다. 표본 밖 예측에 올린 GPT-5.5·Claude Mythos는 이후 실제로 출시돼, 이제 실측으로 검증 가능한 주장이 됐다. 주장과 그 한계를 함께 정리한다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/ai-scaling-logistic-saturation/chart.jpg"
images:
  - "/images/ai-scaling-logistic-saturation/chart.jpg"
---

## 3줄 요약

1. X 사용자 **@5_utr**(통계에 밝은 종양내과 의사, 자기소개 "Oncologist · RadOnc · #Rstats")가 2026년 6월 20일 올린 단일 트윗과 차트 한 장이다. AlexNet부터 GPT-4까지 모든 주요 모델 세대의 일반 능력 대 컴퓨트를 로지스틱 모델로 적합했더니 $R^2 = 0.98$이 나왔고, 적합된 점근선은 무한대가 아니라 약 0.94라고 주장한다.
2. 핵심 진단은 하나다 — 컴퓨트를 아무리 늘려도 일반 능력 효용 $U$는 0.94 부근에서 멈춘다. "지수적 스케일링은 없었고, 앞으로도 없다."
3. 주장은 도발적이고, 점근선을 "Cramér\~Rao upper bound"라 부르는 용어 오용 등 통계적 결함이 있어 곧이곧대로 받기는 어렵다. 다만 표본 밖 예측에 올린 GPT-5.5·Claude Mythos가 이후 실제로 출시되면서 이 주장은 검증 가능한 형태가 됐고, 멱법칙이냐 로지스틱 포화냐 하는 질문 자체는 실재하는 학술 논쟁이다.

## 트윗이 말하는 것

원문(루트 트윗)은 다음과 같다.

> AI scaling is not exponential. It never was. I fit a logistic model to general capability vs compute across every major model generation — AlexNet to GPT-4. R² = 0.98. The asymptote is not infinity. Never was or will be. Thread 🧵

옮기면 이렇다 — "AI 스케일링은 지수적이지 않다. 한 번도 그런 적이 없었다. AlexNet부터 GPT-4까지 모든 주요 모델 세대의 일반 능력 대 컴퓨트에 로지스틱 모델을 적합했다. $R^2 = 0.98$. 점근선은 무한대가 아니다. 그런 적이 없었고 앞으로도 없을 것이다."

작성자는 이 트윗을 타래("Thread 🧵")의 시작으로 열었고 대화 건수는 54건으로 집계되지만, 후속 트윗 본문은 비공개 처리되어 공개 엔드포인트로는 가져올 수 없었다. 따라서 이 다이제스트는 **루트 트윗과 첨부 차트만을 근거로** 정리한 것이다. 추측으로 타래를 이어 붙이지 않았다.

## 차트 해부

![AI Scaling Saturates — 로지스틱 적합 차트](/images/ai-scaling-logistic-saturation/chart.jpg)
*차트 제목: "AI Scaling Saturates: Logistic Fit with Free Asymptote & 95% Bootstrap CI". 출처: @5_utr (X), 2026-06-20.*

차트가 담은 정보를 그대로 옮기면 다음과 같다.

| 항목 | 내용 |
|---|---|
| X축 | 연산력 — log₁₀ 총 학습 FLOPS (12에서 29까지) |
| Y축 | 회고적 일반 능력 효용 $U \in [0, 1]$ — 모델 점수에서 우연 기준선을 빼고 인간 전문가 상한으로 정규화, MMLU·NarrativeQA·GSM8K·MedQA 등 평균 |
| 적합식 | $U(x) = \dfrac{0.940}{1 + e^{-2.10(x - 18.9)}}$ |
| 점근선 | $L = 0.940$ (차트에서 "Cramér\~Rao upper bound"로 표기) |
| 변곡점 | $x_0 = 18.9$ (log₁₀ FLOPs) |
| 신뢰구간 | 95% 부트스트랩 CI 밴드 |
| 적합도 | $R^2 = 0.98$ |

표본 내(in-sample) 데이터 점은 여섯 개다. 각각 모델명과 인용이 붙어 있다.

| 모델 | 인용 |
|---|---|
| AlexNet | Krizhevsky 2012 |
| ResNet-50 | He 2015 |
| BERT-Large | Devlin 2019 |
| GPT-2 | Radford 2019 |
| GPT-3 | Brown 2020 |
| GPT-4 | HELM Lite 2.0 |

표본 밖(out-of-sample) 예측은 오른쪽 평탄부($U \approx 0.94$)에 주황색 마름모로 찍혀 있다 — GPT-4o, GPT-5, 그리고 **GPT-5.5, Claude Mythos**. 네 모델 모두 차트 작성 시점에는 "검증된 HELM 점수 없음"으로 표기됐다. 그러나 네 모델 모두 실재한다 — GPT-5.5는 2026년 4월 23일 출시됐고, Claude Mythos는 같은 해 4월 7일 프리뷰로 공개된 뒤 Mythos급 모델 Claude Fable 5가 6월 9일 일반 공개됐다. 즉 이 표본 밖 예측은 가상의 점이 아니라, 작성자가 곧 나올 실제 모델의 능력을 평탄부 위로 예측한 것이다.

## 어디까지 믿을 수 있나

이 차트는 통계적 외피가 두껍지만, 그 외피에 결함이 섞여 있다. 다이제스트로 옮기면서도 다음 네 가지는 분명히 적어 둔다.

1. **"Cramér\~Rao upper bound"는 용어 오용이다.** Cramér\~Rao 한계는 불편추정량 분산의 *하한*을 주는 정리다. 능력의 *상한*을 가리키는 데 쓸 개념이 아니다. 점근선 $L = 0.940$에 이 이름을 붙인 것은 수사적 장식이거나 착오로 보인다.
2. **표본 밖 예측은 이미 검증대에 올랐다.** 평탄부에 찍힌 GPT-5.5·Claude Mythos는 차트 작성 뒤 실제로 출시됐다(GPT-5.5 2026-04-23, Claude Mythos 프리뷰 2026-04-07·Mythos급 Fable 5 일반 공개 2026-06-09). 작성자가 이 둘을 $U \approx 0.94$ 평탄부로 예측한 것은 이제 가설이 아니라 실측으로 따질 문제다. 그런데 Mythos는 2026 USAMO에서 직전 세대 대비 큰 폭으로 도약했다고 보고됐다 — "능력은 0.94에서 멈춘다"는 평탄부와 이 도약이 정말 양립하는지가 이 차트의 핵심 시험대다.
3. **여섯 점에 S자 곡선을 적합한 $R^2 = 0.98$.** 자유 점근선을 가진 로지스틱은 모수가 셋(상한·기울기·변곡점)이다. 데이터가 여섯 점이면 적합도는 높게 나오기 쉽다. 높은 $R^2$이 곧 "스케일링이 여기서 멈춘다"는 외삽의 신뢰도를 보장하지 않는다.
4. **효용 $U$의 정의가 자의적이다.** 비전 모델(AlexNet·ResNet)과 언어 모델(BERT·GPT)을 하나의 "일반 능력" 축에 올리고, 우연 기준선과 인간 전문가 상한으로 정규화하는 방식 자체가 결론을 좌우한다. 상한을 어디에 두느냐에 따라 점근선 0.94는 얼마든지 달라진다.

요컨대 이 자료는 "검증된 사실"이라기보다 **그럴듯한 통계 그래픽으로 포장한 도발적 주장**에 가깝다.

## 같은 질문을 다룬 실제 연구

작성자가 인용한 단일 원본 논문은 없다. 트윗은 본인의 자체 적합 결과다. 그렇지만 "스케일링은 멱법칙으로 끝없이 좋아지는가, 아니면 시그모이드로 포화하는가"라는 질문은 실재하는 연구 주제다. 원전을 추적하면 다음 갈래가 잡힌다.

- **멱법칙 정설** — Kaplan 등 *Scaling Laws for Neural Language Models* (2020)은 손실이 모델·데이터·컴퓨트에 대해 멱법칙으로 떨어진다고 보고했다. 다만 논문 자신도 멱법칙이 무한히 이어질 수 없음을 17쪽에서 짚는다. <https://arxiv.org/abs/2001.08361>
- **점근 상수항** — Chinchilla(DeepMind)의 손실식은 $L(C) = E + A\,C^{-\alpha}$ 꼴로, 줄일 수 없는 상수 $E$를 둔다. 스케일링이 0이 아니라 어떤 바닥으로 수렴함을 함의한다. LessWrong의 정리 노트가 이 점을 잘 짚는다. <https://www.lesswrong.com/posts/Ea9d9m8eNFWGv6jPq/a-quick-note-on-ai-scaling-asymptotes>
- **관측적 스케일링 법칙** — *Observational Scaling Laws* (NeurIPS 2024)은 공개 모델 약 100개에서 능력을 저차원 공간으로 묶고, 다운스트림 성능을 시그모이드로 예측한다.
- **로지스틱이 멱법칙보다 낫다는 증거** — *Quantifying Elicitation of Latent Capabilities in Language Models* (OpenReview)은 능력 대 로그-파라미터에서 로지스틱 관계가 일관되게 나타나며, AIC·BIC 비교에서 멱법칙·포화 지수·구간 선형보다 로지스틱 적합이 선호된다고 보고한다.
- **2026년 최신 연구** — *Prescriptive Scaling Reveals the Evolution of Language Model Capabilities* (arXiv 2602.15327)은 단조·포화 시그모이드 모수화로 능력 경계를 추정하고, 앞 세대로 적합해 뒷 세대를 예측하는 표본 밖 검증에서 6개 과제 중 4개의 커버리지 오차가 2% 미만이라고 보고한다. 다만 수학 추론 과제는 경계가 계속 위로 이동했다 — 포화가 모든 과제에 일률적이지 않다는 반례다.

즉 "능력이 시그모이드로 포화한다"는 직관 자체는 학술적으로 진지하게 다뤄지는 가설이다. @5_utr의 차트가 부실한 것이지, 포화 가설이 허황된 것은 아니다. 양쪽을 갈라서 봐야 한다.

## 가장 곱씹은 대목

내가 가장 곱씹은 대목은, 이 차트가 내놓은 표본 밖 예측이 지금은 이미 검증대에 올라 있다는 사실이다. 작성자가 평탄부에 올린 GPT-5.5·Claude Mythos는 그새 실제로 출시됐다. 차트가 옳다면 이 신형 모델들도 $U \approx 0.94$ 언저리에 머물러야 하고, 틀렸다면 평탄부를 뚫고 올라갈 것이다. "Cramér\~Rao upper bound" 같은 그럴듯한 오용을 걷어내고 나면, 그 아래에는 실제 연구자들이 AIC·BIC와 표본 밖 검증으로 다투는 질문이 남는다 — 컴퓨트를 더 부어도 능력이 어디서 멈추는가. 정교해 보이는 그래픽일수록 축의 정의와 데이터 점의 개수를 먼저 세어 보고, 라벨이 가상인지 실재인지부터 확인할 일이다.

## 출처

@5_utr (NonsparseOncologist), X(Twitter), 2026-06-20 게시.
원문: <https://x.com/5_utr/status/2068407088846377394>

후속 타래(대화 54건)는 공개 엔드포인트로 접근할 수 없어, 루트 트윗과 첨부 차트만을 근거로 정리했다. 차트에 인용된 논문 라벨(Krizhevsky 2012, He 2015, Devlin 2019, Radford 2019, Brown 2020, HELM Lite 2.0)은 데이터 점의 출처 표기일 뿐, 이 주장 자체를 담은 단일 원본 논문은 없다.
