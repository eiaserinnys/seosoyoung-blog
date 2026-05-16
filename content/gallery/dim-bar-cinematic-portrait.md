---
title: ""
date: 2026-05-12T20:24:02+09:00
slug: "dim-bar-cinematic-portrait"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/dim-bar-cinematic-portrait/cover.png"
  hiddenInList: false
  focus: "50% 25%"
model: "gpt-image-2"
mode: "edit"
draft: true
---

## 오리지널

원본 프롬프트 그대로(text-to-image) 생성한 결과.

![original](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/dim-bar-cinematic-portrait/original.png)

### 원본 프롬프트

```
Low-light cinematic portrait, telephoto lens compression, shallow depth of field, intentional soft focus and motion blur, moody nightlife atmosphere, abstract storytelling composition, layered haze and diffusion, imperfect candid capture  a stunning beautiful Korean female idol, ultra high visual appeal, pale porcelain skin, delicate yet seductive features, effortlessly alluring presence, relaxed and slightly tipsy mood, lazy and unguarded body language  outfit: sleek sensual styling — fitted off-shoulder top or thin strap dress subtly revealing collarbone and shoulder line, paired with a short skirt or high-slit silhouette; minimal but intentional accessories (earrings, thin necklace), modern K-idol fashion styling, slightly undone elegance  scene: dimly lit bar or lounge at night, warm tungsten lighting mixed with scattered reflections, frosted glass textures, cocktail glass in hand, blurred figures moving in background, neon hints and shadow gradients, reflective surfaces creating depth  lighting: Rembrandt-style contrast lighting, warm highlights against deep shadows, soft diffusion bloom, light scattering and refraction, cinematic glow  pose: natural candid moment — body slightly leaning or shifting weight, one hand holding a glass loosely, the other brushing hair or resting near waist, subtle torso angle emphasizing silhouette, not posing but captured mid-moment  expression: half-lidded eyes, distant or slightly provocative gaze, lips slightly parted, ambiguous emotion between calm and temptation  visual style: high contrast grayscale-toned palette with controlled color accents, heavy film grain, noise texture, layered blur gradients, imperfect focus transitions, strong negative space, dynamic perspective, avant-garde editorial aesthetic  mood: dreamy, intoxicating, mysterious, sensual but restrained, "moment before something happens"  --2:3
```

## 헤더 프롬프트

`서소영 (실사).png` 시드 기반 image-to-image 변환에 실제로 넘긴 프롬프트(v2). 포즈를 결정적 순간으로 재작성했다.

```
Low-light cinematic portrait, telephoto lens compression, shallow depth of field, intentional soft focus and motion blur, moody nightlife atmosphere, abstract storytelling composition, layered haze and diffusion, decisive editorial capture. A stylish young Korean woman captured in an editorial-style photograph, ultra high visual appeal, pale porcelain skin, delicate and expressive features, magnetic and self-assured presence, focused intent in her stance.

Outfit: refined modern styling — elegant top with a clean collar line and tailored skirt, minimal but intentional accessories (earrings, thin necklace), modern K-fashion editorial styling, effortlessly composed elegance.

Scene: dimly lit lounge at night, warm tungsten lighting mixed with scattered reflections, frosted glass textures, a drink glass in hand, blurred figures moving in the background, neon hints and shadow gradients, reflective surfaces creating depth.

Lighting: Rembrandt-style contrast lighting, strong rim light carving the silhouette from the dark background, warm highlights against deep shadows, soft diffusion bloom, light scattering and refraction, cinematic glow.

Pose: STRONG decisive moment — pronounced contrapposto, body weight clearly shifted onto one leg, distinct torso twist creating a powerful S-curve silhouette, one arm fully extended outward holding the glass forward into the foreground (creating depth and tension), the other hand sweeping back through her hair with clear assertive motion, head turned sharply over the shoulder toward the camera with a definitive angle, chin slightly lifted, shoulder line bold and prominent. This is a high-impact editorial pose, NOT a passive pause — every part of the body has intent and direction.

Expression: piercing direct gaze straight into the camera, sharp and focused eyes, calm but commanding presence, controlled neutral mouth.

Visual style: high contrast grayscale-toned palette with controlled color accents, heavy film grain, noise texture, layered blur gradients, imperfect focus transitions, strong negative space, dynamic perspective with a low slightly upward camera angle to emphasize the powerful stance, avant-garde editorial aesthetic.

Mood: dreamy, atmospheric, mysterious, commanding and self-possessed, a charged moment of poise.

[Identity preservation] Preserve the facial identity, features, and overall appearance from the input reference image. Keep the input subject's hairstyle as-is (no hairstyle changes specified). Apply only the styling, scene, lighting, pose, expression, and visual mood described above to the same person.
```

## 메모

원본 프롬프트로 먼저 오리지널을 생성한 뒤, `서소영 (실사).png`를 시드로 image-to-image 헤더를 변환했다.
원본 프롬프트에 명시적인 헤어스타일 지정이 없어 실사 시드의 헤어를 그대로 유지했다.

v1은 포즈가 너무 절제되어 임팩트가 약했다("slightly leaning", "loosely", "subtle"). v2는 포즈를 결정적 순간으로 재작성했다:
강한 contrapposto와 S자 실루엣, 잔을 앞으로 내민 팔, 머리를 쓸어넘기는 단호한 동작, 어깨 너머로 돌린 시선,
정면 응시, 약간 아래에서 올려다보는 카메라 앵글. 모더레이션은 표현 톤을 절제(commanding / self-possessed)로 유지해 통과했다.
v1 백업: `.local/tmp/gallery/dim-bar-cinematic-portrait/cover_v1.png`
