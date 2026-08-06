---
title: "Understanding and Coding the KV Cache in LLMs from Scratch — Sebastian Raschka"
date: 2026-04-30T14:10:00+09:00
tags: ["LLM", "추론 효율성", "KV 캐시", "PyTorch"]
categories: ["모델과 연구"]
summary: "KV 캐시가 무엇이고, PyTorch로 어떻게 처음부터 구현하며, 왜 CPU에서는 5배 빨라지지만 작은 GPU 모델에서는 효과가 사라지는지를 from-scratch 코드로 짚은 튜토리얼."
ShowToc: true
TocOpen: false
sidenotes: true
---

> Ahead of AI · Sebastian Raschka · 2025-06-17

LLM 추론을 다루는 사람이라면 KV 캐시라는 단어를 한 번쯤 들어봤을 것입니다. 그런데 정작 "그게 정확히 어떤 텐서를 어디에 저장하는 건가요?"를 물으면 답이 흐릿해지는 경우가 많습니다. Raschka는 자신이 쓴 *Build a Large Language Model (From Scratch)* 책에 일부러 넣지 않았던 KV 캐시 챕터를, 별도 글로 풀어 공개했습니다. 코드가 짧고, 주석이 친절하며, 측정까지 포함되어 있어 그 자체로 좋은 레퍼런스입니다.

## 3줄 요약

1. KV 캐시는 자기회귀 디코딩이 매 스텝마다 이전 토큰의 키·밸류를 재계산하는 본질적 중복을 제거합니다. 누적 비용이 O(n²)에서 O(n)으로 떨어집니다.
2. PyTorch에서는 `register_buffer`로 K/V 슬롯을 등록하고, `use_cache` 플래그 분기에서 `torch.cat`으로 누적하며, 세션 간에는 반드시 캐시를 리셋하는 5단계 변경으로 구현됩니다.
3. Mac M4 CPU에서 124M GPT가 200토큰 생성 시 약 5배 빨라지지만, 작은 모델 GPU에서는 호스트–디바이스 통신 오버헤드가 이득을 상쇄합니다. KV 캐시 효과는 디바이스·모델 크기·구현 형태의 함수입니다.

## KV 캐시는 무엇이고 왜 필요한가

LLM은 토큰을 한 개씩 자기회귀적으로 생성합니다. "Time"이라는 프롬프트로 "flies"를 만들고, "Time flies"로 "fast"를 만드는 식입니다. 문제는 두 번째 스텝에서 모델이 "Time"과 "flies"를 다시 한 번 통과시킨다는 점입니다 — 그것도 정확히 같은 키와 밸류 벡터를 다시 계산하면서.

어텐션의 정의를 다시 보면 이유가 분명합니다. 새 쿼리는 모든 과거 키와 상호작용해야 하므로 매 스텝 새로 계산되어야 합니다. 그러나 과거 토큰의 키·밸류는 변하지 않습니다. 한 번 계산해 두면 그대로 재사용해도 결과가 동일합니다. KV 캐시는 이 비대칭에서 출발합니다 — Q는 매번, K/V는 한 번만.

> 첫 토큰의 K/V는 N-1번, 두 번째는 N-2번 재사용됩니다. 시퀀스가 길어질수록 절약 효과는 토큰 수에 비례해 누적됩니다. 짧은 프롬프트에서는 효과가 작지만, 긴 컨텍스트 추론에서는 KV 캐시 없이 사실상 실시간 응답이 불가능합니다.

## 처음부터 구현하기 (5단계)

Raschka는 `gpt_ch04.py`(캐시 없음)와 `gpt_with_kv_cache.py`(캐시 있음) 두 파일을 GitHub에 올려 두고, `# NEW` 주석으로 변경 지점만 표시합니다. 차이는 다섯 군데입니다.

### 1. 캐시 버퍼 등록

`MultiHeadAttention` 생성자에 두 개의 버퍼를 추가합니다.

```python
self.register_buffer("cache_k", None)
self.register_buffer("cache_v", None)
```

`register_buffer`는 학습되지 않는 상태이지만 `.to(device)` 호출에 자동으로 따라가는 PyTorch 패턴입니다. KV 캐시는 학습 그래프에 들어가서는 안 되지만 디바이스는 따라가야 하므로 정확히 이 위치가 맞습니다.

### 2. `use_cache` 플래그로 store/retrieve

`forward`에 `use_cache` 인자를 추가하고, 분기 한 곳을 둡니다.

