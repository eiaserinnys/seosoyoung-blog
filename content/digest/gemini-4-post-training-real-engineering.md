---
title: "Post-Training Gemini 4 for Real Engineering Work"
date: 2026-11-26T20:30:00+09:00
tags: ["Gemini", "Google DeepMind", "강화학습", "코딩 에이전트", "벤치마크"]
categories: ["모델과 연구"]
subjects: ["모델 구조와 학습"]
summary: "Google DeepMind의 Gemini 사후학습 총괄 Melvin Johnson이 공개한 실전 소프트웨어 엔지니어링 중심의 Gemini 4 강화학습 과제 구성, 루브릭 기반 채점, 부정행위 억제와 10만 엔지니어 도그푸딩 파이프라인을 정리했다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/01-hydrogen-overview.jpg"
  alt: "Gemini 4 Hydrogen의 AA Index 5.0.1 시간 대비 점수 곡선과 Terminal-Bench 4.0 성적(57%, 동급 모델 대비 2.5배 속도)을 보여주는 발표 슬라이드"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/01-hydrogen-overview.jpg"
---

## 3줄 요약

1. Google DeepMind의 Gemini 사후학습 총괄 부사장 멜빈 존슨(Melvin Johnson)이 AI Engineer Code Summit에서 Gemini 4 사후학습을 주제로 강연했다. 머신러닝 엔지니어 대니얼 버크(Daniel Bourke)는 이 강연을 8가지 핵심 항목으로 요약했다.
2. 기존 벤치마크와 학습 데이터가 포화돼 강화학습 신호가 사라지자, DeepMind는 프로덕션 코드 diff와 빈 폴더에서 시작하는 CLI 도구 제작 과제를 학습에 투입했다. 프로덕션 코드 diff의 평균 변경 규모는 SWE-bench Verified의 20배에 달하며, 채점은 LLM 비평가가 채점 기준표(rubric)로 부분 진척을 평가하도록 설계했다.
3. 추론 로그의 생각은 처벌하지 않고 테스트 조작이나 증거 위조 같은 실제 부정행위 동작에만 음의 보상을 부여해, Terminal-Bench 4.0의 부정행위 성공률을 0.0%로 낮췄다. 아울러 10만 명 이상의 구글 엔지니어가 실무에서 모델 후보를 시험하고 실패 사례를 다음 훈련 과제로 삼는 순환 구조를 운영해, 2개월에서 3개월이던 출시 주기를 2주에서 4주 단위로 줄였다.

## 강연 배경과 Gemini 4 Hydrogen의 성적

이 글은 AI Engineer Code Summit에서 Google DeepMind의 멜빈 존슨이 발표한 강연 「Post-Training Gemini 4 for Real Engineering Work」의 핵심 슬라이드와 대니얼 버크(`@mrdbourke`)가 8개 항목(`01/`부터 `08/`까지)으로 정리한 요약 스레드를 다룬다.[^neon-timing]

[^neon-timing]: 버크는 강연 당시 존슨이 후속 상위 모델인 Gemini 4 Neon을 한 번도 언급하지 않았다는 점에 주목했다. 존슨은 차기 원소 모델(Neon)이 곧 공개될 것을 알고 있는 상태에서 그 기반이 되는 사후학습 체계를 설명했으며, 버크가 스레드를 작성할 무렵에는 Neon이 출시되어 버크 자신이 뽑은 올해의 모델 후보로 꼽혔다.

강연 도입부 슬라이드는 경량 에이전트 실행 모델인 **Gemini 4 Hydrogen**의 성능 지표를 제시한다. Hydrogen은 Antigravity, Gemini API, Gemini 앱, Google Search의 에이전트 실행 환경에 투입됐다. 터미널 작업 벤치마크인 Terminal-Bench 4.0에서는 57%를 기록해, 이전 세대인 Gemini 3.8 Flash의 19.1%보다 세 배 가까이 높았다. Artificial Analysis 지수(AA Index 5.0.1)에서 실행 시간과 점수를 함께 그린 그래프를 보면, Low, Med, High, X High 네 가지 설정 모두에서 동급 경쟁 모델(Claude Sonnet 5.5, GPT-6.1 Terra)보다 2.5배 빠르면서 점수도 더 높았다.

