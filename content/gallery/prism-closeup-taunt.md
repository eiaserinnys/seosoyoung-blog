---
title: ""
date: 2026-05-13T10:17:00+09:00
slug: "prism-closeup-taunt"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/cover.png"
  hiddenInList: false
  focus: "50% 30%"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. 모던 anime 결의 도발적인 미소녀 클로즈업 — 머리카락은 바람에 휘날리고, 검지는 카메라를 향해 디포커스로 뻗는 한 컷. 시드는 갤러리 스킬 정본 `서소영 (포트레이트).png`, 채색 모티프는 프리즘·크리스탈의 정교한 굴절감 + 하이키 톤이다.
2. 텍스트로 만든 오리지널 → 시드 기반 헤더 후보 3장 → 선택안의 검지 배리에이션 3종 → 최종안의 2048 / `high` 업스케일 + 살짝 오버 노출 + 부드러운 블룸까지 4단계로 끊었다. 단계마다 1024 / `low`로 후보 스캔, 마지막 한 장만 2048 / `high`로 굳혔다.
3. 가장 큰 굴곡은 *카메라를 가리킨 손이 bokeh로 뭉개져 손가락임을 알아보기 어려웠던 것* — 디포커스 자체를 풀지 않고 *손가락 윤곽만 인식 가능한 수준으로 살짝* 풀라는 *부분 디포커스 해제* 지시가 깔끔하게 통했다.

## 의도와 시드

만들고 싶었던 그림은 분명했다. 단순한 선의 모던 anime, 도발적이고 장난기 어린 표정, 화려하게 바람에 날리는 머리카락, 카메라를 가리킨 손은 포커스 아웃된 극단적 클로즈업. 채색은 프리즘이나 크리스탈처럼 정교하면서도 서늘하고 가벼운 하이키.

시드는 갤러리 스킬 정본의 `서소영 (포트레이트).png`. 상반신·얼굴 정체성 유지가 핵심인 클로즈업이라 포트레이트 시드가 정답이었다. 프롬프트에는 헤어스타일을 따로 지정하지 않았다 — "머리카락이 바람에 날린다"는 *동작 묘사*이지 *스타일 변경 지시*가 아니라서 시드의 헤어스타일을 그대로 따라갈 수 있었다.

## 1단계 · 오리지널 (text-to-image, 비교 레퍼런스)

먼저 시드 없이 텍스트만으로 1024x1024 / `medium`을 한 장 굴렸다. 프롬프트 결 자체가 무엇을 만들어 내는지 확인하고, 이후 시드 변환과 어떤 정체성 차이가 생기는지 비교하기 위한 레퍼런스다.

![오리지널 — 시드 없이 텍스트만](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/original.png)

톤·구도·색감은 의도대로였다. 다만 얼굴은 *전혀 다른 인물*이 떨어졌다 — 텍스트 묘사("modern anime bishojo")만으로는 매번 다른 얼굴이 나온다. 이 차이가 시드의 필요성을 확정해 주었다.

## 2단계 · 시드 기반 헤더 후보 3장

같은 프롬프트를 `서소영 (포트레이트).png` 시드로 image-to-image로 돌렸다. 1024x1024 / `low`로 셋.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/header-1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/header-1.png" alt="후보 1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">후보 1</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/header-2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/header-2.png" alt="후보 2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">후보 2</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/header-3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/header-3.png" alt="후보 3 (선택)" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">후보 3 ← 선택</figcaption>
  </figure>
</div>

후보 3의 *표정과 구도, 채색의 합*이 가장 강했다. 다만 한 가지 약점이 분명했다 — 카메라를 가리킨 손이 bokeh로 너무 뭉개져 *손가락임을 알아보기 어려웠다*. 의도한 *극단적 디포커스*에서 *형태 인식 가능성*까지 침범당한 셈이다.

## 3단계 · 검지 배리에이션 3종

후보 3을 그대로 다음 단계의 시드로 넘겼다. *얼굴·구도·채색·하이키 톤은 정본 유지하고, 검지만 알아보기 쉽게* — 이 지시 한 줄을 명확히 한 채 손가락 표현만 셋으로 갈랐다. 1024x1024 / `low`.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/finger-a.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/finger-a.png" alt="A. 정면 직진형 (선택)" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">A. 정면 직진형 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/finger-b.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/finger-b.png" alt="B. 살짝 비스듬형" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">B. 살짝 비스듬형</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/finger-c.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/prism-closeup-taunt/finger-c.png" alt="C. 손등 회전형" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">C. 손등 회전형</figcaption>
  </figure>
</div>

A가 가장 강했다. 검지를 카메라로 *곧게* 뻗은 정공법이라, 가장 클래식한 "you" 포즈로 한 번에 읽혔다. B는 옆면이 보이는 입체감은 좋았지만 *도발의 직선성*이 약해졌고, C는 우아함이 더해진 대신 *손등의 회전 곡선*이 클로즈업의 단순한 결과 살짝 충돌했다.

