---
title: "Reimagining the mouse pointer for the AI era"
date: 2026-05-13T07:00:00+09:00
tags: ["AI UX", "HCI", "Gemini", "Google DeepMind"]
categories: ["다이제스트"]
summary: "Google DeepMind가 50년 된 마우스 포인터를 Gemini로 증강하는 실험을 공개했다. 정밀한 프롬프트 대신 가리키기와 자연스러운 단축 어휘로 의도를 전달하는 네 가지 인터랙션 원칙을 제시한다."
ShowToc: true
TocOpen: false
sidenotes: true
---

![DeepMind AI 마우스 포인터 컨셉 — 3개의 커서가 음성 명령 'Move this', 'Merge those', 'Add that'와 함께 표시된 인터페이스 mockup](/images/deepmind-ai-pointer/cover.png)

## 3줄 요약

1. Google DeepMind가 2026년 5월 12일 블로그 *"Reimagining the mouse pointer for the AI era"* 를 공개했다. 저자는 Adrien Baranes와 Rob Marchant.
2. 핵심 진단은 이렇다 — 마우스 포인터는 반세기 동안 *어디를* 가리키는지만 추적했고, 일반적인 AI 도구는 자신의 창 안에 갇혀 사용자에게 "AI 우회로"를 강요해 왔다. Gemini로 증강된 포인터는 *무엇을* 가리키는지까지 이해해 그 우회로를 없앤다.
3. DeepMind는 네 가지 인터랙션 원칙(Maintain the flow, Show and tell, This/That의 힘, 픽셀→엔티티)을 제시하고, 이를 Gemini in Chrome과 신규 Googlebook의 Magic Pointer, Google Labs Disco에 점차 통합한다고 밝혔다.

## 출발점 — 반세기 동안 거의 변하지 않은 인터페이스

DeepMind는 글 서두에서 마우스 포인터가 모든 웹사이트·문서·워크플로우의 항구적 동반자였음에도, 그 형태와 능력이 50년 넘게 거의 진화하지 않았다는 점을 짚는다. 그동안 등장한 AI 도구는 대개 *자체 창 안*에 머물러 있다. 사용자는 자기 작업 맥락을 그 창 안으로 끌어다 붙여야 한다 — 드래그하고, 복사하고, 붙여 넣고, 다시 설명한다.

DeepMind는 그 방향을 뒤집겠다고 말한다. AI가 사용자의 *모든 도구로 찾아오는* 형태다.

> 우리는 사용자가 사용하는 모든 도구에서 흐름을 끊지 않고 만나는 직관적인 AI를 원한다. 예를 들어 어떤 건물 사진을 가리키며 "길 안내해줘"라고 요청한다고 상상해 보자. AI가 이미 맥락을 알고 있다면 그 이상 아무것도 더 필요하지 않다.

