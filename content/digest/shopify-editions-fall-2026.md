---
title: "Shopify Editions Fall '26"
date: 2026-10-29T11:00:00+09:00
tags: ["HTML-in-Canvas", "WebGPU", "셰이더", "프론트엔드"]
categories: ["게임"]
subjects: ["그래픽스와 렌더링"]
summary: "Shopify가 반년마다 내는 업데이트 특설 사이트의 Fall '26판. 평소에는 분야별 색면과 노드 그래프로 150여 건의 업데이트를 정리한 페이지인데, 숨은 Expo Mode를 켜면 Chrome 오리진 트라이얼 기능 HTML-in-Canvas로 페이지 전체를 WebGPU 텍스처에 옮겨 3D 바닥으로 눕히고, 그 위에서 공을 굴리는 게임까지 돌린다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/00-cover-hero-graph.png"
  alt: "Shopify Editions Fall '26 첫 화면. 왼쪽에 세로로 세운 큰 글자 Exponential과 분야 목록, 수치 카드 세 장이 있고, 오른쪽 넓은 남색 영역에 11개 분야 허브에서 업데이트 점과 썸네일이 선으로 뻗어 나간 노드 그래프가 있다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/00-cover-hero-graph.png"
---

## 3줄 요약

1. Shopify Editions는 Shopify가 1년에 두 번 그동안의 기능 업데이트를 모아 소개하는 특설 사이트이고, 이번 Fall '26판의 주제는 「Exponential」이다. 11개 분야, 150여 건의 업데이트를 분야별 색면과 노드 그래프로 정리했다. 일본 개발자 이케다 야스노부(@clockmaker)는 이 사이트를 HTML-in-Canvas의 선진 사례로 소개했다.
2. 숨은 Expo Mode를 켜면 페이지 전체가 뒤로 누워 검은 3D 공간의 바닥이 된다. 글과 버튼은 여전히 실제 HTML이고, Chrome이 시험 중인 API가 페이지 모습이 바뀔 때마다 그 HTML을 WebGPU 텍스처로 복사한다. 페이지를 코스로 삼아 공을 굴리는 게임도 들어 있다.
3. Shopify는 실험 단계 API를 운영 사이트에 쓰면서 안전장치를 여러 가지 마련했다. 지원 여부를 엄격하게 판정해, 조건이 맞지 않는 브라우저에는 버튼조차 그리지 않는다. 켠 뒤에 실패하면 평소 페이지로 되돌리고, Chrome 버전마다 달라진 API 이름과 인자 형식도 모두 처리한다.

## 어떤 사이트인가

이번 판의 주소는 shopify.com/editions/fall2026이고, 반년 치 기능 업데이트를 한 페이지에 모았다. 페이지 설명에는 「150+ updates」라고 적혀 있다. 업데이트는 Agentic, Sidekick, Online, Merchandising, Retail, Payments, Operations, Shop, Marketing, Fulfillment, Developer의 11개 분야로 분류돼 있다. Sidekick은 Shopify 관리 화면에 내장된 AI 비서의 이름이다.

@clockmaker가 이 사이트를 소개한 트윗의 본문은 다음과 같다.

> Shopify의 특설 사이트, 이번에도 굉장하다! HTML-in-Canvas의 선진 사례. Chrome 오리진 트라이얼 단계에서 실서비스에 도입한 것도 멋지다.[^tweet]

HTML-in-Canvas는 실제 HTML 요소를 `<canvas>` 안에 그림처럼 그려 넣는 웹 API다. 지금까지는 캔버스에 글이나 버튼을 표시하려면 글자와 모양을 직접 다시 그려야 했다. 그렇게 그린 글은 선택할 수도, 검색할 수도, 화면 낭독기로 읽을 수도 없었다. 브라우저가 렌더링한 HTML 화면이 캔버스나 3D 텍스처 위에 그대로 그려진다. 화면에는 그림으로 나오지만 원래 요소도 문서에 남아 있어서, 화면 낭독기가 읽을 수 있고 클릭과 키 입력도 받는다. 아직 정식 기능이 아니어서 Chrome은 오리진 트라이얼로만 제공한다. 오리진 트라이얼은 정식 출시 전의 기능을 시험하는 Chrome의 토큰 제도다. Chrome은 신청한 사이트에만 토큰을 발급하고, 기능은 그 사이트에서만 켜 볼 수 있다. 사이트가 응답 헤더로 토큰을 보내면, 그 사이트를 여는 일반 사용자의 Chrome에서도 기능이 켜진다.

