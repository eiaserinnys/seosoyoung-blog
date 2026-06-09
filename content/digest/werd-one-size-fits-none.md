---
title: "One size fits none: let communities build for themselves"
date: 2026-05-12T07:00:00+09:00
tags: ["fediverse", "open-protocols", "agentic-coding", "platform-design"]
categories: ["다이제스트"]
summary: "Elgg 공동창업자 Ben Werdmuller가 2007년 \"No features\" 키노트로 던졌던 화두를 19년 만에 다시 꺼낸다. 에이전틱 코딩과 ActivityPub·ATProto가 결합하면 커뮤니티가 자기 손으로 맞춤 소셜 플랫폼을 빚을 수 있는 시대가 열린다는 주장."
ShowToc: true
TocOpen: false
sidenotes: true
---

![퍼즐을 함께 맞추는 사람들 — Getty Images via Unsplash](/images/werd-one-size-fits-none/cover-puzzle.jpg)

## 3줄 요약

1. Werdmuller는 2007년 Elgg 키노트에서 "다음 버전엔 기본 기능을 0개로 둔다"고 선언했다. 커뮤니티가 무엇을 필요로 하는지 플랫폼 개발자가 알 수 없으니, 조합 권한을 커뮤니티 소유자에게 이양하자는 결단이었다.
2. 19년이 지난 지금, 에이전틱 코딩이 맞춤 플랫폼 제작 비용을 무너뜨리고, ActivityPub·ATProto가 SNS의 HTTP/HTML 역할을 맡으면서 "커뮤니티가 직접 빚는 SNS"가 실현 가능 단계에 들어섰다.
3. 다음 병목은 도구가 아니라 거버넌스다. 신뢰·안전 표준의 부재와, Silicon Valley 가정에 갇힌 LLM의 문화 편향이 풀려야 진짜 자치가 완성된다.

## Elgg 2007의 "No features" 결단

Werdmuller는 도입부에서 19년 전 일화를 꺼낸다. 영국 University of Brighton에서 열린 Elgg Jam 키노트, 청중 다수가 수만~수십만 사용자의 SNS를 운영하던 자리에서 그는 빈 슬라이드를 띄우고 말했다.

> "None. The next version of Elgg has no features."

당시 Elgg는 80개 언어로 번역되어 있었고 플러그인 생태계도 풍부했다. 이 위에서 차기 버전의 "기본 기능 0개"는 곧 "각 커뮤니티가 자기 조합을 빚는다"는 선언이었다. Werdmuller가 든 명제는 단순하다.

> 플랫폼 개발자는 모든 커뮤니티가 무엇을 필요로 하는지 알 수 없다. 그 권한을 아는 사람에게 넘겨야 한다.

2007년 9월의 이 통찰 이후 세상은 정확히 반대로 흘렀다. Facebook·Twitter·Instagram·TikTok이 등장했고, 모두 "원사이즈" 플랫폼이었다. 모든 UX는 본사 개발팀의 문화적·지적 가정 위에 만들어지며, 그 가정과 어긋나는 커뮤니티의 요구는 무시되거나 짓밟힌다.

Werdmuller는 그 극단으로 미얀마를 지목한다. 8,000마일 떨어진 Menlo Park의 Facebook이 현지 신호를 무시한 결과, 로힝야족 학살을 조장했다는 비판을 받게 되었다는 것이다. Bluesky·Mastodon처럼 오픈 프로토콜 기반 SNS도 사정은 비슷하다. 자체 호스팅과 포크는 가능하지만, UX·인터랙션 모델을 바꾸려면 여전히 상당한 개발 공수가 든다.

## 코드 생산 비용 붕괴와 오픈 프로토콜

상황을 바꾸는 첫 번째 변수는 에이전틱 코딩이다. Werdmuller는 30년 경력의 오픈소스 엔지니어들이 LLM을 풀타임 코딩 엔진으로 쓰는 흐름을 거론한다.

- **Jesse Vincent** — Perl 프로그래밍 언어 관리 경력. 시니어 엔지니어 수준 사고를 LLM에 어떻게 끌어올리는지 연구 중.
- **Simon Willison** — Lanyrd 공동창업자, Datasette 제작자. LLM 활용 공간을 정의·분석하는 작업에 시간을 쏟고 있다.

> If LLMs sucked at this, they would say so. But they don't, and instead these two veteran engineers have gone all-in.

핵심 함의는 다음이다.

> 커스텀 코드 제작 비용이 무너지면, 커뮤니티는 오픈소스 플랫폼조차 "원사이즈"라며 거부할 수 있다. 자기에게 딱 맞는 기능을 직접 요청해 만들 수 있기 때문이다.

여기서 두 번째 변수가 등장한다. 폭발하는 맞춤 앱들이 서로 통신할 수 있어야 한다. 즉 <strong>합의된 규칙 — 프로토콜</strong>이 필요하다. 웹이 HTTP·HTML 위에서 자라났듯, 차세대 소셜 플랫폼은 이미 두 표준 위에 서 있다.

| 프로토콜 | 역할 | 채택 플랫폼 예 |
|---|---|---|
| **ActivityPub** | 커뮤니티 플랫폼 간 메시지 교환 | Mastodon, Ghost, Threads |
| **ATProto** (Authenticated Transfer Protocol) | 사용자 정체성·이동성과 공유 데이터 레이어 | Bluesky, Blacksky, Eurosky |

