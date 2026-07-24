---
title: "구글은 황금알을 낳는 거위를 죽이고 있는가 — 어느 대형 광고주의 고발과 팩트체크"
date: 2026-07-24T12:30:00+09:00
tags: ["경제·금융", "구글", "디지털 광고", "독점", "AI"]
categories: ["다이제스트"]
summary: "월 50만 달러 이상을 구글 광고에 쓰는 광고주가 '구글이 AI 투자를 위해 황금알 낳는 거위를 죽이고 있다'며 세 가지를 고발했다. 2차 가격 경매 폐지, exact match의 붕괴, 예산 상한 2배 초과다. 세 주장을 구글 공식 문서와 반독점 재판 기록으로 하나씩 검증한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. 월 50만 달러 이상을 구글 검색광고에 집행해 온 광고주 Max Anderson(@MaxAnderson)이 2026년 7월 23일 X에 올린 스레드다. 검색 볼륨이 LLM에 잠식되어 줄어드는 와중에 구글이 매출 성장을 억지로 만들어내느라 광고주에게 적대적인 수법을 쓰고 있다고 고발했다.
2. 고발은 세 가지다. (1) 오랫동안 유지하던 2차 가격 경매를 조용히 없애고 입찰가 상한까지 최대한 과금한다, (2) exact match로 정확히 지정해도 "close variant"라는 이름으로 무관한 검색어 수천 개에 광고를 붙이고 과금하며 끌 수 없다, (3) 일 예산 상한을 2배까지 넘겨 지출한다.
3. 검증 결과는 갈린다. 고발 2는 사실, 고발 3은 대체로 사실이되 뉘앙스가 있고, 고발 1은 과장이다. 다만 "구글이 검색광고 가격을 은밀히 올려 왔다"는 큰 줄기는 2023년 미국 반독점 재판에서 실제로 드러났다.

## 누가, 무엇을 말했나

Anderson은 자신을 "수년간 매달 50만 달러 넘게 구글 광고를 집행해 온 사람"으로 소개하며 스레드를 열었다. 그의 진단은 이렇다.

> This revenue growth in Search is artificial & extremely unhealthy for Google's business long term. (검색 부문의 이 매출 성장은 인위적이고, 장기적으로 구글 사업에 대단히 해롭다.)

배경은 LLM이다. 사람들이 검색 대신 챗봇에 질문하면서 돈이 되는 검색 쿼리가 줄어드는데, 구글은 그 구멍을 "근시안적이고 극도로 착취적이며 고객에게 적대적인" 방식으로 메우고 있다는 것이다. 그리고 스레드는 이렇게 닫힌다.

> At the alter[altar] of AI capex, Google is sacrificing the golden goose. (AI 투자라는 제단 위에서, 구글은 황금알을 낳는 거위를 제물로 바치고 있다.)

Anderson은 구글이 지난 25년간 "선의의 독점(benevolent monopoly)"을 운영했다고 표현한다. 검색에서 뽑아낸 가치가 창출한 가치의 작은 일부에 불과했고, 그 격차가 먼 미래까지의 성장 기대를 정당화했는데, 이제는 그렇지 않다는 것이다.

## 고발 1 — "2차 가격 경매가 사라졌다"

Anderson의 설명은 명확하다.

> if you bid USD 5 CPC and the next highest bidder bids USD 1 CPC, Google charged you USD 1.01 for the click ... However recently, Google silently deprecated the 2nd price auction and began charging advertisers as much as their bid and budget caps allow. (내가 클릭당 5달러를 부르고 다음 입찰자가 1달러를 부르면 구글은 1.01달러만 청구했다. 그런데 최근 구글은 2차 가격 경매를 조용히 폐기하고, 입찰가와 예산 상한이 허용하는 최대치를 청구하기 시작했다.)

**판정: 과장.** 구글 공식 문서(How the Google Ads auction works, About Ad Rank)는 2026년 현재도 검색광고의 실제 클릭당 비용이 대개 최대 입찰가보다 낮으며, 바로 아래 경쟁자를 이기는 데 필요한 최소 금액만 청구한다고 명시한다. 이것이 전형적인 GSP(Generalized Second Price) 구조다. 2019\~2021년 구글이 2차 가격에서 1차 가격으로 실제 전환한 것은 디스플레이 네트워크·애드센스·애드 매니저였고, **검색 텍스트 광고는 전환 대상이 아니었다.** Anderson이 검색과 디스플레이를 뭉뚱그린 것으로 보인다.

