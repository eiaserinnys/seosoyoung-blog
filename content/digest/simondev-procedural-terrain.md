---
title: "three.js로 절차적 지형을 그럴듯하게 만드는 트릭 열두 가지"
date: 2026-08-04T09:30:00+09:00
tags: ["게임 개발", "그래픽스", "three.js", "절차적 생성", "셰이더", "노이즈"]
categories: ["게임"]
summary: "SimonDev가 three.js 절차적 지형을 개선하는 트릭 열두 가지를 코드와 렌더 화면으로 공개했다. 값 노이즈 한 줄에서 시작해 fBM, 능선 노이즈, 미분 기반 침식, 높이 안개, 소광과 산란 분리까지 층층이 쌓는다. 같은 열한 가지 손잡이를 붙인 라이브 데모를 함께 실었다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/demo-cover.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/demo-cover.png"
---

## 3줄 요약

1. 그래픽스 교육 유튜버 SimonDev(@iced_coffee_dev)가 2026년 8월 3일 X에 올린 스레드다. three.js에서 절차적 지형을 더 그럴듯하게 만드는 트릭 열두 가지를 코드 몇 줄과 렌더 화면으로 하나씩 보여준다.
2. 트릭 대부분이 셰이더 서너 줄이다. 값 노이즈 한 줄로 시작해 fBM으로 겹치고, `abs`를 씌워 능선을 세우고, 노이즈의 미분으로 침식을 흉내 내고, 안개를 소광과 산란으로 갈라 놓는 식으로 층을 얹는다.
3. 값비싼 시뮬레이션은 한 번도 등장하지 않는다. 침식도 안개도 물리를 푸는 대신 결과만 닮은 근사로 대신하며, 그 근사들이 겹쳐 완성된 산악 풍경이 나온다.

## 열한 개의 손잡이를 직접 돌려보기

원문의 트릭을 같은 순서로 붙여 라이브 데모를 만들었다. 오른쪽 패널에서 주파수와 진폭을 밀어 보고, 노이즈 종류를 바꾸고, 침식과 테라스와 안개를 하나씩 켜면 각 트릭이 화면을 어떻게 바꾸는지 바로 보인다. 상단 PRESETS의 Basic부터 Full까지를 차례로 눌러 보면 아래 본문의 순서를 그대로 따라갈 수 있다.

<iframe src="/demos/simondev-procedural-terrain/" title="절차적 지형을 만드는 손잡이들" loading="lazy" allow="fullscreen" allowfullscreen style="width:100%;height:clamp(560px,62vw,720px);border:0;border-radius:16px;"></iframe>

원문이 도달한 지점은 이렇다. 안개에 잠긴 능선이 겹겹이 물러나는 60초짜리 비행 영상으로 스레드가 열린다.

![SimonDev의 완성 화면](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-00-intro.jpg)
*스레드 첫 게시물의 한 프레임. 아래 열두 가지가 모두 켜진 상태다.*

## 하이트맵

테셀레이션된 평면에서 출발해 각 정점의 높이를 계산한다. 예제는 값 노이즈를 샘플한다.

```glsl
height = noise(position.xy * frequency) * amplitude;
```

`frequency`는 노이즈를 샘플하는 xy 스케일을, `amplitude`는 지형의 높이를 정한다. 손잡이는 이 둘뿐이고, 결과는 완만한 언덕이다.

<video src="https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-01-heightmap.mp4" poster="https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-01-heightmap.jpg" muted loop playsinline controls style="width:100%;border-radius:12px;"></video>

*값 노이즈 구현과 그 결과. 좌하단 작은 사각형이 실제로 샘플되는 노이즈 텍스처다. (SimonDev)*

## fBM과 pow 재조형

값 노이즈 한 겹은 매끄럽고 단조로워 지형으로 쓰기엔 부족하다. fBM(fractional brownian motion)은 같은 노이즈를 서로 다른 스케일로 반복 샘플하며 디테일을 더해 나간다. 옥타브를 돌 때마다 진폭은 `persistence`만큼 줄고 좌표는 `lacunarity`만큼 조밀해진다.

여기에 `pow()`로 높이 분포를 다시 빚는다. 지수를 3 근처로 올리면 골짜기는 평탄해지고 봉우리는 도드라진다.

```glsl
float fbm(vec2 p) {
  float value = 0.0;
  float amplitude = 0.5;
  for (int i = 0; i < octaves; ++i) {
    value += amplitude * noise(p);
    amplitude *= persistence;
    p *= lacunarity;
  }
  value = value * 0.5 + 0.5;
  value = pow(value, exponentiation);
  return value * 2.0 - 1.0;
}
```

<video src="https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-02-fbm.mp4" poster="https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-02-fbm.jpg" muted loop playsinline controls style="width:100%;border-radius:12px;"></video>

*한 겹짜리 언덕이 산맥으로 바뀌는 구간. (SimonDev)*

## 능선 노이즈

아주 작은 변경으로 성격이 완전히 달라진다. 노이즈에 절댓값을 씌우고 1에서 빼면 골짜기였던 자리가 날카로운 능선으로 접힌다.

