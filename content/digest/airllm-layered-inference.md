---
title: "AirLLM: 4GB GPU로 70B 모델 돌리기"
date: 2026-07-17T15:00:00+09:00
tags: ["AI", "LLM", "오픈소스", "로컬 추론", "GPU", "양자화"]
categories: ["모델과 연구"]
summary: "AirLLM은 트랜스포머 레이어를 한 장씩만 GPU에 올리는 방식으로 671B 모델을 12GB 카드에 얹는다. 필요 VRAM을 총 파라미터가 아니라 레이어 크기로 바꾸는 영리한 트릭이지만, 그 대가로 토큰마다 모델 전체를 디스크에서 다시 읽는다."
math: false
ShowToc: true
TocOpen: false
cover:
  image: "/images/airllm-layered-inference/star-history.png"
images:
  - "/images/airllm-layered-inference/star-history.png"
---

![AirLLM 로고](/images/airllm-layered-inference/airllm-logo.png)

## 3줄 요약

1. AirLLM은 Gavin Li가 2023년 11월에 공개한 Apache-2.0 파이썬 라이브러리다. 양자화나 증류, 가지치기 없이 70B 모델을 4GB GPU 한 장에서, 671B DeepSeek-V3를 12GB에서 돌린다고 내세운다. 별 22,900개를 모았다.
2. 원리는 단순하다. 모델을 트랜스포머 레이어 단위로 쪼개 디스크에 저장해 두고, 추론할 때 레이어 하나를 GPU에 올려 계산하고 곧바로 내린다. 필요한 VRAM이 모델 총 크기가 아니라 <strong>가장 큰 레이어 하나의 크기</strong>로 결정된다.
3. 대가는 디스크 I/O다. 레이어를 캐시하지 않으므로 토큰 하나를 생성할 때마다 모델 전체를 디스크에서 다시 읽는다. 실사용자 보고로는 7B 모델에 짧은 질문 하나를 던지고 답을 받는 데 10분 안팎이 걸린다.

## 무엇을 하는 라이브러리인가

설치와 사용은 한 줄이다.

```python
from airllm import AutoModel

model = AutoModel.from_pretrained("Qwen/Qwen3-32B")
# model = AutoModel.from_pretrained("Qwen/Qwen3-235B-A22B")     # 235B, ~3GB
# model = AutoModel.from_pretrained("deepseek-ai/DeepSeek-V3")  # 671B, ~12GB
```

허깅페이스 리포 ID를 그대로 넘기면 된다. 지원 모델은 Llama 2/3/3.1/3.3/4, Qwen 1/2/2.5/3(MoE와 FP8 포함), DeepSeek V2/V3/R1, Mistral과 Mixtral, Phi, Gemma, ChatGLM, Baichuan, InternLM, Yi다.

리포가 광고하는 메모리 표는 이렇다.

| 모델 | 크기 | GPU VRAM |
|---|---|---|
| Qwen3 / Mistral / Phi | 8B | \~1–2 GB |
| Qwen3-30B / Mixtral (MoE) | 30–47B | \~1–3 GB |
| Qwen3-235B (MoE) | 235B | \~3 GB |
| Llama 3.x 70B (full precision) | 70B | \~4 GB |
| Llama 3.1 405B | 405B | \~8 GB |
| DeepSeek-V3 | 671B | \~12 GB |

235B MoE 모델이 30B dense 모델보다 적은 VRAM을 쓴다는 점이 표의 논리를 드러낸다. 총 파라미터는 아무 상관이 없고, 레이어 한 장의 크기만이 변수다.

## 코드는 실제로 무엇을 하는가

README만 읽으면 마법처럼 들려서 소스를 직접 확인했다. 핵심 패키지 `air_llm/airllm/`은 파이썬 파일 18개, 1,881줄로 작다.

**모델 분할** — `utils.py`의 `split_and_save_layers()`가 `model.safetensors.index.json`의 `weight_map`을 읽어 `model.embed_tokens.`, `model.layers.{i}.`, `model.norm.`, `lm_head.` 단위로 state_dict를 갈라 낸다. 레이어 하나당 safetensors 파일 하나로 저장하고, 다 쓰면 `<layer>.safetensors.done` 마커 파일을 만들어 둔다. 분할이 중간에 끊겨도 재시작할 때 어디까지 됐는지 알아보기 위해서다.

**추론** — 흥미로운 설계 결정이 여기 있다. 이 라이브러리는 아키텍처별 forward를 재구현하지 않는다. `airllm_base.py`의 `init_model()`은 `accelerate.init_empty_weights`로 진짜 허깅페이스 `AutoModelForCausalLM`을 meta 디바이스에 통째로 올린다. 파라미터는 비어 있고 구조만 있는 껍데기다. 실제 계산은 transformers가 그대로 수행하고, AirLLM은 각 모듈에 forward hook만 건다.

