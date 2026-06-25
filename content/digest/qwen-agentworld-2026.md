---
title: "Qwen-AgentWorld: Language World Models for General Agents"
date: 2026-06-25T19:00:00+09:00
tags: ["AI", "Qwen", "월드 모델", "에이전트", "벤치마크", "RL"]
categories: ["다이제스트"]
summary: "Qwen 팀이 일곱 가지 에이전트 환경(MCP·Search·Terminal·SWE·Web·OS·Android)을 하나의 모델로 시뮬레이션하는 언어 월드 모델 Qwen-AgentWorld를 공개했다. CPT→SFT→RL 3단계로 훈련했고, 397B-A17B 모델이 GPT-5.4·Claude Opus 4.8·Gemini 3.1 Pro를 넘는 AgentWorldBench 성능과 함께 시뮬레이션 RL이 실제 환경 학습을 능가하는 결과를 보였다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/qwen-agentworld-2026/teaser.png"
images:
  - "/images/qwen-agentworld-2026/teaser.png"
---

![Qwen-AgentWorld 마스코트](/images/qwen-agentworld-2026/group_capybaras_flat.png)

## 3줄 요약

1. Qwen 팀이 2026년 6월 22일 공개한 *Qwen-AgentWorld*는 일곱 가지 에이전트 환경을 단일 모델로 시뮬레이션하는 *native* 언어 월드 모델(Language World Model, LWM)이다. 환경 모델링이 사후 파인튜닝이 아니라 *continual pre-training*부터의 핵심 학습 목표다.
2. CPT → SFT → RL의 3단계 파이프라인으로 1천만 개 이상의 실제 환경 상호작용 궤적을 학습했고, 397B-A17B 모델이 AgentWorldBench에서 GPT-5.4·Claude Opus 4.8·Gemini 3.1 Pro를 넘는 종합 점수(58.71)를 기록했다.
3. 시뮬레이션 RL(Sim RL)이 실제 환경에서의 RL을 능가하며, 제어 가능한 시뮬레이션이 실제 환경이 만들 수 없는 방향으로 에이전트 행동을 빚어낸다는 것을 보였다. 35B-A3B 모델과 AgentWorldBench는 Hugging Face와 ModelScope에 오픈소스로 공개됐다.

## 일곱 도메인, 하나의 모델

Qwen-AgentWorld는 일곱 가지 상호작용 환경을 한 모델로 다룬다. GUI 도메인 세 가지(Web·Android·OS)는 픽셀 프레임이 아니라 렌더링 가능한 코드(접근성 트리 XML·HTML·UI 계층 마크업)로 환경 관찰을 표현한다 — 텍스트만 다루는 월드 모델로 시각 환경까지 시뮬레이션하기 위한 설계다.

| 도메인 | LWM이 시뮬레이션하는 것 | 대표 예측 |
|---|---|---|
| **Terminal** (텍스트) | 셸 출력, 파일시스템 상태, 프로세스 동작 | 다단계 명령 파이프라인의 셸 출력 전체 |
| **Search** (텍스트) | 검색 결과: URL, 스니펫, 랭킹, 페이지 본문 | 현실적인 URL 식별자, 자연스러운 출처 랭킹, 질의별 사실 디테일 |
| **MCP** (텍스트) | API 서버 응답: 도구 호출 결과, DB 상태, 서비스 프로토콜 | 9차례 연속 Notion API 호출 간 스키마 일관성 |
| **SWE** (텍스트) | IDE/코드 편집 환경: `git diff`, 테스트 결과, 컴파일 오류 | 코드 변경에 대한 파일 수정과 테스트 결과 |
| **Web** (GUI) | 사용자 상호작용 후 브라우저 DOM 상태 변화 | HTML + 접근성 트리 갱신 |
| **Android** (GUI) | 터치/제스처 후 Android UI 계층 변화 | UI 계층 XML 마크업 |
| **OS** (GUI) | 데스크톱 OS 상태: 파일시스템, 윈도우 관리, 앱 동작 | 접근성 트리 XML 갱신 |

## 3단계 훈련: CPT 주입, SFT 활성화, RL 연마

![훈련 파이프라인](/images/qwen-agentworld-2026/pipeline_overview.png)