```glsl
height = 1.0 - abs(noise(position.xy * frequency));
```

![ridged 노이즈](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-03-ridged.jpg)
*한 줄을 바꿨을 뿐인데 매끈하던 언덕에 각진 마루가 생긴다. (SimonDev)*

## Voronoi 노이즈

성격이 다른 노이즈도 있다. 각 그리드 셀 안에 점을 하나씩 흩뿌리고, 지금 위치에서 가장 가까운 점까지의 거리를 높이로 쓴다. 주변 3×3 셀만 확인하면 완전히 다른 노이즈 함수가 된다.

```glsl
float voronoi(vec2 p) {
  vec2 cell = floor(p);
  vec2 local = fract(p);
  float nearest = 8.0;
  for (int y = -1; y <= 1; ++y) {
    for (int x = -1; x <= 1; ++x) {
      vec2 neighbour = vec2(x, y);
      vec2 point = hash22(cell + neighbour);
      float distance = length(neighbour + point - local);
      nearest = min(nearest, distance);
    }
  }
  return nearest;
}
```

![Voronoi 노이즈](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-04-voronoi.jpg)
*셀 경계가 그대로 드러난 상태. 아직 지형이라기보다 비늘에 가깝다. (SimonDev)*

## 겹치는 방식을 다른 노이즈에 적용하면

여기서 원문이 짧게 정리하는 대목이 있다. fBM은 별도의 노이즈 함수라기보다 노이즈를 겹치는 방식에 가깝다. 그러니 겹칠 대상을 바꾸면 그대로 다른 지형이 나온다. 앞의 능선 노이즈를 fBM으로 겹치면 훨씬 바위질 느낌이 된다.

```glsl
float fbmRidged(vec2 p) {
  float value = 0.0;
  float amplitude = 0.5;
  for (int i = 0; i < 8; ++i) {
    value += amplitude * ridgedNoise(p);
    amplitude *= persistence;
    p *= lacunarity;
  }
  return value;
}
```

![fBM과 능선 노이즈의 결합](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-05-fbm-ridged.jpg)
*능선이 여러 스케일로 겹쳐 바위산의 표면이 된다. (SimonDev)*

같은 트릭을 Voronoi에 적용하면 곰보 자국이 난 지형이 된다. 함수 안의 `ridgedNoise`를 `voronoi`로 바꾸는 것이 전부다.

![fBM과 Voronoi의 결합](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-06-fbm-voronoi.jpg)
*셀 구덩이가 여러 크기로 포개진 표면. (SimonDev)*

## 노이즈 미분으로 얻는 침식

노이즈의 미분값은 그 지점이 얼마나 가파른지 알려준다. 경사가 급한 자리에서 이후 옥타브의 진폭을 나눠 주면 가파른 면의 잔디테일이 줄고, 평범한 fBM이 풍화된 산의 모습으로 바뀐다. 침식 시뮬레이션 없이 얻는 값싼 침식이다.

```glsl
float weatheredFbm(vec2 p) {
  float value = 0.0;
  float amplitude = 0.5;
  vec2 derivative = vec2(0.0);
  for (int i = 0; i < 8; ++i) {
    vec3 n = noiseWithDerivative(p);
    derivative += n.yz;
    float erosion = 1.0 + dot(derivative, derivative);
    value += amplitude * n.x / erosion;
    amplitude *= persistence;
    p *= lacunarity;
  }
  return value;
}
```

![미분 기반 침식](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-07-erosion.jpg)
*능선을 따라 흘러내린 자국이 생긴다. (SimonDev)*

![우리 데모의 침식](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/demo-06-erosion.png)
*재구현 데모에서 풍화 강도만 올린 화면. 산등성이의 잔디테일이 눌리는 방향이 같다.*

## 테라스

또 하나의 값싼 조형 트릭이다. 높이를 계단으로 나누되 각 평탄면 사이에 짧은 램프를 남긴다. 모든 전이를 수직 절벽으로 만들지 않으면서 넓고 평평한 영역을 얻는다.

```glsl
height = fbm(position.xy * frequency);
float band = height * steps;
float level = floor(band);
float ramp = min(2.0 * fract(band), 1.0);
height = (level + ramp) / steps;
```

![테라스](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-08-terraces.jpg)
*계단참과 램프가 번갈아 나타나는 지형. (SimonDev)*

![우리 데모의 테라스](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/demo-07-terrace.png)
*계단 수를 아홉으로 둔 재구현 화면.*

## 테라스와 풍화를 함께

지금까지의 조각은 원하는 대로 섞을 수 있다. 원문의 예시는 저주파 테라스로 큰 형태를 잡고, 그 위에 풍화된 fBM을 고주파로 얹는 조합이다.

```glsl
float terraces = steppedFbm(position.xy * baseFrequency);
float weathering = weatheredFbm(position.xy * detailFrequency);
height = terraces + weathering * detailStrength;
```

![테라스와 풍화의 조합](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-09-combine.jpg)
*큰 단은 테라스가, 표면의 자잘한 요철은 풍화 fBM이 맡는다. (SimonDev)*

