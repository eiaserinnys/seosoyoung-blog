---
title: "X For You Feed Algorithm (xAI, 2026)"
date: 2026-05-16T09:00:00+09:00
tags: ["AI", "추천 시스템", "트랜스포머", "오픈소스", "xAI"]
categories: ["다이제스트"]
summary: "xAI가 X(트위터) For You 피드의 추천 시스템을 오픈소스로 공개했다. Grok-1 기반 트랜스포머가 수공 피처 없이 engagement sequence만 보고 직접 학습하며, 2026-05-15 업데이트로 사전학습 mini Phoenix 체크포인트와 end-to-end 추론 파이프라인이 함께 풀려 외부 재현이 가능해졌다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. xAI가 X(트위터) For You 피드를 떠받치는 추천 시스템을 오픈소스로 공개했다 (Apache 2.0). Home Mixer / Thunder / Phoenix / candidate-pipeline 4개 컴포넌트로 분리되어 있으며, Grok-1 기반 트랜스포머가 ranking을 담당한다.
2. 핵심 설계는 "수공 피처와 휴리스틱을 모두 제거하고 트랜스포머가 engagement sequence를 직접 학습한다"는 것. 후보끼리 attention을 차단하는 candidate isolation, 다중 해시 기반 임베딩, 15개 행동 확률을 동시 예측하는 multi-action head가 핵심 디자인 결정이다.
3. 2026-05-15 업데이트로 단순 코드 공개를 넘어 *돌아가는 시스템*이 풀렸다. 사전학습 mini Phoenix 체크포인트 (256-dim, 4 heads, 2 layers, 약 3GB)가 Git LFS로 배포되어 훈련 없이 즉시 추론할 수 있고, 537K 스포츠 글 데모 코퍼스와 예시 사용자 시퀀스도 포함되어 외부 연구자가 "같은 입력으로 같은 추천"을 재현할 수 있게 됐다.

## 시스템 구조 — 4개 컴포넌트의 역할 분리

| 컴포넌트 | 언어/런타임 | 역할 |
|---|---|---|
| **Home Mixer** | Rust | 오케스트레이션 레이어. gRPC `ScoredPostsService`를 노출하고 단계별 파이프라인을 조립한다. |
| **Thunder** | Rust | In-memory post store. Kafka 이벤트를 받아 팔로우 계정의 최근 글을 sub-millisecond에 서빙한다. |
| **Phoenix** | Python / JAX | ML 컴포넌트. retrieval(two-tower)과 ranking(트랜스포머)을 모두 담당한다. |
| **candidate-pipeline** | Rust crate | 추천 단계를 7개 트레이트로 추상화한 재사용 프레임워크. |

데이터 저장(Thunder)과 ML 연산(Phoenix)을 별도 서비스로 분리해 언어와 런타임을 각자에 맞게 최적화한 점이 특징이다. Rust로 된 가벼운 인-메모리 저장소가 in-network 후보를 즉답하고, JAX로 된 무거운 트랜스포머가 ranking을 처리한다.

## Retrieval → Ranking 두 단계 파이프라인

Phoenix는 추천을 두 단계로 분리한다.

```
User → [Stage 1: Retrieval]  → [Stage 2: Ranking]   → Feed
        Two-Tower              Transformer
        수백만 → 1,000개       1,000개 → 정렬
```

- **Stage 1 Retrieval** — User Tower와 Candidate Tower가 각각 임베딩을 생성하고 dot-product 유사도로 top-K(약 1,000개)를 뽑는다. ANN 검색에 가까운 가벼운 단계다.
- **Stage 2 Ranking** — 뽑힌 후보를 더 표현력 있는 트랜스포머에 넣어 최종 순위를 매긴다. 무겁지만 정확한 모델을 좁은 후보 집합에만 적용하는 전형적 추천 시스템 패턴이다 (YouTube의 candidate generation + ranking 계열).

## In-Network · Out-of-Network 통합 랭킹

후보 소스는 두 갈래다.

- **Thunder** — 팔로우 계정의 최근 글 (in-network).
- **Phoenix Retrieval** — 글로벌 코퍼스에서 ML 유사도로 발굴한 글 (out-of-network).

두 후보는 같은 Phoenix 트랜스포머에 입력되어 *동일한 점수 체계*로 ranking된다. 즉 "팔로우 글이 무조건 우대"가 아니라, 사용자의 engagement history에 비추어 더 끌릴 만한 쪽을 고르는 구조다. OON Scorer가 별도로 score 보정을 더하긴 하지만 본질은 통합 랭킹이다.

## 핵심 디자인 결정 5가지

### 1. 수공 피처 제거 — 트랜스포머가 모든 것을 학습

> We have eliminated every single hand-engineered feature and most heuristics from the system. The Grok-based transformer does all the heavy lifting...