```python
# _install_streaming_hooks() — 각 모듈에 훅 등록
module.register_forward_pre_hook(self._pre_hook)
module.register_forward_hook(self._post_hook)
```

`_pre_hook`은 레이어가 계산되기 직전에 디스크에서 가중치를 읽어 GPU에 올리고, 곧바로 다음 레이어의 로딩을 백그라운드 스레드에 맡긴다. `_post_hook`은 계산이 끝나자마자 `module.to('meta')`로 파라미터를 다시 meta 디바이스로 되돌린다. GPU 메모리가 즉시 비워진다. 뒤이어 `clean_memory()`가 `gc.collect()`와 `torch.cuda.empty_cache()`, 리눅스에서는 `malloc_trim(0)`까지 호출한다.

프리페칭은 CUDA 스트림이 아니라 워커 하나짜리 `ThreadPoolExecutor`다. CPU로 읽어 온 텐서는 `pin_memory()`로 고정해 GPU 전송을 앞당긴다. 다만 압축을 켜면 프리페칭은 강제로 꺼진다. 코드 주석에 "prefetching is not supported together with compression for now"라고 적혀 있다.

## 압축은 양자화와 다르다

`compression='4bit'` 또는 `'8bit'`을 넘기면 3배 빨라진다고 한다.

![압축에 따른 속도 개선](/images/airllm-layered-inference/time-improvement.png)

구현은 `compress_layer_state_dict()`가 레이어의 각 텐서에 bitsandbytes의 `quantize_nf4(blocksize=64)`나 `quantize_blockwise(blocksize=2048)`를 개별 호출하는 방식이다. 로드할 때 다시 dequantize한다.

README가 압축과 양자화를 구분하는 대목이 이 프로젝트의 자기 인식을 가장 잘 보여준다.

> 양자화는 정말로 속도를 내려면 보통 가중치와 활성값을 모두 양자화해야 한다. 그래서 정확도를 지키고 온갖 입력의 이상치 영향을 피하기가 더 어렵다. 반면 우리 경우엔 <strong>병목이 주로 디스크 로딩</strong>이므로, 모델 로딩 크기만 줄이면 된다. 그래서 가중치 부분만 양자화하면 되고, 정확도를 보장하기가 더 쉽다.

계산이 병목이 아니라 디스크 읽기가 병목이니, 읽을 바이트 수만 줄이면 3배가 나온다는 이야기다. 정직한 설명이다. `profiling_mode=True`가 재는 항목도 이 인식과 정확히 일치한다. `load_safe_tensor`(디스크에서 CPU로 읽는 시간)와 `compression_time`(역양자화 시간) 두 가지뿐이고, GPU 전송 시간이나 forward 계산 시간은 아예 재지 않는다.

## v3.0의 FP8은 캐스팅을 하지 않는 것이다

2026년 6월 v3.0의 FP8 지원은 별도 양자화 코드가 아니다. `move_layer_to_device()`가 텐서 dtype이 `float8_e4m3fn`이나 `float8_e5m2`이거나 이름이 `_scale_inv`로 끝나면 캐스팅 없이 그대로 GPU에 얹고, 나머지만 `running_dtype`으로 변환한다. 커밋 메시지에 사연이 남아 있다. FP8 가중치를 fp16으로 캐스팅하면 양자화가 조용히 사라져 "produced garbage"가 나왔다는 것이다.

분할 로직도 FP8 때문에 고쳐졌다. FP8 체크포인트는 가중치마다 짝을 이루는 `weight_scale_inv` 텐서가 따로 있어서 레이어 하나가 여러 shard에 걸친다. 이전 코드는 shard 하나만 읽어 텐서가 누락됐다.

MoE는 사정이 다르다. **MoE 전용 코드가 없다.** `airllm_mixtral.py`는 22줄짜리 빈 서브클래스다. MoE 레이어는 그냥 `model.layers.{i}` 통짜 모듈로 스트리밍된다. 즉 라우터가 고르지 않은 expert까지 전부 디스크에서 읽어 GPU에 올린다는 뜻이다. MoE의 "파라미터는 많지만 실제 연산은 일부만"이라는 장점이 디스크 I/O 관점에서는 하나도 살지 않는다.

## 그래서 얼마나 느린가

README에 절대 속도 수치가 없다. 있는 것은 "3x run time speed up"(압축)과 "10% speed improvement"(프리페칭)라는 상대 배수뿐이고, 나머지는 전부 GB 단위 메모리 수치다.

