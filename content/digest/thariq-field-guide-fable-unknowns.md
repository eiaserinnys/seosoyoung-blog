---
title: "A Field Guide to Fable: Finding Your Unknowns"
date: 2026-07-04T14:00:00+09:00
tags: ["AI", "Claude Code", "Anthropic", "에이전트", "프롬프트 엔지니어링", "Fable 5"]
categories: ["에이전트와 코딩"]
summary: "Anthropic Claude Code 팀 Thariq이 Fable 5로 일하며 재발견한 오래된 교훈. 이제 작업의 병목은 모델이 아니라 내가 unknown을 얼마나 명확히 하는가로 옮겨갔다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/thariq-field-guide-fable-unknowns/cover.jpg"
  alt: "A Field Guide to Fable — Finding Your Unknowns"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/thariq-field-guide-fable-unknowns/cover.jpg"
---

## 3줄 요약

1. Anthropic Claude Code 팀의 Thariq Shihipar가 2026년 7월 3일 X 아티클로 발행한 장문 글. Claude Fable 5로 일하면서 다시 배우게 된 오래된 교훈 — "지도는 영토가 아니다" — 를 실무 매뉴얼로 옮겼다.
2. Fable은 작업 품질의 병목이 모델이 아니라 "내가 unknown을 얼마나 명확하게 만드느냐"로 옮겨간 최초의 모델이다. Rumsfeld 4분면(Known Knowns, Known Unknowns, Unknown Knowns, Unknown Unknowns)을 에이전트 코딩에 적용해, 구현 전, 중, 후로 unknown을 발견하는 반복 프로세스로 재정의한다.
3. Blind Spot Pass, HTML 목업 브레인스토밍, 튀어보이는 결정을 위로 올린 실행 계획, 실행 노트, 인수인계 문서까지 5가지 레시피를 각각의 프롬프트 예시와 함께 제시하고, 총 11개의 인터랙티브 HTML 데모로 시각화했다.

## 지도는 영토가 아니다

Thariq은 글을 오래된 명제 하나로 연다.

> Working with Claude Fable 5 keeps re-teaching me an old lesson: the map is not the territory.

지도는 내가 에이전트에게 넘겨주는 프롬프트, 스킬, 컨텍스트다. 영토는 실제로 해야 할 작업이다. 둘 사이의 간극을 그는 "unknown", 즉 내가 아직 모르는 세계로 부른다.

> Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns.

Fable을 다뤄본 뒤 그가 내린 진단은 이렇다. 작업 품질의 병목은 모델이 아니라, 내가 unknown을 명확히 하는 능력이다. 그래서 Fable과 일하는 과정은 처음부터 계획을 짜는 일이 아니라, 구현 전, 도중, 이후에 걸쳐 unknown을 반복해서 발견하는 프로세스가 된다.

> I've found that working with Fable is an iterative process of discovering my unknowns before, during, and after implementation.

## unknown의 4분면

Thariq은 Rumsfeld의 유명한 4분면을 에이전트 코딩에 옮긴다.

| 분면 | 뜻 | 특징 |
| --- | --- | --- |
| Known Knowns | 이미 알고 있고, 알고 있음을 아는 것 | 프롬프트에 그대로 등장한다 |
| Known Unknowns | 모르는 것을 안다 | "이 부분은 확인이 필요하다"로 표현된다 |
| Unknown Knowns | 알지만 언어화되지 않은 것 | 이른바 암묵지 |
| Unknown Unknowns | 모르는지조차 모르는 것 | 가장 위험한 사각지대 |

그가 관찰한 실무 규칙은 단순하다. 뛰어난 에이전틱 코더는 unknown이 상대적으로 적다.

> The best agentic coders have relatively few unknowns.

## Claude는 어떻게 도움이 되는가

Claude는 내 unknown을 더 빨리 찾도록 돕는다. 코드베이스와 인터넷을 매우 빠르게 뒤지고, 평균적인 주제에 대해 나보다 훨씬 많이 알며, 실패에서 더 빠르게 반복한다.

> Claude can help you discover your unknowns faster. It can search through your codebase and the internet extremely quickly and it knows much more about the average topic than you. It can also iterate from failure faster.

