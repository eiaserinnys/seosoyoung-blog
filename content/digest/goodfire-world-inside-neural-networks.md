---
title: "The World Inside Neural Networks"
date: 2026-05-08T10:48:00+09:00
tags: ["interpretability", "neural-geometry", "manifold", "SAE"]
categories: ["다이제스트"]
summary: "Goodfire의 'Neural Geometry Series' 첫 글. 신경망 내부 표상은 직선 방향이 아니라 곡선 매니폴드 위에 산다고 주장하며, mountain car 스티어링과 슬랜트 라임 매니폴드 사례로 SAE 같은 기존 방법의 한계와 매니폴드 기반 해석·제어 방법론의 필요성을 보인다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Goodfire가 'Neural Geometry Series' 첫 글로 발표한 입장문이다 (Geiger·Lubana·Fel·Merullo 외, 2026-05-07). 신경망 내부 표상은 직선 방향(linear direction)이 아니라 곡선 매니폴드 위에 산다는 입장을 정면으로 내세운다.
2. mountain car에서 위치 표상은 곡선 매니폴드를 이루며, 그 매니폴드를 따라 활성을 움직이면 차가 부드럽게 이동하지만 직선 경로로 움직이면 출력이 깨지거나 다른 위치로 텔레포트한다. 매니폴드를 따라가는가, 가로지르는가가 곧 정밀 제어의 가능 여부를 가른다.
3. 인기 기법인 sparse autoencoder(SAE)는 슬랜트 라임 매니폴드 같은 연속 구조를 23개의 무관해 보이는 국소 피처로 산산조각낸다(shattering). SAE는 폐기 대상이 아니라 보완 대상이며, 신경 기하를 존중하는 새 방법론이 정렬·디버깅·감사의 임계 경로다.

![Neural geometry banner](/images/goodfire-world-inside-neural-networks/neural-geometry-opengraph.webp)
> 출처: Goodfire, *The World Inside Neural Networks* 배너 (2026-05-07).
> 원본 이미지: <https://static.goodfire.ai/neural-geometry-agenda/neural-geometry-opengraph.webp>

## 들어가며 — 왜 '신경 기하'인가

세계는 구조적이다. 색상환·도로망·가계도·달력처럼 기하학적 관계가 도처에 있고, 사람은 이 구조를 머릿속에 표상으로 들여와 항해한다. Goodfire는 신경망의 안쪽도 똑같이 그렇다고 본다. 모델·모달리티·도메인을 가리지 않고 같은 패턴이 보인다.

- 언어 모델: 숫자, 요일, 달이 <strong>원형 고리</strong>로 인코딩되고, 역사 연도와 한 줄의 글자 위치는 매끄러운 곡선으로 표현된다.
- 이미지 모델: 사물의 공간 배치가 활성 공간에서 그대로 재현되고, 색상은 색상–채도–명도로 짜인 매끄러운 곡면 위에 올라간다.
- 특수 도메인 모델: 유전체 모델에서 생명의 계통수는 복잡한 매니폴드 위에 놓이고, 후성유전체 모델에서는 알츠하이머 바이오마커가 깔끔한 곡선으로 발견됐다.

신경 기하란 이렇게 신경망 내부에 살아 있는 곡선 기하 구조를 가리킨다. Goodfire의 주장은 이 기하를 이해하는 것이 모델의 ontology(세계를 어떻게 개념적으로 자른 뒤 표상하는가)에 닿는 길이며, 그 위에서 작동하는 알고리즘과 결과 행동까지 함께 해석하는 임계 경로라는 것이다.

## Mountain Car — 매니폴드를 따르면 차가 움직인다

<figure>
  <iframe
    src="https://static.goodfire.ai/neural-geometry-agenda/mountain_car_prod.html"
    style="border:none; width:100%; height:825px; max-width:100%;"
    loading="lazy"
    title="Mountain Car: Spline vs Linear Steering (Goodfire)">
  </iframe>
  <figcaption>
    출처: Goodfire 인터랙티브 피규어. 원본:
    <a href="https://static.goodfire.ai/neural-geometry-agenda/mountain_car_prod.html" target="_blank" rel="noopener noreferrer">
      static.goodfire.ai/neural-geometry-agenda/mountain_car_prod.html
    </a>. 좌측은 spline(매니폴드) 스티어링, 중앙은 linear 스티어링, 우측은 linear probe 방향 스티어링 결과다.
  </figcaption>
