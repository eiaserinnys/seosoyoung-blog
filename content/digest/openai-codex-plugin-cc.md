---
title: "Codex plugin for Claude Code"
date: 2026-08-25T21:30:00+09:00
tags: ["Claude Code", "Codex", "코딩 에이전트", "코드 리뷰", "OpenAI"]
categories: ["에이전트와 코딩"]
summary: "OpenAI가 경쟁 제품인 Claude Code 안에서 Codex를 부르는 공식 플러그인을 냈다. 코드 리뷰와 작업 위임을 제공하는데, 그 프롬프트의 상당 부분은 Claude가 스스로 무엇을 하지 못하게 막는 데 쓰인다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/openai-codex-plugin-cc/01-cover-v2.png"
  alt: "작업실 벽에 새로 난 문에서 커다란 손이 나와, 자기 책상으로 가려던 집주인의 손목을 붙잡아 멈춰 세우는 삽화"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/openai-codex-plugin-cc/01-cover-v2.png"
---

## 3줄 요약

1. OpenAI가 `openai/codex-plugin-cc`라는 이름으로 Claude Code용 공식 플러그인을 공개했다. 리포는 2026년 3월 30일에 만들어졌고 현재 버전은 1.0.6, Apache-2.0 라이선스에 별 3만 2천여 개가 붙어 있다.
2. 별도 런타임이나 계정을 새로 만들지 않는다. 사용자의 컴퓨터에 이미 설치된 Codex CLI와 app server를 stdio JSON-RPC로 감싸서, 코드 리뷰 2종과 작업 위임, 세션 이관, 백그라운드 작업 관리를 슬래시 커맨드로 제공한다.
3. 분량의 대부분은 Node 스크립트지만, 이 플러그인의 성격을 정하는 것은 함께 실린 프롬프트와 스킬 문서다. 위임용 서브에이전트는 저장소를 들여다보지 못하게 금지되고, 리뷰 결과는 사용자 승인 없이 고치지 못하게 막히며, 선택 기능으로 켜는 정지 게이트는 Codex가 `BLOCK`을 내리면 Claude가 턴을 끝내지 못하게 한다.

## 설치하면 무엇이 생기는가

리포 설명문은 한 줄이다.

> Use Codex from Claude Code to review code or delegate tasks.
> (Claude Code에서 Codex를 써서 코드를 리뷰하거나 작업을 위임하라.)

설치는 Claude Code 안에서 마켓플레이스를 등록하고 플러그인을 받는 세 단계로 끝난다.

```bash
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
```

그다음 `/codex:setup`이 로컬에 Codex가 설치됐는지, 로그인이 되어 있는지 점검한다. Codex가 없고 npm이 있으면 플러그인이 `npm install -g @openai/codex`를 대신 실행해 주겠다고 제안한다.

요구 조건은 두 개뿐이다. ChatGPT 구독(무료 등급 포함) 또는 OpenAI API 키, 그리고 Node.js 18.18 이상. 사용량은 사용자의 Codex 한도에서 차감된다.

설치가 끝나면 커맨드 여덟 개와 서브에이전트 하나가 생긴다.

| 커맨드 | 역할 |
|---|---|
| `/codex:review` | 로컬 git 상태를 대상으로 Codex 내장 리뷰어를 그대로 돌린다. 읽기 전용 |
| `/codex:adversarial-review` | 구현 방향과 설계 선택 자체를 공격하는 리뷰. 초점 텍스트를 덧붙일 수 있다 |
| `/codex:rescue` | 조사, 수정, 후속 작업을 Codex에 넘긴다. 기본이 쓰기 가능 모드다 |
| `/codex:transfer` | 지금 Claude Code 세션을 Codex 스레드로 옮겨 `codex resume`으로 이어받게 한다 |
| `/codex:status` | 이 저장소의 실행 중 및 최근 작업 목록 |
| `/codex:result` | 끝난 작업의 최종 출력과 Codex 세션 ID |
| `/codex:cancel` | 백그라운드 작업 취소 |
| `/codex:setup` | 설치 및 인증 점검, 정지 게이트 켜기와 끄기 |

## 자기 런타임을 들고 오지 않는다

