---
title: "7년의 개발, 위시리스트 35,000, 판매 300 — Generation Exile 개발자의 회고"
date: 2026-07-01T23:30:00+09:00
tags: ["게임", "인디 게임", "Steam", "얼리액세스", "인디게임 마케팅"]
categories: ["다이제스트"]
summary: "Sonderlust Studios의 Nels Anderson이 5년에서 7년을 들여 만든 솔라펑크 시티빌더 Generation Exile을 얼리 액세스로 출시한 뒤, 위시리스트 35,000이 넘는데도 첫 주 판매가 300장에 못 미쳤다는 스레드를 r/gamedev에 열었다. 개발자는 EA 회의론과 크리에이터 커버리지 병목을 원인 후보로 지목했고, 상위 답글은 그 자기 진단과 결이 상당히 다른 방향에서 원인을 짚었다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Sonderlust Studios의 Nels Anderson이 5년에서 7년을 들여 만든 솔라펑크 시티빌더 <em>Generation Exile</em>이 위시리스트 35,000이 넘는 상태에서 얼리 액세스로 출시했지만 첫 주 판매량이 300장에 못 미쳤다. Anderson은 r/gamedev에 스레드를 열어 원인 분석을 공개 처리했다.
2. 개발자 본인은 원인 후보로 (1) EA 회의론의 심화, (2) 다른 EA 실패작이 남긴 카테고리 전반의 평판 오염, (3) 가을 인디 러시로 인한 크리에이터와 언론 커버리지 병목 세 가지를 제시했고, 게임 자체 품질과 30달러 가격, 마케팅 실행은 원인이 아니라고 조심스럽게 반박한다.
3. 상위 답글은 개발자의 자기 진단과 결이 상당히 다르다. 트레일러가 "무엇을 하는 게임인가"를 3초 안에 전달하지 못한다는 UX 지적, 30달러가 무명 인디에게는 심리적 경계선을 넘는다는 가격 재프레임, 솔라펑크라는 라벨과 실제 아트 디렉션이 어긋난다는 지적이 상위 표를 받았다.

## 자료의 정체

- <strong>저자</strong>: Nels Anderson (u/nelsormensch). Klei Entertainment의 <em>Mark of the Ninja</em> 리드 디자이너, <em>Firewatch</em>를 만든 Campo Santo 공동창립자.
- <strong>게시일</strong>: 2025년 11월 9일. Reddit r/gamedev에 게시되었고 스레드 스코어는 308, 댓글 수는 355개.
- <strong>게임</strong>: <em>Generation Exile</em>. Sonderlust Studios 6인 팀이 개발한 솔라펑크 시티빌더. Steam appid 2963240. 가격은 29.99달러이고 런칭 주간 10% 할인이 붙었다.
- <strong>사운드트랙</strong>: 본문에서는 "현재 살아 있는 게임 작곡가 중 가장 재능 있는 사람 중 하나"라고만 언급된다. 다른 매체 커버리지에서 Ben Prunty (<em>FTL</em>, <em>Into the Breach</em>)로 확인된다.

## 지표는 모두 맞았다 — 판매 숫자만 빼고

Anderson이 본문에 정리한 지표 요약은 이렇다.

- 2024년 6월 PC Gaming Show에서 트레일러 공개와 동시에 Steam 스토어 페이지 오픈. 1주 만에 위시리스트 17,000 확보.
- 2025년 6월 PC Gaming Show에서 두 번째 트레일러 공개와 함께 Next Fest 데모를 그 자리에서 오픈. 약 2,600개 데모 중 상위 70위권 진입. 1주 만에 위시리스트가 15,000 추가.
- Van Game Garden 오프라인 이벤트에서 낯선 참가자들이 "얼리 액세스 게임치고 완성도가 높아 보인다"는 반응을 남겼다고 기록.
- 출시 전 크리에이터와 언론에 프리뷰 키를 대량 배포. Anderson은 "메일을 정말 많이 보내서 아직도 엄지가 아프다"고 적었다.
- 출시 후 환불률이 얼리 액세스 평균보다 오히려 낮은 수준으로 유지.
- 그리고 얼리 액세스 출시 첫 주 판매량이 300장 미만.

