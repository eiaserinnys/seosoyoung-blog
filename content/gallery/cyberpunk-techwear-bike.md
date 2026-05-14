---
title: ""
date: 2026-05-14T13:37:03+09:00
slug: "cyberpunk-techwear-bike"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/cyberpunk-techwear-bike/cover.png"
  hiddenInList: false
  focus: "50% 0%"
source: "https://x.com/missdelulu9/status/2054756878098530567"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 오리지널

원본 트윗 그대로 — beautiful Asian woman 표현을 유지한 text-to-image 결과.

![original](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/cyberpunk-techwear-bike-original/cover.png)

## 시안 선택 과정

1차 시안은 서소영 실사 포트레이트만 시드로 넣었더니 시드의 *정면성*이 그대로 남아 카드의 hero shot으로는 어색했다. 사용자는 *오리지널처럼 반측면 샷, 표정은 장난기 있게 눈웃음*을 요청했다.

2차 시안은 1차 v3을 visual master로 인계하고 정체성 시드는 그대로 유지한 뒤, 프롬프트에 three-quarter 포즈·over-the-shoulder 헤드 턴·smize(눈웃음)을 명시해 굴렸다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/cyberpunk-techwear-bike/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/cyberpunk-techwear-bike/v1.png" alt="v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1. 가장 또렷한 over-the-shoulder ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/cyberpunk-techwear-bike/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/cyberpunk-techwear-bike/v2.png" alt="v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 정면 쪽으로 풀린 변주</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/cyberpunk-techwear-bike/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/cyberpunk-techwear-bike/v3.png" alt="v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 미드샷 클로즈 변주</figcaption>
  </figure>
</div>

사용자는 v1을 선택했다. 세 장 중 반측면 회전과 over-the-shoulder 헤드 턴이 가장 또렷이 살아 있고, 눈웃음의 장난기도 가장 깔끔하게 떨어졌다. 이 한 장을 visual master로 두고 1536x2304 / `quality=high`로 한 번 더 굴려 정본 업스케일을 만들었다.

## 프롬프트

