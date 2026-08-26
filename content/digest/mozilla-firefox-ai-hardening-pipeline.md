---
title: "Behind the Scenes: Hardening Firefox with Claude Mythos Preview"
date: 2026-05-08T18:15:00+09:00
tags: ["AI 보안", "Firefox", "agentic harness", "취약점 발견"]
categories: ["에이전트와 코딩"]
summary: "Mozilla가 agentic harness 파이프라인을 구축해 Firefox 150에서 271개 잠재 보안 버그를 발견·수정한 과정. 핵심은 모델보다 파이프라인이며, 정적 분석의 false positive 한계는 동적 testcase 검증으로 돌파됐다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Mozilla가 Firefox 150에서 271개의 잠재 보안 버그를 Claude Mythos Preview로 발견·수정한 과정을 공개했다. 발신자는 Brian Grinstead, Christian Holler, Frederik Braun(Mozilla, 2026-05-07).
2. 핵심 진단은 정적 분석 LLM이 false positive로 무너졌던 자리를 *agentic harness*가 동적 testcase 실행으로 돌파했다는 것이다. 모델 능력 향상과 harness 기법(steering·scaling·stacking) 진화가 곱해지면서 슬롭이 신호로 바뀌었다.
3. 결론은 "모델은 프리미티브, 파이프라인이 스케일을 만든다"는 것. 누구든 단순 프롬프트로 지금 시작해 점진적으로 정제하면, 다음 모델 업그레이드의 효과를 곱셈으로 누리게 된다.

## 자료의 정체

- 발행 기관: Mozilla Hacks (Mozilla 공식 개발자 블로그)
- 저자: Brian Grinstead(Distinguished Engineer, Firefox), Christian Holler(Tech Lead·Principal Engineer), Frederik Braun(Application Security 매니저)
- 발행일: 2026-05-07
- 배경: 2주 전 Mozilla는 AI 모델의 도움으로 Firefox에서 *유례없는 양*의 잠재 보안 버그를 식별·수정했다고 발표했다. 본 글은 그 후속 — 어떻게 접근했고, 무엇을 발견했고, 다른 프로젝트에 어떤 권고를 남기는가.

## 갑자기, 버그가 매우 좋아졌다

원문이 첫 섹션 제목으로 잡은 표현은 "Suddenly, the bugs are very good"이다. 몇 달 전만 해도 오픈소스 프로젝트에 들어오는 AI 생성 보안 리포트는 대부분 *unwanted slop*으로 알려져 있었다. 그럴듯하지만 틀린 리포트는 메인테이너에게 비대칭 비용을 강요한다 — 만들기는 싸지만, 응대는 비싸다.

이 역학이 단 몇 달 만에 뒤집혔다. 두 축이 동시에 움직였다고 원문은 적는다.

1. 모델 자체의 추론 능력 향상.
2. *모델을 다루는 기법(harnessing)*의 진화 — steering, scaling, stacking으로 신호를 키우고 노이즈를 거른다.

두 축이 곱해지면서 신호가 노이즈를 압도했다.

## 공개된 정교한 버그 사례

Mozilla는 이례적으로 13개 버그 리포트의 베일을 일찍 걷었다. *발견된 것이 얼마나 정교한지를 보여주고, 방어자들의 행동을 촉구하기 위해서*다. 표를 그대로 옮긴다.

| Bug ID | 요약 |
|---|---|
| 2024918 | 잘못된 동등성 검사로 JIT가 살아있는 WebAssembly GC struct 초기화를 최적화로 제거. 가짜 객체 프리미티브 → 임의 read/write. 내·외부 fuzzing이 광범위하게 다룬 코드였다. |
| 2024437 | 15년 묵은 `<legend>` 버그. 재귀 스택 깊이 제한, expando 속성, 사이클 컬렉션 등 멀리 떨어진 영역의 엣지 케이스를 정밀 조립. |
| 2021894 | IPC race condition을 안정적으로 트리거. 침해된 콘텐츠 프로세스가 부모의 IndexedDB refcount를 조작 → UAF · sandbox escape. |
| 2022034 | 원시 NaN이 IPC 경계를 넘으며 태그된 JS 객체 포인터로 위장. 이중 역직렬화로 부모 프로세스 가짜 객체 프리미티브. |
| 2024653 | 중첩 이벤트 루프, pagehide 리스너, 가비지 컬렉션을 엮어 `<object>` 요소 속성 setter UAF. |
| 2022733 | WebTransport에 수천 개 인증서 해시를 흘려 refcount-heavy 복사 루프의 race를 늘림. 침해된 콘텐츠 프로세스에서 IPC로 부모 UAF. |
| 2023958 | 악성 DNS 서버 시뮬레이션. glibc DNS 함수 호출 인터셉트로 UDP→TCP fallback 엣지 케이스 재현 → HTTPS RR · ECH 파싱 중 buffer over-read와 부모 프로세스 스택 메모리 누출. |
| 2025977 | 20년 묵은 XSLT 버그. 재진입 `key()` 호출이 해시 테이블 rehash를 일으켜 backing store가 해제됐는데 raw entry 포인터가 여전히 사용 중. |
| 2027298 | 색상 선택기를 패치해 자동화 불가 사용자 선택을 시뮬레이트. 동기 입력 이벤트로 중첩 이벤트 루프를 돌려 actor teardown 재진입 → 콜백 free 중 unwinding → 콘텐츠 프로세스 UAF. |
| 2023817 | 침해된 콘텐츠 프로세스가 임의 배경화면 이미지를 부모에서 디코딩하게 함. 이미지 디코더의 가상 취약점과 결합 시 sandbox escape. 부모의 입력 신뢰 수준을 추론해야 했다. |
| 2029813 | RLBox(서드파티 라이브러리용 in-process sandboxing)를 우회. untrusted→trusted 경계 값 복사 검증 로직의 빈틈 활용. |
| 2026305 | 매우 작은 testcase로 HTML 테이블의 `rowspan=0` 특수 의미를 악용. 65535 행 이상을 추가해 클램프를 우회하고 16-bit 레이아웃 비트필드를 오버플로. 수년간 fuzzer가 놓침. |