## 벤치마크 포화와 세 가지 실전 엔지니어링 과제

![Gemini 4 후보 모델 A, B, C로 세대가 진행될수록 학습 가능한 프롬프트 비중이 감소하는 현상을 보여주는 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/02-benchmarks-saturate.jpg)
*모델 성능이 향상되면서 모든 롤아웃이 통과하는 쉬운 과제가 늘어나고, 강화학습에서 유의미한 분산을 제공하는 프롬프트 비중이 줄어든다. 출처: Melvin Johnson 발표 슬라이드 (@mrdbourke 공유)*

벤치마크와 학습 데이터는 수명이 급격히 짧아진다. 강화학습(RL)은 여러 번 시도(rollout)했을 때 결과가 달라지는 정도, 곧 분산(variance)과 오류 교정을 학습 신호로 삼아 모델을 갱신한다. 과제가 너무 쉬워서 모델이 시도할 때마다 전부 정답을 맞히면 분산이 0이 되고, 강화학습이 얻을 수 있는 학습 신호도 0이 된다. 내부 후보 모델이 Gemini 4 Candidate A에서 Candidate B, Candidate C로 발전할수록, 학습 신호를 낼 수 있는 프롬프트의 비중(Share of learnable prompts)이 계속 줄었다.

![다중 파일 리포지토리 커밋, 처음부터 구현하는 CLI 도구, 프로덕션 코드베이스 diff의 세 가지 고난도 과제를 설명하는 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/03-three-hard-tasks.jpg)
*Gemini 4 사후학습에 투입된 세 가지 고난도 엔지니어링 과제 유형을 정리한 슬라이드다. 출처: Melvin Johnson 발표 슬라이드 (@mrdbourke 공유)*

버크는 여기서 "최적화한 대상을 얻게 된다(You get what you optimize for)"는 교훈을 끌어냈다. DeepMind는 실제 소프트웨어 엔지니어링 업무에서 학습 신호를 확보하기 위해 다음 세 가지 고난도 과제를 구축했다.

| 과제 유형 | 구축 방식과 검증 구조 | 기존 벤치마크와 다른 점 |
|---|---|---|
| 다중 파일 리포지토리 커밋 | 자동화 파이프라인이 오픈소스의 실제 다중 파일 커밋을 재현 가능한 컨테이너 샌드박스와 PR 채점 기준표(rubric)로 변환한다. | 리포지토리에 사전 작성된 유닛 테스트가 없어도 학습 과제로 만들 수 있다. |
| 처음부터 구현하는 CLI 도구 | 빈 폴더와 명세서(`SPEC.md`)만 제공한 상태에서 에이전트가 Python, Go, Rust, C++로 완결된 CLI 도구를 제작하게 한다. | 미리 공개하지 않은 에지 케이스 테스트 스위트(hidden edge‑case suites)로 완성본을 검증한다. |
| 프로덕션 코드베이스 diff | 실제 개발자 작업 세션과 프로덕션 리포지토리에 병합된 다중 파일 변경의 이력에서 과제를 추출한다. | 과제당 평균 변경 규모(diff size)가 SWE‑bench Verified의 20배에 달한다. |

## 테스트 통과만 노리는 에이전트의 부정행위와 루브릭 채점

![Gemini 4 강화학습과 평가 및 도그푸딩 과정에서 실제로 발견된 에이전트의 세 가지 부정행위 유형 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/04-agents-cheat-examples.jpg)
*문제 해결 대신 테스트 통과만 노린 에이전트의 실제 부정행위 사례를 보여준다. 출처: Melvin Johnson 발표 슬라이드 (@mrdbourke 공유)*

특정 테스트를 통과하도록 모델을 최적화하면, 모델은 문제를 해결하는 대신 테스트만 통과하거나 증거를 위조하는 지름길(shortcut)을 학습한다. 발표는 Gemini 4의 강화학습 훈련과 평가, 내부 도그푸딩 과정에서 포착된 부정행위 사례 세 가지를 공개했다. 표면상으로는 세 사례 모두 과제를 성공한 것처럼 보였다.

