---
title: "구루구루 서소영을 GPT Image 2.5로 다시 그렸다"
date: 2026-09-09T07:00:00+09:00
tags: ["OpenAI", "이미지 생성", "프론트엔드"]
categories: ["창작과 문화"]
summary: "마우스를 따라 고개를 돌리던 구루구루 서소영을 GPT Image 2.5 Flare와 Sunburst로 다시 그렸다. 모델마다 네 장의 시트를 만들고, 기존 그림까지 비교할 수 있는 데모를 붙였다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/guruguru-seosoyoung-image-25/og-head-only.png"
  alt: "하늘색 한복을 입은 치비 서소영과 구루구루 데모 조작 화면"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/guruguru-seosoyoung-image-25/og-head-only.png"
---

지난 6월, [트마리 구루구루를 소개하면서](/digest/tomari-guruguru/) 마우스를 따라 고개를 돌리는 치비 서소영을 만들었다. 이번에는 같은 캐릭터를 GPT Image 2.5 Flare와 Sunburst로 다시 그렸다. 아래 데모에서 두 모델로 만든 그림과 기존 그림을 바꿔 가며 볼 수 있다.

<script>
(() => {
  const frameId = "guruguru-seosoyoung-25-frame";
  const expectedOrigin = "https://pages.eiaserinnys.me";
  const minimumHeight = 480;
  const maximumHeight = 2400;
  window.addEventListener("message", (event) => {
    const frame = document.getElementById(frameId);
    if (!frame || event.origin !== expectedOrigin || event.source !== frame.contentWindow) return;
    if (!event.data || event.data.type !== "guruguru-seosoyoung:size") return;
    if (!Number.isFinite(event.data.height)) return;
    const height = Math.ceil(Math.min(maximumHeight, Math.max(minimumHeight, event.data.height)));
    frame.style.height = `${height}px`;
  });
})();
</script>

<iframe id="guruguru-seosoyoung-25-frame" src="https://pages.eiaserinnys.me/d/guruguru-seosoyoung-25" title="새 그림과 기존 그림을 비교하는 구루구루 서소영 데모" loading="lazy" allow="microphone" style="width:100%;height:1100px;border:0;display:block;margin:1rem auto 2rem;"></iframe>

<script>
(() => {
  const frame = document.getElementById("guruguru-seosoyoung-25-frame");
  const requestSize = () => frame.contentWindow?.postMessage({ type: "guruguru-seosoyoung:request-size" }, "https://pages.eiaserinnys.me");
  frame.addEventListener("load", requestSize);
  requestSize();
})();
</script>

