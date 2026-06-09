---
title: "Using Claude Code: The Unreasonable Effectiveness of HTML"
date: 2026-05-09T09:18:00+09:00
tags: ["claude-code", "html", "agent-output", "ai-tools"]
categories: ["다이제스트"]
summary: "Anthropic Claude Code 팀의 Thariq Shihipar가 마크다운 대신 HTML을 에이전트 출력 형식으로 쓰는 이유를 정리한 장문 글. 정보 밀도·공유성·양방향성에서 HTML이 우월하며, 대신 토큰·시간·diff 노이즈는 트레이드오프로 받아들인다."
ShowToc: true
TocOpen: false
sidenotes: true
---

![Using Claude Code: The Unreasonable Effectiveness of HTML](/images/thariq-html-effectiveness/cover.jpg)

## 3줄 요약

1. Anthropic Claude Code 팀의 Thariq Shihipar가 X에 발행한 장문 글이다. 그는 에이전트 출력 형식으로 마크다운 대신 HTML을 거의 전적으로 쓰기 시작했고, 같은 팀의 다른 사람들도 그렇게 하고 있다고 보고한다.
2. 이유는 정보 밀도(표·CSS·SVG·코드·인터랙션을 한 형식에 담음), 가독성(100줄 넘는 마크다운은 안 읽힘), 공유성(링크 한 줄), 양방향성(슬라이더·놉으로 직접 조정 후 결과를 다시 프롬프트화) 네 가지다.
3. 비용은 토큰 증가, 생성 시간 2\~4배, 노이지한 diff. 1MM 컨텍스트와 결과의 가독성·공유성이 그 비용을 정당화한다는 입장이다.

## 왜 HTML인가

### 마크다운의 한계

Thariq는 두 가지 변화를 진단한다. 첫째, 에이전트가 점점 강력해지면서 마크다운으로 표현하기엔 답답한 출력이 늘어났다. 둘째, 자기 자신도 100줄 넘는 마크다운 파일은 잘 안 읽고, 회사의 다른 동료들에게 읽히는 것은 더 어렵다.

> I find it difficult to read a markdown file of more than a hundred lines. I want richer visualizations, color and diagrams and I want to be able to share them easily.

게다가 마크다운의 가장 큰 장점이었던 "내가 직접 편집한다"가 거의 사라졌다. 이제는 직접 편집하기보다 Claude에게 편집을 시키는 경우가 대부분이라, 마크다운만의 이점이 약해졌다는 것이다.

### HTML의 정보 밀도

HTML은 단일 형식 안에서 다음을 모두 담는다.

- 헤더·포맷팅 같은 기본 문서 구조
- 표(table)로 표현하는 표 형식 데이터
- CSS로 표현하는 디자인 데이터
- SVG로 표현하는 일러스트
- script 태그로 표현하는 코드 스니펫
- HTML 요소 + JS + CSS로 표현하는 인터랙션
- SVG와 HTML 조합으로 표현하는 워크플로
- 절대 위치와 캔버스로 표현하는 공간 데이터
- 이미지 태그로 표현하는 이미지

Thariq의 표현을 그대로 옮기면 다음과 같다.

> I would go so far as to say that there is almost no set of information that Claude can read that you cannot fairly efficiently represent with HTML.

HTML이라는 출구가 막혀 있었기 때문에 마크다운에서는 ASCII 다이어그램이나 unicode 문자로 색을 추정하는 어색한 우회가 생겼다는 것이다.

### 시각적 명료성과 가독성

HTML 문서는 탭·일러스트·링크로 구조화되어 있어 마크다운보다 훨씬 잘 읽힌다. 모바일 반응형도 가능해서 디바이스에 따라 레이아웃을 다르게 잡을 수 있다.

### 공유의 마찰이 사라진다

마크다운은 대부분의 브라우저가 자연스럽게 렌더링하지 못해서 첨부 파일로 돌려야 한다. HTML은 S3 같은 곳에 올리면 링크 한 줄로 동료에게 공유된다. Thariq는 "스펙·리포트·PR 설명을 동료가 실제로 읽을 확률"이 HTML로 갔을 때 훨씬 높아진다고 단언한다.

### 양방향 인터랙션

