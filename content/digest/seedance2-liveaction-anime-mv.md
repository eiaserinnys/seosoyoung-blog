---
title: "Seedance2.0으로 만드는 실사×애니메이션 합성 MV (tapehead.lab)"
date: 2026-05-27T15:30:00+09:00
tags: ["AI", "영상 생성", "프롬프트 엔지니어링", "Seedance", "Runway"]
categories: ["다이제스트"]
summary: "AI MV 크리에이터 tapehead.lab이 신곡 「free will」 MV의 실사×애니메이션 합성 워크플로우를 공개했다. 핵심은 합성과 동영상 생성을 따로 하던 두 갈래가 Seedance2.0에서 하나로 합쳐졌다는 것 — 합성하면서 생성한다. 캐릭터 시트 한 장과 프롬프트만으로 드론 샷급 카메라워크까지 캐릭터가 붕괴 없이 버틴다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/seedance2-liveaction-anime-mv/00-cover.jpeg"
images:
  - "/images/seedance2-liveaction-anime-mv/00-cover.jpeg"
---

## 3줄 요약

1. tapehead.lab이 신곡 「free will」 MV에 쓴 *실사×애니메이션 합성* 워크플로우를 note.com에 공개했다. 같은 저자가 지난주 공개한 [콜라주 애니메이션 워크플로우](/digest/seedance2-collage-animation-workflow/)의 후속편이고, 도구도 Seedance2.0·Runway로 같다.
2. 1년간 합성 기법은 ① "합성된 정지화면을 만들어 동영상으로 움직인다" ② "그린백 애니 소재만 움직여 나중에 합성한다"는 두 갈래뿐이었다. Seedance2.0은 이 둘을 하나로 묶어 *합성하면서 동영상을 생성*한다.
3. 결론은 단순하다 — 배경도 합성 레퍼런스도 필요 없다. *캐릭터 시트 한 장과 프롬프트만*으로 드론 샷 같은 큰 카메라워크에서도 캐릭터가 붕괴되지 않고 액션을 유지한다. 프롬프트는 ①합성 룰 ②물리 룰 ③숏별 사건 ④마감 지정의 4단 구조다.

![「free will」 MV 헤더](/images/seedance2-liveaction-anime-mv/00-cover.jpeg)

지난주 정리한 [콜라주 애니메이션 다이제스트](/digest/seedance2-collage-animation-workflow/)의 결론은 두 가지였다. *Start Frame이 아니라 Reference로 넣어라*, 그리고 *Seedance2.0은 프롬프트가 전부다*. 이번 글은 그 두 명제를 실사 합성이라는 더 어려운 무대에서 한 번 더 확인한다. 레퍼런스로 주는 건 캐릭터 시트 한 장뿐이고, 나머지는 전부 프롬프트가 통제한다. 같은 저자가 같은 도구로 *다른 표현*에 도달한 사례라, 두 글을 나란히 읽으면 도구 하나가 표현을 어디까지 밀어내는지가 선명해진다.

## 1년간의 진화 — "합성하고 나서 움직인다"에서 "합성하면서 생성한다"로

저자는 실사×애니 합성 MV를 1년간 정기적으로 만들어 왔고, 그 라인업이 생성 AI의 진화를 보기 쉬운 표본이라고 적었다.

| 시점 | 작품 | 도구 |
|------|------|------|
| 2025년 7월 | 「Lazy talk」 | Midjourney |
| 2025년 9월 | 「Missact」 | Nano banana |
| 2025년 11월 | 「Futa-rhythm」 | Nano banana |
| 2026년 1월 | 「Side Step」 | Nano banana Pro |
| 2026년 (이번) | 「free will」 | Seedance2.0 |

도구가 Midjourney → Nano banana → Nano banana Pro로 진화하며 퀄리티도 올라갔다. 그러나 만드는 *방식*은 그동안 두 갈래 중 하나였다.

> <strong>· 「합성된 정지화면」을 준비해서, 그것을 동영상 생성으로 움직인다<br>
> · 애니 소재만 그린백에서 움직여, 나중에 합성한다</strong>

Seedance2.0의 등장으로 비로소 가능해진 것이 이것이다.

> <strong>합성하면서 동영상을 생성한다.</strong>

특히 봐 달라고 한 건 *카메라워크와 액션*이다. 드론 샷처럼 움직임이 큰 카메라워크에서도 붕괴되지 않고 액션을 하면서 합성되는 건 현시점 Seedance2.0만 된다는 게 저자의 진단이다.

## ① 캐릭터 소재 — 도구에 맞는 스타일을 먼저 찾는다

"좋아하는 걸 쓰면 된다"고 말하고 싶지만, 그보다 먼저 *동영상 생성 도구에 맞는 스타일을 찾는* 것이 이후 공정을 매끄럽게 한다. 그래서 캐릭터 소재를 만들면 바로 동영상 생성 테스트부터 돌려 본다.

> <strong>· 제대로 붕괴 없이 움직이는가?<br>
> · 캐릭터 스타일을 유지하는가?<br>
> · 3D로 쏠리거나 반대로 2D로 쏠리는 등, 의도치 않은 방향으로 끌리지 않는가?</strong>

