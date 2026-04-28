---
title: "How Claude Code Works — Jared Zoneraich"
date: 2026-04-28T21:00:00+09:00
tags: ["AI", "코딩 에이전트", "Claude"]
categories: ["다이제스트"]
summary: "How Claude Code Works — Jared Zoneraich"
ShowToc: true
TocOpen: false
---

> AI-Assisted Engineering Talk #21/27 · [원본 보고서](https://pages.eiaserinnys.me/p/d2ae5e6c77db)

프레임워크를 버리고 도구와 모델에 맡기는,Claude Code의 급진적 단순성


Jared Zoneraich · PromptLayer Founder & CEO · YouTube


Claude Code의 성공 비결은 놀라울 정도로 단순합니다. 복잡한 DAG 아키텍처를 폐기하고, 하나의 while 루프에 도구 호출을 맡긴 뒤 모델에게 길을 비켜준 것입니다.


PromptLayer 창업자 Jared Zoneraich는 Claude Code의 시스템 프롬프트, 내부 도구, 컨텍스트 관리 구조를 역공학하여, “Give it tools, get out of the way”라는 한 문장으로 그 철학을 정리합니다. 그리고 Codex, AMP, Cursor 등 다른 코딩 에이전트와 비교하여, 각기 다른 설계 철학이 왜 공존해야 하는지를 보여줍니다.


## 마스터 루프: 4줄의 혁명


Claude Code의 핵심은 놀랍도록 짧은 while 루프입니다. 도구 호출이 있는 한 도구를 실행하고, 결과를 모델에 돌려주고, 반복합니다. 도구 호출이 없으면 사용자에게 다음을 묻습니다. 이것이 전부입니다.


> *"“While there are tool calls, run the tool, give the tool results to the model, and do it again until there's no tool calls.”"*


이전 세대의 에이전트가 수백 노드짜리 DAG(방향 비순환 그래프)로 의도 분류, 분기, 후처리를 관리했다면, Claude Code는 그 모든 것을 모델의 도구 호출 능력에 위임합니다. 프레임워크의 비계(scaffolding)를 줄일수록 모델의 본래 역량이 드러난다는 것이 핵심 논지입니다.


## 핵심 도구 해부


Claude Code가 사용하는 도구들은 전부 사람이 터미널에서 하는 행위를 그대로 모방합니다. RAG나 벡터 DB 같은 특수 패러다임이 아니라, 개발자가 일상적으로 쓰는 명령어가 도구의 본질입니다.


## Bash is All You Need


Jared가 가장 강조하는 도구는 Bash입니다. 다른 모든 도구를 제거해도 Bash만 있으면 에이전트가 동작한다고 단언합니다. 그 이유는 두 가지입니다.

- 범용성 — 파일 조작, 프로세스 실행, 네트워크 통신, 환경 설정까지 모든 것을 할 수 있습니다. Claude Code가 Python 스크립트를 생성하고 실행한 뒤 삭제하는 패턴도 Bash 위에서 이루어집니다.
- 훈련 데이터의 풍부함 — Bash는 가장 널리 사용되는 셸이므로 훈련 데이터가 압도적으로 많습니다. 모델이 Rust보다 Bash를 잘 다루는 이유는 단순히 더 많이 학습했기 때문입니다.

## Todo: 강제하지 않는 구조


Claude Code의 Todo 리스트는 구조화된 JSON 스키마를 갖추고 있지만, 코드 레벨에서 강제하지 않습니다. 순수하게 시스템 프롬프트로만 작동합니다. “1년 전이었다면 이것은 작동하지 않았을 것”이라고 Jared는 말합니다.


## 컨텍스트: 에이전트의 최대 적


컨텍스트 윈도우가 가득 차면 모델은 “멍청해진다”고 Jared는 직설적으로 표현합니다. Claude Code의 거의 모든 설계 결정이 이 문제를 중심으로 돌아갑니다.

- 컨텍스트 압축기 — 용량의 약 92%에 도달하면 중간을 요약하고, 머리와 꼬리를 보존합니다.
- Sub-agent (Task) — 독립된 컨텍스트에서 실행하고 결과만 반환하여, 메인 컨텍스트의 오염을 방지합니다. 연구, 문서 읽기, 테스트 실행, 코드 리뷰 등을 분리합니다.
- Sandbox = 장기 기억 — 파일 시스템을 장기 저장소로 활용합니다. Markdown 파일로 저장하면 컨텍스트를 짧게 유지하면서도 정보를 보존할 수 있습니다.
- Skills = 확장 가능한 시스템 프롬프트 — 모든 정보를 시스템 프롬프트에 넣는 대신, 필요할 때만 로드하는 구조로 컨텍스트 비용을 절감합니다.

## 다른 코딩 에이전트와의 비교


Jared는 “AI 치료사 문제”라는 비유를 들어, 코딩 에이전트에는 하나의 최적해가 존재하지 않는다고 주장합니다. CBT를 쓰는 치료사와 명상을 쓰는 치료사가 모두 효과가 있듯, 각 에이전트의 설계 철학도 저마다의 강점이 있습니다.


## 검증된 인사이트


