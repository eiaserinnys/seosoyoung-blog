---
title: "Seedance2.0でつくる コラージュアニメーション (tapehead.lab)"
date: 2026-05-18T17:00:00+09:00
tags: ["AI", "영상 생성", "프롬프트 엔지니어링", "Seedance", "Runway", "Midjourney"]
categories: ["다이제스트"]
summary: "AI MV 크리에이터 tapehead.lab이 신곡 「かわいそうな知性」 MV의 콜라주 애니메이션 워크플로우를 공개했다. Midjourney로 20장의 단편 소재를 만들고 → Runway 노드에서 Seedance2.0에 5장씩 Reference로 묶어 15초 시퀀스 88본을 생성하고 → 편집과 작곡을 거꾸로 돌린다. 핵심은 '스타트 프레임이 아니라 Reference 입력'과 'Seedance2.0은 프롬프트가 전부'라는 두 명제다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. tapehead.lab은 X·YouTube에서 AI MV를 만드는 일본 크리에이터다. 신곡 「かわいそうな知性」 MV에 쓴 콜라주 애니메이션 워크플로우를 노트(note.com)에 정리해 공개했다.
2. 워크플로는 ① Midjourney로 단편 소재 20장 생성 → ② Runway 노드 환경에서 Seedance2.0에 5장씩 Reference로 넣어 15초 시퀀스 88본(총 22분+) 생성 → ③ 편집 후 *영상을 음악보다 먼저* 만드는 역프로세스로 마감하는 순서다.
3. 두 가지 명제가 핵심이다. 입력 슬롯을 *Start Frame이 아니라 Reference*로 두면 모델은 이미지의 세계관만 차용하고 동작은 프롬프트에 위임한다. 그리고 *Seedance2.0은 프롬프트가 전부* — 같은 5장이라도 프롬프트만 갈아 끼우면 결과가 크게 달라진다.

![「かわいそうな知性」 MV 헤더](/images/seedance2-collage-animation-workflow/00-cover.jpeg)

## ① Midjourneyで画像生成 — 단편을 모으는 단계

콜라주 영상은 *완성된 한 장의 그림*이 아니라 *분리되고 재조합될 수 있는 단편*을 필요로 한다. tapehead.lab은 처음부터 "断片的な素材を集める" 자세로 이미지 풀을 만든다고 적었다. 완성도 높은 그림은 오히려 콜라주 단계에서 결합이 막힌다.

![Midjourney 생성 일람](/images/seedance2-collage-animation-workflow/01-midjourney-gallery.png)

스타일 통일은 두 가지 손잡이로 잡는다. 첫째, Midjourney의 `sref`(스타일 레퍼런스)를 조합한다. 둘째, *자기 생성물을 다시 스타일 레퍼런스로 넣어* 시리즈 전체의 결을 점진적으로 좁힌다. "스타일을 한 번 설정"하는 방식이 아니라 자기 출력을 피드백 루프에 넣어 결을 빚어내는 방식이다.

![생성 파라미터와 chaos](/images/seedance2-collage-animation-workflow/02-midjourney-params.png)

다양성은 `chaos` 파라미터로 의도적으로 키운다. 수치를 올리면 같은 프롬프트에서도 출력이 흩어진다. 콜라주처럼 *비슷한 결의 서로 다른 조각*이 필요한 작업에 잘 맞는 손잡이다.

![최종 선별된 20장](/images/seedance2-collage-animation-workflow/03-selected-20.png)

> 画像の選び方は感性で！
> 人物だけではなく一部のパーツや抽象的なオブジェクトなど、
> バランスよく選んでいきます。

선별 기준은 분명하다. 인물 전신만이 아니라 *신체 일부와 추상 오브젝트*까지 의도적으로 섞는다. 풀의 카테고리 분포를 균형 있게 잡지 않으면 콜라주 결합이 단조로워지기 때문이다.

## ② Seedance2.0で動画生成 — 모델 통제의 무게중심

호스트는 Runway. tapehead.lab이 Runway를 고른 이유는 두 가지다.

> <strong>・ノードベースのワークフローがめちゃ便利！<br>
> ・Unlimitedでクレジット気にせず生成試せる</strong>
> （720pまでだし生成遅いけど、、、）

노드 UX는 워크플로우 관리를 쉽게 만들고, Unlimited 플랜은 크레딧 걱정 없이 시안을 굴리게 한다. 720p 상한과 느린 생성 속도라는 단점을 *무한히 굴릴 수 있는 운영 조건*으로 압도하는 모델이다.

![Runway 노드 구성](/images/seedance2-collage-animation-workflow/04-runway-nodes.jpg)

### Start Frame이 아니라 Reference 입력

가장 강한 한 줄은 이것이다.

> 스타트프레임이 아니라 *리퍼런스 지정*으로 입력하기

Seedance2.0의 Reference 성능이 워낙 좋아서, 이미지가 가진 세계관을 그대로 확장해 영상으로 만들어준다. 그래서 *Start Frame으로 넣지 않고* Reference 입력으로 두면 모델은 색·텍스처·세계관만 차용하고 동작은 프롬프트가 결정한다. 같은 자료를 어느 슬롯에 넣느냐가 결과 성격을 완전히 가른다.

![Ref Image 입력 슬롯](/images/seedance2-collage-animation-workflow/05-ref-image-slot.jpg)

