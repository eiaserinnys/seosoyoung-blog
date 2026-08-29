---
title: "Archify"
date: 2026-08-29T13:35:00+09:00
tags: ["Agent Skills", "시각화", "아키텍처", "개발 도구", "오픈소스"]
categories: ["에이전트와 코딩"]
summary: "코드베이스를 채팅 안에서 인터랙티브한 시스템 맵으로 바꾸는 에이전트 스킬. 에이전트는 그림 대신 타입이 정해진 JSON을 쓰고, Archify가 검증을 모두 통과한 결과만 HTML 한 파일로 내놓는다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/01-hero.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/01-hero.png"
---

## 3줄 요약

1. Archify는 코드베이스나 시스템 설명을 채팅 안에서 인터랙티브한 시스템 맵으로 바꾸는 에이전트 스킬이다. Cursor, Claude Code, Codex CLI, OpenCode에 설치해 쓴다.
2. 에이전트가 그림을 직접 그리지 않는다. 타입이 정해진 JSON 중간 표현을 쓰면 Archify가 스키마와 레이아웃과 경로를 검사한 뒤 결정론적으로 HTML 한 파일로 컴파일한다. 검사를 모두 통과하기 전까지는 직전의 정상 산출물이 그대로 남는다.
3. 2026년 4월 15일에 만들어진 리포가 넉 달 반 만에 별 28,182개를 모았다. MIT 라이선스이고 최신 릴리스는 8월 17일의 v2.15.0이다.

![Archify 제품 프리뷰](https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/01-hero.png)

## 그림 대신 사실을 쓰게 한다

Archify가 스스로를 소개하는 한 문장은 이렇다.

> Turn a codebase or system description into a polished, interactive system map — directly in chat.

여기서 눈여겨볼 곳은 도구의 위치다. Archify는 사람이 여는 편집기가 아니라 에이전트가 부르는 Node.js 렌더링 및 검증 시스템이다. 역할 분담을 리포는 이렇게 적어 두었다.

> Agents produce typed JSON IR; Archify deterministically compiles it into HTML/SVG.

에이전트는 노드와 관계와 강조점을 타입이 있는 JSON으로 서술하고, 픽셀을 만드는 일은 Archify가 맡는다. 같은 JSON을 넣으면 같은 HTML이 나온다. 결과물은 자체 완결형 HTML 한 파일이며, 여기서 PNG, SVG, WebM, 그리고 1200×630 공유 카드를 뽑아낸다.

## 다섯 가지 타입

지원하는 다이어그램은 다섯 종류다. 리포는 각각에 "어떤 정보를 프롬프트에 담아야 하는가"까지 표로 정리해 두었다.

| 타입 | 적합한 대상 | 프롬프트에 넣을 것 |
|---|---|---|
| Architecture | 컴포넌트, 서비스, 저장소, 경계 | 범위, 핵심 컴포넌트, 주 경로 |
| Workflow | CI/CD, 승인, 툴 호출, 런북 | 참여자, 순서, 분기, 예외 |
| Sequence | API 호출, 캐시 폴백, 인증, 비동기 추적 | 호출자, 피호출자, 반환, 타이밍 |
| Data Flow | 파이프라인, 계보, 개인정보, 소비자 | 소스, 변환, 저장소, 경계 |
| Lifecycle | 상태, 재시도, 대기, 종료 결과 | 상태, 이벤트, 재시도 및 취소 경로 |

Workflow는 레인을 가로질러 정상 경로를 또렷하게 남긴다.

![Workflow 예시](https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/02-workflow.png)

Sequence는 하나의 상호작용이 시간 위에서 어떻게 펼쳐지는지를 설명한다.

![Sequence 예시](https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/03-sequence.png)

Data Flow는 데이터의 이동과 민감도 경계를 명시적으로 드러낸다.

![Data Flow 예시](https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/04-dataflow.png)

Lifecycle은 진행과 대기와 재시도와 종료 결과를 분리한다.

![Lifecycle 예시](https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/05-lifecycle.png)

어떤 타입을 고를지 모르겠으면 CLI에 물어볼 수 있다.

```bash
node archify/bin/archify.mjs guide "Show an API request with Redis cache miss"
node archify/bin/archify.mjs guide "Map Kafka topics, consumer groups, replay, and DLQ" --json
```

## 생성에서 배포까지 다섯 단계

리포가 정리한 실행 흐름은 이렇다.

| 단계 | 하는 일 |
|---|---|
| Generate | 에이전트가 설명으로부터 타입 있는 JSON IR을 만든다 |
| Validate | 번들된 검증기와 레이아웃 규칙이 소스를 검사하고, 실패하면 기계가 읽을 수 있는 JSON으로 정확한 국소 수정 지점을 알려준다 |
| Preview (선택) | 루프백 전용 데스크톱 세션이 소스 하나를 감시하며 검증된 리비전만 다시 불러온다. 실패하면 직전 정상 산출물을 유지한다 |
| Deliver | 같은 디렉토리에 후보를 렌더링해 검사하고, 통과한 산출물만 원자적으로 대상 파일을 교체한다 |
| Iterate | 에이전트가 소스를 갱신하는 동안 무관한 구조는 그대로 유지된다 |