세 단계의 역할은 한 줄로 요약된다 — **CPT injects, SFT activates, RL sharpens.**

**Stage 1 — Continual Pre-Training (CPT).** non-thinking 궤적으로 환경 지식을 주입한다. 데이터는 전용 에이전트 인프라(컨테이너 실행 샌드박스, MCP 서버, Android/Web/OS 에뮬레이터)와 공개 환경 상호작용 트레이스, 자체 에이전틱 궤적에서 끌어왔다. 환경 데이터 외에도 산업제어·사이버보안·법·의료·금융·시사 등 특정 도메인의 월드 지식 코퍼스를 추가했다. 핵심 기여는 *turn-level information-theoretic loss masking* — 각 (action, observation) 쌍마다 네 가지 표면 통계로 진짜 환경 정보를 담은 턴을 식별하고, 나머지는 컨텍스트로는 남기되 손실에서는 가린다.

**Stage 2 — Supervised Fine-Tuning (SFT).** `<think>...</think>` 블록을 통해 다음 상태 예측을 명시적 사고 패턴으로 활성화한다. 거절 샘플링으로 고품질 사고 궤적을 7,094개 선별했다.

**Stage 3 — Reinforcement Learning (RL).** GSPO를 사용해 출력 품질을 다듬는다. 보상은 다차원 품질을 평가하는 루브릭 기반 LLM 저지와 프로그램적으로 정답 확인이 가능한 도메인에서의 규칙 기반 검증을 결합한 *하이브리드 리워드*다.

## AgentWorldBench

![AgentWorldBench 개요](/images/qwen-agentworld-2026/bench_overview.png)

언어 월드 모델을 평가하기 위해 만든 새 벤치마크다. Tool Decathlon, Terminal-Bench 1.0·2.0, OSWorld-Verified 등 9개 기성 벤치마크에서 다섯 프런티어 모델의 궤적으로부터 구축했다. **모든 평가 샘플은 실제 환경 실행으로 얻은 ground-truth observation과 짝지어져 있어** 참조 기반 채점이 가능하다. 평가 차원은 다섯 가지 — format, factuality, consistency, realism, quality.

### 성능

![AgentWorldBench 결과](/images/qwen-agentworld-2026/bench_results_bar.png)

Qwen-AgentWorld-397B-A17B가 평균 58.71로 가장 높은 점수를 기록하며 GPT-5.4(58.25)와 다른 프런티어 모델을 모두 앞섰다. 격차가 가장 뚜렷한 도메인은 **Terminal과 SWE** — 코드 실행 상태와 도구 API 동작을 정확히 모델링해야 하는 두 영역이다.

35B-A3B 스케일에서는 3단계 파이프라인이 평균을 47.73 → 56.39로 +8.66점 끌어올려, Qwen-AgentWorld-35B-A3B가 Claude Sonnet 4.6(56.04)을 넘어섰다. 텍스트와 GUI 도메인 양쪽에서 일관된 향상이다.

## 월드 모델의 사고 패턴

![추론 패턴](/images/qwen-agentworld-2026/lwm_reasoning_patterns.png)

129개 사고 궤적을 분석해 네 텍스트 도메인에서 세 가지 *emergent reasoning pattern*을 발견했다.

**1. Deliberative self-correction (숙고적 자기교정).** 모델은 "Wait!"을 인지 인터럽트로 사용해 중간 예측을 수정한다. 129 턴에서 이런 인터럽트가 **1,347회**, 턴당 평균 10.4회 등장했다. 사실 오류, 인식론적 한계(`"I cannot actually execute np.random.seed(42)"`), 관점 전환에 걸쳐 일어났다.

**2. Information leakage prevention (정보 누출 방지).** Search 도메인에서 모델은 에이전트가 찾아내야 할 정답을 알고 있다. 질의가 정답과 무관할 때는, 스니펫이 우연히 정답을 노출하지 않도록 차단한다 — **월드 모델 판 Theory-of-Mind다.**

**3. Multi-step causal reasoning (다단계 인과 추론).** `curl -s localhost:3000 | python3 -m json.tool`의 출력을 예측하려면 여섯 단계 사슬을 거쳐야 한다. Node.js 누락 → 서버 미실행 → 포트 3000 미점유 → curl 무음 실패 → 빈 파이프 → `json.tool`이 `JSONDecodeError` 발생.