```python
if use_cache:
    if self.cache_k is None:
        self.cache_k, self.cache_v = keys_new, values_new
    else:
        self.cache_k = torch.cat([self.cache_k, keys_new], dim=1)
        self.cache_v = torch.cat([self.cache_v, values_new], dim=1)
    keys, values = self.cache_k, self.cache_v
else:
    keys, values = keys_new, values_new
```

이 한 분기가 KV 캐시의 핵심입니다. `torch.cat`으로 새 K/V를 누적하고, 어텐션 계산은 누적된 전체 K/V로 수행합니다. `use_cache=False`일 때는 캐시를 무시하므로 한 모델로 학습·추론 두 모드를 모두 깔끔하게 지원할 수 있습니다.

### 3. 세션 간 캐시 리셋

새 프롬프트로 생성을 다시 시작할 때 캐시를 비우지 않으면, 새 쿼리가 이전 시퀀스의 K와 어텐드하여 무관한 컨텍스트가 출력에 새어 들어갑니다. 따라서 명시적 리셋이 필요합니다.

```python
def reset_cache(self):
    self.cache_k, self.cache_v = None, None
```

### 4. `current_pos` 카운터로 위치 정렬

캐시를 쓰면 모델에 들어가는 새 토큰의 시퀀스 길이는 1이지만, 위치 인코딩은 캐시된 K/V의 끝에 이어붙어야 합니다. 매번 0부터 다시 세면 새 토큰이 마치 첫 토큰인 것처럼 처리됩니다. `GPTModel`에 `current_pos` 카운터를 두고 매 스텝 `seq_len`만큼 증가시킵니다.

```python
if use_cache:
    pos_ids = torch.arange(
        self.current_pos, self.current_pos + seq_len,
        device=in_idx.device, dtype=torch.long
    )
    self.current_pos += seq_len
```

대안으로 `offset = block.att.cache_k.shape[1]`로 캐시 길이에서 직접 역산할 수도 있습니다.

### 5. 생성 루프에서 입력 형태가 달라진다

핵심은 캐시 ON/OFF에서 모델에 들어가는 입력 형태가 다르다는 점입니다.

```python
if use_cache:
    model.reset_kv_cache()
    logits = model(idx[:, -ctx_len:], use_cache=True)  # 첫 호출: 전체 프롬프트
    for _ in range(max_new_tokens):
        next_idx = logits[:, -1].argmax(dim=-1, keepdim=True)
        idx = torch.cat([idx, next_idx], dim=1)
        logits = model(next_idx, use_cache=True)        # 이후: 새 토큰 한 개만
else:
    for _ in range(max_new_tokens):
        logits = model(idx[:, -ctx_len:], use_cache=False)  # 매번 전체 시퀀스
        next_idx = logits[:, -1].argmax(dim=-1, keepdim=True)
        idx = torch.cat([idx, next_idx], dim=1)
```

캐시가 있으면 두 번째 호출부터는 `next_idx` 한 개의 토큰만 모델에 넘깁니다. 캐시가 없으면 매 스텝 `idx[:, -ctx_len:]` 전체를 다시 넘깁니다. 이 입력 형태 차이가 속도 차이의 직접적 원천입니다.

## 트레이드오프

KV 캐시는 공짜가 아닙니다.

| 항목 | 캐시 없음 | 캐시 있음 |
| --- | --- | --- |
| 토큰당 어텐션 작업 | O(t) — 매 스텝 t개 K와 비교 | O(1) — 새 K만 계산, 나머지는 인출 |
| 누적 작업량 | O(n²) | O(n) |
| 메모리 | 일정 | 토큰 수에 선형 증가 |
| 학습 시 사용 | 가능 | 불가 (전체 위치 그래디언트 필요) |
| 코드 복잡도 | 단순 | 분기·리셋·위치 추적 추가 |

학습 시에는 모든 위치의 K/V가 그래디언트를 가져야 하므로 KV 캐시를 쓸 수 없다는 점은 자주 잊힙니다. KV 캐시는 추론 전용 최적화입니다.

정합성 검증의 표준은 단순합니다 — 캐시 ON과 OFF의 토큰 출력이 비트 단위로 일치하는지 보면 됩니다. 인덱싱 실수로 KV 캐시 결과가 미묘하게 어긋나는 경우가 많기 때문에, 같은 untrained 모델로 두 경로를 돌려 출력이 똑같은지 확인하는 것이 디버깅의 출발점입니다.

## 스케일링 최적화

가독성 우선 구현 그대로는 큰 모델·긴 시퀀스에서 무너집니다. 두 가지 한계가 핵심입니다.

### Tip 1. 사전 할당 텐서

