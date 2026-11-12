---
title: "카드 담당 Opus의 토큰 과소비와 위임 구조 8판"
date: 2026-11-12T10:30:00+09:00
categories: ["에이전트와 코딩"]
subjects: ["하네스와 에이전트 설계"]
tags: ["멀티에이전트", "하네스", "컨텍스트 관리", "Claude Code", "아키텍처"]
summary: "카드 담당 Opus가 18시간 동안 12.7억 입력 토큰을 쓴 원인을 살폈다. 실행과 검색 도구를 제외하고 기계가 봉인한 검증 꾸러미만 읽게 한 위임 구조 8판으로 검수 턴 평균 입력을 5분의 1로 줄인 시범 결과를 정리했다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/opus-card-assignee-delegation-v8/01-cover.png"
  alt: "자물쇠로 잠긴 도구 상자 옆 책상에 앉아 하늘색 봉인 인장이 붙은 검수 꾸러미 한 장만 차분히 읽고, 앞쪽의 작은 태엽 조수 인형 둘에게 두루마리 과업을 분담시키는 치비 서소영"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/opus-card-assignee-delegation-v8/01-cover.png"
---

## 3줄 요약

1. 카드 담당 Opus가 18시간 동안 12.7억 입력 토큰을 쓴 원인과 위임 구조 8판의 시범 결과를 정리했다.
2. 완료 보고 뒤에도 결함이 남은 일이 반복돼 담당이 약 22만 토큰 대화를 유지한 채 직접 확인을 반복한 탓이었다.
3. 담당의 도구에서 실행과 검색을 제외하고 기계가 봉인한 꾸러미만 읽게 하자 검수 턴 평균 입력이 5분의 1로 줄었다.

## 1. 18시간 동안 12.7억 토큰은 어디에 쓰였는가

멀티에이전트 환경에서 `카드`는 사용자 요청 하나를 기록하는 작업 단위다. 각 카드의 상위 세션인 `카드 담당`이 과업을 발주하면 `하위 세션`이 별도 컨텍스트에서 조사와 구현을 맡고, 담당은 결과를 검수한다. 2026년 11월 11일 0시부터 18시까지 카드 담당 Opus 36세션(288턴)이 쓴 `캐시 읽기를 포함한 입력 토큰`은 12.7억 토큰이었다. 새 입력과 이전 대화 캐시 읽기를 합친 값으로, 출력 525만 토큰을 더한 정가 추정 비용은 약 542달러였다[^1]. 같은 시간 코드를 작성한 DeepSeek(5.4억), Terra(5.0억), Sol(2.8억)이나 화면을 검수한 세라피엘 Opus(3.5억) 각각보다 일을 맡기는 담당이 훨씬 많이 썼다.

도구를 한 번 부를 때마다 API를 한 번 호출하고 그때까지 누적된 대화 전체를 다시 입력한다. 담당의 호출당 평균 대화는 약 22만 토큰이었다. 1시간 캐시가 만료돼서 비용이 늘어난 것도 아니었고, Fable 5.2 출시(11월 9일) 뒤 Opus가 위임을 꺼린다는 가설도 452세션의 시기별 지표를 대조해 기각했다[^2].

<figure class="blog-diagram">
<style>.blog-diagram{margin:var(--space-4) 0;}.blog-diagram .diagram-svg-desktop{display:block;width:100%;height:auto;background:var(--bg-2);border:1px solid var(--rule);font-family:var(--sans);}.blog-diagram .diagram-svg-mobile{display:none;width:100%;height:auto;background:var(--bg-2);border:1px solid var(--rule);font-family:var(--sans);}@media (max-width:640px){.blog-diagram .diagram-svg-desktop{display:none;}.blog-diagram .diagram-svg-mobile{display:block;}}</style>
<svg class="diagram-svg-desktop" viewBox="0 0 720 256" role="img" aria-label="옛 구조에서 카드 담당 Opus가 하위 보고 뒤 직접 조사와 검증을 반복하며 호출마다 약 22만 토큰 대화를 재입력하는 흐름" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-f1d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-f1d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="256" fill="var(--bg-2)"/>
  <rect x="16" y="42" width="172" height="156" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="30" y="68" font-size="13" font-weight="700" fill="var(--ink)">하위 작업 세션</text>
  <text x="30" y="88" font-size="11" fill="var(--ink-2)">구현원, 화면 검수 등</text>
  <line x1="16" y1="100" x2="188" y2="100" stroke="var(--rule)" stroke-width="1"/>
  <text x="30" y="122" font-size="12" fill="var(--ink)">코드 수정과 자체 시험</text>
  <text x="30" y="144" font-size="12" fill="var(--ink)">말로 쓴 완료 보고 전달</text>
  <text x="30" y="172" font-size="11" fill="var(--accent)" font-weight="700">실제 결함 5건과 보고 불일치</text>
  <line x1="188" y1="120" x2="234" y2="120" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f1d)"/>
  <text x="211" y="110" text-anchor="middle" font-size="11" fill="var(--ink-2)">보고</text>
  <rect x="240" y="18" width="464" height="220" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="256" y="44" font-size="13" font-weight="700" fill="var(--ink)">카드 담당 Opus (대화 누적 유지)</text>
  <rect x="524" y="27" width="164" height="24" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <text x="606" y="43" text-anchor="middle" font-size="11" font-weight="700" fill="var(--ink)">평균 대화 약 22만 토큰</text>
  <line x1="240" y1="58" x2="704" y2="58" stroke="var(--rule)" stroke-width="1"/>
  <rect x="256" y="70" width="210" height="46" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="268" y="90" font-size="12" font-weight="700" fill="var(--ink)">1. 직접 코드 조사와 검색</text>
  <text x="268" y="107" font-size="11" fill="var(--ink-2)">1,905호출 (입력의 42.1%)</text>
  <rect x="478" y="70" width="210" height="46" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="490" y="90" font-size="12" font-weight="700" fill="var(--ink)">2. 직접 시험 실행과 CI 조회</text>
  <text x="490" y="107" font-size="11" fill="var(--ink-2)">하위 보고 재검증과 수습</text>
  <rect x="256" y="126" width="210" height="46" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="268" y="146" font-size="12" font-weight="700" fill="var(--ink)">3. PR 머지와 배포 확인</text>
  <text x="268" y="163" font-size="11" fill="var(--ink-2)">상태 조회마다 대화 재전송</text>
  <rect x="478" y="126" width="210" height="46" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="490" y="146" font-size="12" font-weight="700" fill="var(--ink)">4. 중간 카드 기록 반복</text>
  <text x="490" y="163" font-size="11" fill="var(--ink-2)">648호출 (입력의 14.3%)</text>
  <rect x="256" y="184" width="432" height="40" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="472" y="202" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)">도구 1회 호출 = API 1회 호출 = 누적 대화 전체 재입력</text>
  <text x="472" y="218" text-anchor="middle" font-size="11" fill="var(--ink-2)">입력 토큰의 98.4%가 캐시 읽기 (18시간 동안 36세션 12.7억 토큰)</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 462" role="img" aria-label="옛 구조에서 카드 담당 Opus가 직접 조사와 검증을 반복하며 대화를 재입력하는 흐름 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-f1m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-f1m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="462" fill="var(--bg-2)"/>
  <rect x="14" y="16" width="322" height="92" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="28" y="40" font-size="13" font-weight="700" fill="var(--ink)">하위 작업 세션 (구현원 등)</text>
  <text x="28" y="62" font-size="12" fill="var(--ink-2)">코드 수정 뒤 말로 쓴 완료 보고 전달</text>
  <text x="28" y="84" font-size="12" font-weight="700" fill="var(--accent)">실제 결함 5건과 완료 보고 불일치</text>
  <line x1="175" y1="108" x2="175" y2="136" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f1m)"/>
  <rect x="14" y="142" width="322" height="304" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="168" font-size="13" font-weight="700" fill="var(--ink)">카드 담당 Opus (대화 누적 유지)</text>
  <text x="28" y="188" font-size="12" font-weight="700" fill="var(--accent)">호출당 평균 대화 약 22만 토큰</text>
  <line x1="14" y1="198" x2="336" y2="198" stroke="var(--rule)" stroke-width="1"/>
  <rect x="28" y="210" width="294" height="36" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="40" y="233" font-size="12" fill="var(--ink)">1. 직접 코드 조사와 검색 (1,905호출)</text>
  <rect x="28" y="254" width="294" height="36" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="40" y="277" font-size="12" fill="var(--ink)">2. 직접 시험 실행과 CI 조회 (91호출)</text>
  <rect x="28" y="298" width="294" height="36" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="40" y="321" font-size="12" fill="var(--ink)">3. PR 머지와 배포 상태 반복 조회</text>
  <rect x="28" y="342" width="294" height="36" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="40" y="365" font-size="12" fill="var(--ink)">4. 중간 카드 기록 반복 (648호출)</text>
  <rect x="28" y="388" width="294" height="46" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="175" y="408" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)">도구 1회 호출마다 누적 대화 전체 재입력</text>
  <text x="175" y="426" text-anchor="middle" font-size="12" fill="var(--ink-2)">입력의 98.4%가 캐시 읽기 (12.7억 토큰)</text>
