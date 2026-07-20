---
title: "Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers"
date: 2026-07-21T06:00:00+09:00
tags: ["AI", "LLM", "추론", "루프 트랜스포머", "잠재 추론", "논문 리뷰"]
categories: ["다이제스트"]
summary: "Fan·Svete·Lee는 3B 스케일에서 latent CoT와 explicit CoT의 성능 격차를 처음으로 좁혔다. Looped padded Transformer가 K개 latent 블록을 R번 병렬 순회하며 gold CoT 토큰에 직접 cross-entropy를 걸어, GSM8K 정확도는 explicit CoT 1점 이내, thought-phase 지연은 2.5배~6.9배 감소한다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/lotus-looped-transformers-latent-cot/fig1-scaling.png"
images:
  - "/images/lotus-looped-transformers-latent-cot/fig1-scaling.png"
---

## 3줄 요약

1. Microsoft Research의 Ying Fan, ETH Zürich의 Anej Svete, KRAFTON·Ludo Robotics의 Kangwook Lee가 2026년 6월 30일 arXiv에 올린 논문(v2는 7월 13일). 언어 모델의 chain-of-thought(CoT)를 hidden state에서 처리하는 *latent* 추론이 1B 파라미터를 넘어가면 명시적 CoT에 밀리고 격차가 스케일과 함께 벌어지는 문제를, looped(recurrent-depth) Transformer로 좁힐 수 있는지 검증한다.
2. 저자들은 **LOTUS**(Looped Transformers with parallel supervision on latents)라는 간단한 레시피를 제안한다. K개 latent 블록을 R번 병렬 순회하는 looped padded Transformer에, 각 블록의 gold CoT 토큰을 base LM head를 통해 병렬 cross-entropy로 지도하는 방식이다. 파라미터를 늘리는 대신 계산 깊이만 늘리고, 지도는 explicit CoT와 동일한 정확도로 그라운딩된다.
3. Llama-3.2-3B-Instruct 백본에서 LOTUS는 GSM8K 인도메인 격차를 명시적 CoT의 1점 이내로 좁히고 out-of-domain 평균에서는 오히려 앞선다. thought-phase 지연은 수식 CoT에서 $2.5\times$, 자연어 CoT에서 $6.9\times$ 감소한다. 게다가 post-loop latent를 그대로 base LM head에 통과시키면 gold 추론 단계가 복원되고, 훈련 데이터에 없는 유효한 대안 단계까지 상위 확률로 떠오른다.

![Figure 1 — LOTUS bridges the latent-explicit CoT accuracy gap across scale](/images/lotus-looped-transformers-latent-cot/fig1-scaling.png)

*Figure 1. GSM8K 테스트에서 LOTUS(빨강)는 백본이 커져도 명시적 CoT(회색)의 상한을 따라간다. 반면 기존 latent 방법(Coconut·CODI·SIM-CoT·KaVa)은 백본이 커질수록 더 벌어진다. 3B에서 thought-phase 지연은 수식 CoT $2.5\times$, 자연어 CoT $6.9\times$ 감소.*

## Latent CoT의 두 가지 병목

논문은 기존 latent 추론 방법이 스케일에서 무너지는 이유를 두 가지로 정리한다.

**P1. 순차 생성이 여전히 남아 있다.** Coconut·CODI·SIM-CoT는 latent thought를 autoregressive하게 만든다. 그러니까 latent 토큰 수만큼 forward pass가 순차적으로 늘어난다. 명시적 CoT의 대안이라기보다는 명시적 CoT의 병목을 그대로 안은 채 중간 표현만 숨긴 형태다.

**P2. CoT 그라운딩이 부재하다.** 명시적 CoT는 각 추론 단계가 gold 토큰과 위치 정렬된다. 이 정도로 직접적인 target 없이 latent를 그저 hidden state distillation이나 teacher key-value cache 압축으로 지도하면, latent trace가 의미 있는 계산에서 이탈해 대규모 학습이 불안정해진다.

