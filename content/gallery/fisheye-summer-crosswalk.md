---
title: ""
date: 2026-05-14T18:19:37+09:00
slug: "fisheye-summer-crosswalk"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk/cover.png"
  hiddenInList: false
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. *모던 일본 애니메이션 + 어안 렌즈 왜곡 + 하이키 사이키델릭 + 한여름 거리*라는 공통의 결을 가진 두 이미지를 같은 시드·같은 패턴으로 빚었다. 본 커버는 횡단보도 위 하이앵글 인물, 두 번째 이미지는 같은 결을 4:3 가로로 변주한 *유리창 너머 손바닥* 컷.
2. 핵심 규칙은 *서소영 시드의 헤어스타일만 차용 / 시드의 화풍·얼굴·의상은 버리고 프롬프트 기준으로 새로 그리기*였다. 첫 시도(시드의 얼굴·헤어 모두 유지)는 시드의 일러스트 톤이 결과를 지배해 폐기 — 시드를 포트레이트로 바꾸고 차용 범위를 헤어로만 좁히니 톤이 비로소 살아났다.
3. *한 번에 한 축씩만 움직인다*는 원칙이 결정적이었다. 두 번째 이미지의 한 단계에서 어안·화이트아웃·인파·뭉게구름을 동시에 입혔다가 시드 톤에서 멀어졌고, 클로즈업·플레어·의상 교체를 각각 한 단계씩 분리해 굴리니 효과가 또렷이 보였다.

## 의도와 시드

사용자가 던진 두 한국어 프롬프트가 출발점이었다. 둘 다 같은 결을 갖되 포즈와 시점이 달랐다.

- 첫 번째 — 하이앵글에서 캐릭터를 내려다보고, 캐릭터도 카메라 쪽으로 팔을 뻗고 올려다본다.
- 두 번째 — 유리창 너머에서 손바닥을 유리에 대고 얼굴을 가까이 댄 자세. 4:3 가로 프레임으로 iPad 배경으로도 활용.

서소영의 정체성은 갤러리 정본 `서소영 (포트레이트).png`로 두고, 차용 범위를 *헤어스타일*로만 좁혔다. 얼굴·표정·의상·포즈·구도·화풍은 시드를 따르지 않고 프롬프트가 명시한 모던 일본 애니메이션 톤으로 새로 그렸다.

## 첫 번째 이미지 — 횡단보도의 어안

### 1단계 · 오리지널 (시드 없음, 프롬프트 그대로)

시드 없이 사용자의 한국어 프롬프트만으로 두 장을 굽었다 — 시드 사용 카드와 비교하기 위한 *원본 의도의 기준선*. 1024x1024 / low.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk-orig/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk-orig/v1.png" alt="original v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">A. 원본 후보 하나</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk-orig/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk-orig/v2.png" alt="original v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">B. 원본 의도 정본 ← 선택</figcaption>
  </figure>
</div>

사용자는 B를 *원본 의도의 정본*으로 선택했다. 본 카드의 헤더는 여기서 출발해 서소영 시드를 입히는 길로 분기한다.

### 2단계 · 첫 시도 — `서소영.png`(풀바디) 시드, 얼굴·헤어 모두 차용

`서소영.png`(풀바디 한복 일러스트)를 시드로 박고 *얼굴과 헤어스타일을 정확히 유지*하면서 의상만 갈아입히는 방식으로 시안 3장을 굴렸다. 결과는 *시드의 일러스트 화풍*을 그대로 따라간 그림이었다 — 가는 선·플랫 채색·사이키델릭의 결이 죽었다.

> 서소영은 너무 원본 그림체를 따라갔네. 헤어스타일만 참고하라고 하는 게 좋을 거 같아.

원인은 명확했다. (1) 시드가 풀바디 한복이라 의상·색감·화풍 정보까지 모델이 학습 신호로 받았고, (2) "얼굴 + 헤어를 유지하라"는 지시가 사실상 *시드 그림 전체를 유지하라*로 해석됐다.

### 3단계 · 시드 변경 + 차용 범위 축소

시드를 `서소영 (포트레이트).png`로 바꾸고, 프롬프트 첫머리에 *시드의 그림체·얼굴·표정·의상·포즈는 따르지 않는다, 헤어스타일만 참고한다*는 분리 지시를 명시적으로 박았다. 톤이 살아났고 어안 왜곡과 사이키델릭 팔레트가 제대로 들어왔다. 사용자는 *포즈·의상·구도*가 좋다고 짚었고, 화풍만 한 번 더 다듬기로 했다.

