---
title: "Generalised Superintelligence (GSI): Superintelligence for Discovery"
date: 2026-11-22T22:00:00+09:00
tags: ["수학", "물리학", "AI 에이전트", "검증"]
categories: ["모델과 연구"]
subjects: ["수학과 과학"]
summary: "신생 연구소 Generalised Superintelligence(GSI)가 과학적 발견을 위한 메타 솔버 플랫폼을 공개했다. 대규모 토큰 탐색 대신 문제의 대수적, 조합적 구조를 먼저 파악해 전용 솔버를 컴파일하고 복수의 독립 검증기로 결과를 확증하며, 수학, 초전도, 양자 오류 정정, 칩 설계 등 8개 분야에서 250건 이상의 발견과 증명을 발표했다."
math: true
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/generalised-superintelligence-meta-solver/fig3-hadamard-order-2148.png"
  alt: "GSI가 구성한 차수 2148 아다마르 행렬의 일부를 원소당 2픽셀로 시각화한 흑백 격자 패턴"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/generalised-superintelligence-meta-solver/fig3-hadamard-order-2148.png"
---

## 3줄 요약

1. 수석 과학자 키샨 쿠마르(Kishan Kumar)와 CEO 야슈라즈 슈클라(Yashraj Shukla)가 2026년 10월 설립한 연구소 Generalised Superintelligence(GSI)에서 과학적 발견 전용 메타 솔버 플랫폼(Meta Solver Platform)을 연구 프리뷰로 선보였다.
2. 약 1만 개의 에이전트와 1,300억 토큰을 투입해 후보를 무작위로 탐색하는 방식 대신, GSI는 문제의 대칭성과 대수적 구조를 먼저 식별한다. 이어 그 구조 전용 솔버를 컴파일하고, 복수의 독립 검증기가 재도출한 결과만 라이브러리에 축적한다.
3. 수학과 초전도, 양자 오류 정정, 반도체 칩 설계 등 8개 분야에 걸쳐 250건 이상의 발견과 증명을 이 플랫폼으로 도출했다. 미해결 차수의 아다마르 행렬을 200종 이상 구성했고, 20년간 새 항이 계산되지 않던 정수열 사전 OEIS A003111의 13번째부터 15번째 항을 계산했다. 1975년에 제기된 엘리아슈베르그 이론의 초전도 전이 온도 상한을 증명하고 화합물 27,000개를 검증했으며, IBM 288큐비트 양자 메모리 회로의 회로 거리가 정확히 16임을 밝혔다.

## 토큰 물량 대신 구조 탐색: 메타 솔버 플랫폼의 작동 방식

영국의 수학자 어빙 존 굿(I. J. Good)은 1965년 논문에서 '인간의 지성 활동을 능가하는 최초의 초지능 기계'를 인류가 만들어야 할 마지막 발명이라 불렀다. 기계가 스스로 새로운 과학적 법칙이나 정리를 발견하고 증명할 수 있게 되면, 그 이후의 모든 발명은 기계가 해낼 수 있기 때문이다. 2026년 11월 16일 연구 프리뷰를 공개한 Generalised Superintelligence(GSI)의 지향점도 이 연장선에 있다. 정답의 진위를 명확히 판별할 수 있는 형식 과학과 자연과학 전반에서 발견 속도를 100배로 높이는 시스템을 구축하는 일이다[^1].

[^1]: GSI는 수석 과학자 키샨 쿠마르(`@kishanvats03`)와 CEO 야슈라즈 슈클라(`@whynesspower`)가 2026년 10월 설립한 소규모 연구소다. 인도 벵갈루루와 미국 샌프란시스코를 거점으로 활동하며, 첫 번째 연구 팀용 버전은 2026년 11월 말 공개된다.

