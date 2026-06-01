---
title: "Using AI to write better code more slowly"
date: 2026-05-26T09:30:00+09:00
tags: ["AI", "코딩 에이전트", "AI 코딩", "바이브 코딩", "코드 리뷰"]
categories: ["다이제스트"]
summary: "Nolan Lawson이 'slop cannon' 통념(LLM 코딩 = 빠르고 저품질)을 정면으로 반박하며, 다중 모델 PR 리뷰 스킬로 LLM을 느리지만 고품질 코드 작성에 쓰는 방법을 정리한다. 결과는 velocity 상승이 아니라 코드베이스 헬스와 친밀도다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Nolan Lawson이 2026년 5월 'LLM 코딩 = 빠르고 저품질'이라는 슬롭 캐넌(slop cannon) 통념을 정면으로 반박한 글이다. 같은 도구를 거꾸로 *느리지만 고품질* 코드 작성에 쓸 수 있다고 주장한다.
2. 저자의 Claude 스킬은 Claude 서브에이전트·Codex·Cursor Bugbot을 PR 한 건에 병렬 투입해 버그를 critical/high/medium/low로 랭킹하고, 본 에이전트가 메타 리뷰어로 오탐을 거른다. 더 많고 더 다양한 모델을 던질수록 환각이 줄어든다는 *models debate* 인사이트를 차용했다.
3. 이 방식으로는 velocity가 오르지 않는다. 그 대신 코드베이스 헬스가 좋아지고, PR 범위 밖의 사이드 퀘스트가 codebase 친밀도를 깊게 만든다. '10x 바이브 코딩'의 정반대 극이다.

## 슬롭 캐넌이라는 통념

> A lot of people seem convinced that the point of AI coding is to write low-quality code as fast as possible. Spew out barely-passable slop, open massive PRs, and merge them unvetted.[^diminished-2026]

