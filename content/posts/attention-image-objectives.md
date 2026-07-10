---
title: "눈길을 끄는 이미지는 하나의 문제가 아니다"
date: 2026-07-10T15:40:00+09:00
tags: ["AI", "컴퓨터 비전", "어텐션", "CTR", "이미지 생성", "에디토리얼"]
categories: ["인사이트"]
summary: "눈길을 끄는 이미지를 예측하고 만드는 연구는 한 덩어리처럼 보이지만 시선과 기억, 미감, 클릭 네 갈래로 갈라져 있다. 그중 예쁨과 클릭은 산업 데이터가 이미 갈라놓은 서로 다른 목적함수다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/attention-image-objectives/01-cover.png"
images:
  - "/images/attention-image-objectives/01-cover.png"
---

눈길을 끄는 이미지를 예측하고 만드는 연구는 한 덩어리처럼 보이지만, 실은 네 갈래로 갈라져 있다. 사람의 어떤 반응을 목표로 두느냐, 시선인가 기억인가 미감인가 클릭인가에 따라 서로 다른 학문이 대응된다. 그리고 그중 예쁨과 클릭은 산업 데이터가 이미 갈라놓은 서로 다른 목적함수다.

## 시작은 뇌였다

이 글은 윗분이 던진 다이제스트 요청에서 흘러나왔다. 뇌 반응으로 영상을 생성하는 논문 하나를 정리했더니, 그렇다면 이걸로 눈길을 끄는 영상을 만들 수 있느냐는 물음이 돌아왔다. 그 물음을 좇다 보니 이미지 도메인 전체의 지형을 훑게 됐다.

