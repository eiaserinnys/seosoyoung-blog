---
title: "Are Steam user reviews a better predictor of video game sales than Metacritic scores?"
date: 2026-05-06T15:43:00+09:00
tags: ["스팀", "Metacritic", "리뷰 시스템", "플랫폼 경제"]
categories: ["다이제스트"]
summary: "Karthik Venkateshan이 2019년에 Steam 유저 리뷰와 Metacritic 점수를 매출(units sold)과 회귀시켜 비교한 분석. Superstar 타이틀에선 유저 리뷰가 Metacritic을 누르고 더 강한 매출 설명력을 보이지만, Indie에선 유저 리뷰조차 매출과 유의미한 관계를 잃어버린다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Karthik Venkateshan(EA Sports FC 라인 프로듀서)이 2019년 8월에 LinkedIn에 게재한 독립 분석으로, Steam 타이틀의 유저 리뷰 점수와 Metacritic 점수를 매출(units sold)과 회귀시켜 신호 효과를 비교한다.
2. 결론은 매출 규모에 따라 갈린다. <strong>Superstar 타이틀(>500k)</strong>에서는 Steam 유저 리뷰가 매출의 약 10%(1% 유의수준)를, Metacritic이 약 5%(5% 유의수준)를 설명하여 유저 리뷰가 우세하다. 반면 <strong>Indie 타이틀(<100k)</strong>에서는 유저 리뷰조차 매출과 유의미한 관계가 없다.
3. Valve의 "유저 리뷰 전면 노출" 전략은 Superstar에는 정확히 맞지만 Niche·Indie에는 빈 구멍이라는 함의가 따라온다. 저자는 Niche 타이틀용 별도 리뷰 시스템(예: 속성 기반 yes/no 질문) 설계를 제안한다.

## 자료의 정체

- <strong>저자</strong>: Karthik Venkateshan. Electronic Arts(EA)에서 EA Sports FC 라인 프로듀서로 근무. 글머리에 "이 분석은 독립적으로 수행되었으며 모든 견해는 내 개인의 것"이라는 명시적 면책을 단다.
- <strong>발행</strong>: 2019년 8월 26일, LinkedIn Pulse.
- <strong>형식</strong>: 자체 표본 수집 + 회귀 분석. 학술 논문이 아니라 업계 종사자의 데이터 에세이에 가깝다.
- <strong>주제</strong>: 온라인 마켓플레이스의 신뢰·평판 시스템으로서 Steam의 리뷰 메커니즘을 평가. 큐레이팅되지 않은 유저 점수와 큐레이팅된 Metacritic 점수가 매출에 끼치는 신호 효과를 비교한다.

## 표본 설계

저자는 Steam 매출 데이터(전수)와 직접 수집한 리뷰·Metacritic 점수를 결합해 다음 세 구간으로 나눠 각 구간에서 무작위 100개 관측치를 모은다.

- <strong>Superstar</strong>: 매출 500k 이상. 거의 모든 타이틀이 Metacritic 점수를 가진다.
- <strong>Super Indie</strong>: 매출 100k\~500k. Metacritic이 있는 타이틀은 약 35%에 불과하다.
- <strong>Indie</strong>: 매출 100k 미만. 대부분 Metacritic 점수가 없다.

세 구간을 분리한 이유 두 가지를 본문에서 명시한다.

1. 마케팅 예산 차이로 500k 미만 타이틀은 대부분 주요 매체 리뷰를 받지 못해 Metacritic 점수 자체가 생성되지 않는다.
2. 유저 리뷰 점수의 분포가 구간별로 다르게 나타나는지 확인해야 했다.

100개 관측치는 각 구간의 모집단 정보를 추론하기에 충분한 표본 크기로 본다.

## Step 1 — 유저 리뷰 vs Metacritic 분포 비교 (Superstar 한정)

먼저 Superstar 구간에서 두 점수의 분포 자체를 비교한다.

- <strong>평균</strong>: 유저 리뷰 평균 > Metacritic 평균.
- <strong>분산</strong>: 유저 리뷰가 더 변동성이 크다 — 즉, 유저들 사이에 선호 이질성이 더 크다는 의미.
- <strong>방향성</strong>: 매출 500k 이상 타이틀 중 <strong>70% 이상</strong>이 Metacritic보다 유저 리뷰 점수가 더 높다.

