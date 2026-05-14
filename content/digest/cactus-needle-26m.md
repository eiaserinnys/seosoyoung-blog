---
title: "Needle — 26M 함수 호출 전용 모델, FFN을 통째로 들어낸 어텐션 네트워크"
date: 2026-05-14T09:00:00+09:00
tags: ["AI", "엣지 AI", "함수 호출", "소형 언어 모델", "어텐션 아키텍처", "모델 증류"]
categories: ["다이제스트"]
summary: "Cactus Compute가 Gemini 3.1을 26M 파라미터로 증류한 함수 호출 전용 모델. FFN을 통째로 들어낸 인코더-디코더 'Simple Attention Network'와 INT4 QAT, 게이트드 잔차, 토큰 가중 손실 등 작은 모델을 위한 설계 결정을 정리한다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Cactus Compute가 Gemini 3.1을 26M 파라미터 모델로 증류한 함수 호출 전용 모델 Needle을 공개했다. 가중치, 학습 코드, 데이터셋 합성 코드까지 MIT로 풀려 있다.
2. 핵심은 트랜스포머에서 FFN을 통째로 들어낸 'Simple Attention Network'이다. 도구 호출은 라우팅·복사 작업이므로 위치별 비선형 재작성(FFN)이 필요 없다는 가설을 실증한다.
3. 동급보다 작은 26M으로 FunctionGemma-270M, Qwen-0.6B, Granite-350M, LFM2.5-350M을 단일샷 함수 호출에서 능가한다. Cactus 런타임 위에서 prefill 6000 tok/s, decode 1200 tok/s. 단, 대화 능력은 갖추지 않은 태스크 특화 모델이다.

## 모델 개요

| 항목 | 값 |
|---|---|
| 파라미터 | 26M |
| 아키텍처 | 인코더-디코더, 순수 어텐션 (FFN 없음) |
| 인코더 | 12층, GQA (8H/4KV), RoPE, 게이트드 잔차 |
| 디코더 | 8층, self-attn + cross-attn, 게이트드 잔차 |
| d_model | 512 |
| Vocab | 8192 (SentencePiece BPE) |
| Norm | ZCRMSNorm (zero-centered, init=0) |
| Precision | bfloat16 (학습 중 INT4 QAT) |
| 사전훈련 | 16x TPU v6e에서 200B 토큰, 27시간 |
| 사후훈련 | 함수 호출 데이터 2B 토큰, 45분 |

## FFN을 제거한 근거

저자들은 도구 호출 태스크가 다음 세 단계로 분해된다고 본다.

1. 쿼리를 도구 이름에 정렬한다 (matching).
2. 쿼리에서 인자 값을 뽑는다 (extraction).
3. JSON을 조립한다 (assembly).

세 단계 모두 입력과 출력 사이를 <strong>정렬·복사</strong>하는 작업이다. 위치별로 *피처를 비선형으로 재작성*하는 단계는 없다.

> Softmax is nonlinear. `softmax(QK^T/sqrt(d)) * V` is a data-dependent nonlinear mixing operation. For a task that is about routing information (query → tool alignment), attention is the right primitive.

softmax 자체가 데이터 의존적 비선형 혼합 연산이므로, 라우팅에는 어텐션이 올바른 프리미티브다. FFN이 제공하는 위치별 비선형 변환은 이 태스크에서 잉여다.

설계 결정의 무게는 자원 재배분 측면에서 더 크다. 표준 트랜스포머는 파라미터의 약 2/3이 FFN이다. 50M 미만 모델에서 그 예산을 들어내 어텐션 층을 더 깊게 쌓거나 인코더와 디코더를 분리하는 데 쓸 수 있다. 추론 측면에서도 FFN은 GEMM/GEMV 차원이 가장 큰 블록이라, 제거하면 엣지 디바이스의 메모리 대역폭 병목이 직접 줄어든다.

## 인코더-디코더를 고른 이유

도구 정의는 구조화된 객체다. 인코더가 양방향으로 한 번에 보면 인과 모델이 왼쪽에서 오른쪽으로 추론해야 하는 구조 정보를 처음부터 갖고 들어간다.

또 인코더-디코더는 입력 토큰을 KV 캐시에 누적하지 않는다. 인코더가 만든 고정 크기 표현을 cross-attention에 재사용하므로, 생성 매 스텝마다 입력을 다시 처리하지 않는다. 엣지 디바이스에서 의미가 큰 절약이다.

같은 인코더 출력을 <strong>생성 헤드와 도구 검색 헤드 모두</strong>가 공유한다는 점도 중요하다. 도구 세트가 크면 모델 호출 전에 contrastive head로 top-k를 골라 디코더에 넘긴다.

