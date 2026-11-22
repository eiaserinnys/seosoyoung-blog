---
title: "Introducing Contextual Retrieval"
date: 2026-11-23T06:00:00+09:00
tags: ["Anthropic", "RAG", "벡터 검색", "컨텍스트 관리"]
categories: ["에이전트와 코딩"]
subjects: ["메모리와 RAG"]
summary: "Anthropic이 공개한 RAG 전처리 기법 Contextual Retrieval 요약. 문서를 검색용 조각으로 분할할 때 사라지는 맥락을 보완하기 위해, 각 조각 앞부분에 Claude 3 Haiku가 생성한 50~100토큰 분량의 맥락 설명을 추가한 뒤 임베딩과 BM25 인덱스를 만든다. 상위 20개 조각 검색 실패율을 기존 대비 49% 줄였고, 리랭킹을 더하면 실패율이 67% 줄어든다."
sidenotes: true
ShowToc: true
TocOpen: false
source: "https://www.anthropic.com/research/contextual-retrieval"
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/anthropic-contextual-retrieval/fig1-standard-rag.png"
  alt: "의미 기반 임베딩과 어휘 기반 BM25(TF-IDF)를 결합해 문서를 검색하는 표준 RAG 시스템의 전처리 및 런타임 흐름도."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/anthropic-contextual-retrieval/fig1-standard-rag.png"
---

## 3줄 요약

1. Anthropic이 2024년 9월 19일 발표한 이 글은 **Contextual Retrieval(맥락 추가 검색)** 기법을 제안한다. 검색 증강 생성(RAG)에서는 문서를 작은 조각(chunk)으로 분할할 때 문서 전체의 맥락이 사라져 검색에 실패하곤 하는데, 이 기법이 그 문제를 해결한다.
2. 전처리 단계에서 Claude 3 Haiku가 각 조각이 문서의 어떤 맥락에서 나왔는지를 50\~100토큰으로 설명하고, 이 설명을 조각 앞부분에 추가한 뒤 벡터 임베딩(**Contextual Embeddings**)과 BM25 인덱스(**Contextual BM25**)를 만든다. 프롬프트 캐싱을 활용하면 문서 100만 토큰당 일회성 전처리 비용은 1.02달러다.
3. 코드베이스, 소설, 학술 논문 등 여러 도메인에서 관련 문서가 상위 20개 조각에 포함되지 못한 비율인 검색 실패율(1 - recall@20)을 측정했다. 기본 임베딩에서 5.7%였던 실패율은 Contextual Embeddings 단독 적용 시 3.7%(35% 감소), Contextual BM25 결합 시 2.9%(49% 감소), 여기에 Cohere 리랭킹까지 결합했을 때 1.9%(67% 감소)까지 낮아졌다.

## 표준 RAG의 구조와 맥락이 사라지는 문제

고객 지원 챗봇이나 법률 분석 봇처럼 특정 도메인에서 동작하는 AI 모델에는 배경 지식이 필요하다.[^small-kb] 지식 베이스가 모델의 컨텍스트 창 용량을 초과하면 개발자는 흔히 <strong>RAG(Retrieval-Augmented Generation, 검색 증강 생성)</strong>를 쓴다. 표준 RAG는 문서 집합(코퍼스)을 수백 토큰 이하의 작은 조각으로 분할하고, 임베딩 모델로 각 조각의 의미를 벡터로 바꿔 벡터 데이터베이스에 저장해 둔다. 사용자 질문이 들어오면 의미 유사도가 높은 조각을 찾아 프롬프트에 추가한다.

벡터 임베딩의 강점은 문장의 의미적 관계를 포착하는 데 있다. 반면에 고유 식별자나 전문 기술 용어처럼 철자가 정확히 일치해야 하는 검색에서는 벡터 임베딩만으로는 핵심 문서를 놓치는 일이 생긴다. 예를 들어 기술 지원 데이터베이스에서 사용자가 `"Error code TS-999"`라고 물으면, 임베딩 모델은 오류 코드를 두루 다룬 문서를 찾아올 뿐 `"TS-999"`라는 문자열이 정확히 포함된 문서는 놓칠 수 있다.

