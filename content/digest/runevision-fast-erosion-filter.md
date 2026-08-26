---
title: "Fast and Gorgeous Erosion Filter"
date: 2026-07-09T23:30:00+09:00
tags: ["게임", "게임 개발", "절차적 생성", "셰이더", "지형 생성"]
categories: ["게임"]
summary: "World Machine 스타일의 침식 지형을, 시뮬레이션 없이 단일 픽셀 셰이더 한 패스로 재현하는 필터의 8개월치 발전 기록. Rune Skovbo Johansen이 Clay John(2018)·Fewes(2023) 계보 위에 fade approach와 stacked fading을 새로 얹었다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/ErodedTerrain.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/ErodedTerrain.png"
---

## 3줄 요약

1. Rune Skovbo Johansen이 2018년 Clay John · 2023년 Fewes의 Shadertoy 계보를 이어받아, World Machine 스타일의 침식 지형을 **시뮬레이션 없이 단일 픽셀 셰이더 한 패스**로 재현하는 필터를 8개월간 발전시킨 기록이다.
2. 핵심은 노이즈에서 gully(도랑)를 만드는 stripe를 뽑고, fade target + stacked mask 조합으로 옥타브를 층층이 쌓아 분기하는 gully와 선명한 능선을 만들되, 모든 지점을 독립 평가 가능하게 유지하는 것이다. 청크 생성·GPU 병렬 친화라는 특성이 그대로 남는다.
3. 코드는 MPL v2로 공개되어 이미 Unity Burst, Unreal Landmass, Godot, Blender Geometry Nodes, Houdini, Hytale Worldgen v2 등으로 광범위하게 포팅되었다.

## 배경 — Clay John에서 Fewes를 거쳐

물방울 낙하 시뮬레이션 기반 침식은 두 가지 문제가 있다. 느리고, 청크 단위 생성이 어렵다. 그래서 결과물의 외형만 흉내내는 필터 계열이 오랫동안 탐구되어 왔다.

