---
title: ""
date: 2026-05-14T22:39:18+09:00
slug: "tokyo-tower-fisheye-stripes"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/cover.png"
  hiddenInList: false
  focus: "50% 30%"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. *도쿄타워 꼭대기에 선 소녀 + 하이앵글 어안 + 스웨터·플레어 미니·오버니 스트라이프 양말*이라는 사용자의 의상 지정 요청에서 출발해, 풀바디 베이스 → 얼굴 클로즈업 + 왜곡 강화 + 색온도 다운 → 2048x2048 high 업스케일의 세 라운드로 빚은 어안 풀바디 카드.
2. 라운드 1은 `서소영.png`(풀바디 일러스트) 단독 시드로 *원본 의도의 풀바디 베이스*를 잡고, 라운드 2는 라운드 1의 선택 컷을 컴포지션 시드로, `서소영.png`를 정체성 시드로 *두 장 동시 입력*해 카메라를 얼굴로 당기는 한 축만 움직였다.
3. 본 카드는 *한 번에 한 축씩* 움직이며 베이스 → 클로즈업 → 업스케일로 분리한 결과다. 마지막 단계는 `2048x2048 high`의 upscale-only 프롬프트로 구도·표정·색감·포즈를 동결하고 픽셀 디테일만 끌어올렸다.

## 의도와 시드

사용자가 던진 한국어 프롬프트가 출발점이었다.

> 도쿄타워 꼭대기에 서 있는 소녀의 전신을 하이앵글로 내려다 본 일러스트.
> 어안렌즈 왜곡. 배경에 도시가 보임.
> 소녀는 아무렇지 않다는 듯 카메라를 쳐다보고 있음.
> 프레임에 꽉 차게 소녀의 전신을 클로즈업.
> 아찔한 느낌.
> 모던 일본 애니메이션 화풍.
> 플랫한 채색이지만 사실적인 색감.
>
> 서소영 이미지와 함께 스웨터, 플레어 미니스커트, 무릎 위로 올라오는 스트라이프 양말을 의상 지정.

서소영의 정체성 시드는 풀바디·환경 포함 일러스트인 `서소영.png`로 두었다. *프레임에 꽉 차게 전신을 클로즈업*이라는 지시가 있어 상반신 포트레이트가 아닌 풀바디 시드가 필요했다. 헤어스타일은 시드 기준으로 일반화해 별도 지정을 두지 않았다.

## 라운드 1 · 풀바디 어안 베이스 (1024x1024 / low)

`서소영.png` 단독 시드로 사용자의 의상 지정과 도쿄타워 어안 컴포지션을 그대로 옮겨 시안 3장. 사용자의 선택은 v1이었다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/v1.png" alt="round 1 v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1. 라운드 1 베이스 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/v2.png" alt="round 1 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/v3.png" alt="round 1 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3</figcaption>
  </figure>
</div>

세 장 다 풀바디·하이앵글·어안 왜곡·도시 배경의 결은 잡혔지만, 모델이 텍스트만으로 어안 왜곡 강도를 결정하다 보니 v2·v3는 왜곡이 다소 약했다. v1이 가장 *아찔한 느낌*에 근접했다.

## 라운드 2 · 얼굴 클로즈업 + 어안 강화 + 색온도 다운 (1024x1024 / low)

사용자의 다음 한 마디.

> v1을 베이스로 하되 얼굴을 더 클로즈업해서 왜곡을 더 키우고 색온도를 약간 낮추자.

라운드 1의 v1을 *컴포지션 시드*로, `서소영.png`를 *얼굴·헤어 정체성 시드*로 두 장 동시에 입력해 시안 3장을 다시 굴렸다. 프롬프트에는 *카메라를 얼굴에 더 붙여 어안 왜곡을 강화한다 + cooler color temperature (blue-tinted shadows, muted palette) + warm orange/golden hour 톤은 회피*의 세 변경만 추가했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes-closeup/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes-closeup/v1.png" alt="round 2 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes-closeup/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes-closeup/v2.png" alt="round 2 v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v2. 클로즈업·왜곡·색온도 모두 균형 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes-closeup/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes-closeup/v3.png" alt="round 2 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3</figcaption>
  </figure>
</div>

라운드 1 대비 카메라가 얼굴에 가까워지며 어안 왜곡이 한층 또렷해졌고, 도쿄타워 red lattice의 채도도 한 단계 낮아졌다. 사용자의 선택은 v2 — 클로즈업·왜곡·색온도가 가장 균형 잡힌 컷.

## 라운드 3 · 2048x2048 high 정본 업스케일

