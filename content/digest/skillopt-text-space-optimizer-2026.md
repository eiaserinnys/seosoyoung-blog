---
title: "SkillOpt: Executive Strategy for Self-Evolving Skills of Frozen LLM Agents"
date: 2026-05-27T00:00:00+09:00
tags: ["AI", "LLM", "AI 에이전트", "프롬프트 엔지니어링", "논문 리뷰"]
categories: ["다이제스트"]
summary: "Microsoft가 공개한 SkillOpt는 모델 가중치를 동결한 채 자연어 기술 문서(skill.md) 한 장을 딥러닝 옵티마이저처럼 반복 학습하여 LLM 에이전트의 성능을 끌어올리는 텍스트 공간 최적화 프레임워크다. 6개 벤치마크에서 52/52 best-or-tied-best를 기록했다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/skillopt-text-space-optimizer-2026/teaser.png"
images:
  - "/images/skillopt-text-space-optimizer-2026/teaser.png"
---

## 3줄 요약

1. SkillOpt는 Microsoft가 2026년 5월 공개한 **텍스트 공간 최적화 프레임워크**다. 모델 가중치는 그대로 두고, 자연어로 쓴 `skill.md` 한 장을 반복 학습하여 LLM 에이전트의 능력을 키운다.
2. 4단계 학습 루프(Rollout → Reflect → Edit Selection → Validation Gate)에 학습률 스케줄·모멘텀·메타학습·조기 종료까지 모두 텍스트 공간으로 옮겨, 딥러닝 훈련 루프를 거의 그대로 재현한다.
3. 6개 벤치마크 × 7개 모델 × 3개 실행 환경의 모든 조합에서 **52/52 best-or-tied-best**를 기록했고, 학습된 스킬은 다른 모델·환경·벤치마크로 재학습 없이 전이된다. 추론 시 추가 비용은 0이다.

## 프로젝트 정체

SkillOpt는 *동결된*(frozen) LLM 에이전트를 위한 **자연어 기술 문서 옵티마이저**다. 공식 소개는 다음과 같다.

> A text-space optimizer that trains reusable natural-language skills for frozen LLM agents through trajectory-driven edits, validation-gated updates, and deployable `best_skill.md` artifacts.

핵심 아이디어는 *단일 마크다운 문서를 모델 파라미터처럼 취급한다*는 것이다. 학습이 끝나면 옵티마이저는 사라지고, `best_skill.md` 한 장만 배포 아티팩트로 남는다. 추론 시점에는 별도의 모델 호출이 일어나지 않아 **inference 비용이 정확히 0**이다.

![SkillOpt 핵심 루프](/images/skillopt-text-space-optimizer-2026/teaser.png "SkillOpt 핵심 루프 — 궤적 기반 편집 → 검증 게이트 → best_skill.md")

기존 접근(수작업 스킬, one-shot LLM 작성, Trace2Skill, TextGrad, GEPA, EvoSkill)은 딥러닝 옵티마이저처럼 *재현 가능하게 수렴하지* 않았다는 것이 저자들의 진단이다. SkillOpt는 이 문제를 체계적·제어 가능한 형태로 해결한 첫 시도라고 주장한다.

## 발신 주체

