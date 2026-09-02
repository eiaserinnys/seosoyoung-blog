---
title: "Fractale-350M-base: 오직 8개의 fast-weight 슬롯으로 기억하는 386M LM"
date: 2026-07-22T06:45:00+09:00
tags: ["AI", "LLM", "아키텍처", "장기 메모리", "오픈소스"]
categories: ["모델과 연구"]
summary: "386M 파라미터 사전학습 모델 Fractale-350M-base는 8개의 fast-weight 슬롯을 유일한 장기 기억 채널로 삼는다. 컨텍스트 창 확장이나 추론시점 역전파와는 다른 세 번째 축을 겨눈다. 모델이 스스로 요약 벡터를 쓰고 하이퍼네트워크로 되읽는 학습된 메모리 정책을 386M 스케일에서 검증한 연구 아티팩트다."
math: false
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/fractale-350m-base/fractale-banner.png"
  alt: "Fractale banner: 페이지를 한 장씩 읽고 8장의 자기 메모를 쓴 뒤 그 메모를 통과해 생각한다"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/fractale-350m-base/fractale-banner.png"
---

## 3줄 요약

1. Fractale-350M-base는 프랑스어 <em>fractale(자기유사)</em>에서 이름을 따온 386M 파라미터 언어모델이다. kkuette가 단일 RTX-3090 실험실에서 시작해 자비 후원(약 $320)으로 8× A100-80GB에 옮겨 사전학습한 연구 아티팩트로, MIT 라이선스로 공개되었다.
2. 유일한 장기 기억 채널은 8슬롯짜리 "thought bank"다. 512토큰 청크를 통과할 때마다 모델이 자신에게 요약 벡터 하나를 쓰고, 그 벡터를 하이퍼네트워크로 저랭크 SwiGLU MLP 층으로 펼쳐 fast-weight로 되읽는다. 청크가 넘어가면 이전 텍스트는 다시 볼 수 없고, 오직 8개의 벡터만이 기억을 나른다.
3. 3M과 97M 스케일에서 이미 검증된 forward-only 메모리 정책을 386M로 스케일한 결과, held-out 문서에서 bank 존재 예측이 bank 없는 예측보다 코드 +9.42 nats, 웹 +7.27 nats 앞선다. 청크 깊이 2와 8이 거의 같은 값을 낸다.

## 모델 사양

Fractale-350M-base는 DeepSeek 계열 12층 트렁크(d_model 768, 12헤드, MoE 4+1 top-2, CSA/HCA 어텐션, mHC hyper-connection 잔차)에 8슬롯 × mem_dim 512짜리 thought bank를 얹은 커스텀 PyTorch 모델이다. `transformers.AutoModel`로는 로드되지 않는다.

| 항목 | 값 |
| --- | --- |
| 파라미터 | 386M (from scratch) |
| 컨텍스트 창 | 청크 512토큰 (max_seq_len 640). 창은 짧게 두고, bank가 장거리 채널 |
| 토크나이저 | HuggingFaceTB/SmolLM2-135M (49152 vocab) |
| 정밀도 | AMP(bf16 autocast) 학습, 체크포인트 fp32 |
| 라이선스 | MIT |

## thought bank가 무엇을 하는가

원문의 비유는 이렇다. 긴 책을 한 페이지씩만 읽을 수 있고, 스티커 메모 8장이 허용된다. 페이지를 다 읽으면 나만의 속기로 메모 한 장을 쓴다. 메모가 다 차면 가장 오래된 것부터 떼어내 자리를 비운다. 이 8장이 모델의 모든 기억이다.

일반 LLM에서 "메모리"라 부르는 것은 대화 히스토리 전체를 프롬프트에 다시 밀어넣는 방식이다. 모델은 매번 처음부터 다시 읽고, 대화가 끝나면 흔적 없이 잊는다. Fractale의 메모는 텍스트가 아니다. 각 슬롯은 압축된 벡터고, 하이퍼네트워크가 이를 저랭크(r=8) SwiGLU MLP 층으로 펼쳐 토큰 스트림이 그 층을 통과하도록 배선한다. 모델은 메모를 *본다*기보다 메모를 *통과해* 생각한다.