두 문제를 동시에 해결하려면, latent를 **몇 번의 병렬 순회로 다듬으면서** 그 결과를 **명시적 CoT만큼 직접적인 target에 그라운딩해야** 한다. Looped(=recurrent-depth) Transformer는 가중치를 재사용해 계산 깊이를 늘리므로 P1에 잘 맞는다. Merrill·Sabharwal은 looped padded Transformer가 그래프 도달성 문제를 CoT 대비 로그 시간(지수적 향상)으로 풀 수 있음을 보였다. 문제는 여기에 어떤 지도를 붙일지다.

## LOTUS의 레시피

LOTUS는 두 재료로 구성된다.

1. **Padded latent prefix** — 질문 $Q$ 뒤에 K개의 학습 가능한 latent 블록(블록당 c개 토큰)을 붙이고, 그 앞뒤를 `<BoT>`·`<EoT>` 특수 토큰으로 감싼다. 블록 예산 $K$는 데이터의 최대 단계 수를 덮도록 고정한다. GSM8K는 99%가 6단계 이하라 $K=6$이 자연스럽다.
2. **Looped 계산** — base LM $f_\theta$를 K개 블록 전체에 대해 $R$번 반복 순회하며 hidden state를 점진적으로 다듬는다. 질문 $Q$의 KV 캐시는 한 번만 계산해 재사용한다. 각 반복은 $\mathbf{h}^{(t)} = f_\theta(\mathbf{E} + \mathbf{h}^{(t-1)} \mid \mathcal{C}_{\text{pre}})$ 형태다.

지도는 두 손실로 나뉜다.

$$\mathcal{L}_{\text{step}} = \frac{1}{N_{\text{step}}} \sum_{i=1}^{K} \sum_{j=1}^{c} \mathrm{CE}\!\left(f_{\text{head}}(\mathbf{h}^{(R)}_{i,j}),\ T_{i,j}\right)$$

$$\mathcal{L}_{\text{ans}} = \frac{1}{|A|} \sum_{m=0}^{|A|-1} \mathrm{CE}\!\left(f_{\text{head}}(\mathbf{z}_m),\ A_{m+1}\right)$$

전체 목적함수는 $\mathcal{L} = \mathcal{L}_{\text{ans}} + \lambda_{\text{step}}\, \mathcal{L}_{\text{step}}$.

핵심은 세 가지다.

- **직접적**: 답을 만드는 것과 같은 base LM head $f_{\text{head}}$로 각 블록의 target $T_i$를 채점한다.
- **병렬**: K개 블록 전체를 동시에 지도한다. 즉 CoT 길이가 $N$이라도 $R \ll N$번의 조밀한 병렬 계산으로 처리된다.
- **Post-loop**: 매 반복이 아니라 마지막 반복 $R$의 hidden state에서만 지도한다.

![Figure 2 — LOTUS 아키텍처 (looped forward + final forward)](/images/lotus-looped-transformers-latent-cot/fig2-architecture.png)

*Figure 2. (a) Looped forward: 백본을 R번 반복해 post-loop hidden state를 얻고 이를 LM head로 gold CoT 토큰에 병렬 매칭한다. (b) Final forward: post-loop latent를 그대로 답 위치의 조건으로 넣어 다음 토큰 예측 손실로 답을 지도한다.*

### 왜 위치별 독립 지도가 학습을 무너뜨리지 않는가

저자들은 이 지도를 **parallel chain likelihood(PCL)** 라는 렌즈로 정당화한다. $\mathcal{L}_{\text{step}}$은 개별 위치의 marginal 분포에 대한 cross-entropy이므로, chain을 각 위치의 conditional이 아닌 marginal의 곱으로 인수분해한다. 언뜻 보면 위치 간 의존성을 버리는 것처럼 보이지만, 실제 dependence는 loss가 아니라 **jointly 계산된 latent state**가 담아낸다.

두 손실은 상보적이다.

- $\mathcal{L}_{\text{step}}$은 **support coverage** — 각 위치가 올바른 gold 토큰 위에 확률 질량을 두게 한다.
- $\mathcal{L}_{\text{ans}}$은 **global selection** — 전체 latent configuration을 조건으로 답을 훈련하므로, 실제로 답을 만들 수 있는 jointly 결정된 상태에만 gradient가 기울어진다.

이 상보성은 5.3절 ablation에서 실증된다. 두 손실 중 하나만 있으면 gold CoT NLL이 나빠진다.

### 변종 — LOTUS-aux

