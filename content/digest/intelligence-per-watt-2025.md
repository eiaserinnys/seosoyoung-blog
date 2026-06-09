---
title: "Intelligence per Watt — 로컬 AI의 와트당 지능을 재다 (Saad-Falcon et al., 2025)"
date: 2026-06-09T08:00:00+09:00
tags: ["AI", "LLM", "벤치마크", "논문 리뷰", "로컬 추론"]
categories: ["다이제스트"]
summary: "Stanford 팀이 제안한 IPW(intelligence per watt)는 정확도를 전력으로 나눈 단일 지표다. 20+ 로컬 LM과 8종 가속기에 100만 개 실제 쿼리를 돌려, ≤20B active 로컬 모델이 단일턴 쿼리 88.7%를 답하고 IPW가 2023–2025년 5.3배 개선됐음을 보였다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/intelligence-per-watt-2025/fig1-overview.png"
images:
  - "/images/intelligence-per-watt-2025/fig1-overview.png"
---

## 3줄 요약

1. Stanford·Together AI·SambaNova 등 합동 연구진이 "intelligence per watt(IPW)" — 정확도를 전력으로 나눈 단일 지표 — 를 제안하고, 20+ 로컬 LM과 8종 가속기 위에 약 100만 개 실제 쿼리(WildChat, NaturalReasoning, MMLU Pro, SuperGPQA)를 돌려 측정한다.
2. ≤20B active parameter의 로컬 LM 앙상블이 단일턴 쿼리의 <strong>88.7%</strong>를 답할 수 있으며, IPW는 2023–2025년 사이 **5.3배**(IPJ 기준 18배) 개선됐고, locally-serviceable 쿼리 비중은 23.2%→71.3%로 올라갔다.
3. 다만 로컬 가속기는 같은 모델·같은 bs=1 조건에서 클라우드 가속기 대비 IPW가 1.4배 낮다 — 결론은 "로컬이 클라우드를 따라잡는다"가 아니라, "라우터 정확도 \~80%의 하이브리드 라우팅이 클라우드 단독 대비 에너지 64%·컴퓨트 62%·비용 59%를 절감한다"는 시스템적 처방이다.

![Figure 1 — Intelligence per Watt 전체 개요: IPW 정의, 실험 설정, 로컬 LM 커버리지 시계열, 5.3배 개선의 분해. 출처: Saad-Falcon et al. 2025](/images/intelligence-per-watt-2025/fig1-overview.png)

## IPW — 와트당 지능을 어떻게 잰다는 것인가

논문은 효율을 정확도와 전력 두 축으로 동시에 잡는다. 정의는 단순하다.

$$\text{APW}(m,h) = \frac{\mathbb{E}_q[\text{acc}(m,q)]}{\mathbb{E}_q[P(m,h,q)]}$$

- $\text{acc}(m,q)$ — 모델 $m$의 쿼리 $q$에 대한 정확도(0 또는 1).
- $P(m,h,q)$ — 가속기 $h$ 위에서 추론 중 평균 전력(watts).

쿼리당 총 에너지로 정규화한 변형 $\text{APJ} = \text{acc} / (P \cdot \tau)$도 같이 본다($\tau$는 prefill + decoding 전체 레이턴시). 논문은 두 지표 모두 보고하지만 *main IPW*는 APW다. perplexity 기반 변형(PPW, PPJ)도 부록에 있다.

정확도 측정은 데이터셋에 따라 다르다.

- 정답이 있는 벤치마크(MMLU Pro, SuperGPQA, NaturalReasoning) — exact-match.
- 개방형 chat 쿼리(WildChat) — LLM-as-a-judge(GPT-4o). 로컬 모델이 frontier reference(Qwen3-235B-A22B, 2025년 8월 LMArena SOTA)보다 나쁘지 않으면 $\text{acc} = 1$로 본다. 즉 *frontier 대비 win/tie rate*가 정확도 프록시다.