Anderson의 표현을 그대로 옮기면 다음과 같다.

> [지표가 가리키고 있었어야 할 방향과] 지난 며칠 사이 실제로 일어난 일 사이의 간극을 이해하려는 것.

## 개발자가 지목한 원인 후보

### 얼리 액세스에 대한 회의론이 이전과 다르다

> seems neat but I don't buy anything in Early Access anymore

Anderson이 여러 댓글에서 반복적으로 마주쳤다고 밝힌 정서다. 여기서 그가 주목한 단어는 <em>anymore</em>다. 원래도 얼리 액세스를 안 사는 사람은 있었지만, 지금은 그 태도가 광범위하게 퍼져 있다는 점이 새롭다는 것이 그의 관찰이다.

Larian과 <em>Baldur's Gate 3</em>, <em>Hades II</em> 같은 극단적으로 알려진 quantity거나 "인기 X와 살짝 다른 무언가"로 즉각 알아볼 수 있는 게임이 아니면 얼리 액세스의 상승 여력이 몇 년 전만큼 남아 있는지 확신이 없다고 정리한다.

### 얼리 액세스는 냄새가 옮는다

첫 번째 원인의 짝이 되는 관찰이다. 다른 EA 게임이 실패하면 무관한 우리 EA 게임까지 색안경을 받는다는 것이다. FPS 하나가 망해도 다른 FPS에 영향은 없지만, EA는 라벨 자체로 묶여 평가된다. Anderson은 이걸 "the Early Access stink on you"라고 표현했다.

### 크리에이터와 언론의 인지 병목

<em>Arc Raiders</em>, <em>Dispatch</em> 같은 가을 인디 히트작 사이에 무명 팀이 끼면 커버리지 후순위로 밀린다는 진단이다. Anderson은 여기에 chicken-and-egg 문제가 있다고 본다. 크리에이터는 이미 잘 알려진 게임이거나 다른 크리에이터가 이미 다루고 있는 게임을 커버하기를 선호하는데, 다들 남이 먼저 움직이기를 기다리면 그 공은 굴러가지 않는다.

Anderson은 팀의 이전 크레딧을 나열한다. <em>Mark of the Ninja</em>의 리드 디자이너 자신, Campo Santo 공동창립과 <em>Firewatch</em>, <em>Gone Home</em>과 <em>Mini Motorways</em>의 핵심 제작진, <em>Baldur's Gate 3</em>와 <em>Far Cry 5/6</em>의 상당한 기여자들. 그 정도면 적어도 "한 번은 볼 만한가"라는 초기 검토 정도는 통과할 줄 알았다고 쓴다.

## 원인이 아니라고 본 것

Anderson은 다른 사람들이 자주 원인으로 지목하는 세 가지를 부드럽게 반박한다.

### 게임 자체의 품질

완성도와 프레젠테이션과 깊이에서 다른 얼리 액세스 타이틀 평균보다 아래는 아니라고 본다. 다만 "3\~4시간이면 다 클리어된다"는 지적은 부분적으로만 인정한다. Generation Exile은 procedural 구조라 재플레이마다 맵과 NPC가 새로 생성되고 이벤트도 상태에 따라 다르게 전개된다. Civ도 3\~5시간이면 한 판이 끝나지만 아무도 Civ가 짧다고 말하지 않는다는 예를 들었다.

### 가격

29.99달러. 유사 장르 대비 가격, 팀의 트랙 레코드, Ben Prunty의 사운드트랙을 고려했을 때 20달러 아래로 내리면 오히려 "싸 보임 = 저품질"이라는 우려가 생긴다는 것이 Anderson의 판단이다. 24.99달러로 낮췄어도 지금의 상황이 근본적으로 달랐을 것 같지는 않다고 유지한다.

