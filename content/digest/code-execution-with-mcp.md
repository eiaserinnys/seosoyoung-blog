---
title: "Code execution with MCP for efficient agents"
date: 2026-11-23T18:30:00+09:00
tags: ["MCP", "Anthropic", "컨텍스트 관리", "Agent Skills"]
categories: ["에이전트와 코딩"]
subjects: ["스킬과 도구 연결"]
summary: "다수의 MCP 서버와 도구를 연결하면 토큰 과부하가 생긴다. Anthropic은 MCP 서버를 파일시스템 기반 코드 API로 제공해 이 문제를 풀고, 토큰 소비를 98.7% 절감하는 설계를 제시한다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/code-execution-with-mcp/01-cover.jpg"
  alt: "올리브색 배경 위에 다섯 개의 격자 막대가 수평으로 배열된 Anthropic 아티클 대표 일러스트"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/code-execution-with-mcp/01-cover.jpg"
---

## 3줄 요약

1. 2025년 11월 Anthropic 엔지니어 Adam Jones와 Conor Kelly는 대규모 MCP 환경을 위한 코드 실행 아키텍처를 공개했다. 에이전트에 연결하는 MCP(Model Context Protocol) 도구가 수백에서 수천 개로 늘어나면 컨텍스트 비용과 지연 시간이 문제가 되는데, 이를 코드 실행 환경으로 해결하는 방법을 다룬다.
2. 기존 MCP 클라이언트는 시작할 때 모든 도구 정의를 컨텍스트 윈도우에 포함시키고, 중간 실행 결과까지 모델 컨텍스트로 전달한다. 반면 MCP 서버를 파일시스템의 코드 API로 변환하면, 에이전트는 필요한 도구만 골라 읽고 실행 환경에서 데이터를 직접 가공할 수 있다.
3. 이 설계를 쓰면 Google Drive 문서를 Salesforce에 기록하는 작업의 토큰 사용량이 150,000토큰에서 2,000토큰으로, 98.7% 줄어든다. 대용량 데이터를 필터링하고 조건문과 반복문을 실행하는 일, 민감 정보를 토큰화하고 재사용할 수 있는 스킬을 만드는 일도 지원한다.

## 도구 규모가 커질 때 기존 MCP 호출이 겪는 두 가지 병목

2024년 11월 공개된 MCP는 AI 에이전트와 외부 시스템을 잇는 오픈 표준 프로토콜이다. 과거에는 에이전트를 외부 데이터 저장소나 업무 도구와 연결할 때마다, 조합별로 전용 연동 코드를 따로 작성해야 했다. 에이전트에 MCP를 한 번 구현해 두면 커뮤니티가 만든 수천 개의 MCP 서버를 쓰고, 주요 프로그래밍 언어별 SDK 생태계도 곧바로 활용할 수 있다. 이 덕분에 지금 개발자들은 한 에이전트에 수십 개의 MCP 서버, 수백에서 수천 개의 도구를 연결해 쓴다.

연결된 도구 수가 많아지자 기존 직접 도구 호출(direct tool-calling) 방식에서 두 가지 문제가 드러났다. 에이전트의 응답 속도가 느려지고 비용이 함께 증가한다.

첫째는 **도구 정의가 컨텍스트 윈도우에 과부하를 일으키는 문제**다. 대다수 MCP 클라이언트는 에이전트가 작업을 시작하기 전에 연결된 모든 도구의 스키마 정의를 모델의 컨텍스트 윈도우에 한꺼번에 불러온다. 예를 들어 Google Drive 문서를 조회하는 `gdrive.getDocument`와 Salesforce 레코드를 수정하는 `salesforce.updateRecord(objectType, recordId, data)`가 있다. 이 도구들은 정의마다 도구 설명, 필수 파라미터와 선택 파라미터의 명세, 반환 객체 구조를 텍스트로 담고 있다.

```text
gdrive.getDocument
  Description: Retrieves a document from Google Drive
  Parameters:
    documentId (required, string): The ID of the document to retrieve
    fields (optional, string): Specific fields to return
  Returns: Document object with title, body content, metadata, permissions, etc.
```

연결된 도구가 수천 개로 늘어나면 에이전트는 사용자의 요청 문장을 읽기도 전에 수십만 토큰의 도구 정의를 먼저 처리해야 한다.