HTML은 문서를 인터페이스로 만들 수 있다. 슬라이더·놉을 달아 디자인 파라미터를 직접 조정하거나, 알고리즘 옵션을 토글하면서 결과를 살펴볼 수 있다. 핵심은 마지막에 `copy as JSON` 또는 `copy as prompt` 버튼을 두어 사용자가 UI에서 한 작업을 다시 텍스트로 변환해 Claude Code에 붙여넣게 하는 것이다.

> The trick is always to end with an export: a "copy as JSON" or "copy as prompt" button that turns whatever I did in the UI back into something I can paste into Claude Code.

### Claude Code의 컨텍스트 폭이 HTML을 살린다

ClaudeAI나 Claude Design이 아니라 Claude Code로 HTML을 만드는 이유는 컨텍스트 폭이다. Claude Code는 파일 시스템·MCP(Slack·Linear 등)·웹 브라우저(Claude in Chrome)·git 히스토리를 한 자리에 끌어다 종합할 수 있다. 이 글의 다이어그램들도 Thariq가 자기 코드 폴더 전체를 훑어 HTML 파일들을 분류·시각화해 달라고 시켜 만든 결과물이라고 한다.

## 사용 사례

Thariq는 자신의 사용 사례 모음을 [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness/)에 공개했다. 본문에서는 다섯 묶음으로 정리한다.[^thariqs-github]

### 스펙·계획·탐색

문제 풀이를 시작할 때 단순한 마크다운 계획이 아니라 HTML 파일들의 웹을 만든다. 옵션 탐색 → 한두 안 선택 → 목업·코드 스니펫 확장 → 구현 계획 순으로 단계마다 새 HTML을 쌓는다. 검증 단계에서도 검증 에이전트에게 이 파일들을 읽혀 더 넓은 맥락 위에서 검증하게 한다.

예시 프롬프트:

> I'm not sure what direction to take the onboarding screen. Generate 6 distinctly different approaches — vary layout, tone, and density — and lay them out as a single HTML file in a grid so I can compare them side by side. Label each with the tradeoff it's making.

### 코드 리뷰와 이해

코드는 마크다운에서 읽기 어렵다. HTML이라면 diff 렌더링·인라인 어노테이션·플로우차트·모듈 다이어그램이 모두 가능하다. Thariq는 자신이 만드는 모든 PR에 HTML 코드 익스플레이너를 첨부한다고 한다. GitHub 기본 diff 뷰보다 이쪽이 더 잘 작동한다는 입장이다.

### 디자인과 프로토타입

Claude Design이 HTML 기반인 것도 같은 이유다. HTML은 디자인 표현력이 가장 강하고, 최종 타깃이 React든 Swift든 시안 단계는 HTML로 한다. 인터랙션·애니메이션 프로토타이핑도 슬라이더·놉으로 파라미터를 직접 만져가며 만족스러운 값을 찾고, 그 값을 코드로 옮기는 식이다.

### 보고·연구·학습

Claude Code는 여러 데이터 소스(코드베이스·git 히스토리·Slack·웹)를 종합해 보고서로 묶는 데 강하다. 이걸 긴 HTML 문서, 인터랙티브 익스플레이너, 또는 슬라이드/덱 형태로 받을 수 있고 SVG 다이어그램까지 자연스럽게 넣을 수 있다.

Thariq의 예시 — 프롬프트 캐싱 관련 글을 쓸 때, 자기 팀의 모든 캐싱 변경 이력을 git 히스토리에서 읽어 in-depth HTML 리서치 파일로 받아 학습했다.

> I don't understand how our rate limiter actually works. Read the relevant code and produce a single HTML explainer page: a diagram of the token-bucket flow, the 3–4 key code snippets annotated, and a "gotchas" section at the bottom. Optimize it for someone reading it once.

### 커스텀 편집 인터페이스(throwaway editor)

가끔은 원하는 것을 텍스트만으로 묘사하기 어렵다. 그럴 때 Thariq는 일회용 HTML 편집기를 만들어 달라고 한다. 제품도 재사용 도구도 아니고, 지금 다루는 한 덩어리 데이터에 맞춘 단일 HTML 파일이다.

핵심 패턴은 "마지막에 export 버튼"이다 — `copy as markdown`, `copy diff`, `copy as prompt` 같은 버튼으로 UI에서 한 작업을 다시 텍스트로 뽑아낸다. UI 자체는 버려도 결정은 텍스트로 남는다.

