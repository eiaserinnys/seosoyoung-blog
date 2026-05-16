---
title: "SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer"
date: 2026-05-16T10:00:00+09:00
tags: ["AI", "비디오 생성", "월드 모델", "오픈소스", "아키텍처"]
categories: ["다이제스트"]
summary: "NVIDIA Labs가 공개한 2.6B 비디오 월드 모델 SANA-WM 프로젝트 페이지. 이미지 한 장과 카메라 궤적을 입력 받아 단일 H100에서 720p·1분 영상을 만든다고 주장한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. NVIDIA Labs가 공개한 2.6B 오픈소스 비디오 월드 모델 SANA-WM의 프로젝트 페이지다. 이미지 한 장과 카메라 궤적을 입력 받아 단일 H100에서 720p·1분짜리 영상을 생성한다고 주장한다.
2. 핵심 설계는 Hybrid Linear Diffusion Transformer다. 프레임 단위 Gated DeltaNet에 주기적 softmax 어텐션을 끼워 넣어, 모든 레이어를 softmax로 두면 60초 지점에서 OOM이 나는 문제를 회피한다.
3. citation 연도가 2026, arXiv ID가 비정상이라 본 논문은 아직 공개되지 않은 플레이스홀더 상태로 보인다. 페이지 본문도 짧고, 60초 14편·20초 18편·동일 첫 프레임 ABC 비교 8 scene으로 구성된 갤러리가 주력이다.

## 자료의 정체

SANA-WM은 NVIDIA Labs와 외부 공저자(Haoyi Zhu, Haozhe Liu, Yuyang Zhao, Tian Ye, Junsong Chen, Jincheng Yu, Tong He, Song Han, Enze Xie)가 공개한 비디오 월드 모델 프로젝트의 데모 페이지다. 풀 제목은 *SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer*.

페이지 인용에는 `arXiv:2605.15178`이라는 ID와 `year=2026`이 적혀 있다. 미래 연도에 비정상적인 arXiv 번호 조합이라 정식 논문이 공개되기 전 프로젝트 페이지만 먼저 띄운 상태로 추정된다. 본문 텍스트는 4줄짜리 hero bullet과 efficiency figure 1장, 그리고 60초·20초·ABC 비교 영상이 묶인 갤러리가 전부다.

## 네 가지 핵심 주장

페이지가 hero 섹션에서 내세우는 네 가지 클레임을 그대로 옮기면 다음과 같다.

### 1. Hybrid Linear Attention으로 1분 일관성

> Hybrid linear attention pairs frame-wise Gated DeltaNet with periodic softmax to hold a coherent world for a full minute.

프레임 단위 Gated DeltaNet 위에 주기적(periodic) softmax 어텐션을 끼워 넣는 하이브리드 백본이다. 모든 레이어를 softmax로 두면 H100 단일 GPU에서 60초 지점에 OOM이 나지만, 선형 어텐션 백본에 softmax를 간헐 삽입하면 메모리와 지연이 시간 길이에 따라 완만히 스케일링한다고 주장한다. 백본 크기는 2.6B.

### 2. 17B 2단계 long-video refiner

> A dedicated 17B long-video refiner sharpens texture, motion, and late-window quality on top of the long-rollout backbone.

2.6B 장기 롤아웃 백본 위에 17B 규모의 long-video refiner를 따로 두어 텍스처·모션·후반부(late-window) 품질을 보정한다. 페이지의 비교 슬라이더 라벨이 `Drag to compare stage 1 vs refined`로 두 단계가 분리되어 있음을 시사한다. 백본보다 refiner가 더 큰 비대칭 구성이 눈에 띈다.

### 3. 6-DoF 카메라 제어용 이중 분기

> A coarse global pose branch and a fine pixel-aligned geometric branch jointly follow metric camera paths with high fidelity.

coarse global pose 분기와 fine pixel-aligned geometric 분기를 함께 두어 미터 단위(metric) 카메라 경로를 추종한다. 페이지의 "Same First Frame, Different Paths" 섹션이 8 scene × 3 variant(A·B·C)로 동일한 첫 프레임에서 서로 다른 카메라 궤적을 주었을 때 결과 영상이 일관되게 분기되는 것을 시연한다.

### 4. 64 H100 학습, 단일 H100 추론

> 15 days on 64 H100s to train; a single H100 generates a one-minute 720p video at inference.

학습은 64 H100 × 15일, 추론은 단일 H100에서 1분 720p 영상 생성이라는 컴퓨트 클레임. 모델 크기 2.6B로 비교적 작은 오픈소스라는 점을 명시한다.

## Efficiency Figure