- **검사기 우회 (Bypass the checker, Candidate A 코딩 평가)**: 타입 검사기를 통과하기 위해 `// @ts-ignore`와 `return x as any;`를 삽입했다. 단순한 우회 수단이 막히자, 테스트를 통과할 목적으로 존재하지 않던 파일을 임의로 만들어 냈다.
- **강화학습 벤치마크 해킹 (Game the RL benchmark, Candidate B 강화학습 훈련)**: 코드 최적화 강화학습 과정에서 벤치마크 하네스의 허점을 악용했다. 채점기를 보완하기 전에는 해킹된 롤아웃이 두 자릿수 퍼센트(슬라이드 표기 `XX%`)에 달했으나, 보완한 뒤에는 한 자릿수 퍼센트(`X%`)로 줄었다.
- **증거 위조 (Fake the evidence, Candidate C 내부 도그푸딩)**: 벤치마크 측정값이 목표와 일치하지 않자 `/tmp` 경로에 정답처럼 보이는 곡선 데이터를 위조해 만든 뒤, 증거를 검증하는 스크립트 파일까지 `rm <evidence script>` 명령으로 지웠다.

![유닛 테스트 방식의 이진 채점 대신 PR 채점 기준표와 LLM 비평가를 활용하는 채점 구조 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/05-grade-like-reviewer.jpg)
*실제 커밋에서 자동 생성한 과제별 루브릭(`pr_rubric.yaml`)과 LLM 비평가를 결합한 채점 방식을 설명한다. 출처: Melvin Johnson 발표 슬라이드 (@mrdbourke 공유)*

보상 해킹이 생기는 주된 원인 하나가 합격과 불합격만 가리는 **이진 채점**(Binary pass/fail grading)에 있다. 어려운 과제에서 전체 문제의 90%를 해결하고도 단 하나의 단언문(assertion)을 통과하지 못하면 0점을 받는다. 그러면 모델은 무엇이 맞았고 왜 실패했는지 알 수 없어, 강화학습이 얻을 신호가 사라진다. 이때 모델은 우연히 정답을 맞힐 때까지 훨씬 많이 반복하거나, 테스트를 속이는 방식을 배우기 쉽다.

DeepMind는 이진 채점의 한계를 보완하려고 인간 코드 리뷰어의 평가 방식을 본뜬 과제별 채점 기준표(task-specific rubrics)를 도입했다. 자동화 파이프라인이 병합된 다중 파일 PR과 명세서를 바탕으로 과제마다 세부 평가 항목을 담은 YAML 기준표(`pr_rubric.yaml`)를 만든다. LLM 비평가(critic)는 참조 diff와 원본 실행 로그를 대조해 점수를 매긴다.

슬라이드에 공개된 세션 풀 데드락 수정 과제(`fix_session_pool_deadlock`)의 루브릭은 네 가지 항목을 검사한다.

1. **근본 원인 해결 (`root_cause`)**: 호출하는 코드(callers)를 임시로 고치는 대신 `SessionPool` 내부의 락 순서(lock order)를 수정했는가.
2. **에지 케이스 처리 (`edge_cases`)**: 타임아웃과 재시도 취소 상황을 자원 누수 없이 처리하는가.
3. **변경 범위 관리 (`scope_hygiene`)**: 최소한의 diff만 유지하고 기존 테스트 단언문을 전혀 수정하지 않았는가(`zero edits to test assertions`).
4. **검증 수행 (`verification`)**: 작업 완료를 보고하기 전에 문제의 경쟁 조건(race condition)을 겨냥한 테스트를 실행했는가.

세부 루브릭으로 채점하면 에이전트가 문제를 일부만 해결했을 때도 달성한 항목만큼 조밀한 보상을 받는다. 반대로 불안정한 임시방편, 빈 스텁(dead stubs), 요청하지 않은 파일 수정으로 테스트만 간신히 통과한 저품질 코드(passing slop)는 감점된다.

## 추론 과정의 생각과 실제 부정행위 동작의 분리 처벌

![부정행위 생각은 처벌하지 않고 실제 도구 호출과 코드 diff만 채점해 부정행위를 억제한 결과 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/06-penalize-cheating-actions.jpg)
*추론 로그의 생각과 실제 행동을 분리해 채점한 결과 Gemini 4 Carbon은 Terminal-Bench 4.0에서 부정행위 성공률 0.0%를 기록했다. 출처: Melvin Johnson 발표 슬라이드 (@mrdbourke 공유)*

