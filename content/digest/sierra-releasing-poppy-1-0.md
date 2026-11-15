---
title: "Releasing Personal Agent Protocol 1.0"
date: 2026-11-15T08:00:00+09:00
tags: ["AI 에이전트", "MCP", "Meta", "Sierra"]
categories: ["에이전트와 코딩"]
subjects: ["하네스와 에이전트 설계"]
summary: "Sierra가 개인용 AI 에이전트와 기업의 웹사이트, API, 비즈니스 에이전트를 직접 연결하는 공개 표준 Personal Agent Protocol(Poppy) 1.0을 발표했다. Meta의 AI 에이전트 Muse와 전 세계 Shopify 가맹점에 기본 적용되었으며, 금융과 항공 등 100개 이상의 파트너 기업이 참여한다."
source: "https://sierra.ai/kr/blog/releasing-poppy"
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/sierra-releasing-poppy-1-0/01-cover.png"
  alt: "상점 아치 앞에서 하늘색 인증 카드를 들어 보이는 치비 서소영과 그 앞에서 악수하는 개인 에이전트 로봇 및 상점 에이전트 로봇"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/sierra-releasing-poppy-1-0/01-cover.png"
---

## 3줄 요약

1. 엔터프라이즈 AI 에이전트 기업 Sierra의 공동창업자 브렛 테일러(Bret Taylor)와 클레이 베이버(Clay Bavor)가 2026년 11월 13일 Personal Agent Protocol(약칭 Poppy) 1.0을 정식 공개했다. 사용자의 개인 에이전트가 기업 시스템과 직접 소통할 수 있도록 연결 규격을 표준화했다.
2. Poppy 1.0은 도메인 루트의 `/.well-known/poppy.json` 탐색 문서와 OAuth 인증, MCP와 OpenAPI, 상거래 표준인 UCP(Universal Commerce Protocol)를 결합했다. 이를 통해 개인 에이전트가 고객의 권한 범위 내에서 기업의 웹사이트, API, 비즈니스 에이전트와 상호작용하도록 규정한다.
3. 출시와 함께 Meta의 개인용 AI 에이전트 뮤즈(Muse)가 방문 사이트에서 Poppy를 가장 먼저 확인하도록 기본 적용되었고, 전 세계 Shopify 가맹점에도 자동 배포되었다. 머큐리(Mercury), 싱크로니(Synchrony), 터키항공 등을 포함한 디자인 파트너도 100개 기업 이상으로 늘었다.

## 100개 이상 기업이 합류한 Poppy 1.0 공개

개인용 AI 에이전트가 사용자를 대신해 진료 예약을 잡거나 항공권을 예매하고 보험 상품을 비교하는 일이 늘어나고 있다. 그동안 대다수 개인 에이전트는 사람과 똑같이 웹페이지를 불러와 입력 양식을 클릭하거나 고객센터 웹 채팅창에 접속하는 방식으로 작업을 처리했다.[^1] 이런 우회 방식은 처리 시간이 길고 웹사이트 구조가 조금만 바뀌어도 작업에 실패하기 쉬웠다. 기업 역시 접속한 에이전트가 고객이 실제로 위임한 프로그램인지, 어떤 범위의 권한을 받았는지 식별하고 통제할 표준 수단이 부족했다.

[^1]: 브렛 테일러와 클레이 베이버가 2026년 10월 6일 발표한 첫 소개 글(「Introducing Personal Agent Protocol」)에서 진단한 배경이다. 당시 Sierra와 Meta는 Genesys, Instinct, NiCE, Rocket, Shopify, Stripe, Walmart 등 초기 파트너와 함께 프로토콜 구상을 처음 공개했다.

첫 초안이 나온 지 약 5주 만인 2026년 11월 13일, 브렛 테일러와 클레이 베이버는 Personal Agent Protocol(약칭 Poppy)을 1.0 정식 명세로 확정해 배포했다. 사용자의 개인 에이전트가 기업의 비즈니스 에이전트, 웹사이트, API와 안전하고 일관되게 소통할 수 있도록 통신 규약을 정의했다.