| 병목 원인 | 발생 시점 | 컨텍스트 소비 규모 |
|---|---|---|
| 도구 정의 일괄 적재 | 사용자 요청을 읽기 전 초기화 단계 | 수천 개 도구 연결 시 수십만 토큰을 미리 소모 |
| 중간 실행 결과 왕복 | 도구 호출 사이의 데이터 복사 단계 | 2시간 회의록 이관 시 약 50,000토큰 추가 소모 |

둘째는 **중간 도구 실행 결과가 토큰을 추가로 소비하는 문제**다. 사용자가 에이전트에게 "Google Drive에서 회의록을 내려받아 Salesforce 리드에 첨부해 줘"라고 요청하는 상황을 가정해 보자. 직접 도구 호출 방식에서 모델은 두 번의 도구 호출을 순차로 실행한다.

```text
TOOL CALL: gdrive.getDocument(documentId: "abc123")
        → returns "Discussed Q4 goals...\n[full transcript text]"
           (모델 컨텍스트에 전문 포함)

TOOL CALL: salesforce.updateRecord(
            objectType: "SalesMeeting",
            recordId: "00Q5f000001abcXYZ",
            data: { "Notes": "Discussed Q4 goals...\n[full transcript text written out]" }
        )
        (모델이 회의록 전문을 컨텍스트에 다시 생성)
```

첫 번째 호출이 돌려준 회의록 전문이 모델 컨텍스트에 포함된 뒤, 모델은 두 번째 호출의 인자를 채우려고 같은 회의록을 처음부터 끝까지 다시 출력해야 한다. 영업 회의록 하나가 2시간 분량일 때, 두 도구 사이에 본문을 옮기는 일에만 약 50,000토큰이 더 쓰인다. 문서가 컨텍스트 한도를 초과하면 작업이 중단된다. 방대한 텍스트나 복잡한 데이터 구조를 모델이 도구 호출 사이에 복사하다 보면, 내용이 빠지거나 바뀌는 오류도 생기기 쉽다.

![기존 MCP 클라이언트가 도구 정의와 매 호출의 중간 결과를 모델의 컨텍스트 윈도우에 반복 포함하며 메시지 루프를 실행하는 구조](https://img.seosoyoung.eiaserinnys.me/images/code-execution-with-mcp/02-mcp-context-loop.png)
*기존 MCP 클라이언트는 도구 정의를 모델 컨텍스트 윈도우에 불러오고, 매 도구 호출과 실행 결과가 모델 컨텍스트에 반복 포함되는 메시지 루프를 반복한다. (출처: Anthropic)*

## MCP 서버를 코드 API와 파일시스템으로 변환하는 구조

에이전트용 코드 실행 환경(샌드박스)이 널리 쓰이게 되자, Anthropic은 MCP 서버를 도구로 직접 호출하게 하는 대신 코드 API로 제공하는 해법을 제시했다[^1]. 연결된 MCP 서버의 도구를 파일시스템의 디렉터리와 소스 파일 트리로 만들어 두고, 에이전트가 코드를 작성해 그 도구를 호출하게 하는 방식이다.

[^1]: Cloudflare도 같은 문제의식에서 MCP 서버를 코드 실행으로 다루는 방식을 'Code Mode'라는 이름으로 발표한 바 있다. LLM이 개별 도구 호출 문법보다 코드 작성에 능숙하다는 점을 활용한 접근이다.

TypeScript 환경이라면 연결된 MCP 서버들이 다음과 같은 파일 트리로 구성된다.

```text
servers
├── google-drive
│   ├── getDocument.ts
│   ├── ... (기타 도구 파일)
│   └── index.ts
├── salesforce
│   ├── updateRecord.ts
│   ├── ... (기타 도구 파일)
│   └── index.ts
└── ... (기타 서버 디렉터리)
```

각 파일은 해당 MCP 도구의 입출력 타입 인터페이스를 정의하고, 내부에서 MCP 클라이언트의 `callMCPTool`을 호출하는 래퍼 함수를 내보낸다.

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

/* Read a document from Google Drive */
export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
}
```

| 파일 트리 계층 | 경로 예시 | 역할 |
|---|---|---|
| 서버 루트 디렉터리 | `./servers/` | 연결된 전체 MCP 서버 목록 제공 |
| 서버별 모듈 폴더 | `./servers/google-drive/` | 개별 MCP 서버의 도구 파일 묶음 및 `index.ts` 노출 |
| 개별 도구 래퍼 파일 | `./servers/google-drive/getDocument.ts` | 입출력 TypeScript 인터페이스와 `callMCPTool` 호출 정의 |

Google Drive에서 회의록을 가져와 Salesforce에 덧붙이던 앞선 예시는 다음과 같은 짧은 TypeScript 코드로 구현된다.

```typescript
// Google Docs에서 회의록을 읽어 Salesforce 리드에 추가
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

