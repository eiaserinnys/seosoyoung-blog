---
title: "Introducing Agent-Native Beta: The Framework for Agentic Apps"
date: 2026-10-15T22:30:00+09:00
tags: ["AI 에이전트", "AI UX", "MCP", "A2A", "오픈소스"]
categories: ["에이전트와 코딩"]
subjects: ["하네스와 에이전트 설계"]
summary: "Builder.io가 베타로 공개한 오픈소스 타입스크립트 프레임워크 Agent-Native를 정리했다. 에이전트와 앱 화면이 같은 액션과 데이터, 화면 상태를 공유하게 만들어, 사람이 에이전트에게 맡기는 일과 직접 고치는 일을 한 앱에서 번갈아 할 수 있게 한다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/00-cover.png"
  alt: "검은 바탕에 Agent-Native 로고와 “the framework for agentic apps” 문구가 적힌 소개 이미지"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/00-cover.png"
---

## 3줄 요약

1. Builder.io의 스티브 수얼과 비슈와스 고피나트가 2026년 10월 14일 오픈소스 타입스크립트 프레임워크 Agent-Native를 베타로 공개했다. AI 에이전트와 그 에이전트 전용 앱 화면을 함께 만드는 프레임워크다.
2. Agent-Native에서는 에이전트와 UI가 같은 액션(기능), 같은 데이터, 같은 화면 상태를 공유한다. 기능을 한 번 정의하면 UI, 에이전트, HTTP API, 명령줄 도구(CLI), MCP, A2A까지 여섯 가지 방식으로 호출할 수 있고, 어느 방식이든 같은 검증과 권한 규칙을 따른다.
3. 메신저 연동, 에이전트 사이의 작업 위임, 팀 단위의 스킬과 메모리, 인증과 실시간 협업, 모델 교체까지 기본 기능으로 갖췄다. 로컬에서 직접 개발해 원하는 곳에 배포하거나, Builder.io에서 온라인으로 만들면 된다.

## AI 에이전트에게 왜 UI가 필요한가

사람이 하는 일에는 대개 그 일을 돕는 화면이 있다. 발표 자료는 슬라이드 편집기에서 다듬고, 아이디어는 디자인 도구에서 구체화하고, 진행 상황은 대시보드로 확인한다. 이런 화면이 있기에 작업 결과를 눈으로 확인하고 바로 고친다.

AI 에이전트는 일하는 방식을 바꾼다. 원하는 결과를 설명하면, 어떤 단계로 처리할지는 에이전트가 정한다. 그래도 결과를 확인하고, 판단하고, 세부를 손보는 일은 여전히 사람의 몫이다. 저자들은 이렇게 눈으로 보고 손으로 고쳐야 하는 작업은 채팅만으로 하기 어렵다고 했다.

저자들이 든 예는 색 하나를 고치는 일이다. 색 하나를 바꾸려고 프롬프트를 작성하고, 에이전트를 기다리고, 토큰 비용을 내야 한다. 다른 부분이 바뀌지 않았는지도 확인해야 한다. 작은 수정 하나를 하려고 이만한 절차를 거치는 것은 과하다. 사람은 작업에 따라 에이전트에게 맡길 수도, 직접 처리할 수도 있어야 한다. 그래서 Builder.io는 프롬프트로 맡기는 자유와 앱에서 직접 고치는 통제력을 한 앱에서 함께 제공하기로 했다.

![흐릿한 채팅 대화가 길게 이어진 에이전트 대화창 위에 “A chat gives you text… and more text…” 문구가 적힌 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/01-chat-text.jpg)
*소개 영상에 따르면 UI는 협업, 조작, 시각화, 내비게이션을 제공하지만 채팅은 글만 계속 내놓는다. 출처: Builder.io 소개 영상*

## 에이전틱 앱이란 무엇인가

에이전틱 앱(agentic app)은 전용 앱을 갖춘 AI 에이전트를 말한다. 에이전트와 앱은 하나로 동작한다. 기존 앱 옆에 채팅 사이드바를 덧붙인 구성과는 다르다. 에이전트와 UI는 대등하게 협력하며, 사람이 UI로 할 수 있는 일은 에이전트도 전부 할 수 있다.

채팅창 하나로는 얻을 수 없는 이점으로 원문은 세 가지를 꼽았다.

