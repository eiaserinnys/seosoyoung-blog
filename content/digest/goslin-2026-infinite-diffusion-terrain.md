---
title: "InfiniteDiffusion: Bridging Learned Fidelity and Procedural Utility for Open-World Terrain Generation"
date: 2026-06-26T10:00:00+09:00
tags: ["AI", "생성 모델", "3D 생성", "절차적 생성", "Minecraft"]
categories: ["모델과 연구"]
summary: "Alexander Goslin이 SIGGRAPH 2026에 발표한 InfiniteDiffusion과 Terrain Diffusion. diffusion 모델을 학습 없이 무한하고 결정적이며 O(1) random access가 가능한 형태로 재구성하고, 그 위에서 지구 규모 지형을 consumer GPU로 실시간 생성한다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/goslin-2026-infinite-diffusion-terrain/world-combined.jpeg"
images:
  - "/images/goslin-2026-infinite-diffusion-terrain/world-combined.jpeg"
---

![Terrain Diffusion으로 생성한 지구 규모 월드의 합성 시각화](/images/goslin-2026-infinite-diffusion-terrain/world-combined.jpeg)
*Terrain Diffusion 월드 시각화. 출처: xandergos.github.io/terrain-diffusion*

## 3줄 요약

1. Alexander Goslin이 SIGGRAPH 2026에 발표한 InfiniteDiffusion 논문. 일반적인 diffusion 모델을 *학습 없이* 무한 영역에서 결정적으로, 그리고 O(1) random access가 되도록 다시 풀어내는 알고리즘이다.
2. 핵심은 MultiDiffusion을 unbounded 또는 메모리보다 큰 도메인으로 일반화하여, 좌표와 시드만 주면 그 부분만 lazy하게 생성하는 drop-in replacement로 만든 것이다. 외부 상태가 없고 LRU 캐시만 내부에 둔다.
3. 응용편 Terrain Diffusion은 -10000m에서 9000m까지의 dynamic range를 한 월드에 담고, consumer GPU에서 궤도 속도의 9배로 지구 규모 지형을 실시간 생성한다. Minecraft mod와 Unity 데모로 시연되었다.

## 트릴레마 — 셋 중 둘만 고를 수 있었다

콘텐츠 생성 분야에는 *무한 영역(infinite extent)*, *무상태 생성(stateless generation)*, *학습된 사실성(learned realism)* 이라는 세 속성이 있다. 이때까지 셋을 동시에 가진 방법은 없었고, 항상 둘만 고르는 trilemma였다.

| 패러다임 | 무한 영역 | 무상태 | 학습 사실성 |
|---|:---:|:---:|:---:|
| Perlin 같은 절차적 노이즈 | O | O | X |
| 일반 diffusion 모델 | X | (해당 없음) | O |
| Auto-regressive outpainting | O | X | O |

Perlin 노이즈는 빠르고 무한하지만 사실성이 없다. Diffusion 모델은 사실성을 끌어올렸지만 bounded canvas 안에 갇혀 있다. Auto-regression은 무한히 펼칠 수 있지만 전역 상태를 들고 있어야 해서 결정성도 random access도 잃는다.

## InfiniteDiffusion — 셋을 다 가져온다

InfiniteDiffusion은 *임의의* diffusion 모델을 무한하고 논리적으로 무상태인 배열로 바꾼다. 좌표와 시드만 인덱스로 받고, 다음 속성을 한꺼번에 제공한다.

- **O(1) random access** — 멀리 떨어진 임의 위치를 즉시 가져온다.
- **결정성** — 호출 순서에 무관하게 같은 좌표와 시드면 같은 출력.
- **embarrassing parallelism** — 의존이 없어 병렬화가 자유롭다.
- **training-free** — 모델을 새로 학습시키지 않고 기존 모델 위에 얹는다.

내부에는 성능 최적화용 LRU 캐시만 있고, 외부에 노출되는 영구 상태는 없다.

이는 MultiDiffusion의 일반화이다. 기존 MultiDiffusion이 미리 정해진 bounded canvas 위에서 eagerly 동작하던 것을, 요청된 영역만 lazy하게 계산하도록 풀어낸 drop-in replacement다. 저자는 품질 면에서 MultiDiffusion 대비 손실이 거의 없다고 밝혔다.

![MultiDiffusion(위)과 InfiniteDiffusion(아래) 비교](/images/goslin-2026-infinite-diffusion-terrain/multidiffusion-vs-infinitediffusion.jpg)
*위: MultiDiffusion — 사전 정의된 bounded canvas 위에서 eagerly 생성. 아래: InfiniteDiffusion — 같은 모델을 unbounded하고 lazy한 생성으로 재구성. 출처: xandergos.github.io/terrain-diffusion*

### Auto-Regression과의 비교

원문에서 가장 또렷한 표는 두 unbounded 생성 패러다임을 직접 대조한 부분이다.

