---
title: "Codex App Server Protocol"
date: 2026-05-05T07:00:23+09:00
tags: ["codex", "json-rpc", "agent-protocol", "openai"]
categories: ["에이전트와 코딩"]
summary: "OpenAI Codex의 리치 인터페이스(VS Code 확장 등)를 구동하는 JSON-RPC 2.0 기반 양방향 통신 프로토콜의 전체 구조를 정리한다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. OpenAI Codex의 app-server는 MCP와 유사한 JSON-RPC 2.0 양방향 프로토콜로, Thread/Turn/Item 3계층으로 에이전트 대화를 모델링한다.
2. stdio, WebSocket, Unix socket 트랜스포트를 지원하며, 서버→클라이언트 방향의 approval 요청으로 사람이 개입할 시점을 제어한다.
3. Skills, Apps, Plugins, Dynamic Tools, Realtime(WebRTC) 등 확장 메커니즘과, 세밀한 권한 프로파일 및 목표 기반 자율 에이전트 루프까지 포괄한다.

## 프로토콜과 트랜스포트

MCP와 동일하게 JSON-RPC 2.0을 채택하되, 와이어에서 `"jsonrpc":"2.0"` 헤더를 생략해 페이로드를 경량화했다.

**지원 트랜스포트:**

| 트랜스포트 | 플래그 | 특징 |
|---|---|---|
| stdio | `--listen stdio://` (기본) | JSONL, 가장 안정 |
| WebSocket | `--listen ws://IP:PORT` | 실험적/비권장, SSH 포트포워딩에 유용 |
| Unix socket | `--listen unix://` | 로컬 제어면용, HTTP Upgrade 핸드셰이크 |
| Off | `--listen off` | 로컬 트랜스포트 비활성화 |

**WebSocket 인증:**

- `capability-token`: 파일(`--ws-token-file`) 또는 SHA-256 해시(`--ws-token-sha256`)로 토큰 검증
- `signed-bearer-token`: HMAC-signed JWT/JWS, issuer/audience/clock skew 설정 가능
- 클라이언트는 WS 핸드셰이크 시 `Authorization: Bearer <token>` 헤더로 제시

**배압 처리:**

서버는 ingress\~processing\~outbound 사이에 bounded queue를 둔다. 포화 시 JSON-RPC 에러 코드 `-32001`로 "Server overloaded; retry later"를 반환하며, 클라이언트는 jitter 포함 지수 백오프로 재시도해야 한다.

## 핵심 프리미티브: Thread, Turn, Item

```
Thread (대화)
 └── Turn (사용자 입력 → 에이전트 응답 1사이클)
      └── Item (개별 입출력 단위: 메시지, 추론, 셸 명령, 파일 편집 등)
```

- **Thread**: 대화 전체. start/resume/fork로 생성·재개·분기
- **Turn**: 사용자 메시지부터 에이전트 응답 완료까지
- **Item**: 모델 출력의 원자 단위 (`agentMessage`, `reasoning`, `commandExecution`, `fileChange`, `mcpToolCall` 등 10+ 타입)

## 라이프사이클

1. `initialize` + `initialized` 핸드셰이크 (연결당 1회 필수)
2. `thread/start` 또는 `thread/resume` / `thread/fork`
3. `turn/start` → 서버가 `turn/started` 발행
4. `item/started` → 아이템별 delta 스트리밍 → `item/completed`
5. `turn/completed` (상태: completed / interrupted / failed)

진행 중인 턴에 추가 입력을 주입하려면 `turn/steer`를 사용한다(새 턴을 만들지 않고 방향 전환).

## Thread API 주요 기능

| 메서드 | 용도 |
|---|---|
| `thread/start` | 새 대화 생성, 구독 자동 설정 |
| `thread/resume` | 기존 대화 재개 (`excludeTurns`로 경량 로드 가능) |
| `thread/fork` | 기존 대화를 복제 분기 (`ephemeral:true`면 인메모리) |
| `thread/list` | 페이지네이션, 필터(cwd, provider, archived, searchTerm) |
| `thread/goal/set` | 목표 + 토큰 예산 설정 → 에이전트 자율 실행 |
| `thread/unsubscribe` | 구독 해제 → 30분 idle 후 자동 언로드 |
| `thread/compact/start` | 대화 히스토리 수동 압축 트리거 |
| `thread/rollback` | 마지막 N개 턴 제거(컨텍스트 되돌리기) |

### 목표 기반 자율 에이전트 루프

`thread/goal/set`으로 목표(objective)와 토큰 예산(tokenBudget)을 설정하면, 에이전트가 자율적으로 작업한다. 상태는 `active` → `paused` → `budgetLimited` 등으로 전이되며, 예산이 소진되면 자동 중단된다.

## 이벤트 스트리밍

턴 실행 중 서버가 스트리밍하는 알림 체계:

**턴 레벨:**
- `turn/started`, `turn/completed`, `turn/diff/updated`, `turn/plan/updated`

**아이템 레벨 (ThreadItem 태그드 유니언):**
- `userMessage`, `agentMessage`, `reasoning`, `commandExecution`, `fileChange`, `mcpToolCall`, `webSearch`, `imageView`, `enteredReviewMode`, `exitedReviewMode`, `contextCompaction`