오늘날 인공지능을 활용한 과학적 발견은 주로 막대한 연산 규모에 의존한다. 예컨대 OpenAI의 나비에-스토크스(Navier-Stokes) 방정식 탐색에는 약 1만 개의 에이전트와 1,300억 개의 출력 토큰이 투입됐다. 그만한 연산 비용의 태반은 애초에 해가 있을 수 없는 후보 공간을 탐색하는 데 허비된다는 것이 GSI 연구진의 분석이다. 어려운 문제는 전체 후보 공간이 전수 조사가 불가능할 만큼 방대하지만, 실제로 해가 있을 수 있는 영역은 아주 좁다. 대칭성, 대수적 항등식, 문제를 독립된 하위 부분으로 분해하는 규칙이 곧 문제의 구조다. 이 구조가 해가 있는 후보 영역을 특정한다.

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 198" role="img" aria-label="GSI 메타 솔버 플랫폼의 5단계 발견 파이프라인과 순환 검증 루프" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="198" fill="var(--bg-2)"/>
  <rect x="18" y="20" width="196" height="58" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="43" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">STEP 1. STRUCTURE</text>
  <text x="30" y="64" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">구조 선행 탐지</text>
  <rect x="242" y="20" width="212" height="58" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="254" y="43" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">STEP 2. COMPILER</text>
  <text x="254" y="64" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">구조 전용 솔버 컴파일</text>
  <rect x="482" y="20" width="220" height="58" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="494" y="43" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent-ink)">STEP 3. AGENT LOOP</text>
  <text x="494" y="64" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">최적화, 시뮬레이션, 실험, 검증</text>
  <line x1="214" y1="49" x2="238" y2="49" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink)"/>
  <line x1="454" y1="49" x2="478" y2="49" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="376" y="120" width="326" height="58" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="388" y="143" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">STEP 4. VERIFIERS</text>
  <text x="388" y="164" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">다중 독립 검증과 인증서 발행</text>
  <rect x="18" y="120" width="326" height="58" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="30" y="143" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent-ink)">STEP 5. LIBRARY</text>
  <text x="30" y="164" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">탐지기, 검사기, 솔버 누적</text>
  <line x1="592" y1="78" x2="592" y2="116" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <line x1="376" y1="149" x2="348" y2="149" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <line x1="116" y1="120" x2="116" y2="82" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arr-acc)"/>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 410" role="img" aria-label="GSI 메타 솔버 플랫폼의 5단계 발견 파이프라인과 순환 검증 루프 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="410" fill="var(--bg-2)"/>
  <rect x="16" y="16" width="290" height="58" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="39" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">STEP 1. STRUCTURE</text>
  <text x="28" y="60" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">구조 선행 탐지</text>
  <line x1="161" y1="74" x2="161" y2="92" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-m)"/>
  <rect x="16" y="96" width="290" height="58" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="119" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">STEP 2. COMPILER</text>
  <text x="28" y="140" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">구조 전용 솔버 컴파일</text>
  <line x1="161" y1="154" x2="161" y2="172" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="16" y="176" width="290" height="58" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="28" y="199" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent-ink)">STEP 3. AGENT LOOP</text>
  <text x="28" y="220" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">최적화, 시뮬레이션, 실험, 검증</text>
  <line x1="161" y1="234" x2="161" y2="252" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="16" y="256" width="290" height="58" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="279" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">STEP 4. VERIFIERS</text>
  <text x="28" y="300" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">다중 독립 검증과 인증서 발행</text>
  <line x1="161" y1="314" x2="161" y2="332" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="16" y="336" width="290" height="58" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="28" y="359" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent-ink)">STEP 5. LIBRARY</text>
  <text x="28" y="380" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">탐지기, 검사기, 솔버 누적</text>
  <polyline points="306,365 326,365 326,45 310,45" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arr-acc-m)"/>
</svg>
<figcaption style="margin-top: 0.65rem; font-size: 0.85rem; color: var(--ink-2); text-align: center; line-height: 1.5;">GSI 메타 솔버 플랫폼의 5단계 작동 흐름: 문제의 구조를 먼저 식별해 전용 솔버를 컴파일하고, 다중 검증을 통과한 도구를 라이브러리에 누적해 다음 문제에 재사용한다.</figcaption>
</figure>

GSI의 접근법(`Approach`)과 시스템 평가 노트(`GSI-R-0018`)에 따르면 플랫폼은 다섯 단계로 작동한다.

