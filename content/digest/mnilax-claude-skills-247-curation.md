---
title: "I deleted 224 of 247 Claude Skills I tested. Here are the 23 I kept."
date: 2026-05-06T23:25:00+09:00
tags: ["claude-code", "claude-skills", "마켓플레이스", "컨텍스트 관리"]
categories: ["에이전트와 코딩"]
summary: "Mnilax가 6주간 247개 Claude Skill을 측정·삭제하며 23개만 남긴 큐레이션. 핵심은 목록이 아니라 활성 5~7개라는 컨텍스트 상한과 capability 대 discipline의 구분이다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Mnilax(@mnilax)가 6주간 Claude Skill 247개를 격리 환경에서 측정·삭제하고 23개만 남긴 X Article이다. 통과선은 1\~5점 품질에서 +1.5점 또는 핵심 과제 시간 -30%였다.
2. 같은 카테고리에 강자가 있으면 후보는 모두 떨어졌다. 80개는 SKILL.md 스키마 없는 프롬프트 모음, 50개는 기능 중복, 40개는 v2.1 hook 스펙 미대응, 25개는 악성·탈취 의심이었다.
3. 결론은 목록 자체가 아니라 두 가지 운영 원칙이다. 첫째, 활성 스킬은 5\~7개를 넘기지 않는다. 둘째, 능력을 더하는 capability skill보다 출력 스타일을 강제하는 discipline skill에서 품질이 나온다.

![247 tested · 224 deleted · 23 kept](/images/mnilax-claude-skills-247-curation/cover.jpg)

## 측정 방법론

저자는 설치 카운트를 신뢰하지 않았다. 상위 설치 스킬의 절반이 측정 가능한 개선을 만들어내지 못했기 때문이다. 대신 다음 절차를 거쳤다.

1. 각 스킬을 깨끗한 `~/.claude/` 디렉터리에 격리 설치
2. 해당 스킬이 다룬다고 주장하는 대표 과제 5개 실행
3. 베이스라인(스킬 없음) 대비 실행 시간 측정
4. 출력 품질을 1\~5점으로 수동 채점
5. 세션당 주입 토큰(컨텍스트 오버헤드) 추적

통과 조건은 다음 중 하나다.

- 5점 척도에서 품질 +1.5점 이상 향상
- 핵심 과제 실행 시간 30% 이상 단축
- 베이스라인이 아예 못 하던 일을 가능하게 함

탈락 조건은 다음과 같다.

- 측정 가능한 개선 없음
- 반환 가치보다 컨텍스트 추가가 큼
- 이미 설치된 다른 스킬과 충돌(lock-file 진단으로 검출된 cascade)
- 2026년 2월 이후 커밋이 없음

이 기준으로 247개가 23개로 줄었다.

## Tier S — 모든 머신, 모든 프로젝트에 설치 (5개)

측정 결과 가장 큰 향상을 만든 다섯 개다. 이 글에서 하나만 가져간다면 이 다섯이다.

### 1. frontend-design (Anthropic, 27만+ 설치)

UI 코드 작성 전 디자인 방향(brutalist, editorial, retro-futurist 등)을 확정하도록 강제한다. AI 슬롭 룩(Inter 폰트 + 보라 그라디언트 + 그리드 카드)을 제거한다. 가장 큰 효과는 시각이 아니라 일관성이었다 — 일단 방향이 정해지면 이후 컴포넌트가 모두 같은 결을 따른다.

설치 조건: UI가 있는 모든 프로젝트.
스킵 조건: 순수 백엔드/API 작업.

대안으로 `pbakaus/impeccable`이 있다(자동 트리거 1개 대신 23개 명령, 브랜드/제품 모드 분리, Chrome 오버레이가 안티패턴을 페이지에 직접 표시). 둘 중 하나만 깐다 — 같은 작업에서 충돌한다.

### 2. superpowers (obra, 17만 7천+ stars)

즉흥 프롬프팅을 7단계 워크플로우로 대체한다: brainstorm → spec → plan → TDD → subagent execution → review → finalize. TDD 강제는 권고가 아니다. 실패하는 테스트가 없으면 구현 자체를 거부한다.

저자는 느려질 줄 알았는데 그 반대였다. 앞단의 20분 브레인스토밍이 잘못된 방향을 푸는 3시간을 절약했다. 2026년 4월 말 기준 스타 수가 1월의 9만 4천에서 17만 7천으로 뛰어, 올해 가장 빠르게 자란 Claude Code 프로젝트로 꼽힌다.

설치 조건: 한 세션을 넘어가는 모든 기능 개발.
스킵 조건: 자잘한 수정, 탐색용 프로토타입, 단일 파일 스크립트.

### 3. simplify (Anthropic, 주간 약 13만 3천 설치)

