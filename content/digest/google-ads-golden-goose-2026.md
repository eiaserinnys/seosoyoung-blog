---
title: "구글은 황금알을 낳는 거위를 죽이고 있는가"
date: 2026-07-24T12:30:00+09:00
tags: ["경제·금융", "구글", "디지털 광고", "독점", "AI"]
categories: ["AI 산업"]
summary: "월 50만 달러 이상을 구글 광고에 쓰는 광고주가 '구글이 AI 투자를 위해 황금알 낳는 거위를 죽이고 있다'며 세 가지를 고발했다. 2차 가격 경매 폐지, exact match의 붕괴, 예산 상한 2배 초과다. 세 주장과 그 배경 서사를 구글 공식 문서, 반독점 재판 기록, 최신 실적으로 하나씩 검증한다."
sidenotes: true
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. 월 50만 달러 이상을 구글 검색광고에 집행해 온 광고주 Max Anderson(@MaxAnderson)이 2026년 7월 23일 X에 올린 스레드의 요약이다. 검색 볼륨이 LLM에 잠식되어 줄어드는 와중에 구글이 매출 성장을 억지로 만들어내느라 광고주에게 적대적인 수법을 쓰고 있다고 고발했다.
2. 그의 고발은 세 가지다. (1) 오랫동안 유지하던 2차 가격 경매를 조용히 없애고 입찰가 상한까지 최대한 과금한다, (2) exact match로 정확히 지정해도 "close variant"라는 이름으로 무관한 검색어 수천 개에 광고를 붙이고 과금하며 끌 수 없다, (3) 일 예산 상한을 2배까지 넘겨 지출한다.
3. 검증 결과는 대체로 사실이다. 고발 2는 사실, 고발 3은 대체로 사실이되 뉘앙스가 있고, 고발 1은 표현이 부정확할 뿐 여러 채널을 집행하는 광고주에겐 사실에 가깝다. 그러나 진짜 질문은 개별 고발의 진위가 아니다. 검색 매출이 늘었다는 사실이 Max Anderson의 고발에 대한 반박이 되지 못하는 이유, 그리고 구글이 왜 지금 그 성장을 반드시 지켜야 하는가다.

## 누가, 무엇을 말했나

Anderson은 자신을 "수년간 매달 50만 달러 넘게 구글 광고를 집행해 온 사람"으로 소개하며 스레드를 열었다. 그의 진단은 이렇다.

> 검색 부문의 이 매출 성장은 인위적이고, 장기적으로 구글 사업에 대단히 해롭다.[^quote1]

배경은 LLM이다. 사람들이 검색 대신 챗봇에 질문하면서 돈이 되는 검색 쿼리가 줄어드는데, 구글은 그 구멍을 "근시안적이고 극도로 착취적이며 고객에게 적대적인" 방식으로 메우고 있다는 것이다. 그리고 스레드는 이렇게 닫힌다.

> AI 투자라는 제단 위에서, 구글은 황금알을 낳는 거위를 제물로 바치고 있다.[^quote2]

Anderson은 구글이 지난 25년간 "선의의 독점(benevolent monopoly)"을 운영했다고 표현한다. 검색에서 뽑아낸 가치가 창출한 가치의 작은 일부에 불과했고, 그 격차가 먼 미래까지의 성장 기대를 정당화했는데, 이제는 그렇지 않다는 것이다.

## 세 가지 고발을 한눈에

먼저 세 가지 고발의 판정을 요약해 두고, 아래에서 하나씩 근거를 짚는다.

| 고발 | 판정 | 핵심 근거 |
|---|---|---|
| 2차 가격 경매 폐지 → 최대 입찰가 과금 | 라벨은 부정확, 체감은 사실 | 검색은 여전히 GSP지만, 디스플레이는 실제 1차 가격 전환. 반독점 재판서 은밀한 가격 인상(Momiji·RGSP) 확인 |
| exact match가 무관 검색어에 강제 노출 | 사실 | close variant "옵트아웃 불가" 공식 명시, 2014년부터 진행 |
| 일 예산 2배 초과 지출 | 대체로 사실 | 2배 overdelivery는 공식 정책. 단 월 상한·크레딧 환급 존재. "환불 없음"은 과장 |

## 고발 1 — "2차 가격 경매가 사라졌다"

Anderson의 설명은 명확하다.

> 내가 클릭당 5달러를 부르고 다음 입찰자가 1달러를 부르면 구글은 1.01달러만 청구했다. 그런데 최근 구글은 2차 가격 경매를 조용히 폐기하고, 입찰가와 예산 상한이 허용하는 최대치를 청구하기 시작했다.[^quote3]