</svg>
<figcaption>그림 1. 옛 위임 구조의 비용 발생 경로. 하위 세션의 말뿐인 보고를 믿기 어려워 카드 담당 Opus가 조사와 검증 도구를 직접 불렀고, 호출마다 약 22만 토큰 분량의 대화가 다시 입력됐다.</figcaption>
</figure>

담당이 도구를 거듭 부른 까닭은 하위 모델이 말로 쓴 보고를 그대로 믿기 어려웠기 때문이다. 하위 세션의 완료 알림으로 시작된 검수 55턴을 살피자 완료 보고와 달리 결함이 남아 있던 일이 다섯 건 있었다. 담당이 이 결함들을 직접 확인하고 수습하면서 호출 수가 급증했다[^3].

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 348" role="img" aria-label="카드 담당 Opus 입력 토큰의 작업별 비중 추정 막대그래프" xmlns="http://www.w3.org/2000/svg">
  <rect width="720" height="348" fill="var(--bg-2)"/>
  <text x="24" y="29" font-size="11" fill="var(--ink-2)">2026-11-11 00:00~18:10 (단위: 입력 토큰 비중 %)</text>
  <rect x="556.1" y="19" width="10" height="10" fill="var(--accent)"/>
  <text x="612.7" y="29" text-anchor="end" text-rendering="geometricPrecision" font-size="11" font-weight="700" fill="var(--ink)">절감 대상</text>
  <rect x="629.2" y="19" width="10" height="10" fill="var(--ink-2)"/>
  <text x="695.5" y="29" text-anchor="end" text-rendering="geometricPrecision" font-size="11" fill="var(--ink-2)">나머지 항목</text>
  <line x1="24" y1="40" x2="696" y2="40" stroke="var(--rule)" stroke-width="1"/>
  <text x="156" y="68" text-anchor="end" font-size="12" font-weight="700" fill="var(--accent)">직접 조사</text>
  <line x1="168" y1="64" x2="528" y2="64" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="56" width="336.8" height="16" fill="var(--accent)"/>
  <text x="514.8" y="68" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">42.1% (1,905호출)</text>
  <text x="156" y="99" text-anchor="end" font-size="12" font-weight="400" fill="var(--ink)">그 밖</text>
  <line x1="168" y1="95" x2="528" y2="95" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="87" width="145.6" height="16" fill="var(--ink-2)"/>
  <text x="323.6" y="99" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">18.2%</text>
  <text x="156" y="130" text-anchor="end" font-size="12" font-weight="700" fill="var(--accent)">카드 관리</text>
  <line x1="168" y1="126" x2="528" y2="126" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="118" width="114.4" height="16" fill="var(--accent)"/>
  <text x="292.4" y="130" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">14.3% (648호출)</text>
  <text x="156" y="161" text-anchor="end" font-size="12" font-weight="400" fill="var(--ink)">위임과 결과 읽기</text>
  <line x1="168" y1="157" x2="528" y2="157" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="149" width="62.4" height="16" fill="var(--ink-2)"/>
  <text x="240.4" y="161" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">7.8%</text>
  <text x="156" y="192" text-anchor="end" font-size="12" font-weight="400" fill="var(--ink)">배포와 머지</text>
  <line x1="168" y1="188" x2="528" y2="188" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="180" width="41.6" height="16" fill="var(--ink-2)"/>
  <text x="219.6" y="192" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">5.2%</text>
  <text x="156" y="223" text-anchor="end" font-size="12" font-weight="400" fill="var(--ink)">임시 파일</text>
  <line x1="168" y1="219" x2="528" y2="219" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="211" width="32.0" height="16" fill="var(--ink-2)"/>
  <text x="210.0" y="223" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">4.0%</text>
  <text x="156" y="254" text-anchor="end" font-size="12" font-weight="400" fill="var(--ink)">스킬과 규칙 읽기</text>
  <line x1="168" y1="250" x2="528" y2="250" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="242" width="29.6" height="16" fill="var(--ink-2)"/>
  <text x="207.6" y="254" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">3.7%</text>
  <text x="156" y="285" text-anchor="end" font-size="12" font-weight="400" fill="var(--ink)">직접 시험과 빌드</text>
  <line x1="168" y1="281" x2="528" y2="281" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="273" width="20.0" height="16" fill="var(--ink-2)"/>
  <text x="198.0" y="285" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">2.5% (91호출)</text>
  <text x="156" y="316" text-anchor="end" font-size="12" font-weight="400" fill="var(--ink)">직접 구현</text>
  <line x1="168" y1="312" x2="528" y2="312" stroke="var(--rule)" stroke-width="1"/>
  <rect x="168" y="304" width="2.5" height="16" fill="var(--ink-2)"/>
  <text x="180.5" y="316" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">0.3% (14호출)</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 426" role="img" aria-label="카드 담당 Opus 입력 토큰의 작업별 비중 추정 막대그래프 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <rect width="350" height="426" fill="var(--bg-2)"/>
  <text x="16" y="30" font-size="12" fill="var(--ink-2)">11-11 00:00~18:10 (%)</text>
  <rect x="186.2" y="20" width="10" height="10" fill="var(--accent)"/>
  <text x="246.5" y="30" text-anchor="end" text-rendering="geometricPrecision" font-size="12" font-weight="700" fill="var(--ink)">절감 대상</text>
  <rect x="263.1" y="20" width="10" height="10" fill="var(--ink-2)"/>
  <text x="334.0" y="30" text-anchor="end" text-rendering="geometricPrecision" font-size="12" fill="var(--ink-2)">나머지 항목</text>
  <line x1="16" y1="42" x2="334" y2="42" stroke="var(--rule)" stroke-width="1"/>
  <text x="16" y="68" font-size="12" font-weight="700" fill="var(--accent)">직접 조사</text>
  <text x="334" y="68" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">42.1% (1,905호출)</text>
  <line x1="16" y1="80" x2="334" y2="80" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="76" width="297.5" height="8" fill="var(--accent)"/>
  <text x="16" y="108" font-size="12" font-weight="400" fill="var(--ink)">그 밖</text>
  <text x="334" y="108" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">18.2%</text>
  <line x1="16" y1="120" x2="334" y2="120" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="116" width="128.6" height="8" fill="var(--ink-2)"/>
  <text x="16" y="148" font-size="12" font-weight="700" fill="var(--accent)">카드 관리</text>
  <text x="334" y="148" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">14.3% (648호출)</text>
  <line x1="16" y1="160" x2="334" y2="160" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="156" width="101.1" height="8" fill="var(--accent)"/>
  <text x="16" y="188" font-size="12" font-weight="400" fill="var(--ink)">위임과 결과 읽기</text>
  <text x="334" y="188" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">7.8%</text>
  <line x1="16" y1="200" x2="334" y2="200" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="196" width="55.1" height="8" fill="var(--ink-2)"/>
  <text x="16" y="228" font-size="12" font-weight="400" fill="var(--ink)">배포와 머지</text>
  <text x="334" y="228" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">5.2%</text>
  <line x1="16" y1="240" x2="334" y2="240" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="236" width="36.7" height="8" fill="var(--ink-2)"/>
  <text x="16" y="268" font-size="12" font-weight="400" fill="var(--ink)">임시 파일</text>
  <text x="334" y="268" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">4.0%</text>
  <line x1="16" y1="280" x2="334" y2="280" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="276" width="28.3" height="8" fill="var(--ink-2)"/>
  <text x="16" y="308" font-size="12" font-weight="400" fill="var(--ink)">스킬과 규칙 읽기</text>
  <text x="334" y="308" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">3.7%</text>
  <line x1="16" y1="320" x2="334" y2="320" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="316" width="26.1" height="8" fill="var(--ink-2)"/>
  <text x="16" y="348" font-size="12" font-weight="400" fill="var(--ink)">직접 시험과 빌드</text>
  <text x="334" y="348" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">2.5% (91호출)</text>
  <line x1="16" y1="360" x2="334" y2="360" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="356" width="17.7" height="8" fill="var(--ink-2)"/>
  <text x="16" y="388" font-size="12" font-weight="400" fill="var(--ink)">직접 구현</text>
  <text x="334" y="388" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="400" fill="var(--ink)">0.3% (14호출)</text>
  <line x1="16" y1="400" x2="334" y2="400" stroke="var(--rule)" stroke-width="6"/>
  <rect x="16" y="396" width="2.5" height="8" fill="var(--ink-2)"/>