![치비 서소영이 웹 페이지가 그려진 종이를 이젤 위 빈 액자에 밀어 넣고 있다. 액자 안에는 같은 페이지가 그림처럼 걸려 있는데, 서소영이 그 그림 속 작은 버튼을 손가락으로 누르자 버튼이 하늘색으로 빛난다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/chibi-01-html-into-canvas.png)

## 평소 화면의 디자인

첫 화면 왼쪽에는 「Exponential」이 화면 높이만 한 글자로 세로로 서 있고, 그 옆 좁은 열에 11개 분야 목록과 수치 카드 세 장이 쌓인다. 카드 문구는 「1B+ products in our catalog can get discovered across AI channels」, 「400M+ shoppers with Shop Pay accounts」, 「Shopify Payments prevents 12K+ high-risk payments each minute」다. 나머지 넓은 영역은 짙은 남색 바탕의 노드 그래프다. 분야마다 허브 점이 있고, 거기서 뻗은 선 끝에 업데이트 하나하나가 점이나 작은 화면 썸네일로 달려 있다. 분야 이름 옆의 작은 숫자(Developer 57, Payments 30 등)는 아마 그 분야의 업데이트 수일 것이다.

스크롤을 내리면 분야가 바뀔 때마다 화면 전체의 바탕색이 바뀐다. Agentic과 Retail은 진한 파랑, Sidekick은 보라, Online은 자홍, Payments는 초록이다. 분야가 시작되면 그 이름이 화면 폭의 절반쯤 되는 큰 글자로 나오고, 배경에는 첫 화면 그래프 중 그 분야에 해당하는 부분이 가는 흰 선으로 그려진다. 왼쪽에는 분야 목록이 고정돼 있고, 지금 읽는 분야의 점이 채워진다.

![Online 분야가 시작되는 화면. 자홍 바탕 왼쪽 아래에 큰 흰 글자 Online이 있고, 화면 가운데 허브 점에서 가는 흰 선들이 업데이트 점과 작은 썸네일로 뻗어 있다. 왼쪽에는 분야 목록이 고정돼 있다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/02-online-title-graph.png)
*Online 분야의 첫 화면. 분야 이름과 그 분야의 그래프가 바탕에 깔린다. 1440×900 데스크톱에서 직접 캡처.*

업데이트마다 반투명한 사각 카드가 하나씩 있다. 카드에는 위에서부터 작은 사각 표식, 제목, 두세 줄의 설명, 「Read help doc」이나 「Copy prompt」 같은 검은 알약 모양 버튼이 차례로 놓인다. 그 아래에는 제품 화면 목업이나 3D 소품 렌더가 붙는다. 큰 카드 오른쪽에는 「Notes」라는 좁은 상자가 따로 있고, [1], [2] 같은 번호를 붙여 주석을 단다. 카드 문장과 이 상자 사이에 가는 선이 그어져 있어서, 어느 문장에 단 각주인지 눈으로 따라갈 수 있다.

![Agentic 분야의 Shop skill 카드. 파란 반투명 카드 위쪽에 제목과 설명, Copy prompt 버튼이 있고, 가운데에 휴대폰 목업, 주변에 물병, 모카 포트, 셔츠, 시계 같은 3D 소품 렌더가 흩어져 있다. 오른쪽 끝에 Notes 상자가 선으로 이어져 있다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/01-agentic-shop-skill.png)
*Agentic 분야의 「Shop skill for any agent」 카드. 오른쪽 끝 Notes 상자로 선이 이어진다.*

사이트는 글꼴 세 가지를 쓴다. 큰 제목과 카드 제목은 PP Neue Montreal, 분야 목록, Notes, 버튼 글자는 고정폭 Söhne Mono, 일부 본문은 Shopify Inter다. 일본어 판을 위해 PP Neue Montreal과 Söhne Mono의 대체 글꼴로 Noto Sans JP를 지정해 두었다. 스크롤은 Lenis 라이브러리로 부드럽게 처리한다. 몇몇 카드의 그림은 Rive 애니메이션이고, 웹 워커에서 실행된다.

