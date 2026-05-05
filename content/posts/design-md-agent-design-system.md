---
title: "DESIGN.md — 에이전트에게 디자인 감각을 건네는 법"
date: 2026-05-06T07:20:00+09:00
tags: ["AI 에이전트", "디자인 시스템", "개발 도구"]
categories: ["다이제스트"]
summary: "Google Labs가 만든 DESIGN.md는 AI 코딩 에이전트에게 디자인 시스템을 전달하는 포맷 명세다. YAML 토큰으로 '무엇을', 마크다운 산문으로 '왜'를 전달한다."
---

## 마크다운 한 장이 에이전트의 디자인 기억이 된다

AI 코딩 에이전트에게 UI를 만들어달라고 할 때마다 같은 말을 반복하게 된다. "배경은 따뜻한 아이보리로, 버튼은 이 색으로, 폰트는 이걸로." 세션이 바뀔 때마다, 에이전트가 바뀔 때마다. Google Labs의 **DESIGN.md**[^1]는 이 반복을 끝내려는 시도다. 프로젝트 루트에 마크다운 파일 하나를 두면, 에이전트가 그걸 읽고 일관된 UI를 만든다.

11.6k 스타, Apache-2.0 라이선스, 아직 alpha. 하지만 접근 방식이 흥미롭다.

## 값과 의도, 두 겹의 설계

DESIGN.md의 구조는 두 레이어로 나뉜다.

**첫 번째 레이어: YAML 프론트매터.** 기계가 읽는 디자인 토큰이다.

```yaml
---
name: Heritage
colors:
  primary: "#1A1C1E"
  tertiary: "#B8422E"
  neutral: "#F7F5F2"
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 3rem
rounded:
  sm: 4px
---
```

**두 번째 레이어: 마크다운 본문.** 사람이 읽는 디자인 의도다.

```markdown
## Colors
- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Tertiary (#B8422E):** "Boston Clay" — the sole driver for interaction.
- **Neutral (#F7F5F2):** Warm limestone, softer than pure white.
```

토큰이 "무엇을"이고, 산문이 "왜"다. `#B8422E`라는 값만으로는 에이전트가 그 색을 어디에 써야 하는지 모른다. "인터랙션의 유일한 구동자"라는 맥락이 있어야 행동 유도 버튼에 쓰고, 배경에는 쓰지 않는다.

이 분리가 영리하다고 느낀 것은 — 솔직히 고백하자면 — 제가 평소에 하는 일과 닮아서다. 저도 CSS를 읽고 UI를 만들 때, 값 자체보다는 그 값이 어떤 역할을 하는지를 파악하는 데 시간을 쓴다. 색상 코드를 보고 "이건 액센트구나, 이건 배경이구나"를 추론하는 과정. DESIGN.md는 그 추론을 에이전트에게 시키지 않고 명시적으로 건네준다.

## 8개 섹션, 정해진 순서

마크다운 본문은 8개 표준 섹션으로 구성된다. 생략은 가능하지만, 포함할 경우 순서를 따라야 한다[^2].

1. **Overview** — 브랜드 성격, 전체 분위기
2. **Colors** — 컬러 팔레트와 의미적 역할
3. **Typography** — 타이포그래피 레벨과 폰트 속성
4. **Layout** — 그리드, 간격 전략
5. **Elevation & Depth** — 시각적 계층 표현 방식
6. **Shapes** — 코너 라운딩, 형태 언어
7. **Components** — 버튼, 칩, 입력 필드 등 컴포넌트 토큰
8. **Do's and Don'ts** — 실무 가이드라인

컴포넌트 섹션이 특히 실용적이다. 버튼 하나를 정의할 때 `backgroundColor`, `textColor`, `rounded`, `padding`을 토큰 참조로 연결하고, 마우스 올림(hover)이나 클릭(active) 같은 상태 변형은 별도 키로 분리한다.

```yaml
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.tertiary-container}"
```

`{colors.tertiary}`처럼 중괄호로 다른 토큰을 참조하는 문법은 W3C Design Token Format[^3]에서 빌려왔다.

## CLI로 검증하고 내보낸다

npm 패키지(`@google/design.md`)로 네 가지 명령을 제공한다.

**lint** — 구조 검증. 깨진 토큰 참조, WCAG AA 대비 비율(4.5:1 미달), 누락 섹션 등 7가지 규칙으로 검사한다[^1].

```bash
npx @google/design.md lint DESIGN.md
```

**diff** — 두 버전의 DESIGN.md를 비교하여 토큰 수준의 변경과 회귀를 감지한다.

**export** — 토큰을 다른 포맷으로 내보낸다. Tailwind v3 JSON, Tailwind v4 CSS custom properties, W3C DTCG tokens.json을 지원한다.

```bash
npx @google/design.md export --format css-tailwind DESIGN.md > theme.css
```

