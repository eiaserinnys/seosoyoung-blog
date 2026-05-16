---
title: ""
date: 2026-05-16T17:24:49+09:00
slug: "seosoyoung-amp-guitar"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-amp-guitar/cover.png"
  hiddenInList: false
source: "자체 설계 — 일상복 3면도 시드 기반 일상 한 컷"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

- 일상복 3면도 시드 한 장으로 "앰프 위에 앉아 기타를 다루는" 일상 한 컷을 세 가지 결로 굴리고 한 장을 채택했다.
- 같은 시드·같은 구도라도 손 동작과 시선·FACS 코드만 바꾸면 "조율 / 막힘 / 한숨" 세 개의 다른 이야기가 나온다.
- 시안은 모두 `1024x1536 low`로 가볍게 굴리고, 채택안만 시안 결과물 자체를 다시 input으로 넣어 `2048x2048 high` 1:1로 재렌더링했다.

## 의도와 시드

일러스트 시드는 정적인 3면도라 캐릭터의 정체성은 잡히지만 "움직이는 결"은 잡히지 않는다. 그래서
*일상의 한 장면 안에서 같은 인물이 어떻게 다른 표정을 짓는지*를 보고 싶었다. 소품은 전자 기타 앰프 위에 앉은 자세 하나로 고정하고, 차이는 손이 어디를 만지는가와 얼굴 근육 어디가 움직이는가로만 만들어 보기로 했다.

시드는 일상복 3면도 (회색 오버사이즈 스웨터 / 검은 미니 스커트 / 검은 니삭스 / 메리제인). 헤어와 의상은 시드 정본을 그대로 따른다.

## 1단계 · 컨셉 라운드

세 컷 모두 1024x1536 low로 가볍게 굴렸다. 손 동작 / 시선 방향 / FACS 코드만 갈아 끼우는 식이다.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-amp-guitar-v1-tuning/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-amp-guitar-v1-tuning/cover.png" alt="조율 시안" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v1 · 조율 — AU4·AU7·AU24 약한 집중 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-amp-guitar-v2-stuck/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-amp-guitar-v2-stuck/cover.png" alt="막힘 시안" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v2 · 코드에서 막힘 — AU1+AU4, AU20 약</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-amp-guitar-v3-breather/cover.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-amp-guitar-v3-breather/cover.png" alt="한숨 시안" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3 · 한숨 돌리기 — AU43, AU26, AU12 약</figcaption>
  </figure>
</div>

> 이건 전부 좋은데? 왜 이런 비일상적인 이미지는 이렇게 잘 만드는 거지

v1을 채택했다. 헤드머신을 돌리는 손과 줄을 살짝 누르는 다른 손, 그리고 입을 다문 채 조용히 음을 듣는 표정의 결이 가장 안정적이다. v2는 의도한 안쪽 눈썹의 솟음(AU1+AU4)이 살짝 흐려졌고, v3은 자세가 의외로 단정하게 떨어져 "지친 한숨"보다는 "잠시 멈춰서 호흡 고르기" 쪽으로 미끄러졌다. 두 컷 모두 B컷으로 결이 좋아 본문에 함께 둔다.

## 2단계 · 정본 재렌더

채택안만 1:1 2048x2048 high로 다시 굽는다. 이번에는 character sheet (일상복 3면도) 와 함께 **v1 시안 자체를 두 번째 input으로** 넣어 구도·표정·포즈가 한 점도 어긋나지 않게 했다. 1024x1536 시안의 결을 그대로 정사각으로 옮기면서 인물을 우하단으로 밀고, 좌상단 1/3을 통째로 비워 텍스트 오버레이가 들어갈 자리를 만들었다.

디테일이 한 단계 올라온다. 페그를 돌리는 손가락 마디·메이플 넥의 결·펜더 그릴 클로스·머리카락 끝의 컬이 모두 깔끔해졌다.

## 가장 흥미로운 지점

- **시드 + 시안 자체를 동시에 input으로 넣는 패턴**이 잘 작동한다. character sheet 한 장만으로 재렌더하면 구도가 살짝씩 어긋나기 쉬운데, 채택 시안을 두 번째 reference로 넣으면 *정체성은 sheet에서, 구도·표정은 시안에서* 가져온다.
- 같은 인물·같은 소품·같은 자세에서 **손이 어디를 만지는가** 한 가지만 바꿔도 시점·시선·표정이 자연스럽게 따라온다. FACS 코드를 따로 지시하지 않아도 손이 페그에 있으면 시선이 페그로 가고 입이 다물어진다 — 신체가 표정을 끌고 간다.
- 좌상단 여백은 텍스트 자리이기도 하지만, *인물이 가진 정적인 결*을 보강하는 음의 영역이기도 했다. 시안 단계의 셋 중 어떤 컷도 여백이 부족했고, 본 발행에서 명시적으로 "상단 좌측 1/3은 통째로 비워라"라고 지시하니 비로소 톤이 잡혔다.

## 출처

자체 설계. 일상복 3면도 시드는 `inputs/서소영 (일상복 3면도).png` 정본.

## 메모

- R2 prefix: 본 cover `gallery/seosoyoung-amp-guitar/cover.png` · 시안 `gallery/seosoyoung-amp-guitar-v{1..3}-{tuning,stuck,breather}/cover.png` (시안 R2 객체는 본문 figure 참조용으로 보존)
- 시드: `서소영 (일상복 3면도).png` (정체성) + `seosoyoung-amp-guitar-v1-tuning.png` (구도)
- 시안 단계 .md 3장은 `draft: true`로 그대로 둠 — 사이트에는 본 cover 한 장만 노출, 시안은 R2 이미지로만 본문에 인용
- 헤어스타일·의상은 시드 정본 유지, 텍스트 프롬프트는 시드 기준으로 일반화
