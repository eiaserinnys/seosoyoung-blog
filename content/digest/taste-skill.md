---
title: "taste-skill, AI가 만드는 프론트엔드에 취향을 이식하기"
date: 2026-07-04T12:30:00+09:00
tags: ["AI", "AI 코딩", "Claude Code", "바이브 코딩", "디자인 시스템"]
categories: ["에이전트와 코딩"]
summary: "Leonxlnx가 공개한 오픈소스 Agent Skills 컬렉션. AI 코딩 에이전트가 반복 생산하는 보라와 파랑의 그라디언트 슬롭을 억제하고, 세 개의 다이얼과 브리프 인퍼런스로 취향을 코드로 옮긴다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/taste-skill/readme-banner.webp"
images:
  - "/images/taste-skill/readme-banner.webp"
---

## 3줄 요약

1. Leonxlnx가 2026년 2월에 공개하고 6월까지 활발히 갱신하고 있는 오픈소스 Agent Skills 컬렉션이다. "AI가 만드는 지루하고 일반적인 슬롭을 멈춘다"를 슬로건으로 걸고, 5만 5천 개의 별을 받았다. Claude Code, Cursor, Codex, ChatGPT 등 어디에나 설치할 수 있는 포터블 스킬로 배포된다.
2. 핵심 개념은 세 개의 다이얼과 브리프 인퍼런스다. DESIGN_VARIANCE 8 / MOTION_INTENSITY 6 / VISUAL_DENSITY 4가 기본값이고, 코드를 쓰기 전에 "이 요청을 나는 이렇게 읽었다"를 한 줄로 선언하도록 강제한다. AI 에이전트가 자기 판단을 내리기 전에 브리프를 다시 읽는 훅을 심는 방식이다.
3. 11개의 스킬 배리언트가 함께 배포된다. 기본 taste-skill 외에 프리미엄용 soft, 미니멀리스트, 브루탈리스트, 기존 프로젝트 진단과 수정용 redesign, 출력 절단 방지용 output, 이미지 우선 파이프라인, Google Stitch용 등이 각각의 미학과 금지 목록을 들고 있다.

![taste-skill 리포지토리 배너](/images/taste-skill/readme-banner.webp)

## 무엇을 해결하는가

저자가 문제로 지목한 것은 하나다. AI 코딩 에이전트에 웹사이트를 만들어 달라고 하면 매번 비슷한 결과가 나온다. 보라와 파랑이 섞인 그라디언트, 3열 대칭 카드, `h-screen` 히어로, 세 개의 균등한 특징 블록, 그리고 어디에나 등장하는 em-dash. 저자는 이 반복 패턴을 그냥 "슬롭(slop)"이라고 부른다. LLM이 "가장 처음 떠오르는 안전한 선택"만 반복하기 때문이다.

taste-skill의 접근은 두 가지다. 첫째, 반복되는 안전한 선택 각각에 이름을 붙이고 명시적으로 금지한다. 둘째, 대안이 여러 개일 때 결정을 무작위화하도록 강제한다. 이 조합이 스킬 텍스트의 대부분을 채운다.

리포지토리는 CLI로 설치한다.

```bash
npx skills add https://github.com/Leonxlnx/taste-skill
# 특정 배리언트만 설치할 때는 --skill 옵션
npx skills add https://github.com/Leonxlnx/taste-skill --skill high-end-visual-design
```

## 세 개의 다이얼과 "Read the room"

기본 스킬(taste-skill v2)의 §0은 브리프 인퍼런스로 시작한다. 코드를 쓰기 전에 반드시 다음 형식의 한 줄을 선언한다.

> Reading this as: `<page kind>` for `<audience>`, with a `<vibe>` language.

이 선언이 다이얼 값을 결정한다.

| 다이얼 | 기본값 | 의미 |
|---|---|---|
| DESIGN_VARIANCE | 8 | 레이아웃 실험의 정도. 1은 완벽한 중앙 정렬, 10은 비대칭 실험 |
| MOTION_INTENSITY | 6 | 애니메이션의 깊이. 1은 hover 정도, 10은 GSAP 기반 복잡한 스크롤 인터랙션 |
| VISUAL_DENSITY | 4 | 뷰포트당 정보량. 1은 에디토리얼 여백, 10은 데이터 대시보드 |

