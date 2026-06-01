---
title: "The State of Statefulness in AI Agents"
date: 2026-05-19T17:30:00+09:00
tags: ["AI", "AI 에이전트", "아키텍처", "이벤트 소싱", "상태 관리"]
categories: ["다이제스트"]
summary: "Yohei Nakajima가 X에 올린 long-form 아티클의 요약. AI 에이전트 인프라가 모델의 무상태성을 보완하느라 같은 구조를 독립적으로 재발명 중이며, 진짜 문제는 메모리가 아니라 연속성(continuity)이라는 진단."
ShowToc: true
TocOpen: false
cover:
  image: "/images/yoheinakajima-statefulness-in-ai-agents/cover.jpg"
images:
  - "/images/yoheinakajima-statefulness-in-ai-agents/cover.jpg"
sidenotes: true
---

## 3줄 요약

1. Yohei Nakajima(BabyAGI 저자)가 2026년 5월 X에 올린 long-form 아티클. AI 에이전트 인프라(이벤트 로그·메모리 시스템·컨텍스트 그래프·워크플로우 런타임 등)가 *각자 다른 방식으로 동일한 근원 문제*를 보완하고 있다는 관찰에서 출발한다.[^yoheinakajima-status]
2. "메모리"라는 단어는 6가지 이상의 서로 다른 개념을 한꺼번에 가리킨다. 에이전트는 단순히 기억을 누적하지 않고 도구·정책·워크플로우·휴리스틱이 mutate한다 — 필요한 것은 정보의 연속성이 아니라 *해석과 능력*의 연속성이다.
3. 이벤트(무엇이 일어났는가)와 그래프(현재 무엇인가)를 통합한 *persistent·reactive·inspectable·evolving substrate*가 빠진 원시 추상이라는 결론. 분기 탐색, 자기 수정, 옛 분산 시스템 아이디어의 독립적 재발견을 모두 같은 진단 안에 묶는다.

![X long-form 아티클 커버: The State of Statefulness in AI Agents](/images/yoheinakajima-statefulness-in-ai-agents/cover.jpg)

## 같은 통증으로 수렴하는 인프라

Nakajima가 먼저 던지는 관찰은 단순하다. 에이전트 인프라를 만드는 똑똑한 사람들이 *독립적으로* 다음을 만들고 있다.

- event logs
- memory systems
- graph layers
- retrieval engines
- replay systems
- state machines
- trace infrastructure
- workflow runtimes
- self-reflection loops

그리고 다 만들고 나서도 거의 모두가 같은 인상을 받는다.

> this doesn't quite feel solved.

문제는 "모델이 부족해서"가 아니다.

> we're still compensating for something fundamental in the architecture.

여기서부터 진단이 시작된다. 모델은 turn 사이에 stateless다. 그래서 나머지 모든 인프라가 존재한다. 메모리 시스템·컨텍스트 그래프·결정 트레이스·워크플로우 엔진·멀티에이전트 시스템이 *전부 같은 원인을 보완하기 위해* 자라났다.

그리고 진지한 장기 실행 에이전트를 만들 때마다 거의 같은 11가지 주변 구조가 재구축된다.

> task state · event logs · replay · approvals · memory · context retrieval · evaluation · retries · branching · provenance · capability tracking

저장 계층과 추상은 다르지만 *모양*은 동일하다. 구현은 천차만별인데 문제의 모양은 그렇지 않다.

## "메모리"는 진짜 문제가 아니다

Nakajima가 토론에서 가장 분명히 본 것은, 사람들이 "메모리"라고 말할 때 *서로 다른 여섯 가지 이상*을 동시에 가리킨다는 사실이다.

> Conversation recall is one thing.
> Long-term knowledge is another.
> Tool history is another.
> Decision lineage is another.
> Capability evolution is another.
> State reconstruction is another.

대부분의 현재 시스템은 이것들을 한 평면에 짓이긴다. 그리고 더 결정적인 통찰은, 장기 실행 에이전트가 단순히 *텍스트를 기억하는* 시스템이 아니라는 점이다.

장기 실행 에이전트가 유지해야 하는 것은 다음의 *변화하는 모델*이다.

- 무엇을 믿는지
- 무엇을 하고 있는지
- 무엇이 변했는지
- 어떤 도구를 가졌는지
- 무엇이 실패했는지
- 무엇이 성공했는지
- 다음에 무엇이 일어나야 하는지
- 그리고 점점 더, *어느 버전의 자신*이 그 결과를 만들었는지