이번에 쓴 캐릭터 시트는 이 정도면 충분하다고 했다.

![이번에 쓴 캐릭터 시트](/images/seedance2-liveaction-anime-mv/01-character-sheet.jpg)

특징을 정리하면 *의상은 심플하게, 칠은 플랫하게, 선의 콘트라스트는 또렷하게*다. 눈 모양도 비교적 왕도 스타일. 큰 액션과 카메라워크를 줬을 때 가장 안정적인 게 바로 이 스타일이었다.

그리고 *의상 색과 머리 색을 선명한 보색*으로 잡아 실사에 너무 녹아들지 않게 의식했다. 여기에 역설이 있다.

> 이미 도구 성능이 너무 높아서 위화감이 남지 않게 됐다. 그래서 의식적으로 실사와 콘트라스트를 주지 않으면, 그냥 퀄리티 높은 보통 애니로 보여 버린다.

![보색 의상·머리색 예시](/images/seedance2-liveaction-anime-mv/02-complementary-color.jpg)

합성이 너무 자연스러워진 탓에, 이번엔 *애니임을 일부러 드러내야* 한다. 라이팅은 알아서 잘 녹아든다.

## ② Seedance2.0 동영상화 — 레퍼런스는 캐릭터 시트 한 장

준비하는 정지화면은 캐릭터 시트, 이것 하나뿐이다.

> <strong>합성한 레퍼런스 필요 없어?<br>
> 배경 이미지 필요 없어?</strong>

저자의 답은 "필요 없다"다. 처음엔 합성한 스타트 프레임을 만들어 보거나 배경만 따로 레퍼런스로 넣어 보는 등 여러 시도를 했지만, 결국 *캐릭터 시트와 프롬프트만으로 만드는 것이 카메라워크와 액션 면에서 가장 좋다*는 결론에 닿았다. (지난 콜라주 편의 *Start Frame이 아니라 Reference* 명제가 여기서도 그대로 작동한다 — 슬롯을 비워 두고 통제를 텍스트로 옮긴다.)

![캐릭터 이미지와 프롬프트만으로 나온 도쿄 풍경](/images/seedance2-liveaction-anime-mv/03-tokyo-scenery.png)

Seedance는 일본 도시부의 자잘한 풍경도 *분위기 해상도*가 높게 나온다. 위 영상이 캐릭터 이미지와 프롬프트만으로 직접 나온다. 그래서 일상 풍경이라면 배경조차 따로 준비할 필요가 없다. (다만 간판 같은 *문자 주변*은 Nano banana 2나 GPT image 2에 비해 약하니, 그럴 땐 따로 준비하는 편이 낫다.)

프롬프트의 한 예는 매에게 채여 하늘로 끌려 올라가는 5개 숏짜리 시퀀스다. 캐릭터에는 *제로 포토리얼리즘*(또렷한 잉크 선, 셀 셰이딩 플랫 컬러, 손으로 칠한 눈동자)을, 그 외 모든 요소(매·하늘·바다·도쿄 풍경)에는 *완전한 포토리얼리즘*을 지정한다.

```
@Image1 as the main character for all shots — anime illustration
style strictly preserved: crisp ink outlines, cel-shaded flat color,
hand-painted pupils, zero photorealism on character.
All other elements — hawk, sky, sea, Tokyo scenery — fully photorealistic.
Bright midday, warm sunlight, clear sky, physics realistic.

Shot 1 [TOKYO WATERFRONT — CREPE]: @Image1 sits on real seaside
railing, legs dangling, eating a real crepe, completely relaxed.
...
Cut to Shot 5 [PURE JOY]: @Image1 fully at ease now, floating
alongside hawk, wind in hair. Takes a calm triumphant bite
of the crepe. Camera wide: hawk soaring in a lazy circle above
the photorealistic Tokyo skyline...

Cinematic 24fps, emotional arc from surprise to panic to wonder,
extreme close-ups on face at every beat, slow motion on awe moment,
consistent ink line and cel-shading on @Image1, avoid jitter
on outlines, avoid fantasy physics.
```

![매에게 채여 가는 장면](/images/seedance2-liveaction-anime-mv/04-hawk-scene.gif)

프롬프트 구조를 정리하면 이렇다.

> <strong>① [캐릭터와 배경의 합성 룰]<br>
> ② [빛·날씨·물리 룰]<br>
> ③ [각 숏별 일어나는 일]<br>
> ④ [편집과 영상의 마감 지정]</strong>

이 프롬프트를 베이스로 두고 *주로 ③의 숏별 내용만 바꿔 가며* 여러 장면을 만든다. 지난 콜라주 편이 1.5초 단위 10블록의 *시간표*였다면, 이번 실사 합성 편은 합성 룰·물리 룰을 앞에 고정하고 사건만 갈아 끼우는 *템플릿*에 가깝다. 같은 "프롬프트가 전부"라는 명제가 작업의 결에 따라 다른 모양으로 굳는 셈이다.