기존 방법(SIM-CoT)이 사용한 autoregressive chain likelihood와 비교하기 위해, 저자들은 동일한 looped 백본 위에 auxiliary decoder $g_\phi$를 얹은 LOTUS-aux를 함께 실험한다. Loop 반복 $t$마다 블록 $i=t$의 latent를 aux decoder의 프리픽스로 넣어 gold CoT 단계 $T_t$를 teacher forcing으로 채점하는 구조다. 학습 때만 쓰고 inference에서는 사용하지 않으므로 지연 비용은 동일하다.

![Figure 3 — LOTUS-aux의 auxiliary decoder 지도](/images/lotus-looped-transformers-latent-cot/fig3-aux.png)

*Figure 3. Loop iteration $t$에서 블록 $t$의 latent를 aux decoder $g_\phi$가 $c$-토큰 프리픽스로 받아 gold CoT 단계 $T_t$를 teacher forcing으로 예측한다. Base LM head 지도(Figure 2a) 자리에만 aux decoder가 대신 들어가는 형태다.*

## 결과

### 3B에서 격차가 실제로 좁혀졌다

Llama-3.2-3B-Instruct에서 LOTUS는 GSM8K 인도메인 격차를 명시적 CoT의 약 1.5점 이내로 좁혔고, LOTUS + CODI는 1점 이내로 더 좁혔다. Out-of-domain 평균(GSM-Hard, MultiArith, SVAMP)에서는 오히려 앞섰다. 논문이 논거의 무게를 두는 지점이 여기다.

- 기존 최강 baseline인 CODI + SIM-CoT는 GPT-2 스케일에서 명시적 CoT와 동률($42.6$ vs $42.7$)이지만 3B에서는 $9.2$점 뒤진다.
- KaVa도 같은 방향으로 벌어진다 (GPT-2 $1.9$점 → 3B $5.8$점).
- LOTUS는 스케일이 커져도 격차가 $\sim 1.5$점 안에서 안정된다.

### Thought-phase 지연이 2.5\~6.9배 줄었다

수식 CoT(GSM8K-Aug)에서 3B 백본 기준:

- 명시적 CoT: 328 ms (thought)
- LOTUS: 133 ms — $\mathbf{2.5\times}$ 빠름
- SIM-CoT: 156 ms — LOTUS가 $1.2\times$ 빠름
- CODI: 88 ms — LOTUS보다 빠르나 정확도가 밀림

논문의 latency 측정은 H100 NVL 단일 GPU, 배치 1, greedy decoding. LOTUS는 latent prefix가 150개 위치(K=6, c=25)로 크지만 병렬로 소비되므로 R=6 순차 스텝만 남고, 이것이 지연 절감의 원천이다. Prefix 폭을 6에서 300으로 늘려도 thought 지연은 약 30 ms만 증가한다.

자연어 CoT stress test(GSM8K를 자연어 문장 단계로 확장)에서 격차는 훨씬 크다. 명시적 CoT thought 963.6 ms → LOTUS 140.8 ms로 $\mathbf{6.9\times}$ 감소하고, 정확도는 $68.13$ vs $68.41$로 variance 안에 들어온다. PCCoT($47.6\%$), CODI($55.9\%$), KaVa($60.0\%$) 같은 latent baseline은 이 setting에서 크게 밀린다.

### Ablation — 어느 하나도 뺄 수 없다

- **Looped 백본만** 두고 지도를 지워도 63.3%로 CODI + SIM-CoT(62.3%)를 능가한다. Looped padded 백본 자체가 이미 이득이다.
- **지도를 붙이면** 70.0%로 올라간다. Looped 백본 + parallel gold CoT 지도가 함께 필요하다.
- **블록 폭 $c$**: 1이면 49.7%, 5이면 67.5%, 25~30에서 70.0%로 plateau. 단일 토큰은 direct-readout 지도에 너무 좁다.
- **Loop 깊이 $R$**: $R=2$이면 14.6%, $R=6$이면 70.0%. $R=7$에서는 소폭 하락($69.3\%$). 훈련 시 $R$을 넘어서면 이득이 없다.
- **지도 스케줄**: LOTUS는 post-loop readout(70.0%)이 per-iteration(68.2%)보다 좋다. 반대로 LOTUS-aux는 per-iteration(69.9%)이 post-loop(68.4%)보다 좋다 — aux decoder가 이미 gradient path를 늘리므로 짧은 경로가 유리하다는 해석.