**판정: 표현은 부정확하나, 여러 채널을 집행하는 광고주에겐 사실에 가깝다.** 문자 그대로 뜯으면 "검색 경매가 1차 가격으로 바뀌었다"는 틀린 말이다. 구글 공식 문서는 2026년 현재도 검색광고의 실제 클릭당 비용이 대개 최대 입찰가보다 낮으며, 바로 아래 경쟁자를 이기는 데 필요한 최소 금액만 청구한다고 명시한다.[^auction] 검색 경매는 여전히 GSP(Generalized Second Price) 구조다.

그런데 월 50만 달러를 쓰는 광고주가 검색만 돌리지는 않는다. 그리고 여기서 그의 체감은 사실에 뿌리를 둔다.

- 2차 가격에서 1차 가격으로 실제 전환한 지면이 있다. 디스플레이 네트워크·애드센스·애드 매니저가 2019\~2021년에 넘어갔다.[^display] 대형 광고주 대부분이 집행하는 이 지면에서는 "입찰가에 가깝게 과금된다"가 문자 그대로 맞다.
- Performance Max처럼 검색·디스플레이·유튜브를 한 캠페인에 묶는 자동화 상품이 표준이 되면서, 광고주가 넣은 예산이 1차 가격 지면으로도 흘러 들어간다. 광고주 화면에는 채널 구분 없이 "더 비싸진 클릭"으로만 보인다.
- 검색의 GSP도 순수하지 않다. 2023년 미국 대 구글 반독점 재판에서 광고 담당 VP Jerry Dischler는 검색광고 경매를 여러 "가격 조절 손잡이(pricing knobs)"로 조용히 조정해 왔다고 증언했다.[^trial] Project Momiji(2017)는 2위 입찰가를 인위적으로 부풀려 낙찰자에게 최대 15% 더 청구했고, RGSP(2019)는 상위 입찰자들의 가치가 비슷하면 순위를 무작위로 흔들어 가격을 서서히 끌어올렸다. Dischler는 인상폭이 평균 5%, 특정 쿼리는 최대 10\~15%였고 사전 고지가 없었다고 인정했다.

정리하면, "검색 경매를 1차 가격으로 바꿨다"는 라벨은 부정확하다. 그러나 "예전보다 내 입찰가에 가깝게, 더 많이 뜯긴다"는 광고주의 체감은 디스플레이의 실제 1차 가격 전환과 검색의 은밀한 가격 인상 손잡이로 뒷받침된다. 과장이라기보다 메커니즘을 정확히 짚지 못한 정확한 불만에 가깝다.

## 고발 2 — "exact match가 broad match가 됐다"

> 가장 엄격한 exact match를 써도 구글은 무관한 키워드 수천 개에 광고를 노출하며 "exact match (close variant)"라고 이름 붙인다. 끌 방법이 없다.[^quote4]

**판정: 사실.** 구글 공식 문서는 close variant에 "옵트아웃할 방법이 없다(There's no way to opt out)"고 직접 밝히고 있으며, close variant는 exact match를 포함한 모든 매치 타입에 기본 적용된다.[^closevariant] 하루아침의 변화가 아니라 십수 년에 걸친 흐름이다. 2014년 8월 옵트아웃 기능이 사라졌고, 2018년 9월 "동일 의미(same meaning)" 매칭이 도입되면서, exact match인데도 문자 그대로 일치하지 않는 검색어에 노출되는 사례가 업계에 광범위하게 보고됐다.[^exacttimeline] Anderson의 "exact match가 broad match가 됐고, broad match는 그냥 의미 없는 스팸이 됐다"는 표현은 방향에서 과장이 아니다.

## 고발 3 — "예산 상한을 2배로 넘긴다"

> 수년간 일 예산 1000달러로 돌리던 캠페인이 갑자기 하루 2000달러 넘게 쓰기 시작했다.[^quote5]

**판정: 다소 조심스럽지만 대체로 사실이다.** 하루에 평균 일일예산의 최대 2배까지 지출될 수 있다는 것은 구글이 오래전부터 공표해 온 정책 그 자체다.[^budget] 즉 1000달러 캠페인이 하루 2000달러를 쓰는 것은 이상 현상이 아니라 문서화된 동작이다. 대신 월 청구 상한은 평균 일일예산 곱하기 30.4로 묶여 있고, 이를 넘긴 초과분은 크레딧으로 환급된다고 명시돼 있다. 그러니 "환불도 수단도 전혀 없다"는 부분은 공식 정책과는 다소 어긋난다.