![Retail 분야의 카드. 파란 바탕에 아이소메트릭 일러스트로 그린 매장 계산대와 태블릿 POS, 손님과 직원이 있고, 오른쪽에 Notes 상자가 있다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/03-retail-isometric-notes.png)
*Retail 분야. 제품 화면을 아이소메트릭 일러스트 속에 넣었다.*

![Payments 분야의 초록 바탕 화면. 흰 카드에 고위험 결제 차단액 3,060.50달러와 날짜별 막대그래프가 있고, 아래에 업데이트 설명이 네 열로 놓여 있다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/04-payments-chart.png)
*Payments 분야. 분야마다 화면 전체의 바탕색이 바뀐다.*

## Expo Mode: 페이지가 바닥이 된다

페이지를 열면 브라우저 개발자 콘솔에 이런 안내가 나온다.

> There's more to this page than meets the eye. Press Shift + \~ to switch on Growth Mode.

키보드에서 Shift와 물결표 키를 함께 누르거나, 주소 뒤에 `?expo-mode`를 붙이거나, 화면 왼쪽 아래의 「Expo Mode」 버튼을 누르면 모드가 켜진다.[^names] Esc를 누르거나 같은 버튼을 다시 누르면 꺼진다.

켜는 순간 평평하던 페이지가 뒤로 눕는다. 화면은 검은 공간이 되고, 페이지는 그 바닥에 깔린 긴 띠가 되어 멀리까지 이어진다. 분야마다 띠의 색이 바뀌고, 분야 제목은 두께가 있는 흰 3D 글자로 띠 위에 선다. 카드는 두께 있는 판으로, 휴대폰 목업은 기울어진 입체 기기로 바뀐다. 띠 양옆에는 흰 선으로 그린 건물과 소품이 서 있고, 7500, 8000, 8500 같은 숫자가 눈금처럼 놓인다. 나는 이 숫자를 페이지 맨 위에서 잰 픽셀 거리로 추정한다. 카드 제목 일부는 띠 바깥 여백에 따로 적히고 가는 선으로 원래 카드와 이어진다.

![Expo Mode의 화면. 검은 공간 바닥에 보라색 Sidekick 구간과 자홍색 Online 구간이 띠처럼 멀리 이어지고, 띠 위에 두께가 있는 흰 3D 글자 Online이 서 있다. 오른쪽 여백에 카드 제목 Your whole store edited in one view가 따로 적혀 있고, 양옆에 7500, 8000 같은 숫자 눈금과 선화 건물이 있다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/05-expo-online-road.jpg)
*Expo Mode의 Sidekick(보라)과 Online(자홍) 구간. 출처: @clockmaker 트윗의 화면 녹화.[^video]*

스크롤하면 카메라가 띠를 따라 앞으로 나아간다. 띠 위의 글은 브라우저가 지금 렌더링한 HTML을 복사한 그림이고, 원래 요소는 문서에 그대로 남는다. 코드는 텍스트 선택이 바뀌거나 포커스, 입력 이벤트가 오면 텍스처를 다시 복사한다. 덕분에 페이지가 기울어진 상태에서도 글을 드래그해 선택하거나 버튼을 누를 수 있다.

![Expo Mode의 Retail 구간. 파란 띠 위에 태블릿 POS 화면 카드 두 장이 두께 있는 판으로 서 있고, 카드 아래에 z(t), y(t) 같은 치수 표기가 있다. 띠 양옆에 흰 선으로 그린 건물과 16000, 16500 같은 숫자 눈금이 있다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/06-expo-retail-city.jpg)
*Retail 구간. 양옆의 선화 건물과 카드 아래의 치수 표기. 출처: @clockmaker 트윗의 화면 녹화.*

### 페이지를 코스로 쓰는 게임

Expo Mode에는 게임이 하나 들어 있다. 아래는 화면 문구와 코드로 확인한 내용이고, 직접 끝까지 해 보지는 못했다.

