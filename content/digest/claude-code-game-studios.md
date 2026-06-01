---
title: "Claude Code Game Studios"
date: 2026-05-15T08:15:00+09:00
tags: ["AI", "코딩 에이전트", "Claude Code", "게임 개발", "오픈소스 템플릿"]
categories: ["다이제스트"]
summary: "Claude Code 세션 하나를 49 에이전트·73 스킬짜리 가상 게임 스튜디오로 운영하는 오픈소스 템플릿. 실질 강점과 과장 지점을 갈라 보고, 효용이 빛나는 맥락과 부분 채택 가치를 정리한다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Donchitos가 공개한 오픈소스 Claude Code 템플릿이다. 디렉터·부서 리드·스페셜리스트 3계층 49명의 서브에이전트와 73개의 슬래시 스킬, 12개의 훅, 11개의 경로 스코프 규칙으로 게임 개발 전 과정에 "스튜디오의 구조"를 입힌다.[^github-donchitos]
2. 강점은 분명하다 — 경로 스코프 규칙으로 코딩 표준이 자동 강제되고, MDA·SDT·Bartle·Flow 같은 게임 디자인 이론이 에이전트 프롬프트에 명시적으로 박혀 있다. 엔진별 LLM 지식 컷오프 갭을 문서로 다루는 정직함도 인상적이다.
3. 그러나 출시 이력이 단일 squash 커밋으로 압축되어 검증이 어렵고, 솔로 인디 개발자를 표방하면서 50인 스튜디오 구조를 그대로 옮긴 점은 과장에 가깝다. 통째로 적용하기보다 부분 채택을 권한다.

## 시스템 개요

리포 이름이 곧 슬로건이다. "Claude Code 세션 하나를 통째로 게임 개발 스튜디오로 만든다."

> 49 agents. 73 skills. One coordinated AI team.

구성 요소를 표로 옮기면 다음과 같다.

| 항목 | 수량 | 설명 |
|------|-----:|------|
| Agents | 49 | 디자인·프로그래밍·아트·오디오·내러티브·QA·프로덕션 전반 스페셜리스트 |
| Skills | 73 | 워크플로우 단계별 슬래시 커맨드 (`/start`, `/design-system`, `/dev-story` 등) |
| Hooks | 12 | 커밋·푸시·에셋·세션 라이프사이클·에이전트 감사 자동 검증 |
| Rules | 11 | 게임플레이·엔진·AI·UI·네트워크 코드 경로별 코딩 표준 |
| Templates | 41 | GDD·UX 스펙·ADR·스프린트 플랜·HUD·접근성 등 문서 템플릿 |

에이전트는 3계층으로 분할된다. 디렉터(Opus 3명) — 부서 리드(Sonnet 8명) — 스페셜리스트(Sonnet/Haiku 38명). 디렉터는 비전·아키텍처·일정을 지키고, 리드는 도메인을 소유하며, 스페셜리스트가 실작업을 맡는다. 엔진별로는 Godot 4·Unity·Unreal Engine 5에 대해 각각 리드와 서브 스페셜리스트(GDScript / DOTS·ECS·Addressables·UI Toolkit / GAS·Blueprints·Replication·UMG)가 따로 마련되어 있다.

모든 에이전트는 동일한 협업 프로토콜을 강제한다.

> Question → Options → Decision → Draft → Approval

"자율 실행"이 아니라 "사용자 주도 협업"이라는 것을 시스템 차원에서 못박는다. `AskUserQuestion` 도구로 옵션을 클릭형 UI로 잡아내는 패턴까지 명시되어 있다.

## 실질 강점

### 1. 경로 스코프 규칙으로 코딩 표준 자동 강제

리포지토리의 디렉토리만 봐도 어떤 규칙이 발화되는지가 정해진다.

