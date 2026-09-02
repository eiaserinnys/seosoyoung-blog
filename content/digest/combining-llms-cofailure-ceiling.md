---
title: "When Does Combining Language Models Help? A Co-Failure Ceiling on Routing, Voting, and Mixture-of-Agents Across 67 Frontier Models"
date: 2026-07-13T20:00:00+09:00
tags: ["AI", "LLM", "멀티에이전트", "벤치마크", "앙상블"]
categories: ["모델과 연구"]
summary: "라우팅·다수결·캐스케이드·MoA 등 어떤 LLM 오케스트레이션도 β(모든 모델이 같은 질의에서 함께 실패하는 비율)로 상한이 정해진다. 관행적으로 보고되는 pairwise error correlation ρ는 β를 원리적으로 볼 수 없다. 67개 프론티어 모델·21개 프로바이더에서 tetrachoric 단일요인 모델도 실측 β를 2.5배 과소예측했고, 같은 GPQA 문항을 free-response로 재출제하면 β=0이 0.127로 열린다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/combining-llms-cofailure-ceiling/fig3.png"
  alt: "Refer to caption"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/combining-llms-cofailure-ceiling/fig3.png"
---

## 3줄 요약

1. KAIKAKU의 Josef Chen이 2026년 6월 arXiv에 올린 논문이다. 어떤 라우터·투표·캐스케이드·MoA도 $1-\beta$를 넘을 수 없고, 여기서 $\beta$는 <em>모든 모델이 같은 질의에서 함께 실패하는 비율</em>이다. 관행적으로 보고되는 pairwise error correlation $\rho$로는 이 $\beta$를 원리적으로 볼 수 없다 (Fréchet class 비식별).
2. 67개 프론티어 모델·21개 프로바이더의 시장 스케일 측정에서 MATH-500 co-failure는 $\beta=0.052$였고, 제대로 tetrachoric으로 보정한 단일요인 Gaussian copula조차 이를 2.5배 과소예측했다. Pool 크기를 $k=2$에서 $k=67$로 늘리면 underpricing 비율이 $1.0 \to 2.5$로 단조 증가한다.
3. 같은 GPQA-Diamond 문항을 객관식에서 자유서술로 바꾸기만 해도 $\beta$가 사실상 0에서 0.127로 열린다. Co-failure는 과목이 아니라 답변 형식(open-endedness) 자체를 추적하며, 오케스트레이션의 레버는 모델 <em>수</em>가 아니라 <em>실패 모드의 이질성</em>이다.

## 배경 — 오케스트레이션은 자원 할당 문제

기업은 지금 하나가 아니라 수백 개의 모델을 프로바이더 수십 곳에서 골라 프로덕션 트래픽에 얹는다. 어느 모델이 최고인가라는 질문은 <em>한정된 달러와 토큰 예산을, 이질적이고 상관된, 빠르게 감가상각하는 모델 풀에 어떻게 배분할 것인가</em>로 옮겨 왔다. 실무의 답은 하나의 진단 지표에 실려 있다 — 모델 사이의 pairwise error correlation $\rho$. $\rho$가 낮으면 다양성이 값을 지불한다는 신호다.

Chen은 이 진단 지표가 잘못된 것을 다룬다고 주장한다. 오케스트레이션의 상한을 잡는 것은 $\rho$가 아니라 $\beta$, 즉 <em>모든 모델이 같은 질의에서 함께 실패하는 비율</em>이다. 그리고 $\rho$는 $\beta$를 원리적으로 볼 수 없다.

## 이론 — $\beta$ 상한과 pairwise $\rho$의 맹점

### 상한과 인증서 (Proposition 1)

$\beta = \Pr_t[\text{모든 } m \text{개가 오답}]$, $a_{\text{sb}} = \max_i \bar{q}_i$라 두자.

