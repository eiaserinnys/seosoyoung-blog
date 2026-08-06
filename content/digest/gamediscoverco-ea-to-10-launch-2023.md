---
title: "Will your Steam 1.0 launch outpace your Early Access start?"
date: 2026-05-06T15:10:01+09:00
tags: ["Steam", "얼리액세스", "게임 출시", "데이터 분석"]
categories: ["게임"]
summary: "GameDiscoverCo와 Gamalytic이 1,500개 이상의 Steam EA 졸업작 데이터를 분석한 결과, 중간값 1.0 출시는 EA 첫 3개월의 0.7배에 그친다. 그러나 분포가 매우 넓어 상위 5%는 5배 이상을 기록하고, EA 기간이 길수록 1.0 배수는 낮아지는 음의 상관이 관찰된다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. GameDiscoverCo의 Simon Carless가 Gamalytic의 Strale와 함께 2015\~2023년 Steam 얼리액세스(EA) 졸업작 1,500여 종을 분석하여, EA 첫 3개월 매출 대비 1.0 첫 3개월 매출 배수의 분포를 정리한 자료다.
2. <strong>중간값 EA→1.0 비율은 약 0.7배</strong>로 1.0이 EA보다 살짝 덜 팔린다. 하지만 분포의 폭이 매우 넓어 상위 25%는 1.34배, 상위 10%는 3.34배, 상위 5%는 5.53배에 달한다.
3. EA 기간이 길수록 1.0 배수가 낮아지는 음의 상관이 있다. Carless의 해석은 "긴 EA 동안 위시리스터를 할인으로 흡수하기 때문이며 꼭 나쁜 일은 아니다"이다.

## 이상적인 1.0 — Hades 사례

Carless가 글의 도입에서 인용한 "fantasy 1.0"의 표본은 Supergiant의 ARPG <strong>Hades</strong>다. Hades는 Epic Games Store 독점 후 2019년 12월에 Steam EA로 진입했고, 2020년 9월 1.0으로 졸업하면서 폭발적으로 팔렸다. 글의 추정으로는 Steam에서만 LTD 600만 장 이상이 팔렸다 (GameDiscoverCo 추정치).

![Hades Steam 리뷰 곡선 — 2020년 9월 1.0 출시 시점에 리뷰 수가 급격히 치솟는다](/images/gamediscoverco-ea-to-10-launch-2023/hades-review-curve.jpeg)

(2020년 11\~12월의 추가 리뷰 점프는 Steam Awards 투표 영향이라고 Carless는 주석을 단다.)

다만 이 정도 곡선은 명백한 outlier다. 글의 본론은 "그렇다면 *중간값* 게임은 어떤가?"라는 질문에서 출발한다.

## 표본과 방법론

* **표본**: 2015\~2023년에 Steam에서 EA로 출시했고 1.0 졸업까지 도달한 게임 중 **1,500여 종**.
* **비교 단위**: EA 첫 3개월 추정 판매 단위 vs 1.0 첫 3개월 추정 판매 단위.
* **데이터 출처**: GameDiscoverCo의 Data Fellow인 Gamalytic.

> The median Early Access to 1.0 ratio hovers around 0.7x (going down slightly as games get bigger!) for all sizes of game.

즉 EA 첫 3개월에 1만 장 판 게임은 1.0 첫 3개월에 약 7천 장 더 파는 것이 중간값이다. EA 전체 기간 동안 추가로 판매되는 분량은 별도 계산이며, 위 비율은 어디까지나 "각 단계의 첫 3개월"만을 비교한 것이다.

![모든 매출 구간에서 중간값 EA→1.0 비율은 약 0.7배](/images/gamediscoverco-ea-to-10-launch-2023/median-ea-to-10-ratio.png)

게임이 클수록 중간값 비율이 약간 더 낮아지는 경향도 같은 차트에서 확인된다.

## 분포의 폭 — 중간값만 보면 절반의 그림이다

Carless가 강조하는 진짜 발견은 분포 자체다. 중간값(50번째 백분위)만 보면 1.0이 EA보다 못한 듯하지만, 분포의 양쪽 끝은 매우 멀리 떨어져 있다.

EA 전체 기간 누적 판매 **2만\~10만 단위** 구간을 예시로 들면 다음과 같다.