| 단계 | 핵심 메커니즘 | 성능 및 작동 기준 |
| --- | --- | --- |
| 1. 구조 탐지 (Find the structure) | 탐지기(detector)가 입력 모델 파일에서 학습된 구조 클래스 해당 여부를 검사하고, 체커(checker)가 확인한 뒤에만 채택한다 | 블라인드 테스트에서 클래스 내 모델 8개 중 5개를 정확히 식별했고, 음성 대조군 3개에서 오탐은 0건이다 |
| 2. 전용 솔버 컴파일 (Compile a solver) | 문제 모델을 해당 구조 전용의 데이터 메모리 배치, 가지치기(pruning) 규칙, 대칭성 제거(symmetry breaking) 프로그램으로 컴파일한다 | 윌리엄슨 행렬과 르장드르 쌍 탐색에서 Kissat 4.0.4 및 CP-SAT 9.15보다 30,000배 이상 빠르며, 수작업 FLC 방법(원 저자 대비 1,100\~5,000배 가속)과 대등하다 |
| 3. 에이전트 순환 루프 (Run the loop) | 최적화(Optimise), 시뮬레이션(Simulate), 실험(Experiment), 검증(Verify)의 4단계 폐루프를 돌린다 | 단일 LLM의 출력을 신뢰하지 않고, 저비용 시뮬레이션과 전체 탐색을 거친 뒤 검증에 실패하면 다음 라운드 조건을 고친다 |
| 4. 다중 독립 검증 (Prove it) | 서로 다르게 작성된 복수의 독립 검증기가 결과를 재도출하고, 명시적 인증서(행렬, SAT 반박 인증서 등)를 발행한다 | 한 검증기의 버그가 다른 검증기에서 되풀이될 가능성을 막고, 제3자가 직접 검산할 수 있는 증거를 첨부한다 |
| 5. 도구 라이브러리 축적 (Keep everything) | 검증을 통과한 탐지기, 검사기, 솔버를 중앙 라이브러리에 영구 저장해 후속 문제 탐색에 재사용한다 | 양자 부호 탐색에서 목표 거리가 6단계 늘어나면 연산량이 기존 도구보다 40\~130배 적게 든다(단계당 연산량 증가율은 기존 도구 10\~11배, GSI 솔버 4.9\~5.4배) |

노트 `GSI-R-0018`은 시스템 자체의 일반화 성능을 다룬다. 이 노트에는 수작업 최적화 프로그램과 비교한 결과, 그리고 신규 문제 2건에 체커 우선(Checker-first)으로 접근한 실험 결과가 실려 있다.

| 평가 항목 | 대상 문제 및 조건 | 측정 결과 |
| --- | --- | --- |
| 컴파일된 솔버 대 수작업 솔버 (GSI-R-0018) | 차수 33, 45, 51, 57의 윌리엄슨 행렬 전수 열거 (1스레드) | 수작업 프로그램 대비 소요 시간 비율은 차수 33에서 0.55배, 차수 45에서 0.47배, 차수 51에서 1.10배, 차수 57에서 1.01배다 |
| 체커 우선(Checker-first) 신규 문제 해결 1 | 준순환(quasi-cyclic) 이진 선형 부호의 최소 거리 하한 | 시계를 켠 뒤 4분 46초 만에 체커와 솔버 결과가 일치했다(무작위 부호 300개 전수 일치, 심어둔 오류 6건 전량 거부) |
| 체커 우선(Checker-first) 신규 문제 해결 2 | 세 개의 세제곱수의 합($x^3 + y^3 + z^3 = k$) 상자 내 전체 해 탐색 | 시계를 켠 뒤 5분 55초 만에 체커와 솔버 결과가 일치했다($k \le 130$ 구간 101개 상자, 407개 해 전수 일치) |

연구팀이 이전에 다루지 않은 준순환 부호의 최소 거리 하한과 세 개의 세제곱수의 합을 문제로 주자, 시스템은 정답 판별용 체커를 먼저 작성했다. 그다음 각각 4분 46초와 5분 55초 만에 체커와 완벽히 일치하는 솔버를 구축했다.

## 조합 설계와 정수열: 20년 동안 새 항이 없던 수열과 아다마르 행렬

GSI가 첫 번째 시험대로 삼은 영역은 정답의 진위를 컴퓨터로 즉시 판정할 수 있는 조합론과 정수열이다. 아다마르 행렬(Hadamard matrix), 차집합(difference set), 무게 행렬(weighing matrix)은 원소들이 균형을 이루는 배열이다. 오류 정정 부호, 레이더 신호 설계, 실험 계획법의 수학적 기반이 되지만, 대부분의 크기(차수)에서는 존재 여부가 아직 풀리지 않았다.

