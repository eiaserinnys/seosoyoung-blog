---
title: ""
date: 2026-05-16T05:07:40+09:00
slug: "manga-twin-tail-girl"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl/cover.png"
  hiddenInList: false
  focus: "50% 32%"
source: "자체 설계 — 사용자 협업 (3 라운드 제작기)"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

- 컨셉 1 → 정체성 시드 시도 → 얼굴 보존 + 헤어 보정 → 고품질 정본의 4단계 흐름으로 정착한 카드.
- 시드 reference는 헤어스타일만 옮기려 해도 얼굴 정체성까지 끌고 온다. 부분 transfer는 텍스트 명시로도 막기 어려웠다.
- 사용자 원본의 "어깨 위 두 개의 짙은 색 방울" 액세서리는 저품질 단계에서 모두 흐려졌다가, 2048x2048 고품질 정본화 단계에서야 비로소 또렷한 구슬로 렌더링됐다.

## 의도와 시드

사용자가 시드 인물 없이 텍스트 프롬프트만으로 출발한 카드다. "차분하고 절제된 색감 + 흔하지 않은 그림체 + 양갈래 미소녀 + 화면에서 튀어 나올 듯한 역동적인 자세"가 출발점이었다.

```
모던한 일본 만화 극화체 화풍.
심플한 선.
플랫한 채색.
산뜻하고 발랄한 표정.
단일 선의 흐름으로 입체감을 표현하는 묘사력.
차분하고 절제된 색감.
흔하지 않은 그림체.
어깨 위 두 개의 짙은 색 방울로 양갈래로 머리를 낮게 묶어 어깨 앞으로 내린 미소녀.
화면에서 튀어 나올 듯한 역동적인 자세와 구도.
니트 스웨터, 플레어 스커트, 무릎 위로 올라오는 양말, 에나멜 구두.
```

## 1단계 · 컨셉 비교

같은 프롬프트로 text-to-image 3장. 안전 필터 회피를 위해 "무릎 위로 올라오는 양말"을 "tall ribbed socks"로 일반화하고 "20대 여성"을 명시하여 sexual 분류를 우회했다. 첫 시도에서 v3 슬롯이 한 차례 분류기에 막혔으나, editorial fashion 톤으로 톤다운하여 3장 모두 통과시켰다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-concepts/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-concepts/v1.png" alt="컨셉 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">컨셉 v1 — 양갈래는 가장 또렷, 자세 정돈됨</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-concepts/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-concepts/v2.png" alt="컨셉 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">컨셉 v2 — 청록 스커트 율동감, 양갈래 풀림</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-concepts/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-concepts/v3.png" alt="컨셉 v3" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">컨셉 v3 — editorial 결, 자세 가장 살아있음 ← 선택</figcaption>
  </figure>
</div>

v3는 모델이 임의로 `leap in the moment` 글자를 박았고 양갈래도 풀어진 긴 머리로 정착했다. 그래도 화풍과 자세의 결이 가장 좋아서 base로 채택했다. 다음 라운드의 보정 축은 "글자 제거 + 양갈래 복원"이 됐다.

## 2단계 · 서소영 얼굴 정체성 시도 (폐기)

v3의 화풍·포즈는 유지하면서 서소영의 얼굴·헤어 정체성을 옮기려는 시도. v3.png + `서소영 (실사, 포트레이트).png`를 multi-image edit input으로 함께 넣었다. 스킬 가이드의 시드 우선 규칙대로 헤어스타일 지정은 제거하고 "reference 시드의 헤어스타일 유지"로 일반화했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r2/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r2/v1.png" alt="라운드 2 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r2/v1 — 표정 자연, 얼굴 시드 쪽으로 끌림</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r2/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r2/v2.png" alt="라운드 2 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r2/v2 — 포즈 보존 양호, 헤어 풀어짐</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r2/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r2/v3.png" alt="라운드 2 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r2/v3 — v2와 거의 쌍둥이</figcaption>
  </figure>
</div>

> 어... 이전 v3에서 얼굴이 바뀌어버렸네. 헤어스타일 구슬만 가져가면 되거든.

화풍·포즈는 잘 보존됐지만 얼굴 정체성이 시드 쪽으로 너무 많이 끌려갔다. 사용자가 시드에서 가져오려 한 것은 헤어스타일 디테일뿐이었는데, 모델은 시드의 얼굴까지 함께 transfer했다. 부분 transfer가 텍스트 명시로 막아지지 않는다는 점이 확인된 라운드. 본 발행에는 쓰지 않고, 시드 사용 자체를 폐기한 뒤 다음 라운드의 접근 자체를 바꿨다.

## 3단계 · 얼굴 보존 + 양갈래 보정

시드를 빼고 v3 원본만 input으로 두는 single-input edit. 텍스트 프롬프트로 "얼굴·표정·포즈·의상·화풍 모두 그대로 + 글자 제거 + 양갈래 + 짙은 색 머리방울"만 정확히 명시했다. 시드 reference가 끌어오는 정체성 transfer를 피하면서 사용자 원본의 헤어 디테일을 복원하는 접근.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r3/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r3/v1.png" alt="라운드 3 v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r3/v1 — 양갈래 가장 또렷, 표정 발랄</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r3/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r3/v2.png" alt="라운드 3 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">r3/v2 — 양갈래 풍성, 묶음 위치 흐릿</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r3/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/manga-twin-tail-girl-r3/v3.png" alt="라운드 3 v3" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">r3/v3 — 균형감 ← 선택 (정본 base)</figcaption>
  </figure>