## 패러다임 I — 분리형 시뮬레이션 (Sim RL)

월드 모델을 *독립 시뮬레이터*로 두고, 정책 에이전트와 월드 모델을 별개 모델로 운용하는 설정이다. 에이전트가 행동하면 월드 모델이 다음 관찰을 예측하고, 에이전트는 이 시뮬레이션 롤아웃으로 학습한다. 핵심 발견 다섯 가지:

- **제로샷 환경 일반화.** Qwen-AgentWorld는 학습 데이터에 전혀 없던 4,000개 OpenClaw 환경을 시뮬레이션해 Claw-Eval에서 +4.3, QwenClawBench에서 +7.1 향상을 만들었다.
- **제어 가능성이 결정적.** 통제 없는 Sim RL은 효과가 미미하지만, 제어 가능한 시뮬레이션은 MCPMark에서 +12.3, WideSearch에서 +16.3을 끌어냈다.
- **실제 환경 학습을 능가.** 라이브 검색엔진으로 훈련한 Real RL보다 controllable Sim RL이 50.3% vs. 45.6% F1로 앞섰고, 적대적 스니펫 설계로 더 표적화된 에이전트 행동을 빚었다.
- **가상의 세계가 실제로 일반화한다.** 자기일관적이지만 완전히 허구인 세계에서 훈련된 에이전트가 실제 검색 과제로 일반화하며, 구조적으로 *시뮬레이션 사실과 실제 지식의 혼동*을 막는다.
- **상태가 병목.** Sim RL의 효과는 월드 모델에 충분히 자세한 초기 상태를 줘야 살아난다. 그렇지 않으면 시뮬레이션 충실도가 무너지고 다운스트림 이득도 약해진다.

### 일반화 가능한 환경 스케일링