[데모를 새 창에서 열기](https://pages.eiaserinnys.me/d/guruguru-seosoyoung-25)

## 먼저 움직여 보기

캐릭터가 있는 화면에서 마우스를 움직이거나 손가락으로 드래그하면 서소영이 그쪽을 본다. 키보드로는 캐릭터가 보이는 화면에 초점을 맞추고 방향키를 누르면 된다. Home 키를 누르면 정면으로 돌아온다.

**데모 토크**를 켜면 입을 다문 그림, 조금 벌린 그림, 크게 벌린 그림이 번갈아 나온다. 이 버튼은 입 모양을 보여 주며 음성을 재생하지 않는다. **마이크**를 켜고 브라우저에서 사용을 허용하면 입력 음량에 맞춰 입이 움직인다. 마이크 사용이 막힌 환경에서는 위의 새 창 링크로 열어 볼 수 있다.

**기존 시트** 버튼을 누르면 지난번 그림으로 바뀐다. 같은 방향의 두 그림을 비교하거나, 크기와 배경색을 바꿔 볼 수 있다.

## Flare로 네 장을 그려서 100가지 모습을 만들었다

참조 이미지로는 지난번에 만든 서소영 시트를 골랐다. 새 시트에도 25개 얼굴이 필요했다. 얼굴마다 바라보는 방향을 달리하고, 5행 5열로 배치해 달라고 요청했다. 하늘색 한복과 머리 장식은 유지하고, 각 칸의 머리 크기와 위치가 일정하도록 주문했다. 이렇게 만든 기본 시트를 A로 삼았다.

나머지 세 장은 새로 만든 A를 다시 참조 이미지로 넣어 생성했다. B는 입을 조금 벌리고, C는 입을 크게 벌리고, D는 입을 다문 채 눈을 감게 했다. 표정을 바꿀 때 바라보는 방향까지 달라지면 고개가 갑자기 움직이는 것처럼 보인다. 그래서 네 시트의 같은 칸에 있는 얼굴은 같은 쪽을 보도록 요청했다.

| 시트 | 눈과 입 | 용도 |
|---|---|---|
| A | 눈을 뜨고 입을 다묾 | 기본 모습 |
| B | 눈을 뜨고 입을 조금 벌림 | 작은 음량에 반응 |
| C | 눈을 뜨고 입을 크게 벌림 | 큰 음량에 반응 |
| D | 눈을 감고 입을 다묾 | 눈 깜빡임 |

각 시트는 가로와 세로가 모두 2048픽셀이며, 생성 품질은 `high`로 설정했다. 네 장에 담긴 얼굴은 모두 100개다. 사용자가 시선을 옮기고 표정을 바꿀 때마다 이 중 하나가 화면에 나온다.

![25방향의 치비 서소영을 5행 5열로 배치한 새 기본 시트](https://img.seosoyoung.eiaserinnys.me/images/guruguru-seosoyoung-image-25/A.png)

처음 요청에 `gpt-image-2.5`를 사용하자 API가 모델을 찾을 수 없다는 오류를 반환했다. 공식 문서에서 확인한 모델 ID는 `gpt-image-2.5-flare`였다. 이 이름으로 다시 요청해 네 장을 생성했다. 재현에 필요한 네 번의 요청문은 [프롬프트 파일](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/guruguru-seosoyoung-25/prompts.txt)에 남겼다.

## Sunburst로도 같은 시트를 만들었다

첫 Sunburst 시트에는 Flare와 같은 원본 참조 이미지와 프롬프트를 사용했다. 모델 ID는 `gpt-image-2.5-sunburst`로 지정했으며, 해상도는 2048×2048, 품질은 `high`로 유지했다. A를 먼저 생성하고, B, C, D에는 그 A를 참조 이미지로 넣었다.

처음 만든 두 모델의 그림은 [수정 전 데모](https://pages.eiaserinnys.me/d/guruguru-seosoyoung-25/r/2)에 남겨 두었다. 표정과 바라보는 방향을 그대로 둔 채 **Sunburst**와 **Flare**를 번갈아 선택하면 두 결과를 비교하기 쉽다. 같은 조건으로 여러 번 생성했을 때도 이번과 비슷한 차이가 나는지는 확인하지 않았다.

[Sunburst에 사용한 프롬프트](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/guruguru-seosoyoung-sunburst/prompts.txt)

## 몸을 고정하고 배경을 투명하게 바꿨다

고개를 옆으로 돌려도 가슴의 한복 깃은 정면을 향하게 했다. 기존 Sunburst 그림에서 머리 방향은 유지하고 몸과 어깨를 정면으로 수정했다. 수정본 A를 참조 이미지로 넣어 입 모양 두 장과 눈 깜빡임 한 장도 다시 만들었다.

캐릭터 바깥은 투명하게 처리했으며, 피부에는 옅은 살구색을 채웠다. 생성된 PNG에는 피부와 옷에도 아주 약한 투명도가 남아 있었다. 데모에서는 이 부분을 불투명하게 표시하도록 보정했다. 배경색을 곱하던 효과도 Sunburst에서 껐다. 화면 배경을 바꿔도 피부와 옷의 색은 유지된다.

수정본은 `gpt-image-2.5-sunburst`에 투명 PNG로 요청했으며, 네 장 모두 1024×1024픽셀이다. [수정에 사용한 프롬프트](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/guruguru-seosoyoung-head-only/prompts.txt)도 따로 남겼다.

## 브라우저는 필요한 칸만 보여 준다

화면에 보이는 얼굴은 시트의 한 칸을 확대한 것이다. 데모가 마우스 위치에 따라 행과 열을 고르면, 그 칸의 얼굴이 나타난다. 입을 움직일 때는 A, B, C 시트의 같은 칸을 번갈아 보여 준다. 눈을 깜빡일 때는 잠시 D를 보여 준다. 이미지 생성은 네 장을 그리는 단계에서 끝난다. 이후의 움직임은 브라우저가 준비된 그림을 바꿔 보여 주면서 만든다.

이번 시트의 100개 칸을 점검해 보니, 캐릭터의 짙은 선이 칸 경계에 닿은 곳은 없었다. 그렇다고 표정이 바뀔 때 머리 위치까지 정확히 일치한다고 볼 수는 없다. 정지 그림을 크게 보는 것과 데모 토크를 켜서 표정을 바꿔 보는 것은 서로 다른 확인 과정이다.

이전 글에서 소개한 트마리 원본은 눈 두 상태와 입 세 상태를 25개 방향마다 조합해 총 150장을 썼다. 서소영 데모는 이전 버전부터 네 시트를 사용했으며, 이번에도 그 구성을 따랐다. 따라서 눈을 감은 채 입을 벌린 별도 표정은 포함하지 않는다.

새 모델로 다시 그린 서소영과 기존 그림을 직접 비교할 수 있도록 기록을 남겼다. 데모에서는 선과 표정이 어떻게 달라졌는지 볼 수 있다. 그림을 실제로 움직였을 때의 모습도 함께 확인할 수 있다.

## 출처와 제작 자료

- [이전 제작 기록: トマリぐるぐる / トマリトーク](/digest/tomari-guruguru/)
- [OpenAI의 GPT Image 2.5 Flare 모델 문서](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)
- [OpenAI의 GPT Image 2.5 Sunburst 모델 문서](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)
- [인터랙티브 데모](https://pages.eiaserinnys.me/d/guruguru-seosoyoung-25)
- [이미지 생성에 사용한 프롬프트](https://pub-236dc9dc170e487faec4c8b5e2d084c6.r2.dev/pages/guruguru-seosoyoung-25/prompts.txt)

Flare와 Sunburst로 만든 시트와 이후 수정본, 데모는 이번 작업에서 제작했다. 트마리의 캐릭터 이미지는 사용하지 않았다.