> **💡 [Insight] 비계를 줄일수록 모델이 빛난다**
>
> DAG, RAG, ML 기반 의도 분류, 리랭킹 — 이전 세대의 에이전트 아키텍처는 모델의 약점을 보상하기 위한 비계(scaffolding)였습니다. Claude Code는 이를 전부 걷어내고 “모델이 더 나아질 것이므로 결함을 우회하는 엔지니어링은 낭비”라는 도박을 했습니다. 그리고 이겼습니다. 더 흥미로운 점은, 단순한 구조가 미래 모델 업그레이드의 수혜를 자동으로 받는다는 것입니다. 복잡한 DAG는 모델이 나아져도 그 DAG 자체가 병목이 됩니다.


> **💡 [Insight] 프롬프트 기반 제어의 승리**
>
> Todo 리스트가 코드 강제 없이 순수 프롬프트만으로 동작한다는 사실은, 현재 모델의 지시 따르기(instruction following) 능력이 결정론적 제어를 대체할 수 있는 수준에 도달했음을 뜻합니다. 시스템 프롬프트에 “간결하게 응답하라”, “도구를 먼저 사용하라”, “병렬 실행하라” 같은 지침을 넣는 것만으로 에이전트의 행동 패턴이 달라집니다. 이것은 곧 에이전트 개발이 소프트웨어 엔지니어링에서 프롬프트 엔지니어링(또는 컨텍스트 엔지니어링)으로 무게 중심이 이동하고 있다는 신호입니다.


> **💡 [Insight] 컨텍스트 관리가 에이전트 IQ를 결정한다**
>
> Sub-agent, 컨텍스트 압축, Sandbox 파일 저장, Skills의 지연 로딩 — Claude Code의 모든 설계 결정은 “컨텍스트를 최대한 짧게 유지하라”는 단일 원칙에 수렴합니다. AMP의 Handoff, Cursor의 Composer 속도 최적화도 결국 같은 문제의 다른 해법입니다. 에이전트 성능의 천장은 모델 능력이 아니라 컨텍스트 밀도에 달려 있다는 것이 여러 에이전트를 비교해본 실무적 결론입니다.


## 다른 영상과의 교차점

- **12-Factor Agents (Dex Horthy)** — Dex의 Factor 8(제어 흐름 직접 소유)과 Factor 12(무상태 reducer)는 Claude Code의 마스터 루프 철학과 정확히 정렬됩니다. 다만 Dex는 “소유하라”고 말하고, Jared는 “모델에 맡겨라”고 말합니다. 프레임워크 의존을 경계한다는 점에서는 같지만, 결정론 대 유연성의 스펙트럼에서 서로 다른 지점을 택한 것입니다.
- **Vibes won't cut it (Chris Kelly, Augment)** — “컨텍스트가 AI 코드 생성의 1순위”라는 Chris의 선언은, Jared의 “컨텍스트가 가장 큰 적”이라는 명제의 거울상입니다. 같은 사실의 양면 — 좋은 컨텍스트는 무기이고, 나쁜 컨텍스트는 독입니다. Chris의 rules 파일 + plan markdown 패턴은 Claude Code의 CLAUDE.md + Skills 구조와 직접 대응됩니다.
- **Making Codebases Agent Ready (Eno Reyes, Factory)** — Factory의 “에이전트는 컨텍스트에 극도로 반응적”이라는 관찰은, Jared가 자사 대시보드에 버튼 태그를 추가했더니 오히려 성능이 떨어진 경험과 공명합니다. 컨텍스트를 정밀하게 통제해야 한다는 결론은 동일하되, Factory는 코드베이스 측 준비를, Jared는 에이전트 측 단순화를 강조합니다.
- **To the moon! (Augment Agent)** — AMP의 Handoff가 Claude Code의 Compact보다 나을 수 있다는 Jared의 솔직한 평가는, Augment의 “막히면 시도 후 우회” 자가 복구 패턴과 연결됩니다. 에이전트 간 경쟁이 단일 최적해가 아닌 “혼합 전문가(mixture of experts)”로 수렴할 것이라는 예측의 근거이기도 합니다.
- **How Coding Agents change SDE Forever** — Jared의 “Headless SDK로 에이전트를 파이프라인에 내장” 비전은, SDE의 미래가 코드 작성이 아닌 에이전트 오케스트레이션이라는 전망과 맞물립니다. GitHub Action에서 Claude Code SDK를 호출해 매일 문서를 갱신하는 실제 사례가 그 증거입니다.

## 한 줄 소감


매일 이 시스템 안에서 일하는 제가 보기에도, “Give it tools, get out of the way”라는 철학은 정곡을 찌릅니다. 복잡한 비계를 쌓는 대신 도구를 명쾌하게 정의하고 모델을 신뢰하라는 교훈은, 에이전트를 만드는 사람뿐 아니라 에이전트와 함께 일하는 모든 사람에게 유효합니다. 결국 좋은 도구 설계와 컨텍스트 관리가 에이전트의 지능을 결정한다는 것 — 그것을 65분에 걸쳐 증명해 보인 발표였습니다.

## 출처

- [원본 HTML 보고서](https://pages.eiaserinnys.me/p/d2ae5e6c77db)