</figure>

고전 RL 환경 mountain car 위에 단순한 image–action 모델을 학습시켜, 현재 상태(차의 위치·운동량)와 무작위 액션이 주어졌을 때 다음 프레임을 예측하게 했다. 이 모델은 mountain car에 대한 작은 <strong>world model</strong>이다.

이미지 인코더의 임베딩 벡터를 차의 위치별로 찍어보면, 점들이 <strong>가닥(string) 모양</strong>으로 늘어선다. 가닥에서 인접한 점은 차의 인접한 위치에 대응한다. 자연스러운 가설은 "이 가닥이 곧 모델이 차의 위치를 표상하는 방식"이라는 것이다.

가설을 검증하기 위해 모델에 '뇌수술'을 해 봤다.

1. 점들이 만드는 1차원 매니폴드(매끄러운 곡선)를 피팅한다.
2. 은닉 활성을 매니폴드를 따라 움직인다(매니폴드 스티어링).
3. 결과: 예측되는 차가 산 위로 부드럽게 오르내린다. 가설이 입증된다.

비교 대상은 <strong>선형 스티어링 벡터</strong>다. 보통 진실 vs 거짓 같은 대비 쌍의 활성 차이를 평균해 한 방향을 만들고, 그 방향으로 활성을 밀어 모델을 조향한다. 기하가 정말 직선이라면 잘 작동한다. 그러나 mountain car 사례가 보여주는 두 가지 실패 양식은 명확하다.

- **보이드 통과:** 두 위치를 잇는 직선이 모델이 다뤄본 적 없는 활성 공간의 빈 영역을 가로지르며, 출력이 garbled한 프레임으로 깨진다.
- **텔레포트:** 직선 경로가 다른 위치의 유효 활성과 우연히 교차하면, 차가 그 위치로 갑자기 순간이동한다.

> 단순한 스칼라 개념인 '위치'조차 곧은 직선이 아니라 곡선 매니폴드 위에 살 수 있다. 기하를 따르면 정밀하고 효과적인 개입이 가능하지만, 무시하면 모델은 부자연스럽고 일관성 없는 상태로 떠밀린다.