- **저자(15인):** Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo
- **소속:** Microsoft
- **공개 시점:** arXiv 2026-05-22(v1), 2026-05-25(v2). GitHub 리포는 2026-05-08 생성, 2026-05-27 기준 Stars 562·Forks 49.
- **라이선스:** MIT
- **동반 프로젝트:** [SkillLens](https://microsoft.github.io/SkillLens/)

## 방법론 — 딥러닝 훈련 루프의 텍스트 공간 재현

학습 목표는 다음과 같이 정의된다.

$$s^*_{\text{sel}} = \arg\max_{s \in \mathcal{C}(D_{\text{tr}})} \sum_{x \in D_{\text{sel}}} r(s)$$

여기서 $\mathcal{C}(D_{\text{tr}})$는 훈련 분할에서 생성된 후보 스킬 집합, $D_{\text{sel}}$은 검증 분할, $r(s) \in [0, 1]$은 태스크 보상이다.

### 스텝 단위: 4단계 루프

![SkillOpt 파이프라인](/images/skillopt-text-space-optimizer-2026/pipeline.png "스텝 단위 4단계 + 에폭 단위 메커니즘 전체 파이프라인")

| 단계 | 딥러닝 대응 | 내용 |
|---|---|---|
| **Rollout** | Forward Pass | 동결된 대상 모델이 현재 스킬을 사용해 훈련 배치를 실행하고 궤적(trajectory)을 수집한다. |
| **Reflect** | Backward Pass | 옵티마이저 모델이 성공·실패 궤적을 분석하여 add / delete / replace 편집 패치를 제안한다. |
| **Edit Selection** | Gradient Clipping | 텍스트 학습률 $L_t$개의 상위 편집만 선택한다. 기본 스케줄은 코사인 감소다. |
| **Validation Gate** | Early Stopping | 후보 스킬을 검증 분할에서 평가하고, 엄격한 개선이 있을 때만 수락한다. 거부된 편집은 별도 버퍼에 보존된다. |

### 에폭 단위 메커니즘

- **Slow Update (Momentum):** 에폭 경계에서 이전 스킬과 현재 스킬로 동일 태스크를 다시 풀어 비교한다. 이 비교로 *보호된 종단 지침*이 생성되며, 스텝 수준의 편집이 이 지침을 덮어쓸 수 없다.
- **Meta Skill (Meta-Learning):** 에폭 간 옵티마이저 전략 메모리. 배포 아티팩트(`best_skill.md`)에는 포함되지 않고, 학습 루프 내부에서만 쓰인다.
- **Rejected-Edit Buffer:** 거부된 편집 패턴을 같은 에폭의 이후 반성(reflect) 단계에서 참조해 같은 실수를 반복하지 않도록 한다.

지원하는 학습률 스케줄은 상수(constant), 선형(linear), 코사인(cosine), 자율(autonomous) 네 가지다.

## 실험 결과

### 벤치마크 6종

| 벤치마크 | 유형 |
|---|---|
| SearchQA | 문서 기반 QA |
| ALFWorld | 체화(embodied) 에이전트 |
| DocVQA | 문서 시각 QA |
| LiveMathematicianBench | 수학 |
| SpreadsheetBench | 코드 생성 |
| OfficeQA | 도구 증강 QA |

비교 베이스라인은 수작업 스킬, one-shot LLM, Trace2Skill, TextGrad, GEPA, EvoSkill이다.

### GPT-5.5 Direct Chat — 스킬 없음 대비 개선

| 벤치마크 | No-Skill | SkillOpt | 개선 |
|---|---:|---:|---:|
| SearchQA | 77.7 | 87.3 | **+9.6** |
| SpreadsheetBench | 41.8 | 80.7 | **+38.9** |
| OfficeQA | 33.1 | 72.1 | **+39.0** |
| DocVQA | 78.8 | 91.2 | **+12.4** |
| LiveMathematicianBench | 37.6 | 66.9 | **+29.3** |
| ALFWorld | 83.6 | 95.5 | **+11.9** |
| **평균** |  |  | **+23.5** |

셀별 최강 베이스라인과 비교해도 평균 **+5.4포인트** 우위다.

### 3가지 실행 환경

| 환경 | 평균 개선 (vs 스킬 없음) | 비고 |
|---|---:|---|
| Direct Chat | +23.5 | |
| Codex agentic loop | +24.8 | EvoSkill 대비 +14.0 |
| Claude Code | +19.1 | EvoSkill 대비 +3.2 |

### 에폭별 성능 트렌드

![에폭별 성능 트렌드](/images/skillopt-text-space-optimizer-2026/epoch-trends.png "SpreadsheetBench·SearchQA·LiveMathematicianBench의 에폭 진행에 따른 성능 곡선")

### 전이 학습

- **크로스 모델 (SpreadsheetBench 스킬):** GPT-5.4 → GPT-5.4-mini **+9.4**, GPT-5.4-nano **+3.0**.
- **크로스 환경:** Codex에서 학습한 스킬을 Claude Code로 옮겼을 때 **+59.7**(22.1 → 81.8).
- **크로스 벤치마크:** OlympiadBench 스킬 → Omni-MATH 전이에서 GPT-5.4 +3.7, mini +1.8, nano +1.3.

### 어블레이션 주요 수치

- 학습률(LR) 제거 시 3개 벤치마크에서 87.1 / 77.5 / 61.3 → 84.6 / 75.7 / 57.3 으로 저하.
- Slow / meta update 제거 시 SpreadsheetBench에서 **-22.5포인트**.
- Rejected-edit buffer 제거 시 -1.6\~-4.6포인트.

### 비용·문서 크기

- 최종 스킬 문서 규모: **379\~1,995 토큰** (중앙값 약 920 토큰).
- 학습 비용: 테스트 포인트당 **0.6M\~46.4M 토큰**.

## 리포 구조와 사용법

```text
SkillOpt/
├── skillopt/
│   ├── engine/trainer.py      # 훈련 루프 메인
│   ├── optimizer/             # LR·스케줄러·슬로우/메타 업데이트·rewrite
│   ├── gradient/              # Reflect (역전파 대응)
│   ├── evaluation/gate.py     # 검증 게이트
│   ├── envs/                  # alfworld, docvqa, searchqa, spreadsheetbench, ...
│   ├── model/                 # azure_openai, claude, codex, qwen
│   └── prompts/               # 옵티마이저·반성 프롬프트 .md 모음
├── scripts/train.py           # 훈련 진입점
├── scripts/eval_only.py       # 평가 전용 진입점
├── configs/                   # 벤치마크별 YAML 설정
├── skillopt_webui/app.py      # Gradio 모니터링 대시보드
└── docs/guide/                # dl-analogy.md, training-loop.md 등
```

지원 백엔드는 Azure OpenAI, OpenAI, Anthropic Claude, Qwen(로컬 vLLM)이다.

설치와 최소 학습 명령:

```bash
git clone https://github.com/microsoft/SkillOpt.git
pip install -e .

python scripts/train.py \
  --config configs/searchqa/default.yaml \
  --split_dir /path/to/split \
  --optimizer_model gpt-5.5 \
  --target_model gpt-5.5
```

출력물은 `outputs/<run>/best_skill.md`(배포 아티팩트), `history.json`, 그리고 `skills/skill_vXXXX.md` 스냅샷 체인이다.

## 가장 흥미로운 지점

가장 인상 깊은 발견은 **편집 경제성**이다. 벤치마크 전반에서 단 1\~4회의 수락된 편집만으로 최대 +39포인트 개선이 나왔고, LiveMathematicianBench의 +29.3포인트는 단 한 번의 편집에서 비롯되었다. 잘 쓰인 자연어 한 단락이 가중치 미세조정의 상당 부분을 대체할 수 있다는 신호로 읽힌다.

크로스 환경 전이의 비대칭도 흥미롭다. Codex에서 학습한 스킬을 Claude Code로 옮길 때 **+59.7포인트**라는 큰 도약이 나타났는데, 정작 Claude Code 환경 자체에서의 SkillOpt 개선 폭(+19.1)은 Direct Chat(+23.5)보다 작다. 실행 환경 간 스킬 호환성이 균일하지 않다는 뜻이며, "어떤 환경에서 학습한 스킬을 어디로 옮길 것인가"라는 *스킬 분업 설계* 문제가 새로 열린다.

Slow update가 가중치 공간의 모멘텀을 그대로 모사한다는 점도 깔끔하다. 이전·현재 스킬을 동일 태스크에 적용해 비교하는 방식이 단순한데, 이를 제거하면 SpreadsheetBench에서 -22.5포인트가 빠진다. 텍스트 공간에서도 *과거 상태를 명시적으로 보존하고 비교하는* 메커니즘이 그만큼 중요하다는 증거다.

## 출처

- 저자: Yifan Yang 외 14인 (Microsoft)
- 공개: arXiv 2026-05-22(v1) / 2026-05-25(v2)
- 프로젝트 사이트: <https://microsoft.github.io/SkillOpt/>
- 논문: <https://arxiv.org/abs/2605.23904>
- GitHub: <https://github.com/microsoft/SkillOpt>
- 데모 영상: <https://youtu.be/JUBMDTCiM0M>
- 동반 프로젝트(SkillLens): <https://microsoft.github.io/SkillLens/>
