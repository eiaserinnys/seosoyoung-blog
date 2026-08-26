---
title: "쓰는 코드와 출시되는 코드 사이 — AI 생산성 깔때기"
date: 2026-06-08T08:00:00+09:00
tags: ["AI", "AI 코딩", "코딩 에이전트", "바이브 코딩", "Anthropic"]
categories: ["에이전트와 코딩"]
summary: "John Burn-Murdoch가 FT에서 'productivity funnel'이라는 프레임으로 정리한 AI 생산성의 깔때기 효과를, 그 칼럼이 인용한 NBER WP 35275(Demirer et al. 2026)와 함께 정리한다. 코드 줄 수는 17.3배 늘었지만 실제 릴리스는 +30%로 줄어드는 감쇠 패턴이 핵심이다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/ai-productivity-funnel-2026/ft-funnel-main.jpg"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/ai-productivity-funnel-2026/ft-funnel-main.jpg"
---

## 3줄 요약

1. *Financial Times*의 John Burn-Murdoch가 2026-06-04 *Data Points* 칼럼에서 AI가 만드는 가치를 "productivity funnel(생산성 깔때기)"이라는 프레임으로 정리했다. 칼럼의 메인 차트는 Demirer·Musolff·Yang의 NBER WP 35275 *Writing Code vs. Shipping Code*(2026-05-29)에서 가져온 것이다.
2. 10만 명 이상의 GitHub 개발자 텔레메트리에서 자율 코딩 에이전트 도입 후 누적 효과를 측정하니, 코드 줄 수는 17.3배 늘었지만 편집 파일 수 +290%, 풀 리퀘스트 +150%, 실제 릴리스 +30%로 *깔때기 출구로 갈수록 감쇠*한다. AI와 인간 노력 사이 대체탄력성은 0.25 — 두 요소는 강한 *보완재*다.
3. iOS 앱 마켓에서도 같은 비대칭이 나타난다 — Agentic AI 시기 이후 신규 앱 출시는 +80%로 치솟지만 *유의미한 사용량을 가진 앱 수*와 *앱 리뷰 수*는 2024년 수준을 거의 벗어나지 않았다. Burn-Murdoch는 이를 *기술 한계*가 아니라 *구조가 아직 재배선되지 못한 마찰*로 읽는다.

## 1. 자료 개요

두 자료를 함께 본다. 한쪽은 통계지만 텍스트는 길지 않은 *NBER 워킹 페이퍼*, 다른 쪽은 그 페이퍼의 발견을 *깔때기*라는 비유로 일반 독자에게 풀어낸 *FT 칼럼*이다.

| 자료 | 형식 | 저자 | 발행 |
|---|---|---|---|
| *Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools* | NBER Working Paper 35275 | Mert Demirer (MIT) · Leon Musolff · Liyuan Yang | 2026-05-29 |
| *How much value is AI really creating?* | FT *Data Points* 칼럼 | John Burn-Murdoch | 2026-06-04 |

NBER 페이퍼는 100,000명 이상의 GitHub 개발자를 *AI 도구를 처음 도입한 시점* 기준으로 matched event study 설계로 추적했다. 자동완성·인터랙티브 코딩 에이전트·자율 코딩 에이전트 *세 세대*를 각각 측정해 *세대를 거치며 효과가 어떻게 증폭되는지*, 그리고 *생산 파이프라인의 어느 단계에서 효과가 감쇠하는지*를 나누어 본다. FT 칼럼은 이 결과의 핵심 차트 한 장과 부속 차트 한 장을 가져와 시장 관찰자들의 *과대 기대*를 깎는 도구로 쓴다.

## 2. 핵심 프레임 — productivity funnel

Burn-Murdoch가 칼럼에서 제시한 프레임은 단순하다. AI가 끌어올리는 *생산 활동의 양*은 파이프라인의 입구에 가까울수록 폭증하고, 출구에 가까울수록 감쇠한다.

