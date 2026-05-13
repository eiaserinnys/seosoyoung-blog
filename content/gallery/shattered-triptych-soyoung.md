---
title: ""
date: 2026-05-13T15:19:03+09:00
slug: "shattered-triptych-soyoung"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/shattered-triptych-soyoung/cover.png"
  hiddenInList: false
  focus: "50% 22%"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 오리지널

원본 프롬프트 충실 시도(서소영 시드 없이 텍스트-투-이미지)

![original](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/shattered-triptych-scarlet/cover.png)

## 프롬프트

```
A surreal vintage haute couture editorial photograph reflected in a PHYSICALLY BROKEN antique mirror. High-resolution master version of the reference image, with the shattered-mirror effect MORE pronounced.

Use the reference image as the authoritative reference for the entire composition: the scattered polygonal mirror shards arrangement, the woman's identity (East Asian, early twenties, dark hair, deep scarlet satin corset gown, powder-blue opera gloves and stockings), her pose (seated on the floor, leaning back against the ornate wooden chair on the right, head tilted FAR back, throat arched, eyes closed in trance, one arm on the chair armrest, the other reaching toward a scattered telephone), the velvet curtain backdrop, the cheval mirror with gilded frame on the LEFT side reflecting her profile, the scattered cream and pale-blue rotary telephones.

Now enhance and amplify the shattered-mirror effect:

1. Same arrangement of irregular polygonal shards as in the reference — the overall mosaic layout, shard sizes and positions are preserved. We are upgrading the same image to high resolution and pushing the cracked-mirror effect harder, not redesigning the layout.

2. MORE PRONOUNCED MISALIGNMENT between shards. Where the reference image's shards meet, push the displacement further:
   - At every seam between two neighboring shards, the image content visibly does NOT line up. Edges of the dress, gloves, hair, curtain folds, telephone outlines, chair contours — all should clearly break and resume at slightly OFFSET positions across the cracks (5-15 pixels of horizontal/vertical jump at each seam).
   - Each shard is rotated 2-8 degrees relative to its neighbors — small but visible angular displacement.
   - The woman's body in particular should clearly break apart at the seams: a forearm may shift several pixels across a crack; the shoulder line may discontinue and resume elsewhere; the hair may split into two visibly misaligned portions across a shard boundary.

3. BLACK VOID between shards is preserved and slightly widened (1-4 pixels wide gaps) — visibly empty space, not continuous image.

4. SILVERED EDGES along each shard's broken perimeter catch sharper highlights at high resolution — fine bright lines of reflected light, occasionally prismatic, confirming the silvered backing of a real antique mirror.

5. The cheval mirror inside the scene (on the LEFT) is itself intact (not broken) — only the LARGER mirror that IS the picture plane is broken. The cheval mirror is still visible across multiple shards of the larger broken mirror, and its profile reflection of the woman is also visible (across multiple shards, misaligned at the seams just like the rest of the scene).

6. Small detached slivers near the bottom and edges have fallen entirely loose, lying on the floor below the larger shards.

VOCABULARY: "physically broken antique mirror", "polygonal shards", "displaced fragments", "black void between shards", "pronounced misalignment at every seam", "silvered prismatic edges". NOT "overlay", NOT "filter".

Style: 1990s–early 2000s Japanese fashion magazine editorial aesthetic. Direct on-camera flash, harsh highlights, deep shadows, slightly oversaturated reds, cool blue undertones, film grain, high contrast. At high resolution, the silvered shard edges catch sharp prismatic highlights against the surrounding black void.

Composition: Vertical portrait orientation (3:4). Break-point near the woman's shoulder. Reference image's overall layout preserved, only sharpened and the misalignment amplified.

This is a fully clothed, modest fashion editorial in the tradition of classical painting — no nudity, no suggestive themes, no violence. Couture styling.
```

## 메모

v11(최종) — v8(좌측 cheval mirror가 있는 v6에 깨진 거울 효과 적용)을 시드로 1536x2304 high 업스케일 + shard 간 misalignment 강화. gpt-image-2의 학습 분포 한계로 진짜 cubist mosaic 수준의 fragmentation까진 안 가지만, polygonal shards + black void + 좌측 cheval mirror(intact)의 mirror-within-mirror 구조까지 보존된 결로 마무리.