- **(i) 상한.** 라우터·(가중)투표·캐스케이드 등 출력이 회원 모델의 답 중 하나가 되는 모든 selection policy의 정확도는 $1-\beta$를 넘을 수 없다. 상한을 달성하는 것은 per-query oracle이며, single-best 대비 최대 이득은 정확히 $\Delta^{\text{ceil}} = (1-\beta) - a_{\text{sb}}$다.
- **(ii) 이득 분해.** 오라클 이득 $G = V^o - a_{\text{sb}} = \Pr_t[\text{single-best 오답}] - \beta$. 이득은 non-unanimous하고 single-best가 틀린 *resolvable* 영역에서만 나온다. Co-failure tail $\beta$는 이득에 아무것도 기여하지 않는다.
- **(iii) 인증서.** $n$개의 i.i.d. 질의 중 $K$개에서 모든 모델이 틀리면, Clopper-Pearson 하한 $\beta_{\text{lo}}(K, n, \delta)$로 확률 $\geq 1-\delta$에서 $\text{Acc} - a_{\text{sb}} \leq (1-\beta_{\text{lo}}) - a_{\text{sb}}$가 보장된다. 이 인증 상한이 오케스트레이션 오버헤드보다 낮으면 어떤 정책도 수지가 안 맞는다는 <em>$0 pre-deployment 검정</em>이 된다 (라우터를 학습시키기도 전에).

주의할 함정 하나 — 작은 $\beta$는 <em>오케스트레이션이 무의미하다</em>가 아니라 <em>상한이 높게 열려 있다</em>는 뜻이다. 상한이 좁아지는 것은 $\beta$가 커지거나 $a_{\text{sb}}$가 이미 상한 근처에 있을 때다.

### pairwise $\rho$가 $\beta$를 볼 수 없는 이유 (Proposition 2, 3)

각 질의가 확률 $\pi$로 <em>공통 하드</em>가 되어 모든 $m$개 모델이 함께 틀리고, 아니면 확률 $\alpha_0$로 독립 실패하는 common-shock 혼합 모델을 생각하자. Marginal error rate은 $\alpha = \pi + (1-\pi)\alpha_0$, pairwise error correlation은

$$\bar{\rho} = \frac{\pi + (1-\pi)\alpha_0^2 - \alpha^2}{\alpha(1-\alpha)} > 0$$

이며 실제 co-failure rate은 $\beta(m) = \pi + (1-\pi)\alpha_0^m$이다. $m \to \infty$에서 $\beta(m) \downarrow \pi > 0$인 반면, $(\alpha, \bar{\rho})$에 맞춰진 단일요인 Gaussian copula의 $\beta_{\text{sf}}(m)$은 0으로 수렴한다. Gaussian copula의 lower tail dependence가 0이기 때문이다. 결과: underpricing 비율 $\beta(m)/\beta_{\text{sf}}(m) \to \infty$, pool 크기가 커질수록 벌어진다.

더 강한 진술은 Proposition 3다 — $m \geq 3$에서 $\beta$는 pairwise error law의 함수가 *아니다*. 동일한 1·2차 marginal, 동일한 Pearson·tetrachoric $\rho$를 가지면서 $\beta$가 다른 결합 분포가 존재한다 (Fréchet class는 양의 차원을 가진다). 따라서 pairwise $\rho$에서 계산된 어떤 통계량도 $\beta$를 원리적으로 식별할 수 없다.

원인은 lower tail dependence 자체가 아니라 *common-mode atom*(Marshall–Olkin형 공유 실패 성분)이다. Chen은 시뮬레이션으로 이 구분을 확인한다 — Clayton copula($\lambda_L = 0.71$)는 $m=53$에서 4.0배 유한한 underpricing만 만들고 $\lambda_L$이 커지면 오히려 줄어드는(pairwise $\rho$가 그만큼 올라가서 단일요인 모델이 흡수하므로) 반면, $\beta_\infty = 0.05$인 shared-failure atom은 ratio를 $10^7$배까지 발산시킨다.

## 시장 스케일 측정 — 67개 모델·21개 프로바이더

Chen은 pillar 실험(15개 모델)에서 시작해 시장 스케일 측정을 위해 OpenRouter의 라이브 프론티어 카탈로그를 그대로 끌어와 67개 모델·21개 프로바이더 풀로 확장한다 — GPT-5.5, Claude Opus 4.8, Gemini 3.1 Pro, Grok-4.3, DeepSeek V4, Qwen3.7-Max, Kimi K2.7부터 작은 open-weight까지. 하드 도메인 세 종을 겨눈다: open-ended 수학(MATH-500, MATH-Hard Level-5, AIME 2024/2025), 대학원 수준 과학(GPQA-Diamond), 그리고 실행 채점 코드(code_contests, 레이팅 1900–3500).