여기서 그가 인용하는 반례는 모바일 게임 시장의 붕괴다. 지금 모바일 게임 산업은 사실상 "플레이어 획득에 2.03달러 쓰고 그 플레이어에게서 평균 2.07달러를 뽑거나, 아이들을 도박에 중독시키거나, 둘 다"의 구조에 얹혀 있다. 그런 race-to-the-bottom에는 참여하지 않겠다는 태도다.

### 마케팅 실행

가능한 것은 다 했다는 입장이다. PC Gaming Show에서 2년 연속 트레일러를 냈고, Next Fest 데모를 그 자리에서 오픈했으며, 크리에이터와 언론에 프리뷰 키를 대량 배포했다. PC Gamer와 Rock Paper Shotgun에서 우호적인 커버리지가 나왔다. 소셜 미디어는 노력 대비 효과가 낮다는 것이 최근 상식이라 안 하는 편이 오히려 나을 수 있다고 쓴다.

## 커뮤니티의 반론 — 결이 다른 원인 진단

r/gamedev의 상위 답글은 개발자의 자기 진단과 상당히 결이 다르다.

### 트레일러가 무엇을 하는 게임인지 보여주지 않는다

가장 많은 표를 받은 <strong>u/jezvin</strong> (163점)의 답글:

> After watching all of your trailers and the interview, and understanding the back story and setting. I can't even picture the first building not to mention the whole of the space ship fully constructed.

대조군으로 <em>Farthest Frontier</em>의 첫 트레일러를 든다. 대사나 UI 없이 한 채의 건물이 마을로, 도시로 자라나는 과정을 그저 보여준다. 시청자는 자기가 게임 안에서 무엇을 할지를 3초 안에 그림으로 그린다.

Anderson의 답변은 자기 진단 조정의 신호로 읽힌다.

> I think we might have overcalibrated a bit on trying to show the ways in which what we have augments the core city-building experience and didn't emphasize enough just what that core experience, y'know, is.

### 세대함선 배경이 트레일러에서 전달되지 않는다

<strong>u/TyRoXx</strong> (68점):

> Please trust me on this: 80% of the people who view your trailer will NOT understand that the game is set inside of a spaceship. Most people will think it's about a colony on a strangely yellow planet.

Generation Exile의 세계관은 흥미로운 세대함선(generation ship) 안이지만, 트레일러에서는 그저 "노란색이 이상하게 감도는 어떤 행성"으로 보인다는 지적이다. 다른 답글들이 "확실히 그렇다"고 확인 답변을 달았다.

### 30달러는 심리적 경계선을 넘는다

<strong>u/0ddSpider</strong> (115점), <strong>u/midge</strong> (81점), <strong>u/LordDrakced</strong> 등:

- "무명 인디 게임에 30달러를 쓰지 않는다."
- 20달러와 30달러 사이는 산술이 아니라 심리다. 20달러 이하는 "가볍게 산다", 30달러에 가까우면 "고민한다."
- <strong>u/PartyWanted</strong>는 보드게임 시장 경험을 근거로 19.99달러라면 상당히 달랐을 것이라고 짚었다. 29에서 25로 내려도 큰 변화는 없겠지만, 19.99는 다른 세계다.

Anderson은 여기에 대해 24.99달러로 갔어도 크게 달라지지 않았을 것이라는 자기 입장을 유지하면서도, 답글에서는 "우리 계기판이 옛 것이었을 수 있다"고 부분적으로 인정한다.

### 솔라펑크 라벨과 아트 디렉션이 어긋난다

<strong>u/SomebodyUnown</strong>:

> I was attracted here by the word 'solarpunk' in the title. If that's intended, the art direction/vibe is very different from what I expected which is lots of light, green, community, vibrancy, and positivity.