</svg>
<figcaption>그림 2. 카드 담당 Opus 일곱 세션의 입력 토큰을 작업 종류별로 분해한 추정치(직전 도구 결과 기준). 직접 구현은 0.3%뿐이었고 직접 조사(42.1%), 그 밖(18.2%), 카드 관리(14.3%) 순으로 비중이 컸다.</figcaption>
</figure>

## 2. 위임 구조 8판: 모델의 보고 대신 기계의 봉인을 읽는다

앞서 검토한 세 안은 기각했다. 대화 압축 상한만 낮추면 추정 절감 폭이 35\~45%에 머물렀다. 서버 도구에 머지와 배포를 맡기는 1판은 리포지토리마다 호스트, 스키마 순서, 롤백 예외가 달라 단일 도구로 통합하지 못했다. 셸 권한을 가진 하위 Opus 관리자를 두는 2판은 검증 호출을 하위 Opus가 대신 맡을 뿐이라 새 세션 초기 캐시 기록(약 6만 토큰)까지 더하면 절감 폭이 2배에도 못 미쳤다.

8판의 핵심 구분은 이것이다. 모델이 작성한 요약문에서는 누락과 착오가 생기곤 한다. 반면 종료 코드와 검증 원출력, 변경분, CI 결론처럼 기계가 직접 남긴 기록은 그대로 신뢰할 수 있다. 따라서 중간 Opus 관리자는 두지 않고 카드 담당 Opus 하나가 설계와 검수를 끝까지 맡게 했다. 대신 일반 셸과 코드 편집, 검색을 담당의 도구 프로필에서 제외해 직접 확인을 반복할 수 없게 했다.

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 388" role="img" aria-label="위임 구조 8판의 여섯 역할 분담과 기준본 및 봉인 꾸러미 흐름" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-f3d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-f3d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="388" fill="var(--bg-2)"/>
  <rect x="16" y="18" width="444" height="134" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="30" y="44" font-size="13" font-weight="700" fill="var(--ink)">카드 담당 (Opus, 대화 압축 상한 25만)</text>
  <line x1="16" y1="56" x2="460" y2="56" stroke="var(--accent)" stroke-width="1"/>
  <text x="30" y="78" font-size="12" font-weight="700" fill="var(--ink)">허용 도구:</text>
  <text x="92" y="78" font-size="12" fill="var(--ink)">기준본 작성, 발췌 읽기, 하위 위임, 눈 호출, 승인 1회</text>
  <text x="30" y="102" font-size="12" font-weight="700" fill="var(--ink)">제외 도구:</text>
  <text x="92" y="102" font-size="12" fill="var(--ink-2)">일반 셸 실행, 리포 코드 편집, 검색, 하위 세션 로그</text>
  <text x="30" y="128" font-size="11" fill="var(--ink-2)">중간 턴 카드 기록은 상황판 1회로 줄이고 마감 턴에 일괄 기록</text>
  <line x1="460" y1="72" x2="494" y2="72" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-f3d)"/>
  <line x1="496" y1="98" x2="462" y2="98" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-f3d)"/>
  <rect x="498" y="18" width="206" height="134" fill="var(--bg)" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="512" y="44" font-size="13" font-weight="700" fill="var(--ink)">눈 (읽기 전용 Opus)</text>
  <line x1="498" y1="56" x2="704" y2="56" stroke="var(--rule)" stroke-width="1"/>
  <text x="512" y="78" font-size="12" fill="var(--ink)">별도 컨텍스트에서 파일과</text>
  <text x="512" y="98" font-size="12" fill="var(--ink)">산출물 그림을 직접 확인</text>
  <text x="512" y="126" font-size="11" fill="var(--ink-2)">판정과 핵심 원문 몇 줄만 반환</text>
  <rect x="16" y="172" width="688" height="34" fill="var(--bg)" stroke="var(--rule)" stroke-width="1"/>
  <text x="360" y="194" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)">산출물 계약: 담당은 기준본(해시 고정)으로 발주하고, 작업자는 봉인 꾸러미를 제출한다</text>
  <line x1="97" y1="206" x2="97" y2="226" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f3d)"/>
  <line x1="272" y1="206" x2="272" y2="226" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f3d)"/>
  <line x1="447" y1="206" x2="447" y2="226" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f3d)"/>
  <line x1="622" y1="206" x2="622" y2="226" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f3d)"/>
  <rect x="16" y="230" width="163" height="140" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="254" font-size="12" font-weight="700" fill="var(--ink)">조사원 블로썸</text>
  <text x="28" y="271" font-size="11" fill="var(--ink-2)">DeepSeek / Terra / Sol</text>
  <line x1="16" y1="281" x2="179" y2="281" stroke="var(--rule)" stroke-width="1"/>
  <text x="28" y="302" font-size="11" fill="var(--ink)">요약이나 제안 없이</text>
  <text x="28" y="320" font-size="11" fill="var(--ink)">원문 발췌와 검색 결과만</text>
  <text x="28" y="338" font-size="11" fill="var(--ink)">담은 조사 꾸러미 작성</text>
  <rect x="191" y="230" width="163" height="140" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="203" y="254" font-size="12" font-weight="700" fill="var(--ink)">구현원 로젤린</text>
  <text x="203" y="271" font-size="11" fill="var(--ink-2)">DeepSeek / Terra / Sol</text>
  <line x1="191" y1="281" x2="354" y2="281" stroke="var(--rule)" stroke-width="1"/>
  <text x="203" y="302" font-size="11" fill="var(--ink)">코드 수정, 시험, PR 뒤</text>
  <text x="203" y="320" font-size="11" fill="var(--ink)">검수 봉인 실행 (미통과 시</text>
  <text x="203" y="338" font-size="11" fill="var(--ink)">스스로 1회 수정 재봉인)</text>
  <rect x="366" y="230" width="163" height="140" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="378" y="254" font-size="12" font-weight="700" fill="var(--ink)">수습공 버터컵</text>
  <text x="378" y="271" font-size="11" fill="var(--ink-2)">일회용 Opus</text>
  <line x1="366" y1="281" x2="529" y2="281" stroke="var(--rule)" stroke-width="1"/>
  <text x="378" y="302" font-size="11" fill="var(--ink)">구현원이 같은 원인으로</text>
  <text x="378" y="320" font-size="11" fill="var(--ink)">두 번 실패한 범위만</text>
  <text x="378" y="338" font-size="11" fill="var(--ink)">직접 고치고 검수 봉인</text>
  <rect x="541" y="230" width="163" height="140" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="553" y="254" font-size="12" font-weight="700" fill="var(--ink)">배달원 버블</text>
  <text x="553" y="271" font-size="11" fill="var(--ink-2)">일회용 Sol</text>
  <line x1="541" y1="281" x2="704" y2="281" stroke="var(--rule)" stroke-width="1"/>
  <text x="553" y="302" font-size="11" fill="var(--ink)">1턴: 머지와 대기 상태 보고</text>
  <text x="553" y="320" font-size="11" fill="var(--ink)">담당의 커밋 대조 승인 뒤</text>
  <text x="553" y="338" font-size="11" fill="var(--ink)">2턴: 배포 봉인과 정리</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 700" role="img" aria-label="위임 구조 8판의 여섯 역할 분담과 기준본 및 봉인 꾸러미 흐름 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-f3m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-f3m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="700" fill="var(--bg-2)"/>
  <rect x="14" y="16" width="322" height="122" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="28" y="40" font-size="13" font-weight="700" fill="var(--ink)">카드 담당 (Opus, 압축 상한 25만)</text>
  <line x1="14" y1="52" x2="336" y2="52" stroke="var(--accent)" stroke-width="1"/>
  <text x="28" y="74" font-size="12" fill="var(--ink)">허용: 기준본, 발췌 읽기, 위임, 눈, 승인 1회</text>
  <text x="28" y="96" font-size="12" fill="var(--ink-2)">제외: 일반 셸, 코드 편집, 검색, 하위 로그</text>
  <text x="28" y="118" font-size="12" fill="var(--ink-2)">중간 카드 기록은 상황판 1회로 축소</text>
  <line x1="155" y1="138" x2="155" y2="166" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-f3m)"/>
  <line x1="195" y1="170" x2="195" y2="142" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-f3m)"/>
  <rect x="14" y="170" width="322" height="78" fill="var(--bg)" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="28" y="194" font-size="13" font-weight="700" fill="var(--ink)">눈 (읽기 전용 Opus)</text>
  <text x="28" y="216" font-size="12" fill="var(--ink)">별도 컨텍스트에서 파일과 그림을 확인하고</text>
  <text x="28" y="234" font-size="12" fill="var(--ink-2)">판정과 핵심 원문 몇 줄만 반환</text>
  <rect x="14" y="264" width="322" height="54" fill="var(--bg)" stroke="var(--rule)" stroke-width="1"/>
  <text x="175" y="286" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)">산출물 계약: 기준본(해시 고정)으로 발주</text>
  <text x="175" y="306" text-anchor="middle" font-size="12" fill="var(--ink-2)">모든 작업자는 봉인된 꾸러미로만 보고</text>
  <line x1="24" y1="318" x2="24" y2="644" stroke="var(--ink-2)" stroke-width="1.5"/>
  <line x1="24" y1="374" x2="40" y2="374" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f3m)"/>
  <rect x="44" y="334" width="292" height="80" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="56" y="358" font-size="12" font-weight="700" fill="var(--ink)">조사원 블로썸 (DeepSeek / Terra / Sol)</text>
  <text x="56" y="380" font-size="12" fill="var(--ink-2)">요약 없이 원문 발췌와 검색 결과만 담은</text>
  <text x="56" y="398" font-size="12" fill="var(--ink-2)">조사 꾸러미 작성</text>
  <line x1="24" y1="464" x2="40" y2="464" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f3m)"/>
  <rect x="44" y="424" width="292" height="80" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="56" y="448" font-size="12" font-weight="700" fill="var(--ink)">구현원 로젤린 (DeepSeek / Terra / Sol)</text>
  <text x="56" y="470" font-size="12" fill="var(--ink-2)">수정과 시험, PR 작성 뒤 검수 봉인 실행</text>
  <text x="56" y="488" font-size="12" fill="var(--ink-2)">미통과(종료 코드 1) 시 스스로 1회 수정</text>
  <line x1="24" y1="554" x2="40" y2="554" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f3m)"/>
  <rect x="44" y="514" width="292" height="80" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="56" y="538" font-size="12" font-weight="700" fill="var(--ink)">수습공 버터컵 (일회용 Opus)</text>
  <text x="56" y="560" font-size="12" fill="var(--ink-2)">같은 원인으로 구현원이 2회 실패한 범위만</text>
  <text x="56" y="578" font-size="12" fill="var(--ink-2)">직접 고치고 검수 봉인</text>
  <line x1="24" y1="644" x2="40" y2="644" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f3m)"/>
  <rect x="44" y="604" width="292" height="80" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="56" y="628" font-size="12" font-weight="700" fill="var(--ink)">배달원 버블 (일회용 Sol)</text>
  <text x="56" y="650" font-size="12" fill="var(--ink-2)">1턴 머지와 대기 보고 → 담당 커밋 승인</text>
  <text x="56" y="668" font-size="12" fill="var(--ink-2)">→ 2턴 배포 완료 확인과 배포 봉인</text>