전력 측정은 가속기 종류별로 도구가 다르다.

- NVIDIA — NVML, accelerator-only scope
- AMD — ROCm SMI, accelerator-only scope
- Apple Silicon — `powermetrics processor_power.actual`, GPU 서브시스템만 (SoC 전체 아님)
- 샘플링 50ms 주기, 쿼리당 10회 반복 평균.

기존 효율 측정 연구들이 100ms–15초 주기를 쓰는 것과 비교하면 분해능이 한 자릿수 높다. 절대 에너지값에는 텔레메트리 도구의 10–15% 오차가 깔려 있어 *상대 비교* 용도로 해석할 것을 저자들이 명시한다.

## 실험 설정 — 무엇을, 어디에, 무엇으로 돌렸는가

**평가 모델**(≤20B active params, 20여 종):

- Qwen3 (4B / 8B / 14B / 32B / 235B-A22B MoE — active ≤22B)
- GPT-OSS (20B / 120B MoE) — OpenAI 오픈소스 모델
- Gemma 3 (1B / 4B / 12B Instruct)
- IBM Granite 4.0 (H-Micro / H-Tiny / H-Small)
- 시계열 분석용 — Mixtral-8x7B-v0.1, Llama-3.1-8B-Instruct

**평가 가속기**(8종 + 스마트폰 1종):

| 카테고리 | 가속기 | 메모리 | 대역폭 | TDP |
|---|---|---|---|---|
| 로컬 워크스테이션 | Apple M4 Max (Mac Studio) | 128 GB unified | 546 GB/s | 480 W (PSU) |
| 로컬 워크스테이션 | NVIDIA Quadro RTX 6000 (Turing) | 24 GB GDDR6 | 672 GB/s | 295 W |
| 로컬 워크스테이션 | NVIDIA RTX 6000 Ada | 48 GB GDDR6 | 960 GB/s | 300 W |
| 모바일 | iPhone 16 Pro (A18 Pro) | 8 GB LPDDR5X | — | \~12 W |
| 클라우드 | NVIDIA A100 40 GB SXM4 | 40 GB HBM2e | 1.6 TB/s | 400 W |
| 클라우드 | NVIDIA H200 SXM | 141 GB HBM3e | 4.8 TB/s | 700 W |
| 클라우드 | NVIDIA GH200 Grace Hopper | 144 GB HBM3e (+624 LPDDR5X) | — | 1000 W |
| 클라우드 | NVIDIA B200 (Blackwell) | 192 GB HBM3e | 8 TB/s | 1000 W |
| 클라우드 | AMD MI300X (CDNA3) | 192 GB HBM3 | 5.3 TB/s | 750 W |
| 클라우드 | SambaNova SN40L | 64 GB HBM2E | 1.6 TB/s | 500 W |

**쿼리 데이터셋**(총 약 100만 건):

- WildChat 500K — 실제 ChatGPT 프롬프트 한 달치, 영어만. 도메인 상위 — Arts/Design/Entertainment 47.1%, Computer/Math 18.1%.
- NaturalReasoning 500K — 수학·물리·화학 등 추론 쿼리 1.2M에서 샘플링. 상위 — Life/Physical/Social Science 36.0%, Computer/Math 34.8%.
- MMLU Pro 12K, SuperGPQA 26.5K.
- 도메인 분류는 Anthropic Economic Index 22개 카테고리(O\*NET 기반)를 GPT-4o-mini로 자동 태깅.

**frontier 비교군**(2025년 10월 기준 cloud SOTA):

- GPT-5 (2025-08-07)
- Gemini 2.5 Pro
- Claude Sonnet 4.5
- WildChat ground truth는 Qwen3-235B-A22B(오픈소스).

## Q1. 로컬 LM이 현재 워크로드를 처리할 수 있는가

저자들은 "단일 로컬 모델"과 "best-of-local 라우팅(여러 로컬 모델 중 최선 응답 선택)" 두 가지로 본다.