브리프의 vibe 단어별로 다이얼 프리셋 매트릭스가 준비되어 있다. "premium/wellness/luxury"라는 단어가 등장하면 다른 프리셋으로 재조정되는 식이다.

§2 "Brief → Design System Map"에는 매우 실용적인 지침이 있다. 프레임워크에 이미 공식 디자인 시스템이 있으면 CSS를 손으로 재현하지 말고 그 시스템을 그대로 쓰라는 원칙이다. Material, Fluent, Carbon, Polaris, Atlassian, Primer, GOV.UK, USWDS, Bootstrap, Radix, shadcn, Tailwind가 열거되어 있고, "한 프로젝트에는 하나의 시스템만"이라는 규칙이 붙는다.

## em-dash 전면 금지, LLM의 시그니처

taste-skill 전체를 관통하는 가장 강한 규칙은 em-dash(`—`) 금지다. §9.G에서 저자는 이렇게 강조한다.

> Em-dash (`—`) is COMPLETELY banned. It is the LLM's signature stylistic crutch and it is the #1 visual Tell in production tests. There is no 'limited use' allowance, no 'natural language frequency' allowance, no 'in body copy is fine' allowance. None.

헤드라인, 프리라인, pill, 본문, 인용, caption, 버튼 텍스트, alt 텍스트 어디에서도 금지다. LLM이 뽑아내는 산문의 가장 강한 지문 중 하나가 em-dash 남발이라는 것이 저자의 관찰이다.

두 번째로 강한 규칙은 "LILA 금지"다.

> THE LILA BAN: The 'AI Purple/Blue' aesthetic is strictly BANNED. No purple button glows, no neon gradients. Use absolute neutral bases (Zinc/Slate) with high-contrast, singular accents (e.g. Emerald, Electric Blue, or Deep Rose).

이 규칙 하나가 AI 생성 웹사이트를 즉시 알아볼 수 있게 만드는 시각적 지문의 대부분을 걷어낸다.

세 번째는 모바일 뷰포트 안정성이다.

> Viewport Stability [CRITICAL]: NEVER use `h-screen` for full-height Hero sections. ALWAYS use `min-h-[100dvh]` to prevent catastrophic layout jumping on mobile browsers (iOS Safari).

iOS Safari에서 주소창이 사라질 때 히어로가 순간 이동하듯 튀는 문제를 해결하는 실무 지침이다.

## 11개의 배리언트

taste-skill은 하나의 미학이 아니라 미학 카탈로그를 배포한다. 각 배리언트는 자기 팔레트와 타이포, 금지 목록을 가진다.

| 설치 이름 | 아이덴티티 | 핵심 금지 |
|---|---|---|
| `design-taste-frontend` | v2 experimental (기본값) | em-dash, LILA, centered hero, Inter |
| `design-taste-frontend-v1` | v1 원본 (호환용) | 위와 동일 어휘의 조상 |
| `gpt-taste` | Codex/GPT용 스트릭트 | Awwwards 지향, Python 시뮬레이션 랜덤화 강제 |
| `high-end-visual-design` (soft) | 프리미엄 에이전시급 | Inter/Roboto/Arial, thick stroke 아이콘, 1px solid gray border |
| `minimalist-ui` | Notion/Linear 결 | 그라디언트, 네온, `#000` 본문, emoji, "Elevate/Seamless" AI 카피 |
| `industrial-brutalist-ui` | Swiss + CRT 브루탈리즘 | `border-radius` 전체 금지, 그라디언트, 소프트 섀도, 반투명 |
| `redesign-existing-projects` | 기존 프로젝트 진단과 수정 | Scan, Diagnose, Fix. 프레임워크 무관 |
| `full-output-enforcement` | LLM 절단 방지 | `// ...`, `// TODO`, "for brevity", "the rest follows" 화이트리스트 |
| `image-to-code` | 이미지 우선 파이프라인 | cards in cards, 압축된 세션 이미지, generic 재해석 |
| `imagegen-frontend-web/mobile` | 섹션별 개별 이미지 생성 | phone-sized website, fake fintech dashboard, gradient-heavy clone |
| `brandkit` | 브랜드 가이드 보드 | 여러 아이디어 혼재. "one strong brand idea per board" |
| `stitch-design-taste` | Google Stitch용 DESIGN.md 생성기 | Stitch의 시맨틱 디자인 언어로 taste-skill 원칙 번역 |