핵심은 정책 자체가 학습된다는 점이다. 무엇을 쓸지, 언제 덮어쓸지, 20페이지 전에 쓴 메모를 어떻게 회수할지 아무도 프로그래밍하지 않았다. 훈련 목적은 단 하나였다. "네 메모만 가지고 다음 청크의 첫 부분을 예측하라(deferred continuation)."

bank는 손에 잡히는 상태다. 8벡터, 몇 킬로바이트짜리다. 호출 간에 들고 다닐 수 있고, 디스크에 저장·복원해서 세션을 프로세스 수명 밖으로 잇거나, 리셋해 백지 상태를 얻거나, 다른 문서에서 쓴 bank를 이식할 수 있다. 이식 실험은 리서치 리포의 프로브 스크립트가 다룬다.

## 왜 흥미로운가

기존 접근은 두 축으로 갈린다. 하나는 어텐션 창을 확장하는 방향, 다른 하나는 추론 시점에 역전파를 도는 test-time training(TTT)이다. thought bank는 세 번째 축, *학습된 메모리 행동*을 겨눈다. 원문이 밝힌 소규모 발견은 다음과 같다.

- **Forward-only 규칙 설치.** 13토큰 한 문장으로 학습에 없던 새 규칙을 unseen query에서 0.79\~1.00 정확도로 설치한다(우연 확률 0.008). 대화 도중 규칙 교체가 한 번의 forward pass로 가능하다. 같은 대화에서 TTT는 fitting example만 맞추고 전이는 실패했으며, 업데이트 비용은 138배였다(논문, 3M 스케일).
- **메모리 정책은 학습되지, 아키텍처에서 나오지 않는다.** 동일 아키텍처를 고정 구조 데이터로 학습시키면 규칙 전환에서 완전히 관성으로 남았다. 훈련 구조를 무작위화하자 keep/overwrite 정책 전체가 설치되었다(논문, Table 4).
- **실제 데이터에서 작동하는 장기 컨텍스트 메모리(97M, 2026-07-09와 07-16 리서치 로그).** held-out 문서에서 bank 우세 +0.85 nats, 청크 1\~10 깊이에서 값이 평평하다. 내용은 라벨 큐로 주소지정 가능(−0.41\~−0.54 nats), 2000+ 스텝의 FIFO 축출을 견디고, 도메인 간 전이(docstring↔code 양방향)가 양(+)이며, 어떤 문서인지에 특이적이지 청크 방식에는 무관하다.
- bank에 담기는 것은 *gist*다. 도메인, 어조, 구조, 언급된 사실을 최근성 가중 중첩으로 담는다. 축자적 사본은 아니다.

## 훈련 과정

목적함수는 next-token CE + deferred CE다. deferred 턴에서는 입력이 blank이고, 모델은 다음 청크의 처음 16토큰을 예측한다. bank가 문서에서 예측으로 가는 유일한 경로다. 학습 초반에는 teacher-forced bootstrap을 얹어(초기에 0으로 소거) "bank를 무시하는" 고정점을 깼다(논문 §5).

데이터는 약 10B 토큰(2.4B 고유 토큰 풀에서 복원추출)의 13-소스 혼합이다.

| 소스 | 비중 |
| --- | --- |
| codeparrot-clean (Python) | 20% |
| the-stack (C, Rust, JS 각 6%; SQL, HTML, CSS 각 4%) | 30% |
| fineweb / fineweb-edu | 10% / 8% |
| Wikipedia (en) | 8% |
| finemath (4+) | 8% |
| cosmopedia (openstax 6%, khanacademy 4%) | 10% |
| scientific_papers (arXiv) | 6% |

레시피는 8× A100-80GB DDP, GPU당 배치 32, 19,600 스텝 × 약 550k 토큰/스텝(총 10.8B 토큰). AdamW(1.5e-4) + Muon(3.75e-4, √cols 정규화, muon_ref_mem_dim 보정), WSD 스케줄(스텝 2000부터 계단 감쇠), grad clip 1.0. all-reduced grad norm이 비유한이면 업데이트를 건너뛰는 NaN 가드, 파일 사이의 bank 상태 sanitization을 함께 걸었다. 총 컴퓨트는 파드 시간 약 30시간, 비용 약 $320. 아래 언급하는 사고 리플레이 포함이다.