| 백분위 | EA→1.0 첫 3개월 배수 |
|---|---|
| 하위 25% | 0.35배 |
| 상위 25% | 1.34배 |
| 상위 10% | 3.34배 |
| **상위 5%** | **5.53배** |

![EA 전체 누적 판매 구간별 백분위 분포 — 매출 구간이 커질수록 상단의 outlier가 더 극단적으로 벌어진다](/images/gamediscoverco-ea-to-10-launch-2023/distribution-by-sales-band.jpeg)

매출 구간이 커질수록 상단의 outlier가 더 극단적이다. 같은 차트에서 추출한 상위 5% 배수는 다음과 같다.

| EA 누적 판매 구간 | 상위 5% 배수 |
|---|---|
| 1k\~5k | 4.46배 |
| 100k\~500k | 7.52배 |

큰 게임일수록 상위 5%의 점프가 더 크다는 의미다. Carless는 이 분포를 두고 다음과 같이 정리한다.

> You **might want to think of 'the middle 50%' (from 25th to 75th percentile)** as your anchor for visualizing things. And **that's a range with 1.0 from about 0.35x to 1.35x of Early Access**.

즉, 일반적으로 "기대할 수 있는" 범위는 0.35\~1.35배의 중앙 50%이고, 그 바깥의 outlier는 분명히 존재하지만 자기 게임이 거기 들어갈 거라 가정해서는 안 된다는 것이다.

## EA 기간 ↔ 1.0 배수 — 음의 상관

마지막 분석은 EA 체류 기간이 1.0 배수에 미치는 영향이다.

![EA 체류 기간이 길수록 1.0 첫 3개월의 EA 대비 배수가 낮아진다](/images/gamediscoverco-ea-to-10-launch-2023/ea-length-vs-multiplier.png)

> the longer you are in Early Access, the lower the 1.0 unit multiplier compared to EA.

Carless의 해석은 위시리스트 흡수다. EA 기간이 길수록 잠재 구매자(위시리스터)들에게 할인·콘텐츠 업데이트로 구매를 유도할 기회가 많아지고, 그 결과 1.0 시점에는 "남아 있는" 위시리스터가 줄어든다는 것이다. Carless는 이를 부정적인 신호로 보지 않는다.

> There's one likely and obvious reason for this — the longer you are in Early Access, the more you'll be tempting your existing wishlisters to buy, via discounting and other methods. (Not a negative, in our view.)

또한 그는 1.0 첫 3개월 배수가 낮다고 해서 총 매출이 낮다는 뜻은 아니라고 짚는다. 3\~4년의 긴 EA 끝에 1.0을 낸 게임이 1년 미만의 짧은 EA 게임보다 *총* 매출은 더 높을 수 있다. 다만 1.0 첫 3개월 ‘피크’는 더 작아진다는 정도의 이야기다.

## 가장 흥미로운 지점

내가 이 글에서 가장 흥미롭게 본 부분은 "중간값과 분포의 폭이 따로 논다"는 사실 그 자체다. 중간값만 보면 "1.0은 EA보다 못 판다(0.7배)"는 비관적 결론으로 가지만, 같은 데이터의 상위 5%는 <strong>5배 이상</strong>의 점프를 만든다. 두 진술 모두 같은 표본에서 나온 사실이다.

또 하나 인상적인 것은 Carless가 EA 기간과 1.0 배수의 음의 상관을 두고 *부정적 신호로 해석하지 않는다*는 점이다. "장기 EA → 1.0 배수 감소"는 마치 게임이 식어가는 것처럼 보이지만, 그 ‘감소분’의 정체가 사실은 EA 기간 동안 이미 흡수된 위시리스트라는 해석은 1.0 시점의 숫자만으로 EA 전략을 평가할 수 없다는 뜻이기도 하다. EA→1.0 배수는 ‘EA가 얼마나 일을 잘했는지’의 음의 지표일 수도 있는 것이다.

## 출처

발행: GameDiscoverCo, 2023-11-08
저자: Simon Carless (with Strale of [Gamalytic](https://www.gamalytic.com))
원문: <https://newsletter.gamediscover.co/p/will-your-steam-10-launch-outpace>

본문 차트 4종은 원문에서 인용했으며, 데이터·차트의 권리는 GameDiscoverCo와 Gamalytic에 있다.