최근 수정한 코드를 동작 변경 없이 정리한다. 중첩 삼항, 한 함수가 세 가지 일을 하는 패턴, '그땐 그게 맞았던' 추상화를 노린다. 핵심 규칙은 <strong>"동작은 절대 바꾸지 않고 표현 방식만 바꾼다"</strong>이다. 대부분의 'AI 정리'가 슬그머니 의미를 바꾸는 것과 다르다.

설치 조건: 모든 프로젝트, 코딩 세션 직후 실행.
스킵 조건: 없음.

### 4. skill-creator (Anthropic)

자기 스킬을 만드는 메타 스킬이다. 워크플로우를 안내하고, SKILL.md 초안을 제안하고, 3\~5개 테스트 프롬프트를 돌리고, 실패 사례에 따라 지시를 다듬는다. 다른 모든 스킬을 좋게 만든다.

저자는 이 메타 스킬이 있을 때 자기 스킬을 5분 만에 짰다. 없이 첫 시도를 하다가 오후를 통째로 태웠다고 한다. 숨은 가치는 "이런 스킬이 필요한데 없네"라는 갭 대부분이 SKILL.md 스캐폴딩만 알면 10분짜리 작업이라는 사실을 알게 되는 것이다.

설치 조건: 같은 CLAUDE.md 지시를 두 번째 쓰고 있는 자신을 발견했을 때.
스킵 조건: 진정으로 Claude를 소비만 하고 만들 일이 없는 경우.

Claude Code v2.1+ 기본 활성화. 비활성화되어 있다면 `/plugin install skill-creator@anthropics/claude-code`.

### 5. web-design-guidelines (vercel-labs/agent-skills, 19.5K stars)

접근성·성능·UX를 다루는 100+ 룰셋이다. 최신 Vercel 가이드라인으로 UI 코드를 감사해 위반을 `file:line` 포맷으로 출력한다. ESLint a11y 플러그인이 놓친 포커스 가시성 위반을 잡아낸 사례가 있다 — '문법적으로 유효한 HTML'과 '실제로 쓸 만한 UI'는 다른 기준이다.

설치 조건: frontend-design과 짝으로. 한쪽이 만들고 한쪽이 감사한다.
스킵 조건: UI를 만들지 않을 때.

## Tier A — 도메인이 맞으면 강력한 8개

| 스킬 | 한 줄 요약 |
| --- | --- |
| ui-ux-pro-max (nextlevelbuilder) | 50+ UI 스타일, 97 컬러 팔레트, 57 폰트 페어, 99 UX 룰, 25 차트 타입을 Python CLI로 조회. 빈 Figma에서 시작할 때. |
| composition-patterns (vercel-labs) | 컴파운드 컴포넌트·컨텍스트 프로바이더·명시적 variant. 룰 하나가 설치를 정당화한다 — `architecture-avoid-boolean-props`. |
| valyu (valyuAI/skills) | 웹 검색 + SEC, PubMed, ChEMBL, ClinicalTrials.gov, FRED 등 36+ 전문 데이터 소스. FreshQA 79% 대 Google 39%, 금융 질문에서 73% 대 55%. |
| claude-seo (AgriciDaniel) | DataForSEO 라이브 데이터, 스키마 검증, GEO-first(AI 크롤러용 시타빌리티 스코어링) 12개 서브 스킬. |
| agent-browser | 안정적 element ref로 웹 UI 제어. Playwright MCP가 과한 상황의 대안. |
| excalidraw-diagram | 자연어에서 Excalidraw 스타일 다이어그램. 아키텍처 다이어그램이 의사소통 수단인 팀에. |
| notebooklm-integration | Claude와 NotebookLM 브리지. 스펙·API 레퍼런스·논문을 한 번 업로드하고 인용과 함께 질의. |
| remotion-best-practices (주간 11만 7천 설치) | React로 프로그래머블 비디오 생성. 별도 비디오 워크플로우 없이 데모·릴리스 영상이 필요할 때. |

## Tier B — 트리거 조건이 맞으면 유용한 10개

14. `pdf` (Anthropic) — 폼·청구서·표 추출.
15. `docx` (Anthropic) — 변경 추적 포함 워드 생성·편집.
16. `pptx` (Anthropic) — 자연어로 슬라이드 덱.
17. `xlsx` (Anthropic) — 스프레드시트 생성, 수식, 차트.
18. `marketing-skills` (coreyhaines) — CRO, 카피라이팅, 이메일 시퀀스, 그로스.
19. `mattpocock/skills` — TypeScript 타입 안전성, 마이그레이션.
20. `claude-deep-research-skill` — 자동 이어가기를 포함한 8단계 리서치.
21. `firecrawl` — JS 무거운, 봇 차단 사이트 스크래핑.
22. `obsidian-skills` (Obsidian CEO Kepano) — 오토 태깅, 오토 링킹, 볼트 네이티브.
23. `awesome-claude-skills` (travisvn) — 메타 카탈로그(2.2만 stars). 만들기 전에 둘러보는 곳.