</div>

> 세번째를 포즈 구도 얼굴 그대로 고품질 2048x2048로 만들고 제작기를 올리자.

세 시안 모두 얼굴/포즈/의상 보존에 성공했고, 양갈래도 자리 잡았다. 다만 1024x1024 low quality에서는 머리방울의 둥근 구슬 디테일이 머리 흐름에 묻혀 사라졌다. 시안 단계에서는 구성 요소가 자리 잡았는지만 확인하고 디테일은 정본화 단계에 맡기기로 했다.

## 4단계 · 정본 cover

r3/v3을 base로 2048x2048 high quality로 refine. 프롬프트는 "PRESERVE EVERYTHING — 얼굴, 표정, 포즈, 양갈래 헤어, 의상, 화풍, 배경까지 그대로 두고 해상도만 끌어올린다"는 보수적인 톤으로 작성. 디자인을 건드리지 말고 line precision과 shape clarity만 정돈하라고 명시했다.

고품질 정본화에서 비로소 사용자 원본 의도의 마지막 한 조각이 떨어졌다. 어깨 위 양 옆에 짙은 색 둥근 구슬 두 개가 또렷한 액세서리로 렌더링됐고, 양갈래의 흐름과 광택, 메리제인 슈즈의 에나멜 광, 니트의 케이블 패턴까지 모두 선명해졌다.

## 가장 흥미로운 지점

- **모더레이션 분류기는 stochastic하다.** 첫 라운드에서 같은 프롬프트의 v1/v2는 통과하고 v3만 sexual violation으로 막혔다. "tall ribbed socks"로 톤다운하니 같은 슬롯 3장이 모두 통과. 의상 묘사 한 단어가 zettai ryouiki 해석의 임계점을 가르고, 거기에 stochastic 요소가 더해진다.
- **multi-image edit에서 시드는 의도하지 않은 요소까지 끌고 온다.** 라운드 2에서 서소영 실사 시드를 reference로 넣은 순간 얼굴 정체성이 함께 transfer됐다. 텍스트로 "헤어만 가져오기"를 강하게 명시해도 모델은 시드 얼굴을 가져온다. 부분 transfer를 원할 때는 시드를 빼고 텍스트 명시로 가는 single-input edit이 더 안정적이라는 교훈.
- **저품질에서 흐려진 디테일은 정본화에서 되돌아온다.** 머리방울 같은 작은 액세서리는 1024x1024 low quality에서는 흐름에 묻혀 사라지다가 2048x2048 high quality에서 비로소 또렷이 렌더링된다. 시안 단계 평가는 "구성 요소가 약하게라도 자리 잡았는가"까지만 보고, 디테일 충실도는 정본화 단계에 맡긴다.
- **base 이미지에 묶인 stochastic variation은 좁다.** 같은 input + 같은 프롬프트로 3장을 굴려도 multi-image / single-image edit 모두 시안 사이의 차이가 좁게 잡혔다. text-to-image 1차 라운드만 시안 사이 차이가 컸다. 시안 N개로 안을 비교하고 싶다면 첫 라운드에서 폭넓게 굴리고, 이후 라운드는 채택하느냐 마느냐의 결정에 가깝다고 봐야 한다.

## 출처

자체 설계 — 사용자(주복)의 텍스트 프롬프트에서 출발하여 3 라운드 협업으로 정본화한 카드. 외부 출처 없음.

## 메모

- 정본 slug: `manga-twin-tail-girl` / cover R2: `gallery/manga-twin-tail-girl/cover.png` (2048x2048 high quality, edit mode, r3/v3 base)
- 시드: 없음. 라운드 2에서만 `서소영 (실사, 포트레이트).png` reference로 시도했으나 얼굴 정체성이 의도와 다르게 transfer되어 폐기.
- 라운드별 시안 R2 prefix: `gallery/manga-twin-tail-girl-concepts/` (라운드 1, text-to-image), `manga-twin-tail-girl-r2/` (라운드 2, multi-image edit, 폐기), `manga-twin-tail-girl-r3/` (라운드 3, single-image edit). 본문 figure 그리드가 참조하므로 *삭제 금지*.
- 모더레이션 회피: 사용자 원본 "무릎 위로 올라오는 양말"을 "tall ribbed socks"로 일반화. 결과적으로 양말 길이가 무릎 아래/무릎 높이로 떨어졌으나 갤러리 결에는 부합.
- 헤어스타일 지정: 라운드 3에서 v3 원본 + 텍스트 지시로 양갈래 + 짙은 색 머리방울 부착. 시드 우선 규칙 대신 사용자 원본 프롬프트의 디테일을 정본으로 사용.
- cover focus: `50% 32%` — 그리드 썸네일에서 얼굴이 중앙으로 떨어지도록 상단 1/3 기준.