위 중 다수는 *sandbox escape*이며, 콘텐츠 프로세스가 이미 별도의 버그로 침해된 상태에서 부모 프로세스로의 권한 상승을 시도하는 시나리오다. 이런 버그는 fuzzing이 잡기 어려운 영역이고, Mozilla는 이를 [IPC fuzzing-with-snapshots](https://blog.mozilla.org/attack-and-defense/2024/06/24/ipc-fuzzing-with-snapshots/) 같은 신기술로 좁혀왔으나 AI 분석이 이 임계 표면을 훨씬 폭넓게 커버한다고 평가한다.

## 못 찾은 것이 더 흥미로웠다

원문에서 가장 인상 깊은 부분이다. 모델이 *못 찾은 것*도 흥미로웠다 — 시도하지 않아서가 아니라, Firefox의 계층적 방어를 뚫지 못해서다.

> 최근 몇 년간 보안 연구자들이 prototype pollution을 통해 부모 프로세스 sandbox escape를 성공시킨 사례가 있었다. 우리는 이 문제들을 일일이 패치하는 대신 [기본 prototype을 freeze하는 아키텍처 변경](https://bugzilla.mozilla.org/show_bug.cgi?id=1771084)을 단행했다. harness 로그를 감사하면서, 같은 escape 경로를 시도하다 이 설계에 막힌 사례를 다수 발견했다. 선행 하드닝의 직접적 보상을 관찰한 것이 새 버그를 찾고 고치는 일보다 더 보람 있었다.

선행 투자한 방어 매커니즘이 미래의 AI 공격 시도까지 막아주는 셈이다.

## Hardening 파이프라인 설계

Mozilla는 지난 몇 년간 LLM 코드 감사 실험을 해왔다. GPT-4·Sonnet 3.5로 고위험 코드를 정적 분석시킨 초기 시도는 가능성을 보였으나, false positive 비율이 높아 스케일이 불가능했다.

전환은 *agentic harness*에서 왔다. 핵심 특성은 다음과 같다.

> 적절한 인터페이스와 지시가 주어지면, harness는 코드의 버그에 대한 가설을 검증하기 위해 *재현 가능한 testcase*를 생성·실행할 수 있다.

즉 의심 → 동적 검증 → 자기 기각의 루프가 자동화된다. 이로써 진짜 버그를 찾고 *동시에* 재현 불가능한 추측을 자체 폐기한다.

Anthropic이 2026년 2월 [전달한 초기 버그](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/)를 수정한 뒤, Mozilla는 [기존 fuzzing 인프라](https://hacks.mozilla.org/2021/02/browser-fuzzing-at-mozilla/) 위에 자체 harness를 구축했다.

작은 실험은 Claude Opus 4.6으로 sandbox escape를 찾는 작업이었다. 처음에는 터미널에서 직접 관찰하며 프롬프트와 로직을 튜닝했다. 안정되자 ephemeral VM 풀에 작업을 병렬화 — 각 VM은 특정 대상 파일을 맡고 발견을 버킷에 기록한다.

## 모델은 프리미티브, 파이프라인이 시스템

원문이 강조하는 핵심 문장을 그대로 옮긴다.

> 발견 서브시스템은 필수지만 충분조건이 아니다. 노력을 스케일하려면 보안 버그 라이프사이클 전체와 통합해야 한다 — 무엇을·어디서 찾을지 결정하고, 산출물을 dedup하고, 트래킹하고, 트리아지하고, 패치를 출시한다. 모델이 harness의 핵심 프리미티브이지만, 이 전체 파이프라인이 있어야 실제 효용이 나온다.

> harness는 프로젝트 간 재사용이 가능할 수 있지만, 파이프라인은 본질적으로 프로젝트별이다. 각 코드베이스의 시맨틱·툴링·프로세스를 반영해야 하기 때문. 이 구축에는 상당한 반복과 Firefox 엔지니어들과의 긴밀한 피드백 루프가 필요했다.

다시 말해 *일반 솔루션을 사오는 식으로는 작동하지 않는다*. 파이프라인은 프로젝트의 누적 자본이다.

## 모델 업그레이드의 곱셈 효과

엔드투엔드 파이프라인이 깔리면 새 모델로 swap하는 것은 trivial해진다. Mozilla는 이 자산을 먼저 만든 덕분에 Mythos Preview를 받자마자 평가에 들어갈 수 있었다고 적는다.

> 우리 경험상 모델 업그레이드는 파이프라인 전체의 효과를 동시에 끌어올린다 — 시스템이 잠재 버그를 찾는 것·POC testcase를 만드는 것·병리와 임팩트를 서술하는 것 모두에서 동시에 좋아진다.

곱셈 효과의 데이터로 다음 그래프를 첨부한다.

![Firefox 보안 버그 수정 월별 추이 — 2025년 매월 20-30개에서 2026년 4월 423개로 급증](https://img.seosoyoung.eiaserinnys.me/images/mozilla-firefox-ai-hardening-pipeline/security-bug-fixes.png "Firefox 월별 보안 버그 수정 수: 2025년 20–30 범위에서 2026년 2–3월 60–70 → 4월 423개. 출처: Mozilla Hacks")

수치 정리.

- Firefox 150에서 Claude Mythos Preview로 발견된 271개 버그를 수정.
- 추가로 149.0.2, 150.0.1, 150.0.2 등 후속 릴리즈에 더 출시.
- 2026년 4월 한 달 동안 보안 버그 수정 *총 423개*. 이 중 271개가 발표분, 41개가 외부 리포트, 나머지 111개가 내부 발견(파이프라인+다른 모델+fuzzing 등으로 분산).
- 271개의 심각도 분포: sec-high 180개, sec-moderate 80개, sec-low 11개.
- 100명 이상이 코드를 기여했다.

## 단일 sec-high가 곧 익스플로잇은 아니다

FAQ 섹션이 다음 한 가지를 분명히 한다 — sec-high·sec-critical 자체가 실전 RCE를 의미하지는 않는다.

> 대부분의 경우 단일 critical/high 버그는 Firefox를 침해하기에 충분하지 않다. Firefox가 defense-in-depth 아키텍처이기 때문이다 — 예: JIT 버그 익스플로잇은 sandboxed·site-specific 프로세스에서 RCE를 달성할 뿐이다. 실제 공격자는 보통 여러 익스플로잇을 체이닝해 sandbox 계층과 ASLR 같은 OS-수준 완화책을 통과한다.

Mozilla는 익스플로잇 가능성을 일일이 시험하지 않고 AddressSanitizer가 보고하는 *예측 가능한 크래시 증상*(UAF, OOB)을 기준으로 sec-high를 분류한다고 밝힌다. 이는 false negative 위험을 낮추고, 자원을 더 많은 발견·수정에 배분하기 위함이다.

## 도입 권고

원문 끝부분의 권고를 정리한다.

- 누구든 *지금* harness와 모던 모델로 시작할 수 있다. 시작 자체를 미루지 마라.
- 초기 프롬프트는 단순했다 — "이 코드 부분에 버그가 있다, 찾아서 testcase를 만들어라" 수준의 inner loop. 이후 점진적으로 orchestration을 쌓았다.
- 모델은 컨텍스트 형태에 유연하므로 *patch-based 스캐닝*이 file-based 스캐닝과 동등하거나 더 나을 가능성이 높다. Mozilla는 가까운 미래에 CI에 통합해 트리에 들어오는 패치를 스캔할 계획이다.

## 가장 흥미로운 지점

내가 가장 인상 깊게 읽은 대목은 두 곳이다.

첫째, 선행 하드닝이 *AI 공격 시도까지* 막은 직접적 보상을 관찰했다는 부분이다. 보안 투자란 본래 보이지 않는 곳에서 일어나지 않는 사고를 관리하는 일이라 ROI 측정이 어렵다. 그런데 harness 로그에 prototype freezing에 막혀 좌절된 시도가 *기록으로* 남는다. 이는 단순히 새 버그를 잡는 것보다 더 깊은 의미가 있다 — *과거의 설계 결정이 미래의 자동화된 공격에 복리 이자를 지급*한다.

둘째, "모델은 프리미티브, 파이프라인이 시스템"이라는 명제다. AI 도입 논의에서 자주 모델 선정·교체가 핵심으로 다뤄지지만, Mozilla 사례는 그 반대를 가리킨다. 파이프라인이 깔려 있을 때만 모델 교체가 trivial해지고, 그제서야 새 모델의 효과가 시스템 전체로 곱해진다. 파이프라인이 없으면 어떤 모델도 스케일을 만들지 못한다. 이는 AI 도입의 *우선순위*에 직접 영향을 준다.

## 출처

발행: Mozilla Hacks
저자: Brian Grinstead, Christian Holler, Frederik Braun (Mozilla)
발행일: 2026-05-07
원문: <https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/>