## 224개를 삭제한 패턴

저자는 다 나열하지 않고 실패 패턴으로 정리했다.

- <strong>~80개 — Cursor 스타일 프롬프트 모음.</strong> 일반 룰 50개를 담은 마크다운 한 장. SKILL.md 스키마 없음. 문서로 설치되지만 모델이 CLAUDE.md로도 할 수 있는 것 이상을 제공하지 않는다.
- <strong>~50개 — 기능 중복.</strong> TDD 프레임워크 두 개, 보안 스캐너 세 개, '코드 리뷰어' 다섯 개. 훅을 계측하니 직렬로 실행되며 모순된 출력을 냈다. 카테고리당 하나만 고른다.
- <strong>~40개 — 2026년 2월 이후 미커밋.</strong> Claude Code v2.1에서 hook 스펙이 21개 라이프사이클 이벤트를 추가하며 바뀌었고, 미업데이트 스킬은 조용히 깨졌다. 특히 새로 들어온 `PostToolUseFailure` 이벤트가 이전 실패 모델을 가정하던 '오토 픽스' 스킬들을 무력화했다.
- <strong>~25개 — 악성 또는 탈취 의심.</strong> 패턴: 별 500+, 2026년 2월 이후 생성된 리포, 컨트리뷰터 이력 없음, 의심스러운 패키지 의존. ECC의 AgentShield는 2026년 1월 한 달, 한 마켓에서만 2,857개 중 341개(12%)를 악성으로 보고했다. 새로 등장한 고스타 스킬은 새로 등장한 고수익 지갑처럼 다룬다.
- <strong>~20개 — 사실상 무효.</strong> 깔끔히 깔리고, 충돌도 없고, 부수지도 않지만 측정 가능한 개선이 없었다. 작은 컨텍스트 세금만 남는다.
- <strong>~9개 — 훌륭하지만 23개와 중복.</strong> 명예의 전당: spartan-ai-toolkit, artifacts-builder, tdd-guard, Plannotator, claude-mem.

## 설치 순서가 목록보다 중요하다

23개를 한 번에 깔면 작살난다. 활성 스킬마다 컨텍스트를 더하고, 23개가 한꺼번에 켜지면 첫 프롬프트도 치기 전에 컨텍스트 윈도우가 다 찬다. 게다가 충돌한다(`web-design-guidelines`와 `ui-ux-pro-max`가 같은 작업에서 디자인 페이즈를 두고 싸운다).

저자가 검증한 설치 순서는 다음과 같다.

<strong>Week 1 — 기반 4개(전부 설치):</strong>

1. `skill-creator`(Claude Code v2.1+ 기본 활성)
2. `simplify` / code-simplifier
3. `superpowers`
4. `frontend-design` 혹은 도메인에 맞는 백엔드 등가물 중 하나

<strong>Week 2 — 갭에 따라 1\~2개 추가:</strong>

- UI 작업 → `web-design-guidelines` (+ 필요 시 `ui-ux-pro-max`)
- TypeScript 작업 → `mattpocock/skills`
- 리서치/데이터 → `valyu`
- SEO/콘텐츠 → `claude-seo`

<strong>Week 3+ — 도메인 특화 1\~2개:</strong>

- 문서 무거움 → `pdf`, `docx`, `pptx`, `xlsx` 중 하나(거의 네 개를 다 깔진 않는다)
- 다이어그램 → `excalidraw-diagram`
- 비디오 → `remotion-best-practices`

활성 스킬은 5\~7개에서 멈춘다. 그 이상은 컨텍스트 오버헤드가 가치를 넘는다. 비활성화는 `/plugin disable <name>`.

상한의 이유는 단순하다. 각 스킬은 관련성이 감지될 때마다 SKILL.md를 컨텍스트에 적재한다. 9개 이상이 보수적인 'load when in doubt' 모드로 켜져 있으면, 어느 것도 필요 없는 작업에서도 매번 약 13,500토큰의 스킬 오버헤드를 먼저 치르고 시작한다. CLAUDE.md를 1,200단어로 묶어두는 것과 똑같은 베이스라인 세금이고, 둘 다 누적된다.

움직이는 표적이라면 2주마다 감사를 돌린다. 실제로 발화한 스킬은 어느 것인가. 발화하지 않은 것은 비활성화한다. 새로 생긴 갭이 있으면 한 개만 채운다.

## 잘 되지 않은 접근들

