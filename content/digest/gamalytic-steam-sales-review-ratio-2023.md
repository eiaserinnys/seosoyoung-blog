---
title: "What makes people review your game? A deep dive into the Steam's sales/review ratio"
date: 2026-05-06T15:01:10+09:00
tags: ["Steam", "게임 데이터", "Gamalytic", "리뷰 비율"]
categories: ["게임"]
summary: "Steam의 sales/review 비율을 9개 변수(연도·가격·할인·평점·장르·플레이타임·인구·청중·인기)로 분해한 Gamalytic의 2023년 분석. 평점과 비율의 관계가 단순한 양의 상관이 아니라 U자형이라는 점이 핵심이다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Gamalytic이 자체 판매량 추정과 공개 데이터를 결합해 Steam의 "리뷰 한 건당 판매 수(sales/review 비율)"가 어떤 요인에 어떻게 반응하는지 9개 변수로 분해한 분석이다.
2. 가장 두드러지는 발견은 평점과 비율의 관계가 단조롭지 않다는 것이다. 90%+ 긍정 평점 게임은 리뷰당 약 30판, 70% 평점은 약 60판, 60% 미만은 다시 약 30판으로 떨어지는 U자형이 관찰된다.
3. 결론은 단호하다. 비율이 게임마다 너무 크게 흩어지므로 리뷰로 매출을 추정해서는 안 된다는 것이다.

## 분석 대상 변수

저자는 다음 9개 변수가 sales/review 비율에 어떤 영향을 주는지 차례로 살핀다.

- 출시 시점(리뷰 작성 시점)
- 가격
- 긍정 리뷰 비율(평점)
- 장르
- 플레이타임
- 인구통계(국가)
- 청중 오버랩
- 리뷰 수(게임의 인기도)
- AAA 대 인디

분석은 Simon Carless(2020), VG Insights(2021)의 선행 연구를 확장하는 위치에 있다.

## 출시 시점 — 2019년의 절벽

가장 잘 알려진 사실부터 정리한다. sales/review 비율은 게임이 출시된 해보다 **리뷰가 작성된 해**에 더 강하게 의존한다. 2019년에 Steam이 플레이어에게 리뷰를 남기도록 프롬프트하기 시작하면서 비율이 절반으로 잘려 나갔다.

![연도별 중간값 sales/review 비율 — 2019년 Steam 리뷰 프롬프트 도입을 기점으로 비율이 절반으로 감소했다](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/year-cliff.png)

그 이후로도 비율은 매년 조금씩 떨어지는 추세인데, 이는 부분적으로 게임 수명 주기 효과로 보인다. 게임이 새로울 때 리뷰를 더 많이 남기고, 시간이 흐르면 할인이 잦아지고 충동 구매가 늘면서 리뷰를 남기지 않는 구매자가 누적된다.

![출시 후 경과 시간에 따른 리뷰 multiple — 시간이 지날수록 리뷰 남기는 비율이 감소한다](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/time-since-release.png)

## 가격과 할인

가격이 낮을수록 리뷰당 판매 수가 많다. <strong>무료 게임은 유료 게임 대비 거의 2배의 sales/review 비율</strong>을 보인다.

![가격대별 평균 sales/review — 저가 구간에서 비율이 크게 올라간다](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/price.png)

가격보다 더 강한 변수는 할인이다. **할인폭이 큰 게임일수록 sales/review 비율이 뚜렷하게 높다.** 번들에 포함된 게임에도 같은 패턴이 적용된다. 세일에 산 플레이어는 리뷰를 남길 확률이 낮다.

![할인율과 sales/review 비율 — 할인이 깊어질수록 리뷰 남기지 않는 구매자 비율이 커진다](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/discount.png)

극단의 사례로 저자는 한 인디 개발자가 트위터에 공개한 사례를 인용한다. 가격·할인 조건의 조합에 따라 어떤 게임은 1,000명당 단 1개의 리뷰(1000:1)밖에 받지 못하기도 한다.

## 평점과 sales/review — U자형 비선형 패턴 (★)

이 자료의 핵심 발견이다. 평점과 비율의 관계는 단순한 양의 상관이 아니다.

![긍정 리뷰 비율과 sales/review 비율 — 70% 부근에서 비율이 정점에 달하고 양 끝에서 다시 낮아지는 U자형 패턴](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/positive-reviews-ushape.png)

- **90%+ 긍정 평점**: 리뷰당 약 30판
- **약 70% 긍정 평점**: 리뷰당 약 60판 (정점)
- **60% 미만 긍정 평점**: 리뷰당 약 30판 (다시 하락)

저자가 제시하는 메커니즘은 비대칭 동기다.

> Unless there are some things about the game that really annoy the players, the percentage of people who write negative reviews is constant. However, the percentage of those who write positive reviews is much higher for games that players enjoy.

정리하면 이렇다. **부정 리뷰를 남기는 비율은 거의 일정한 상수**이고, **긍정 리뷰를 남기는 비율은 게임이 즐거울수록 훨씬 높다**. 이 두 동기의 합이 평점에 따라 다르게 작동하기 때문에, 호평 게임은 리뷰가 많이 쌓여 sales/review 비율이 낮게(즉 리뷰당 판매 수가 적게) 보이고, 평점이 낮은 게임은 부정 리뷰의 절대 분모가 작아 다시 비율이 낮아진다. 중간(70% 부근) 구간에서 정점이 형성되는 까닭이다.

