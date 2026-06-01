---
title: "LLM Oriented Engineering"
date: 2026-06-01T15:30:00+09:00
tags: ["AI", "LLM", "AI 코딩", "코딩 에이전트", "조직 변화"]
categories: ["다이제스트"]
summary: "Reindeer CTO Yair Wein이 LLM 기반 제품·개발 조직을 1년 반 동안 운영하며 굳힌 9가지 원칙. 인간 컨텍스트가 가장 희소한 자원이라는 전제에서 출발해, load-bearing 코드와 padded rooms, 자동 enforcement, PM의 별도 MVP 레포, 보상 함수로서의 테스트, 미래 개발자의 능력까지 펼친다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/yairwein-llm-oriented-engineering/cover.jpg"
images:
  - "/images/yairwein-llm-oriented-engineering/cover.jpg"
---

## 3줄 요약

1. Reindeer CTO Yair Wein이 X에 올린 *LLM Oriented Engineering* 9원칙 장문 트윗을 정리한다. 25년차 산업 베테랑이 1년 반 동안 LLM 기반 제품·개발 조직을 운영하며 굳힌 결론이다.
2. 핵심 전제는 단순하다 — *인간 컨텍스트가 가장 희소한 자원*이고, *LLM이 만든 슬롭(slop)이 다음 LLM의 컨텍스트를 오염시킨다*. 이 두 가지가 새 시대 엔지니어링의 모든 디시플린을 강제한다.
3. 결론은 load-bearing 코드 vs padded rooms 이분법, API에 "no"라고 말할 인간, 자동 enforcement 두 계층(린터 + LLM judge), PM의 별도 MVP 레포, 보상 함수로서의 E2E 테스트 + 깨끗한 컨텍스트의 LLM judge, 그리고 *깊은 지식보다 컨텍스트 스위칭이 더 중요한 미래 개발자*다.

![Reindeer 일러스트 — 슬레지를 탄 개발자가 LLM 슬롭에 둘러싸여 PR description 종이가 날아다닌다. 양과 순록이 슬레지를 끈다.](/images/yairwein-llm-oriented-engineering/cover.jpg "원문 첨부 일러스트")

## 인간 컨텍스트가 희소 자원이다

> At the end of the day (and this hasn't changed in the 25 years I've been in the industry), human context is the most expensive resource.

사람의 컨텍스트 윈도우와 어텐션 마스크는 LLM과 똑같이 유한하다. LLM 등장 이후 콘텐츠 생산 속도는 폭발했지만, 인간의 소비 속도는 그대로다. **생산량 ÷ 인간이 실제로 처리 가능한 양**의 비율이 새 병목이고, 이 시대 엔지니어링 통찰의 대부분이 이 인식에서 파생된다.

문제는 더 나빠진다 — *슬롭이 슬롭을 먹인다*. LLM이 토해낸 장황한 코드 주석·PR 설명·과정만 적힌 문서는 무해해 보이지만, 다음 LLM이 그것을 읽고 자기 컨텍스트를 노이즈로 채운 채 같은 결로 이어간다. 조직 내 텍스트 콘텐츠는 타이트해야 하고, 코드만 봐도 자명한 내용은 굳이 적지 않는다.

## 인간을 대체할 수 없는 영역

### 모델링은 여전히 인간의 일

> Modeling is human work. Taking a CUJ and translating it to API flows, deciding what the components are, what the concerns of each are, and where their boundaries lie requires humans.

CUJ(critical user journey)를 API 흐름으로 번역하고 컴포넌트의 경계와 관심사를 결정하는 일은 인간이 한다. LLM이 코드를 빠르게 토해내니 *나쁜 모델링은 빠르게 퍼져* 사후에 풀 수 없는 의존성을 만든다. 실행이 싸질수록 *구조 결정*의 가치 비중은 최종 가치의 더 큰 부분을 차지한다.

### API는 공공 계약이지 스크래치패드가 아니다

LLM은 특정 태스크에 편한 필드를 자꾸 API에 끼워 넣는다. 그런 필드 하나하나가 API를 영구히 더럽힌다. **"no"라고 말할 수 있는 인간**이 반드시 있어야 하고, API·모델링 변경 시점에는 진짜 인간 리뷰가 필요하다.

## 스케일에서 슬롭을 막는 법

### 인간 코드 리뷰로 LLM을 이길 수 없다

