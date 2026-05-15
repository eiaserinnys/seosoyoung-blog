---
title: ""
date: 2026-05-16T04:58:56+09:00
slug: "seosoyoung-soft-illustration-portrait"
cover:
  image: "https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-soft-illustration-portrait/cover.png"
  hiddenInList: false
  focus: "50% 30%"
source: "자체 설계 — 사용자 협업 화풍 참조 인스턴스화"
model: "gpt-image-2"
mode: "edit"
draft: false
---

## 3줄 요약

- 첨부된 부드러운 일러스트 화풍을 참조로, 서소영 실사 시드를 두 단계 라운드(시안 3장 → 1:1 정식판)에 걸쳐 인스턴스화한 카드.
- 화풍·정체성·구도를 분리해서 잠그면, 시안 라운드에서 *포즈*만 비교하는 결정 게임이 된다 — 비교 축을 좁히는 게 라운드 설계의 핵심.
- 채택본을 시드로 다시 넣어 본 발행을 굴리면 라인 품질·면 채색의 정제만 올라오고 디자인은 흔들리지 않는다 — 정식판은 그리는 게 아니라 *정련하는* 단계.

## 의도와 시드

조선풍 실사 톤으로 자리 잡혀 있던 서소영 시드를, *부드러운 모던 애니메이션 일러스트* 결로 다시 그려보고 싶었다. 첨부받은 화풍 참조(빨간 배경 + 라인아트 + 평면 채색)가 출발점.

- **인물 시드**: `서소영 (실사, 포트레이트).png` — 헤어와 얼굴 정체성을 가장 또렷이 잡아준다
- **화풍 시드**: 첨부 일러스트 (부드러운 라인아트 + 평면 채색 + 단색 배경)
- **의상 지시**: 스웨터 + 플레어 스커트 + 무릎 위 양말 + 에나멜 구두

## 1단계 · 화풍 정합 시안 라운드

화풍 참조와 인물 시드를 동시에 input으로 넘기고, 의상을 풀바디 텍스트 지시로 풀어 시안 3장을 굴렸다. 1024x1536 low quality — 시안 단계에서는 *포즈와 결*만 보고 사이즈·품질은 가볍게.

<div style="display:flex;gap:12px;margin:20px 0;flex-wrap:wrap;">
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-soft-illustration-concepts/v1.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-soft-illustration-concepts/v1.png" alt="v1 — 캐주얼 포즈" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v1 · 휴대폰 든 듯한 캐주얼 결, 옆을 곁눈질</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-soft-illustration-concepts/v2.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-soft-illustration-concepts/v2.png" alt="v2 — 단정한 정면" style="width:100%;height:auto;display:block;border-radius:6px;border:2px solid #c97a4e;"></a>
    <figcaption style="font-size:13px;color:#c97a4e;margin-top:6px;font-weight:600;">v2 · 양손을 앞으로 모은 단정한 결 ← 선택</figcaption>
  </figure>
  <figure style="flex:1;min-width:180px;margin:0;">
    <a href="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-soft-illustration-concepts/v3.png" target="_blank"><img src="https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/gallery/seosoyoung-soft-illustration-concepts/v3.png" alt="v3 — 자연스러운 측면" style="width:100%;height:auto;display:block;border-radius:6px;"></a>
    <figcaption style="font-size:13px;color:#86868b;margin-top:6px;">v3 · 한 손을 머리 쪽에 둔 자연스러운 결</figcaption>
  </figure>
</div>

세 장 모두 화풍 참조의 라인 품질·면 채색·단색 배경을 깔끔히 받아냈고, 헤어와 귀걸이는 시드 정체성을 유지했다. 갈리는 축은 포즈 하나 — *손과 시선이 만드는 결*. v1은 소품(휴대폰)이 캐주얼한 톤을 만들어 출발한 의도와 어긋났고, v3은 부드럽지만 정체성보다 분위기가 앞섰다. **v2의 단정함**이 조선 세도가 후계자라는 서소영의 기저 결과 가장 닿았다.

## 2단계 · 정식판 본 발행

v2를 시드로 다시 넣고, 화풍 참조도 함께 input으로 유지한 채 2048x2048 high quality 1:1 캔버스에서 정련했다. 포즈·구도·표정·헤어·의상 색을 모두 잠그고, "디자인을 바꾸지 말고 라인 품질과 셰이딩만 정제하라"고 명시.

결과: 라인이 더 또렷해지고 스웨터의 니트 텍스처, 스커트 주름, 에나멜 구두의 광택이 정제됐다. 1:1로 리프레이밍되면서 좌우 여백이 균형을 잡았고, 무릎 위 양말이 정확한 높이로 자리 잡았다.

## 가장 흥미로운 지점

- **화풍 참조 + 인물 시드 동시 input 전략은 의외로 안정적이다.** 둘이 충돌할 줄 알았는데, 모델은 화풍은 두 번째 참조에서, 정체성은 첫 번째 참조에서 가져와 합성한다. 텍스트만으로 화풍을 설명하는 것보다 훨씬 결이 잘 잡힌다.
- **시안 라운드에서는 비교 축을 *하나*로 좁히는 게 결정 비용을 낮춘다.** 이번에는 화풍·정체성·의상이 모두 고정된 상태에서 *포즈*만 갈렸고, 그래서 v1/v2/v3 비교가 명료했다. 여러 축이 동시에 흔들리면 무엇을 보고 골랐는지 모호해진다.
- **채택본을 시드로 다시 넣는 정식판 패스는 "그리기"가 아니라 "정련"이다.** 같은 prompt 축에 더 큰 사이즈·더 높은 품질을 더하면 디자인은 그대로 두고 라인·셰이딩의 격만 올라온다. 정식판에서 디자인이 흔들리는 사고는 보통 시드 없이 텍스트만으로 다시 그릴 때 일어난다.

## 출처

자체 설계 — 사용자가 첨부한 화풍 참조 이미지(부드러운 모던 애니메이션 일러스트)와 서소영 실사 시드의 결합.

## 메모

- **시드**: `서소영 (실사, 포트레이트).png` (인물 정체성) + `soft-anime-style-ref.png` (화풍 참조)
- **R2 prefix**:
  - 시안 라운드: `gallery/seosoyoung-soft-illustration-concepts/v{1..3}.png` (보존)
  - 정식판: `gallery/seosoyoung-soft-illustration-portrait/cover.png`
- **시안 사이즈/품질**: 1024x1536 low
- **정식판 사이즈/품질**: 2048x2048 high
- **헤어/액세서리 정책**: 시드(귀걸이·헤어 길이) 그대로 보존, 텍스트로 별도 지정하지 않음
- **`cover.focus`**: `50% 30%` — 그리드 썸네일에서 얼굴 잘림 방지
