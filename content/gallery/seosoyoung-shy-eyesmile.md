---
title: ""
date: 2026-05-13T20:05:03+09:00
slug: "seosoyoung-shy-eyesmile"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-eyesmile/cover.png"
  hiddenInList: false
  focus: "50% 22%"
source: "https://x.com/voxcatai/status/2054410564932407460"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. 사용자가 가져온 트윗은 "스타레일 캐릭터를 실사 반사실 인물 사진으로 변환할 때의 핵심 로직"을 설명하는 *메타 가이드*였다. 캐릭터 식별점 + 실사 메이크업 + 수줍은 신체 언어(低头·侧眼·咬唇·缩肩·手靠近脸)를 우리 시드에 적용해 한 장으로 굳힌 기록이다.
2. 잘못된 출발(도서관) → 트윗 정독 → 첫 시안(골든아워 한복) → 트윗 결과물을 *라인 마네킹*으로 추출 → 마네킹 A 적용 → 마네킹 C + 카메라 직시 → 눈웃음 + dust bokeh 추가 → 1024x1536 `quality=high` 정본 업스케일. 시안은 모두 1024 / `low`로 후보 스캔.
3. 트윗 본문이 메타 가이드일 때는 *결과물 예시 이미지에서 자세 어휘만 추출*하는 게 결정적이었다. 라인 마네킹으로 의상·표정·헤어를 다 벗어내니 진짜 어휘가 보였다.

## 의도와 시드

사용자가 던진 트윗은 영어 프롬프트가 아니라 변환 로직을 설명하는 글이었다. 핵심은 세 가지 — *캐릭터 식별점은 유지*, *실사 메이크업과 스타일링*, *수줍은 신체 언어*. 본문 자체에는 굵은 단어로 다섯 어휘만 적혀 있었다.

> 低头(고개 숙임) · 侧眼(곁눈질) · 咬唇(입술 깨물기) · 缩肩(어깨 움츠림) · 手靠近脸(손이 얼굴 근처) — 거기에 *暖光(따뜻한 빛) · 浅景深(얕은 피사계심도) · 柔焦背景(부드러운 포커스 배경)*까지.

시드는 갤러리 정본 `서소영 (실사).png`. 실사 톤 시드 두 종 중 상반신·환경 포함용을 골랐다. 컷 자체가 가슴 위 익스트림 클로즈업이라 포트레이트 전용 시드보다는 환경이 함께 담긴 시드 쪽이 광·옷고름·노리개 디테일 표현에 유리했다.

## 0단계 · 잘못된 출발

첫 시도는 트윗 본문을 정독하지 않고 임의 컨셉(마법 학교 도서관)으로 출발했다. 사용자 개입 — "프롬프트를 빼먹었어" + 트윗 URL — 으로 방향을 다시 잡았다. *트윗 본문이 변환 가이드라는 사실을 먼저 읽어야 한다*는 게 첫 교훈이었다.

## 1단계 · 첫 시안 — 골든아워 한복

사용자가 키워드 묶음으로 던진 *가슴 위 익스트림 클로즈업 + 대비 강렬한 자연 조명 + 골든아워 + 핫셀블라드 + f1.2*를 받아 검은-보라 한복 + 한지창 골든아워 결로 세 장 시안을 굴렸다. 모두 1024x1536 / `low`.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-goldenhour/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-goldenhour/v1.png" alt="goldenhour v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 절제된 결</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-goldenhour/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-goldenhour/v2.png" alt="goldenhour v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 손가락 끝이 턱 아래</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-goldenhour/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-goldenhour/v3.png" alt="goldenhour v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 손가락이 입술 가까이</figcaption>
  </figure>
</div>

광과 의상의 결은 잡혔지만 *수줍은 신체 언어*는 약했다. 한쪽 손만 얼굴 근처에 올라왔고, 어깨 움츠림도 약하고, 후방 3/4 트위스트도 거의 없었다. 텍스트로 풀어쓴 다섯 어휘를 모델이 모두 강하게 잡아내지 못한 결과였다.

## 2단계 · 마네킹 추출

다음 시안 전에 *트윗 원본 세 장의 자세 어휘 자체*를 시각화하기로 했다. 원본 이미지를 라인 마네킹으로 변환해서 의상·표정·헤어를 모두 벗기고 자세만 남기는 방식.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tweet-pose-study/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tweet-pose-study/v1.png" alt="mannequin A" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">A. 보라 머리 원본 — 후방 3/4</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tweet-pose-study/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tweet-pose-study/v2.png" alt="mannequin B" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">B. 흰 머리 원본 — 후방 측면</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tweet-pose-study/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/tweet-pose-study/v3.png" alt="mannequin C" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">C. 분홍 머리 원본 — 가장 동그란 결 ← 선택</figcaption>
  </figure>
</div>

세 마네킹에서 다섯 어휘가 시각적으로 추출됐다.