LLM이 쏟아내는 코드 양은 인간 리뷰로 따라잡히지 않는다. 시도하면 모두가 *보지 않고 승인*하는 결과가 된다. 슬롭 방어는 인간 리뷰가 아니라 자동 enforcement 레이어로 한다.

### 자동 enforcement 두 계층

Reindeer는 두 층으로 수렴했다.

| 계층 | 대상 | 예시 |
|---|---|---|
| 린터 | 절대 논리 규칙 | 서비스 간 금지 의존성, 아키텍처 경계 |
| LLM judge | 코드화하기 어렵지만 모델이 검사 가능한 것 | 암묵 계약(implicit contracts) |

단, API 변경·모델링 변경에는 *진짜 인간 리뷰*가 여전히 기대된다.

### PR은 주의의 기본 단위다

일일 운영의 규칙은 단순하다 — **서로에게 슬롭을 던지지 마라**. 작은 PR, 필요하면 stacked. 2,000줄 슬롭 PR을 던지고 싶은 유혹은 크지만, 리뷰어의 컨텍스트 윈도우를 넘는 PR은 *승인은 되지만 읽히지 않는다*.

## 패디드 룸 — LLM에게 풀어줄 영역

> "Padded rooms" that don't affect modeling and don't create long-term dependencies. There you can be forgiving of slop because you can always replace it easily.

시스템을 위처럼 짜면 *LLM이 자유롭게 뛰놀 수 있는 영역*을 식별할 수 있다. 모델링에 영향을 주지 않고 장기 의존성을 만들지 않는 "패디드 룸". 거기서는 슬롭을 너그럽게 둬도 된다 — 언제든 쉽게 교체되고, 코드베이스 전체로 퍼지지 않으니까. 실제로 회사 코드의 대부분이 이런 영역일 수 있지만, 그것은 *load-bearing(하중을 지탱하는)*이 아니다.

이 분리는 **고객 커스터마이징의 답**이기도 하다. 커스터마이징은 100% 패디드 룸 안에 살아야 한다. 코어로 새는 순간 코어가 갈라지고, 새 고객 한 명 한 명이 리스크가 된다. 패디드 룸은 *아키텍처 비용을 치르지 않고 고객에게 빠르게 "예"라고 답할 수 있게 하는 인프라*다.

## 기술 부채 — 경제 역전

과거에는 개발 중간에 모델링 문제를 발견하면 *미래의 자신*에게 떠넘겼다. 다시 쓰는 비용이 비쌌으니까. 큰 태스크를 하는 중이면 기술 부채를 삼키는 게 합리적이었다.

오늘은 다시 쓰는 비용이 0에 가깝다. 진짜 투자는 *모델링*이었지 타이핑이 아니었다. 버리고 모델링을 고치고 다시 쓰는 일이 *싸다*. 반대로 그대로 두고 나중에 고치는 일은 매우 비싸다 — 잘못된 코드를 지나치는 모든 LLM이 그것을 채택하고, 슬롭이 슬롭을 먹이며, 즉시 고치지 않은 모델링 실수는 짧은 시간 안에 몇 배 복잡한 부채가 된다.

## 이 시대의 PM

### PM과 모델러는 한 결정의 양면

PM의 역할이 바뀌고 있다. PM은 모델링하는 사람과 *밀착해서* CUJ가 API·컴포넌트 번역 과정에서 깨지지 않도록 한다. 둘이 어긋나면 두 가지 실패가 나온다.

- *기술적으로는 동작하지만 CUJ를 못 살리는 제품*
- *깔끔하지만 정상적으로 구현할 수 없는 CUJ*

### PM은 별도 레포에서 직접 MVP를 만든다

> The PM also builds the MVP themselves, in a completely separate repo, with the assumption that this code will never touch production.

Reindeer에서 PM은 *프로덕션에 절대 닿지 않을 코드*라는 가정 아래 완전히 분리된 레포에서 자기 손으로 MVP를 만든다. LLM과 빠르게 움직여 고객에게 보여주고, 살아남거나 고객 접점이 필요한 것만 *질서 있는 모델링·개발 프로세스*를 통과한다. 핵심 제품을 외과적으로 보호하면서, 동시에 빠른 검증을 잡는 구조다.

## 루프에서 풀려나는 인프라

### 좋은 보상 함수가 개발자를 잠재운다

