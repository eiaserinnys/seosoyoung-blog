---
title: "GPUIX — Node.js & React bindings for Zed GPUI"
date: 2026-08-26T06:30:00+09:00
tags: ["React", "Rust", "렌더링", "UI 설계", "오픈소스"]
categories: ["에이전트와 코딩"]
summary: "Zed의 GPU 가속 UI 프레임워크 GPUI를 React로 감싼 바인딩. React 리컨사일러의 뮤테이션을 JSON 직렬화 없이 Rust로 그대로 넘겨, Electron이나 웹뷰 없이 데스크톱 앱을 GPU에 직접 그린다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/gpuix-zed-gpui-react-bindings/chat-app.png"
  alt: "GPUIX로 만든 Waku 스타일 채팅 앱"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/gpuix-zed-gpui-react-bindings/chat-app.png"
---

## 3줄 요약

1. GPUIX는 Zed 에디터의 GPU 가속 UI 프레임워크 **GPUI**를 Node.js와 React에서 쓰도록 감싼 바인딩이다. `remorses`가 2026년 1월 말 공개했고 Apache-2.0, 별 1,100개를 넘겼다.
2. React 리컨사일러가 만든 DOM 형태의 뮤테이션(`createElement`, `appendChild`, `setStyle`…)을 JSON 트리 직렬화 없이 Rust로 직접 넘기고, Rust가 유지하는 보존 트리를 GPUI가 매 프레임 읽어 Metal·DirectX·Vulkan으로 그린다. Electron도 웹뷰도 없다.
3. 문법 강조 코드 블록, 유니파이드 diff, GFM 마크다운이 전부 네이티브 요소로 들어 있고, 가상 리스트·네이티브 텍스트 입력·IME·헤드리스 Select/Combobox/Tooltip·Playwright식 자동화 API까지 갖췄다. 캔버스 요소와 다중 창은 아직 없다.

## 무엇을 만든 프로젝트인가

GPUI는 Zed 에디터가 자기 UI를 그리려고 만든 Rust 프레임워크다. Zed가 빠른 이유의 상당 부분이 여기 있고, 그동안 이 프레임워크를 쓰려면 앱 전체를 Rust로 써야 했다.

GPUIX는 그 진입 장벽을 React로 낮춘다. 화면은 `<div>`와 `<text>`로 짜고 상태는 `useState`로 들되, 그 결과가 브라우저 엔진을 거치지 않고 GPU로 바로 간다.

```tsx
import React, { useState } from 'react'
import { render } from '@gpuix/react'

function App() {
  const [count, setCount] = useState(0)
  return (
    <div style={{ display: 'flex', gap: 8, padding: 16 }}>
      <div
        style={{ backgroundColor: '#3b82f6', borderRadius: 8, padding: 12 }}
        onClick={() => setCount(c => c + 1)}
      >
        <div style={{ color: '#ffffff' }}>Count: {count}</div>
      </div>
    </div>
  )
}

render(<App />, { title: 'My App', width: 800, height: 600 })
```

패키지는 둘로 나뉜다.

| 패키지 | 담당 |
|---|---|
| `@gpuix/native` | GPUI에 붙는 Rust 바인딩. napi-rs 데스크톱 바이너리와 wasm-bindgen 브라우저 빌드를 함께 낸다 |
| `@gpuix/react` | React 리컨사일러, 이벤트 레지스트리, 타입 정의 |

Rust나 Bun을 깔지 않고도 볼 수 있게, GitHub 릴리스에 채팅 예제의 단독 실행 바이너리를 올려 두었다. 파일명은 `example-chat-<target>` 형태다.

## 아키텍처

GPUIX는 React를 GPUI에 **뮤테이션 기반 프로토콜**로 잇는다. 트리 전체를 JSON으로 말아 넘기는 대신, React 리컨사일러가 계산한 개별 변경만 Rust로 건넨다.

