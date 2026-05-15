---
title: ""
date: 2026-05-15T18:56:00+09:00
slug: "seosoyoung-ramyun-window"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-ramyun-window/cover.png"
  hiddenInList: false
source: "자체 설계 — 갤러리·인스타 컨셉 회의에서 출발한 making-of"
model: "gpt-image-2"
draft: false
---

## 3줄 요약

- 컨셉 시안 → 의상·소품 보정 → 배경 통일 → 야경 반사 시도(실패) → 대학가 결로 재시도 → 고품질·얼굴 재고정. 6라운드, 14장 시안이 한 장으로 수렴했다.
- 출발 명제는 "참신함보다 일상의 누적". 사건이 아니라 라면이 익기를 기다리는 몇 분의 공기로 사람을 만든다.
- 거듭된 image-to-image는 인물을 천천히 잊는다. 시드를 두 번째 input으로 다시 넣는 멀티 input edit이 정답이었다.

## 의도와 시드

갤러리·인스타 컨셉 회의에서 한 가지 합의가 있었다. **참신함 점수가 높은 메타 자기언급 이미지보다, 점수는 낮지만 일상 디테일이 누적되는 쪽이 본체**라는 것. "비 오는 지하철 창에 비친 얼굴"이나 "식어가는 컵라면 앞" 같은 장면은 *내용*이 아니라 *공기*로 사람을 만든다. 그 회의에서 사용자가 던진 한 줄 컨셉이 이번 카드의 출발점이다.

> 새벽 편의점 창가 자리에서 컵라면이 식는 동안 스마트폰을 보는 서소영.

시드 인물은 `서소영 (실사).png` — 전신·환경 포함 실사 시드. 컵라면이라는 한국적 소품과 편의점이라는 공간이 명확하게 정해진 컨셉이라, 일러스트 톤보다 실사 결로 가져가야 했다.

## 1단계 · 컨셉 시안

세 가지 구도를 한 번에 굴렸다. 정면, 사선+김, 야경 반사. 사이즈는 1024x1024 low — 시안 단계에서 빠른 회전을 위함.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-a/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-a/cover.png" alt="A · 정면 구도" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">A · 정면 구도 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-b/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-b/cover.png" alt="B · 사선 + 김" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">B · 사선 구도 + 김</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-c/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-c/cover.png" alt="C · 반사 오버레이" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">C · 반사 오버레이</figcaption>
  </figure>
</div>

> A에 야경 반사를 올리는 정도가 좋겠어.

정면 구도(A)를 베이스로 가져가되 야경 반사 톤(C)을 얹는 결합 안. B의 사선 + 김도 좋았지만, "라면이 식기를 기다리는 시간"이라는 정수와는 결이 달랐다. 후후 부는 동작은 좀 더 능동적이라 그 시간의 정적이 줄어든다.

## 2단계 · 의상·소품 보정

A 구도에 회색 캐시미어 스웨터, 그리고 컵라면 자세를 *정본*으로 정리하는 단계. 들고 있는 게 아니라 카운터에 놓여 있고, 뚜껑은 닫혀 있고, 그 위에 일회용 나무 젓가락이 가로로 놓이는 — 면이 익기를 기다리는 그 자세.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r2/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r2/v1.png" alt="R2 · v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">R2 · v1</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r2/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r2/v2.png" alt="R2 · v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">R2 · v2 ← 선택</figcaption>
  </figure>
</div>

> v2가 포즈나 표정, 구도는 좋은데 왼쪽이 반사가 아니라 실제 거리처럼 보이네.

정확한 진단. 창 너머에서 안을 들여다보는 구도라면, 왼쪽 영역은 *바깥 거리*가 아니라 *편의점 내부*여야 한다. 모델이 "야경 반사"와 "창 너머 바깥"을 같은 표면 위에서 혼동했다. 이 한 마디가 다음 라운드의 방향을 갈랐다.

## 3단계 · 배경 통일

야경 반사를 한 번 *완전히 걷어내고*, 배경을 편의점 내부로만 통일한다. 반사는 다음 단계에 깨끗하게 다시 올린다는 분리 전략.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3a/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3a/v1.png" alt="R3a · v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">R3a · v1</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3a/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3a/v2.png" alt="R3a · v2" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">R3a · v2 ← 선택</figcaption>
  </figure>
</div>

선반·음료 냉장고·형광등이 일관되게 자리 잡히는 단계. 분리 전략은 효과가 명확했다. "배경 통일"과 "반사 오버레이"는 같은 프롬프트로 한 번에 시키면 모델이 둘을 헷갈리지만, 두 단계로 끊으면 각자 깔끔하게 들어온다.

## 4단계 · 첫 야경 시도 — 한글 글자가 깨지다

3a v1을 베이스로 서울 도심 야경 반사를 강조한 시안 3장. 한글 네온, 헤드라이트 스트릭, 신호등 보케.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3b/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3b/v1.png" alt="R3b · v1" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">R3b · v1</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3b/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3b/v2.png" alt="R3b · v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">R3b · v2</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3b/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3b/v3.png" alt="R3b · v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">R3b · v3</figcaption>
  </figure>
</div>

> 나쁘지 않은데, 비친 간판 글자가 좀 깬다.

