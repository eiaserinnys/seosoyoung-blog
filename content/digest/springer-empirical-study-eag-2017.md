---
title: "An empirical study of early access games on the Steam platform"
date: 2026-05-06T15:40:00+09:00
tags: ["Steam", "얼리액세스", "인디게임", "학술 논문"]
categories: ["게임"]
summary: "Lin·Bezemer·Hassan이 2016년 3월 시점 Steam 게임 8,025종을 크롤링해 1,182개 EAG(15%)를 동정하고, EA 단계와 1.0 단계 사이의 업데이트 빈도·리뷰 참여율·평점·토론 활동을 통계적으로 비교한 첫 대규모 실증 연구다. 핵심 발견은 \"EA 단계의 평균 평점이 1.0 이후보다 유의하게 높다\"이며, 긍정 평점률은 EA 길이·업데이트 빈도와 무관하다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Dayi Lin·Cor-Paul Bezemer·Ahmed E. Hassan이 2017년 7월에 *Empirical Software Engineering*(Springer)에 발표한 학술 논문으로, Steam의 얼리액세스(EA) 모델을 1,182개 EAG 표본으로 본격 분석한 최초의 대규모 실증 연구다.[^springer-link]
2. <strong>EAG의 88%가 인디 게임</strong>이며, 가장 인기 있는 EAG는 *Killing Floor 2*로 owner 약 2,888만 명. EA 단계에서 개발자는 더 자주 업데이트(중간값 11일 vs 15일)하고 플레이어는 토론에 더 많이 참여하지만 리뷰는 덜 남긴다.
3. 가장 강한 발견은 <strong>EA 단계의 평균 평점이 1.0 이후보다 통계적으로 유의하게 높다</strong>는 것이다(Cliff's δ=0.454, medium effect). 그리고 EAG의 89%가 EA 단계에서 더 높거나 동일한 긍정 평점률을 받는다. 이 긍정 평점률은 <strong>EA 기간 길이·업데이트 빈도와 상관이 없다</strong>(Spearman -0.06, 0.01).

## 자료의 정체

- <strong>저자</strong>: Dayi Lin, Cor-Paul Bezemer, Ahmed E. Hassan (Software Analysis and Intelligence Lab(SAIL), Queen's University).[^sail-2017]
- <strong>발표</strong>: *Empirical Software Engineering* Volume 23, pages 771–799 (2018). 온라인 선공개 2017-07-08.
- <strong>DOI</strong>: 10.1007/s10664-017-9531-3.[^s10664-doi]
- <strong>분석 대상</strong>: 2016년 3월 7일 시점 Steam 스토어의 모든 게임 8,025종, 그 중 EAG 1,182종.

이 논문은 EA 모델을 단일 사례 보고가 아닌 *플랫폼 전체 표본*으로 통계 분석한 최초의 학술 작업이다. 이후 EA 관련 업계 글들이 인용·전제로 삼는 토대 자료다.

## 연구 질문 세 개

논문은 세 개의 RQ로 구성된다.

> <strong>RQ1</strong>: What are the characteristics of the early access model?
> Steam 게임의 15%가 EA 모델을 사용한다. EA는 주로 개인이나 소규모 스튜디오의 인디 게임 출시 통로로 작동한다. 다만 EA가 개발 자금 조달을 보장하지는 않는다.[^fair-use]

> <strong>RQ2</strong>: How do developers and players of EAGs interact with the Steam platform?
> 개발자는 EA 단계에서 더 자주 업데이트한다. 플레이어는 EA 단계에서 리뷰는 덜 남기지만 토론 게시물은 더 많이 작성한다.

> <strong>RQ3</strong>: How tolerant are players of the quality of EAGs?
> 플레이어는 EA 단계의 게임 품질에 대해 더 관용적이다. 89%의 EAG가 EA 단계에서 동일하거나 더 높은 긍정 평점률을 받는다. 그리고 이 관용도는 EA 기간 길이와 상관이 없으므로, 개발자는 EA 기간을 부담 없이 결정해도 된다.

## 표본과 방법

데이터 수집 기간은 2016년 3월 7일–19일이다. 데이터 출처는 다음과 같다.

- <strong>Steam Store</strong>: 제목, 개발사·퍼블리셔, 태그·장르, EA 상태.
- <strong>Steam Community</strong>: 리뷰, 토론 게시물, news/release-note 채널.
- <strong>Steam Spy</strong>: owner 수 추적치(2015-03-20부터).
- <strong>Steam DB</strong>: 가격 변동 이력(2014-11-27부터).

EAG 동정 기준은 보수적이다.

- <strong>현재 EAG</strong>: 스토어 페이지에 EA 표시가 있는 게임.
- <strong>former EAG</strong>: "early access review" 태그가 붙은 리뷰가 하나라도 존재하는 게임. 이는 그 게임이 EA를 거쳤다는 최소 신호다.

릴리스 노트 추출은 정밀도 89%, 재현율 87%로 검증되었다(383개 무작위 샘플, 95% 신뢰, 5% 오차 한계).

전체 데이터셋은 다음과 같다.

| 항목 | 수 |
|---|---:|
| 분석한 게임 | 8,025 |
| EAG | 1,182 (현재 786, former 396) |
| EA 종료일·시작일 모두 식별 가능한 former EAG | 227 |
| 전체 리뷰 | 12,338,364 |
| EA 리뷰 | 1,564,574 |
| former EAG 토론 게시물 | 801,128 |

## RQ1 — EA 모델의 특성

### Steam 전체의 15%

분석 시점 기준 Steam 게임의 <strong>15%(1,182/8,025)</strong>가 EA 모델을 사용했다. 이는 단순 누적이 아니라 SEARP(Steam Early Access Release Program, 2013-03-20 도입) 시작 후 약 3년이 지난 시점의 누적치다.

![Fig. 2 — SEARP 시작 이후 월별 EAG 출시 수. 어두운 부분은 데이터 수집 시점에 여전히 EA 단계인 게임, 밝은 부분은 EA를 졸업한 게임](/images/springer-empirical-study-eag-2017/fig2-eag-releases-over-time.png)

EAG 절대 수는 2013년 64개에서 2015년 485개로 <strong>660% 증가</strong>했다. 같은 기간 월별 Steam 출시작 대비 EAG 비율도 5%에서 20%로 올랐다.

### 졸업률 34% — 1.0까지 도달하는 게임은 절반도 안 된다

표본 시점에 전체 EAG 중 <strong>34%(396/1,182)</strong>가 EA를 졸업했다. 다만 2014년 이전부터 EA에 있던 게임만 보면 졸업률은 50%로 올라간다. (Walker 2014가 보고한 25%보다 다소 높다.)

### EAG의 88%는 인디

장르 분포(상위 10개, 다중 태그 가능)를 보면 EAG와 non-EAG 모두 인디가 가장 많지만 비중은 크게 다르다.

| 장르 | EAG % | non-EAG % |
|---|---:|---:|
| Indie | <strong>88.49</strong> | 56.45 |
| Early Access | 66.24 | – |
| Action | 63.62 | 47.44 |
| Adventure | 42.22 | 41.78 |
| Strategy | 34.09 | 24.30 |
| RPG | 30.71 | 19.26 |
| Simulation | 29.44 | 17.14 |
| Multiplayer | 27.24 | 15.84 |
| Singleplayer | 25.04 | 31.02 |
| Casual | 19.54 | 29.27 |

EA는 사실상 인디 모델이다. 4,927개 고유 개발자 중 대부분(3,814)은 EAG를 출시한 적이 없고, EAG를 만든 1,113개 스튜디오 중 95%(1,062)는 EAG를 단 1개만 보유한다.

### owner 분포 — 중간값 11,270, 최대 2,888만

EAG의 owner 수 중간값은 11,270명이다. 25% 이상이 47,950명이 넘는 owner를 가지며, 3%(43개 EAG)는 100만 명 이상이다. 가장 인기 있는 EAG는 <strong>Killing Floor 2</strong>로 owner <strong>28,878,959명</strong>(~2,888만 명)이다.

### EA 기간 — 중간값 225일, 최장 929일

EA 진입과 졸업 시점이 모두 식별된 227개 former EAG의 EA 기간 분포는 다음과 같다.

![Fig. 6 — former EAG의 EA 단계 일수 분포. 70%가 1년 이내에 졸업한다](/images/springer-empirical-study-eag-2017/fig6-ea-duration-distribution.png)

- <strong>중간값 225일</strong>, 70%가 1년(365일) 이내 졸업.
- 최장 EA: *Prison Architect* 929일.
- 최단 분석 사례: *Parcel* 26일, *RONIN* 34일.
- 800일 이상 EA에 머문 게임의 토론을 직접 확인해 추출한 장기화 사유는 (a) 인력 부족, (b) 특정 스킬(예: UI 아트) 부재, (c) 예산 추정 실패, (d) 개발자 자체 기준이 너무 높음 — 네 가지로 요약된다.

## RQ2 — 개발자·플레이어와 플랫폼의 상호작용

### 업데이트 빈도 — EA에서 더 자주 (11일 vs 15일)

![Fig. 7 — 업데이트 빈도 분포. EA 단계 중간값 11일, 졸업 후 15일. Cliff's δ=-0.207 (small)](/images/springer-empirical-study-eag-2017/fig7-update-frequency.png)

- EA 단계 업데이트 간격 중간값 <strong>11일</strong>, 졸업 후 <strong>15일</strong>.
- Wilcoxon signed-rank p=5.833e-10, Cliff's δ=-0.207 (small effect).
- 63%의 EAG가 EA 단계에서 더 자주 업데이트한다. 3%는 동일.
- 단, 졸업 후 12개월간 업데이트 활동은 50% 미만의 EAG가 활발히 유지한다 — "졸업 후 방치"가 적지 않다.

### 리뷰 참여 — EA에서 *덜* 남긴다

owner 대비 리뷰 비율을 보면 65%의 EAG가 EA 단계에서 동일하거나 더 적은 리뷰 활동을 보인다. Wilcoxon p=0.009이지만 Cliff's δ=-0.039로 effect는 무시할 수준(negligible)이다.

저자들의 해석: EA 플레이어는 게임이 미완성임을 알고 있으므로 굳이 리뷰를 남기지 않을 수 있다. 또한 Steam은 EA 리뷰와 1.0 리뷰를 평점 산정에서 동등하게 다루므로, 플레이어가 EA에서 리뷰를 남기는 데 추가 동기가 없다.

### 토론 — EA에서 *훨씬* 더 활발 (Cliff's δ=0.304)

![Fig. 11 — 토론 참여율 분포. EA 단계 중간값 0.04, 졸업 후 0.02. Cliff's δ=0.304 (small)](/images/springer-empirical-study-eag-2017/fig11-discussion-participation.png)

owner 1인당 토론 게시물 수의 중간값은 EA 단계 <strong>0.04</strong>, 졸업 후 <strong>0.02</strong>. 즉 EA 단계에서 두 배다. Wilcoxon p=4.918e-16, Cliff's δ=0.304.

66%의 EAG가 EA 단계에서 더 높은 토론 참여를 받고, 15%는 동일하다. 합치면 <strong>81%</strong>가 EA 단계에서 토론 참여가 동등 이상이다.

저자들의 해석: 리뷰 점수는 EA·1.0이 합산되므로 동기가 약하지만, 토론은 개발자에게 직접 피드백을 전달하는 통로다. 미완성 게임에 영향을 미치고 싶은 EA 플레이어가 토론으로 몰린다.

## RQ3 — 플레이어는 EA에 더 관용적이다 (핵심 발견)

### EA 단계의 평균 평점이 1.0 이후보다 유의하게 높다

이 논문에서 가장 강한 발견이다.

![Fig. 12 — 긍정 평점률 분포. EA 단계 중간값 88%, 졸업 후 69%. Cliff's δ=0.454 (medium)](/images/springer-empirical-study-eag-2017/fig12-positive-review-rate.png)

- 긍정 평점률 중간값: EA 단계 <strong>88%</strong>, 졸업 후 <strong>69%</strong>.
- Wilcoxon p<2.2e-16, Cliff's δ=0.454 (medium effect — 본 논문에서 가장 큰 효과 크기).
- <strong>89%의 EAG가 EA 단계에서 동일하거나 더 높은 긍정 평점률을 받는다</strong>(88%는 더 높음, 1%는 동일).

저자들의 해석은 단순하다 — <strong>플레이어가 EA의 미완성을 더 관용적으로 받아들인다.</strong> 개발자가 EA에서 더 자주 업데이트한다는 사실(RQ2)이 이 관용을 일부 설명하지만, 통계적으로는 업데이트 빈도와 평점 사이의 직접 상관이 약하다(다음 절 참조).

### EA 기간·업데이트 빈도와 긍정 평점률은 상관 없다

가장 정책적으로 중요한 결과다.

| 변수 1 | 변수 2 | Spearman ρ |
|---|---|---:|
| EA 기간 길이 | 긍정 평점률 | <strong>-0.06</strong> |
| EA 단계 업데이트 빈도 | 긍정 평점률 | <strong>0.01</strong> |

즉 EA를 길게 끌어도, 자주 업데이트해도 평점이 좋아지지 않는다. 저자들의 정책 제언:

> Developers update a game more frequently in its early access stage. Players post less reviews, however players have more discussion posts in the early access stage.
>
> Game developers can use the early access model as a method for eliciting early feedback and more positive reviews to attract additional new players. Developers can also <strong>determine their release schedule without worrying about the length of the early access stage and the game update frequency</strong>.

EA 기간과 업데이트 빈도는 평점에 큰 영향이 없으므로 개발자가 자유롭게 결정해도 된다. 다만 EA 모델 자체가 더 긍정적인 리뷰를 유도하는 효과는 있다.

## 가격 정책 — EAG의 47%는 EA에서 무료 또는 더 싸다

추가 분석에서 저자들은 가격 정책을 EA의 동기를 추론하는 단서로 활용한다(Fig. 13). 95개 EAG(24%)는 평생 무료(F2P), 나머지 중 가격 정보가 충분한 300개에서:

- <strong>48.3%(145개)</strong>는 EA와 1.0 가격이 동일.
- <strong>30.3%(91개)</strong>는 1.0에서 가격을 올림.
- <strong>21.3%(64개)</strong>는 1.0에서 가격을 내림. 이 중 6개는 1.0에서 완전 무료화.

요약하면 <strong>EAG의 47%(F2P 24% + 1.0에서 가격 인하/유지 23%)는 EA 단계에서 무료 또는 더 싸다</strong> — 자금 조달보다 피드백을 우선시한 가격 설계다. 반대로 16%는 EA 단계에 프리미엄을 매겼는데 이들은 EA를 자금 조달 통로로 명시적으로 활용한다.

## 실패 사례 — Spacebase DF-9의 다섯 교훈

저자들은 EA 실패의 첫 공개 사례인 *Spacebase DF-9*을 단일 케이스 스터디로 분석한다.

- 2013-10-15 SEARP 출시 → 2014-10-27 1.0으로 *급작스레* 졸업 → 2014-11-21 12명 정리해고 → 2014-12-16 사실상 개발 포기.
- 2,598개 부정 리뷰(<strong>79%</strong> 부정)가 영구히 따라붙음.

저자들이 추출한 다섯 교훈:

1. EA를 *주된 자금 조달 통로*로 쓰는 것은 위험하다.
2. 콘텐츠가 부족한 상태에서 SEARP에 너무 일찍 진입하지 말라.
3. 약속과 계획을 명시적으로 진술하라.
4. 게임 포기는 스튜디오 전체의 평판을 손상시킨다.
5. 문제와 계획 변경을 *제때* 커뮤니케이션하라.

저자들의 종합 결론: EA에서 플레이어 참여는 양방향 통로다 — 플레이어가 게임에 영향을 미치고 싶어하므로 그들의 정서적 투자를 인정하고 응답해야 한다.

## Threats to Validity

저자들은 다음 한계를 명시적으로 인정한다.

- <strong>인과 vs 상관</strong>: 본 연구는 EA가 더 높은 평점을 *야기한다*고 증명하지 않는다. EA 구매자가 더 관용적인 자기 선택 효과(self-selection)일 수도 있다.
- <strong>오너 수의 추정성</strong>: Steam Spy는 샘플 크롤링 기반 추정치이므로 실제 판매와의 편차를 모른다. 다만 분석 시점에서 가용한 최선의 데이터다.
- <strong>릴리스 노트는 자발적</strong>: 일부 개발자는 노트를 게시하지 않으므로 업데이트 빈도는 하방 편향이 있다.
- <strong>실패 사례는 단일</strong>: 5.2절의 다섯 교훈은 *Spacebase DF-9* 한 사례에서 도출됐다. 이는 분석 시점에 *공개적으로 문서화된 유일한 EA 실패*였다.
- <strong>외적 타당도</strong>: 결론은 Steam EAG에 한정되며 다른 플랫폼에 일반화되지 않는다(다만 Steam은 PC 플랫폼 중 가장 크다).

## 가장 흥미로운 지점

<strong>EA 단계 평균 평점이 1.0 이후보다 유의하게 높다는 발견</strong>(Cliff's δ=0.454, medium)이다. 효과 크기로는 본 연구에서 단연 가장 크다. 다른 비교(업데이트 빈도, 토론 참여)는 모두 small effect에 머무는 데 비해 평점 차이만이 medium까지 올라간다.

이 발견은 업계 데이터 분석들이 보여주는 "1.0 출시가 EA 첫 달의 0.7배~0.4배"라는 매출 후퇴 현상의 *심리적 메커니즘*을 설명하는 짝이 된다. 같은 게임에 대해 동일한 플레이어 풀이 EA에서는 88% 만족이라고 평가하다가, 1.0에서는 69%로 떨어진다 — 같은 콘텐츠 같은 사람이라도 "정식 출시"라는 라벨이 평가 기준을 끌어올린다.

저자들의 해석은 보수적이다. "관용적이다"라고 표현할 뿐 인과를 주장하지 않는다. 하지만 <strong>긍정 평점률이 EA 기간·업데이트 빈도와 무관</strong>(Spearman -0.06, 0.01)하다는 후속 결과는 흥미롭다. 이는 "더 잘 만들면 점수가 오른다"는 직관이 EA 단계에서는 거의 작동하지 않는다는 뜻이다 — 점수의 절반은 게임 품질이 아니라 *EA라는 라벨*이 만든다.

이 점이 사실이라면 개발자에게 시사하는 바는 단순하지 않다. EA는 더 좋은 점수를 자동으로 부여하지만, 그 점수는 1.0에 들고 가기 어렵다. 1.0 졸업 시점에 평점이 떨어질 것을 예측하고 마케팅 동선을 짜야 한다. 이 논문은 그 트레이드오프의 *수치적 증거*를 처음으로 제시했다.

## 출처

- 저자: Dayi Lin, Cor-Paul Bezemer, Ahmed E. Hassan (Software Analysis and Intelligence Lab(SAIL), Queen's University)
- 게재지: *Empirical Software Engineering* 23(2), 771–799 (2018). 온라인 선공개 2017-07-08.

[^s10664-doi]: DOI: [10.1007/s10664-017-9531-3](https://doi.org/10.1007/s10664-017-9531-3)
[^springer-link]: 원문(Springer 페이월드): <https://link.springer.com/article/10.1007/s10664-017-9531-3>
[^sail-2017]: 저자 사본(SAIL Lab PDF): <https://sailresearch.github.io/sail-website/data/pdfs/EMSE2017_AnEmpiricalStudyOfEarlyAccessGamesOnTheSteamPlatform.pdf>
[^fair-use]: 본문 인용 그림은 모두 위 PDF에서 발췌했으며, 학술 인용 목적의 fair use로 사용한다.