도구를 찾는 과정은 `./servers/` 디렉터리 목록을 읽어 연결된 서버(`google-drive`, `salesforce`)를 확인하는 데서 출발한다. 그 뒤에는 이번 작업에 쓸 `getDocument.ts`와 `updateRecord.ts` 두 파일만 읽어 함수의 입출력 시그니처를 확인한다. 회의록 본문은 코드 실행 환경의 `transcript` 변수에 저장된 채 Salesforce 업데이트 함수로 바로 전달되고, 모델 컨텍스트에는 포함되지 않는다. 그 결과 작업 전체의 토큰 소비량이 **150,000토큰에서 2,000토큰으로 줄었고, 비용과 시간이 98.7% 절감됐다.**

| 비교 항목 | 기존 직접 도구 호출 방식 | 코드 실행 기반 MCP 방식 |
|---|---|---|
| 도구 정의 조회 | 연결된 모든 도구 스키마를 시작 시 한꺼번에 불러옴 | 디렉터리 탐색이나 검색으로 필요한 도구 파일만 골라서 불러옴 |
| 중간 데이터 전달 | 매 도구 반환값과 다음 호출 인자가 모델 컨텍스트에 포함됨 | 코드 실행 환경의 변수와 메모리에서 도구 간 직접 전달 |
| 제어 흐름 처리 | 모델 추론 루프를 반복하며 개별 도구 호출을 연쇄 실행 | 단일 코드 블록의 반복문, 조건문, 예외 처리로 일괄 실행 |
| 회의록 이관 예시 토큰 | 150,000토큰 | 2,000토큰 (98.7% 절감) |

## 코드 실행과 MCP를 결합해 얻는 네 가지 이점

코드 실행 환경을 MCP와 결합했을 때 얻는 실무상 이점은 토큰 절감을 포함해 네 가지로 요약된다.

### 1. 점진적 도구 탐색(Progressive disclosure)

모델은 파일시스템을 탐색해 필요한 정보를 찾아내는 작업에 익숙하다. 도구를 파일 트리로 배치하면 모델이 필요한 정의만 온디맨드로 읽을 수 있다. 파일 탐색 대신 서버에 `search_tools`라는 도구를 추가해 키워드(예: `"salesforce"`)로 관련 도구를 검색하게 구성할 수도 있다. 이때 `search_tools`에 상세 수준(detail level) 파라미터를 두면, 에이전트가 조회 범위를 직접 고를 수 있다. 필요에 따라 도구 이름만 받아 볼 수도 있고, 이름과 설명이나 전체 스키마 정의까지 요청할 수도 있다. 이렇게 하면 컨텍스트 소비가 한층 정밀하게 조절된다.

| 상세 수준 | 반환 정보 | 적합한 사용 단계 |
|---|---|---|
| 이름만 조회 | 도구 식별자 목록 | 관련 도구가 있는지와 후보를 빠르게 확인 |
| 이름과 설명 | 도구 식별자와 기능 요약 | 현재 작업에 적합한 도구 최종 선별 |
| 전체 스키마 정의 | 입출력 파라미터 타입과 전체 스키마 | 호출 코드 작성 직전의 인터페이스 확인 |

### 2. 컨텍스트를 아끼는 결과 처리와 제어 흐름

대규모 데이터셋을 다룰 때 에이전트는 데이터를 모델로 반환하기 전에 코드 실행 환경에서 필터링과 집계를 먼저 수행할 수 있다. 10,000행짜리 스프레드시트에서 보류 중인 주문만 확인하는 경우를 비교해 보자.

```typescript
// 코드 실행 환경에서 필터링 후 요약만 출력
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(row => 
  row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // 검토용으로 처음 5행만 출력
```

직접 도구 호출에서는 10,000행 전체가 컨텍스트에 포함되지만, 코드 실행 환경에서 모델이 받는 것은 전체 건수와 처음 5행뿐이다. 여러 데이터 소스의 조인(join)이나 특정 필드 추출도 같은 방식으로 처리한다.