콘텐츠 관련성 신호를 사람이 디자인하지 않는다. Grok 기반 트랜스포머가 사용자의 engagement sequence (좋아요·답글·리포스트·dwell 등)만 보고 직접 학습한다. 결과적으로 데이터 파이프라인과 서빙 인프라의 복잡도가 크게 줄었다는 주장이다.

### 2. Candidate Isolation — 후보끼리 attention 차단

랭킹 트랜스포머의 attention mask가 핵심이다. User/History 토큰끼리는 양방향으로 attention을 허용하지만, **Candidate 토큰은 자기 자신만 보고 (diagonal only) 다른 candidate는 보지 못한다**. 후보가 user/history는 참조하되 서로는 격리되는 구조다.

```
                    ATTENTION MASK (요약)
                ┌──────┬──────────┬─────────────┐
                │ User │ History  │ Candidates  │
    ┌───────────┼──────┼──────────┼─────────────┤
    │ User      │  ✓   │   ✓      │     ✗       │
    │ History   │  ✓   │   ✓      │     ✗       │
    │ Candidate │  ✓   │   ✓      │  diagonal   │
    └───────────┴──────┴──────────┴─────────────┘
```

효과는 두 가지다.

1. 한 게시물의 점수가 같은 배치에 어떤 다른 게시물이 들어왔는지에 *의존하지 않으므로* 점수가 일관되고 캐싱 가능하다.
2. 배치 구성을 자유롭게 바꿔도 점수가 안정적이다.

서빙 시점의 캐싱 가능성을 모델 구조 자체로 보장한 영리한 설계다.

### 3. 해시 기반 임베딩 — vocab 1M에 hash 2개

User/Item/Author ID를 임베딩 테이블에 직접 매핑하지 않고 *복수의 해시 함수*로 lookup한다. mini config 기준 vocab 1,000,000 × hashes 2 — ID 하나당 두 개의 해시 인덱스에서 임베딩을 가져와 합친다. Bloom-filter 스타일의 다중 해시로 충돌 영향이 분산된다.

효과:

- 새 사용자/게시물에도 즉시 임베딩이 생긴다 (콜드 스타트 우회).
- ID 공간이 무한해도 임베딩 테이블 크기는 유한하게 고정된다 (어휘 폭발 대응).

### 4. 멀티 액션 예측과 가중치 합 스코어링

랭킹 모델은 단일 "관련성" 점수가 아니라 15가지 행동 확률을 동시에 예측한다.

```
P(favorite), P(reply), P(repost), P(quote), P(click),
P(profile_click), P(video_view), P(photo_expand), P(share),
P(dwell), P(follow_author),
P(not_interested), P(block_author), P(mute_author), P(report)
```

최종 점수는 가중치 합이다.

```
Final Score = Σ wᵢ × P(actionᵢ)
```

좋아요·리포스트·공유 같은 *긍정 행동*은 양의 가중치를, 차단·뮤트·신고 같은 *부정 행동*은 음의 가중치를 가진다. 이 구조의 함의는 두 가지다.

1. 비즈니스 우선순위가 바뀌어도 모델 재학습 없이 *가중치만* 조정해 새 목표에 맞출 수 있다.
2. 부정 신호가 양의 신호와 같은 비중으로 결합되어 "끌리지만 해롭지 않은" 콘텐츠를 강제한다.

### 5. Composable Pipeline — 실행 엔진과 비즈니스 로직 분리

candidate-pipeline crate는 추천 단계를 7개 트레이트로 추상화한다.

| 트레이트 | 역할 |
|---|---|
| `QueryHydrator` | 요청 시점에 사용자 컨텍스트(engagement history, following list 등) 페치 |
| `Source` | 후보 수집 |
| `Hydrator` | 후보별 메타데이터 enrichment |
| `Filter` | 부적격 후보 제거 |
| `Scorer` | 점수 계산 |
| `Selector` | 정렬 + top-K 선택 |
| `SideEffect` | 비동기 후처리 (캐싱·로깅) |

프레임워크가 독립 단계의 병렬 실행과 단계별 graceful 에러 핸들링·로깅을 일괄 제공하므로, 새 소스/필터/스코어러를 추가할 때는 *비즈니스 로직만* 작성하면 된다. 추천 도메인에 *플러그인 아키텍처*를 적용한 사례다.

## 2026-05-15 업데이트의 의의

이번 릴리스가 단순 리포 갱신을 넘어선 사건인 이유는 *재현 가능한 시스템*이 처음으로 외부에 풀렸다는 점이다.

### 1. End-to-end 추론 파이프라인

`phoenix/run_pipeline.py`가 retrieval → ranking을 한 진입점에서 실행한다 (이전의 분리되어 있던 `run_ranker.py` + `run_retrieval.py`를 대체). 외부 연구자가 production에서 두 단계가 합쳐지는 방식을 그대로 재현할 수 있다.

### 2. 사전학습 mini Phoenix 체크포인트 공개

