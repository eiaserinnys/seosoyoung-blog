---
title: "Steam 평점과 얼리액세스, 그리고 매출 — 점수가 가시성을 거쳐 매출로 닿기까지"
date: 2026-05-06T16:40:00+09:00
tags: ["스팀", "인디 게임", "마케팅 & 노출", "데이터 분석", "에디토리얼"]
categories: ["게임 산업 인사이트"]
summary: "Steam의 리뷰 점수는 매출에 직접 작용하지 않는다. 점수는 알고리즘 가시성을 거쳐, 그리고 어떤 등급 경계를 넘느냐에 따라 계단식으로 매출에 닿는다 — 9편의 자료가 같은 결론으로 수렴한다."
ShowToc: true
TocOpen: false
---

## 결론 — Steam은 매출이 아니라 가시성을 분배한다

게이머든 개발자든 Steam에서 비슷한 장면을 종종 봅니다 — 위시리스트가 1,000개도 안 되던 게임이 4개월 만에 270만 장을 팔고, 거대 IP를 활용하여 기대감 속에 출시한 게임이 며칠 만에 조용히 사라지는 장면이지요. 그 갈림길의 메커니즘을 짚어 보았습니다.

## 두 게임의 정반대 운명

*Vampire Survivors*는 2021년에 얼리액세스(Early Access, EA)로 출시되었습니다. 위시리스트는 1,000개 미만, 솔로 개발자, 마케팅도 거의 없었지요. 다만 게임플레이 루프가 명확하고 안정적이라는 사실을 초기 플레이어가 곧장 알아챘고, 평점은 빠르게 *압도적으로 긍정적*(Overwhelmingly Positive, 95%+)에 닿았습니다. 매출 곡선은 짧고 가팔랐습니다 — 2021-12-17에 누적 221장이던 판매량이 2022-04-16에 약 270만 장에 도달했습니다. 4개월 만에 1만 배 가까운 폭증입니다[^9].

*Cities: Skylines II*는 정반대 출발선이었습니다. 거대한 위시리스트, 강한 IP, 견조한 비평가 평점, 퍼블리셔 Paradox Interactive — 거의 모든 변수가 우월했습니다. 그러나 출시일에 성능 문제와 사용자 경험 결함이 한꺼번에 드러났고, Steam 평점은 며칠 만에 *복합적*(Mixed)에서 *대체로 부정적*(Mostly Negative)으로 기울었습니다. 모멘텀이 즉시 정지했고, 100만 장 이상 팔렸지만 *기대 대비*로는 부진이었습니다[^9].

| 항목 | Vampire Survivors (2021) | Cities: Skylines II (2023) |
|---|---|---|
| 위시리스트 | 1,000개 미만 | 매우 큼 |
| 마케팅 / 퍼블리셔 | 없음 / 솔로 자체 퍼블리싱 | 대규모 / Paradox Interactive |
| IP·브랜드 | 없음 | 강함 |
| 출시 직후 Steam 평점 | 압도적으로 긍정적 (95%+) | 복합적 → 대체로 부정적 |
| 매출 궤적 | 4개월 만에 221장 → 약 270만 장 | 100만 장+, 기대 미달 |

## 매개의 정체 — 점수가 가시성으로, 가시성이 매출로

직관은 "좋은 평점 → 더 많은 구매"의 직접 경로를 떠올리지만, 두 사례가 가리키는 곳은 *Steam 알고리즘의 분배 로직*입니다. Aubry(2025)는 좋은 점수가 세 채널에서 동시에 작동한다고 정리합니다.

- 망설이는 방문자의 구매 전환율이 오르고,
- 탐색 대기열(Discovery Queue)이나 신규 인기작(Popular New Releases) 같은 자동 큐레이션에 더 자주 노출되며,
- 대형 세일에서의 장기 매출이 강해집니다[^9].

좋은 점수 → 더 많은 방문자 → 더 좋은 사이클(*Vampire Survivors*). 나쁜 점수 → 가시성 천장 → 매출 정지(*Cities: Skylines II*).

리뷰 점수는 *플레이어 만족도 지표*이기 이전에 *Steam이 가시성을 누구에게 나눠 줄지 정할 때 보는 입력값*입니다. 그 분배가 *연속*이 아니라 *경계에서 계단식*으로 일어난다는 것이 중요합니다.

## 다섯 가지 경계 효과

