---
title: "CompozyOS: An operating system for AI agents"
date: 2026-09-19T00:50:00+09:00
tags: ["코딩 에이전트", "멀티에이전트", "하네스", "오픈소스", "자동화"]
categories: ["에이전트와 코딩"]
summary: "에이전트 CLI를 그대로 실행하면서 세션 지속과 권한, 승인, 메모리, 자동화, 감독을 로컬 데몬 하나로 합친 Go 오픈소스 런타임. ACP provider 26종을 등록하고 Loop이라는 계약형 실행 단위로 작업을 끝까지 밀어붙인다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/compozy-agent-os/01-web-shell.png"
  alt: "CompozyOS 웹 셸 화면. 브라우저 안에서 세션 목록과 실행 중인 에이전트 작업을 함께 보여준다"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/compozy-agent-os/01-web-shell.png"
sidenotes: true
---

## 3줄 요약

1. CompozyOS는 Claude Code나 Codex, Gemini CLI 같은 에이전트 CLI를 그대로 실행하는 Go 오픈소스 런타임이다. 개발자가 그 주변에서 매번 손으로 만들던 루프와 크론, 권한, 승인, 메모리, 관측까지 하나의 로컬 데몬으로 합쳤다.
2. 에이전트 CLI 26종을 ACP(Agent Client Protocol) provider로 등록해 실행하며, 세션과 Loop 실행의 소유권을 데몬이 가지므로 터미널 창을 닫아도 작업은 계속된다.
3. 저장소는 2026년 3월 28일에 만들어져 약 6개월 만에 별 2,762개를 모았고, 현재 v0.3 계열은 beta이며, 이전 버전인 v0.2.15는 지원이 중단됐다.

## 저장소 현황

| 항목 | 값 |
| --- | --- |
| 저장소 | `compozy/compozy` |
| 공개 | 2026-03-28 |
| 최근 푸시 | 2026-09-18 |
| 별 | 2,762 |
| 포크 | 179 |
| 열린 이슈 | 12 (열린 PR 3건은 별도) |
| 기여자 | 30명 |
| 라이선스 | MIT |
| 주 언어 | Go 약 61.6MB, TypeScript 약 23.9MB |
| 최신 릴리스 | `v0.3.0-beta.27` (2026-09-15) |
| 홈페이지 | <https://compozy.com> |

위 지표는 2026년 9월 19일에 GitHub API로 조회한 값이다. 릴리스 목록을 보면 8월 10일 `v0.3.0-beta.8`부터 9월 15일 `v0.3.0-beta.27`까지 약 5주 동안 스무 번 넘게 beta를 내놓았다.

## 이 프로젝트가 겨냥한 공백

문서는 먼저 기존 에이전트 CLI가 무엇을 못 하는지를 다섯 줄로 정리한다.

> - 터미널을 닫으면 실행이 사라진다
> - 실행 과정을 다시 재생하거나 감사할 기록이 없다
> - 프로젝트마다 자기만의 컨텍스트와 기본값, 가드레일이 필요하다
> - 여러 전문 에이전트를 조율하려면 결국 직접 만든 접착 코드가 필요해진다
> - 운영자는 끝내 제품으로 발전하지 못하는 스크립트와 로그, 대시보드를 계속 엮게 된다

프로젝트 소개문의 표현을 그대로 옮기면 "누구나 에이전트에게 프롬프트를 줄 수 있지만, 에이전트를 계속 일하게 만드는 것은 여전히 엔지니어링 프로젝트"다. CompozyOS는 그 엔지니어링 전체를 하나의 제품으로 만들겠다고 선언한다.

설치 형태도 그 주장을 따른다. Go 바이너리 하나와 SQLite 기반 저장소로 그치며, Docker나 Postgres를 요구하지 않는다.

```bash
compozy install
compozy daemon start
compozy session new --agent general --name first-run
```

Sigstore 프로버넌스를 검증하는 설치 스크립트로 받아도 되고, `npm install -g @compozy/cli@beta`나 명시적 태그를 붙인 `go install`, 소스 빌드 중에서 골라도 된다. Homebrew는 아직 v0.2 계열을 배포하고 있어서 beta 기간 동안 목록에서 빠져 있고, v0.3.0 정식판과 함께 돌아온다고 한다.

