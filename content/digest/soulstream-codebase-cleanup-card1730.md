---
title: "소울스트림 코드베이스 정리 리팩터링 (카드 #1730)"
date: 2026-11-23T02:00:00+09:00
tags: ["코딩 에이전트", "멀티에이전트", "코드 품질", "코드 리뷰"]
categories: ["에이전트와 코딩"]
subjects: ["소프트웨어 엔지니어링"]
summary: "소울스트림 코드베이스에서 중복 코드와 레거시, 느슨한 시험을 정리하기 위해 여덟 차례 검토를 거쳐 PR 92건을 머지했다. 지운 줄이 더한 줄보다 8,669줄 많았고, 고친 패턴의 재발을 막는 정적 검사 규칙 스무 개를 예외 목록 없이 CI에 켰다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/soulstream-codebase-cleanup-card1730/01-cover.png"
  alt: "뒤엉킨 두루마리 더미에서 돋보기로 중복을 골라내고 하늘색 리본으로 묶은 깔끔한 두루마리만 책상에 남긴 서소영"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/soulstream-codebase-cleanup-card1730/01-cover.png"
---

## 3줄 요약

1. 동작은 그대로 두고 소울스트림 코드를 정리했다. 나흘 동안 PR 92건을 머지했고, 지운 코드가 더한 코드보다 8,669줄 많다.
2. 중요도 8점 이상인 지적이 남지 않을 때까지 검토를 여덟 번 돌렸다. 8회차에서 나온 8건까지 고친 뒤 디렉터 결정으로 9회차 없이 마감했다.
3. 고친 패턴이 다시 생기면 잡아내는 재발 방지 검사 규칙 스무 개를 CI에 켰다. 예외 목록은 두지 않았고, `main`의 위반이 0건인 상태에서 적용했다.

## 자료 정보

- **자료**: 소울스트림 카드 #1730 마감 보고와 PR 92건의 본문[^report-html]
- **기간**: 2026년 11월 19일부터 22일까지
- **맡은 이**: 카드 담당은 서소영이다. 검토는 1회차부터 4회차까지 서소영 Astra가, 5회차부터 8회차까지 서소영 Fable이 맡았다. 고칠 항목은 서소영 Fable이 선별했고, 구현은 로젤린이, 머지와 배포는 버블이 했다.
- **분량**: 더한 코드는 13,029줄, 지운 코드는 21,698줄이다. 바뀐 파일은 PR마다 센 수를 더하면 2,692개다. 같은 파일이 여러 PR에 들어 있으면 그 횟수만큼 센 값이다.

