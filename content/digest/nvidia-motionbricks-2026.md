---
title: "MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives"
date: 2026-06-15T13:00:00+09:00
tags: ["AI", "논문 리뷰", "모션 생성", "게임 개발", "휴머노이드 로봇"]
categories: ["다이제스트"]
summary: "NVIDIA가 SIGGRAPH 2026 / ACM TOG에 발표한 실시간 모션 생성 프레임워크. 35만+ 모션 클립을 단일 신경 backbone으로 학습해 2ms 지연·15,000 FPS로 생성한다. UE5 게임 캐릭터와 Unitree G1 휴머노이드 로봇이 같은 모델 위에서 움직이는 것이 핵심 시연이다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/nvidia-motionbricks-2026/teaser.jpg"
images:
  - "/images/nvidia-motionbricks-2026/teaser.jpg"
---

## 3줄 요약

1. NVIDIA가 SIGGRAPH 2026 / ACM Transactions on Graphics에 발표한 실시간 모션 생성 프레임워크. 35만+ 모션 클립을 *단일* 신경망 backbone으로 학습한다.
2. Modular latent generative 백본 + smart primitives 인터페이스의 두 축으로, *2ms latency · 15,000 FPS* 라는 산업급 실시간 성능에 도달했다.
3. 같은 모델이 Unreal Engine 5 게임 데모와 Unitree G1 휴머노이드 로봇을 함께 구동한다. 가상 캐릭터 애니메이션과 물리 로봇 제어가 하나의 backbone으로 묶이는 것이 이 논문의 진짜 지점이다.

![MotionBricks 티저 — 단일 backbone이 애니메이션과 로보틱스 양쪽을 통제한다](/images/nvidia-motionbricks-2026/teaser.jpg)

## 자료 개요

- 제목: <em>MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives</em>
- 저자: Tingwu Wang, Olivier Dionne (joint first authors) 외 15인. 대부분 NVIDIA 소속, 일부 ETH Zürich · SFU · UT Austin 겸직.
- 게재: ACM Trans. Graph. Vol. 45, No. 4 (SIGGRAPH 2026), 2026년 7월 게재 예정. arXiv 공개일 2026-04-27.
- 프로젝트 페이지: <https://nvlabs.github.io/motionbricks/>
- arXiv: <https://arxiv.org/abs/2604.24833>
- 코드: <https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/motionbricks> (preview 릴리스, 풀 릴리스는 \~1개월 뒤 예정)

## 왜 지금까지 게임 애니메이션은 신경망으로 갈아치워지지 않았나

논문의 출발점은 자기 비판이다. 생성 모델 연구가 영상·이미지를 휩쓰는 동안, *실시간 인터랙티브 모션 제어는 여전히 전통적 기법이 지배하고 있다*.

전통적 기법의 정점은 *animation graph(애니메이션 그래프)* 다. 사전 녹화된 모션 클립을 상태로, 클립 간 전이를 게임 이벤트와 사용자 입력으로 트리거하는 거대한 상태 머신이다. 논문은 이 한계를 한 줄로 요약한다.

> AAA 타이틀의 모던 애니메이션 상태 머신, 예컨대 어쌔신 크리드에 쓰이는 그래프는 *15,000개 이상의 애니메이션, 5,000개 상태, 12단계 깊이의 중첩 서브그래프*를 관리해야 할 수 있다. 이 정도 규모가 되면 유지·확장이 거의 불가능해진다.

거대 스튜디오만 감당할 수 있는 노동량이 곧 *지금까지의 모션 시스템*이었다는 진단이다. 그렇다면 왜 생성 모델이 이 자리를 차지하지 못했는가. 논문은 두 가지 미해결 도전을 짚는다.

| 도전 | 내용 |
|---|---|
| **Real-time scalability** | 산업 응용은 방대한 모션 스킬을 실시간으로 다뤄야 한다. 그런데 기존 생성 모델은 실시간 연산 제약 아래에서 *품질과 확장성이 동시에 무너진다*. 디퓨전 기반 모션 모델(MDM)들은 한 클립을 만드는 데 수초\~수분이 걸린다. |
| **Integration** | 산업은 속도·헤딩·스타일·정확한 키프레임 같은 *세밀한 멀티모달 제어*를 요구한다. 텍스트 프롬프트 모델이나 태그 모델로는 이 통합이 안 된다. |

이 두 벽이 동시에 무너져야 신경망 모션이 production에 들어올 수 있다 — 이것이 MotionBricks의 문제 정의다.

## Modular Latent Generative Backbone

해법의 첫 절반은 backbone 쪽에 있다. *In-betweening*을 기본 패러다임으로 삼는다. 컨텍스트 키프레임은 캐릭터의 최근 상태, 타깃 키프레임은 smart primitive가 공급하는 목표 — backbone은 그 사이를 채운다.