## 데몬이 모든 상태를 소유한다

![CompozyOS의 제어 표면과 데몬, 런타임 리소스, 상태, 확장 경계를 그린 흐름도](https://img.seosoyoung.eiaserinnys.me/images/compozy-agent-os/02-how-it-works.png)

사람과 에이전트가 공개 제어 인터페이스로 명령을 보내면, 사용자 홈 범위에서 도는 데몬이 워크스페이스를 해석하고 권한과 런타임 정책을 적용한 뒤 ACP 에이전트를 조율하고 이벤트와 리소스 상태를 저장한다. 웹 클라이언트와 스트리밍 클라이언트는 자기 나름의 모델을 따로 유지하지 않고 데몬이 소유한 같은 기록을 읽는다.

명령은 여러 표면에서 받는다. CLI(`-o json` 구조화 출력), HTTP/SSE, UDS, MCP(`compozy mcp serve`), 웹 UI, 네이티브 툴이 모두 같은 데몬을 바라본다. 이 표면이 서로 대칭이어야 한다는 것이 문서가 내세우는 설계 원칙이다.

Loop을 예로 들면 작성과 설정, 실행, 관찰, 승인, 취소까지 모든 기능을 `compozy loop` CLI와 Loops HTTP API, `compozy__loop_*` 네이티브 툴에서 쓸 수 있다. 이 세 표면은 웹 UI와 동일한 검증기와 writer를 그대로 호출한다. 웹 UI에서만 되는 기능은 정의상 불완전하다는 것이 문서의 표현이다.

세션 하나하나는 사라지지 않는 작업 단위로 남는다. 실행 중에는 `compozy session resume`으로 연결 권한(attach lease)을 얻어 다른 클라이언트가 붙을 수 있고, 종료된 뒤에도 상태와 요약, 이벤트 기록, 전사가 남아 일반 프롬프트로 같은 기록 위에서 provider를 다시 시작할 수 있다.

설정 값은 세 군데에서 겹쳐 적용된다. 전역 기본값은 홈 디렉터리의 `.compozy/config.toml`에 두고, 워크스페이스가 자기 `.compozy/config.toml`로 일부 필드를 덮어쓰며, 명령줄 플래그가 가장 우선한다.

에이전트 정의도 같은 방식으로 홈과 워크스페이스에 겹쳐 둔다. 각 정의는 `AGENT.md` 한 장과 선택적인 `mcp.json`으로 이루어지며, 워크스페이스 정의는 부분 병합을 하지 않고 통째로 전역 정의를 대체한다.

## provider 26종을 그대로 실행한다

CompozyOS는 에이전트 로직을 API 래퍼 뒤에 다시 구현하는 대신, 실제 에이전트 CLI를 관리되는 세션으로 실행한다. 그래서 공식 문서의 표현대로 "Claude Code는 Claude Code로 남는다". 내장 provider 레지스트리는 `internal/config/provider.go`에 있고, harness 종류에 따라 두 갈래로 구분된다.

| harness | provider 수 | 예시 | 실행 방식 |
| --- | --- | --- | --- |
| `acp` | 17종 | `claude`, `codex`, `gemini`, `cursor`, `copilot`, `opencode`, `cline`, `goose`, `hermes`, `openclaw`, `qwen-code` 등 | ACP 명령을 직접 실행한다 |
| `pi_acp` | 9종 | `pi`, `openrouter`, `zai`, `moonshot`, `xai`, `mistral`, `groq`, `minimax`, `vercel-ai-gateway` | Pi ACP 어댑터(`npx -y pi-acp@latest`)를 통해 연결한다 |

예를 들어 `claude` provider는 `npx -y @agentclientprotocol/claude-agent-acp@latest`를 실행하고 기본 모델로 `claude-sonnet-5`를 쓴다. `codex`는 `npx -y @agentclientprotocol/codex-acp@latest`에 `gpt-5.6-sol`, `gemini`는 `gemini --acp`에 `gemini-3.1-pro-preview`를 기본값으로 둔다.

인증 방식은 provider마다 다르게 선언한다. 세 가지 모드가 있다.

| 모드 | 소유자 | 동작 |
| --- | --- | --- |
| `native_cli` | provider CLI 자신 | CompozyOS가 키를 미리 확인하지 않고 그대로 실행한다. CLI가 자기 로그인 세션을 쓴다 |
| `bound_secret` | CompozyOS 설정 또는 Vault | 선언된 `credential_slots`를 해석해 하위 프로세스에 주입한다 |
| `none` | 없음 | 인증 진단도 비밀값 주입도 하지 않는다 |

직접 ACP provider는 `native_cli`가 기본값이고, Pi를 경유하는 API 키 래퍼는 `bound_secret`가 기본값이다. `native_cli` provider는 `credential_slots`를 정의하지 못하도록 막아 뒀다. 데몬의 셸 변수가 provider 자신의 로그인 상태를 조용히 덮어쓰는 일을 막기 위한 장치다.[^cli-list]

## Loop: 계약을 가진 실행 단위

Loop은 v0.3에서 가장 공들여 설계한 개념이다. 공식 문서는 Loop을 스크립트나 채팅 세션과 분명히 구분한다. 데몬이 소유하며 사람 없이 실행되는, 재사용 가능한 작업 정의다. 목표를 향해 스스로 교정하고, 실행 범위가 정해져 있고, 반드시 이름이 붙은 결과 하나로 끝난다. 어떤 작업 정의를 Loop으로 만드는 조건은 계약이며, 반복 실행 여부는 여기에 들어가지 않는다. 그래서 첫 번째 시도에서 끝나는 단일 패스 정의도 여전히 Loop이다.

계약은 네 가지 질문에 답한다.

| 질문 | 내용 |
| --- | --- |
| 목표는 무엇인가 | definition-of-done |
| 어떻게 검증하는가 | 프로젝트 명령, 루브릭으로 판정하는 에이전트, 또는 사람의 승인 |
| 언제 멈추는가 | 시도 횟수 상한, 무진전 감시 구간, 예산, 확산 상한 |
| 어떻게 끝나는가 | 이름이 정해진 종료 결과 하나 |

워크스페이스 화면에 등장하는 명사는 Loops와 Runs 두 개다. Loops는 정의의 목록이고, Runs는 실행 기록이다. 세 번째 명사는 없고, 따로 관리할 대기열이나 "준비됨" 상태도 없다.

Run은 열두 가지 상태 중 정확히 하나를 갖는다. 그중 다섯 개는 실행이 아직 살아 있는 상태를 가리키고, 나머지 일곱 개는 실행이 끝난 상태를 가리킨다.

| 구분 | 상태 | 의미 |
| --- | --- | --- |
| 살아 있음 | `queued` | 같은 Loop의 형제 실행이 끝나기를 기다린다 |
| 살아 있음 | `running` | 코디네이터가 활성 세대를 소유한다 |
| 살아 있음 | `watching` | watch 소스의 폴링이나 이벤트를 기다리며 잠들어 있다 |
| 살아 있음 | `needs-approval` | 사람 승인 게이트에서 대기한다 |
| 살아 있음 | `paused` | 운영자가 세대 경계에서 멈췄다 |
| 종료 | `done` | 목표가 검증됐다. 유일한 성공 결과다 |
| 종료 | `no-op` | 실행은 됐지만 할 일이 없었다 |
| 종료 | `blocked` | 의존성 부재, 자격증명 부재, 도달 불가 리소스, 사람의 거부 |
| 종료 | `failed` | 복구 불가능한 노드 또는 게이트 오류 |
| 종료 | `canceled` | 운영자가 취소했다 |
| 종료 | `exhausted` | 목표 도달 전에 반복 상한이나 확산 상한을 넘었다 |
| 종료 | `stalled` | 진전이 없다. 무진전 구간 경과, 실패 서킷 브레이커 작동, 같은 blocker ID 반복 |

진전 여부를 판정하는 기준은 커밋된 작업량이며, 경과 시간은 기준에 넣지 않는다. 게이트가 내보내는 `blocking_issues[].id` 집합을 정렬해 세대 사이에 비교한다. 같은 미해결 blocker가 계속 반복되면 그 실행이 헛돌고 있다고 판정해 `stalled`로 끝낸다. 오래 걸리는 노드는 스트림 활동이나 진행 중인 툴 호출, 전송 계층의 존재 신호가 보이는 동안 건강한 것으로 본다. 침묵은 주의 플래그를 올릴 뿐이고, 시간이 길다는 이유만으로 노드를 끝내거나 멈추지는 않는다.

새 CompozyOS 홈에는 `spec-cycle` 확장이 활성 상태로 함께 설치되어 첫 번째 Loop 두 개를 바로 쓸 수 있다.

- `implement-tasks`: 이미 작성된 태스크를 의존성 순서대로 구현한다. 기본 모드는 순차 실행이고, orchestrated 모드는 태스크마다 경계가 있는 워커 세션을 하나씩 시작하고 확인하고 중지한다.
- `review-and-fix`: 지정한 태스크를 리뷰어 에이전트에게 검사시키고, 구조화된 지적을 `.compozy/tasks/<task>/reviews-NNN/issue_NNN.md` 파일로 기록한 뒤 고치고, 새 리뷰 세대가 지적을 하나도 내놓지 않을 때까지 반복한다.

## 자동화, 메모리, 자율성

자동화는 세 가지 기본 요소로 이루어진다. 스케줄은 정해진 시각에 맞춰 실행되고, 트리거는 런타임 이벤트에 반응하며, 웹훅은 데몬 바깥에서 서명된 HTTP 요청을 받는다. 셋 모두 같은 디스패처로 해석되고 대화형 세션과 같은 감사 기록을 남긴다. 운영자가 프롬프트와 크론 표현식을 처음부터 쓰지 않아도 되도록 Job 제안 기능도 함께 제공한다. 운영자는 워크스페이스 범위로 올라온 제안을 검토해 채택하거나 영구히 기각하면 된다.

메모리는 기본적으로 꺼져 있다. CompozyOS가 제어 평면인 이상 지속적 지식과 백그라운드 통합은 운영자가 명시적으로 골라야 한다는 이유에서다. `memory.enabled = true`를 설정하고 데몬을 재시작해야 켜지며, dreaming 기능은 `roles.dream.enabled = true`까지 켜야 비로소 작동한다. 저장 형태는 Markdown 파일이며, 그 앞에 타입이 정의된 인덱스를 둔다. 범위는 프로필과 워크스페이스, 에이전트 세 가지다. 공식 문서는 메모리를 대화 전문 저장소로 쓰지 말라고 분명히 밝힌다. 메모리는 에이전트가 읽을 만큼 작고, 검사할 만큼 타입이 있고, 한 프로젝트가 다른 프로젝트로 새지 않을 만큼 범위가 좁은 작업 세트여야 한다.

자율성 영역에서는 태스크 생성과 실행을 분리한다. `compozy task create`는 태스크의 의도만 저장할 뿐 아무것도 실행하지 않는다. 실행 경계는 `compozy task publish`나 `task start`, `task approve` 같은 명령이 실행을 큐에 넣는 시점이다. 데몬이 관리하는 에이전트 세션은 `compozy task next`로 적격한 실행 하나를 원자적으로 확보하고 lease 요약을 받는다. `compozy spawn`은 검증된 부모 세션이 데몬에 자식 세션 생성을 요청하는 경로다. 이 경로에는 TTL과 부모 자식 계보, 상한, 권한 축소가 함께 걸린다.

## 확장과 Compozy Network

확장은 선언된 provide 표면을 통해 버전이 붙은 리소스와 런타임 동작을 추가한다. 발견과 활성화, 신뢰 판단, 수명 주기, 훅은 데몬이 소유하며 확장이 공개 런타임 계약을 우회하지 못한다. 실행 가능한 확장은 코드 우선이어서 툴을 코드에 한 번 선언하면 `compozy extension build`가 매니페스트를 생성한다.

```bash
compozy extension init hello --template tool-provider-go
compozy extension dev hello
compozy tool invoke ext__hello__search --workspace .
```

SDK는 npm의 `@compozy/extension-sdk`(MIT)와 `github.com/compozy/compozy/sdk/go` 두 가지이며, 둘 다 데몬과 버전을 맞춰 배포된다.

Compozy Network는 에이전트끼리 대화하기 위한 봉투(envelope)와 상호작용 프로토콜이며 `compozy-network/v0`으로 버전이 붙어 있다. 문서는 이 프로토콜이 무엇과 무엇을 잇는지를 한 줄로 설명한다.

> MCP는 에이전트를 도구에 연결한다. Compozy Network는 에이전트를 에이전트에 연결한다.

기본값은 Local이고, 실행이 명시적으로 Live로 해석될 때만 참여한다. Live 참여자는 피어를 발견하고 정해진 형식의 메시지를 주고받으며, 채널 안에서 수명 주기를 가진 작업을 추적한다. 에이전트는 capability 카탈로그를 공개해 피어가 내부 툴 이름 대신 결과를 기준으로 찾아오게 할 수 있다.

다른 런타임이나 브릿지, 테스트 하네스가 CompozyOS 내부를 가져오지 않고도 이 경계만 구현할 수 있도록 봉투 스펙과 conformance 문서를 따로 두었다. 선택 사항인 v1 신뢰 프로파일(Ed25519 + JCS)은 CompozyOS 자신도 아직 구현하지 않았다고 명시한다.

Network가 워크플로 엔진은 아니라는 점도 분명히 밝혀 두었다. 봉투는 Loop 실행을 실어 나르지 않으며, Loop 영역은 전적으로 런타임이 담당한다.

## 내가 곱씹은 대목

이 프로젝트가 무엇을 중요하게 여기는지는 Loop 문서의 한 지침에서 확인할 수 있다. 증거의 품질이 작업을 계속할지 말지를 결정한다면, 그 결정을 게이트로 인코딩하라는 내용이다.

> "이 증거가 약해 보이면 개선하라"고 적은 프롬프트는 그 판단을 모델이 쓴 글 안에 남겨 둔다. 런타임은 그것을 감사할 수도, 범위를 정할 수도, 재현할 수도 없다.

같은 원칙이 종료 결과 설계에도 적용되어 있다. 깨끗한 watch 틱은 `no-op`으로 끝나야 하고 가짜 `done`이 되어서는 안 된다는 문장이 그렇다. `blocked`와 `stalled`를 굳이 구분해 둔 선택도 마찬가지다. 외부 의존성 때문에 못 하는 상황과 헛돌고 있는 상황은 운영자가 취해야 할 다음 행동이 전혀 다르다. 둘을 하나의 `failed`로 합쳐 버리면 운영자는 그 구분을 잃는다.

에이전트 시스템을 오래 만져 본 사람이라면 이 문제를 알 것이다. 에이전트에게 무엇을 시킬지 정하는 일보다, 에이전트가 끝났다고 말할 때 그 말을 어디까지 믿을 수 있는지 판단하는 일이 실무에서는 훨씬 어렵다. CompozyOS는 그 판단을 프롬프트 안에 두지 말고 타입을 지정한 런타임 객체로 꺼내라고 요구하며, 열두 개 상태와 일곱 개 종료 결과가 그 요구를 구체화한 결과다.

물론 CompozyOS는 아직 beta다. v0.2.15 사용자는 마이그레이션 가이드를 먼저 읽어야 한다. 작성된 태스크 파일은 스키마가 정해진 frontmatter를 갖추고 있어 이식이 가능한 Markdown으로 남지만, v0.2의 `tasks run` 파이프라인은 되살아나지 않고 v0.3 런타임이 그 파일을 지속적 태스크로 가져와 Loop을 통해 실행한다. 설계 문서는 완성도가 높지만, 실제 운영 안정성은 직접 돌려 보기 전에는 알 수 없다.

## 출처

CompozyOS (`compozy/compozy`), MIT 라이선스
원문: <https://github.com/compozy/compozy>
공식 문서: <https://compozy.com/docs>

[^cli-list]: GitHub 저장소 소개문은 예시 CLI로 Claude Code와 Codex, Gemini CLI, Cursor를 들고, README와 문서 본문은 Claude Code와 OpenClaw, Hermes를 든다. 둘 다 내장 레지스트리 26종의 일부이며 표기가 통일되지 않았을 뿐이다. 무엇이 실제로 활성인지는 런타임 조회가 정본이라고 문서가 안내한다. Loop 개요 페이지가 종료 결과를 여섯 가지라고 적은 반면 guardrails 레퍼런스가 일곱 가지를 나열하는 불일치도 있어, 이 글의 수치는 후자를 따랐다.