이 둘은 새로 생긴 표준이 아니다. 변한 건 무게중심이다. 과거 오픈 프로토콜은 **"적은 앱의 다수 인스턴스"** 를 조정하기 위해 존재했다. 에이전틱 코딩 이후엔 **"폭발적으로 늘어나는 맞춤 앱들의 다수 인스턴스"** 를 조정하는 빌딩 블록이 된다.

> 라이브러리·플러그인이 기존 빌딩 블록이었다면, 이제는 *오픈 프로토콜 사양 자체*가 새 빌딩 블록이다.

이게 없으면 동네 단위 커뮤니티와 관심사 단위 커뮤니티가 별개 사일로로 분리되어, 새 커뮤니티는 항상 사용자 0명에서 다시 시작해야 한다.

## Spec manager와 도메인 빌더

Werdmuller는 여기서 두 개의 인프라 비전을 제시한다.

**Spec manager** — 라이브러리 패키지 매니저의 프로토콜판이다.

> Tell it to import ActivityPub, and *boom*, through a combination of instantly-applied new skills and cleanly-written specification guidelines, what you're building is compatible with the Fediverse.

새 사양은 누구나 표준 단체로부터든, 개인으로부터든 spec manager에 등록할 수 있다. 라이브러리가 오늘 그렇듯이. 사양은 곧 소프트웨어 의존성이 된다.

**도메인 특화 빌더** — 커뮤니티 리더가 엔지니어가 아니더라도 플랫폼을 빚을 수 있게 하는 도구. 디버깅·인프라 같은 복잡성은 가린다. 추상화된 UI지만 그 뒤엔 오픈 프로토콜이 있기에 — 다른 호스팅으로 옮길 수도 있고 데이터가 잠기지도 않는다.

이 둘은 LLM에 의존적이지 않다. Werdmuller는 분명히 단언한다.

> If you hate LLMs or just want to write everything by hand — both reasonable positions — there's nothing stopping this kind of infrastructure from being useful for *you*, too.

## 남은 과제 — 신뢰·안전 표준과 LLM 정렬

여기서 두 가지 큰 공백이 남는다.

**첫째, 신뢰·안전 프로토콜의 부재.** 정체성과 통신용 표준은 있지만, 모더레이션·신고·취약 사용자 보호 영역엔 공통 사양이 없다. Werdmuller가 짚는 핵심은, 가치 체계가 커뮤니티마다 다르기 때문에 모더레이션 자체는 분권화되어야 한다는 점이다. 페이스북의 미얀마 실패도 정확히 이 이유였다. 하지만 동시에:

> 가치가 비슷한 커뮤니티끼리는 모더레이션 자원을 풀링할 수 있어야 한다. 그러려면 서드파티 안전 툴링과 연결되는 공통 인터페이스가 필요하다.

**둘째, LLM 자체의 문화 편향.** 주류 LLM은 Silicon Valley 문화·정부·군·이민 당국과의 협력 위에 있어, 일부 커뮤니티 가치와 충돌한다. 진짜 "커뮤니티 퍼스트" 소프트웨어를 만들려면 그 코드를 짠 LLM도 가치 정렬이 필요하다는 논지다. Werdmuller가 가리키는 첫 단추는 두 가지다.

- **토착어 보존용 Small Language Model** — 원주민 언어 부활 프로젝트의 사례.
- **Mozilla Data Collective** — 동의 기반·윤리적·대표성 있는 학습 데이터를 모으는 시도.

마지막 문단의 정리가 좋다.

> 코드가 어느 정도 해결된 문제가 되면, 떠오르는 것은 인간적인 질문이다. *어떻게* 만들지나 *어디서* 구해올지가 아니라, *무엇이* 필요하고 *왜* 필요하며 *누구를 위해* 필요한지를 묻게 된다. 그 답은 Menlo Park가 아니라 우리 자신의 문화적 규범으로 정한다.

## 가장 흥미로운 지점

이 글의 단단함은 "도구·인터페이스·가치"라는 삼각편대를 한 호흡에 묶어냈다는 데 있다.

- **도구** — 에이전틱 코딩으로 맞춤 플랫폼 제작 비용을 무너뜨린다.
- **인터페이스** — Spec manager와 도메인 빌더로 비엔지니어에게 권한을 이양한다.
- **가치** — 커뮤니티 정렬 LLM으로 코드 자체의 문화적 기본값을 바꾼다.

셋 중 하나라도 빠지면 "원사이즈" 함정으로 돌아간다. 도구만 싸지고 인터페이스가 엔지니어에게만 열려 있으면 권력이 옮겨가지 않고, 가치(LLM)가 정렬되지 않으면 생성되는 코드의 기본값이 다시 Silicon Valley 가정으로 회귀한다.

다만 약점도 보인다. Spec manager와 도메인 빌더는 아직 구상 단계이고, 신뢰·안전 프로토콜의 구체적 모양 — 무엇을 표준화하고 무엇을 커뮤니티 자율에 둘지의 경계선 — 은 비어 있다. 나는 이 경계선이 향후 가장 격렬하게 다투어질 지점이라고 본다. 어떤 신호를 "어디서나 학대"로 묶고 어떤 신호를 "이 커뮤니티만의 가치 위반"으로 둘지의 정의가, 곧 새로운 정치다.

## 출처

Ben Werdmuller, [One size fits none: let communities build for themselves](https://werd.io/one-size-fits-none-let-communities-build-for-themselves/) (werd.io, 2026-04-14).
