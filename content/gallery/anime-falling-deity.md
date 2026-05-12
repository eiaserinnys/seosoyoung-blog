---
title: ""
date: 2026-05-12T23:08:12+09:00
slug: "anime-falling-deity"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/anime-falling-deity/cover.png"
  hiddenInList: false
  focus: "50% 8%"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 오리지널

원본 프롬프트 그대로 (일본 신사 무녀 + 일본 목조 도시 버전)

![original](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/anime-falling-deity-original/cover.png)

## 프롬프트

```
A stunning anime theatrical movie poster in portrait format. Studio Ghibli meets Makoto Shinkai visual language. The reference subject Seosoyoung — a young Joseon noblewoman, magic student at Cloistermont Academy — is shown in STRICT SIDE PROFILE view, her body in a dramatic cinematic pose: standing at the very tip of the wing of a crumbling giant stone titan, her chest lifted skyward in a gentle arch (subtle, anatomically natural — not an extreme backbend).

POSE — explicit and exact:
- She has EXACTLY TWO ARMS. No extra limbs, no duplicated arms, no phantom or ghostly arm shapes anywhere in the composition.
- Her FRONT arm (the one closer to camera in profile) is raised straight up and slightly forward toward the celestial rift, elbow gently bent, fingers spread wide. This is the only arm reaching skyward.
- Her BACK arm (the one further from camera) trails behind her body at hip level, hand open with fingers relaxed, following the line of her trailing skirt — clearly grounded against her silhouette, not raised.
- Her face is in pure side-profile silhouette, chin lifted slightly toward the sky, eye half-closed in resolute calm.
- She wears a flowing white ceremonial hanbok-inspired magic robe with worn frayed edges, long sleeves and skirt panels billowing horizontally in the wind like banners.
- Her hair streams horizontally behind her in a long ribbon against gravity, kept exactly as in the portrait reference.

Beneath her, the colossus — an ancient stone deity covered in moss and glowing golden arcane sigils intermixed with Korean hanja script — slowly falls through a sea of clouds, its silhouette in side view, one massive stone hand reaching feebly downward as fragments crumble away. Above her, the heavens split open in a vast celestial rift; through it an inverted ocean floats above the clouds, and the gothic stone spires and cathedral towers of Cloistermont magic academy hang upside down from its surface, glowing windows and floating lanterns drifting like stars between the cathedral arches.

The sky transitions from deep twilight blue at the bottom to a luminous peach and rose gold at the top. Strong rim light from behind catches the silhouette of her profile and raised arm in glowing peach-gold. Volumetric god rays pierce through cloud layers behind her. Cherry blossom petals and worn parchment talismans inscribed with Korean and Latin script spiral horizontally past her in the wind, emphasizing speed and gravity.

Composition: she occupies the upper-center as a small dramatic silhouette, the colossus filling the mid-frame, clouds and sky dominating. Negative space above her head for the celestial rift. Strong cinematic side-lighting, theatrical movie poster framing.

Art style: hand-drawn 2D animation, ultra-detailed background painting, expressive linework, rich cel shading. Palette: deep indigo, peach, rose gold, warm amber, soft white. Title in large elegant typography at the bottom with English subtitle beneath in a clean modern font. Tagline in small white italic text above the title. Mood: mythological, spiritual, bittersweet wonder. Theatrical release quality anime cinema poster.

Strict anatomy rules:
- Exactly two arms total. Count them: ONE raised forward-up, ONE trailing behind at hip level. No third arm. No ghost arm.
- No double exposure, no overlapping duplicate limbs, no transparent extra appendages.
- Maintain the reference subject's facial features (seen in profile) and character identity exactly from the portrait seed.
- Architecture in the inverted upper region must follow the Cloistermont seed — gothic spires, stone arches, ornate cathedral towers — never Japanese wooden buildings.
```

## 메모

서소영 + 클로이스터몽트 인스턴스화 헤더 (v3 — 옆모습 + 유령 팔 결함 수정).
- 시드: `서소영 (포트레이트).png` + `Cloistermont (Dawn).png`
- v2에서 backbend + 뻗는 팔을 동시에 처리하다 모델이 팔을 한 쌍 더 그린 결함 발생 → v3에서 수정:
  - backbend 톤다운 (gentle arch, 과한 뒤젖힘 제거)
  - 팔 위치 명시적으로 단일화: 앞팔은 위로, 뒷팔은 허리 옆 trailing
  - "EXACTLY TWO ARMS" / "no phantom limbs" 등 anatomy rule 명문화
- 일본 신사 무녀복 → 한복풍 의례 마법 로브
- 떠 있는 일본 목조 도시 → 클로이스터몽트 고딕 첨탑
- "golden kanji script" → "arcane sigils + Korean hanja" 혼합
- 헤어스타일 지정 제거 / 시드 기준 일반화