발단은 EPFL의 <strong>NEvo</strong>다. fMRI 인코더를 점수 함수로 두고, 진화 검색으로 "특정 뇌 영역을 가장 크게 흔드는 2초짜리 영상"을 생성해낸다. 얼굴 영역(FFA)을 겨냥하면 정면 클로즈업이 자라나고, 사람 사이 상호작용을 읽는 영역(pSTS)을 겨냥하면 두 형체가 마주 보는 장면이 자라난다. 진흙 원반 두 개에서 시작해 얼굴이 돋아나는 통제 실험까지 있다.{{< sn >}}NEvo(Neural Encoding-guided Video Optimization). 생성기로 SDXL-Turbo와 LTX-Video를 쓰고, V-JEPA 2 다중 레이어 인코더로 시각 피질 반응을 예측해 이를 fitness로 진화 검색을 돌린다. 프로젝트 페이지: [nevo-project.epfl.ch](https://nevo-project.epfl.ch/) (EPFL, 2026).{{< /sn >}}

<figure>
<div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;">
  <video autoplay loop muted playsinline style="width:47%;min-width:220px;max-width:300px;border-radius:8px;">
    <source src="/images/attention-image-objectives/nevo_FFA_vid01.mp4" type="video/mp4">
  </video>
  <video autoplay loop muted playsinline style="width:47%;min-width:220px;max-width:300px;border-radius:8px;">
    <source src="/images/attention-image-objectives/nevo_pSTS_vid01.mp4" type="video/mp4">
  </video>
</div>
<figcaption>NEvo가 뇌 영역별로 최적화해 생성한 2초짜리 자극. 왼쪽은 얼굴 영역(FFA)을 겨냥한 결과로 얼굴과 눈이 두드러지고, 오른쪽은 사회적 상호작용을 읽는 영역(pSTS)을 겨냥한 결과로 형체들이 서로 얽히는 장면이 나온다. 출처: <a href="https://nevo-project.epfl.ch/">NEvo</a> (EPFL, 2026).</figcaption>
</figure>

여기서 자연스러운 물음이 따라온다. 그렇다면 이걸로 눈길을 끄는 숏츠를 만들 수 있을까. 답은 곧바로는 어렵다는 쪽이었다. NEvo가 최적화하는 대상은 시청 유지율이나 좋아요 같은 창작 지표가 아니라 뇌 피질의 활성이고, 산출물도 콘텐츠가 아니라 512×512 지각 실험용 자극이며, 쓰이는 인코더가 예측하는 것 역시 참여도와 무관한 시각 피질 반응이다. 셋 다 콘텐츠 제작과는 목적이 어긋나 있다.

그럼에도 버릴 수 없는 골격이 하나 남는다. <strong>타겟을 정하고, 그것을 점수화하는 인코더를 fitness로 두고, 생성 프롬프트 공간을 진화 검색으로 뒤진다</strong>는 삼단 구조다. 뇌를 목표로 두지 않아도 이 틀은 성립한다. 그래서 눈을 정지 이미지 쪽으로 돌렸다. 동영상보다 학술이 훨씬 두터울 것이라는 짐작이 있었고, 결과는 짐작보다 두터웠다.

## 네 갈래의 지형

"눈길을 끄는 이미지"라는 한 마디를 풀어 보면, 실제로는 사람의 서로 다른 반응 네 가지를 겨냥하는 별개의 연구 전통이 나온다. 시선이 어디로 가는가, 뇌에 남는가, 보기에 좋은가, 정말 손가락이 눌리는가. 각 물음마다 시조 논문과 현재 최전선, 성숙도가 뚜렷하게 다르다.

| 갈래 | 겨냥하는 반응 | 시조 | 현재 최전선 | 상태 |
|---|---|---|---|---|
| Saliency (시선) | 시선이 어디로 향하는가 | Itti, Koch, Niebur (1998) | DeepGaze MSDB (2025) | 성숙, 산업화 |
| Memorability (기억) | 뇌에 남는가 | Isola 외 (2011) | ResMem (2021) | 포화, 이식 공백 |
| Aesthetic (미감) | 미적으로 좋은가 | Datta 외 (2006) | Q-Align (2024) | 성숙, 편향 논쟁 |
| CTR (클릭) | 실제로 클릭하는가 | Chen 외 (2016) | JD CAIG (2025) | 학술 얇음, 산업 선행 |

<figure>
<svg viewBox="0 0 760 210" role="img" aria-label="저수준 지각에서 행동 결과로 향하는 네 갈래의 배치" style="width:100%;height:auto;font-family:inherit;">
  <defs><marker id="ar" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor" fill-opacity="0.5"></path></marker></defs>
  <line x1="40" y1="172" x2="720" y2="172" stroke="currentColor" stroke-opacity="0.3" stroke-width="2" marker-end="url(#ar)"></line>
  <text x="40" y="196" fill="currentColor" fill-opacity="0.6" font-size="13">저수준 지각</text>
  <text x="720" y="196" text-anchor="end" fill="currentColor" fill-opacity="0.6" font-size="13">행동과 수익 결과</text>
  <g>
    <rect x="40" y="44" width="150" height="96" rx="8" fill="rgba(59,110,219,0.16)" stroke="#5b8def" stroke-opacity="0.5"></rect>
    <text x="115" y="78" text-anchor="middle" fill="currentColor" font-weight="700" font-size="15">Saliency</text>
    <text x="115" y="100" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="13">시선</text>
    <text x="115" y="120" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="12">AUC 0.894</text>
    <rect x="210" y="44" width="150" height="96" rx="8" fill="rgba(127,127,127,0.12)" stroke="currentColor" stroke-opacity="0.25"></rect>
    <text x="285" y="78" text-anchor="middle" fill="currentColor" font-weight="700" font-size="15">Memorability</text>
    <text x="285" y="100" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="13">기억</text>
    <text x="285" y="120" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="12">ρ 0.68</text>
    <rect x="380" y="44" width="150" height="96" rx="8" fill="rgba(127,127,127,0.12)" stroke="currentColor" stroke-opacity="0.25"></rect>
    <text x="455" y="78" text-anchor="middle" fill="currentColor" font-weight="700" font-size="15">Aesthetic</text>
    <text x="455" y="100" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="13">미감</text>
    <text x="455" y="120" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="12">AVA / LAION</text>
    <rect x="550" y="44" width="170" height="96" rx="8" fill="rgba(180,83,26,0.16)" stroke="#c8763a" stroke-opacity="0.55"></rect>
    <text x="635" y="78" text-anchor="middle" fill="currentColor" font-weight="700" font-size="15">CTR</text>
    <text x="635" y="100" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="13">클릭</text>
    <text x="635" y="120" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="12">별도 목적함수</text>
  </g>
</svg>
<figcaption>네 갈래는 저수준 지각에서 행동 결과로 이어지는 스펙트럼 위에 놓인다. 왼쪽으로 갈수록 예측이 성숙했고, 오른쪽으로 갈수록 학술은 얇아지고 산업이 앞선다.</figcaption>
</figure>

## 갈래별로 무엇이 밝혀졌나

### 1. Saliency: 시선이 어디로 향하는가

가장 오래되고 가장 산업화된 갈래다. Itti, Koch, Niebur(1998)가 색과 명도, 방향 같은 저수준 특징을 다중 스케일로 합쳐 위상적 시선 지도를 만든 골격이 20년간 기준이었다. SALICON(2015)이 마우스 트래킹 1만 장으로 딥러닝 시대를 열었고, 튀빙겐의 DeepGaze 계열이 정착했다. 최신 SOTA인 <strong>DeepGaze MSDB</strong>(2025)는 CLIP과 DINOv2 피처를 결합해 MIT300 벤치마크에서 AUC 0.894까지 올라, 인간 상한(약 0.92)에 바짝 다가섰다.{{< sn >}}자유 응시 조건의 MIT300/MIT1003 벤치마크 기준. 인간 사이 일치도 상한이 약 0.92로 알려져 있다. 다중 데이터셋 시선 예측 모델, [arXiv:2505.10169](https://arxiv.org/abs/2505.10169) (2025).{{< /sn >}} 구글이 주도한 <strong>UniAR</strong>(2024)은 시선과 스캔패스, 미감, 좋아요를 하나의 모델로 통합 예측하며 지금의 최전선을 보여준다.{{< sn >}}UniAR: Unifying Human Attention and Response. [arXiv:2312.10175](https://arxiv.org/abs/2312.10175), NeurIPS 2024.{{< /sn >}}

<figure>
<img src="/images/attention-image-objectives/saliency-uniar-overlay.png" alt="이미지 위에 시선 히트맵을 겹쳐 예측 결과를 실측과 대비한 예시" style="width:100%;border-radius:8px;">
<figcaption>한 장의 이미지에서 사람의 시선이 어디로 쏠리는지 예측한 결과. 초록 테두리가 실제 시선, 주황 테두리가 모델 예측이다. 거리 사진부터 웹페이지, 영화 포스터까지 도메인을 가리지 않고 예측한다. 출처: UniAR (NeurIPS 2024), Fig. 2.</figcaption>
</figure>

산업 응용도 이 갈래에 몰려 있다. Neurons Inc, Attention Insight, 3M VAS가 내세우는 시선 히트맵 서비스와 "95% 정확도" 주장은 대부분 MIT와 튀빙겐 벤치마크에 뿌리를 둔다. 정작 성숙한 것은 자유 응시 조건이고, 무언가를 찾거나 읽는 태스크 응시와 시선 이동 순서(스캔패스)는 아직 덜 여물었다.

<figure>
<img src="/images/attention-image-objectives/saliency-msdb-architecture.png" alt="현대 시선 예측 파이프라인의 구조도" style="width:100%;border-radius:8px;">
<figcaption>현대 시선 예측 파이프라인의 구조. 입력 이미지에서 CLIP과 DINOv2의 다중 스케일 특징을 뽑아 읽어낸 뒤, centerbias와 blur를 거쳐 시선 밀도 지도를 낸다. 출처: 다중 데이터셋 시선 예측 모델 (arXiv:2505.10169, 2025).</figcaption>
</figure>

### 2. Memorability: 뇌에 남는가

이 갈래를 지탱하는 발견 하나가 있다. Isola 외(2011)의 "What Makes an Image Memorable?"는 <strong>기억성이 개인차가 아니라 이미지에 내재한 고유 속성</strong>임을 보였다. 서로 다른 관찰자 집단이 어떤 이미지를 기억하는지가 Spearman 0.68에서 0.83으로 일치한다.{{< sn >}}관찰자 집단을 둘로 나눠 각각의 기억성 순위를 비교했을 때의 일치도. 색이나 밝기처럼 이미지에 내재해 계산 가능한 성질이라는 근거가 됐다. Isola 외, What Makes an Image Memorable? (CVPR 2011).{{< /sn >}} 색이나 밝기처럼 계산 가능한 이미지의 성질이라는 뜻이다. Khosla 외(2015)가 LaMem 6만 장으로 확장했고, ResMem(2021)이 Spearman 0.679로 인간 상한에 도달하며 예측 자체는 포화됐다.

<figure>
<img src="/images/attention-image-objectives/mem-isola-memorability-map.png" alt="이미지 안에서 기억을 끌어올리는 영역과 잊히게 하는 영역을 표시한 기억성 지도" style="width:100%;border-radius:8px;">
<figcaption>이미지 안에서 어느 영역이 기억을 끌어올리고(빨강) 어느 영역이 잊히게 하는지(파랑) 나타낸 기억성 지도. 기억은 관찰자 개인이 아니라 이미지의 어느 부분에 담겨 있는지를 보여준다. 출처: Isola 외, What Makes an Image Memorable? (CVPR 2011), Fig. 7.</figcaption>
</figure>

2024년부터 연구 에너지는 "왜 기억되는가"로 넘어갔다. Nature Human Behaviour(2024)는 재구성이 어려운 시각 표상을 가진 이미지일수록 기억 흔적이 강하다는 계산 이론을 제시했다.{{< sn >}}Images with harder-to-reconstruct visual representations leave stronger memory traces. Nature Human Behaviour (2024), [PubMed 38740989](https://pubmed.ncbi.nlm.nih.gov/38740989/).{{< /sn >}} 기억성은 뇌 신호와도 연결된다. 하측두피질 집단 반응이 기억성을 예측하고, 고기억성 이미지에서 ERP의 N300, N400 진폭이 낮아진다(더 효율적인 처리).

<figure>
<img src="/images/attention-image-objectives/mem-ganalyze-sequence.png" alt="생성 이미지를 기억성과 미감, 감정가가 높아지도록 변형한 시퀀스" style="width:100%;border-radius:8px;">
<figcaption>생성 이미지를 왼쪽에서 오른쪽으로 갈수록 기억성(또는 미감, 감정가)이 높아지도록 변형한 시퀀스. 강아지는 0.58에서 0.77로, 피망은 0.58에서 0.92로 기억성 점수가 오른다. 뒤에서 볼 "점수를 fitness로 둔 최적화" 골격의 원형이다. 출처: Goetschalckx 외, GANalyze (ICCV 2019), Fig. 1.</figcaption>
</figure>

### 3. Aesthetic: 미적으로 좋은가

Datta와 Ke(2006)가 열고 AVA 데이터셋(2012, 25만 장에 5,500만 평점)이 표준을 세웠다. NIMA(2018)가 평점 분포를 예측하는 아이디어로 IQA 표준을 만들었지만, 실질적 영향력이 가장 큰 물건은 <strong>LAION-Aesthetics Predictor V2</strong>(2022)다. CLIP 임베딩에 선형 레이어 하나를 얹은 소박한 구조인데, 이것이 LAION-5B 필터링을 거치며 <strong>Stable Diffusion의 "예쁨 편향"의 근원</strong>이 됐다.{{< sn >}}CLIP 임베딩을 선형 레이어로 1~10점에 매핑하는 단순 예측기. LAION-5B의 미적 필터링에 쓰여 생성 모델의 톤 편향으로 이어졌다. [improved-aesthetic-predictor](https://github.com/christophschuhmann/improved-aesthetic-predictor) (Schuhmann, 2022).{{< /sn >}} 지금 SD 생성물이 특정 톤에 쏠리는 이유가 이 예측기의 라벨 분포에 있다.

<figure>
<img src="/images/attention-image-objectives/aes-nima-ava-ranking.png" alt="풍경 사진을 NIMA 예측 미감 점수 순으로 늘어놓은 결과" style="width:100%;border-radius:8px;">
<figcaption>같은 소재의 풍경 사진 15장을 NIMA가 매긴 예측 미감 점수 순으로 늘어놓은 결과. 사진마다 예측 점수가 붙어 6.38에서 3.55까지 내려간다. 미감을 숫자로 매기는 일이 실제로 가능함을 보여준다. 출처: Talebi &amp; Milanfar, NIMA (2018), Fig. 10.</figcaption>
</figure>

최근(2023~2026)은 언어와 비전 결합 쪽으로 넘어갔다. CLIP-IQA(2023)는 "고품질 대 저품질" 반의어 프롬프트의 softmax를 점수로 쓰고, Q-Align(2024)은 연속 점수 회귀 대신 Bad~Excellent 이산 레벨로 파인튜닝하는 편이 인간 평가와 더 맞는다는 걸 보였다.{{< sn >}}Q-Align: Teaching LMMs for Visual Scoring via Discrete Text-Defined Levels. [arXiv:2312.17090](https://arxiv.org/abs/2312.17090), ICML 2024.{{< /sn >}} 한편 FAccT 2026 감사 연구는 LAION 예측기의 서구권 스톡사진 편향과 특정 집단 이미지 필터링을 실증하며, 규범적 미적 척도 대신 다원적 평가를 요구했다.

<figure>
<img src="/images/attention-image-objectives/aes-qalign-levels.png" alt="텍스트 레벨 기반으로 미감을 학습시키는 Q-Align 도식" style="width:100%;border-radius:8px;">
<figcaption>연속 점수를 회귀하는 대신 bad, poor, fair, good, excellent 같은 텍스트 레벨로 학습시키는 Q-Align의 도식. 사람이 실제로 품질을 매기는 방식에 더 가깝고, 그 편이 인간 평가와 잘 맞았다. 출처: Wu 외, Q-Align (ICML 2024), Fig. 3.</figcaption>
</figure>

### 4. Thumbnail과 CTR: 실제로 클릭하는가

이 갈래만 성격이 완전히 다르다. 학술 문헌은 얇고 산업이 훨씬 앞서 있다. 출발은 Chen 외(상하이교통대와 알리바바, 2016)로, 노출 레코드 5,000만 건 이상에서 raw 픽셀만으로 CNN이 CTR을 end-to-end로 예측할 수 있음을 초기에 실증했다. 앞의 세 갈래가 "사람이 무엇을 보고 느끼는가"를 겨냥한다면, 이 갈래는 그 끝에 있는 "손가락이 정말 눌리는가"를 겨냥한다. 그리고 그 목표를 세우는 순간, 앞의 세 갈래가 쌓아 온 미감과 기억, 시선 예측이 곧바로 정답이 되지는 않는다. 이 갈래는 아래에서 더 깊이 다룬다.

## 되풀이되는 골격

가장 흥미로운 대목은 여기다. NEvo가 보여준 삼단 구조, "생성기를 두고, 점수화 인코더를 fitness로 삼아, 탐색으로 출력을 최적화한다"는 틀은 이미지 도메인에 <strong>2019년부터 존재</strong>했다. NEvo는 동영상판일 뿐, 방법론적 조상은 이미 있었다.

| 프레임워크 | 도메인 | 생성기 | 탐색 | Fitness |
|---|---|---|---|---|
| NEvo (2026) | 동영상 | SDXL-Turbo + LTX-Video | 진화 탐색(GA) | fMRI 인코딩 |
| BrainDiVE (2023) | 정지 이미지 | Latent Diffusion | 그래디언트 | fMRI 인코딩 |
| GANalyze (2019) | 정지 이미지 | BigGAN | 그래디언트 | MemNet / 미감 |
| EvoGen (2022) | 정지 이미지 | Stable Diffusion | GA(텍스트 프롬프트) | 미감 |

<figure>
<svg viewBox="0 0 720 210" role="img" aria-label="타겟, 생성기, 점수 인코더, 탐색으로 이어지는 최적화 루프" style="width:100%;height:auto;font-family:inherit;">
  <defs><marker id="ar2" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#5b8def"></path></marker></defs>
  <rect x="30" y="80" width="130" height="56" rx="8" fill="rgba(59,110,219,0.16)" stroke="#5b8def" stroke-opacity="0.5"></rect>
  <text x="95" y="104" text-anchor="middle" fill="currentColor" font-weight="700" font-size="14">타겟 지정</text>
  <text x="95" y="122" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="12">뇌영역, 미감, CTR</text>
  <rect x="210" y="80" width="130" height="56" rx="8" fill="rgba(127,127,127,0.12)" stroke="currentColor" stroke-opacity="0.25"></rect>
  <text x="275" y="104" text-anchor="middle" fill="currentColor" font-weight="700" font-size="14">생성기</text>
  <text x="275" y="122" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="12">Diffusion / GAN</text>
  <rect x="390" y="80" width="130" height="56" rx="8" fill="rgba(127,127,127,0.12)" stroke="currentColor" stroke-opacity="0.25"></rect>
  <text x="455" y="104" text-anchor="middle" fill="currentColor" font-weight="700" font-size="14">점수 인코더</text>
  <text x="455" y="122" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="12">fitness</text>
  <rect x="570" y="80" width="130" height="56" rx="8" fill="rgba(59,110,219,0.16)" stroke="#5b8def" stroke-opacity="0.5"></rect>
  <text x="635" y="104" text-anchor="middle" fill="currentColor" font-weight="700" font-size="14">탐색</text>
  <text x="635" y="122" text-anchor="middle" fill="currentColor" fill-opacity="0.65" font-size="12">진화 / 그래디언트</text>
  <g stroke="#5b8def" stroke-width="2.5" marker-end="url(#ar2)" fill="none">
    <line x1="160" y1="108" x2="205" y2="108"></line>
    <line x1="340" y1="108" x2="385" y2="108"></line>
    <line x1="520" y1="108" x2="565" y2="108"></line>
    <path d="M 635 136 L 635 176 L 275 176 L 275 141"></path>
  </g>
  <text x="455" y="196" text-anchor="middle" fill="currentColor" fill-opacity="0.6" font-size="12">점수가 높아지는 방향으로 프롬프트를 되먹임</text>
</svg>
<figcaption>점수원만 바꾸면 뇌 반응이든 기억성이든 클릭률이든 같은 루프가 돈다. GANalyze(2019)가 NEvo와 구조적으로 가장 닮은 조상이고, BrainDiVE는 NEvo가 직접 baseline으로 삼은 정지 이미지 그래디언트 버전이다.</figcaption>
</figure>

두 가지가 눈에 걸린다. 첫째, GANalyze(MIT, 2019)는 BigGAN의 잠재 공간에서 MemNet 점수를 높이는 방향 벡터를 찾아 이미지의 기억성을 실제로 끌어올렸고 행동 실험까지 마쳤다.{{< sn >}}Goetschalckx 외, GANalyze: Toward Visual Definitions of Cognitive Image Properties. [arXiv:1906.10112](https://arxiv.org/abs/1906.10112), ICCV 2019.{{< /sn >}} "점수원을 fitness로 두고 생성기 출력을 최적화한다"는 골격이 NEvo와 같고, 대상이 정지 이미지와 그래디언트라는 점만 다르다. 둘째, NEvo 논문의 발견 중 하나였던 "동영상에서는 그래디언트가 무너지고 진화 검색이 이긴다"는 결론은, 정지 이미지의 BrainDiVE(그래디언트)와의 대비에서 나온 실증이다.

## 클릭이라는 목적함수

넷 중에서 아마도 가장 관심이 많은 갈래는 CTR에 대한 연구일 것 같다. 네 갈래 중 CTR만 유독 성격이 다르기도 하고. 나머지 셋은 대학 실험실에서 벤치마크를 놓고 겨루지만, 이 갈래의 최전선은 광고와 커머스 플랫폼의 A/B 테스트 로그에 있다.

그래서 논문의 저자 목록에 알리바바, 텐센트, JD, Shopee, 메르카리 같은 이름이 붙는다. 그들이 던지는 질문은 하나로 모인다. 사람이 무엇을 예쁘다고 느끼는가와, 사람이 무엇을 누르는가는 같은 문제인가.

<figure>
<img src="/images/attention-image-objectives/jd-ctr-fig1-motivation.png" alt="같은 상품이라도 배경 연출에 따라 CTR이 달라지는 사례와 CTR 최적화 전후 비교" style="width:100%;border-radius:8px;">
<figcaption>같은 물병, 같은 의자인데 배경 연출만 바꾸면 예측 CTR이 0.013에서 0.023으로, 0.009에서 0.017로 벌어진다(왼쪽). 오른쪽은 CTR 기반 최적화 전후의 생성 이미지 비교다. 상품은 그대로인데 무엇이 클릭을 가르는지 한 장으로 보여준다. 출처: Xingye Chen 외, CAIG (WWW 2025), Fig. 1.</figcaption>
</figure>

### 클릭을 목적함수로 삼으면 무엇이 달라지나

JD의 <strong>CAIG</strong>(WWW 2025)가 이 갈래의 선언문이다. 논문은 상품 배경 생성이 "주로 미적 품질에 초점을 맞추는데, 이것이 만족스러운 온라인 성능으로 이어지지 않을 수 있다"고 적는다.{{< sn >}}"Most existing methods ... primarily focus on the aesthetic quality, which may fail to achieve satisfactory online performance." CTR-Driven Advertising Image Generation with MLLMs (CAIG), [arXiv:2502.06823](https://arxiv.org/abs/2502.06823), WWW 2025. 단정이 아니라 "may fail"이라는 조건부 표현임에 유의.{{< /sn >}} 단정이 아니라 조건부 경고라는 점이 오히려 무겁다. 해법으로 이커머스 지식을 사전학습한 MLLM에 CTR 예측을 보상으로 붙이고, 상품과 배경의 어긋남을 줄이는 선호 최적화(PCPO)를 돌린다. 그 결과 상품과 배경의 매치율이 표준 DPO의 59.7%에서 79.8%로 올랐다.

더 앞선 증언은 Shopee의 <strong>CG4CTR</strong>(WWW 2024)에 있다. Stable Diffusion inpainting에 프롬프트 모델과 보상 모델을 물려 스스로 반복 개선하는 자기순환 구조인데, 반복을 한 번만 돌리면 온라인 CTR이 4.2% 오르고 열 번 돌리면 10.4%까지 오른다. 매출은 9.7% 늘었다.{{< sn >}}자기순환(self-cyclic) 반복 횟수에 따라 오프라인과 온라인 성과가 함께 올랐다. CG4CTR, [arXiv:2401.10934](https://arxiv.org/abs/2401.10934), WWW 2024 Companion (Shopee). 논문은 CTR을 목표로 삼지 않은 생성물이 "노출을 희석해 온라인 성과를 직접 악화시킨다"고 적는다.{{< /sn >}} 논문은 CTR을 목표로 삼지 않은 생성물이 노출을 희석해 온라인 성과를 직접 악화시킨다고 못 박는다. 미감만 좇은 이미지가 그냥 무해한 것이 아니라 지표를 갉아먹는다는 얘기다.

<div style="display:flex;flex-wrap:wrap;gap:12px;margin:1.2em 0;">
  <div style="flex:1 1 150px;border:1px solid rgba(127,127,127,0.3);border-radius:8px;padding:14px;"><div style="font-size:1.5rem;font-weight:700;">+10.4%</div><div style="opacity:0.65;font-size:0.85rem;">CG4CTR 온라인 CTR 리프트(자기순환 10회, Shopee)</div></div>
  <div style="flex:1 1 150px;border:1px solid rgba(127,127,127,0.3);border-radius:8px;padding:14px;"><div style="font-size:1.5rem;font-weight:700;">+9.7%</div><div style="opacity:0.65;font-size:0.85rem;">같은 실험의 매출 리프트</div></div>
  <div style="flex:1 1 150px;border:1px solid rgba(127,127,127,0.3);border-radius:8px;padding:14px;"><div style="font-size:1.5rem;font-weight:700;">79.8%</div><div style="opacity:0.65;font-size:0.85rem;">JD PCPO 상품과 배경 매치율(표준 DPO 59.7%)</div></div>
</div>

<figure>
<img src="/images/attention-image-objectives/jd-ctr-fig2-pipeline.png" alt="CTR 신호로 광고 이미지 생성을 최적화하는 CAIG 파이프라인 개요" style="width:100%;border-radius:8px;">
<figcaption>CTR 신호로 광고 이미지 생성을 최적화하는 CAIG 파이프라인. 이커머스 지식 사전학습 MLLM이 CTR 보상 모델의 신호를 받아 프롬프트와 배경 생성을 함께 밀어 올린다. 앞에서 본 NEvo의 골격(타겟, 점수 인코더, 탐색)이 커머스 언어로 그대로 반복된다. 출처: Xingye Chen 외, CAIG (WWW 2025), Fig. 2.</figcaption>
</figure>

### 얼굴, 미소, 그리고 시선의 방향

클릭을 움직이는 구체적 요소로 학술이 반복해서 지목하는 것은 얼굴이다. Bakhshi 외의 "Faces Engage Us"(CHI 2014)는 인스타그램 사진 110만 장에서 얼굴이 담긴 사진이 좋아요를 38%, 댓글을 32% 더 받는다는 것을 보였다(얼굴의 수나 나이, 성별과는 무관했다).{{< sn >}}Bakhshi, Shamma, Gilbert, Faces Engage Us: Photos with Faces Attract More Likes and Comments on Instagram. CHI 2014.{{< /sn >}} 앨버타대와 텐센트가 함께 낸 <strong>AdSEE</strong>(KDD 2023)는 여기서 한 걸음 더 나가, StyleGAN2로 광고 속 얼굴의 잠재 코드를 편집하며 어떤 방향이 예측 클릭률을 올리는지 측정했다. 상위 방향은 미소, 얼굴을 살짝 아래로 향한 각도(시선이 아니라 머리 각도다), 여성적 특징이었다.{{< sn >}}QQ-AD 데이터셋에서 얼굴을 포함한 광고 2만여 건을 분석. QQ 브라우저에서 편집본 250개와 대조군 250개를 5일간 A/B로 비교해 유의미한 차이를 확인(p=3.68×10⁻⁵). 다만 헤드라인 리프트 수치는 논문에 명시되지 않았다. AdSEE, [arXiv:2309.08159](https://arxiv.org/abs/2309.08159), KDD 2023.{{< /sn >}}

<figure>
<img src="/images/attention-image-objectives/adsee-fig7-before-after.png" alt="AdSEE가 얼굴 속성을 편집해 광고 매력도를 높인 전후 예시" style="width:100%;border-radius:8px;">
<figcaption>AdSEE가 얼굴 속성을 편집한 전(왼쪽)과 후(오른쪽). 표정과 각도를 미세하게 옮기는 것만으로 광고 이미지의 예측 클릭률이 달라진다. 출처: Liyao Jiang 외, AdSEE (KDD 2023), Fig. 7.</figcaption>
</figure>

흥미로운 수렴이 하나 있다. 소비자 심리학 쪽의 To와 Patrick(Journal of Consumer Research, 2021)은 다섯 개의 실험에서 모델이 카메라를 정면으로 보지 않고 <strong>시선을 돌린</strong> 광고가 직접 응시보다 클릭과 구매를 더 끌어낸다는 것을 보였다. 기제는 이야기에 빨려드는 내러티브 몰입이다.{{< sn >}}To &amp; Patrick, How the Eyes Connect to the Heart: The Influence of Eye Gaze Direction on Advertising Effectiveness. Journal of Consumer Research 48(1), 2021. 단, 감성적 소구에서는 돌린 시선이, 이성적이고 정보 위주인 제품에서는 직접 응시가 우세했다.{{< /sn >}} AdSEE의 "살짝 아래를 향한 얼굴"과 이 "돌린 시선"은 방법이 완전히 다른데(GAN 편집 대 필드 실험) 같은 방향을 가리킨다. 물론 하나는 머리 각도, 다른 하나는 눈의 방향이라 동일한 현상은 아니다. 같은 결론으로 수렴하는 독립 증거로 읽는 편이 정확하다. 그리고 To와 Patrick은 단서를 하나 더 단다. 감성적 소구에서는 돌린 시선이 이기지만, 이성적이고 정보 위주의 제품에서는 직접 응시가 낫다. 정답이 맥락에 따라 뒤집힌다.

### 그래도 미감은 약한 신호다

메르카리(2024)의 결과가 이 갈래의 온도를 잘 보여준다. 이 팀은 GPT-4 비전으로 미감 라벨을 만들고 CLIP에 얹어 상품 이미지 점수를 매긴 뒤, 클릭된 상품과 클릭되지 않은 상품의 점수 분포가 다른지 검정했다. 차이는 통계적으로 분명했지만(Kolmogorov-Smirnov 검정, p=8.37×10⁻⁹), 중앙값 차이는 0.6 대 0.5로 작았다.{{< sn >}}Oinar 외, Image Score: Learning and Evaluating Human Preferences for Mercari Search. [arXiv:2408.11349](https://arxiv.org/abs/2408.11349), 2024. 검색 정렬에 반영했을 때 웹에서는 ATPU가 6.99% 올랐으나 모바일에서는 지표가 오히려 악화됐다.{{< /sn >}} 미감은 클릭과 상관이 있으되 약한 신호라는 뜻이다. 결정적으로, 이 점수를 검색 결과 정렬에 반영했을 때 웹에서는 지표가 올랐지만 <strong>모바일에서는 오히려 나빠졌다</strong>. 예쁨을 밀어 올리는 것이 언제나 이롭지는 않다는 반례를, 산업 데이터가 직접 내놓은 셈이다.

<figure>
<img src="/images/attention-image-objectives/mercari-fig4-score-dist.png" alt="클릭된 상품과 클릭되지 않은 상품의 이미지 미감 점수 분포 비교" style="width:100%;max-width:560px;border-radius:8px;">
<figcaption>클릭된 상품(위)과 클릭되지 않은 상품(아래)의 이미지 점수 분포. 통계적으로는 갈리지만 겹치는 영역이 넓다. 미감이 클릭을 설명하는 힘은 작다. 출처: Chingis Oinar 외, Image Score (Mercari, arXiv 2024), Fig. 4.</figcaption>
</figure>

### 클릭베이트의 그림자

클릭을 목적함수로 삼는 순간 따라오는 값이 있다. Wang 외의 "Clicks can be Cheating"(SIGIR 2021)은 제목과 썸네일이 유발한 클릭이 실제 만족과 어긋난다는 것을 반사실 추론으로 분리했다. 클릭은 기만당할 수 있는 신호라는 명제를 학술적으로 정식화한 셈이다.{{< sn >}}Wang 외, Clicks can be Cheating: Counterfactual Recommendation for Mitigating Clickbait Issue. SIGIR 2021.{{< /sn >}} Mukherjee 외(Journal of the Academy of Marketing Science, 2022)는 퍼블리셔 특성을 통제한 뒤에도 헤드라인의 클릭베이트성이 공유를 떨어뜨린다는 것을 필드 데이터로 보였다. 사람들이 낚시를 감지하면 저항한다는 설득지식 모델이 배경이다.

그렇다고 클릭베이트가 모든 것을 무너뜨린다고 단정하면 반박당한다. Munger 외(Public Opinion Quarterly, 2020)는 두 실험에서 클릭베이트 헤드라인이 양극화나 미디어 신뢰, 학습에 유의미한 영향을 주지 않는다는 무효과를 보고했다.{{< sn >}}Munger 외, The (Null) Effects of Clickbait Headlines on Polarization, Trust, and Learning. Public Opinion Quarterly 84(1), 2020.{{< /sn >}} 정직한 정리는 이렇다. 플랫폼 지표(공유, 만족, 장기 리텐션)의 손실은 실증되지만, 개인의 심리가 상한다는 증거는 엇갈린다. 클릭을 목적함수로 두는 일의 대가는 사람이 아니라 먼저 지표에서 나타난다.

## 두 개의 씨앗

조사를 정리하며 더 파고들 만한 씨앗 두 개가 남았다.

<strong>씨앗 하나. 예쁨과 클릭은 다른 목적함수다.</strong> LAION-Aesthetics는 이미지를 예쁘게 만들지만, 그것이 곧 클릭 유도는 아니다. JD의 WWW 2025 논문이 이걸 명시적으로 선언했고, 메르카리 데이터도 상관은 있으되 약하다는 걸 보였다. 지금의 이미지 생성 생태계가 하나의 미감 예측기에 기대어 균질해지고 있다는 비평 각도가 여기서 열린다. 처음에 "숏츠에 쓸 수 있냐"는 물음의 답이 애매했던 까닭도 이 지점에서 드러난다. 무엇을 목표로 삼느냐에 따라 완전히 다른 학문이 대응되기 때문이다.

<strong>씨앗 둘. 기억은 개인이 아니라 이미지에 있다.</strong> 관찰자 간 일치도 ρ=0.68이라는 Isola(2011)의 발견은 "기억은 개인 경험이 지배한다"는 통념을 뒤집는다. 그런데 이 발견을 콘텐츠 제작에 명시적으로 적용한 생성 도구는 아직 없다. GANalyze가 학술적으로 시연했지만 요즘의 생성 AI에 이식된 흔적은 보이지 않는다. 기억성 유도 생성은 2019년 이후 정체 중이고, 여기가 가장 흥미로운 공백이다.

한 가지 실전 함의를 덧붙인다. saliency 산업은 이미 성숙했다. 숏츠와 썸네일 관점에서 가장 실전적인 도구는 이런 API로 시선 히트맵을 뽑아 "제목이나 얼굴이 첫 3초에 눈에 걸리는지"를 검증하는 것이다. 단, 이건 만드는 도구가 아니라 검증하는 도구라는 한계가 있다. 그리고 진화 검색 골격은 EvoGen 같은 오픈소스로 이미 도구화되어 있어, 쓸 만한 점수원만 손에 있다면 곧바로 재활용할 수 있다.

정리하면, 눈길을 끄는 이미지는 하나의 문제가 아니다. 시선과 기억, 미감, 클릭이라는 네 개의 목표가 각자의 학문을 거느리고, 그 목표를 무엇으로 세우느냐가 곧 도구의 성패를 가른다. 뇌에서 출발한 물음이 광고 서버의 A/B 로그에서 끝난 것은, 결국 같은 질문을 서로 다른 언어로 물었기 때문이다.

<p style="opacity:0.6;font-size:0.85rem;margin-top:2em;">일부 2026년 문헌의 식별자와 수치는 조사 시점 캐시 기준이며, 인용 전 원문 재확인이 필요하다. JD CAIG와 AdSEE의 온라인 A/B는 유의성은 보고됐으나 헤드라인 CTR 리프트 수치가 원문에 명시되지 않았거나 대조를 마치지 못해 본문에 싣지 않았다.</p>
