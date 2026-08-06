---
title: "GitReverse"
date: 2026-07-23T18:00:00+09:00
tags: ["AI", "오픈소스", "바이브 코딩", "프롬프트 엔지니어링", "LLM"]
categories: ["에이전트와 코딩"]
summary: "공개 GitHub 저장소를 바이브 코딩으로 다시 만들 법한 '합성 프롬프트' 한 장으로 되돌리는 오픈소스 웹앱. 코드를 디컴파일하는 게 아니라 그 프로젝트를 낳았을 원래 요청을 추론한다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/gitreverse-repo-to-prompt/gitreverse-og.png"
images:
  - "/images/gitreverse-repo-to-prompt/gitreverse-og.png"
---

## 3줄 요약

1. GitReverse는 filiksyos가 2026년 3월 말 공개한 오픈소스 웹앱이다. 공개 GitHub 저장소나 라이브 웹사이트 주소를 넣으면, 그것을 처음부터 만들 때 누군가 커서나 클로드 코드에 붙여 넣었을 법한 짧은 프롬프트 한 장을 되돌려 준다.
2. 핵심은 역발상이다. 보통은 프롬프트에서 코드로 가지만, 이 도구는 코드에서 프롬프트로 거슬러 올라간다. 그것도 소스 전체를 뜯어보는 게 아니라 저장소 메타데이터, 최상위 파일 트리, README 세 조각만 LLM에 넘겨 원래 의도를 추론한다.
3. 별 1,235개에 포크 231개(2026-07-23 기준), 오늘도 커밋이 올라오는 활발한 프로젝트다. 완성된 결과물을 다시 '만들고 싶다는 한마디'로 압축하는 실험이 어디까지 그럴듯한지 보여 준다.

## 무엇을 하는 도구인가

GitReverse의 한 줄 설명은 저장소 설명란에 그대로 적혀 있다. "Reverse engineer any repo into it's original prompt." 공개 GitHub 저장소를 하나의 합성 사용자 메시지로 바꾸는 것이 목표다. 커서, 클로드 코드, Codex, ChatGPT 코드 모드, v0 같은 코딩 에이전트에 그대로 붙여 넣으면 그 프로젝트를 한 번의 바이브 코딩으로 만들어 낼 만한 요청문이다.

사용법은 단순하다. 홈 화면에 GitHub 주소나 `owner/repo` 형태를 붙여 넣으면 된다. `/vercel/next.js`처럼 주소창에 직접 경로를 넣어도 같은 흐름이 돌아가고, 그 링크는 그대로 공유할 수 있다. GitHub식 `/owner/repo/tree/...` 주소는 404를 피하려고 `/owner/repo`로 넘긴다. 지금은 하위 폴더를 넣어도 저장소 전체를 기준으로 프롬프트를 만들고, 폴더 범위에 맞춘 추론은 다음 과제로 남겨 두었다.

## 어떻게 만드는가, 세 조각의 컨텍스트

가장 눈여겨본 것은 이 도구가 소스 코드를 거의 읽지 않는다는 점이다. 저장소를 디컴파일하지 않는다. 대신 GitHub API로 딱 세 가지만 긁어 온다.

- **저장소 메타데이터**: 설명, 주 언어, 별 개수, 기본 브랜치, 토픽.
- **최상위 파일 트리(depth 1)**: 루트에 어떤 폴더와 파일이 있는지만 본다. 전체 구조를 훑지 않는다.
- **README**: 최대 8,000자까지만 넣고, 넘치면 잘라 낸다.

이 셋을 하나의 사용자 메시지로 엮어 LLM에 넘긴다. `main` 브랜치가 없으면 `master`로 다시 시도하고, README가 비어 있으면 "없음"으로 표시한 채 진행한다. 코드 로직 대신 프로젝트가 밖으로 드러낸 최소한의 표면만 보고 원래의 소망을 되짚는 구조다.

파일 트리는 별도 포매터가 `├──`, `└──` 기호로 사람이 읽기 좋은 디렉터리 모양으로 다듬어 넣는다. 깊이와 경로로 걸러 내는 함수도 갖춰 두어, 앞서 말한 폴더 범위 추론의 밑작업은 이미 코드에 준비되어 있다.

## 시스템 프롬프트가 본체다

이 프로젝트의 알맹이는 `lib/system-prompt.ts` 한 파일이다. LLM에게 "사람들이 실제로 코딩 에이전트에게 어떻게 말하는지 아는 전문가"가 되라고 시키고, 출력 규칙을 상세히 건다. 원문 지시의 뼈대는 이렇다.

> - **Plain language.** Sounds like a real request ("Build me…", "I want…"), not an architecture doc.
> - **Outcome focused.** Describe what the app or library should *do* for a user using words a normal person would use.
> - **Honest scope.** Only claim features or stacks you infer from the README and tree you received.
> - **Length:** about 120 to 200 words, usually one short paragraph or a few tight sentences.
> - Do not invent features that are not supported by the evidence in the context.

