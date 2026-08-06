---
title: "CoreWeave Trains DeepSeek-V3 Benchmark in Two Minutes"
date: 2026-06-18T06:30:00+09:00
tags: ["AI", "벤치마크", "LLM", "MLPerf", "AI 인프라"]
categories: ["AI 산업"]
summary: "코어위브가 MLPerf Training v6.0에서 8,192개의 NVIDIA Blackwell Ultra GPU로 DeepSeek-V3 671B를 2.02분에 학습 완료하며 역대 최고 기록을 세웠다. 코어위브는 풀스택 소프트웨어 최적화 덕에 GPU를 더 늘리지 않고도 v5.0 대비 2.8배 빠른 결과를 냈다고 주장한다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/coreweave-deepseek-v3-two-minutes/mlperf-hero.jpg"
images:
  - "/images/coreweave-deepseek-v3-two-minutes/mlperf-hero.jpg"
---

## 3줄 요약

1. 코어위브(CoreWeave)는 MLPerf Training v6.0에서 8,192개의 NVIDIA Blackwell Ultra GPU(GB300 NVL72)로 DeepSeek-V3 671B를 **2.02분**에 학습 완료했다. Closed/Available-cloud 부문 1위, 역대 최고 기록.
2. Llama 3.1 405B는 4,096 GPU로 9.77분에 끝냈다. v5.0의 자기 기록 대비 **2.8배 빠르고**, GB200 NVL72 대비 GPU를 **20% 적게** 쓰고도 동등한 성능을 냈다.
3. 코어위브는 이 결과가 하드웨어 증설이 아니라 NVLink 인지 스케줄링, 토폴로지 인지 배치, rail-aware 네트워킹 같은 **풀스택 소프트웨어 최적화** 덕분이라고 주장한다. 벤치마크 전용 클러스터가 아닌, 고객이 매일 쓰는 프로덕션 인프라 위에서 돌렸다는 점을 강조한다.

## MLPerf Training v6.0과 코어위브의 위치

MLPerf Training은 ML Commons 컨소시엄이 주관하는 학습 성능 표준 벤치마크다. v6.0 라운드에서 코어위브는 NVIDIA HGX B200과 GB300 NVL72 두 플랫폼을 64 GPU부터 8,192 GPU까지 다양한 규모로 제출했다.

코어위브가 강조한 핵심 메시지는 두 가지다. 첫째, **벤치마크 전용 사이드 클러스터가 아니라 고객이 매일 사용하는 프로덕션 인프라**에서 측정했다. 둘째, "진짜 AI 성능은 하드웨어 혼자 만드는 게 아니다. GPU 인프라부터 고속 네트워킹, 오케스트레이션, 스토리지, 관찰 가능성, 전문 운영까지 플랫폼의 모든 레이어가 함께 작동할 때 나온다"는 입장이다.

## DeepSeek-V3 671B — 2분 학습

DeepSeek-V3는 MoE(Mixture of Experts) 구조의 대형 모델로, AI 클라우드의 모든 레이어를 동시에 자극하는 워크로드다. dense 행렬 처리량, MoE 라우팅 효율, 통신 프리미티브, 수천 GPU 클러스터의 결함 허용, NVLink·NVL72·scale-out fabric을 가로지르는 토폴로지 인식 샤딩이 한꺼번에 작동한다. 플랫폼에 약점이 있으면 이 워크로드가 찾아낸다.

코어위브는 GB300 NVL72 플랫폼으로 세 가지 규모 제출을 냈다.

| Compute Platform | Nodes | GPUs | Time-to-train | Precision |
|---|---|---|---|---|
| NVIDIA GB300 NVL72 | 2,048 | 8,192 | 2.02 min | MXFP8 |
| NVIDIA GB300 NVL72 | 1,024 | 4,096 | 3.09 min | MXFP8 |
| NVIDIA GB300 NVL72 | 512 | 2,048 | 5.54 min | MXFP8 |

8,192 GPU 클러스터는 Spectrum-X Ethernet 네트워킹으로 연결됐다. 2.02분이라는 wall-clock 시간 자체보다, 이 라운드에서 GB300 NVL72를 **2,048 GPU를 넘는 규모로 스케일한 유일한 제출자**라는 점이 더 중요하다. 2,048 → 4,096 → 8,192로 두 차례 두 배 확장하면서 강한 스케일링 효율을 유지했다.