</svg>
<figcaption>그림 3. 위임 구조 8판의 여섯 역할 분담. 카드 담당 Opus는 일반 셸, 편집, 검색 도구 없이 기준본 발주와 봉인 꾸러미 검수만 맡는다.</figcaption>
</figure>

담당이 해시로 고정한 기준본으로 발주하면 네 작업자가 조사와 구현, 수습, 배포를 맡는다. 코드 전체 맥락이나 산출물 그림을 꼭 봐야 할 때만 별도 컨텍스트의 읽기 전용 Opus인 `눈` 에이전트를 짧게 부른다.

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 276" role="img" aria-label="봉인 스크립트의 종료 코드 0, 1, 2 판정과 후속 처리 흐름" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-f4d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-f4d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="276" fill="var(--bg-2)"/>
  <rect x="16" y="78" width="176" height="120" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="104" font-size="13" font-weight="700" fill="var(--ink)">봉인 스크립트 실행</text>
  <line x1="16" y1="116" x2="192" y2="116" stroke="var(--rule)" stroke-width="1"/>
  <text x="30" y="138" font-size="11" fill="var(--ink-2)">기준본 해시 대조</text>
  <text x="30" y="156" font-size="11" fill="var(--ink-2)">커밋 잔여물과 변경분</text>
  <text x="30" y="174" font-size="11" fill="var(--ink-2)">검증 원출력과 대상 CI</text>
  <line x1="192" y1="108" x2="232" y2="56" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-f4d)"/>
  <line x1="192" y1="138" x2="232" y2="138" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f4d)"/>
  <line x1="192" y1="168" x2="232" y2="220" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f4d)"/>
  <rect x="238" y="18" width="466" height="72" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="254" y="42" font-size="12" font-weight="700" fill="var(--ink)">종료 코드 0: 기계 통과</text>
  <text x="254" y="61" font-size="11" fill="var(--ink)">잔여물 없음, 검증 명령 모두 0, 대상 커밋 CI 성공 확정, 기준본 해시 일치</text>
  <text x="254" y="79" font-size="11" font-weight="700" fill="var(--ink)">→ 카드 담당 Opus가 꾸러미만 읽고 설계 부합 여부 판단</text>
  <rect x="238" y="102" width="466" height="72" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="254" y="126" font-size="12" font-weight="700" fill="var(--ink)">종료 코드 1: 미통과</text>
  <text x="254" y="145" font-size="11" fill="var(--ink-2)">미커밋 잔여물, 검증 명령 실패, 미푸시, CI 실패</text>
  <text x="254" y="163" font-size="11" font-weight="700" fill="var(--ink)">→ 담당 호출 없이 구현원이 스스로 1회 고쳐 다시 봉인</text>
  <rect x="238" y="186" width="466" height="72" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="254" y="210" font-size="12" font-weight="700" fill="var(--ink)">종료 코드 2: 확인 미완료</text>
  <text x="254" y="229" font-size="11" fill="var(--ink-2)">대기 한도 초과, CI 조회 불가, CI 커밋 불일치, 기준본 해시 불일치</text>
  <text x="254" y="247" font-size="11" font-weight="700" fill="var(--ink)">→ 구현원이 고칠 수 없어 그대로 봉인해 카드 담당 호출</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 380" role="img" aria-label="봉인 스크립트의 종료 코드 0, 1, 2 판정과 후속 처리 흐름 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-f4m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-f4m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="380" fill="var(--bg-2)"/>
  <rect x="14" y="16" width="322" height="74" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="40" font-size="13" font-weight="700" fill="var(--ink)">봉인 스크립트 실행</text>
  <text x="28" y="62" font-size="12" fill="var(--ink-2)">기준본 해시, 잔여물, 검증 원출력,</text>
  <text x="28" y="79" font-size="12" fill="var(--ink-2)">대상 커밋 CI 결론, 변경분을 한 꾸러미로 수집</text>
  <line x1="24" y1="90" x2="24" y2="324" stroke="var(--ink-2)" stroke-width="1.5"/>
  <line x1="24" y1="144" x2="40" y2="144" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f4m)"/>
  <rect x="44" y="104" width="292" height="80" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="56" y="128" font-size="12" font-weight="700" fill="var(--ink)">종료 코드 0: 기계 통과</text>
  <text x="56" y="150" font-size="12" fill="var(--ink)">잔여물 없음, 검증 0, 대상 CI 성공, 해시 일치</text>
  <text x="56" y="170" font-size="12" font-weight="700" fill="var(--ink)">→ 카드 담당이 꾸러미만 읽고 합격 판단</text>
  <line x1="24" y1="234" x2="40" y2="234" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f4m)"/>
  <rect x="44" y="194" width="292" height="80" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="56" y="218" font-size="12" font-weight="700" fill="var(--ink)">종료 코드 1: 미통과</text>
  <text x="56" y="240" font-size="12" fill="var(--ink-2)">잔여물 존재, 검증 명령 실패, 미푸시, CI 실패</text>
  <text x="56" y="260" font-size="12" font-weight="700" fill="var(--ink)">→ 담당 호출 전 구현원이 1회 자체 수정</text>
  <line x1="24" y1="324" x2="40" y2="324" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-f4m)"/>
  <rect x="44" y="284" width="292" height="80" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="56" y="308" font-size="12" font-weight="700" fill="var(--ink)">종료 코드 2: 확인 미완료</text>
  <text x="56" y="330" font-size="12" fill="var(--ink-2)">대기 한도 초과, CI 불명, 해시 불일치</text>
  <text x="56" y="350" font-size="12" font-weight="700" fill="var(--ink)">→ 그대로 봉인해 카드 담당에게 보고</text>