- 단일 최고 로컬 모델 GPT-OSS-120B의 평균 커버리지 — **71.4%**.
- 20+ 모델 앙상블 best-of-local 라우팅 — **88.7%** (+17.3pp).

벤치마크별 best-of-local 커버리지는 다음과 같다.

| 데이터셋 | best-of-local 커버리지 |
|---|---|
| WildChat (chat) | 88.9% |
| MMLU Pro | 92.4% |
| SuperGPQA | 77.0% |
| NaturalReasoning | 64.9% (best single LM 기준) |

도메인별로 보면 격차가 크다. GPT-OSS-120B 기준 평균이 가장 높은 영역과 가장 낮은 영역만 추리면 다음과 같다(WildChat/MMLU Pro/SuperGPQA 평균).

| 도메인 | 평균 |
|---|---|
| Computer and mathematical | 85.6% |
| Life, physical, social science | 75.4% |
| Sales and related | 75.1% |
| Business and financial operations | 74.9% |
| Architecture and engineering | 71.6% |
| Arts, design, entertainment, media | 65.5% |
| Healthcare support | 61.8% |
| Personal care and service | 54.8% |

NaturalReasoning에서는 "Architecture & Engineering" 도메인 솔버빌리티가 <strong>40.8%</strong>로 최저다(같은 도메인 WildChat은 97.8%). 즉 *대화체 질문*은 거의 다 풀지만 *해결을 요구하는 추론*에서 끝단이 무너진다는 그림이다.

![Figure 2 — 벤치마크별 개별 모델과 best-of-local/cloud 커버리지 비교. 출처: Saad-Falcon et al. 2025](/images/intelligence-per-watt-2025/fig2-coverage.png)

스케일 단조성도 깔끔하게 보인다 — Qwen3-4B 49.6% → 8B 57.5% → 14B 60.0% → GPT-OSS-120B 71.4%.

![Figure 5 — 22개 경제 카테고리별 로컬 모델 win/tie rate 스택 바. 출처: Saad-Falcon et al. 2025](/images/intelligence-per-watt-2025/fig5-domain-winrate.png)

## Q2. 로컬 추론의 효율은 얼마나 빠르게 좋아지고 있는가

핵심 표는 다음과 같다. 연도별 SOTA 로컬 모델 + SOTA 가속기 쌍 기준.

| 연도 | SOTA 모델 | SOTA 가속기 | Success Rate | IPW (×10⁻³) | YoY 증가 |
|---|---|---|---|---|---|
| 2023 | Mixtral-8x7B-v0.1 | NVIDIA Quadro RTX 6000 | 23.2 ± 1.9% | 0.792 ± 0.032 | — |
| 2024 | Llama-3.1-8B-Instruct | NVIDIA RTX 6000 Ada | 48.7 ± 2.7% | 1.80 ± 0.21 | 2.27× |
| 2025 | GPT-OSS-120B | Apple M4 Max | 71.3 ± 2.2% | 4.18 ± 0.53 | 2.32× |

전체 5.3× IPW 개선의 **기여 분해**:

- per-watt 기준 — 모델 진보 **3.1×** + 하드웨어 진보 **1.7×**.
- per-joule 기준 — 전체 **18.0×** (모델 3.1× + 하드웨어 **5.9×**). 신형 가속기가 전력과 레이턴시를 같이 줄여서 차이가 벌어진다.

모델 쪽 기여 요인은 MoE 아키텍처, 사전훈련 개선, 정렬 기법(RLHF/GRPO), 파라미터 효율화. 하드웨어 쪽은 HBM3e 대역폭(4.8–8 TB/s), 전용 텐서 유닛, 통합 메모리 확장. 2012–2025년 사이 로컬 가속기의 메모리는 126× 늘었다.

![Figure 3 — Intelligence per Joule 18배 개선의 모델·하드웨어 분해(9개 모델 패밀리). 출처: Saad-Falcon et al. 2025](/images/intelligence-per-watt-2025/fig3-ipj-decomposition.png)

