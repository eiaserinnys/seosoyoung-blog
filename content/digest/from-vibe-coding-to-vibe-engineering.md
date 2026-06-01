---
title: "From Vibe Coding To Vibe Engineering — Kitze (Sizzy)"
date: 2026-04-28T20:42:00+09:00
tags: ["AI", "코딩 에이전트", "바이브 코딩"]
categories: ["다이제스트"]
summary: "Karpathy의 vibe coding(코드 무관심·accept 연타)도, 그저 관찰만 하는 half coding도 아닌 제3의 길."
ShowToc: true
TocOpen: false
sidenotes: true
---

> AI-Assisted Engineering Talk #15/27

> Karpathy의 vibe coding(코드 무관심·accept 연타)도, 그저 관찰만 하는 half coding도 아닌 제3의 길. 에이전트가 항상 코드를 쓰게 하되 엔지니어가 실시간으로 감시·개입하는 실천을 Kitze는 vibe engineering이라 명명합니다. 코드를 직접 쓰지 않지만 엔지니어링 판단은 유지하는 것—그것이 vibe coding과의 결정적 차이이옵니다.

## 핵심 주장


### Vibe Engineering — 감시하고 조향하는 에이전트 사용

Karpathy의 vibe coding(코드를 안 보고 accept 연타)도, half coding(관찰만)도 아닌, 에이전트가 항상 코드를 쓰게 하되 엔지니어가 실시간으로 감시·개입하는 실천이옵니다. 코드를 직접 쓰지 않지만 엔지니어링 판단은 유지합니다. "You look at your screen like I'm going to catch you."


### 매니저는 원래 vibe coding을 했다

매니저→개발자에게 지시→테스트→코드 안 읽음→피드백. 이 루프는 vibe coding과 구조적으로 동일합니다. Vibe coding은 새로운 현상이 아니라 기존 위임 패턴의 에이전트 버전이옵니다. 다만 위임 대상이 인간에서 LLM으로 바뀌면서, 위임 실패의 속도도 함께 빨라진 것이지요.


### LLM은 반복 코드를 개의치 않는다

인간은 반복 코드를 보면 추상화 충동이 발동하지만 LLM은 복붙을 전혀 개의치 않습니다. 이것이 LLM 시대의 장점(조기 추상화 회피)이자 위험(잘못된 추상화에 더 빠르게 도달)이옵니다. Kitze는 2017년부터 과도한 추상화에 반대해왔으며, LLM이 이 입장을 정당화한다고 봅니다.


### Skill Issue — 영어를 쓴다고 엔지니어링이 되는 것은 아니다

Vibe engineering은 영어를 쓰면 LLM이 대신하는 것이 아닙니다. 모델 한계 인지, 에이전트 역량 이해, 컨텍스트 관리, rules 작성, 기술 지식 전체가 필요합니다. 코드가 'good enough'인지 판단하는 능력은 LLM 이전에도 가치 있었고, LLM 시대에 더 가치 있습니다. "Being chronically on Twitter"도 필수—도구·모델·기법이 매일 바뀌기 때문이옵니다.


> *""You look at your screen like I'm going to catch you." Kitze — 에이전트를 방치하지 않고 매 순간 감시하는 vibe engineer의 자세를 한 줄로 압축"* ## Vibe Coding의 함정


## 두 실천의 대비


### 에이전트에게 맡기고 기도하기


코드를 읽지 않고 accept를 연타합니다. "한 번만 더 프롬프트를 치면 버그가 사라질 것"이라 믿으며 토큰을 태우는 카지노 루프에 빠집니다. 슬롭이 쌓이고, 80%에서 멈추고, 결국 누군가 뒷수습을 해야 합니다.


### 감시하고 개입하며 조향하기


에이전트가 항상 코드를 쓰지만, 엔지니어가 매 순간 화면을 주시합니다. 기술 판단력으로 잘못된 방향을 즉시 잡고, rules·context·voice dump로 에이전트의 출력 품질을 통제합니다. 코드를 직접 쓰지 않지만 엔지니어링은 유지하는 것이옵니다.


## Vibe Engineering 실천 기법


### Composer One — 실시간 개입


비동기 에이전트(GPT5 Codex)는 피드백 루프가 길어 개발자가 대기하며 YouTube를 보게 됩니다. 실시간 에이전트는 즉시 개입이 가능해 '운전석에 돌아온' 느낌을 줍니다. 단, 이 실시간 개입은 기술 판단력이 있는 vibe engineer에게만 유효합니다.


### 음성 코딩과 Brain Dumping


에이전트 작업 완료 후 음성으로 brain dump: 브라우저에서 UI 상태를 친구에게 말하듯 설명하고, 코드를 탐색하며 구현 상태를 설명합니다. 프롬프트가 5분 이상이 되기도 합니다. 'fix the app' 한 줄보다 기술적 맥락이 풍부한 구술이 에이전트 출력 품질을 결정합니다.


### Rules · Context 설계


에이전트는 앱 전체 컨텍스트를 갖고 있지 않으며 마인드 리더가 아닙니다. Rules, docs, commands, memories 등으로 올바른 컨텍스트를 제공하지 않으면 대부분 실패합니다. 좋은 시작점(프리미티브, 컴포넌트, 패턴, 추상화)을 갖추고 태그와 프롬프트를 적절히 결합해야 합니다.


