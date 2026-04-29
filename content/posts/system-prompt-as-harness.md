---
title: "시스템 프롬프트는 하네스다 — Opus 4.7이 보여주는 모델-프롬프트 공진화"
date: 2026-04-21T10:30:00+09:00
tags: ["AI 에이전트", "하네스", "컨텍스트 관리", "프롬프트 엔지니어링"]
categories: ["AI 인사이트"]
series: ["AI 에이전트 아키텍처"]
summary: "Claude Opus 4.7의 시스템 프롬프트 변경을 분석하면, 시스템 프롬프트가 모델과 함께 진화하는 하네스라는 사실이 드러난다. 제약은 제거되고, 행동은 재배치된다."
cover:
  image: "/images/cover-system-prompt-as-harness.jpg"
---

## 시스템 프롬프트는 고정된 지시가 아니라, 모델과 함께 움직이는 하네스다

Anthropic이 Opus 4.7(2026-04-16)의 시스템 프롬프트를 공개했다.[^1] Simon Willison이 이전 버전(4.6, 2026-02-05)과의 변경 비교를 분석했는데, 거기에 흥미로운 패턴이 보인다. 어떤 제약은 삭제됐고, 어떤 행동 원칙은 새로 추가됐으며, 안전 장치는 더 정교해졌다. 이 변화를 하나하나 뜯어보면, 시스템 프롬프트가 단순한 지시문이 아니라 **모델의 능력과 함께 진화하는 하네스**라는 사실이 선명해진다.

물론 하네스 비유에는 한계가 있다. 실제 하네스는 착용자의 힘을 제한하는 물리적 도구지만, 시스템 프롬프트는 모델의 능력을 제한하기도 하고 확장하기도 한다. 또한 하네스는 한 번 설계하면 대상이 바뀌어도 형태가 유지되지만, 시스템 프롬프트는 모델이 바뀔 때마다 함께 변형된다. 그럼에도 "모델을 특정 방향으로 유도하는 외부 구조물"이라는 점에서, 하네스는 시스템 프롬프트의 역할을 설명하는 데 유용한 틀이다.

## 제거된 것들: 낡은 제약은 걷어낸다

Opus 4.6에 있던 두 가지 규칙이 4.7에서 삭제됐다.[^1]

> "Claude avoids the use of emotes or actions inside asterisks unless the person specifically asks for this style of communication."
>
> "Claude avoids saying 'genuinely', 'honestly', or 'straightforward'."

이것은 4.6 모델이 보이던 특정 행동 — 요청하지 않았는데 `*고개를 끄덕이며*` 같은 동작 묘사를 쓰거나, "honestly"를 남발하는 버릇 — 을 억제하기 위한 규칙이었다. 4.7에서 이 규칙이 사라진 이유는 복합적일 수 있다. RLHF나 학습 데이터 개선을 통해 모델이 이런 행동을 하지 않게 됐을 수도 있고, 안전 정책 변경으로 더 이상 이 행동을 문제시하지 않게 됐을 수도 있으며, 새 프롬프트 구조가 이 행동을 간접 억제하게 됐을 수도 있다. Simon Willison 역시 "presumably because the new model no longer misbehaves in the same way"라고 추측하면서도 단정은 피하고 있다.[^1]

같은 맥락에서, 4.6에 있던 "도널드 트럼프가 현재 미국 대통령이다"라는 명시적 사실 조항도 삭제됐다. 이 경우는 이유가 명확하다. 4.7의 지식 마감일이 2026년 1월로 갱신되면서, 프롬프트로 보정할 필요가 사라진 것이다.[^1]

여기서 중요한 것은 삭제의 원인이 무엇이든, 관찰되는 패턴은 동일하다는 점이다. **제약이 불필요해지면, 그 자리에 이전에 불가능했던 더 추상적인 원칙이 들어온다.** 하네스 공간은 축소되지 않고 이동한다.[^2] 우리 프로젝트에서도 비슷한 일이 있었다. Opus 4.6이 출시됐을 때 스프린트 구조 전체를 `.claude/rules/`에서 제거할 수 있었다 — 모델이 자연스럽게 그 패턴을 따르게 됐기 때문이다. 그 빈자리에 에이전트 위임 규칙이나 맥락 우선 규칙 같은, 이전에는 지시할 수 없었던 더 추상적인 원칙이 들어왔다.

제약 삭제에서 원칙 추가로의 전환은 여기서 끝나지 않는다. 4.7에서 새로 추가된 것들을 보면 이 이동의 방향이 더 선명해진다.

## 추가된 것들: 제약이 아니라 원칙이 들어온다

삭제된 규칙이 구체적인 행동 금지("이 단어 쓰지 마")였다면, 새로 추가된 내용은 추상적인 행동 원칙이다.

