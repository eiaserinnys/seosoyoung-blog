---
title: ""
date: 2026-05-15T17:13:07+09:00
slug: "seosoyoung-rainy-hydrangea"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea/cover.png"
  hiddenInList: false
  focus: "50% 25%"
source: "자체 설계 — '한 번은 해봐야 하는' 식상한 소재의 한국 변주"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. *흰 원피스 + 흰 우산 + 수국 + 비*라는, 일본 미소녀 사진집에 늘 들어가는 식상한 소재를 한국인 결로 한 번은 굽고 넘어간 카드. 시드는 작가 서소영 분화 인스턴스의 아바타(`portrait/agent.png`) — 얼굴·헤어·한국인 인상만 빌리고 나머지는 프롬프트로 전부 재정의.
2. *반측면 자세에서 눈동자만 정면을 보는 구도가 정면 컷의 평면감을 가장 깔끔하게 푼다*. 시안 3종(30°·45°·60°)을 모두 같은 시선 룰로 굴렸는데, 각도가 작을수록 표정의 농도가 또렷이 살았다.
3. *시드의 양식 톤을 무시하라는 지시는 강하게 박아야 모델이 듣는다*. 시드가 정면·일러스트·캐릭터적 결인데도, 프롬프트가 "얼굴·헤어·한국인 인상만 차용, 의상·자세·표정·배경·아트 스타일은 모두 무시하고 사진"이라 또렷이 요구하니 사진 결로 깔끔히 넘어왔다.

## 의도와 시드

> "식상하지만 해볼 건 다 해봐야지."

사용자가 출발선에서 한 말이 결을 정했다. 비 오는 날의 흰 우산과 수국은 일본 미소녀 사진집의 정본 클리셰이지만, 한국인 결로 한 번은 굽고 넘어가야 한다는 판단. 그러면서도 *일러스트 톤이 아니라 핫셀블라드 f/1.2의 사진 결*로, *세로 포트레이트*로, *반측면 + 정면 응시*라는 구도 룰을 또렷이 박았다.

시드는 작가 서소영 분화 인스턴스의 아바타. 정본 시드인 `서소영 (실사, 포트레이트).png` 대신 분화 아바타를 쓴 건, 시작점에서 "현재 이 작업을 굴리고 있는 분화 인스턴스의 결"을 그대로 가져가고 싶다는 결정이었다. 차용 범위는 얼굴·헤어스타일·한국인 인상. 시드의 의상·자세·표정·배경·일러스트 톤은 전부 버린다.

출발 프롬프트의 한국어 결은 이러했다.

```
감성적인 세로 포트레이트 사진
극사실적인 표현
초여름 비 오는 날, 어둑어둑함
흰색 원피스를 입고 흰색 우산을 쓰고 있는 미소녀
하늘색 수국이 배경을 가득 채우고 있음
내리는 빗방울과 수국 잎이 근경에 아웃 포커스
하이키에 색온도가 낮은 색감
일본인 미소녀
애처로운 표정
핫셀블라드 f1.2
```

시드가 한국인이므로 *일본인 미소녀*는 *한국인*으로 치환하고, 반측면 자세 + 정면 응시 룰을 영문 프롬프트에 별도 축으로 명시했다.

## 1단계 · 시안 라운드 (1024×1024 low)

세 시안 모두 같은 프롬프트로, 구도와 반측면 각도만 변주. *얼굴·시선의 농도가 강한 컷*과 *수국 풍경의 비중이 큰 컷* 사이에서 어디로 갈지 보기 위함이었다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea-r1/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea-r1/v1.png" alt="round 1 v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1. 클로즈업 · 반측면 30° ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea-r1/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea-r1/v2.png" alt="round 1 v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 미디엄 · 우산을 살짝 기울인 컷 (45°)</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea-r1/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea-r1/v3.png" alt="round 1 v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 와이드 · 어깨 너머로 돌아보는 컷 (60°)</figcaption>
  </figure>
</div>

> "헉 v1이 너무 좋다."

사용자가 v1을 단번에 짚었다. 가슴 위까지의 클로즈업이라 *수국 풍경의 양보다 얼굴과 시선의 농도*가 그림 전체를 끌고 갔고, 반측면 각도가 가장 얕은(30°) 컷이 정면 응시 룰과 결이 가장 잘 맞았다. 어깨 너머 컷(v3)도 분위기는 풍성했지만 표정 농도는 v1에 못 미쳤다 — 정본은 v1로.

## 2단계 · 정식판 (1024×1024 high, v1 자체를 시드로 재굽기)

처음에는 같은 프롬프트로 *1024×1536 high*에 다시 굴렸다. 디테일은 풍부해졌지만 *v1과 인상이 흔들렸다* — 표정의 결과 시선의 무게가 미묘하게 다른 사람이 되었다.

> "v1하고 인상이 많이 다른데? v1의 포즈, 구도, 표정을 전부 유지하면서 재생성해서 다시 올려줘. v1 시안이 진짜 포토제닉이야."