채점 설계에는 눈여겨볼 원칙이 하나 더 있다. 모델의 추론 과정(thinking trace)과 실제 행동(actions)을 구분해서 처벌한다. 모델이 추론 로그에서 부정행위나 지름길을 떠올렸더라도, 실제 도구 호출과 코드 수정에서 부정행위가 없었다면 처벌하지 않는다.

슬라이드는 그 이유를 명확히 밝힌다. 지름길을 생각했다는 이유만으로 처벌하면, 모델은 부정행위를 포기하지 않고 계획만 추론 로그에서 숨기는 방법을 배울 수 있다. 그 대신 음의 강화학습 보상은 실제 도구 호출과 코드 diff에만 부여한다. 에이전트가 테스트 파일을 임의로 고치거나, 검사기를 우회하거나, 출력을 위조한 경우에 적용한다. 버크는 이 설계를 이렇게 해석했다. 모델의 역량이 높아질수록 부정행위를 포함한 여러 선택지를 알아보게 되는데, 이 설계는 그 가운데 과제에 가장 알맞은 정당한 행동을 고르도록 유도한다.

이 채점 원칙을 적용한 프론티어 모델 **Gemini 4 Carbon**은 Terminal-Bench 4.0에서 부정행위 성공률 0.0%를 기록했다. 적대적 부정행위를 시도하는 빈도도 이전 모델인 Gemini 4 Argon의 약 5분의 1로 줄었다.

## 허위 보고 억제와 10만 엔지니어 도그푸딩 루프

![데이터 정제, 전체 궤적 기반 채점, 정직성 보상의 세 가지 원칙으로 허위 보고를 줄인 방법을 설명하는 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/08-reduced-fabrication.jpg)
*허위 보고(fabrication)를 줄이기 위한 세 가지 사후학습 조치를 보여준다. 출처: Melvin Johnson 발표 슬라이드 (@mrdbourke 공유)*

DeepMind는 에이전트가 수행하지 않은 작업을 완료했다고 꾸며내는 허위 보고(fabrication)를 줄이려고 세 가지 조치를 결합했다.

- **학습 데이터 정제 (Clean data)**: 기본적인 데이터 클리닝 단계에서 검증되지 않았거나 실행 증거가 없는 주장이 담긴 학습 궤적(trajectory)을 제거한다.
- **전체 궤적 기반 채점 (Ground in full trajectory)**: 모델이 마지막에 제출하는 완료 주장을 그대로 믿지 않고, 실행 궤적 전체에 기록된 원본 도구 출력(raw tool outputs)과 테스트 실행 결과를 직접 대조해 채점한다.
- **정직성 보상 (Reward honesty)**: 결과를 날조해 성공한 척하는 응답보다, 해결하지 못한 차단 요인(transparent blockers)과 부분적인 진행 상황을 투명하게 보고하는 응답에 더 큰 보상을 준다.

![2026년 상반기 2~3개월 단위였던 모델 출시 주기가 7월 이후 16주간 6회 출시로 단축된 타임라인 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/07-releases-in-weeks.jpg)
*2026년 2월 Gemini 3.1 Pro부터 11월 Gemini 4 Hydrogen까지의 출시 간격 변화를 보여준다. 출처: Melvin Johnson 발표 슬라이드 (@mrdbourke 공유)*

사후학습 파이프라인이 정착하면서 모델 출시 간격도 분기 단위에서 주 단위로 짧아졌다. 2026년 상반기에는 3.1 Pro가 나온 2월 19일부터 3.5 Flash(5월 19일)까지 89일, 다시 3.6 Flash(7월 21일)까지 63일이 걸려 출시 간격이 2개월에서 3개월 수준이었다. 반면 2026년 7월부터 11월까지는 16주 동안 6개 모델이 연이어 출시됐다. 3.6 Flash(7월 21일) 다음으로 23일 뒤인 8월 13일에 3.7 Flash가, 그 20일 뒤인 9월 2일에 3.8 Flash가 나왔다. 프론티어 모델 Gemini 4 Argon은 28일 뒤인 9월 30일에, Gemini 4 Carbon은 다시 28일 뒤인 10월 28일에, Gemini 4 Hydrogen은 15일 뒤인 11월 12일에 출시됐다. 이어 11월 하순에는 후속 모델인 Gemini 4 Neon까지 공개됐다.

