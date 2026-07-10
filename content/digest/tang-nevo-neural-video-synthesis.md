---
title: "NEvo: Neural-Guided Evolutionary Video Synthesis for Dynamic Visual Selectivity"
date: 2026-07-10T13:30:00+09:00
tags: ["AI", "신경과학", "fMRI", "비디오 생성", "진화 알고리즘"]
categories: ["다이제스트"]
summary: "뇌의 특정 시각 피질을 가장 강하게 활성화할 2초짜리 영상을 진화 검색으로 만들어내는 EPFL·존스홉킨스의 프레임워크. 정적 이미지에 갇혀 있던 in silico 자극 합성을 동적 영상으로 확장한 첫 사례다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/tang-nevo-neural-video-synthesis/fig1.png"
images:
  - "/images/tang-nevo-neural-video-synthesis/fig1.png"
---

## 3줄 요약

1. EPFL NeuroAI 랩과 존스홉킨스가 2026년 7월 공개한 **NEvo**는 뇌 시각 피질의 특정 영역(FFA·PPA·MT·EBA·pSTS 등)을 가장 강하게 자극할 2초짜리 동영상을 진화 검색으로 만들어내는 프레임워크다. fMRI 인코딩 모델이 fitness 함수 역할을 한다.
2. 프롬프트 유전자 → 이미지 → 영상의 2단계 검색으로, 자연 영상 상위 **99.8%**, 손수 설계한 로컬라이저 영상의 **95.8%** 수준까지 예측 활성을 끌어올렸다. 그래디언트 기반 이전 방법(BrainDiVE)은 동적 세팅에서 자연 영상 평균의 24%까지밖에 도달하지 못했다.
3. 이 방법으로 측면 시각 경로(V1 → MT → EBA → pSTS → aSTS)를 훑으면 저수준 텍스처 → 신체 움직임 → 조율된 조인트 액션 → 얼굴 대 얼굴 사회적 접촉의 매끄러운 그라디언트가 자동으로 드러난다.

![Figure 1. NEvo 프레임워크 개요와 결과 요약](/images/tang-nevo-neural-video-synthesis/fig1.png)

## NEvo가 하는 일

인간의 시각 피질은 정적 이미지가 아니라 시간에 따라 흐르는 세계에 맞춰 진화했다. 그런데 지금까지 뇌 인코딩 모델을 이용해 "이 영역을 가장 강하게 자극할 자극"을 만들려는 시도(BrainDiVE 계열)는 거의 전부 정적 이미지에 머물러 있었다. 시공간 검색 공간이 훨씬 크고, 그래디언트 기반 생성이 영상에서 잘 작동하지 않았기 때문이다.

NEvo는 이 문제를 다른 각도로 우회한다. 그래디언트로 픽셀을 밀어붙이지 않고, **텍스트 프롬프트 공간에서 진화 검색**을 돈다.

- **프롬프트 공간**은 시각 속성 카테고리들의 데카르트 곱이다. 외모(주체·기분·조명), 동작(이벤트 구조·카메라 모션) 등 카테고리마다 사전 정의된 옵션 집합이 있고, 각 옵션을 하나씩 골라 유전자 시퀀스를 만든다.
- 이 시퀀스를 콤마로 이은 문장이 비디오 확산 모델에 입력되어 2초짜리 영상을 생성한다.
- 생성된 영상은 fMRI 인코딩 모델을 통과해 목표 ROI의 예측 활성값을 얻는다. 이 값이 fitness다.
- 세대마다 상위 30%가 부모로 선택되고, 크로스오버(비율 0.5)와 카테고리별 뮤테이션(비율 0.2)으로 자손이 생긴다. 개체군 크기는 20.

프롬프트가 유전자, 뇌 반응 예측치가 fitness, 세대별 자연선택으로 뇌를 자극할 영상을 "진화"시키는 셈이다. 저자들의 표현을 빌리면 이건 **뇌를 위한 프롬프트 엔지니어링**에 가깝다.

