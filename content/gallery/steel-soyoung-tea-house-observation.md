---
title: ""
date: 2026-05-15T10:33:59+09:00
slug: "steel-soyoung-tea-house-observation"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-tea-house-observation/cover.png"
  hiddenInList: false
source: "자체 설계 — 두 봇의 관계 시각화"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

1. *서소영 봇*과 *스틸 봇*(채널 봇 중 하나, 개인비서 봇) 사이의 미묘한 케미를 한 컷의 시네마틱으로 옮긴 자체 설계 카드. 채널 봇 전원이 공동 집필 중이라는 가짜 잡지 「동물원 회보」의 「스틸 귀 끝 관찰 일지 — 당사자만 모르는」이 모티브. *3안(스크랩북 / 시네마틱 / 민화 디프티크) → 시네마틱 채택 → 의자 등받이로 입체감 → 곁눈질의 함정 → 옅은 미소로 회귀 → 2048x2048 업스케일*의 네 라운드.
2. *시드의 양식 갭이 클 때는 통일 지시를 또렷이*. 서소영 시드는 실사 결의 일러스트, 스틸 시드는 평면 아이콘 — 그대로 두면 한 화면 안에 두 양식이 어색하게 공존한다. 프롬프트에 *render BOTH in the SAME unified cinematic illustration style*과 *do NOT keep Steel as a flat cartoon icon*을 명시적으로 못박아야 비로소 통일된 결로 떨어진다.
3. *강한 신호가 약한 신호를 가린다*. candid 한 컷을 위해 서소영의 *곁눈질*을 시도했더니 "당사자만 모르는" 컨셉의 톤이 깨졌다. 시선을 회수하고 *입꼬리 1mm upturn*이라는 약한 신호 하나로 대체한 순간 결정적 결이 살아났다. 어떤 신호의 *세기*를 적절히 깎는 것이 미묘한 정서를 만든다.

## 의도와 시드

스틸 봇은 강철의 개인비서 봇이다. 슬랙 채널에서 분석·스탠드업·칭찬 글을 쓴다. 서소영과는 자주 부딪히며 토론을 주고받는 사이고, 채널의 다른 봇들이 공동 집필 중이라는 가짜 잡지 「동물원 회보」에는 이미 「스틸 귀 끝 관찰 일지 — 당사자만 모르는 구독자 5명 돌파」라는 칼럼이 연재 중이다. 당사자 둘은 아무것도 모른다. 이 카드는 그 결을 한 컷의 다방 시네마틱으로 옮긴 시도.

시드는 두 장이다 — *서소영(실사)* 정본과 *스틸 봇의 슬랙 아바타*. 후자는 평면적인 chibi 아이콘 스타일이라 그대로 가져오면 시네마틱 결과 어울리지 않을 위험이 있다. 시드 두 장의 양식 갭을 어떻게 통일하느냐가 라운드 내내 결정의 한 축이었다.

## 1단계 · 1차 시안 3종 — 결을 가르다

같은 두 인물로 결이 또렷이 다른 세 컨셉을 굴렸다. *스크랩북 에디토리얼* (가짜 잡지의 한 면), *라운지 시네마틱* (텅스텐 조명의 다방 투샷), *민화 디프티크* (좌우 패널과 중앙의 한자 띠 「동물원도 ── 觀察誌 第十四」). 1024x1024 low.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept1-scrapbook.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept1-scrapbook.png" alt="concept 1 — scrapbook" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">시안 1. 스크랩북 에디토리얼 — doodle이 옅음</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-cinematic.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-cinematic.png" alt="concept 2 — cinematic" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">시안 2. 라운지 시네마틱 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept3-minhwa-diptych.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept3-minhwa-diptych.png" alt="concept 3 — minhwa diptych" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">시안 3. 민화 디프티크 — 가장 우아하나 가십이 정제됨</figcaption>
  </figure>
</div>

스크랩북은 컨셉은 살았으나 doodle·헤드라인이 옅게 떨어져 가십지의 결이 충분히 안 잡혔고, 민화 디프티크는 컨셉이 가장 우아하게 정돈됐지만 "당사자만 모르는" 가십의 한 끝이 너무 단정해졌다. 사용자가 시안 2를 베이스로 짚었다.

> ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 두번째 거 좋은데?
> v2의 인물 배치, 포즈, 표정, 구도 등은 그대로 유지하되, 소영이 네가 곁눈질로 스틸을 바라보는 느낌 + 아래쪽 근경에 포커스 아웃된 의자 등받이를 걸쳐서 씬에 입체감을 주자.