## Llama 3.1 405B — GB200 대비 GPU 20% 적게

dense 기반 모델 학습에서도 코어위브는 v5.0 자기 기록을 큰 폭으로 갱신했다.

| Compute Platform | Nodes | GPUs | Time-to-train |
|---|---|---|---|
| NVIDIA GB300 NVL72 | 1,024 | 4,096 | 9.77 min |

9.77분은 동일 테스트에서 코어위브가 v5.0에서 낸 결과보다 **2.8배 빠르다**. GPU 수를 늘려서가 아니라 NVLink 도메인 인지 스케줄링(CKS), 토폴로지 인지 워크로드 배치(SUNK), 깊은 네트워킹 최적화 같은 스택 전반의 소프트웨어 개선 덕분이라고 주장한다.

런타임 구성은 NVIDIA NeMo Framework Release 26.04 위에서 full CUDA Graphs를 활용해 CPU 스케줄링 오버헤드를 줄이고 GPU 활용도를 최대화했다. 텐서·파이프라인·컨텍스트 병렬 파라미터는 GB300 NVL72 아키텍처에 맞춰 튜닝했다. 네트워크 레이어에서는 Spectrum-X Ethernet 위의 RoCE가 스케일아웃 패브릭을 제공했다.

핵심 결과 한 줄: 이 GB300 NVL72 구성이 더 큰 GB200 NVL72 구성과 거의 같은 성능을 내면서 **GPU를 20% 적게 썼다**. 코어위브는 이 점을 "raw 컴퓨팅 용량도 중요하지만, 실제 성능과 경제성을 결정하는 것은 시스템 전반 최적화"라는 자사 원칙의 증거로 내세웠다.

## 64 GPU 소규모 클러스터 — 작은 규모에서도 격차

코어위브는 프론티어 규모뿐 아니라 64 GPU 소규모 구성도 제출했다. NVIDIA HGX B200 클러스터를 Quantum-2 InfiniBand로 연결한 셋업이다.

- GPT-OSS-20B → 26.98분
- Llama 3.1 8B → 16.54분 (동일 셋업의 차순위 제출자보다 **9.7% 빠름**)

작은 클러스터에서의 9.7% 격차도 결국 같은 메시지를 향한다. 더 많은 하드웨어에 접근한 게 아니라 오케스트레이션, 통신 라이브러리, 네트워킹, 스케줄링, 분산 학습 구성에서 같은 Blackwell 플랫폼을 더 잘 짜냈다는 것이다.

## 8,192 GPU에서 효율을 유지하는 방법

수백 GPU 클러스터와 8,192 GPU 클러스터는 같은 문제가 아니다. 이 규모에서는 컴퓨트, 네트워킹, 스토리지, 스케줄링, 오케스트레이션이 *하나의 연결된 플랫폼*으로 함께 움직여야 성능이 나온다. 코어위브는 Mission Control, SUNK, CKS 세 가지 컴포넌트가 그 역할을 한다고 설명한다.

### 함대(fleet) 전반의 일관된 성능

8,192 GPU에서는 *몇 퍼센트의 노드*가 표준 이하면 전체 클러스터 효율이 무너진다. 잘못 구성된 NIC 한 장, straggler GPU 하나, 열 이상치 하나가 stall을 만들어 클러스터 전체에 영향을 준다.

CoreWeave Kubernetes Service(CKS)는 대규모 학습을 위한 일관된 AI 서브스트레이트를 제공한다. 스케줄링·배치·운영을 위한 표준화된 오케스트레이션 표면을 만들고, Mission Control이 그 아래의 함대 상태를 계속 검증한다. MLPerf 실행 전 Mission Control이 한 일은 다음과 같다.

- GB300 NVL72 시스템, NIC, 스위치, DPU의 펌웨어 일관성 검증
- GPU 클럭, 전력 한계, 열 프로파일 확인
- 하드웨어 열화나 marginal 링크를 잡 스케줄 전에 식별

실행 중에는 함대 전반의 텔레메트리로 열 핫스팟, 전력 공급 이상, 네트워크 혼잡 패턴, GPU 성능 아웃라이어를 감지한다. DeepSeek-V3 같은 MoE 워크로드는 동기화 지연과 all-to-all 통신이 인프라의 작은 불일치까지 증폭시키기 때문에, 이런 함대 단위 일관성이 특히 중요하다고 한다.