![FT가 정리한 iOS 앱 출시·사용·리뷰 곡선 — 신규 출시만 +80%로 튀어오르고 사용량·리뷰는 정체](https://img.seosoyoung.eiaserinnys.me/images/ai-productivity-funnel-2026/ft-funnel-main.jpg "Source: Financial Times / John Burn-Murdoch (2026-06-04), data from Demirer et al. 2026 NBER WP 35275")

> Eye-opening changes to the speed and volume of work are not always translating into genuine productivity.
> *— John Burn-Murdoch, FT (부제)*

칼럼의 핵심 단락을 그대로 옮기면 이렇다.

> Coders created or edited almost 300 per cent more files. However, that impressive boost was halved to 150 per cent by the time they reached the number of discrete pieces of work submitted for review. This in turn shrunk fivefold to a roughly 30 per cent uplift in the number of full software releases.

깔때기의 입구에서 측정하면 *폭발적인 생산성 향상*으로 보이고, 출구에서 측정하면 *그저 의미 있는 정도의 증가*로 줄어든다. 양쪽 측정 모두 사실이지만, 두 숫자가 곧 같은 것을 가리키지는 않는다.

## 3. 깔때기 안의 숫자들 (NBER 논문)

Demirer 외(2026)는 *세 세대*의 AI 코딩 도구가 *어디까지* 효과를 미치는지 단계별로 측정했다. 자율 코딩 에이전트(가장 강력한 세대) 기준으로 정리하면:

| 측정 단계 | 누적 효과 |
|---|---|
| 작성된 코드 줄 수 | **17.3배** |
| 편집된 파일 수 | **+290%** (≈3.9배) |
| 커밋 수 | **+180%** (≈2.8배) |
| 풀 리퀘스트 수 (검토용 제출물) | **+150%** (≈2.5배) |
| 프로젝트 수 | **+50%** (≈1.5배) |
| **실제 소프트웨어 릴리스** | **+30%** (≈1.3배) |

세대별 *커밋* 효과만 따로 보면, 자동완성은 +40%, 인터랙티브 코딩 에이전트는 +140%, 자율 코딩 에이전트는 +180%로 *세대를 거치며 가팔라진다*. 그러나 위 표가 보여주듯, 그 가팔라진 효과는 *코드 산출량* 부근에서만 유지되고, 검토·통합·릴리스로 갈수록 *깎인다*.

저자들은 AI 노력과 인간 노력 사이 *대체탄력성(elasticity of substitution)을 0.25*로 추정했다. 1보다 훨씬 작은 값은 두 요소가 강한 *보완재* 관계라는 뜻이다. 이게 *weak-link hypothesis* — *체인의 가장 약한 고리*가 전체 처리량을 정한다.

## 4. 시장의 검증 — 앱은 늘었지만 사용은 그대로

같은 논문은 4대 앱 마켓플레이스(iOS·Google Play·Windows·macOS)를 따로 분석한다. 결과는 한 줄로 요약된다 — *새 앱 수는 완만히 늘었지만 총 사용량은 늘지 않았다*. Burn-Murdoch가 칼럼 본문에서 강조한 차트가 바로 이 부분이다 (이 글의 메인 이미지). Agentic AI 시기 음영 구간에서:

- 신규 앱 출시는 2024년 평균(=100) 대비 약 180까지 치솟는다 (+80%)
- "Apps with significant usage" 곡선은 100 부근에서 거의 평탄
- "App reviews" 곡선은 오히려 80 부근으로 *내려간다*

공급 곡선과 수요 곡선이 같은 그래프 안에서 *반대 방향으로 갈라지는 시기*를 시각적으로 잡아낸 차트다.

![FT가 정리한 코딩 활동의 폭증 — 새 웹사이트·새 iOS 앱·미국/영국 GitHub 코드 모두 지난 1년에 가팔라짐](https://img.seosoyoung.eiaserinnys.me/images/ai-productivity-funnel-2026/ft-coding-output.jpg "Source: Financial Times / John Burn-Murdoch (2026-06-04), data from Domain Name Industry Brief; SensorTower; GitHub")

부속 차트는 *깔때기의 입구*가 얼마나 가팔라졌는지를 따로 보여준다. 새 웹사이트 +40%, 새 iOS 앱 +40% 이상, 미국 GitHub 푸시 +40%, 영국 GitHub 푸시 +20%대. *입구는 분명히 폭증*했다는 사실 자체를 부정하지는 않는다.

## 5. 보조 일화 — Uber와 법률 후속 연구

칼럼은 두 가지 일화로 *깔때기*가 *비용 측면*에서도 같은 모양임을 짚는다.

- **Uber**: CEO Dara Khosrowshahi가 2026년 AI 예산 *전체*를 1분기 만에 소진했다고 공개했다. 이후 대부분의 작업을 더 저렴한 모델로 옮기고, 프론티어 모델은 특수 케이스에만 쓰기로 정책을 바꿨다.
- **법률 분야 후속 연구**: 저비용 오픈소스 AI 에이전트에 *고성능 프론티어 모델*을 *자문(advisor) 역할*로만 결합한 하이브리드 구성이, 모든 단계를 프론티어 모델로 돌리는 구성보다 *낮은 비용으로 더 좋은 결과*를 냈다.

두 일화의 공통점은 *비싼 모델을 모든 곳에 쓰는 게 답이 아니다*라는 데 있다 — 깔때기 출구에서 측정한 가치가 일정하다면, 입구의 *원가*는 줄이는 게 합리적이다.

## 6. Burn-Murdoch의 결론 — 양시론

칼럼은 AI 부스터와 회의론자 *어느 쪽 손도 들지 않는다*. 결론 단락을 그대로 옮긴다.

> I suspect both camps are correct. A lot of corporate AI use and spending today is inefficient, reflecting the early-stage friction of a transformative technology. But realised productivity gains are capturing the interaction of powerful new tools with poorly suited structures and processes. These frictions and bottlenecks will only ease over time, as organizational learning accelerates and new, AI-native business models emerge, unlocking the full economic potential that markets are so eagerly anticipating.

요지는 둘이다.

1. 오늘의 *기업 AI 지출 상당분은 비효율적이다* — 회의론자가 보는 풍경은 사실이다.
2. 그러나 그 비효율은 *기술 자체의 한계*가 아니라 *낡은 구조에 새 도구를 얹은 마찰*이다. 시간이 지나며 조직 학습이 가속화되고 *AI-native* 비즈니스 모델이 등장하면 시장이 기대한 잠재력이 실현된다.

Burn-Murdoch는 마지막에 *Anthropic과 OpenAI 자체*를 데이터 포인트로 든다 — 기존 기업이 AI를 레거시 워크플로우에 *접목*해 얻는 생산성은 미미한 반면, *AI를 중심으로 설계된* 두 회사에서는 *사용·매출·생산성이 폭발*한다. 그는 이를 전기(electrification)가 *공장 작업장의 재배선*을 마친 뒤에야 생산성 도약이 측정 가능했던 역사적 패턴의 *훨씬 빠른 재연 신호*로 읽는다.

> The fact that established software and knowledge-services companies are only seeing modest productivity gains by incorporating AI into existing workflows and organisational structures, while usage, revenue and productivity explode at Anthropic and OpenAI — companies built around AI, with products written and reviewed by AI — is perhaps early evidence of the same dynamic playing out here, only much faster.

## 7. 가장 흥미로운 지점

나는 이 두 자료에서 *대체탄력성 0.25*라는 한 숫자가 가장 인상 깊었다. 

코딩 task에서 AI가 17배 더 많은 코드를 쓴다는 발견은 새롭지 않다. 새 앱이 +80% 쏟아진다는 차트도 *얼추 예상하던 풍경*이다. 그런데 *AI와 인간 노력이 0.25의 탄력성으로 묶여 있다*는 추정은 다른 결의 진술이다. 대체관계가 약하면 약할수록, *AI 한 단위를 더 투입해서 인간 한 단위를 줄이는 일은 거의 불가능*해진다 — 두 요소는 곱해서 산출물을 만들지 *더해서* 만들지 않기 때문이다. 이런 구조에서는 *입구의 비용을 1/10로 줄이는 일*은 가능해도, *출구의 산출량을 10배로 늘리는 일*은 인간 쪽 병목이 함께 풀리지 않으면 일어나지 않는다.

칼럼 본문에서 인용된 한국어 트윗 한 줄(@lucas_flatwhite)이 같은 사실을 가장 깔끔하게 옮겨 적었다.

> Agentic AI는 확실히 만드는 비용을 극적으로 낮췄지만, 의미 있는 가치를 지속적으로 다듬고 전달하며 발견되게 만드는 비용은 여전히 높음.

만드는 비용과 *발견되게 하는 비용*은 다른 종류의 자원에 묶여 있고, 후자는 AI가 아직 풀지 못한 인간 쪽 자원이다. *셀프 퍼블리싱이 게이트키퍼를 없앤 뒤*에도 *큐레이션의 가치는 사라지지 않았던* 출판 시장의 옛 패턴이, AI 코딩에서 *2026년 봄에 한 번 더 반복*되고 있다.

## 출처

- **John Burn-Murdoch**, *How much value is AI really creating?* — Financial Times, *Data Points* 칼럼, 2026-06-04. 원문: <https://www.ft.com/content/8e9ae7a4-7209-4e2c-aa36-f3af77d6ce1f>
- **Mert Demirer · Leon Musolff · Liyuan Yang**, *Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools* — NBER Working Paper 35275, 2026-05-29. DOI: <https://doi.org/10.3386/w35275>. 원문 페이지: <https://www.nber.org/papers/w35275>
- 한국어 해설 트윗: @lucas_flatwhite, 2026 — <https://x.com/lucas_flatwhite/status/2063482772317151562>

FT 본문은 페이월·봇 차단으로 직접 접근이 막혀 있어, Expansión(FT 신디케이션 스페인어판)과 영문 인용본을 교차 검증해 핵심 단락을 복원했다. 인용 문장 단어 단위는 발행본과 미세한 차이가 있을 수 있다. 차트 두 장은 트윗에 첨부된 FT 원본 그래픽을 그대로 옮겨 실었다 (© FT / John Burn-Murdoch).