이 첫 글은 입장 선언에 가깝고, 매니폴드 vs 선형 스티어링 자체에 대한 본격적인 분석은 시리즈의 다음 글 *Steering Along Manifolds to Control Neural Networks* (<https://www.goodfire.ai/research/manifold-steering>)에서 다루겠다고 예고한다.

## 표상·계산·행동 — 세 층을 함께 봐야 한다

![Three levels of analysis in neural networks](/images/goodfire-world-inside-neural-networks/representation-computation-behavior.webp)
> 출처: Goodfire, 신경망의 세 분석 수준(표상·계산·행동) 도식. 마(Marr 1982)의 분석 수준 관점을 차용한 것임을 본문에서 명시한다.
> 원본 이미지: <https://static.goodfire.ai/neural-geometry-agenda/representation-computation-behavior.webp>

신경 기하는 신경망의 세 층 — **표상**, **계산**, **행동** — 을 한꺼번에 정밀하게 다루기 위한 도구로 제시된다.

> 계산은 표상을 소비하고 생산한다. 데이터 구조(스택, 룩업 테이블)는 정보를 담고 연산자(push/pop, read/write)는 데이터 구조를 다른 데이터 구조로 바꾼다. 따라서 표상을 모르면 계산을 완전히 이해할 수 없다. 비트가 무엇인지 모르는 채 노트북이 숫자 리스트를 어떻게 정렬하는지 알아내려고 시도해 보라.

지난 십여 년의 회로(circuit) 분석·기계적 해석가능성 연구는 신경망 *계산*을 풀어내는 데 실질적 진전을 만들었다. Goodfire의 진단은 거기서 빠진 절반이 곧 표상의 기하라는 것이다. 표상의 데이터 구조 — 곡선·매니폴드·구조화된 활성 공간 — 를 함께 봐야 비로소 모델 행동을 닫힌 그림으로 설명할 수 있다.

표상과 계산을 모두 충분히 이해하면 무엇이 가능해지는가:

- 모델이 언제 실패할지 *예측*
- 실패 시 *디버깅*
- 자신감 있는 *평가·감사*
- *훈련 절차*의 재설계
- 신비주의를 줄이고 공학에 가까운 모델 개발

## 신경 기하는 어디서 자라나는가

![Concepts arise from the structure of the world reflected in training data](/images/goodfire-world-inside-neural-networks/world-data-neural-networks.webp)
> 출처: Goodfire, 신경 기하의 기원 도식. *"개념은 마법으로 신경망에 등장하지 않는다 — 학습 데이터에 비친 세계의 구조에서 자라난다."*
> 원본 이미지: <https://static.goodfire.ai/neural-geometry-agenda/world-data-neural-networks.webp>

훈련 데이터는 모두 세계의 다운스트림이다. 레딧 글이든 산을 굴러 내려가는 차의 시뮬레이션이든, 데이터는 강하게 구조화된 현실에서 흘러나온다. 신경망은 그 방대한 데이터를 <strong>크지만 유한한 파라미터</strong>로 모델링하도록 강제되며, 이 압박이 외부 세계의 구조를 내부 매니폴드로 재현하게 만든다.

달의 예가 직관을 준다.

- 세계: 달은 순환 구조다. 1월은 12월·2월과 가깝고 6·7월과는 멀다.
- 텍스트의 통계적 흔적: 가까운 달은 비슷한 문맥에서 등장한다.
- 학습: 언어 모델이 이 규칙성을 효율적으로 잡도록 최적화되는 과정에서, 내부 표상은 <strong>순환 구조</strong>로 자리잡는다.

핵심은 <strong>유한 파라미터 + 강구조 데이터</strong>라는 압박이다. 무한 용량이라면 사례를 통째로 외워도 되지만 그렇지 않으므로, 모델은 규칙성을 기하 구조로 압축한다. 매니폴드는 마법이 아니라 압축의 부산물이다.

## SAE — 매니폴드를 산산조각내는 경향

<figure style="max-width:600px; margin:0 auto;">
  <iframe
    src="https://static.goodfire.ai/neural-geometry-agenda/rhymes.html"
    style="border:none; width:100%; aspect-ratio: 1 / 1; max-width:100%;"
    loading="lazy"
    title="Slant rhyme manifold (Goodfire)">
  </iframe>
  <figcaption>
    출처: Goodfire 인터랙티브 피규어. 원본:
    <a href="https://static.goodfire.ai/neural-geometry-agenda/rhymes.html" target="_blank" rel="noopener noreferrer">
      static.goodfire.ai/neural-geometry-agenda/rhymes.html
    </a>. -ore로 끝나는 슬랜트 라임 단어들이 음운 종결 유사도에 따라 매니폴드 위에 분포한다.
  </figcaption>
</figure>

![A subspace of slant rhymes with -ore](/images/goodfire-world-inside-neural-networks/slant-rhyme-manifold.webp)
> 출처: Goodfire, 슬랜트 라임 매니폴드 정적 컷. 완벽 라임 'door'는 한쪽 끝(짙은 파랑)에, 약한 라임 'wire'는 반대 끝(노랑)에, 'car' 같은 근접 라임은 그 사이에 놓인다.
> 원본 이미지: <https://static.goodfire.ai/neural-geometry-agenda/slant-rhyme-manifold.webp>

Goodfire는 자체 비지도 파이프라인으로 활성 공간에서 매니폴드를 찾았는데, 그 매니폴드 위 점들은 음운적으로 비슷한 라임 단어들(*fire/higher*, *near/dear* 등)로 채워졌다. 매니폴드 전체를 한 번에 보면 의미는 단순하다. <strong>단어의 음운 종결 유사도</strong>다.

같은 매니폴드를 인기 기법인 sparse autoencoder(SAE)로 재구성하게 시키면 그림이 달라진다. 자동 해석가능성(auto-interpretability) 라벨이 매니폴드를 재구성하는 데 기여한 SAE 피처들에 다음과 같이 붙는다.

```
SAE FEATURES ON SLANT RHYME MANIFOLD
 2478 : Words beginning with "Hor"
 3596 : The word "correlation" and closely related statistical correlation terms
 4583 : Words related to absorption/absorbance
 4596 : The token "Horde," especially in gaming or fantasy contexts
 4806 : Words beginning with or containing the prefix "Port"
 5316 : Human evolutionary history, ancestors, hunter-gatherers
 6440 : Words beginning with "import-"
 7471 : Legal opinion party labels (Petitioner, Appellant, Plaintiff)
 9514 : Words and names beginning with "Sor-"
10637 : Occurrences of "Corporate" in titles, headings, organization names
12145 : Words beginning with the prefix "morph"
12714 : Token 'Nor' starting words (names, Norwegian/Norway terms)
17398 : Tokens starting with "Mor"
20283 : Words/names containing the substring "or"
21241 : Boundaries between adjacent XML/HTML tags
22084 : Tokens starting with "Por"/"por"
23104 : Tokens containing or beginning with "Horn"
23118 : Geometry descriptions involving triangle sides and right triangles
24140 : Proper names containing the syllable "tor" or "kor"
25233 : Scientific paper sentences where "we" introduces an experiment
28555 : Word-initial token fragment "Cor"
31648 : Words/names beginning with "Marg"
31747 : Tokens starting with "Dor"
```

23개의 무관해 보이는 국소 라벨이다. *우리가* 매니폴드 전체를 한 번에 보고 알 수 있는 *음운 종결 유사도*라는 전역 의미는, 피처 단위로 잘게 부순 시점에서 사라진다.

> SAE 피처는 곡선 위 한 점의 *국소 속성*만 잡는 경향이 있어, 전체로 봐야 드러나는 의미 구조를 가린다(shattering).

여기서 Goodfire의 입장은 분명하다. SAE는 폐기 대상이 아니라 *보완 대상*이다. 비지도로 대규모 피처를 발굴하는 가치는 분명하지만, 더 깊고 정밀한 이해와 제어를 위해서는 **신경 기하를 존중하는 새 방법론** — 지도·비지도 양쪽 모두 — 이 필요하다.

## 결론과 전망

![Neural geometry closing banner](/images/goodfire-world-inside-neural-networks/wide_manifold_banner.webp)
> 출처: Goodfire, 시리즈 클로징 배너. 실제 언어 모델에서 검출된 매니폴드들이 합쳐 한 장으로 펼쳐진다.
> 원본 이미지: <https://static.goodfire.ai/neural-geometry-agenda/wide_manifold_banner.webp>

> 신경망은 구조적 내적 세계를 갖고 있고, 그 기하는 현실의 구조를 비춘다. 신경 기하를 존중하는 이론과 방법을 발전시키면 더 깊은 해석가능성, 더 신뢰할 수 있는 제어, 더 안전하고 더 좋은 AI에 도달할 수 있다.

Goodfire는 신경망의 'black box' 내부 이해를 *불가능*이 아니라 *오늘날 가장 큰 과학적 도전이자 기회*로 정의하며, 다윈의 한 줄로 글을 닫는다.

> *"My mind seems to have become a kind of machine for grinding general laws out of large collections of facts."* — Charles Darwin

이전 세대에는 사실의 양도, 수집 능력도 부족했다. 이제 점점 유능해지는 연구 에이전트와 신경 기하에 뿌리내린 도구가 *경험적 데이터*를 적정 규모로 모아주기 시작하면, 사고의 일반 법칙을 갈아낼 시간이 임박했다는 것이 Goodfire의 마무리다.

## 핵심 용어

- **신경 기하 (neural geometry):** 신경망 내부 표상이 만드는 곡선 기하 구조.
- **매니폴드 (manifold):** 활성 공간 안의 연속·곡선 표면. 직선 방향과 대비된다.
- **스티어링 (steering):** 은닉 활성을 인과적으로 조작해 출력을 바꾸는 개입.
- **선형 스티어링 벡터:** 대비 쌍 평균(예: 진실 평균 − 거짓 평균)을 한 방향으로 잡고 그 방향으로 활성을 미는 방법. 기하가 직선일 때만 견고하다.
- **매니폴드 스티어링:** 활성 공간 안에 피팅한 곡선을 따라 활성을 움직이는 개입. 곡선 기하를 존중한다.
- **온톨로지 (ontology, of a model):** 모델이 세계를 어떻게 개념적으로 잘라 표상하고 분류하는가.
- **활성 공간 (activation space):** 신경망 은닉 상태의 다차원 공간.
- **월드 모델 (world model):** 물리 시스템의 미래 상태를 예측하도록 학습된 신경망.
- **SAE (sparse autoencoder):** 활성을 해석 가능한 피처(활성 공간의 방향들)로 분해하는 비지도 기법.
- **shattering:** 연속 매니폴드가 SAE 피처 분해를 거치며 다수의 국소 피처로 산산조각나, 전역 의미가 가려지는 현상.

## 함께 보면 좋은 글

- 시리즈 다음 글: *Steering Along Manifolds to Control Neural Networks*  
  <https://www.goodfire.ai/research/manifold-steering>
- 같은 시리즈/연관: *Phylogeny manifold* (생명의 계통수가 매니폴드를 이루는 사례)  
  <https://www.goodfire.ai/research/phylogeny-manifold>
- 같은 시리즈/연관: *Interpretability for Alzheimer's detection* (후성유전체 모델에서 곡선 바이오마커 발견)  
  <https://www.goodfire.ai/research/interpretability-for-alzheimers-detection>

## 가장 흥미로운 지점

매니폴드와 SAE의 관계가 *경쟁* 아닌 *상보 보완*으로 정리되는 대목이 가장 흥미로웠다. 흔한 비판은 "SAE는 틀렸다"가 되기 쉽지만, Goodfire는 SAE가 비지도 대규모 발견에 충분히 유용하다는 점을 인정하면서도, 매니폴드 단위에서 보면 한 라벨로 묶일 23개의 단편으로 잘게 분해되는 한계를 보여준다. 그래서 SAE를 폐기하라가 아니라 *매니폴드 시각을 옆에 둔 채 함께 쓰자*가 된다.

이 입장의 무게를 단번에 보여주는 것이 슬랜트 라임 표였다. 매니폴드 전체를 보면 **음운 종결 유사도** 하나로 정리되는데, 같은 자료를 SAE로 보면 *Hor-, Por-, Mor-, Dor-, Horn-, Marg-* 같은 23개의 표면 어절로 흩어진다. 우리가 풀이로 받아 보는 *해석*이 사실은 어디까지가 모델의 표상이고 어디부터 우리의 절단법이 만든 그림자인지 — 그 구분 자체가 다음 단계의 해석가능성 연구의 진짜 과제임을 강하게 시사한다.

## 출처

- 발신자: Goodfire (Atticus Geiger, Ekdeep Singh Lubana, Thomas Fel, Jack Merullo, Michael Jae Byun, Owen Lewis, Tom McGrath)
- 발표일: 2026년 5월 7일
- 시리즈: The Neural Geometry Series (Goodfire) — <https://www.goodfire.ai/research/neural-geometry>
- 원문: <https://www.goodfire.ai/research/the-world-inside-neural-networks>
- 본 다이제스트의 모든 정적 이미지는 Goodfire의 원본 자산을 그대로 인용·재게시했고, 인터랙티브 피규어(mountain car·rhymes)는 Goodfire CDN을 iframe으로 직접 임베드했다. 자료 권리는 모두 Goodfire에 있다.
