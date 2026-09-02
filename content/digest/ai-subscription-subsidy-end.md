---
title: "AI 구독은 보조금이었다 — Copilot 토큰 청구 사건과 4인 체인"
date: 2026-06-08T20:30:00+09:00
tags: ["AI", "코딩 에이전트", "오픈소스", "경제·금융", "토큰 이코노미"]
categories: ["AI 산업"]
summary: "GitHub Copilot이 토큰 기반 청구로 전환된 첫날 쏟아진 사용자 반발을 시작으로, HedgieMarkets·Patrick O'Shaughnessy·Brian Armstrong·Marc Andreessen이 인용 체인으로 이어간 AI 구독·토큰 이코노미 논쟁의 정리."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/ai-subscription-subsidy-end/monthly-quota-error.jpg"
  alt: "Code-review 에이전트가 CAPIError 402 'You have exceeded your monthly quota' 로 끊긴 화면 — 사건의 시각적 정황. 출처: HedgieMarkets·O'Shaughnessy 트윗 첨부"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/ai-subscription-subsidy-end/monthly-quota-error.jpg"
---

## 3줄 요약

1. GitHub Copilot이 토큰 기반 청구로 전환된 당일, Pro+ 구독자들이 2시간 만에 월 크레딧의 60%를 소진하는 사태가 X에서 화제가 됐다.
2. 시장 코멘터 HedgieMarkets의 사건 정리 트윗에서 출발한 이 논쟁은 투자자 Patrick O'Shaughnessy의 거시 시나리오, Coinbase CEO Brian Armstrong의 80/20 라우팅·에너지 제약론, Marc Andreessen의 짧은 격상 한 마디로 이어지는 4인 체인을 이뤘다.
3. 핵심 논점은 한 줄로 압축된다 — 좌석당 정액 구독은 처음부터 보조금이었고, 오픈소스 추론과 중국 모델이 가격 천장을 누르는 동안 OpenAI 같은 웹2 AI 랩의 마진(-122% 보도)이 외부 자본에 의존하는 한, 자본 사이클이 끊기는 순간이 시나리오의 트리거가 된다.

## 사건 — Copilot 토큰 청구 전환 첫날 (HedgieMarkets)

HedgieMarkets는 시장·매크로 코멘터리를 던지는 익명 핀테크 트위터 계정이다. 자신의 분석을 "My Take"로 따로 분리해 적는 형식을 쓴다. 이번 트윗은 사건 정리 + 본인 코멘트로 구성됐다.

사실 위주 정리:

- 월 \$39 Pro+ 구독자들이 정상 사용 2시간 만에 크레딧의 60%를 소진했다.
- 한 사용자는 단일 파일 리뷰 한 번에 월 할당량의 20%를 잃었다 (코드 변경은 없었다).
- 또 다른 사용자는 달이 6월로 넘어가기도 전에 월 캡에 도달했다.
- 조직 단위 공용 토큰 풀은 개별 사용량을 볼 수 없어, 한 사람의 무거운 프롬프트로 팀 전체가 끊긴다.
- 사용자들이 Claude Code와 Codex로 이주 중이며, GitHub 커뮤니티 포럼은 불바다다.

본인 견해 — "My Take":

> 정액제 AI 구독은 처음부터 보조금이었다. 업계가 다 알고 있던 사실이다. 오늘 수백만 개발자에게 동시에 그 보조금이 끝났다. 문제는 많은 회사가 이미 이 도구를 전제로 재구조화를 끝냈다는 것이다. 인력을 감축하고, 남은 엔지니어에게 사내 역량을 키우는 대신 Copilot에 의존하라고 지시했다. 그 회사들은 이제 비용이 예측 불가능해지고, 프롬프트를 아껴 예산 안에 머무르는 순간 효용 자체가 바뀌어 버리는 도구에 묶여 있다.

마지막 한 줄이 사건 전체의 함의를 닫는다 — Anthropic이 같은 날 S-1을 신청했다는 점을 짚으며, "\$39 구독자가 첫날 도구가 못쓰겠다고 해지하면, 그 행동을 수백만 좌석에 곱했을 때 churn 리스크가 산업 차원의 문제가 된다"고 정리한다.

원문: <https://x.com/hedgiemarkets/status/2061577782594056321>

## 거시 시나리오 — AI가 터질 수 있는 가장 기본 방식 (Patrick O'Shaughnessy)

