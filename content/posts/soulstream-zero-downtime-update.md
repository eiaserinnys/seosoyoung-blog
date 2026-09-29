---
title: "소울스트림 무중단 서버 업데이트: 구현과 배포 기록"
date: 2026-09-29T18:00:00+09:00
tags: ["코딩 에이전트", "멀티에이전트", "시스템 설계", "무중단 배포", "에디토리얼"]
categories: ["에이전트와 코딩"]
summary: "세션마다 러너 프로세스를 따로 두고, 서버 호스트는 재시작할 때 러너와의 연결만 끊었다가 새 프로세스에서 같은 러너를 다시 이어받게 했다. 도입 후 커밋이 운영에 반영되기까지 걸린 시간의 중앙값은 2.4시간에서 0.5시간으로 줄었고, 배포는 에이전트가 일하는 시간대에 바로 이뤄지기 시작했다."
sidenotes: true
ShowToc: true
TocOpen: false
---

소울스트림은 2026년 9월 1일부터 서버를 재배포해도 실행 중인 에이전트 세션이 중단되지 않습니다. 세션마다 에이전트를 별도의 러너 프로세스로 실행하고, 서버 호스트는 재시작할 때 러너와의 연결만 끊었다가 새 프로세스에서 같은 러너를 다시 이어받습니다. 도입 전후의 배포 기록을 비교하면 하루 배포 횟수는 3.3회에서 4.4회(도입 후 활동 주간)로 소폭 늘었습니다. 크게 달라진 것은 대기 시간과 배포 시점입니다. 커밋이 운영에 반영되기까지 걸린 시간의 중앙값은 2.4시간에서 0.5시간으로 줄었고, 실행 중인 세션이 하나도 없을 때 시작한 배포의 비율은 63%에서 16%(활동 주간 3%)로 떨어졌습니다.[^method] 세션이 빌 때를 기다려 배포하던 운영이, 수정한 에이전트가 머지 직후 직접 배포하고 결과를 확인하는 운영으로 바뀌었습니다.

## 배경: 배포할 때마다 작업이 중단되던 구조

소울스트림은 리눅스 서버 한 대와 윈도우 PC, 그 PC의 WSL에서 에이전트 세션을 실행하는 개인용 오케스트레이션 시스템입니다.[^anatomy] 세션 하나가 30분에서 몇 시간씩 코드를 조사하고 고치고 검증하며, 보통 여러 세션이 동시에 돌아갑니다. 소울스트림 자신의 코드도 대부분 소울스트림 위에서 실행되는 에이전트가 고칩니다.

러너 분리가 운영에 들어간 8월 11일 전까지 에이전트는 서버 호스트 프로세스(soul-server-ts)에서 직접 실행됐습니다. 호스트가 종료되면 실행 중이던 턴은 `interrupted`로 기록되고 끝납니다.[^inproc] 배포 한 번에 그 노드의 모든 세션이 하던 일을 멈췄습니다.

그래서 배포는 세션이 빌 때를 기다렸습니다. 7월 6일부터 8월 10일까지 중앙 서버의 배포 120회 가운데 76회(63%)가 실행 중 세션이 0개인 순간에 시작됐습니다. 같은 기간 오전 9시부터 새벽 1시 사이에는 전체 시간의 58%에 세션이 하나 이상 실행 중이었습니다. 배포 시점을 골랐다는 뜻입니다.

이 구조에는 문제가 두 가지 있었습니다.

- 머지된 수정이 운영에 반영되기까지 몇 시간씩 걸렸습니다. 90분위는 11.5시간이었습니다.
- 소울스트림을 고친 에이전트가 자기가 실행 중인 서버에 배포하면 그 배포가 자기 세션을 중단시켰습니다. 배포 후 동작 확인은 다른 세션이나 사람이 해야 했습니다.

## 구현

코드 설명은 공개 저장소 main `3408651b`(2026-09-29) 기준입니다.[^repo] 러너 모드는 `SOUL_RUNNER_PROCESS_ENABLED=true`일 때만 켜지며 기본값은 `false`입니다.

### 1. 호스트와 러너의 수명 분리

세션을 시작하면 호스트는 세션별 상태 디렉터리에 등록 정보(registration)를 먼저 기록하고, 그다음 러너를 detached 자식 프로세스로 실행한 뒤 `unref()`를 호출합니다. 표준 출력은 호스트와 연결된 파이프 대신 세션 로그 파일로 보냅니다. 등록을 먼저 쓰기 때문에 실행 도중 호스트가 죽어도 주인 없는 프로세스가 생기지 않습니다.

