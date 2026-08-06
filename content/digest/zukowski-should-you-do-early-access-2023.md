---
title: "Should you do Early Access?"
date: 2026-05-06T15:10:00+09:00
tags: ["스팀", "얼리액세스", "인디게임 마케팅", "VGInsights"]
categories: ["게임"]
summary: "Chris Zukowski가 VGInsights 데이터를 끌어 EA 경로와 일반 출시 경로의 매출·평점을 정면 비교한다. 평균만 보면 EA가 더 좋아 보이지만, 100+ 리뷰 게임만 추리면 차이가 모호해지고 'EA quicksand'라는 비대칭 위험이 드러난다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Chris Zukowski가 2023년 7월에 발표한 글로, VGInsights 데이터를 바탕으로 일반 출시(Normal Launch) · EA 진입 · 1.0 졸업 세 경로의 매출·리뷰·평점을 직접 비교한다.
2. 평균/중앙값 매출 모두에서 1.0 졸업 게임이 가장 높고 일반 출시가 그 다음이지만, 100+ 리뷰 게임만 추리면 일반 출시가 평균 매출에서 도리어 EA를 앞선다. EA의 "더 좋아 보이는 평균"의 상당 부분은 1.0 졸업까지 도달한 생존자 효과다.
3. EA는 두 번의 위시리스트 이메일 폭격이라는 명확한 마케팅 이점을 가지지만, 출시를 망치면 영구 negative 리뷰가 따라붙는 "EA quicksand"에 빠진다. EA 출시는 베타가 아니라 <strong>진짜 출시</strong>이며, 자금 조달이나 피드백 수집 목적의 EA 진입은 거의 항상 실패한다.

## 자료의 정체

- <strong>저자</strong>: Chris Zukowski. 인디게임 마케팅 컨설턴트, "How To Market A Game" 운영자.
- <strong>시점</strong>: 2023년 7월 27일.
- <strong>데이터 출처</strong>: vginsights.com에서 받은 CSV. 분석은 ChatGPT-4 Code Interpreter로 수행.
- <strong>분석 범위</strong>: 2019년 이후 출시된 게임. 2018년 Valve의 알고리즘 변경(shovelware 가시성 축소) 이전과 이후를 명확히 분리한다.

저자는 첫 작품 개발자에게 거의 항상 "그냥 정식 출시하라"고 답해 왔는데, 이번에 직접 숫자를 돌려보고 자신의 직감을 일부 수정한다. 다만 그 수정은 "EA가 정답"이 아니라 "EA는 보상이 약간 높지만 위험도 훨씬 큰 길"이라는 결론에 닿는다.

## 용어 정리

- <strong>EA</strong>: Steam Early Access 프로그램으로 출시되어 판매 중이지만 아직 1.0이 아닌 게임. (Electronic Arts 회사가 아니다.)[^strong-2023][^estimating-2023]
- <strong>1.0</strong>: EA로 먼저 출시된 후 정식 출시까지 마친 게임.
- <strong>Normal Launch (일반 출시)</strong>: EA를 거치지 않고 처음부터 정식으로 출시된 게임.

## EA의 짧은 역사

Valve는 2013년 3월 20일에 Early Access를 도입했다. 핵심 약속은 두 가지였다.

1. EA 게임은 출시가 두 번이다. EA 출시 한 번, 1.0 졸업 한 번.
2. 개발자가 개발 중에 매출을 받기 시작한다. 게임 산업의 가장 나쁜 점 중 하나가 "긴 개발 기간 동안 한 푼도 못 받다가 출시 직후 한 번에 큰 매출을 받는다"는 구조였는데, EA는 이걸 분산한다.

![연도별 EA 게임 출시 수 — 2014년 이후 꾸준히 증가하여 2022년 약 2,300개에 도달](/images/zukowski-should-you-do-early-access-2023/image-18.png)

2014년 이후 EA 프로그램에 참여한 게임은 누계 10,549개 이상이다. Steam 전체 출시작 대비 비율로 보면 2017\~2020년에 약 20%까지 부풀어 올랐다가 최근 약간 줄어든 상태다.