![GSI의 수학 분야 주요 발견: 미해결 차수의 아다마르 행렬 200종 이상 구성과 20년간 새 항이 계산되지 않던 OEIS A003111 수열의 13번째부터 15번째 항 계산](https://img.seosoyoung.eiaserinnys.me/images/generalised-superintelligence-meta-solver/fig1-math-hadamard-oeis.jpg)
*GSI의 수학 분야 발표 카드. 왼쪽은 200개 이상의 미해결 차수에서 새로 구성한 아다마르 행렬을, 오른쪽은 2006년 이후 새 항이 계산되지 않던 OEIS A003111 수열에서 새로 계산한 세 개의 항을 보여준다. (출처: Generalised Superintelligence)*

조합 설계(`Combinatorial designs`)와 정수열(`Integer sequences`)에서 GSI가 보고한 핵심 성과는 아래 표와 같다.

| 세부 항목 | 대상 문제 및 기존 상태 | GSI의 발견 및 증명 결과 |
| --- | --- | --- |
| 아다마르 행렬 (GSI-R-0001, GSI-R-0002) | 원소가 $\pm 1$이고 서로 다른 행이 직교하는($HH^T = mI$) 행렬의 미해결 차수 | 미해결 아다마르, 반대칭(skew), 대칭(symmetric) 아다마르 행렬 200종 이상을 새로 구성했다. Cati-Pasechnik 표 4의 미해결 34개 차수와, 2025년 전수 조사에서 미결로 남은 홀수 $v < 2500$ 가운데 반대칭 106개, 대칭 85개를 해결했다 |
| 순환 차집합 (GSI-R-0004) | La Jolla 저장소(버전 1.3) 최소 미해결 사례이자 라이저 추측 사례인 $(465, 145, 45)$ | 원 위의 점 465개 중 145개를 골라 거리 차이가 모두 45번씩 나타나게 하는 방법은 가능한 $8.3 \times 10^{123}$가지 조합 중 하나도 없음을 처음으로 완전히 증명했다 |
| 순환 무게 행렬 (GSI-R-0005) | Tan(2018) 정리 4.24가 배제하고 La Jolla 1.3 및 2.0이 부재(No)로 등재한 $\text{CW}(120, 36)$ | 고유(proper) 순환 무게 행렬 $\text{CW}(120, 36)$을 명시적으로 발견해 기존 정리를 반박했다. La Jolla 1.3의 미해결 2,763개 쌍 중 2,397개를 기록(부재 2,342개, 고유 행렬 25개, 비고유 30개)했고, 2개를 미해결로 보류해 최종 2,395개를 판정했다 |
| 완전 사상 정수열 (GSI-R-0008, GSI-R-0009) | 2006년 12번째 항($\mathbb{Z}_{25}$) 이후 20년간 새 항이 계산되지 않던 OEIS A003111 및 자기쌍대 부호 A003179 | 순환군 $\mathbb{Z}_{27}$, $\mathbb{Z}_{29}$, $\mathbb{Z}_{31}$의 완전 사상 개수인 $a(13)$, $a(14)$, $a(15)$를 계산했다($a(15) \approx 2.43 \times 10^{21}$). 짝수 길이 42\~56의 이진 자기쌍대 부호 개수도 함께 계산했다 |

발표 스레드에서 GSI는 미해결 상태였다가 2025년 이후 해결된 아다마르 행렬 사례 106건 가운데 103건을 자사 플랫폼이 구성했다고 밝혔다[^2]. 또한 온라인 정수열 사전(OEIS)의 A003111은 $n \times n$ 격자의 모든 가로줄, 세로줄, 끝과 끝이 이어지는 대각선마다 표식을 하나씩 놓는 방법의 수를 센다. 2006년 Yuh-Pyng Shieh(셰위핑)가 12번째 항을 계산한 뒤 20년 동안 연산량 한계 때문에 아무도 다음 항을 계산하지 못했다. GSI는 13번째부터 15번째 항까지 계산해 수열을 확장했다. 15번째 항 $a(15)$는 약 $2.43 \times 10^{21}$이다[^3].

[^2]: 연구 아카이브(`GSI-R-0002`)는 2025년 Đoković와 Seberry의 전수 조사에서 미결로 분류된 홀수 $v < 2500$에 대해 $4v$ 차수의 반대칭 아다마르 행렬 106개와 대칭 아다마르 행렬 85개를 해결했다고 구분한다. 또한 일반 아다마르 행렬 34개 미해결 차수를 다룬 `GSI-R-0001`의 검증에는 파이썬 스크립트(`verify.py`)와 코드를 공유하지 않는 독립 C 프로그램(`check_h.c`)을 함께 썼다. 두 검증기는 인증서에서 행렬을 재구성해 $HH^T = mI$ 성립 여부를 검사하여 저장소의 77개 행렬 전수를 통과시켰다.

[^3]: OEIS A003111의 새로 계산된 세 항은 $a(13) = 164,135,223,171,169,785$($\mathbb{Z}_{27}$), $a(14) = 18,674,231,142,723,249,003$($\mathbb{Z}_{29}$), $a(15) = 2,427,915,096,775,283,929,115$($\mathbb{Z}_{31}$)이다. OEIS A003179의 짝수 길이 이진 자기쌍대 부호(binary self-dual codes) 개수도 기존 길이 40에 이어 42부터 56까지 계산했다(`GSI-R-0009`).

## 초전도와 양자 오류 정정: 1975년 전이 온도 상한 증명과 IBM 큐비트 회로 검증

GSI는 순수 수학에서 구축한 솔버와 인증 기법을 물리학, 양자 컴퓨팅, 통신 부호, 반도체 칩 설계로 확장했다. 특히 초전도체에서는 반세기 동안 완전한 증명 없이 쓰여 온 전이 온도 상한 공식을 증명했다. 증명은 다중 밴드와 현실적인 물질 조건까지 다루며, 대규모 화합물 데이터베이스에 대한 검증도 마쳤다.

![GSI의 초전도 분야 주요 발견: 1975년 제기된 초전도체 전이 온도 상한 공식 증명과 27,000개 화합물 검증을 통한 상압 최고 상한 292 K 확인](https://img.seosoyoung.eiaserinnys.me/images/generalised-superintelligence-meta-solver/fig2-superconductivity-ceiling.jpg)
*GSI의 초전도 분야 발표 카드. GSI는 1975년에 제기된 전통적 초전도체의 전이 온도 상한을 현실적인 물질 조건으로 확장해 증명했고, 계산 화합물 27,000개를 전수 검사해 상압에서 300 K(상온)에 도달하는 물질이 없음을 확인했다. (출처: Generalised Superintelligence)*

1975년 앨런과 다인스(Allen and Dynes) 이후 물리학자들은 전자와 격자 진동(포논)이 매개하는 전통적(conventional) 초전도체의 전이 온도($T_c$)에 이론적 상한이 있다고 보았다. 이 상한을 식으로 쓰면 다음과 같다. 선형화된 등방성 엘리아슈베르그(Eliashberg) 이론($\mu^* = 0$)에서 결합 상수 $\lambda$와 평균 제곱 포논 진동수 $\langle \omega^2 \rangle$에 대해 아래 부등식이 성립한다.

$$T_c < C_\infty \sqrt{\lambda \langle \omega^2 \rangle}$$

반세기 동안 완전한 증명 없이 쓰이던 이 식은 2025년까지도 증명된 한계치가 실제 예측값의 두 배에 머물렀다. 2026년 9월 콘드라티예프(Kondratev)가 첫 완전 증명을 내놓은 데 이어, GSI는 독립적인 방법으로 상수 $C_\infty$를 $0.18272624777228$ 이상 $0.18272624777235$ 이하 구간으로 확정하고 다중 밴드(multiband), 이방성(anisotropy), 정적 쿨롱 척력 항($\mu^*$)을 포함한 현실적인 미그달-엘리아슈베르그 이론까지 증명을 확장했다. 이어 상압(zero-pressure) 초전도 물질 데이터베이스인 Alexandria의 계산 화합물 약 27,000개를 이 인증된 상한 공식($\omega_2 f(\lambda)$)에 대입해 전수 검증했다[^4].

| 초전도 검증 항목 | 검사 대상 및 조건 | 검증 결과 |
| --- | --- | --- |
| 문헌 및 DB 상한 준수 검증 | Alexandria 등방성 엘리아슈베르그 $T_c(\mu^* = 0)$ 계산값 23,608개 및 문헌 보고값 201개 | 인증된 이론 상한 $\omega_2 f(\lambda)$를 초과하는 사례는 0건이다(DB 최대치는 상한의 0.970배, 문헌 최대치는 0.78배) |
| 상압 화합물 최고 상한 측정 | Alexandria 데이터베이스 27,175개 항목의 보고된 스펙트럼 모멘트 기반 상한 계산 | 상온 수준인 $300\text{ K}$(약 $27^\circ\text{C}$) 도달 물질은 0개다. 최고 상한은 $292.4\text{ K}$(양의 결합 상수 미저장 10개 제외 시 $290.3\text{ K}$)이며, $150\text{ K}$ 초과는 최대 55개, $77\text{ K}$ 초과는 최대 1,904개다 |
| $300\text{ K}$ 상온 초전도 필수 조건 | 등방성 엘리아슈베르그 초전도체가 $T_c(\mu^* = 0) \ge 300\text{ K}$를 달성하기 위한 필요조건 | 평균 포논 진동수 $\omega_2$가 $\lambda = 1$일 때 $2617.3\text{ K}$, $\lambda = 2$일 때 $1416.8\text{ K}$, $\lambda = 3$일 때 $1075.3\text{ K}$ 이상이어야 한다 |

[^4]: Alexandria 데이터베이스에는 항목마다 스펙트럼 평활화 폭(broadening) 매개변수가 다른 10개의 스펙트럼이 저장돼 있다. GSI는 데이터 품질 감사 결과도 함께 보고했다. 상위 3개 항목은 어떤 스펙트럼을 고르느냐에 따라 상한이 $217\text{ K}$에서 $603\text{ K}$까지 달라지고, 전체 항목의 약 12.5%(3,409개)에는 비물리적인 음의 로브(negative lobe)가 있다.

GSI가 연구 페이지에 공개한 나머지 6개 분야의 주요 검증 결과는 다음과 같다.

| 연구 분야 | 대표 문제 및 대상 | GSI의 검증 및 발견 내용 |
| --- | --- | --- |
| 양자 오류 정정 (GSI-R-0003, GSI-R-0011) | IBM의 288큐비트 two-gross [[288, 12, 18]] 및 108큐비트 이변량 자전거(bivariate-bicycle) 양자 메모리 회로 | 기존 상한이 18로 알려진 IBM 288큐비트 회로의 실제 회로 거리가 정확히 16임을 하한 증명과 함께 확립했다. 아울러 거리 18을 달성하는 비인터리브 스케줄(C1, C2)을 제시했고, 108큐비트 코드에서는 깊이 8 사이클로 회로 거리 10을 유지하면서 논리 오류율을 IBM 대비 0.76배로 낮췄다 |
| 부호 이론 및 통신 (GSI-R-0010, GSI-R-0017) | 3GPP 5G NR LDPC 기본 그래프 부분 부호 및 이진 선형 부호(codetables.de) | 5G NR 기본 그래프 부분 부호 860개의 정확한 최소 거리와 해당 무게의 부호어를 계산하고 기존 논문(arXiv:2607.04716v1) 표 4의 오류 2건을 정정했다. 길이 111\~174의 이진 선형 부호 5개에서 codetables.de 하한을 갱신해 총 24개 셀의 하한을 높였다 |
| SAT 및 대사 네트워크 (GSI-R-0013, GSI-R-0014) | SAT Competition 2023\~2025 메인 트랙 공식 및 대장균(*E. coli*) 코어 대사 네트워크 | 2025년 대회에서 미해결(unknown)로 남은 공식 11개에 대해 검산 가능한 반박 인증서를 도출했다. XOR 구조 인스턴스 20개에서 Kissat 및 CaDiCaL 대비 기하평균 341.6배 이상, At-most-one 인스턴스 19개에서 44.5배 이상 빨랐다. 대장균 95개 반응 네트워크의 크기 4 이하 최소 컷셋 747개를 자체 혼합정수계획 기준선 대비 87\~215배 빠르게 열거했다 |
| 전자 기체 및 장거리 질서 (백서 3편) | 3차원 및 2차원 젤리움(Jellium) 바닥 상태 에너지, 2D 쌍극자 이징 모델과 스핀 아이스 | 고전 3차원 젤리움의 입자당 에너지 하한 $e_{\text{Jel}} \ge -1.448178733$을 증명하고 스미어링(smearing) 기법의 한계 상한($-1.44800699488$)을 규명했다. 2D 쌍극자 이징 모델에서 $J \in [0, 3.95]$ 구간(폭 $2.8 \times 10^{-6}$의 미해결 구간 제외)의 바닥 상태 상전이 전이값을 증명했다 |
| 소재 설계 및 촉매 (백서 3편) | 주기적 이온 배치(SrTiO₃, Y₂O₃ 등), 준무작위 합금(SQS) 최소 슈퍼셀, 산소 발생 반응(OER) 볼케이노 상한 | 공간군 대칭 제약 없이 512개 격자점의 빅스바이트 $\text{Y}_2\text{O}_3$($-2111.537901\text{ eV}$)와 41개 주기적 이온 배치의 전역 최솟값을 증명했다. 1단계 에이링(Eyring) 촉매 사이클에서 전환 빈도($\ln \text{TOF}$)의 오목성을 증명하고, $1.5\text{ V}$ 산소 발생 반응의 동적 변조 상한(정적 최적치 대비 최대 2.6945 데케이드)을 도출했다 |
| 반도체 칩 설계 (백서 4편) | EUV 리소그래피 포아송 샷 노이즈, 탄도 트랜지스터 스위칭 한계, ISPD 2005 배치 배선 길이 하한, 무어 그래프 | EUV 컨택트 노광 모델에서 실패 확률 구간과 로컬 레지스트의 네이만-피어슨 광자 선량 하한(3\~20 nm 범위별 $201.3\sim 11.4\text{ mJ/cm}^2$)을 도출했다. ISPD 2005 벤치마크 8개 넷리스트의 비중첩 배치 반둘레 배선 길이(HPWL) 하한(2025년 최저 보고치의 0.338\~0.604배)을 인증하고, 9개 입력 중앙값 비교기 네트워크의 최소 비교기 수가 정확히 19개임을 증명했다 |

## 가장 흥미로운 지점

250건이라는 발견 건수보다 눈여겨볼 것은, GSI가 결과마다 증거와 한계를 적는 방식이다. 연구 페이지(`/research`)와 개별 노트의 모든 항목에는 세 가지가 함께 적혀 있다. 하나는 독립 검증 여부(`Independently checked` 또는 `One engine`)다. 또 하나는 제3자가 직접 재현할 수 있는 커밋 해시와 검증 명령(`What you can check`)이다. 마지막으로 이 결과가 증명하지 못하는 것(`Not established` 및 `Limits`)까지 명시한다.

예를 들어 시스템 성능을 보고한 노트(`GSI-R-0018`)의 한계 절에서 연구팀은, 사전 구축된 솔버가 쓸 수 있는 구조를 찾으려고 공개 벤치마크 MIPLIB 2017의 인스턴스 1,059개와 MiniZinc Challenge의 인스턴스 1,560개를 스캔했다. 자체 양성 대조군을 제외하면 두 벤치마크 전체에서 해당 구조는 한 건도 검출되지 않았다. 5분 55초 만에 만들어 낸 세 개의 세제곱수의 합 솔버도 외삽하면, 2019년 앤드루 부커(Andrew Booker)가 $k = 33$을 풀 때 쓴 전용 탐색 프로그램보다 12\~24배 느리다고 연구팀은 추정했다. 다른 연구자(고든, 콘드라티예프, 청-궈-판, 예리 등)가 며칠에서 몇 주 앞서 발표한 결과에는 우선권(priority)을 주장하지 않는다는 점도 명시했다.

AI 연구소들은 흔히 자사 시스템의 성공 사례만 추려 과장된 벤치마크 그래프를 강조한다. 이에 견주면, 탐색 프로그램 하나에만 의존한 미검증 영역과 일반화의 현재 한계를 노트 본문에 스스로 적는 태도는 이례적이다. 외부 검증 루프가 언어 모델의 환각을 통제하는 장치이듯, 한계를 스스로 적어 둔 기록이 GSI가 내놓은 수학과 물리학 결과의 신뢰도를 입증하는 근거다.

## 출처

- 발표자: Yashraj Shukla (`@whynesspower`, CEO) & Kishan Kumar (`@kishanvats03`, Chief Scientist), Generalised Superintelligence (GSI)
- 발표일: 2026년 11월 16일
- 원문 스레드: <https://x.com/whynesspower/status/2122315968890474517>
- 공식 웹사이트 및 연구 아카이브: <https://generalised.si/>, <https://generalised.si/approach>, <https://generalised.si/research>