[^report-html]: [소울스트림 코드베이스 정리 리팩터링 마감 보고 HTML](https://pages.eiaserinnys.me/d/soulstream-card1730-cleanup)

## 무엇을 하려 했나

동작은 그대로 두고 코드에서 불필요한 부분을 줄이는 것이 목표다. 요청에 적힌 검토 대상은 다섯이다.

- 중복 코드
- 레거시
- `xstate` 상태 기계를 쓸 이유가 있는지
- 상태를 더 간결하게 만들 부분
- 느슨한 시험

진행하며 디렉터가 지시 네 가지를 덧붙였다.

- 중요도 8점 이상인 지적이 남지 않을 때까지 반복한다.
- 고친 것이 다시 생기지 않게 정적 검사로 막는다.
- 안 쓰는 코드와 시험은 지운다.
- 결과는 글로 정리하고, 그 글은 작가 서소영이 손본다.

작업 지침은 이랬다. 바꾸기 전에 그 코드가 왜 있는지 기록으로 확인한다. 더하기보다 지우기를 먼저 생각한다. 증상 대신 원인을 고친다. 더하지 않는 것은 여섯 가지다. 추측성 방어 코드, 호환용 중간 상태, 새 설명 주석, 커버리지를 채우려는 시험, 구현을 고정하는 시험, 새 CI 워크플로다.

## 여덟 번의 검토

| 회차 | 검토 | 중요도 8점 이상 확정 | 머지한 PR |
| :-- | :-- | :-- | :-- |
| 1부터 4 | Astra 검토, Fable 선별 | 1회차 기록 없음, 2회차 7건, 3회차 6건, 4회차 4건 | 17건 (#2120부터 #2144까지) |
| 5 | Fable 검토와 선별 | 10건 (9점 1건) | 10건 (#2162부터 #2177까지) |
| 6 | Fable | 8건 (9점 1건) | 8건 (#2179부터 #2186까지) |
| 7 | Fable | 5건 (9점 2건) | 9건 (#2191부터 #2195까지, 추가 삭제 #2198, #2199, #2202, #2203) |
| 8 | Fable | 8건 (9점 이상 없음) | 26건 (#2204부터 #2232까지) |
| 재발 방지 검사 | 카드 담당 설계 | 검사에 걸리던 곳 전부 | 22건 (#2233부터 #2264까지) |

1회차부터 4회차까지의 검토 문서는 남지 않아 1회차 건수는 다시 확인하지 못했다. 5회차부터는 Astra(Codex)가 주간 사용 한도에 걸려, 디렉터 답(「fable 리뷰」)에 따라 Fable이 검토와 선별을 함께 맡았다.

반복 규칙은 「확정 건수가 회차마다 줄면 계속하고, 줄지 않으면 멈추고 여쭙는다」였다. 5회차(10건)와 8회차(8건)에는 건수가 늘었다. 카드 담당은 두 번 모두 같은 원인으로 판단했다. 저장소 전체를 중복 탐지 스크립트로 훑으면서 검토가 보는 범위가 넓어졌다는 것이다. 카드 담당은 그 판단을 적어 디렉터께 여쭸다.

- 5회차 답: 「10건 고치고 계속」
- 8회차 답: 「다 고치고 켬」. 8회차의 8건과 재발 방지 검사에 걸리는 `main`의 코드를 모두 고친다. 그다음 검사를 켜고 9회차 없이 마감한다는 뜻이다.
- 카드 담당이 질문에서 권장한 안은 같은 선언이 두 곳에 있는 쌍 118건만 예외 목록에 두는 것이었다. 디렉터가 「118건도 수정」이라고 답해 예외 목록 없이 모두 고쳤다.

8회차 결정 때 `main`에서 재발 방지 검사에 걸리던 곳은 다음과 같았다. 8회차 8건도 이 목록에 포함되어 있었다.

- 생성된 타입을 손으로 다시 적은 곳 24건
- 보내는 코드가 없는 이벤트 4건
- 정본 함수를 다시 선언한 곳 41건
- 아무도 쓰지 않는 파일 19개
- 같은 선언이 두 곳에 있는 쌍 118건

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 198" role="img" aria-label="여덟 번의 검토와 재발 방지 검사 적용 흐름" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="198" fill="var(--bg-2)"/>
  <rect x="20" y="24" width="154" height="62" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="48" font-family="var(--sans)" font-size="11" font-weight="700" fill="var(--ink-2)">1부터 4회차</text>
  <text x="30" y="68" font-family="var(--sans)" font-size="12.5" font-weight="700" fill="var(--ink)">Astra 검토, PR 17건</text>
  <rect x="196" y="24" width="154" height="62" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="206" y="48" font-family="var(--sans)" font-size="11" font-weight="700" fill="var(--ink-2)">5부터 8회차</text>
  <text x="206" y="68" font-family="var(--sans)" font-size="12.5" font-weight="700" fill="var(--ink)">Fable 검토, PR 53건</text>
  <rect x="372" y="24" width="156" height="62" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="382" y="48" font-family="var(--sans)" font-size="11" font-weight="700" fill="var(--accent-ink)">전부 수정</text>
  <text x="382" y="68" font-family="var(--sans)" font-size="12.5" font-weight="700" fill="var(--accent-ink)">위반 0건, PR 22건</text>
  <rect x="550" y="24" width="150" height="62" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="562" y="48" font-family="var(--sans)" font-size="11" font-weight="700" fill="var(--ink-2)">CI 고정</text>
  <text x="562" y="68" font-family="var(--sans)" font-size="12.5" font-weight="700" fill="var(--ink)">규칙 20개 켜기</text>
  <line x1="174" y1="55" x2="192" y2="55" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink)"/>
  <line x1="350" y1="55" x2="368" y2="55" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <line x1="528" y1="55" x2="546" y2="55" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="20" y="114" width="680" height="60" fill="var(--bg)" stroke="var(--rule)" stroke-width="1"/>
  <text x="34" y="138" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">검증과 배포 흐름</text>
  <text x="34" y="159" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">작업 명세 작성과 해시 고정 → 로젤린 자동 검증 → 담당 검토 후 버블에게 머지 인계 → 세 노드 배포</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 316" role="img" aria-label="여덟 번의 검토와 재발 방지 검사 적용 흐름 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="marr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="marr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="316" fill="var(--bg-2)"/>
  <rect x="16" y="16" width="318" height="48" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="45" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 1회차부터 4회차: Astra 검토, PR 17건</text>
  <line x1="175" y1="64" x2="175" y2="80" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#marr-ink)"/>
  <rect x="16" y="84" width="318" height="48" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="113" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">2. 5회차부터 8회차: Fable 검토, PR 53건</text>
  <line x1="175" y1="132" x2="175" y2="148" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#marr-acc)"/>
  <rect x="16" y="152" width="318" height="48" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="28" y="181" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">3. 전부 수정: 예외 없이 0건 달성, PR 22건</text>
  <line x1="175" y1="200" x2="175" y2="216" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#marr-acc)"/>
  <rect x="16" y="220" width="318" height="80" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="252" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">4. CI 고정과 배포</text>
  <text x="28" y="276" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">정적 검사 규칙 20개 적용과 세 노드 운영 확인</text>
</svg>
<figcaption style="margin-top: 0.65rem; font-size: 0.85rem; color: var(--ink-2); text-align: center; line-height: 1.5;">검토 여덟 차례와 재발 방지 검사 전부 수정, CI 고정까지의 진행 흐름.</figcaption>
</figure>

## 무엇을 바꿨나

### 안 쓰는 코드와 레거시 삭제

- **#2120**: 체크리스트 컨트롤, 워커 폴더 행을 변환하던 도우미, 응답 대기 푸시를 가려내던 판별기, 즉시 승계 훅까지 호출 경로에서 빠진 옛 구현 네 개를 지워 670줄을 덜어 냈다.
- **#2179**: 호출하는 곳 없는 폴더 세션 문맥 훅을 없앴다.
- **#2199**: 아무도 보내지 않는 `subtree_update` 이벤트와 그 수신 코드, 시험을 제거했다.
- **#2198, #2202**: 4월 21일 이전의 옛 형식 메시지에 발신 에이전트를 표시하던 코드를 지웠다. 디렉터가 승인한 동작 변경이다(자세한 내용은 아래 「동작이 바뀐 두 가지」에 있다).
- **#2203, #2227**: 읽는 곳 없는 `parentEventId` 필드를 없앴다.
- **#2224**: 보내는 코드가 없는 SSE 이벤트 네 가지를 제거했다.
- **#2211**: `session_id`의 구버전 필드를 지웠다.
- **#2216**: 쓰지 않는 `fallback_model` 필드를 응답에서 뺐다.
- **#2212**: `soul-ui`가 호환용으로 다시 내보내던 이름들을 삭제했다.
- **재발 방지 검사 단계**: 아무도 쓰지 않는 파일 19개를 그 시험과 함께 지웠다.

### 상태 기계 간결화 (`xstate`)

- **#2122**: 전이가 없는 노드 요청 상태 기계를 표에서 값을 찾는 방식으로 바꾸었다. 중앙 재확인 상태 기계에서는 운영 경로가 만들지 않는 `applied` 입력을 지웠다.
- **#2135**: 러너 복구 상태 기계를 판정 함수로 바꾸었다.
- **#2164**: 러너 중앙 확인 상태 기계와 복구 판정 상태 기계를 지우고 판정 결과를 직접 돌려주도록 고쳤다.
- 이제 전이가 없는 상태 기계는 재발 방지 검사의 `single-state-machine` 규칙이 잡는다.

### 중복 정리

![흩어져 있던 중복 복사본을 하나의 원본 두루마리로 합치고 낡은 종이 조각을 쓸어 담는 서소영](https://img.seosoyoung.eiaserinnys.me/images/soulstream-codebase-cleanup-card1730/02-dedup-cleanup.png)

- **SQL**: #2124(세션 검색 연결 조인 세 벌)와 #2141(턴 요약 집계 두 벌)을 정리했다. #2162(세션 연결 카드 `LATERAL` 조인 두 벌)와 #2185(세션 배달 `INSERT`와 `UPDATE`)의 중복도 정리했다.
- **웹과 앱의 정책과 문구**: #2123(사용량 요약 갱신 정책), #2129(동작 실패 문구), #2140(반복 스케줄과 한도 알림)을 통합했다. #2143(첨부 미리보기 MIME 목록), #2144(PAS 보고 링크 인식), #2168(카드 상태 라벨 일곱 벌)도 합쳤다.
- **서버의 판정과 응답**: #2130(세션 종료와 보드 갱신 판정), #2165(폴더 가시성 집합 네 벌), #2166(서비스 bearer 인증 실패 매핑)을 정리했다. #2181(세션 명령 오류 응답 네 벌), #2184와 #2192(라우트 본문 검증과 `INVALID_REQUEST` 도우미), #2217(발신자 신원 판정)도 정리했다.
- **공용 정본과 패키지 통합**: 중앙과 워커, 화면이 함께 쓰는 타입과 직렬화를 공용 정본 한 곳으로 모았다. #2193(턴 요약 직렬화), #2213(호스트 계약 행), #2223(중앙과 워커 공용 타입), #2231(선호 설정을 감싸는 타입)이 대상이었다. 공용 패키지로 통합한 #2131과 #2230에서는 원자적 파일 교체와 Codex 실행 파일 경로 찾기(새 공용 패키지)를 정리했다.
- **값 판정 함수 사본**: 값이 객체인지 따지는 함수 사본들은 #2208과 #2237, #2243(17벌), #2246(108벌), 그리고 #2248, #2253, #2254를 거치며 모두 `wire-schema`의 `isRecord`와 `asRecord` 한 곳으로 합쳤다.
- **함수 사본 정리**: #2207, #2209, #2210, #2225에서는 대시보드 아홉 쌍, `orch` 열한 쌍, 워커 열세 쌍, 앱 여섯 개의 함수 사본을 정리했다.
- **다시 내보내기와 별칭**: #2182, #2236, #2242에서 선언을 옮길 때 기존 모듈에서 다시 내보내지 않고, 가져오는 곳을 모두 새 모듈로 고쳤다.
- **순환 `import`**: #2244(화면), #2245(마크다운 뷰어), #2247(서버)의 순환 참조를 끊었다.

손으로 다시 적은 타입을 `wire-schema` 생성 타입으로 교체한 목록은 다음 표와 같다.

| 회차 | PR | 대상 |
| :-- | :-- | :-- |
| 2회차 | #2132 | 세션 효과와 예약 타입 |
| 4회차 | #2142 | `event-ack` |
| 5회차 | #2171, #2177 | 카탈로그 델타, 세션 배달 |
| 6회차 | #2183, #2186 | 폴더 항목 목록, SSE 이벤트 타입 53쌍 |
| 7회차 | #2191, #2194, #2195 | 세션 배정, 남은 SSE 타입 사본, `intervene` 배달 필드 열두 개 |
| 8회차 | #2214, #2219, #2221, #2229, #2232 | 워커, 앱, `soul-ui`의 Claude 타입, Claude 계정, `ContextItem` |

### 느슨한 시험

- **#2264**: 늘 참이던 단언 아홉 곳(상수끼리 비교하는 `expect`, 아무 데도 넘기지 않은 모의 함수와 그 단언)을 지우거나 타입 검사로 옮겼다.
- **#2263**: 패널 통합 시험 708줄짜리 `MarkdownDocumentPanel.test.tsx`가 넉 달 내내 타입 검사를 비켜 가고 있었다. `soul-ui`의 같은 폴더에 같은 이름의 `MarkdownDocumentPanel.test.ts`가 함께 있었기 때문이다. 파일 이름을 바꾸고 나서야 검사가 다시 붙었다.
- **#2238**: 워커 시험 파일도 타입 검사를 받게 했다.
- **#2218**: warmup 시험의 시계를 고정했다.
- **#2122**: 삭제한 상태 기계를 자기 자신과 비교하던 시험과, 도달할 수 없는 단언을 지웠다.

## 재발 방지 검사

재발 방지 검사는 CI의 기존 작업에 단계를 더하는 방식으로만 켰다. 새 워크플로는 없다. 검사를 켠 곳은 `workspace-validation.yml`과 `soul-app.yml`의 「Check source guards」 단계와 「Check TypeScript guards」 단계, 그리고 `ci-paths.yml`이다. 위반이 하나라도 있으면 실패하고, 실패 메시지에 고치는 법이 함께 나온다.

`scripts/check-source-guards.mjs`

- **`wire-copies`**: `wire-schema` 생성 타입과 같은 이름을 손으로 다시 선언한 경우
- **`sse-alias-only`**: SSE 이벤트 타입을 생성 타입의 별칭으로 두지 않고 직접 선언한 경우
- **`sse-sender`**: 보내는 코드가 없는 SSE 이벤트
- **`fingerprints`**: 정본 파일에만 있어야 할 고유 값(라벨 키, MIME 목록, 링크 정규식 등)이 다른 파일에 나타난 경우
- **`canonical-redecl`**: 정본 모듈이 내보낸 이름을 다른 파일에서 다시 선언한 경우
- **`renamed-reexport`**: 이름만 바꿔 다시 내보낸 경우
- **`cross-package-reexport`**: 다른 패키지의 것을 다시 내보낸 경우
- **`same-name-alias`**: 별칭으로 가져와 원래 이름으로 되돌려 내보낸 경우
- **`runtime-cycle`**: 런타임 `import` 순환
- **`cross-identical`**: 두 패키지에 이름과 본문이 같은 선언이 있는 경우
- **`intra-identical`**: 한 패키지 내에 본문이 같은 150자 이상 함수가 있는 경우
- **`dead-module`**: 아무도 가져오지 않거나 시험만 가져오는 모듈
- **`single-state-machine`**: 전이가 없는 상태 기계
- **`record-copy`**: `isRecord`와 `asRecord`의 지역 사본
- **`reflect-key`**: 문자열 리터럴 키로 부르는 `Reflect.get`, `set`, `has`

`scripts/check-ts-guards.mjs`

- **`shadowed-source`**: 같은 폴더에 같은 이름의 `.ts`가 있어 타입 검사에서 빠지는 `.tsx`
- **`duplicate-import`**: 같은 모듈을 `import` 문 여러 개로 가져온 경우
- **`omit-index`**: 인덱스 시그니처 타입에 `Omit`을 쓴 경우
- **`unwired-mock`**: 아무 데도 넘기지 않는 `vi.fn`, `jest.fn` 모의 함수
- **`constant-expect`**: 상수끼리 비교하는 `expect`

`.github/scripts/check-ci-paths.mjs`는 워크플로 경로, 시험 경로, `.easignore` 항목이 실제 파일을 가리키는지 본다. 생성 스크립트가 설치된 실행 파일을 쓰지 않고 `npx`로 대신 실행하는 폴백도 잡는다.

`tsconfig`: 지금 패키지 열 곳에 `noUnusedLocals`가 켜져 있다. `chrome-extension`, `orch-server-ts`, `chat-ui`, `mcp-contract`, `page-model`, `soul-ui`, `soul-app`, `soul-desktop`, `soul-server-ts`, `unified-dashboard`다. 서버 쪽은 #2259에서 켰다. 화면과 앱 쪽은 #2262에서 걸리던 안 쓰는 지역 변수와 `import`를 지웠다.

## 동작이 바뀐 두 가지 (디렉터 승인)

- **#2198, #2202**: 4월 1일부터 20일까지 저장된 옛 형식 메시지는 40건이다. 이 메시지는 세션 36개에 들어 있고, 세션은 모두 일곱 달 전에 끝났다. 이제 이 메시지는 발신 에이전트의 아바타와 이름 없이 일반 사용자 메시지처럼 보인다. 본문은 그대로다. 디렉터는 「지움」이라고 답했다.
- **#2230**: 중앙과 노드가 따로 갖던 Codex 실행 파일 경로 찾기를 노드 쪽 동작 한 벌로 모았다. 설정에 적힌 경로가 실제로 실행되는지 확인하는 일도 이제 중앙이 함께 한다. 윈도우에서 실행 파일 확장자를 고를 때는 시스템의 `PATHEXT` 설정을 따른다. 디렉터는 「새 패키지로 모음」이라고 답했다.

그 밖의 변경은 외부 동작을 바꾸지 않는다.

## 어떻게 확인했나

작업 단위마다 목표와 고칠 범위, 멈출 조건, 검사 명령을 적어 작업 명세를 만들고 그 해시를 고정하는 일은 카드 담당이 맡았다. 로젤린은 같은 명세로 리뷰 전 자동 검증을 돌렸다. 카드 담당은 자동 검증을 통과한 결과 묶음만 읽은 뒤, 머지를 버블에게 맡겼다.

- **자동 검증이 보는 것**: 타입 검사, 관련 시험, 범위 밖 파일 변경, 바뀐 블록의 주석, 시험이 약해진 흔적
- **범위에 따라 더한 검사**: `soul-server-ts`에는 `check:quick`을, `orch-server-ts`에는 `check:session-machine`을, UI에는 CSS 기준치 검사를, 앱에는 EAS 허용 목록과 앱 `tsc` 검사를 더했다.

![문지기처럼 체크리스트와 하늘색 자를 들고 들어오는 두루마리를 검사하는 서소영](https://img.seosoyoung.eiaserinnys.me/images/soulstream-codebase-cleanup-card1730/03-verify-gate.png)

동작이 그대로인지는 변경 전후의 출력을 비교해 확인했다. 사례는 넷이다.

- **#2122**: 노드 요청 44건, 실행 투영 7,680건, 중앙 재확인 60건을 실행해 보니 바꾸기 전후의 판정 결과가 같았다.
- **#2124**: 고정 입력 SQL 여섯 건을 정규화해 비교하니 같았다. PostgreSQL CI 시험 24건이 통과했다.
- **#2125**: 실제 MCP `tools/list`에서 꺼낸 이름과 설명, 상태 `enum`은 고치기 전과 차이가 없었다.
- **#2129**: 192가지 입력의 문구 출력이 앱 사본, 옛 공용 모듈, 새 공용 모듈에서 모두 일치했다.

재발 방지 검사를 켠 작업 단위는 자동 검증 기록에 두 가지를 남겼다. 고치기 전에 검사가 낸 출력과, 고친 뒤 0줄로 줄어든 결과다. 예를 들어 #2264는 고치기 전 출력이 워크스페이스에서 일곱 줄, 앱에서 두 줄이었고, 고친 뒤에는 둘 다 0줄이 되었다.

머지는 CI를 통과한 뒤 squash 방식으로 했다. 배포는 카드 담당이 승인했다. 버블은 배포가 끝난 뒤 자동 검증으로 노드별 서비스 커밋과 연결 상태를 확인했다. 마지막 배포 뒤 세 노드(`eiaserinnys`, `eias-linegames`, `eias-linegames-wsl`)는 모두 마지막 머지 커밋으로 서비스하고 있었다. 시각은 UTC 기준 11월 22일 `eias-linegames` 14시 18분 44초, `eiaserinnys` 14시 19분 7초, `eias-linegames-wsl` 14시 20분 5초다.

## 판단 근거

- 지우기 전에 왜 있었는지 `git` 기록과 PR 본문으로 확인했다. 가령 #1065, #656, #1595, #1112가 마지막 호출을 없애면서 남긴 코드가 #2120에서 지운 네 개였다.
- 회차를 이어 갈지는 앞 절(「여덟 번의 검토」)의 반복 규칙과 디렉터 답으로 정했다.
- 재발 방지 검사의 규칙은 실제로 고친 패턴에서 일반화했다. 검사에 걸리면 바로 고칠 수 있게 메시지에 고치는 법을 적었다.
- 재발 방지 검사를 예외 목록 없이 켠 것은 디렉터 결정(「다 고치고 켬」, 「118건도 수정」)에 따른다.
- 디렉터는 구현 모델로 `deepseek`를 우선하라고 지시했다. `deepseek-flash-4.1`은 11월 23일까지 한도를 다 쓴 상태였다. 그동안의 작업 단위는 `codex-6.1-terra`(max)로 띄웠다.

## 남은 일

### 보지 못한 것

- 집 PC(`silent-manari-ts`)는 11월 19일 22시 33분(UTC)부터 연결이 끊겨 반영을 확인하지 못했다.
- 지운 이름이 다시 생기는 것은 막지 않는다. 막으려면 지운 이름을 영구 목록으로 관리해야 해서 규칙에 넣지 않았다.

### 하지 않은 것

- **검사 규칙에 못 담은 패턴**: 함수가 아닌 문맥의 `isRecord(E) ? E : D` 삼항(약 80곳)과 화면 쪽 인라인 판정, `isPlainObject` 둘, 예외를 던지는 `asRecord`, 뜻이 둘로 달라지는 문자열 해석 함수 다섯, 기존 `void x;` 일곱 곳, `import` 합치며 120자를 넘긴 줄 44개, `reflect-key`의 주석 및 문자열 포함, `import` 별칭 규칙 미도입
- **시험**: `plannerSplitLayout.test.tsx:413` 상수 전제 단언, `n5Coverage`의 `LEGACY` 개수 단언, 지울 만한 기계적 시험(#2122 순회 시험 둘, #2123 `account-pool` 시험, #2125에서 복원한 `skip` 셋)
- **타입 검사 미적용**: `plugins/chatgpt-card-renderer`(워크스페이스 바깥, 기존 `tsc` 오류), `wire-schema`의 `tests/*.typecheck.ts`, `soul-app`의 `@types/node` 간접 의존
- **동작 변경 우려로 제외**: 제어 명령 스키마를 엄격하게 좁히는 검사(#2195의 `additionalProperties`), #2181에서 응답이 달라 합치지 않은 `persistent_session_settings_routes.ts:132`
- **작은 잔여 항목**: 주석 및 상대 경로, `NodePanelCentralCard` 타입 변환, `orch`와 화면의 `ModelPresetAvailability` 및 `WeeklyHeadroom` 사본, `orch` 필터 결함 등 세부 항목, `json_record.ts` 정본 목록 등록, 빌드 환경 변수와 postgres 시험의 CI 위임, `test.each<...>` 미집계, 작업 트리 둘 미정리

### 따로 넘긴 것 (서소영 영구 세션)

- 불안정한 시험 일곱과 `runner_process_reconnect.e2e`의 `EPIPE` 경합, `UsageStatsSettingsSection` 시험의 불안정
- 실행 중인 세션이 429를 받아도 대체 모델(`model_preset_fallbacks`)로 넘어가지 않는 문제
- CI만 바꾼 머지에도 세 노드에 배포 대기가 생기는 문제, `kaleidoscope` 배포 대기
- 격리 실행 환경(샌드박스) 안 `soul-server`의 postgres 권한, 로컬 postgres 시험 정책이 `docker` 유무로만 정해지는 문제
- 기존 `void x;` 일곱 곳, `wire-schema`의 `typecheck` 파일, `chatgpt-card-renderer`의 CI 타입 검사

## 가장 흥미로운 지점

가장 눈에 띈 것은 파일 이름 하나가 겹친 일이다. 이름이 같은 `.ts` 파일 하나 때문에 패널 통합 시험 708줄이 넉 달 내내 타입 검사에서 빠져 있었다. 재발 방지 검사 규칙(`shadowed-source`)을 만들면서 비로소 찾아냈다.

또한 5회차와 8회차에는 확정 건수가 도리어 늘었다. 한편 최종 92건을 머지한 결과, 지운 코드가 더한 코드보다 8,669줄 많았다. 카드 담당은 코드 품질이 나빠졌다고 보지 않았다. 저장소 전체를 훑으며 검토가 보는 범위가 넓어진 탓이라고 판단했다. 예외 목록을 두자는 권고안 대신 디렉터가 118건까지 모두 고치게 했고, 그 덕에 위반이 0건인 상태에서 검사를 켤 수 있었다.

## 출처

- 소울스트림 카드 #1730 (소울스트림 카드 보드)
- 마감 보고 HTML: <https://pages.eiaserinnys.me/d/soulstream-card1730-cleanup>
- 대표 PR: [#2120](https://github.com/eiaserinnys/soulstream/pull/2120), [#2122](https://github.com/eiaserinnys/soulstream/pull/2122), [#2246](https://github.com/eiaserinnys/soulstream/pull/2246), [#2257](https://github.com/eiaserinnys/soulstream/pull/2257), [#2263](https://github.com/eiaserinnys/soulstream/pull/2263), [#2264](https://github.com/eiaserinnys/soulstream/pull/2264)
- 치비 서소영 삽화 3장은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 gpt-image-2.6-flare로 따로 생성했다.