![Steam 전체 출시 대비 EA 비율 — 2019\~2020년에 약 20%로 정점을 찍은 뒤 18%대로 안정](/images/zukowski-should-you-do-early-access-2023/image-19.png)

## 1.0까지 졸업하는 게임은 얼마나 되는가

초창기(2014\~2017)의 EA는 "킥스타터처럼 일단 던져 보고 반응을 보는 곳"으로 남용되었다. 2016년에 EA로 출시된 게임의 <strong>90%</strong>가 끝내 1.0으로 졸업하지 못했다.

![연도별 EA 게임 중 1.0 졸업 비율 — 2014\~2017년은 졸업률 10% 미만, 2018년부터 점프](/images/zukowski-should-you-do-early-access-2023/image-17.png)

저자가 두 번째 차트에서 확인한 시청자 정서는 가혹하다. "어렸고 어리석었던 시절에 이 \*게임\*을 샀다. 그 덕분에 다시는 EA 게임을 사지 않게 됐다." 이런 부정적 학습 효과가 EA 전반의 평판을 짓눌렀다.

2018년부터 1.0 졸업률이 뚜렷하게 점프하는 이유로 저자는 같은 해 Valve의 알고리즘 개편을 지목한다. 매출이 나오는 게임에 가시성을 몰아주는 방향으로 바뀌면서 shovelware 업체가 EA에서 빠르게 빠져나갔다는 것이다. 이 분기점 때문에 글의 나머지 모든 비교는 2019년 이후 데이터로 한정된다.

## VGInsights 비교 표 — 전체 게임

2019년 이후 출시된 모든 게임을 출시 유형별로 묶은 결과다.

| 출시 유형 | 평균 추정 매출 | 중앙값 추정 매출 | 평균 리뷰 수 | 중앙값 리뷰 수 | 평균 Steam 평점 |
|---|---|---|---|---|---|
| 일반 출시 (Normal Launch) | $360,000 | $613 | 711 | 14 | 72% |
| EA 진입 (Early Access) | $263,937 | $847 | 676 | 14 | 69% |
| 1.0 졸업 | $523,000 | $2,847 | 1,287 | 35 | 75% |

표면적으로 보면 1.0 졸업 게임이 매출·리뷰·평점 모두에서 압도적이고, EA 진입 단계조차 일반 출시보다 중앙값 매출이 약간 높다.

다만 저자는 평균과 중앙값의 격차에 즉시 주의를 환기한다. Steam은 승자에게 너무나 강하게 가시성을 몰아주기 때문에 평균이 중앙값을 크게 끌어올린다. 매출 요약에서는 보통 평균 대신 중앙값을 사용해야 한다.

## VGInsights 비교 표 — 100+ 리뷰만

저자는 여기에 더해 "100개 이상 리뷰가 달린 게임만" 한 번 더 추려 본다. 100이라는 숫자에 이론적 근거는 없고, 단지 "취미 개발자(hobbyist)"를 걷어낸 결과를 보고 싶다는 통계 위생 차원이다.

| 출시 유형 (100+ 리뷰) | 평균 추정 매출 | 중앙값 추정 매출 | 평균 리뷰 수 | 중앙값 리뷰 수 | 평균 Steam 평점 |
|---|---|---|---|---|---|
| 일반 출시 | $1,900,000 | $43,500 | 3,709 | 369 | 82% |
| EA 진입 | $1,300,000 | $62,828 | 3,200 | 372 | 78% |
| 1.0 졸업 | $1,600,000 | $77,000 | 3,900 | 486 | 80% |

이 단계에서 그림이 흔들린다.

- <strong>평균 매출</strong>: 일반 출시(190만 달러) > 1.0 졸업(160만 달러) > EA 진입(130만 달러). 즉, 진지하게 출시한 게임만 보면 일반 출시 경로가 평균 매출에서 가장 높다.
- <strong>중앙값 매출</strong>: 1.0 졸업($77,000) > EA 진입($62,828) > 일반 출시($43,500). 즉 "전형적인" 게임으로 좁히면 EA 경로의 우위가 살아남는다.
- <strong>평점</strong>: 일반 출시가 82%로 EA·1.0보다 일관되게 높다.