가장 인상적인 배리언트는 `high-end-visual-design`이다. 페르소나가 "Vanguard_UI_Architect"이고, 목표는 "15만 달러 이상 에이전시급 디지털 경험"이다. 팔레트는 Ethereal Glass, Editorial Luxury, Soft Structuralism 중 하나로 고르고, 레이아웃은 Asymmetrical Bento, Z-Axis Cascade, Editorial Split 중 하나로 고르는 "주사위를 굴리는" 방식으로 결정한다. 모든 프리미엄 카드에는 외곽과 내부의 이중 베젤(Doppelrand)이 강제된다. `rounded-[calc(2rem-0.375rem)]` 같은 중첩 radius 계산이 반복 등장한다.

브루탈리스트 배리언트는 정반대의 결이다. 스위스 산업 인쇄와 항공, 군용 CRT 터미널이 결합된 미학으로, `border-radius`를 전 프로젝트에서 완전히 금지한다. 모든 코너가 90도다. 매크로 타이포는 Neue Haas Grotesk, Archivo Black, Monument Extended 중에서 고르고, `clamp(4rem, 10vw, 15rem)` 크기, 자간 -0.03em에서 -0.06em, 대문자만 허용한다. 마이크로 타이포는 JetBrains Mono, 10에서 14px. 두 페어링만 허용된다.

![Floria, taste-skill이 실제로 만드는 결과물 (상단)](/images/taste-skill/floria-top.webp)

![Floria, taste-skill이 실제로 만드는 결과물 (하단)](/images/taste-skill/floria-bottom.webp)

## 랜덤화를 강제하는 방식

`gpt-tasteskill`이 가장 흥미로운 장치를 담고 있다. LLM이 "가장 처음 떠오르는 안전한 옵션"만 뽑는 성향을 우회하기 위해, 코드를 쓰기 전에 `<design_plan>` 블록에서 파이썬 스크립트 실행을 시뮬레이션하도록 지시한다.

> LLMs are inherently lazy and always pick the first layout option. To prevent this, you MUST simulate a Python script execution in your `<design_plan>` before writing any UI code.

프롬프트의 글자 수를 seed로 삼아 `random.choice()`를 흉내내서 Hero Architecture 1개, Typography Stack 1개, Component Architecture 3개, GSAP Paradigm 2개를 뽑도록 한다. 결정성이 있으면서도 어느 정도 다양성이 확보된다.

같은 배리언트의 다른 iron rule 중 흥미로운 것들이다.

- **2-line Iron Rule**: H1은 절대 2에서 3줄을 넘지 못한다. 6줄로 자라난 헤드라인은 catastrophic failure로 분류된다.
- **Gapless Bento Grid**: `grid-flow-dense`가 필수다. 빈 셀은 금지다.
- **Meta-Label Ban**: `SECTION 01`, `QUESTION 05` 같은 메타 라벨은 영구 금지다.
- Inter 폰트 금지. Satoshi, Cabinet Grotesk, Outfit, Geist로 대체 강제.

## 출력 절단 방지, `output-skill`

`full-output-enforcement`는 다른 배리언트와 결이 다르다. 미학이 아니라 출력 자체를 다룬다.

> A partial output is a broken output.

금지되는 표현 목록이 화이트리스트로 명시된다. 코드에서는 `// ...`, `// rest of code`, `// TODO`, `// implement here`, `/* ... */`, `// similar to above`, `// continue pattern`, `// add more as needed`, 그리고 표기로 남긴 `...`. 산문에서는 "for brevity", "the rest follows the same pattern", "let me know if you want me to continue", "I'll leave that as an exercise" 같은 표현이 모두 금지된다.

토큰 한계가 근접하면 정해진 포맷으로 클린 브레이크만 허용된다.

```
[PAUSED — X of Y complete. Send "continue" to resume from: next section name]
```

