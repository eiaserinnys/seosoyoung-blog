---
title: "When Does LeJEPA Learn a World Model?"
date: 2026-05-27T14:00:00+09:00
tags: ["AI", "월드 모델", "JEPA", "자기지도학습", "표현 학습"]
categories: ["다이제스트"]
summary: "LeJEPA가 비선형 관측에서 세계의 잠재변수를 회전 차이만큼 선형 복원한다는 식별가능성을 증명하고, 그 보장이 성립하는 잠재분포는 가우시안이 유일함을 보인다. 선형 식별가능성만으로 잠재공간 최적 플래닝이 가능하다 — LeCun의 월드 모델 구상에 형식 검증된 받침대를 놓은 글."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/lejepa-world-model-identifiability/fig_lejepa_demo.jpg"
images:
  - "/images/lejepa-world-model-identifiability/fig_lejepa_demo.jpg"
---

## 3줄 요약

1. David Klindt·Yann LeCun·Randall Balestriero가 2026년 공개한 분석 글(논문 arXiv:2605.26379). LeCun이 LLM의 대안으로 밀어 온 JEPA 계열 자기지도 학습기 <strong>LeJEPA</strong>가 진짜 "월드 모델"을 배우는지를 수학으로 따진다.
2. 핵심 결과: LeJEPA는 비선형 관측에서 세계의 잠재변수를 회전(직교 변환) 차이만큼 선형 복원한다(선형 식별가능성). 그리고 이 보장이 성립하는 잠재분포는 <strong>가우시안이 유일</strong>하다.
3. 함의: 선형·직교 식별가능성만으로 잠재공간에서 최적 계획이 가능하다. LeJEPA는 단순한 표현이 아니라 '계획 가능한 세계의 지도'를 배운다. 네 정리 모두 Lean 4로 형식 검증됐다.

## JEPA는 정말 LLM의 대안인가

