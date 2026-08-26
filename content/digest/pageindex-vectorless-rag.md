---
title: "PageIndex: Vectorless, Reasoning-based RAG"
date: 2026-05-05T23:15:00+09:00
tags: ["RAG", "LLM", "검색", "에이전트"]
categories: ["모델과 연구"]
summary: "벡터 DB도 청킹도 없이, LLM이 문서의 계층적 트리 인덱스를 추론하며 탐색하는 Vectorless RAG 프레임워크. FinanceBench 98.7% 정확도를 달성했다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. PageIndex는 VectifyAI가 공개한 오픈소스 RAG 프레임워크로, 벡터 유사도 검색 대신 LLM 추론 기반 트리 검색으로 문서를 탐색한다.
2. PDF를 계층적 트리 인덱스(목차와 유사한 구조)로 변환한 뒤, 에이전트가 트리를 내려가며 관련 페이지를 좁혀가는 human-like retrieval 방식을 사용한다.
3. 이 방식으로 금융 문서 QA 벤치마크 FinanceBench에서 98.7% 정확도를 달성하여, 벡터 RAG 대비 현저한 우위를 보였다.

## 핵심 전제: 유사도는 관련성이 아니다

전통적인 벡터 RAG는 쿼리와 문서 청크의 시맨틱 유사도로 검색한다. 그런데 전문 문서에서 진짜 필요한 것은 <strong>유사도(similarity)</strong>가 아니라 <strong>관련성(relevance)</strong>이다. 관련성을 판단하려면 도메인 지식과 다단계 추론이 필요한데, 임베딩 벡터 비교로는 이를 포착할 수 없다.

PageIndex는 이 간극을 LLM의 추론 능력으로 메운다. AlphaGo의 트리 탐색에서 영감을 받아, 문서를 계층적 인덱스로 변환하고 LLM이 그 인덱스를 **추론하며 내려가는** 방식으로 검색한다.

![PageIndex의 Vectorless RAG 아키텍처. 문서를 트리 구조로 인덱싱한 뒤, LLM이 트리를 추론하며 관련 페이지를 찾는다.](https://img.seosoyoung.eiaserinnys.me/images/pageindex-vectorless-rag/vectorless-rag.png)

## 두 단계로 작동한다

### 1단계: 트리 인덱스 생성

PDF를 입력받으면 목차(Table of Contents)와 유사한 계층적 트리 구조를 생성한다. 각 노드에는 제목, 시작/끝 페이지 번호, 요약이 포함된다. 인위적 청킹 대신 문서의 자연스러운 섹션 경계를 따른다.

트리 생성은 세 가지 경로로 분기한다:

- **ToC + 페이지번호 있음**: 기존 목차를 추출하고, 물리 페이지와 매핑하여 오프셋을 보정한다.
- **ToC만 있음 (페이지번호 없음)**: 목차를 추출한 뒤, 본문과 대조하여 각 섹션의 위치를 매핑한다.
- **ToC 자체가 없음**: LLM이 본문을 분할하여 구조를 직접 생성한다.

모든 경우에서 랜덤 샘플링으로 물리 페이지와 제목의 일치 여부를 검증한다. 정확도가 60% 이상이면 오답만 재시도로 수정하고, 60% 미만이면 더 단순한 모드로 전체 폴백한다. 최대 3회 재시도하는 자기 치유(self-healing) 루프다.

한 노드가 너무 크면(기본 10페이지 이상 + 토큰 임계값 초과) 해당 노드 내부를 재귀적으로 하위 트리로 분할한다. `asyncio.gather`로 병렬 처리되어 긴 문서도 적절한 깊이의 트리로 변환된다.

### 2단계: 추론 기반 트리 검색

검색 시 에이전트에게 세 가지 도구만 주면 된다:

- `get_document()` — 문서 메타데이터 (상태, 페이지 수 등)
- `get_document_structure()` — 트리 구조 인덱스 (텍스트 제외, 토큰 절약)
- `get_page_content(pages)` — 특정 페이지의 텍스트

에이전트는 먼저 트리 구조를 보고 어느 섹션이 질문과 관련 있는지 추론한 뒤, 좁은 페이지 범위만 요청한다. 전체 문서를 컨텍스트에 넣지 않고도 정확한 답변이 가능하다. 사람이 전문 문서를 다룰 때 목차를 훑어 관련 장으로 이동하는 과정과 동일하다.

## 벤치마크: FinanceBench 98.7%

PageIndex 기반 시스템 Mafin 2.5가 금융 문서 QA 벤치마크 <strong>FinanceBench</strong>에서 98.7% 정확도를 달성했다. SEC 공시, 실적 보고서 등 복잡한 금융 문서에서 계층적 인덱싱과 추론 기반 검색이 벡터 RAG 대비 현저한 우위를 보였다.

![FinanceBench 벤치마크 결과. PageIndex 기반 Mafin 2.5가 98.7%로 SOTA를 달성했다.](https://img.seosoyoung.eiaserinnys.me/images/pageindex-vectorless-rag/benchmark.png)

## 코드 구조

오픈소스 구현의 핵심 모듈은 다음과 같다:

- `pageindex/page_index.py` — 트리 생성 파이프라인. ToC 감지, 구조 생성, 검증, 자기 수정, 재귀 분할의 전체 흐름을 담당한다.
- `pageindex/page_index_md.py` — 마크다운 문서용 트리 생성. 헤딩(`#`) 기반으로 계층을 파악한다.
- `pageindex/retrieve.py` — 검색 도구 3종(`get_document`, `get_document_structure`, `get_page_content`) 구현.
- `pageindex/client.py` — `PageIndexClient` 클래스. 인덱싱부터 검색까지의 통합 인터페이스. 워크스페이스에 인덱스를 캐싱하여 재사용한다.
- `pageindex/utils.py` — LLM 호출(LiteLLM 기반), 토큰 카운팅, JSON 파싱 유틸리티.

에이전틱 RAG 예제(`examples/agentic_vectorless_rag_demo.py`)는 OpenAI Agents SDK와 결합하여, 세 도구만으로 문서 QA 에이전트를 구성하는 데모를 제공한다.

## 가장 흥미로운 지점

소스 코드를 직접 읽어보면 트리 생성 파이프라인의 <strong>방어적 설계</strong>가 인상적이다. LLM 출력은 불완전할 수 있다는 전제 아래, 모든 단계에서 검증하고, 정확도에 따라 수정 또는 폴백하는 자기 치유 루프를 돌린다. "LLM이 완벽하지 않으니 검증을 겹겹이 쌓는다"는 접근은 에이전트 시스템 설계의 보편적 패턴이기도 하다.

검색 쪽에서는 도구가 딱 세 개라는 점이 눈에 띈다. 구조를 보고, 페이지를 좁히고, 내용을 가져오는 것. 에이전트에게 너무 많은 도구를 주면 오히려 혼란이 생기는데, 최소한의 도구로 추론을 극대화하는 설계가 FinanceBench 98.7%의 기반일 것이다.

## 출처

VectifyAI / Mingtian Zhang, Yu Tang and PageIndex Team
원문: <https://github.com/VectifyAI/PageIndex>
