---
title: "On the Ability of Deep Networks to Learn Symmetries from Data: A Neural Kernel Theory"
date: 2026-06-09T22:00:00+09:00
tags: ["AI", "논문 리뷰", "학습 역학", "등변성", "일반화"]
categories: ["모델과 연구"]
summary: "Perin·Deny(Aalto, NeurIPS 2024 v2 2025-06)가 무한폭 NTK 한계에서 신경망의 대칭 학습 능력을 분석한 논문. 일부 클래스에서만 대칭을 부분 관측한 상황에서의 일반화 오차가 단 하나의 공식, λ_N^{-1}/⟨λ^{-1}⟩로 결정되며, 표준 MLP·CNN·ViT는 아키텍처에 사전 내재되지 않은 대칭을 학습할 메커니즘이 없다는 것을 이론과 실험으로 보였다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/perin-deny-2024-neural-kernel-symmetry/fig1-problem-setup.png"
images:
  - "/images/perin-deny-2024-neural-kernel-symmetry/fig1-problem-setup.png"
---

## 3줄 요약

1. Andrea Perin·Stéphane Deny(Aalto Univ., 2024-12 v1, 2025-06 v2)가 무한폭 NTK 한계에서 신경망의 *대칭 학습 능력*을 이론적으로 분석한 논문이다. 일부 클래스는 모든 회전을, 일부 클래스는 일부 회전만 본 부분 관측 설정에서 표준 신경망이 빠진 자세까지 일반화할 수 있는가를 묻는다.
2. 핵심 결과는 일반화 오차가 단 하나의 비율, <em>spectral error</em> $\varepsilon_s = \lambda_N^{-1} / \langle\lambda^{-1}\rangle$ 로 결정된다는 것이다. 분자 $\lambda_N$은 클래스 분리 거리에, 분모 $\langle\lambda^{-1}\rangle$은 궤도(orbit) 밀도에 각각 대응한다.
3. 결론은 단호하다. 표준 MLP·CNN·ViT는 *아키텍처에 a priori로 내재되지 않은* 대칭을 학습할 메커니즘이 없다. 데이터의 국소 구조가 비국소·대칭 구조를 압도할 때만 일반화에 성공한다. 다만 GAP-CNN처럼 대칭이 구조에 그대로 흡수된 특수 케이스만 완벽 일반화를 보장한다.

## 자료의 정체