라운드 2의 v2를 단일 시드로 잡고 `--size 2048x2048 --quality high`로 한 번 더 굴렸다. 약 4분 39초, 8.3MB. 프롬프트는 영문 *upscale-only* 톤으로 짧게 — *구도·표정·색감·포즈는 일절 건드리지 마라*를 또렷이 명시하고, 변경 허용은 *linework·texture·edge definition·anime cel shading*의 픽셀 디테일에만 두었다.

<div style="display:flex;justify-content:center;margin:20px 0;">
  <figure style="max-width:540px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tokyo-tower-fisheye-stripes/cover.png" alt="final cover" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;text-align:center;">정본 (2048x2048 high)</figcaption>
  </figure>
</div>

라운드 2 v2의 컴포지션·왜곡·표정·색감을 거의 그대로 유지한 채 스웨터 니트의 결, 스트라이프 양말의 줄 간격, 도쿄타워 red lattice의 선, 배경 도시의 그리드가 명확히 살아났다.

## 가장 흥미로운 지점

**두 장 동시 시드의 역할 분리.** 라운드 2에서 라운드 1의 v1을 *컴포지션 시드*, `서소영.png`를 *얼굴·헤어 정체성 시드*로 두 장을 같이 넣었다. 한 장만 넣었다면 컴포지션이 흔들리거나 얼굴이 흐트러졌을 텐데, 역할이 분리되니 카메라를 얼굴 쪽으로 당기는 *한 축* 변경만 또렷이 들어왔다. gpt-image-2 edit는 입력 이미지가 여러 장이면 *각 이미지가 다른 신호*임을 자동으로 받아들이는 듯하다 — 시드 한 장이 *모든 것*을 끌어가는 시드 1장 워크플로우와는 다른 결.

**어안 왜곡 강도는 텍스트 지시만으론 잡히지 않는다.** 라운드 1에서 *fisheye lens distortion, strong barrel curvature, wide field of view* 같은 영문 지시를 잔뜩 넣었지만 v2·v3는 왜곡이 약했다. 결국 라운드 2에서 라운드 1의 v1 자체를 시드로 넣고 *EXTREME fisheye, camera positioned very close to her face*라는 추가 한 축을 더하니 비로소 왜곡이 또렷이 들어왔다. *어안의 결은 시각 시드로 보여주는 게 텍스트로 설명하는 것보다 정확하다.*

**색온도는 텍스트로도 잡힌다.** 어안 왜곡과 달리 색온도(*cool blue-tinted shadows, avoid warm orange/golden hour*)는 텍스트 지시만으로도 라운드 1 → 라운드 2 사이의 변화가 또렷이 잡혔다. *기하학적 왜곡*은 시각 시드가 필요한 반면 *색조*는 어휘로 통제 가능한 영역이라는 차이를 본 라운드에서 다시 확인했다.

**upscale-only 프롬프트의 정밀화.** 이전 카드(`fisheye-window-press`)에서 본문 프롬프트를 길게 동봉했더니 모델이 *재렌더*로 받아 구도가 미세하게 흐트러진 적이 있었다. 본 카드의 라운드 3에서는 그 교훈을 살려 프롬프트 상단을 *Upscale this exact input image. This is a pixel-detail upscale only — do NOT reinterpret*로 시작하고, 변경 허용 항목과 보존 항목을 명시적으로 나누어 적었다. 결과적으로 라운드 2 v2와 라운드 3 cover는 픽셀 디테일만 다른 거의 같은 그림이 됐다.

**의상 지정은 충돌 없이 통과한다.** *스웨터 + 플레어 미니스커트 + 무릎 위로 올라오는 스트라이프 양말*이라는 세 가지 의상 지정은 세 라운드 모두에서 정확히 반영됐다. 이는 의상 지정이 *시드의 얼굴·헤어·구도와 경쟁하지 않는 가산형 변경*이기 때문이다 — `fisheye-summer-crosswalk`에서 정리한 *서로의 효과를 가리는 경쟁적 변경*과는 결이 다르다. 의상은 시드 위에 새로 입히는 레이어로 들어오므로 동시에 여러 항목(상의·하의·양말)을 지정해도 무리가 없다.

## 원본 프롬프트

```
도쿄타워 꼭대기에 서 있는 소녀의 전신을 하이앵글로 내려다 본 일러스트.
어안렌즈 왜곡. 배경에 도시가 보임.
소녀는 아무렇지 않다는 듯 카메라를 쳐다보고 있음.
프레임에 꽉 차게 소녀의 전신을 클로즈업.
아찔한 느낌.
모던 일본 애니메이션 화풍.
플랫한 채색이지만 사실적인 색감.

서소영 이미지와 함께 스웨터, 플레어 미니스커트, 무릎 위로 올라오는 스트라이프 양말을 의상 지정.
```

## 출처

사용자가 직접 작성한 한국어 프롬프트.
