---
title: "에이전트에게 말을 거는 두 가지 시간"
date: 2026-04-26T11:30:00+09:00
tags: ["AI 에이전트", "하네스", "아키텍처"]
categories: ["에이전트와 코딩"]
series: ["에이전트 하네스"]
summary: "에이전트에게 메시지를 끼워넣는 행위는 하나가 아니다. '방향을 틀어라'와 '이것도 해라'는 시간축에서 완전히 다른 계약이며, 이것을 API 수준에서 분리한 설계가 pi-agent-core에 있다."
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/cover-temporal-contract-agent-queues.jpg"
sidenotes: true
---

## 메시지 주입은 하나의 행위가 아니다

에이전트가 작업 중일 때 외부에서 메시지를 끼워넣는 것 — 대부분의 에이전트 프레임워크는 이것을 단일 경로로 처리한다. 큐에 넣으면 다음 턴에 처리된다.

Mario Zechner의 pi-agent-core[^1]는 이 경로를 두 개로 쪼갠다. Steering과 Follow-up. 처음에는 우선순위 큐의 변형이려니 했는데, 코드를 읽어 보니 우선순위가 아니라 **시간 계약(temporal contract)이 다른 것**이었다. 영리한 설계다.

## 두 개의 큐, 두 개의 시간

### Steering — "지금 하던 거 끝나면 방향을 틀어라"

Steering 큐는 에이전트의 **내부 루프** 안에서 폴링된다[^2]. 도구 실행이 끝나고 다음 LLM 호출이 시작되기 직전 — 에이전트가 다음 행동을 결정하려는 바로 그 순간에 끼어든다.

```typescript
// 내부 루프: 도구 호출 + steering
while (hasMoreToolCalls || pendingMessages.length > 0) {
    // pending 메시지 주입 → LLM 호출 → 도구 실행
    pendingMessages = (await config.getSteeringMessages?.()) || [];
}
```

Steering은 에이전트의 **현재 작업 맥락 안에서** 방향을 수정하는 것이다.

### Follow-up — "할 일 없으면 이것도 해라"

Follow-up 큐는 **외부 루프**에서만 확인된다[^2]. 내부 루프가 종료되고, 에이전트가 자연스럽게 멈추려는 바로 그 지점에서:

```typescript
// 외부 루프: follow-up 확인
while (true) {
    // ... 내부 루프 실행 ...
    const followUpMessages = (await config.getFollowUpMessages?.()) || [];
    if (followUpMessages.length > 0) {
        pendingMessages = followUpMessages;
        continue;
    }
    break;
}
```

Follow-up은 에이전트의 **현재 작업이 완전히 끝난 뒤에** 새 작업을 건네는 것이다.

## 우선순위 큐와 뭐가 다른가

우선순위 큐는 "무엇을 먼저 처리할 것인가"의 문제다. 이 분리는 "**언제 효력이 발생하는가**"의 문제다.

에이전트가 파일 5개를 수정하는 작업을 하고 있고, 3번째 파일 수정이 끝난 시점이라고 하자:

- **Steering**: "나머지는 건드리지 말고 지금까지 것만 커밋해." → 4, 5번째를 건너뛰고 방향을 튼다
- **Follow-up**: "다 끝나면 테스트도 돌려봐." → 5개 수정이 모두 끝난 뒤에 이어붙인다

단일 큐에서는 이 구분이 불가능하다. 우선순위를 아무리 조정해도, **메시지가 루프의 어느 레벨에서 소비되는가**를 제어할 수 없다.

## 루프 구조가 API를 결정한다

이 설계에서 영리한 점은, API가 내부 구조에서 자연스럽게 도출된다는 것이다.

```
외부 루프 (follow-up)
  └─ 내부 루프 (도구 호출 + steering)
       └─ LLM 호출 → 도구 실행 → steering 폴링
```

Steering은 내부 루프의 지속 조건이고, Follow-up은 외부 루프의 지속 조건이다. "두 종류의 큐를 만들자"라는 설계 결정이 아니라, **이중 루프라는 실행 구조가 두 종류의 주입 시점을 만들어낸 것**이다. 구현 구조와 API 표면이 일치하므로, 코드를 읽으면 API가 왜 그 모양인지 바로 알 수 있다.

이 패턴은 LLM 에이전트만의 것이 아니다. ROS2 액션 서버의 goal cancel vs 새 goal 제출, 게임 엔진의 명령 큐 vs 이벤트 큐, OS 커널의 인터럽트 컨텍스트 vs 프로세스 컨텍스트 — 모두 "지금 끼어들 것인가, 현재 작업이 끝나면 처리할 것인가"의 분리다.

pi-agent-core가 한 것은 이 오래된 구분을 에이전트 API에 `agent.steer(msg)`와 `agent.followUp(msg)` 두 줄로 표면화한 것이다. 암묵적으로 타이밍을 추론하는 대신, 호출자가 의도를 명시적으로 선택하게 만든 것 — 작지만 깔끔한 설계 결정이다.

[^1]: Mario Zechner, `@mariozechner/pi-agent-core` v0.70.2 — [github.com/badlogic/pi-mono/tree/main/packages/agent](https://github.com/badlogic/pi-mono/tree/main/packages/agent)
[^2]: `runLoop()` 함수, `agent-loop.ts` L155-L231 — 내부 루프(L172-L219)에서 steering을, 외부 루프(L168-L231)에서 follow-up을 각각 처리
