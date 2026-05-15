---
title: ""
date: 2026-05-13T07:25:24+09:00
slug: "angel-harajuku-finger-guns"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/angel-harajuku-finger-guns/cover.png"
  hiddenInList: false
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 오리지널

원본 프롬프트 그대로 — 플래티넘 블론드 천사 하라주쿠 스트리트웨어

![original](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/angel-harajuku-finger-guns/original.png)

## 프롬프트

```
Upscale and refine the reference image at high fidelity. PRESERVE the composition, camera angle, pose, expression, framing, lighting, color palette, and overall layout EXACTLY as in the reference — do not reinterpret the scene, do not change the pose, do not move the camera. Only sharpen lineart, clarify shading, and clean up anatomical detail.

Pay special, deliberate attention to ANATOMY of HANDS and FEET:
- Hands: exactly five fingers per hand, clear finger separation, natural finger placement, no fused or melted fingers, no extra digits, no warped knuckles. The fingerless gloves should sit cleanly at the knuckle line. Sleeves of the oversized jacket may engulf the hands but where fingers emerge, they must be drawn correctly.
- Feet & shoes: feet sit naturally inside the chunky white platform sneakers, ankle angles correct, the over-the-knee black-and-white striped sock and the short white crew sock terminate cleanly into the shoe tops, sneaker silhouettes are symmetric, solid, and convincingly proportioned — not melted, not lopsided, no fused soles.

The subject is the same character as the reference: a young woman in a chic angel-meets-harajuku streetwear outfit, in a defiant yankee-squat crouch on the ground, captured from an extreme HIGH-ANGLE WIDE-ANGLE viewpoint, with a sharp SIDE-EYE GLARE (head tilted slightly away, eyes cutting back toward the camera). Keep her face, hairstyle, and hair color exactly as in the reference. Exactly ONE feathered white wing flaring from her LEFT shoulder only — no second wing, no symmetric pair. A thin metallic halo floats just above her head as a flat ellipse from this top-down view.

Outfit details to preserve and clean up:
- White nurse-style frilled bonnet with a chunky black five-pointed star pinned to the side
- Oversized white varsity-style jacket pushed off the shoulders, sleeves engulfing the hands, white fingerless gloves underneath
- Black corseted bustier over a black fishnet/mesh long-sleeve, lace-up front, tiny butterfly charms
- Layered ruffled mini-skirt: black underlayer with monochrome ornaments, ivory tiered lace ruffles, ribbon ties trailing
- Mismatched legwear: right leg short white crew sock, left leg thick black-and-white horizontal-striped over-the-knee sock
- Massive chunky white platform sneakers, exaggerated soles, dirty-cute proportions

Rendering. Bold confident inked lineart with strong, slightly heavy outlines in the gekiga / modern manga illustration tradition. Crisp cel shading with clear hard shadow shapes, accented by delicate watercolor-like gradients on the skin. Muted monochrome palette (white / ivory / charcoal) with the subject's own hair tone from the reference as the only warm accent. Flat warm-gray ground beneath her, soft drop shadow pooled around the squat with the artist's mark "aiko" subtly embedded. The square frame is densely filled — body, wing, sneakers all kiss the edges, almost no negative space.

Negative. Do not redesign hands or feet — only clean them up. Do not change the pose, the camera angle, or the composition. No symmetric pair of wings — exactly ONE wing on the LEFT shoulder. No melted or fused fingers. No extra digits. No misaligned ankles. No standing pose. No direct frontal eye contact. No low angle or eye-level shot. No overly saturated colors, no busy background, no chibi proportions, no soft airbrush look. No empty borders — composition must fill the square.
```

## 메모

- 시드: `서소영.png` (풀바디 정본) → 시안 라운드 후 draft-b를 레퍼런스로 사용하여 업스케일
- v5 (final): 1:1 정사각 2048x2048, high quality, draft-b 구도·포즈·표정을 그대로 유지하며 업스케일
- 손가락(5개·융합 없음)·발(스니커즈·발목·양말 종단부) 해부학 정정 지침 추가
- 헤어스타일·헤어색·얼굴은 시드 기준으로 일관성 유지 (헤어스타일·warm-accent 지정 일반화)
- 외날개(왼쪽 어깨)는 의도된 비대칭 — 부정문에 거듭 명시
- 시안 비교용 draft-a/b/c, 원본 충실판 original은 같은 R2 prefix에 보존