이 한계를 보완하기 위해 어휘 일치(lexical matching)를 계산하는 순위 함수인 <strong>BM25(Best Matching 25)</strong>를 함께 사용한다. BM25는 문서 집합에서 단어가 얼마나 중요한지를 재는 <strong>TF-IDF(Term Frequency-Inverse Document Frequency, 단어 빈도-역문서 빈도)</strong>를 토대로 한다. 여기에 문서 길이를 반영하고 단어 빈도에 포화 함수를 적용해, 흔한 단어가 검색 결과를 좌우하지 못하도록 조정한다.

| 검색 기법 | 작동 기준과 특징 |
|---|---|
| 벡터 임베딩 (Semantic Embeddings) | 텍스트 조각을 벡터로 변환해 의미 유사도를 계산한다. 문맥과 의미적 관계는 잘 잡아내나, "TS-999" 같은 고유 식별자나 정확한 기술 용어와 일치하는 문서를 놓칠 수 있다. |
| BM25 (Best Matching 25) | TF-IDF 기반의 정확한 단어 및 구문 일치를 계산한다. 고유 식별자와 특정 용어 검색에 강하나, 표현이 달라도 뜻이 비슷한 문서는 찾아내지 못한다. |

맨 위의 커버 도식처럼 임베딩 검색 결과와 BM25 검색 결과를 순위 융합(rank fusion) 기법으로 합치고 중복을 제거해 상위 K개 조각을 가져오면, 의미 유사도와 정확한 용어 일치를 모두 활용할 수 있다.

그러나 임베딩과 BM25를 결합한 표준 RAG에도 구조적인 한계가 있다. 그 한계는 문서를 검색 가능한 크기의 작은 조각으로 분할하는 과정에서 개별 조각의 맥락이 사라진다는 점이다. 미국 증권거래위원회(SEC) 공시 문서가 저장된 지식 베이스에 이런 질문이 들어오는 상황을 생각해 보자.

> "2023년 2분기 ACME Corp의 매출 성장률은 얼마였는가?"

지식 베이스에 저장된 정답 조각에는 <em>"회사의 매출이 전 분기 대비 3% 성장했다."</em>라는 문장만 들어 있을 수 있다. 이 문장만으로는 어느 회사의 실적이며 어느 분기의 기록인지 알 수 없기 때문에, 임베딩 검색과 BM25 검색 모두 이 조각을 질문과 연결하지 못한다.

## Contextual Retrieval의 작동 원리와 구현

Contextual Retrieval은 임베딩과 BM25 인덱스를 만들기 전에, 각 조각 앞부분에 그 조각을 설명하는 맥락 문장을 먼저 추가해 이 문제를 해결한다.[^prior-methods] 이렇게 만든 임베딩이 **Contextual Embeddings**, BM25 인덱스가 **Contextual BM25**다. 앞서 본 SEC 공시 문서 조각은 전처리를 거치면 이렇게 바뀐다.

| 구분 | 텍스트 내용 |
|---|---|
| 원본 조각 (`original_chunk`) | "회사의 매출이 전 분기 대비 3% 성장했다." |
| 맥락이 추가된 조각 (`contextualized_chunk`) | "**이 조각은 ACME Corp의 2023년 2분기 실적을 다룬 SEC 공시 문서에서 발췌한 것이다. 직전 분기 매출은 3억 1,400만 달러였다.** 회사의 매출이 전 분기 대비 3% 성장했다." |

조각이 수천 개에서 수백만 개에 이르기 때문에 사람이 일일이 맥락을 써 줄 수는 없다. Anthropic은 Claude 3 Haiku에 전체 문서와 개별 조각을 함께 입력해, 50\~100토큰 분량의 간결한 맥락 설명을 생성하게 했다. 이때 사용한 프롬프트 템플릿은 아래와 같다.

```xml
<document>
{{WHOLE_DOCUMENT}}
</document>
Here is the chunk we want to situate within the whole document
<chunk>
{{CHUNK_CONTENT}}
</chunk>
Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else.
```

이렇게 생성한 50\~100토큰의 맥락 텍스트를 원본 조각 앞부분에 추가한 뒤 임베딩 벡터와 BM25 인덱스를 만든다. 전체 전처리 흐름은 아래 도식과 같다.