더 짧은 시간축에서도 흐름이 또렷하다(Figure 12, 2024-04 → 2025-08 SOTA 로컬 모델 릴리스 기준).

- WildChat win/tie rate — 28.0% → **78.2%** (16개월 만에 2.8×)
- NaturalReasoning accuracy — 48.7% → **80.9%** (+66% 상대 개선)

![Figure 12 — 2024년 4월부터 2025년 8월까지 SOTA 로컬 LM의 WildChat·NaturalReasoning 커버리지 시계열. 출처: Saad-Falcon et al. 2025](/images/intelligence-per-watt-2025/fig12-timeline.png)

같은 모델 같은 조건(bs=1)으로 로컬과 클라우드를 정면 비교한 표는 다음과 같다(Qwen3 패밀리, M4 Max vs. B200).

| 모델 | M4 Max IPW | B200 IPW | B200/M4 |
|---|---|---|---|
| Qwen3-4B | (1.40 ± 0.38)×10⁻³ | (1.95 ± 0.14)×10⁻³ | 1.39× |
| Qwen3-8B | (1.63 ± 0.20)×10⁻³ | (2.27 ± 0.18)×10⁻³ | 1.39× |
| Qwen3-14B | (1.69 ± 0.31)×10⁻³ | (2.35 ± 0.09)×10⁻³ | 1.39× |
| Qwen3-32B | (1.97 ± 0.24)×10⁻³ | (2.75 ± 0.14)×10⁻³ | 1.40× |

per-joule 격차는 더 크다 — B200이 M4 Max 대비 **1.6–2.3×**(예: Qwen3-8B에서 8.71 vs. 3.80 ×10⁻⁵). SambaNova SN40L은 GPT-OSS-120B에서 IPJ 기준 M4 Max의 <strong>6.5–7.4×</strong>까지 벌어진다. 결국 단일 가속기 효율 경쟁에서는 데이터센터 하드웨어가 우위에 있고, 그 격차가 좁혀지고 있을 뿐 사라진 것은 아니다.

다만 스마트폰 NPU(iPhone 16 Pro, A18 Pro)는 12W SoC 기준 per-watt만 보면 워크스테이션 GPU 대비 **\~7×** 높다 — *경량 쿼리 한정*으로 별도 tier가 가능하다는 신호다.

## Q3. 라우팅으로 얻을 수 있는 효율 게인은 얼마인가

여기가 논문의 진짜 결론이다. 단일 가속기 비교에서는 클라우드가 1.4× 효율적이지만, *시스템 레벨*에서는 라우터의 정확도가 들어오는 순간 게임이 바뀐다.

24시간 × 80.2M 쿼리 시뮬레이션에서, 80% 정확도 라우터(RouteLLM 수준의 현실적 목표)는 로컬-클라우드 하이브리드를 운영해 클라우드 단독(bs=16) 대비 다음을 절감한다.

- 에너지 **64.3%**
- 컴퓨트 **61.8%**
- 비용 **59.0%**

![Figure 4 — 24시간 80.2M 쿼리 시뮬레이션에서 라우터 정확도별 에너지·컴퓨트·비용 절감. 출처: Saad-Falcon et al. 2025](/images/intelligence-per-watt-2025/fig4-routing-savings.png)

저자들이 도출한 실무 지침은 짧다.

- **모델 선택** — 메모리 풍부한 로컬 디바이스에서는 MoE가 최고 IPW. FP16→FP4 양자화는 에너지 3–3.5× 절감, 정확도 손실은 단계당 \~2.5pp — *작은 FP16보다 큰 FP4가 우위*.
- **라우터 투자 지점** — 라우터 정확도를 \~80%까지 끌어올리는 데 자원을 쓰고, 그 이상은 *로컬 앙상블 다양성 확대*가 더 효과적. 17.3pp의 best-single↔best-of-local 격차가 그 근거다.
- **도메인 우선순위** — 창작·대화는 이미 >93% 커버. 병목은 *기술 추론*(Architecture & Engineering \~60%)이다. 로컬 모델 R&D는 이쪽에 우선순위.