**라우팅의 비대칭성**: LOTUS-aux는 3B에서만 LOTUS와 동등하고 작은 백본에서는 무너진다. 반면 base LM head 직접 지도(LOTUS)는 GPT-2\~3B 모두에서 강건하다. 명시적 CoT와 동일한 head로 지도하는 단순함이 규모에 걸쳐 유리하다는 것이 논문의 관찰이다.

## 가장 흥미로운 지점 — Latent 공간이 실제로 CoT와 정렬된다

LOTUS의 결과 중 내가 가장 눈여겨본 것은 정확도나 지연이 아니라 **latent 공간의 해석 가능성**이다.

Post-loop latent $\mathbf{h}^{(R)}$을 그대로 base LM head에 통과시켜 gold CoT 토큰의 negative log-likelihood를 재면 $3.07$이 나오고, top-1 정확도는 $70.9\%$다. 훈련 시 명시적으로 이 방향으로 지도했으니 그럴 만하다. 놀라운 부분은 다음이다.

- LOTUS-aux는 $\mathbf{h}^{(R)}$을 base LM head로 읽도록 훈련된 적이 없다. 그런데도 top-5에서 $25.8\%$의 확률로 gold 토큰이 잡힌다. Aux decoder를 통해 지도했음에도 latent가 여전히 base LM head 좌표계에서 CoT 방향으로 정렬된다.
- 훈련 데이터에 없는 **유효한 대안 chain**에 대해서도 mass가 크게 붙는다. Ground-truth 답 108에 도달하는 두 가지 다른 중간 경로 중 학습에 안 쓰인 경로의 숫자(24, 18)를, post-loop readout이 top-1 $15.3\%$, top-5 $64.0\%$로 잡아낸다. 무작위 대조 대비 압도적으로 낮은 NLL이다.

이 결과는 latent가 opaque한 embedding이 아니라 **discrete CoT 어휘와 같은 좌표계에 사는 이산 분포**임을 시사한다. Wei et al.이 "Latent thoughts carry strictly more information than discrete tokens"라는 이론적 주장을 편 지점(같은 문제를 CoT 대비 log 스텝으로 풀 수 있다)을, LOTUS는 표현 공간의 실제 관찰로 뒷받침한다. Latent CoT의 promise가 **효율만이 아니라 확장성** — 하나의 latent 상태가 여러 유효한 명시적 CoT를 동시에 지지할 수 있다는 확률 그래프 — 에 있다는 방향을 열어 준다.

또 하나 놓치기 아까운 관찰. $\mathcal{L}_{\text{step}}$만 두면 latent가 gold 토큰에 붙긴 하지만 답을 정합적으로 만들지 못하고, $\mathcal{L}_{\text{ans}}$만 두면 답 근방으로는 가지만 gold 체인에 정렬되지 않는다. 저자들이 "support coverage vs joint selection"이라 부르는 이 분업이 latent CoT 학습의 새로운 문법일 수 있다.

## 한계와 후속

논문 스스로 밝힌 한계 세 가지.

1. **수학 벤치마크에만 검증**했다. Coconut·SIM-CoT의 흐름을 따랐지만, 자연어 이해·다중 홉 질의응답·코드 등 다른 도메인으로 이 레시피가 이관될지는 열린 문제다.
2. **블록 예산 $K$, 폭 $c$, 깊이 $R$이 고정 하이퍼파라미터**다. $K$ 단계를 넘는 chain은 tail을 autoregressive 완성으로 넘긴다.
3. $K$, $c$, $R$을 문제 난이도에 따라 적응적으로 조절하는 방향이 다음 개선 축으로 열려 있다.

## 출처

Ying Fan, Anej Svete, Kangwook Lee. *Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers.* arXiv:2606.31779 (v2, 2026-07-13).

- 원문: <https://arxiv.org/abs/2606.31779>
- 코드: <https://github.com/yingfan-bot/lotus>
- 소속: Microsoft Research, ETH Zürich, KRAFTON, Ludo Robotics
