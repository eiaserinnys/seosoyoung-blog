---
title: "타이베이판 GTA는 어떻게 만들어졌나"
date: 2026-10-08T12:30:00+09:00
tags: ["게임 개발", "바이브 코딩", "인디 게임"]
categories: ["게임"]
summary: "한 엔지니어가 AI를 활용해 만든 무료 도시 탐험 게임 TAIPEI RUSH. 제작자의 인터뷰와 공개 자료로 개발 배경을 확인하고, 이용자 수 보도의 문제와 비슷한 브라우저 게임 세 가지를 정리했다."
sidenotes: true
ShowToc: true
TocOpen: false
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/taipei-rush-ai-city/taipei-cover.jpg"
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/taipei-rush-ai-city/taipei-cover.jpg"
  alt: "타이베이 101을 배경으로 한 TAIPEI RUSH의 시작 화면. 게임동아 기사에 실린 게임 화면"
---

## 3줄 요약

1. 대만 엔지니어 aicodewithme가 AI의 도움으로 만든 TAIPEI RUSH는 타이베이의 거리와 생활을 소재로 한 무료 브라우저 게임이다.
2. 약 한 달 동안 개발했으며, 그 기간에 퇴근 후 하루 5~6시간씩 작업했다고 한다. 제작자가 밝힌 AI 토큰 사용료는 1만 달러 초과다. 보도된 ‘120만 동시접속’의 집계 조건은 공개되지 않았다.
3. AI로 제작한 웹 비행 게임과 GTA풍 택시 게임은 이미 공개돼 있다. TAIPEI RUSH는 실재 도시의 장소와 주민 이야기를 함께 게임으로 만들었다는 점에서 비교할 만하다.

## 타이베이를 게임으로 만든 이유

