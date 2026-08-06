---
title: "How the Open Knowledge Format can improve data sharing"
date: 2026-06-15T02:00:00+09:00
tags: ["AI", "AI 에이전트", "Google Cloud", "오픈소스", "컨텍스트 관리"]
categories: ["에이전트와 코딩"]
summary: "Google Cloud의 Data Cloud 팀이 LLM-wiki 패턴을 휴대 가능한 상호운용 포맷으로 정형화한 Open Knowledge Format(OKF) v0.1을 공개했다. YAML frontmatter가 붙은 마크다운 파일 디렉토리로 지식을 표현하며, 벤더·플랫폼·에이전트 프레임워크에 종속되지 않는 형식만으로 에이전트 간 컨텍스트 공유를 가능하게 한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Google Cloud의 Data Cloud 팀(Sam McVeety, Amir Hormati)이 2026년 6월 12일 Open Knowledge Format(OKF) v0.1을 공개했다. Karpathy가 정리한 *LLM-wiki* 패턴을 휴대 가능한 상호운용 포맷으로 정형화한 벤더 중립 오픈 스펙이다.
2. OKF는 YAML frontmatter가 붙은 마크다운 파일들의 디렉토리로 지식을 표현한다. 새 런타임도 SDK도 없다. *just markdown, just files, just YAML*. 파일 경로가 곧 개념의 정체성이고, 마크다운 링크가 개념 사이의 그래프를 만든다.
3. 참조 구현으로 BigQuery 데이터셋을 걸어 OKF 문서를 자동 생성하는 enrichment agent, 단일 HTML 파일로 동작하는 시각화 도구, GA4·Stack Overflow·Bitcoin 샘플 번들을 함께 공개했다. 스펙·코드·예시 모두 [GitHub](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)에 있다.

## 왜 또 하나의 포맷이 필요한가

조직 안에서 파운데이션 모델이 쓰는 정보의 대부분은 *내부 지식*이다. 테이블 스키마, 비즈니스에서 통용되는 메트릭 의미, 인시던트 런북, 두 시스템 사이의 조인 경로, deprecated된 API 공지 같은 것들.

이 *지식의 원자*들은 오늘날 분절된 시스템 곳곳에 흩어져 있다:

- 각자 API를 가진 메타데이터 카탈로그
- 위키, 서드파티 시스템, 공유 드라이브
- 코드 주석, docstring, 노트북 셀
- 시니어 엔지니어 몇 명의 머릿속

AI 에이전트가 "이벤트 스트림에서 주간 활성 사용자를 어떻게 계산하지?"라는 질문에 답하려면, 이 호환되지 않는 표면들로부터 답을 조립해야 한다. 벤더마다 자기 카탈로그·자기 SDK·자기 지식그래프 스키마를 가지며, 어느 것도 제품·조직 사이에서 휴대 가능하지 않다.

> 결과적으로, 모든 에이전트 빌더는 같은 *컨텍스트 조립* 문제를 처음부터 풀고, 모든 카탈로그 벤더는 같은 데이터 모델을 다시 발명하며, 지식 자체는 그것을 만든 표면 뒤에 갇혀 있다.

## 지식을 살아 있는 위키로

저자들은 개발 팀의 변화를 짚는다. 모델로 같은 문서를 매번 다시 검색하게 하는 대신, 시간이 지날수록 더 유용해지는 *공유 마크다운 라이브러리*를 에이전트에게 주는 방식으로 옮겨가고 있다는 것이다. 에이전트는 자기 파일을 읽고 갱신하는 잡일을 떠맡고, 팀은 콘텐츠를 코드처럼 큐레이션한다.

이 아이디어를 가장 명료하게 정리한 글이 Andrej Karpathy의 [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)다.

> LLM은 지루해하지 않고, 상호참조 갱신을 잊지 않으며, 한 패스에 15개 파일을 건드릴 수 있다. 사람이 개인 위키를 포기하게 만드는 <em>부기(bookkeeping)</em>가 정확히 LLM이 잘하는 일이다.