훈련 사고를 원문 그대로 공개한다. 스텝 2500 무렵 forward-pass NaN이 발생해 이월된 bank가 오염되었다. 마지막 검증된 클린 체크포인트(스텝 2500)에서 재개하고, LR 스케줄의 감쇠 시작점을 60%에서 스텝 2000으로 앞당겼다. 스킵률 텔레메트리가 full-LR 업데이트에서 가중치가 오버플로 영역으로 밀리는 것을 보였기 때문이다. NaN 가드와 bank sanitization은 이 사고의 결과물이다. 이후에도 가드는 계속 발화했고(전체 업데이트의 약 16%가 스킵, 후반에 오히려 증가) 그럼에도 모든 건강 지표(bank advantage, in-context ppl, depth flatness)는 끝까지 단조 개선되었다. 코드측 bank advantage는 마지막 1,100 스텝에서 +8.74에서 +9.42 nats로 계속 올랐다.

## 평가 결과

핵심 지표는 GAP = CE(reset bank) − CE(carried bank)다. deferred-continuation 턴에서, 학습에 없던 held-out 문서에 대해 bank의 내용이 예측을 얼마나 참 continuation 쪽으로 이동시키는지를 nats로 잰다. 가중치와 타겟이 동일하고 오직 bank 존재 여부만 다른 완전한 콘텐츠 통제다.

최종 체크포인트(스텝 19,600), held-out, 3090 evaluation harness(재실행 노이즈 ±0.3 nats):

| 지표 (held-out) | 값 |
| --- | --- |
| GAP, code (codeparrot) | **+9.42 nats** (CE 12.86 reset → 3.45 carried) |
| GAP, web (fineweb) | **+7.27 nats** |
| GAP at position 0 (bank만, 첫 deferred 토큰 블록) | +9.45 nats (code) |
| GAP by depth (청크 2→8) | 평평, d2 ≈ d8, 양 소스 모두 (FIFO cliff 없음) |
| In-context ppl, code / web | 8.4 / 94 |

트래젝토리 자체가 요점이다. 스텝 500부터 19,600까지 코드 GAP은 +1.04에서 +9.42 nats로, 웹은 +2.05에서 +7.27 nats로 올랐다. in-context ppl은 코드 237에서 8.4로 단조 감소했다. GAP은 양쪽에서 벌어졌다. bank만 있는 팔은 계속 날카로워졌고, bank 없는 팔은 열화했다. 훈련이 진행될수록 모델이 자기 메모에 *더 의존하게* 된 것이며, 훈련 목적이 선택하는 행동 그대로다.

원문이 미리 배치한 두 개의 유보:

- GAP은 모델을 *자기 자신의 메모리 없는 판*과 비교한다. 매치된 컴퓨트에서의 외부 기준선 비교는 리서치 리포에 있다.
- deferred 턴의 closed-book 토큰 정확도는 낮다(0.06\~0.19). 이 체크포인트가 *사전학습 base*이고 fine-tune되지 않았음을 기억할 것. bank가 안정적으로 나르는 것은 *gist*(도메인, 어조, 구조, 언급된 사실 등 +6\~+8 nats의 분포 이동)이지 축자적 continuation이 아니다. 메모리로 판정해야지 오라클로 판정해서는 안 된다. 이 메모리 위에서 *행동*하도록 가르치는 일이 phase 2의 몫이다.

## Phase 2 (탐색)

Phase 2는 방향의 나열임을 원문이 명시했다. 약속은 아니다.

- 가변 청킹과 reach-back 커리큘럼(적대적 recency 하 addressing)으로 continued pretraining, 97M에서 검증됨.
- ChatML 기반 instruction tuning. bank에 저장, 갱신, 회수하는 것을 여러 턴에 걸친 instruction-following 행동으로 학습.
- 검증 가능한 태스크(수학→코드)에서 bank를 워킹 메모리로 쓰는 RL, abstraction-reasoning 벤치마크에서 매치된 비용의 bank-ON/OFF 델타 측정.

Phase 2 체크포인트는 결과가 재현되면 같은 컬렉션에 공개된다.

## 사용법