## 게이트드 잔차와 ZCRMSNorm — 깊은 무-FFN 네트워크의 학습 가능성

FFN이 없으면 층마다 위치별 비선형 재작성이 사라진다. 잔차 설계가 곧 학습 가능성을 결정한다.

세 가지 옵션을 저울질한다.

- **표준 잔차** `x = x + Attn(Norm(x))` — 어텐션은 델타만 더할 수 있다. FFN이 빠진 상태에서 순수 가산은 제한적이다.
- **잔차 없음** `x = Attn(Norm(x))` — 매 층이 전부 재작성한다. 그래디언트 고속도로가 끊기고, 12층 이상에서는 학습이 잘 되지 않는다.
- **게이트드 잔차** `x = x + sigmoid(g) * Attn(Norm(x))` — 서브레이어별 학습 가능 스칼라를 0으로 초기화. sigmoid(0) = 0.5라 학습은 반쪽 잔차에서 시작한다. 유용한 층은 g→1로 강화하고, 쓸모없는 층은 g→0으로 가라앉힌다. 그 동안에도 그래디언트는 흐른다.

ZCRMSNorm은 게이트드 잔차와 짝이 되도록 설계됐다. 표준 RMSNorm `x * gamma / RMS(x)`는 gamma를 1로 초기화한다. ZCRMSNorm은 `x * (1 + gamma) / RMS(x)`로 두고 gamma를 0으로 초기화한다. 초기에는 항등에 가깝다. 블록 전체가 *감쇠된 항등 + 감쇠된 정규화 어텐션*에서 출발한다. 학습 안정성을 위해 QK 헤드에도 같은 정규화(QK-norm)를 적용한다.

## 듀얼 옵티마이저 — Muon + AdamW

- Muon: Q/K/V/O 프로젝션. 학습률 0.02, weight decay 0.01.
- AdamW: 나머지. 학습률 3e-4.

FFN이 빠진 모델은 본질적으로 *softmax 라우팅으로 연결된 선형 프로젝션의 깊은 스택*이다. 비선형이 자주 끼어들지 않으면 표현 붕괴(representation collapse) 위험이 있다. Muon은 Newton-Schulz로 가중치 업데이트의 직교성을 강제해 이 붕괴를 막는다.

## INT4 QAT를 정규화 도구로 쓴다

100스텝마다 fake quantization을 수행한다. 가중치를 그룹별 INT4(symmetric, group_size=32)로 양자화하고, straight-through estimator(STE)로 그래디언트를 흘린다.

부수 효과가 두 가지다.

1. **정규화.** 양자화 노이즈가 weight noise처럼 작동해, 파라미터가 작고 FFN이 없는 모델의 과적합 위험을 누른다.
2. **PTQ 갭 제거.** 추론 시 마주칠 양자화와 동일한 양자화로 학습한다. 사후 양자화(PTQ) 갭이 사라져 배포 시점의 손실이 없다.

## 토큰 가중 손실 — 오류 분포를 모델에 가르친다

손실 가중치를 토큰 종류별로 차등화한다.

| 토큰 종류 | 가중치 |
|---|---|
| JSON 구조 (base) | 1.0× |
| 도구 이름 | 2.0× |
| 인자 키 | 1.5× |
| 인자 값 | 4.0× |

근거는 단순하다. JSON 파싱 성공률은 학습 초기에 \~99%에 도달한다. 남는 오류는 *값 > 이름 > 키 > 구조* 순서다. 손실 가중치를 실제 오류 분포에 맞추면 작은 모델에서도 의미 있는 헤드룸을 확보한다. 부수적으로 z-loss(로짓 안정화)와 CLIP contrastive loss(0.1×)를 더한다.

## CLIP 스타일 도구 검색 헤드

대규모 도구 세트에서 top-k 필터링이 필요할 때 쓰는 보조 헤드다.

- **아키텍처**: 인코더 출력 → 비-패딩 위치 평균 풀링 → Dense(d/4) → ReLU → Dense(128) → L2 정규화. 입력당 단위 벡터 하나.
- **학습**: 배치 내 쿼리-도구 쌍을 양성, 같은 배치의 다른 쌍을 음성으로 쓰는 대칭 contrastive loss(CLIP). 학습 가능 온도(`log_temp`).
- **추론**: 쿼리와 후보 도구를 공유 임베딩 공간에 인코딩해 코사인 유사도로 top-k를 뽑는다.

같은 인코더가 생성과 검색을 모두 서비스하므로 추가 파라미터 비용이 거의 없다.

## 위치 — 태스크 특화 소형 모델 전략의 실제 사례