```
React (JavaScript)
        │ napi 데스크톱 / wasm-bindgen 브라우저
        │ createElement(1, "div") / appendChild(0, 1)
        │ setStyle(1, "{...}") / commitMutations()
        ▼
Rust 호스트 브리지
  RetainedTree ── 요소·스타일·이벤트 플래그 보존
        │  매 GPUI 프레임
        ▼
  GpuixView::render() → build_element() → GPUI 요소
        ▼
GPUI: Metal / DirectX / Vulkan / 브라우저 WebGPU·WebGL2
      Taffy 플렉스박스 레이아웃
```

JS와 Rust 사이의 호스트 표면은 `NativeRenderer` 인터페이스 하나다.

```ts
interface NativeRenderer {
  createElement(id: number, elementType: string): void
  destroyElement(id: number): Array<number>
  appendChild(parentId: number, childId: number): void
  removeChild(parentId: number, childId: number): void
  insertBefore(parentId: number, childId: number, beforeId: number): void
  setStyle(id: number, styleJson: string): void
  setText(id: number, content: string): void
  setEventListener(id: number, eventType: string, hasHandler: boolean): void
  setRoot(id: number): void
  commitMutations(): void
}
```

### 즉시 모드와 보존 트리가 만나는 자리

GPUI는 **즉시 모드**라 매 프레임 요소 트리를 통째로 다시 짓는다. 리액트의 보존 모델과 정면으로 어긋나 보이는 성질인데, GPUIX는 이걸 거스르지 않고 그대로 쓴다.

1. React 리컨사일러가 상태 변화를 감지해 호스트 뮤테이션을 부른다.
2. 각 뮤테이션이 Rust 쪽 `RetainedTree`를 갱신한다. 스타일·자식·이벤트 플래그를 담은 노드 해시맵이다.
3. GPUI 프레임마다 `GpuixView::render()`가 그 보존 트리를 훑어 `build_element()`로 일회성 GPUI 요소를 만든다.
4. GPUI가 Taffy 플렉스박스로 배치하고 GPU에 그린다.
5. FFI 경계를 넘는 것은 **변경된 요소뿐**이다.

요소 ID는 JS 쪽 증가 카운터가 매기는 평범한 숫자다. React가 동시성 렌더 모드에서 작업을 버릴 수 있으므로, GPUIX는 새 호스트 노드를 커밋 시점까지 JS에 붙들어 둔다. React가 받아들인 서브트리를 배치한 뒤에야 그 뮤테이션이 배치에 합류하고, `commitMutations()`가 그 커밋을 흘려보내면서 Rust 뷰를 다음 프레임 대상으로 표시한다.

### 이벤트는 반대 방향으로

데스크톱에서 이벤트는 `ThreadsafeFunction` 콜백을 타고 GPUI에서 React로 돌아온다.

```
id=3 요소 클릭
   → GPUI가 on_click 발화
   → Rust 클로저가 emit_event_full(callback, 3, "click", {x, y, ...})
   → ThreadsafeFunction이 Node.js 이벤트 루프에 EventPayload를 넣음
   → JS 레지스트리: eventHandlers.get(3)?.get("click")?.(payload)
   → React 핸들러 실행 → 상태 갱신 → 뮤테이션이 다시 Rust로
```

핸들러 자체는 `(elementId, eventType)`을 키로 하는 JS 레지스트리에 산다. Rust는 `setEventListener`로 **리스너가 있는지 없는지만** 알고 클로저는 모른다.

지원하는 이벤트는 클릭·마우스 다운/업/이동/진입/이탈, 바깥 클릭(`onMouseDownOutside`), 키 다운/업, 포커스/블러, 스크롤, 그리고 요소별 전용 이벤트다. `<diff>`는 `onToggleFile`·`onShowMore`·`onLineClick`을, `<markdown>`은 `onLinkClick`을 낸다.

## 네이티브 텍스트 컴포넌트

세 요소가 Rust에서 계산한 Syntect 문법 강조로 텍스트를 그린다. 색은 `theme` 프롭에서 오므로, 강조 결과가 늦게 도착해도 레이아웃을 건드리지 않고 색만 다시 입힌다.

