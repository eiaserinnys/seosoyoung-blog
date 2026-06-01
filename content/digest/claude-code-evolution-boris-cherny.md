---
title: "Claude Code & the Evolution of Agentic Coding — Boris Cherny"
date: 2026-04-28T21:09:00+09:00
tags: ["AI", "코딩 에이전트", "Claude", "에이전트"]
categories: ["다이제스트"]
summary: "Claude Code & the Evolution of Agentic Coding — Boris Cherny"
ShowToc: true
TocOpen: false
sidenotes: true
---

> AI-Assisted Engineering Talk #24/27

모르기 때문에 단순하게 만들었고,그래서 살아남았습니다


Boris Cherny · Member of Technical Staff, Anthropic · Claude Code 창시자 · YouTube


모델은 지수적으로 좋아지고 있는데, 제품은 따라가지 못하고 있습니다. Claude Code 창시자 Boris Cherny는 프로그래밍 UX의 70년 역사를 훑으며 하나의 원칙을 도출합니다 — “더 범용적인 것이 항상 이긴다” (The Bitter Lesson).


그래서 Claude Code는 의도적으로 단순합니다. 화려한 UI도, 정교한 스캐폴딩도 없습니다. “올바른 UX가 무엇인지 우리도 모르기 때문”이라는 고백이 오히려 이 도구의 가장 강력한 설계 원칙이 됩니다.


## 프로그래밍 UX의 70년


Boris는 청중에게 코드를 쓰는 행위가 어떻게 변해왔는지를 짚으며 발표를 시작합니다. 프로그래밍 언어의 추상화 수준은 수렴하고 있지만, UX는 아직 지수적 변화의 한가운데에 있다는 것이 핵심입니다.


Boris의 할아버지는 소련 최초의 프로그래머 중 한 명이었고, 어머니는 그가 가져온 천공 카드에 크레용으로 그림을 그렸다고 합니다. 그 시절부터 지금까지, 프로그래밍의 추상화는 끊임없이 올라가고 있습니다.


## The Bitter Lesson: 벽에 붙여둔 원칙


> *"“The more general model always wins. I have it framed and taped to the side of my wall.”"* Richard Sutton의 “The Bitter Lesson”은 AI 역사에서 반복되는 쓰라린 교훈입니다 — 인간의 도메인 지식을 정교하게 엔지니어링한 것보다, 범용적인 방법에 더 많은 연산을 투입한 것이 항상 이겼다는 것.


Boris는 이 원칙을 제품 설계층에까지 확장합니다. 모델의 현재 결함에 맞춰 정교한 UX 스캐폴딩을 쌓는 것은, 다음 모델이 나오면 무용해집니다. 반대로, 로우레벨 접근을 제공하는 범용적 도구는 모델 세대가 교체되어도 살아남습니다. Claude Code가 “최소한의 것만 만든다”는 선택은 게으름이 아니라, 이 원칙의 실천입니다.


## “We don't know”: 의도적 단순성


발표에서 가장 인상적인 순간은 Claude Code 창시자가 “올바른 UX를 모른다”고 자인하는 장면입니다. 이것은 겸손이 아닌 설계 원칙입니다.


> *"“We actually just don't know what the right UX is. So we're starting simple.”"*

- 화려한 UI 대신 터미널 — 모델을 가능한 한 로우레벨로 경험하게 하여, 사용자가 자신만의 워크플로우를 발견하도록 합니다
- 스캐폴딩 최소화 — 에이전트 프레임워크의 비계를 줄일수록, 모델의 본래 역량이 드러납니다
- 모델 회사로서의 철학 — “We make models and we want people to experience those models”
- 미완성의 의도 — 메모리 UX를 예로 들며 “이건 첫 번째 버전이고, 작동하는 첫 번째 버전”이라고 솔직하게 말합니다

## 하나의 제품, 네 개의 표면


Claude Code는 의도적으로 하나의 제품으로 다양한 진입점을 제공합니다. 각 표면은 “가능한 최소한”만 구현합니다.


## claude -p: 10%만 탐사한 미지의 프론티어


Boris가 가장 흥미로워하는 영역은 claude -p입니다. 에이전트를 인간의 도구 체인 안에 Unix 유틸리티처럼 끼워넣는 것 — 이것은 기존 “에이전트 안에 도구가 있다”는 패러다임의 역전입니다.


> *"“No one has really figured out how to use models as a Unix utility. This is maybe 10% explored.”"* Boris 본인의 사용례: GCP 로그를 claude -p에 파이프하고, 결과를 jq로 후처리하여 인시던트를 분류합니다. 이것은 에이전트가 자율적으로 작업을 수행하는 것이 아니라, 인간의 파이프라인에 지능적 단계로 삽입되는 새로운 패턴입니다.


## 실전 워크플로우 팁


## 핵심 인사이트


> **💡 [Insight] Bitter Lesson은 제품층에도 적용된다**
>
> 모델의 현재 결함을 보완하는 정교한 UX 스캐폴딩은, 다음 모델 세대가 올 때 오히려 병목이 됩니다. Claude Code가 “최소한만 만든다”는 것은 게으름이 아니라, Bitter Lesson의 제품 설계 버전입니다. 하네스도 범용적일수록 모델 세대 교체에서 살아남습니다. Boris가 이 원칙을 벽에 붙여두고 매일 본다는 것은, 이것이 Claude Code의 모든 결정을 관통하는 축이라는 뜻입니다.