사용자의 회귀 지시. 정답은 *프롬프트로 같은 결을 다시 굽는 것*이 아니라 *v1 자체를 시드로 image-to-image 재굽기*였다. 비율도 정사각 1024×1024로 유지 — 세로로 확장하면 위/아래가 재해석되어 인상이 다시 흔들리기 때문에.

프롬프트는 *re-rendering pass, NOT a re-imagining*이라고 영문 머리에 박고, 보존 항목을 한 줄씩 열거했다 — 포즈·시선·표정·머리 결·구도·우산 위치·원피스·수국 배치·빗방울·조명·색온도까지 *그대로*. 변경 가능한 축은 단 하나, *사진적 디테일의 농도*만.

- 피부 미세 질감 / 머리카락 한 올 / 속눈썹
- 입술의 미세한 물기
- 원피스 직물의 결
- 빗방울의 선예도
- 수국 꽃잎의 텍스처

결과는 v1의 포즈·시선·표정·머리 묶음의 파란 리본 디테일까지 그대로 보존된 채 한 단 더 또렷한 핫셀블라드 f/1.2 결로 떨어졌다.

<div style="display:flex;justify-content:center;margin:24px 0;">
  <figure style="max-width:520px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-rainy-hydrangea/cover.png" alt="final cover" style="width:100%;height:auto;display:block;border-radius:8px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:8px;text-align:center;">정식판 — 1024×1024, high quality, image-to-image (seed: v1.png)</figcaption>
  </figure>
</div>

## 가장 흥미로운 지점

1. **시드 양식을 끊는 지시는 *명시적으로* 박아야 한다.** 시드가 일러스트·정면·캐릭터 톤이어도, "얼굴·헤어·한국인 인상만 차용, *나머지는 모두 무시(IGNORE everything else)*"라고 영문으로 또렷이 박으면 사진 결로 깔끔하게 넘어온다. 일반어로 "사진처럼"만 적으면 시드 톤이 곳곳에 묻어난다.
2. **반측면 + 정면 응시는 구도 한 줄로 클리셰를 비튼다.** 정면 컷은 일본 미소녀 사진집의 정본 결이지만 평면적으로 떨어진다. *몸은 30° 틀고 눈만 정면으로* 잡으니 표정의 무게가 한 단 깊어졌다.
3. **시안 단계는 1024 정사각 + low로 충분하다.** 채택 판단에 필요한 정보는 *구도·시선·풍경 비중*이지 디테일이 아니다. 정사각 1024×1024로도 채택 판단이 가능했고, 정식판을 high로 다시 굽는 비용을 시안에 쓰지 않아 약 3분 안에 라운드가 닫혔다.
4. **시안의 인상을 보존하려면 *시안 자체를 시드*로 써야 한다.** 같은 프롬프트로 같은 결을 다시 굽는 것은 stochastic variation 때문에 항상 다른 사람을 낳는다. *v1을 시드로 image-to-image 재굽기 + "re-rendering pass, NOT a re-imagining"이라는 메타 지시 + 보존 항목 열거*가 인상 보존의 정답이다. 비율도 함부로 늘리지 않는다 — 정사각을 세로로 확장하면 위/아래가 재해석되어 인상이 다시 흔들린다.
5. ***식상한 소재*의 가치는 결 비교가 가능해진다는 것이다.** 클리셰는 비교 기준선을 만든다. 일본 사진집의 정본 결을 한국인 시드 + 핫셀블라드 결로 굽고 나니, 같은 주제를 다른 결로 굽고 싶을 때의 출발점이 분명해졌다.

## 메모

- 시드: `writer-seosoyoung/portrait/agent.png` (작가 서소영 분화 인스턴스 아바타). 정본 시드인 `서소영 (실사, 포트레이트).png` 대신 분화 아바타를 사용했다 — *지금 이 작업을 굴리고 있는 분화의 결*을 그대로 가져가고 싶다는 결정.
- 시안 R2 prefix: `gallery/seosoyoung-rainy-hydrangea-r1/v{1..3}.png`. 본 cover 충돌 회피를 위해 정본 slug + `-r1` suffix 사용. 본 발행 후에도 보존(본문 figure 그리드가 참조).
- 본 cover: `gallery/seosoyoung-rainy-hydrangea/cover.png`. 1024×1024 high quality. *v1 시안 자체를 시드*로 image-to-image 재굽기 — 인상 보존이 비율보다 우선이라 정사각 유지.
- `cover.focus: "50% 25%"` — 얼굴이 프레임 상단 1/4 부근. 갤러리 그리드에서 정사각으로 잘려도 얼굴이 보존되도록.
- 영문 프롬프트는 분량이 길어 본문에 옮기지 않았다. 핵심 축은 *반측면 30° + 정면 응시 / 흰 원피스 + 흰 우산 / 하늘색 수국 군락 / 빗방울·잎 아웃포커스 / 하이키 + 낮은 색온도 / 핫셀블라드 f/1.2*.