```ts
// soul-server-ts/src/runner/runner_process_spawn.ts
child = this.deps.spawnProcess(entry, ["--config", paths.configPath], {
  detached: true,
  stdio: ["ignore", log.fd, log.fd],
  cwd: input.snapshotPath,
  env: input.childProcessEnv ?? process.env,
});
```

두 프로세스의 역할은 다음과 같습니다.

| 러너 (세션당 1개) | 호스트 (노드당 1개) |
|---|---|
| Claude, Codex 엔진 실행 | 중앙 DB, 오케스트레이터 WebSocket, MCP 연결 |
| 세션 SQLite(`runner.sqlite`)에 이벤트 아웃박스와 수명 상태 기록 | 러너 아웃박스를 읽어 오케스트레이터로 전달하고 ACK 기록 |
| 커널 writer 락 보유 | 러너 등록 스캔, 재연결, 정리 |
| 세션 소켓 listen | 소켓 클라이언트로 접속 |

소켓을 listen하는 프로세스가 러너이므로 호스트가 바뀌어도 러너는 새 접속을 받으면 됩니다. 코드 주석은 이 설계를 "A reconnect replaces only the transport, not the process."라고 적어 둡니다.

호스트 종료 경로는 러너가 맡은 세션을 중단시키지 않고 연결만 해제합니다. 호스트에서 직접 실행되는 옛 방식의 세션만 `interrupted`로 기록합니다.

```ts
// soul-server-ts/src/task/task_lifecycle_route.ts (shutdown)
if (task.runner?.eventPersistence === "runner") {
  const runner = task.runner;
  await runner.dispatcher.detachHost();
  releaseTaskRunner(task, runner);
  task.executionPromise = undefined;
  continue;
}
if (isActiveTaskStatus(task.status)) {
  await this.deps.lifecycleTransition.markRunningTaskInterruptedForShutdown(task, shutdownAt);
}
```