![미사용 장면 ①](/images/seedance2-liveaction-anime-mv/05-unused-scene-1.gif)

![미사용 장면 ②](/images/seedance2-liveaction-anime-mv/06-unused-scene-2.gif)

## ③ 즐거운 편집 — 尺과 음하메

이번에 출력한 동영상 클립은 15초 × 약 100본. (검증을 겸했던 터라 실패 클립도 많다.) 이번에도 Runway에서 생성을 계속 돌렸다. 역시 *무제한 플랜*이 있는 플랫폼이 강하다는 평 — 느긋하게 기다릴 수 있는 사람에게 한정되지만. 지난 편의 *15초 × 88본, 22분 분량*과 거의 같은 규모다. 대량으로 만들고 편집에서 추리는 운영 방식이 이번에도 그대로다.

![편집 시퀀스 화면](/images/seedance2-liveaction-anime-mv/07-editing.png)

편집은 꽤 세밀하게 한다("시퀀스는 더러운 파"라고 했다). 저자가 편집할 때 의식하는 두 가지는 이렇다.

> <strong>· 영상의 화각과 카메라워크에 맞춰, 보여줄 尺(길이)을 정한다<br>
> · 컷 점과 화면 안의 움직임, 둘 다로 음하메(音ハメ)한다</strong>

*화각*은 이렇게 가른다.

> <strong>· 롱 숏 → 정보량이 많고 시선 이동도 생기므로, 어느 정도 긴 尺이 필요해지기 쉽다<br>
> · 클로즈업 → 정보가 정리돼 있어, 짧은 尺으로도 성립하기 쉽다</strong>

*카메라워크*도 마찬가지다.

> <strong>· 큰 카메라워크 → 움직임 자체를 기분 좋게 보여주려 길게 쓰는 일이 많다<br>
> · 고정 카메라 → 짧게 끊어도 성립하기 쉽다</strong>

이 사고를 베이스로 균형을 잡아 전체 리듬을 짠다.

![화각·카메라워크별 尺 조절 예시](/images/seedance2-liveaction-anime-mv/08-shot-length.gif)

*음하메*는 컷 점과 액션 양쪽을 쓴다. 0:08 부분의 「선택했다고」「말하면」「얘기가 빠르다」「탄탄탄(소리)」 네 포인트 중, 앞 세 곳은 같은 포지션에서 점프 컷으로 리듬에 맞추고, 마지막 「탄탄탄」은 *여자아이의 액션*으로 음하메했다. 컷 점과 액션을 함께 쓰면 그루브감이 살고 단조로워지지 않는다고 추천한다. *타임리맵*(급가속·슬로)도 같은 발상으로, 컷 점 외의 음하메를 만드는 데 효과적이다.

![음하메 예시](/images/seedance2-liveaction-anime-mv/09-otohame.gif)

편집은 저자가 가장 좋아하는 작업이라 시간을 제일 많이 들인다.

> <strong>편집 시간은, 길면 길수록 즐겁다.</strong>

## 가장 흥미로운 지점

지난 콜라주 편의 결론이 *AI 영상 작업은 사진가의 일에 가깝다*였다면, 이번 편은 그 사진가가 다루는 *카메라가 한 단계 좋아졌을 때 무슨 일이 일어나는가*를 보여준다. 합성과 생성을 따로 하던 두 공정이 한 번의 생성으로 합쳐지자, 작업자가 손대는 곳이 *준비*에서 *통제*로 더 옮겨갔다. 배경을 만들지 않고, 합성 레퍼런스를 만들지 않고, 캐릭터 시트 한 장과 프롬프트만 남긴다. 도구가 좋아질수록 입력은 줄고, 줄어든 입력은 더 정교한 텍스트로 채워진다.

가장 흥미로운 건 *보색 콘트라스트*의 역설이다. 합성이 너무 자연스러워진 탓에, 이제는 *애니임을 일부러 드러내야* 작품이 성립한다. 도구가 위화감을 지워 버리면, 작업자는 *의도적으로 위화감을 다시 넣는* 일을 한다. 리얼리즘이 공짜가 된 순간, 비(非)리얼리즘이 디자인의 대상이 되는 것이다. 기술이 어떤 능력을 평준화하면, 가치는 그 능력의 *반대편*으로 옮겨간다 — 이 글은 그 패턴의 작은 사례다.

그리고 결국 *편집*이 가장 많은 시간을 먹는 인간의 작업으로 남는다. 생성이 100본을 토해내도, 尺을 정하고 음하메를 맞추고 타임리맵을 거는 일은 여전히 사람의 리듬 감각이다. 도구가 푸는 건 *소재의 양*이고, 사람이 쥐는 건 *순서와 박자*다.

## 출처

- 저자: tapehead.lab ([@tapehead_Lab](https://x.com/tapehead_Lab))
- 매체: note.com, 2026년 5월 27일
- 관련 작품: 「free will」 MV
- 원문: <https://note.com/tapehead/n/n86658f111f6d>
- 관련 글: [Seedance2.0으로 만드는 콜라주 애니메이션 (tapehead.lab)](/digest/seedance2-collage-animation-workflow/)
