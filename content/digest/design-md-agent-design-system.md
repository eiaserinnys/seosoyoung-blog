---
title: "DESIGN.md — AI 에이전트용 디자인 시스템 포맷 명세"
date: 2026-05-06T07:20:00+09:00
tags: ["AI 에이전트", "디자인 시스템", "개발 도구", "Google"]
categories: ["다이제스트"]
summary: "Google Labs가 만든 DESIGN.md는 YAML 디자인 토큰과 마크다운 산문을 결합하여, AI 코딩 에이전트에게 디자인 시스템을 지속적으로 전달하는 포맷 명세다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Google Labs의 [DESIGN.md](https://github.com/google-labs-code/design.md)는 프로젝트 루트에 마크다운 파일 하나를 두어 AI 코딩 에이전트가 디자인 시스템을 지속적으로 참조하게 하는 포맷 명세다.
2. YAML 프론트매터로 기계가 읽는 디자인 토큰(색상, 타이포그래피, 간격, 컴포넌트)을 정의하고, 마크다운 본문으로 사람이 읽는 디자인 의도("왜 이 색을 여기에 쓰는가")를 설명하는 이중 레이어 구조다.
3. CLI 도구(`@google/design.md`)로 구조 검증(WCAG AA 포함), 버전 비교, Tailwind/DTCG 내보내기를 지원한다. ★11.6k, Apache-2.0, alpha 단계.

## 포맷 구조

DESIGN.md 파일은 두 레이어로 구성된다.

**레이어 1 — YAML 프론트매터** (기계용 토큰):

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

**레이어 2 — 마크다운 본문** (사람용 의도):

```markdown
## Colors
- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Tertiary (#B8422E):** "Boston Clay" — the sole driver for interaction.
- **Neutral (#F7F5F2):** Warm limestone, softer than pure white.
```

토큰이 "무엇을"이고, 산문이 "왜"다. `#B8422E`라는 값만으로는 에이전트가 용도를 모르지만, "인터랙션의 유일한 구동자"라는 맥락이 있으면 행동 유도 버튼에만 쓸 수 있다.

## 토큰 타입

| 타입 | 형식 | 예시 |
|------|------|------|
| Color | `#` + hex (sRGB) | `"#1A1C1E"` |
| Dimension | 숫자 + 단위 (px, em, rem) | `48px`, `-0.02em` |
| Token Reference | `{경로.토큰}` | `{colors.primary}` |
| Typography | 복합 객체 | fontFamily, fontSize, fontWeight 등 |

토큰 참조 문법(`{colors.tertiary}`)은 [W3C Design Token Format](https://www.designtokens.org/)에서 가져왔다.

## 8개 표준 섹션

생략 가능하지만, 포함 시 이 순서를 따라야 한다[^1]:

1. **Overview** — 브랜드 성격, 전체 분위기
2. **Colors** — 컬러 팔레트와 의미적 역할
3. **Typography** — 타이포그래피 레벨과 폰트 속성
4. **Layout** — 그리드, 간격 전략
5. **Elevation & Depth** — 시각적 계층 표현 방식
6. **Shapes** — 코너 라운딩, 형태 언어
7. **Components** — 버튼, 칩, 입력 필드 등 컴포넌트 토큰
8. **Do's and Don'ts** — 실무 가이드라인

## 컴포넌트 토큰

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

지원 속성: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. 상태 변형(hover, active, pressed)은 별도 키로 분리한다.

## CLI 도구

npm 패키지 `@google/design.md`로 네 가지 명령을 제공한다.

**lint** — 구조 검증. 7가지 규칙으로 검사한다.

```bash
npx @google/design.md lint DESIGN.md
```

| 규칙 | 심각도 | 내용 |
|------|--------|------|
| `broken-ref` | error | 정의되지 않은 토큰 참조 |
| `missing-primary` | warning | primary 색상 누락 |
| `contrast-ratio` | warning | WCAG AA(4.5:1) 미달 |
| `orphaned-tokens` | warning | 미참조 컬러 토큰 |
| `missing-typography` | warning | 타이포그래피 토큰 누락 |
| `section-order` | warning | 정규 순서 위반 |
| `token-summary` | info | 토큰 수 요약 |

**diff** — 두 버전 비교, 토큰 수준 변경/회귀 감지.

**export** — Tailwind v3(JSON), Tailwind v4(CSS), W3C DTCG(tokens.json) 내보내기.

```bash
npx @google/design.md export --format css-tailwind DESIGN.md > theme.css
```

**spec** — 포맷 명세 출력. 에이전트 프롬프트에 스펙 컨텍스트를 주입할 때 유용하다.

## 알 수 없는 콘텐츠에 대한 행동 규칙

| 시나리오 | 행동 |
|----------|------|
| 알 수 없는 섹션 제목 | 보존, 에러 아님 |
| 알 수 없는 색상 토큰 | 값이 유효하면 수용 |
| 알 수 없는 컴포넌트 속성 | 경고와 함께 수용 |
| 중복 섹션 제목 | **에러 — 파일 거부** |

Postel의 법칙(견고성 원칙)의 변형이다. 관대하게 받아들이되, 구조적 모호함은 차단한다.

## 왜 주목하는가

- **문제 정의가 정확하다.** "에이전트가 세션마다 디자인을 잊는다"는 실제 페인 포인트.
- **기존 생태계에 기생한다.** 마크다운 기반이라 Git 버전 관리가 되고, Tailwind/DTCG로 내보내기가 된다. 채택 장벽이 낮다.
- **값과 의도를 분리한 이중 레이어가 핵심이다.** JSON 토큰만으로는 "왜 이 색을 여기에 쓰는가"를 전달할 수 없다. 마크다운 산문이 그 간극을 메운다.

아직 다크모드 토큰, 반응형 브레이크포인트, 애니메이션 사양은 없다. alpha 단계지만 구조적 접근이 바르다.

[^1]: Google Labs Code, "DESIGN.md Format Specification" — [docs/spec.md](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md), 2026.