- **무엇을 시킬 수 있는지 분명하다.** UI가 에이전트로 할 수 있는 일을 보여 주므로, 무엇을 요청할지 짐작하지 않아도 된다.
- **필요한 맥락이 이미 있다.** 데이터와 업무 흐름이 앱에 있으므로, 에이전트는 사용자가 지금 하는 작업을 알고 시작한다.
- **결과를 함께 만든다.** 에이전트가 일하는 동안 결과가 UI에 바로 나타난다. 사용자는 에이전트와 동시에 편집을 계속할 수 있다. 원하는 요소를 선택해 에이전트에게 그 부분을 알려 줄 수도 있고, 작업을 다시 에이전트에게 맡겨도 된다.

소개 영상은 이사회 보고용 발표 자료로 이 흐름을 보여 준다. 에이전트가 분기별 매출 차트에 4분기 전망치 550만 달러를 추가하면, 사용자가 이어서 슬라이드 제목을 직접 고쳐 쓴다.

![이사회 보고용 슬라이드에서 사용자가 제목 “On track for”를 직접 입력하고 있고, 아래 차트에는 4분기 전망치 550만 달러가 표시된 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/02-step-in.jpg)
*사용자가 슬라이드 제목을 직접 고쳐 쓰는 장면. 전망치는 에이전트가 먼저 추가했다. 출처: Builder.io 소개 영상*

## Agent-Native는 어떻게 동작하는가

Agent-Native는 에이전트와 UI가 세 가지를 공유하게 만든다.

**액션을 공유하므로 할 수 있는 일이 같다.** 각 기능은 한 번만 정의한다. 에이전트는 그 기능을 도구(tool)로 호출하고, UI는 코드에서 호출한다. 여기서 도구는 AI 모델이 작업 중에 필요할 때 부르는 함수를 말한다. 양쪽 모두 같은 입력 검증과 권한 확인을 거쳐 같은 구현을 실행한다.

**데이터를 공유하므로 작업 내용이 일치한다.** 에이전트가 한 작업은 UI에 나타나고, 사용자가 UI에서 바꾼 내용은 에이전트도 이용할 수 있다.

**화면 상태를 공유하므로 맥락을 안다.** 에이전트는 지금 사용자 화면에 무엇이 표시되어 있는지 안다. 현재 페이지, 선택한 레코드, 열어 둔 뷰 같은 정보다. 이 정보 덕분에 사용자가 “이것”이라고만 말해도 에이전트는 무엇을 말하는지 안다.

영상 속 예시 코드는 슬라이드를 추가하는 액션이다. 설명(`description`), 입력 형식(`schema`), 실행 함수(`run`)로 구성된다.

```ts
export default defineAction({
  description: "Add a slide to a deck",
  schema: z.object({ deckId, content }),
  run: async (args) => slides.add(args),
})
```

![add-slide.ts 파일의 defineAction 코드와 “Add a sli”까지 입력 중인 에이전트 대화창이 선으로 이어진 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/03-define-action.jpg)
*에이전트 대화창의 요청도 UI 버튼과 같은 `add-slide` 액션을 호출한다. 출처: Builder.io 소개 영상*

이렇게 정의한 액션 하나는 UI, 에이전트, HTTP API, 명령줄 도구(CLI), MCP, A2A까지 여섯 가지 방식으로 호출할 수 있다. MCP(Model Context Protocol)는 Claude나 ChatGPT 같은 AI 도구가 외부 프로그램의 기능을 불러 쓸 때 따르는 표준 규약이다. A2A(Agent-to-Agent)는 에이전트끼리 작업을 주고받을 때 쓰는 규약이다.

![가운데 Action 상자가 UI, Agent, HTTP API, MCP, CLI, A2A 여섯 상자와 선으로 연결된 구성도](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/04-action-surfaces.jpg)
*액션 하나를 UI, 에이전트, HTTP API, MCP, CLI, A2A가 함께 쓰는 구성도. 출처: Builder.io 소개 영상*

원문은 이 설계를 컴퓨터 사용(computer use) 에이전트와 비교했다. 컴퓨터 사용 에이전트는 사람처럼 화면을 보며 일한다. 클릭할 곳이나 입력할 내용을 정하고, 실행하고, 결과를 확인하는 과정을 한 단계씩 되풀이한다. 저자들은 컴퓨터 사용 방식이 작동은 하지만 느리고 토큰을 많이 쓴다고 평가했다.

