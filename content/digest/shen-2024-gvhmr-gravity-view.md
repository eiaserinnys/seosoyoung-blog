---
title: "World-Grounded Human Motion Recovery via Gravity-View Coordinates"
date: 2026-07-01T12:30:00+09:00
tags: ["AI", "논문 리뷰", "3D 자세 추정", "인간 동작 복원", "트랜스포머"]
categories: ["다이제스트"]
summary: "Shen 외(Zhejiang Univ., SIGGRAPH Asia 2024)가 단안 비디오에서 세계 좌표계 기반 인간 동작을 복원하는 방법을 제시한다. 각 프레임마다 중력 방향과 카메라 시선으로 유일하게 정의되는 Gravity-View 좌표계에서 자세를 예측해 자기회귀 오차 누적을 없애고, RoPE 트랜스포머로 45초짜리 1430프레임 시퀀스를 0.28초에 처리한다. RICH·EMDB 벤치마크에서 세계 좌표 W-MPJPE를 WHAM 대비 31% 낮췄다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/shen-2024-gvhmr-gravity-view/teaser.png"
images:
  - "/images/shen-2024-gvhmr-gravity-view/teaser.png"
---

## 3줄 요약

1. Zehong Shen 외(Zhejiang University, HKU, Deep Glint, Shenzhen University, SIGGRAPH Asia 2024)가 단안 비디오에서 세계 좌표계 기반의 인간 동작을 복원하는 방법을 제안한 논문이다. 기존 자기회귀 방식이 시간을 따라 오차를 누적하는 근본 원인을 짚고, 프레임마다 독립적으로 정의되는 새 좌표계로 문제를 재구성한다.
2. 핵심 아이디어는 <em>Gravity-View(GV) 좌표계</em>다. 세계 중력 방향과 카메라 시선 방향으로 각 프레임에서 유일하게 결정되며, 중력 정렬성 덕분에 자세 학습 모호성을 크게 줄인다. GV에서 예측한 자세는 카메라 회전을 곱해 세계 좌표로 옮긴다.
3. 결과는 정확도와 속도 양쪽에서 이전 SOTA WHAM을 능가한다. EMDB-2 세계 좌표 W-MPJPE는 354.8→276.5로 22% 개선되고, RICH의 W-MPJPE는 184.6→126.3로 31% 개선된다. 추론 속도는 1430프레임 시퀀스에 0.28초로 WHAM의 2.0초 대비 14배 빠르다.

## 자료의 정체