```
High-resolution polished version of the reference scene. Hyper-detailed full-body cinematic fashion editorial portrait — Neo-Tokyo cyberpunk techwear, premium studio editorial. Vertical magazine-cover composition, theatrical low-angle hero framing, ultra-fine detail, 8k.

You receive TWO reference images:
- IMAGE 1 (identity reference): the female subject. Preserve her face identity EXACTLY — East Asian features, eye shape, brow shape, nose, lip shape, skin tone, and her usual hairstyle as in this seed (most of which is concealed beneath the white technical hood).
- IMAGE 2 (visual master): treat this image as the visual master. Preserve the EXACT composition, framing, three-quarter body rotation away from the camera, over-the-shoulder head turn back toward the lens, low-angle hero camera, seating posture on the yellow-and-black cyberpunk motorcycle, right leg extended to the ground / left leg bent on the footpeg, hands resting near the handlebars, head tilt, eye-smile (smize) expression with subtly upturned mouth corners, wardrobe silhouette, motif arrangement, palette, lighting direction, and background layout of IMAGE 2. This is a high-resolution refinement of IMAGE 2 — same image, more detail.

EXPRESSION — preserve IMAGE 2 unchanged:
- Playful, mischievous warmth. Soft genuine eye-smile (smize), eyes slightly crinkled at the outer corners, lower eyelids gently lifted.
- Closed-mouth smile with a subtle upward curve at the corners — confident hero who is also clearly enjoying the moment.

POSE — preserve IMAGE 2 unchanged:
- Three-quarter body view rotated 30-45 degrees away from the camera.
- Over-the-shoulder head turn back to the lens.
- Right leg extended naturally to the ground; left leg bent on the bike's footpeg.
- Hands rest casually near the handlebars in a poised, ready stance.
- Dramatic low-angle hero shot.

OUTFIT — preserve IMAGE 2 unchanged:
- Intricate white technical hood with embedded red optical sensor details.
- Bold yellow armored shoulder mantle with exposed metallic bolts and industrial mechanical design.
- Weathered cybernetic corset with bronze-toned gears, exposed wiring, layered mechanical plating, subtle battle-worn textures, over a fitted white tactical inner suit.
- Dramatically oversized sleeves in rich pink satin-silk with bold black Japanese-inspired typography and subtle distressed detailing.
- Black tactical fingerless leather gloves, realistic stitching, matte carbon textures.
- High-waisted charcoal-black oversized techwear cargo pants with utility straps, hanging buckles, reinforced seams, minimal red accents.
- Chunky futuristic yellow-and-red high-top sneakers with thick mechanical soles, intricate layered panels, red lacing, metallic trims, realistic rubber textures.

REFINEMENT TARGETS — improve over IMAGE 2:
- Face: more refined naturally beautiful skin micro-texture, visible pores, fine skin grain, sharper iris with cleaner catchlights, more lifelike lip detail, refined eyeliner crispness, high-arched dark eyebrows with individual hair detail. No plastic skin, no AI smoothing, no exaggerated anime features. Identity must remain identical to IMAGE 1.
- Hood: cleaner panel seams, sharper red optical sensor glow with subtle bloom, refined fabric-and-resin material reading.
- Yellow shoulder mantle: crisper bolt heads, subtle scratches and edge wear, cleaner armor-plate edges.
- Cybernetic corset: finer gear-tooth detail, individual exposed wires with realistic insulation textures, layered plating with refined battle-worn weathering.
- Pink satin sleeves: more luxurious satin-silk sheen with refined fold highlights, crisper bold black Japanese-inspired typography, subtle fabric distressing.
- Gloves: finer stitching, sharper carbon-weave matte texture.
- Cargo pants: more pronounced techwear stitching, crisper utility straps and buckles, refined denim grain and reinforced seams.
- Sneakers: finer panel layering, crisper red lacing, sharper metallic trims, more realistic rubber sole texture, individual lace eyelets clean.
- Motorcycle: cleaner yellow-and-black panel reflections, refined chrome and metallic highlights, crisper headlight assembly, refined tire tread detail.
- Background: cleaner large bold red Japanese kanji typography on the white studio backdrop, sharper futuristic editorial graphic elements (UI-inspired floating accents) arranged like a premium magazine cover.
- Lighting: more refined cinematic Rembrandt key light shaping the face and outfit folds, cleaner rim lighting separating the silhouette from the white backdrop, subtler volumetric studio atmosphere.

CAMERA — preserve IMAGE 2:
- Dramatic low-angle hero shot, full-body framing, vertical editorial magazine-cover crop.
- Shot on Fujifilm GFX 100 II with an 85mm f/1.4 lens, ultra-shallow depth of field on the bike background, razor-sharp facial detail, cinematic color grading, photorealistic materials.

Everything else (face identity, pose, hands, expression, wardrobe silhouette, motif arrangement, color palette, crop) must remain identical to IMAGE 2. No text overlays beyond the existing background kanji and editorial graphic elements. Hyper-realistic cyberpunk editorial fashion photography aesthetic.
```

## 출처

[원본](https://x.com/missdelulu9/status/2054756878098530567)

## 메모

- 시드는 `서소영 (실사, 포트레이트).png` (정체성) + `cyberpunk-techwear-bike-v1-master.png` (visual master) 두 장을 multi-input edit으로 묶었다.
- 원본 프롬프트의 첫 문장 *beautiful Asian woman* 부분은 *the woman shown in the FIRST reference image, preserving her exact facial identity*로 치환했다. 외형은 시드를 따른다.
- 헤어스타일 지정은 원본에도 따로 없고 흰색 technical hood가 머리를 덮는 구성이라, 시드 헤어와의 충돌 정리는 별도로 필요하지 않았다.
- 그리드 썸네일은 풀바디 vertical이라 얼굴이 맨 위에 있다. `cover.focus: "50% 0%"`로 썸네일 영역을 이미지 상단에 붙여 얼굴을 온전히 노출시켰다.