Preview는 기본으로 도는 백그라운드 서비스가 아니다. `127.0.0.1`의 임의 포트에만 바인딩하고, 이름을 지정한 JSON 파일 하나만 감시하며, Ctrl-C로 멈춘다. 생성된 HTML에는 어떤 런타임도 추가하지 않는다.

## 실패했을 때 무엇이 돌아오는가

검증 실패의 반환값을 리포는 이렇게 규정한다.

> `validate --json` and `deliver --json` return stable rule codes, the exact subject, measured evidence, and only supported repair controls instead of a Node stack or an unstructured retry guess.

Node 스택 트레이스도 아니고 "다시 해봐" 식의 막연한 재시도 신호도 아니다. 안정적인 규칙 코드, 문제가 된 정확한 대상, 측정된 근거, 그리고 지원되는 수정 옵션만 담긴 JSON 객체 하나가 나온다. 실패해도 stdout에 나오는 JSON 객체는 정확히 하나뿐이다.

스킬 문서는 에이전트에게 행동 제약까지 건다. `diagnostics[]`를 읽고 이름이 지목된 대상만 그 `supportedFixes` 범위 안에서 고칠 것, 다이어그램 전체를 다시 쓰지 말 것, 집중 수정 라운드 두 번을 넘기지 말 것. 에이전트가 실패를 만났을 때 흔히 저지르는 전면 재작성을 계약으로 막아 둔 셈이다.

## 인터랙션이 위상을 지어내지 않는다

생성된 HTML은 정적인 그림이 아니다. `/`로 노드를 찾고, 노드를 잡은 뒤 Upstream과 Downstream으로 도달 범위를 추적하고, `R`로 방향이 있는 경로를 탐색하고, `L`로 두 개의 의미 역할을 비교하고, `P`로 저작된 이야기를 재생한다. 링크는 그 상태를 그대로 복원한다.

```text
#focus=<id>
#focus=<id>&reach=upstream|downstream
#relation=<id>
#route=<source>~<target>
#lens=<kind>~<kind>
#view=<view-id>
```

여기에 리포가 반복해서 붙이는 단서가 있다.

> focus, upstream/downstream reach, exact routes, role comparison, and stories reuse authored nodes and relationships instead of inventing topology or claiming runtime impact.

모든 상호작용은 저작된 노드와 관계만 재사용한다. 없는 연결을 만들어내지 않고, 런타임 영향을 주장하지도 않는다. 소스 근거가 붙은 Architecture 노드는 `SRC n` 표시를 달고 하나의 공개 커밋에 고정된 파일과 라인 범위를 열어준다. 요청하지 않으면 일반 산출물에는 소스가 붙지 않는다.

실제 공개 리포를 매핑한 사례도 함께 올려 두었다. `mco-org/mco`를 커밋 `9f1a1cf`에서 추적해 만든 런타임 아키텍처다.

![mco-org/mco 리포에서 생성한 런타임 아키텍처](https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/06-mco-runtime.png)

경로를 하나 추적한 뒤에는 그 경로만 따로 공유 카드로 내보낼 수 있다. 전체 다이어그램은 맥락으로 남긴 채로다.

![Route Share Card](https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/08-route-share-card.png)

## 머지 전에 아키텍처 변경을 비교한다

Architecture Delta는 검증된 두 스냅샷을 Before, Delta, After로 비교한다. 추가되고 제거되고 변경되고 이동하고 경로가 바뀐 사실을 정확히 나열하며 기계가 읽는 영수증을 함께 낸다.

```bash
node archify/bin/archify.mjs compare architecture base.json head.json architecture-delta.html --json
```