숫자는 이슈 트래커에 있다. 이슈 #258의 사용자들은 T4 Colab에서 Mistral-7B에 "What is the capital of the United States?" 하나를 물어 답을 받는 데 약 10분이 걸렸다고 보고했다. Qwen-7B에 4bit 압축을 걸고 엔티티 추출을 돌리면 10\~15분이다. 한 코멘트는 이렇게 정리했다.

> AirLLM is openly SLOW because it does all on hard disk. The only way I see a possibility to improve is either someone improving the code or using fast SSD or RAM as disk.

코드 구조를 보면 당연한 결과다. `_post_hook`이 매번 레이어를 meta로 되돌려 버리므로 캐시가 없다. 디코딩 스텝 하나마다 모델 레이어 전체를 처음부터 다시 읽는다. 20토큰을 생성하면 70B 모델 전체를 20번 읽는 셈이다.

커뮤니티가 개선안을 내놓긴 했다. 이슈 #298은 더블 버퍼링으로 I/O 레이턴시를 줄이자고 하고, #269는 디스크에서 RAM, 핀 고정 RAM, GPU로 이어지는 멀티스테이지 파이프라인을 제안한다. 둘 다 열린 채로 커밋이 없다.

재현 가능한 벤치마크도 리포에 없다. 테스트는 `test_compression.py` 하나뿐이고, 내용은 랜덤 텐서 두 개에 압축을 걸어 RMSE가 0.1 미만인지 보는 것이다. 이슈 #295가 정확히 이 지점을 지적한다. "4GB로 70B", "3배속" 같은 헤드라인을 뒷받침할 하드웨어 기록과 측정 스크립트가 없다는 것이다.

## 리포 상태

![스타 히스토리](/images/airllm-layered-inference/star-history.png)

- 별 22,927개, 포크 2,621개, 열린 이슈 106개, 라이선스 Apache-2.0 (2026년 7월 17일 기준)
- 최근 push는 2026년 7월 16일이지만 내용은 스폰서 링크 문서 수정이다. FP8과 MoE 관련 실질 코드 커밋은 6월에 몰려 있다.
- 최상위에 `anima_100k`, `training`, `rlhf`, `eval` 같은 디렉토리가 남아 있다. 저자의 다른 프로젝트(Anima) 잔재로 보인다. 실제 pip 패키지는 `air_llm/` 하나다.
- `AutoModel.from_pretrained()`가 기본값으로 `trust_remote_code=True`를 쓴다. 이슈 #293이 이를 지적하고 있다.

## 가장 눈여겨본 것

이 프로젝트의 매력과 한계는 같은 문장에서 나온다. "병목이 주로 디스크 로딩이다."

보통 추론 최적화는 계산을 줄이려 한다. AirLLM은 계산을 건드리지 않는다. transformers가 원래 하던 계산을 그대로 하게 두고, 가중치가 GPU에 머무는 시간만 극단적으로 줄인다. 그러니 정확도 손실이 없다. 이건 양자화가 아니라 스와핑이고, 운영체제가 40년 전부터 하던 페이징을 레이어 단위로 옮긴 것이다. VRAM 부족을 디스크 대역폭으로 바꾸는 환율 거래다.

문제는 그 환율이 지금 너무 나쁘다는 데 있다. 12GB에 671B가 올라간다는 문장과 7B에 10분이 걸린다는 보고가 동시에 참이다. 별 22,900개는 앞 문장을 보고 모인 숫자고, 열린 이슈 106개는 뒷 문장에서 나온다.

그렇다고 이 아이디어가 틀렸다고 보진 않는다. 환율은 하드웨어가 바꾼다. NVMe가 빨라지고 PCIe 세대가 올라가고 GPU 직결 스토리지 경로가 열리면, 같은 코드가 다른 도구가 된다. 실제로 커뮤니티가 낸 개선안(더블 버퍼링, 멀티스테이지 파이프라인)은 전부 이 환율을 조금이라도 낫게 만들려는 시도다. 다만 그 작업이 열린 이슈로 방치된 채 README 헤드라인만 671B로 갱신되는 지금의 상태는, 이 프로젝트가 실용 도구보다 개념 증명 쪽에 가깝다는 사실을 보여준다.

배치 처리나 오프라인 파이프라인처럼 지연 시간이 상관없는 작업이라면 쓸모가 있다. 대화형으로 쓸 물건은 아니다.

## 출처

Gavin Li, AirLLM (Apache-2.0)
원문: <https://github.com/lyogavin/airllm>
본문의 코드 인용은 2026년 7월 17일 시점의 `main` 브랜치 기준이며, 속도 관련 사용자 보고는 리포 이슈 트래커(#258, #269, #295, #298)에서 가져왔다.
</content>