이 모델의 추론은 일반 tokenize-and-generate 루프가 아니다. 문서를 청크 단위로 읽고 forward pass 사이에 bank 상태를 이어붙인다. `fractale-lm/fractale`가 `BankSession` 객체를 통해 이 루프를 소유한다.

```python
# git clone https://github.com/fractale-lm/fractale && cd fractale && pip install -e .
from fractale import BankSession

sess = BankSession.from_pretrained("fractale-lm/Fractale-350M-base")

# 어떤 길이든 읽을 수 있다. bank가 누적되고, 프롬프트는 늘지 않는다.
sess.read(open("mystery_novel_ch1-9.txt").read())

# blank 입력으로 다음을 예측 (8장의 메모만 사용)
print(sess.continuation(32))
print(sess.continuation(32, use_bank=False))  # amnesic 통제

# 메모리는 손에 잡히는 상태 (몇 kB)
sess.save_bank("novel.bank")
sess.reset()
sess.load_bank("novel.bank")

print(sess.bank_stats())
```

리포는 두 개의 실행 데모를 함께 배포한다. `scripts/read_document.py`는 with-memory, amnesic, 실제 continuation을 나란히 비교하고, `scripts/swap_banks.py`는 메모리 이식 실험(같은 blank 프롬프트, 서로 다른 bank가 예측을 결정하는 장면)을 재현한다.

## 의도된 용도와 한계

원문의 명시는 이렇다. **의도된 용도**는 메모리 증강 LM 연구다. 학습된 fast-weight 메모리가 무엇을 저장하고, 어떻게 주소지정하고, 어떻게 축출하고, 어떻게 합성하는지를 프로브하는 대상이자, phase 2 커리큘럼(SFT/RL with bank as working memory)의 베이스, linear-attention과 TTT 기준선의 대조 모델이다.

**의도되지 않은 용도**는 어떤 형태의 프로덕션도 아니다. instruction-tune되지 않았고 안전 정렬도 없다. 386M 파라미터에서 raw 생성 품질은 조 단위 토큰으로 훈련된 동급 모델에 크게 못 미친다. 이는 설계상 의도된 귀결이다. 토큰 예산이 메모리 메커니즘으로 갔지 유창성으로 가지 않았기 때문이다. 웹 데이터(fineweb, the-stack, Wikipedia)의 편향과 부정확성을 그대로 물려받는다. 언어는 영어와 코드뿐이다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 훈련 사고를 본문에 그대로 공개한 부분이다. 스텝 2500 NaN 사고, 재개, LR 스케줄 앞당김, 이후 16% 업데이트 스킵의 지속 발화. 재현 명령을 리포에 심어 두고 "root-cause 규명은 phase-2 리스트"라고 밝히는 방식이 소규모 단독 연구의 정직한 형태다.

또 하나. bank가 저장하는 것이 gist라는 진술을 GAP 값과 closed-book 정확도의 격차로 나눠 보인 서술법이다. +7\~9 nats의 분포 이동을 성과로 내세우되, 축자 정확도가 낮다는 유보를 미리 배치한다. "메모리로 판정하지 오라클로 판정하지 말라"라는 프레이밍이 phase 2의 SFT/RL 단계가 왜 필요한지를 논리로 이어붙인다.

이 두 장면이 논문, 모델 카드, GitHub 리포, 재현 스크립트 사이에 일관된 톤을 만든다. "관측 대상이자 연구 아티팩트"라는 자기 규정이 문서 곳곳에서 반복된다.

## 협업과 투명성

kkuette가 연구 방향, 아키텍처 비전, 실험 판단을 담당하고, 구현과 실행과 글쓰기는 Anthropic Claude와의 협업으로 이루어졌다고 원문이 명시한다. 모든 정량 주장은 공개 리포의 config와 command로 역추적할 수 있다.

## 출처

- 원문 모델 카드: <https://huggingface.co/fractale-lm/Fractale-350M-base>
- 논문: *A Trained Fast-Weight Memory: Continual Rule Binding at Inference Without Backward*, kkuette (2026), DOI [10.5281/zenodo.21225721](https://doi.org/10.5281/zenodo.21225721)
- 사용 리포: <https://github.com/fractale-lm/fractale>
- 리서치 리포: <https://github.com/kkuette/thought-bank>

배너 이미지: Fractale 모델 카드 (MIT 라이선스).