| 항목 | 내용 |
|---|---|
| 조작 | ← →(A D)로 방향, ↑(W)나 위로 스크롤하면 가속, ↓(S)나 아래로 스크롤하면 감속, 스페이스로 점프 |
| 목표 | 공을 굴려 페이지 끝까지 간다. 남은 거리는 「↑ 1234 px to the finish」처럼 픽셀로 표시한다 |
| 점수 | 지나가며 주운 노드와 단어만큼 공이 커지고, 「노드 수 + 단어 수」로 합산해 A++부터 등급을 매긴다 |
| 장애물 | 빠지면 끝나는 구멍, 속도를 올려 띄우는 점프대, 옆으로 미는 구간, 마지막 점프 |
| 물리 값 | 순항 속도 700px/s, 최저 350px/s, 최고 1500px/s, 중력 6500px/s² |

거리, 속도, 구멍 크기 단위가 모두 픽셀이다. 페이지의 픽셀 좌표가 게임 세계의 좌표 노릇을 하고, 페이지의 단어가 주울 수 있는 물건이 된다.

## 구현: HTML을 텍스처로 옮기는 과정

### 기반

응답 헤더에는 `powered-by: Shopify, Oxygen`이 있다. Oxygen은 Shopify가 직접 운영하는 호스팅 플랫폼이다. 프런트엔드 코드는 `clientEntry()`로 등록한 컴포넌트만 브라우저에서 활성화한다. 코드에는 `X-Remix-Frame`이라는 요청 헤더와, 이름이 `rmx`로 시작하는 속성도 들어 있다. Shopify가 인수한 Remix 팀은 React 없이 새 런타임을 만들고 있고, 나는 이 프런트엔드를 그 Remix 계열 런타임으로 판단한다. 공식 발표나 제작기는 찾지 못했다.[^remix]

### HTML-in-Canvas의 기본 동작

Chrome 개발자 블로그에 따르면 기본 사용법은 세 단계로 이루어진다.

1. `<canvas>`에 전용 속성을 단다(이름은 Chrome 버전마다 다르다). 그러면 브라우저는 캔버스의 자식 요소를 화면에 직접 그리지 않고 레이아웃만 계산해 둔다. 자식 요소는 접근성 트리에는 남는다.
2. 자식 요소의 모습이 바뀔 때마다 캔버스에 `paint` 이벤트가 온다. 이 이벤트는 `requestPaint()`로 직접 요청할 수도 있다.
3. 이벤트 처리기에서 요소의 지금 모습을 캔버스나 텍스처에 옮긴다. 2D 캔버스는 `drawElementImage()`, WebGL은 `texElementImage2D()`, WebGPU는 `copyElementImageToTexture()`를 쓴다.

트라이얼 기간에도 API는 계속 바뀌었다. 이름과 인자 형식은 Chrome 150에서 한 번, 155에서 또 한 번 달라졌다. 사이트 코드에는 150\~154용 호출과 155 이후용 호출이 둘 다 들어 있다.

| 바뀐 것 | Chrome 150\~154 | Chrome 155부터 | 이 사이트의 대응 |
|---|---|---|---|
| 캔버스 속성 | `layoutsubtree` | `content="drawable"` | 두 속성을 모두 단다 |
| WebGPU 복사 함수 | `copyElementImageToTexture(원본, 대상)` | `drawElementImageToTexture()`, 인자 이름도 바뀜 | 있는 함수를 찾아 그 형식의 인자로 부른다 |
| 요소 좌표 맞추기 | 개발자가 `style.transform`을 직접 고친다 | `updateElementGeometry()`로 브라우저에 알린다 | 시험 이동으로 동작 여부를 확인해 고른다 |
| WebGL 함수 인자 | 149까지는 6개, 150부터 3개 | 함수 이름이 `texElementSubImage2D`로 바뀜 | 6개짜리 옛 형식은 지원 판정에서 제외한다 |

Shopify는 응답 헤더 `origin-trial`로 토큰을 보낸다. 토큰 뒷부분을 base64로 풀면 아래 내용이 나온다.

```json
{"origin":"https://shopify.com:443","feature":"HTMLInCanvas","expiry":1803945600,"isSubdomain":true}
```

만료 시각 1803945600은 유닉스 시간 값이고, 날짜로 바꾸면 2027년 3월 2일 0시(UTC)다. 이 토큰은 하위 도메인까지 포함하므로 www.shopify.com에서도 유효하다.

### 지원 판정과 실패 처리

사이트는 아래 네 조건을 모두 만족할 때만 Expo Mode 버튼을 그린다. 압축된 코드를 읽기 좋게 풀었다.