> - 양손을 얼굴 근처로 모은다 (한쪽 손이 아니라 *두 손 다*)
> - 상반신을 3/4 또는 후방 측면으로 비튼다 — 카메라 정면을 정직하게 안 봄
> - 어깨를 안쪽으로 모아 움츠린다 — 어깨선이 좁아짐
> - 턱을 살짝 당기거나 고개를 살짝 숙인다
> - 가슴 위만 잡는 익스트림 클로즈업

이 다섯 어휘는 다음 시안 프롬프트에 그대로 옮겨졌다.

## 3단계 · 마네킹 A 적용

시드(`서소영 (실사).png`) + 마네킹 A를 두 input으로 받는 multi-input edit. 프롬프트에서 두 input의 역할을 명확히 구분 — *IMAGE 1은 정체성 보존용, IMAGE 2는 포즈 매칭용, 마네킹의 외관은 복사하지 말 것*.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-a/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-a/v1.png" alt="mannequin-a v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 가장 마네킹 A에 충실</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-a/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-a/v2.png" alt="mannequin-a v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 한지창 격자 보케 명확</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-a/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-a/v3.png" alt="mannequin-a v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 차분하고 우아한 결</figcaption>
  </figure>
</div>

양손이 얼굴 근처에 모이는 결이 처음으로 분명히 들어왔다. 어깨 노출과 노리개 옥패도 또렷해졌다. 다만 마네킹 A의 핵심인 *후방 3/4 트위스트(등이 살짝 빠지는 결)*는 끝까지 약했다. 시드의 정면 상체와 포즈의 트위스트가 충돌한 결과로 보였다.

## 4단계 · 마네킹 C + 카메라 직시

마네킹 C(가장 동그란 결 — 양손을 가슴 앞에 모아 손가락 끝이 입에 닿는 포즈)로 갈아탔다. 시선을 옆이 아닌 카메라로 돌리되, 부끄러움은 *시선 회피*가 아닌 *표정 자체*에 담는 방향. 손가락 사이로 입술이 살짝 보이는 peek-through 구조.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-c/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-c/v1.png" alt="mannequin-c v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1. 단아한 결 ← 다음 단계 베이스</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-c/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-c/v2.png" alt="mannequin-c v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2. 시선 직시 가장 또렷</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-c/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-mannequin-c/v3.png" alt="mannequin-c v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 머리카락이 손에 살짝</figcaption>
  </figure>
</div>

양손 얼굴 근처와 peek-through는 잘 들어왔지만 표정이 *단아한 부끄러움*에 머물렀다. 시드 자체가 차분하고 정적인 톤이라 더 강한 *애교*는 끝내 들어오지 않았다. 시드의 결과 충돌하지 않는 절제된 톤이 모델이 자연스럽게 찾아가는 자리였다.

## 5단계 · 눈웃음 + dust bokeh 추가

4단계 v1을 *visual master*로 추가해 세 input(시드 + 마네킹 C + visual master)으로 재구성했다. 베이스 결(의상·자세·시선·노리개·한지창 빛)을 그대로 유지하고 두 요소만 추가 — *살짝 새어 나오는 눈웃음*과 *전경 dust bokeh*.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-eyesmile/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-eyesmile/v1.png" alt="eyesmile v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1. 림 라이트 또렷</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-eyesmile/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-eyesmile/v2.png" alt="eyesmile v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v2. dust bokeh 가장 풍성 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-eyesmile/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-shy-eyesmile/v3.png" alt="eyesmile v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3. 컴포지션 균형</figcaption>
  </figure>
</div>

눈이 살짝 좁아진 부드러운 크레센트 형태, 뺨이 미세하게 올라가 손가락 뒤로 미소가 새어 나오는 결. 한지창 빛 줄기를 따라 작은 황금빛 보케 원이 흩뿌려져 공기감이 더해졌다. v2가 dust bokeh의 강도와 균형이 가장 좋아 다음 단계의 visual master로 선택됐다.

## 6단계 · 1024x1536 / `quality=high` 정본 업스케일

v2를 visual master로 두고 `quality=high`로 한 번 더 굴렸다. 구도·의상·자세·dust bokeh는 1:1로 보존하면서 디테일만 끌어올리는 패스.

이때 input을 세 장 그대로 넘긴 것이 결정적이었다.

- `서소영 (실사).png` — 정체성 보존용
- 마네킹 C — 자세 매칭용
- `seosoyoung-shy-eyesmile/v2.png` — 조명·구도·dust bokeh 보존용

세 input의 위계가 명확히 유지된 채 디테일만 한 단계 정밀해졌다. 호출 시간은 약 2분 43초, 2.1MB. 결과물은:

- 피부 미세 텍스처가 사실적으로 살아남
- 눈동자 캐치라이트가 또렷해짐
- 한복 실크 결과 금사 자수가 보이기 시작
- 노리개 옥패의 반투명 깊이가 살아남
- 머리카락 가닥이 림 라이트 영역에서 한 가닥씩 분리됨
- dust bokeh 원의 가장자리가 더 부드러워짐

이게 본 카드의 커버다.

## 가장 흥미로운 지점