[OpenClaw](https://github.com/openclaw/openclaw)는 스케줄링·코딩·이메일 분류·브라우저 자동화·파일 관리에 걸친 오픈소스 에이전트 플랫폼으로, Qwen-AgentWorld 학습에 포함되지 않는다. 4,000개 OpenClaw 환경을 시뮬레이션해 도메인 적응 없이 에이전트 RL을 돌렸다. 시뮬레이터를 Qwen3.6-Plus로 바꿔보면 향상은 무시할 정도였고, Qwen-AgentWorld-397B-A17B를 시뮬레이터로 쓸 때만 실질적 향상이 나왔다 — **월드 모델 품질 자체가 병목**임을 확인한 ablation이다.

|  | Claw-Eval | QwenClawBench |
| --- | --- | --- |
| Qwen3.5-35B-A3B | 65.4 | 47.9 |
| + Sim RL (Qwen3.6-Plus) | 66.7 | 47.8 |
| + Sim RL (Qwen-AgentWorld-397B-A17B) | 69.7 | 55.0 |
| Δ | +4.3 | +7.1 |

### Controllable Simulation — 자연어로 시뮬레이터를 빚는다

더 강력한 능력은 *제어 가능성*이다 — 자연어 지시로 시뮬레이터의 행동을 학습 중에 빚는다. 두 가지 모드로 검증했다.

**MCP — 환경 적응.** 실제 MCP 도구 사용 궤적에서 시뮬레이션 시스템 프롬프트를 합성했다. 각 프롬프트는 도구 스키마와 서버 설정을 명시하고, 숨은 환경 상태(DB 내용, 권한 설정, 서비스 가용성)를 요약하며, 매 턴 시뮬레이터의 응답을 빚는 *제어 지시*를 정의한다. 제어 지시는 표적화된 교란을 주입한다 — 간헐적 API 오류, 후속 호출을 요구하는 페이지네이션 응답, 다단계 검색을 강요하는 불완전한 중간 결과, 배치 연산의 부분 실패 등. 실제 배포에서는 거의 발생하지 않는 에이전트 약점을 체계적으로 노출시키는 설계다.

결과는 대조가 날카롭다. **제어 지시가 없으면 Sim RL은 의미 있는 향상을 만들지 못한다** — Tool Decathlon은 32.4에서 31.5로 *떨어졌다*. 제어 가능한 시뮬레이션을 켜면 Tool Decathlon이 +3.7, MCPMark가 +12.3 향상된다. 제어 가능성은 향상의 *크기*에 영향을 주는 변수가 아니라, 이 도메인에서 Sim RL이 작동하기 위한 **전제 조건**이다.

|  | Tool Decathlon | MCPMark |
| --- | --- | --- |
| Qwen3.5-35B-A3B-SFT | 32.4 | 21.5 |
| + Sim RL (uncontrolled) | 31.5 | 24.6 |
| + Sim RL (controlled) | 36.1 | 33.8 |
| Δ | +3.7 | +12.3 |

**Search — 허구 세계의 구축.** 1,000개의 자기완결적 허구 환경을 만들었다. 각 환경은 300\~500행의 관계형 DB로 닻을 내려, 내부적으로 일관된 허구 사실로 채워진다. 예: 실제 브랜드명이 등장하지만 존재하지 않는 모델 번호로 채워진 *2029년 스마트폰 시장 랭킹*. 정답이 허구 설정 안에만 존재하므로 에이전트는 파라메트릭 메모리로 검색 도구를 우회할 수 없고, 모든 사실이 지어낸 것이라 시뮬레이션 사실을 실제 지식으로 착각할 수도 없다.

|  | F1 by Item | F1 by Row |
| --- | --- | --- |
| Qwen3.5-35B-A3B-SFT | 34.02 | 13.72 |
| + Sim RL (controlled) | 50.31 | 24.21 |
| Δ | +16.29 | +10.49 |
| Qwen3.5-397B-A17B-SFT | 70.11 | 45.69 |
| + Sim RL (controlled) | 73.98 | 51.74 |
| Δ | +3.87 | +6.05 |

### Sim RL vs Real RL

![Sim RL vs Real RL 학습 곡선](/images/qwen-agentworld-2026/widesearch_rl_comparison.png)

WideSearch에서 controllable Sim RL을 라이브 검색엔진으로 훈련한 Real RL과 직접 비교했다. **Sim RL이 Real RL을 따라가거나 살짝 앞선다** — step 60에서 F1 by Item이 50.3% 대 45.6%.

![툴 사용 비교](/images/qwen-agentworld-2026/widesearch_tool_use_comparison.png)

더 흥미로운 신호는 *에이전트 행동*에서 나온다. 두 학습 방식 모두 `web_search` 호출을 궤적당 \~5회에서 \~3.5회로 줄였다. 그런데 `web_extractor` 호출은 정반대로 갈라졌다 — Sim RL은 2.5회에서 4.0회로 늘리고, Real RL은 2.5회에서 1.5회로 줄였다. 시뮬레이션된 스니펫이 의도적으로 본문 디테일을 감추므로, Sim RL 에이전트는 *완전한 답을 조립하려면 페이지를 통째로 추출해야 한다*는 것을 학습한다. 제어 가능한 시뮬레이션은 실제 환경이 만들 수 없는 방식으로 에이전트 행동을 표적화해 빚는다.

## 패러다임 II — 통합형 에이전트 파운데이션 모델

패러다임 I에서는 에이전트와 월드 모델이 분리돼 있었다. 여기서는 둘을 통합한다 — 행동을 선택하는 모델이 동시에 환경 상태도 예측한다. LWM 훈련이 다음 상태 예측을 내재화된 추론 능력으로 새겨 넣는다는 가설이다. 핵심 발견:

- **급진적 과제 일반화.** 도구 호출이 없는 단일 턴 LWM RL 워밍업이 다섯 도메인 일곱 벤치마크의 멀티턴·도구 호출 에이전틱 과제로 전이된다.
- **도메인 일반화.** LWM 훈련에 전혀 없던 out-of-distribution 도메인에서 향상이 나온다 (Claw-Eval +11.3, QwenClawBench +9.7, BFCL v4 +9.0).
- **메타 추론 패턴.** LWM 훈련은 에이전트에게 *행동 전에 환경 응답을 머릿속으로 시뮬레이션하는* 사고를 가르치고, 이는 과제 형식과 도메인을 가로질러 일반화된다.

Qwen3.5-35B-A3B-SFT 위에 LWM RL을 돌리고 — 도구 호출 없는 단일 턴 과제다 — 추가 파인튜닝 없이 곧장 멀티턴·도구 호출 에이전틱 과제 일곱 개를 평가했다 (그중 셋은 LWM 훈련에 없던 out-of-domain).

|  | In Domain ||| | Out of Domain |||
|---|---|---|---|---|---|---|---|
|  | Terminal-Bench 2.0 | SWE-Bench Verified | SWE-Bench Pro | WideSearch F1 Item | Claw-Eval | QwenClawBench | BFCL v4 |
| Base | 33.3 | 64.5 | 42.2 | 33.4 | 53.6 | 39.8 | 62.3 |
| + LWM RL | 39.6 | 67.9 | 47.4 | 46.2 | 64.9 | 49.4 | 71.3 |
| Δ | +6.3 | +3.4 | +5.2 | +12.8 | +11.3 | +9.7 | +9.0 |

LWM 훈련 파이프라인에 Claw나 function-calling 데이터가 전혀 없는데도 out-of-domain 세 벤치에서 +11.3·+9.7·+9.0 향상이 나왔다는 점이 특히 눈에 띈다.

## 배포와 평가

**오픈소스 공개:** Qwen-AgentWorld-35B-A3B ([Hugging Face](https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B), [ModelScope](https://modelscope.cn/models/Qwen/Qwen-AgentWorld-35B-A3B)). MoE 아키텍처, 총 35B 파라미터/활성 3B, 256K 컨텍스트 윈도.

**AgentWorldBench:** Hugging Face와 ModelScope에 도메인별 JSONL 파일로 공개. 평가는 `eval/eval.py`로 세 단계 — (1) infer, 월드 모델로 예측 관찰 생성 (2) judge, LLM 저지가 다섯 차원으로 채점 (3) aggregate, 도메인별·전체 점수 산출. SGLang·vLLM·독점 엔드포인트를 모두 지원한다.

## 가장 흥미로운 지점

내가 가장 곱씹은 대목은 *허구 세계가 실제로 일반화한다*는 부분이다. 1,000개의 자기일관적이지만 완전히 지어낸 환경(예: 2029년 스마트폰 시장 랭킹)에서 훈련한 에이전트가 실제 검색 과제에서 SFT 베이스라인을 +16점 능가하면서도, 시뮬레이션 사실을 실제 지식으로 착각할 위험은 **구조적으로** 제거된다. 모든 사실이 지어낸 것이기 때문이다.

이는 RL 학습의 데이터 문제에 대한 새로운 관점을 연다. 검색 도구를 우회해 파라메트릭 메모리로 답하는 *지름길 학습*과, 시뮬레이션 환경의 잘못된 사실이 실제 지식을 오염시키는 *지식 오염*은 RL 학습의 두 고질병이다. 허구 세계는 *둘 다*를 한 번에 차단한다. 에이전트는 검색 도구를 써야만 하고, 시뮬레이션에서 얻은 사실은 *명백히 시뮬레이션의 것*이므로 실제 추론에 끼어들 여지가 없다.

또 하나는 *제어 가능성이 효과의 크기가 아니라 작동 조건*이라는 발견이다. 통제 없는 Sim RL은 Tool Decathlon에서 오히려 점수를 떨어뜨렸다(32.4 → 31.5). 시뮬레이터에 충분한 grounding이 없으면 학습 신호가 잡음이 되어 에이전트를 *나쁘게* 만든다. 자연어 제어 지시로 환경 상태와 교란 방식을 시뮬레이터에 알려줘야 비로소 Sim RL이 의미를 갖는다. 이는 *시뮬레이션 RL의 데이터 엔지니어링이 곧 자연어 프롬프트 엔지니어링이 되는* 미래를 시사한다.

## 출처

Qwen Team, "Qwen-AgentWorld: Language World Models for General Agents", Qwen Studio, 2026-06-22.

원문: <https://qwen.ai/blog?id=qwen-agentworld>

논문: <https://arxiv.org/abs/2606.24597>

GitHub: <https://github.com/QwenLM/Qwen-AgentWorld>

Hugging Face 컬렉션: <https://huggingface.co/collections/Qwen/qwen-agentworld>
