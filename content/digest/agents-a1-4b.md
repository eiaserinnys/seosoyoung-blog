---
title: "Agents-A1-4B"
date: 2026-07-20T08:00:00+09:00
tags: ["AI", "AI 에이전트", "오픈소스", "벤치마크", "스케일링 법칙", "중국"]
categories: ["다이제스트"]
summary: "상하이 AI 연구소 InternAgent 팀이 공개한 롱 호라이즌 에이전트 모델 Agents-A1의 4B dense 버전. '파라미터가 아니라 호라이즌을 키운다'는 기조로, 장기 궤적과 이종 에이전트 능력을 함께 스케일링해 작은 모델로 큰 모델급 성능에 닿는다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. **Agents-A1**은 상하이 인공지능연구소(Shanghai AI Laboratory)의 InternAgent 팀이 `InternScience` 이름으로 공개한 롱 호라이즌(long-horizon) 에이전트 모델이다. 2026년 6월 26일 플래그십 35B-A3B MoE를 오픈소스로 낸 뒤, 7월 14일 약 4B 규모의 dense 버전 **Agents-A1-4B**를 추가했다.
2. 기술 보고서의 제목이 곧 핵심 주장이다 — "파라미터가 아니라 호라이즌을 키운다"(Scaling the Horizon, Not the Parameters). 장기 궤적과 이종(heterogeneous) 에이전트 능력을 함께 스케일링해서, 작은 모델로 훨씬 큰 모델급 성능에 닿는 것을 목표로 한다.
3. 4B 모델은 BrowseComp 66.8, XBench-DS-2510 90.0, GAIA 95.1, IFEval 94.8 등에서 동급 크기 모델을 크게 앞서고, 일부 지표는 35B-A3B MoE 계열에 근접하거나 역전한다.

## 무엇을 공개했나

Agents-A1은 한 개의 모델이 아니라 계열(series)이다. 공개 타임라인은 이렇다.

- **2026.6.26** — 35B-A3B(활성 파라미터 약 3B) MoE 모델과, 일부 도메인의 평가 코드·기술 보고서를 오픈소스로 공개.
- **2026.7.2** — 양자화 변형 계열 공개. `mlx-community`가 여러 규모의 양자화 버전을 제공해 맥에서도 구동 가능.
- **2026.7.14** — 커뮤니티 요청에 따라 약 4B dense 모델 **Agents-A1-4B** 공개. "로컬 AI 비서를 더 빠르고 쉽게 만들 수 있게" 하는 것이 명분이다.

배포 아티팩트는 Hugging Face Transformers 포맷의 가중치·설정 파일이며, Transformers·vLLM·SGLang 등과 호환된다. 컨텍스트 길이는 262K 토큰, 추론 파서는 `qwen3`, 툴콜 파서는 `qwen3_coder`를 쓰도록 안내한다. 즉 Qwen 계열 아키텍처를 기반으로 삼았다.

## 핵심 아이디어 — 파라미터가 아니라 호라이즌

Agents-A1은 에이전트-호라이즌 스케일링을 두 방향에서 본다.

**첫째, 장기 궤적(long-horizon trajectory)의 스케일링.** 도메인에 뿌리내린 "지식-행동 인프라"(domain-grounded knowledge-action infrastructure)의 도움으로 학습한다. 이 인프라는 행동(action)·관측(observation)·검증 결과(verifier outcome)를 함께 구성해서, 에이전트가 문제를 풀어 나가는 *과정 자체*를 학습 가능한 목표(trainable target)로 바꾼다. 결과만이 아니라 중간 궤적을 학습 신호로 삼는 것이 핵심이다.

**둘째, 이종 에이전트 능력의 스케일링.** 롱 호라이즌 탐색(Long-horizon Search), 엔지니어링, 과학 연구, 지시 따르기(Instruction Following), 도구 호출(Tool-calling)처럼 성격이 다른 능력을 한 모델 안에 함께 키운다.

모델 카드가 내세우는 강점은 네 가지다.

