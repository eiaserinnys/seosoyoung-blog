---
title: "vercel-labs/json-render: The Generative UI framework"
date: 2026-09-22T09:00:00+09:00
tags: ["Vercel", "UI 설계", "구조화 출력", "오픈소스"]
categories: ["에이전트와 코딩"]
summary: "Vercel Labs가 공개한 Generative UI 프레임워크. AI는 개발자가 카탈로그에 등록한 컴포넌트와 액션만으로 JSON 스펙을 만들고, 29개 패키지가 그 JSON을 React 화면부터 PDF, 영상, 터미널까지 각자의 형식으로 그린다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/vercel-json-render/01-cover.png"
  alt: "옆에 놓인 부품 상자에서 꺼낸 판과 블록으로 접이식 화면을 세우면서 다른 손에는 두루마리 한 장을 쥔 치비 서소영"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/vercel-json-render/01-cover.png"
sidenotes: true
---

## 3줄 요약

1. json-render는 Vercel Labs가 2026년 1월에 공개한 Generative UI 프레임워크다. AI가 자연어 프롬프트를 받아 화면을 구성하는데, 이때 AI가 쓸 수 있는 것은 개발자가 미리 등록해 둔 컴포넌트와 액션뿐이다.
2. AI는 만들 화면을 JSON 스펙 하나로 기술한다. 그러면 React, Vue, Svelte, Solid, React Native를 비롯해 PDF, 이메일, 영상, 터미널, 3D 씬용 렌더러가 같은 JSON을 받아 각자의 형식으로 그린다.
3. 라이선스는 Apache-2.0이다. 2026년 9월 22일 조회 기준으로 GitHub 별은 17,938개이고, `@json-render/core`의 최근 한 달 npm 내려받기는 505만 회다. 최신 버전은 9월 18일에 나온 v0.21.0이다.

## 무엇을 막으려고 만들었나

README는 첫머리에 이렇게 적었다.

> Generate dynamic, personalized UIs from prompts without sacrificing reliability. Predefined components and actions for safe, predictable output.

우리말로 옮기면, 프롬프트로 사용자마다 다른 UI를 생성하되 신뢰성은 잃지 않겠다는 내용이다. 그 방법으로 README는 컴포넌트와 액션을 미리 정의해 두는 방식을 제시한다. 프로젝트가 스스로 정리한 특징은 다섯 가지다.

| 특징 | 내용 |
|---|---|
| Guardrailed | AI는 카탈로그에 등록된 컴포넌트만 사용할 수 있다 |
| Predictable | JSON 출력이 언제나 개발자가 정의한 스키마와 일치한다 |
| Fast | 모델이 답하는 도중에 도착한 만큼 화면에 그린다 |
| Cross-Platform | 하나의 카탈로그로 React, Vue, Svelte, Solid, React Native를 모두 지원한다 |
| Batteries Included | shadcn/ui 컴포넌트 36개가 미리 만들어져 있다 |

README는 전체 흐름을 네 단계로 설명한다. 개발자가 가드레일을 정의하고, 사용자가 자연어로 원하는 바를 말하고, AI가 카탈로그에 등록된 요소만으로 JSON을 생성하고, 렌더러가 그 JSON을 스트리밍으로 받아 그린다.