다만 "구글이 가격을 은밀히 올려 왔다"는 취지 자체는 근거가 있다. 2023년 미국 대 구글 반독점 재판에서 광고 담당 VP Jerry Dischler는 검색광고 경매를 여러 "가격 조절 손잡이(pricing knobs)"로 조용히 조정해 왔다고 증언했다.

- **Project Momiji**(2017): 2위 입찰가를 인위적으로 부풀려 낙찰자에게 최대 15% 더 청구.
- **RGSP**(Randomized Generalized Second Price, 2019): 상위 입찰자들의 가치가 비슷하면 순위를 무작위로 흔들어 가격을 서서히 끌어올리는 방식. Dischler는 이것이 매출을 늘린다는 점을 인정했다.
- Dischler 증언에 따르면 인상폭은 평균 5%, 특정 쿼리는 최대 10\~15%였고, 사전 고지는 없었다.

즉 "2차 가격을 없앴다"는 문자 그대로는 틀렸지만, "가격을 조용히 조작해 매출을 뽑아낸다"는 큰 그림은 법정에서 확인된 사실이다.

## 고발 2 — "exact match가 broad match가 됐다"

> even if you bid on a specific term ... using the strictest exact-match targeting settings, Google will show your ad across 1000's of unrelated keywords, labeling them as "exact match (close variant)" ... there's no ability to turn this off. (가장 엄격한 exact match를 써도 구글은 무관한 키워드 수천 개에 광고를 노출하며 "exact match (close variant)"라고 이름 붙인다. 끌 방법이 없다.)

**판정: 사실.** 구글 공식 문서(Keyword close variants)는 close variant에 "옵트아웃할 방법이 없다(There's no way to opt out)"고 직접 밝히고 있으며, close variant는 exact match를 포함한 모든 매치 타입에 기본 적용된다. 이는 오래 진행된 변화다.

| 시점 | 변화 |
|---|---|
| 2012-04 | 오탈자·변형 자동 매칭 도입 (당시엔 옵트아웃 가능) |
| 2014-08 | 옵트아웃 기능 완전 삭제 — 모든 캠페인에 변형 강제 포함 |
| 2017-03 | 어순 변경·기능어 추가/삭제까지 close variant 범위 확대 |
| 2018-09 | "동일 의미(same meaning)" 매칭 도입 — 암시어·패러프레이즈까지 |
| 2019 | 동일 의미 매칭을 phrase match·broad match modifier로 확장 |

"exact match인데 문자 그대로 일치하지 않는 검색어에 노출된다"는 현상은 2018년 이후 업계에서 광범위하게 보고됐다. Anderson의 "exact match가 broad match가 됐고, broad match는 그냥 의미 없는 스팸이 됐다"는 표현은 방향에서 과장이 아니다.

## 고발 3 — "예산 상한을 2배로 넘긴다"

> campaigns we've been running for years with USD 1,000 daily budget caps suddenly began spending USD 2,000+ per day. (수년간 일 예산 1000달러로 돌리던 캠페인이 갑자기 하루 2000달러 넘게 쓰기 시작했다.)

**판정: 대체로 사실이나 뉘앙스가 있다.** 하루에 평균 일일예산의 최대 2배까지 지출될 수 있다는 것은 구글이 오래전부터 공표해 온 정책 그 자체다(About overdelivery). 즉 1000달러 캠페인이 하루 2000달러를 쓰는 것은 이상 현상이 아니라 문서화된 동작이다. 대신 월 청구 상한은 평균 일일예산 곱하기 30.4로 묶여 있고, 이를 넘긴 초과분은 크레딧으로 환급된다고 명시돼 있다. 그러니 "환불도 수단도 전혀 없다"는 부분은 공식 정책과는 다소 어긋난다.

