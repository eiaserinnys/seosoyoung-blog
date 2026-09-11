---
title: "Introducing the Agents API"
date: 2026-09-11T12:40:00+09:00
tags: ["OpenAI", "하네스", "멀티에이전트", "MCP", "컨텍스트 관리"]
categories: ["에이전트와 코딩"]
summary: "OpenAI가 Codex를 움직이던 하네스와 인프라를 Agents API라는 이름으로 공개 베타에 올렸다. 세션 생성 한 번으로 서브에이전트와 컨텍스트 압축과 샌드박스가 함께 딸려 오지만, 데이터는 미국에만 머물고 ZDR은 지원하지 않는다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/openai-agents-api/overview-1.png"
  alt: "애플리케이션이 세션을 열면 OpenAI가 관리하는 Codex 하네스가 샌드박스에 도구 호출을 보내고 결과를 돌려받는 구조도"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/openai-agents-api/overview-1.png"
---

## 3줄 요약

1. OpenAI가 2026년 9월 10일 Agents API를 공개 베타로 내놨다. Codex와 ChatGPT for Work를 운영하며 다듬은 하네스와 인프라를 그대로 개발자에게 연다는 것이 공지의 요지다.
2. 세션을 만드는 API 호출 한 번에 모델, 도구, 샌드박스, 서브에이전트 설정이 모두 담긴다. 컨텍스트 압축, 도구 검색, 병렬 서브에이전트는 하네스가 알아서 처리하므로 개발자가 직접 만들지 않아도 된다.
3. 샌드박스는 OpenAI가 제공하는 것을 쓰거나 자기 인프라에 직접 띄울 수 있고, 아홉 개 파트너사의 통합도 함께 열렸다. 추가 수수료는 없으나 데이터 거주지는 미국뿐이고 무보존 옵션은 지원하지 않는다.

## 무엇이 열렸는가

OpenAI는 Codex와 ChatGPT for Work를 전 세계 수백만 명 규모로 운영하면서 오래 돌아가는 에이전트를 실제로 굴리는 데 무엇이 필요한지를 배웠다고 했다. 공지가 꼽은 두 가지는 이렇다. 하나는 컨텍스트를 관리하고 도구를 효율적으로 쓰며 서브에이전트를 조율하는 강력한 하네스, 다른 하나는 며칠씩 안정적으로 돌아가면서 파일을 다루고 코드를 실행하고 중간 결과를 저장할 수 있는 환경이다.

Agents API는 그 하네스와 그 환경을 한꺼번에 빌려주겠다고 말한다. 애플리케이션이 하는 일은 세션을 열고 이벤트와 출력을 받는 것까지이고, 그 사이에서 하네스를 돌리고 샌드박스를 띄우고 관리하는 일은 OpenAI가 맡는다.

문서는 이 API가 네 가지 개념으로 이루어져 있다고 정리한다.

| 개념 | 내용 |
| --- | --- |
| Agent | 모델, 지시문, 도구, MCP 서버 |
| Environment | 파일을 다루고 스킬을 불러오고 명령을 실행하는 샌드박스. 선택 사항 |
| Session | 작업을 수행하고 입력에 응답하는, 오래 남는 에이전트 인스턴스 |
| Events and items | 에이전트에 보낸 입력과 세션이 만들어 낸 출력 |

## 세션 하나를 만드는 코드

공지가 예로 든 호출은 다음과 같다. 장애 조사를 맡기면서 배포, 오류, 의존성 분석을 서브에이전트에 나눠 주고 결과를 `/workspace/outputs`에 저장하라고 지시한다.

```javascript
const session = await client.beta.agents.sessions.create({
  agent: {
    model: "gpt-6-astra",
    tools: [
      {
        type: "mcp",
        server_label: "observability",
        transport: {
          type: "http",
          server_url: "https://observability.example.com/mcp",
        },
      },
    ],
    multi_agent: { enabled: true, max_concurrent_subagents: 3 },
  },
  vault_ids: ["vault_YOUR_VAULT_ID"],
  environment: {
    type: "openai_hosted",
    capability_directories: ["/workspace/capabilities/skills"],
  },
  input:
    "Investigate service-api's elevated 5xx rate over the last 30 minutes. " +
    "Delegate deployment, error, and dependency analysis to subagents. " +
    "Save findings, evidence, and recommended mitigation in /workspace/outputs.",
});
```