![Refer to caption](https://img.seosoyoung.eiaserinnys.me/images/combining-llms-cofailure-ceiling/fig2.png)
*Figure 2: Co-failure 잔차는 common-mode atom이지 copula misspecification이 아니다. 세 예측(단일요인 tetrachoric 0.021, 완전 67×67 Gaussian copula 0.023) 대비 실측 $\beta = 0.052$는 nearest-PSD full-$\Sigma$ Gaussian fit도 2.25배 초과한다. 우측: pool 크기를 무작위로 스캔하면 underpricing 비율이 $k=2$의 1.0에서 $k=67$의 median 2.5까지 단조 증가한다.*

핵심 발견을 순서대로 짚는다.

- **MATH-500 (n=330, 67 모델).** 모든 모델이 같은 문제를 놓친 비율은 $\beta = 0.052$였다 (k=17 all-wrong, Clopper–Pearson 95% [0.030, 0.081]). Tetrachoric $\bar{\rho} = 0.78$로 보정한 단일요인 Gaussian copula의 예측은 $\beta_{\text{sf}} = 0.021$ — 실측이 약 **2.5배** 두꺼웠다 (bootstrap 90% CI 1.7–3.4배). 실측 $\beta$를 재현하려면 implied $\rho_{\text{eff}} = 0.89$가 필요하다(측정된 0.78보다 훨씬 크다).
- **Full-$\Sigma$ Gaussian copula로도 안 됨.** 67×67 pairwise-tetrachoric 상관행렬을 그대로 쓴 nearest-PSD Gaussian copula Monte-Carlo도 $\beta_{\text{full-}\Sigma} = 0.023$에 그쳐 실측 대비 **2.25배** 잔차가 남았다. Clayton copula($\lambda_L = 0.69$)도 $\beta = 0.026$(1.96배 잔차)에 그친다. 잔차는 어떤 exchangeable pairwise-calibrated copula로도 설명되지 않는 — common-mode atom의 지문이다.
- **Pool 크기가 드라이버다.** 무작위 $k$-모델 부분집합(k당 60개 리샘플)에서 tetrachoric underpricing 비율이 $k=2$의 1.0에서 $k=67$의 median 2.5(5–95% band [2.1, 2.7])까지 단조 증가했다. 모든 부분집합이 populated tail을 보였다 — 특정 모델 조합이 아니라 pool 크기 자체가 드라이버라는 뜻이다. GPT-5.5를 포함한 최신 프론티어에서도 co-failure는 지속된다.
- **Calibration trap.** 초기 버전에서 0/1 correctness indicator의 순수 Pearson 상관 $\bar{\rho} = 0.53$으로 단일요인 copula를 보정하면 $\beta_{\text{sf}} = 0.0016$이 나와 실측 대비 32배라는 스푸리어스 결과가 뜬다. 실제 정본은 20세기 심리계량학의 tetrachoric(잠재변수) 상관이며, LLM 평가 문헌은 이 세기말 상식을 자주 잊는다.

MATH-Hard(n=298)에서도 $\beta = 0.044$, 실행 채점 코드(n=63)에서도 $\beta = 0.079$로 tail이 populated 상태였고, tetrachoric 단일요인 모델의 underpricing이 3.1배(90% CI [1.5, 6.2])로 1을 벗어난다. Co-failure의 시그니처는 세 개의 구조적으로 분리된 open-ended 도메인에 걸쳐 재현된다.

## 두 국면 — 상한이 낮거나, 라우터가 못 잡거나

이득 분해 identity $G = \Pr[\text{single-best 오답}] - \beta$는 오케스트레이션 헤드룸이 두 가지 정반대 방식으로 봉쇄될 수 있음을 알려 준다.

![Refer to caption](https://img.seosoyoung.eiaserinnys.me/images/combining-llms-cofailure-ceiling/fig4.png)
*Figure 4: 두 국면. 도메인별 all-models-wrong 비율 $\beta$와 95% Clopper–Pearson 신뢰구간. Ceiling-bound 도메인(open-ended 수학·코드, free-response GPQA)은 $\beta > 0$의 co-failure tail이 모든 selection policy를 $1-\beta$에서 봉쇄하며 pairwise $\rho$는 2.5–8.3배(tetrachoric) 과소예측한다. Realizability-bound 도메인(객관식 GPQA, MMLU-Pro)은 $\beta \approx 0$이라 오라클 이득이 순수 resolvable disagreement인데도 라우터가 이를 잡지 못한다.*

- **Ceiling-bound (수학·코드).** MATH-500은 $\beta = 0.052$의 co-failure tail로 모든 정책을 $1-\beta$에서 봉쇄한다. Pairwise $\rho$가 이 상한을 원리적으로 볼 수 없어 시장 리포트가 잘못된 신호를 준다. Single-best가 이미 상한 근처에 있어 오케스트레이션 이득 자체가 원천적으로 작다.
- **Realizability-bound (객관식 과학).** GPQA-Diamond의 52-모델 complete-coverage subset에서 $\beta$는 사실상 0(130개 중 0개 all-wrong, CP 상한 0.03)이라 이론적 상한이 열려 있다. 그런데 오라클 이득 $G = 0.15$로 크다 — 이득이 전부 resolvable disagreement인데도 배포 가능한 라우터가 이를 못 잡는 *routing regret*이 지배한다. 상한이 아니라 실현 가능성이 병목이다.

세 도메인이 두 국면으로 명확히 갈리고, pairwise $\rho$는 어느 국면인지 알려주지 못한다. Clopper-Pearson 인증서만이 답한다.

## 형식이 국면을 결정한다

Chen이 개인적으로 가장 강조하는 실험은 content-controlled test다. 같은 79개 GPQA-Diamond 문항을 두 형식으로 출제했다.

*Figure 3: 형식이, 내용이 아니라, 국면을 결정한다. 동일한 79개 GPQA-Diamond 문항을 객관식(위)과 자유서술(아래, 옵션 제거 후 5-judge LLM panel 채점, $\kappa$ 0.73–0.92)로 각각 출제. 형식만 바꿔도 객관식에서 $\beta \approx 0$이던 co-failure 블록이 자유서술에서 10/79($\beta = 0.127$, CP [0.062, 0.220])로 열리고, 평균 정확도는 $0.66 \to 0.51$로 떨어진다. 오렌지 셀은 모든 모델이 함께 틀린 문항.*

- 객관식(원본): $\beta \approx 0$.
- 자유서술(옵션 제거, 5-judge LLM panel, pairwise $\kappa$ 0.73–0.92): $\beta = 0.127$ (k=10 over 79, CP [0.062, 0.220]).
- 평균 정확도 $0.66 \to 0.51$, 최고 모델 $0.91 \to 0.77$.

과목은 동일한데 형식만 바꿨을 뿐이다. Co-failure는 과목이 아니라 open-endedness 자체를 추적한다. 객관식의 넓은 guess-floor는 joint failure를 희소하게 만들고(MMLU-Pro에서 124개 중 1개), open-ended 형식은 세 개의 구조적으로 분리된 도메인(수학 두 계열 + 실행 채점 코드 + 자유서술 GPQA) 모두에서 populated $\beta$를 만든다. 이 발견은 LLM-judge 태스크에서도 재현되므로 프로그램적 검증 태스크의 아티팩트가 아니다.

## 라우터·다수결·캐스케이드 실증

### Pillar A — 학습된 라우터가 오라클 이득의 \~0%를 잡는다

15-모델 saturated mix에서 held-out TF-IDF+domain logistic 라우터는 정확도 0.906 (vs single-best 0.901) — 오라클 이득 $G$의 9%(95% CI $[-0.67, 0.50]$). 강한 라우터도 결과가 같다. Gradient-boosted per-model correctness predictor는 $-0.09$를, direct multiclass는 $-1.27$(오히려 해)를, GPT-5-mini에게 각 모델 강점 캡슐과 함께 라우팅을 시키는 LLM-as-router는 100% 질의를 single-best로 라우팅해 정확히 0을 잡는다. 프롬프트 자체에 *누가 이 문제에서 옳을 것인가* 신호가 거의 없다 — 라우터가 약해서가 아니라 신호가 없어서 이득이 못 잡힌다.

### Pillar B — 순진한 다양성은 부채, 매칭된 품질에서만 낮은 $\rho$가 이긴다

15개 모델의 모든 $\binom{15}{3} = 455$ 3-모델 triplet에서 unweighted majority vote의 이득은 평균 $-0.10$(hard), $-0.02$(saturated)로 대체로 음수다. 이질적 품질 풀에서는 다양한-약한 회원들이 강한 회원을 밀어낸다.

반면 정확도를 매칭한 6-모델 band(멤버 정확도 0.74–0.865)에서는 낮은 inter-model $\rho = 0.42$가 Self-MoA($\rho = 0.80$)를 이긴다. 60번의 partition 리샘플 전부에서 양의 이득 +0.010에서 +0.050, 평균 +0.027. 방향은 견고하지만 크기는 partition에 민감하다. 결론: 레버는 <em>숫자</em>가 아니라 <em>매칭된 품질 위의 실패 이질성</em>이다.

### Pillar C — 캐스케이드 이득은 verifier AUC와 함께 붕괴한다

GPT-5-nano($a_L = 0.748$) $\to$ Opus 4.8($a_H = 0.921$) 캐스케이드에서 self-consistency verifier의 AUC를 0.899에서 0.510으로 노이즈 주입해 떨어뜨리면, random mixing 대비 이점이 $0.121 \to 0.012$로 단조 붕괴한다 (20 seed, std $\leq 0.005$). Volume ceiling은 $1 - a_L/a_H = 0.188$. 5-fold held-out에서도 +0.114 이득이 유지되어 in-sample 아티팩트는 아니지만, 캐스케이드 가치는 근본적으로 verifier의 AUC lift 적분과 같다.

## 실무 함의

Chen은 논의에서 세 결과가 별개 vignette이 아니라 하나의 자원 할당 문제를 두 시간 축에서 본 것이라고 정리한다. 하나의 릴리스 에폭 내에서는 가격과 풀이 고정이고 buyer는 shadow price $\lambda_B$가 하나인 예산 할당을 풀며, 에폭을 가로지르는 시점에서는 다음 풀에 대한 옵션을 쥔다. 프론티어가 수렴하고 오차가 상관될수록 세 값(routing, fusion, cascade)이 모두 축소된다 — 라우팅 레이어의 가치는 최고 모델의 절대 능력이 아니라 시장 churn과 이질성을 추적한다.

2026년 프론티어에서 시그니처는 이미 보인다 — 오라클 이득은 작고, 순진한 fusion은 오늘의 최고 모델들이 서로 동의해서 순손실이며, 그럼에도 회원 품질이 매칭되고 오차 상관이 낮으면 유의미한 이득이 남는다. 레버는 실패 모드의 다양성이지 개수나 능력 정점이 아니다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 형식 통제 실험이다. 같은 GPQA 문항을 객관식에서 자유서술로 바꾸기만 해도 $\beta$가 사실상 0에서 0.127로 열린다는 것 — 즉 오케스트레이션의 여지 자체가 답변 형식에 의해 부여되고 회수된다. 벤치마크가 객관식이라서 안 열리는 tail을 프로덕션은 자유서술로 매일 여는 셈이다. 벤치마크에서 관찰한 낮은 $\beta$를 근거로 오케스트레이션 시장을 낙관하는 리포트는, 프로덕션 형식이 국면을 바꾼다는 사실을 반영하지 못한 채 잘못된 조언을 내놓게 된다.

그리고 pairwise $\rho$가 $\beta$를 원리적으로 볼 수 없다는 Proposition 3의 논지 — Fréchet class는 양의 차원이라 저차 marginal로 결합을 결정할 수 없다는, 통계학의 오래된 사실이다. Chen은 이 사실을 새롭게 발견한 것이 아니라 *LLM 오케스트레이션 판정에 옮겼을* 뿐이다. 그런데 그 옮김이 실무의 판정 방식을 통째로 뒤집는다. 지표를 선택하는 순간 이미 무엇을 볼 수 있는지가 결정된다는 것 — 이건 이 논문 밖에서도 반복해서 쓰는 렌즈가 될 것 같다.

## 출처

- 저자: Josef Chen (KAIKAKU, josef@kaikaku.ai) 단독 저자
- 발행: arXiv 2606.27288v1, 2026-06-25
- 원문: <https://arxiv.org/abs/2606.27288>
- HTML: <https://arxiv.org/html/2606.27288v1>