</svg>
<figcaption>그림 4. 봉인 스크립트의 세 가지 판정 경로. 기계 통과(0)는 합격 확정이 아닌, Opus가 읽을 준비를 마쳤다는 신호다.</figcaption>
</figure>

구현원은 마지막에 봉인 스크립트를 실행해 검증 결과를 수집한다. 종료 코드 `0`인 기계 통과가 나와도 설계 부합 여부는 담당이 꾸러미를 읽어 판단한다. 코드 `1`인 미통과는 구현원이 먼저 한 번 고치고, 검증을 마치지 못한 코드 `2`만 담당에게 바로 알린다.

## 3. 시범 세 장의 결과와 남은 한계

코드 카드 세 장을 시범 운영해 모두 마쳤고, `눈` 입력을 더한 검수 턴 평균 입력은 5분의 1로 줄었다[^4].

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 288" role="img" aria-label="옛 담당 55턴과 8판 시범 23턴의 검수 턴 입력 토큰 전후 비교 그래프" xmlns="http://www.w3.org/2000/svg">
  <rect width="720" height="288" fill="var(--bg-2)"/>
  <text x="24" y="29" font-size="11" fill="var(--ink-2)">단위: 백만 입력 토큰 (M)</text>
  <rect x="578.1" y="19" width="10" height="10" fill="var(--ink-2)"/>
  <text x="625.4" y="29" text-anchor="end" text-rendering="geometricPrecision" font-size="11" fill="var(--ink-2)">옛 담당</text>
  <rect x="641.9" y="19" width="10" height="10" fill="var(--accent)"/>
  <text x="696.0" y="29" text-anchor="end" text-rendering="geometricPrecision" font-size="11" font-weight="700" fill="var(--ink)">8판 시범</text>
  <line x1="24" y1="40" x2="696" y2="40" stroke="var(--rule)" stroke-width="1"/>
  <text x="166" y="80" text-anchor="end" font-size="12" font-weight="700" fill="var(--ink)">검수 턴 중앙값</text>
  <rect x="180" y="60" width="99.8" height="16" fill="var(--ink-2)"/>
  <text x="289.8" y="72" font-family="var(--mono)" font-size="12" fill="var(--ink-2)">2.85M</text>
  <rect x="180" y="82" width="19.2" height="16" fill="var(--accent)"/>
  <text x="209.2" y="94" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">0.55M</text>
  <text x="166" y="138" text-anchor="end" font-size="12" font-weight="700" fill="var(--ink)">상위 10% (P90)</text>
  <rect x="180" y="118" width="406.0" height="16" fill="var(--ink-2)"/>
  <text x="596.0" y="130" font-family="var(--mono)" font-size="12" fill="var(--ink-2)">11.60M</text>
  <rect x="180" y="140" width="33.9" height="16" fill="var(--accent)"/>
  <text x="223.9" y="152" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">0.97M</text>
  <text x="166" y="196" text-anchor="end" font-size="12" font-weight="700" fill="var(--ink)">평균 (눈 입력 합산)</text>
  <rect x="180" y="176" width="186.6" height="16" fill="var(--ink-2)"/>
  <text x="376.6" y="188" font-family="var(--mono)" font-size="12" fill="var(--ink-2)">5.33M</text>
  <rect x="180" y="198" width="37.1" height="16" fill="var(--accent)"/>
  <text x="227.1" y="210" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">1.06M</text>
  <rect x="24" y="236" width="328" height="36" fill="var(--bg)" stroke="var(--rule)" stroke-width="1"/>
  <text x="188" y="259" text-anchor="middle" font-size="12" fill="var(--ink)">검수 턴 일량 중앙값: 도구 16회 → 모델 호출 4회</text>
  <rect x="368" y="236" width="328" height="36" fill="var(--bg)" stroke="var(--rule)" stroke-width="1"/>
  <text x="532" y="259" text-anchor="middle" font-size="12" fill="var(--ink)">담당 첫 호출 입력: 0.19M → 0.05M</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 364" role="img" aria-label="검수 턴 입력 토큰 전후 비교 그래프 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <rect width="350" height="364" fill="var(--bg-2)"/>
  <text x="16" y="30" font-size="12" fill="var(--ink-2)">단위: 백만 토큰 (M)</text>
  <rect x="209.6" y="20" width="10" height="10" fill="var(--ink-2)"/>
  <text x="259.8" y="30" text-anchor="end" text-rendering="geometricPrecision" font-size="12" fill="var(--ink-2)">옛 담당</text>
  <rect x="276.4" y="20" width="10" height="10" fill="var(--accent)"/>
  <text x="334.0" y="30" text-anchor="end" text-rendering="geometricPrecision" font-size="12" font-weight="700" fill="var(--ink)">8판 시범</text>
  <line x1="16" y1="42" x2="334" y2="42" stroke="var(--rule)" stroke-width="1"/>
  <text x="16" y="72" font-size="12" font-weight="700" fill="var(--ink)">검수 턴 중앙값</text>
  <rect x="16" y="82" width="56.1" height="14" fill="var(--ink-2)"/>
  <text x="80.1" y="94" font-family="var(--mono)" font-size="12" fill="var(--ink-2)">2.85M</text>
  <rect x="16" y="102" width="10.8" height="14" fill="var(--accent)"/>
  <text x="34.8" y="114" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">0.55M</text>
  <text x="16" y="152" font-size="12" font-weight="700" fill="var(--ink)">상위 10% (P90)</text>
  <rect x="16" y="162" width="228.1" height="14" fill="var(--ink-2)"/>
  <text x="252.1" y="174" font-family="var(--mono)" font-size="12" fill="var(--ink-2)">11.60M</text>
  <rect x="16" y="182" width="19.1" height="14" fill="var(--accent)"/>
  <text x="43.1" y="194" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">0.97M</text>
  <text x="16" y="232" font-size="12" font-weight="700" fill="var(--ink)">평균 (눈 입력 합산)</text>
  <rect x="16" y="242" width="104.8" height="14" fill="var(--ink-2)"/>
  <text x="128.8" y="254" font-family="var(--mono)" font-size="12" fill="var(--ink-2)">5.33M</text>
  <rect x="16" y="262" width="20.8" height="14" fill="var(--accent)"/>
  <text x="44.8" y="274" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">1.06M</text>
  <rect x="16" y="302" width="318" height="48" fill="var(--bg)" stroke="var(--rule)" stroke-width="1"/>
  <text x="28" y="322" font-size="12" fill="var(--ink)">검수 일량 중앙값: 도구 16회 → 모델 호출 4회</text>
  <text x="28" y="340" font-size="12" fill="var(--ink-2)">담당 첫 호출 입력: 0.19M → 0.05M</text>