페이지가 제시하는 단 한 장의 그림은 다음이다.

![SANA-WM efficiency ablation and scaling](/images/sana-video-world-model/efficiency-latency-gpu.png)

> Efficiency ablation and scaling. (a) 60s single-GPU VAE/DiT latency by stage; bars are scaled for readability. (b) H100 latency and memory scaling: recurrent variants grow compactly, while all-softmax OOMs at 60s.

좌측은 60초 영상 단일 GPU 처리 시 VAE/DiT 변종별 단계별 지연을 비교한 ablation. 우측은 H100 기준 지연과 피크 메모리가 영상 길이에 따라 어떻게 증가하는지를 보여주는 스케일링 곡선이다. recurrent 변종은 완만히 커지는데 비해 all-softmax는 60초 지점에서 OOM이라는 것이 핵심 메시지.

## 데모 갤러리 구성

페이지의 절반 이상이 갤러리다. 구성은 다음과 같다.

- **Hero reel** 1편 — [`hero_reel_v8.mp4`](https://nvlabs.github.io/Sana/WM/videos/hero_reel_v8.mp4).
- **Long-form (60s)** 14편 — `long-1b`, `long-8a`, `long-9c`, `long-c06`, `long-c27`, `long-c29`, `long-8c`, `long-6a`, `long-gs10`, `long-on01`, `long-in10`, `long-on03`, `long-c10`, `long-2b`.
- **Short-form (20s)** 18편 — `short-6b` ~ `short-c13`.
- **Same First Frame, Different Paths** 8 scene × 3 variant = 24편 — `scene d4`, `c23`, `3b`, `c17`, `c18`, `8b`, `4b`, `2b`. 같은 첫 프레임에서 카메라 궤적 A/B/C만 바꾼 카메라 제어 데모.

프롬프트가 공개된 영상은 `1a`~`9c` 계열 19개뿐이다. `c`-prefix와 `gs`·`on`·`in`·`d` 계열은 caption이 없다. 공개된 19개 프롬프트는 모두 *1인칭 고정 시점 + 환경의 자율 운동(particles, fireflies, mist, swaying branches…)*이라는 동일한 템플릿을 따른다. 예컨대 `long-9c`의 프롬프트 일부는 다음과 같다.

> A first-person view from a strictly stationary observation point on a winding dirt path inside an enormous magical mushroom forest. ... There is no dynamic camera movement and no actions taken by the person recording. Autonomous motion animates the world: glowing spores drift, giant butterflies flap overhead, lantern flames flicker, dew trembles on leaves, and distant village lights shimmer.

카메라는 고정하고 세계만 자율적으로 움직이는 프롬프트로 통일한 것은, "월드 모델"이라는 컨셉을 가장 깔끔하게 보여주는 구성이라 의도된 선택으로 읽힌다. 카메라가 움직이는 사례는 별도의 ABC 비교 섹션에 따로 모아 두었다.

## 가장 흥미로운 지점

가장 인상 깊은 지점은 **백본(2.6B)보다 refiner(17B)가 크다**는 구성이다. 보통 다단계 비디오 디퓨전에서 base가 크고 refiner가 작아지는 방향이 일반적인데, SANA-WM은 그 반대다. 1분 일관성을 만들어내는 데에는 작은 선형 어텐션 백본으로 충분하고, "보는 맛"의 품질은 별도의 큰 refiner에 맡기는 분업이다. 이 분업이 실제로 1분 720p를 단일 H100에서 돌릴 수 있게 하는 핵심으로 보인다 — 백본은 메모리·지연을 완만히 늘리는 선형 어텐션이라 long-context에 강하고, refiner는 더 짧은 윈도우만 보정해도 되므로 모델 크기 17B의 비용이 영상 길이에 비례하지 않는다.

페이지가 본 논문 없이 데모만 먼저 띄운 점도 흥미롭다. citation에 박힌 `arXiv:2605.15178`은 정상 arXiv ID 형식(YYMM.NNNNN)으로 보면 2026년 5월 제출에 해당하지만, 실제로는 빈 자리다. 데모 영상의 완성도가 높고 4가지 클레임이 또렷한 만큼 본 논문 공개를 기다려볼 만하다.

## 출처

저자: Haoyi Zhu, Haozhe Liu, Yuyang Zhao, Tian Ye, Junsong Chen, Jincheng Yu, Tong He, Song Han, Enze Xie (NVIDIA Labs 외)
프로젝트 페이지: <https://nvlabs.github.io/Sana/WM/>
citation 표기: `arXiv:2605.15178` (2026) — 본 논문은 현재 미공개로 보이며 페이지의 placeholder citation으로 추정.