솔라펑크라는 단어로 유입된 사람이 실제 화면에서 마주치는 것은 어둡고 채도가 짙은 빨강과 보라와 노랑이다. 유저 태그로 검색이 걸리는 colony sim이나 nature나 survival 같은 단어에 맞춰 마케팅 언어를 바꾸는 편이 나았을 수 있다는 제안이 뒤따른다.

### 위시리스트-판매 전환율이 원래 그 수준일 수 있다

<strong>u/0ddSpider</strong> (115점)는 통계적 재프레임도 함께 던진다. 인디 얼리 액세스에서 위시리스트 대비 첫 주 전환율은 낮은 한 자릿수 %가 보통이다. 위시리스트 35,000 대비 판매 300은 발화자가 느끼는 것만큼 극단적인 이상치가 아닐 수 있고, 얼리 액세스와 무명 팀과 30달러가 겹치면 자연스럽게 나오는 결과라는 시각이다.

## 가장 곱씹은 대목

내가 곱씹은 것은 개발자와 커뮤니티가 서로 다른 언어로 실패를 설명하고 있다는 점이다.

Anderson은 시장 구조의 언어로 말한다. 얼리 액세스 카테고리의 평판, 크리에이터 파이프라인의 병목, 가을 인디 러시의 타이밍. 세 가지 모두 "우리 팀 밖의 요인"이다.

상위 답글은 제품의 언어로 말한다. 트레일러가 무엇을 하는 게임인지를 안 보이게 하고, 30달러가 심리 경계선을 넘고, 아트 디렉션이 장르 라벨과 어긋난다. 세 가지 모두 "너희 팀이 만든 결과물 안의 문제"다.

Anderson은 커뮤니티의 지적을 부드럽게 받아들이면서도 자기 진단을 크게 바꾸지 않는다. "계기판이 옛 것이었을 수 있다", "말할 필요가 있는 것을 덜 강조했을지도 모른다"고 인정하지만, 결론의 무게는 여전히 EA 회의론이라는 시장 요인 쪽에 놓여 있다.

Chris Zukowski가 2023년 얼리 액세스 데이터 분석에서 이미 지적한 <em>EA quicksand</em> — 출시를 망치면 영구 negative 리뷰가 따라붙는 비대칭 위험 — 은 Anderson도 명확히 인지하고 있었다. Zukowski의 데이터는 "얼리 액세스는 보상이 약간 높지만 위험도 훨씬 큰 길"이었는데, Anderson의 회고는 그 위험 축이 2025년에 더 가팔라졌음을 증언한다. 다만 그 가팔라짐이 얼리 액세스 자체의 시장 실패 때문인지, 아니면 Generation Exile의 개별 실행 문제 때문인지는 이 스레드만으로는 결론이 나지 않는다.

Anderson은 스레드 말미에 이렇게 적었다.

> 우리는 여섯 명이고, 부양할 가족이 있고, 낼 월세가 있고, 사야 할 식료품이 있다. 그리고 우리는 끝없는 탐욕적 성장과 그것이 요구하는 잔인한 수확에 관한 것이 아닌 장르의 게임을 만드는 여섯 명이기도 하다.

지표가 가리키던 방향과 실제 판매 사이의 간극이 왜 그렇게 벌어졌는지에 대한 최종 답은 여기에 없다. 다만 다른 팀이 어느 지표를 어떻게 읽어야 할지에 대한 참고 데이터포인트가 하나 남았다.

## 출처

- 저자: Nels Anderson (u/nelsormensch, Sonderlust Studios)
- 게시일: 2025-11-09
- 매체: Reddit r/gamedev
- 원문: <https://www.reddit.com/r/gamedev/comments/1osr00n/i_spent_7_years_making_generation_exile_a/>
- 관련 다이제스트: [Should you do Early Access? — Zukowski (2023)](/digest/zukowski-should-you-do-early-access-2023/)
- 게임 페이지: <https://store.steampowered.com/app/2963240/Generation_Exile/>
- 원문 selftext에는 인용할 이미지가 포함되어 있지 않아 텍스트 다이제스트로 진행했다.