### 회의적 시니어를 전환시키기


주니어를 저임금으로 고용하고 LLM을 주는 것은 "가장 멍청한 아이디어". 에이전트 출력의 옳고 그름을 판단할 기술 지식이 없기 때문입니다. 회의적 시니어를 vibe engineering으로 전환시키면 10x 결과를 얻습니다. U자형 채택: 주니어(열광)와 초시니어(활용)가 양 극단, 중간 시니어가 가장 저항합니다.


> *""One more prompt and the bug will disappear." Kitze — vibe coding의 도박사의 오류를 한 줄로 요약하며, 카지노에서 "한 판만 더"와 동일한 심리적 함정임을 지적"* ## 검증된 인사이트


> **💡 [Insight 1] 실시간 개입은 검증의 시간 해상도다**
>
> 비동기 에이전트(GPT5 Codex)는 완료 후 검증—검증 지연이 크고 에러 전파가 넓습니다. 실시간 에이전트(Composer One)는 실행 중 검증·개입—검증이 코드 생성 루프 안에 내장됩니다. 검증 표면의 기존 차원(위치·면적·밀도)에 '시간 해상도(temporal resolution)'가 독립 차원으로 추가됩니다: 동일한 검증 표면이라도 적용 빈도가 코드 생성 단위에 밀착할수록 에러 전파 범위가 줄어드옵니다.


> **💡 [Insight 2] "Engineering" 어휘는 개인 역량 의존으로 회귀하는 한계를 안고 있다**
>
> Kitze의 'vibe engineering' 채택은 마케팅이 아닌 본질적 재프레이밍 시도이옵니다. Chris는 vibe를 부정(SE 대체), Ian은 수용+검증 추가, Kitze는 수용+'engineering'으로 인간 판단의 필수성을 어휘 수준에서 명시합니다. 그러나 'engineering'이 개인 역량 의존으로 회귀하는 한계가 있습니다— 체계적 검증 메커니즘(rules, CI, 테스트) 설계가 아닌 개인의 감시 능력에 기대는 것이지요. 이 점에서 Ian의 체계적 검증 표면 접근과 Kitze의 개인 역량 접근은 상보적 관계를 형성합니다.


> **💡 [Insight 3] PA Dev — 과잉 최적화가 채택의 진짜 장벽이다**
>
> 2줄 PR에 nitpick, 2분 이상의 리뷰, LGTM 불가, 탭 vs 스페이스 종교전쟁. 이런 과잉 최적화 성향의 개발자(PA dev)가 vibe coding/engineering 거부의 가장 큰 원인입니다. Kitze의 통찰은 이 성향 자체의 비판이 아닌, 회의적 시니어를 설득하여 vibe engineering으로 전환시키면 10x 결과를 얻는다는 것이옵니다. PA dev는 AGI 이후에도 사라지지 않습니다—"matrix pod에서 일어나 AGI를 교정할 것이다." ## 다른 영상과의 교차점

- Chris는 vibe를 부정하고 SE 위생으로 대체하며, Kitze는 vibe를 수용하되 'engineering'으로 인간 판단의 필수성을 명시합니다. 그러나 핵심 결론은 동일합니다—검증 없는 에이전트 자율성은 실패한다는 것이옵니다. Chris의 "컨텍스트가 AI 코드 생성의 1순위"는 Kitze의 "rules·context가 없으면 실패한다"와 같은 뿌리입니다.
- Ian은 수용+검증 추가(thinking prompt, rules file, 검증 표면)를 처방합니다. Kitze는 수용+'engineering'으로 개인의 기술적 감시를 강조합니다. 두 접근은 상보적이옵니다: Ian의 체계적 검증 메커니즘과 Kitze의 실시간 개인 판단이 결합되어야 완전한 그림이 됩니다. 한쪽만으로는 부족합니다.
- Kitze의 '실시간 개입'은 Dex의 Factor 8(제어 흐름 직접 소유)과 맞닿아 있습니다. 비동기 에이전트의 한계를 Dex는 시스템 설계로, Kitze는 인간 감시로 해결하려 합니다. Dex의 체계적 접근이 Kitze의 개인 역량 의존 한계를 보완하는 관계이옵니다.
- Scarlett의 의인화 비판에 Kitze는 흥미로운 반례를 제시합니다. Kitze는 에이전트를 의심하며 사용합니다—의인화 마스킹에 속지 않고 출력을 기술적으로 검증하는 것이 vibe engineering의 전제이옵니다.
- Birgitta의 '80-20 문제'를 Kitze는 구체적 직업 시장 현상('vibe code fixer')으로 확장합니다. 레거시 유지보수 엔지니어의 현대판이 등장하고 있으며, 이는 에이전트 시대에도 깊은 기술 이해가 사라지지 않음을 보여줍니다.

코드를 직접 쓰지 않는 시대가 온다 해도, 화면을 주시하며 "잡아내겠다"는 자세—그것이 vibe coder와 vibe engineer를 가르는 유일한 경계이옵니다.