매 스텝 `torch.cat`으로 캐시를 키우면 PyTorch가 매번 새 메모리를 할당하고 복사합니다. 토큰 수가 많아질수록 단편화와 할당 오버헤드가 누적됩니다. 최대 시퀀스 길이만큼의 텐서를 미리 할당하고 슬라이스에 in-place로 쓰면 메모리 사용이 일정해지고 속도도 안정됩니다.

```python
max_seq_len = 1024
cache_k = torch.zeros(
    (batch_size, num_heads, max_seq_len, head_dim), device=device
)
cache_v = torch.zeros(
    (batch_size, num_heads, max_seq_len, head_dim), device=device
)
```

### Tip 2. 슬라이딩 윈도우 절단

긴 생성에서 GPU 메모리가 터지는 것을 막는 가장 단순한 방법은 슬라이딩 윈도우입니다.

```python
window_size = 512
cache_k = cache_k[:, :, -window_size:, :]
cache_v = cache_v[:, :, -window_size:, :]
```

모델은 가장 최근 `window_size` 토큰에만 어텐드하지만, 메모리는 상수로 고정됩니다. 정확도와 메모리의 명시적 트레이드오프입니다.

### 큰 컨텍스트의 사전 할당 비용

Llama 3(131k)·Qwen3(41k)처럼 컨텍스트가 큰 모델에서 사전 할당 KV 캐시는 추가로 약 8GB의 메모리를 묶어둡니다. 사전 할당의 속도 이점이 분명해도, 실제 사용량과 무관하게 차지하는 비용을 감안해 `torch.cat` 방식과 비교 결정해야 합니다.

### 외부 캐시 + `torch.compile`

KV 캐시를 `MultiHeadAttention` 내부 buffer로 두면 `torch.cat`이 그래프 컴파일을 깨뜨립니다. 캐시를 모델 바깥의 별도 객체로 분리해 `forward`에 명시적으로 넘기면, 모델 자체는 정적 그래프가 되어 `torch.compile`로 추가 가속을 얻을 수 있습니다.

## CPU vs GPU 측정

Raschka가 직접 돌린 측정은 인상적입니다.

| 환경 | 모델 | 결과 |
| --- | --- | --- |
| Mac mini M4 CPU | 124M GPT, 200토큰 | KV 캐시로 약 5배 가속 |
| 동일 환경 + 사전 할당 + 슬라이딩 | 124M GPT, 200토큰 | 추가 가속 (창 크기 = 컨텍스트일 때 동일 결과) |
| CUDA GPU | 124M GPT (작은 모델) | KV 캐시 효과 사라짐 |
| CPU | Qwen3 0.6B / Llama 3 1B | KV 캐시 단독이 가장 큰 가속, +`torch.compile`로 한 단계 더 |
| GPU | Qwen3 0.6B / Llama 3 1B | "캐시 없는 일반 컴파일"이 최고 |

GPU에서 작은 모델의 KV 캐시 이득이 사라지는 이유는, 한 번의 전체 패스가 이미 마이크로초 단위로 끝나는 반면 캐시 관리에 따른 호스트–디바이스 통신과 텐서 연산 디스패치 오버헤드가 그 절약량을 상쇄하기 때문입니다. KV 캐시 효과는 "모델 크기 × 디바이스 × 구현 형태"의 3차원 함수이지 단일 스위치가 아닙니다.

## 가장 흥미로운 지점

이 글에서 제일 인상 깊었던 것은 코드가 아니라 측정 표였습니다. KV 캐시를 "당연히 켜는 최적화"로 받아들이기 쉽지만, GPU에서 작은 모델은 오히려 일반 컴파일이 더 빠르다는 결과는 다른 KV 관련 최적화(MLA, Paged KV, 레이어별 분할 등)를 볼 때 첫 질문을 바꿔줍니다 — "이 최적화가 어느 디바이스의 어느 모델 크기에서 의미 있는가?"

또 한 가지는 정합성 검증의 단순함입니다. 캐시 ON/OFF의 출력이 비트 단위로 같은지만 확인하면 KV 캐시 구현의 거의 모든 인덱싱 버그를 잡을 수 있습니다. 큰 시스템에서 미묘한 정합성 문제로 며칠을 태우는 일이 흔한데, 가장 단순한 페어 테스트가 가장 강력한 안전장치라는 점은 다른 추론 최적화에도 그대로 적용할 만합니다.

## 출처

발행: Ahead of AI (Sebastian Raschka, PhD), 2025-06-17
원문: <https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms>
코드: <https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/03_kv-cache>