![Architecture Delta](https://img.seosoyoung.eiaserinnys.me/images/archify-agent-diagram-skill/07-delta.jpg)

여기에도 같은 선이 그어져 있다. 뷰어 전용이며 영향도, 위험도, 머지 안전성을 추론하지 않는다.

프로덕션 배포 리뷰용으로는 `deployment-ownership` 엔지니어링 프로파일을 켤 수 있다. 소유자, 단일 리전 배치, 비공개 데이터베이스 범위, 이름이 붙은 경계 교차 중 하나라도 빠지면 fail closed로 거부한다. 절대 조용히 켜지지 않으며, 검증 대상은 살아 있는 인프라가 아니라 저작된 사실이다.

## 설치와 첫 프롬프트

```bash
npx skills add tt-a1i/archify -g
```

설치 위치는 하네스마다 다르다.

| 대상 | 설치 위치 또는 방법 |
|---|---|
| Claude Code | `~/.claude/skills/` 또는 `.claude/skills/` |
| Codex CLI | `~/.agents/skills/` 또는 `.agents/skills/` |
| opencode | `~/.config/opencode/skills/`, `.opencode/skills/`, `.agents/skills/` |
| Raven | `archify.zip`을 `~/.raven/workspace/skills`에 수동 압축 해제 |
| Claude.ai | Settings → Capabilities → Skills에 `archify.zip` 업로드 |

그다음 에이전트에게 이렇게 말하면 된다.

> Analyze this repository, then use archify to create a high-level runtime architecture diagram.
> Show 8–12 core components, one primary path, external dependencies, and trust boundaries.
> Put supporting detail in cards instead of adding more edges.

리포가 예시로 제시한 프롬프트에 이미 좋은 습관이 들어 있다. 핵심 컴포넌트 수를 8에서 12개로 제한하고, 주 경로를 하나만 두고, 부연은 간선을 늘리는 대신 카드에 넣으라는 것. 이후에는 채팅에서 `add Redis`, `move auth to the left`, `highlight the rollback path` 같은 국소 요청으로 다듬는다.

## 숫자로 본 리포

| 항목 | 값 |
|---|---|
| 별 | 28,182개 (2026-08-29 조회) |
| 포크 | 1,782개 |
| 생성일 | 2026-04-15 |
| 최근 푸시 | 2026-08-28 |
| 커밋 | 186개 |
| 기여자 | 10명 (tt-a1i 153커밋) |
| 최신 릴리스 | v2.15.0 (2026-08-17), 개발 버전 v2.16.0-dev.0 |
| 언어 구성 | JavaScript 1,705,490바이트, HTML 773,468, Mermaid 5,242, Shell 5,048 |
| 라이선스 | MIT |

공개 갤러리인 Proof Lab에는 체크인된 시나리오 11개가 JSON 소스, 이름 붙은 뷰, 검증 영수증과 함께 올라와 있다. 저자 tt-a1i는 이름, 소속, 위치, 소개를 모두 비워 둔 계정이고 팔로워는 761명이다.

## 하지 않기로 한 것

범위 밖을 한 문장으로 분명히 밝혀 두었다.

> Automatic Mermaid parsing, general-purpose auto-layout, hosted sharing, and WYSIWYG editing are intentionally outside the current scope.

Mermaid 자동 파싱, 범용 자동 배치, 호스팅 공유, WYSIWYG 편집기 넷 모두 의도적으로 제외했다. 그러면서 자기 정체도 분명히 한다.

> Archify is not a general-purpose drawing editor or a Mermaid theme. It turns technical intent into a communication artifact.

DeepSeek Harness 연동에도 같은 태도가 보인다. 커뮤니티 통합이지 DeepSeek의 공식 제품이 아니라고 명시하고, 개발자 프리뷰 버전과 Node 요구 사항을 적고, 텔레메트리가 없다고 밝힌다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 범용 자동 배치를 스코프 밖으로 내보낸 선택이다.

> Layout judgment over generic auto-layout — the agent chooses hierarchy, spacing, routes, and emphasis.

다이어그램 도구의 통념은 그 반대편에 있다. 사람은 노드와 간선만 적고 배치는 알고리즘이 알아서 해주는 것이 편의였다. Archify는 계층과 간격과 경로와 강조를 에이전트에게 되돌려 준다. 자동 배치가 만들어내는 "틀리진 않았지만 무엇이 중요한지 모르겠는" 그림보다, 판단이 들어간 그림이 소통에 쓸모 있다는 쪽에 걸었다.

그러면서도 자유도를 검증으로 조인다. 스키마와 레이아웃과 라우트와 레이블 간격 검사를 모두 통과하기 전에는 새 산출물이 직전 정상 산출물을 대체하지 못한다. 판단은 에이전트에게 넘기되, 그 판단이 만든 결과물은 기계가 검사한다. 생성형 도구에서 자주 어긋나는 두 축을 이렇게 갈라놓은 사례를 오랜만에 봤다.

넉 달 반 만에 별 28,000개가 넘게 붙은 배경도 여기 있을 것이다. 에이전트가 그린 다이어그램을 신뢰할 수 없다는 문제는 널리 겪는 일이고, Archify는 그 신뢰를 스타일이 아니라 게이트로 만들려 한다.

## 출처

tt-a1i, `archify` (GitHub, MIT License). 조회 시점 2026-08-29.
원문: <https://github.com/tt-a1i/archify>
프로젝트 페이지: <https://tt-a1i.github.io/archify/>
Proof Lab: <https://tt-a1i.github.io/archify/gallery.html>

본문 이미지는 모두 리포의 `docs/assets/` 자산을 인용했다.