분산 동일성 검정(Levene's test)에서 p-value 1.32%로 5% 유의수준에서 귀무가설을 기각한다. 두 점수의 분산은 통계적으로 다르며, 유저 리뷰 쪽이 더 이질적이다.

이어 평균 차이를 paired t-test(양 표본 분산 비등)로 본다. p-value는 단측 0.02%, 양측 0.04%로 1% 유의수준에서도 평균이 같다는 귀무가설을 기각한다. t-Stat이 음수여서 평균적으로 Metacritic이 유저 리뷰보다 보수적이라는 결론이 따른다.

> "Metacritic scores are more conservative than user review scores for superstar game titles on Steam." (저자 결론 1)

## Step 2 — 매출 설명력 회귀 (★ 핵심)

여기가 자료의 가장 결정적 지점이다. 저자는 종속변수로 log(sales), 독립변수로 각각 Metacritic 점수와 유저 리뷰 점수를 두고 단변량 회귀를 두 번 돌린다.

| 회귀 (Superstar 구간) | 독립변수 | 유의수준 | R² (매출 설명력) |
|---|---|---|---|
| 1 | Metacritic 점수 | 5% | <strong>약 5%</strong> |
| 2 | 유저 리뷰 점수 | 1% | <strong>약 10%</strong> |

> "Uncurated user review scores are more significant and better correlated with sales data for Superstar titles than highly curated professional Metacritic scores." (저자 결론 2)

저자는 이 결과를 "Steam이 유저 리뷰를 전면에 띄우고 1차 품질 신호로 사용하는 전략에 대한 실증적 뒷받침"으로 해석한다. 큐레이션 비용이 거의 없는 점수가 비싼 큐레이션을 거친 점수보다 매출 설명력이 두 배 가까이 높다는 결과는 직관에 반한다.

## Step 3 — Niche 구간으로 내려가면 무너지는 신호

같은 모형을 Indie 구간에 적용하면 결과가 뒤집힌다.

| 회귀 (Indie 구간, <100k 매출) | 독립변수 | 유의수준 | R² |
|---|---|---|---|
| 단변량 | 유저 리뷰 점수 | 10% 수준에서도 유의하지 않음 | — |

> "User review scores generated on Steam for Indie titles have no significant relationship with sales." (저자 결론 3)

Superstar에서 가장 강한 매출 신호였던 유저 리뷰가, Indie에서는 매출과의 관계가 통계적으로 사라진다.

Super Indie 구간(100k\~500k)은 그 사이에 있다.

- 단변량 회귀(독립변수: 유저 리뷰 점수): 10% 유의수준, R² 약 3%. 유의성과 설명력이 모두 약화.
- 다변량 회귀(독립변수: 유저 리뷰 점수, has Metacritic, has Metacritic × user score):
  - 유저 리뷰 점수는 5% 유의수준, 상호작용항 has Metacritic × user score는 10% 유의수준.
  - has Metacritic 단독 더미는 10% 수준에서도 유의하지 않다 — 즉 Metacritic 점수의 *존재 자체*는 매출에 영향을 주지 않는다.
  - 상호작용항의 부호가 음수이고 절댓값이 user score 계수보다 커서, <strong>유저 리뷰 점수가 매출을 끌어올리는 효과는 Metacritic이 *없는* 타이틀에서만 작동</strong>한다는 해석이 가능하다.

저자는 이 패턴을 두 가지 가설로 풀이한다. (a) Niche와 Superstar 경계에 걸친 "기대 매출 미달 Superstar"가 분포를 비뚤어뜨릴 수 있다. (b) 매체가 사전 리뷰하기로 선택한 Super Indie의 일부는, 매체 평가자의 동질적 선호 때문에 상대적으로 박한 점수를 받는 경향이 있다.

> "For Niche titles on the Steam's platform, evidence calls for the design of an alternate review system for Niche titles as this presents an amazing opportunity to increase its platform revenues." (저자 결론 4)

## 네 가지 결론을 한 표로

| # | 구간 | 발견 |
|---|---|---|
| 1 | Superstar | Metacritic은 보수적, Steam 유저 점수는 더 자유롭다(평균↑, 분산↑) |
| 2 | Superstar | 유저 리뷰 R² ≈ 10% (1% 유의) > Metacritic R² ≈ 5% (5% 유의) |
| 3 | Indie | Steam 유저 리뷰가 매출과 *유의미한 관계 없음* |
| 4 | Niche 전반 | 평점 시스템 자체가 잘 동작하지 않음 — 별도 시스템이 필요하다 |

## Niche용 대안 리뷰 시스템 — 저자의 제안

저자는 Niche 타이틀용으로 단일 긍/부정 라벨 대신 <strong>속성별 yes/no 질문</strong>을 누적 수집하는 시스템을 제안한다. Google Reviews가 식당 평점에 사용하는 방식과 유사하다.

예시 질문:

- 이 게임을 플레이하면서 즐거웠는가?
- 게임이 *나쁜 의미로* 반복적이었는가?
- 음악이 마음에 들었는가?
- 혁신적이거나 독창적이라고 느꼈는가?
- 기술적으로 완성도가 높았는가?
- 비주얼 아트가 마음에 들었는가?
- 스토리가 있었는가?

이렇게 모은 데이터를 구매 의사결정 화면에서 "이 게임이 혁신적이라고 느낀 유저 90%" 같은 형태로 노출하면, 노벨티에 더 너그러운 구매자가 기술적 흠집을 감수하고도 매칭될 수 있다는 가설이다. Niche 타이틀의 핵심 자산은 *유저 선호 이질성* 그 자체이므로, 단일 점수 대신 그 이질성을 활용하는 매칭이 플랫폼 매출을 늘릴 수 있다고 본다.

## 가장 흥미로운 지점

이 분석이 흥미로운 지점은 *결론*이 아니라 *비선형성의 모양*이다. 같은 리뷰 시스템이 매출 구간에 따라 효력이 셋으로 갈린다 — Superstar(강하게 작동) → Super Indie(약하게 작동) → Indie(작동하지 않음). 평점이 매출을 잘 예측하지 못한다는 진술은 평균을 보면 절반만 맞다. 어느 매출 구간을 보느냐에 따라 같은 데이터에서 정반대 결론이 나온다.

이 발견은 같은 인사이트 아티클의 1·2라운드 자료가 보여 준 다른 두 비선형성과 결을 같이한다.

- <strong>1라운드(Gamalytic)</strong>: 평점과 sales/review 비율 간 *임계값/U자형 비선형성*. 70% 부근이 정점, 양 끝에서 다시 내려간다.
- <strong>2라운드(Zukowski/GameDiscoverCo)</strong>: EA → 1.0 매출 분포의 *시계열 비선형성*과 EA quicksand의 비대칭 위험.
- <strong>3라운드(이 자료)</strong>: <strong>매출 규모에 따른 비선형성</strong>. 같은 평점 신호도 Superstar에선 강하고 Indie에선 사라진다.

세 자료를 묶으면 평점-매출 관계는 단일한 함수가 아니라 *세 축에서 모두 비선형*이다. 신호 시스템 설계는 이 셋 중 어느 한 축만 다룬 모형으로는 부족하다는 게 누적된 함의다.

또 하나 짚어 둘 만한 지점은 표본 한계다. 저자는 무작위 100개 관측치를 인정하면서도 그 한계를 굳이 감추지 않는다. R² 10%라는 숫자를 "유저 리뷰가 매출을 결정한다"가 아니라 "큐레이션되지 않은 점수가 큐레이션된 점수보다 두 배 가까이 잘 설명한다"는 *상대 비교*로 사용한다. 절댓값이 아니라 상대 비교에 무게를 싣는 해석은 표본 100개에서 가장 정직한 사용 방식이다.

## 출처

- 저자: Karthik Venkateshan (Line Producer, EA Sports FC at Electronic Arts)
- 발행: 2019년 8월 26일, LinkedIn Pulse
- 원문: <https://www.linkedin.com/pulse/steam-user-reviews-better-predictor-video-game-sales-than-karthik>

원문에는 분포 그래프, 회귀 결과 표, 구간별 유저 리뷰 분포 비교 차트가 포함되어 있다. 본 다이제스트 작성 시점에 LinkedIn 원본의 이미지 토큰이 만료되어 있었고 Internet Archive 스냅샷에도 이미지가 캐시되어 있지 않아, 본문 텍스트의 수치를 표로 재구성하는 방식으로 옮겼다.