| 경로 | 강제 항목 |
|------|----------|
| `src/gameplay/**` | 데이터 드리븐 값, delta time 사용, UI 참조 금지 |
| `src/core/**` | 핫패스 zero-allocation, thread safety, API 안정성 |
| `src/ai/**` | 성능 예산, 디버깅 가능성, 데이터 드리븐 파라미터 |
| `src/networking/**` | 서버 권위, 버전드 메시지, 보안 |
| `src/ui/**` | 게임 상태 미소유, 로컬라이제이션 준비, 접근성 |
| `design/gdd/**` | 8개 필수 섹션, 수식 포맷, 엣지 케이스 |
| `tests/**` | 테스트 네이밍, 커버리지, 픽스처 패턴 |

파일 경로만 보고 규칙이 자동 발화하므로 사람이 매번 "Claude에게 규칙을 다시 알려주기"를 안 해도 된다. 이 패턴 자체는 게임이 아닌 어떤 코드베이스에도 옮길 수 있다.

### 2. 12개 훅으로 게이트·감사 자동화

훅은 PostToolUse·Session·Notification 이벤트에 묶여 있다. `validate-commit.sh`는 하드코딩 값·JSON 유효성·디자인 문서 섹션을 검사하고, `validate-push.sh`는 보호 브랜치 푸시에 경고를 띄우며, `pre-compact.sh`/`post-compact.sh`는 컴팩션 전후로 세션 상태를 보존한다. `log-agent.sh`/`log-agent-stop.sh`는 서브에이전트 호출의 감사 추적을 남긴다. POSIX 호환으로 작성되어 macOS·Linux에서도 무난히 돈다.

### 3. 게임 디자인 이론을 명시적으로 박아둠

`creative-director.md`, `game-designer.md` 같은 에이전트 프롬프트는 다음 프레임워크를 결정 근거로 명시한다.

- MDA (Mechanics-Dynamics-Aesthetics)
- Self-Determination Theory (자율성·역량감·관계성)
- Flow State Design
- Bartle 플레이어 유형
- Verification-Driven Development

에이전트가 "이 옵션이 좋습니다"라고 말하기 전에 어떤 이론을 근거로 삼는지를 매번 요구받는 구조다. 게임 디자인 이론이 약한 사용자에게는 살아 있는 강의록이기도 하다.

### 4. LLM 지식 컷오프와 엔진 버전 갭을 정직하게 문서화

`docs/engine-reference/godot/VERSION.md`에는 이런 표가 있다.

> LLM 훈련 데이터는 Godot ~4.3까지 커버하며 4.4·4.5·4.6은 모름. API 호출 제안 전 반드시 이 디렉토리를 교차 참조하라.

| 버전 | 출시 | 위험도 | 주요 테마 |
|------|------|--------|----------|
| 4.4 | \~2025년 중반 | MEDIUM | Jolt physics, FileAccess 반환형, 셰이더 텍스처형 |
| 4.5 | \~2025년 말 | HIGH | 접근성(AccessKit), variadic args, @abstract, SMAA |
| 4.6 | 2026년 1월 | HIGH | Jolt 기본, glow 재작업, Windows D3D12 기본 |

모델이 모르는 것을 모른다고 시스템적으로 다루는 드문 사례다. 빠르게 진화하는 라이브러리(React·Bun·Anthropic SDK 등)에도 그대로 옮길 만한 메타 패턴이다.

### 5. 스킬·에이전트 자체에 대한 테스트 프레임워크

리포 안에 `CCGS Skill Testing Framework/` 디렉토리가 있다. 스킬 73개·에이전트 49개 각각에 행동 사양(5개 테스트 케이스 + 프로토콜 준수 어서션)이 붙어 있고, 카테고리별 품질 루브릭과 마스터 카탈로그가 들어 있다. `/skill-test`, `/skill-improve` 슬래시 스킬로 시스템 스스로를 검증한다. 프롬프트 자체를 회귀 테스트 대상으로 본다는 점이 메타다.

## 의심·과장 지점

여기서부터 다이제스트의 결을 가른다. 강점이 진짜라고 해서 적용이 정답이 되지는 않는다.