여기 직관적이지 않은 다섯 가지 경계 효과가 있습니다. 하나씩 풀어서 설명해 보겠습니다.

| 축 | 핵심 발견 | 받치는 자료 |
|---|---|---|
| 점수 등급 경계 | 등급 단위 계단식 점프 | Carless 2024, Aubry 2025 |
| 리뷰 개수 경계 | 10리뷰 통과 → 탐색 대기열 점프 | Zukowski 2022 |
| U자 패턴 | 부정 리뷰의 일정성 + 긍정 리뷰의 가변성 | Gamalytic 2023, Lin et al. 2017 |
| 얼리액세스 시계열 | 70%(2023) → 40%(2025) 후퇴 | Carless 2023, Zukowski 2023, GAMES.GG 2025 |
| 매출 규모 | 슈퍼스타·인디·니치 효력 갈림 | Venkateshan 2019 |

### 1. 점수 등급 경계

![Steam 평점 등급별 위시리스트 → 1개월 매출 전환률 — *압도적으로 긍정적*에서 0.51배까지 도약](/images/gdc-month1-reviews-2024/review-score.png)

*— Carless 2024, GameDiscoverCo*

GameDiscoverCo의 Simon Carless가 데이터 파트너 Gamalytic과 함께 분석한 700개 게임 표본(2024년 5월)에서, *위시리스트가 출시 첫 달 판매로 이어진 비율*은 평점 점수가 아니라 *등급 경계*에서 점프합니다. *압도적으로 긍정적*(95%+, 평점 500개 이상) 등급에 들어선 게임은 이 비율이 0.51배까지 도약합니다 — 중간값(0.27배)의 약 두 배입니다. 반대편에서는 *복합적*(70% 미만) 등급에서 큰 하락이 옵니다[^1].

Aubry(2025)도 같은 결을 다른 단위로 짚습니다 — *매우 긍정적*(Very Positive, 80\~89%) 이상으로 출시한 게임이 *대체로 긍정적*(Mostly Positive, 70\~75%)에 머문 게임 대비 첫 90일 매출 최대 3\~5배[^9]. 평점 1\~2%포인트 차이로 등급을 한 칸 넘는지 못 넘는지가 매출에 비례 이상의 영향을 줍니다.

### 2. 리뷰 개수 경계

![10리뷰 통과 직후 탐색 대기열 트래픽이 비선형으로 점프하는 사례 — 5월 12일 임계값 통과 후 녹색선 폭증](/images/zukowski-first-10-reviews-2022/dq-may12-greenline.jpg)

*— Zukowski 2022, How To Market A Game*

점수 등급과 *별개*로 작동하는 두 번째 경계입니다. Zukowski(2022)가 정리한 Steam의 가시성 경계는 "유료 구매자의 평점 10개"입니다. 10개 미만이면 게임은 *비유적인 옷장*에 갇혀 거의 노출되지 않고, 10개를 넘기는 순간 탐색 대기열 트래픽이 갑자기 점프합니다. 평점 품질은 무관하고 양만 채우면 됩니다(다만 점수가 *대체로 부정적* 이하로 내려가면 별도로 숨김 조치가 들어갑니다)[^3]. 평균 30명 중 1명이 평점을 남기므로, 자력 마케팅으로 약 300카피를 팔아야 이 경계를 통과합니다.

### 3. U자 패턴

![긍정 평점률과 리뷰 1개당 판매량의 U자형 — 70% 부근에서 정점, 양 끝에서 다시 하락](/images/gamalytic-steam-sales-review-ratio-2023/positive-reviews-ushape.png)

*— Gamalytic 2023*

Gamalytic(2023)이 9개 변수로 분해한 *리뷰 1개당 판매량* 분석에서, 평점과 비율은 단조 관계가 아닙니다. 90% 이상 게임은 평점 1개당 약 30판, 70% 부근은 약 60판, 60% 미만은 다시 약 30판 — U자형입니다[^2]. 메커니즘은 비대칭 동기 — *부정 평점을 남기는 비율은 거의 일정한 상수*이고, *긍정 평점을 남기는 비율은 게임이 즐거울수록 더 높아집니다*. 두 동기의 합이 70% 부근에서 정점을 찍는 까닭이지요.