![MotionBricks 추론 파이프라인의 4단계 (논문 Fig. 2 재현 영상 포스터)](/images/nvidia-motionbricks-2026/overview-demo.jpg)

추론 루프는 4단계로 짜여 있다.

| 단계 | 모듈 | 역할 |
|---|---|---|
| Stage 0 | Smart Primitives | 게임 이벤트·사용자 명령을 키프레임 제약으로 변환 |
| Stage 1 | Root Module | 타이밍과 root trajectory(전체 이동 경로) 예측 |
| Stage 2 | Pose Module | multi-head latent pose token 분포 모델링 |
| Stage 3 | Token Decoder | pose token + root + 키프레임을 연속 모션으로 디코딩 |

핵심 설계 결정은 세 가지다.

**구조적 multi-head tokenizer.** 단일 거대 코드북이나 신체 부위 단위로 수동 분할한 코드북이 아니다. K개의 discrete codebook을 *feature dimension 축에서* 분할하여, 모델이 학습 중에 *데이터 주도적으로* 잠재 분해를 찾도록 했다. 부위별 수동 분할이 한국어 모션 데이터의 실제 다양성을 못 담는다는 판단이다. 부가 효과로 *graceful degradation* — 개별 토큰이 잘못 예측돼도 전체가 무너지지 않는다.

**Root-pose disentanglement.** root(이동 경로)와 pose(자세)는 강하게 상관되지만, *pose intent는 root intent와 분리될 수 있다* — 같은 보행 패턴을 다른 속도로 걸을 수 있는 것과 같은 의미. 그래서 인코더가 둘을 분리해서 처리한다.

**Progressive coarse-to-fine.** root를 먼저 예측해 거친 궤적을 잡고, 그 위에 pose token을 채워 넣는다. 이 순서가 *transparent inspection* 가능한 파이프라인을 만든다 — 중간 단계 결과물을 검사하고 다듬을 수 있다는 의미다.

## Smart Primitives — Animation Graph를 brick으로 바꾼다

해법의 나머지 절반은 *유저 인터페이스* 쪽이다. Smart primitive는 게임 디자이너가 backbone에게 말을 거는 통일된 키프레임 인터페이스다. 사전 정의된 컨트롤 타입이나 태스크별 태그가 필요하지 않다.

논문은 두 종류의 smart primitive를 시연한다.

### Smart Locomotion — 스타일과 믹싱

![Smart Locomotion: 좀비 스타일 보행 (zero-shot 단일 프롬프트로 생성)](/images/nvidia-motionbricks-2026/smart-locomotion-zombie.jpg)

속도·헤딩·스타일 명령으로부터 *재학습이나 태스크별 튜닝 없이* 자연스러운 로코모션을 만든다. 시연된 스타일: Zombie · Injured-Leg · Injured-Torso · Skipping · Strafing · Crouch Strafing. 모두 단일 smart-primitive 프롬프트의 zero-shot 결과다.

블렌드스페이스(blendspace) 믹싱도 같은 인터페이스 안에 들어 있다.

![Smart Locomotion: 여러 블렌드스페이스를 자유롭게 섞는 freestyle 모드](/images/nvidia-motionbricks-2026/smart-locomotion-mixing.jpg)

### Smart Objects — 오브젝트 상호작용

오브젝트 인터랙션은 *proxy keyframe* 집합으로 명시한다. 검을 잡는 손의 위치, 벤치를 넘는 양발의 위치 — 이런 부분 제약만 주면 backbone이 접근·접촉·후속 동작을 자연스럽게 채운다. 같은 명령을 여러 번 실행해도 매번 *자연스러운 변주(variation)* 가 들어간다.

![Smart Object: 검 줍기 — 여러 접근 방향에 따라 생성된 변주들](/images/nvidia-motionbricks-2026/smart-object-pickup-sword.jpg)

![Smart Object: 벤치 점프 — 접근 각도와 속도에 따른 다양한 동작](/images/nvidia-motionbricks-2026/smart-object-jump-bench.jpg)

벤치 점프 영상은 같은 "벤치를 넘어라"라는 명령에 대해 캐릭터의 접근 속도·각도에 따라 도약 폭이 어떻게 달라지는지를 보여준다. 데이터 매칭이 아니라 *생성된* 변주다.

### UE5 안에서의 저작 — brick을 쌓듯이

backbone과 smart primitive를 게임 엔진과 묶는 저작 도구도 함께 공개됐다. Unreal Engine 5 안에서 *애니메이션 그래프 배선 없이, 전문 애니메이션 지식 없이* primitive를 끼워 맞추는 방식이다.

![UE5 인 엔진 저작 — animation graph 배선 없이 brick을 끼워 넣는다](/images/nvidia-motionbricks-2026/ue5-authoring.jpg)

저자들의 표현 그대로다 — "brick을 쌓듯이 plug-and-play".