Needle은 26M으로 FunctionGemma-270M, Qwen-0.6B, Granite-350M, LFM2.5-350M보다 단일샷 함수 호출에서 더 잘 한다. 다만 이 모델들은 대화·범용 능력의 스코프가 넓다. Needle은 그 스코프를 의도적으로 좁힌다.

저자들은 명시한다.

> Those model are have more scope/capacity and excel in conversational settings. Also, small models can be finicky.

작은 모델의 변동성 문제는 알고 있고, 그래서 web UI에서 자기 도구로 파인튜닝하는 흐름을 기본 사용 경로로 제시한다.

```bash
git clone https://github.com/cactus-compute/needle.git
cd needle && source ./setup
needle playground
```

`needle playground`를 띄우면 브라우저(http://127.0.0.1:7860)에서 Gemini로 데이터를 합성하고, Needle을 파인튜닝하고, 평가하고, 결과를 패키징한다. 가중치는 자동으로 다운로드된다.

CLI도 풍부하다.

```
needle playground                  Test and finetune via web UI
needle finetune <data.jsonl>       Finetune on your own data
needle run --query "..." --tools   Single inference
needle train                       Full training run
needle pretrain                    Pretrain on PleIAs/SYNTH
needle eval --checkpoint <path>    Evaluate a checkpoint
needle tokenize                    Tokenize dataset
needle generate-data               Synthesize training data via Gemini
needle tpu <action>                TPU management (see docs/tpu.md)
```

## Cactus 런타임 — 엣지 디바이스 추론 속도

배포 시 Needle은 같은 회사의 [Cactus](https://github.com/cactus-compute/cactus) 런타임 위에서 동작한다. 보고된 속도는 prefill 6000 tok/s, decode 1200 tok/s. 휴대전화·시계·안경 같은 소비자 디바이스를 타깃으로 한다.

저자들의 노선은 "AI를 작은 디바이스에 다시 집어넣기 위해 모델만 줄이는 게 아니라, 모델 구조 자체를 디바이스 형태에 맞춰 다시 설계한다"이다. Needle은 그 노선의 구체 사례다.

## 사용 예 (Python)

```python
from needle import SimpleAttentionNetwork, load_checkpoint, generate, get_tokenizer

params, config = load_checkpoint("checkpoints/needle.pkl")
model = SimpleAttentionNetwork(config)
tokenizer = get_tokenizer()

result = generate(
    model, params, tokenizer,
    query="What's the weather in San Francisco?",
    tools='[{"name":"get_weather","parameters":{"location":"string"}}]',
    stream=False,
)
print(result)
# [{"name":"get_weather","arguments":{"location":"San Francisco"}}]
```

## 가장 흥미로운 지점

가장 인상 깊은 결정은 <strong>FFN을 제거한 자리에 더 깊은 어텐션과 인코더-디코더 분리, 그리고 도구 검색 헤드를 함께 넣은 것</strong>이다. 작은 모델은 보통 큰 모델의 축소판이지만, Needle은 태스크에 불필요한 회로를 들어내고 그 예산을 *태스크에 더 잘 맞는 회로*로 옮긴다. "작게 만든다"가 아니라 "다르게 만든다"에 가깝다.

또 하나는 학습-추론 정합성을 위해 INT4 QAT를 정규화로 동시에 활용한다는 점이다. 보통 QAT는 배포 직전 손실을 줄이기 위한 조정 단계로 쓰는데, Needle은 사전훈련 단계부터 100스텝마다 fake quantization을 끼워 넣어 모델이 "양자화된 자기 자신"으로 학습된다. 부수적으로 작은 모델의 과적합도 누른다. 작은 모델이 가장 약한 두 지점(과적합과 PTQ 갭)을 같은 손잡이로 해결한다.

## 출처

저자: Henry Ndubuaku, Jakub Mroz, Karen Mosoyan, Roman Shemet, Parkirat Sandhu, Satyajit Kumar, Noah Cylich, Justin H. Lee (Cactus Compute, 2026).

원문 리포: <https://github.com/cactus-compute/needle>
아키텍처 문서: <https://github.com/cactus-compute/needle/blob/main/docs/simple_attention_networks.md>
HuggingFace 가중치: <https://huggingface.co/Cactus-Compute/needle>
Cactus 런타임: <https://github.com/cactus-compute/cactus>

원문은 README와 아키텍처 노트, 모델 카드 형식으로 짧게 정리되어 있다. 외부 URL로 인용 가능한 도식이 없어 본 다이제스트에는 이미지를 싣지 않았다. 리포 안에는 ASCII 아키텍처 다이어그램과 `assets/banner.png` 한 장이 있다.
