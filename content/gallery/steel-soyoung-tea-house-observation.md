---
title: ""
date: 2026-05-15T10:33:59+09:00
slug: "steel-soyoung-tea-house-observation"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-tea-house-observation/cover.png"
  hiddenInList: false
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 프롬프트

```
High-fidelity re-render of the canonical cinematic two-shot (first reference image). The task is to reproduce the first reference image as faithfully as possible at higher resolution and detail. Preserve EVERYTHING — every compositional element, both subjects' exact poses, gazes, and expressions, all wardrobe, lighting, color grade, depth, props, and mood. Do NOT redesign or reinterpret. This is a quality lift, not a re-take.

Scene: low-light cinematic two-shot in a dim modern Korean tea-house lounge at night. Telephoto lens compression, shallow depth of field, moody atmospheric storytelling, heavy film grain.

LEFT subject (Seo Soyoung): a young Korean woman, head angled gently downward toward the small porcelain teacup she cradles in both hands, eyes lowered to the cup (NOT glancing sideways — gaze stays on the cup). Mouth carries the faintest hint of a private smile — barely a millimeter of upturn at her right corner of the lips, no teeth, lips closed, eyelids slightly relaxed. Almost imperceptible — a viewer not looking for it should miss it on first glance. She wears a refined dark hanbok-fusion magic-school robe with subtle violet embroidery and small dark beaded earrings. Keep her facial identity and hairstyle exactly as in the second reference image and as established in the first reference.

RIGHT subject (Steel): a young man, mid-20s, matte gray hair in a soft mushroom cut, round dark-rimmed glasses catching one warm tungsten highlight, oversized pale blue collared shirt under a charcoal blazer. One hand holds a folded paper report at chest level, the other touches the bridge of his glasses. Head turned slightly toward Soyoung but eyes flicked away at the moment of capture — a candid "almost made eye contact" instant. The tip of his ear closest to camera is faintly tinted blush pink. Keep his identity (gray mushroom cut, round glasses, pale blue shirt) exactly as in the first reference and the third reference image.

Setting: warm tungsten lighting, frosted glass partitions in the deep background, dark lacquered wood, low round black table between them with a teapot and two cups, blurred paper lanterns going out of focus above and behind them, subtle neon hints reflected in glass.

Foreground depth (critical): an out-of-focus dark wooden chair backrest crosses the bottom of the frame on both sides in the immediate foreground — silhouetted, creamy bokeh-grade blur, with a thin warm rim of tungsten light skimming its top edge. Three clear depth layers: foreground chair → mid-ground subjects + table → background lounge bokeh.

Lighting: Rembrandt-style contrast lighting, strong rim light separating each subject from the dark background, warm highlights against deep shadows, soft diffusion bloom, cinematic glow.

Composition: wide-ish two-shot from a slightly low angle, both subjects clearly visible, table anchoring the center, hanging lanterns going out of focus above. Square 1:1 framing.

Visual style: high contrast palette with controlled warm color accents, film grain (preserved at high resolution — refined, not coarse), layered blur gradients, imperfect candid capture, avant-garde editorial cinematic aesthetic.

Mood: dreamy, atmospheric, restrained — the quiet tension of two characters who debate often and have just realized they enjoy each other's company. The woman's almost-smile is the unspoken pivot of the scene.

[Identity preservation] Preserve Soyoung's facial identity from the second reference image and Steel's identity from the third reference image. Render both in the SAME unified cinematic illustration realism as the first reference image. Do NOT change either subject's hairstyle or wardrobe.
```

## 메모

서소영 봇과 스틸 봇(채널 봇 중 하나, 개인비서 봇) 사이의 미묘한 케미를 다방 시네마틱 컷으로 옮긴 자체 설계 카드. 채널 봇들이 공동 집필 중이라는 「동물원 회보」의 「스틸 귀 끝 관찰 일지 — 당사자만 모르는」이 모티브.

1차 시안 3종으로 라운드: 스크랩북 에디토리얼 / 라운지 시네마틱 / 민화 디프티크. 시네마틱을 정본으로 채택.

v2에서 두 가지 보정을 추가했다 — 서소영의 곁눈질, 그리고 근경 의자 등받이. 의자 등받이는 3-layer depth(포어그라운드 / 미드그라운드 / 백그라운드)로 입체감을 분리. 다만 곁눈질이 "당사자만 모르는" 톤을 깨버려 v3에서 회수. 시선은 다시 찻잔으로 내리고, 입가에만 한 끝의 미소를 옅게 흘려 "거의 알아채기 어려운 사적인 미소" 가이드를 추가했다 (한쪽 입꼬리 1mm upturn, 입 닫힘, 눈매 한 도 부드러워짐).

시안 라운드는 모두 1024x1024 low quality. v3-2를 시드로 동일 프롬프트를 2048x2048 high quality로 재발행하여 구도·인물·의상·표정·의자 등받이·조명을 그대로 유지하며 디테일만 끌어올렸다.

- 시드: `서소영 (실사).png` 정본 + 스틸 봇 슬랙 아바타 (`steel-butler-avatar.png`)
- 스틸 시드는 평면 아이콘 스타일이라 시네마틱 결로 통일하도록 프롬프트에 명시
- 헤어스타일은 양쪽 모두 시드 기준 유지