```
oss-phoenix-artifacts/
  retrieval/
    model_params.npz          # ~3 MB
    embedding_tables.npz      # ~1.4 GB
    config.json
  ranker/
    model_params.npz          # ~3 MB
    embedding_tables.npz      # ~1.4 GB
    config.json
  sports_corpus.npz           # 537K 스포츠 글
  example_sequence.json       # NFL/NBA/NHL 좋아요 예시
```

256-dim 임베딩, 4 attention heads, 2 transformer layers의 mini 모델이 약 3GB 아카이브로 Git LFS에 올라왔다. *프로덕션 모델보다 작지만 같은 실시간 engagement 데이터로 학습된 frozen checkpoint*다. 훈련 단계 없이 즉시 추론이 가능하다.

### 3. 데모 코퍼스와 예시 사용자

537K개 스포츠 관련 글로 구성된 `sports_corpus.npz`와, 사용자가 NFL·NBA·NHL 글을 좋아요·dwell한 예시 시퀀스(`example_sequence.json`)가 함께 풀렸다. 외부 사람이 "이 입력으로 어떤 추천이 나오는가"를 직접 돌려볼 수 있다는 뜻이다.

### 4. 주변 모듈 확장

기존 컴포넌트 외에 다음이 새로 들어왔다.

- **Grox** — 콘텐츠 이해 파이프라인. classifier·embedder·task execution engine을 묶어 스팸 탐지, 게시물 카테고리 분류, PTOS 정책 enforcement 같은 작업을 처리한다.
- **home-mixer/ads** — 광고 블렌딩 모듈. 피드 내 광고 위치 결정과 sensitive content 경계를 존중하는 brand-safety 추적.
- **Query/Candidate hydrators 다수 확장** — 팔로우 토픽, 스타터 팩, 임프레션 블룸 필터, IP, 상호 팔로우 그래프, served history, engagement counts, brand safety 신호, 언어 코드, 미디어 감지, 인용 게시물 확장 등.
- <strong>신규 candidate sources</strong> — 광고, who-to-follow, Phoenix MoE, Phoenix topics, prompts.

## 가장 흥미로운 지점

이번 공개에서 가장 인상 깊은 결정은 *Candidate Isolation*이다.

추천 시스템에서 "한 게시물의 점수가 같은 배치에 어떤 다른 게시물이 들어왔는지에 따라 달라진다"는 것은 운영상 골치 아픈 문제다. 점수를 캐싱할 수도 없고, A/B 테스트나 디버깅에서 같은 입력에 다른 출력이 나오는 비결정성이 생긴다. 그렇다고 단순히 후보를 한 번에 하나씩만 처리하면 트랜스포머의 배치 효율을 못 살린다.

xAI의 답은 우아하다. <strong>모델 구조(attention mask) 자체로 그 문제를 푼다.</strong> 후보들은 한 배치에 묶여 효율적으로 forward되지만, attention 차원에서는 서로를 보지 못한다. 그러므로 점수는 어떤 다른 후보와 묶이든 *수학적으로* 동일하다. 캐싱 가능성과 일관성이 *학습 단계나 서빙 단계의 정책*이 아니라 *모델 정의 자체*에서 보장되는 것이다.

이건 단순한 추천 시스템 트릭을 넘어, "운영상 보장하고 싶은 속성을 모델 구조 안으로 끌어들인다"는 일반적인 설계 태도로 읽힌다. 비슷한 결의 사례를 찾자면, 트랜스포머의 causal mask가 "미래를 보지 않는다"는 시간 순서 속성을 모델 구조로 보장하는 것이 떠오른다. 시스템 운영 지식이 아키텍처 결정으로 응결된 사례다.

또 하나 인상 깊은 점은 *재현 가능성을 진지하게 다뤘다*는 것이다. 코드만 푸는 것과 사전학습 체크포인트 + 데모 코퍼스 + 예시 사용자 시퀀스를 함께 푸는 것은 외부 검증 가능성에서 차이가 크다. "알고리즘이 투명하다"는 주장이 실제로 *돌아가는* 시스템으로 뒷받침된다는 점에서, 정치적 의미와 기술적 의미를 모두 가진 릴리스다.

## 출처

- 발행: xAI, Apache License 2.0
- 발표일: 2026년 5월 15일 (이번 업데이트)
- 원문 리포: <https://github.com/xai-org/x-algorithm>
- Phoenix 모듈 README: <https://github.com/xai-org/x-algorithm/blob/main/phoenix/README.md>
- 참고 — 트랜스포머 코어는 [Grok-1 오픈소스](https://github.com/xai-org/grok-1)에서 포팅되어 추천 시스템에 맞게 적응됨.

원문에 별도 이미지는 없고 README의 ASCII 다이어그램이 핵심 도식이라, 본 다이제스트에는 이미지를 첨부하지 않고 본문에 일부 도식을 그대로 옮겨두었다.