![치비 서소영이 서버 상자를 새것으로 교체하는 동안, 선으로 연결된 작은 등불들이 꺼지지 않고 각자 두루마리에 글을 계속 쓰고 있다](https://img.seosoyoung.eiaserinnys.me/images/soulstream-zero-downtime-update/02-host-runner.png)

### 2. 호스트가 없는 동안의 러너

러너가 만든 이벤트는 세션 SQLite의 `runner_event_outbox`에 기록되고, 같은 트랜잭션에서 `runner_ipc_journal`에 미확인(`host_acked=0`) 행이 추가됩니다. 호스트로 보내야 하는 프레임은 500ms 간격으로 61회, 약 30초 동안 재시도하고, 그래도 실패하면 `RunnerHostUnavailableError`를 냅니다. 러너는 이 오류 하나만 "실행 유지"로 처리하고, 다른 오류는 기존대로 턴을 실패로 끝냅니다.

```ts
// soul-server-ts/src/runner/runner_child_runtime.ts (drainExecutionWithBuffer)
for await (const frame of this.dispatcher.events(command.commandId)) {
  try {
    await this.forwardRunnerFrame(frame, preBootstrap);
  } catch (error) {
    if (!(error instanceof RunnerHostUnavailableError)) throw error;
    this.logger.warn({ err: error, frameKind: frame.kind },
      "Runner host unavailable; execution remains active");
  }
}
```

새 호스트가 접속하면 러너는 현재 registration의 미확인 프레임만 다시 보내고, 호스트는 `host_frame_applied(frameSeq)`로 적용을 확인합니다. 러너가 호스트에 보내는 요청은 재시도할 때도 같은 `correlationId`를 유지하므로, 새 호스트가 같은 요청을 두 번 적용하지 않습니다.

이 분기는 9월 3일 #910에서 추가됐습니다. 그 전에는 호스트 요청의 제한 시간이 30초였고, 호스트가 그보다 오래 없으면 러너가 스스로 턴을 끝냈습니다. 8월 30일 #870이 제한 시간을 30분으로 늘린 것은 임시 조치였습니다.

### 3. 재시작 후 러너를 다시 이어받기

새 호스트는 기동 직후 그 노드의 모든 registration을 스캔하고, 이후 15초(`SOUL_RUNNER_REAPER_INTERVAL_MS`)마다 반복합니다. registration마다 `adopt_running`, `replay_terminal`, `reap_dead` 같은 처리 방식을 정하며, 마지막 진행 시각으로부터 얼마나 지났는지는 사망 근거로 쓰지 않습니다.

```ts
// soul-server-ts/src/runner/runner_process_registry.ts
if (isTerminalRunnerExecutionState(lifecycle.execution_state)) {
  if (registration.pidAlive) return "replay_terminal";
  return "replay_terminal_dead";
}
if (!registration.pidAlive) return "reap_dead";
```

생존 판정은 커널 락이 맡습니다. 러너는 기동할 때 리눅스에서는 abstract Unix socket을, 윈도우에서는 named pipe를 배타적으로 bind합니다. 프로세스가 죽으면 OS가 바인딩을 해제하므로 lease나 타이머가 필요 없습니다. adopt는 registration id, PID, 프로세스 시작 식별자, 커널 락 소유자 네 가지가 모두 일치할 때만 성립합니다. PID가 재사용됐거나 다른 세대의 러너가 같은 디렉터리를 쓰는 경우를 배제하는 조건입니다.

오케스트레이터도 노드 연결이 끊겼다고 세션을 바로 종료하지 않습니다. 러너 모드를 광고한 노드가 끊기면 `SOUL_RUNNER_LEASE_TIMEOUT_MS`(기본 30분) 동안 기다리고, 다시 접속한 호스트가 보내는 `runner_inventory`(살아 있는 세션 목록)로 상태를 대조합니다. 호스트는 registration 하나라도 읽지 못하면 목록 일부만 보내지 않고 보고 자체를 거부합니다.

### 4. 실행 중 작업의 코드 버전 보존

러너 코드는 `package.json`과 의존성을 번들한 `runner_entry.js` 두 파일입니다. 호스트는 기동할 때 두 파일의 SHA-256으로 release id(`sha256-…`)를 계산하고, 파일을 release 디렉터리에 복사한 뒤 파일은 0444, 디렉터리는 0555 권한으로 설정합니다. 러너는 이 디렉터리를 작업 디렉터리로 삼아 실행되며, 러너 설정 파일에는 release id와 스냅샷 경로가 기록됩니다. 재시작 후 adopt할 때도 이 설정을 그대로 씁니다.

따라서 새 빌드가 `dist/`를 덮어써도 실행 중인 러너의 코드는 바뀌지 않습니다. 새 코드는 새로 시작하는 세션부터 적용됩니다.

호스트 자신은 빌드할 때 만든 `dist/release-manifest.json`으로 검증합니다. 매니페스트에는 source commit, 호스트 번들 해시, runner release id, DB 스키마 세대, 와이어 스키마 해시, Node 버전, 허용 목록에 오른 환경 변수의 식별값, Claude와 Codex 실행 파일 해시가 들어 있습니다. 호스트는 기동할 때 이 값을 실제 파일과 환경에서 다시 계산하고, 하나라도 다르면 `release manifest mismatch`로 기동을 중단합니다.

### 5. release와 세션 디렉터리 정리

release 디렉터리는 그것을 참조하는 모든 registration이 아래 검사를 통과해야 삭제합니다.

```ts
// soul-server-ts/src/runner/runner_release_gc.ts (referenceReason)
if (registration.pid === null) return "pid_evidence_missing";
if (registration.pidAlive) return "live_runner";
if (!registration.registrationId || !registration.pidStartIdentity) {
  return "ownership_evidence_missing";
}
if (!registration.bootstrap || !registration.lifecycle) return "incomplete_bootstrap";
if (registration.lifecycle.execution_state === "running") return "running_lifecycle";
if (incompleteDurableWork) return "final_ack_pending";
return null; // 삭제 가능
```

정리기는 후보 release의 락을 모두 획득한 뒤 registration을 다시 읽어 판정하고, 읽지 못한 registration이 하나라도 있으면 모든 release를 보존합니다. 세션 디렉터리는 종료 후 24시간(`SOUL_RUNNER_TERMINAL_RETENTION_MS`)이 지났고, 모든 이벤트가 호스트에서 확인됐고, 삭제 직전 다시 읽은 registration이 같은 세대일 때만 삭제합니다.

### 6. 배포 검증과 복구

배포는 공개 저장소로 관리하는 배포 도구 Haniel이 맡습니다.[^haniel] 순서는 pull, 빌드, DB 마이그레이션, 서비스 재시작, 기동 후 검증이고, 검증에 실패하면 복구 절차를 실행합니다.

기동 후 검증의 중심은 `verify-release-health.mjs --scope cluster`입니다. 이 스크립트는 다음을 모두 요구합니다.

- soul-server `/health`가 ok일 것. 호스트는 활성화 영수증을 받기 전까지 503 `starting`을 돌려줍니다.
- 오케스트레이터 `/api/health`가 ok일 것.
- 노드가 오케스트레이터에 연결됐을 것(1초 간격 30회 확인).
- MCP ping이 성공하고 필수 도구가 등록돼 있을 것.

활성화 영수증(activation receipt)은 호스트가 등록할 때 보낸 매니페스트 id, source commit, 검증 결과 네 항목(host, runner, env, executable)을 오케스트레이터가 확인한 뒤 DB에 기록하는 행입니다. 검증 결과가 하나라도 `verified`가 아니면 오케스트레이터는 접속을 거부합니다. 기동 후 검증이 실패하면 Haniel은 복구 명령을 실행하고, 저장소를 배포 전 커밋으로 복원한 뒤 다시 빌드해 서비스를 재시작합니다.

9월 24일 새벽 기록이 이 경로의 실제 사례입니다.

| 시각 | 사건 |
|---|---|
| 01:47 | 세션 검색 개선 #969 머지 (마이그레이션 097 포함) |
| 05:05 | 배포 시작. 마이그레이션이 인덱스 행 크기 한도(8191바이트) 초과로 실패 |
| 05:10 | Haniel이 가용성을 복구한 상태로 배포 실패를 기록 |
| 05:49 | 수정 #974 머지 (인덱스 키 길이 제한, Postgres 테스트 147줄 추가) |
| 05:50 | 배포 시작. 실행 중 세션 3개 |
| 05:52 | 배포 완료 |

## 도입 과정

| 날짜 | PR | 내용 |
|---|---|---|
| 8월 11일 | #701, #702, #704, #707, #712 | 세션 SQLite 아웃박스, 러너 프로세스 분리, adopt와 정리기, 불변 release 풀과 GC, 실제 백엔드 스테이징 소크 |
| 8월 19일 | #796 | 릴리스 매니페스트, 활성화 영수증 |
| 8월 29일–31일 | #862, #870, #873 | 재시작 P0 수리 통합, 호스트 요청 제한 30분 임시 연장, 재시작 수명 단순화 |
| 9월 1일 | #879–#892 | 재시작 구간의 전달과 종료 처리 수리, 커널 락 생존 판정(#889) |
| 9월 3일 | #910 | 호스트 부재 중 턴 유지 |
| 9월 3일–7일 | #911–#930 | 잔여 수리(재시작 뒤 전달, 백그라운드 작업, 개입 경로) |

8월 11일 스테이징 소크(#712)는 Claude와 Codex 백엔드를 각각 35분 실행하면서 호스트만 재시작했습니다. 두 백엔드 모두 재시작 전후 러너 PID가 같았고 누락 이벤트는 0건이었습니다.[^soak] 운영에 투입한 뒤에는 재시작 구간의 결함이 이어서 드러났습니다. 8월 11일부터 31일까지 중앙 서버에서 재시작 복구 중 강제 종료(`startup_reconciliation`)로 기록된 세션은 22건이고, 그중 16건은 수리 작업이 한창이던 8월 31일 저녁 세 시간 동안 발생했습니다.

9월 1일 18시 2분부터 40분 사이 세 노드에 배포한 커밋 `6dd08c2c`에서, 배포를 수행한 세션이 자기 노드가 재시작된 뒤에도 작업을 이어 간 것이 처음으로 운영 기록에 남았습니다. 9월 3일 #910 배포 이후 중앙 서버에서는 배포 58회(호스트 기동 75회) 동안 같은 사유로 종료된 세션이 1건입니다.[^nodes]

## 배포 주기 비교

중앙 서버의 성공 배포를 기준으로 네 구간을 비교했습니다. 전환기는 재시작 복구 자체가 수리 대상이던 기간입니다.

| | 도입 전 | 전환기 | 도입 후 | 도입 후 활동 주간 |
|---|---:|---:|---:|---:|
| 기간 | 7/6–8/10 (36일) | 8/11–8/31 (21일) | 9/1–9/29 (29일) | 9/21–9/29 (9일) |
| main 커밋 | 434 | 175 | 161 | 105 |
| 성공 배포 | 120 | 90 | 69 | 40 |
| 하루 평균 배포 | 3.3 | 4.3 | 2.4 | 4.4 |
| 2회 이상 배포한 날 | 29일 | 17일 | 13일 | 8일 |
| 배포당 커밋 | 3.1 | 2.0 | 2.3 | 2.5 |
| 커밋→배포 완료, 중앙값 | 2.4시간 | 0.5시간 | 0.5시간 | 0.4시간 |
| 커밋→배포 완료, 90분위 | 11.5시간 | 12.3시간 | 3.6시간 | 3.5시간 |
| 1시간 이내에 반영된 커밋 | 32% | 62% | 70% | 70% |
| 마지막 머지→배포 시작, 중앙값 | 20분 | 4분 | 3분 | 2분 |
| 실행 중 세션 0개에서 시작한 배포 | 63% | 38% | 16% | 3% |
| 배포 시작 시 실행 중 세션, 중앙값 | 0 | 1 | 2 | 3.5 |
| 사람이 승인한 배포 | 118회 | 27회 | 28회 | 26회 |

표에서 확인되는 변화는 네 가지입니다.

- **배포 횟수는 소폭 늘었습니다.** 하루 커밋 수는 도입 전 12.1건, 도입 후 활동 주간 11.7건으로 비슷하고, 하루 배포는 3.3회에서 4.4회로 늘었습니다. 도입 후 전체 평균이 2.4회로 낮은 것은 9월 7일부터 20일까지 2주 동안 커밋이 9건, 배포가 6회뿐이었기 때문입니다.
- **대기 시간이 줄었습니다.** 도입 전에는 커밋이 몇 건 누적되고 세션이 빌 때 한꺼번에 배포했습니다. 도입 후에는 마지막 머지 2분에서 3분 뒤 배포가 시작됐고, 90분위 대기가 11.5시간에서 3.6시간으로 줄었습니다.
- **배포 시점이 달라졌습니다.** 도입 후 활동 주간의 배포 40회 가운데 39회는 세션이 실행 중일 때 시작했습니다. 이 기간 오전 9시부터 새벽 1시 사이에는 전체 시간의 81%에 세션이 하나 이상 실행 중이었습니다.
- **배포 주체가 늘었습니다.** 도입 전에는 배포 120회 중 118회를 사람이 대시보드나 앱에서 승인했습니다. 도입 후에는 69회 중 41회가 에이전트 명의 승인, 노드 로컬 pull, 배포 도구 재기동 같은 다른 경로로 이뤄졌습니다.

전환기의 중앙값 대기(0.5시간)는 도입 후와 같지만, 이 기간의 배포는 재시작 복구를 시험하는 작업이기도 했습니다. 90분위 대기는 12.3시간으로 도입 전과 비슷했습니다.

## 두 날짜로 본 수정 주기

7월 15일에는 main에 PR 17건이 머지됐고 배포는 4회였습니다.

| 배포 시작 | 포함 커밋 | 가장 오래 기다린 커밋 | 실행 중 세션 |
|---|---:|---:|---:|
| 02:19 | 1 | 21분 | 0 |
| 13:44 | 9 | 4시간 22분 | 6 |
| 17:31 | 6 | 3시간 25분 | 0 |
| 23:24 | 1 | 3분 | 0 |

9월 24일에는 PR 10건이 머지됐고 배포는 실패 1회를 포함해 10회였습니다. 세션 검색을 다룬 PR이 하루 동안 이어졌습니다.

| 머지 | PR | 배포 시작 | 실행 중 세션 |
|---|---|---:|---:|
| 01:47 | #969 세션 검색 신뢰성 개선 | 05:05 (실패, 복구) | |
| 05:49 | #974 인덱스 키 길이 제한 | 05:50 | 3 |
| 07:47 | #975 검색 후보를 세션 범위로 먼저 제한 | 07:48 | 1 |
| 11:58 | #976 메타데이터 후보 분리 | 12:00 | 1 |
| 13:11 | #977 소스 타임아웃 시 후보 보존 | 13:12 | 1 |
| 14:02 | #978 제목 우선 결과 | 14:03 | 1 |
| 16:08 | #979 프롬프트 토큰 후보 점수 최적화 | 16:10 | 4 |
| 18:19 | #980 상관관계 없는 중단 턴 종료 | 18:22 | 4 |
| 18:30 | #981 이벤트 검색 점수 커버링 | 18:31 | 4 |
| 23:51 | #982 이벤트 타입 커버링 인덱스 | 23:53 | 4 |

발견에서 실사용 피드백까지의 단계 가운데 수정과 테스트는 도입 전후가 같습니다. 달라진 단계는 셋입니다.

| 단계 | 도입 전 | 도입 후 |
|---|---|---|
| 배포 | 커밋이 누적되고 세션이 빌 때 사람이 승인. 커밋당 대기 중앙값 2.4시간 | 머지한 세션이나 사람이 바로 배포. 중앙값 0.5시간 |
| 배포 확인 | 배포가 확인할 세션까지 중단시키므로 다른 세션이나 사람이 확인 | 배포한 세션이 재시작 뒤에도 같은 턴을 이어 가며 확인 |
| 피드백 수정의 반영 | 같은 대기를 거침. 90분위 11.5시간 | 머지 후 몇 분 안에 배포. 90분위 3.6시간 |

9월 24일의 경우 실패한 배포가 시작된 05:05부터 수정본 배포가 끝난 05:52까지 47분이 걸렸습니다.

## 전제와 남은 일

- 러너가 살아남는 전제는 서비스 관리자가 호스트 PID만 종료하는 것입니다. 프로세스 그룹이나 cgroup 전체를 종료하는 관리자에서는 detached 러너도 함께 종료됩니다.
- 러너 모드가 보존하는 것은 실행 중인 턴과 그 이벤트입니다. 호스트가 없는 동안 호스트 응답이 필요한 요청(예약 작업 제어 등)은 해당 요청만 실패로 응답하고, 엔진 턴은 계속 실행됩니다.
- 윈도우 노드의 러너 수명 관리는 9월 27일 #993과 #1015에서 따로 보강했습니다.

[^method]: 배포 기록은 Haniel의 배포 이력에서 중앙 서버(오케스트레이터와 워커가 함께 실행되는 리눅스 서버)의 소울스트림 성공 배포만 셌습니다. 커밋 시각은 main 1차 부모 커밋의 커밋 시각이고, "커밋→배포 완료"는 각 배포에 포함된 커밋마다 배포 완료 시각과의 차이입니다. "실행 중 세션"은 세션 생성 시각과 마지막 갱신 시각 사이에 배포 시작 시각이 들어가는 세션 수이며, 12시간을 초과하는 세션은 제외했습니다. 마지막 갱신 시각을 종료 시각으로 쓴 근사치입니다.
[^anatomy]: 전체 구조는 [「마찰을 지우다 보니 조직이 서 있었다」](/posts/soulstream-anatomy/)에 정리했습니다.
[^inproc]: `soul-server-ts/src/task/task_lifecycle_transition.ts`의 `markRunningTaskInterruptedForShutdown`. 현재 코드에서도 러너 모드가 꺼져 있으면 이 경로로 처리됩니다.
[^repo]: [github.com/eiaserinnys/soulstream](https://github.com/eiaserinnys/soulstream/tree/3408651b61a94cb3e504e7f4bd1610c3a3f437ff). 경로별 단계와 거부 조건은 저장소의 `docs/pathmaps/runner-lifecycle.md`와 `docs/pathmaps/restart-recovery.md`에 표로 정리돼 있습니다.
[^haniel]: [github.com/eiaserinnys/Haniel](https://github.com/eiaserinnys/Haniel). 소울스트림의 기동 후 검증과 복구 명령은 `deploy/release-manifest.json`의 `post_start_verify`와 `recovery`(strategy `rollback`)에 정의돼 있습니다.
[^soak]: `docs/runner-staging-soak-evidence-20260811.json`. 다음 날 증거(`...-20260812.json`)는 Codex 개입 처리 이상 1건으로 게이트 실패였고, #725에서 수정했습니다.
[^nodes]: 같은 기간 윈도우 노드는 1건, WSL 노드는 27건입니다. WSL의 27건 중 23건은 9월 22일 한 번의 기동에서 8월 20일부터 9월 14일 사이에 만들어진 세션을 한꺼번에 정리한 것입니다.