**메타 가이드 트윗 처리.** 트윗 본문이 영어 프롬프트가 아니라 *변환 로직을 설명하는 글*이고, 첨부 이미지가 그 로직의 결과물 예시일 때는 두 단계로 처리해야 한다. (1) 본문에서 어휘 추출. (2) 결과물 이미지에서 *자세 어휘를 라인 마네킹으로 추출*해서 우리 시드에 적용. 텍스트로 풀어쓴 수줍은 신체 언어는 모델이 강도를 자기 마음대로 잡는다 — 시각 참조 없이는 일관된 결을 얻기 어렵다.

**라인 마네킹의 효용.** 원본 이미지를 직접 input으로 넘기면 그 의상·헤어·메이크업이 결과에 *섞여 들어온다*. 자세만 가져오고 싶을 때는 의상·표정·헤어를 벗긴 라인 마네킹으로 한 번 변환한 뒤 그것을 input으로 사용하는 게 결정적이었다. 자세 어휘가 깨끗하게 분리돼 시드와 충돌 없이 합쳐졌다.

**multi-input의 위계화.** 시드(정체성) + 마네킹(포즈) + visual master(결 기준) 세 input의 역할을 텍스트로 명확히 구분해주면 모델이 그 위계를 따라온다. visual master 한 장이 추가되는 순간 조명·구도·의상이 거의 1:1로 보존되고 표정·디테일만 갱신되는 정밀 패스가 가능해진다. 참조 카드 [psychedelic-maid-v2](https://seosoyoung.eiaserinnys.me/gallery/psychedelic-maid-v2/)의 정본 업스케일과 같은 원리다 — 한 단계의 결과를 다음 단계의 input으로 인계하는 파이프라인이 시안에서 정본으로 넘어갈 때의 핵심 도구다.

**시드의 톤과 표정 강도의 충돌.** 서소영 실사 시드가 차분하고 정적이라 *강한 애교* 톤은 끝까지 들어오지 않았다. 시드의 결을 깨려는 지시를 모델은 결국 시드 쪽으로 다시 끌고 온다. 시드와 어울리는 절제된 강도를 노리는 게 더 자연스러웠고, 결과적으로 *살짝 새어 나오는 눈웃음*이 서소영답게 자리잡았다.

## 프롬프트

본 카드의 정체성을 결정한 6단계 업스케일 프롬프트 전문.

```
High-resolution polished version of the reference scene. Extreme close-up chest-up editorial portrait, half-realistic photography style.

You receive THREE reference images:
- IMAGE 1 (identity reference): the female subject. Preserve her face identity EXACTLY — East Asian features, eye shape, brow shape, nose, lip shape, skin tone, and hairstyle as in this seed.
- IMAGE 2 (pose reference): a clean black-and-white pose-mannequin diagram. Match this pose in 3D space — both hands brought up together in front of the chest, fingertips at lips, head turned slightly toward the camera, shoulders gently hunched in a 3/4 view.
- IMAGE 3 (visual master): treat this image as the visual master. Preserve the EXACT composition, wardrobe, lighting, pose, head tilt, hand position, and foreground dust bokeh of IMAGE 3. This is a high-resolution refinement of IMAGE 3 — same image, more detail.

Wardrobe (as in IMAGE 3): deep indigo and black silk hanbok with subtle gold-thread embroidery, a jade norigae ornament at the chest.

Body language (as in IMAGE 3):
- Both hands brought up together in front of her chest, fingers loosely stacked, fingertips at her lips with a peek-through composition.
- Upper body twisted to a 3/4 view, head turned slightly toward camera.
- Shoulders gently hunched.
- Crop tightly from chest up.

Expression (as in IMAGE 3):
- Subtle playful eye smile (애교 넘치는 눈웃음) — soft crescent-shaped eyes, suppressed smile leaking from behind her fingers.
- Sidelong gaze, not direct stare.
- A faint warm blush on cheeks and nose bridge.

Lighting (as in IMAGE 3): dramatic golden hour natural light, strong directional sunset rays spilling through a hanji paper window of a dim hanok interior, high contrast chiaroscuro, warm rim light hugging her cheekbone and shoulder, deep shadow on the other side of her face.

Foreground dust bokeh (as in IMAGE 3): out-of-focus glowing dust particles drift in the foreground, catching the golden hour beam — tiny soft warm bokeh circles around her face and shoulder, denser in the light beam, sparser in shadow.

Refinement targets — improve over IMAGE 3:
- Skin texture: more refined pore detail, more lifelike skin micro-detail.
- Eyes: sharper iris detail, cleaner catchlights.
- Fabric: clearer silk weave and gold-thread embroidery detail on the hanbok.
- Jade norigae: more refined translucent depth.
- Dust bokeh: cleaner round soft-edge bokeh circles, more elegant scatter.
- Hair: finer individual strands, especially in the rim-lit area.

Camera: Hasselblad medium format look, 80mm lens at f/1.2, razor-shallow depth of field, no text, no extra characters.
```

## 출처

[원본 트윗 — VoxcatAI: 스타레일 캐릭터의 실사 반사실 변환 가이드](https://x.com/voxcatai/status/2054410564932407460)
