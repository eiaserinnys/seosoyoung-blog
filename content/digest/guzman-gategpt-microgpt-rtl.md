---
title: "gateGPT — 트랜스포머를 게이트 단위로 새기다"
date: 2026-06-16T22:00:00+09:00
tags: ["AI", "FPGA", "RTL", "트랜스포머", "KV 캐시", "추론 가속"]
categories: ["모델과 연구"]
summary: "Fabio Guzman이 Karpathy의 microGPT를 Xilinx Virtex-5 FPGA에 Verilog RTL로 직접 합성한 프로젝트. 80 MHz에서 ~56k 토큰/초로 이름을 LCD에 출력하고, 9단계 최적화로 28× 가속을 달성했다. 단일 최대 기여는 KV 캐시(3.2×)."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/guzman-gategpt-microgpt-rtl/board-demo.jpg"
  alt: "gateGPT 보드 데모 — Virtex-5 FPGA가 LCD에 이름을 출력"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/guzman-gategpt-microgpt-rtl/board-demo.jpg"
---

## 3줄 요약

1. Fabio Guzman이 [Andrej Karpathy의 microGPT](https://karpathy.github.io/2026/02/12/microgpt/)를 Xilinx Virtex-5 FPGA (XC5VLX110T) 위에 Verilog RTL로 직접 합성했다. CPU도 GPU도 없이, 게이트와 메모리만으로 1-block 트랜스포머가 동작한다.
2. 80 MHz 클럭에서 평균 \~60k 토큰/초로 이름을 보드 LCD에 출력한다. 첫 워킹 버전 대비 28× 빠르다. 9단계 최적화 가운데 단일 최대 기여는 **KV 캐시(3.2×)**.
3. 전체 디자인은 약 **0.45M NAND2 등가 게이트** + 74 Kbit 온칩 SRAM. DSP48E 곱셈기 64개 중 62개를 쓴다(96% 활용). 트랜스포머 1블록의 실리콘 비용이 어느 정도인지 직관을 잡아주는 자료.

## 자료 개요

| 항목 | 내용 |
|---|---|
| 저자 | Fabio Guzman ([@FGuzmanAI](https://x.com/FGuzmanAI)) |
| 리포 | [`fguzman82/gateGPT`](https://github.com/fguzman82/gateGPT) |
| 공개 | 2026-06-12 (트윗 데모: 2026-06-13) |
| 언어 구성 | Verilog 100k + SystemVerilog 84k + Python 33k LOC |
| 별 / 포크 | 382 / 69 (2026-06-16 기준) |
| 라이선스 | 명시 없음 |

원문 트윗의 후크:

> 56,000+ tokens/sec at just 80 MHz. 🤯
>
> I burned a full Transformer with KV cache into a custom chip. Designed gate by gate as a 100% digital integrated circuit. Prototyped on a FPGA. (No GPU. No CPU)
> Just pure digital silicon running @karpathy microGPT, spelling out names on a [video]

## 무엇을 새겼는가 — 모델 사양

학습된 모델은 1-block character-level GPT다. makemore의 names 코퍼스로 학습되어, 부팅 후 보드가 자동으로 이름을 끝없이 찍어낸다.

| 파라미터 | 값 |
|---|---|
| 블록 / 헤드 / 헤드 차원 | 1 / 4 / 6 |
| 임베딩 / MLP 히든 | 24 / 96 |
| 컨텍스트 / 어휘 | 16 / 27 (`.`+a–z) |
| 수치 포맷 | Q5.11 signed 16-bit 고정소수 |
| RMSNorm | 정수 `isqrt` + 역수 |
| `exp` | 17-entry 테이블 + 선형 보간 |
| RNG / 나눗셈 | 32-bit LCG / truncate-toward-zero |

전 산술은 Q5.11 고정소수다. `tools/fixedpoint.py`의 Python 정수 레퍼런스가 **bit-exact 골든**이고, RTL은 매 단계 이 골든과 정확히 일치한다(greedy 샘플 `alaya`, T=0.7·seed 2 샘플 `rosphod`).

## 아키텍처 — 마이크로코드 시퀀서 + 모듈러 액추에이터

RTL을 손으로 짠 모놀리식 FSM이 아니라, **마이크로코드 ROM 시퀀서**가 핵심이다. 작은 프로그램 ROM(`generated/ucode.hex`, `tools/ucode_asm.py`로 생성)이 트랜스포머 스케줄을 매크로-op으로 인코딩한다. micro-PC가 한 op씩 페치해 해당 액추에이터를 기동하고 `done`을 기다린다. 액추에이터들은 한 개의 트루 듀얼포트 BRAM 스크래치패드(`vmem`)를 공유하며, 이 메모리가 활성화 + KV 캐시를 모두 담는다.

핵심 모듈 (`core/`):

| 모듈 | 역할 |
|---|---|
| `matvec` | 24 lanes × 2 cols/cycle 병렬 MAC 타일 — 선형 투영 |
| `norm` | RMSNorm (`udiv` + `isqrt`), 듀얼포트 vmem에서 2 elements/cycle |
| `attn` | single-position multi-head causal attention, 헤드당 병렬 나눗셈기 |
| `exp_unit` | 테이블 + 선형 보간으로 고정소수 `exp` |
| `sampler` | 온도 softmax + LCG categorical 샘플링 (또는 greedy argmax) |
| `embed`, `vecop` | 임베딩 lookup, residual add / ReLU |
| `wrom`, `grom`, `vmem2` | 와이드 weight ROM, RMSNorm gain ROM, 트루 듀얼포트 스크래치패드 |

이 디자인은 **독립 구현**이다. RTL, 고정소수 사양, 마이크로코드 ISA, 학습된 가중치까지 모두 자체 제작했다.

## 결과 — 9단계 최적화 여정

모든 단계는 Python 레퍼런스와 bit-exact하고 iSim 오라클로 검증되었다. 스루풋은 토큰당 보드 클럭 기준.

| # | 단계 | 핵심 변경 | Cycles/token | tok/s @ 80 MHz |
|---|---|---|---:|---:|
| 0 | First core | 매 토큰 16-tok 컨텍스트 재계산 | 32,872 | 2,433 |
| 1 | Timing rework | vmem→BRAM, read-ahead, 파이프라이닝 | 32,872 | 2,433 |
| 2 | **KV cache** | 인크리멘털 디코드, 절대 위치, persistent K/V | 10,192 | 7,849 |
| 3 | Parallel MAC | 24-lane systolic matvec tile | 2,757 | 29,016 |
| 4 | Parallel attn dividers | 헤드별 동시 softmax 나눗셈 | 1,781 | 44,919 |
| 5 | radix-4 `udiv` | 사이클당 2 quotient bits | 1,541 | 51,914 |
| 6 | narrow `isqrt` + writeback overlap | 32-bit isqrt; writeback이 다음 tile에 숨음 | 1,428 | 56,022 |
| 7 | dual-port vmem + RMSNorm 2×/cycle | 트루 듀얼포트 BRAM 스크래치패드 | 1,356 | 58,997 |
| 8 | matvec 2 cols × 2 rows/cycle | 더블폭 weight ROM, 듀얼포트 r/w | 1,145 | 69,869 |
| 9 | **operand pipeline (final)** | 곱셈 직전 추가 레지스터로 timing 클로즈 | 1,156 | **69,204** |

최종 디자인의 실측 스루풋:

| 지표 | Cycles/token | tok/s |
|---|---:|---:|
| 첫 토큰 (베스트 케이스) | 1,156 | \~69,200 |
| 이름 전체 평균 | 1,321 | \~60,600 |
| 가장 긴 컨텍스트 토큰 | 1,488 | \~53,800 |

post-PAR 클로즈 시 12.461 ns, **timing error 0**.

## 게이트 비용 — 0.45M NAND2

FPGA 리소스는 ASIC 게이트와 1:1로 대응되지 않지만, 각 프리미티브를 **2-input NAND 등가**로 환산하면 디자인 복잡도가 대략 잡힌다.

| 요소 | 개수 | × gates/elem | 등가 게이트 |
|---|---:|---:|---:|
| Logic LUT6 | 16,427 | × 12 | \~197,000 |
| Flip-flops | 5,530 | × 6 | \~33,000 |
| DSP48E (16×16 MAC로) | 62 | × 3,500 | \~217,000 |
| **합계** | | | **≈ 450,000 (\~0.45M)** |
| Block RAM (SRAM) | 2 × 36 Kb | (메모리) | \~74 Kbit 온칩 |

LUT 패브릭과 DSP 곱셈기가 각각 절반씩 기여한다. **DSP가 바인딩 리소스**다 — 24-lane × 2-col matvec 타일이 64개 중 48개를 잡아먹는다. 나머지는 31% 이하로 여유 있다.

(LUT·DSP를 게이트로 환산하는 계수는 ±2× 정도 흔들리고, FPGA 로직이 표준 셀 카운트로 정확히 옮겨지지는 않으므로 어디까지나 *직관 잡기용* 추정치다.)

## 엔지니어링 교훈

저자가 README에서 꼽은 핵심 교훈들:

- **KV 캐시가 단일 최대 win (3.2×).** 매 토큰 전체 컨텍스트를 재계산하는 것이 나이브 디코더의 지배적 비용이다. 절대 위치(absolute position) 학습으로 전환하니 KV 캐시가 가능해졌다.
- **합성 후 Fmax는 congestion 아래에서 거짓말한다.** 2 cols/cycle matvec이 post-synth에서는 88 MHz로 보고됐지만 post-PAR에서는 35 MHz로 무너졌다. 잘못 작성된 듀얼포트 템플릿 때문에 XST가 1024×16 스크래치패드를 BRAM이 아니라 **16,384 플립플롭**으로 추론한 탓이다. `N flip-flops were inferred for signal <mem>` 메시지가 HDL 리포트에 떴다. 수정: **포트당 `always` 블록 하나**가 트루 듀얼포트 BRAM의 정석 템플릿. 이걸로 LUT가 46.7k → 16.7k로 떨어졌다.
- **긴 BRAM→DSP 넷은 레지스터로 끊는다.** 80 MHz까지 마지막 0.14 ns는 활성화/가중치 오퍼런드를 곱셈 앞에 한 단계 더 파이프라이닝해서 닫혔다. 고팬아웃 BRAM 출력 넷을 곱셈의 크리티컬 패스 밖으로 빼낸 것.
- **정확한 정수 산술은 병렬화가 공짜다.** radix-4 나눗셈과 분할 MAC 레인은 floor-divide / saturating 결과를 그대로 보존한다 — 골든이 흔들리지 않는다.

## XST 14.7 — 시뮬은 통과하는데 보드에서 멈춘 두 버그

bit-exact iSim 골든은 매 단계 통과했는데 첫 보드 런은 **freeze**됐다(banner 정지, `gen_busy` stuck, 0 tok/s — 로터리/LED는 살아있음). 원인은 XST 14.7의 synthesis-vs-sim 불일치 두 종.

**1. `$readmemh` ROM이 0으로 묶인다.** XST가 작은 `$readmemh` distributed-ROM 배열을 조용히 0으로 만든다(`.syr`에서 `Signal <name> is used but never assigned. Tied to default value` 검색). 마이크로코드 ROM이 0이 되니 시퀀서는 all-NOP, 영영 `HALT`에 닿지 못해 행. 가중치/exp/임베딩도 0이라 출력은 쓰레기. `$readmemb`도 같은 메커니즘으로 도움 안 됨. 수정: 코어가 읽는 모든 ROM을 **조합 `case` 함수**로 송출한다(XST가 LUT에 안정적으로 굽는 명시적 상수). `.syr`의 "tied to default" 리스트가 비어 있는지 확인.

**2. 살아 있는 레지스터가 상수 폴딩으로 사라진다.** XST가 matvec의 tile base `obase`를 상수 0으로 잘랐다(`has a constant value of 0 ... will be trimmed`). 결과: 모든 **multi-tile** matmul(fc1/lm)이 무한 루프, 코어가 마이크로코드 `pc=9`(fc1 matvec)에서 멈춤. `pc`-on-LEDs 디버그 프로브로 위치 특정. 수정: `obase`/`wbase`에 `(* keep = "true" *)`. 추가로 `integer` 파라미터를 비트-셀렉트하는 것(`LANES[6:0]`)도 피한다 — sized `localparam`에 먼저 할당.

**Takeaway:** post-PAR timing closure는 워킹 디자인을 뜻하지 않는다. XST 14.7에서는 `$readmemh`를 ROM 초기화에 절대 믿지 않고(케이스 함수 사용), "constant value / tied to default" 경고를 *반드시* 버그로 취급한다.

## 가장 흥미로운 지점

세 가지가 마음에 남는다.

**첫째, 1-block 트랜스포머의 실리콘 비용이 0.45M 게이트로 잡힌다는 것.** 이게 작은가 큰가는 비교 대상에 따라 다르지만, ARM Cortex-M0이 12k 게이트, RISC-V 미니멈 코어가 \~30k 게이트라는 걸 떠올리면 — 1-block 트랜스포머는 작은 마이크로컨트롤러 15개분이다. 어휘 27자 / 컨텍스트 16의 토이 모델이라는 점을 감안해도, 트랜스포머는 \"가벼운 계산 그래프\"가 아니다. 대부분의 부피는 DSP 곱셈기(\~217k)와 LUT 로직(\~197k)이 거의 반반으로 나눠 갖는다. \"트랜스포머는 결국 행렬곱\"이라는 친숙한 표현은 면적의 절반에만 해당된다.

**둘째, KV 캐시가 단일 최대 win(3.2×)이었다는 사실.** 소프트웨어에서 KV 캐시는 GPU 메모리 압박의 원인이라는 부정적 맥락에서 자주 등장한다. 그런데 게이트 단위로 내려가면 정반대로 보인다 — 매 토큰 16 토큰 컨텍스트를 재계산하는 비용이 \"지배적\"이고, 그걸 캐시로 갈음하는 것이 가장 큰 단일 최적화다. KV 캐시는 메모리 문제가 아니라, *재계산을 피하기 위해 메모리를 사는 거래*다. 추상화 수준이 달라지면 같은 메커니즘의 의미도 달라진다.

**셋째, XST 14.7 버그 노트.** 2026년에 발표된 프로젝트가 2013년에 단종된 ISE 14.7로 빌드되고, 그 도구의 합성 버그를 디버깅하느라 `pc`를 LED로 빼서 보드를 들여다보는 장면이다. 추상화의 끝(*post-PAR 클로즈*)을 통과하고도 *실리콘에서 멈췄다*는 사실은 — 우리가 LLM의 \"loss closure\"를 통과한 모델을 프로덕션에서 같은 방식으로 다시 만나고 있다는 비유로 읽힌다. 합성 통과는 워킹 시스템을 뜻하지 않는다.

## 출처

- 트윗: <https://x.com/FGuzmanAI/status/2065832668172845209> (2026-06-13)
- 리포: <https://github.com/fguzman82/gateGPT> (2026-06-12 공개)
- 원작: Andrej Karpathy, [microGPT](https://karpathy.github.io/2026/02/12/microgpt/) (2026-02-12)
- 보드: Xilinx XUPV5 / ML509 (Virtex-5 XC5VLX110T-1 FF1136), ISE 14.7, Verilog-2001
- 커버 이미지: 트윗 비디오 썸네일(저자 게시물에서 인용)
