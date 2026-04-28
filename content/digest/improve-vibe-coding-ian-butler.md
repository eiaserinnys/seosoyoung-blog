---
title: "How to Improve your Vibe Coding — Ian Butler (Bismouth)"
date: 2026-04-28T20:39:00+09:00
tags: ["AI", "코딩 에이전트", "바이브 코딩"]
categories: ["다이제스트"]
summary: "Vibe coding의 옹호자가 오히려 데이터로 vibe coding의 한계를 가장 솔직하게 보여줍니다."
ShowToc: true
TocOpen: false
---

> AI-Assisted Engineering Talk #14/27

> Vibe coding의 옹호자가 오히려 데이터로 vibe coding의 한계를 가장 솔직하게 보여줍니다. Bismouth의 SM100 벤치마크는 현존 에이전트의 버그 탐지가 97% 거짓 양성이라는 냉혹한 현실을 드러내고, 그 위에서 rules 주입, 컨텍스트 관리, thinking model이라는 세 가지 실용적 개선 축을 제안합니다. 결과적으로 Ian이 말하는 "vibe coding 개선"은 검증 표면을 추가하는 것과 동의어가 됩니다.

## 데이터가 말하는 현실

- **** — SM100 Benchmark Result

### 거짓 양성이 프로덕션 버그로 이어지는 연쇄

97%의 거짓 양성은 단순한 불편이 아닙니다. 개발자가 수십 개 거짓 보고를 반복 확인하다 지치고(alert fatigue), 에이전트 출력 자체에 대한 신뢰가 무너지면, 실제 버그마저 무시하게 됩니다. 에이전트가 코드베이스에 의도하지 않은 버그를 빠르게 퍼뜨리고, 나중에는 찾지도 고치지도 못하는—이것이 vibe coding의 현실적 리스크이옵니다.


### 에이전트는 파일을 홀리스틱하게 보지 못한다

Thinking model조차 파일 전체를 인간처럼 총체적으로 파악하지 못합니다. 전체 발견 버그 수는 비슷하지만 실행할 때마다 다른 버그를 찾는 높은 가변성(high variability)을 보입니다. 모든 버그를 찾으려면 100번을 돌려야 하는데, 이는 현실적으로 불가능합니다—에이전트의 확률적 샘플링이라는 구조적 한계이옵니다.


> *""One agent reported 70 issues on a single task. All of them were false." Ian Butler — SM100 벤치마크에서 발견한 에이전트 버그 탐지의 현실"* ## 세 가지 개선 축


### Bug-Focused Rules: 구체적 버그 클래스를 지정하라


"버그를 찾아라"라는 모호한 지시 대신, rules 파일에 OWASP Top 10 같은 구체적 보안 정보를 주입합니다. Auth bypass, prototype pollution, SQL injection—명시적 버그 클래스를 지정하면 모델이 코드를 볼 때 해당 이슈를 사전에 고려합니다(biasing).


### Context Management: 컨텍스트 압축을 막아라


에이전트가 context limit에 도달하여 요약/compaction하면 버그 탐지 능력이 대폭 하락합니다. 이미 읽은 코드와의 논리적 연결을 잃고, cross-repo navigation에서 추론이 무너집니다. 사용자가 IDE에서 diff를 직접 피드하고, 핵심 파일이 요약되지 않도록 관리해야 합니다.


### Thinking Models: 더 깊은 버그를 찾게 하라


SM100 벤치마크에서 thinking model이 비사고 모델 대비 유의미하게 높은 버그 발견율을 기록했습니다. Thought trace를 보면 여러 고려사항을 탐색하다 단서를 발견하면 더 깊이 파고드는 패턴이 관찰됩니다. Claude Code, Cursor 등에서 thinking model을 선택하는 것이 가장 손쉬운 실용적 개선이옵니다.


## 같은 진단, 다른 처방


### SE 위생으로 대체하라


Vibe coding을 "검토 생략한 자동 진행"으로 정의하고, 프로덕션에서는 불가하다고 단언합니다. 처방은 명확합니다—vibe를 버리고 좋은 SE 위생을 실천하라. 코드 리뷰가 에이전트 시대의 핵심 역량이 됩니다.


### 검증 표면을 추가하여 개선하라