## 2단계 검색 — 이미지 먼저, 영상 나중

영상 검색 공간은 크다. 그래서 NEvo는 검색을 두 단계로 나눈다.

![Figure 2. 진화 프롬프팅과 2단계 검색 구조](/images/tang-nevo-neural-video-synthesis/fig2.png)

- **Stage 1 (이미지 검색)**: SDXL-Turbo로 이미지를 생성하고 목표 ROI의 예측 활성을 최대화한다. 기본 예산 400 evaluations.
- **Stage 2 (영상 검색)**: Stage 1에서 뽑힌 최고 이미지를 첫 프레임으로 두고, LTX-Video 0.9.8 13B distilled 모델로 image-to-video를 생성한다. 여기서 다시 200 evaluations의 진화 검색을 돌려 동적 프롬프트를 최적화한다.

이 분해는 단순히 계산량 절감을 위한 트릭이 아니다. Ablation에 따르면 FFA(얼굴 선택 영역) 같은 곳은 **먼저 얼굴이라는 외양 앵커를 확보한 뒤** 그 위에서 동작을 최적화해야 활성이 올라간다(+0.13 ± 0.04). 반면 MT처럼 애초에 모션에 반응하는 영역은 두 단계의 이득 차이가 작다(+0.09 ± 0.14). 영역마다 "정체성"이 앵커에서 오는지 동작에서 오는지가 갈린다는 이야기다.

## 어떤 부품을 어떻게 조립했는가

세 개의 프로즌 모델을 오케스트레이션한다. 세 모델 모두 학습시키지 않고 그대로 쓴다.

| 역할 | 기본 모델 |
|---|---|
| 인코더 (image/video → fMRI) | `epfl-neuroai/vjepa2-encoder-basic` (V-JEPA 2 다중 레이어) |
| Text → Image | `stabilityai/sdxl-turbo` |
| Image → Video | `Lightricks/LTX-Video-0.9.8-13B-distilled` |

인코더 선택은 결정적이다. 사회적 상호작용 fMRI 데이터셋으로 학습한 뒤 BOLDMoments에 out-of-distribution으로 테스트해보면 **V-JEPA 2 다중 레이어**가 CLIP 계열(단일·다중 레이어) 및 자기 자신의 last-layer 통제를 유의하게 상회한다. 시간에 근거한(temporally grounded) 비디오 표현이 필요하다는 방증이다.

기본 검색 하이퍼파라미터도 정리해 두면 다음과 같다.

| 항목 | 기본값 |
|---|---|
| 이미지 검색 evals | 400 |
| 영상 검색 evals | 200 |
| 개체군 크기 | 20 |
| 뮤테이션 비율 | 0.25 |
| 엘리트 비율 | 0.35 |
| 스코어 프레임 수 | 24 |
| 스코어 해상도 | 224 |

## 결과

![Figure 4. 2단계 검색 궤적과 각종 ablation](/images/tang-nevo-neural-video-synthesis/fig4.png)