```js
"requestPaint" in HTMLCanvasElement.prototype &&
WebGL2RenderingContext.prototype.texElementImage2D?.length !== 6 &&
"gpu" in navigator &&
("drawElementImageToTexture" in GPUQueue.prototype ||
 "copyElementImageToTexture" in GPUQueue.prototype)
```

두 번째 조건은 Chrome 150 이전의 옛 인자 형식(인자 6개)을 제외한다. 네 조건을 통과하지 못하는 브라우저, 곧 Safari와 Firefox, 오리진 트라이얼 이전의 Chrome을 쓰는 사람은 이 모드가 있는지도 모른 채 평소 페이지를 본다.

켠 뒤에 실패해도 페이지는 망가지지 않는다. 이 글을 쓰며 서버의 헤드리스 Chrome 153으로 열어 보니 실제로 실패 처리가 실행됐다. 상태 값이 entering에서 failed로 바뀌었고, 평소 페이지는 그대로 남았다. 상황별 처리는 이렇다.

| 상황 | 처리 |
|---|---|
| WebGPU 장치를 못 받음, 파이프라인 생성 오류, 장치 유실 | 렌더러를 정리하고 HTML을 원래 문서로 돌려놓는다. 버튼은 사라지고 화면 낭독기용 상태 문구가 「Expo Mode unavailable」로 바뀐다 |
| 인쇄 | 인쇄 직전에(`beforeprint`) 캔버스를 제거해 원래 HTML로 인쇄하고, 끝나면(`afterprint`) 다시 켠다 |
| 운영체제의 동작 줄이기 설정 | 기울어지는 전환을 건너뛰고 바로 마지막 장면으로 간다 |
| 입력창, 대화 상자, 메뉴, 팝오버에서 누른 키 | 단축키로 처리하지 않는다 |
| 다른 페이지로 이동 | 모드를 끈다 |

### 페이지를 띠로 만드는 과정

1. **슬롯으로 옮기기.** 모드가 켜지면 페이지 본문을 감싼 요소의 섀도 루트(shadow root)에 새 `<canvas>`를 만들고, 본문은 슬롯을 통해 이 캔버스의 자식 요소로 배치한다.
2. **렌더 패스 준비.** 패스 이름은 전부 `inception-`으로 시작하고, page(페이지 띠), city(양옆 선화 건물), titles(3D 제목), product(입체 제품), grid(바닥 격자), shadow(그림자 맵), pick(포인터 판정) 같은 패스가 있다. 화면은 Display P3 색 공간과 4배 다중 샘플링을 쓴다.
3. **기울이기.** 카메라는 바로 위에서 내려다보는 -90도에서 출발해 -30.2도까지 800ms 동안 기운다. 이 각도에서 본 3D 장면은 평소 페이지와 모습이 같다. 버튼을 누른 직후의 첫 프레임이 평소 화면과 같아지도록 이 각도에서 출발한 것으로 짐작한다. 전환의 진행도는 Web Animations API로 만든 애니메이션 하나에서 읽는데, 이 애니메이션에는 대상 요소가 없고 진행도 값을 내는 데만 쓰인다. 모드를 끌 때는 재생 속도를 -1로 바꿔 같은 애니메이션을 거꾸로 재생한다. 켜고 끄는 전환에는 View Transitions API도 함께 쓴다.

![치비 서소영이 웹 페이지가 그려진 긴 두루마리를 바닥에 펼치며 웃고 있다. 두루마리는 길처럼 멀리 이어지고, 그 위에 하늘색 두꺼운 판들이 서 있으며, 양옆에는 선으로 그린 건물들이 늘어서 있다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/chibi-02-page-to-road.png)