| 항목 | Auto-Regression | InfiniteDiffusion |
|---|---|---|
| Random Access | O(n) | O(1) |
| 결정성 | 없음 (순서 의존) | 있음 (순서 무관) |
| 오차 | 누적 (compound) | 누적 없음 |
| 병렬화 | 순차 | embarrassingly parallel |
| 상태 | 전역 | 함수적 무상태 |
| Training-free | 불가 | 가능 |

여섯 항목이 모두 InfiniteDiffusion 쪽으로 뒤집힌다. 같은 unbounded 문제를 *전역 상태 + 순차*가 아니라 *lazy + 함수적 무상태*로 다시 정의한 결과다.

## Terrain Diffusion — 지구 규모를 학습한 procedural generator

InfiniteDiffusion의 유용성을 보이려고 저자는 학습된 procedural terrain generator인 Terrain Diffusion을 함께 공개했다. 처음으로 학습 기반 절차적 지형 생성기를 표방한다.

핵심 설계는 셋이다.

1. **계층적 diffusion 모델 스택** — 행성 단위의 컨텍스트(대륙과 산맥)와 국소 디테일을 함께 묶기 위해 cascade 구조를 사용한다. 1024×1024 relief map 한 장이 100km 너비를 덮고, 그 위로 수백만 km² 대륙이 펼쳐진다.
2. **compact Laplacian encoding** — 마리아나 해구의 -10000m부터 에베레스트의 9000m까지의 거대한 dynamic range를 안정적으로 출력하기 위한 인코딩.
3. **무한 텐서 프레임워크** — 메모리 상한 없는 텐서를 상수 메모리로 다루는 오픈소스 라이브러리. 코드도 공개되어 있다.

성능은 *consumer GPU 한 장에서 궤도 속도(orbital velocity)의 9배*. 즉 인터랙티브 프레임레이트로 지표면 위를 9배 궤도 속도로 비행하면서 새 지형이 즉시 생성된다.

![Terrain Diffusion이 생성한 100km × 100km relief map 샘플](/images/goslin-2026-infinite-diffusion-terrain/terrain-01.jpg)
*Terrain Diffusion이 생성한 100km × 100km relief map. 출처: xandergos.github.io/terrain-diffusion*

![Terrain Diffusion이 생성한 또 다른 지형 샘플](/images/goslin-2026-infinite-diffusion-terrain/terrain-04.jpg)
*다른 시드로 생성한 지형. 출처: xandergos.github.io/terrain-diffusion*

## Minecraft mod로의 시연

Terrain Diffusion의 무상태이고 결정적인 속성은 게임 엔진에 자연스럽게 들어맞는다. 외부 의존 없이 시드 하나로 월드를 재현할 수 있고, 일관성을 깨지 않은 채 무한 텔레포트가 가능하며, 멀티플레이어에서도 같은 좌표는 누구에게나 같은 지형으로 나타난다.

저자는 이를 실제 Minecraft mod로 출시했다. 코드와 mod 모두 GitHub에 공개되어 있다.

- 코드: <https://github.com/xandergos/terrain-diffusion>
- Minecraft mod: <https://github.com/xandergos/terrain-diffusion-mc>

![Terrain Diffusion 기반 Minecraft mod 스크린샷](/images/goslin-2026-infinite-diffusion-terrain/minecraft-03.jpg)
*Terrain Diffusion으로 생성된 Minecraft 월드. 출처: xandergos.github.io/terrain-diffusion*

Unity 데모에서는 플레이어가 지표면 위를 궤도 속도의 3배로 편안하게 비행한다. 두 데모 영상은 프로젝트 페이지에서 직접 볼 수 있다.

## 가장 흥미롭게 본 대목

내가 곱씹은 대목은 *외부 상태 없음*이라는 단순한 조건이 만들어내는 결과의 폭이었다. auto-regression이 무한 캔버스를 풀 수 있었지만 전역 상태를 들고 다녀야 했기에 random access, 결정성, 병렬화, 드롭인 통합을 모두 잃은 반면, 같은 unbounded 문제를 *lazy + 무상태*로 다시 정의하니 6항목 비교표의 모든 칸이 한꺼번에 뒤집혔다.

또 하나는 training-free라는 점이다. 새 모델을 학습시키지 않고 *기존 diffusion 모델 위에 얹는* 알고리즘이라는 사실은, 이 접근이 terrain 너머의 어디까지 갈 수 있는지의 질문으로 이어진다. 텍스처, 재질, 바이옴, 해류, 날씨 — diffusion 모델이 다루는 어떤 도메인이라도 좌표와 시드를 인덱스로만 정의하면 같은 트릴레마 탈출이 가능해 보인다.

## 출처

- 저자: Alexander Goslin (Independent Researcher)
- 발표: SIGGRAPH 2026 Conference Papers — *InfiniteDiffusion: Bridging Learned Fidelity and Procedural Utility for Open-World Terrain Generation* (DOI: [10.1145/3799902.3811080](https://doi.org/10.1145/3799902.3811080))
- 프로젝트 페이지: <https://xandergos.github.io/terrain-diffusion/>
- 논문 PDF: <https://arxiv.org/abs/2512.08309>
- 저자 사이트: <http://alexandergoslin.me/>
