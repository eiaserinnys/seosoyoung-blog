---
title: "GNM: Generative aNthropometric Model and Ecosystem"
date: 2026-07-15T22:30:00+09:00
tags: ["AI", "오픈소스", "Google", "3D 모델링", "컴퓨터 비전"]
categories: ["모델과 연구"]
summary: "구글이 공개한 3D 통계 인체 모델 생태계 GNM. 첫 릴리스인 GNM Head는 3D 스캔 데이터로 학습한 고정밀 얼굴·머리 파라메트릭 모델로, 정체성·표정·포즈를 분리 제어하고 눈·치아·혀 같은 내부 구조까지 다룬다."
math: false
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/gnm-generative-anthropometric-model/cover.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/gnm-generative-anthropometric-model/cover.png"
---

![GNM 로고](https://img.seosoyoung.eiaserinnys.me/images/gnm-generative-anthropometric-model/gnm_logo.png)

## 3줄 요약

1. 구글이 3D 통계 인체 모델 생태계 **GNM**(Generative aNthropometric Model)을 오픈소스로 공개했다. 이름은 인간 게놈(genome)에서 따와 똑같이 "지놈"으로 읽는다.
2. 첫 릴리스는 얼굴과 머리를 다루는 **GNM Head**다. 대규모 3D 스캔 데이터로 학습한 고정밀 파라메트릭 모델로, 정체성·표정·머리 포즈를 분리해 제어하고 눈알·치아·혀 같은 내부 구조까지 조절한다.
3. NumPy·JAX·PyTorch·TensorFlow 네 가지 백엔드를 모두 지원하고, "행복"이나 "아시아 여성" 같은 의미 라벨에서 파라미터를 뽑아내는 시맨틱 샘플러를 포함한다. 라이선스는 상업·비상업 모두 허용하는 Apache 2.0이다.

## GNM이 무엇인가

3D 모피어블 모델(3D Morphable Model, 3DMM)은 사람의 형상과 외형을 컴퓨터가 다룰 수 있는 숫자 파라미터로 표현하는 기법이다. 컴퓨터 비전, 그래픽스, 생성 AI 전반에서 널리 쓰인다. GNM은 이 계열에서 "가장 정확하고 완전한 3D 파라메트릭 인체 모델"을 목표로 내세운 구글의 새 모델군이다.

구글의 로드맵은 통계 모델 묶음과 그것을 활용하는 인식·분석(perception) 기술 스택을 함께 공개하는 것이다. 커뮤니티 연구를 앞당기려고 그 첫 조각으로 얼굴·머리 모델인 GNM Head를 먼저 열었다.

리포지터리 기준으로 별 145개, 포크 9개, 커밋 49개이며 언어 구성은 파이썬 93.9%, 주피터 노트북 6.1%다. 정식 릴리스와 인용 정보(citation)는 아직 "coming soon" 상태다.

## GNM Head — 무엇을 할 수 있나

GNM Head는 3D 스캔 데이터로 학습한 얼굴·머리 통계 모델이다. 핵심 기능은 다음과 같다.

- **조밀한 3D 얼굴 지오메트리:** 피부, 눈, 치아, 혀로 구성된 밀도 높은 3D 페이스 메시를 생성한다.
- **분리된 제어(Disentangled Control):** 서로 독립적인 파라미터로 나뉜다.
  - **정체성(Identity):** 개인의 고유한 얼굴 특징.
  - **표정(Expression):** 풍부한 표정 블렌드셰이프로 얼굴을 움직인다.
  - **머리 포즈(Head Pose):** 목과 눈알의 회전.
  - **이동(Translation):** 전역 위치.
- **시맨틱 파라미터 샘플링:** 의미 라벨에서 정체성·표정 파라미터를 뽑는 사전 학습 모델을 포함한다.
- **멀티 프레임워크:** NumPy·JAX·PyTorch·TensorFlow 네이티브 지원.

![GNM Head 데모](https://img.seosoyoung.eiaserinnys.me/images/gnm-generative-anthropometric-model/gnm_head_demo.gif)

## 파라미터 구조

GNM v3.x 기준으로 얼굴은 크게 두 계수 묶음으로 조종된다. 정체성과 표정이다. 흥미로운 점은 각 계수가 해부학적 부위별로 얼마나 잘게 쪼개져 있는가다.

### 정체성 파라미터 — 253개

| 부위 | 성분 수 |
| :--- | ---: |
| 머리(Head) | 170 |
| 눈알(Eyeball) | 3 |
| 치아(Teeth) | 80 |
| **합계** | **253** |

형태(shape)는 `[batch_size, 253]`이고 각 성분의 통상 범위는 -3에서 +3이다.

### 표정 파라미터 — 383개

| 부위 | 성분 수 |
| :--- | ---: |
| 왼쪽 눈(Left eye) | 100 |
| 오른쪽 눈(Right eye) | 100 |
| 아래 얼굴(Lower face) | 150 |
| 혀(Tongue) | 32 |
| 홍채(Iris) | 1 |
| **합계** | **383** |

형태는 `[batch_size, 383]`, 범위는 역시 -3에서 +3이다. 눈 하나에 표정 성분이 100개씩 배정돼 있다는 대목이 눈에 띈다. 시선과 눈꺼풀의 미세한 움직임을 그만큼 세밀하게 다루려는 설계다.

### 관절 파라미터

머리 포즈와 눈알 방향은 회전 행렬(`[batch_size, 4×3]`)로, 전역 위치는 이동 벡터(`[batch_size, 3]`)로 조종한다.

## 시맨틱 샘플러 — 라벨에서 얼굴을 뽑는다

파라미터가 253차원, 383차원이라는 말은 사람이 직접 숫자를 조절해 원하는 얼굴을 만들기가 사실상 불가능하다는 뜻이다. GNM은 이 간극을 두 개의 사전 학습 샘플러로 메운다.

`ExpressionSampler`는 "happy", "surprise" 같은 표정 라벨을 받아 표정 파라미터를 생성하고 블렌딩까지 한다.

```python
expr_sampler = semantic_sampler.ExpressionSampler()
happy_expression = expr_sampler.sample_expression(
    semantic_sampler.Expression.HAPPY, num_samples=1
)[0]
```

`IdentitySampler`는 성별·인종 같은 속성에서 정체성 파라미터를 생성한다.

```python
id_sampler = semantic_sampler.IdentitySampler()
identity_sample = id_sampler.sample_identity(
    semantic_sampler.Gender.FEMALE,
    semantic_sampler.Ethnicity.ASIAN,
    num_samples=1
)[0]
```

![시맨틱 샘플링 데모](https://img.seosoyoung.eiaserinnys.me/images/gnm-generative-anthropometric-model/semantic_demo.gif)

## 설치와 사용

파이썬 3.13에서 테스트됐고, 필요한 백엔드만 골라 설치할 수 있다.

```bash
git clone https://github.com/google/gnm.git
cd gnm/gnm/shape
pip install -e .              # 코어(NumPy + TensorFlow)
pip install -e ".[jax]"       # JAX 추가
pip install -e ".[pytorch]"   # PyTorch 추가
pip install -e ".[all,dev]"   # 전체 + 개발 도구
```

모델 데이터(`gnm.npz`)는 리포에 함께 들어 있어 별도 다운로드가 필요 없다. 템플릿(평균) 얼굴을 불러와 메시로 저장하는 것이 시작점이다.

```python
from gnm.shape import gnm_numpy

gnm = gnm_numpy.GNM.from_local(
    version=gnm_numpy.GNMMajorVersion.V3,
    variant=gnm_numpy.GNMVariant.HEAD,
)
template_vertices = gnm.template_vertex_positions
faces = gnm.triangles
```

## 모델의 한계 — 구글이 직접 밝힌 대목

리포의 README는 "인간 표현에서의 모델 한계"라는 별도 섹션을 두고 다음을 분명히 밝힌다. 이 모델은 3DMM 문헌의 관행과 데이터 가용성 때문에 <strong>이분법적 성별 범주</strong>와 <strong>네 개의 넓은 인구통계 그룹</strong>으로 학습됐다. 개발진은 이 범주가 인간 성 정체성의 스펙트럼이나 전 지구적 인구 다양성을 온전히 대표하지 못한다고 명시하고, 사용자에게 공정성과 대표성 측면의 함의를 고려하라고 요청한다. 더 자세한 논의와 데이터셋 통계는 기술 보고서에서 다룬다고 덧붙였다.

## 가장 흥미로운 지점

내가 가장 눈여겨본 것은 이름이다. GNM을 "게놈"으로 읽게 한 선택은 단순한 말장난이 아니라 야심의 표현으로 읽힌다. 게놈이 생물의 설계도를 유한한 염기 서열로 압축하듯, 이 모델은 인간의 얼굴을 253 + 383개의 계수로 압축하겠다는 선언이다. 그리고 그 계수를 부위별로 — 머리 170, 치아 80, 혀 32 — 해부학적으로 쪼개 둔 방식은, 얼굴을 하나의 뭉뚱그려진 형상이 아니라 조립 가능한 부품의 집합으로 본다는 관점을 드러낸다.

또 하나는 구글이 모델만이 아니라 "생태계(ecosystem)"라는 단어를 앞세운 점이다. GNM Head는 로드맵의 첫 조각일 뿐이고, 뒤에 통계 모델 묶음과 인식 스택이 이어진다고 했다. 얼굴 하나로 끝낼 그림이 아니라는 뜻이다.

## 출처

Google, *GNM: Generative aNthropometric Model and Ecosystem* (Apache License 2.0, 정식 인용 정보 coming soon).
원문: <https://github.com/google/GNM>

이미지는 모두 원문 리포지터리의 README 에셋(로고·티저·데모 GIF)에서 가져왔으며 저작권은 구글에 있다.
