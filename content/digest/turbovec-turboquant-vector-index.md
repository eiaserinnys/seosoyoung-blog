---
title: "turbovec — Google's TurboQuant for vector search"
date: 2026-07-17T11:00:00+09:00
tags: ["RAG", "벡터 검색", "양자화", "Rust", "오픈소스"]
categories: ["모델과 연구"]
summary: "구글 리서치의 TurboQuant 양자화 알고리즘을 Rust로 구현한 벡터 인덱스. 학습 단계 없이 벡터를 16배로 압축하고, 손수 짠 SIMD 커널로 FAISS보다 빠르게 검색한다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/header.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/header.png"
---

![turbovec — Google's TurboQuant for vector search](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/header.png)

## 3줄 요약

1. turbovec은 구글 리서치의 [TurboQuant](https://arxiv.org/abs/2504.19874) 양자화 알고리즘을 Rust로 구현하고 Python 바인딩을 붙인 벡터 인덱스다. 코어 주장은 하나다 — 1천만 문서 코퍼스가 float32로는 31GB인데 turbovec은 4GB에 담고, 그러면서 FAISS보다 빠르게 검색한다.
2. 핵심은 학습(train) 단계가 없다는 것이다. TurboQuant은 데이터에 무관한(data-oblivious) 양자화기라, 벡터를 랜덤 회전시키면 좌표 분포가 데이터와 상관없이 알려진 형태로 수렴한다는 성질에 기댄다. 그래서 파라미터 튜닝도, 코퍼스가 커질 때마다의 리빌드도 없다.
3. 검색 커널은 NEON(ARM)·AVX-512BW(x86)로 손수 짰다. ARM에서는 FAISS의 IndexPQFastScan을 모든 구성에서 10\~19% 앞서고, x86에서는 4-bit 구성을 이기며 2-bit에서만 몇 퍼센트 뒤진다.

## turbovec이 겨냥하는 자리

turbovec은 매니지드 서비스가 아니다. 데이터가 기기나 VPC 바깥으로 나가지 않는 완전 로컬 인덱스이고, 오픈소스 임베딩 모델과 짝지으면 에어갭 RAG 스택을 만들 수 있다. 프라이버시·메모리·지연이 문제가 되는 RAG를 만든다면 이 자리를 노린 도구다.

설치와 기본 사용은 이렇다.

```python
from turbovec import TurboQuantIndex

index = TurboQuantIndex(dim=1536, bit_width=4)
index.add(vectors)
index.add(more_vectors)

scores, indices = index.search(query, k=10)

index.write("my_index.tv")
loaded = TurboQuantIndex.load("my_index.tv")
```

삭제 후에도 유지되는 안정적 id가 필요하면 `IdMapIndex`를 쓴다. uint64 외부 id를 붙이고 O(1)로 삭제한다.

LangChain·LlamaIndex·Haystack·Agno에는 드롭인 교체본이 있다. 각 프레임워크의 기본 인메모리 벡터/문서 스토어와 같은 공개 인터페이스·같은 영속화 의미를 가지므로, import만 갈아끼우면 파이프라인은 그대로 둔다.

## 어떻게 작동하나 — 6단계

각 벡터는 고차원 초구(hypersphere) 위의 방향 하나다. TurboQuant은 이 방향들을 하나의 통찰로 압축한다. 랜덤 회전을 적용하면, 입력 데이터가 무엇이든 모든 좌표가 알려진 분포를 따른다는 것이다.

1. **정규화.** 각 벡터에서 길이(norm)를 떼어내 float 하나로 저장한다. 이제 모든 벡터는 초구 위의 단위 방향이다.
2. **랜덤 회전.** 모든 벡터에 같은 랜덤 직교행렬을 곱한다. 회전 후 각 좌표는 독립적으로 베타 분포를 따르고, 고차원에서는 N(0, 1/d) 가우시안으로 수렴한다. 어떤 입력에도 성립한다 — 회전이 좌표 분포를 예측 가능하게 만든다.
3. **좌표별 캘리브레이션 (TQ+).** 2단계의 베타 분포는 점근적이다. 유한 차원에서는 개별 좌표가 표준 형태에서 벗어난다(특히 저비트·워드벡터류 임베딩). TQ+는 첫 add 때 좌표마다 shift·scale 두 스칼라를 맞춰, 각 좌표의 실측 5/95% 분위를 표준 베타 주변부에 매핑한다. 캘리브레이션은 첫 add 이후 고정되어 이후 add에 재사용된다 — 재학습도, 리빌드도, 별도 train 단계도 없다. 가장 많이 드리프트하는 셀에서 R@1 기준 최대 +1.4pp의 recall 이득.
4. **Lloyd-Max 스칼라 양자화.** 분포를 알기 때문에 각 좌표를 담을 최적의 버킷을 미리 계산할 수 있다. 2-bit면 4개, 4-bit면 16개 버킷이다. Lloyd-Max 알고리즘이 평균제곱오차를 최소화하는 경계와 중심을 찾는다. 데이터가 아니라 수학에서 한 번 계산된다.
5. **비트팩.** 이제 각 좌표는 작은 정수다(2-bit는 0\~3, 4-bit는 0\~15). 이를 바이트에 촘촘히 담는다. 1536차원 벡터가 6,144바이트(FP32)에서 384바이트(2-bit)로 줄어든다. 16배 압축이다.
6. **길이 재정규화 스코어링.** 스칼라 양자화는 내적을 체계적으로 과소평가한다 — 복원된 단위 방향이 원본보다 조금 짧다. 인코딩 시점에 벡터마다 스칼라 하나(회전된 단위벡터와 자기 중심 복원값의 내적)를 계산해 `||v|| / ⟨u, x̂⟩`를 압축 벡터 옆에 저장한다. 검색 커널이 heap 삽입 전에 후보 점수에 이 스칼라를 곱해, 하향 편향된 내적 추정기를 검색 시점 비용·추가 저장 없이 불편(unbiased)으로 바꾼다.

검색은 데이터베이스 벡터를 일일이 압축 해제하지 않는다. 쿼리를 같은 도메인으로 한 번 회전시킨 뒤 코드북 값에 직접 점수를 매긴다. 스코어링 커널은 SIMD 인트린식(ARM은 NEON, 최신 x86은 AVX-512BW, 아니면 AVX2 폴백)과 nibble-split 룩업 테이블로 처리량을 끌어올린다.

Lloyd-Max 코드북은 정보이론적 하한(섀넌의 왜곡-율 한계)의 2.7배 이내 왜곡을 달성하고, 길이 재정규화가 코드북이 내적 추정기에 남긴 잔여 편향을 제거한다.

## Recall

기준선은 FAISS `IndexPQ`(LUT256, nbits=8)로, 논문 4.4절의 베이스라인이자 대부분의 사용자가 프로덕션에서 먼저 손대는 PQ다. 조건은 10만 벡터, k=64.

![Recall — OpenAI d=1536](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/recall_d1536.svg)

![Recall — OpenAI d=3072](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/recall_d3072.svg)

![Recall — GloVe d=200](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/recall_glove.svg)

OpenAI d=1536·d=3072에서 TurboQuant은 2-bit·4-bit 전반에 걸쳐 R@1 기준 FAISS를 0.2\~1.9포인트 앞서고, 양쪽 다 k=8에서 1.0에 닿는다(k=4에서 이미 0.997 이상). GloVe d=200은 더 까다로운 영역이다 — 저차원에서는 점근적 베타 가정이 느슨해진다. 여기서 TurboQuant은 4-bit에서 0.9포인트 앞서고 2-bit에서는 사실상 동률(0.1포인트 이내)이며, k가 16쯤 되면 둘 다 FAISS를 바짝 따라붙는다. 저자는 FAISS `IndexPQ`가 논문의 자체 u8-LUT PQ보다 오히려 강한 기준선이라고 밝힌다 — 스코어링 시점에 더 높은 정밀도의 LUT와 k-means++ 코드북 학습을 쓰기 때문이다.

## Compression

![Compression](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/compression.svg)

1536차원 벡터 기준 6,144바이트(FP32) → 384바이트(2-bit), 16배다. 서두의 "31GB → 4GB"가 여기서 나온다.

## Search Speed

모든 벤치마크 조건은 10만 벡터, 1천 쿼리, k=64, 5회 실행의 중앙값이다.

### ARM (Apple M3 Max)

![ARM Speed — Single-threaded](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/arm_speed_st.svg)

![ARM Speed — Multi-threaded](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/arm_speed_mt.svg)

ARM에서 TurboQuant은 모든 구성에서 FAISS FastScan을 10\~19% 앞선다.

### x86 (Intel Xeon Platinum 8481C / Sapphire Rapids, 8 vCPU)

![x86 Speed — Single-threaded](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/x86_speed_st.svg)

![x86 Speed — Multi-threaded](https://img.seosoyoung.eiaserinnys.me/images/turbovec-turboquant-vector-index/x86_speed_mt.svg)

x86에서는 4-bit 구성을 최대 \~5% 앞서고(d=3072 멀티스레드는 동률), 2-bit에서는 FAISS에 다소 뒤진다 — 가장 두드러진 곳이 d=1536 싱글스레드(\~8%)다. 짧은 2-bit 누산 루프에서는 FAISS의 AVX-512 VBMI 경로가 우위를 가진다.

## 하이브리드 검색 — 검색 시점 필터링

turbovec은 다른 시스템(SQL·BM25·ACL·시간 윈도우 등)이 좁혀준 후보 집합 안으로 결과를 제한할 수 있다. `search()`에 id allowlist나 slot bitmask를 넘기면 커널이 직접 그것을 존중한다.

```python
# 1단계: 외부 시스템이 후보 id를 좁힌다.
allowed = np.array(db.execute("SELECT id FROM docs WHERE tenant=?", (t,)).fetchall(),
                   dtype=np.uint64)

# 2단계: 후보 집합 안에서 dense 재순위.
scores, ids = idx.search(query, k=10, allowlist=allowed)
```

필터링은 SIMD 커널 안에서 32-벡터 블록 단위로 일어난다. 허용된 슬롯이 하나도 없는 블록은 LUT 조회나 스코어링 전에 short-circuit되고, 스코어링된 블록 안의 비허용 슬롯은 heap 삽입에서 버려진다. 그래서 선택적 allowlist(인덱스의 작은 일부만 허용)는 SIMD 비용을 치르고 나중에 결과를 버리는 대신, 비용 대부분을 애초에 회피한다. recall 손실도 없다.

## 가장 눈여겨본 지점

내가 곱씹은 대목은 "학습이 없다"는 설계가 실제로는 두 단계로 나뉜다는 점이다. 원래 TurboQuant의 무학습 성질은 순수하게 수학에서 온다 — 랜덤 회전이 좌표 분포를 데이터와 무관하게 만들고, Lloyd-Max 버킷은 그 알려진 분포에서 한 번 계산된다. 데이터를 아예 보지 않는다.

그런데 저차원 임베딩(GloVe d=200 같은)에서는 이 점근 가정이 느슨해져 recall이 새어나간다. turbovec의 TQ+는 여기서 타협한다. 첫 add 때 데이터의 실측 분위(5/95%)를 한 번 보고 좌표별로 shift·scale을 맞춘 뒤 그대로 고정한다. 완전한 무학습과 완전한 데이터 의존 사이의 얇은 층 하나를 둔 셈이다 — "첫 배치를 한 번 보되 재학습은 없다". 이 한 겹이 가장 많이 드리프트하는 셀에서 최대 1.4pp를 되찾는다. 순수한 이론이 유한 차원의 현실과 만나는 지점을, 리빌드 없는 최소 개입으로 메운 것이 인상적이었다.

## 출처

RyanCodrai, *turbovec* (Rust vector index built on Google Research's TurboQuant, MIT License).
원문: <https://github.com/RyanCodrai/turbovec>

참조 논문:
- TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate (arXiv:2504.19874, ICLR 2026) — 구현 대상 논문
- RaBitQ (arXiv:2405.12497, SIGMOD 2024) — 6단계의 길이 재정규화 보정 출처
- FAISS FastScan — x86 SIMD 커널의 pack 레이아웃·nibble-LUT 스코어링 차용

본문의 차트·배너는 리포 `docs/` 디렉토리의 원문 이미지다.