## 장르

Steam 태그(태그 위치로 가중)와 sales/review 비율 간에는 일정한 상관이 있다.

![Steam 태그별 sales/review multiples — 태그 위치 가중치를 적용한 장르별 비율](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/tag-multiples.png)

장르와 평점 자체의 상관도 존재한다. 다만 **리뷰를 남기는 비율을 결정하는 요인으로서 장르의 비중은 의외로 크지 않다**고 저자는 정리한다.

## 플레이타임

플레이타임이 길수록 리뷰를 남길 확률이 올라간다. 단순하지만 강한 신호다.

![플레이타임과 sales/review 비율 — 플레이타임이 길수록 리뷰 비율이 높아진다](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/playtime.png)

## 인디 대 AAA, 그리고 인기

Multiple(=리뷰 한 건당 판매 수)이 가장 낮은 그룹은 양극단이다. 작고 니치한 인디, 그리고 초인기·논쟁적 AAA. 그 사이의 "인기 인디·AA" 구간이 가장 높은 비율을 보인다.

저자가 든 사례를 그대로 옮긴다.

> Bravery and Greed(Team17 퍼블리싱)는 sales/review 비율이 100 부근으로 매우 높다. 반면 ELDEN RING은 약 1,000만 카피 / 50만 리뷰 — 비율이 약 20에 불과하다.

화제성이나 논쟁이 큰 게임은 관여도가 높은 만큼 리뷰가 더 많이 쌓이고, AAA는 가격이 높고 할인 빈도가 낮은 점도 비율을 끌어내린다.

![퍼블리셔 유형별 sales/review 중간값 — 인디·AA가 가장 높고 AAA·소형 인디가 낮다](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/publisher-indie-aaa.png)

리뷰 수 자체로 본 인기도와의 관계도 같은 방향이다. 리뷰가 매우 적거나 매우 많은 양극단에서 multiple이 낮다.

![리뷰 수와 평균 multiple — 양극단에서 multiple이 낮은 U자에 가까운 곡선](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/number-of-reviews.png)

## 청중 오버랩

저자가 "가장 큰 영향을 주는 요인"으로 꼽는 변수다. 청중이 비슷한 게임끼리 sales/review 비율도 비슷하게 묶인다.

- Bravery and Greed (높은 비율) ↔ Rogue Heroes, Backpack Hero (높은 비율)
- ELDEN RING (낮은 비율) ↔ Dark Souls III, Monster Hunter: World, Sekiro (낮은 비율)

장르나 가격보다 청중 오버랩이 비율을 더 잘 설명한다는 시사다. "이 게임을 사는 사람들"의 리뷰 작성 성향이 어느 정도 일관되게 게임 사이에 옮겨 다닌다는 것이다.

## 인구통계

아시아권 플레이어가 서구권보다 리뷰를 약간 더 자주 남기는 경향이 관찰된다. 다만 저자 본인이 단서를 단다. Steam이 아시아 시장에 늦게 침투했고 시간이 흐르며 비율이 떨어진다는 사실을 이미 보았기 때문에, 인구통계 효과의 일부는 시점 효과의 그림자다. **통계적으로 유의하지 않다**고 정리한다.

## 결론 — 리뷰로 매출을 추정하지 마라

전체 분포는 다음과 같다.

![Steam sales/review 비율 분포 — 게임 간 편차가 매우 크다](https://img.seosoyoung.eiaserinnys.me/images/gamalytic-steam-sales-review-ratio-2023/distribution.png)

저자의 결론은 한 줄이다.

> The ratio of sales to reviews varies a lot between games and is hard to predict. **You shouldn't rely on reviews to judge game sales**, because the percentage of people who leave reviews is very unpredictable.

리뷰는 여전히 커뮤니티 형성, 구매 의사결정 보조, 개발자 피드백이라는 본래의 가치가 있다. 다만 **매출 추정 도구로서의 신뢰성은 낮다**는 것이 이 분석의 결론이다.

## 가장 흥미로운 지점

U자 패턴의 메커니즘 해석이 가장 인상 깊다. "잘 만든 게임일수록 리뷰가 더 많이 달린다"는 직관은 절반만 맞다. 정확히는 **부정 리뷰는 일정한 상수처럼 깔리고, 긍정 리뷰만 게임의 품질에 따라 가변한다**는 비대칭 모형이다.

이 모형이 맞다면 sales/review 비율 자체가 평점의 대리 지표가 될 수 없다는 결론이 따라 나온다. 비율이 50인 게임은 평점 70%일 수도 있고 30%일 수도 있다 — 둘은 같은 비율을 만들지만 정반대의 시장 신호다. 리뷰 수와 sales 추정을 한 변수로 압축해 의사결정에 쓰는 일이 얼마나 위험한지를, 이 한 장의 그래프가 보여준다.

## 출처

Gamalytic, "What makes people review your game? A deep dive into the Steam's sales/review ratio" (2023-07-23).

원문: <https://gamalytic.com/blog/a-deep-dive-into-the-steam-review-ratio>
미러(Game Developer): <https://www.gamedeveloper.com/marketing/what-makes-people-review-your-game-a-deep-dive-into-the-steam-s-sales-review-ratio>

이미지는 모두 원문에서 인용했으며, Game Developer 미러의 contentstack CDN에서 다운로드해 블로그 정본에 포함했다.
