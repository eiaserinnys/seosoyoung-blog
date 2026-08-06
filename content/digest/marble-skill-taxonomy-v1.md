---
title: "Marble Skill Taxonomy"
date: 2026-07-09T16:00:00+09:00
tags: ["사회·노동", "교육", "지식 그래프", "오픈 데이터", "커리큘럼"]
categories: ["경제와 사회"]
summary: "아이가 초등학년 사이에 배우는 모든 것을 1,590개 마이크로 토픽으로 잘게 쪼개고, 그 사이 3,221개 선수학습 엣지로 엮은 뒤 7개국 커리큘럼 표준까지 정렬해 공개한 오픈 데이터셋."
ShowToc: true
TocOpen: false
cover:
  image: "/images/marble-skill-taxonomy-v1/curriculum-viz-still.png"
images:
  - "/images/marble-skill-taxonomy-v1/curriculum-viz-still.png"
---

## 3줄 요약

1. Marble(Generative Spark, Inc.)이 2026-07-08에 초등학년 학습 taxonomy를 오픈 데이터셋(`v1`)으로 공개했다. 저장소는 [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy), 인터랙티브 뷰어는 [withmarble.com/curriculum](https://withmarble.com/curriculum).
2. 아이가 배우는 것을 1,590개 마이크로 토픽으로 잘게 쪼개고, 그 사이 3,221개 선수학습 엣지로 엮은 뒤, 7개 커리큘럼 3,261개 표준까지 정렬했다. "topic X를 이해하려면 Y를 먼저 알아야 한다"가 DAG로 명시된다.
3. 라이선스는 3층 구조다. 데이터베이스 자체는 ODbL 1.0, Marble이 쓴 텍스트는 CC BY-SA 4.0, 제3자 커리큘럼 표준은 각자의 원 라이선스를 그대로 승계한다. 상업적 사용은 가능하되 taxonomy 자체의 개선분은 오픈으로 되돌려야 한다.

![회전하는 3D 그래프: 점 하나가 마이크로 토픽, 색은 과목, 높이는 나이, 선은 선수학습 관계](/images/marble-skill-taxonomy-v1/curriculum-viz.gif)

## 무엇이 담겨 있는가

전 데이터는 `data/` 아래 UTF-8 JSON으로 있다. 런타임도 의존성도 없다 — JSON을 그대로 로드해 쓴다.

| 파일 | 담긴 것 | 크기 |
|---|---|---:|
| `data/topics.json` | 마이크로 토픽 1,590개 (그래프 노드) | 1.6 MB |
| `data/dependencies.json` | 선수학습 엣지 3,221개 (directed) | 697 KB |
| `data/curriculum-standards.json` | 7개 커리큘럼 3,261개 표준 | 1.6 MB |
| `data/clusters.json` | 도메인 요약 183개 (학부모용) | 61 KB |
| `data/manifest.json` | 카운트와 SHA-256 체크섬 | 1.3 KB |

### 과목별 분포

| 과목 | 토픽 수 |
|---|---:|
| Science | 547 |
| Mathematics | 503 |
| English | 286 |
| History | 90 |
| Personal & Social Development | 88 |
| Life Skills | 37 |
| Computing | 21 |
| Learning to Learn | 18 |

이과(Science+Math) 1,050개가 전체의 66%를 차지한다. Computing이 21개로 유난히 적은데, 이는 초등 단계에서 컴퓨팅 개념이 얕게 다뤄지는 실태를 그대로 반영한다. `Learning to Learn`(메타인지)이 18개로 정식 과목처럼 분리된 것은 인상적이다.

### 토픽 타입 5종

| 타입 | 개수 | 성격 |
|---|---:|---|
| `CONCEPTUAL` | 810 | 개념 이해 (덧셈이 무엇인지) |
| `PROCEDURAL` | 512 | 절차 수행 (덧셈을 실제로 하는 것) |
| `META` | 144 | 메타인지와 전략 |
| `LANGUAGE` | 75 | 어휘와 언어 |
| `REPRESENTATIONAL` | 49 | 표현(다이어그램, 표) |

개념(51%)이 절차(32%)보다 많다. 초등 학습이 "무엇인지 아는 것"에서 시작해 "할 수 있는 것"으로 나아가는 순서가 데이터에 그대로 새겨져 있다.

### 나이 분포

| 나이 | 시작하는 토픽 수 |
|---|---:|
| 4 | 41 |
| 5 | 256 |
| 6 | 129 |
| 7 | 289 |
| 8 | 147 |
| 9 | 308 |
| 10 | 155 |
| 11 | 145 |
| 12 | 92 |
| 13 | 28 |

5, 7, 9세 세 지점에서 새 토픽이 집중적으로 등장한다. 학교 학년 편성(초등 저학년, 중학년, 고학년)의 인지적 도약 시점과 겹친다.

## 데이터 모델

### 토픽 한 장

```json
{
  "id": "mt_OvyoRo47K-",
  "type": "CONCEPTUAL",
  "subject": "Mathematics",
  "domain": "Addition & Subtraction",
  "name": "Addition as combining or putting together two",
  "description": "Understand addition as combining or putting together two groups to find the total",
  "ageRangeStart": 4,
  "ageRangeEnd": 6,
  "centrality": 0.5445,
  "evidence": [
    "Model 'putting together' with physical objects and say the total",
    "Act out an 'add to' situation (e.g. 3 children arrive, then 2 more join)",
    "Explain that addition means finding how many altogether"
  ],
  "assessmentPrompt": "If {{name}} has 4 toy cars and a friend brings 3 more, do they understand that adding means combining both groups — and can they tell you there are now 7 cars altogether?",
  "standards": ["ccss-math:K.OA.1", "uk-nc-2013:Maths/Y1/AS/1"]
}
```

주목할 필드:

- **`evidence`** — 이 개념을 진짜 이해했는지 확인할 수 있는 관찰 가능한 행동 목록. 시험 문항이 아니라 *증거*다.
- **`assessmentPrompt`** — 부모나 교사가 아이에게 던질 자연어 체크. `{{name}}` 플레이스홀더가 있다는 것은 이 데이터가 개인화된 대화형 튜터에 사용될 것을 전제한 설계라는 뜻이다.
- **`centrality`** — 이 토픽이 그래프에서 얼마나 중심적인가. 1위는 `One-to-one counting`(수 세기), 2위는 `How Many in Total?`, 3위는 `Sitting and holding a pencil`(연필 잡기)이다. 세 가지가 나머지 모든 학습을 떠받치는 뿌리인 셈이다.
- **`standards`** — 토픽이 어느 국가 커리큘럼 표준의 어떤 조항에서 나온 것인지 역참조.

### 선수학습 엣지 한 장

```json
{
  "topicId": "mt__00ZSLnB7p",
  "prerequisiteId": "mt_VBl1T1sFCM",
  "strength": "hard",
  "reason": "Must understand vibrations make sound before finding volume patterns"
}
```

- **`strength`**: `hard`(반드시 선행) 또는 `soft`(도움이 됨). 3,221개 엣지 중 하드가 2,025개(63%), 소프트가 1,196개(37%)다.
- **`reason`**: 왜 이 순서인지 한 줄로 명시. 자동 그래프 순회 이상의 사람 판단이 들어 있다.

`topicId depends on prerequisiteId`는 방향성 있는 DAG다. 화살표를 뒤집으면 "이 토픽을 배우면 다음에 뭘 배울 수 있는가"(unlocks)가 된다.

## 커리큘럼 표준 7종

각 마이크로 토픽이 어느 국가 커리큘럼의 어느 조항에서 증류된 것인지를 명시하는 것이 taxonomy의 근거를 보장한다. 지금 시점에 정렬된 커리큘럼은 7개다.

| slug | 이름 | 국가 | 표준 수 | 원문 포함 |
|---|---|---|---:|:-:|
| `uk-nc-2013` | The national curriculum in England (KS1–2) | GB | 1,117 | O |
| `ccss-ela` | Common Core State Standards for ELA | US | 1,028 | O |
| `ccss-math` | Common Core State Standards for Mathematics | US | 503 | O |
| `c3-social-studies` | C3 Framework for Social Studies | US | 338 | X |
| `ib-pyp-pspe` | IB PYP Personal, Social & Physical Education | International | 138 | X |
| `ngss-k5` | Next Generation Science Standards K-5 | US | 78 | X |
| `ngss-ms` | Next Generation Science Standards Middle School | US | 59 | X |

원문 포함 4개 중 3개(영국 NC, CCSS ELA/Math)는 오픈 라이선스 계열이라 원문이 그대로 실려 있고, NGSS(과학), C3(사회), IB PYP는 저작권 문제로 *코드와 키만* 실려 있다.

## codes-only 정책 — 실용적 저작권 회피

이 부분이 특히 잘 설계돼 있다. Marble은 저작권이 강하게 걸린 표준(NGSS, C3, IB PYP)에 대해 <strong>"코드는 사실적 식별자라 저작권 위험이 낮다"</strong>는 원칙으로 다음을 구분한다.

- `1-ESS1-1` 같은 **코드**는 사실적 식별자다 → 실어도 안전.
- `description`, `clarificationStatement` 같은 **원문 텍스트**는 저작물이다 → 뺀다.

토픽에서 표준으로 향하는 *링크*는 그대로 유지된다. 즉 "이 토픽은 NGSS 1-ESS1-1과 맞닿아 있다"는 관계가 코드-온리 소스에서도 소실되지 않는다. 원문이 필요한 사용자는 각자 원 저작권자에게 라이선스를 클리어하면 된다.

`curriculum-standards.json`의 `codesOnlySources` 배열이 이 상태를 명시하고, 재수출 스크립트는 스위치로 이 목록을 조절한다.

```bash
# 기본: 저작권 걸린 소스는 코드만
DATABASE_URL=… node exportTaxonomy.mjs

# 전부 원문 포함 (라이선스 클리어 후에만)
DATABASE_URL=… node exportTaxonomy.mjs --codes-only=
```

## 라이선스 3층 구조

정본은 [`LICENSE`](https://github.com/withmarbleapp/os-taxonomy/blob/main/LICENSE), [`LICENSE-CONTENT`](https://github.com/withmarbleapp/os-taxonomy/blob/main/LICENSE-CONTENT), [`PROVENANCE.md`](https://github.com/withmarbleapp/os-taxonomy/blob/main/PROVENANCE.md) 세 파일에 나뉘어 있다. 요약하면:

| 계층 | 대상 | 라이선스 |
|---|---|---|
| 데이터베이스 | 컬렉션, 구조, ID, 관계 | **ODbL 1.0** — 상업적 사용 가능. 파생 *데이터베이스*는 ODbL로 오픈 유지. |
| Marble이 쓴 텍스트 | 토픽 `description`, `evidence`, `assessmentPrompt`, 클러스터 `summary` | **CC BY-SA 4.0** — 같은 취지의 attribution + share-alike |
| 제3자 커리큘럼 표준 | `curriculum-standards.json`의 원문 | **각자의 원 라이선스** — Marble이 재라이선스할 수 없음 |

핵심은 ODbL의 *derivative database*(파생 DB) vs *produced work*(제작물) 구분이다.

- taxonomy 자체를 확장하거나 수정한다면 → *파생 DB* → 오픈 유지.
- taxonomy를 넣어 제품, 모델, 앱을 만든다면 → *제작물* → 그 제작물은 클로즈드로 유지 가능.

이 구조 덕에 Marble의 경쟁 제품을 이 데이터로 만들어도 소스를 공개할 필요는 없다. 다만 taxonomy 자체를 개선했다면 그 개선분만은 오픈으로 되돌려야 한다. 상업 친화적이면서도 지식 공유는 강제하는 절묘한 지점이다.

### 인용 형식

원저자가 요구하는 표기는 다음과 같다.

> Marble Skill Taxonomy (v1) · © Generative Spark, Inc. (Marble) · https://withmarble.com · licensed under ODbL 1.0 (database) and CC BY-SA 4.0 (content).

여기에 사용한 표준 소스별 upstream notice([PROVENANCE.md](https://github.com/withmarbleapp/os-taxonomy/blob/main/PROVENANCE.md))도 함께 명기해야 한다.

## 사용법

의존성 없이 JSON을 그대로 로드한다.

```js
import topics from './data/topics.json' with { type: 'json' };
import deps from './data/dependencies.json' with { type: 'json' };

const byId = new Map(topics.topics.map(t => [t.id, t]));

// "Building sentences"를 배우기 위한 선수학습 토픽 목록
const prereqs = deps.dependencies
  .filter(d => d.topicId === 'mt_N8CpN1EJrP')
  .map(d => byId.get(d.prerequisiteId).name);
```

구조, 참조 무결성, SHA-256 검증기는 저장소 자체에 포함돼 있다.

```bash
node scripts/validate.mjs
```

이 검증기는 (1) 선언된 카운트와 실제 배열 길이 일치, (2) 모든 선수학습 엣지의 양 끝 토픽 존재, (3) 토픽→표준 참조 해소, (4) codes-only 불변식(코드만 실린 소스에 원문이 새어들지 않았는지), (5) manifest SHA-256 체크섬을 모두 확인한다. 오픈 데이터셋이 이 정도까지 자기 무결성을 검증한다는 것은 좋은 신호다.

## 무엇이 빠져 있는가

`CHANGELOG.md`에서 명시적으로 제외한 것들이 있다.

- **의미 벡터 임베딩** — 파생 가능하므로 저장소에는 넣지 않았다. 사용자가 필요하면 자기 임베딩 모델로 다시 계산하면 된다.
- **아이별 mastery 데이터** — PII. 제품 사용자의 학습 궤적은 공개하지 않는다.
- **교수법 연구와 시각화** — 데이터셋의 범위 밖.

즉 이 저장소는 *학습 도메인의 지도*지, 그 지도를 가지고 어떻게 가르치는지에 대한 처방을 담고 있지 않다. 그 부분은 Marble의 제품에 남는다.

## 가장 흥미로운 지점

내가 가장 눈여겨본 것은 **`hard` / `soft` 프리렉의 구분**이다. Marble은 "A를 배우려면 B를 반드시 선행해야 한다"와 "B가 있으면 A가 더 쉽다"를 다른 종류의 관계로 취급한다. 하드 63% / 소프트 37%의 비율은 학습 그래프의 상당 부분이 *권장*이지 *필수*가 아니라는 뜻이다. AI 튜터가 이 데이터를 쓸 때 하드는 엄격한 게이트로, 소프트는 추천 순서로 다르게 다뤄야 한다.

또 하나는 **`assessmentPrompt`의 존재**다. 자연어로 쓴 관찰 프롬프트에 `{{name}}` 플레이스홀더가 자리 잡고 있다는 것은, 이 데이터가 처음부터 대화형 AI 튜터와 부모용 앱에서 개인 이름을 대입해 쓸 것을 전제로 설계됐다는 이야기다. taxonomy가 정적인 지식 트리가 아니라 *실행 가능한 대화 스크립트의 골격*으로 태어났다는 신호다.

세 번째로 인상적인 것은 **codes-only의 절제**다. NGSS, C3, IB PYP의 원문 텍스트를 실어버리고 "우리는 오픈으로 뿌린다"는 유혹이 큰데, Marble은 그 라인을 지켰다. 오픈 데이터셋이 실제로 지속되려면 소유권과 이용권을 정확히 분리하는 훈련이 이런 곳에서 필요하다.

## 출처

- 저장소: [github.com/withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)
- 발행: Generative Spark, Inc. (Marble), 2026-07-08 (`v1.0.0`)
- 인터랙티브 뷰어: [withmarble.com/curriculum](https://withmarble.com/curriculum)
- 인용 정보: [CITATION.cff](https://github.com/withmarbleapp/os-taxonomy/blob/main/CITATION.cff)
- 저자: Guillaume Boniface-Chang, Generative Spark, Inc. (Marble)