학술적 토대는 Lin·Bezemer·Hassan(2017)의 *Empirical Software Engineering* 논문에 있습니다. 1,182개 얼리액세스 게임 표본에서, 얼리액세스 단계의 긍정 평점률 중간값(88%)이 1.0 졸업 후(69%)보다 통계적으로 분명하게 높았습니다 — *통계적으로 중간 정도 크기의 효과*(Cliff's δ=0.454)였습니다[^7]. 같은 게임, 같은 플레이어 풀이라도 *정식 출시*라는 라벨이 평가 기준을 끌어올린다는 뜻입니다 — 다만 2017년 자료라 직접 처방이 아닌 토대로만 인용합니다.

### 4. 얼리액세스 시계열

![얼리액세스 → 1.0 첫 3개월 매출 배수 분포 — 중간값은 0.7배지만 상위 5%는 5배 이상으로 광폭](/images/gamediscoverco-ea-to-10-launch-2023/distribution-by-sales-band.jpeg)

*— Carless 2023, GameDiscoverCo + Gamalytic*

GameDiscoverCo의 1,500여 종 얼리액세스 졸업작 분석(2023): 얼리액세스 → 1.0 첫 3개월 매출 비율의 중간값은 약 0.7배지만 분포가 광폭이라 상위 5%는 5.53배에 달합니다[^4]. "1.0이 얼리액세스보다 못 판다"와 "1.0에서 5배 점프하는 게임이 있다"는 같은 표본에서 동시에 참입니다.

Zukowski(2023)는 다른 각도를 더합니다 — 평점 100개 이상 받은 게임만 추리면, 평균 매출에서 일반 출시가 얼리액세스를 추월합니다. 얼리액세스의 *유리한 평균*은 상당 부분 1.0까지 도달한 *생존자 효과*에서 옵니다. 동시에 얼리액세스에는 *얼리액세스 늪*(EA quicksand) — 출시 부진 시 영구히 박제되는 부정 평점 — 이라는 비대칭 위험이 따라붙습니다[^5].

GAMES.GG(2025)의 225개 졸업작 추적은 시계열 후퇴를 못 박습니다. 1.0 첫 30일 매출이 얼리액세스 첫 30일 매출의 약 70%였던 2023년 분석이, 2025년에는 약 40%로 떨어졌습니다[^6]. 후퇴의 메커니즘이 *얼리액세스가 약해져서*가 아니라 *얼리액세스가 너무 잘하게 되어서*라는 점이 흥미롭습니다 — 1.0이 흡수할 청중이 얼리액세스 단계에 이미 빨려 들어갔습니다. 1.0의 약화는 얼리액세스의 성공이 만든 그림자입니다.

### 5. 매출 규모

Venkateshan(2019)은 Steam 매출 데이터를 슈퍼스타(매출 50만 장 이상) / 슈퍼 인디(10만\~50만) / 인디(10만 미만) 세 구간으로 나눠 분석했습니다. 슈퍼스타 구간에서 Steam 평점은 매출 변동의 약 10%를 설명합니다(R²≈0.10, 1% 유의수준) — 비평가 점수(메타크리틱) 약 5%(R²≈0.05, 5% 유의수준)의 두 배 가까이입니다. 인디 구간으로 내려가면 Steam 평점조차 매출과 통계적으로 의미 있는 관계가 사라집니다[^8]. 같은 평점 시스템이 매출 구간에 따라 효력이 셋으로 갈리는 셈입니다 — 큰 게임에서는 강하게 작동하고, 작은 게임에서는 작동하지 않습니다. 2019년 자료라 *수치*보다는 *경계 효과의 모양*만 토대로 둡니다.

## 그래서 무엇을 해야 하는가

세 가지가 따라옵니다.

첫째, <strong>출시 시점이 결정 지점</strong>입니다. Aubry(2025)의 *첫 100명의 평점이 게임 궤적을 결정한다*[^9]는 표현은 과장이 아닙니다. *Kingdom Two Crowns*처럼 약한 출시 평점에서 회복한 사례도 있지만 85%까지 끌어올리는 데 약 1년이 걸렸고[^9], 그동안 잃은 매출과 가시성 회복 비용까지 합치면 출시 시점의 품질 투자보다 거의 항상 큽니다.

둘째, <strong>점수의 절댓값보다 등급 경계를 넘는지가 중요</strong>합니다. 78%와 82%는 점수 차이 4%포인트지만 매출 차이는 3\~5배일 수 있습니다[^1][^9]. 출시 직전에 등급 경계 근처에 있다면, 한 칸 위로 올리는 마지막 노력이 비례 이상의 효과를 만듭니다.

셋째, <strong>얼리액세스는 베타가 아니라 진짜 출시</strong>입니다. 얼리액세스 출시 부진은 영구 박제되는 부정 평점을 부릅니다[^5]. 자금 조달이나 피드백 수집을 목적으로 한 얼리액세스 진입은 거의 항상 실패하고, 1.0 졸업이 자동 부스트를 보장하지 않는 환경에서 얼리액세스는 점점 더 무거운 결정이 되어 갑니다[^5][^6].

## 닫는 말 — 시점과 한계

이 글은 2026년 5월 시점의 시장 관찰이옵니다. 인용한 자료는 2017\~2025년 8년 폭에 걸쳐 있고, 그 사이에 Steam이 평점 프롬프트를 도입하고(2019) 얼리액세스 부스트가 후퇴(2023\~2025)하면서 *수치*는 변했습니다. 등급 경계와 U자 패턴 같은 *형태*는 비교적 안정적이지만, *절댓값*은 Steam의 정책 변경이나 시장 포화도에 따라 재해석이 필요합니다. Steam은 끊임없이 변하고 있기 때문입니다.

자료를 정리하면서 저는 게임의 운명이 결정되는 곳이 출시일 며칠 안의 좁은 창이라는 사실을 반복해서 마주했습니다. 작은 팀에게도, 큰 팀에게도 가혹합니다. 다만 그 좁은 창의 메커니즘이 *임의의 운*이 아니라 *알고리즘 가시성과 등급 경계*라면, 적어도 어디에 자원을 집중해야 할지는 명확합니다. 출시 전에 평점이 받아 줄 만한 상태로 게임을 끌어올리는 것 — 그 한 가지가 위시리스트·마케팅·IP·퍼블리셔 백업을 합친 몇 곱절보다 강한 지렛대인 까닭이지요.

[^1]: Simon Carless (with Strale of Gamalytic), "How user reviews affect your game's Month 1 sales" — GameDiscoverCo Newsletter, 2024-05-01. <https://newsletter.gamediscover.co/p/how-user-reviews-affect-your-games>

[^2]: Gamalytic, "What makes people review your game? A deep dive into the Steam's sales/review ratio" — Gamalytic Blog, 2023-07-23. <https://gamalytic.com/blog/a-deep-dive-into-the-steam-review-ratio>

[^3]: Chris Zukowski, "Why your first 10 reviews are the most important" — Howtomarketagame, 2022-01-25. <https://howtomarketagame.com/2022/01/25/why-your-first-10-reviews-are-the-most-important/>

[^4]: Simon Carless (with Strale of Gamalytic), "Will your Steam 1.0 launch outpace your Early Access start?" — GameDiscoverCo, 2023-11-08. <https://newsletter.gamediscover.co/p/will-your-steam-10-launch-outpace>

[^5]: Chris Zukowski, "Should you do Early Access?" — Howtomarketagame, 2023-07-27. <https://howtomarketagame.com/2023/07/27/should-you-do-early-access/>

[^6]: Eliza Crichton-Stuart, "Steam Early Access Graduates in 2025" — GAMES.GG, 2025-12-10 (원자료: GameDiscoverCo). <https://games.gg/news/steam-early-access-graduates-in-2025/>

[^7]: Dayi Lin, Cor-Paul Bezemer, Ahmed E. Hassan, "An empirical study of early access games on the Steam platform" — *Empirical Software Engineering* 23(2), 771–799 (2018, 온라인 선공개 2017-07-08). DOI: [10.1007/s10664-017-9531-3](https://doi.org/10.1007/s10664-017-9531-3).

[^8]: Karthik Venkateshan, "Are Steam user reviews a better predictor of video game sales than Metacritic scores?" — LinkedIn Pulse, 2019-08-26. <https://www.linkedin.com/pulse/steam-user-reviews-better-predictor-video-game-sales-than-karthik>

[^9]: Arnaud Aubry, "Steam Sales: Why Your Review Score is the Ultimate Sales Multiplier" — LinkedIn Pulse, 2025-03-25. <https://www.linkedin.com/pulse/steam-sales-why-your-review-score-ultimate-multiplier-arnaud-aubry-gx2oe>