</svg>
<figcaption>그림 5. 옛 담당 다섯 세션(검수 55턴)과 8판 시범(검수 23턴)의 입력 토큰 비교. 눈 에이전트가 쓴 입력을 모두 검수 턴에 합산해도 평균이 5.33M 토큰에서 1.06M 토큰으로 줄었다.</figcaption>
</figure>

재연결 중복 실행 수정에서는 `눈`이 오류 턴 기록이 사라지는 원인을 먼저 찾아냈다. 담당은 재시도 축소 대신 그 원인을 고치도록 설계했고, 검수에서는 이미 실패하던 시험 세 건도 가려냈다.

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 292" role="img" aria-label="완료된 8판 시범 카드 세 장의 카드 담당, 눈, 수습공 Opus 입력 토큰 구성 막대그래프" xmlns="http://www.w3.org/2000/svg">
  <rect width="720" height="292" fill="var(--bg-2)"/>
  <text x="24" y="29" font-size="11" fill="var(--ink-2)">단위: 백만 입력 토큰 (M)</text>
  <rect x="454.3" y="19" width="10" height="10" fill="var(--accent)"/>
  <text x="511.1" y="29" text-anchor="end" text-rendering="geometricPrecision" font-size="11" fill="var(--ink)">카드 담당</text>
  <rect x="527.6" y="19" width="10" height="10" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="604.2" y="29" text-anchor="end" text-rendering="geometricPrecision" font-size="11" fill="var(--ink)">눈 (읽기 전용)</text>
  <rect x="620.2" y="19" width="10" height="10" fill="var(--ink-2)"/>
  <text x="696.0" y="29" text-anchor="end" text-rendering="geometricPrecision" font-size="11" fill="var(--ink)">수습공 버터컵</text>
  <line x1="24" y1="40" x2="696" y2="40" stroke="var(--rule)" stroke-width="1"/>
  <text x="182" y="74" text-anchor="end" font-size="12" font-weight="700" fill="var(--ink)">격리 캐시 수정</text>
  <rect x="196" y="60" width="123.2" height="18" fill="var(--accent)"/>
  <rect x="319.2" y="60" width="24.6" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <rect x="343.8" y="60" width="34.8" height="18" fill="var(--ink-2)"/>
  <text x="388.6" y="74" font-size="12" font-weight="700" fill="var(--ink)">합계 8.30M</text>
  <text x="196" y="94" font-size="11" fill="var(--ink-2)">담당 5.60M, 눈 1.12M(1회), 수습공 1.58M</text>
  <text x="182" y="132" text-anchor="end" font-size="12" font-weight="700" fill="var(--ink)">배포 관리기 갱신</text>
  <rect x="196" y="118" width="232.5" height="18" fill="var(--accent)"/>
  <rect x="428.5" y="118" width="6.6" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="445.1" y="132" font-size="12" font-weight="700" fill="var(--ink)">합계 10.88M</text>
  <text x="196" y="152" font-size="11" fill="var(--ink-2)">담당 10.57M, 눈 0.30M(4회), 수습공 없음</text>
  <text x="182" y="190" text-anchor="end" font-size="12" font-weight="700" fill="var(--ink)">재연결 중복 실행 수정</text>
  <rect x="196" y="176" width="192.9" height="18" fill="var(--accent)"/>
  <rect x="388.9" y="176" width="198.7" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="597.6" y="190" font-size="12" font-weight="700" fill="var(--ink)">합계 17.80M</text>
  <text x="196" y="210" font-size="11" fill="var(--ink-2)">담당 8.77M, 눈 9.03M(3회), 수습공 없음</text>
  <rect x="24" y="238" width="672" height="36" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <text x="360" y="261" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)">세 카드 Opus 입력 합계: 36.98M (카드 담당 24.94M + 눈 10.45M + 수습공 1.58M)</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 376" role="img" aria-label="완료된 8판 시범 카드 세 장의 Opus 입력 토큰 구성 막대그래프 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <rect width="350" height="376" fill="var(--bg-2)"/>
  <text x="16" y="30" font-size="12" fill="var(--ink-2)">단위: 백만 토큰 (M)</text>
  <rect x="191.1" y="20" width="10" height="10" fill="var(--accent)"/>
  <text x="227.9" y="30" text-anchor="end" text-rendering="geometricPrecision" font-size="12" fill="var(--ink)">담당</text>
  <rect x="244.5" y="20" width="10" height="10" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="270.9" y="30" text-anchor="end" text-rendering="geometricPrecision" font-size="12" fill="var(--ink)">눈</text>
  <rect x="286.9" y="20" width="10" height="10" fill="var(--ink-2)"/>
  <text x="334.0" y="30" text-anchor="end" text-rendering="geometricPrecision" font-size="12" fill="var(--ink)">수습공</text>
  <line x1="16" y1="42" x2="334" y2="42" stroke="var(--rule)" stroke-width="1"/>
  <text x="16" y="72" font-size="12" font-weight="700" fill="var(--ink)">격리 캐시 수정</text>
  <text x="334" y="72" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">8.30M</text>
  <rect x="16" y="82" width="92.4" height="14" fill="var(--accent)"/>
  <rect x="108.4" y="82" width="18.5" height="14" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <rect x="126.9" y="82" width="26.1" height="14" fill="var(--ink-2)"/>
  <text x="16" y="114" font-size="12" fill="var(--ink-2)">담당 5.60M, 눈 1.12M(1회), 수습공 1.58M</text>
  <text x="16" y="156" font-size="12" font-weight="700" fill="var(--ink)">배포 관리기 갱신</text>
  <text x="334" y="156" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">10.88M</text>
  <rect x="16" y="166" width="174.4" height="14" fill="var(--accent)"/>
  <rect x="190.4" y="166" width="5.0" height="14" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="16" y="198" font-size="12" fill="var(--ink-2)">담당 10.57M, 눈 0.30M(4회), 수습공 없음</text>
  <text x="16" y="240" font-size="12" font-weight="700" fill="var(--ink)">재연결 중복 실행 수정</text>
  <text x="334" y="240" text-anchor="end" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent)">17.80M</text>
  <rect x="16" y="250" width="144.7" height="14" fill="var(--accent)"/>
  <rect x="160.7" y="250" width="149.0" height="14" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="16" y="282" font-size="12" fill="var(--ink-2)">담당 8.77M, 눈 9.03M(3회), 수습공 없음</text>
  <rect x="16" y="312" width="318" height="48" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <text x="175" y="332" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)">세 카드 Opus 합계: 36.98M</text>
  <text x="175" y="350" text-anchor="middle" font-size="12" fill="var(--ink-2)">담당 24.94M + 눈 10.45M + 수습공 1.58M</text>