에이전트의 손을 잡고 따라다니는 것과, 여러 태스크를 병렬로 돌려놓고 자러 가는 것의 차이는 *좋은 보상 함수* 하나에 달려 있다. 없으면 LLM은 돌아오지 못하는 여행을 떠나고, 있으면 자기가 가까운지 먼지를 안다.

### E2E 테스트 + 깨끗한 컨텍스트의 LLM judge

개발에서 좋은 보상 함수는 *좋은 테스트*로 번역된다. 플랫폼은 E2E까지. 아무것도 검증하지 않는 mock 습관에서 LLM을 떼어내야 한다. LLM 출력이 들어가는 곳엔 evals. 그리고 *깨끗한 컨텍스트의 LLM judge*가 자동 리뷰 루프를 돌린다 — 코드를 쓴 에이전트가 빠진 환각에 judge까지 빠지지 않도록.

### 스킬 마켓플레이스 = 조직 인프라

> At Reindeer there's a central skill marketplace repo, divided into categories, that contains all internal skills. It's supported automatically in all harnesses: Claude Code, Codex, and for the deeply unhinged like myself, also pi.dev.

Reindeer에는 카테고리별로 분류된 *중앙 스킬 마켓플레이스 레포*가 있고, Claude Code·Codex·pi.dev 등 모든 하네스에서 자동 지원된다. 새 개발자는 즉시 모든 조직 스킬을 받는다 — 그 안에는 당연히 *온보딩·셋업 스킬*도 들어 있다.

## 미래의 개발자

### 핵심 능력은 깊은 지식이 아니라 컨텍스트 스위칭

이 시대 개발자의 결정적 능력은 *깊은 지식*이 아니다. **컨텍스트 스위칭**과 *자기 컨텍스트 윈도우/어텐션 마스크의 크기*다. 큰 컨텍스트를 잡고, 태스크 사이를 옮겨도 초점을 잃지 않고, 여러 에이전트를 병렬 관리할 수 있는 사람이 이긴다. 뾰족한 기술 깊이는 LLM이 채우니 덜 중요해진다. 보조 능력은 *모델링*과 *설계 단계에서 무엇을 경계해야 하는지*에 대한 감각.

### 적응 못 한 개발자는 net negative

> The LLM is a multiplier. For someone who knows how to work with it is productivity, and for someone who doesn't it is damage at high speed.

LLM은 *승수(multiplier)*다. 다룰 줄 아는 사람에겐 생산성이지만, 못 다루는 사람에겐 *고속으로 만들어내는 손상*이다. 적응한 사람은 초생산적이 되고, 적응 못 한 사람은 팀에 중립이 아니라 *순손실*이다. 두 번째 유형의 보상은 영(0)에 수렴할 것이다 — 일이 없어질 테니까. 적은 인원으로 훨씬 많은 일을 할 수 있지만, 그래서 채용은 매우 까다로워진다.

## 토큰 비용에 대해

토큰 가격이 5\~10배 뛰면 어쩌느냐는 질문이 자주 나오지만, 시간 축에서 비현실적이다. AI에는 *가속된 무어의 법칙*이 있어 달러당 품질이 계속 오르고, 카르텔을 형성할 수 없을 만큼 오픈 모델이 충분하다. Claude/Codex가 비합리적으로 비싸지면 우리는 모두 어떤 neocloud의 Qwen으로 갈아탄다 — 그래서 토큰이 싸다.

## 가장 흥미로운 지점

**load-bearing 코드 vs padded rooms**의 이분법이 글 전체를 관통한다. *어디까지 인간의 어텐션을 쓸 것인가*를 시스템 설계에 못박는 발상이다. 모델링·API 정의는 인간이 "no"라고 말하는 영역, 그 밖은 LLM에 풀어주는 영역. 슬롭이 슬롭을 먹이는 자기증식 메커니즘을 막으려면 *애초에 슬롭이 닿을 수 없는 구역*을 분리해 두는 길밖에 없다는 결론이다.

PM이 *프로덕션에 닿지 않는다는 가정 아래 별도 레포에서 직접 MVP를 만든다*는 운영 디테일도 인상적이다. 빠른 검증과 외과적인 코어 보호를 동시에 잡는, 패디드 룸 원칙을 *PM 역할*에 직접 적용한 사례다.

## 출처

저자: Yair Wein (@yairwein), Reindeer CTO. 25년차 산업 베테랑.
원문 트윗: <https://x.com/yairwein/status/2060058912351732137>