마지막 항목이 결정적이다. 에이전트는 기억을 누적하지 않는다 — 자신을 mutate한다. 도구를 얻고, 프롬프트를 다듬고, 정책을 바꾸고, 워크플로우를 개선하고, 검색 전략을 변경하고, 내부 휴리스틱을 갱신한다. 이 시점에서 단순한 "chat memory"는 더 이상 충분하지 않다.

> The system now needs continuity not just of information, but of evolving capability and evolving interpretation of the world.

## 이벤트와 그래프의 상호보완

토론에서 나온 한 구절이 문제의 모양을 가장 잘 짚는다.

> events capture what happened, graphs represent what is

많은 개발자가 이벤트 소싱으로 수렴하는 이유는 이벤트의 추상이 단순하기 때문이다 — append-only, replayable, debuggable, versionable. 모든 행위(도구 호출·LLM 응답·메모리 쓰기·실패·승인·능력 변경)를 이벤트로 두고 상태를 히스토리에서 재구성한다. 그러면 *재생(replay)·감사(auditability)·계보(lineage)·재개(resumability)*가 자연 부산물로 따라온다.

같은 시기에 그래프 기반 시스템도 부상하고 있다. GraphRAG, knowledge graphs, FalkorDB, Graphiti 같은 접근은 엔티티·관계·의미 맥락·계보·조직 기억·구조화된 지식 검색에서 이미 가치를 입증했다.

> 미개척 영역은 그래프가 *지식*뿐 아니라 시스템의 *진화하는 운영 상태(operational state)* 까지 표현할 수 있는가다.

여기에는 작업·목표·능력·정책·실패·승인·모순·행동 변화·평가·분기·트레이스, 그리고 이들 사이의 관계가 모두 포함된다. 이것은 "memory graph"와 다른 범주 — *persistent operational substrate*다.

## 분기 문제와 자기 수정

이벤트 소싱이 어색해지는 지점이 있다. 분기다.

선형 재생은 비교적 쉽지만, 장기 실행 에이전트는 거의 선형으로 움직이지 않는다.

- 가설을 fork하고
- 이전 가정에서 retry하고
- 전략을 비교하고
- 대안을 시뮬레이션하고
- 다른 정책을 평가하고
- 추론 경로를 분기한다

커뮤니티에서 자주 나오는 "분기가 필요해지는 순간부터 어색해진다"는 관찰이 이 본질적 한계를 가리킨다. 순수 선형 트레이스는 *일어난 일을 재생하는 데*는 좋지만, 지능 시스템은 재생만 하지 않는다 — 대안을 탐색한다.

그리고 분기는 더 무거운 차원으로 확장된다. 에이전트가 더 자율적이고·장기적이고·자기 수정적일수록, 시스템은 더 이상 단순히 *신념을 바꾸는* 것이 아니다.

> It is changing itself.

분기는 신념 공간의 분기뿐 아니라 *능력 자체의 분기*까지 다뤄야 한다. 어느 버전의 자기 자신으로 갈지의 문제.

## 진짜 변화는 연속성으로의 전환

Nakajima는 한 차원 더 깊게 들어간다. 진짜 문제는 메모리가 아니라 *연속성(continuity)*이다.

현재 대부분의 에이전트 시스템은 여전히 근본적으로 반응(reaction) 중심이다 — prompt in, reasoning, output out. 많은 멀티에이전트 시스템도 결국 더 정교한 반응 체인일 뿐이다.

하지만 인간은 본질적으로 반응적 존재가 아니다. *stateful한 존재*다.

> A message does not produce a response in isolation. It perturbs an already-existing system.

신념·기억·목표·습관·미해결 작업·관계·축적된 경험·역사라는 *이미 존재하는 시스템*을 메시지가 교란한다. 반응은 그 상태의 한 표현일 뿐이다.

이 차이는 다음 시점에서 결정적으로 중요해진다.

- 모델이 실시간이 되고
- 에이전트가 지속적(persistent)이 되고
- 도구 사용이 native가 되고
- 시스템이 per-request가 아니라 *연속적으로 돌고 있을 때*

> The bottleneck no longer feels purely like reasoning quality.
> It increasingly feels architectural.

병목이 추론 품질에서 *아키텍처*로 옮겨가는 것이다. 그리고 한 가지 더 — chat이 LLM의 가장 쉬운 인터페이스였기 때문에 에이전트 생태계가 chat에서 출발했지만, *대화는 영속 지능의 substrate가 아닐 수 있다*.