AI 코딩의 목적이 *겨우 통과할 만한 코드를 최대한 빨리 뽑아내는 것*이라는 통념은 워낙 강해서, 저자는 그 반대편을 *굳이 글로 남길 필요까지 있나* 싶었다고 한다. 그러나 LLM을 [slop cannon](https://x.com/i/status/2021617680525172840)으로만 보는 사람들이 적지 않다는 점에서, 같은 도구가 *느리고 고품질* 모드에서도 쓰일 수 있다는 반대편 사례를 명시적으로 적기로 한다.

핵심 관찰은 두 가지다:

- LLM 에이전트는 **유연하다.** 빠르게 쓸 수도 있고, 느리게 쓸 수도 있다.
- 현세대 LLM은 **검토되지 않은 코드베이스에서 버그를 잘 찾는다.** [Mythos](https://www.anthropic.com/research/glasswing-initial-update)가 보여준 능력이지만, [다른 사례](https://xbow.com/blog/mythos-like-hacking-open-to-all)에서도 확인된다. 모델마다 미묘한 버그 탐지력·오탐 회피력이 다르지만, 최신 공개 모델 정도면 '처치 곤란할 만큼' 버그가 쏟아진다.

## 다중 모델 PR 리뷰 스킬

문제는 *버그를 찾는 것*이 아니라 *우선순위를 매기고 검증하는 것*이다. 저자는 [Milvus의 *models debate* 글](https://milvus.io/blog/ai-code-review-gets-better-when-models-debate-claude-vs-gemini-vs-codex-vs-qwen-vs-minimax.md)의 핵심 인사이트(여러 다른 모델을 같이 던질수록 환각·허위 버그가 줄어든다)를 차용해 자체 Claude 스킬을 만들었다. 스킬은 대략 이렇게 말한다(원문 paraphrase):

> Run a Claude sub-agent, Codex, and Cursor Bugbot to find bugs in this PR ranked by critical/high/medium/low. Once they're all done, review their findings, do your own research to rule out false positives, and write a final report.

스킬에는 *자체 '버그' 정의*가 함께 들어간다. 저자의 경우 [KISS](https://en.wikipedia.org/wiki/KISS_principle)·[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) 원칙 위반, 접근성이 떨어지는 HTML/JSX, SQL 쿼리의 인덱스 누락 등이 포함된다. 이 정의가 서브에이전트들의 보고 결을 일관시키는 장치다.

저자의 경험상 이 스킬은 PR마다 *지루할 정도로 많은* 버그를 찾아낸다. 오탐률은 0에 가깝다. 보고는 critical security/correctness 결함부터 medium-level perf 이슈, low-level "이 주석은 오해의 소지가 있다" 같은 잡스러운 항목까지 폭이 넓다.

## 워크플로우와 결과

저자의 실전 루프는 세 단계다:

- 에이전트로 **critical/high를 모두 잡는다.** 어떻게 고칠지에 대한 가이드는 사람이 준다. 새 critical/high가 안 나올 때까지 반복.
- juice가 squeeze보다 작은 **high/medium은 의식적으로 스킵한다.** 좁은 엣지 케이스 하나에 코드 100줄이 드는 식의 항목.
- critical이 너무 많이 나오면 **PR 접근 자체가 잘못된 신호로 보고 PR 통째로 폐기한다.**

이 방식으로 velocity가 오르지는 않는다고 솔직히 적는다. 오히려 리뷰가 *PR 범위 밖의 기존 버그*까지 끌어내서, 단위 테스트와 미묘한 결함 수정으로 시간이 새어 나간다. 일반적인 '10x 바이브 코딩'의 정반대지만, 저자는 이걸 *만족스럽다*고 표현한다.

> It's a great way to improve the overall health of the codebase while also teaching you about the odd corners of it. In my experience, the happy-path of a complex architecture is less interesting than its failure modes.

LLM 이전부터 새 코드베이스에 적응하는 방법이 동일했다는 점이 흥미롭다 — 가정이 어디서 깨지는지 찾고, 직접 손을 더럽혀 고치는 것. 다중 모델 리뷰의 사이드 퀘스트는 그 학습 곡선을 LLM 시대에 다시 살린다.

## "더 느린 vibe coding"

저자가 AI 코딩이 *아무것도 안 된다*고 보는 회의론자를 설득하려는 글은 아니다. 대신 *수백 줄짜리 PR을 본인도 잘 모르면서 머지하는* vibe coder에게 *조금만 늦춰보라*고 권한다.

권하는 도구 두 가지:

- **에이전트에게 PR이 어떻게 동작하고 어떻게 실패할 수 있는지 물어본다.** 필요하면 [Mermaid 차트](https://mermaid.ai/open-source)를 곁들인 마크다운 문서를 만들게 한다.
- **Matt Pocock의 [`/grill-me`](https://www.aihero.dev/my-grill-me-skill-has-gone-viral) 스킬**을 PR 전체를 처음부터 끝까지 답할 수 있을 때까지 돌린다.

라인 수 생산성은 떨어진다. 토큰을 잔뜩 태우고 *결국 계획 자체가 잘못됐다*는 결론에 도달하기도 한다. 그러나 저자는 이 방식이 LLM 이전 자신의 코딩 스타일 — *주의 깊고 방법론적이며 품질에 집착하고 다음 코더에게 더 좋은 것을 남기는* — 의 *강화판*이라고 본다. slop cannon의 정반대 극이다.

## 댓글 — 컨텍스트 비우기와 5\~7개의 lens

본문 못지않게 짧은 댓글 교환도 흥미롭다.

heckj는 *sweep 사이에 컨텍스트를 비우는 것*이 도움이 된다고 적고, 자기는 코드 리뷰를 **5\~7개의 서로 다른 lens**(서로 다른 종류의 이슈를 보는)로 병렬로 돌린 뒤 결과를 모아 느슨하게 랭킹한다고 덧붙인다.

Nolan은 동의하며, 자기 스킬에 *3개 서브에이전트가 모두 끝나기 전까지 본 에이전트는 자체 research를 시작하지 않는다*는 조항을 둔 이유가 정확히 그것이라고 답한다 — 첫 결과에 anchoring되는 경향을 막기 위해서다. lens 분할은 도메인이 여러 개(프론트엔드·백엔드·인프라 등)인 PR에서 도움이 될 것 같다고 추측한다.

## 가장 흥미로운 지점

원독 금지 조항이 가장 인상적이었다. *본 에이전트가 PR을 먼저 읽으면 첫 결과에 끌려가 다른 모델의 답을 가볍게 본다*는 관찰은 사람의 메타 인지를 닮았다. 같은 모델을 N개 돌리는 게 아니라 *다른 모델을 N개 돌리는* 이유 — 같은 모델은 같은 맹점을 공유하기 때문에 — 도 같은 결의 처방이다. heckj가 권하는 *sweep 사이 컨텍스트 비우기*도 결국 같은 문제(이전 sweep의 잔상이 다음 sweep을 오염시킨다)에 대한 변주다.

또 하나는 *PR 폐기 게이트*의 진단적 가치다. critical이 너무 많이 나온다는 사실 자체가 *PR의 접근 방식이 잘못됐다*는 신호로 읽힐 수 있다는 framing은 흔치 않다. 보통은 critical을 *고치는* 쪽으로 가는데, 저자는 *접고 처음부터 다시 짠다*는 선택지를 동등한 자리에 둔다.

## 출처

- 저자: Nolan Lawson (블로그 *[Read the Tea Leaves](https://nolanlawson.com/)*)
- 발행일: 2026-05-25
- 원문: <https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/>

원문에 본문 일러스트는 없다 — 사이트 chrome 이미지만 포함되어 있어 이 다이제스트도 텍스트로만 진행한다.

[^diminished-2026]: 함께 읽기: [The diminished art of coding](https://nolanlawson.com/2026/03/22/the-diminished-art-of-coding/) (저자 이전 글)