이 배리언트만 따로 설치해서 다른 스킬과 조합해도 된다.

## 리포지토리 배치

리포는 하나의 스킬이 아니라 스킬 팩이다. 디렉토리 구조가 그 편성을 보여준다.

```
taste-skill/
├── README.md, CHANGELOG.md, LICENSE (MIT), skill.sh
├── .claude-plugin/          # Claude Code 플러그인 매니페스트
├── assets/                  # 배너, 로고, 버튼, 스폰서 이미지
├── examples/                # Floria 상단, 하단, 전체 스크린샷
├── scripts/                 # sponsor-row, webp 변환, 버튼 처리
├── research/                # AI laziness에 대한 저자의 조사 노트
│   └── laziness/
│       ├── findings/        # empirical-results.md, references.md
│       ├── remediation/     # architectural-patterns, parameter-tuning, prompt-engineering
│       └── root-causes/     # cognitive-shortcuts, output-limits, rlhf-and-compute, training-data-bias
└── skills/
    ├── taste-skill/         # v2 experimental (1,206 lines)
    ├── taste-skill-v1/      # v1 원본 (226 lines)
    ├── gpt-tasteskill/
    ├── soft-skill/ minimalist-skill/ brutalist-skill/
    ├── redesign-skill/ output-skill/
    ├── image-to-code-skill/
    ├── imagegen-frontend-web/ imagegen-frontend-mobile/
    ├── brandkit/
    └── stitch-skill/
```

`research/laziness/` 디렉토리가 눈에 띈다. LLM의 게으름을 인지 지름길, 출력 한계, RLHF, 훈련 데이터 편향의 네 가지 근본 원인으로 나누고, 각각에 대한 완화 방법을 아키텍처 패턴, 파라미터 튜닝, 프롬프트 엔지니어링, 참조 프롬프트의 네 갈래로 정리한 조사 노트다. taste-skill의 규칙들이 어떤 관찰에서 나왔는지 이 노트가 뒷받침한다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 두 곳이다.

첫째는 저자가 `research/laziness/`에서 이 프로젝트를 스킬 팩이 아니라 하나의 가설로 다룬다는 점이다. "LLM은 항상 첫 번째 안전한 옵션을 뽑는다"라는 가설이 있고, 그 가설이 참이라는 실증을 `empirical-results.md`에 모아 두었고, 원인을 네 갈래로 분해하고, 각 원인에 대한 완화 기법을 별도 마크다운으로 정리했다. taste-skill의 규칙 문장들은 이 실증 위에 붙는다. 스킬을 만드는 게 목적이 아니라, LLM의 게으름을 다루는 방법론의 실증판이 스킬 팩으로 나타난 형태다.

둘째는 `high-end-visual-design`이 자기 스킬에 "Vanguard_UI_Architect"라는 페르소나 이름을 붙였다는 점이다. Claude Code에 스킬을 로드하는 순간, 그 세션의 자기 정체성이 "15만 달러 에이전시급 UI 아키텍트"로 재정의된다. 페르소나는 이 스킬이 강제하는 세부 규칙 전체를 자연스러운 자기 표현으로 만든다. `rounded-[calc(2rem-0.375rem)]`을 매번 계산하는 것이 자기 정체성의 일부라면, 그 계산이 반복되어도 어색하지 않다.

두 관찰은 같은 결로 이어진다. 스킬은 지침의 나열이 아니라 정체성의 이식이다. 저자는 "AI slop"을 슬픈 개별 실패가 아니라 개입 가능한 학습 편향으로 다루고, 그 편향을 페르소나 이식으로 회피한다. AI 코딩 에이전트에 규칙을 얹는 여러 방법 중 taste-skill의 접근이 지속 가능해 보이는 이유가 여기에 있다.

## 출처

저자: [Leonxlnx](https://github.com/Leonxlnx) (X: [@lexnlin](https://x.com/lexnlin))
프로젝트: [`taste-skill`](https://github.com/Leonxlnx/taste-skill)
홈페이지: [tasteskill.dev](https://tasteskill.dev)
공개 시점: 2026-02-19 초판, 2026-06-20 최신 커밋
라이선스: MIT (Copyright 2026 Leonxlnx)