저자의 표현 그대로 옮긴다.

> When I strip the data down to just the "real" games it is a little more ambiguous as to whether the Early Access or the Normal launch path is better.

## 1.0이 일반 출시보다 약간 더 좋은 이유 — 세 가지 가설

저자는 1.0 졸업 게임이 일반 출시보다 약간 더 잘 되는 이유로 세 가지를 든다.

1. <strong>두 번의 이메일 폭격</strong>. 일반 출시는 위시리스트 이메일을 한 번 받고 끝이다. EA 게임은 EA 출시 시점에 한 번, 1.0 졸업 시점에 또 한 번 위시리스트 이메일이 발송된다. 공짜로 받는 가시성이 두 배다. 저자는 이걸 EA의 가장 큰 마케팅 이점으로 꼽는다.
2. <strong>완성도와 커뮤니티</strong>. EA를 거친 게임은 1.0 시점에 더 다듬어져 있고 커뮤니티가 단단해서 New & Trending 진입 가능성이 높고 버그로 이탈하는 비율도 낮다.
3. <strong>생존자 편향</strong>. EA에서 망한 게임은 대부분 그 단계에서 개발이 중단된다. 우리가 1.0 통계에서 보는 게임은 "끝까지 갈 만하다고 개발자가 판단한" 게임만 추린 것이다.

세 번째 이유가 결정적이다. 1.0 졸업 라인의 빛나는 숫자에는 EA에서 사라진 다수가 빠져 있다.

## 단점 — Steam 고객의 의심

EA의 단점은 한마디로 Steam 고객이 EA를 의심한다는 것이다.

2014\~2018년의 학습 효과로 Steam 쇼퍼들은 EA 게임에 매우 회의적이다. EA로 출시하면 곧 다음과 같은 질문이 쏟아진다.

> "그 업데이트 어디 갔어요?"
> "이거 죽은 게임인가요?"
> "왜 빌드 안 올려요? 마지막 빌드 이후 8일 됐는데, 이거 죽은 거 맞죠?"

EA 출시는 사실상 두 번째 직업을 추가하는 것이다. 공식 커뮤니티 보모(community babysitter) 역할이다. 자주 dev blog를 쓰고, Discord를 관리하고, 정기적으로 빌드를 푸시해야 한다. 골방에서 조용히 만들고 싶다면 EA는 맞지 않는다.

## EA quicksand — 비대칭 위험의 본체

저자가 EA를 의심해 온 이유는 한 단어로 요약된다. <strong>quicksand(퀵샌드)</strong>다.

EA 출시 자체가 부진하면 게임은 즉시 갇힌다. 매출 없음, 나쁜 리뷰, 그리고 이미 산 사람들의 끊임없는 "왜 안 업데이트해?" 압박. 이 시점에서 개발자에게 남는 선택지는 셋뿐이다.

1. <strong>게임을 버린다.</strong> 다음 작품을 내면 "저거 그 게임 안 끝낸 사람이잖아" 낙인이 따라붙는다.
2. <strong>대충 마무리해서 1.0 출시한다.</strong> "버그투성이에 너무 짧다"는 평가가 쏟아진다.
3. <strong>자비를 들여 끝까지 간다.</strong> 시장에 맞지 않는 게임에 매몰비용과 기회비용을 동시에 쏟는다.

세 선택지 모두 평판과 재정에 손해다. EA 출시 한 번의 실패가 영구적으로 따라붙는 negative 리뷰로 굳어지는 것 — 이게 EA 경로의 진짜 비용이다. 평균 숫자로는 보이지 않는 이 꼬리 위험이 EA를 일반 출시보다 비대칭적으로 위험하게 만든다.

## 두 가지 EA 함정 — 자금 조달과 피드백

저자는 두 가지 잘못된 EA 진입 사유를 명시적으로 단언한다.

### 1. 돈 때문에 EA에 가지 마라

2014년 EA 도입 직후 Valve가 성공한 EA 개발자들과 진행한 라운드테이블에서 나온 권고가 그대로 인용된다.

