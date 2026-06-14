---
title: "Coding Is No Longer the Constraint: Scaling Developer Experience to Teams and Agents at Spotify"
date: 2026-06-14T20:00:00+09:00
tags: ["AI 코딩", "Anthropic", "코딩 에이전트", "플랫폼 엔지니어링", "조직 변화"]
categories: ["다이제스트"]
summary: "Spotify가 사내 AI 코딩 도구 채택과 백그라운드 에이전트 Honk를 공개한 자료. 수년 전 만든 Backstage·Fleet Management·Soundcheck가 에이전트의 가드레일이 됐고, 병목이 코딩에서 의사결정으로 이동했다는 것이 골자다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/spotify-coding-no-longer-constraint/cwc01-header.png"
images:
  - "/images/spotify-coding-no-longer-constraint/cwc01-header.png"
---

![Feature Image](/images/spotify-coding-no-longer-constraint/cwc01-header.png)

## 3줄 요약

1. Spotify Engineering이 Code with Claude 2026 강연을 정리해 공개한 자료다. 발표자는 Niklas Gustavsson(Spotify Chief Architect & VP of Engineering).
2. 사내 AI 코딩 도구 채택은 *완전히 미친 수준* — 엔지니어 99%가 매주 사용, 94%가 생산성 향상을 체감, PR 빈도는 76% 증가했다. 핵심은 도구 자체가 아니라 *수년 전부터 다져온 플랫폼*(Backstage, Fleet Management, Soundcheck)이 에이전트의 컨텍스트와 가드레일이 됐다는 점이다.
3. 백그라운드 코딩 에이전트 Honk가 마이그레이션을 자동화하면서 병목은 코딩에서 *결정과 리뷰*로 이동했다.

## "완전히 미친" 채택률

Spotify에서 사내에 새 도구를 도입한 일은 수도 없이 많지만, AI 코딩 도구만큼 빠르게 채택된 경우는 한 번도 없었다고 한다. Opus 4.5 출시 이후 그래프는 다시 한 번 가속됐다.

- 엔지니어 <strong>99%</strong>가 매주 AI 코딩 도구 사용
- <strong>94%</strong>가 AI로 생산성이 올랐다고 보고
- PR 빈도 **76% 증가** — 대부분 *사람 + AI 에이전트* 공동 작성

![Spotify의 AI 전환 — 연말 휴가철에 잠시 떨어지지만, 오렌지색 라인이 Opus 4.5 출시와 함께 폭발적으로 올라간다](/images/spotify-coding-no-longer-constraint/cwc02-ai-transition.png)

> "We roll out tools internally all the time to make our developers more productive, but we have never seen the rate of adoption that we've seen rolling out AI coding tools."

## 에이전트가 등장하기 전부터 시작된 여정 — Fleet Management

몇 년 전 Spotify는 프로덕션 코드베이스가 *엔지니어 수보다 7배 빠르게 성장*하고 있다는 사실을 발견했다. 개발자들은 신규 기능보다 의존성 업그레이드, API 마이그레이션, 보안 패치 같은 *유지보수*에 점점 더 많은 시간을 쓰고 있었고, 마이그레이션은 사내 개발자 불만 1위였다.

수백 개 팀에게 각자 자기 컴포넌트를 수동으로 갱신하라고 시키는 대신, Spotify는 *수백·수천 개 컴포넌트를 한 번에 변경하는 자동화*를 상상했다. 이 아이디어가 **Fleet Management**가 되었고, 그 실행 엔진이 **Fleetshift**다. 현재까지 누적 **자동 PR 250만 건**, 대부분은 사람의 개입 없이 자동 머지됐다.

![Fleetshift를 통한 자동 PR의 누적 증가. 초록색 영역이 자동 머지된 PR이다](/images/spotify-coding-no-longer-constraint/cwc03-shifts.png)

> "Instead of doing this component per component and fairly manually, can we imagine a way where we do this as a way to mutate our entire fleet of components?"

## Honk — 백그라운드 코딩 에이전트

Fleet Management는 단순한 변경에는 잘 들어맞았지만, *복잡한 코드 수정*(API 호출 교체, 사용 패턴 리팩토링)에서는 결정론적 스크립트가 한계에 부딪혔다. 수백만 줄, 수천 개 컴포넌트를 가로지르면 모든 코너 케이스가 한 번씩 튀어나오기 때문이다.