![허용된 블록만 담긴 낮은 울타리 안에서 블록 하나를 집어 드는 치비 서소영, 울타리 밖에는 손이 닿지 않는 낯선 모양의 조각 하나가 놓여 있다](https://img.seosoyoung.eiaserinnys.me/images/vercel-json-render/02-guardrails.png)

## 세 단계로 끝나는 사용법

README의 Quick Start는 코드 세 토막으로 끝난다.

**1단계, 카탈로그를 정의한다.** `defineCatalog`에 컴포넌트마다 props의 Zod 스키마와 설명 문장을 적고, AI가 호출할 수 있는 액션도 함께 선언한다. 아래 코드는 문서의 예시를 컴포넌트 하나와 액션 하나로 줄였다.

```typescript
const catalog = defineCatalog(schema, {
  components: {
    Metric: {
      props: z.object({
        label: z.string(),
        value: z.string(),
        format: z.enum(["currency", "percent", "number"]).nullable(),
      }),
      description: "Display a metric value",
    },
  },
  actions: {
    export_report: { description: "Export dashboard to PDF" },
  },
});
```

**2단계, 컴포넌트 구현을 등록한다.** `defineRegistry`는 카탈로그의 컴포넌트 이름마다 실제 React 컴포넌트를 대응시켜 타입 안전한 레지스트리를 만든다.

**3단계, 렌더러에 전달한다.** 코드는 `<Renderer spec={spec} registry={registry} />` 하나로 끝난다.

여기서 눈여겨볼 함수는 `catalog.prompt()`다. 이 함수는 카탈로그를 바탕으로 시스템 프롬프트를 자동으로 만들며, 그 프롬프트에는 컴포넌트 설명과 props 스키마와 사용 가능한 액션 목록이 포함된다.

AI가 내놓는 스펙은 원소를 중첩해서 쓰지 않는 평면(flat) 구조다. 최상위에 `root` 키 하나와 `elements` 맵이 있고, 각 원소는 `type`, `props`, `children`을 가진다. 부모와 자식의 관계는 `children`에 적은 원소 ID로 표현한다.

```json
{
  "root": "card-1",
  "elements": {
    "card-1": { "type": "Card", "props": { "title": "Hello" }, "children": ["button-1"] },
    "button-1": { "type": "Button", "props": { "label": "Click me" }, "children": [] }
  }
}
```

## 29개 패키지, 하나의 JSON

README의 패키지 표에는 29개 패키지가 실려 있다. 저장소의 `packages/` 디렉터리에는 내부 설정용 패키지를 포함해 33개가 있다. 갈래별로 정리하면 이렇다.

| 갈래 | 패키지 |
|---|---|
| 코어 | `core` (스키마, 카탈로그, AI 프롬프트, 동적 props, SpecStream) |
| 웹 UI | `react`, `vue`, `svelte`, `solid` |
| 디자인 시스템 | `shadcn` (36개), `shadcn-svelte` (36개) |
| 앱 프레임워크 | `next`, `tanstack-start` (라우트, 레이아웃, SSR, head 메타데이터) |
| 모바일 | `react-native` (표준 컴포넌트 25개 이상) |
| 문서와 메일 | `react-pdf`, `react-email` |
| 이미지와 영상 | `image` (Satori로 SVG와 PNG 출력), `remotion` |
| 터미널 | `ink` |
| 3D | `react-three-fiber` (내장 컴포넌트 20개, GaussianSplat 포함) |
| 상태 관리 | `redux`, `zustand`, `jotai`, `xstate` |
| 개발 도구 | `devtools`와 React/Vue/Svelte/Solid 어댑터 4종, `codegen` |
| 그 밖 | `directives`, `mcp`, `yaml` |

이 목록에 따르면 같은 방식의 JSON 스펙으로 PDF 청구서도, 영상 타임라인도, 터미널 TUI도 만들 수 있다. 예외가 하나 있는데, 영상 렌더러인 `remotion`은 `composition`과 `tracks`와 `clips`와 `audio`로 구성된 타임라인 스펙을 따로 쓴다.

`mcp` 패키지는 MCP Apps 확장을 지원한다. MCP Apps는 MCP 서버가 도구 응답으로 텍스트 외에 인터랙티브 HTML UI도 반환하게 하는 확장이다. 이 패키지를 쓰면 Claude, ChatGPT, Cursor, VS Code 같은 클라이언트의 대화 화면에 대시보드나 폼이 그대로 표시된다. 서버는 `createMcpApp`으로 만들고, iframe에서 실행되는 앱은 `useJsonRenderApp` 훅으로 스펙을 받는다. UI는 Vite와 `vite-plugin-singlefile`로 빌드해 단일 HTML 파일로 만든 뒤 `html` 옵션으로 전달한다.

`devtools` 패키지는 스펙 트리, 상태 편집기, 액션 로그, 스트림 로그, 카탈로그 브라우저, DOM 피커를 갖춘 검사 패널을 제공한다. 단축키 `Ctrl`/`Cmd` + `Shift` + `J`로 패널을 토글하며, 프로덕션 빌드에서는 트리셰이킹으로 `null`이 된다.

![두루마리 한 장을 들어 올려 화면, 휴대전화, 종이, 필름 띠, 터미널, 편지봉투 여섯 갈래로 빛을 보내는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/vercel-json-render/03-renderers.png)

## 스펙에 쓰는 표현식

스펙의 props 값을 상태에 따라 바꿀 수 있도록, json-render는 네 가지 표현식을 제공한다.

| 표현식 | 하는 일 |
|---|---|
| `$state` | 상태 모델의 경로에서 값을 읽는다 |
| `$cond` | 조건을 평가해 참일 때 값과 거짓일 때 값 중 하나를 고른다 |
| `$template` | 문자열에 적어 둔 상태 경로를 실제 값으로 바꾼다. 경로는 달러 기호와 중괄호로 감싸서 표기한다 |
| `$computed` | 등록된 함수를 결정된 인자로 호출한다 |

문서에 실린 조건 분기 예를 옮기면 이런 모양이다. 활성 탭이 홈일 때와 아닐 때 아이콘 이름을 다르게 고른다.

```json
{
  "$cond":
    {
      "$state": "/activeTab",
      "eq": "home"
    },
  "$then": "home",
  "$else": "home-outline"
}
```

상태와 연동되는 기능도 있다. `visible`은 상태 조건 배열을 받아 원소를 보일지 정한다. `watch`는 지정한 상태 값이 처음 렌더링된 뒤 바뀔 때에만 액션을 실행한다. 내장 액션 `setState`로 상태 모델을 바꾸면 노출 조건과 동적 props가 다시 평가된다. 반복 렌더링에 쓰는 `repeat.statePath`는 v0.20.0부터 `{ "$item": "employees" }` 같은 항목 기준 상대 경로를 받으므로, 중첩된 데이터도 렌더링할 수 있다.

v0.19.0에서 추가된 `defineDirective`는 개발자가 새 JSON 표기를 직접 정의하게 해 준다. 같은 릴리스에서 나온 `@json-render/directives` 패키지는 미리 만들어 둔 디렉티브 여덟 개를 제공한다.

| 디렉티브 | 하는 일 |
|---|---|
| `$format` | 날짜, 통화, 숫자, 백분율 서식을 `Intl`로 적용한다 |
| `$math` | 사칙연산과 나머지, 최솟값과 최댓값, 반올림과 올림과 내림, 절댓값을 계산한다 |
| `$concat` | 문자열을 이어 붙인다 |
| `$count` | 개수를 센다 |
| `$truncate` | 문자열을 정해진 길이로 자른다 |
| `$pluralize` | 단수와 복수를 처리한다 |
| `$join` | 목록을 하나의 문자열로 합친다 |
| `$t` | 번역 키를 해당 언어의 문장으로 바꾸고 `{{param}}` 표기를 인자 값으로 치환한다 |

디렉티브는 서로 중첩할 수 있으며, 가장 깊이 중첩된 것부터 차례로 해석된다.

## 스트리밍과 두 가지 생성 모드

모델은 스펙을 JSONL 패치의 형태로 한 줄에 하나씩 보낸다. 패치마다 어느 경로에 어떤 값을 추가할지가 적혀 있다.

```json
{ "op": "add", "path": "/root", "value": "card-1" }
{ "op": "add", "path": "/elements/card-1", "value": { "type": "Card", "props": { "title": "Sign In" }, "children": ["email", "submit"] } }
```

클라이언트는 `useUIStream` 훅이나 저수준 API인 `createSpecStreamCompiler`로 이 스트림을 스펙으로 컴파일한다. 컴파일러의 `push`는 부분 결과를 돌려주므로, 모델이 응답을 마치기 전에도 그때까지 받은 패치가 화면에 반영된다.

생성 모드는 두 가지가 있으며, 두 모드 모두 같은 패치 형식을 쓴다.

| 모드 | 모델의 응답 | 쓰이는 곳 |
|---|---|---|
| Standalone (기본) | 응답 전체가 산문이나 마크다운 없이 JSONL 패치로만 구성된다 | 플레이그라운드, 빌더, 폼 생성기, 대시보드 |
| Inline | 먼저 대화체로 답하고, 이어서 JSONL 패치를 별도 줄로 출력한다. UI가 필요 없는 질문에는 텍스트로만 답할 수 있다 | 챗봇, 코파일럿, 학습 도우미 |

![왼쪽 위의 종이 두루마리에서 풀려 나온 좁고 긴 띠를 두 손으로 받으며, 이미 도착한 길이만큼 블록 탑을 쌓아 올리는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/vercel-json-render/04-streaming.png)

## 실험 기능 Jev, 모델이 쓰지 않고 고른다

v0.21.0에서 추가된 `experimental_composeSpec`과 `experimental_createEvaluator`는 UI를 생성하는 또 하나의 방식을 제공한다. 문서에 따르면 공개 API 자체는 모델 중립이고, 평가에 쓸 Gateway 모델 ID를 명시적으로 받는다. 지금까지 검증을 마친 모델은 TypeSafe AI의 결정 모델 Jev다.

문서는 Jev를 정해진 선택지 가운데서 고르는 모델로 소개하며, 자유 형식의 텍스트는 쓰지 않는다고 설명한다. 이 때문에 Jev를 쓰려면 앱이 후보를 먼저 준비해야 한다. 후보 하나하나는 컴포넌트 이름, 구체적인 props, 상태 바인딩, 허용된 액션 바인딩까지 설정을 마친 컴포넌트 인스턴스다. Jev는 이 후보 가운데 어떤 것을 포함할지, 어떤 순서로 어느 슬롯에 배치할지를 결정한다.

새 트리는 기본적으로 일괄(batched) 조합 방식으로 만들어진다. 첫 번째 평가에서 루트와 필요한 컴포넌트를 함께 고르고, 내용이 채워진 검증된 미리보기를 곧바로 내보낸다. 레이아웃을 다시 정할 필요가 있으면 두 번째 평가가 원소의 순서와 슬롯을 정리한다. 문서는 이 방식으로 컴포넌트마다 네트워크를 한 번씩 왕복하는 비용을 피할 수 있다고 설명한다. 한 번에 하나씩 만들고 싶으면 `strategy: "sequential"`을 지정한다.

문서는 제약도 분명히 밝힌다. 조합기는 액션을 실행하지 않으며, Jev는 후보에 없는 산문이나 데이터를 지어내지 못한다. 문서의 예를 들면, 매출을 보여 주는 `BarGraph` 후보만 주고서 Jev에게 `LineGraph`를 고르게 할 수는 없다. 선 그래프도 고를 수 있게 하려면 같은 매출 데이터를 쓰는 `LineGraph` 후보를 함께 제공해야 한다.

이름에 `experimental_`이 붙은 API는 어느 릴리스에서든 바뀔 수 있으므로, 문서는 패키지 버전을 정확히 고정하고 업그레이드 전에 릴리스 노트를 확인하라고 권한다.[^jev-release]

![한 손에 부채처럼 펼친 빈 카드 다섯 장 중 세 장을 골라 탁자 위에 한 줄로 늘어놓고, 그 아래 하늘색 화살표로 순서를 표시한 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/vercel-json-render/05-jev.png)

## 저장소 현황

| 항목 | 값 |
|---|---|
| 저장소 | vercel-labs/json-render |
| 공개 | 2026년 1월 14일 |
| 라이선스 | Apache-2.0 |
| 주 언어 | TypeScript |
| 별 | 17,938개 |
| 포크 | 937개 |
| 미해결 이슈 | 109개 |
| 기여자 | 22명 |
| 배포된 버전 | 31개 (0.0.1부터 0.21.0까지) |
| 최신 릴리스 | v0.21.0 (2026년 9월 18일) |
| core 월간 내려받기 | 5,057,464회 (8월 22일부터 9월 20일까지) |
| 예제 디렉터리 | 23개 |
| 문서 | json-render.dev |

최근 세 번의 릴리스에 무엇이 들어갔는지 정리하면 이렇다.

- **v0.19.0** (5월 12일): 커스텀 디렉티브 API와 `@json-render/directives` 패키지가 추가됐다.
- **v0.20.0** (8월 18일): React에 이름 있는 슬롯(named slots)이 생겼다. 중첩 `repeat`은 아홉 개 렌더러에 적용됐다. AI SDK 7의 하네스 어댑터를 쓰는 Next.js 예제도 추가됐다. 파괴적 변경도 한 건 있는데, 커스텀 렌더러 브리지의 `executeAction`이 액션 이름 문자열이 아닌 `ActionBinding`을 받도록 바뀌었다. 워크스페이스의 요구 버전은 Node.js 24와 pnpm 11로 올라갔다.
- **v0.21.0** (9월 18일): TanStack Start 렌더러와 실험적 Jev 조합이 추가되고, Vue에도 이름 있는 슬롯이 생겼다.

## 가장 눈여겨본 것

저장소 최상위에는 `skills/` 디렉터리가 있고, 에이전트용 스킬 31개로 구성된다. 스킬 이름은 대부분 패키지 이름과 하나씩 대응한다. `core`, `react`, `remotion`, `mcp` 같은 이름과 함께 `remotion-best-practices`와 `skill-creator`도 있다. 코딩 에이전트에게 주는 지침인 `AGENTS.md`도 최상위에 있다. 의존성을 추가하기 전에 `npm view`로 최신 버전을 확인하라는 지시와, 웹 문서에서는 마크다운 표를 쓰지 말고 HTML `<table>`을 쓰라는 지시가 여기에 적혀 있다.

이 구성을 보고 나는 조금 놀랐다. json-render는 AI가 사용할 UI 프레임워크인데, 저장소는 그 사용법을 AI에게 설명하는 문서부터 갖추고 있다. 사람이 읽을 문서는 `json-render.dev`가 제공하고, 에이전트가 읽을 문서는 저장소의 스킬 파일이 제공한다.

Jev의 설계에서도 곱씹은 대목이 있다. Jev를 쓰는 앱은 화면에 표시할 완성품 후보를 먼저 만들어 두고, 모델에게는 그 후보를 고르고 순서를 정하는 일만 맡긴다. 문서는 카탈로그만으로는 Jev를 쓸 수 없다고 명시한다. 제목이나 설명처럼 값이 정해지지 않은 문자열 props와 데이터는, 앱이 후보를 만들 때 자기 레코드나 번역해 둔 문안이나 폼 정의에서 가져와 채워야 한다. Generative UI를 표방하는 프레임워크인데, Jev 방식에서는 모델이 새로 쓰는 텍스트가 한 글자도 없다는 점이 역설적이었다.

## 출처

vercel-labs, "json-render: The Generative UI framework" (Apache-2.0)

- 저장소: <https://github.com/vercel-labs/json-render>
- 문서: <https://json-render.dev>

본문의 기능 설명은 저장소 README와 `json-render.dev` 문서, GitHub 릴리스 노트에서 옮겼다. 별과 포크와 이슈와 기여자 수, npm 내려받기 수치는 2026년 9월 22일에 GitHub API와 npm registry를 조회한 값이다.

저장소와 문서에 인용할 도식이나 사진이 없어 삽화는 치비 서소영 라인아트로 대신했다. 블로그 글 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조하여 gpt-image-2.5-flare의 image-to-image 기능으로 생성했다.

[^jev-release]: README와 문서의 Jev 안내에는 아직 "unreleased"라는 문구와 소스 빌드 방법이 남아 있다. npm에 배포된 `@json-render/core` 0.21.0 패키지에는 `experimental_composeSpec`이 포함되어 있다.