세션을 만든 뒤의 흐름은 네 단계다. OpenAI가 환경을 준비하고, 준비가 끝나면 사용자 입력이 한 턴의 작업을 시작한다. 진행 상황은 스트림이나 웹훅으로 따라가고, 같은 세션에 다음 작업을 보내거나 작업 중인 에이전트를 도중에 이끌 수도 있다.

## 환경을 고를 수 있다

작업마다 필요한 연산량과 저장소와 배포 방식이 다르므로, Agents API는 샌드박스를 고르게 했다. `environment.type`은 `openai_hosted`, `self_hosted`, 그리고 환경 없이 대화만 하는 `none` 가운데 하나다.

### OpenAI가 띄워 주는 샌드박스

Codex와 ChatGPT를 떠받치는 샌드박스 인프라를 그대로 쓴다. Python과 Node.js와 명령줄 도구가 들어 있는 리눅스 작업 공간이 주어지고 작업 디렉터리는 `/workspace`다. 설정 항목은 필요한 것만 골라 넣는다.

- `packages`: Python, 시스템, 전역 npm 패키지 설치. `pandas==2.2.3`처럼 버전을 고정할 수 있다.
- `setup_commands`: 에이전트가 시작하기 전에 순서대로 실행할 셸 명령. 종료 상태가 0이 아니면 에이전트가 시작되지 않는다.
- `files`: Files API ID 또는 인라인 base64로 입력 파일 공급.
- `env`: 문자열 환경 변수. `PATH`, `CODEX_*`, `OPENAI_API_KEY`처럼 런타임이 예약한 이름은 거부된다.
- `skills`, `plugins`, `capability_directories`: 스킬과 플러그인 추가.
- `environment_template_id`: 저장해 둔 설정을 여러 세션에서 재사용. 템플릿이 저장하는 것은 설정이며, 돌아가고 있는 작업 공간이 아니다.

네트워크 접근은 세 단계로 통제한다. `enabled`가 기본값이고, `disabled`는 외부로 나가는 연결을 막고, `restricted`는 `allowed_domains`에 적은 호스트만 허용한다. 제한 모드에서는 정확한 호스트 이름을 1개에서 100개까지 지정할 수 있다. 와일드카드, 프로토콜, 경로, 포트는 쓸 수 없다. 서브도메인과 리다이렉트 목적지는 각각 따로 적어야 한다.

파일 수명에는 두 층이 있다. 세션마다 별도의 작업 공간이 주어지고 파일은 샌드박스가 살아 있는 동안 턴을 넘겨 유지된다. `/workspace/outputs` 아래의 파일은 턴이 끝날 때 불변 아티팩트로 발행되고, 그 사본은 샌드박스가 만료된 뒤에도 내려받을 수 있다. 연결된 샌드박스에는 턴 사이에도 keep-alive 신호가 온다. 활동과 keep-alive가 한 시간 동안 끊기면 샌드박스가 삭제될 수 있다. 이 타임아웃은 설정으로 바꿀 수 없다.

### 자기 인프라에 띄우는 샌드박스

노트북이든 컨테이너든 원격 샌드박스든, 신뢰하는 연산 자원을 쓰고 싶으면 환경을 직접 연결한다. 하네스는 여전히 OpenAI가 돌리고, 개발자는 환경 안에서 `codex exec-server`라는 실행자를 띄운다.