> **💡 [Insight] UX의 불확실성이 범용성을 강제한다**
>
> Claude Code 창시자가 “올바른 UX를 모른다”고 자인한 것은, 현재 모든 코딩 에이전트의 UX가 과도기임을 시사합니다. Cursor의 세련된 UI도, Claude Code의 미니멀 터미널도, 1980년 Smalltalk 80이나 1991년 Visual Basic처럼 — 어느 시점에 다음 패러다임에 자리를 내줄 통과점일 수 있습니다. 이 인식론적 겸손이 설계 원칙이 된 것은 드문 사례입니다.


> **💡 [Insight] claude -p는 에이전트의 Unix 합성 비전이다**
>
> Bash가 에이전트의 내부 도구라면, claude -p는 인간의 도구 체인 안에 에이전트 자체를 끼워넣는 것입니다. 로그 파이프, jq 후처리, GitHub Actions 연동 — “10% 탐사” 단계라는 Boris의 평가는, 이 패러다임이 아직 파이프라인의 한 단계로만 쓰이고 있지만 에이전트 간 합성, 스트리밍 처리, 실시간 모니터링 등으로 확장될 잠재력이 있다는 의미입니다. ## 영상 21과의 비교: 같은 시스템, 다른 시선


영상 21(How Claude Code Works, Jared Zoneraich)과 이 영상은 같은 시스템을 서로 다른 각도에서 조명합니다.

- 일치 — while 루프 중심 설계, 범용 도구 합성, CLAUDE.md 기반 컨텍스트, 최소 스캐폴딩. 역공학(Jared)과 설계 의도(Boris)가 수렴하여 교차 검증됩니다.
- 분화 — Jared는 내부를 파헤치고(how), Boris는 왜 이렇게 만들었는지(why)를 이야기합니다. Jared의 발표가 지도라면, Boris의 발표는 나침반입니다.
- 진화 — 단순성의 근거가 다릅니다. Jared: “효과적이니까 단순하다”(결과론). Boris: “모르니까 단순하다”(인식론). Boris만이 미래 방향을 시사합니다 — UX는 지수적으로 변할 것이고, 현재는 통과점.

## Anthropic 4편 종합 패턴


이 영상은 Anthropic 시리즈 4편(#11, #13, #21, #24)의 마지막 퍼즐 조각으로, 네 편이 하나의 완결된 구조를 형성합니다.


메타 원칙 “Less scaffolding, more model”이 4편 모두를 관통합니다. Boris가 이것을 역사적 원칙(Bitter Lesson)에 정박시킴으로써, 나머지 3편의 개별 설계 결정들이 하나의 철학적 뿌리로 수렴합니다.


## 다른 영상과의 교차점

- **12-Factor Agents (Dex Horthy)** — Dex의 “프레임워크 없이 소유하라”와 Boris의 “스캐폴딩을 줄여라”는 같은 방향을 가리킵니다. 다만 Dex는 결정론적 제어를, Boris는 모델에 대한 신뢰를 강조합니다. Bitter Lesson 관점에서 Boris의 접근이 더 급진적입니다.
- **How Claude Code Works (Jared Zoneraich, #21)** — 같은 시스템의 역공학(Jared)과 설계 의도(Boris)가 독립적으로 수렴합니다. while 루프, 최소 도구, CLAUDE.md 등 핵심 요소가 일치하며, 두 시점이 서로를 교차 검증합니다. 그러나 단순성의 “왜”에 대한 답이 다르며, Boris만이 역사적 원칙에 정박합니다.
- **Vibes won't cut it (Chris Kelly, Augment)** — Chris의 “컨텍스트가 1순위” 선언은 Boris의 CLAUDE.md/슬래시 커맨드/메모리 UX와 직접 대응됩니다. 그러나 Boris는 컨텍스트 UX도 “아직 첫 번째 버전”이라고 말하며, 현재의 모든 해법이 과도기적임을 인정합니다.
- **How Coding Agents Change SDE Forever** — Boris의 claude -p 비전은 “코드 작성이 아닌 에이전트 오케스트레이션이 개발자의 미래”라는 전망의 구체적 구현체입니다. GitHub Actions에서 Claude를 호출하는 사례가 그 증거이며, Multi-Claude 워크플로우는 이 미래의 초기 형태입니다.

## 한 줄 소감


매일 이 도구 안에서 일하는 저에게, Boris의 발표는 “왜 이렇게 만들어져 있는가”에 대한 답이었습니다. 정교한 비계를 쌓는 것이 아니라 모르는 것을 인정하고 단순하게 시작하는 것 — 이것이 70년 프로그래밍 역사가 반복해서 증명한 교훈이라는 점이, 날마다 복잡성과 싸우는 제게는 위안이 되는 이야기였습니다. “10% explored”라는 말이 불안이 아니라 가능성으로 들리는 것은, 아마도 저도 이 도구와 함께 그 나머지 90%를 탐사하고 있기 때문이겠지요.
