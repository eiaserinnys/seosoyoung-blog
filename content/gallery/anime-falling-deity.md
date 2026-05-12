---
title: ""
date: 2026-05-12T20:27:00+09:00
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
A stunning anime theatrical movie poster in portrait format. Studio Ghibli meets Makoto Shinkai visual language. The reference subject Seosoyoung — a young Joseon noblewoman, magic student at Cloistermont Academy — is shown in STRICT SIDE PROFILE view, her body in a dramatic cinematic pose: standing at the very tip of the wing of a crumbling giant stone titan, her back arched in a graceful backbend, one arm thrust upward toward the celestial rift with fingers spread, the other arm trailing behind her like a fallen wing, head tilted back, chin lifted skyward. Her face is in pure profile silhouette against the glowing sky — sharp nose line, parted lips, eye half-closed in resolute calm. She wears a flowing white ceremonial hanbok-inspired magic robe with worn frayed edges, long sleeves and skirt panels billowing horizontally in the wind like banners. Her hair streams horizontally behind her in a long ribbon against gravity, kept exactly as in the portrait reference.

Beneath her, the colossus — an ancient stone deity covered in moss and glowing golden arcane sigils intermixed with Korean hanja script — slowly falls through a sea of clouds, its silhouette also in side view, one massive stone hand reaching feebly downward as fragments crumble away. Above her, the heavens split open in a vast celestial rift; through it an inverted ocean floats above the clouds, and the gothic stone spires and cathedral towers of Cloistermont magic academy hang upside down from its surface, glowing windows and floating lanterns drifting like stars between the cathedral arches.

The sky transitions from deep twilight blue at the bottom to a luminous peach and rose gold at the top. Strong rim light from behind catches the silhouette of her profile and outstretched arm in glowing peach-gold. Volumetric god rays pierce through cloud layers behind her. Cherry blossom petals and worn parchment talismans inscribed with Korean and Latin script spiral horizontally past her in the wind, emphasizing speed and gravity.

Composition: she occupies the upper-center as a small dramatic silhouette, the colossus filling the mid-frame, clouds and sky dominating. Negative space above her head for the celestial rift. Strong cinematic side-lighting, theatrical movie poster framing.

Art style: hand-drawn 2D animation, ultra-detailed background painting, expressive linework, rich cel shading. Palette: deep indigo, peach, rose gold, warm amber, soft white. Title in large elegant typography at the bottom with English subtitle beneath in a clean modern font. Tagline in small white italic text above the title. Mood: mythological, spiritual, bittersweet wonder. Theatrical release quality anime cinema poster.

Strict identity rules: maintain the reference subject's facial features (now seen in profile) and character identity exactly from the portrait seed. The architecture in the inverted upper region must follow the Cloistermont seed — gothic spires, stone arches, ornate cathedral towers — never Japanese wooden buildings.
```

## 메모

서소영 + 클로이스터몽트 인스턴스화 헤더 (v2 — 옆모습 극적 포즈).
- 시드: `서소영 (포트레이트).png` + `Cloistermont (Dawn).png`
- v1(정면 손 뻗는 포즈) → v2(strict side profile + backbend + 한 손 천상 균열로 뻗는 시네마틱 실루엣)으로 재생성
- 일본 신사 무녀복 → 한복풍 의례 마법 로브
- 떠 있는 일본 목조 도시 → 클로이스터몽트 고딕 첨탑·대성당 타워
- "golden kanji script" → "arcane sigils + Korean hanja" 혼합
- 헤어스타일 지정 제거 / 시드 기준 일반화 (수평으로 흩날리는 모션만 유지)
- 강한 rim light + 옆모습 실루엣으로 영화 포스터 톤 강화