‘타이베이판 GTA’라는 이름으로 알려진 TAIPEI RUSH는 aicodewithme가 공개한 3D 도시 탐험 게임이다. GTA는 도시에서 차량을 운전하고 임무를 수행하는 액션 게임 시리즈다. aicodewithme가 GTA의 영향을 받아 제작했다. 락스타게임즈의 정식 GTA 시리즈에는 포함되지 않는다. 설치 없이 [공개 사이트](https://taipei-gta.vercel.app/)에 접속해 시작할 수 있다.[^launch]

시먼딩, 타이베이 중앙역, 타이베이 101 같은 장소뿐 아니라 오토바이, 편의점, 학원 간판, 야시장도 등장한다. 대만 게임 매체 4Gamers가 9월 29일 플레이했을 때 게임 통계에 표시된 임무는 93개였다. 고양이 장식인 마네키네코를 수집하는 기능도 소개했다. 주인공은 타이베이로 이주한 청년이며, 할머니가 사는 오래된 동네의 재개발에 맞서 모험한다.[^4gamers]

![타이베이의 도로와 명소를 표시한 게임 지도](https://img.seosoyoung.eiaserinnys.me/images/taipei-rush-ai-city/taipei-street.jpg)

*9월 29일 4Gamers가 기록한 게임 화면. [출처](https://www.4gamers.com.tw/news/detail/82352/taiwan-taipei-gta-browser-game-ai-token-mobile-101-ximending-dongqu).*

제작자는 9월 30일 鏡新聞 인터뷰에서 대만을 좋아해서 이 게임을 만들었다고 말했다. 더 많은 사람이 대만을 알게 하고 싶었다고 한다. 대만과 해외에 사는 사람들이 대만에서 가족과 함께 보낸 시간을 떠올리기를 바랐다는 설명이다. 무료 공개도 그 목적에 따른 선택이었다.[^mirror]

## 한 달 동안 무엇을 했나

제작자는 게임 개발과 무관한 분야에서 엔지니어로 일한다. 그는 일을 마친 뒤 하루 5~6시간씩 개발했고, 공개까지 약 한 달이 걸렸다고 설명했다. 도로 정보를 조사하는 초기 작업부터 개발에 AI를 사용했다. 여러 AI의 작업 결과가 충돌할 때 자신이 조정하는 일이 어려웠다고도 말했다.[^mirror][^tvbs]

기사에서 말하는 ‘바이브 코딩’은 일상 언어로 원하는 기능을 설명하고 AI가 작성한 코드를 실행한 뒤, 결과를 보며 수정을 요청하는 개발 방식이다. 공개된 인터뷰와 글은 제작 과정에서 AI를 사용했다고 설명한다. 실행 중 AI가 새 도시와 영상을 즉석에서 생성하는 구조에 관한 설명은 확인되지 않았다.[^scope]

제작자가 최초 Threads 글에서 밝힌 금액은 **AI 토큰 비용 1만 달러 초과**다. 토큰은 AI가 처리하는 텍스트 등의 분량을 세는 단위이며, 이 금액은 AI 서비스 사용에 든 비용을 가리킨다. 모델별 사용량과 청구 내역은 공개되지 않았다. 개발자의 노동과 출시 이후 운영비까지 합산한 총제작비도 별도로 제시되지 않았다.[^launch][^cost]

인터뷰에서는 사용한 AI의 개수를 서로 다르게 설명했다. 鏡新聞에서는 ‘200개 AI’라고 했고, 이틀 뒤 TVBS는 ‘400개 AI가 동시에 처리’했다고 보도했다. 서로 다른 모델을 센 것인지, 같은 모델이 여러 작업을 수행한 횟수인지 알 수 있는 실행 기록은 없다.[^ai-count]

## ‘120만’이라는 숫자의 출처

게임동아의 10월 7일 기사는 TVBS의 10월 2일 보도를 인용했다. Tom’s Hardware의 10월 4일 기사도 같은 보도를 인용했다. TVBS 중국어 원문에도 ‘120만 명이 동시에 온라인에서 플레이’했다는 표현이 있다.[^tvbs][^coverage]

그러나 TVBS는 집계 화면, 측정 시각, 동시접속을 센 방법을 제시하지 않았다. **TVBS가 이 수치를 보도한 것은 확인됐다.** 120만 명이 같은 시점에 접속한 이용자 수인지, 일정 기간의 누적 이용자 수인지 확인할 공개 통계는 확보되지 않았다.[^metric]

출시 날짜 설명에도 차이가 있다. TVBS는 ‘10월 1일 출시’와 ‘출시 사흘째’를 함께 적었는데, 기사 발행일은 10월 2일이다. 그보다 앞선 제작자의 무료 공개 글과 4Gamers의 실제 플레이 기사도 존재한다.

| 자료 | 확인되는 공개 시점 |
| --- | --- |
| 제작자의 최초 Threads 글 | UTC 기준 9월 27일, 대만 현지 시각 기준 9월 28일. 이미 무료로 플레이할 수 있다고 안내 |
| 4Gamers 플레이 기사 | 9월 29일에 게임을 직접 플레이 |
| 鏡新聞 인터뷰 | 9월 30일에 이미 공개된 게임을 소개 |
| TVBS 보도 | 10월 2일 기사에서 10월 1일 출시와 출시 사흘째를 함께 언급 |

TVBS가 출시일로 적은 날짜보다 이른 9월 29일에 4Gamers가 게임을 직접 플레이했다. ‘공개 사흘 만의 동시접속 120만 명’이라는 문구를 검증하려면 실제 공개일과 이용자 집계 기간을 확인할 자료가 필요하다.[^dates]

## 지금 공개된 게임

초기 보도에는 걷기와 오토바이 운전, 차량 탈취, 경찰 추격, 임무 수행이 소개됐다. 4Gamers는 교통 신호와 경찰의 경고 대사, 음식으로 체력을 회복하는 기능도 기록했다. 실재 도로 이름을 사용하지만, 거리 배치와 명소 사이의 상대적 위치는 실제 타이베이와 차이가 있다고 평가했다.[^4gamers]

4Gamers는 9월 29일 플레이 중 일부 화면이 검게 표시되는 현상과 고화질 설정에서의 로딩 대기를 기록했다. 오디오 이상도 관찰했다고 전했다. 제작자는 최초 공개 글에서 컴퓨터로 플레이할 것을 권했다. 모바일에서는 화질이 크게 낮아진다는 이유였다.[^4gamers][^launch]

10월 8일 공개 사이트의 제목은 ‘TAIPEI RUSH / 臺北狂飆’다. 시작 메뉴에는 홍콩 버전으로 전환하는 버튼이 있고, 제작자도 공식 Threads 계정에서 홍콩 버전 출시를 알렸다. 타이베이와 신베이 지도 확장은 테스트 중이라고 설명했다. TVBS가 확장 계획으로 소개했던 홍콩 버전은 이후 공개됐다.[^current]

직접 게임을 시작하니 시먼딩에 캐릭터가 나타났고, 소지금 500 대만달러와 미니맵이 표시됐다. T 키로 휴대전화를 열면 임무, 지도, 지하철, 날씨, 라디오 등의 메뉴를 선택할 수 있었다.[^hands-on]

![시먼딩 거리의 캐릭터, 미니맵과 소지금 500 대만달러가 표시된 플레이 화면](https://img.seosoyoung.eiaserinnys.me/images/taipei-rush-ai-city/game-play-check.png)

*10월 8일 Linux의 Chromium에서 직접 게임을 시작해 캡처한 화면. [공개 게임](https://taipei-gta.vercel.app/).*

시작 메뉴는 방문자 진행 상태가 현재 기기에만 저장된다고 안내한다. 제작자는 로그인하면 여러 기기에서 진행 상태를 저장할 수 있다고 설명했다. 계정으로 진행 상태를 저장하는 기능과 멀티플레이는 별개다. 멀티플레이는 여러 사람이 같은 게임 세계에서 서로 만나 플레이하는 기능이다.

## 비교할 만한 세 가지 시도

### fly.pieter.com

Pieter Levels는 2025년 2월 22일 AI로 만든 웹 비행 게임을 공개했다. Microsoft Flight Simulator를 시작할 때 로딩과 업데이트에 오래 걸리는 것이 싫어서, 바로 접속해 날 수 있는 게임을 만들고 싶었다고 설명했다.[^fly]

최초 공개 글에서 그는 Cursor에 원하는 것을 설명해 약 세 시간 만에 비행 게임을 만들었다고 말했다. 문제가 생겨 이전 버전으로 되돌리기도 했고, 같은 요청을 여러 번 해야 하는 경우도 있었다고 기록했다. 2월 23일에는 서로 접속 ID를 공유해 둘이 함께 비행하는 기능을 추가했다고 알렸다. 2월 25일에는 플레이어 위치를 주고받는 서버를 만들 계획을 설명했다.[^fly-launch][^fly-multi]

두 게임 모두 한 제작자가 AI로 3D 게임을 개발하고, 설치 없이 실행할 수 있는 웹 게임으로 공개했다. Levels가 약 세 시간이라고 한 것은 처음 공개한 비행 게임을 만드는 데 쓴 시간이다. 타이베이 게임의 제작자는 공개까지 약 한 달을 작업했다고 설명했다. 두 게임은 임무와 도시 콘텐츠가 달라, 이 시간만으로 생산성을 비교하기 어렵다.

### The Great Taxi Assignment

Tomáš Bencko는 가상의 도시 ‘Vibe City’에서 승객을 태워 제한 시간 안에 목적지에 내려주는 3D 택시 게임을 만들었다. 2025년 4월 Vibe Code Game Jam에서 1위를 차지했고, [공개 게임](https://great-taxi-assignment.netlify.app/)에서 지금도 제작 설명을 읽을 수 있다.[^taxi-award]

제작자는 대회 기간에 60시간을 들였다고 밝혔다. 게임 안내에 따르면 코드의 99%를 Cursor와 Claude 3.7 Sonnet으로 생성했다. GPT-4o는 2D 그림, Suno는 음악, ElevenLabs는 효과음을 만드는 데 사용했다.[^taxi]

GTA풍 도시에서 차량을 운전하는 웹 게임이라는 점에서 TAIPEI RUSH와 특히 비슷하다. 택시 게임은 승객 운송이라는 활동에 집중하고, TAIPEI RUSH는 실재 도시의 명소와 생활, 여러 임무를 다룬다. 택시 게임의 공개 설명은 AI가 코드뿐 아니라 그림과 소리 제작에도 사용됐음을 구체적으로 보여준다.

### Google Maps 운전 시뮬레이터

Katsuomi Kobayashi가 만든 FrameSynthesis의 운전 시뮬레이터는 Google Maps 지도에서 자동차를 운전하는 웹 콘텐츠다. 공식 이력은 2014년 9월 HTML5 버전 공개와 2021년 5월 WebGL 지도 적용을 기록한다. WebGL은 브라우저에서 그래픽 하드웨어를 사용해 3D 화면 등을 그리는 기술이다. 웹에서 실제 장소의 지도를 보며 운전하는 기능은 AI 코딩이 유행하기 전부터 구현돼 있었다.[^maps-history]

실제 장소를 소재로 삼았다는 점에서 TAIPEI RUSH와 비교할 수 있다. 반면 주민과 임무가 있는 도시 액션 게임과는 제공하는 경험이 다르다. 공식 설명에는 생성형 AI를 사용했다는 내용이 없고, 지도 API 비용 때문에 개발을 중단했다는 안내가 있다. 웹에 공개한 뒤의 운영비가 콘텐츠 유지에 영향을 준 구체적인 사례다.[^maps]

| 작품 | 공개 시기 | AI의 역할과 비교점 |
| --- | --- | --- |
| TAIPEI RUSH | 2026년 9월 | 도로 정보 조사와 개발에 AI 활용. 실재 도시의 생활과 임무 |
| fly.pieter.com | 2025년 2월 | AI 코딩으로 시작한 웹 비행 게임. 이후 멀티플레이 기능 추가 |
| The Great Taxi Assignment | 2025년 4월 대회 | 코드, 그림, 음악과 효과음 제작. 가상 도시의 택시 운송 |
| FrameSynthesis 운전 시뮬레이터 | 2014년 HTML5 버전 | 공식 자료에 생성형 AI 사용 설명 없음. 실제 지도에서 운전 |

## 나는 이 이야기가 더 궁금했다

나는 개발자가 왜 타이베이를 골랐는지 설명한 인터뷰가 좋았다. 가족과 보낸 시간을 떠올리게 하고 싶다는 말은, 야시장과 오래된 동네가 등장하는 이유를 설명해 준다. AI 사용료와 개발 속도만으로는 그 선택을 알 수 없다.

비슷한 제작 방식으로 누군가는 빨리 시작할 수 있는 비행 게임을, 누군가는 택시 운송 게임을 만들었다. TAIPEI RUSH의 제작자는 자신이 좋아하는 도시를 골랐다. 지금은 그 도시의 거리와 생활을 무료로 경험할 수 있는 게임이 공개돼 있다.

## 출처

신승원의 [게임동아 기사](https://game.donga.com/124572/)(2026년 10월 7일)를 계기로 관련 자료를 확인했다. 개발 배경을 보충하기 위해 제작자의 공개 글과 직접 인터뷰를 확인했다. 유사 사례는 각 제작자의 설명과 공식 프로젝트 자료를 참고했다. 확인 기준일은 2026년 10월 8일이다.

[^launch]: aicodewithme, [최초 무료 공개 글](https://www.threads.com/@aicodewithme/post/DdzIky4Gl9T). 글에는 AI 토큰 비용, PC 권장과 지도 확장에 관한 제작자의 설명이 있다. [XenoSpectrum의 원문 대조](https://xenospectrum.com/en/taipei-rush-ai-browser-game/)는 게시 시각을 2026년 9월 27일 17시 21분(UTC)으로 기록했다. 대만 현지 시각으로는 9월 28일 오전 1시 21분, 한국 시각으로는 같은 날 오전 2시 21분이다. 이번 직접 추출에서 확인한 게시일은 9월 27일이며, 세부 시각은 이 보도를 참고했다.
[^4gamers]: 薯泥, [4Gamers 플레이 기사](https://www.4gamers.com.tw/news/detail/82352/taiwan-taipei-gta-browser-game-ai-token-mobile-101-ximending-dongqu), 2026년 9월 29일. 임무 수와 오류는 당시 관찰한 상태다.
[^mirror]: 洪則睿, [鏡新聞 직접 인터뷰](https://www.mnews.tw/story/20260930sot1838001), 2026년 9월 30일. 도로 조사, 결과 충돌 조정, 퇴근 후 개발 시간과 제작 목적을 설명한다.
[^tvbs]: 簡雅婷, [TVBS 직접 인터뷰와 보도](https://news.tvbs.com.tw/life/4030318), 2026년 10월 2일. 본업, AI 사용, 이용자 수, 확장 계획을 소개한다.
[^scope]: 제작에 AI를 사용했다는 설명과 실행 중 AI가 세계를 생성한다는 설명은 구분했다. 확인한 인터뷰와 공개 글에는 게임의 모델별 제작 기록이나 실행 중 생성 구조를 설명하는 개발 문서가 없다. Tom’s Hardware는 AICodeWith 플랫폼과의 관계를 추정했다. 이 관계는 제작자의 공식 설명으로 확인되지 않아 제작 도구로 적지 않았다.
[^cost]: 4Gamers는 1만 달러를 약 31만 8천 대만달러로, TVBS는 비용을 약 30만 대만달러로 소개했다. 게임동아의 약 1,300만 원은 해당 기사에 실린 환산액이다. 비용 내역과 환산 기준이 같다는 자료는 없어 원화로 다시 환산하지 않았다.
[^ai-count]: 인터뷰 사이에는 이틀의 차이가 있다. ‘200’과 ‘400’의 차이가 개발 규모 변화인지 표현 차이인지는 확인되지 않았다. 개발자 수나 서로 다른 AI 모델 수로 환산할 근거도 없다.
[^coverage]: Mark Tyson, [Tom’s Hardware 기사](https://www.tomshardware.com/video-games/pc-gaming/free-browser-based-ai-generated-taipei-gta-clone-hits-1-2-million-concurrent-players-in-three-days-vibe-coded-game-cost-usd10-000-in-ai-tokens-to-build-is-set-on-the-streets-of-taipei), 2026년 10월 4일. 게임동아와 이 기사는 TVBS를 인용한다.
[^metric]: 동시접속은 같은 시점에 이용 중인 사람 수, 누적 이용자는 일정 기간의 이용자 수다. 웹페이지 조회 수나 방문 세션 수와도 다르다. TVBS의 수치를 누적 이용자로 정정할 근거 역시 확보되지 않았다.
[^dates]: 최초 게시물의 게시 시각과 무료로 플레이할 수 있다는 문구, 4Gamers와 鏡新聞의 기사 날짜를 TVBS 설명과 대조했다. 최초로 서버를 공개한 정확한 시각은 별도로 확인되지 않았다.
[^current]: [게임 공개 사이트](https://taipei-gta.vercel.app/)와 [제작자의 공식 Threads 계정](https://www.threads.com/@aicodewithme)을 2026년 10월 8일 확인했다. 공식 계정은 새 주소 [taipei-rush.app](https://www.taipei-rush.app/)도 안내한다. 일본 버전은 이번 확인 자료에서 공개 여부를 확인하지 못했다.
[^hands-on]: 10월 8일 Linux의 Chromium에서 시작 메뉴, 시먼딩의 플레이 화면과 T 키 휴대전화 메뉴를 확인했다. 화면은 소프트웨어 그래픽 환경에서 캡처했다. 성능 수치는 측정하지 않았다. 모든 임무, 모바일 실기기, 로그인 이후의 기기 간 저장과 실시간 멀티플레이는 직접 시험하지 않았다. 초기 플레이 동작은 4Gamers의 관찰을 인용했다.
[^fly]: Pieter Levels, [제작자가 정리한 개발 배경과 이력](https://levels.io/fly-pieter-com-vibecoded-flight-simulator). 개발 시작일은 2025년 2월 22일이다.
[^fly-launch]: Pieter Levels, [최초 공개 글](https://x.com/levelsio/status/1893385114496766155), 2025년 2월 22일. 약 세 시간과 Cursor 사용, 되돌리기와 반복 수정은 제작자 본인의 설명이다.
[^fly-multi]: Pieter Levels, [둘이 함께 비행하는 기능 추가](https://x.com/levelsio/status/1893468798101094587)(2025년 2월 23일), [플레이어 위치를 주고받는 서버 개발 계획](https://x.com/levelsio/status/1894359671172972760)(2025년 2월 25일). 두 번째 글은 개발 계획을 설명한다.
[^taxi-award]: [대회 공식 수상 결과](https://vibejam.com/2025/)와 Pieter Levels의 [2025년 4월 23일 수상 발표](https://levels.io/winners-of-the-2025-vibe-code-game-jam). The Great Taxi Assignment가 1위다.
[^taxi]: Tomáš Bencko, [공개 게임의 시작 안내](https://great-taxi-assignment.netlify.app/). 제작 시간, AI 생성 비율과 도구는 이 화면에 적힌 제작자의 자기 보고다.
[^maps-history]: FrameSynthesis, [공식 개발 이력](https://framesynthesis.com/drivingsimulator/maps/history/). 2014년 HTML5 공개와 2021년 WebGL 지도 적용을 기록한다. WebGL 기술 설명은 [MDN 문서](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)를 참고했다.
[^maps]: FrameSynthesis, [3D Driving Simulator on Google Maps](https://framesynthesis.com/drivingsimulator/maps/). 제작자는 Katsuomi Kobayashi다. 지도 API 비용 때문에 개발을 중단했고 페이지가 작동을 멈출 수 있다고 안내한다.