LLM이 성숙하면서 Spotify는 *결정론적 스크립트를 계속 복잡하게 만드는 대신 모델에게 맡기는 길*을 시도했다. 그 결과가 Honk다.

![Code with Claude 2026에서 공개된 Honk](/images/spotify-coding-no-longer-constraint/cwc04-meet-honk.png)

> "It has a silly name and a silly icon, but it's a very useful tool, as it turns out."

Honk의 내부 구조는 다음과 같다.

- **Claude를 Agent SDK로 구동** — 모델 호출은 Anthropic SDK 표준 흐름을 따른다.
- **사내 harness로 감싼다** — 도구 허용 목록, 안전 가드, 실행 추적.
- **Kubernetes pods에 배포** — 다수 세션을 동시에 스케줄, 클라우드 환경 전체에 분산.
- **CI 환경에서 빌드 실행 권한** — 여러 OS에 걸쳐 자기가 만든 변경이 통과하는지 직접 검증한다.

Honk는 Fleet Management 도구 안에 들어앉아 있다. **Fleetshift가 오케스트레이션**을 맡고(대상 식별, 변경 스케줄, 진행 추적), **Honk는 그 가운데서 실제 코드 수정**을 수행한다. 마이그레이션을 돌리는 팀은 PR이 몇 개 생성됐고 몇 개가 머지됐는지, 어떤 PR이 사람의 손이 필요한지 한 화면에서 본다.

![Honk를 Fleet Management에 끼워 넣는 구조](/images/spotify-coding-no-longer-constraint/cwc05-honk-plus-fleetshift.png)

![Fleetshift 플러그인 UI](/images/spotify-coding-no-longer-constraint/cwc06-fleetshift-plugin.png)

가장 최근의 Java 백엔드 마이그레이션은 **3일** 만에 끝났다.

> "What used to be hundreds of teams doing migrations for their components, taking weeks and weeks or months, now can be done by a single engineer in a few days."

개발자들은 곧바로 새로운 사용법을 찾아냈다. 이제 Honk는 Slack에서도 호출 가능하다 — 대화 중에 멘션하면(자연스러운 컨텍스트 원천이다) Honk가 날아가 작업을 마치고 PR을 들고 돌아온다.

![Goose Farm — 사내 실시간 대시보드. 각 거위 한 마리가 Honk로 구동되는 활성 백그라운드 코딩 세션이다](/images/spotify-coding-no-longer-constraint/goose-farm.gif)

Honk v2에서는 **멀티플레이어 협업**이 도입된다 — 공유 에이전트 세션, 팀 프로젝트, Chirp를 통한 에이전트 오케스트레이션. 한 명의 개발자가 한 터미널에서 쓰는 도구가 아니라, *여러 개발자·팀과 동시에 협업하는* 에이전트 시대를 향한다.

## 개발자 경험(DevEx)은 에이전트에게도 필요하다

Spotify의 가장 오래된 엔지니어링 원칙 중 하나:

> "The fewer technologies we are world-leading in, the faster we go."

AI보다 한참 앞서 만들어진 원칙이다. 적은 수의 기술에 집중함으로써 더 깊은 전문성을 쌓고, 팀이 매번 선택을 다시 하지 않아도 되며, 코드베이스 전반의 협업이 쉬워진다. Spotify의 일반적인 백엔드 서비스는 *다른 백엔드 서비스와 거의 같은 모양*을 하고 있다 — 같은 기술 스택, 거의 같은 설계 패턴.

이 원칙이 에이전트에게도 똑같이 중요하다는 사실이 드러났다. *참조할 수 있는 비슷한 코드가 많을수록* Claude의 성능이 측정 가능한 수준으로 개선되고, 반대로 *파편화된 코드베이스*에서는 에이전트 성능이 측정 가능하게 나빠진다.

> "If Claude has a lot of other code to look at, and that code looks roughly consistent, Claude will do a better job. That's what we're seeing."

이 일관성의 출발점이 **Backstage** — Spotify가 오픈소스로 공개한 사내 개발자 포털(IDP)이다. Backstage 도입 전 Spotify는 사내 도구가 *100개 정도*로 흩어져 있었다(배포는 이 도구, CI는 저 도구, A/B 테스트는 또 다른 도구). Backstage는 이것을 *컴포넌트 카탈로그를 중심으로 한 단일 창*으로 통합했다. 오늘날 컴포넌트와 관련된 모든 작업은 Backstage에서 일어난다.