> One of the recommendations was, you should never choose the Early Access route because of money. The scenario they caution against is where your financial runway has ended and the game isn't done, and you hope that the Early Access release will fund the rest of development. That strategy won't work.

자금이 떨어져 가는데 EA 매출로 나머지 개발비를 충당하겠다는 전략은 거의 항상 실패한다. 그리고 실패한 자리에서 EA quicksand가 시작된다.

### 2. EA 출시는 베타가 아니라 진짜 출시다

두 번째 함정은 더 흔한 오해다. "가시성이 안 나오는데 EA로 한번 띄워 보자"는 발상이다.

> They don't realize that the game's EA launch is their launch. You still need to get \~7,000 wishlists, you still need to try to get in popular upcoming. You still need to try your best during Steam Next Fest. Don't do an EA launch because your visibility is flat and you hope that an EA launch will improve your game's marketing. It will not. EA Launch is the culmination of your visibility, not a catalyst.

요약하면 EA 출시에서 필요한 마케팅 체크리스트는 일반 출시와 같다. <strong>위시리스트 \~7,000개</strong>, <strong>Popular Upcoming 진입 시도</strong>, <strong>Steam Next Fest 참여</strong> 모두 EA에서도 동일하게 요구된다. EA는 가시성을 만들어 주는 촉매가 아니라 그동안 쌓아 온 가시성을 소진하는 정점이다.

세 번째로 저자가 덧붙이는 함정은 "피드백을 받고 싶어서 EA에 가는" 경우다. 피드백이 필요하면 베타 테스트, 사용자 테스트, 데모를 돌려라. EA로 피드백을 받겠다는 결정은 quicksand에 머리부터 다이빙하는 것과 같다.

## 가장 흥미로운 지점

이 글의 핵심 가치는 두 표를 나란히 놓고 본 사람만 읽을 수 있는 메시지에 있다.

전체 게임을 묶어 보면 EA 경로(EA $847 / 1.0 $2,847)가 일반 출시($613)를 중앙값에서 명백히 앞서지만, 100+ 리뷰 게임으로 좁히면 일반 출시의 평균 매출($1.9M)이 EA($1.3M)를 추월하고 1.0($1.6M)에도 근접한다. 이 변화는 EA의 "유리한 평균"이 상당 부분 1.0까지 도달한 생존자에서 온다는 사실을 시각화한다.

내가 보기에 진짜 메시지는 "EA가 더 좋다/나쁘다"가 아니라 <strong>위험 분포가 다른 길</strong>이라는 것이다. EA 경로는 두 번의 이메일 폭격과 1.0 졸업 시 New & Trending 재진입이라는 상방을 제공하지만, 출시를 망치면 영구 negative 리뷰가 게임 페이지에 박제된다. 일반 출시는 한 번에 끝나기 때문에 실패해도 quicksand가 없다. 평균 한 줄로는 이 비대칭이 보이지 않는다 — 그래서 저자가 굳이 두 표를 모두 보여 주는 것이다.

또 하나 인상 깊은 지점은 저자가 자신의 직관을 데이터로 뒤집는 데 정직하다는 점이다. "I may have been wrong about Early Access, it might secretly be great"라고 글 초입에서 인정하고, 그러면서도 quicksand 논의를 통해 자신의 원래 직관(첫 작품에는 일반 출시를 권한다)을 다시 단단히 세운다. "데이터가 직관을 약간 수정시킨 만큼만" 입장을 옮긴 글이다.

## 출처

- <strong>저자</strong>: Chris Zukowski (zukalous), How To Market A Game
- <strong>발행</strong>: 2023년 7월 27일 (2023년 8월 21일 갱신)
- <strong>데이터</strong>: vginsights.com (CSV) + ChatGPT-4 Code Interpreter

[^strong-2023]: <strong>원문</strong>: <https://howtomarketagame.com/2023/07/27/should-you-do-early-access/>
[^estimating-2023]: <strong>이어지는 글</strong>: [Estimating Early Access success based on your EA launch numbers (2023-08-21)](https://howtomarketagame.com/2023/08/21/estimating-early-access-success/)