- <strong>`npx skills add` 맹목 설치.</strong> 절반이 SKILL.md frontmatter가 부실해 설치는 됐는데 모델이 절대 호출하지 않았다. 설치 후 항상 `/plugin list`로 확인한다 — 떠 있는데 예상 작업에서 트리거되지 않으면 그 스킬은 망가진 상태다.
- <strong>설치 카운트를 품질 신호로 신뢰.</strong> 상위 30위 중 둘은 벤치마크에서 측정 가능한 개선이 0이었다. 설치 카운트는 마케팅 도달이지 품질이 아니다.
- <strong>'awesome-claude-skills' 리스트에서 일괄 설치.</strong> 같은 문제가 50배. 큐레이트 리스트는 너비를 최적화한다. 자기가 실제 쓰는 스킬에서는 깊이를 원해야 한다.
- <strong>감사 단계 생략.</strong> 첫 2주는 측정 없이 깔기만 했다. 뭐가 도움이 되는지 알 길이 없었다. 베이스라인이 없으면 좋아졌는지 나빠졌는지 판단할 수 없다.
- <strong>web-design-guidelines와 ui-ux-pro-max 동시 설치.</strong> 디자인 페이즈를 두고 둘 다 운전하려 한다. 만들기 도움(ui-ux-pro-max)인지 감사 도움(web-design-guidelines)인지에 따라 하나만 고른다.
- <strong>frontend-design과 impeccable 동시 설치.</strong> 같은 문제, 다른 레이어. 둘 다 미적 취향을 인코딩한다. 하나만.
- <strong>2개월 이상 미업데이트 스킬 설치.</strong> hook 스펙이 바뀌었다. `PostToolUseFailure` 이벤트가 추가됐다. 미업데이트 스킬은 조용한 실패를 만든다. 설치 전 마지막 커밋 날짜를 본다.
- <strong>Search and Tools 기본 기능을 valyu와 동시 사용.</strong> 둘 다 웹 검색을 호출한다. 토큰을 같이 먹고, 어느 쪽도 깨끗한 신호를 받지 못한다. valyu 같은 검색 전문 스킬을 쓸 때는 Anthropic 빌트인 검색을 끈다.

10분짜리 주간 의식: 비활성화는 하되 제거하지 않는다. 30일간 발화하지 않은 스킬은 제거한다.

## Capability vs Discipline — 두 종류의 스킬

저자가 마지막에 던진 분류가 글의 결론이다.

- <strong>Capability skills</strong> — 모델이 못 하던 일을 가능하게 한다. `firecrawl`(적대적 사이트 스크래핑), `valyu`(페이월 데이터), `pdf`(폼 추출), `agent-browser`(UI 자동화). 이게 없으면 모델은 그 작업 자체를 못 한다.
- <strong>Discipline skills</strong> — 모델이 내가 원하는 방식, 내 스타일, 내 컨벤션으로 실행하도록 강제한다. `frontend-design`(미적 취향), `simplify`(코드 스타일), `superpowers`(프로세스), `web-design-guidelines`(감사). 이게 없으면 일반적인 AI 출력이 나온다.

대부분 사용자는 capability 쪽만 깔고 자기 출력이 다른 사람과 똑같아 보이는 이유를 의아해한다. 품질 향상의 대부분은 discipline에서 온다. Tier S 다섯 중 넷이 discipline인 이유다.

## 가장 흥미로운 지점

가장 인상 깊었던 것은 사실 목록이 아니라 컨텍스트 윈도우의 경제학이다. 저자가 정한 5\~7개 활성 상한, 그리고 9개 이상이면 매 작업마다 약 13,500토큰의 스킬 세금이 먼저 깔린다는 추정 — 이 두 숫자가 모든 의사결정의 뼈대다.

같은 저자의 이전 글에서도 결론이 같았다. 모델 능력이나 프롬프트 품질이 아니라 컨텍스트 비대화가 실제 병목이라는 것. 이번 글의 23개 큐레이션은 그 결론의 자연스러운 따름정리에 가깝다 — 활성 컨텍스트의 베이스라인 세금이 정해져 있다면, 거기에 들어갈 자리는 일곱 개뿐이고, 그 일곱 자리는 능력이 아니라 규율에 써야 한다.

또 한 가지 짚어둘 만한 지점은 악성 스킬 비율이다. 한 마켓 한 달치에서 12% 적발이라는 숫자는 결코 작지 않다. 마켓플레이스가 패키지 매니저처럼 자라고 있다면, npm·pip 생태계가 겪은 공급망 공격을 같은 속도로 학습하게 될 가능성이 높다. 설치 전 마지막 커밋 날짜와 컨트리뷰터 이력을 보는 절차가 단순한 충고가 아니라 보안 베이스라인이 되어가고 있다.

## 출처

Mnilax (@mnilax) | X Article | 2026-05-06
원문: <https://x.com/mnilax/status/2051701429987897712>