## 거리 안개

여기까지 오면 지형은 근사해 보이지만 깊이감이 없다. 가장 기본적인 대책은 거리 안개다. 카메라에서 멀어질수록 하늘을 흐리게 샘플한 색 쪽으로 블렌드한다. 동작은 하지만 멋있지는 않다는 것이 원문의 평가다.

```glsl
float fogAmount = smoothstep(fogNear, fogFar, distanceToCamera);
vec3 fogColor = sampleBlurredSky(viewDirection);
color = mix(color, fogColor, fogAmount);
```

![거리 안개](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-10-distance-fog.jpg)
*거리만 보는 안개는 화면 전체를 고르게 덮는다. (SimonDev)*

![우리 데모의 거리 안개](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/demo-09-distance-fog.png)
*재구현 데모에서 거리 안개만 켠 상태.*

## 높이 안개

Crytek이 2006년에 발표한 방식은 거리 대신 카메라에서 표면으로 향하는 레이를 따라 안개를 적분한다. 밀도가 고도에 따라 지수적으로 얇아진다고 두면 적분이 닫힌 형태로 풀린다. 골짜기는 안개로 차오르고 봉우리는 상대적으로 맑게 남는다.

```glsl
vec3 applyHeightFog(vec3 color, vec3 worldPosition) {
  vec3 ray = worldPosition - cameraPosition;
  float viewerHeight = cameraPosition.y - fogBaseHeight;
  float fogIntegral = length(ray) * exp(-heightFalloff * viewerHeight);
  float t = heightFalloff * ray.y;
  if (abs(t) > 0.01) {
    fogIntegral *= (1.0 - exp(-t)) / t;
  }
  float transmittance = exp(-density * fogIntegral);
  vec3 fogColor = sampleBlurredSky(normalize(ray));
  return mix(fogColor, color, transmittance);
}
```

![Crytek 높이 안개](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-11-height-fog.jpg)
*같은 지형이지만 안개가 골짜기에 고인다. (SimonDev)*

![우리 데모의 높이 안개](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/demo-10-height-fog.png)
*재구현 데모에서 높이 안개를 켜고 밀도를 올린 화면.*

## 소광과 산란

마지막 트릭은 앞의 함수에서 두 줄을 바꾼다. 안개를 한 가지 색으로 섞는 대신 두 계산으로 가른다. 소광(extinction)은 빛이 얼마나 잡아먹히는지를, 산란(in-scattering)은 안개 자체가 얼마나 밝게 빛나는지를 맡는다. 실루엣은 더 어두워지고 헤이즈는 더 밝아져 대비가 살아난다.

```glsl
float transmittance = exp(-extinction * fogIntegral);
float scattering = 1.0 - exp(-inScattering * fogIntegral);
vec3 fogColor = sampleBlurredSky(normalize(ray));

return color * transmittance + fogColor * scattering;
```

![소광과 산란 분리](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/src-12-scattering.jpg)
*안개 낀 골짜기가 밝아지고 앞쪽 바위는 더 어둡게 가라앉는다. (SimonDev)*

![우리 데모의 소광과 산란](https://img.seosoyoung.eiaserinnys.me/images/simondev-procedural-terrain/demo-11-scattering.png)
*재구현 데모에서 소광과 산란을 나눈 최종 상태.*

## 가장 흥미로운 지점

내가 두 번 돌려 본 것은 일곱 번째 트릭이다. 침식은 보통 물을 흘리고 퇴적을 누적하는 시뮬레이션으로 얻는다. 원문은 그 대신 노이즈의 미분을 이미 가지고 있다는 점을 이용한다. 경사가 급한 곳에서 다음 옥타브의 기여를 나누어 줄이면, 물 한 방울 굴리지 않고도 물이 깎아 낸 것처럼 보이는 표면이 나온다. 원인을 흉내 내는 대신 결과가 남긴 통계만 흉내 낸 셈이다.

안개를 소광과 산란으로 가르는 마지막 트릭도 같은 종류의 절약이다. 산란 방정식을 제대로 적분하는 대신, 눈이 알아채는 두 가지 효과만 따로 계산해 더한다. 열두 가지 중 물리적으로 옳은 것은 하나도 없지만 화면은 매번 좋아진다.

원문이 스레드를 닫으며 남긴 문장도 옮겨 둔다.

> 이것들이 무엇을 하는지 배워 두면 AI에게 더 잘 프롬프트할 수 있다.

## 출처

SimonDev(@iced_coffee_dev), 2026년 8월 3일 X 스레드
원문: <https://x.com/iced_coffee_dev/status/2084276803833581736>
원본 라이브 데모: <https://simondev.io/demos/gamedev/>

본문의 영상과 스크린샷 중 SimonDev 표기가 붙은 것은 원문 스레드의 자료이며, 나머지는 같은 트릭을 붙여 다시 만든 [라이브 데모](/demos/simondev-procedural-terrain/)에서 캡처했다. 코드는 원문 화면에 표시된 것을 그대로 옮겼다.