2018년 Shadertoy 사용자 Clay John이 올린 [Eroded Terrain Noise](https://www.shadertoy.com/view/MtGcWh)가 원점이다. Clay John은 이렇게 적었다.

> This shader is the result of a long time dreaming of a noise function that looked like eroded terrain, complete with branching structure, that could be run in a single pass pixel shader. I wanted to avoid anything simulated because then you cannot easily make infinite terrains.

2023년 Felix Westin(Fewes)이 이 위에 [Terrain Erosion Noise](https://www.shadertoy.com/view/7ljcRW)로 개선판을 얹었다. 침식 효과를 미세 조정하고, 프레젠테이션을 훨씬 정돈된 형태로 다듬었다.

Rune Skovbo Johansen은 2025\~2026년 동안 이 기법을 자기 방식으로 다시 구현했다. 처음에는 기존 방식의 몇 가지 단점을 손보고 파라미터를 직관적으로 정리한 버전을, 그다음에는 완전히 다른 방식으로 동작하며 더 선명한 gully와 능선을 만드는 버전을 만들어냈다. 이 글은 그 여정 전체의 정리다.

## 기본 아이디어 — 경사 방향으로 stripe를 얹는다

높이 함수의 각 지점에서 기울기(gradient), 즉 가장 가파른 오르막의 방향과 세기를 알 수 있다고 가정하자. 물은 그 반대 방향으로 흐른다.

이 기울기 방향을 따라 stripe(줄무늬)를 얹으면, 그 stripe가 만들어내는 오목·볼록이 그럴싸한 gully와 능선처럼 보인다.

stripe 자체도 경사를 가지므로, 원래 기울기와 stripe의 기울기를 더해 새 기울기를 만든다. 다음 옥타브에서는 그 새 기울기를 따라 더 작은 stripe를 얹는다. 이 과정을 옥타브(octave) 단위로 반복하면, 각 옥타브의 gully가 이전 옥타브에서 만들어진 경사를 따라 자연스럽게 분기된다.

![여러 옥타브의 gully가 층층이 쌓인 경사면](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/Slant3.png)

*여러 옥타브의 gully가 이전 옥타브의 경사를 따라 분기하며 쌓인다.*

이걸 그대로 실제 지형에 적용하면 문제가 드러난다. 기울기가 위치마다 달라지는 상황에서 stripe 패턴을 회전시키면 카오스한 무늬가 나온다.

![카오스한 stripe](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/ChaoticGullies.png)

*기울기에 맞춰 stripe 패턴을 회전시키면 카오스한 결과가 나온다.*

## stripe를 셀 단위로 회전시키기

stripe 패턴을 어떤 pivot point 하나를 중심으로 회전시키면, pivot에서 멀어질수록 왜곡이 커진다. 회전 각도가 조금만 바뀌어도 그 지점에서 "어느 stripe 위에 있는지" 자체가 바뀌기 때문이다.

해법은 격자 셀 단위로 pivot을 하나씩 두는 것이다. Worley noise처럼 각 셀 안에 랜덤 위치의 pivot을 배치하고, 각 셀은 자기 pivot을 중심으로 stripe를 회전시킨다. pivot이 너무 멀어질 일이 없어 왜곡이 감당 가능한 수준으로 줄어든다.

셀 간 경계에서 불연속이 생기지 않도록 이웃 셀의 stripe를 블렌딩한다. stripe는 본질적으로 코사인(높이)·사인(기울기) 파형의 압출이라, 정렬되지 않은 두 사인파를 블렌딩하면 진폭이 줄어든 새로운 사인파가 나온다. 이 성질 덕분에 블렌딩만으로도 정렬되지 않은 stripe들이 연속된 하나의 stripe처럼 이어진다.

![셀 간 stripe 블렌딩](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/CellsBlended.png)

*이웃 셀의 stripe를 블렌딩하면 정렬되지 않은 stripe들도 연속된 하나의 gully로 이어진다.*

## 봉우리를 지키는 두 접근 — Frequency vs Fade

이대로는 산의 봉우리와 골짜기가 이상하게 보인다. 봉우리 근처에서 기울기가 0에 가까워지면 방향이 정의되지 않아 stripe 패턴이 급격히 요동친다.

Clay John과 Fewes의 원래 접근은 frequency approach다. stripe의 주기(빈도)를 기울기에 비례시켜서, 평평한 곳에서는 stripe가 무한히 두꺼워지도록 만든다. 각 셀 중앙에 흰색(=능선) stripe가 위치하도록 설계되어 있어, 봉우리와 골짜기는 항상 "능선" 위에 놓인다. 봉우리 보존은 잘되지만, 골짜기 바닥에 볼록한 혹(bulge)이 생기는 부작용이 있다. Clay John과 Fewes는 저지대에서 침식 효과를 페이드 아웃시켜 이 문제를 우회했다.

Johansen이 새로 제안한 것이 fade approach다. stripe의 폭은 고정하고, 대신 기울기가 0에 가까워지는 지점에서 stripe를 페이드 아웃시킨다. 이때 페이드하는 목표값(fade target)을 봉우리에서는 흰색(+1), 골짜기에서는 검은색(-1)으로 두면 봉우리는 뾰족하게, 골짜기는 V자로 선명하게 유지된다.

![Fade approach로 얻은 뾰족한 봉우리와 V자 골짜기](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/TerrainUniformFreqSmoothingOffWithInvPow5.png)

*fade approach는 봉우리와 골짜기를 동시에 선명하게 유지한다.*

fade target은 고도(altitude) 등을 기준으로 사용자가 함수 입력으로 넘기도록 설계했다.

```
float inverse_lerp(float a, float b, float v) {
    return (v - a) / (b - a);
}

// 고도를 -1~1 범위로 변환
float fadeTarget =
    inverse_lerp(valleyAlt, peakAlt, h) * 2.0 - 1.0;
```

초기에는 기울기의 제곱근을 침식 강도로 썼는데, 이 함수는 원점에서 수직으로 시작해 아주 미미한 기울기에도 침식이 급격히 증가하는 특성이 있어 봉우리 근처에서 불연속이 만들어졌다. 대체 함수로 `1 - (1 - saturate(t))^2`, 즉 제곱근을 대각선으로 뒤집은 곡선을 쓰면 시작부가 완만해져 이 불연속이 대부분 사라진다.

## Stacked Fading — 옥타브마다 fade target을 다시 쓴다

Johansen이 새로 제안한 핵심 개선이다. 봉우리와 골짜기에서 침식을 페이드했다면, 이전 옥타브에서 만들어진 능선과 골 위에서도 같은 처리를 해야 한다는 발상이다.

각 옥타브를 마칠 때마다 fade target과 mask를 갱신한다. 옥타브 N의 gully를 계산한 뒤, 그 결과 자체를 옥타브 N+1의 새로운 fade target으로 쓴다. mask도 옥타브 N의 능선·골에서 불투명해지도록 새 기여분을 곱해 누적한다.

![Stacked fading의 옥타브 간 정보 흐름](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/FlowChart.png)

*fade target과 mask가 각 옥타브에서 어떻게 갱신되어 다음 옥타브로 전달되는지의 흐름도.*

이렇게 하면 옥타브가 늘어날수록 이전 능선과 골이 이후 gully의 영향 범위를 점점 좁힌다. 결과적으로 큰 gully의 능선이 작은 gully에 의해 잘려나가지 않고 선명하게 유지된다.

`combiMask = pow_inv(combiMask, detail) * newMask` 같은 형태로 mask를 결합하면 `detail` 파라미터로 고빈도 gully를 어느 정도 가파른 경사에만 제한할지 조절할 수 있다.

## Normalized Gullies — gully 크기의 일관성

블렌딩된 stripe는 정렬 정도에 따라 진폭이 들쭉날쭉하다. gully 크기가 일정치 않으면 능선·골이 선명하게 나오지 않는다.

Johansen이 발견한 것은, 코사인·사인 쌍을 단위원 위의 한 점으로 보고 그 점을 다시 반지름 1로 정규화하면 진폭을 일정하게 맞출 수 있다는 사실이다. 다만 사인·코사인이 완전히 상쇄되는 지점(반지름이 0에 근접)에서 정규화를 하면 스파이크·구멍 같은 아티팩트가 생긴다. 그래서 일정 임계값(예: 0.5) 이상인 벡터만 정규화하는 부분 정규화를 선택했다.

![부분 정규화가 만들어낸 일관된 gully 크기](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/NormalizedHalf.png)

*임계 이상의 벡터만 정규화하면 균일한 gully와 능선을 얻으면서 스파이크는 피할 수 있다.*

이렇게 얻은 방향성 있는 노이즈는 침식 외에도 유용하다고 판단해 [Phacelle Noise](https://blog.runevision.com/2026/01/phacelle-cheap-directional-noise.html)라는 이름으로 별도 함수로 분리해 공개했다.

## Straight Gullies — 깔끔한 분기

능선이 선명해지자 새 문제가 보였다. 작은 gully가 큰 gully와 나란히 흐르다가 나중에야 분기되는 현상이다.

이유는 stripe 모델의 한계다. gully 옆면에서는 지형 경사가 gully 방향에서 벗어나 있지만, gully 바닥과 능선 꼭대기에서는 경사에 거의 영향을 주지 못한다. 그래서 그 지점 위에서는 작은 gully가 큰 gully와 나란히 흐른다.

해법은 가짜 경사 사용이다. sin 파형의 값을 그대로 쓰지 말고 부호만 취해 -1 또는 1로 대체한다. 이는 gully가 사인 파형이 아니라 삼각 파형처럼 위·아래 어디서든 일정한 경사를 유지한다고 가정하는 것과 같다.

![Straight gullies 기법이 만든 깔끔한 능선 분기](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/straight_gullies_on_zoom.png)

*직선 gully 기법을 적용한 뒤의 능선·골 — 큰 능선에서 작은 능선이 깔끔한 각도로 분기한다.*

여기서 흥미로운 부분은, 출력용 미분값과 내부용 미분값을 병렬로 관리했다는 점이다. 출력 미분값은 여전히 mask를 적용받아 능선·골에서 0으로 페이드되지만, 내부의 직선 gully용 미분값은 mask를 적용하지 않고 유지한다. 이렇게 분리하지 않으면 직선 gully 기법이 무너진다.

## 뾰족 봉우리 · 능선 라운딩 · 물빠짐

**Pointy peaks.** gully를 정규화하면 봉우리가 원래 높이 함수의 둥근 형태에 가까워진다. 이걸 다시 뾰족하게 만들려고 별도 처리를 시도했으나, 결국 훨씬 단순한 해법을 찾았다. faded gully의 gully 성분을 어떤 비율(예: 0.5)로 축소하는 동시에 침식 강도를 그 역수(2.0)만큼 키운다.

![gully weight와 침식 강도의 조합으로 얻는 뾰족한 봉우리](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/GullyWeight.png)

*왼쪽 위: 침식 없음. 오른쪽 위: 침식 적용, 봉우리 뭉툭. 왼쪽 아래: gully weight를 0으로 낮춰 봉우리만 보임. 오른쪽 아래: 강도 2배 · gully weight 절반으로 뾰족 봉우리와 gully 공존.*

**Rounding of ridges and creases.** 실제 능선은 완전 칼날이 아니고, 골 바닥은 퇴적으로 둥글어질 수 있다. mask의 shaping function 뒤에 크기 조절 가능한 ease-in 함수를 연결해 능선과 골의 라운딩을 각각 다르게 조절할 수 있게 만들었다.

![능선·골 라운딩의 각각 조절](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/Rounding.png)

*라운딩 없음, 능선만, 골만, 둘 다 라운딩 적용.*

**Water drainage.** 침식이 충분히 선명해지자 "이 기법으로 분기하는 하천망도 그릴 수 있지 않을까"라는 아이디어에 도달한다. 마지막 옥타브를 마스크로 중립값(회색)으로 페이드시키면 능선·골의 분포를 담은 ridge map이 나온다. 이 ridge map을 텍스처링에 얹으면 물이 흘러내리는 자국(dendritic drainage)을 그럴싸하게 표현할 수 있다.

![Ridge map을 지형에 얹은 결과](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/RidgemapTerrain.png)

*능선을 흰색, 골을 검정으로 표시한 ridge map을 지형에 시각화한 것.*

블렌딩된 stripe로는 완전히 이어지는 선을 항상 얻을 수는 없어, 산 중턱에서 gully와 물길이 끊기는 일이 발생한다. 정확도가 크게 중요치 않은 용도에는 충분하다.

여기까지 다 적용한 최종 지형은 이렇다.

![최종 텍스처링을 얹은 지형](https://img.seosoyoung.eiaserinnys.me/images/runevision-fast-erosion-filter/NewTerrainTextured.png)

*바위·흙·풀·나무·물빠짐 자국까지 얹은 최종 지형.*

## 실제 어디에 쓰이는가

Johansen은 코드를 MPL v2로 공개했다. 아티클이 나온 뒤 다양한 엔진·툴로 포팅되어 다음이 공개되어 있다.

- 온라인 데모: [optozorax의 optolab_wasm](https://optozorax.github.io/optolab_wasm/?scene=erosion_filter) 파라미터 조절 데모
- Unity Burst: [Luke Mitchell의 AdvancedTerrainErosion](https://github.com/lpmitchell/AdvancedTerrainErosion) (Reddit 공개)
- Unity Shader Graph: [Jens Maier의 erosionFilter](https://github.com/Jens-Maier/erosionFilter)
- Unreal Landmass: [Michael Kinsey의 트위터 포스트](https://x.com/MichaelKinsey3D/status/2043407307984523608)
- Godot: [Henry의 Godot forum 포스트](https://forum.godotengine.org/t/fast-and-gorgeous-erosion-filter/136436)
- Blender Geometry Nodes: [Jérémy Derlande(Kollapse3D)의 Quick Erosion Filter](https://kollapse3d.gumroad.com/l/nhrvg)
- Houdini: [eetu의 dailyhip 블로그 구현](https://dailyhip.wordpress.com/2025/07/23/erosion-filter/)
- Leveller (heightmap 툴): Ray Gardener가 [v4.4에 통합](https://www.daylongraphics.com/support/lev44_upgrade.php)
- PNG 웹 위젯: [Robert Winslow의 웹 위젯](https://blog.rmwinslow.com/maps/erosion)
- Hytale Worldgen v2: [Verday의 구현](https://github.com/ItsVerday/Hytale_Worldgen_Additions)

Johansen의 최종 iteration은 Shadertoy [Advanced Terrain Erosion Filter](https://www.shadertoy.com/view/wXcfWn)와 [Mouse-Paint Eroded Mountains](https://www.shadertoy.com/view/sf23W1)에서 직접 조작해볼 수 있다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 저자가 코멘트 답변에서 "발표 이후 여러 사람이 curvature(2차 미분)를 fade target으로 쓰라고 제안했지만, 모든 입력 높이 함수에서 2차 미분을 뽑아 넣기가 부담이고, curvature 자체도 [-1, 1] 범위가 아니라 별도 wrangling이 필요해서 결국 altitude를 그대로 쓰기로 했다"고 밝힌 부분이다.

이 대답이 흥미로운 이유는, 이 기법 전체가 "완벽한 물리적 정확성보다 GPU·병렬 친화적인 근사"라는 하나의 방향으로 일관되게 정렬되어 있다는 사실을 코멘트 답변 한 줄에서 다시 확인할 수 있기 때문이다. 저자는 논문에 들어갈 만한 curvature 기반 해법을 명시적으로 인지하고도, "구현 부담"과 "사용자에게 결정을 맡기는 것이 낫다"는 판단으로 물러섰다. Advanced Terrain Erosion Filter라는 결과물은 이런 결정들이 모여 만들어진 것이다.

또 하나는 "분석적 미분값을 정확히 만들려고 초기에 상당한 시간을 썼지만, 결국 출력용 미분값은 아무 데도 쓰이지 않았고, 내부용 미분값은 오히려 정확도보다 straight gullies를 위한 가짜 값이 더 유용했다"는 회고다. 8개월 여정의 큰 부분이 이런 "정확성을 목표로 삼았다가 실용에 굴복한 우회"로 이뤄져 있다. 이런 부분이 짧게라도 남아 있는 것이 Fewes와 Clay John의 Shadertoy와 이 아티클을 결정적으로 구별해준다.

## 출처

Rune Skovbo Johansen, ["Fast and Gorgeous Erosion Filter"](https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html), Rune's Dev Blog, 2026-03-30.
동영상 설명: [Fast & Gorgeous Erosion Filter Explained](https://www.youtube.com/watch?v=r4V21_uUK8Y) (YouTube).
코드: MPL v2, Shadertoy [Advanced Terrain Erosion Filter](https://www.shadertoy.com/view/wXcfWn) 및 [Mouse-Paint Eroded Mountains](https://www.shadertoy.com/view/sf23W1).
계보: Clay John(2018) [Eroded Terrain Noise](https://www.shadertoy.com/view/MtGcWh), Felix Westin(Fewes, 2023) [Terrain Erosion Noise](https://www.shadertoy.com/view/7ljcRW).