핵심은 시작 시점에 컨텍스트를 얼마나 풍부하게 넘겨주느냐다. 내가 지금 사고 과정의 어느 지점에 있는지, 어떤 경험이 있고 어떤 코드베이스와 씨름 중인지 — 이 정보가 unknown 발견의 출발선이 된다.

## 레시피 — 구현 전, 도중, 이후

Thariq은 unknown 발견을 세 단계로 나눈다.

### 구현 전 — 가장 싼 발견 지점

코드 한 줄 쓰기 전이 unknown을 잡아내는 가장 저렴한 자리다. 이 단계에서 그는 네 가지 방식을 제시한다.

**Blindspot pass.** 낯선 영역에 발을 딛기 전에 "내가 무엇을 모르는지 모르는 채로 시작한다"고 Claude에게 알려주는 프롬프트다. 아직 자신에게 unknown이 있음을 인정하는 것 자체가 프롬프트의 핵심이다.

> "I'm working on adding a new auth provider but I know nothing about the auth modules in this codebase. Can you do a blindspot pass to help me figure out my relevant unknown unknowns and help me prompt you better."

색보정처럼 전문 지식이 필요한 영역이면 이렇게 부탁한다.

> "I don't know what color grading is but I need to grade this video. Can you teach me to understand my unknown unknowns about color grading, so that I can prompt better?"

**Brainstorms and prototypes.** 보기 전엔 뭘 원하는지 알 수 없는 문제에는 HTML 목업을 여러 방향으로 만들게 해서 반응을 본다.

> "I want a dashboard for this data but I have no visual taste and don't know what's possible. Make me an HTML page with 4 wildly different design directions so I can react to them."

> "Before wiring anything up, make a single HTML file mocking the new editor toolbar with fake data. I want to react to the layout before you touch the real app."

> "Here's my rough problem: users churn after onboarding. Search the codebase and brainstorm 10 places we could intervene, from cheapest to most ambitious. I'll tell you which ones resonate."

**The tweakable plan.** 실행 계획을 HTML로 쓰되, 실행 순서가 아니라 "내가 손댈 확률이 높은 결정"부터 위로 올린다. 데이터 모델 변경, 새 타입 인터페이스, 사용자에게 닿는 결정 같은 것들이다. 반복 리팩토링처럼 기계적인 부분은 아래로 밀어 넣는다.

> "Write an implementation plan in HTML, but lead with the decisions I'm most likely to tweak with: data model changes, new type interfaces, and anything user-facing. Bury the mechanical refactoring at the bottom, I trust you on that part."

**The interview.** 애매한 기능은 Claude가 나를 인터뷰하게 한다. 아키텍처 파급 반경이 큰 질문부터 순서대로 하나씩 던지게 하고, 답을 모으면 곧바로 실행 프롬프트로 이어진다.

### 구현 중 — 예상하지 못한 이탈을 기록한다

아무리 계획을 잘 세워도 영토에는 unknown이 숨어 있다. Thariq은 이 단계에서 "implementation notes"라는 러닝 로그를 두기를 권한다.

> "Keep an implementation-notes.md file. If you hit an edge case that forces you to deviate from the plan, pick the conservative option, log it under 'Deviations', and keep going."

계획에서 벗어나야 했던 지점마다 보수적인 선택을 남기고, 왜 벗어났는지 짧게 적어두면, 다음 시도가 훨씬 똑똑해진다.

### 구현 후 — 남에게 넘겨줄 unknown을 정리한다

배포한다는 건 결국 다른 사람이 내 unknown을 물려받는다는 뜻이다.

**Pitches and explainers.** 프로토타입, 스펙, 실행 노트를 하나의 인수인계 문서로 묶는다. 리뷰어가 던질 만한 반박을 미리 답해두고, 승인이 필요한 사람과 항목을 명시한다.

> "Package the prototype, the spec, and the implementation notes into a single doc I can drop in Slack to get buy-in. Lead with the demo GIF."

**Quiz me before I merge.** 머지 전에 내가 실제로 이해했는지 스스로 확인한다. 14개 파일 변경분에 대해 여섯 문항 퀴즈를 만들고, 틀린 답은 내가 훑고 지나간 정확한 섹션으로 돌려보낸다.

## 11개 HTML 데모