## 한계와 주의점

저자들이 부록 C에 명시한 한계를 정리하면 다음과 같다.

- 단일턴 쿼리 한정. 멀티턴, agentic workflow, tool use, long-context는 본 연구 제외(GAIA·TerminalBenchV2 확장은 부록 E.12의 소규모 sanity check 수준).
- 멀티모달 미평가 — 텍스트 전용.
- WildChat 정확도가 LLM-as-a-judge(Qwen3-235B)에 의존하므로 judge 모델 편향이 내재.
- 메인 비교는 클라우드 가속기에 보수적인 bs=1 — bs=64 B200은 bs=1 대비 IPJ 11–20× 높다. 즉 *고배치 데이터센터 운용*과의 격차는 훨씬 크다.
- vLLM 단일 런타임 — 절대 IPW가 vLLM/SGLang/llama.cpp 사이에서 3–12% 이동하나 순위는 보존(Kendall's τ ∈ [0.87, 0.93]).
- DRAM/HBM 가격 상승이 로컬 보급 속도를 둔화시킬 수 있음.
- **Jevons 역설** 경고를 저자들이 직접 단다 — 로컬 배포는 에너지를 *소비자 전력망으로 분산*할 뿐 *제거*하지 않는다. 효율 개선이 총 에너지 소비를 늘릴 위험은 정량화되지 않았다.

## 가장 흥미로운 지점

논문이 직접 던지는 역사적 비유 한 줄이 정확히 결론을 압축한다.

> "This transition occurred when efficiency improvements enabled computing to meet user needs within personal device power constraints, not when PCs surpassed mainframes in raw performance."

PC가 메인프레임을 *성능으로* 추월해서 워크스테이션 시대가 온 게 아니라, *개인 기기의 전력 예산 안에서* 요구사항을 충족할 수 있게 된 순간 전환이 일어났다는 관찰이다. 저자들은 로컬 AI도 같은 곡선 위에 있다고 본다 — 단일 가속기 효율로 클라우드를 이기는 것이 아니라, 충분히 좋아진 와트당 지능과 *라우팅*이 만나면 시스템 전체의 에너지·비용 곡선이 꺾인다는 것이다.

다른 한 줄도 같은 결을 다른 면으로 짚는다.

> "The path to efficient AI infrastructure lies not in local accelerators matching cloud efficiency, but in routing systems that leverage the complementary strengths of both paradigms."

직전에 정리한 ["AI 구독은 보조금이었다"](/digest/ai-subscription-subsidy-end/) 다이제스트가 던진 질문 — *토큰 이코노미가 비싸지면 어디로 가는가* — 에 이 논문이 정량적 답을 준다. 한쪽은 가격·자본 사이클의 끝에서 본 위기이고, 다른 한쪽은 그 위기를 흡수할 수 있는 *기술적 헤드룸*의 측정이다. 둘을 같이 두고 읽으면, 라우팅이 산업 차원의 시나리오에서 어느 정도 크기의 완충재가 될 수 있는지 윤곽이 잡힌다.

## 출처

- 저자 — Jon Saad-Falcon, Avanika Narayan, Hakki Orhun Akengin, J. Wes Griffin, Herumb Shandilya, Adrian Gamarra Lafuente, Medhya Goel, Rebecca Joseph, Shlok Natarajan, Etash Kumar Guha, Shang Zhu, Ben Athiwaratkun, John Hennessy, Azalia Mirhoseini, Christopher Ré
- 소속 — Stanford University 외
- 발행 — arXiv, 2025-11-11 (online date 2026-05-21, v4)
- 원문 — <https://arxiv.org/abs/2511.07885>
- PDF — <https://arxiv.org/pdf/2511.07885>