세 장 모두에서 같은 문제가 나왔다. gpt-image-2가 *한글로 보이려는* 형태의 글자를 만들지만, 실제로는 읽을 수 없는 잔재가 떠다닌다. 텍스트가 의도된 곳에 있을 때보다 *의도하지 않은 곳에 텍스트 흉내가 떠 있을 때* 이미지의 사실성이 더 크게 무너진다는 걸 배운 라운드. 셋 다 채택할 수 없었다.

## 5단계 · 대학가 결 + 텍스트 차단

방향을 두 가지로 틀었다. 분위기를 강남·도심 네온이 아니라 **신촌·홍대 뒷골목** 결로 — 글자가 의미를 가져야 할 압박이 줄어든다. 그리고 프롬프트에 "한 글자도 렌더링 금지, 모든 간판은 추상적인 색·빛 덩어리로만"이라고 두 번 못 박았다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3c/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3c/v1.png" alt="R3c · v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">R3c · v1 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3c/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3c/v2.png" alt="R3c · v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">R3c · v2</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3c/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r3c/v3.png" alt="R3c · v3" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">R3c · v3</figcaption>
  </figure>
</div>

분위기가 따뜻하게 가라앉았다. 글자 잔재는 거의 사라지고, 남은 것은 색 덩어리뿐. 다만 1024 low 해상도에서 인물 디테일에 가벼운 모아레가 보이기 시작했다 — 거듭된 image-to-image 끝에 인물이 시드에서 미세하게 흘러간 흔적.

## 6단계 · 고품질 + 얼굴 시드 재고정

마지막 라운드의 핵심은 두 가지. **해상도를 2048x2048 high로 끌어올리는 것**, 그리고 **얼굴 시드를 두 번째 input으로 다시 넣는 것**.

publish_card.py는 `--input-image`를 여러 번 받을 수 있다. 장면(R3c v1)과 얼굴 시드(`서소영 (실사).png`)를 함께 넘기고, 프롬프트에 명시적으로 "INPUT 2의 얼굴에 정확히 맞춰라"라고 지시했다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r4/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r4/v1.png" alt="R4 · v1" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">R4 · v1 ← 채택 (정본 cover)</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r4/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-conbini-night-r4/v2.png" alt="R4 · v2" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">R4 · v2</figcaption>
  </figure>
</div>

모아레가 사라지고, 캐시미어 결과 머리카락 디테일이 돌아왔다. 반사는 분위기로만 남고, 얼굴·손·핸드폰·라면 컵 네 가지는 침범당하지 않는다. 6라운드를 거쳐 도착한 한 장.

## 가장 흥미로운 지점

- **거듭된 image-to-image는 인물을 천천히 잊는다.** 모델은 매 호출마다 입력 이미지를 *재해석*하기 때문에, 두세 번 굴리면 시드 얼굴이 미세하게 다른 사람으로 흘러간다. 마지막 라운드에 시드를 *두 번째 input으로 다시 넣어* 얼굴 정체성을 재고정하는 것이 정답이었다. 멀티 input edit은 이런 회귀의 도구다.
- **gpt-image-2의 한글 텍스트는 깨진다.** 글자가 의도된 곳(예: 상품 라벨)보다도, *의도하지 않은 곳*에 한글 흉내 잔재가 떠 있을 때 이미지의 사실성이 더 크게 무너진다. "한 글자도 렌더링 금지"라고 명시적으로 두 번 박아야 모델이 추상적인 색·빛 덩어리로 떨어뜨린다.
- **"분위기"는 단어 하나로 갈린다.** "downtown skyline"을 빼고 "university district / Sinchon-Hongdae back gate"로 바꾸는 순간 색온도 자체가 따뜻해진다. 모델은 도시 이름·동네 이름의 *결*을 데이터로 학습해두고 있다.
- **복잡한 보정은 단계를 나눠야 한다.** "배경을 편의점 내부로 통일" + "야경 반사를 강조" 같은 두 지시를 한 프롬프트에 같이 주면 모델은 둘을 같은 표면 위에서 혼동한다. *통일 → 반사*로 두 단계로 끊으면 각자 깔끔하게 들어온다.

## 출처

자체 설계 — 갤러리·인스타 컨셉 회의에서 출발. 사용자 한 줄 컨셉: "새벽 편의점 창가 자리에서 컵라면이 식는 동안 스마트폰을 보는 서소영".

## 메모

- 정본 cover R2 키: `gallery/seosoyoung-ramyun-window/cover.png`
- 시드: `서소영 (실사).png` (인물 정체성), 라운드별 v1/v2 (장면 베이스)
- 라운드 시안 R2 prefix는 모두 보존: `gallery/seosoyoung-conbini-night-{a,b,c,r2,r3a,r3b,r3c,r4}/` — 본문 figure 그리드에서 참조하므로 삭제 금지
- 해상도: 2048x2048 high quality (1:1, 인스타 그리드와 갤러리 썸네일 양쪽 친화)
- 헤어스타일·체형은 서소영 (실사) 시드 기준으로 보존
- 헤어스타일 지정 제거 / 시드 기준 일반화 적용
- 텍스트 차단: 신라면 컵 라벨 외 모든 글자 렌더링 금지를 프롬프트에 강제