![Backstage 소프트웨어 카탈로그 — 사람도 에이전트도 컴포넌트의 모든 정보를 여기서 찾는다](/images/spotify-coding-no-longer-constraint/cwc08-backstage-context.png)

흥미로운 점은 *이 단일 창이 에이전트에게도 그대로 작동한다*는 것이다. Spotify는 Backstage의 기능을 MCP와 CLI 도구로 노출했고, Claude는 컴포넌트 소유자를 조회하거나, 문서를 읽거나, 책임 팀에게 Slack으로 핑을 보낼 수 있다.

또 Backstage 위에는 **Soundcheck**와 **golden state**가 올라간다. Golden state는 각 컴포넌트 유형의 *권장 기술과 관행*을 정의하고, Soundcheck는 팀이 자기 컴포넌트를 그 기준에 비추어 자가 진단할 수 있는 UI를 제공한다. 여기에 정적 분석과 린트가 결합되면 이 표준은 *능동적 가드레일*로 변한다 — Claude가 사내 인프라에 맞지 않는 패턴을 사용하면 린트 시스템에서 즉시 피드백을 받고 스스로 교정한다.

![Golden state는 도달점이 아니라 여정으로 정의된다](/images/spotify-coding-no-longer-constraint/cwc09-golden-state.png)

> "When Claude works in our codebase, it will get immediate feedback on if it's using the right set of technologies and right set of design patterns."

이 피드백 루프는 사람과 에이전트 모두에게 동일하게 작동한다.

## 코딩은 더 이상 병목이 아니다

코딩 속도가 올라가면 제약은 *사람의 결정*으로 옮겨간다. Spotify는 늘 capacity보다 아이디어가 많은 회사였지만, 이제는 누구든 클라이언트 모노레포에 Claude를 열어 *몇 분 안에* 기능 아이디어를 시제품으로 만들 수 있다. CEO조차 그렇게 프로토타입을 만들고 있다고 한다.

> "This has brought prototyping from something that could take days or weeks to literally taking minutes now."

반대 면도 있다 — *리뷰해야 할 PR이 76% 늘었다*. Spotify는 어떤 부분에 사람의 판단을 적용해야 하는지 학습 중이다. 안전한 것은 자동 머지하고, 가장 중요한 곳에 리뷰를 집중시키고, *병목이 코딩에서 의사결정으로 옮겨가는 흐름에 맞게 계획과 우선순위를 다시 짠다*.

수년 전에 Fleet Management, Backstage, 엔지니어링 표준화에 들인 투자가 *지금 시점에* 결정적인 자산이 됐다는 것이 결론이다.

## 가장 흥미로운 지점

이 자료에서 가장 인상 깊은 대목은 *새 인프라를 어떻게 만들었는가*가 아니라 *이미 있던 인프라가 에이전트 시대에 어떻게 재해석되는가*다. Backstage·골든 스테이트·Soundcheck는 본래 *인간 개발자의 표준화*를 위해 만들어졌지만, 결과적으로 *에이전트의 컨텍스트와 가드레일* 역할을 하고 있다. "에이전트를 위한 DevEx"라는 새 카테고리는 그리 새로운 것이 아니라 *기존 플랫폼 엔지니어링의 자연스러운 연장*에 가깝다. 사람과 에이전트가 같은 컨텍스트·같은 표준·같은 피드백 루프 위에서 일한다는 그림은, 사실 *플랫폼이 충분히 잘 만들어졌을 때 자연히 도달하는 상태*다.

또 하나는 "병목이 이동했다"는 명제가 슬로건이 아니라 *경험적 부담*으로 드러난다는 점이다. PR 76% 증가는 그저 좋은 숫자가 아니라 *리뷰 capacity를 어떻게 분배할 것인가*라는 새로운 조직 문제다. AI 시대의 핵심 문제는 코드 생산량이 아니라 *결정과 검토의 흐름을 어디서 어떻게 막을 것인가*다.

## 출처

- 발신 기관: Spotify Engineering
- 발표자: Niklas Gustavsson (Spotify Chief Architect & VP of Engineering)
- 발표: Code with Claude 2026
- 게시: 2026년 6월
- 원문: <https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint>
- 함께 보기: [Fleetshift](https://backstage.spotify.com/fleetshift), [Honk part 4 — Background coding agents for dataset migrations](https://engineering.atspotify.com/2026/4/background-coding-agents-dataset-migrations-honk-part-4), [Backstage](https://backstage.spotify.com/)