Agent-Native의 에이전트는 화면을 조작하지 않고 UI가 쓰는 액션을 직접 호출한다. 이런 에이전트는 자신이 할 수 있는 일을 정확히 알기 때문에 작업을 더 빨리 끝내고 토큰도 덜 쓴다고 한다.[^1] 화면이 필요 없으므로 슬랙 메시지나 예약된 일정, 다른 에이전트의 요청에 따라 실행할 수도 있다.

## 이미 쓰는 앱과 에이전트 연결하기

Agent-Native의 연결은 양방향이다. 내 에이전트는 팀이 쓰는 앱을 이용하고, 다른 AI 도구와 에이전트는 내 앱을 이용한다.

### 어디서든 에이전트에게 말 걸기

슬랙, 마이크로소프트 팀즈, 디스코드, 이메일, 텔레그램, 왓츠앱에서 메시지를 보내면 앱을 열지 않아도 에이전트가 일을 시작한다. Notion, Linear, GitHub 같은 도구는 MCP나 기본 연동 기능으로 연결한다. 그러면 에이전트가 여러 도구의 정보를 모으고 각 도구에서 작업을 실행한다.

![board-prep 슬랙 채널에서 Vishwas Builder가 @Slides에게 이번 주 수치로 4번 슬라이드를 갱신해 달라고 요청하고, Slides가 작업을 시작했다고 답하는 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/05-slack-tag.jpg)
*슬랙 채널에서 Slides 에이전트에게 이번 주 수치로 4번 슬라이드를 갱신해 달라고 요청하는 장면. 출처: Builder.io 소개 영상*

### A2A로 에이전트끼리 일 맡기기

모든 Agent-Native 앱은 A2A 규약을 지원한다. 한 에이전트가 다른 에이전트에게 작업을 맡기면, 맡은 쪽은 자기 도구와 맥락을 활용해 작업을 처리하고 결과를 돌려준다. 새로 만든 에이전트의 기능은 기존 에이전트들도 A2A로 호출할 수 있다.

영상은 앞의 슬랙 요청이 처리되는 과정을 이어서 보여 준다. 요청을 받은 Slides 에이전트가 A2A로 Analytics 에이전트에게 4분기 매출 전망을 부탁한다. Analytics 에이전트는 자기 앱에서 HubSpot의 영업 파이프라인과 Stripe의 3분기 매출을 바탕으로 전망을 계산한다. Slides 에이전트는 그 결과로 슬라이드를 만든다.

![Analytics 앱의 매출 전망 대시보드 오른쪽 에이전트 패널에 Slides 에이전트가 A2A로 보낸 4분기 매출 전망 요청이 표시된 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/06-a2a-analytics.jpg)
*Slides 에이전트의 A2A 요청을 받은 Analytics 에이전트가 자기 앱에서 매출 전망을 계산하는 장면. 출처: Builder.io 소개 영상*

### Claude, ChatGPT, Cursor에서 내 앱 쓰기

모든 Agent-Native 앱은 MCP 서버이기도 하다. Claude, ChatGPT, Cursor, Codex에 연결하면 이 도구들이 앱의 액션을 직접 호출한다. MCP Apps를 지원하는 도구에서는 앱의 UI가 대화창에 그대로 표시된다.[^2]

## 지침, 스킬, 메모리로 에이전트를 업무에 맞추기

범용 에이전트라도 사용자의 업무를 모르면 제대로 일하지 못한다. Agent-Native로 만든 에이전트에는 지침, 스킬, 메모리, 그리고 참고용 파일을 줄 수 있다.

지침과 스킬은 팀 전체가 공유하고, 개인 취향과 메모리는 사람마다 따로 관리한다. 누군가 공유 스킬을 개선하면 팀원 모두가 그 혜택을 받는다.

전문 작업에는 하위 에이전트(sub-agent)를 추가한다. 하위 에이전트마다 대화 스레드와 지침, 도구가 따로 있다. 정해진 일정에 따라, 또는 특정 사건이 생겼을 때 에이전트가 실행되게 할 수도 있다. 실행 조건은 일상 언어로 적는다. 영상에서는 매주 금요일 오전 9시에 4번 슬라이드를 갱신하라는 문장을 조건으로 입력한다.

![에이전트 패널에 board-deck 스킬로 4번 슬라이드 준비를 요청하자 Northwind 지침 읽기, board-deck 스킬 사용, 메모리 확인, 하위 에이전트 생성, 슬라이드 갱신 단계가 차례로 완료 표시된 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/07-sub-agent.jpg)
*4번 슬라이드 준비를 요청받은 에이전트가 팀 지침과 `board-deck` 스킬, 메모리를 확인하고 내용 검증은 하위 에이전트에게 맡기는 과정. 출처: Builder.io 소개 영상*