### 4단계 · 화풍 리파인 — 시안 3에서 출발

3단계의 시안 3을 시드로 다시 박고 *포즈·의상·구도는 그대로, 화풍만 더 단순한 선·플랫 채색·하이키 사이키델릭·색수차 강조*로 한 번 더 굴렸다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk/v1.png" alt="refine v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1. 가장 자연스러운 결 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk/v2.png" alt="refine v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 색면이 더 평면적</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-summer-crosswalk/v3.png" alt="refine v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 색수차가 강조됨</figcaption>
  </figure>
</div>

### 5단계 · 2048x2048 high 정본 업스케일

v1을 시드로 박고 `--size 2048x2048 --quality high`로 한 번 더 굴렸다. 약 4분 45초, 7MB. 가는 선과 색수차가 정밀하게 정돈된 결이 본 카드의 커버다.

## 두 번째 이미지 — 유리창 너머의 손바닥

첫 카드의 결을 다른 포즈로 한 번 더 — 4:3 가로 프레임으로 iPad 배경 활용까지 염두에 둔 변주. 시드 사용 방식은 첫 카드의 *3단계 패턴*을 그대로 가져왔다.

### 1단계 · 첫 시도

`서소영 (포트레이트).png` 시드 + 헤어만 차용 + 유리창 너머 손바닥 포즈로 시안 3장. 톤이 자연스럽게 들어왔고 사용자는 v3의 *포즈·구도*를 베이스로 다음 단계를 요청했다.

### 2단계 · 한 호출에 너무 많은 변경 — 회귀

> 조금 더 왜곡을 늘리고 사이키델릭한 색감을 강조해보자. 뒤에 보이는 도시를 거의 흰색에 가깝게 날리고, 사람들이 거리를 메우고 오가는 느낌. 멀리 하늘에 높이 솟은 뭉게구름.

1차 v3를 시드로 박고 어안 강화·도시 화이트아웃·인파·뭉게구름·색수차 등을 한 호출에 입혔다. 사용자의 한 마디.

> 이전 v3가 나은데? 이전 v3의 인물 포즈 구도를 유지하고 조금 더 클로즈업.

여러 축을 동시에 움직인 결과 시드 톤에서 더 멀어졌다. *한 번에 한 축씩*이라는 원칙으로 회귀.

### 3단계 · 클로즈업 + 채도 한 단계

1차 v3를 다시 시드로 박고 클로즈업과 채도만 살짝 올렸다. 시안 v3가 자연스럽게 떨어졌다.

### 4단계 · 우상단 렌즈 플레어 + 여름 반팔 프린트 티

3차 v3를 시드로 박고 두 가지를 입혔다 — *의상을 한여름 반팔 프린트 티셔츠로 교체* + *우상단에서 들어오는 렌즈 플레어*. 한 호출에 두 변경이지만 둘 다 시드의 결과 자연스럽게 어울리는 가산형 변경이었다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-window-press/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-window-press/v1.png" alt="window v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 플레어가 가장 또렷</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-window-press/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-window-press/v2.png" alt="window v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v2. 균형 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-window-press/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-window-press/v3.png" alt="window v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 프린트 티 가장 또렷</figcaption>
  </figure>
</div>

### 5단계 · 2048x1536 high 정본 업스케일 (iPad 4:3 네이티브)

v2를 시드로 박고 `--size 2048x1536 --quality high`로 굴렸다. 첫 시도에서는 본문 프롬프트를 길게 동봉했더니 모델이 *재렌더*로 받아 구도가 미세하게 재해석됐다. 사용자의 지적.

> v3하고 구도 같은 게 다른데? v3를 그대로 업스케일한 게 아니야?

두 번째 시도에서 프롬프트를 *픽셀 디테일만 올리고 구도는 일절 건드리지 마라* 수준으로 축약하고 보존 지시만 영문으로 또렷이 박았다. 드리프트가 줄었다.

<div style="display:flex;justify-content:center;margin:20px 0;">
  <figure style="max-width:540px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-window-press/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/fisheye-window-press/cover.png" alt="window press final" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;text-align:center;">두 번째 이미지 정본 (2048x1536, iPad 4:3 네이티브)</figcaption>
  </figure>