4. **텍스처 복사.** `paint` 이벤트가 오면 화면 근처의 행만 텍스처로 복사한다. 텍스처의 높이는 보이는 화면과 그 아래 네 화면, 곧 화면 높이의 다섯 배까지다. 스크롤하는 동안은 1배 해상도로 복사하다가, 스크롤이 멈추고 150ms가 지나면 1.25배로 다시 복사한다. 기울기 진행도가 0.2 미만이라 페이지가 거의 평평할 때는 2배로 복사한다.
5. **변경 추적.** 텍스처를 다시 복사할지는 코드가 따로 판단한다. 우선 MutationObserver로 DOM 변경을 감시하고, 이벤트도 받는다. 받는 이벤트는 애니메이션과 트랜지션의 시작과 끝, 포인터, 포커스, 입력, 이미지 로드 같은 17종이고, 여기에 텍스트 선택 변경과 글꼴 로딩 완료가 더해진다. 실행 중인 CSS 애니메이션이 있는지도 확인한다. 아무 변화가 없으면 1초 동안 재복사를 건너뛴다.
6. **굽히기와 칠하기.** 정점 셰이더가 평평한 페이지 메시를 휘게 하고, 조각 셰이더가 페이지 텍스처를 읽는다. HTML이 투명한 부분은 그 행이 속한 분야의 색으로 채우고, 분야가 바뀌는 행에서는 두 색을 섞지 않고 바로 바꾼다. 3D 글자와 카드의 그림자는 주광원(키 라이트)을 기준으로 만든 그림자 맵으로 계산해 바닥에 드리운다.

### 3D 제목 글자

분야 제목의 3D 글자는 HTML을 복사하지 않고 따로 그린다. PP Neue Montreal, Söhne Mono, Noto Sans JP의 글리프 윤곽은 JSON 파일로 미리 받아 둔다. 조각 셰이더는 이 윤곽으로 픽셀마다 「이 픽셀의 몇 퍼센트를 글자가 덮는지」를 직접 계산한다. 셰이더 주석에 따르면 글자마다 자기 세로 중심선을 기준으로 돌 수 있고, 바닥에 누운 워드마크는 눌렸다가 튀어 오른다. 옆면은 회색, 뒷면은 앞면과 같은 흰색이어서 글자가 한 바퀴 돌 때도 비어 보이는 순간이 없다.