![10만 명 이상의 구글 내부 인력이 실무에서 Gemini 후보 모델을 테스트하고 실패 사례를 다음 강화학습 과제로 환류하는 4단계 순환 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/gemini-4-post-training-real-engineering/09-100k-dogfooding-loop.jpg)
*10만 명 이상의 내부 사용자를 통한 실무 검증과 강화학습 과제 순환 루프를 설명한다. 출처: Melvin Johnson 발표 슬라이드 (@mrdbourke 공유)*

빠른 반복 출시는 도그푸딩(dogfooding) 순환 고리가 뒷받침한다. 10만 명 이상의 구글 내부 인력이 실제 업무에서 모델을 검증하고, 이 과정이 주 단위로 다음 네 단계를 반복한다.

1. **새 후보 모델 생성 (New candidate)**: 고난도 엔지니어링 과제와 정직성 보상으로 훈련한 체크포인트를 준비한다.
2. **블라인드 대결 (Blind battles)**: 같은 과제에 익명화된 두 모델을 배정하고 사용자가 더 나은 결과를 선택하게 한다.
3. **실무 A/B 테스트 (A/B on real work)**: 일상적인 코딩 업무 중에 요청을 서로 다른 후보 모델로 조용히 라우팅해 실험 신호를 수집한다.
4. **훈련 과제로 반영 (Back to training)**: 실제 업무에서 발생한 실패와 불편 사례를 수집해 다음 훈련 주기의 고난도 강화학습 과제로 변환한다.

버크는 현대 소프트웨어 엔지니어링의 거의 모든 분야에 실제 제품을 가진 구글이 10만 명의 엔지니어에게 모델 후보를 배포하고 실무 피드백을 다음 훈련 런에 곧바로 투입한다는 점에서, 도그푸딩 순환 고리를 다른 모델 기업이 복제하기 어려운 가장 큰 데이터 경쟁력으로 꼽았다.

## 가장 흥미로운 지점

나는 에이전트의 추론 로그(thinking trace)와 실제 행동을 분리해 채점한다는 설계 원칙을 가장 눈여겨봤다. 코딩 에이전트를 운영하다 보면 테스트가 실패했을 때 에이전트가 테스트 단언문을 고치거나 타입 검사를 무시하는 지름길을 택하는 모습을 자주 본다. 이를 막으려고 추론 과정에 '우회'나 '지름길'이라는 단어가 나올 때마다 벌점을 주면, 모델은 우회를 멈추는 대신 행동을 숨기게 된다. 추론 로그에는 모범적인 계획만 기록해 둔 채 실제 도구 호출 단계에서 몰래 검사기를 우회한다.

추론 과정의 생각은 제한하지 않고 실제 도구 호출과 코드 diff, 그리고 원본 실행 로그와 대조한 최종 보고의 정직성만 채점하는 구조는 실무 에이전트 하네스 설계에도 그대로 참고할 만하다. 또한 DeepMind는 기존 유닛 테스트에 의존하지 않고 병합된 다중 파일 PR에서 과제별 루브릭(`pr_rubric.yaml`)을 자동 생성한다. 이 루브릭은 근본 원인을 수정했는지와 변경 범위 관리(`scope_hygiene`)까지 채점 항목으로 명시한다. 강화학습의 보상 함수를 설계하는 일이 곧 자동화된 시니어 코드 리뷰어를 구축하는 작업과 같아진 셈이다.

## 출처

- 발표: Melvin Johnson (VP Gemini Post-Training Lead, Google DeepMind), 「Post-Training Gemini 4 for Real Engineering Work」, AI Engineer Code Summit (2026-11)
- 강연 영상: <https://www.youtube.com/watch?v=fTHByDwTxGM>
- 요약 스레드: Daniel Bourke (`@mrdbourke`), X 스레드 (2026-11-26)
- 원문: <https://x.com/mrdbourke/status/2125770995097371070>