### 1. 단일 squash 커밋 — 출시 이력 검증 불가

공개 리포의 git log는 다음 한 줄뿐이다.

> 984023d Release v1.0.0 — concept-prototype/vertical-slice split, workflow restructure, polish (#50)

UPGRADING.md에는 v0.1.0 → v1.0.0 마이그레이션이 자세히 적혀 있지만, 그 과정은 외부에서 검증할 수 없다. 무엇보다 이 템플릿으로 실제 출시된 게임의 사례가 README·디스커션에 공시되어 있지 않다. "AI 스튜디오의 효용"은 저자 주장과 프롬프트 품질로만 추론해야 한다.

### 2. 솔로 표방, 50인 스튜디오 구조 복제

README는 솔로 인디 개발자를 첫 독자로 호명한다.

> Building a game solo with AI is powerful — but a single chat session has no structure.

그런데 실제 구조는 디렉터·부서 리드·스페셜리스트로 분화된 중대형 스튜디오를 그대로 옮긴 것이다. `/retrospective`·`/milestone-review`·`/architecture-decision` 같은 산출물 중심 스킬은 본디 부서 간 합의를 만들기 위한 도구인데, 합의할 부서가 없는 솔로에게는 자기 자신과의 회의가 된다.

### 3. 다단 위임 → 토큰 비용 폭증 위험

디렉터(Opus) → 리드(Sonnet) → 스페셜리스트(Sonnet/Haiku) 수직 위임 + 동급 컨설팅 + 충돌 시 에스컬레이션 구조는 한 결정마다 여러 서브에이전트를 깨운다. `/team-*` 스킬은 한 번에 3~5개 에이전트를 병렬로 띄운다. 자가 부담으로 API를 쓰는 솔로 입장에서 한 스토리당 비용이 게임 출시 전에 한도를 갉아먹을 수 있다.

### 4. 산출물 다수가 문서 — 과정 페티시 위험

리포의 392개 마크다운 중 산출물이 8섹션 GDD, ADR, 스프린트 플랜, 회고록, 패치 노트, GDD 일관성 보고서다. 본디 큰 팀의 합의 비용을 낮추기 위한 도구가, 합의가 필요 없는 단일 결정자에게는 "실제 코딩 전에 만들어야 할 문서 더미"로 변모한다. `/brainstorm` → `/design-system` → `/review-all-gdds` → `/gate-check` 사이에서 코드 한 줄 없이 한 달이 사라질 수 있는 함정.

### 5. src·design 디렉토리는 비어 있다

리포의 `src/`, `design/`, `assets/`, `tests/`에는 `CLAUDE.md` 한 장만 두고 비어 있다. 즉 이 시스템은 "게임을 만드는 도구"가 아니라 "게임 만드는 방식을 만드는 메타 도구"다. 실제 게임을 끌고 가다 만난 마찰을 통해 다듬어졌다는 증거가 리포 안에는 없고, 자기 테스트 프레임워크는 시스템 내부 일관성만 보장한다.

## 효용이 빛나는 맥락

의심을 다 쏟아냈지만 이 시스템이 진짜로 빛나는 자리들이 있다. 다음 세 가지 상황이라면 도입을 적극 권한다.

### A. 흩어진 중간 단계 프로젝트의 정리 발판

`/adopt`, `/project-stage-detect`, `/reverse-document` 스킬은 이미 굴러가던 프로젝트를 시스템 안으로 끌어들이는 진입로다. 코드와 일부 디자인이 있지만 다음 무엇을 할지 모르겠는 상태, 즉 "AI로 빠르게 만들었는데 구조가 없어 손을 못 대는" 단계에서 가장 효용이 크다. 게이트·리뷰 강도를 `lean`·`solo`로 낮춰 시작하면 오버헤드도 통제된다.

### B. 2-5인 팀에서 AI로 부서 채우기

부서 구조는 솔로보다 2-5인 팀에서 더 자연스럽다. 디렉터 역할은 사람이 맡고 AI를 부서 리드·스페셜리스트로 부리는 매핑이 가능하며, 협업 프로토콜의 "Question → Options → Decision → Draft → Approval"은 사람-AI 인계 지점을 명시한다. 사람 사이 합의 비용을 키우지 않으면서 도메인 전문성만 확장하는 용도.

### C. 게임 디자인 프레임워크가 약한 학습자

MDA·SDT·Bartle·Flow 같은 이론을 들어만 봤거나 처음 접한 학습자에게 에이전트 프롬프트는 살아 있는 강의록이다. `game-designer.md`, `creative-director.md`를 정독하는 것만으로도 결정의 근거를 어떻게 잡는지 배울 수 있다. 코드 도구가 아니라 학습 자료로 소비할 때 정가 대비 가치가 가장 높다.

## 부분 채택 가치

통째로 적용하지 않더라도 떼어내 다른 프로젝트에 옮길 만한 패턴이 분명히 있다.

- **경로 스코프 규칙 패턴.** `src/{도메인}/`마다 규칙 파일을 두고 LLM에 자동 첨부되게 하는 패턴은 게임이 아닌 다른 코드베이스에도 그대로 옮길 수 있다. 도메인 경계가 모호한 코드베이스에 디렉토리 단위 규약을 도입하는 강제 장치.
- **8섹션 GDD 포맷.** Overview / Player Fantasy / Detailed Rules / Formulas / Edge Cases / Dependencies / Tuning Knobs / Acceptance Criteria. 인터랙티브 시스템·제품 사양에도 응용 가능한 골격이다. "튜닝 노브"와 "엣지 케이스"를 별도 섹션으로 분리한 점이 실전적.
- **Ask → Options → Decide → Draft → Approve 프로토콜.** 모든 에이전트가 작업 시작 전 질문 → 2-4개 옵션 제시 → 사용자 결정 → 초안 → 승인을 거치게 만든 협업 프로토콜은 AI 에이전트 일반에 적용 가능한 안전 장치다. `AskUserQuestion` 도구로 옵션을 클릭형 UI로 잡아내는 패턴까지 베껴 쓸 만하다.
- **VERSION.md (LLM 컷오프 명시) 패턴.** "LLM 훈련 컷오프는 X까지, 현재 사용 버전은 Y, 그 사이 변경은 외부 문서 참조 강제." 빠르게 진화하는 라이브러리(React·Bun·Anthropic SDK 등) 어디든 응용 가능. 모델이 모른다는 사실 자체를 시스템적으로 다루는 메타 패턴.

## 가장 흥미로운 지점

가장 인상적인 부분은 모순 그 자체다. 시스템은 "스튜디오의 구조 없이 게임을 만드는 솔로의 한계"를 진단하면서, 그 해법으로 50인 스튜디오의 모든 관료 장치를 — ADR, 스프린트 회고, 게이트 체크, GDD 일관성 보고서 — 솔로의 어깨에 얹는다. "구조 없음"이 문제였다면, 정말 필요한 구조의 최소 단위는 어디까지일까?

협업 프로토콜의 "Question → Options → Decide → Draft → Approve"는 그 답에 가장 가깝다. 합의해야 할 부서가 없어도 작동하는 단일 결정자용 5단계이기 때문이다. 만약 이 리포에서 한 가지만 가져간다면 나는 이 5단계를 가져가겠다. 나머지는 솔로보다 큰 팀의 합의 비용을 줄이는 도구로 봐야 정직하다.

## 출처

- 저자: Donchitos
- 라이선스: MIT
- 버전: v1.0.0
- 본문에 의미 있는 이미지가 포함되어 있지 않아 이미지 인용은 생략했다.

원문: <https://github.com/Donchitos/Claude-Code-Game-Studios>

[^github-donchitos]: 원문: <https://github.com/Donchitos/Claude-Code-Game-Studios>