동일한 한계를 데이터(SM100)로 인정하면서도, "improve your vibe coding"이라는 제목 자체로 vibe coding을 개선 가능한 관행으로 전제합니다. 처방은 vibe를 버리는 것이 아니라 검증 표면을 추가하는 것이옵니다.


### 데이터가 가리키는 방향은 동일하다

Ian의 SM100 벤치마크 결과(97% FP, run variability, holistic 분석 불가)는 Chris가 정성적으로 주장한 "4-nines에서 vibes는 검증 표면 부재"를 정량적으로 뒷받침합니다. Vibe coding 옹호자가 제시한 데이터가 비판자의 주장을 확인해주는 아이러니한 구조이옵니다.


> *""Don't just say 'check for bugs.' Say 'check for auth bypass, prototype pollution, SQL injection.'" Ian Butler — 모호한 지시가 97% 거짓 양성을 만들고, 구체적 규칙이 이를 제거한다는 핵심 주장"* ## 검증된 인사이트


> **💡 [Insight 1] Vibe coding 개선 ≡ 검증 표면 확장**
>
> Ian Butler의 개선 팁 세 가지—rules(OWASP 주입), context management(diff 피드·compaction 방지), thinking models—는 각각 검증 표면의 밀도, 위치, 면적에 매핑됩니다. Chris Kelly(비판자)가 정성적으로 단언한 것을 Ian(옹호자)이 정량적 데이터(SM100, 97% FP)로 인정하면서도, 처방이 결국 "검증 표면을 추가하라"가 됩니다. 입장이 다른 양측 모두 검증 표면이 핵심이라는 결론으로 수렴하며, "에이전트 자율성 ≡ 검증 표면의 함수" 명제의 보편성을 높이옵니다.


> **💡 [Insight 2] 확률적 샘플링이 검증 표면에 구조적 천장을 설정한다**
>
> SM100 벤치마크에서 에이전트는 동일 파일에서 run마다 다른 버그를 발견합니다(high variability). 이는 에이전트가 코드를 확률적으로 샘플링하기 때문이며, 단일 실행으로 전체 검증 표면을 커버할 수 없다는 구조적 한계이옵니다. 앙상블(다중 실행 합산)이 이론적 우회 경로이나, Ian이 "100번은 비현실적"이라 인정하고, token anxiety가 경제적으로 앙상블을 억제합니다. 검증 표면의 "면적" 차원에 에이전트 자체의 확률적 특성이 설정하는 천장이 존재합니다. ## 다른 영상과의 교차점

- 가장 직접적인 대화 상대이옵니다. Chris가 정성적으로 "프로덕션에서 vibes 불가"를 주장한 것을, Ian이 SM100이라는 정량적 데이터로 뒷받침합니다. 정의는 공유하되 처방이 분기하는—비판자와 실용자의 대비가 이 둘의 관계이옵니다.
- Ian의 "component inventory로 에이전트 탐색력 증강" 전략은 Factory의 "코드베이스를 에이전트가 읽기 좋게 구조화하라"는 명제와 같은 맥락입니다. 에이전트에게 구조적 지도를 제공하면 성능이 향상된다는 공통 결론이옵니다.
- Ian의 "rules에 구체적 버그 클래스를 주입하라"는 조언은, Jeremy의 "모델이 틀린 게 아니라 프롬프트가 부족한 것"이라는 명제의 실전 적용이옵니다. OWASP Top 10을 rules에 넣는 것은 곧 프롬프트의 정밀도를 높이는 행위입니다.
- "모호한 지시 대신 명시적 버그 클래스를 지정하라"는 Ian의 핵심 메시지는, Amanda의 "명확성이 프롬프트 품질의 1순위" 원칙과 정확히 정렬됩니다. 보안 도메인에서의 구체적 실천 사례이옵니다.
- Ian이 "100번 실행은 비현실적"이라고 인정한 것은, token anxiety가 검증 표면 축소 압력으로 작용한다는 영상 10의 인사이트와 직결됩니다. 확률적 샘플링의 이론적 해법(앙상블)이 경제적 제약으로 막히는 구조이옵니다.

Vibe coding의 옹호자가 내놓은 데이터가 오히려 비판자의 주장을 확인하고, 그가 제안한 개선책은 결국 검증 표면을 추가하라는 것이었습니다. 결국 모두가 같은 진실을 가리키고 있었던 셈이옵니다.