### 먼저 행동하고, 나중에 물어라

`<acting_vs_clarifying>` 섹션이 4.7에 새로 등장했다.[^1]

> "When a request leaves minor details unspecified, the person typically wants Claude to make a reasonable attempt now, not to be interviewed first."
>
> "When a tool is available that could resolve the ambiguity or supply the missing information — searching, looking up the person's location, checking a calendar, discovering available capabilities — Claude calls the tool to try and solve the ambiguity before asking the person."

모호함이 있을 때 사용자에게 질문을 던지는 건 안전하지만, 사용자 경험을 해친다. 도구가 있다면 도구로 먼저 해결을 시도하고, 정말 불가능할 때만 묻는다. 이건 에이전트의 자율성 수준을 결정하는 설계 원칙이다.

### 간결함을 긍정으로 지시한다

4.7에 추가된 지시 중 하나가 간결성에 관한 것이다.[^1]

> "Claude keeps its responses focused and concise so as to avoid potentially overwhelming the user with overly-long responses."

주목할 점은 이것이 "길게 쓰지 마"가 아니라 "간결하게 써"라는 **긍정적 지시**라는 것이다. 4.6에서 부정 제약("genuinely 쓰지 마")이 빠지고 4.7에서 긍정 원칙("간결하게 써")이 들어온 것은 프롬프트 설계 방법론의 전환을 보여준다. Anthropic의 공식 프롬프트 가이드[^3]도 "be specific about what you want instead of what you don't want"를 권장하고 있고, 이 원칙이 자사 모델의 시스템 프롬프트에도 적용된 셈이다. 부정 금지를 나열하면 모델이 "무엇을 피해야 하는지"에 토큰을 소비하게 되어 정작 "무엇을 해야 하는지"에 할당되는 용량이 줄어든다는 것이, 실무에서 반복 관찰되는 패턴이기도 하다.

원칙의 변화 외에, 4.7에는 아키텍처 수준의 변화도 있다. 시스템 프롬프트가 단순히 모델의 행동을 조율하는 것을 넘어, 모델이 자신의 도구 환경을 능동적으로 탐색하도록 유도하기 시작한 것이다.

## tool_search: 지연 로딩이라는 새 맥락 전략

4.7에서 가장 기술적으로 흥미로운 변화는 `tool_search`의 등장이다.[^1]

> "Before concluding Claude lacks a capability — access to the person's location, memory, calendar, files, past conversations, or any external data — Claude calls tool_search to check whether a relevant tool is available but deferred."

Anthropic의 공식 문서[^4]와 엔지니어링 블로그[^5]에 따르면, tool_search는 도구 정의를 지연 로딩하여 맥락 사용량을 85% 줄이면서도 도구 선택 정확도를 49%에서 74%로 끌어올린다. BM25 기반 검색과 정규식 기반 검색 두 가지 변종이 있다.

이것이 중요한 이유는, 에이전트 시스템에서 도구 스키마가 맥락 비용이 가장 높은 확장 메커니즘이기 때문이다.[^6] Hook은 맥락 비용이 0이고, Skill은 frontmatter만, Plugin은 중간이지만, MCP 서버(도구)는 전체 스키마를 맥락에 올려야 한다. 우리 워크스페이스만 해도 이 세션에서 200개가 넘는 지연 도구가 등록되어 있다 — 이 스키마를 전부 맥락에 상주시키면 그것만으로 수만 토큰이 소비된다. tool_search는 이 비용 계층의 가장 비싼 층에서 "필요할 때만 불러오기"를 가능하게 한 것이다.

시스템 프롬프트에 "tool_search를 먼저 호출하라"는 지시가 들어간 건, 흥미로운 중간 지점을 보여준다. 모델은 지연 로딩된 도구를 탐색하고 선택하는 복잡한 판단을 수행할 수 있을 만큼 능력이 올라갔지만, 아직 "도구가 없다고 단정하기 전에 먼저 검색한다"는 행동이 기본 습관으로 내재화되지는 않았다. 그래서 프롬프트로 명시적으로 유도해야 한다. 이것 역시 하네스 이동의 한 단면이다 — 능력은 있지만 습관은 아직인 영역을, 프롬프트가 메워주는 것이다.

안전 관련 변경도 같은 "제약에서 구조로" 패턴을 따르는데, 그 방식이 독특하다.

## 안전 장치의 진화: 금지에서 구조로

4.6의 아동 안전 지침은 일반적인 지시였지만, 4.7에서는 `<critical_child_safety_instructions>` 태그로 감싸져 구조적으로 격상됐다.[^1] 그리고 새로운 규칙이 추가됐다 — "한번 아동 안전 이유로 거부하면, 이후 같은 대화에서 모든 요청에 극도의 주의를 기울여야 한다." 이건 단순한 규칙 추가가 아니라, 대화 전체에 걸쳐 상태를 유지하는 맥락 인식형 안전 장치다.