반복문과 조건문 같은 제어 흐름도 코드로 처리하면 더 효율적이다. 예를 들어 Slack 채널에 배포 완료 알림이 올라올 때까지 기다리는 작업이 있다. 에이전트 루프에서 도구 호출과 대기 명령을 번갈아 실행하는 대신, 다음과 같은 `while` 루프 하나로 처리하면 된다.

```typescript
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({ channel: 'C123456' });
  found = messages.some(m => m.text.includes('deployment complete'));
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

조건 분기 트리를 코드로 작성해 실행 환경에 맡기면, 모델이 매 단계 조건문을 평가하느라 생기는 첫 토큰 지연(Time to First Token)도 줄어든다.

| 작업 유형 | 직접 도구 호출 방식 | 코드 실행 환경 처리 |
|---|---|---|
| 10,000행 시트 필터링 | 10,000행 전체를 컨텍스트에 포함해 모델이 직접 선별 | `filter`와 `slice(0, 5)`로 건수와 처음 5행만 반환 |
| Slack 배포 알림 폴링 | 에이전트 루프에서 도구 호출과 `sleep` 명령을 반복 왕복 | 단일 `while` 루프와 `setTimeout`으로 완료 시점까지 대기 |
| 조건 분기 평가 | 매 분기마다 모델 추론을 호출해 첫 토큰 지연 누적 | 코드 실행 환경이 조건 트리를 즉시 평가해 지연 제거 |

### 3. 개인정보 보호와 민감 데이터 자동 토큰화

코드 실행 환경에서는 에이전트가 명시적으로 `console.log`로 출력하거나 반환한 값만 모델에 노출된다. 보안이 더 중요한 워크로드에서는 에이전트 하네스(MCP 클라이언트)가 개인식별정보(PII)를 자동으로 토큰화해, 모델이 실제 값을 볼 수 없게 차단할 수 있다. 여기서 토큰화는 실제 값을 `[EMAIL_1]` 같은 대체 문자열로 바꾸는 일이고, 모델이 소비하는 컨텍스트 토큰과는 다른 개념이다.

에이전트가 Google Sheets의 고객 연락처를 읽어 Salesforce 리드를 갱신하는 코드를 실행한다고 하자.

```typescript
const sheet = await gdrive.getSheet({ sheetId: 'abc123' });
for (const row of sheet.rows) {
  await salesforce.updateRecord({
    objectType: 'Lead',
    recordId: row.salesforceId,
    data: { 
      Email: row.email,
      Phone: row.phone,
      Name: row.name
    }
  });
}
console.log(`Updated ${sheet.rows.length} leads`);
```

만약 에이전트가 중간에 `sheet.rows`를 로그로 출력하더라도, MCP 클라이언트가 데이터를 중간에서 받아 민감 정보를 치환한 상태로 모델에 전달한다.

```text
// 에이전트가 sheet.rows를 출력했을 때 보게 되는 치환 데이터
[
  { salesforceId: '00Q...', email: '[EMAIL_1]', phone: '[PHONE_1]', name: '[NAME_1]' },
  { salesforceId: '00Q...', email: '[EMAIL_2]', phone: '[PHONE_2]', name: '[NAME_2]' },
  ...
]
```

이후 이 대체 문자열이 다른 MCP 도구 호출(`salesforce.updateRecord`)의 인자로 전달되면, MCP 클라이언트가 내부 매핑 테이블을 조회해 실제 이메일, 전화번호, 이름으로 복원한 뒤 전송한다. 실제 개인정보는 Google Sheets에서 Salesforce로 직접 전달되며 모델 컨텍스트에는 단 한 번도 노출되지 않는다. 이 구조를 활용하면 어떤 데이터가 어느 시스템으로 전달될 수 있는지 결정론적(deterministic) 보안 규칙으로 정의할 수 있다.

| 데이터 처리 단계 | 실행 주체 | 데이터 형태 |
|---|---|---|
| 1. 원본 시트 조회 | `gdrive.getSheet` → MCP 클라이언트 | 실제 이메일, 전화번호, 이름 수신 및 내부 매핑 저장 |
| 2. 모델 컨텍스트 노출 시 | MCP 클라이언트 토큰화 필터 | `[EMAIL_1]`, `[PHONE_1]`, `[NAME_1]` 대체 문자열로 치환 |
| 3. 외부 도구 갱신 호출 시 | MCP 클라이언트 역토큰화 조회 | 매핑 테이블에서 실제 값으로 복원해 Salesforce로 전송 |

### 4. 파일시스템 기반 상태 유지와 스킬(Skills) 축적

파일시스템 접근 권한이 있는 코드 실행 환경에서는 에이전트가 중간 작업 결과를 파일로 저장해 상태를 유지할 수 있다. Salesforce에서 조회한 리드 1,000건을 `./workspace/leads.csv`로 기록해 두면 이후 실행에서 파일을 읽어 중단된 작업을 이어갈 수 있다.

나아가 에이전트가 특정 과제를 해결하며 작성한, 실제로 동작하는 코드를 재사용 가능한 함수 파일로 저장해 둘 수도 있다.

```typescript
// ./skills/save-sheet-as-csv.ts에 재사용 함수로 저장
import * as gdrive from './servers/google-drive';
export async function saveSheetAsCsv(sheetId: string) {
  const data = await gdrive.getSheet({ sheetId });
  const csv = data.map(row => row.join(',')).join('\n');
  await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
  return `./workspace/sheet-${sheetId}.csv`;
}
```

함수를 저장해 둔 폴더에 사용 지침을 적은 `SKILL.md` 파일을 추가하면, 이 폴더는 모델이 이후 과제에서 참조하고 호출할 수 있는 구조화된 스킬(Skills)이 된다[^2].

[^2]: 에이전트가 생성한 코드를 실행하려면 보안 실행 환경이 반드시 있어야 한다. 이 환경은 적절한 샌드박싱(sandboxing), 컴퓨팅 리소스 제한, 실행 모니터링을 갖춰야 한다. 직접 도구 호출에는 없던 인프라 구축과 운영 부담이 추가되므로, 토큰 비용 절감과 지연 단축 효과가 이러한 운영 복잡성을 상쇄하는지 작업 특성에 맞춰 판단해야 한다.

| 핵심 기능 | 구현 메커니즘 | 기대 효과 |
|---|---|---|
| 점진적 도구 탐색 | 파일 트리 탐색 및 `search_tools` 상세 수준 조절 | 시작할 때 도구 스키마를 불러오는 데 드는 토큰이 대폭 감소 |
| 로컬 필터링과 제어 흐름 | 실행 환경 내 배열 필터링, 집계, `while`/`if` 실행 | 대용량 응답의 컨텍스트 유입 방지 및 첫 토큰 지연 단축 |
| 개인정보 보호 처리 | MCP 클라이언트의 PII 자동 토큰화 및 호출 시 복원 | 모델에 민감 데이터를 노출하지 않는 결정론적 보안 구현 |
| 상태 유지와 스킬화 | 중간 결과 파일 저장 및 검증된 함수를 `SKILL.md`와 결합 | 작업 재개 지원 및 고수준 도구 상자(scaffolding) 진화 |

## 가장 흥미로운 지점

Anthropic이 제안한 설계의 핵심은 외부 도구를 JSON 스키마 목록으로 나열하는 대신 파일시스템과 코드 인터페이스로 제공한 데 있다. 에이전트 시스템의 난제로 꼽히던 컨텍스트 한도 관리, 다중 도구 조합, 민감 데이터 격리, 장기 상태 유지는 모두 같은 원인에서 생겼다. 모델이 모든 도구 호출과 데이터 전달의 중앙 중계자 역할을 맡았기 때문이다.

도구를 파일시스템의 모듈로 배치하고 실행 환경을 분리하면, 이 문제들은 익숙한 소프트웨어 엔지니어링 기법으로 풀린다. 필요한 모듈만 임포트하고, 스트림과 배열은 로컬에서 필터링한다. 민감 정보는 프록시 계층에서 마스킹하고, 반복되는 코드는 라이브러리 함수로 추출한다. LLM이 개별 도구 호출 문법보다 코드 작성과 파일시스템 탐색에 능숙하다는 원문 진단을 감안하면, 에이전트 아키텍처는 기존 소프트웨어 설계 원칙을 에이전트 하네스에 적용하는 방향으로 발전하고 있다.

## 출처

Anthropic Engineering / Research, Adam Jones & Conor Kelly, 2025년 11월 4일 발표.

- 원문: <https://www.anthropic.com/research/code-execution-with-mcp>