## 4단계 · 2048 / `high` 업스케일 + 살짝 오버 노출 + 블룸

A를 정본으로 굳히는 마지막 패스. 2048x2048 / `quality=high`로 한 번에 세 가지를 보강 요청했다.

- **업스케일**: 라인·머리카락 결·프리즘 굴절 디테일까지 한 단계 정밀화
- **살짝 오버 노출**: 하이라이트만 *살짝* 블론 아웃(pure white를 살짝 넘어서는 정도)
- **부드러운 블룸**: 머리 가장자리·스킨 하이라이트·프리즘 액센트 주변에 은은한 글로우

가장 신경 쓴 단서는 "블룸이 얼굴이나 손가락 실루엣을 덮지 않도록"이라는 한 줄. 하이키 + 블룸은 자칫 얼굴이 사라질 수 있어, 모델에게 *블룸을 어디에 얹고 어디에 얹지 말지*를 명시했다.

호출 시간은 약 3분 44초, 6.0MB. 본 카드의 커버다.

## 가장 흥미로운 지점

**디포커스를 *0으로 풀지 말고 살짝만* 풀기.** 손가락이 bokeh로 뭉개진 것을 고치겠다고 단순히 "in focus"라고 적으면 카메라를 가리킨 손이 또렷한 *주연*이 되어 클로즈업 구도 전체가 깨진다. *"soften the bokeh just slightly so the index finger silhouette becomes clearly recognizable"* — 디포커스의 *깊이*는 유지하되 *형태 인식 가능성*만 끌어올리는 지시가 정확히 의도한 결을 잡아냈다. *전부 vs 0*이 아니라 *몇 % 풀기*를 어휘로 풀어내는 게 핵심이었다.

**시드의 헤어스타일은 텍스트 동작 묘사보다 강하다.** 프롬프트에 *"머리카락이 바람에 날린다"*는 *동작*을 넣어도 시드의 헤어스타일 자체는 보존된다. 시드에서 머리 길이·색·결을 가져오고, 텍스트에서 *흐름의 동적 표현*만 가져오는 식이다. 갤러리 스킬의 "헤어스타일 지정 충돌 처리" 원칙(시드 사용 시 명시적 헤어스타일 지정은 충돌 — 빼거나 일반화)이 *동작 묘사는 충돌 아님*이라는 점에서 자연스럽게 보완되는 사례였다.

**시안과 정본의 사이즈/품질 분배.** 8회의 호출 중 7회는 1024 / `low` (오리지널만 `medium`), 마지막 한 번만 2048 / `high`. 시안 7장 총 호출 시간은 약 4분 30초, 정본 업스케일이 약 3분 44초. 만약 모든 호출을 `high`로 굴렸다면 시안 단계만 30분 가까이 누적됐을 것이다. 참조 카드 [psychedelic-maid-v2](https://seosoyoung.eiaserinnys.me/gallery/psychedelic-maid-v2/)와 [starbucks-scrapbook-alter-egos](https://seosoyoung.eiaserinnys.me/gallery/starbucks-scrapbook-alter-egos/)가 강조했던 *후보 스캔은 가볍게, 굳히는 한 장만 무겁게* 원칙이 여기서도 그대로 통했다.

**단계별 시드 인계가 곧 핀포인트 교정이다.** 각 단계의 *선택안*을 그대로 다음 단계의 시드로 넘겼다. 2단계 → 3단계는 *손가락만* 손보기, 3단계 → 4단계는 *디테일·노출·블룸만* 얹기. 같은 한 인물의 같은 한 컷을 *조금씩만 다르게* 손보는 방식이라, 매 단계의 변화 폭이 작아 모델의 결과가 더 안정적이었다.

## 프롬프트

본 카드의 정체성을 결정한 것은 4단계의 업스케일 프롬프트다. 그 전문을 그대로 옮긴다.

```
Keep this image faithfully — same face, same provocative taunting expression, same extreme close-up framing, same hair flow in the wind, same index finger pointing straight at the camera, same prismatic crystal-like coloring, same high-key palette. Upscale to ultra-high resolution with crisp, refined detail — sharper linework, finer hair strands, more delicate prismatic refraction in the coloring. Add a very subtle overexposure: highlights are slightly blown out, just a touch beyond pure white in the brightest areas, giving the image a luminous, airy feel without losing the face. Add a soft bloom filter effect — gentle light blooming around the brightest highlights (hair edges, skin highlights, prismatic accents), creating a dreamy ethereal glow. Keep the bloom subtle, never washing out the face or finger silhouette. Overall mood: dreamy, luminous, ethereal high-key with a delicate prismatic shimmer.
```

## 출처

원본 프롬프트 모티프 — 사용자가 직접 제안한 *모던 anime 클로즈업 + 프리즘 채색 + 도발적 표정* 컨셉.