Thariq은 이 방법론을 말로만 남기지 않았다. 실제로 인터랙티브 HTML 페이지 11개로 데모를 만들어 [thariqs.github.io/html-effectiveness/unknowns](https://thariqs.github.io/html-effectiveness/unknowns/)에 공개했다.

| 단계 | 데모 |
| --- | --- |
| Pre (8개) | Blindspot pass, Teach me my unknowns(색보정 인터랙티브 해설), Four design directions, Mock before you wire, Brainstorm the intervention, The interview, Point at a reference, The tweakable plan |
| During (1개) | Implementation notes(러닝 로그 실제 예시) |
| Post (2개) | The buy-in doc, Quiz me before I merge |

각각의 데모는 "Claude가 이 순간 어떤 산출물을 만들어야 하는가"의 시각적 답이다. 프롬프트 → 결과물 → 사람이 반응하는 인터랙션까지 하나의 HTML 페이지 안에 들어 있다.

## 실사용례 — Fable 5 발표 영상은 Fable이 편집했다

Thariq 자신이 이 방법론을 가장 크게 시연한 것이 Fable 5 발표 영상이다. 그는 영상 편집기를 한 번도 열지 않았다.

- ElevenLabs로 17개 테이크의 워드 레벨 타임스탬프를 뽑는다.
- Claude가 이 타임스탬프를 grep으로 뒤져 각 씬에서 최고의 테이크를 고른다. 판정 근거("C012의 마지막 테이크는 ums가 하나도 없다, 인트로 웜업이 66.40에 끝나므로 66.45가 침묵 구간이라 커팅 지점으로 안전하다")까지 JSON에 함께 적힌다.
- final-edit.json이 곧 편집본이다. 프로젝트 파일이 아니라 위에서 아래로 읽을 수 있는 텍스트다.
- ffmpeg가 JSON을 실행한다. Claude가 컷된 결과물을 다시 전사해 "zero ums"를 확인한다.
- 로어서드, 키포인트 같은 오버레이 큐는 워드 타임스탬프에서 특정 문구를 grep해서 그 지점에 붙인다. 타임라인 스크러빙이 없다.
- 컬러 그레이딩은 "그레이딩이 너무 밋밋하다"고 말로 지시했고, 디자인 팀은 Figma MCP를 통해 익숙한 도구 안에서 손댔다.

이 워크플로우 자체가 unknown을 발견하는 프로세스였다. Thariq은 색보정을 몰랐고, 편집 소프트웨어의 관습도 몰랐지만, Claude에게 "내 unknown을 가르쳐달라"고 계속 요청하면서 진행했다.

## 가장 눈여겨본 것은

내가 곱씹은 대목은 unknown의 4분면 자체가 아니라, Thariq이 "언어로 옮기지 못한 것"을 다루는 방식이었다. Unknown Knowns — 알지만 언어로 꺼내지 못한 암묵지 — 를 Claude에게 인터뷰나 HTML 목업으로 끌어내는 흐름은, 결국 에이전트를 상대로 자신을 취조하는 프로토콜이다.

한국에서 이런 대화를 사람 사이에서 자주 못 갖는 이유는 시간 문제만이 아니다. 상대의 unknown을 진단하는 대화 자체가 위계와 얽혀 있기 때문에 서로가 방어적이 된다. Claude와의 blindspot pass는 그 위계가 없다. 내가 아무것도 모른다고 인정하는 프롬프트를 부담 없이 던질 수 있고, 상대는 판단하지 않고 나열만 해준다.

또 하나 눈여겨본 것은 "실행 순서가 아니라 손댈 확률로 정렬된 실행 계획"이라는 발상이다. 계획서의 순서가 실행 순서를 따라야 한다는 습관이 얼마나 낭비인지 새삼 보였다. 리뷰어가 반응할 가능성이 높은 결정을 위로 올리면, 실제로 반응이 필요한 지점만 대화가 된다. 기계적인 일은 위임하면 그만이다.

## 출처

Thariq Shihipar (@trq212), Anthropic Claude Code 팀
"A Field Guide to Fable: Finding Your Unknowns", 2026-07-03
원문 아티클: <https://x.com/i/article/2073090223194755072>
트윗: <https://x.com/trq212/status/2073100352921215386>
데모 페이지: <https://thariqs.github.io/html-effectiveness/unknowns/>