## 인증, 협업, UI 도구 모음

Agent-Native는 모든 앱에 필요하지만 직접 만들기는 번거로운 기능을 기본으로 제공한다. 인증, 권한, 조직과 팀 관리, 데이터 저장, 멀티테넌시, 실시간 동기화다. 멀티테넌시는 여러 고객사가 한 서비스를 함께 쓰면서도 각자의 데이터는 서로 분리되는 구조를 말한다.

에이전트가 무엇을 하는지 볼 수 있어야 일을 맡기기도 쉽다. 사용자는 에이전트가 작업하는 과정을 지켜볼 수 있다. 민감한 작업은 실행 전에 승인을 받도록 설정할 수 있고, 내가 바꾼 것인지 팀원이 바꾼 것인지 에이전트가 바꾼 것인지도 언제든 구분된다.

![투자자에게 자료를 공개해 달라는 요청에 에이전트 패널이 “Make this deck public” 확인 카드를 띄우고 “Approved by you”로 승인이 표시된 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/08-approval.jpg)
*에이전트가 “투자자에게 이 자료를 공개해 달라”는 요청을 받고, 공개 범위를 바꾸기 전에 사용자 승인을 받는 장면. 출처: Builder.io 소개 영상*

선택 사항인 [Agent-Native Toolkit](https://www.agent-native.com/docs/agent-native-toolkit)은 앱의 나머지 부분에 쓸 수 있도록 미리 만들어 둔 구성 요소를 제공한다. Builder.io의 예제 앱 Clips, Slides, Design도 같은 구성 요소로 만들었다.

| 분류 | 구성 요소 |
|---|---|
| 편집 | 서식 있는 텍스트 편집기, 캔버스 조작 |
| 협업 | 실시간 접속자 표시, 공유, 댓글 |
| 이력 | 버전 기록, 실행 취소, 복원 |
| 앱 구성 | 설정 화면, 팀, 내비게이션, 외부 서비스 연결 |

## 원하는 AI 모델 쓰기

Anthropic, OpenAI, Google Gemini, OpenRouter의 API 키나 OpenAI 호환 엔드포인트의 키를 직접 넣는 방식을 지원한다. Ollama로 로컬 모델을 실행하거나 Builder.io가 관리하는 AI 연결을 써도 된다. 모델을 바꿔도 액션, 데이터, UI는 그대로이므로 앱을 고칠 필요가 없다.

기존 ChatGPT 구독으로 Codex 모델을 쓰는 방법도 실험 기능(Labs)으로 제공한다.

![프롬프트 입력창의 모델 선택 메뉴에 Claude Opus 5.5, Sol 6.1, Builder.io Gateway, DeepSeek V4 Pro, Kimi K2.5, Qwen3 Coder가 나열된 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/09-model-picker.jpg)
*모델 선택 메뉴. Claude Opus 5.5, Sol 6.1, Builder.io Gateway, DeepSeek V4 Pro, Kimi K2.5, Qwen3 Coder 등이 목록에 있다. 출처: Builder.io 소개 영상*

## 로컬에서 만들거나 온라인에서 만들기

코드를 자기 환경에 두고 싶다면 로컬에서 시작한다. 코딩 에이전트에게 만들게 해도 되고 코드를 직접 고쳐도 된다.

```bash
npx @agent-native/core@latest create my-app
```

코드는 사용자의 저장소에 있다.[^3] Neon이나 Supabase 같은 PostgreSQL 데이터베이스를 연결하고 Node, Vercel, Netlify, Cloudflare, AWS 중 원하는 곳에 배포한다. 이미 React 앱이 있다면 처음부터 다시 만들지 않고 에이전트 패널만 추가해도 된다.

로컬 설정 없이 Builder.io에서 온라인으로 만들 수도 있다. 원하는 것을 설명하고, AI로 손보고, 팀과 공유하는 방식이다.

## Agent-Native로 만든 예제 앱

Builder.io는 Agent-Native로 만든 에이전틱 앱 세 개를 함께 공개했다.

- **[Clips](https://clips.agent-native.com/)**: 화면을 녹화해 에이전트와 공유한다. 링크 하나로 녹화 속 말소리를 받아 적은 글과 시점별 화면 이미지를 전달하므로, 에이전트가 버그 보고, 피드백, 사용법 시연을 확인하고 바로 작업한다.
- **[Slides](https://slides.agent-native.com/)**: 에이전트에게 발표 자료를 만들게 한 뒤 슬라이드를 직접 편집한다. 슬라이드를 하나 선택하면 에이전트가 어느 슬라이드를 말하는지 안다.
- **[Design](https://design.agent-native.com/)**: 에이전트와 함께 디자인을 만들고, 직접 조작해 볼 수 있는 시제품도 만든다. 결과물은 시각적 조작 도구로 손보거나 다시 에이전트에게 맡긴다.

세 앱 모두 오픈소스여서 그대로 쓰거나, 만든 방식을 살펴보거나, 하나를 골라 자기 앱의 출발점으로 삼을 수 있다. 원문은 마지막으로 잘 아는 업무 하나를 골라 에이전트를 직접 만들어 보라고 권한다. 그 에이전트에는 사람이 작업을 지켜보고, 고치고, 지시할 수 있는 UI가 함께 있어야 한다고 덧붙인다.

![“The Q4 plan” 슬라이드의 글머리 목록에 Agent 표시가 붙어 있고, 오른쪽 에이전트 패널에 “Fix the layout overflow” 요청과 “Rewrote 5 bullets to fit” 완료 기록이 표시된 장면](https://img.seosoyoung.eiaserinnys.me/images/agent-native-beta/10-app-asks-agent.jpg)
*Slides 앱이 직접 에이전트에게 일을 시키는 장면. 글머리 목록이 슬라이드보다 180픽셀 길어지자 앱이 레이아웃 수정을 요청하고, 에이전트는 항목 다섯 개를 다시 써서 분량을 맞춘다. 출처: Builder.io 소개 영상*

## 가장 흥미로운 지점

색 하나를 고치는 예는 읽자마자 수긍이 갔다. 같은 일을 에이전트에게 맡기면 앞에서 본 절차를 모두 거쳐야 하지만, 마우스로 고치면 몇 초면 끝난다.

Agent-Native는 사람과 에이전트가 같은 액션을 호출하게 하는 방식으로 이 문제를 해결한다. 화면과 API가 같은 업무 로직을 쓰게 하는 설계는 웹 개발에서 오래 써 온 원칙이다. Agent-Native는 에이전트를 그 로직을 호출하는 또 하나의 사용자로 취급한다. 컴퓨터 사용 방식은 사람이 쓰던 화면을 에이전트가 그대로 조작하게 한다. 반면 Agent-Native는 처음부터 앱의 기능을 에이전트도 호출할 수 있게 설계한다.

화면 상태를 공유한다는 설계도 눈여겨볼 만하다. 채팅으로 무언가를 고치려면 고칠 대상을 말로 설명해야 한다. 예를 들어 “세 번째 슬라이드 오른쪽 차트의 점선”이라고 적어야 한다. 사용자가 무엇을 선택했는지 에이전트가 알면 “이것”이라는 한 마디로 충분하다.

대신 앱의 에이전트는 개발자가 미리 정의한 액션만 호출한다. 덕분에 에이전트의 행동을 미리 예측할 수 있고 권한이 없는 작업을 막기도 쉽다. 하지만 목록에 없는 일을 시키면 에이전트는 수행하지 못한다. 내가 고른다면, 자주 반복하는 업무는 이런 앱으로 만들고 처음 해 보는 탐색 작업은 범용 에이전트에게 맡길 것이다.

## 출처

- 저자: Steve Sewell, Vishwas Gopinath (Builder.io)
- 발행일: 2026년 10월 14일
- 원문: <https://www.builder.io/blog/introducing-agent-native>
- 소개 영상: <https://www.youtube.com/watch?v=6t_AMjY5gJc>
- 본문 이미지는 원문에 실린 소개 영상의 장면을 캡처한 것이다.

[^1]: 원문은 속도와 토큰 절감 폭을 수치로 제시하지 않았다.
[^2]: MCP Apps는 MCP의 확장 규격이다. MCP 서버가 도구 실행 결과와 함께 대화형 화면을 돌려주면, 이를 지원하는 AI 도구가 그 화면을 대화창에 그려 준다.
[^3]: 프레임워크 코드는 GitHub의 [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) 저장소에 공개되어 있다. 저장소는 2026년 3월 12일에 만들어졌고, 10월 15일 기준 GitHub 스타는 7,295개다.