## 결과 — 2분 40초 컷 없는 UE5 데모

논문이 가장 자랑하는 시연은 2분 40초짜리 컷 없는(uncut) UE5 데모다.

> 모든 모션이 신경망으로 생성됐다. *foot-locking 없음, 블렌딩 없음, 충돌 감지 없음, 수작업 전이 없음*.

![Uncut UE5 demo 포스터 — 2분 40초 분량, 모든 동작이 신경망 생성](/images/nvidia-motionbricks-2026/uncut-demo.jpg)

원본 영상은 NVIDIA Research가 호스팅하고 있다.

<video controls poster="/images/nvidia-motionbricks-2026/uncut-demo.jpg" preload="none" style="width:100%;max-width:960px;display:block;margin:1em auto;">
  <source src="https://research.nvidia.com/labs/gear/motionbricks/videos/aibm_runtime_main_demo_latest_art_v3_1080p.mp4" type="video/mp4">
  영상이 재생되지 않으면 <a href="https://research.nvidia.com/labs/gear/motionbricks/videos/aibm_runtime_main_demo_latest_art_v3_1080p.mp4">원본 영상</a>을 직접 열어 보라.
</video>

수치로 보면 다음과 같다.

| 항목 | 값 |
|---|---|
| 모션 클립 수 | 350,000+ |
| 실시간 처리량 | 15,000 FPS |
| 추론 지연 | 2 ms |
| 단일 모델 적용 범위 | 네비게이션 + 오브젝트 인터랙션 전 영역 |
| 다운스트림 적용 방식 | zero-shot (fine-tuning · 태그 추가 불필요) |

저자들이 "현존하는 어떤 신경망 모델도 이 수준의 *quality · controllability · complexity · completeness* 를 동시에 보여준 적이 없다"고 말하는 데에는 이 컷 없는 데모가 근거다.

## 가상에서 물리로 — Unitree G1 휴머노이드

이 논문에서 가장 흥미로운 한 줄은 마지막에 있다.

> 같은 MotionBricks를 Unitree G1 휴머노이드 로봇에 deploy하여, 가상 캐릭터 애니메이션과 물리 로봇 제어 사이의 간극을 잇는다.

게임 엔진 안의 캐릭터를 움직이는 backbone과, 실세계 휴머노이드 로봇의 전신 제어를 담당하는 backbone이 *같다*. NVIDIA는 이 통합을 자사의 [GR00T Whole-Body Control](https://github.com/NVlabs/GR00T-WholeBodyControl) 스택의 모션 생성 레이어로 굳히려 하고 있다. preview 코드는 이미 공개됐고, 풀 릴리스는 약 한 달 뒤 예정이다.

## 가장 흥미로운 지점

두 가지를 짚어 둔다.

**첫째, 모션 생성의 진짜 게이트는 품질이 아니라 인터페이스다.** 디퓨전 기반 모션 모델은 이미 몇 년 전부터 정밀한 모션을 만들어 왔지만, 게임 산업에는 들어오지 못했다. 이유는 명백하다 — 추론에 수 초가 걸리고, 디자이너가 *디자이너의 언어*로 모델에게 말을 걸 방법이 없었기 때문이다. MotionBricks는 두 벽을 동시에 부순다. 2ms 추론 + smart primitive라는 *키프레임 인터페이스*. 산업 채택을 결정하는 변수는 "AI가 얼마나 잘 만드는가"가 아니라 "AI가 *기존 워크플로우와 얼마나 자연스럽게 결합되는가*"라는 사실이 다시 확인된다.

**둘째, 가상-물리의 경계가 backbone 수준에서 사라진다.** 같은 모델이 게임 캐릭터를 움직이고 휴머노이드 로봇을 움직인다는 사실은 NVIDIA의 사업 포트폴리오 측면에서도, 모션 데이터의 *경제* 측면에서도 중요하다. 35만+ 모션 클립을 학습한 단일 backbone이 만들어 두는 *데이터 해자*는 그래픽스 + 로보틱스 양쪽을 동시에 잠근다. 단일 회사가 양 분야의 모션 데이터를 함께 축적할 수 있을 때 어떤 일이 벌어지는지 — 이 논문은 그 미리보기에 가깝다.

## 출처

발행: NVIDIA, ACM Transactions on Graphics Vol. 45, No. 4 (SIGGRAPH 2026), 게재 예정일 2026년 7월. arXiv 공개일 2026-04-27.
프로젝트 페이지: <https://nvlabs.github.io/motionbricks/>
논문(arXiv): <https://arxiv.org/abs/2604.24833>
코드(preview): <https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/motionbricks>

본 다이제스트의 이미지는 프로젝트 페이지의 영상 포스터·티저를 인용했다. 영상 원본은 NVIDIA Research(`research.nvidia.com/labs/gear/motionbricks/videos/`)에 호스팅된 것을 그대로 참조한다.