![Personal Agent Protocol(Poppy) 1.0에 참여하는 100개 이상의 디자인 파트너 기업 로고](https://img.seosoyoung.eiaserinnys.me/images/sierra-releasing-poppy-1-0/02-design-partners.png)
*Personal Agent Protocol(Poppy) 설계 및 도입에 참여하는 100개 이상의 디자인 파트너 기업들 (출처: Sierra)*

이번 1.0 발표에는 정식 명세 배포와 함께 Meta, Shopify 및 초기 파트너사들의 실제 서비스 적용 소식이 담겼다.

| 발표 항목 | 주요 내용 | 적용 대상 및 규모 |
|---|---|---|
| 프로토콜 1.0 명세 공개 | 5주간의 실제 환경 테스트를 반영한 정식 명세(`v1.0`)와 기업용 구현 키트 및 검증 도구 배포 | 모든 기업이 자체 구현 가능 |
| Meta AI 에이전트 기본 탑재 | Meta의 AI 에이전트 뮤즈(Muse)에 기본 활성화되어 방문하는 모든 사이트에서 Poppy 지원 여부를 최우선 확인 | Muse 전체 사용자 |
| Shopify 전 가맹점 자동 활성화 | 플랫폼 내 모든 상점이 별도 개발 없이 Poppy 파일을 자동 게시하도록 기본 적용 | 전 세계 175개국 이상의 Shopify 가맹점 |
| 초기 파트너 본운영 개시 | 머큐리(Mercury), 싱크로니(Synchrony), 터키항공 등 다수 파트너사가 실제 서비스에 적용 | 금융, 유통 결제, 항공 예약 실서비스 |
| 디자인 파트너 생태계 확장 | 신규 기업 60곳이 합류해 초기 파트너를 포함한 전체 참여 기업이 100곳 이상으로 증가 | 금융, 커머스, 보안, 클라우드, 여행 등 전 산업군 |

이번에 새로 합류한 디자인 파트너 60곳은 산업군이 고르다. 세일즈포스(산하 Fin, Commerce Cloud, Agentforce 포함)와 시스코, 트윌리오, 브레이즈, 워크OS, 줌 같은 엔터프라이즈 기술 기업이 참여했다. 여기에 어펌, 소파이, 체크아웃닷컴, 인튜이트, 레모네이드 같은 금융과 보험사, 델타항공, 하얏트, 아고다, 웨이페어 같은 여행과 유통 기업도 이름을 올렸다.[^2]

[^2]: 이외에도 Aflac과 Guardian 같은 보험 및 금융 기업, Zendesk와 Freshworks 같은 SaaS 기업을 포함해 40여 곳이 새로 합류했으며, 10월 초안부터 참여한 OpenAI, Visa, Mastercard, PayPal, Stripe, Cloudflare, 1Password, Notion, Okta, Plaid 등도 파트너로 함께하고 있다(전체 명단은 원문 참고).

## Poppy 1.0의 작동 구조와 초안 이후 네 가지 개선 사항

디자인 파트너들은 지난 5주 동안 실제 웹사이트와 API, 에이전트 환경에서 초안을 시험했고, 그 요구사항이 Poppy 1.0 명세에 반영되었다. 개인 에이전트는 이 규격을 통해 기업이 제공하는 기능과 접속 경로를 파악하고 고객이 승인한 권한에 맞춰 안전하게 작업을 처리한다.

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 250" role="img" aria-label="Poppy 1.0 프로토콜의 탐색, 인증, 3대 상호작용 채널 구조" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="250" fill="var(--bg-2)"/>
  <rect x="16" y="24" width="206" height="202" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="50" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 개인 에이전트 (Muse 등)</text>
  <text x="28" y="74" font-family="var(--sans)" font-size="11.5" fill="var(--ink-2)">사용자 위임 작업 요청</text>
  <rect x="28" y="92" width="182" height="52" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="38" y="113" font-family="var(--mono)" font-size="11" fill="var(--ink)">/.well-known/poppy.json</text>
  <text x="38" y="132" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">최우선 탐색 및 신원 제시</text>
  <rect x="28" y="156" width="182" height="52" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="38" y="177" font-family="var(--sans)" font-size="11.5" font-weight="700" fill="var(--ink)">고객 권한 통제</text>
  <text x="38" y="196" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">중요 동작 전 사용자 승인</text>
  <line x1="222" y1="125" x2="246" y2="125" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="250" y="24" width="206" height="202" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="262" y="50" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">2. Poppy 1.0 연결 규격</text>
  <text x="262" y="74" font-family="var(--sans)" font-size="11.5" fill="var(--accent-ink)">세션 연속성 및 OAuth 권한 관리</text>
  <rect x="262" y="90" width="182" height="36" fill="var(--bg)" stroke="var(--accent)" stroke-width="1"/>
  <text x="272" y="113" font-family="var(--mono)" font-size="11" fill="var(--ink)">Session JWT + OAuth 2.0</text>
  <rect x="262" y="136" width="182" height="36" fill="var(--bg)" stroke="var(--accent)" stroke-width="1"/>
  <text x="272" y="159" font-family="var(--mono)" font-size="11" fill="var(--ink)">MCP / OpenAPI / UCP 결합</text>
  <rect x="262" y="182" width="182" height="32" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="272" y="202" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">산업별 확장 (Commerce 등)</text>
  <line x1="456" y1="125" x2="480" y2="125" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="484" y="24" width="220" height="202" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="496" y="50" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">3. 기업의 3대 상호작용 채널</text>
  <rect x="496" y="68" width="196" height="42" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="506" y="87" font-family="var(--sans)" font-size="11.5" font-weight="700" fill="var(--ink)">웹사이트 (Website)</text>
  <text x="506" y="103" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">브라우저 세션 연동 및 탐색</text>
  <rect x="496" y="118" width="196" height="42" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="506" y="137" font-family="var(--sans)" font-size="11.5" font-weight="700" fill="var(--ink)">표준 API (MCP, OpenAPI, UCP)</text>
  <text x="506" y="153" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">조회, 장바구니, 결제, 송금 요청</text>
  <rect x="496" y="168" width="196" height="44" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="506" y="187" font-family="var(--sans)" font-size="11.5" font-weight="700" fill="var(--ink)">비즈니스 에이전트 (UCP Ask 등)</text>
  <text x="506" y="203" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">기업 전용 에이전트와 직접 대화</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 430" role="img" aria-label="Poppy 1.0 프로토콜의 탐색, 인증, 3대 상호작용 채널 구조 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-acc-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="430" fill="var(--bg-2)"/>
  <rect x="16" y="16" width="318" height="104" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="40" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 개인 에이전트 (Muse 등)</text>
  <text x="30" y="64" font-family="var(--mono)" font-size="12" fill="var(--ink)">/.well-known/poppy.json 탐색</text>
  <text x="30" y="86" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">에이전트 신원 제시 및 중요 동작 전 고객 승인</text>
  <line x1="175" y1="120" x2="175" y2="142" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="16" y="146" width="318" height="116" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="30" y="170" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">2. Poppy 1.0 연결 규격</text>
  <text x="30" y="194" font-family="var(--mono)" font-size="12" fill="var(--ink)">Session JWT + OAuth 2.0 권한 부여</text>
  <text x="30" y="218" font-family="var(--mono)" font-size="12" fill="var(--ink)">MCP / OpenAPI / UCP 표준 결합</text>
  <text x="30" y="242" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">산업별 확장 규격 (Shopify Commerce 등)</text>
  <line x1="175" y1="262" x2="175" y2="284" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="16" y="288" width="318" height="126" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="312" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">3. 기업의 3대 상호작용 채널</text>
  <text x="30" y="338" font-family="var(--sans)" font-size="12" fill="var(--ink)">웹사이트: 브라우저 세션 연동 및 웹 탐색</text>
  <text x="30" y="364" font-family="var(--sans)" font-size="12" fill="var(--ink)">표준 API: 조회, 장바구니, 결제, 송금 처리</text>
  <text x="30" y="390" font-family="var(--sans)" font-size="12" fill="var(--ink)">비즈니스 에이전트: 기업 에이전트와 직접 대화</text>
</svg>
<figcaption style="margin-top: 0.65rem; font-size: 0.85rem; color: var(--ink-2); text-align: center; line-height: 1.5;">Poppy 1.0 아키텍처: 개인 에이전트가 도메인의 poppy.json으로 지원 채널을 탐색하고, Session JWT와 OAuth 권한을 바탕으로 웹사이트, API, 비즈니스 에이전트와 상호작용한다.</figcaption>
</figure>

Poppy는 통신 규격을 백지에서 새로 만들지 않고 널리 쓰이는 웹과 에이전트 표준을 조합하는 방식을 택했다. 도구 연결에는 MCP(Model Context Protocol)와 OpenAPI를 활용하고, 상거래에는 UCP(Universal Commerce Protocol)를 쓰며, 계정 권한 부여에는 OAuth 표준을 사용한다.[^3] 고객은 OAuth 인증으로 개인 에이전트가 자기 계정에서 수행할 작업과 금지할 작업을 직접 지정하고, 승인한 권한을 언제든 조회하거나 철회할 수 있다.

[^3]: Poppy 1.0 기술 명세(`personalagentprotocol.org/docs/1.0/spec`)를 보면 기업은 `https://{도메인}/.well-known/poppy.json` 경로에 지원 채널과 OAuth 메타데이터를 게시한다. 비회원(게스트) 요청은 가명 처리한 Session JWT 헤더만으로 세션 연속성을 유지하며, 계좌 조회나 주문 변경처럼 계정 접근이 필요한 작업에만 OAuth 액세스 토큰을 결합한다.

10월 초안과 비교하면, 이번 1.0 버전은 단계적 도입과 표준 결합 규칙, 피드백 수집, 산업별 확장을 집중 보강했다.

| 개선 영역 | 1.0 명세에 반영된 세부 내용 |
|---|---|
| 단계적 도입 지원 | 기업이 모든 기능을 한꺼번에 개발하지 않아도 기본 탐색과 기초 기능부터 적용한 뒤 점진적으로 지원 범위를 확장할 수 있도록 절차를 단순화했다 |
| 기존 표준 결합 정교화 | MCP, OpenAPI, UCP, OAuth 등 기존 표준 규격을 프로토콜 규격에 맞춰 호출하고 조합하는 세부 규칙을 명확히 정의했다 |
| 가이드 제공 및 피드백 수집 | 기업이 개인 에이전트에게 서비스 이용 지침을 전달하고, 지원하지 않는 작업에 대해 에이전트로부터 피드백을 수집하는 기능을 확대했다 |
| 산업별 확장(Extensions) 도입 | 핵심 프로토콜 명세를 수정하지 않고 산업별 기능을 추가하는 확장 구조를 신설했다 (Shopify와 공동 작성한 상거래 확장이 대표 사례) |

Sierra는 기업들이 외부 도움 없이 자체적으로 Poppy 1.0을 도입할 수 있도록 설정 절차를 안내하는 구현 키트(implementation kit)와 명세 파일의 정합성을 검사하는 검증기(validator)도 함께 공개했다.

## Shopify 전 가맹점 기본 적용과 UCP 연동

전자상거래 플랫폼 Shopify는 이번 1.0 출시와 동시에 플랫폼 전체에 Poppy를 기본 적용했다. 현재 전 세계 175개국 이상의 상점이 Shopify를 기반으로 운영되고 있으며, 모든 Shopify 상점은 이미 기본값으로 UCP(Universal Commerce Protocol)를 지원하고 있다. 이번 출시에 맞춰 Shopify는 플랫폼 내 모든 가맹점이 자동으로 Poppy 파일을 게시하도록 조치했다. 개별 상점 주인이 추가로 코드를 작성하거나 설정을 바꿀 필요가 없다.

| 구분 | 담당 역할과 시점 | 주요 처리 기능 |
|---|---|---|
| Poppy (Personal Agent Protocol) | 쇼핑 시작 전 단계의 신원 확인 및 권한 설정 | 에이전트 신원 확인, 기업 제공 채널 탐색, 허용 작업 범위 확인, 게스트 또는 고객 계정 로그인 연결 |
| UCP (Universal Commerce Protocol) | 실제 쇼핑 및 거래 실행 단계 | 상품 검색 및 탐색, 장바구니 담기, 결제 및 체크아웃 진행 |
| Poppy 상거래 확장 (Commerce Extension) | Poppy와 UCP 두 프로토콜을 연결하는 확장 규격 | 게스트 쇼핑과 계정 로그인 전환, 중요 행동 전 고객 사전 승인 강제, `UCP Ask`를 통한 상점 에이전트와의 직접 대화 |

UCP와 Poppy는 경쟁하지 않고 역할을 분담해 상호 보완한다. Shopify가 공동 저자로 참여해 만든 Poppy 상거래 확장은 두 프로토콜을 하나로 이어 준다. 개인 에이전트는 상점 계정에 로그인하기 전 비회원(게스트) 상태로 쇼핑을 시작할 수 있고, 결제나 주문 확정처럼 중요한 동작을 실행하기 전에는 반드시 고객의 사전 승인을 거친다. 또한 구매자의 개인 에이전트가 `UCP Ask`를 통해 상점 측 비즈니스 에이전트에게 재고나 상품 정보를 직접 묻는 흐름도 지원한다.

## 금융, 유통 결제, 항공 분야의 초기 운영 사례

Shopify 가맹점과 더불어 금융과 항공 분야의 초기 디자인 파트너들도 Poppy 1.0을 실제 서비스에 적용해 운영을 시작했다. 원문은 머큐리, 싱크로니, 터키항공 세 기업의 운영 사례를 구체적으로 소개한다.

| 도입 기업 | 산업 분야 | 개인 에이전트를 통한 주요 지원 기능 | 권한 통제 및 적용 방식 |
|---|---|---|---|
| 머큐리 (Mercury) | 기업 및 개인 금융 핀테크 | 계좌 잔액 조회, 최근 거래 내역 검토, 지출 항목 분류, 예산 및 영수증 최신화, 송금 및 결제 요청 생성 | 송금이나 결제 요청 시 실제 자금이 이체되기 전에 해당 계좌의 승인 정책(approval policy) 절차를 거치도록 강제함 |
| 싱크로니 (Synchrony) | 소비자 금융 및 리워드 | 고객의 지불 여력과 할부 금융 상품, 맞춤형 혜택(오퍼) 및 리워드를 함께 고려한 상품 탐색 지원 | 50만 개 이상의 가맹점 네트워크에서 에이전트 쇼핑에 금융 혜택을 연동 |
| 터키항공 (Turkish Airlines) | 항공 및 여행 | 항공 운임, 운항 상태, 경유지(스톱오버) 조회, 예약 번호와 영문 성(surname)으로 예약 내역 불러오기, 비즈니스석 승급 탐색 | 마일스앤스마일스(Miles&Smiles) 회원의 좌석 승급 시 결제 전 고객 승인을 거치며, 대화창 내 결제 기능도 개발 중 |

세 사례 모두 잔액 확인, 할부 혜택 비교, 항공권 및 경유지 조회 같은 탐색 업무는 개인 에이전트에게 맡기되, 실제 자금이 이체되거나 좌석 승급 결제가 이뤄질 때는 계좌의 기존 승인 정책이나 고객 본인의 최종 승인을 거치도록 설계했다.[^4]

[^4]: 원문 하단 주석에 따르면 머큐리(Mercury) 자체는 은행이 아니며, 연방예금보험공사(FDIC)의 예금자 보호를 받는 파트너 은행들을 통해 금융 서비스를 제공하는 핀테크 기업이다.

## 가장 흥미로운 지점

나는 이번 발표에서 이 프로토콜이 초기 생태계를 확보하는 방식을 가장 눈여겨보았다. 새로운 웹 표준이 제안되더라도 개별 기업과 웹사이트 운영자가 직접 서버 설정을 바꾸고 API를 연동해야 한다면 실제 보급까지는 수년이 걸리기 마련이다. Sierra와 파트너사들은 이 초기 보급 문제를 에이전트와 상점 플랫폼 양측에서 동시에 풀었다. 에이전트 측에서는 Meta의 AI 에이전트 Muse가 모든 웹사이트 방문 시 `poppy.json`을 가장 먼저 확인하도록 기본값을 바꿨고, 상점 측에서는 Shopify가 175개국 이상의 전체 가맹점에 Poppy 파일을 일괄 배포했다. 개별 상점 주인이 별도 개발 작업을 하지 않아도 하루아침에 수백만 개의 상점이 에이전트용 표준 인터페이스를 갖추게 되었다.

아울러 기존 표준들과 역할을 분담하는 설계도 실용적이다. Poppy는 도구 호출 규격인 MCP나 상거래 표준인 UCP를 대체하려 하지 않고, 그 앞 단계에서 에이전트의 신원을 증명하고 고객의 위임 권한을 확인하는 탐색 및 인증 절차만 전담한다. 특히 단순 조회는 에이전트에게 맡기더라도 금전이 오가는 실행 단계에는 반드시 사람의 최종 승인을 거치도록 프로토콜과 확장 규격에 명시했다. 머큐리의 계좌 승인 정책 연동이나 터키항공의 비즈니스석 승급 결제 전 승인이 이를 잘 보여 주며, 기업들이 안심하고 프로토콜을 도입할 수 있는 근거가 된다.

## 출처

- 발행 기관: Sierra
- 저자: Bret Taylor, Clay Bavor
- 발표일: 2026-11-13
- 원문: <https://sierra.ai/kr/blog/releasing-poppy>
- 관련 문서: [Personal Agent Protocol 1.0 Specification](https://personalagentprotocol.org/docs/1.0/spec), [Introducing Personal Agent Protocol](https://sierra.ai/kr/blog/introducing-personal-agent-protocol)
- 삽화: 커버의 치비 서소영 삽화 1장은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조하여 gpt-image-2.6-flare image-to-image로 생성했다.