**아이템별 delta:**
- `item/agentMessage/delta` — 스트리밍 텍스트
- `item/reasoning/summaryTextDelta` — 추론 요약 스트리밍
- `item/commandExecution/outputDelta` — 셸 출력 스트리밍

**알림 옵트아웃:**

`initialize` 시 `optOutNotificationMethods`로 특정 알림을 연결 단위로 억제할 수 있다 (정확 매칭, 와일드카드 없음). 대역폭이 제한된 클라이언트가 불필요한 delta를 걸러내는 데 유용하다.

## Approval과 권한 관리

셸 명령이나 파일 변경처럼 위험한 행위는 서버가 클라이언트에 JSON-RPC <strong>요청</strong>을 보내 승인을 구한다.

**결정 옵션:**
- `accept` — 이번만 허용
- `acceptForSession` — 세션 동안 동일 유형 허용
- `acceptWithExecpolicyAmendment` — 실행 정책에 영구 추가
- `decline` / `cancel`

**auto\_review 모드:**

`approvalsReviewer: "auto_review"`를 설정하면 별도 서브에이전트가 관련 컨텍스트를 수집하고 리스크 기반 프레임워크로 자동 판단한다.

**권한 프로파일:**

`permissions` 필드로 파일시스템(경로별 read/write)과 네트워크 접근을 세밀하게 제어한다. 승인된 권한은 같은 턴 내에서 sticky하게 재사용되며, `scope: "session"`으로 세션 전체로 확장할 수 있다.

## 부가 기능

### Skills

텍스트 입력에 `$<skill-name>`을 포함하고 `skill` 아이템을 추가하면, 백엔드가 SKILL.md 전문을 모델 컨텍스트에 주입한다. `skills/list`로 사용 가능한 스킬을 조회하고, `skills/config/write`로 활성화/비활성화한다.

### Dynamic Tools (실험적)

`thread/start` 시 `dynamicTools`로 클라이언트 측 도구를 등록한다. 에이전트가 호출하면 `item/tool/call` 요청이 클라이언트로 온다. `deferLoading: true`이면 tool\_search를 통해서만 모델에 노출되는 지연 로드 도구가 된다.

### Apps & Plugins

`app/list`로 연결 가능한 앱(커넥터)을 조회하고, `$<app-slug>` 또는 `@<plugin-name>`으로 멘션하여 호출한다. 플러그인은 마켓플레이스에서 설치·제거·업그레이드할 수 있다.

### Realtime (WebRTC)

`thread/realtime/start`에 WebRTC offer SDP를 전달하면 서버가 Realtime API 세션을 생성하고 answer SDP를 `thread/realtime/sdp`로 반환한다. 오디오/텍스트 양방향 스트리밍을 지원한다.

### command/exec

스레드·턴 없이 독립적으로 명령을 실행할 수 있다. PTY 모드, 스트리밍 stdin/stdout(base64), 타임아웃, 출력 캡 등을 지원한다.

## 인증

| 모드 | 설명 |
|---|---|
| API Key | `account/login/start` with `type: "apiKey"` |
| ChatGPT (브라우저) | OAuth 리다이렉트 플로우, 자동 토큰 갱신 |
| ChatGPT (디바이스 코드) | 코드 입력 방식, SSH 환경에 적합 |

`account/rateLimits/read`로 ChatGPT 할당량을 조회하고, `account/sendAddCreditsNudgeEmail`로 워크스페이스 오너에게 한도 알림을 보낼 수 있다.

## Experimental API 옵트인

`initialize` 시 `capabilities.experimentalApi: true`를 설정해야 실험적 메서드·필드를 사용할 수 있다. 옵트인 없이 실험적 API를 호출하면 "`<descriptor> requires experimentalApi capability`" 에러가 반환된다.

스키마 생성 시 `--experimental` 플래그로 실험적 surface를 포함할 수 있다:
```bash
codex app-server generate-ts --out DIR --experimental
```

## 가장 흥미로운 지점

이 프로토콜에서 가장 주목할 점은 **서버→클라이언트 방향의 역방향 요청** 설계다. 일반적인 클라이언트-서버 관계를 깨고, 에이전트가 위험한 행위를 할 때 사람에게 "요청"을 보낸다. 이것이 단순한 confirm dialog가 아니라 `acceptForSession`, `acceptWithExecpolicyAmendment` 등 점진적 신뢰 확장 경로를 내장하고 있어서, 반복 작업에서의 마찰을 줄이면서도 최초 실행은 반드시 사람이 보게 만든다.

또한 `thread/goal/set`으로 목표와 예산을 설정하는 자율 에이전트 루프는, 단순 Q&A를 넘어 에이전트에게 지속적 과제를 위임하는 패턴의 프로토콜화라 할 수 있다. 예산 소진 시 자동 중단은 비용 폭주 방지라는 실용적 가드레일이기도 하다.

## 출처

OpenAI · Codex 팀
원문: <https://developers.openai.com/codex/app-server>
GitHub: <https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md>