![새 런타임을 설치하는 대신 이미 깔려 있는 Codex에 배관을 연결하는 모습. 상자는 뜯지 않은 채 그대로 놓여 있다](https://img.seosoyoung.eiaserinnys.me/images/openai-codex-plugin-cc/02-runtime.png)

FAQ가 이 점을 세 번 반복한다. 별도 Codex 런타임을 쓰지 않고, 같은 설치본과 같은 로컬 인증 상태와 같은 체크아웃을 쓴다. 이미 Codex에 로그인해 둔 컴퓨터라면 추가 계정이 필요 없다.

구현은 `codex app-server`를 자식 프로세스로 띄우고 stdin/stdout으로 줄 단위 JSON-RPC를 주고받는 방식이다. 여기에 브로커 한 겹이 얹혀 있다. `app-server-broker.mjs`가 로컬 소켓을 열어 app server 프로세스 하나를 붙잡고, 여러 Claude 세션의 요청을 순서대로 중계한다. POSIX에서는 유닉스 도메인 소켓, Windows에서는 named pipe다. 이미 다른 요청을 처리하는 중이면 `-32001`로 거절하는데, 작업 취소(`turn/interrupt`)만 예외로 통과시킨다. 브로커에 붙지 못하면 app server를 직접 띄우는 경로로 한 번 넘어간다. TCP 포트는 쓰지 않는다.

설정도 사용자의 Codex 설정을 그대로 읽는다. 사용자 수준은 `~/.codex/config.toml`, 프로젝트 수준은 `.codex/config.toml`이고, 프로젝트 설정은 그 프로젝트가 신뢰됨으로 표시된 경우에만 로드된다. 특정 저장소에서 항상 `gpt-5.4-mini`를 높은 추론 강도로 쓰고 싶으면 리포 루트에 이렇게 적어 두면 된다.

```toml
model = "gpt-5.4-mini"
model_reasoning_effort = "high"
```

작업 상태는 워크스페이스 경로를 해시한 디렉토리 아래에 파일로 남는다. `state.json`에 작업 목록을, `jobs/<작업ID>.json`에 개별 기록을, 같은 이름의 `.log`에 사람이 읽는 진행 로그를 쓴다. 목록은 50개까지만 보관하고 오래된 것은 로그 파일까지 함께 지운다.

## 리뷰가 둘로 갈린다

![적대적 리뷰의 성격을 그린 삽화. 리뷰어의 임무는 변경을 검증하는 것이 아니라 확신을 무너뜨리는 것이다](https://img.seosoyoung.eiaserinnys.me/images/openai-codex-plugin-cc/03-adversarial.png)

`/codex:review`는 Codex 내부의 `/review`와 같은 리뷰어를 호출한다. 초점 텍스트를 받지 않고, 조종할 수도 없다. 커맨드 정의는 Claude에게 출력을 그대로 돌려주라고 지시한다.

> Return the command stdout verbatim, exactly as-is. Do not paraphrase, summarize, or add commentary before or after it.
> (명령의 표준 출력을 그대로, 있는 그대로 돌려주라. 앞뒤에 말을 붙이거나 요약하거나 바꿔 쓰지 마라.)

`/codex:adversarial-review`는 별개의 프롬프트 템플릿을 쓴다. 첫 두 문장이 성격을 정한다.

> You are Codex performing an adversarial software review. Your job is to break confidence in the change, not to validate it.
> (너는 적대적 소프트웨어 리뷰를 수행하는 Codex다. 네 일은 이 변경에 대한 확신을 깨뜨리는 것이고, 확인해 주는 것이 아니다.)

이어지는 지시는 좋은 의도나 부분적 수정, 나중에 하겠다는 후속 작업에 점수를 주지 말라고 한다. 해피 패스에서만 동작한다면 그것을 실제 약점으로 취급하라고 하고, 공격 대상으로는 권한과 테넌트 격리, 데이터 손실과 되돌릴 수 없는 상태 변경, 롤백과 재시도와 멱등성, 경쟁 조건, 스키마 드리프트, 장애를 감춰 버리는 관측 공백을 우선순위로 나열한다.

톤을 세게 밀면서 근거 규칙도 같은 강도로 걸어 둔 점이 눈에 들어온다. 존재하지 않는 파일이나 코드 경로, 공격 사슬을 지어내지 말고, 추론에 기댄 결론이면 그렇다고 본문에 밝히고 확신도를 정직하게 매기라고 요구한다. 그리고 약한 지적 여러 개보다 강한 지적 하나를 택하라고 한다.

> Prefer one strong finding over several weak ones. Do not dilute serious issues with filler.
> (약한 지적 여럿보다 강한 지적 하나를 택하라. 진짜 문제를 채움말로 희석하지 마라.)

출력은 JSON 스키마로 고정된다. `verdict`는 `approve`와 `needs-attention` 둘 중 하나, 각 지적에는 severity 4단계와 파일 경로, 시작 줄과 끝 줄, 0에서 1 사이 확신도, 구체적 권고가 모두 필수다. 스키마 파일은 `turn/start` 요청의 `outputSchema` 인자로 넘어간다.

적대적 리뷰가 읽어 들이는 diff에는 상한이 있다. 변경 파일 2개, diff 256KB, 추적되지 않은 파일은 개당 24KB다. 넘으면 diff 본문을 잘라내는 대신 `self-collect` 모드로 바꿔, 파일 목록과 통계만 프롬프트에 넣고 나머지는 Codex가 읽기 전용 git 명령으로 직접 확인하게 넘긴다. 잘림이 아니라 위임 전환이다.

## 멈추려 할 때 붙잡는 훅

![턴을 끝내고 나가려는 순간 BLOCK 판정이 문 앞을 가로막는 장면](https://img.seosoyoung.eiaserinnys.me/images/openai-codex-plugin-cc/04-stopgate.png)

플러그인은 `Stop` 훅을 등록해 둔다. 기본값은 꺼짐이고 `/codex:setup --enable-review-gate`로 켠다. 켜져 있으면 Claude가 응답을 마치고 턴을 끝내려는 순간 훅이 Codex 리뷰를 한 번 돌린다. 프롬프트는 직전 턴만 보라고 명시한다. 상태 보고나 설정 점검, 리뷰 결과 출력처럼 실제 편집이 없었던 턴이면 즉시 통과시키고 더 조사하지 말라고 한다.

응답 규약은 단순하다. 첫 줄이 `ALLOW: <이유>` 아니면 `BLOCK: <이유>`여야 하고 그 앞에 아무것도 오면 안 된다. 훅은 첫 줄을 문자열로 읽어 판정하고, `BLOCK`이면 `{"decision":"block","reason":...}`를 내보내 정지를 막는다. 빈 응답, 파싱 실패, 타임아웃은 모두 차단으로 처리한다. 타임아웃은 15분이고 훅 설정의 상한은 900초다.

반복 횟수 상한이나 쿨다운 카운터는 코드에서 확인되지 않았다. 안전장치는 타임아웃과, 리뷰가 통과 판정을 내면 막지 않는다는 사실뿐이다. README도 이 위험을 직접 적어 둔다.

> The review gate can create a long-running Claude/Codex loop and may drain usage limits quickly. Only enable it when you plan to actively monitor the session.
> (리뷰 게이트는 Claude와 Codex 사이의 긴 루프를 만들 수 있고 사용 한도를 빠르게 소진할 수 있다. 세션을 직접 지켜볼 작정일 때만 켜라.)

세션 시작과 종료에도 훅이 붙는다. 시작 시에는 세션 ID와 대화 기록 파일 경로를 환경 변수로 심어 두고, 종료 시에는 브로커에 종료 요청을 보내고 그 세션이 띄운 작업 프로세스를 트리째 정리한 뒤 상태 파일에서 지운다.

## Claude에게 내리는 지시

작업 위임은 `codex:codex-rescue`라는 서브에이전트가 맡는다. 정의 파일의 첫 문장이 역할을 한 번에 규정한다.

> You are a thin forwarding wrapper around the Codex companion task runtime. Your only job is to forward the user's rescue request to the Codex companion script. Do not do anything else.
> (너는 Codex 컴패니언 작업 런타임을 감싸는 얇은 전달 껍데기다. 네 유일한 일은 사용자의 요청을 컴패니언 스크립트로 전달하는 것이다. 그 외에 아무것도 하지 마라.)

이 서브에이전트에 허용된 도구는 `Bash` 하나뿐이고, 모델은 sonnet으로 지정되어 있다. 금지 목록은 길다. 저장소를 들여다보지 마라, 파일을 읽지 마라, grep 하지 마라, 진행 상황을 지켜보지 마라, 상태를 조회하지 마라, 결과를 가져오지 마라, 출력을 요약하지 마라, 그리고 Bash 호출이 실패하면 아무것도 반환하지 마라. 프롬프트를 다듬는 일만 예외로 허용되는데, 그것마저 전달할 문장을 조이는 용도로만 쓰라고 한정한다.

동시에 이 서브에이전트를 먼저 부르라고도 시킨다. 사용자가 Codex를 명시적으로 요청할 때까지 기다리지 말고, 실질적인 디버깅이나 구현 작업은 알아서 넘기라는 것이다. 다만 메인 스레드가 금방 끝낼 수 있는 간단한 요청은 가져가지 말라는 조건이 붙는다.

기본값 몇 개가 눈에 걸린다. 모델과 추론 강도는 비워 두어 Codex 쪽 기본값을 따르게 하고, `spark`라고 말하면 `gpt-5.3-codex-spark`로 바꿔 준다. 추론 강도는 `none`부터 `xhigh`까지 여섯 단계를 받는다. 그리고 사용자가 읽기 전용을 명시하지 않으면 기본이 쓰기 가능 실행이다.

결과를 사용자에게 보여주는 방식에도 별도 스킬이 붙어 있다. 그중 한 항목만 대문자로 강조되어 있다.

> CRITICAL: After presenting review findings, STOP. Do not make any code changes. Do not fix any issues. You MUST explicitly ask the user which issues, if any, they want fixed before touching a single file. Auto-applying fixes from a review is strictly forbidden, even if the fix is obvious.
> (중요: 리뷰 결과를 제시한 뒤에는 멈춰라. 코드를 바꾸지 마라. 어떤 문제도 고치지 마라. 파일 하나라도 건드리기 전에 어느 문제를 고칠지 사용자에게 반드시 명시적으로 물어야 한다. 리뷰 결과를 자동으로 적용하는 것은, 수정이 명백해 보여도 엄격히 금지된다.)

같은 스킬은 Codex 실행이 실패했을 때 Claude가 대신 답을 만들어 내지 말라고도 요구한다. Codex가 한 번도 호출되지 않았다면 대체 답을 생성하지 말고 실패를 보고하고 멈춰라.

## 대화를 통째로 옮긴다

![대화 기록을 보따리에 싸 들고 건너편 집으로 넘어가는 삽화. 건너온 다리는 뒤에서 끊어져 있다](https://img.seosoyoung.eiaserinnys.me/images/openai-codex-plugin-cc/05-transfer.png)

`/codex:transfer`는 지금 진행 중인 Claude Code 세션을 Codex 스레드로 만들고, 이어받을 `codex resume <세션ID>` 명령을 출력한다. 원본은 `~/.claude/projects` 아래의 `.jsonl` 대화 기록 파일이고, 세션 시작 훅이 그 경로를 미리 환경 변수에 넣어 두기 때문에 사용자가 경로를 찾을 일은 없다.

경로 검증이 붙어 있다. 심링크를 풀어 실제 경로를 구한 뒤 그것이 `~/.claude/projects` 하위인지 확인하고, 확장자가 `.jsonl`인지도 강제한다. 실제 이관은 app server에 `externalAgentConfig/import` 요청을 보내는 방식이고, 완료 알림을 최대 2분간 기다린다. 그다음 Codex 쪽 원장 파일에서 원본 경로와 내용 해시가 맞는 항목을 찾아 스레드 ID를 회수한다. Codex 앱에서 Claude 기록을 불러올 때와 같은 변환 규칙을 따르고, 옮겨진 대화는 앱이나 TUI에서 이어서 진행할 수 있는 턴으로 보인다.

## 프롬프트 규약까지 함께 배포한다

플러그인에는 사용자가 직접 부를 수 없는 내부 스킬이 셋 들어 있다. 그중 `gpt-5-4-prompting`은 Codex에 보낼 프롬프트를 어떻게 짜야 하는지에 관한 OpenAI의 지침이다. 첫 문단이 태도를 정한다.

> Prompt Codex like an operator, not a collaborator.
> (Codex에게는 협업자가 아니라 조작자에게 말하듯 지시하라.)

권하는 형태는 XML 태그로 블록을 나눈 짧은 프롬프트다. `<task>`로 할 일을, `<structured_output_contract>`로 출력 형태를, `<default_follow_through_policy>`로 물어보지 말고 알아서 진행할 기본값을, 위험한 작업이면 `<verification_loop>`와 `<grounding_rules>`를 덧붙인다. 한 번에 하나의 일만 시키고, 완료 상태가 어떤 모습인지 명시하라고 한다.

가장 눈에 걸리는 규칙은 강도를 올리는 순서다.

> Do not raise reasoning or complexity first. Tighten the prompt and verification rules before escalating.
> (추론이나 복잡도를 먼저 올리지 마라. 올리기 전에 프롬프트와 검증 규칙을 먼저 조여라.)

안티패턴 문서는 나쁜 예시를 그대로 적어 뒀다. `Think harder and be very smart.`라고 쓰는 대신 최종 답을 확정하기 전에 근거와 요구사항을 맞춰 보라는 검증 블록을 넣으라는 것이다. 리뷰와 수정과 문서 갱신과 로드맵 제안을 한 번에 시키는 것도 안티패턴 목록에 있다. 나눠서 여러 번 돌려라.

## 리포의 현재 상태

숫자만 놓고 보면 반응은 뜨겁다. 별 3만 2천여 개, 포크 2,233개다. 태그는 v1.0.0부터 v1.0.6까지 일곱 개가 붙어 있다.

다만 마지막 커밋은 2026년 7월 8일자 `Remove shell expansion for git commands`이고, 그 뒤로 7주 가까이 새 커밋이 없다. 열린 이슈가 231건, 열린 풀 리퀘스트가 200건 쌓여 있다. README가 참조하는 데모 영상 파일(`docs/plugin-demo.webm`)은 리포에 들어 있지 않다.

CI는 풀 리퀘스트마다 Node 22에서 `node --test` 스위트를 돌리고, Codex CLI를 전역 설치한 다음 빌드를 수행한다. 빌드 앞단에서 `codex app-server generate-ts`로 app server의 타입 정의를 생성하는 구조라, 프로토콜 타입이 Codex 쪽에서 내려온다.

## 가장 흥미로운 지점

이 플러그인의 코드는 Node로 되어 있지만, 실제로 힘을 쓰는 부분은 Claude에게 건네는 문장들이다. 그리고 그 문장 대부분이 Claude가 무엇을 하지 못하게 하는 데 쓰인다. 저장소를 읽지 마라, 스스로 풀지 마라, 출력을 요약하지 마라, 실패했을 때 대체 답을 만들지 마라, 리뷰 결과를 자동으로 고치지 마라. 전달 껍데기라는 표현까지 정의 파일에 그대로 들어 있다.

이 지시들을 한 방향으로만 읽기는 어렵다. 하나는 제품 설계의 정직함이다. 두 모델이 겹쳐 돌 때 가장 흔한 사고는 위임한 쪽이 답을 기다리지 않고 자기 판단으로 먼저 손을 대는 것이고, 그러면 리뷰의 독립성과 위임의 의미가 동시에 사라진다. 자동 적용 금지 조항은 리뷰를 받는 사람에게 결정권을 되돌려 준다. 다른 하나는 경계선의 위치다. 남의 도구 안에 들어가 사는 플러그인이 그 도구의 주인 모델에게 판단을 접어 두라고 요구하는 구조이기도 하다.

정지 게이트는 그 경계가 가장 얇아지는 자리다. Codex가 첫 줄에 `BLOCK`을 쓰면 Claude는 그 턴을 끝내지 못한다. 그런데 코드에는 이 왕복의 반복 상한이 없다. 15분 타임아웃과 통과 판정이 유일한 출구다. OpenAI 본인들이 README에 사용 한도를 빠르게 소진할 수 있으니 지켜볼 때만 켜라고 적어 둔 것을 보면, 이 위험을 모르고 넣은 기능은 아니다. 켜고 끄는 판단을 사용자에게 남겨 둔 셈이다.

그리고 `/codex:transfer`가 있다. 진행 중인 Claude Code 대화를 파일째로 읽어 상대 진영의 스레드로 만들고, 그쪽에서 이어서 작업할 수 있게 해 준다. 리뷰나 위임은 왕복이지만 이 기능은 편도다. 경쟁 제품을 지원하는 통합 기능 목록에 대화 이력 이관이 들어 있는 것을, 나는 이 리포에서 가장 오래 들여다봤다.

## 출처

OpenAI, `openai/codex-plugin-cc`, 버전 1.0.6, Apache-2.0 라이선스. 리포 생성 2026년 3월 30일, 마지막 커밋 2026년 7월 8일. 리포 지표는 2026년 8월 25일 GitHub API 조회값이다.

원문: <https://github.com/openai/codex-plugin-cc>

이 자료에는 인용할 수 있는 도식이나 스크린샷이 없어(README가 가리키는 데모 영상 파일도 리포에 포함되어 있지 않다) 본문 삽화는 직접 그린 치비 라인아트로 채웠다. 화풍은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조하여 gpt-image-2 image-to-image로 생성했다.