</svg>
<figcaption>그림 6. 완료된 시범 카드 세 장의 Opus 입력 토큰 구성. 코드 수정과 시험, 배포 대기는 하위 모델이 맡고 수습공 버터컵은 격리 캐시 수정 카드에서 한 번 투입됐다.</figcaption>
</figure>

시범 중 생긴 작업자 중복 배정과 반복 재개는 포그라운드 실행과 결론 후 단일 알림으로 없앴다. 격리 조사원의 로그 제한도 서버 수정 없이 Sol 지정으로 해소했다.

11월 12일 개인 리포에 이어 회사 PC에도 새 담당과 세 작업자를 등록해 시험 기동이 통과했고, 회사 코드 카드도 새 구조의 담당이 맡게 규칙을 고쳤다. 담당의 반려를 시험하려고 결함을 심은 첫 시도는 구현원이 몰래 넣으라는 지시를 거부하고 밝혀 무산됐다. 디렉터가 재연 시험을 고르자 시범을 이끈 담당이 배포 관리기 갱신 기준본을 그대로 썼다. 기준본은 기록에 실패한 요청을 기억하지 않고 계속 다시 시도하도록 정했다. 담당은 결과 기록에 실패한 요청까지 기억해 재시도를 막는 한 줄을 넣어 PR 초안과 봉인 꾸러미를 직접 만들었다. 단위 시험과 CI 12건이 통과해 기계 통과 봉인까지 마쳤다. 시험이라고 알리지 않은 새 담당 세션에 검수만 맡겼더니 `눈`을 부르지 않고 4회 호출에 Opus 입력 0.27M 토큰만 써서 반려했다. 기준본 두 문장을 들어 그 한 줄을 정확히 지목했고, 결과 쓰기가 한 번 실패하면 요청한 쪽이 제한 시간까지 기다린다는 영향과 기존 시험이 못 잡는 까닭을 적었다. 그 줄을 지우고 시험 하나를 더하라는 방법도 남겼다.

