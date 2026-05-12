---
title: ""
date: 2026-05-12T23:54:00+09:00
slug: "starbucks-scrapbook-alter-egos"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/starbucks-scrapbook-alter-egos/cover.jpg"
  hiddenInList: false
  focus: "35% 35%"
source: "https://www.meigen.ai/"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. 모던한 스타벅스에서 맥북을 펴고 골머리를 썩는 코지 스크랩북 일러스트 한 장을 만든 6단계 파이프라인 기록이다. 시드는 갤러리 정본의 풀바디 서소영, 변환 모티프는 [scrapbook-mini-alter-egos](https://seosoyoung.eiaserinnys.me/gallery/scrapbook-mini-alter-egos/) 카드의 프롬프트.
2. 한 번에 완성을 노리지 않고 "후보 스캔 → 변환 → 업스케일 → 핀포인트 교정 → 해부학 폴리시"로 단계를 끊었을 때가 가장 안정적이었다. 한 단계 결과물을 그대로 다음 단계의 시드로 넘기는 식.
3. gpt-image-2의 한계(4:3 부재·안전 필터·미니 분신 그라운딩 실패)는 단계 분리·시드 고정·핀포인트 교정으로 모두 우회할 수 있었다.

## 의도와 시드

만들고 싶었던 그림은 분명했다. 모던한 스타벅스, 펼쳐진 맥북, 화면을 향해 깍지를 끼고 미간을 찌푸린 채 골머리를 썩는 한 컷. 의상은 헐렁한 회색 니트 + 검은 미니스커트 + 검은 오버니 삭스로 잡았다. 시드는 갤러리 스킬 정본의 `서소영.png` — 풀바디·환경 포함 일러스트라 의상 시각화에 적합하다.

결과적으로는 이미 발행되어 있던 [scrapbook-mini-alter-egos](https://seosoyoung.eiaserinnys.me/gallery/scrapbook-mini-alter-egos/) 카드의 변환 프롬프트를 같은 인물·다른 장면에 적용한 자매 카드가 되었다.

## 1단계 · 기본 장면 후보 3장

먼저 후보 스캔. 랜드스케이프 1536x1024 / `quality=low`로 세 컷을 뽑았다. 양손으로 관자놀이를 짚는 정면(A), 의자에 기대 한숨 쉬는 3/4(B), 턱을 괴고 화면을 응시하는 옆모습(C).

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung/starbucks-headache-frontal.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung/starbucks-headache-frontal.png" alt="A. 정면 관자놀이" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">A. 정면 관자놀이</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung/starbucks-sigh-three-quarter.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung/starbucks-sigh-three-quarter.png" alt="B. 한숨 3/4" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">B. 한숨 3/4</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung/starbucks-side-focus.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung/starbucks-side-focus.png" alt="C. 옆모습 집중" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">C. 옆모습 집중</figcaption>
  </figure>
</div>

옆모습 집중(C)의 정적인 결이 가장 마음에 들었지만, 옆모습이라 표정의 무게가 약해 보였다. 같은 결을 정면으로 옮기면 더 강해질 것 같았다.

## 2단계 · 정면 + 약간 하이앵글 재구도

같은 정적 분위기를 카메라만 정면 + 약간 위에서 본 시점으로 재구도했다. 손짓의 디테일을 셋으로 갈랐다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung-v2/v2-front-high-chin.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung-v2/v2-front-high-chin.png" alt="A. 턱을 괴고" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">A. 턱을 괴고</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung-v2/v2-front-high-clasped.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung-v2/v2-front-high-clasped.png" alt="B. 두 손 깍지 (선택)" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">B. 두 손 깍지 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung-v2/v2-front-high-hairtouch.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-soyoung-v2/v2-front-high-hairtouch.png" alt="C. 머리카락 매만지며" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">C. 머리카락 매만지며</figcaption>
  </figure>
</div>

깍지(B)가 "지금 진짜 골머리 썩고 있다"는 긴장도를 가장 잘 잡아냈다. 이 컷이 이후 모든 단계의 베이스가 된다.

## 3단계 · 스크랩북 변환 (피치 결)

`scrapbook-mini-alter-egos` 카드의 변환 프롬프트를 B 컷에 적용했다. 미니 분신들의 활동·캡션·파스텔 액센트를 세 갈래로 가지치기.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-v3/scrapbook-pink-comfort.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-v3/scrapbook-pink-comfort.png" alt="핑크 위로형" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">핑크 위로형 — 응원 결, 가장 로코틱</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-v3/scrapbook-peach-bustle.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-v3/scrapbook-peach-bustle.png" alt="피치 분주형 (선택)" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">피치 분주형 ← 선택 · 불릿저널풍 도두락</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-v3/scrapbook-blue-pensive.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-v3/scrapbook-blue-pensive.png" alt="블루 사색형" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">블루 사색형 — 야경, 가장 코지</figcaption>
  </figure>
</div>

피치 분주형이 작업의 "골머리"라는 본 주제에 가장 충실했다. 아래가 이 단계 직후 — 업스케일 전 — 산출물이다.

![scrapbook 변환 직후 (3단계 산출물)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-v3/scrapbook-peach-bustle.png)

## 4단계 · 고해상도 업스케일 + 손글씨 큐트화

3072x2048 / `quality=high`로 한 번에 업스케일하면서 두 가지를 보강 요청했다.

- 청키 니트의 코·머리카락 결·맥북 키캡·우드 그레인 등 텍스처 정밀화
- 손글씨를 두루뭉술한 <strong>버블 스타일 라운드 핸드라이팅</strong>으로 교체하고, `◕‿◕` `ʕ•ᴥ•ʔ` `>_<` 같은 카와이 이모티콘과 ✨ ♡ ☆ 도형을 분산 배치. 잉크는 검정이 아닌 웜 브라운/뮤트 피치로 지정

이 단계만 4분 가까이 걸렸다. 결과물은 디테일이 한 단계 올라갔지만, 자세히 들여다보니 두 군데가 어색했다 — 노트북 앞 미니 분신이 화면을 뚫고 있고, 종이 뭉치를 든 미니 분신의 한 발이 공중에 떠 있었다.

![4단계 업스케일본 — 두 군데 어색한 곳이 보인다](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-final/scrapbook-peach-bustle-final.png)

## 5단계 · 핀포인트 교정 두 번

업스케일본을 베이스로 두고 같은 사이즈(3072x2048) / `quality=low`로 빠르게 핀포인트 교정에 들어갔다. 낮은 품질 패스라도 베이스가 좋으면 국소 수정에는 충분하다.

먼저 (1) 노트북 미니 분신만 잡았다. 화면 가장자리 또는 키보드 위에 깔끔히 앉히되 화면 패널을 통과하지 않도록 명시.

![1차 교정 — 노트북 미니 안착](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-fix/fix-pass-1-large-low.png)

(2)는 처음에 "한 다리로 균형 잡으며 휘청"으로 시도해 봤지만, 휘청대는 자세가 카드 전체의 단정한 결과 어울리지 않아 폐기했다.

![2차 시도 — 한 다리 휘청 (폐기)](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-fix2/fix-pass-2-paper-wobble.png)

대신 "의자 등받이 위에 두 다리를 모으고 단정히 직립"으로 재시도했다. 의자 등받이가 충분히 보이지 않을 경우 카페 톤에 맞춰 미니멀하게 살짝 그려도 좋다고 단서를 달았다.

![3차 교정 — 의자 등받이 위 직립](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/candidates/starbucks-scrapbook-fix3/fix-pass-3-chair-backrest.png)

## 6단계 · 해부학 고품질 폴리시

마지막은 해부학 폴리시. 3072x2048 / `quality=high`. 구도·캡션·미니 분신 위치는 절대 유지하되, 모든 캐릭터(메인 + 미니 분신 전부)의 팔·다리 관절 흐름, 손가락 수와 인터록, 발과 그림자를 다듬도록 명시했다.

- 메인 인물의 두 손은 인터록된 상태에서 손가락 총 10개·엄지 방향이 자연스럽게
- 미니 분신 손은 피규어 톤에 맞춰 <strong>하나의 양식으로 통일</strong>되도록 (미튼 또는 4지 치비 중 하나)
- 모든 미니의 발은 접촉면 + 작은 그림자로 그라운딩

이 폴리시본이 본 카드의 커버다.

## 가장 흥미로운 지점

한 번에 완성을 노리지 않은 것이 결과적으로 가장 중요한 결정이었다.

각 단계의 호출 시간과 비용은 일정하지 않다. 1536x1024 / `low`는 30초·1MB, 3072x2048 / `high`는 4분·9MB로 한 자릿수 배율 차이가 난다. 같은 4분을 쓰더라도 그 4분을 어디에 쓰느냐가 결과를 가른다. "구도가 안 굳었는데 고품질로 굳히려" 들면 4분짜리 실패가 누적되고, "구도가 굳었으니 폴리시만 고품질로" 가면 4분이 한 번의 마무리에 쓰인다.

미니 분신의 그라운딩(다리·발·접촉면)을 모델이 자주 놓치는 것도 흥미로웠다. 이건 단일 프롬프트의 한계라기보다, 미니 분신이 메인 인물의 디테일 우선순위 뒤로 밀리는 모델의 주의 분배 문제처럼 보였다. 핀포인트 교정 단계를 따로 둔 이유가 여기 있다 — 메인이 굳은 다음에 미니만 따로 호명해 손봐야 모델이 거기 집중한다.

안전 필터에 한 번 걸렸던 것도 기록할 만하다. "허벅지·살결 갭"(zettai ryouiki에 해당하는 묘사)을 의상 설명에 넣었더니 `safety_violations=[sexual]`로 차단됐다. 표현을 빼고 "헐렁한 회색 니트 + 검은 스커트 + 무릎 위로 올라오는 검은 긴 양말"로 톤다운하니 통과. 시각적 인상은 거의 동일했다. 시드 외형이 충분히 자리 잡혀 있으면 텍스트 묘사는 항목만 짚어도 모델이 채워 준다.

## 프롬프트

본 카드의 커버에 도달하기까지 4 회의 다른 프롬프트가 쌓였지만, 카드의 정체성을 결정한 것은 3단계의 스크랩북 변환 프롬프트다. 그 전문을 그대로 옮긴다 — 메인 장면(스타벅스 + 깍지 + 맥북) 묘사가 포함된 인스턴스화된 버전.

```
Transform the provided reference image into a cozy aesthetic scrapbook-style composition while strictly preserving the original subject, identity, pose, lighting, and background. The original is a scene of a young woman at a modern Starbucks café, hands clasped in front of her mouth, troubled and concentrating on her open MacBook — preserve this scene exactly.

Add multiple small "mini version" characters of the same person (chibi / doll-like style), placed naturally around the scene — on the MacBook keyboard, on top of the Starbucks paper cup, perched on her shoulder, sitting on the table edge, etc. These mini figures must match the subject's face, hairstyle, outfit (oversized gray knit sweater, black skirt, tall black over-knee socks), and vibe consistently, styled as cute 3D collectible figurines. Show them doing different activities — one mini-her frantically typing on a tiny laptop on the keyboard, another carrying a stack of papers across the table, a third reading a tiny book on top of the coffee cup lid, a fourth pointing at the MacBook screen as if explaining a bug.

Overlay handwritten-style doodles and annotations across the image: arrows pointing to the MacBook screen and coffee cup, hearts, stars, sparkles, icons, and playful captions connected to elements in the scene ('TODO ✏️', 'bug here →', 'next sprint?', 'coffee +1', 'help me').

Use a soft pastel color palette (white base with dominant peach and cream accents, light tan highlights).

Keep the frame visually rich and filled but balanced and clean.

Style: warm, cozy lighting, dreamy Instagram scrapbook aesthetic, soft depth of field, highly detailed, polished but playful. Doodles feel like a productivity bullet journal — checkboxes, small calendar grids, arrows between elements.

The final result must look like the SAME original image enhanced with mini alter-egos and aesthetic annotations — not a recreated or different scene.
```

## 출처

원본 프롬프트 모티프 — [meigen.ai](https://www.meigen.ai/) (자매 카드: [scrapbook-mini-alter-egos](https://seosoyoung.eiaserinnys.me/gallery/scrapbook-mini-alter-egos/))