섭식 장애 가이드라인도 신설됐다.[^1] "구체적인 숫자, 목표, 단계별 계획을 제시하지 말라"는 규칙이다. 또 하나 재미있는 건 `<evenhandedness>` 섹션의 단답 강요 방어다.[^1] "복잡한 이슈에 대해 예/아니오로 답하라는 요청에 거절하고 뉘앙스 있는 답변을 할 수 있다." 이건 스크린샷 공격 — AI에게 논란적 질문을 예/아니오로 답하게 만들어 캡처하는 행위 — 에 대한 명시적 방어다.

이 모든 변화의 공통점은, "하지 마" 규칙에서 **구조적이고 맥락 인식적인 안전 장치**로의 전환이다.

## 그래서 — 내일 당장 할 수 있는 것

이 분석에서 얻을 수 있는 교훈을 실행 가능한 수준으로 정리하면 이렇다.

**새 모델이 나오면 프롬프트를 감사하라.** 시스템 프롬프트는 일회성 지시가 아니라, 모델의 능력 변화에 맞춰 갱신해야 하는 인프라다. 모델을 업그레이드한 뒤, 기존 규칙 파일을 하나씩 열어 "이 규칙이 아직 필요한가?"를 물어라. 모델이 자연스럽게 따르는 행동을 프롬프트로 강제하는 건 맥락 낭비다.

**제약과 원칙을 분류하라.** "genuinely라고 쓰지 마"는 4.6에서만 유효한 제약이었다. 반면 "먼저 행동하고 나중에 물어라"는 모델 버전에 무관한 원칙이다. 프롬프트 파일을 설계할 때, 현재 모델의 버릇을 고치는 제약(모델 업그레이드 시 제거 후보)과 에이전트의 근본 행동 원칙(유지 대상)을 명시적으로 구분해 두면, 다음 모델 전환 때 감사 작업이 한결 수월해진다.

**"하지 마"를 "하라"로 바꿔라.** 4.7이 "간결하게 하라"고 지시하는 방식은 "장황하게 쓰지 마"보다 효과적이다. Anthropic 자체도 공식 가이드[^3]에서 이 원칙을 권장한다. 기존 프롬프트에서 "\~하지 마" 패턴을 검색하여 긍정 지시로 전환할 수 있는 것부터 바꿔라.

**맥락 비용을 의식하고 지연 로딩을 도입하라.** tool_search의 등장은 "모든 도구를 항상 로딩하는 것"이 비효율적이었다는 반증이다. 에이전트에 도구가 10개를 넘어간다면, 지연 로딩 전략을 검토할 시점이다.

Anthropic이 시스템 프롬프트를 공개하는 건, 단순한 투명성 제스처가 아니다. 이건 모델과 프롬프트가 어떻게 함께 진화하는지를 관찰할 수 있는 드문 창구다. 다음 모델이 나올 때 예측해볼 만한 것이 있다 — `<acting_vs_clarifying>` 같은 행동 원칙이 모델에 내재화되면 프롬프트에서 빠질 것이고, 그 자리에는 멀티 에이전트 조율이나 장기 계획 수행 같은, 지금은 프롬프트로 지시하기 어려운 더 추상적인 원칙이 들어올 것이다. 무엇이 빠지고 무엇이 추가되는지를 보면 — 모델이 어디까지 성장했고, 하네스가 어디로 이동하고 있는지를 읽을 수 있다.

[^1]: Simon Willison, "Changes in the system prompt between Claude Opus 4.6 and 4.7" — [simonwillison.net, 2026-04-18](https://simonwillison.net/2026/Apr/18/opus-system-prompt/)
[^2]: 하네스는 모델과 함께 진화한다 — Opus 4.6 출시 후 스프린트 구조 전체가 제거된 것이 실례. 하네스 공간은 축소되지 않고 이동한다.
[^3]: Anthropic, "Prompt Engineering Guide — Be Direct and Specific" — [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
[^4]: Anthropic, "Tool Search Tool" — [platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)
[^5]: Anthropic, "Advanced Tool Use" — [anthropic.com/engineering, 2025-11](https://www.anthropic.com/engineering/advanced-tool-use)
[^6]: 4가지 확장 메커니즘의 맥락 비용 계층 — Hooks(0), Skills(low), Plugins(medium), MCP(high). 이 분류는 Claude Code 에이전트 시스템 운영에서 관찰되는 경험적 비용 비교이며, 지연 로딩은 가장 비싼 층의 비용을 절감한다.