Patrick O'Shaughnessy는 *Invest Like the Best* 팟캐스트 운영자이자 O'Shaughnessy Asset Management 계열의 투자자다. 이 트윗은 본인이 며칠 전 올린 Copilot 사건 정리 트윗을 자기 인용하면서, 그 사건이 함의하는 거시 시나리오를 불릿 형식으로 전개한 1인 스레드다. 첫 문장은 강하다.

> The most basic way AI could blow up imo. I'm not saying it does but this is the most obvious way I can see it happening.

논리 흐름을 그대로 따라가면 다음과 같다.

**1단계 — 좌석당 구독은 보조금이다.**
좌석당 정액 요금은 헤비 사용 비용보다 한참 아래로 책정됐다. 실제 비즈니스 도입은 데이터 보호·업무 통합·컴플라이언스 승인 때문에 결국 API로 가야 하는데, API는 미터링 요금이다. 그래서 기업은 좌석당 가격이 시사한 것보다 훨씬 빠르게 크레딧을 태운다. 그가 예시로 든 사례는 Uber가 2026 AI 예산을 4개월 만에 다 태웠다는 보도, Microsoft의 코멘트, 그리고 본인 조직 내부에서 관찰된 동일 패턴.

**2단계 — 기업에는 값싼 대안이 있다.**
오픈소스 모델을 OpenRouter·Venice·Baseten·Together 같은 어그리게이터로 호출하면서 프라이버시도 가져갈 수 있다. Venice의 프라이빗 데이터센터, 또는 E2EE/TEE 서빙 환경에서 GLM 5.1을 돌리는 식이다. 가격 차이가 결정적이다 — DeepSeek V4는 SWE-bench에서 Opus와 거의 동급이면서 1/30 가격이고, 최저가 오픈 모델은 1/100 수준이다.

**3단계 — 중국 랩이 오픈소싱하는 한 추론 제공자는 최대 비용을 공짜로 얻는다.**
추론 제공자에게 가장 큰 비용은 모델 그 자체인데, 그 부분이 공짜로 들어온다. 이 시나리오가 깨지려면 중국이 클로즈드 소스로 돌아서야 한다. 그건 오히려 웹2 AI 랩에 호재다 — 모두가 클로즈드라면 최고 지능에 프리미엄을 지불해야 하므로.

**4단계 — 매출은 아직 폭증 중이다.**
Anthropic이 5개월 만에 \$9B에서 \$47B 런레이트로 점프했다. 누수의 신호는 아직 매출에 안 보인다.

**5단계 — 그러나 누수가 시작되면 캡이 씌워진다.**
Venice 사용량, OpenRouter \$113M 모집, Baseten이 3개월 만에 밸류 3배(\$11B)로 모집하면서 ARR이 \$200M에서 \$600M로 분기 만에 늘어난 사례. 매출이 오픈소스 추론 쪽으로 새기 시작하면 가격 인상 여력이 캡이 씌워진다.

**6단계 — 마진이 깊게 마이너스다.**
OpenAI는 마진 -122%로 보도된다. 캐시플로우가 없으니 외부 자본에 전적으로 의존해 GPU·학습·보조금을 유지한다 (Google이 \$80B 지분 매각, 그중 \$30B는 직원 RSU 세금 — 명백히 지분이 고평가라고 생각하지 않으면 팔지 않을 자산이다).

**7단계 — 트리거는 자본의 신념이 꺾이는 순간이다.**
가격은 캡으로 막혀 마진 개선이 불가능한데, 투자자가 페이백 신념을 잃는 순간 흐름은 역전된다. 페이백 신념을 왜 잃는가? 다시 원점 — 마진이 개선되지 않거나 기업이 더 지불할 의사가 없거나.

**단서 — 새로운 가치를 만들면 시나리오는 달라진다.**
AI로 신약이 나오거나 완전히 새로운 비즈니스가 만들어지면, 사람들은 AI 사용에 최대치를 지불할 것이다. 즉, 이 블로우업 시나리오는 "현재 가격대에서 가치 창출이 더 이상 증가하지 않는다"를 전제로 한다.

원문: <https://x.com/shaughnessy119/status/2061807418829578413>

## 응수 — 80/20 라우팅과 에너지 제약 (Brian Armstrong)

Brian Armstrong은 Coinbase 공동창업자이자 CEO다. O'Shaughnessy의 트윗을 인용하면서 "Good take"로 시작한 뒤, 본인의 추측을 짧은 불릿으로 덧붙인다.