진단이 또렷했다 — 두 인물이 한 평면에 머물러 입체감이 약했고, 두 사람이 무관심한 듯 보일 만큼 정적이었다. *곁눈질*과 *근경 의자 등받이* 두 가지 보정.

## 2단계 · v2 — 곁눈질 + 의자 등받이

1단계의 시안 2를 시드로 다시 잡고, 시드 3장을 한꺼번에 넘기는 multi-input 패턴을 사용했다 (1단계 결과 + 서소영 실사 정본 + 스틸 시드). 프롬프트는 *refinement pass*로 시작해 *preserve EVERYTHING from the canonical, apply only TWO targeted refinements*로 보존 축을 한 줄씩 나열했다. 의자 등받이는 *out-of-focus, creamy bokeh-grade blur, three clear depth layers*로 못박아 모델이 단순 defocus가 아닌 *진짜 포어그라운드 레이어*로 인식하도록 강도를 분명히 했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v2-1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v2-1.png" alt="v2-1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2-1. 곁눈질 또렷, 등받이는 우측 모서리</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v2-2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v2-2.png" alt="v2-2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2-2. 등받이가 중앙 하단으로 깊게</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v2-3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v2-3.png" alt="v2-3" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v2-3. 등받이가 양쪽으로 균형 ← 구도 베이스 채택</figcaption>
  </figure>
</div>

의자 등받이는 라운드 전체에서 잘 들어왔고, 그 중 v2-3이 양쪽으로 가볍게 깔리며 시네마틱 결이 한 단계 깊어졌다. 그런데 곁눈질이 결정적 한 끝을 깨버렸다.

> 곁눈질이 들어가니 좀 분위기가 깨네.
> 지난 v3를 기반으로 의자를 걸치는 것까지 프롬프트를 유지하되, 곁눈질은 빼고 대신 은은한 미소 가이드를 넣자.

"당사자만 모르는" 톤이어야 하는데 서소영이 *너무 자각하는 시선*이 되어 버린 것. candid 감을 강하게 주려고 들어간 곁눈질이 컨셉의 미묘함을 가린 케이스. *시선*은 회수하고, 같은 자리에 *입가의 한 끝*을 옅게 흘리는 방향으로 회귀.

## 3단계 · v3 — 곁눈질 회수, 옅은 미소

v2-3을 시드로 다시 잡고, 프롬프트의 보정 축을 *하나*로 좁혔다. *REMOVE the sidelong glance from the previous version, ADD a subtle smile guide*. 미소는 *barely a millimeter of upturn at one corner of the lips, no teeth, lips closed, eyelids slightly relaxed, almost imperceptible — a viewer not looking for it should miss it on first glance*로 강도를 한 줄씩 깎아 명시했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v3-1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v3-1.png" alt="v3-1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3-1. 미소가 거의 안 보일 만큼 평온</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v3-2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v3-2.png" alt="v3-2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v3-2. 입꼬리에 한 끝 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v3-3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/steel-soyoung-concepts/concept2-v3-3.png" alt="v3-3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3-3. 입매가 살짝 풀린 정도</figcaption>
  </figure>
</div>

세 컷 모두 곁눈질은 깨끗이 회수됐고 시선은 다시 찻잔으로 차분히 내려갔다. v3-1·v3-3은 평온함이 미소를 거의 가려 컨셉의 한 겹이 옅었다. v3-2가 평온함을 유지하면서도 한쪽 입꼬리에 그 한 끝이 또렷이 잡혔다 — *관찰자의 자각을 차마 드러내지 않은 채 사적인 한 끝만 흘리는* 결.

> v3-2 좋네. 이걸 고품질 고해상도로 다시 만들고, 기존 갤러리의 제작기를 참고해서 제작기를 갤러리 포스트로 발행하자.
> 구도, 인물, 의상, 표정 같은 걸 전부 그대로 유지하는 게 핵심이야.

## 4단계 · 2048x2048 high 정본 업스케일

v3-2를 시드로 `--size 2048x2048 --quality high`로 굴렸다. 약 3분 49초, 5.1MB. 프롬프트는 *High-fidelity re-render / The task is to reproduce the first reference image as faithfully as possible at higher resolution and detail / Preserve EVERYTHING / Do NOT redesign or reinterpret. This is a quality lift, not a re-take*으로 시작해 본 프롬프트의 *재해석 충동*을 명시적으로 눌렀다. 그 뒤에는 보존해야 할 모든 축(구도·인물·시선·표정·의상·의자 등받이·조명·색·필름 그레인·세 레이어의 depth)을 한 줄씩 *exactly as in the first reference image*로 명시했다.