- **에이전트적 추론** — 복잡한 과제를 실행 가능한 하위 단계로 분해하고, 미리 계획하며, 중간 결과에 따라 전략을 조정한다.
- **도구 사용** — 함수 호출과 도구 통합을 기본 지원해 API·코드 인터프리터·검색엔진 등 외부 도구와 맞물려 동작한다.
- **과학·전문 추론** — 도구를 결합한 과학적 추론과 전문 지식 질의응답을 다룬다.
- **지시 따르기** — 다중 제약이 걸린 세밀한 지시를 정확히 따른다.

## 3단계 학습 패러다임

이종 능력을 확장 가능하게 키우기 위해 3단계 훈련을 제안한다.

1. **전(全) 도메인 지도 미세조정(full-domain SFT)** — 베이스 모델을 넓은 에이전트 행동에 정렬한다.
2. **도메인별 teacher 모델 학습** — 각 도메인의 전문성을 포착하는 교사 모델을 따로 훈련한다.
3. **multi-teacher multi-domain on-policy distillation** — 여러 교사·여러 도메인에서 나온 지식을 on-policy 증류로 학생 모델에 옮긴다. 이때 이종성을 고려한 최적화(heterogeneity-aware optimization)로 도메인 간 지식 전이 효율을 높인다.

여러 도메인의 전문 교사를 하나의 범용 학생으로 증류하는 구조가, 작은 파라미터로 넓은 능력을 담는 방법론의 뼈대다.

## 성능

InternScience는 약 4B 파라미터의 dense 모델만으로도 롱 호라이즌 탐색, 엔지니어링·연구, 지시 따르기, 범용·과학 에이전트 과제에서 인상적인 성능을 낸다고 밝힌다. 동급 크기 모델을 크게 앞서고, 일부 점수는 Nex-N2-mini나 Qwen3.6 같은 더 큰 MoE 모델에 근접하거나 넘어선다는 것이다. 표에서 🥇는 해당 벤치마크에서 표 안 최고 점수를 뜻한다.

| 벤치마크 | Qwen3.5-4B | Agents-A1-4B | Qwen3.5 | Qwen3.6 | Nex-N2-mini | Agents-A1 |
|---|---|---|---|---|---|---|
| *모델 유형* | Dense 약 4B | **Dense 약 4B** | MoE 35B-A3B | MoE 35B-A3B | MoE 35B-A3B | MoE 35B-A3B |
| **🔍 롱 호라이즌 탐색** | | | | | | |
| BrowseComp | 47.2 | 66.8 | 61.0 | 67.9 | 74.1 | 🥇 75.5 |
| XBench-DS-2510 | 73.0 | 🥇 90.0 | 77.0 | 71.0 | 82.0 | 86.0 |
| Seal0 | 31.5 | 45.8 | 41.4 | 38.7 | 49.6 | 🥇 56.4 |
| GAIA | 58.3 | 95.1 | 59.8 | 78.6 | 82.5 | 🥇 96.0 |
| **⚙️ 엔지니어링·연구** | | | | | | |
| SciCode | 16.1 | 29.6 | 37.7 | 35.8 | 29.9 | 🥇 44.3 |
| MLE-Lite | 7.6 | 22.7 | 24.2 | 34.9 | 34.9 | 🥇 43.9 |
| LiveCodeBench-V6 | 55.8 | 59.6 | 76.2 | 🥇 78.1 | 59.1 | 76.2 |
| FrontierScience-Research | 1.7 | 33.3 | 2.5 | 2.9 | 5.0 | 🥇 40.0 |
| **📋 지시 따르기** | | | | | | |
| IFBench | 59.2 | 69.1 | 70.2 | 64.4 | 54.1 | 🥇 80.6 |
| LongBench-v2 | 50.0 | 52.1 | 59.0 | 57.7 | 59.6 | 🥇 60.2 |
| IFEval | 89.8 | 🥇 94.8 | 91.9 | 91.3 | 88.4 | 🥇 94.8 |
| **🤖 범용·과학 에이전트** | | | | | | |
| τ²-Bench | 79.9 | 78.2 | 🥇 81.2 | 79.0 | 74.5 | 79.8 |
| VitaBench | 22.0 | 🥇 40.3 | 31.9 | 35.6 | 23.0 | 38.8 |
| MatTools | 10.9 | 🥇 49.3 | 21.0 | 15.9 | 34.1 | 47.1 |