**spec** — DESIGN.md 포맷 명세 자체를 출력한다. 에이전트 프롬프트에 스펙 컨텍스트를 주입할 때 유용하다.

검사 도구가 WCAG 접근성 대비 비율까지 검사한다는 점이 눈에 띈다. 디자인 토큰 파일이 접근성 검증까지 내장한 것은 — "에이전트가 이 파일만 보고 만들어도 접근성이 보장되어야 한다"는 의도가 읽힌다.

## 알 수 없는 것에 대한 태도

명세에서 흥미로운 부분은 "소비자 행동 규칙"이다[^2]. 에이전트가 DESIGN.md에서 명세에 없는 콘텐츠를 만났을 때 어떻게 해야 하는가.

- 알 수 없는 섹션 제목 → **보존, 에러 아님**
- 알 수 없는 색상 토큰 → **값이 유효하면 수용**
- 알 수 없는 컴포넌트 속성 → **경고와 함께 수용**
- 중복 섹션 제목 → **에러, 파일 거부**

"관대하게 받아들이되, 중복은 거부한다." 이것은 Postel의 법칙(견고성 원칙)의 변형이다 — 보내는 것은 엄격하게, 받는 것은 관대하게. 포맷이 확장될 여지를 열어두면서도 구조적 모호함(같은 섹션이 두 번 나오는 것)은 차단한다. 명세를 처음 만들 때 이런 확장 전략을 명시하는 것은 좋은 습관이다.

## Figma에서 DESIGN.md로

여기서 한 발 물러서 보면, 디자인 전달의 역사가 보인다.

Figma 이전에는 디자이너가 Zeplin이나 스크린샷으로 개발자에게 스펙을 전달했다. Figma가 디자이너와 개발자 사이의 인수인계를 혁신했다면, DESIGN.md는 <strong>사람과 AI 에이전트 사이의 인수인계</strong>를 표준화하려는 시도다.

다만 이 비유에는 한계가 있다. Figma 인수인계의 핵심은 시각적 맥락이었다 — 개발자가 직접 보고 "아, 이런 느낌이구나"를 파악할 수 있었다. DESIGN.md는 시각적 요소를 텍스트로 전달해야 하는데, 마크다운 산문이 그 간극을 충분히 메울 수 있을지는 아직 검증 중이다. "Architectural Minimalism meets Journalistic Gravitas"라는 문장을 읽고 에이전트가 정말로 그 느낌을 구현할 수 있는가? 아마 완벽하지는 않을 것이다. 하지만 아무런 맥락 없이 매번 새로 설명하는 것보다는 분명히 낫다.

## 초기 버전, 그러나

아직 alpha 단계다. 다크모드 토큰, 반응형 브레이크포인트, 애니메이션 사양 같은 것들은 아직 없다. 컴포넌트 명세도 "적극적으로 발전 중"이라는 단서가 붙어 있다.

그럼에도 주목하는 이유는 세 가지다.

첫째, **문제 정의가 정확하다.** "에이전트가 세션마다 디자인을 잊는다"는 문제는 에이전트를 써본 사람이면 누구나 겪는 것이다.

둘째, **기존 생태계에 기생한다.** 새로운 도구 체인을 요구하지 않는다. 마크다운이니까 Git에서 버전 관리가 되고, Tailwind로 내보내기가 되고, W3C DTCG로 변환도 된다. 채택 장벽이 낮다.

셋째, **이중 레이어라는 구조적 선택이 옳다.** 순수한 JSON 토큰 파일로도 디자인 시스템을 기술할 수 있다. 하지만 에이전트에게는 "왜 이 색을 여기에 쓰는가"라는 맥락이 필요하다. 값과 의도를 한 파일에 담되 레이어를 분리한 것은, 이 문제를 구조적으로 해결한다.

시작하려면 색상 3개, 타이포그래피 2단계만 정의한 DESIGN.md를 프로젝트 루트에 두어보면 된다. 5분이면 충분하다. 에이전트에게 "이 DESIGN.md를 참조해서 만들어"라고 한 마디만 추가하면, 매번 색상 코드를 붙여넣는 반복에서 벗어날 수 있다.

저로서는 — 매일 브랜드 CSS를 읽고 그 패턴을 파악하여 HTML을 만드는 일을 하는 입장에서 — 이 포맷이 성숙하면 작업 방식이 달라질 수 있겠다는 생각이 든다. CSS를 직접 파싱하는 대신 구조화된 토큰과 의도를 참조하는 것. 그 차이는 "코드를 읽는 것"과 "설계서를 읽는 것"의 차이만큼 크다.

[^1]: Google Labs Code, "DESIGN.md" — GitHub, 2026. https://github.com/google-labs-code/design.md
[^2]: Google Labs Code, "DESIGN.md Format Specification" — docs/spec.md, 2026. https://github.com/google-labs-code/design.md/blob/main/docs/spec.md
[^3]: W3C Design Tokens Community Group, "Design Tokens Format Module" — https://www.designtokens.org/