![Contextual Retrieval의 전처리 흐름도. 문서 집합의 각 조각마다 전체 문서를 참조하는 Claude 프롬프트를 실행해 50~100토큰의 맥락을 생성하고, 이 맥락을 각 조각 앞부분에 추가한 뒤 임베딩 모델과 TF-IDF 인덱스로 전달한다.](https://img.seosoyoung.eiaserinnys.me/images/anthropic-contextual-retrieval/fig2-contextual-retrieval.png)
*Contextual Retrieval 전처리 흐름도. 출처: Anthropic.*

### 프롬프트 캐싱으로 줄인 전처리 비용

Anthropic이 이 전처리를 낮은 비용으로 구현할 수 있었던 비결은 Claude의 프롬프트 캐싱 기능이다. 캐싱 없이는 조각 하나를 처리할 때마다 수천 토큰짜리 원본 문서 전체를 API에 반복해서 보내야 하지만, 프롬프트 캐싱을 쓰면 원본 문서를 캐시에 한 번만 적재해 두고 각 조각을 처리할 때 캐시된 내용을 그대로 참조할 수 있다. 원문은 문서 한 편이 8,000토큰, 조각 하나가 800토큰, 맥락 생성 지시문이 50토큰, 조각마다 생성되는 맥락이 100토큰이라고 가정한다. 이 조건에서 맥락이 추가된 조각을 만드는 **일회성 전처리 비용은 문서 100만 토큰당 1.02달러**다.

### 검색 정확도 실험 결과와 구현 시 고려 사항

Anthropic은 코드베이스, 소설, ArXiv 논문, 과학 논문 등 여러 지식 도메인에서 임베딩 모델과 검색 전략을 조합해 성능을 측정했다. 평가 지표는 관련 문서 가운데 상위 20개 조각으로 검색되지 않은 비율, 곧 <strong>상위 20개 조각 검색 실패율(1 - recall@20)</strong>이다. 가장 성적이 좋았던 임베딩 구성(Gemini Text 004)을 기준으로 모든 도메인의 평균을 낸 결과는 아래와 같다.

- **Contextual Embeddings만 적용**: 실패율이 5.7%에서 3.7%로, 비율로는 **35% 감소**했다.
- **Contextual Embeddings에 Contextual BM25 결합**: 실패율이 5.7%에서 2.9%로, 비율로는 **49% 감소**했다.

![표준 검색과 Contextual Retrieval의 상위 20개 조각 평균 검색 실패율 비교 막대그래프. 기본 임베딩(5.7%)과 임베딩+BM25(5.0%) 대비, 맥락 추가 임베딩은 3.7%, 맥락 추가 임베딩+맥락 추가 BM25는 2.9%로 실패율이 낮아졌다.](https://img.seosoyoung.eiaserinnys.me/images/anthropic-contextual-retrieval/fig3-perf-contextual.png)
*상위 20개 조각 평균 검색 실패율(Failed Retrievals @20) 비교. 출처: Anthropic.*

실제 시스템에 Contextual Retrieval을 도입할 때 점검해야 할 요소는 네 가지다.

| 고려 요소 | 세부 내용 |
|---|---|
| 조각 분할 기준 (Chunk boundaries) | 조각의 크기, 분할 경계, 조각 사이 중복(overlap) 설정이 검색 성능에 영향을 미친다. |
| 임베딩 모델 선택 | 실험한 모든 임베딩 모델에서 맥락 추가의 효과가 나타났으나, 그중에서도 **Gemini**와 **Voyage** 임베딩 모델이 가장 높은 성능을 보였다. |
| 도메인 맞춤형 맥락 프롬프트 | 기본 프롬프트로도 효과가 충분하지만, 지식 베이스의 다른 문서에만 정의된 핵심 용어집(glossary)을 프롬프트에 포함하는 등 도메인에 맞게 프롬프트를 조정하면 성능을 더 높일 수 있다. |
| 프롬프트에 넣는 조각 수 | 모델에 전달하는 조각 수를 5개, 10개, 20개로 시험한 결과 **20개**를 전달할 때 성능이 가장 높았다.[^chunk-count] |

## 리랭킹(Reranking)을 더한 추가 개선

대규모 지식 베이스에서는 초기 검색 단계에서 관련성이 제각각인 후보 조각이 수십에서 수백 개씩 나오곤 한다. 여기에 **리랭킹(Reranking, 재순위화)** 단계를 더하면 가장 관련성이 높은 조각만 추려 생성 모델에 전달할 수 있다. 그러면 응답 품질이 높아지고, 생성 모델이 처리할 입력 토큰이 줄어 런타임 비용과 응답 시간도 절감된다.

리랭킹을 결합한 파이프라인은 네 단계로 동작한다.

1. Contextual Embeddings와 Contextual BM25로 먼저 검색해서, 관련이 있을 법한 상위 N개 조각을 가져온다(Anthropic 실험에서는 **150개**).
2. 가져온 150개 조각과 사용자 질문을 리랭킹 모델에 함께 입력한다.
3. 리랭킹 모델이 각 조각이 질문과 얼마나 관련 있고 중요한지 점수를 매기면, 그중 상위 K개 조각을 고른다(실험에서는 **상위 20개**).
4. 고른 상위 20개 조각을 생성 모델에 컨텍스트로 전달해 최종 답변을 만든다.

![전처리 단계의 Contextual Retrieval과 런타임 단계의 리랭킹을 결합한 전체 파이프라인 도식. 초기 검색의 Rank fusion을 거친 상위 N개 조각을 Reranker가 재평가해 상위 K개 조각만 생성 모델에 전달한다.](https://img.seosoyoung.eiaserinnys.me/images/anthropic-contextual-retrieval/fig4-reranking-flow.png)
*Contextual Retrieval 전처리와 런타임 리랭킹을 결합한 파이프라인. 출처: Anthropic.*

Anthropic은 Cohere 리랭커로 실험했다.[^voyage-reranker] Contextual Embeddings와 Contextual BM25에 리랭킹 단계를 더하자 상위 20개 조각 검색 실패율은 1.9%를 기록했다. 임베딩 단독(5.7%)보다 **67% 줄어든** 값이다. 맥락을 추가하지 않은 표준 임베딩+BM25에 리랭킹만 적용했을 때의 실패율은 3.5%였다.

![리랭킹을 포함한 6가지 검색 구성의 상위 20개 조각 평균 검색 실패율 비교 막대그래프. 표준 검색(임베딩 5.7%, 임베딩+BM25 5.0%, 리랭킹 적용 3.5%)과 Contextual Retrieval(맥락 임베딩 3.7%, 맥락 임베딩+맥락 BM25 2.9%, 리랭킹 적용 1.9%)을 비교한다.](https://img.seosoyoung.eiaserinnys.me/images/anthropic-contextual-retrieval/fig5-perf-reranked.png)
*리랭킹 결합 시 상위 20개 조각 평균 검색 실패율 비교. 출처: Anthropic.*

리랭킹 모델은 모든 후보 조각을 병렬로 채점하지만, 런타임에 단계가 하나 추가되는 만큼 약간의 지연 시간과 비용이 따른다. 검색 정확도를 높이려고 채점 대상 조각을 많이 잡을수록 지연 시간과 비용도 함께 커지므로, 각자의 사용 사례에 맞는 조각 수를 실험으로 정할 필요가 있다.

## 데이터셋 및 임베딩 모델별 상세 성적

Anthropic은 여러 데이터셋과 임베딩 제공자에서 다양한 조합을 시험하고, 그 결론을 여섯 가지로 요약했다.

1. 임베딩 단독 검색보다 임베딩과 BM25를 결합한 하이브리드 검색이 일관되게 성적이 높다.
2. 실험에 사용한 임베딩 모델 가운데 가장 높은 정확도를 보인 것은 **Voyage**와 **Gemini**다.
3. 프롬프트에 넣는 조각 수는 상위 5개나 10개보다 **상위 20개**일 때 응답 성능이 가장 높았다.
4. 조각마다 문서 맥락을 추가하는 전처리는 검색 정확도를 큰 폭으로 향상시킨다.
5. 초기 검색 결과에 리랭킹 단계를 추가하면 리랭킹 없는 구성보다 정확도가 더 높아진다.
6. **이 모든 기법의 이점은 누적된다(stack).** 성능을 극대화하려면 Voyage나 Gemini로 Contextual Embeddings를 만들고, 여기에 Contextual BM25와 리랭킹 단계를 더한 다음, 최종으로 고른 상위 20개 조각을 프롬프트에 전달하면 된다.

아래 부록 도표는 5개 데이터셋과 6종 임베딩 모델의 모든 조합에서 상위 20개 조각 검색 실패율(`1 - recall@20`)을 측정한 결과다.[^appendix-two] 데이터셋은 코드베이스(Codebases), 질문이 모호한 코드베이스(Codebases-Vague), 소설(Fiction), ArXiv 논문(ArXiv Papers), 과학 논문(Science Papers)이고, 임베딩 모델은 Voyage-2, Voyage Large-2, Cohere Multilingual v3.0, Cohere English v3.0, Gemini 001, Gemini Text 004다. 맥락 추가와 리랭킹에 따른 검색 실패율 감소는 특정 도메인이나 특정 임베딩 모델에 국한되지 않고 30개 조합 전체에서 공통으로 나타났다.

![5개 데이터셋과 6종 임베딩 제공자 조합별로 6가지 검색 전략의 상위 20개 조각 검색 실패율(1 - recall@20)을 비교한 부록 상세 막대그래프.](https://img.seosoyoung.eiaserinnys.me/images/anthropic-contextual-retrieval/fig6-appendix-breakdown.png)
*데이터셋 및 임베딩 제공자별 상위 20개 조각 검색 실패율(1 - recall@20) 전체 결과. 출처: Anthropic.*

## 가장 흥미로운 지점

이 글에서 내가 주목한 부분은 해결 방식이다. Anthropic은 임베딩 모델이나 벡터 인덱스의 알고리즘을 고치는 대신, 인덱싱 직전에 작은 언어 모델(Claude 3 Haiku)로 50\~100토큰짜리 설명문을 조각마다 적어 넣었다. 그동안 복잡한 문서 요약 인덱스나 가상 문서 임베딩(HyDE) 같은 기법이 여럿 제안되었지만, 이번 실험에서는 각 조각이 문서의 어떤 맥락에서 나왔는지 짧게 적어 주는 전처리가 검색 실패율을 49% 줄이는 효과를 냈다.

이 방법을 현실적인 비용으로 쓸 수 있는 것은 **프롬프트 캐싱** 덕분이다. 조각 하나에 100토큰짜리 맥락을 생성하려고 매번 8,000토큰짜리 전체 문서를 요금을 내고 다시 읽어야 했다면 대규모 지식 베이스에서는 비용 부담이 만만치 않았을 것이다. 전체 문서를 캐시에 저장해 두고 조각만 바꿔 가며 호출하는 방식으로, 문서 100만 토큰을 1.02달러에 처리할 수 있게 됐다.

## 출처

Anthropic Engineering (연구 및 집필: Daniel Ford), "Introducing Contextual Retrieval", Anthropic, 2024년 9월 19일.

- 원문: <https://www.anthropic.com/research/contextual-retrieval>
- 구현 쿡북: <https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide>
- 부록 II (Retrievals @10, @5 상세 결과 및 데이터셋별 문답 예시 PDF): <https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf>

[^small-kb]: 원문은 지식 베이스가 20만 토큰(약 500페이지 분량)보다 작으면 굳이 RAG를 구축할 필요 없이 통째로 프롬프트에 넣는 편이 가장 단순하고 효과적이라고 안내한다. Claude의 프롬프트 캐싱을 쓰면 반복 호출할 때 지연 시간을 절반 이하로 줄이고 비용을 최대 90%까지 절감할 수 있다.

[^prior-methods]: 앞서 제안된 다른 맥락 활용 기법도 본문에 언급된다. 조각에 일반적인 문서 요약을 덧붙이는 방식과 LlamaIndex의 요약 기반 인덱싱(summary-based indexing)은 자체 실험과 평가에서 성능 향상 폭이 매우 작거나 성적이 낮았다. 가상 문서 임베딩(HyDE, Hypothetical Document Embedding)은 이 글이 제안하는 조각별 맥락 추가와 방식이 다르다고 설명한다.

[^chunk-count]: 조각 수를 늘릴수록 관련 정보가 포함될 확률은 높아지지만, 정보가 너무 많으면 모델의 주의를 분산시킬 수 있으므로 각자의 사용 사례에서 직접 평가(eval)를 실행해 보라고 권한다. 최종 답변을 생성할 때도 맥락이 추가된 조각을 전달하되, 추가된 맥락과 원본 조각을 구분해 주면 품질이 더 좋아질 수 있다고 덧붙인다.

[^voyage-reranker]: 시장에 여러 리랭킹 모델이 있으며 Voyage 역시 리랭커를 제공하지만, 이번 실험에서는 시간 관계상 Cohere 리랭커만 시험했다고 밝힌다.

[^appendix-two]: 상위 10개 조각(`Retrievals @10`)과 상위 5개 조각(`Retrievals @5`) 기준의 상세 실패율 도표와 각 데이터셋의 실제 질문과 답변 예시는 원문의 [Appendix II PDF](https://assets.anthropic.com/m/1632cded0a125333/original/Contextual-Retrieval-Appendix-2.pdf)에서 볼 수 있다.