- **활성 강도**: 여섯 개의 대표 ROI(FFA·PPA·EBA·MT·V3A·pSTS)에서 NEvo가 만들어낸 영상은 평균적으로 Moments-in-Time 자연 영상 상위 **99.8%**, 손수 설계된 dynamic localizer 영상의 **95.8%** 수준의 예측 활성을 기록했다.
- **동적 성분의 기여**: 최적화된 영상과 그 첫 프레임을 정지 영상으로 재생한 통제 조건을 비교하면, 모션 관련 영역인 **MT에서 +0.61 ± 0.05**, 얼굴 선택 영역인 **FFA에서도 +0.14 ± 0.02**의 개선이 있었다. 정지 이미지로는 놓쳤을 시간 구조가 FFA 같은 복측 영역에도 유의하게 기여한다는 뜻이다.
- **그래디언트 vs 진화**: 캐노니컬한 그래디언트 기반 방법인 BrainDiVE는 동적 세팅에서 자연 영상 평균의 **24%** 수준까지밖에 도달하지 못했다. NEvo는 모든 데이터 포인트에서 이를 상회했다.
- **검색 알고리즘 ablation**: Genetic search가 Random search를 유의하게 앞섰다(Cohen's d = 0.46, p < 0.001, paired bootstrap). Hill climbing도 이겼다.

## 측면 시각 경로의 사회-동적 위계

여기서부터가 이 논문이 발견 도구로서 힘을 발휘하는 대목이다.

![Figure 5. Lateral stream searchlight와 속성-활성 상관](/images/tang-nevo-neural-video-synthesis/fig5.png)

저자들은 V1에서 aSTS까지 측면 시각 경로를 따라 대뇌 피질 표면 위의 최단 경로(geodesic)로 서치라이트 궤적을 정의하고, 각 패치마다 NEvo로 최적 자극을 합성했다. 그 다음 Gemini-2.5-Flash에 각 자극을 한 문장으로 캡션 달게 하고, 캡션을 워드클라우드로 집약했다.

결과는 매끄러운 그라디언트다.

- 초기 시각(V1 부근, 패치 5, 10): "textured", "numerous", "red" 같은 저수준 텍스처 어휘가 지배한다.
- 중간 측면(패치 14, MT·EBA 인근): 신체와 동작 관련 어휘가 늘어난다.
- 후방(패치 18, 22, 24): "struggling", "dancing" 같은 조율된 조인트 상호작용 어휘가 등장한다.
- aSTS(패치 29): 얼굴 대 얼굴의 사회적 접촉 어휘로 쏠린다.

수치로도 확인된다. **MT는 biological motion 속성과 r = 0.84**, **pSTS는 joint action 속성과 r = 0.73**의 상관을 보인다(모두 p < 0.001). 합성 자극이 우연한 이상치가 아니라 각 영역의 기능적으로 특성적인 자극에 수렴한다는 이야기다.

## 추상 앵커에서 자란 뇌 자극

논문에서 가장 눈여겨본 것은 이 통제 실험이다.

![Figure 6. 추상 앵커(진흙 원반 두 개)에서 시작한 pSTS·MT 최적화 대비](/images/tang-nevo-neural-video-synthesis/fig6.png)

저자들은 첫 프레임을 **두 개의 쌓여 있는 plasticine 원반**이라는 비자연적 앵커로 고정하고, 여기서부터 pSTS 최적화와 MT 최적화를 각각 돌렸다.

- **pSTS를 겨냥한 최적화**는 얼굴 같은 특징과 조율된 상호작용이 자라났다. 진흙 덩어리에서 사회적 무언가가 자라난 것이다.
- **MT를 겨냥한 최적화**는 얼굴 없이 순수 모션 동역학이 자라났다.

같은 앵커에서 시작해도 목적 영역이 무엇이냐에 따라 자극이 갈라진다. 뇌 영역이 무엇을 "원하는지"를 강제로 표출시킨 셈이다.

## 갤러리 — 영역별 자극 예시

HuggingFace 갤러리에 각 ROI별 대표 자극이 GIF로 공개되어 있다. 정지 이미지로는 감이 오지 않으므로 여기 함께 걸어 둔다.

| FFA (얼굴) | MT (모션) |
|---|---|
| ![FFA gallery](/images/tang-nevo-neural-video-synthesis/ffa.gif) | ![MT gallery](/images/tang-nevo-neural-video-synthesis/mt.gif) |
| **EBA (신체)** | **pSTS (사회적 움직임)** |
| ![EBA gallery](/images/tang-nevo-neural-video-synthesis/eba.gif) | ![pSTS gallery](/images/tang-nevo-neural-video-synthesis/psts.gif) |

## 코드와 재현성

NEvo는 HuggingFace 커스텀 Diffusers 파이프라인으로 배포된다. 별도 GitHub 리포지토리 없이 HuggingFace 단일 채널이다.

```python
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained(
    "epfl-neuroai/NEvo",
    custom_pipeline="epfl-neuroai/NEvo",
    trust_remote_code=True,
)

out = pipe(roi="FFA", progress=True)
print(out.best_prompt, out.best_score)
```

한 줄로 팔로우업할 수 있다. 사용 가능한 명명 ROI는 `FFA`, `PPA`, `MT`, `EBA`, `LOC`, `RSC`, `pSTS`, `aSTS`, `V1`, `V2`, `V3`, `V4`이며, 반구별로 접미사(`FFA_lh`, `MT_rh`)를 붙일 수 있다. 서치라이트는 양반구 58개, 좌반구 28개, 우반구 30개가 준비되어 있다.

기본 파이프라인이 요구하는 것: CUDA GPU(13B 비디오 모델을 감당할 수 있는 메모리), fsaverage5 표면(20,484 vertex)에 맞춰진 인코더. 시드를 고정하면 비트 단위로 재현된다.

## 한계

논문 스스로 밝힌 한계는 세 가지다.

1. **인코더 편향이 자극에 새어들 수 있다.** 최적화가 특정 인코더의 아티팩트를 exploit할 수 있으므로 held-out 검증이 필요하다.
2. **비전 전용.** 오디오가 없어 aSTS처럼 음성·시청각 단서에 의존하는 영역의 특성 반영에는 취약하다.
3. **프롬프트 스키마 밖 차원은 놓칠 수 있다.** 구조화된 프롬프트 공간이 해석 가능성을 주는 대신, 사전 정의된 카테고리 밖 시각 차원은 검색할 수 없다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 두 개다.

첫째는 **그래디언트에서 진화로의 이동**이다. 이미지 도메인에서는 인코딩 모델의 그래디언트로 픽셀을 직접 최적화하는 BrainDiVE 계열이 정착돼 있었는데, 영상으로 넘어가는 순간 그 접근이 무너진다. 자연 영상 평균의 24%까지밖에 못 간다. 그런데 프롬프트 공간에서 진화 검색으로 우회하니 곧바로 상위 99.8%에 도달한다. 검색 공간이 커질수록 "부드러운 그래디언트"보다 "의미론적으로 유효한 이산 후보들 사이의 자연선택"이 유리해진다는 신호가 아닐까 싶다. 이 관측은 LLM 프롬프트 엔지니어링·에이전트 검색 문제와도 결이 닿는다.

둘째는 <strong>진흙 덩어리에서 얼굴이 자라나는 실험(Fig. 6)</strong>이다. 이건 뇌 자극 합성이라는 도구가 단순히 "이 영역이 잘 반응하는 예쁜 자극을 만든다"에 그치지 않고, **가설을 강제로 관찰 가능한 자극으로 육화**시키는 도구가 될 수 있다는 걸 보여준다. pSTS가 진흙 두 덩이에서 얼굴을 끌어당긴다면, 그건 pSTS가 어떤 시각 통계에 "사회성"을 부여하는지에 대한 강한 검증 가능한 가설이 된다. 다음 단계인 closed-loop fMRI 실험에서 이 가설이 실제 사람 뇌에서도 유지되는지 볼 수 있게 되는 것이다.

## 출처

- Tang, Y., Salehi, S., Zhou, M., Zamir, A., Isik, L., & Schrimpf, M. (2026). *NEvo: Neural-Guided Evolutionary Video Synthesis for Dynamic Visual Selectivity*. arXiv:2607.02317.
- 소속: EPFL NeuroAI Lab, Johns Hopkins University
- 프로젝트 사이트: <https://nevo-project.epfl.ch/>
- 논문: <https://arxiv.org/abs/2607.02317>
- 코드·모델(HuggingFace): <https://huggingface.co/epfl-neuroai/NEvo>