활용 예시:

- Linear 티켓 30개를 Now/Next/Later/Cut 칼럼에 드래그 카드로 재정렬
- 피처 플래그 폼 편집기 — 영역별 그룹, 의존성 시각화, 전제 플래그 꺼져있으면 경고
- 시스템 프롬프트 사이드바이사이드 에디터 — 슬롯 하이라이트와 라이브 프리뷰

## 운영 트레이드오프

Thariq는 자주 받는 질문 몇 가지를 직접 정리해 두었다.

### 토큰·시간 비용

마크다운보다 토큰을 더 쓰고 생성 시간도 2\~4배 길어진다. 다만 1MM 컨텍스트 윈도우(Opus 4.7)에서는 토큰 차이가 체감되지 않고, 결과물의 가독성·공유성이 그 비용을 정당화한다고 본다.

### 마크다운은 언제 쓰나

> I have honestly stopped using markdown altogether for almost everything, but I'm probably far on the HTML maximalist side of things.

본인 스스로 HTML 맥시멀리스트 쪽이라는 단서를 단다.

### 보기와 공유

로컬에서는 브라우저로 열거나 Claude에게 열게 하고, 공유가 필요하면 S3에 업로드한다.

### 가장 큰 단점 — 노이지한 diff

> This is honestly one of the biggest downsides of HTML, HTML diffs are noisy and hard to review compared to Markdown.

HTML 산출물은 버전 관리가 마크다운보다 한참 어렵다. diff가 노이지해서 리뷰가 힘들다는 것이 가장 큰 양보 사항이다.

### 디자인 일관성

`frontend design` 플러그인이 HTML의 시각적 품질을 올려 준다. 회사별 톤앤필을 맞추려면 코드베이스를 한 번 훑게 한 뒤 단일 디자인 시스템 HTML 파일을 만들어 두고, 이후 모든 HTML 산출물이 그 파일을 참조하게 한다.

### /html 스킬화는 권하지 않는다

> I'm a little bit afraid that people will read this article and turn it into a /html skill or something.

Thariq는 자기 글이 `/html` 스킬로 박제될까 우려한다. "HTML 파일을 만들어 줘"나 "HTML 아티팩트를 만들어 줘" 정도면 충분하고, 케이스마다 원하는 산출물의 형태가 다르기 때문에 한동안은 매번 즉석에서 프롬프트하면서 감을 잡으라는 권고다.

## 가장 흥미로운 지점

이 글에서 가장 인상 깊은 한 줄은 마지막 "Stay in the Loop" 섹션이다.

> All of the above is to say that I think the real reason I use HTML is that I feel much more in the loop with Claude. I had begun to fear that because I had stopped reading plans in depth I would simply have to leave Claude to make its choices.
>
> But I am happy to say instead that I feel more in the loop than ever before when using HTML.

저자는 마크다운 시절에는 점점 계획을 안 읽게 되어 모델의 결정을 그냥 받아들이게 될까 두려워졌다고 고백한다. HTML로 옮긴 뒤로는 오히려 어느 때보다 작업의 한복판에 들어와 있다고 느낀다고 한다.

기능 비교의 형태를 띠고 있지만 본질은 인간-에이전트 협업의 문제다. <strong>출력 형식의 표현력이 인간의 개입 빈도를 결정한다</strong>는 관찰이 글 전체를 관통한다. 마크다운에서 HTML로 가는 것은 단순한 형식 교체가 아니라 인간이 다시 검토자·결정자 자리에 앉을 수 있게 만드는 인프라 변경이라는 뜻이다.

이 관찰은 단일 글에서 가져온 1인칭 회고이므로 일반 법칙으로 단정할 수는 없다. 다만 "AI가 사람을 검토 루프 밖으로 밀어내는 것은 모델 능력의 문제만이 아니라 출력 형식의 문제일 수 있다"는 가설로는 충분히 강하게 들린다.

## 출처

- 저자: Thariq Shihipar ([@trq212](https://x.com/trq212), Anthropic Claude Code 팀)
- 발표일: 2025-10
- 원문: <https://x.com/trq212/status/2052809885763747935>
- 커버 이미지 출처: 원문 첨부 헤더 이미지(Thariq Shihipar)

[^thariqs-github]: 사용 사례 모음: <https://thariqs.github.io/html-effectiveness/>