한편 최근의 실제 변경도 있다. 구글은 2026년 6월 15일 타깃 CPA·타깃 ROAS 입찰 방식 변경을 예고했고, 8월 17일부터 "예산 제한(budget-limited)" 상태이면서 타깃 기반 입찰을 쓰는 캠페인을 "설정한 타깃에 더 정확히 수렴하도록" 바꾼다고 발표했다. 구글이 든 예시가 문제의 핵심이다. 타깃 CPA가 10달러인데 최근 실제 CPA가 5달러였다면, 8월 17일 이후엔 10달러에 더 가깝게 수렴한다는 것이다. 저비용으로 전환을 뽑아내던 캠페인의 실질 비용이 최대 2배까지 오를 수 있다는 뜻이라, 업계에서 "CPA가 두 배로 뛴다"는 반발이 나오고 있다.

다만 "초과분이 전부 close variant 쓰레기 키워드로 들어간다"는 인과는 개별 광고주의 추정이다. 실제로는 8월 17일 입찰 변경, close variant 확장, Performance Max의 자동 확장 같은 여러 요인이 섞여 있을 수 있다.

## 세 고발 한눈에

| 고발 | 판정 | 핵심 근거 |
|---|---|---|
| 2차 가격 경매 폐지 → 최대 입찰가 과금 | 과장 | 검색은 여전히 GSP(공식 문서). 1차 전환은 디스플레이만. 단 반독점 재판서 은밀한 가격 인상(Momiji·RGSP) 확인 |
| exact match가 무관 검색어에 강제 노출 | 사실 | close variant "옵트아웃 불가" 공식 명시, 2014년부터 진행 |
| 일 예산 2배 초과 지출 | 대체로 사실 | 2배 overdelivery는 공식 정책. 단 월 상한·크레딧 환급 존재. "환불 없음"은 과장 |

## 가장 눈여겨본 것은

개별 사실을 따지면 Anderson은 몇 군데서 과장하거나 검색과 디스플레이를 섞었다. 그런데 그의 체감이 틀렸다고 말하기는 어렵다. 흥미로운 지점이 여기다. 그가 지목한 정책들은 대부분 오래됐거나 공식 문서에 적혀 있는 것들이다. close variant는 2014년부터, 2배 overdelivery는 처음부터, 가격 조절 손잡이는 2017년부터 있었다. 각각은 새롭지 않다.

새로운 것은 타이밍이다. 검색 볼륨이 LLM으로 빠져나가 성장이 꺾이는 순간, 구글은 이미 갖고 있던 이 손잡이들을 동시에, 더 세게 당길 유인을 얻는다. 광고주가 느끼는 "갑자기 나빠졌다"는 감각은 어느 한 정책이 새로 도입돼서가 아니라, 오래된 장치들이 한꺼번에 조여지는 국면에 들어섰기 때문일 수 있다. Anderson이 말한 "선의의 독점"의 종료란, 규칙이 바뀌는 사건이 아니라 같은 규칙을 운영하는 태도가 바뀌는 과정이다. 그리고 그 태도를 바꾸는 압력의 이름이 AI capex라는 것이 이 스레드의 진짜 주장이다.

## 출처

Max Anderson(@MaxAnderson), X 스레드, 2026년 7월 23일
원문: <https://x.com/MaxAnderson/status/2080229375773941871>

팩트체크에 참고한 자료:
- Google Ads Help, "Keyword close variants" / "About overdelivery" / "How the Google Ads auction works": <https://support.google.com/google-ads/answer/9342105>, <https://support.google.com/google-ads/answer/1704443>, <https://support.google.com/google-ads/answer/6366577>
- Search Engine Land, "Timeline: The long, slow death of Exact Match in Google Ads": <https://searchengineland.com/timeline-the-long-slow-death-of-exact-match-in-google-ads>
- MarTech, "How Google harms search advertisers in 20 slides": <https://martech.org/how-google-harms-search-advertisers-in-20-slides/>
- Bloomberg, "Google Tweaks Ad Auctions to Hit Revenue Targets, Executive Says" (2023-09-18)
- ppc.land, "Google Ads bidding overhaul forces CPAs to double, sparking backlash": <https://ppc.land/google-ads-bidding-overhaul-forces-cpas-to-double-sparking-backlash/>

이 다이제스트의 원 소스는 텍스트 트윗 스레드라 인용할 이미지가 없어 텍스트로 정리했다.