핵심은 세 가지다. 첫째, 결과물은 아키텍처 문서가 아니라 보통 사람이 쓸 법한 말이어야 한다. 프레임워크 이름이나 폴더 구조를 늘어놓지 말고, 앱이 사용자에게 무엇을 해 주는지를 일상어로 적으라고 못을 박는다. 둘째, 증거에 없는 기능을 지어내지 말라고 거듭 강조한다. README와 트리에서 추론되는 것만 주장하고, 근거가 얇으면 주장도 흐릿하게 두라는 것이다. 셋째, 길이는 약 120에서 200단어, 짧은 한 문단 정도다.

내가 웃은 대목은 문체 규칙 한 줄이다. "NEVER use hyphens or dashes, split into shorter sentences or use commas." 하이픈과 대시를 절대 쓰지 말고 짧은 문장이나 쉼표로 끊으라는 지시인데, AI가 쓴 티가 나는 대표적 흔적을 결과물에서 지우려는 장치다.

## 두 번째 모드, 웹사이트도 되돌린다

GitReverse는 저장소만 다루지 않는다. 라이브 웹사이트 주소를 넣으면 브랜딩 데이터, 페이지 콘텐츠, 간단한 디자인 시스템 요약을 뽑아, 그 사이트를 다시 만들 법한 프롬프트를 돌려준다. 이쪽 시스템 프롬프트는 색과 타이포그래피, 브랜드 무드 같은 시각적 개성을 자연스럽게 녹여 넣으라고 따로 주문한다. 저장소 역생성이 '무엇을 하는가'를 복원한다면, 웹사이트 역생성은 '무엇처럼 보이고 느껴지는가'까지 복원하는 셈이다.

## 스택과 운영

기술 스택은 최신 조합이다. Next.js 16(App Router), React 19, TypeScript, Tailwind CSS 4를 쓰고, Supabase와 Stripe는 선택이다.

빠른 역생성 엔드포인트는 네 개의 LLM 공급자를 지원한다. 환경변수 `GITREVERSE_QUICK_LLM`으로 하나를 고정하거나, 비워 두면 키가 있는 것을 자동으로 고른다. 자동 모드의 우선순위는 Grok, OpenRouter, Azure, Google 순이다.

| 공급자 | 기본 모델 |
|---|---|
| Grok (xAI) | `grok-3` |
| OpenRouter | `google/gemini-2.5-pro` |
| Azure OpenAI | `gpt-5.4` |
| Google AI Studio | `gemini-2.5-pro` |

Supabase를 붙이면 만들어진 프롬프트를 캐시에 저장하고 `/library` 페이지에서 다른 사람들이 만든 결과를 둘러볼 수 있다. 이 라이브러리 검색과 프롬프트 캐시 임베딩은 Azure의 `text-embedding-3-small`(차원 512)을 기본으로 쓴다. 프로덕션에서는 `VIEWS_IP_SALT` 값을 반드시 넣어야 하고, 기본값 그대로면 앱이 시작을 거부한다.

작은 디테일 하나. 이 저장소 루트에는 `CLAUDE.md`와 `AGENTS.md`가 놓여 있다. 저장소를 프롬프트로 되돌리는 도구가, 정작 자기 자신은 에이전트 지시문을 품고 만들어진 셈이다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 이 도구가 '되돌린다'고 말하면서도 코드를 거의 보지 않는다는 사실이다. 소스 전체를 분석하면 훨씬 정확한 복원이 나올 텐데, GitReverse는 일부러 README와 파일 트리, 메타데이터라는 얇은 표면만 본다. 결과물이 구현의 재현이 아니라 의도의 재구성이기 때문이다. 완성된 코드가 아니라 "이런 걸 만들어 줘"라는 첫 마디로 돌아가려는 것이고, 그 첫 마디는 원래도 저장소의 표면에만 드러나 있었다.

그래서 이 프로젝트는 정확한 리버스 엔지니어링 도구라기보다, 바이브 코딩 시대의 사고 실험에 가깝다. 우리가 만든 것을 다시 '만들고 싶다는 한마디'로 압축할 수 있다면, 그 한마디는 얼마나 짧아도 되는가. 로고가 우노 카드의 리버스 카드를 본뜬 것도 같은 농담의 연장으로 읽힌다.

## 출처

filiksyos, GitReverse (오픈소스 웹앱). 별 1,235개, 포크 231개, 2026-03-31 생성, 2026-07-23 기준.
서비스: <https://gitreverse.com>
원문: <https://github.com/filiksyos/gitreverse>

커버 이미지는 gitreverse.com이 소셜 카드용으로 제공하는 공식 OG 이미지다.