공정한 비교를 위해, 다른 모델의 점수는 각자의 원 기술 보고서 수치를 가져오고, 보고되지 않은 항목만 Agents-A1과 같은 평가 프로토콜로 재측정했다고 밝힌다.

## 사용법과 권장 설정

SGLang과 vLLM 양쪽의 서빙 명령을 제공한다. 표준 구성은 GPU 1장, 262K 컨텍스트다. 도구 호출을 켜려면 vLLM은 `--enable-auto-tool-choice --tool-call-parser qwen3_coder`를, SGLang은 `--tool-call-parser qwen3_coder`를 붙인다. 비전 인코더를 건너뛰어 KV 캐시 메모리를 아끼는 `--language-model-only`(text-only) 옵션도 있다.

권장 샘플링 파라미터는 다음과 같다.

- `temperature`: 0.85
- `top_p`: 0.95
- `top_k`: 20
- `min_p`: 0.0
- `presence_penalty`: 1.1
- `repetition_penalty`: 1.0

권장 시스템 프롬프트는 모델을 "Intern-A1, 상하이 인공지능연구소 InternAgent 팀이 개발한 딥 리서치 비서"로 정의한다. 일상 대화·간단한 질문에는 도구 없이 바로 답하고, 최신 정보나 심층 조사·다중 출처 검증이 필요할 때만 `tavily_search` 도구를 쓰라고 지시한다. 처음에는 좁은 질의로 개요를 잡고, 부족하면 더 구체적인 용어로 재질의하며, 충분한 정보를 얻으면 과도한 조사 없이 멈추라는 검색 전략도 담겨 있다.

InternScience는 도구 사용·다단계 추론 등 에이전트 핵심 능력을 재현 가능하게 평가하는 통합 평가 프레임워크도 `Agents-A1/evaluation`에 함께 공개했다.

## 가장 눈여겨본 지점

내가 가장 눈여겨본 것은 **FrontierScience-Research**와 **MatTools** 두 줄이다. 전자에서 4B 모델은 33.3을 받는데, 같은 표의 Qwen3.5-4B는 1.7, 심지어 35B-A3B급인 Qwen3.5·Qwen3.6·Nex-N2-mini도 각각 2.5·2.9·5.0에 그친다. MatTools에서도 4B가 49.3으로, 15.9(Qwen3.6)나 21.0(Qwen3.5) 같은 훨씬 큰 MoE를 크게 앞선다.

이 격차는 파라미터 수로는 설명되지 않는다. 같은 4B라도 도메인 교사에서 증류한 전문성이 실제로 옮겨졌는지, 아니면 그 벤치마크 형식에 특화됐을 뿐인지가 이 모델의 진짜 시험대일 것이다. 한편 LiveCodeBench-V6나 τ²-Bench처럼 큰 모델이 여전히 우위인 항목도 남아 있어, "작은 모델이 호라이즌 스케일링으로 큰 모델을 따라잡는다"는 주장이 모든 도메인에서 균일하지는 않다는 점도 표가 함께 보여 준다.

## 출처

InternScience(상하이 인공지능연구소 InternAgent 팀), 모델 카드 *Agents-A1-4B* (2026.7.14 공개).
기술 보고서: Lei Bai 외, "Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent", arXiv:2606.30616 (2026, cs.CL).

원문: <https://modelscope.ai/models/InternScience/Agents-A1-4B/summary>

(원문 모델 카드에는 인용할 이미지가 없어, 벤치마크 표만 마크다운으로 옮긴 텍스트 다이제스트다.)