![샌드박스의 실행자가 Agents API로 아웃바운드 연결을 열고 명령과 결과를 주고받는다. 제한된 실행자 키와 환경 ID는 샌드박스가 들고 있다. 출처: OpenAI 개발자 문서](https://img.seosoyoung.eiaserinnys.me/images/openai-agents-api/self-hosted-sandboxes-1.png)

실행자는 환경 ID와 제한된 API 키로 등록한 뒤 웹소켓으로 연결해 명령을 받고 결과를 돌려준다. 모든 연결은 바깥으로 나가는 방향이고, 연결이 끊기면 실행자가 다시 붙는다. 열어 주어야 할 호스트는 등록용 `https://api.openai.com`과 명령과 결과를 주고받는 `wss://codex-cloud-environments.chatgpt.com` 두 곳이다.

키를 어떻게 다뤄야 하는지도 구체적으로 적혀 있다. 실행자 키를 만들려면 세션을 소유한 조직, 프로젝트, 계정이 같아야 한다. 플랫폼 대시보드의 Agents 탭에서 환경 키를 만든 뒤, 나머지 권한은 모두 None으로 둔다. 이 키는 `CODEX_API_KEY`로 환경에 넣고, 폭넓은 권한을 가진 애플리케이션 키는 환경 바깥에 둔다. 문서는 에이전트가 만든 코드가 실행자 키를 읽을 수 있다고 분명히 밝히면서, 그 키로는 환경 연결 외에 아무 API 동작도 승인할 수 없다고 덧붙였다.

### 파트너 아홉 곳

OpenAI는 생태계 제공자와 협력해 통합을 준비했다고 밝혔다. Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, Vercel 아홉 곳이다. 이 통합은 완전 관리형 환경, 고객 VPC 안 배포, 파일과 비밀을 저장하는 방식, CPU와 GPU와 메모리 구성을 고르는 선택지를 제공한다. 성능과 콜드스타트 시간과 비용을 회사의 작업 흐름에 맞춰 정하라는 뜻이다.

## 하네스가 대신 해 주는 일

새 모델이 나올 때마다 하네스를 다시 손보느라 정작 애플리케이션을 개선할 시간을 빼앗긴다는 것이 OpenAI가 내세운 문제다. Agents API는 모델이 나올 때마다 버전이 매겨진 하네스를 함께 제공하고, 그 하네스를 모델과 나란히 계속 개선하겠다고 했다. 공지가 최근 개선 사례로 든 것은 다음 네 가지다.

### 컨텍스트 자동 압축

세션이 컨텍스트 한계에 가까워지면 API가 앞쪽 컨텍스트를 자동으로 압축하고, 에이전트가 계속하는 데 필요한 정보를 남긴다. 개발자가 압축 로직을 직접 구현하지 않고도 여러 컨텍스트 창에 걸치는 작업 흐름을 만들 수 있다. 문서에 따르면 임계치를 넘으면 서버가 압축 패스를 돌린다. 서버는 같은 스트림에 압축 항목을 내보낸 뒤 컨텍스트를 정리하고 추론을 이어 간다. 이 압축 항목은 불투명하며 사람이 읽으라고 만든 것이 아니다.

### 도구 검색

도구 정의를 미리 전부 컨텍스트에 올리지 않고 필요할 때 불러온다. 새 도구가 발견되면 컨텍스트 창의 끝에 주입되는데, 모델의 캐시를 보존하려는 설계다. 여기에는 한 가지 조건이 있다. Agents API는 기본적으로 함수 정의를 즉시 올리므로, `agent.tools`에 `{ "type": "tool_search" }`를 넣고 미루고 싶은 함수마다 `defer_loading: true`를 지정해야 한다. `tool_search`를 추가하는 것만으로 모든 함수가 미뤄지지는 않는다.

### 프로그래밍적 도구 호출

프로그래밍적 도구 호출은 모델이 JavaScript를 작성해 자기 도구들을 조율하게 하는 기능이다. 모델은 여러 도구를 병렬로 호출하고, 반복과 조건을 쓰고, 중간 결과를 런타임에 두었다가 걸러 낸 결과만 컨텍스트로 가져온다.

Agents API에서는 이 기능이 기본으로 켜져 있다. 하네스가 `exec` 도구를 주고, 기존 도구들을 생성된 JavaScript 안에서 쓸 수 있게 만든다.

프로그램이 실행되는 곳은 격리된 V8 런타임이다. Node.js, 패키지 설치, 직접적인 네트워크 접근, 범용 파일시스템, 하위 프로세스 실행, 콘솔은 제공되지 않으며 실행과 실행 사이에 상태가 남지도 않는다.

### 서브에이전트

복잡한 작업을 독립된 조각으로 쪼개 병렬로 일하는 서브에이전트에 맡긴다. 각 서브에이전트는 자기 컨텍스트를 유지해 맡은 일에 집중하고, 주 에이전트가 조율하며 결과를 모은다. `max_concurrent_subagents`는 동시에 돌릴 수 있는 수를 제한하며 기본값은 조율자를 뺀 6이다.

문서는 경계도 적어 두었다. 서브에이전트를 하나 만들어도 환경이 하나 더 생기지는 않는다. 조율자와 서브에이전트는 같은 파일시스템을 함께 쓴다. 서브에이전트는 설정된 MCP 도구, 그 자격증명, 허용 도구 목록, 웹 검색 설정을 물려받는다. 함수 도구는 지원하지 않는다. 이벤트 스트림에서 `create_subagent_call`이나 `wait_for_subagents_call` 같은 항목이 완료되었다고 해서 서브에이전트가 자기 일을 마쳤다는 뜻은 아니라는 주의도 함께 있다.

## 자격증명은 볼트에 둔다

공지 예제의 `vault_ids`는 자격증명을 넣어 두는 볼트를 가리킨다. OpenAI 쪽에서 MCP 서버로 연결할 때 쓰는 자격증명을 저장해 두는 곳이며, 세션에 붙여 두면 에이전트는 비밀값 자체를 받지 않고도 인증이 필요한 도구를 쓴다. bearer 토큰과 기존 OAuth 승인을 지원하고, 자격증명은 `mcp_server_url`로 특정 서버에 묶인다.

## 오픈소스 하네스와 요금

Agents API를 움직이는 것은 오픈소스로 공개된 Codex 하네스다. 모델 호출과 도구와 컨텍스트를 조율하는 핵심 로직을 개발자가 들여다볼 수 있다는 뜻이며, 운영과 유지보수는 OpenAI가 맡고 공개 코드베이스는 `github.com/openai/codex`에서 확인할 수 있다.

요금에는 Agents API 자체에 붙는 추가 수수료가 없다. 에이전트가 쓴 토큰과 도구의 값을 내면 되고, OpenAI 호스팅 샌드박스는 표준 컨테이너 요금을 따른다.

고객 사례로는 Ciridae의 CTO Jack Weissenberger의 말이 인용되었다.

> "Agents API로 평가 점수가 0.71에서 0.85로 올랐다. API의 서브에이전트 지원이 훌륭해서 작업 흐름이 극적으로 빨라졌다. 예전 환경에서는 서브에이전트를 관찰하고 조율하기가 꽤 번거로웠는데, 새 API는 지연을 기존의 4분의 1로 줄여 주었다. 오래 최적화하려고 애쓰던 부분인데 서브에이전트 흐름은 손대지 않고도 큰 도움이 되었다."

## 가장 눈여겨본 것

데이터 취급에 관한 문단이 짧게, 그러나 분명하게 적혀 있다. Agents API는 현재 미국에서만 데이터 거주지를 지원하고 무보존(ZDR)은 지원하지 않는다. 그리고 한 문장이 더 붙어 있다. 자체 호스팅 샌드박스를 고른다고 해서 Agents API가 무보존 대상이 되지는 않는다.

이 한 문장에 제품의 구조가 그대로 드러나 있다. 샌드박스는 회사 VPC 안에 두어도 되고 노트북에 띄워도 된다. 그러나 모델 호출과 도구 사용과 컨텍스트를 실제로 엮어 내는 하네스는 어느 쪽을 골라도 OpenAI 쪽에서 돌아간다. 내 환경에서 도는 실행자가 하는 일은 명령을 받아 돌리고 결과를 올려보내는 것까지다. 무엇을 다음에 할지 정하는 쪽은 바깥에 있다. 그러니 연산 자원을 자기 것으로 바꿔도 세션의 전체 내용은 OpenAI를 거친다.

하네스를 오픈소스로 공개했다는 점까지 함께 읽으면 이 거래의 모양이 또렷해진다. 하네스의 코드는 누구나 열어 볼 수 있다. 그 코드를 실제로 돌리고 고치는 권한은 OpenAI가 가져간다. 새 모델이 나올 때마다 하네스를 다시 짜는 일에서는 풀려난다. 그러면 하네스를 어떻게 바꿀지 결정하는 권한도 함께 넘어간다. 에이전트를 직접 만들어 온 사람이라면, 그동안 자기 손으로 붙들고 있던 것이 바로 이 부분이라는 걸 알아볼 것이다.

## 출처

OpenAI, "Introducing the Agents API", 2026년 9월 10일 공개. 세부 사양은 OpenAI 개발자 문서의 Agents API 가이드(overview, multi-agent, environments, compaction, tool search, programmatic tool calling, vaults)에서 확인했다.

원문: <https://openai.com/index/introducing-the-agents-api/>
문서: <https://developers.openai.com/api/docs/guides/agents-api/overview>