| 주장 | 내용 |
|---|---|
| 지능 수요 | 거의 무한대다. |
| 12\~18개월 시야 | 워크로드의 80%가 99% 더 싼 모델로 옮겨간다. |
| 잔여 20% | 최신 세대 모델에서 돌아간다 — 과학적 돌파구, 상위 오케스트레이터 에이전트 같은 IQ 맥싱이 필요한 작업. |
| 비유 | 맥북·게이밍 PC에서 풀스펙 CPU/GPU를 쓰는 비율을 떠올리면 된다. 가격 하락은 무어 법칙보다 빠르다. |
| 진짜 제약 | 더 나은 모델이 아니라 에너지와 컴퓨트다. |

마지막은 사례로 마무리한다.

> At Coinbase we're working hard on routing prompts to cheaper models where appropriate, and in some cases have been able to keep costs roughly flat, while token usage continues to grow exponentially.

토큰 사용량이 지수적으로 늘어나는데 비용은 평탄하게 유지한 경우가 있다는 발언이다. O'Shaughnessy의 "API 미터링이 좌석당 가격보다 훨씬 빨리 탄다"는 진단을, 라우팅으로 무력화할 수 있다는 반론으로 받은 셈이다.

원문: <https://x.com/brian_armstrong/status/2063782620815876515>

## 격상 — Marc Andreessen

Marc Andreessen은 Netscape 공동창업자이자 a16z 공동창업자다. 그의 인용 트윗은 한 단어다.

> Interesting.

본문 논평은 없지만, Armstrong의 80/20·라우팅·에너지 제약 견해를 자신의 팔로워에게 격상해 전파하는 신호 역할을 한다. 체인은 사건 → 거시 시나리오 → 라우팅 반론 → 한 마디 격상 순으로 4단을 채우고 닫힌다.

원문: <https://x.com/pmarca/status/2063798598068846984>

## 가장 흥미로운 지점

같은 데이터를 보면서 결론이 갈리는 지점이 가장 흥미롭다.

O'Shaughnessy는 *공급측*을 본다 — 마진 -122%, 외부 자본 의존, 가격 인상 캡, 오픈소스 모델이 추론 제공자에게 공짜로 들어오는 구조. 그래서 자본 사이클이 끊기는 순간이 트리거다.

Armstrong은 *수요측·운영측*을 본다 — 80%의 워크로드는 라우팅으로 99% 싼 모델에 옮길 수 있고, Coinbase가 실제로 비용 평탄화를 만들어내고 있다. 그래서 진짜 제약은 모델 가격이 아니라 에너지·컴퓨트다.

두 사람의 데이터는 거의 동일하다 — 오픈소스 가격이 1/30~1/100이고, 가격 하락이 빠르다는 점. 다른 것은 그 사실을 *누구의 손익계산서로 보는가*다. 한쪽에서 보면 자본 사이클의 파괴이고, 다른 쪽에서 보면 사용자 측의 단가 절약이다. 둘 다 옳다.

Andreessen이 굳이 "Interesting." 한 마디로 Armstrong을 끌어올린 신호는 한 번 음미할 만하다. 그는 OpenAI에 직접 베팅하지 않는 a16z의 입장에서, 가격 하락·라우팅·에너지 제약이라는 후자의 프레임을 자신의 팔로워에게 노출시키는 쪽을 택했다. 이 짧은 단어가 4인 체인의 마무리가 됐다.

또 하나 — HedgieMarkets가 마지막에 짚은 "Copilot 의존을 전제로 인력을 감축한 회사들" 이야기는 두 거시 시나리오 어느 쪽에도 잘 들어맞지 않는 잔여 문제다. 가격이 평탄화되든 자본 사이클이 끊기든, *프롬프트를 아끼는 순간 도구의 효용 자체가 바뀌어 버리는* 구조에 묶인 팀은 별도의 출구를 찾아야 한다. 라우팅도 모델 가격 하락도 이 문제를 직접 풀지 않는다.

## 출처

- HedgieMarkets, "GitHub Copilot switched to token-based billing this morning…"
  <https://x.com/hedgiemarkets/status/2061577782594056321>
- Patrick O'Shaughnessy (@Shaughnessy119), "The most basic way AI could blow up imo…"
  <https://x.com/shaughnessy119/status/2061807418829578413>
- Brian Armstrong (@brian_armstrong), Coinbase CEO, "Good take…"
  <https://x.com/brian_armstrong/status/2063782620815876515>
- Marc Andreessen (@pmarca), a16z 공동창업자, "Interesting."
  <https://x.com/pmarca/status/2063798598068846984>

본문 인용 이미지의 원출처는 HedgieMarkets·O'Shaughnessy 트윗에 첨부된 캡처로, Code-review 에이전트가 monthly quota 초과로 끊긴 상황을 보여준다.