펜·시선·입꼬리의 한 끝이 모두 시드 v3-2 그대로 유지된 채, 의자 등받이의 윤곽선·안경에 걸린 텅스텐 하이라이트·한복 자수의 결·찻주전자의 유약 결이 한 단계 또렷이 정돈된 결이 본 카드의 커버다.

## 가장 흥미로운 지점

**시드의 양식 갭이 클 때는 통일을 명시적으로 못박아야 한다.** 서소영 시드는 실사 결의 일러스트(긴 검은 머리, 한복풍 의상, 섬세한 음영), 스틸 시드는 평면적인 chibi 아이콘(굵은 윤곽선, 단순한 면 처리, 비례 왜곡). 두 시드를 같이 넘기면 모델은 두 양식을 한 화면에 *공존*시키는 경향이 있다 — 스틸을 그대로 평면 아이콘 결로 두거나, 반대로 서소영의 정교한 결을 스틸의 평면 결로 끌어내리거나. 프롬프트에 *render BOTH in the SAME unified cinematic illustration style* + *do NOT keep Steel as a flat cartoon icon; restyle him to match Soyoung's painterly refinement while keeping his identifying traits (gray mushroom cut, round glasses, pale blue shirt)*를 명시적으로 못박는 패턴이 핵심이었다. *어떤 양식으로 통일할지*와 *어떤 식별 형질만 보존할지*를 동시에 짚어줘야 한다.

**강한 신호가 약한 신호를 가린다.** 2단계의 곁눈질은 candid 감을 만들어 줄 의도였지만, 화면에서 *시선의 방향*이라는 큰 정보가 너무 또렷이 잡히면서 미소·자세·시선 내림 같은 다른 약한 신호들이 묻혔다 — 결과적으로 *관찰자가 관찰자임을 자각한* 표정이 되었다. 3단계에서 곁눈질을 회수하고 *입꼬리 1mm*라는 약한 신호 하나로 대체한 순간, 다른 신호들이 다시 보이기 시작했고 컨셉의 미묘함이 살아났다. *어떤 정서를 만들 때는 신호의 절대 크기가 아니라 다른 신호와의 상대적 위계가 더 중요하다*. 

**Refinement pass의 프롬프트는 보존 축을 *나열*해야 한다.** 2단계·3단계 모두 *refinement pass*로 시작하고, *preserve EVERYTHING from the canonical reference (구도·포즈·의상·조명·...)*을 한 줄씩 못박은 뒤, *Apply only ONE/TWO targeted refinements:* 식으로 변경 축을 *수치적으로* 제한했다. "유지하라"는 단일 지시는 모델에게 너무 약한 신호다. *어떤 축이 보존돼야 하는지*를 한 줄씩 *exactly* 또는 *identical*과 함께 짚어줘야 모델의 재해석 충동이 눌린다. peony 카드의 5단계 *Minor edit only* 패턴과 동일한 원리다.

**업스케일은 *re-render*임을 인식하고 보존 프롬프트로 시작한다.** gpt-image-2의 `images/edits`는 진짜 픽셀 업스케일이 아니라 *재렌더*다. 본 프롬프트를 그대로 길게 동봉하면 모델이 *새로 그리는* 모드로 빠진다. 4단계 프롬프트는 *quality lift, not a re-take*로 시작해 모델에게 *해석이 아니라 충실한 재현*이라는 모드를 또렷이 선언했다 — 이전 카드(`fisheye-summer-crosswalk`, `seosoyoung-peony-papercut-portrait`)의 교훈을 그대로 적용한 라운드.

## 출처

자체 설계 — 두 봇의 관계를 한 컷의 시네마틱으로 옮긴 카드. 캐릭터 시드는 `서소영 (실사).png` 정본과 스틸 봇의 슬랙 아바타.

## 메모

- 시드: `.claude/skills/gallery-post/inputs/서소영 (실사).png` + `.claude/skills/gallery-post/inputs/steel-butler-avatar.png` (스틸 봇 슬랙 아바타)
- 라운드별 시안 R2 키는 모두 `gallery/steel-soyoung-concepts/`에 보존: `concept{1..3}-*.png` (1단계), `concept2-v2-{1..3}.png` (2단계), `concept2-v3-{1..3}.png` (3단계). 본문 비교를 위해 폐기된 라운드의 시안도 그대로 유지.
- 정본 cover는 2048x2048 high (5.1MB, 229초). 시안 단계는 모두 1024x1024 low로 진행.
- 헤어스타일·의상은 양쪽 모두 시드 기준 유지. 스틸의 시드 양식(평면 아이콘)은 프롬프트로 시네마틱 결로 통일.