![문법 강조 코드 블록](https://img.seosoyoung.eiaserinnys.me/images/gpuix-zed-gpui-react-bindings/code.png)

- **`<code>`** — 문법 강조 코드 블록. 한 줄이 정확한 행 높이의 한 행이라, 강조가 끝나기 전에 블록 높이가 정해진다.
- **`<diff>`** — 유니파이드 diff 뷰어. 기본값은 부모를 따라 흐르는 것이라 부모 목록 하나만 스크롤러가 되면 된다. 파일을 접으면 행을 숨기는 대신 없애므로, 접힌 1만 줄짜리 파일이 한 행 값이다. `wordDiff`로 바뀐 토큰만 강조할 수 있다.
- **`<markdown>`** — GitHub 스타일 마크다운. 제목·목록·표·인용·펜스 코드·취소선·작업 목록·자동 링크를 처리한다.

![단어 단위 강조가 들어간 유니파이드 diff](https://img.seosoyoung.eiaserinnys.me/images/gpuix-zed-gpui-react-bindings/diff.png)

번들된 언어는 Rust, TypeScript, TSX, JavaScript, JSX, Python, Go, JSON, Bash, TOML, YAML, Markdown, HTML, CSS, C 열다섯 가지다.

### 레이아웃 수치도 테마에 있다

세 컴포넌트가 같은 `theme` 프롭을 받는다. 각 필드는 기본 다크 테마 위에 겹쳐지므로 토큰 하나만 덮어써도 나머지는 그대로다. 여기서 눈여겨볼 것은 색뿐 아니라 **행 높이·거터 너비·패딩·제목 크기 같은 레이아웃 수치가 `metrics`로 함께 노출된다**는 점이다. 디자인을 손보는 일이 Rust 상수 수정이 아니라 React 리렌더로 끝난다.

```tsx
<diff
  patch={patch}
  theme={{
    metrics: {
      diffLineHeight: 26,
      diffGutterWidth: 48,
      mdHeadingSizes: [24, 19, 16, 14],
    },
  }}
/>
```

![metrics만 키워 다시 튜닝한 같은 컴포넌트들](https://img.seosoyoung.eiaserinnys.me/images/gpuix-zed-gpui-react-bindings/metrics.png)

### 선택은 페인트 순서로 복원한다

GPUIX가 그리는 모든 텍스트는 선택하고 복사할 수 있다. `<code>`, `<diff>`, `<markdown>` 내부 텍스트도 포함이고, 제목에서 시작해 펜스 코드 블록 안에서 끝나는 드래그가 그 사이를 전부 잡는다. 빼려면 `userSelect: "none"`을 준다. CSS 속성처럼 상속된다.

![마크다운 블록을 가로질러 선택된 텍스트](https://img.seosoyoung.eiaserinnys.me/images/gpuix-zed-gpui-react-bindings/selection.png)

Zed의 마크다운이 연속 선택되는 이유는 문서 전체가 하나의 텍스트 모델 위 단일 요소이기 때문이다. GPUIX는 텍스트 요소의 트리를 그리므로, 그 연속성을 페인트 시점에 다시 만든다. 각 텍스트 요소가 페인트 순서(곧 문서 순서)로 프레임별 레지스트리에 자기를 등록하고, 드래그는 그 레지스트리에 대고 요소별 스팬으로 풀린다. 이 방식은 같은 문제를 겪은 [Comet](https://github.com/zeronsh/comet)(MIT)에서 옮겨 왔다.

## 긴 목록과 스크롤

![채팅 턴 안에 들어간 diff와 마크다운 표](https://img.seosoyoung.eiaserinnys.me/images/gpuix-zed-gpui-react-bindings/chat-diff.png)

`overflow: "scroll"`을 준 컨테이너는 네이티브 스크롤 대상이 된다. 스크롤 물리, 클리핑, 오프셋 유지를 GPUI가 알아서 맡는다.

**중첩 스크롤은 지원하지 않는다.** 부모 하나만 스크롤할 수 있고 안쪽 `overflow: "scroll"`·`<virtual-list>`·`<diff>`는 그러면 안 된다. GPUI가 두 히트박스에 같은 휠 이벤트를 주기 때문에 안쪽 목록이 제스처를 가로챈다. 긴 내용은 자식에게 별도 뷰포트를 주지 말고, 미리보기와 더 보기 버튼을 쓰는 펼침 컴포넌트로 접어 두라는 것이 권장 패턴이다. 가로는 예외라 넓은 자식에 `overflowX: "scroll"`을 줘도 세로 휠을 뺏지 않는다.

컬렉션이 길어지면 `<virtual-list>`를 쓴다. React와 Rust는 모든 행을 그대로 들고 있고, GPUI만 뷰포트 근처 행을 짓고 배치하고 칠한다.

```tsx
<virtual-list
  alignment="bottom"
  followTail
  estimatedItemHeight={180}
  style={{ flexGrow: 1, minHeight: 0 }}
>
  {messages.map((message) => (
    <Message key={message.id} message={message} />
  ))}
</virtual-list>
```

| 프롭 | 기본값 | 용도 |
|---|---:|---|
| `alignment` | `"top"` | 채팅식 초기 위치는 `"bottom"` |
| `followTail` | `false` | 사용자가 떠나기 전까지 새 행을 따라감 |
| `overdraw` | `512` | 뷰포트 밖에 미리 짓는 픽셀 |
| `estimatedItemHeight` | 없음 | 아직 재지 않은 행의 초기 높이 추정 |

GPUI는 행이 뷰포트에 들어올 때 높이를 잰다. 추정값은 실측이 도착하면 자동으로 교체된다. 보존 트리의 자손이 바뀌면 GPUIX가 그 직계 행만 다시 재도록 표시하고, 키가 그대로인 행의 측정치는 추가·삭제·재정렬 후에도 살아남는다.

작업량은 이렇게 갈린다.

| 작업 | 일반 스크롤 컨테이너 | `<virtual-list>` 자식 | `VirtualList` + `itemCount` |
|---|---|---|---|
| React 파이버 노드 | 전 행 | 전 행 | 보이는 구간 |
| Rust 보존 노드 | 전 행 | 전 행 | 보이는 구간 |
| GPUI 행 생성 | 전 행 | 보이는 행 + 오버드로 | 보이는 행 + 오버드로 |
| 레이아웃·페인트 | 전 행 | 보이는 행 + 오버드로 | 보이는 행 + 오버드로 |

1만 행짜리 `turns.map`은 여전히 React 자식을 전부 만든다. 긴 대화록에는 `itemCount`와 `renderItem`을 받는 `VirtualList`를 써서 마운트 시점부터 보이는 구간만 만들라고 권한다. 수백만 행이면 애플리케이션 수준 페이징이나 데이터를 직접 소유하는 네이티브 요소가 필요하다.

## 입력과 포커스

`<input>`과 `<textarea>`는 GPUI의 플랫폼 입력 핸들러를 쓴다. 네이티브 캐럿, 텍스트 선택, IME 조합, 클립보드, 실행 취소·재실행, 자소 단위로 안전한 삭제, 마우스 위치 지정이 전부 들어 있다. 편집기가 먼저 네이티브에서 갱신되고 그다음 완성된 값을 React에 알린다. 같은 값을 계속 넘긴다고 해서 브라우저의 제어 입력처럼 편집이 거부되지는 않는다.

포커스는 **GPUI의 개념**이다. GPUIX는 안정적인 React 요소 ID를 영속 `gpui::FocusHandle`에 이어 붙여, React가 다시 렌더해도 포커스가 살아남게 한다. `Tab`은 GPUI의 `window.focus_next()`를, `Shift+Tab`은 `focus_prev()`를 부른다. 이 이동은 Rust 안에서 끝나고 JavaScript를 왕복하지 않는다.

내장 컨트롤은 고정된 컴포넌트 라이브러리가 아니라 **스타일 없는 프리미티브**다. shadcn이 Radix 프리미티브를 쓰는 방식 그대로, 네임스페이스를 들여와 로컬 파일에서 감싸고 꾸민 뒤 앱 전체에서 그 로컬 컴포넌트를 쓰라고 안내한다.

| 임포트 | 주요 파트 |
|---|---|
| `@gpuix/react/select` | `Root`, `Trigger`, `Value`, `Content`, `Item` |
| `@gpuix/react/combobox` | `Root`, `Input`, `Content`, `List`, `Item`, `Empty` |
| `@gpuix/react/tooltip` | `Provider`, `Root`, `Trigger`, `Content` |

## 애니메이션은 Rust가 계산한다

`motion.div`에 시작 스타일과 목표 스타일을 준다. React는 목표를 **한 번** 보내고, 그다음부터는 Rust가 중간값을 계산하며 전환이 끝날 때까지 GPUI 프레임을 요청한다. 프레임마다 React 렌더도 N-API 호출도 일어나지 않는다.

```tsx
<motion.div
  initial={{ width: 0, opacity: 0 }}
  animate={{ width: 320, opacity: 1 }}
  transition={{ duration: 0.25, ease: 'easeOut' }}
  style={{ overflow: 'hidden' }}
>
  <text style={{ color: '#ffffff' }}>Welcome</text>
</motion.div>
```

받는 목표는 아직 숫자 값뿐이다. `width`·`height`, `top`·`right`·`bottom`·`left`, `opacity`, `borderRadius`. 전환 옵션은 Motion for React와 같은 초 단위로 `duration`(기본 0.3), `delay`(기본 0), `ease`(기본 `easeOut`, 큐빅 베지어 배열도 가능)를 받는다. 스프링, 키프레임, 배리언트, 종료 전환, 공유 레이아웃 애니메이션은 아직 없다.

모션이 도는 중에 목표가 바뀌면 다음 전환이 현재 보이는 값에서 출발한다. 되돌리는 애니메이션이 튀지 않는다.

## 개발 루프

핫 리로드는 JS 쪽만 된다. 엔트리 파일 끝에 `render()`를 두고 `bun --hot`으로 띄우면, 저장할 때마다 같은 창 위에서 React 트리만 다시 마운트된다. 창, GPU 디바이스, 네이티브 `.node` 애드온, GPUI의 스크롤 물리는 그대로 남고 `useState`·포커스·이벤트 핸들러는 초기화된다.

이건 리마운트이지 React Refresh가 아니다. 훅 상태를 지키려면 Bun이 `--hot` 중에 <code>&#36;RefreshReg&#36;</code> 변환을 주입해야 하는데, 그 변환은 현재 `bun build --react-fast-refresh`에만 있다([oven-sh/bun#40179](https://github.com/oven-sh/bun/issues/40179)에서 추적 중).

네이티브 절반은 핫 리로드가 **원리적으로 불가능하다**는 설명을 문서에 그대로 적어 두었다. `.node` 파일의 `require()`는 `process.dlopen`을 부르는데 Node에는 짝이 되는 언로드가 없고, GPUI의 플랫폼·GPU 디바이스·열린 창·UI 스레드·선택 레지스트리 같은 살아 있는 상태가 로드된 라이브러리 안에 있다. 두 번째 로드는 첫 번째가 남아 있는 채로 독립된 네이티브 상태를 하나 더 만든다.

대신 재빌드가 문제가 되지 않을 만큼 빠르다는 실측을 내놓는다. M 시리즈 맥에서 파일 하나를 고친 뒤 기준이다.

| 단계 | 시간 |
|---|---:|
| `cargo check --lib` | 1.5s |
| `cargo build --lib` | 4.9s |
| `bun run build:debug` (napi) | 약 2s |
| vitest 스크린샷 파일 하나 | 약 2s |

`bun run dev`가 이걸 루프로 엮는다. `packages/native/src`를 감시하고 다시 빌드한 뒤 스크린샷 테스트를 재렌더한다. **Rust 편집에서 새 PNG까지 약 4초.** 라이브 창과 달리 PNG는 에이전트도 읽을 수 있다는 이유로, 문서는 스크린샷 모드를 기본값으로 권한다.

### 플랫폼별 루프

macOS에서는 `startFrameLoop`가 기본 약 125fps로 `renderer.tick()`을 부른다. 프로세스 메인 스레드의 AppKit을 Node를 막지 않고 펌프한다. Windows와 Linux에서는 GPUI가 전용 Rust UI 스레드 하나에서 평소의 블로킹 네이티브 이벤트 루프를 돌고, `startFrameLoop`는 아무 일도 하지 않는 핸들을 돌려준다. Windows 런타임 검증은 아직 진행 중이라고 밝힌다.

경고 하나가 굵게 붙어 있다. macOS에서 `tick()`을 `setImmediate` 루프로 돌리면 초당 수만 번 회전하면서, **완전히 유휴 상태인 앱이 CPU 73%를 먹는다.** 속도를 맞춰 부르면 1%다.

### 프레임 오버레이

GPUI가 레이아웃 뒤에 프레임 시간 통계를 창에 직접 칠한다. React FPS 라벨은 매 프레임 갱신되면서 일을 더 만들 테니 React 요소로 두지 않았다.

```tsx
render(<App />, { title: 'My App', debugFrameOverlay: 'full' })
```

`minimal`은 마지막 그리기 시간만, `full`은 `CUR`·`1%`·`10%`·`MAX`·`FRAMES`를 보여준다. 이 숫자는 FPS가 아니라 **그리기 시간**이라 `8.3 MS`가 대략 120Hz다. `p90Ms`가 오버레이의 10% 줄, `p99Ms`가 1% 줄이고 그게 느린 꼬리다.

## 자동화와 테스트

요소에 `testId`를 달면 Playwright처럼 몰 수 있다. 같은 클라이언트가 vitest 안에서도, 브라우저 페이지 안에서도, 자식 프로세스를 상대로도 동작한다.

```ts
const { render, renderer } = createTestRoot()
render(<ChatApp />)
const app = await connectTest(renderer)

await app.clock.pause()
await app.getByTestId('sidebar-collapse').click()
await app.clock.fastForward(200)
await app.screenshot({ path: 'collapsed.png' })

await app.getByTestId('composer').fill('hello gpuix')
await app.getByTestId('send').click()
```

로케이터는 `getByTestId`, `getByText`, `getByType`을 제공하고 로케이터 안에서 다시 좁힐 수 있다. `click()`은 마지막으로 칠해진 경계의 중심을 때리고, `waitFor()`는 매치가 정확히 하나가 될 때까지 폴링한다.

주목할 만한 것은 **시계 제어**다. `app.clock.pause()`·`set(ms)`·`fastForward(ms)`가 네이티브 모션 시간을 얼려서, 사이드바 애니메이션의 특정 타임스탬프를 정확히 캡처할 수 있다. 타이머 슬립 없이 CI가 매번 같은 프레임을 얻는다.

```ts
const startedAt = await app.clock.pause()
await app.getByTestId('sidebar-collapse').click()
await app.captureFrames('review/sidebar', [startedAt, startedAt + 100, startedAt + 200])
```

라이브 앱은 `launch({ command, args })`로 띄운다. 같은 명령을 stdin에 SSE `data:` 줄로 보내는데, stdin이 **파이프**일 때만 앱이 듣는다. 평범한 터미널 실행은 영향을 받지 않고, `data:` 접두사가 없는 줄은 무시되므로 `console.log`가 메시지를 깨뜨리지 못한다.

테스트 렌더러(`TestGpuixRenderer`)는 **GPU로 실제 그린다**. 창이 화면 밖에 놓일 뿐 Metal이 온전히 렌더하고, 프로덕션과 같은 `GpuixView`·`build_element()`·`apply_styles()`·이벤트 핸들러를 돌린다. 이벤트 시뮬레이션도 합성 JS 이벤트가 아니라 GPUI의 좌표 기반 히트 테스트와 디스패치를 통과한다.

`getAllText()`는 보존 트리의 `<text>` 노드만 보므로, 텍스트를 GPUI 안에서 칠하는 `<code>`·`<diff>`·`<markdown>`은 마지막 프레임에 칠해진 문자열을 페인트 순서로 돌려주는 `getPaintedText()`로 확인한다.

성능 회귀 테스트도 하나 들어 있다. `examples/chat.perf.test.tsx`가 마운트, 휠 그리기, 사이드바 클릭 시간을 재고 매 프레임이 아니라 p95를 검사한다. macOS에서 `THROTTLE=utility`를 주면 프로세스를 `taskpolicy -c utility` 아래 다시 띄워 작업을 효율 코어에 묶는다. Chrome의 6배 스로틀이 아니라 **M1/M2 에어 CPU 대역의 대리 지표**이고, GPU와 램은 빠른 상태로 남는다.

## 브라우저 타깃

같은 Rust 렌더러가 wasm-bindgen으로 브라우저에도 올라간다. 웹 예제는 데스크톱 채팅 예제와 같은 React 앱과 리컨사일러를 번들해, 기존 보존 트리와 `GpuixView`를 GPUI의 브라우저 플랫폼 위에서 돌린다.

두 가지 제약이 붙는다. 브라우저 이벤트 콜백은 아직 연결되지 않았고, 생성된 Wasm이 공유 메모리를 쓰므로 프로덕션 서버가 페이지·JavaScript·Wasm 응답 모두에 `Cross-Origin-Opener-Policy: same-origin`과 `Cross-Origin-Embedder-Policy: require-corp`를 실어야 한다. 빌드에는 나이틀리 Rust와 버전이 맞는 wasm-bindgen CLI(0.2.127)가 필요하다.

브라우저에서는 자동화 `App`이 `globalThis.gpuix`로 항상 설치되어 있어서, Playwright의 `page.evaluate` 안에서 곧바로 로케이터와 시계를 쓸 수 있다.

## 아직 없는 것

README의 상태 목록에서 체크가 비어 있는 항목은 넷이다.

- 캔버스 요소
- 다중 창
- `bun --hot` 중의 React Refresh (Bun 런타임 변환이 필요)
- 네이티브 `.node` 애드온의 핫 리로드 (원리적으로 불가능, `bun run dev`가 재빌드·재시작으로 대체)

여기에 브라우저 이벤트 콜백 미연결, Windows 런타임 검증 진행 중, 모션의 스프링·키프레임·배리언트 부재가 더해진다.

![마크다운, 코드, 가상화된 diff가 한 프레임에](https://img.seosoyoung.eiaserinnys.me/images/gpuix-zed-gpui-react-bindings/showcase.png)

## 가장 눈여겨본 것

내가 가장 오래 머문 대목은 성능 표가 아니라 **네이티브 핫 리로드를 못 한다고 적어 둔 자리**였다.

보통 이런 문서는 미구현을 로드맵 항목으로 미뤄 둔다. GPUIX는 그러지 않고 왜 불가능한지를 먼저 설명한다. `process.dlopen`에 짝이 되는 언로드가 없고, 살아 있는 네이티브 상태가 라이브러리 안에 있으니 두 번째 로드는 독립된 상태를 하나 더 만들 뿐이라고. 그리고 곧바로 그 제약을 우회하는 대신 **감당 가능하게 만드는 쪽**으로 넘어간다. cargo check 1.5초, 빌드 4.9초, Rust 편집에서 새 스크린샷 PNG까지 4초.

`theme.metrics`도 같은 태도의 다른 얼굴이다. 행 높이와 제목 크기를 Rust 상수로 두면 디자인을 만질 때마다 재빌드가 걸린다. 그래서 그 수치를 아예 프롭으로 끌어올려 튜닝을 React 리렌더로 만들었다. 재빌드를 없애는 대신 재빌드가 필요한 표면을 줄인 것이다.

스크린샷 모드를 기본 개발 루프로 권하는 이유도 한 줄 붙어 있다. 라이브 창과 달리 PNG는 에이전트가 읽을 수 있어서다. 2026년의 프레임워크 문서가 사람 개발자와 코딩 에이전트를 같은 문단에서 독자로 셈하는 장면이었다.

## 출처

`remorses`, GPUIX — Node.js & React bindings for Zed GPUI. Apache-2.0.
2026-01-29 첫 공개, 2026-08-25 기준 별 1,133개·포크 32개.
원문: <https://github.com/remorses/gpuix>

본문 이미지는 모두 저장소 `docshttps://img.seosoyoung.eiaserinnys.me/images/`의 공개 스크린샷이다.