남은 한계 세 가지 가운데 우선 옛 담당 세션과 시범 카드의 과업 크기가 같지 않다. 재연도 실제 카드 흐름 대신 검수 한 턴만 따로 한 번 본 것이라, 반려 뒤 구현원이 다시 고치고 재검수받는 경로는 아직 돌리지 않았다. 화면 작업 카드도 아직 시범하지 않았다.

## 가장 흥미로운 지점

이번 개편에서 내가 눈여겨본 대목은 하위 모델의 보고를 믿지 못하는 문제를 해결하면서 상위 모델 호출을 늘리는 대신 기계의 종료 코드와 원출력을 계약의 근거로 삼았다는 점이다. 카드 담당의 도구에서 일반 셸과 검색을 제외하자 상위 모델은 기준본을 분명하게 적고 기계가 봉인한 증거만 읽어 가부를 판단하게 됐다. 지시문에 당부를 적는 방식만으로는 상위 모델의 직접 개입이 쉽게 줄지 않았다. 프롬프트 수정 대신 도구 권한을 제한했을 때 비로소 설계한 역할 분담이 작동했다.

## 출처

소울스트림 내부 엔지니어링 제안서와 시범 운영 기록(진단 카드 `#1222`, 시범 카드 `#1231`, 작성과 시범 기준 시점 2026-11-12 KST). 커버의 치비 서소영 일러스트는 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 `gpt-image-2.6-flare`의 image-to-image 방식으로 생성했다.

- 원문 제안서 (8판): <https://pages.eiaserinnys.me/d/card1222-proposal-v8/>

[^1]: 같은 날 18시 32분(한국 시간) 이후의 집계에서는 카드 담당 Opus 36세션 295턴, 캐시 읽기를 포함한 입력 12.9억 토큰으로 기록됐다. 이 글의 본문과 그래프는 제안서가 기준으로 삼은 0시부터 18시까지 집계의 초기 진단 수치를 따랐다.
[^2]: 10월, 11월 2일부터 7일, 11월 9일부터 11일 세 구간을 순서대로 비교하면 턴당 도구 호출은 15.5회, 12.4회, 25.7회였고 턴당 위임 호출은 0.50회, 0.41회, 0.80회였다. 턴당 사고 토큰 중앙값은 1,654개, 1,160개, 3,995개였고 직접 편집 비율은 3.5%, 2.7%, 2.9%였다. 11월 9일 이후 사고량과 위임 빈도는 도리어 늘었다. 일별 작업 종류 차이는 보정하지 않은 집계다.
[^3]: 검수 55턴(1,422호출, 입력 2.93억 토큰) 가운데 입력 상위 8턴이 검수 입력의 55%(최대 148호출, 4,243만 토큰)를 썼고, 대화가 25만 토큰을 초과한 호출이 전체 입력의 46.7%를 차지했다.
[^4]: 시범 세 카드 합계(36.98M 토큰)와는 별도로, 구현 없이 조사만으로 끝난 첫 시범 카드에서는 카드 담당이 15번 호출하는 동안 입력 토큰 1.07M(1,066,430)을 썼다.