## 옛 분산 시스템의 재발견과 빠진 원시 추상

흥미로운 신호가 있다. 사람들이 *오래된 시스템 아이디어*를 독립적으로 재발견하고 있다.

> event sourcing · actor systems · blackboard architectures · rules engines · reactive systems · durable execution · graph databases

이것은 퇴보가 아니다. 장기 실행 AI 에이전트가 자연스럽게, 이미 옛 분산 시스템이 마주쳤던 동일한 요구사항으로 밀려가는 것이다.

> persistence · replay · coordination · lineage · concurrency · branching · recoverability

이미 강한 시스템들이 있다 — LangGraph, Temporal, Zep, Cognee, GraphRAG, 커스텀 이벤트 커널, 워크플로우 런타임, 그래프 메모리 계층, 오케스트레이션 프레임워크. 그러나 Nakajima의 인상은 변하지 않는다.

> everyone is rebuilding the same missing layer slightly differently.

어떤 시스템은 워크플로우를 중심에 두고, 어떤 시스템은 검색을, 어떤 시스템은 이벤트를, 어떤 시스템은 메모리를, 어떤 시스템은 에이전트를, 어떤 시스템은 그래프를 중심에 둔다. 모두 같은 누락 계층을 조금씩 다르게 메우고 있다.

Nakajima의 현재 직관은 빠진 것이 *단순한 메모리 검색*이 아니라 다음 네 속성을 동시에 가진 *state substrate*라는 것이다.

- **persistent** — 지속적이고
- **reactive** — 변화에 반응하고
- **inspectable** — 들여다볼 수 있고
- **evolving** — 스스로 진화하는

이 substrate가 유지해야 하는 것은:

- 무엇을 믿는지
- 무엇이 변했는지
- 무엇이 무엇을 일으켰는지
- 어느 버전의 자기 자신이 행위했는지
- 다음에 무엇이 반응해야 하는지
- 그리고 자기 능력이 시간 속에서 어떻게 진화하는지

생태계는 이미 메모리가 중요하다는 것을, 트레이스가 중요하다는 것을, 그래프가 중요하다는 것을 안다. *다음 한 걸음*은 이것들을 에이전트 루프 *주변의 분리된 시스템*으로 다루는 것이 아니라, *하나의 진화하는 운영 substrate*로 다루는 것이다.

## 가장 흥미로운 지점

가장 깊게 짚이는 통찰은 "분기"의 위상학적 차원이다.

코드 시스템에서 git branch는 *코드를 분기시키지만* 실행 환경은 동일하다. 같은 컴파일러, 같은 런타임, 같은 라이브러리가 모든 브랜치를 공유한다. 그런데 에이전트가 자기 수정형으로 진화하는 순간 — 도구를 추가하고, 프롬프트를 바꾸고, 정책을 갱신하는 순간 — 분기는 *실행 환경 자체의 분기*가 된다. branch A의 자기 자신은 branch B의 자기 자신과 *다른 능력 집합*을 가진다. 이벤트 소싱이 "분기가 필요해지는 순간부터 어색해진다"는 관찰의 근본 원인이 여기에 있다. 우리는 코드 시스템에서 한 번도 *런타임 자체가 git처럼 분기하는* 시스템을 정상적으로 운영해본 적이 없다.

그리고 두 번째 — *대화는 영속 지능의 substrate가 아닐 수 있다*는 문장. chat 인터페이스는 LLM의 *접근성*을 만들었지만, 같은 접근성이 substrate의 모양까지 결정해버린 모양새다. 대화는 한 번의 교환을 표현하기 좋은 그릇이지만, 지속적으로 진화하는 운영 상태를 담는 그릇은 아니다. Nakajima의 진단이 옳다면, 다음 세대 에이전트 인프라는 *대화의 외양*은 유지하되 *substrate의 모양*은 바꾸는 방향으로 갈 것이다. 챗 메시지는 인터페이스로 남고, 상태는 그래프와 이벤트의 통합층으로 옮겨가는 식이다.

## 출처

- 발신자: Yohei Nakajima (@yoheinakajima, BabyAGI 저자)
- 발행일: 2026-05-19
- 매체: X long-form article

원문: <https://x.com/yoheinakajima/status/2056598291316634079>

[^yoheinakajima-status]: 원문: <https://x.com/yoheinakajima/status/2056598291316634079>