### 5장 × 4세트 — 노드 분할 운용

20장을 한꺼번에 레퍼런스로 넣지 않는다. 5장씩 4세트로 나눠 노드를 4개 구성한다. 레퍼런스가 너무 많으면 모델이 산만해지고, 5장 단위로 묶으면 세트별로 결이 다른 콜라주가 안정적으로 나온다.

### 프롬프트는 1.5초 단위 10블록으로 분해

> ①リファレンス指定の指示
> ②全体のスタイルやテンション、方向性の指示
> ③カットごとの具体的な動きの指示

15초 시퀀스 한 컷의 프롬프트는 사실상 *시간표*다. 0-1.5s, 1.5-3s, … 식으로 10블록으로 쪼개 블록마다 *무엇이 어떻게 변형되는가*를 구체적인 동사로 지정한다. 본문에 공개된 영문 프롬프트의 한 블록을 옮기면 이런 식이다.

```
0-1.5s
A figure's silhouette fills with a new color seeping inward
while its outline detaches and drifts upward.
The background inverts to a complementary color.
The surface texture flows downward against the direction of the color seep.
```

블록은 10단계까지 이어지고 마지막 13.5-15s 블록에서는 앞선 모든 변형을 *동시에* 일으켜 누적 카오스를 만든다. 영상 모델에 던지는 프롬프트가 어디까지 정교해질 수 있는지 보여주는 사례다.

![콜라주 결과 GIF 1](/images/seedance2-collage-animation-workflow/06-collage-gif-1.gif)

> プロンプト次第で様々な動きに変えながらコラージュできます。
> <strong>（Seedance2.0はとにかくプロンプトです。プロンプト次第で出力が大きく変わります。）</strong>

여기서 *Seedance2.0은 프롬프트가 전부*라는 명제가 나온다. 같은 5장의 레퍼런스라도 프롬프트만 바꾸면 결과가 크게 달라진다. 모델 통제력의 무게중심이 이미지가 아니라 텍스트 쪽에 있다는 진단이다.

![콜라주 결과 GIF 2](/images/seedance2-collage-animation-workflow/07-collage-gif-2.gif)

![콜라주 결과 GIF 3](/images/seedance2-collage-animation-workflow/08-collage-gif-3.gif)

## ③ 楽しい編集作業 — 폐기 전제와 역프로세스

> 今回出力した素材の数は、「15秒✖️88本」
> トータル20分超え

본편보다 훨씬 많은 양을 만들고 편집에서 추린다. 15초×88본이면 22분이 넘는 분량이다. 자원 제약이 큰 전통 영상에서는 불가능했던 *대량 생성 → 대량 폐기*가 AI 영상의 기본 운영 모드로 자리 잡는다.

![출력 소재 정리](/images/seedance2-collage-animation-workflow/09-output-files.png)

> 普通、こんな贅沢なアニメーションの使い方はできないです。
> AIだからできる暴挙！

![편집 화면](/images/seedance2-collage-animation-workflow/10-editing.png)

그리고 더 흥미로운 지점은 *영상을 먼저 만들고 음악을 나중에 작곡*했다는 사실이다. 보통 MV는 곡이 먼저 있고 영상이 따라오는데, 이번에는 순서가 뒤집혔다.

> このコラージュアニメーションに耐えられる音楽にしないと、成立しないなと思ったので。

콜라주에 견딜 수 있는 음악을 거꾸로 맞춘 셈이다. 더 나아가 *일부 가사는 영상에서 역으로 끌어낸다*. 무작위에 가까운 콜라주 영상에 의미를 부여하기 위해 가사를 영상에 맞춰 짜는 후공정이다. 시청자가 "의미가 있다"고 느끼게 만드는 장치 — AI로 영상을 양산할 수 있을 때 가능한 의도된 순서 전도다.

## 가장 흥미로운 지점

기법 자체는 분명하지만, 가장 흥미로운 것은 *세 가지 인프라 조건이 결합해야* 이 워크플로가 가능하다는 점이다.

1. <strong>Reference 입력을 다루는 모델</strong> — Seedance2.0처럼 이미지를 첫 프레임이 아니라 분위기 입력으로 받는 모델.
2. <strong>노드 UX와 Unlimited 크레딧</strong> — Runway가 제공하는 두 가지가 합쳐져야 "크레딧 걱정 없이 시안을 굴리는" 모델이 성립한다.
3. <strong>폐기 전제의 운영 방식</strong> — 본편의 4배 가까운 분량을 만들고 자르는 사고방식 자체.

세 조건 중 하나라도 빠지면 이 콜라주는 일상적 워크플로가 되지 못한다. 그래서 이 글은 "Seedance2.0 사용법"이라기보다 *모델 + UX + 크레딧 정책이 결합해야 새로운 영상 표현이 일상화된다*는 사례 보고에 가깝다. 도구가 풀린 그날 새 표현이 자동으로 따라오지 않는다 — 운영 조건이 같이 풀려야 한다.

## 출처

- 저자: tapehead.lab ([@tapehead_Lab](https://x.com/tapehead_Lab))
- 매체: note.com, 2026년 5월 18일
- 관련 작품: 「かわいそうな知性」 MV (2026-05-13 공개)
- 원문: <https://note.com/tapehead/n/n94eaf79a519b>