- **저자:** Andrea Perin, Stéphane Deny (Department of Computer Science, Aalto University, Finland)
- **arXiv:** [2412.11521v2](https://arxiv.org/abs/2412.11521) (v1 2024-12-16, v2 2025-06-26)
- **분야:** Machine Learning (cs.LG). 무한폭 신경망 이론 + 등변 표현 학습.
- **코드:** <https://github.com/Andrea-Perin/gpsymm>
- **목적:** 표준 supervised 학습된 일반 아키텍처(MLP, CNN, ViT)가 데이터에 잠재된 <em>대칭(symmetry)</em>을 학습할 수 있는가에 대한 이론을 세운다. 부분 관측이라는 현실적 설정 위에서 무한폭 한계의 NTK 분석으로 이 질문에 정량적 답을 준다.

## 부분 관측된 대칭이라는 문제

대칭은 데이터의 정체성을 바꾸지 않는 군 작용(group action)으로 정의된다. 의자는 정립 자세든 거꾸로든 의자다 ($SO(3)$ 작용). 회전된 MNIST에서 숫자 '4'는 어떤 각도로 돌려도 '4'다.

논문이 다루는 시나리오는 단순하다. 아이가 발달기에 *손에 잡히는 장난감*은 모든 3D 자세에서 보지만, *무거운 가구*는 몇 자세에서만 본다. 신경망도 마찬가지로 학습 데이터에서 어떤 클래스는 대칭 변환의 모든 인스턴스를 보고, 어떤 클래스는 일부만 본다. 그렇다면 신경망은 부분 관측 클래스에 대해 *대칭 불변성을 외삽*할 수 있는가?

![Figure 1: 학습 과제 설정과 표준 아키텍처의 실패](/images/perin-deny-2024-neural-kernel-symmetry/fig1-problem-setup.png)

A 패널이 과제를 보여준다. 한 클래스(예: 숫자 '5')를 *leave-out 클래스*로 정하고, 그 클래스의 정립(upright) 자세만 학습에서 빼고 다른 회전은 모두 포함시킨다. 나머지 클래스는 모든 회전을 포함한다. 일반화가 가능한 모델이라면, 학습에서 본 적 없는 정립 자세의 '5'를 옳게 분류해야 한다.

결과는 B·C 패널에서 명확하다. MLP·ConvNet·ViT-S 세 아키텍처 모두 train·in-test 정확도는 높지만 *out-test*(빠진 자세) 정확도는 chance level(10%)에 가까이 떨어진다. 1000 epoch 이상 학습해도 그로킹(grokking)은 일어나지 않는다. 단, 회전 각도를 더 촘촘히 샘플링하면 out-test 정확도가 점진적으로 회복된다. 이 점진성 자체가 "신경망에는 대칭을 *발견하는* 메커니즘이 없고, *밀도로 채워 메우는* 일밖에 못한다"는 본 논문의 결론과 일치한다.

## 이론: Spectral Error 공식

논문의 두 관찰이 이론의 골격을 이룬다. 첫째, NTK 한계에서 신경망 학습은 커널 회귀(kernel regression)와 동치다. 둘째, 데이터가 대칭을 가지면 커널 회귀가 극도로 단순화된다.

### Circulant Gram 행렬

크기 $N$의 순환군(cyclic group)의 궤도로 생성된 데이터셋을 두 개 가져와 인터리브하면 (라벨 +1·-1을 교차 배치), 정상(stationary) 커널 또는 내적(dot product) 커널은 Gram 행렬이 *순환(circulant) 구조*를 가진다. RBF 커널은 자명히, MLP의 NTK 커널은 내적 구조 덕분에 단일 궤도 위에서 자동으로 그렇다.

### 핵심 공식

순환 그램 행렬은 <em>이산 푸리에 변환(DFT)</em>으로 대각화되며, 한 점을 빼고 그 점을 회귀로 추정한 <em>spectral error</em>는 다음과 같다.

$$
\varepsilon_s = \frac{\lambda_N^{-1}}{\langle\lambda^{-1}\rangle}
$$

- $\lambda_N$ : 그램 행렬의 *최고 주파수* 고유값.
- $\langle\lambda^{-1}\rangle$ : 모든 주파수에 걸친 고유값 역수의 평균.

이 비율이 작아질수록 일반화 오차가 작다. 분자가 작아지려면 $\lambda_N$이 커야 하고, 분모가 커지려면 저주파 성분의 역수가 발산해야 한다.

![Figure 2: 원형 데이터셋에서 가우시안 커널의 spectral error 기하 해석](/images/perin-deny-2024-neural-kernel-symmetry/fig2-circular-dataset.png)

A 패널의 데이터셋은 $\mathbb{R}^3$에서 두 클래스가 인터리브된 원형 점들이다. B는 그램 행렬이 순환 구조임을 시각화한다. C에서 한 행을 뽑으면 같은 라벨·반대 라벨 값이 교대로 나타나는데, 이것이 *암묵적 고주파 성분*에 해당한다. D는 spectral error를 두 영역의 비율로 본 기하 해석이다. 회색 영역(분자)이 작고 빨간 영역(분모)이 클수록 일반화 오차가 낮다.

### 두 축의 기하학적 해석

![Figure 3: 클래스 분리도 Δ와 궤도 점 개수 N의 영향](/images/perin-deny-2024-neural-kernel-symmetry/fig3-delta-N.png)

A-C는 두 원형 클래스 사이의 거리 $\Delta$를 늘리는 경우다. $\Delta$가 커질수록 최고 주파수 $\lambda_N$의 파워가 커져 분자가 작아지고, 오차가 감소한다. *클래스가 서로 멀어지면 국소 커널로도 빠진 점을 추측하기 쉬워진다*는 직관과 정확히 맞물린다.

D-F는 같은 클래스의 점 개수 $N$을 늘리는 경우다. $N$이 커지면 DFT 주파수 슬롯이 늘어나 저주파 슬롯에 잡혀 있던 작은 값들이 한층 더 작아지고, $\langle\lambda^{-1}\rangle$이 발산한다. *궤도가 촘촘할수록 빠진 점이 이웃에 둘러싸여 채우기 쉬워진다*는 직관에 대응한다.

## Rotated-MNIST에서의 검증

![Figure 4: MLP의 NTK와 spectral error의 대응](/images/perin-deny-2024-neural-kernel-symmetry/fig4-mlp-rotated-mnist.png)

이론은 단일 시드(seed) 짝의 단순한 설정에서 출발하지만, 실험은 곧장 회전된 MNIST 위에서 확장된다. 두 디지트 클래스에서 한 시드씩 뽑아 8개 회전 궤도를 만들고, MLP의 NTK 커널을 적용한다. NTK 커널은 원형으로 인터리브된 경우가 아니어서 <em>ex-post 순환화(circularization)</em>가 필요하다. 대각선 평균으로 그램 행렬을 순환 행렬로 근사한다. 이 근사 후에 적용된 spectral error는 *정확한 NTK 오차와 매우 잘 일치*한다 (B).

D·E 패널이 기하 해석을 입증한다. $\lambda_N$은 *입력 공간에서 두 궤도 중심 사이 거리*에 거의 선형, $\langle\lambda^{-1}\rangle$은 *궤도 반지름의 역수*에 거의 선형이다. 즉 커널 공간의 spectral 양은 입력 공간의 *클래스 분리*와 *궤도 밀도*에 직접 매핑된다.

이 대응은 다양한 아키텍처에서도 유지된다 (Figure 5에서 5층 MLP, 유한폭 Adam 학습 MLP, FC ConvNet 모두 spectral error와 NTK error가 일치). GAP-CNN만 일치도가 떨어지는데, 그 이유는 후술한다.

## 다중 클래스로의 확장

![Figure 6: 다중 시드·다중 클래스에서의 일반화 정확도](/images/perin-deny-2024-neural-kernel-symmetry/fig6-multiclass.png)

논문은 단일 시드·이항 분류 설정을 (1) 시드 여러 개·이항, (2) 시드 여러 개·10-클래스로 확장한다. 확장 트릭은 단순하다. 두 클래스의 *모든 시드 쌍*에 대해 spectral error를 계산하고 평균한다 (선형 상호작용 근사). 10-클래스의 경우는 *one-vs-many* 전략으로 클래스마다 별도 평균을 낸다.

B 패널이 결정적이다. 횡축은 궤도 각도 수 $N_{rot}$, 종축은 정확도. 이론(spectral)과 실험(MLP cross-entropy 학습)이 거의 같은 곡선을 그린다. *어디에도 phase transition이 없다.* 신경망이 "대칭을 알아챘다"는 순간이 존재하지 않고, 단지 궤도 밀도와 클래스 분리가 임계 수준에 도달했을 때 spectral 비율이 작아져 분류가 정확해질 뿐이다.

## 등변 아키텍처와 대칭의 일치

CNN은 평행이동(translation)에 대해 등변이다. 회전(rotation)에 대해서는 아니다. 논문은 두 경우를 모두 다룬다.

| 아키텍처 | 데이터 대칭 | Gram 행렬 | 일반화 |
|---|---|---|---|
| FC-Conv | Translation | 순환, 비퇴화 | 불완전 (MLP와 동일 한계) |
| GAP-Conv | Translation | 상수, 퇴화 | **완벽** (오차 0) |
| FC-Conv | Rotation | 순환, 비퇴화 | 불완전 |
| GAP-Conv | Rotation | 순환, 비퇴화 | 불완전 (단, 실험상 매우 낮은 오차) |

GAP-CNN이 translation에서 완벽 일반화하는 이유는 그램 행렬이 *블록 상수*가 되어 rank-deficient가 되기 때문이다. 분모 $\langle\lambda^{-1}\rangle$이 발산하여 $\varepsilon_s \to 0$. 회전에서는 그렇지 않다. GAP은 평행이동 불변일 뿐 회전 불변이 아니므로.

이 결과는 등변 신경망(equivariant network)의 성공이 *데이터 대칭을 학습했기 때문이 아니라*, *아키텍처가 대칭을 이미 흡수하기 때문*임을 spectral 수준에서 확정한다.

## 함의와 한계

논문이 도출하는 함의는 명확하다.

- **표준 신경망은 대칭을 학습하지 못한다.** 학습 데이터에 부분 관측된 대칭을 본 적이 있다고 해서 그 대칭이 *비국소적*으로 일반화되지 않는다. 그저 데이터의 *국소* 구조가 일반화를 결정한다.
- **scaling law와의 정합.** 데이터를 늘리면 일반화가 점진적으로 개선되는 현상은 spectral error의 분모가 점진적으로 커지는 것과 일치한다. 그로킹 같은 갑작스러운 전환이 관측되지 않는 이유다.
- **데이터 비효율의 근원.** 회전·이동·스케일링 등 변환이 결합되면 *combinatorial explosion*이 일어나므로, 모든 변환을 학습 데이터로 본 적 없는 변환 조합에서 현 신경망이 취약한 이유가 설명된다.

한계는 저자들이 명시한다.

- 무한폭 NTK 한계(*lazy regime*) 위의 분석이다. *feature learning regime*에서는 커널이 시간에 따라 진화하므로 결론이 달라질 수 있다 ([Marion et al. 2024](https://arxiv.org/abs/2402.16469)가 active regime에서 *저-차원 함수*로서의 대칭은 학습 가능하다고 보고).
- 가설은 *직접* 공간에 작용하는 대칭(이미지 회전·이동)에 한정. 잠재 공간 대칭(3D 회전된 객체의 2D 이미지)은 더 어렵다.
- 이산 순환군 중심. 비가환 유한군까지 확장(부록 C)했지만 $SO(3)$ 같은 연속군은 후속 과제.

대안 경로로 저자들이 제시하는 것: (1) 매우 큰 데이터셋 + 데이터 증강, (2) soft bias로 등변 구조를 유도, (3) self-supervised pretraining, (4) Bayesian model selection / Kolmogorov 최소 기술 길이, (5) feature-rich learning regime.

## 가장 흥미로운 지점

논문이 단순한 식 하나로 길게 발견되어 온 현상을 통합하는 방식이 인상적이다. *데이터 증강이 진짜 등변성을 만들지 못한다*는 보고, *3D 자세 변환에서 사람이 SOTA 비전 모델보다 잘한다*는 관찰, *대형 데이터셋(JFT-300M·LAION-5B)이 비전에서 필수가 된 이유*, 이 모든 것이 하나의 식 $\varepsilon_s = \lambda_N^{-1}/\langle\lambda^{-1}\rangle$로 동시에 설명된다.

저자들이 결론에 슬쩍 던지는 인지과학 단서도 흥미롭다. 정신적 회전(mental rotation) 과제에서 인간의 반응 시간이 각도 차에 *비례*한다는 사실은, 인간의 뇌가 *재귀적 처리*로 대칭 변환을 처리할 가능성을 시사한다. 현 트랜스포머에는 그런 재귀가 없다. 아이의 발달기에 *거울 대칭을 풀어내는* 단계가 필요하다는 발달심리학 관찰, *병아리가 태어나면서부터 3D 객체를 다각도로 인식*한다는 발견도 함께 인용된다. "대칭은 아키텍처에 a priori 새겨져 있어야 한다"는 본 논문의 결론이, 어쩌면 자연의 신경계에도 똑같이 적용되는 명제일 수 있다는 암시다.

추론과 일반화의 한계를 *수식 하나로* 짚어 두면, 다음 단계의 메커니즘 설계가 무엇을 갖춰야 하는지가 비로소 보인다. 본 논문은 그 다음 단계로 가기 위한 가장 확실한 측정자 하나를 손에 쥐여 준다.

## 출처

- 저자: Andrea Perin, Stéphane Deny (Aalto University, Finland)
- arXiv: [2412.11521v2](https://arxiv.org/abs/2412.11521). 발행: 2024-12-16 (v1), 2025-06-26 (v2)
- 라이선스: arXiv 표준 라이선스 (figures 본문 인용)
- 원문: <https://arxiv.org/abs/2412.11521>
- 코드: <https://github.com/Andrea-Perin/gpsymm>