![Expo Mode의 Shop 구간. 보라색 띠 위에 두께가 있는 흰 3D 글자 Shop이 서 있고, 아래쪽 카드 설명 두 단락이 연보라색으로 선택돼 있으며 그 위에 텍스트 커서가 있다. 오른쪽 여백에 카드 제목 Carts in Shop sync to online store가 따로 적혀 있다.](https://img.seosoyoung.eiaserinnys.me/images/shopify-editions-fall-2026/07-expo-shop-title-selection.jpg)
*Shop 구간의 3D 제목. 아래쪽 연보라 부분은 기울어진 페이지 위에서 마우스로 끌어 선택한 글이다. 출처: @clockmaker 트윗의 화면 녹화.*

### 클릭 대상 맞추기

화면의 페이지는 3D로 누웠지만 실제 HTML 요소는 원래 레이아웃 좌표에 있다. 둘을 맞추지 않으면 눈에 보이는 버튼을 눌러도 엉뚱한 요소가 눌린다. 사이트는 두 단계로 맞춘다.

- **pick 패스.** 같은 장면을 한 번 더 그리되 색 대신 그 픽셀에 있는 페이지 좌표를 기록한다. 셰이더 주석은 「Write the page point instead of its colour」다. 이 값으로 포인터 아래에 있는 페이지 지점을 알아낸다.
- **HTML 옮기기.** pick 패스로 알아낸 페이지 지점이 실제 HTML에서도 포인터 바로 밑에 오도록 본문 래퍼를 평행 이동한다. 포인터가 띠 바깥에 있으면 래퍼의 `pointer-events`를 끈다.

이동 방법은 앞의 표처럼 Chrome 버전에 따라 다르다. 코드는 처음에 한 번, `updateElementGeometry()`로 래퍼를 1000px 옮겨 달라고 요청해 본다. 그 뒤 `getBoundingClientRect()` 값이 달라졌으면 이 함수가 동작한다고 판정하고, 달라지지 않았으면 `style.transform`을 직접 고친다.

### 게임 쪽 기법 두 가지

- **주운 단어 지우기.** 공이 단어를 주우면, 코드가 CSS Custom Highlight API의 `::highlight(game-picked)`로 그 단어의 글자색을 투명하게 바꾼다. 다음 텍스처 복사부터 그 글자가 띠에서 빠지고, 공에 붙은 조각이 그 단어를 싣고 다닌다. 문서의 글은 그대로 두고 그림에서만 지우는 방식이다.
- **바닥에 누운 시작 버튼.** 공 아래 바닥의 「start」 버튼은 CSS `matrix3d`로 원근에 맞게 눕힌 실제 `<button>`이다. 3D 장면 속 물체처럼 그려지지만 키보드 포커스와 클릭은 일반 버튼과 같다.

## 확인한 것과 추측한 것

| 구분 | 내용 |
|---|---|
| 직접 확인 | 응답 헤더의 오리진 트라이얼 토큰과 그 내용, 지원 판정 코드, 트윗 영상 속 3D 화면에서 글이 선택되는 장면, 렌더 패스 이름과 셰이더 주석, 텍스처 복사 해상도와 1초 재복사 생략 값, 두 API 세대 대응 코드, 게임 문구와 물리 값, 헤드리스 Chrome에서 실패 시 평소 페이지로 돌아가는 동작 |
| 추정 | 분야 이름 옆 숫자가 업데이트 수라는 것, 띠 옆 숫자가 픽셀 거리라는 것, 프런트엔드가 Remix 계열 런타임이라는 것, 3D 전환을 매끄럽게 하려는 카메라 설계 의도 |
| 확인 못 함 | 실제 GPU에서의 프레임 속도, 게임을 끝까지 했을 때의 화면, 제작 팀과 제작 과정(공개된 제작기를 찾지 못했다) |

## 내가 오래 곱씹은 대목

Expo Mode는 페이지 내용을 그대로 게임 소재로 쓴다. 공이 굴러가는 바닥은 방금까지 스크롤하며 읽던 업데이트 소개 페이지이고, 선화 건물과 3D 제목만 새로 그린 장식이다. 그래서 결승선까지 남은 거리를 픽셀로 세고, 공이 줍는 물건도 페이지의 단어다. 주운 단어는 CSS 하이라이트로 글자색을 투명하게 바꿔 화면에서 지운다.

실험 기능을 쓰는 방식도 참고할 만하다. HTML-in-Canvas는 트라이얼 기간에만 두 번 이름과 인자가 바뀌었고, 트라이얼이 끝난 뒤 정식 기능이 된다는 보장도 없다. Shopify는 이 API를 숨은 모드 하나에서만 쓰고, 평소 페이지는 이 API가 없어도 똑같이 보이게 만들었다. 2027년 3월에 토큰이 만료되어도 대부분의 방문자가 보는 평소 페이지에는 아무 변화가 없다.

## 출처

- 원 트윗: 이케다 야스노부(@clockmaker), 2026-10-29. <https://x.com/clockmaker/status/2115599934380806255>
- 사이트: Shopify Editions Fall '26. <https://www.shopify.com/editions/fall2026>
- Chrome for Developers, 「Introducing the HTML-in-Canvas API origin trial」. <https://developer.chrome.com/blog/html-in-canvas-origin-trial>
- Chrome for Developers, 「HTML-in-Canvas updates: Iterating toward a better Web API」. <https://developer.chrome.com/blog/html-in-canvas-ot-changes>
- 구현 분석은 2026-10-29에 사이트의 응답 헤더와 공개 자바스크립트 번들을 내려받아 읽은 결과다. 평소 화면 캡처는 직접 찍었고, Expo Mode 화면 두 장은 원 트윗의 화면 녹화에서 가져왔다.
- 치비 서소영 삽화 2장은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 gpt-image-2.5-flare로 따로 생성했다.

[^tweet]: 원문은 일본어다. 「Shopifyのスペシャルサイト、今回もすごい！HTML-in-Canvasの先進事例。Chromeオリジントライアルの状況で本番採用したこともカッコいい。」

[^names]: 이 모드의 이름은 세 가지다. 콘솔 안내는 Growth Mode, 화면 버튼과 상태 문구는 Expo Mode, 코드에 남은 기본 문구는 New Dimension이다.

[^video]: Expo Mode 장면은 원 트윗의 화면 녹화(macOS의 Chrome)에서 프레임을 가져왔다. 이 글을 준비하며 사용한 서버의 헤드리스 Chrome은 소프트웨어 GPU로 동작해 Expo Mode가 켜지지 않았다(「지원 판정과 실패 처리」 참고).

[^remix]: 번들에는 「clientEntry() requires an entry ID」, 「Remix UI error」 같은 문자열과 `X-Remix-Frame`, `X-Remix-Target` 요청 헤더가 있고, React 런타임은 없다.