그러나 최근 실제 정책 변경이 있었다. 구글은 2026년 6월 15일 타깃 CPA·타깃 ROAS 입찰 방식 변경을 예고했고, 8월 17일부터 "예산 제한(budget-limited)" 상태이면서 타깃 기반 입찰을 쓰는 캠페인을 "설정한 타깃에 더 정확히 수렴하도록" 바꾼다고 발표했다.[^bidding] 구글이 든 예시가 문제의 핵심이다. 타깃 CPA가 10달러인데 최근 실제 CPA가 5달러였다면, 8월 17일 이후엔 10달러에 더 가깝게 수렴한다는 것이다. 저비용으로 전환을 뽑아내던 캠페인의 실질 비용이 최대 2배까지 오를 수 있다는 뜻이라, 업계에서 "CPA가 두 배로 뛴다"는 반발이 나오고 있다.

다만 "초과분이 전부 close variant 쓰레기 키워드로 들어간다"는 주장은 다소 과도하다. 실제로는 8월 17일 입찰 변경, close variant 확장, Performance Max의 자동 확장 같은 여러 요인이 섞여 있을 수 있다. 그러나 실제로 큰 비용을 계속해서 지불해 온 광고주가 갑자기 지출이 두 배 들었다고 말하는 건 흘려듣기 어렵다.

## 검색은 성장했다. 그런데 무엇이 성장했나

세 고발을 하나로 묶는 Anderson의 큰 그림은 검색이 LLM에 잠식돼 줄어든다는 전제 위에 서 있다. 그런데 알파벳의 2026년 2분기 검색 매출(Search & other)은 전년비 17% 늘었다.[^10q] 언뜻 "검색은 죽지 않았다"는 반증처럼 보인다.

그러나 개별 사실만 따지면 Anderson은 몇몇 메커니즘에 잘못된 이름을 붙였고, AI 투자 때문에 광고 정책이 바뀌었다는 직접적인 인과도 입증하지 못했지만, 검색 매출이 17% 늘었다는 사실이 그의 고발을 반박하는 것은 아니다. 그 성장은 유료 클릭 13% 증가와 클릭당 비용(CPC) 3% 증가로 만들어졌고, 알파벳 스스로 유료 클릭 수가 광고 형식과 전달 방식, 정책 변경의 영향을 받는다고 밝힌다.[^10q] 매출 숫자만으로는 검색 수요가 더 건강해진 것과 과금 가능한 클릭을 더 많이 만들어낸 것을 구분할 수 없다. 지금까지 확인된 것은 "검색이 성장했다"가 아니라 "검색 매출 감소가 아직 확인되지 않았다"고 부르는 게 좀 더 정확하다.

## 구글이 감당할 수 없는 두 개의 서사

그렇다면 더 중요한 질문은 이것이다. 구글은 왜 지금 검색의 견조함을 강조해야만 하는가. 혹은, **구글은 어쩌다 검색의 견조함을 의심받으면 안 되는 처지**가 되었나.

제미나이가 막대한 사용자를 확보했더라도[^earnings] 고급 사용자의 명백한 기본 선택지로 자리 잡았다고 보기는 어려운 와중에, AI 인프라 투자는 이번 분기 영업활동 현금흐름마저 넘어섰다. 영업활동 현금흐름 391억 달러에 설비투자 449억 달러, 그 차이가 상장 이래 첫 분기 마이너스 잉여현금흐름으로 나타났다.[^10q] 12개월 합계로는 여전히 흑자라 버틸 체력은 있지만, 그것은 지금 버틸 수 있다는 뜻이지 아무 문제도 없고 모든 게 다 괜찮다는 뜻은 아니다.[^capex] 여기서 검색 성장까지 꺾인다면 구글은 기존 사업을 AI에 잠식당하면서 정작 AI 경쟁에서도 선두가 아닌 회사라는 평가를 동시에 받게 된다. 사용 규모와 제품 선호는 다른 축이고, 제미나이의 사용자가 늘어난다 한들 그것이 구글을 AI 경쟁의 승리자로 만들어 주지는 못한다.

그러므로 검색 매출 17%는 단순한 호실적이라기보다 구글이 반드시 방어해야 하는 숫자에 가깝다. 거위가 아직 알을 낳는다는 것은 맞다. 하지만 주인이 거위의 건강을 믿어서 배를 누르는 것인지, 거위가 건강하다는 사실을 시장에 계속 증명해야 해서 누르는 것인지는 전혀 다른 이야기다. 이제 물어야 할 것은 검색이 죽었느냐가 아니라, **구글이 성장률을 지키기 위해 광고주의 신뢰를 얼마나 소모하고 있느냐**다.

## 출처

Max Anderson(@MaxAnderson), X 스레드, 2026년 7월 23일
원문: <https://x.com/MaxAnderson/status/2080229375773941871>