### NVLink 도메인 인지 스케줄링

MoE 워크로드는 통신 지연과 대역폭에 매우 민감하다. 전문가 병렬(expert-parallel) 그룹이 네트워크 경계 너머로 분산되면 all-to-all 통신 오버헤드가 실행 시간을 잡아먹는다.

CKS 위에서 동작하는 SUNK는 토폴로지를 안다. NVLink, rack-scale 디자인, 클러스터 fabric 토폴로지를 이해하고 워크로드를 지역성 최대화 방향으로 배치한다. 대규모 MoE 학습에서는 전문가 병렬 그룹을 같은 NVL72 도메인 안에 우선 배치해 인터-rack 통신을 최소화하고, 가장 빈번한 collective 연산을 가장 짧은 지연 경로 위에 둔다.

### Rail-aware 네트워킹

다중 천 GPU 규모에서는 네트워크가 학습 효율을 결정하는 1차 요인이 된다. DeepSeek-V3 같은 워크로드는 전문가 병렬 그룹 사이의 all-to-all 교환을 학습 내내 만들어낸다.

코어위브는 rail-aware 네트워킹 전략으로 모든 RoCE rail에 트래픽을 균형 있게 분산시켜 fabric 안에서 핫스팟이 생기지 않도록 한다. 대규모 잡 실행 전, rail 균형을 검증하고 NCCL이 GPU를 host channel adapter에 올바르게 매핑하는지 확인해 collective 통신이 가용 네트워크 대역폭을 전부 사용할 수 있게 한다.

## 고객에게 무엇을 의미하는가

코어위브가 이 보고를 마무리하는 방식은 일관되다. 모든 측정은 고객이 매일 쓰는 같은 플랫폼에서 나왔다는 것이다.

- **프론티어 규모 MoE 모델**의 경우, 클러스터가 두 배로 확장돼도 강한 스케일링 효율을 유지할 수 있다. 통신 병목이나 인프라 제약 때문에 수익체감(diminishing returns)을 만나지 않는다.
- **dense 기반 모델**의 경우, 코어위브 Llama 3.1 405B 결과처럼 영리한 인프라 오케스트레이션이 학습 효율을 실질적으로 끌어올린다. GPU 20% 적게 쓰는 게 곧 학습 예산이 멀리 가고, iteration cycle이 짧아진다는 뜻이다.
- **소형 AI 모델**의 경우, 같은 소프트웨어 스택이 그대로 효과를 낸다. 우위는 클러스터 크기가 아니라 플랫폼이 하드웨어를 돌리는 방식에 있다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 같은 주장 — *"system-wide optimization이 real-world performance를 결정한다"* — 가 v5.0과 v6.0 두 라운드의 자기 비교로 뒷받침된다는 점이다.

v5.0 → v6.0에서 Llama 3.1 405B 학습 시간이 2.8배 빨라졌다. 같은 클라우드가 같은 워크로드에 같은 클래스의 칩(GB300이라는 차이는 있지만)을 갖고도 1년 새 이만큼의 폭을 짜낸다는 사실이, "GPU만 많이 사면 된다"는 단순한 인프라 서사를 흔든다.

또 하나 — *GB200 대비 GPU 20% 적게 쓰고 동등 성능*이라는 비교는 NVIDIA가 자기 세대 간 효율 격차를 인정하는 모양새다. 마케팅 포지셔닝이긴 하지만, GPU를 늘리지 못하는 고객(전력 한계, 자본 한계, 공급 한계 어느 쪽이든)에게는 같은 학습 시간을 더 적은 GPU로 달성한다는 게 직접적인 비용 효과다.

다만 이 모든 측정이 *코어위브 자체 제출*이라는 사실은 분명히 한다. MLPerf은 표준 벤치마크지만 결과 해석은 제출자의 마케팅 결을 입는다. 같은 라운드의 다른 제출자(Google, Microsoft, AWS 등)가 같은 워크로드에서 어떤 숫자를 냈는지는 이 자료만으로는 모른다.

## 출처

CoreWeave 공식 블로그, Shadi Saba, 2026-06-16.

원문: <https://www.coreweave.com/blog/coreweave-trains-deepseek-v3-in-two-minutes>

MLPerf Training v6.0 결과 발표.