</div>

이 이미지는 별도 카드로 발행하지 않는다 — 첫 카드와 컨셉이 같고 본질적으로 *iPad 배경용 변주*이기 때문이다. 본 카드의 제작기에 함께 보존한다.

## 가장 흥미로운 지점

**시드는 한 가지만을 위한 도구다.** 서소영 시드를 *얼굴 + 헤어 + 의상 보존*으로 쓰면 시드의 화풍이 통째로 결과를 지배한다. *헤어스타일만* 같은 좁은 차용이 분명하게 시드의 일러스트 톤을 떼어내고, 프롬프트가 명시한 새 화풍이 비로소 들어온다. 시드 사용은 *무엇을 가져올지*를 한 가지로 좁히는 작업이다 — 모호하게 "비슷한 느낌"을 요구하면 시드가 결과를 통째로 끌어간다.

**한 번에 한 축씩 움직인다.** 두 번째 이미지의 2단계가 패착이었다 — 어안 강화·도시 화이트아웃·인파·뭉게구름을 한 호출에 모두 입히니 어느 변경이 효과를 냈는지 추적이 어려워졌고, 결과적으로 시드의 톤에서 멀어졌다. 사용자의 회귀 지시 후 클로즈업·플레어·의상 교체를 각각 한 단계씩 분리해 굴리니 각 변경의 효과가 또렷이 보였다. 단, 4단계의 *플레어 + 의상 교체*는 둘 다 가산형(시드 위에 새 요소를 더하는)이라 한 번에 같이 입혀도 무리가 없었다. 동시 변경이 패착인 경우는 *서로의 효과를 가리는* 경쟁적 변경일 때다.

**gpt-image-2 edit의 "업스케일 환상".** 이 엔드포인트는 진짜 픽셀 업스케일이 아니라 *재렌더*다. 사이즈를 늘리면 모델은 *고해상도로 다시 그리라*로 받는다. 프롬프트가 길수록 *재해석*이 일어나 구도가 미세하게 흐트러진다. 두 번째 이미지의 정본 업스케일에서 영문으로 *upscale-only*를 또렷이 박아 드리프트를 줄였지만, 100% 픽셀 보존이 필요한 경우는 외부 도구(waifu2x·Real-ESRGAN)가 정답이다.

**iPad 배경 → 4:3 가로.** gpt-image-2가 정확히 4:3을 지원하지 않을 줄 알았지만 `2048x1536`이 통과했다. iPad의 네이티브 비율(4:3)에 정확히 맞는 사이즈로 굽으니 배경 활용 시 추가 크롭이 필요 없다. 모델의 지원 사이즈 목록은 공식 문서보다 실험으로 검증하는 편이 빠르다.

## 첫 번째 이미지의 원본 프롬프트

```
모던 일본 애니메이션 스타일의 미소녀 캐릭터
가는 선, 플랫한 채색, 사이키델릭한 색감
눈, 턱선 등이 동글동글한 인상
하이앵글에서 캐릭터를 내려다보고 있고 캐릭터도 카메라 쪽으로 팔을 뻗고 쳐다보고 있음
어안 렌즈처럼 화면의 왜곡이 과장되어 그려짐
스웨터, 플레어스커트, 무릎 위로 올라오는 양말
하이키의 밝고 맑은 색감
횡단보도가 있는 번화가의 거리 풍경
습한 여름날의 밝은 태양광
구름 그림자
```

## 두 번째 이미지의 원본 프롬프트

```
모던 일본 애니메이션 스타일의 미소녀 캐릭터
가는 선, 플랫한 채색, 사이키델릭한 색감
눈, 턱선 등이 동글동글한 인상
유리창 너머에서 손바닥을 대고 얼굴을 가까이 대고 안쪽을 보고 있는 것 같은 포즈
어안렌즈처럼 보임
스웨터, 플레어스커트, 무릎 위로 올라오는 양말
하이키의 밝고 맑은 색감
횡단보도가 있는 번화가의 거리 풍경
습한 여름날의 밝은 태양광
구름 그림자
색수차
어안렌즈 같은 왜곡
4:3 비율
```

## 출처

사용자가 직접 작성한 두 한국어 프롬프트.