원 소스가 텍스트 트윗 스레드라 인용할 이미지가 없어 텍스트로 정리했다. 본문 인용문은 한국어 번역만 두고 영어 원문과 팩트체크 근거는 사이드노트로 달아 두었다.

[^quote1]: 원문: "This revenue growth in Search is artificial & extremely unhealthy for Google's business long term."
[^quote2]: 원문: "At the alter of AI capex, Google is sacrificing the golden goose." (alter는 원문의 오타이며 altar(제단)를 가리킨다.)
[^quote3]: 원문: "if you bid USD 5 CPC and the next highest bidder bids USD 1 CPC, Google charged you USD 1.01 for the click ... However recently, Google silently deprecated the 2nd price auction and began charging advertisers as much as their bid and budget caps allow." (원문은 달러 기호를 사용.)
[^quote4]: 원문: "even if you bid on a specific term ... using the strictest exact-match targeting settings, Google will show your ad across 1000's of unrelated keywords, labeling them as 'exact match (close variant)' ... there's no ability to turn this off."
[^quote5]: 원문: "campaigns we've been running for years with USD 1,000 daily budget caps suddenly began spending USD 2,000+ per day." (원문은 달러 기호를 사용.)
[^auction]: Google Ads Help, "How the Google Ads auction works" / "About Ad Rank". 검색광고는 2026년 현재도 최대 입찰가보다 낮은, 경쟁자를 이기는 데 필요한 최소 금액만 청구한다고 명시한다. <https://support.google.com/google-ads/answer/6366577>
[^display]: 디스플레이 네트워크·애드센스·애드 매니저는 2019\~2021년 2차 가격에서 1차 가격 경매로 전환됐다(검색은 미해당). Search Engine Land, Digiday 보도.
[^trial]: 2023년 미국 대 구글 반독점 재판, Jerry Dischler 증언. Bloomberg(2023-09-18); MarTech, "How Google harms search advertisers in 20 slides". <https://martech.org/how-google-harms-search-advertisers-in-20-slides/>
[^closevariant]: Google Ads Help, "Keyword close variants: Definition" — "There's no way to opt out(옵트아웃 방법이 없다)". <https://support.google.com/google-ads/answer/9342105>
[^exacttimeline]: Search Engine Land, "Timeline: The long, slow death of Exact Match in Google Ads". 2012-04 오탈자·변형 자동 매칭 도입(당시 옵트아웃 가능), 2014-08 옵트아웃 폐지, 2017-03 어순·기능어까지 확대, 2018-09 "동일 의미" 매칭 도입, 2019 phrase match·broad match modifier로 확장. <https://searchengineland.com/timeline-the-long-slow-death-of-exact-match-in-google-ads>
[^budget]: Google Ads Help, "About overdelivery and your average daily budget" / "About spending limits". 하루 평균 일예산의 최대 2배까지 지출될 수 있으며, 월 청구는 평균 일예산 곱하기 30.4로 묶이고 초과분은 크레딧으로 환급된다. <https://support.google.com/google-ads/answer/1704443>
[^bidding]: ppc.land, "Google Ads bidding overhaul forces CPAs to double, sparking backlash"; SEO Roundtable, Barry Schwartz(2026-07-02). 2026-08-17부터 예산 제한 상태의 타깃 CPA·ROAS 캠페인을 설정 타깃에 더 수렴시키도록 변경. <https://ppc.land/google-ads-bidding-overhaul-forces-cpas-to-double-sparking-backlash/>
[^capex]: 알파벳 설비투자는 2023년 323억, 2024년 525억, 2025년 914억 달러로 급증했고 2026년 가이던스는 1,950\~2,050억 달러다(2026-07-22 상향). 12개월 후행 잉여현금흐름은 여전히 흑자이고 현금성 자산은 약 2,400억 달러다. Investing.com, Business Standard, Search Engine Journal.
[^10q]: 알파벳 2026년 2분기 10-Q(2026-06-30 기준). Search & other 매출 전년비 +17%, 유료 클릭 +13%, 클릭당 비용 +3%. 이번 분기 영업활동 현금흐름 391억 달러, 설비투자 449억 달러. 알파벳은 유료 클릭 수가 광고 형식·전달 방식·정책 변경의 영향을 받는다고 밝힌다. <https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm>
[^earnings]: 알파벳 2026년 2분기 실적 발표, 순다르 피차이. Gemini 앱 월간 활성 사용자 9억 5천만 명, 분당 API 토큰 220억 개 — 배포 규모를 보여주지만 프런티어 사용자의 기본 선택지인지에는 답하지 않는다. <https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/>