이 비전을 구현한 실험 시스템이 Google AI Studio의 [이미지 편집](https://aistudio.google.com/apps/bundled/ai-pointer-create?showPreview=true&showAssistant=true&fullscreenApplet=true) 데모와 [지도 위에서 장소 찾기](https://aistudio.google.com/apps/bundled/ai-pointer-find?showPreview=true&showAssistant=true&fullscreenApplet=true) 데모로 공개되어 있다.

![DeepMind의 AI-enabled pointer 실험 환경 — 본문의 비디오 스틸](/images/deepmind-ai-pointer/fig1.png)

## 네 가지 인터랙션 원칙

DeepMind는 텍스트 중심 프롬프트의 부담을 *컴퓨터 쪽으로 옮기는* 네 가지 원칙을 정리한다.

### 1. Maintain the flow — 흐름을 끊지 마라

AI 기능은 모든 앱에서 작동해야 하며, 사용자를 별도의 "AI 우회로"로 끌고 가서는 안 된다. 데모로 제시된 사례는 다음과 같다.

- PDF를 가리켜 "이메일에 붙일 수 있도록 불릿 요약을 만들어줘"
- 표 위에 호버해 "이걸 파이 차트로 보여줘"
- 레시피를 하이라이트하고 "재료를 두 배로 늘려줘"

세 시나리오의 공통점은 *별도의 앱으로 옮겨가지 않는다*는 점이다. AI가 사용자가 머무는 자리에 합류한다.

### 2. Show and tell — 정밀한 프롬프트 대신 시각적 맥락

> 현재 AI 모델은 정밀한 지시를 요구한다. 좋은 응답을 얻으려면 상세한 프롬프트를 써야 한다.

DeepMind의 AI-enabled pointer는 그 부담을 덜어준다. 커서 주변의 시각적·의미적 맥락을 매끄럽게 캡처해, 컴퓨터가 사용자에게 *무엇이 중요한지* 보고 이해하게 만든다. 단어 하나, 문단 하나, 이미지의 특정 부분, 코드 블록 — 가리키는 행위 자체가 가장 정확한 프롬프트가 된다.

### 3. "This"와 "That"의 힘 — 직시와 단축 어휘

사람은 일상에서 긴 문단으로 말하지 않는다. "이거 고쳐", "저거 여기로 옮겨", "이게 무슨 뜻이야?" — 신체적 제스처와 공유된 맥락이 빈틈을 메운다. 맥락·가리키기·말을 결합해 이해하는 AI는 사용자가 *자연스러운 단축 어휘*로 복잡한 요청을 표현하게 만든다. 까다로운 프롬프팅이 필요하지 않다.

### 4. 픽셀을 행동 가능한 엔티티로

수십 년 동안 컴퓨터는 사용자가 *어디를* 가리키는지만 추적해 왔다. 이제 AI는 *무엇을* 가리키는지까지 이해해, 픽셀을 장소·날짜·객체 같은 구조화된 엔티티로 변환한다. 즉시 상호작용 가능한 형태로 — 손글씨 메모 사진이 인터랙티브 to-do 리스트가 되고, 여행 영상의 일시정지 프레임이 그 식당의 예약 링크가 된다.

블로그 본문의 표현 그대로 옮기면 이렇다.

> 인간의 행동에 적응하는 기술을 만드는 일 — 사용자가 기술에 적응하도록 강요하는 대신 — 은 AI와의 협업이 진정으로 직관적이고 유려하며 매끄럽게 느껴지는 미래를 가능하게 한다.

## 제품 통합 — Chrome, Googlebook, Disco

DeepMind는 이 원칙들을 다음 제품 표면에 통합한다고 밝혔다.

- **Gemini in Chrome**: 복잡한 프롬프트 대신 포인터로 웹페이지의 관심 부분을 가리켜 질문할 수 있다. 페이지 위 상품 몇 개를 선택해 비교를 요청하거나, 거실 사진에서 새 소파를 시각화하고 싶은 지점을 가리키는 식이다.
- **Googlebook의 Magic Pointer**: 곧 출시 예정. 사용자가 손끝에서 Gemini를 다룰 수 있도록 한다.
- **Google Labs의 [Disco](https://labs.google/disco)**: 향후 컨셉의 테스트베드.

## 가장 흥미로운 지점

내가 가장 인상 깊게 본 대목은 *"AI 우회로"* 라는 진단이다. 도구가 사용자에게 와야 하는데 그동안은 사용자가 도구로 가야 했다는 표현은, 지금 쓰이는 거의 모든 챗봇형 AI 도구의 근본 마찰을 한 문장으로 잘 잡아낸다. 별도 탭을 열고, 컨텍스트를 복사하고, 결과를 다시 원래 자리로 돌려 붙이는 일상의 의례는 의외로 인지 부담이 크다.

포인터를 통한 직시(deixis)는 그 우회로를 줄이려는 가장 자연스러운 후보로 보인다. 일상 대화에서 사람은 이미 "이거", "저거"로 의도를 절반쯤 압축한다. 키보드와 텍스트라는 단일 채널이 그 압축을 풀어내도록 강제했을 뿐이다.

다만 본문은 *제안*에 가깝다. 실제 시스템이 다양한 도메인에서 얼마나 정확하게 의도를 잡아내는지, 음성 인식 오류와 컨텍스트 오해석이 누적될 때 어떤 폴백을 두는지는 데모 너머에서 검증해 봐야 알 수 있다. 데모가 가장 잘 작동하는 사례만 모아 보여주는 것은 어느 회사나 마찬가지이고, 일상의 거친 사용 패턴에서도 같은 매끄러움이 유지될지가 진짜 관건이다.

## 출처

Google DeepMind Research Blog, 2026-05-12. *"Reimagining the mouse pointer for the AI era."* Adrien Baranes & Rob Marchant.

원문: <https://deepmind.google/blog/ai-pointer/>

소개 타래(트위터): <https://x.com/googledeepmind/status/2054246119635300451>