- **저자:** Zehong Shen, Huaijin Pi, Yan Xia, Zhi Cen, Sida Peng, Zecen Hu, Hujun Bao, Ruizhen Hu, Xiaowei Zhou
- **소속:** Zhejiang University, The University of Hong Kong, Deep Glint, Shenzhen University
- **발표:** SIGGRAPH Asia 2024 Conference Proceedings
- **arXiv:** [2409.06662](https://arxiv.org/abs/2409.06662)
- **코드:** <https://github.com/zju3dv/GVHMR>
- **프로젝트 페이지:** <https://zju3dv.github.io/gvhmr/>
- **라이선스:** CC-BY-NC-SA 4.0 (비상업적 사용 조건부)
- **분야:** 컴퓨터 비전, 인간 동작 복원(HMR). 단안 비디오 입력에서 SMPL 파라미터와 세계 좌표계 위치를 동시 추정.

![Teaser: GVHMR의 세계 좌표계 인간 동작 복원 결과](/images/shen-2024-gvhmr-gravity-view/teaser.png)

## 세계 좌표계 기반 복원의 모호성 문제

Human Motion Recovery는 두 가지 결로 나뉜다. <em>Camera-Space HMR</em>은 카메라 시점 위에서만 3D 자세를 복원하고, <em>World-Grounded HMR</em>은 실제 물리 공간에서 중력을 고려한 궤적까지 복원한다. 후자가 근본적으로 어렵다. 카메라가 움직이면 세계 좌표계의 정의 자체가 시퀀스마다 달라지기 때문이다.

기존 접근은 크게 두 갈래다. SLAHMR, PACE 같은 SLAM 결합 방식은 최적화가 무겁고 느리다. WHAM은 자기회귀(autoregressive) 방식으로 프레임 간 상대 이동을 예측해 누적한다. 실시간 처리가 가능해졌지만, 상대 예측의 미세한 오차가 시간을 따라 쌓여 긴 시퀀스에서 궤적이 어긋난다.

논문이 던지는 질문은 단순하다. *왜 자세 자체를 절대 좌표계에서 예측할 수 없는가?* 답은 이렇다. 세계 좌표계 정의가 시퀀스마다 다르므로 신경망이 학습할 <em>이미지→자세</em> 매핑이 애초에 유일하지 않기 때문이다. 이 모호성을 해결하려면 각 프레임에서 <em>자동으로 결정되는</em> 좌표계가 필요하다.

## Gravity-View 좌표계

![Gravity-View 좌표계 정의 다이어그램](/images/shen-2024-gvhmr-gravity-view/method-gv-coordinate.png)

Gravity-View 좌표계는 세 축으로 정의된다.

- **Y축**: 중력의 반대 방향 $\vec{y} = -\vec{g}$
- **X축**: $\vec{x} = \vec{y} \times \overrightarrow{view}$ (카메라 시선과 중력 평면의 수직 벡터)
- **Z축**: $\vec{z} = \vec{x} \times \vec{y}$ (우수 좌표계)

카메라 좌표계 $\Gamma_c$에서 GV 좌표계 $\Gamma_{GV}$로의 회전 행렬은 다음과 같다.

$$
\Gamma_{GV} = R_{c2GV} \cdot \Gamma_c = [\vec{x}, \vec{y}, \vec{z}]^T \cdot \Gamma_c
$$

이 좌표계의 매력은 세 가지다. 첫째, 중력 축이 항상 세로로 정렬되어 인간 자세의 학습 편향이 물리 세계와 일치한다. 둘째, 각 프레임마다 카메라 회전만 알면 유일하게 결정되므로 시퀀스 정의의 모호성이 사라진다. 셋째, 프레임별 독립 예측이 가능해 자기회귀 오차 누적이 원천 차단된다.

## 파이프라인

![파이프라인 구조도: 특징 인코딩부터 세계 좌표 변환까지](/images/shen-2024-gvhmr-gravity-view/pipeline.png)

전체 파이프라인은 다섯 단계로 이어진다.

**1. 특징 인코딩.** 입력 비디오에서 네 종류의 특징을 뽑는다.
- 바운딩박스 (YOLOv8)
- 2D 키포인트 (ViTPose)
- 이미지 특징 (고정 ViT 인코더)
- 상대 카메라 회전 (DPVO 또는 IMU 자이로)

각 특징을 개별 MLP로 512차원에 매핑한 뒤 요소별로 더하는 <em>early-fusion</em> 방식을 쓴다.

**2. RoPE 트랜스포머.** 12층, 8헤드, 은닉 512차원 트랜스포머 인코더로 시퀀스를 처리한다. 핵심 설계는 <em>Rotary Positional Embedding</em>이다. 상대 위치 인코딩이라 학습 시퀀스 길이(L=120)를 넘어서도 일반화한다. 추론 시에는 창 밖 토큰에 $-\infty$ 마스킹을 걸어 슬라이딩 윈도우 없이 임의 길이 비디오를 한 번에 처리한다.

**3. 다중 작업 예측.** 트랜스포머 출력에서 여러 MLP 헤드가 병렬로 예측한다.
- 약원근 카메라 파라미터 $c_w$
- SMPL 로컬 포즈 $\theta$, 형상 $\beta$
- GV 좌표계의 인간 방향 $\Gamma_{GV}$
- 루트 속도 $v_{root}$
- 관절 정지 확률 $p_j$ (손, 발가락, 뒤꿈치)

**4. GV → World 변환.** 카메라가 움직이는 경우, GV 좌표계 자체가 프레임마다 회전한다. 프레임 사이 상대 회전 $R_{\Delta GV}^t$를 카메라 회전에서 xz 평면 투영으로 계산하고, 이를 누적해 세계 방향을 복원한다.

$$
\Gamma_w^t = \begin{cases} \Gamma_{GV}^0 & t=0 \\ \prod_{i=1}^t R_{\Delta GV}^i \cdot \Gamma_{GV}^t & t>0 \end{cases}
$$

세계 평행이동은 루트 속도의 시간 적분으로 얻는다.

$$
\tau_w^t = \sum_{i=0}^{t-1} \Gamma_w^i v_{root}^i
$$

**5. 후처리.** 예측된 관절 정지 확률로 발 미끄러짐을 억제한다.

## 학습 설정과 손실함수

학습 데이터는 AMASS(합성), BEDLAM(합성 고품질), H36M(실내 다중 카메라), 3DPW(야생)를 혼합한다. 배치 크기 256, 시퀀스 길이 L=120, 총 500 에포크. RTX 4090 2장에서 13시간이 걸린다.

손실함수는 세 종류로 나뉜다.

- **MSE Loss**: 3D 관절, 정점, 카메라 평행이동, 세계 평행이동, SMPL 파라미터
- **L2 Loss**: 3D 관절과 2D 키포인트 거리
- **BCE Loss**: 관절 정지 확률(손, 발가락, 뒤꿈치)

## 실험 결과

### 세계 좌표 메트릭 (RICH, EMDB-2)

![세계 좌표계 정확도 표: WHAM 대비 대폭 개선](/images/shen-2024-gvhmr-gravity-view/table1-world-metric.png)

| 모델 | RICH WA-MPJPE | RICH W-MPJPE | RICH RTE | EMDB-2 W-MPJPE | 발 미끄럼 |
|---|---|---|---|---|---|
| WHAM (DPVO) | 109.9 | 184.6 | 4.1 | 354.8 | 4.4 |
| **GVHMR (DPVO)** | **78.8** | **126.3** | **2.4** | **276.5** | **3.5** |
| **GVHMR (GT gyro)** | **78.8** | **126.3** | **2.4** | **274.9** | **3.5** |

핵심은 두 가지다. 첫째, WHAM 대비 W-MPJPE가 31%(RICH) 및 22%(EMDB-2) 줄었다. 둘째, DPVO 추정 회전과 GT 자이로 회전의 결과 차이가 거의 없다. 프레임별 독립 예측 방식이라 회전 노이즈에 견고하다는 뜻이다.

### 카메라 공간 메트릭 (3DPW, RICH, EMDB-1)

![카메라 공간 정확도 표: HMR2.0, WHAM 대비](/images/shen-2024-gvhmr-gravity-view/table2-camera-metric.png)

| 모델 | 3DPW PA-MPJPE | 3DPW MPJPE | RICH MPJPE | EMDB PA-MPJPE |
|---|---|---|---|---|
| HMR2.0 | 44.4 | 69.8 | 96.0 | 60.6 |
| WHAM* | 35.9 | 57.8 | 80.0 | 50.4 |
| **GVHMR\*** | **36.2** | **55.6** | **66.0** | **42.7** |

세계 좌표에 특화된 방법인데 카메라 공간에서도 SOTA를 갱신한다. RICH MPJPE는 80.0에서 66.0으로 14mm 줄었고, EMDB PA-MPJPE는 50.4에서 42.7로 감소한다.

### 추론 속도

1430프레임(약 45초) 비디오에서 트랜스포머 추론 자체는 0.28초에 끝난다. WHAM은 같은 시퀀스에 2.0초가 걸리므로 약 14배 빠르다. 전처리(YOLOv8, ViTPose, ViT 특징 추출)에 46초가 더 붙는 것은 두 방법 모두에서 공통이므로, 정확한 비교는 코어 네트워크 속도로 봐야 한다.

## Ablation: 어떤 설계가 얼마나 기여하는가

RICH 벤치마크에서 각 구성 요소를 하나씩 제거한 결과다.

| 변형 | PA-MPJPE | W-MPJPE | RTE | Jitter | 발 미끄럼 |
|---|---|---|---|---|---|
| w/o GV 좌표계 | 40.0 | 278.9 | 5.9 | 9.7 | 7.5 |
| w/o $\Gamma_{GV}$ (상대 회전 예측) | 41.4 | 177.5 | 4.5 | 14.9 | 3.0 |
| w/o 트랜스포머 | 43.3 | 138.9 | 2.7 | 7.6 | 3.3 |
| w/o RoPE | 87.5 | 304.4 | 6.3 | 22.8 | 11.5 |
| w/o 후처리 | 39.5 | 145.2 | 3.0 | 14.5 | 6.8 |
| **Full Model** | **39.5** | **126.3** | **2.4** | 12.8 | **3.0** |

두 개의 결과가 눈에 띈다. RoPE를 절대 위치 인코딩으로 바꾸면 카메라 공간 오차 자체가 39.5→87.5로 두 배 이상 커진다. 상대 위치 인코딩이 장시간 시퀀스 일반화에 결정적이라는 뜻이다. GV 좌표계 대신 카메라 좌표계에서 학습하면 W-MPJPE가 126.3→278.9로 두 배 이상 커진다. 세계 좌표 성능의 뿌리가 <em>GV 좌표계 자체</em>임을 확인한다.

## 한계와 함의

논문은 별도의 Limitations 절을 두지 않지만, 실험 설정에서 몇 가지 의존성이 드러난다.

- **상대 카메라 회전이 필요하다.** DPVO 같은 SLAM 프론트엔드나 IMU 자이로가 필수 입력이다. 다만 두 소스의 성능 차가 거의 없어 실용상 큰 제약은 아니다.
- **전처리 비용이 크다.** 코어 네트워크는 0.28초에 끝나지만 YOLOv8, ViTPose, ViT 특징 추출에 45초짜리 시퀀스 기준 46초가 든다. 실시간 응용에는 프론트엔드 최적화가 병목이다.
- **세계 방향은 첫 프레임 기준.** $\Gamma_w^0 = \Gamma_{GV}^0$으로 두므로, 첫 프레임의 카메라 회전 추정에 세계 궤적 전체가 걸린다. 첫 프레임이 크게 흔들리면 이후 궤적 전체가 편향된다.

함의는 세 갈래로 정리된다.

- **좌표계 설계가 학습을 결정한다.** 신경망 아키텍처와 손실함수를 다듬는 대신, 학습 문제 자체가 유일하게 정의되도록 좌표계를 잡으면 훨씬 큰 이득이 온다. Gravity-View는 그 사례다.
- **자기회귀 없이도 시퀀스가 안정적일 수 있다.** 프레임별 독립 예측이라도 세계 좌표계 정의가 견고하면 시간적 일관성이 유지된다. WHAM이 짐진 오차 누적의 무게는 알고 보면 자기회귀 자체가 아니라 <em>좌표계 모호성</em>의 결과였다.
- **속도와 정확도가 함께 얻어진다.** 자기회귀 제거는 병렬화가 가능하고 오차 누적도 줄이므로 두 축이 동시에 개선된다. 논문의 14배 속도 향상과 30% 정확도 개선이 우연히 겹친 것이 아니다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 좌표계 하나를 새로 잡는 발상이 얼마나 큰 파장을 낳는지다. 신경망 자체는 표준 ViT 인코더에 12층 트랜스포머, 다중 헤드 예측이라는 흔한 구성이다. 데이터도 AMASS와 BEDLAM 위주로 새로 만들지 않았다. 그럼에도 SOTA를 두 자릿수 퍼센트로 앞지른 이유는 단 하나, 신경망이 학습할 매핑을 <em>유일하게</em> 정의해 준 좌표계에 있다.

RoPE Ablation도 인상적이었다. 상대 위치 인코딩을 절대 위치로 바꾸면 카메라 공간 PA-MPJPE가 39.5에서 87.5로 두 배 이상 튄다. 세계 좌표를 위해 도입한 상대성이 카메라 공간 정확도까지 함께 끌어올렸다. 시퀀스 길이 일반화가 정확도 자체의 조건이라는 관찰이다.

한 가지 눈에 걸리는 것은 이 모든 성능의 뿌리인 첫 프레임 카메라 회전이 여전히 SLAM 프론트엔드에 의존한다는 점이다. 논문이 자기회귀 오차 누적을 없앤다고 강조하지만, 회전 추정은 여전히 자기회귀적이다. GV의 다음 진화 방향이 있다면 그 지점일 것이다.

## 출처

- 저자: Zehong Shen, Huaijin Pi, Yan Xia, Zhi Cen, Sida Peng, Zecen Hu, Hujun Bao, Ruizhen Hu, Xiaowei Zhou
- 소속: Zhejiang University, The University of Hong Kong, Deep Glint, Shenzhen University
- 발표: SIGGRAPH Asia 2024 Conference Proceedings
- arXiv: [2409.06662](https://arxiv.org/abs/2409.06662)
- 원문: <https://zju3dv.github.io/gvhmr/>
- 코드: <https://github.com/zju3dv/GVHMR>
- 라이선스: CC-BY-NC-SA 4.0 (figures 본문 인용)
