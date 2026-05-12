---
title: ""
date: 2026-05-12T19:25:18+09:00
slug: "scrapbook-mini-alter-egos"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/scrapbook-mini-alter-egos/cover.png"
  hiddenInList: false
source: "https://www.meigen.ai/"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 오리지널

1단 베이스 — 코지 상반신 일러스트(변환 input)

![original](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/scrapbook-mini-alter-egos-base/cover.png)

## 프롬프트

```
Transform the provided reference image into a cozy aesthetic scrapbook-style composition while strictly preserving the original subject, identity, pose, lighting, and background.

Add multiple small "mini version" characters of the same person (chibi / doll-like style), placed naturally around the scene (on objects, table, shoulder, etc.). These mini figures must match the subject's face, hairstyle, outfit, and vibe consistently, styled as cute 3D collectible figurines. Show them doing different activities (reading, posing, taking photos, relaxing).

Overlay handwritten-style doodles and annotations across the image: arrows, hearts, stars, sparkles, icons, and playful captions connected to elements in the scene.

Use a soft pastel color palette (white base with pink, peach, blue accents).

Keep the frame visually rich and filled but balanced and clean.

Style: warm, cozy lighting, dreamy Instagram scrapbook aesthetic, soft depth of field, highly detailed, polished but playful.

The final result must look like the SAME original image enhanced with mini alter-egos and aesthetic annotations — not a recreated or different scene.
```

## 출처

[원본](https://www.meigen.ai/)

## 메모

2단 파이프라인. 1단에서 서소영 캐릭터를 코지 상반신 포즈로 재구성한 뒤(scrapbook-mini-alter-egos-base), 2단에서 그 결과를 reference로 스크랩북 변환 프롬프트 적용. 원본 reference가 정자세 프로필이면 변환 결과도 정자세로 굳어버리는 한계를 우회.