비슷한 *지식을 위키로* 패턴이 여러 이름으로 반복 등장한다. 코딩 에이전트와 연결된 [Obsidian vault](https://obsidian.md/help/vault), `AGENTS.md` / `CLAUDE.md` 같은 컨벤션 파일 가족, 진짜 작업 전에 에이전트가 참조하는 `index.md` / `log.md` 산출물로 가득 찬 리포, 데이터 팀 안의 *metadata as code* 리포.

문제는 이 인스턴스들이 각자 *bespoke*라는 점이다. Karpathy의 위키, 너희 팀의 위키, 벤더의 카탈로그 export가 겉으로는 비슷해 보여도(마크다운·frontmatter·상호 링크), *협력하도록 의도된 설계는 어디에도 없다*. 모든 문서가 가져야 할 필드, 파일 이름의 의미에 합의된 답이 없다. 그래서 위키에 새겨진 지식은 원래 팀 안에 고립되고, 새 에이전트를 만들 때마다 같은 작업이 반복된다.

## 필요한 건 또 다른 서비스가 아니라 포맷이다

저자들의 진단은 분명하다. 답은 또 다른 *지식 서비스*가 아니라, 지식을 *표현하는 방식*이다. 다음 조건을 만족해야 한다:

- SDK 없이 누구나 생산할 수 있다
- 통합 없이 누구나 소비할 수 있다
- 시스템·조직·도구 사이를 이동해도 살아남는다
- 자기가 묘사하는 코드와 함께 버전 관리에 들어간다
- 사람도 읽을 수 있고 에이전트도 파싱할 수 있다 — 같은 파일, 번역 레이어 없음

OKF는 설계상 그 포맷이다.

## OKF가 어떻게 동작하는가

OKF <em>번들(bundle)</em>은 <em>개념(concept)</em>을 표현하는 마크다운 파일들의 디렉토리다. 테이블, 데이터셋, 메트릭, 플레이북, 런북, API 등 잡고 싶은 모든 것이 개념이 될 수 있다. 개념 하나가 파일 하나. 파일 경로가 그 개념의 정체성이다.

```
sales/
├── index.md
├── datasets/
│   ├── index.md
│   └── orders_db.md
├── tables/
│   ├── index.md
│   ├── orders.md
│   └── customers.md
└── metrics/
    ├── index.md
    └── weekly_active_users.md
```

각 개념 문서는 구조화 필드를 담는 작은 YAML frontmatter 블록과, 나머지 모든 것을 담는 마크다운 본문을 가진다.

```yaml
---
type: BigQuery Table
title: Orders
description: One row per completed customer order.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, revenue]
timestamp: 2026-05-28T14:30:00Z
---

# Schema

| Column | Type | Description |
|---------------|-----------|------------------------------------------|
| `order_id` | STRING | Globally unique order identifier. |
| `customer_id` | STRING | FK to [customers](/tables/customers.md). |

# Joins

Joined with [customers](/tables/customers.md) on `customer_id`.
```

개념은 일반 마크다운 링크로 서로를 가리킨다. 그래서 디렉토리는 *그래프*가 된다. 파일 시스템이 암묵적으로 만드는 부모/자식 링크보다 풍부한 관계망이 생긴다.

번들에는 선택 사항으로 `index.md`(에이전트가 계층을 따라 내려갈 때 단계적 공개에 쓰임)와 `log.md`(변경 이력의 시간순 기록)를 둘 수 있다.

v0.1 명세 전체는 — *conformance 기준, 상호 링크 규칙, 예약된 파일 이름까지 포함하여* — 한 페이지에 들어간다.

## 설계를 떠받치는 세 원칙

**1. 최소한으로 의견을 가진다(Minimally opinionated).** OKF가 모든 개념에 요구하는 것은 정확히 *하나*다 — `type` 필드. 나머지는 모두(어떤 type이 있는지, 어떤 필드를 더 둘지, 본문에 어떤 섹션이 있을지) 생산자에게 맡긴다. 스펙이 정의하는 것은 *상호운용 면적*이지 콘텐츠 모델이 아니다.

**2. 생산자와 소비자의 분리(Producer/consumer independence).** 누가 쓰는지와 누가 읽는지가 깨끗하게 분리된다. 사람이 손으로 쓴 번들을 AI 에이전트가 소비할 수도 있고, 메타데이터 export 파이프라인이 생성한 번들을 시각화 도구에서 브라우즈할 수도 있고, 한 LLM이 합성한 번들을 다른 LLM이 질의할 수도 있다. *포맷이 계약이고, 양 끝의 도구는 각자 독립적으로 교체된다.*

**3. 플랫폼이 아니라 포맷(Format, not platform).** OKF는 특정 클라우드·DB·모델 공급자·에이전트 프레임워크에 묶이지 않는다. 읽고 쓰고 서빙하기 위해 독점 계정이나 SDK를 절대 요구하지 않는다. *지식 포맷의 가치는 그것을 말하는 당사자의 수에서 나오지, 누가 소유하는지에서 나오지 않는다.*

## 함께 공개된 참조 구현

포맷을 구체적으로 만들기 위해, 생산자·소비자 양쪽 끝의 참조 구현을 함께 공개했다:

- **Enrichment agent** — BigQuery 데이터셋을 걸어 모든 테이블과 뷰에 대해 OKF 개념 문서 초안을 만들고, 두 번째 LLM 패스에서 권위 있는 문서를 크롤링해 인용·스키마·조인 경로를 각 개념에 보강한다.
- **Static HTML visualizer** — 어떤 OKF 번들이든 자기 완결적인 단일 파일의 인터랙티브 그래프 뷰로 바꾼다. 백엔드도, 보는 쪽의 설치도, 페이지를 떠나는 데이터도 없다.
- **세 개의 샘플 번들** — GA4 e-commerce, Stack Overflow, Bitcoin public dataset을 참조 에이전트로 생산해 살아 있는 conformant OKF 예시로 리포에 올려 두었다.

저자들은 이들을 *의도적으로 PoC*라고 부른다. 에이전트는 OKF를 생산하는 *한 가지* 방법을 보여주는 것이고, 포맷 자체는 특정 에이전트 프레임워크나 LLM을 요구하지 않는다. 시각화 도구도 *한 가지* 소비 방식일 뿐, HTML이나 그래프 뷰가 필수는 아니다. 생산자·소비자 생태계가 자신들이 공개한 것보다 훨씬 넓게 자라기를 기대한다(*want!*)고 적었다.

## 앞으로

OKF v0.1은 *완성된 표준이 아니라 출발점*이다. 생산자·소비자가 늘어나고, 에이전트가 실제로 어떤 지식 표현을 필요로 하는지 함께 배워 가면서 포맷이 진화할 것이다.

저자들은 다음을 권한다:

- **스펙을 읽어라** (짧다)
- **생산자를 작성하라** — 너희 소스 시스템, DB, 문서 사이트에 대해
- **소비자를 작성하라** — 뷰어, 검색 인덱스, 번들 위에서 추론하는 에이전트
- **참조 구현을 너희 데이터에 돌려 보라**
- **이슈를 올리고, PR을 보내고, 확장 제안을 하라** — 스펙은 버저닝되어 있고 명시적으로 *하위 호환 성장*을 위해 설계되었다

Google Cloud의 Knowledge Catalog도 OKF를 ingest하여 자사 에이전트에게 서빙할 수 있도록 갱신했다고 한다. 관련 코드와 예시는 [knowledge-catalog/toolbox/mdcode/demo](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode/demo)에서 볼 수 있다.

## 가장 흥미로운 지점

이 글에서 가장 눈에 띄는 것은 *Google이 또 하나의 카탈로그 서비스를 내놓지 않았다*는 점이다. 보통 클라우드 벤더의 새 발표는 자기 콘솔 안에서 동작하는 새 SaaS이지만, 이번에는 SDK도 런타임도 없는 *형식*만 발표했다. "포맷의 가치는 그것을 말하는 당사자의 수에서 나오지, 누가 소유하는지에서 나오지 않는다"는 결론 문장이 그 의도를 분명히 드러낸다.

다른 관점에서 보면 이건 *이미 일어나고 있는 패턴의 정형화*다. Karpathy의 LLM-wiki, Obsidian vault, `AGENTS.md` / `CLAUDE.md`, metadata as code 리포 — 이미 사람들은 마크다운+frontmatter로 에이전트 컨텍스트를 관리하고 있었다. Google이 한 일은 새 패러다임을 발명한 게 아니라, 분산된 컨벤션에 *공통 면적*을 그려 준 것이다. 그 면적이 작을수록(여기서는 `type` 필드 하나) 더 많은 당사자가 받아들일 수 있다.

서소영의 atom 지식 트리도 본질적으로 같은 패턴을 따른다 — 카드 본문은 마크다운, 카드 메타는 구조화 필드, 카드 사이는 참조로 묶이고, 폴더 구조가 그래프를 만든다. OKF의 v0.1 형태를 보면서, 이 트리를 *내보낼 때* 어떤 면적이 표준 면적과 겹치는지 점검해 볼 만하다. 특히 `type`·`title`·`description`·`tags`·`timestamp` 같은 최소 필드 집합은 별다른 손질 없이 직접 매핑이 가능하다.

## 출처

- 저자: Sam McVeety (Tech Lead, Data Analytics, Engineering, Data Cloud, Google Cloud), Amir Hormati (Tech Lead, BigQuery, Engineering, Data Cloud, Google Cloud)
- 발행: Google Cloud Blog, 2026-06-12
- 원문: <https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/>
- 스펙·코드: <https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf>
- 인용된 LLM-wiki gist (Karpathy): <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

원문은 텍스트 위주의 발표문이라 본문에 이미지 자산이 없다. 코드 블록(디렉토리 트리, YAML frontmatter 예시)을 그대로 옮겼다.