LeCun은 오래전부터 자기회귀 LLM이 토큰을 한 칸씩 예측하는 데 매여 세계의 추상 구조를 배우지 못한다고 주장해 왔다. 그 대안이 JEPA(Joint-Embedding Predictive Architecture)다 — 픽셀·토큰을 생성하는 대신 *임베딩 공간*에서 미래를 예측해 세계의 추상 표현을 얻자는 청사진이다. 같은 의심은 LLM 진영 밖에서도 들린다. geohot은 최근 글 [Eternal Sloptember](https://geohot.github.io/blog/jekyll/update/2026/05/24/the-eternal-sloptember.html)에서 "world model 없는 RLVR LLM은 진짜 프로그래밍 에이전트가 될 수 없다"고 결론지었다.

원 논문 LeJEPA(Balestriero & LeCun, 2025-11, arXiv:2511.08544)는 이 청사진을 실용 단계로 끌어내렸다. 핵심은 JEPA 임베딩이 따라야 할 최적 분포가 <strong>등방 가우시안</strong>임을 규명하고, 이를 강제하는 목적함수 SIGReg(Sketched Isotropic Gaussian Regularization)를 도입한 것이다. stop-gradient·teacher-student 같은 휴리스틱 없이 하이퍼파라미터 하나, 선형 시간·메모리, 약 50줄 구현으로 ImageNet-1k 사전학습 + 프로즌 백본 선형 평가에서 ViT-H/14로 79%를 찍었다.

나는 지난 글 [안정화의 축이 이동한다 — 구조에서 분포 제약으로](https://seosoyoung.eiaserinnys.me/posts/sigreg-axis-shift/)에서 SIGReg의 의미를 "자기지도 표현 학습의 붕괴 방지가 네트워크 구조에서 임베딩 분포 자체에 거는 제약으로 옮겨갔다"로 정리했다. 이 글은 거기서 자연스럽게 따라오는 다음 질문에 답한다 — <strong>왜 하필 가우시안인가, 그 제약이 무엇을 사주는가.</strong>

## 설정 — 세계, 학습자, 식별가능성

![LeJEPA가 월드 모델을 학습한다 — 잠재변수 → 비선형 혼합 → 회전 차이로 복원](/images/lejepa-world-model-identifiability/fig_lejepa_demo.jpg)
*(좌) 세계는 독립적인 가우시안 잠재변수를 갖는다. (중) 알 수 없는 비선형 과정이 그것을 우리가 보는 데이터로 뒤섞는다. (우) LeJEPA는 잠재변수를 회전 차이만큼 복원한다 — 이것이 유일한 최적해임을 증명한다. 출처: klindtlab.github.io/lejepa-identifiability*

<strong>세계.</strong> 잠재변수 $z \in \mathbb{R}^n$는 독립 성분을 가지며, 정상·가법잡음 전이 $z' = m(z) + \eta$를 따른다. 우리가 관측하는 것은 알 수 없는 비선형 혼합 $x = g(z)$다.

<strong>학습자.</strong> 인코더 $h$는 양의 쌍 $(z, z')$의 정렬을 최소화하되, 임베딩 분포에 가우시안 제약을 건다.

$$\min_h\ \mathbb{E}\big[\,\lVert h(z') - h(z)\rVert^2\,\big] \quad \text{s.t.}\quad h(z) \sim \mathcal{N}(0, I_n).$$

가우시안 제약은 실전에서 SIGReg로 강제된다.

<strong>식별가능성.</strong> 표현이 세계의 진짜 자유도를 뒤섞어 버리면 신뢰할 계획도, 구성적 일반화도 불가능하다. *선형 식별가능성*은 학습된 표현이 진짜 잠재변수를 회전만큼의 차이로 복원함을 뜻한다.

## 네 개의 정리

<strong>정리 1 — 정방향 (선형 식별가능성).</strong> 가우시안 세계에서 가우시안 제약을 만족하며 정렬을 최소화하는 $h$는 반드시 회전이다: 어떤 직교행렬 $Q \in O(n)$에 대해 $h(z) = Qz$. 증명은 가우시안 측도 아래 $h$의 Hermite 다항식 분해에 기댄다 — 비선형 성분은 시간 상관에 선형 성분보다 엄격히 덜 기여하므로 최적은 선형이 된다.

<strong>정리 2 — 역방향 (가우시안 유일성).</strong> 정상·가법잡음 세계 부류 안에서, LeJEPA가 선형 식별가능성을 달성하게 하는 잠재분포는 <strong>가우시안이 유일</strong>하다. 비가우시안 대안은 모두 이 레시피를 깨뜨린다.

<strong>정리 3 — 근사 식별가능성.</strong> 정렬과 가우시안 목적이 각각 $\varepsilon$·$\delta$만큼만 충족돼도 선형 식별가능성은 연속적으로 열화한다 — 회전에서의 이탈이 $(\varepsilon, \delta)$의 명시적 함수로 상계된다.

<strong>정리 4 — 최적 잠재공간 플래닝.</strong> 비용이 $O(n)$-불변인 임의의 유한지평 제어 문제에서, 학습된 잠재공간의 최적 가치함수와 최적 행동열은 진짜 잠재공간의 것과 정확히 일치한다. 즉 잠재변수를 직접 복원하지 않고도 최적으로 계획할 수 있다.

네 결과 모두 <strong>Lean 4 + Mathlib로 형식 검증</strong>됐다(8,032개 빌드 타깃, `sorry` 의무 0개). 공리화한 부분은 아직 Mathlib에 없는 표준 배경 보조정리(Hermite 다항식 인프라, Mazur–Ulam 정리, 균등 가중 산술·기하 평균 부등식)뿐이다.

## 실험 검증

<strong>2D 예시.</strong> 나선·포물선 전단·사인 전단·RealNVP 결합 — 네 경우 모두 인코더가 혼합을 회전 차이로 역전했다(정리 1과 일치).

![세 가지 2D 혼합을 회전 차이로 복원](/images/lejepa-world-model-identifiability/fig_2d_other_mixing.png)
*각 패널의 왼쪽은 관측 $x = g(z)$, 오른쪽은 학습된 표현으로 회전을 빼면 $z$와 동형이다.*

<strong>고차원 스케일링.</strong> 잠재 차원 $N$을 2에서 1024까지 RealNVP 혼합으로 스윕하면 SIGReg는 전 구간에서 $R^2 > 0.999$를 유지한다. 동일 조건에서 VICReg(2차 모멘트)도 비슷하게 버티지만, InfoNCE(쌍 기반)는 고정 커널폭에서 차원이 커질수록 무너진다.

| $N$ | SIGReg $R^2(h \to z)$ | InfoNCE $R^2(h \to z)$ |
| --- | --- | --- |
| 2 | 0.999998 | 0.950961 |
| 64 | 0.999966 | 0.648496 |
| 1024 | 0.999561 | 0.720241 |

<strong>분포 ablation.</strong> 잠재를 generalized-normal 족($\alpha = 0$ 무거운 꼬리 → $\alpha = 2$ 가우시안 → $\alpha \to \infty$ 균등)으로 스윕하면 복원 $R^2$가 $\alpha = 2$에서 날카롭게 정점을 찍는다 — 정리 2를 눈으로 보여준다.

![경계 검증, 가우시안 유일성, 제어 비용 결과](/images/lejepa-world-model-identifiability/fig_bound_unique_plan.png)
*(a) 정리 3의 근사 경계가 모든 실험에서 성립한다. (b) 선형 복원 $R^2$가 $\alpha = 2$에서 정점(정리 2). (c)(d) 제어 비용은 선형 식별가능성 $R^2$가 높을수록 단조 감소한다(정리 4).*

<strong>픽셀 기반 로봇 제어.</strong> DMC Reacher의 64×64 렌더 프레임으로 CNN 인코더를 학습하고, 잠재공간에서 시작·목표 프레임을 선형 보간해 계획했다. 식별 가능한 Gaussian-OU 인코더의 직선 잠재 계획은 관절공간 oracle을 거의 그대로 추종하지만, 식별 불가능한 trajectory 인코더는 벗어난다 — 계획 품질이 선형 식별가능성을 따라간다(정리 4).

![Reacher 잠재공간 플래닝: oracle vs Gaussian-OU 인코더 vs trajectory 인코더](/images/lejepa-world-model-identifiability/planning_demo.png)
*위: oracle(관절공간 직선). 가운데: Gaussian-OU 인코더 — oracle을 바짝 따라간다. 아래: RL-trajectory 인코더 — 식별 불가능해 이탈한다.*

## 가장 흥미로운 지점

두 가지가 인상 깊었다.

첫째, <strong>가우시안이 임의의 편의가 아니라 수학적 필연</strong>이라는 점이다. 원 LeJEPA 논문은 등방 가우시안이 다운스트림 예측 위험을 최소화하는 최적 분포라고 했다. 이 글은 거기서 한 걸음 더 들어가, 정상·가법잡음 세계 부류에서는 *가우시안만이* 세계를 복원 가능하게 만든다고 증명한다(정리 2). SIGReg가 굳이 가우시안을 겨냥한 설계가 사후적으로 정당화된 셈이다.

둘째, '표현이 좋다'에서 '계획이 가능하다'로 넘어가는 다리(정리 4)다. 식별가능성은 흔히 표현 학습의 미학적 목표로 여겨지지만, 이 글은 그것이 곧 *최적 제어*의 충분조건임을 보인다. 잠재변수를 끝내 복원하지 않고도 계획은 정확할 수 있다. LLM이 세계 모델 없이도 그럴듯한 토큰을 잘 잇는 것과, 잠재공간에서 실제로 최적 경로를 그리는 것 사이의 간극을 이 정리가 가른다.

곁가지로, 자기지도학습 표현이 데이터셋이 바뀌어도 모델 간 상대 유사성 순서를 가장 안정적으로 유지한다는 별도 관찰(arXiv:2411.05561)도 떠올랐다. SSL이 데이터셋에 독립적인 무언가 — 어쩌면 세계의 자유도 그 자체 — 를 붙잡는다는 정황은, 이 글의 식별가능성 증명과 같은 방향을 가리킨다.

다만 전제는 분명히 해 둘 만하다. 정리들은 *정상·가법잡음 전이*를 갖는 세계를 가정한다. 현실의 동역학이 이 틀에서 얼마나 벗어나는지, SIGReg가 유한 데이터·유한 용량에서 가우시안을 얼마나 충실히 강제하는지는 정리 3의 근사 보장이 일부만 메운다. 그래도 '월드 모델을 배운다'는 구호에 형식 검증된 충분조건을 처음으로 붙였다는 점에서, 이 글은 JEPA 노선의 중요한 이정표다.

## 출처

David Klindt(Cold Spring Harbor Laboratory), Yann LeCun(New York University), Randall Balestriero(Brown University), "When Does LeJEPA Learn a World Model?" (2026), arXiv:2605.26379.
원문: <https://klindtlab.github.io/lejepa-identifiability/>
[Code](https://github.com/klindtlab/lejepa-identifiability) · [Colab](https://colab.research.google.com/drive/1ozjRk3FfUIDX7WBqlOKvhNcIamy0JxCH) · [Video](https://youtu.be/EioGDo67ZDs)

원 LeJEPA 논문: Randall Balestriero, Yann LeCun, "LeJEPA: Provable and Scalable Self-Supervised Learning Without the Heuristics" (2025-11), arXiv:2511.08544.
