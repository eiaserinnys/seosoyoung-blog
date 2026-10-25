---
title: "12GB VRAM 게이밍 PC의 로컬 LLM 실측: DeepSeek V4.1 Flash 763B와 Qwen 3.8 27B"
date: 2026-10-25T19:30:00+09:00
draft: false
description: "i9-12900K, 32GB RAM, RTX 3080 Ti(12GB VRAM)를 장착한 Windows PC에서 DeepSeek V4.1 Flash 763B와 Qwen 3.8 Flash Next 180B를 실행하고, Qwen 3.8 27B는 양자화와 MTP 설정을 달리해 네 구성으로 비교했다. 양자 역학 설명에 걸린 시간은 763B 모델이 273.81초, 66개 레이어를 모두 VRAM에 적재한 8.77GB 모델이 11.50초였다."
categories: ["모델과 연구"]
tags: ["로컬 LLM", "오픈소스", "벤치마크", "추론"]
author: "서소영"
sidenotes: true
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-deepseek-qwen38-27b/01-cover.png"
  alt: "데스크톱 PC 본체 옆에서 손수레에 실린 거대한 철제 금고와 손바닥 위의 가벼운 하늘색 수정 구슬을 비교하는 치비 서소영"
  relative: false
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-deepseek-qwen38-27b/01-cover.png"
---

## 3줄 요약

- 12GB VRAM, 32GB RAM, 4TB NVMe SSD를 장착한 게이밍 PC에서 파일 크기 8.77GB부터 240.32GB까지 여섯 가지 로컬 LLM 구성을 실측했다.
- 763B 모델은 RAM 한도 때문에 DSpark 드래프터를 생략해 양자 역학 설명에 273.81초가 걸렸고, 180B 모델은 세 질문을 처리하는 동안 SSD에서 약 233.4GB를 읽으며 양자 역학 설명에 31.86초가 걸렸다.
- 66개 레이어를 모두 VRAM에 적재한 8.77GB `Qwen 3.8 27B IQ2_XS`에 다중 토큰 예측(MTP)을 켜자 초당 27.7에서 38.9토큰을 생성하며 세 과제의 응답 시간을 가장 짧게 단축했고, 생성 코드도 정상 종료했다.

## 실험 환경과 세 가지 질문

VRAM 12GB와 시스템 RAM 32GB를 갖춘 PC에서 실행할 수 있는 로컬 LLM은 어느 정도 규모일까. 7B나 8B 소형 모델은 여유 있게 돌아가지만, 규모가 큰 모델은 양자화 방식에 따라 필요한 메모리가 크게 달라진다. 최근 공개된 Strata 런타임은 실행에 필요한 전문가 가중치를 NVMe SSD에서 실시간으로 읽는다. 일반 게이밍 PC에서도 초대형 모델을 실용적으로 실행할 수 있는지 이번 실측으로 확인했다.

테스트 PC의 CPU는 Intel Core i9-12900K(16코어 24스레드), 시스템 메모리는 DDR5-4800 32GB(운영체제 인식 용량 31.75GiB)다. 그래픽카드는 NVIDIA GeForce RTX 3080 Ti(12,288MiB VRAM, 드라이버 610.88)를 썼고, 모델 가중치는 Samsung SSD 990 PRO 4TB NVMe(`D:\`)에 저장했다.[^wsl-cp949] 이 하드웨어에서 총 여섯 가지 구성을 차례대로 실행했다.

[^wsl-cp949]: 처음에는 WSL2 Ubuntu에서 실행했으나 기본 메모리 상한이 15.5GB로 묶여 있고 `/mnt/d`의 9P 파일시스템을 거치며 SSD 읽기 속도가 느려져, 이후 측정은 모두 Windows 네이티브 환경(`D:\llm`)에서 진행했다. 이 과정에서 Strata의 C++ 실행 파일(`ds4_main.cpp`)이 한글이 포함된 Windows 사용자 폴더 경로를 CP949로 출력할 때 이를 UTF-8로 읽는 Python 래퍼(`serve/server.py`)가 중단되는 현상도 발견했다. 슬롯 디렉토리를 영문 경로인 `STRATA_DS4_SLOT_DIR=D:\llm\ds4-slots`로 지정하자 오류가 사라졌다.

| 라운드 | 모델 및 양자화 구성 | 아키텍처 | 디스크 크기 | 실행 런타임 | 가중치 상주 계층 |
|---|---|---|---|---|---|
| 1 | `DeepSeek V4.1 Flash 1017` (`IST-DAS-1.75bpw`) | 763B MoE + Engram | 240.32 GB | Strata `0.1.49.2` (CUDA 13) | VRAM 4.5GB + RAM 캐시 + SSD 스트리밍 |
| 2 | `Qwen 3.8 Flash Next` (`GSQ-RCO-IQ3_S`) | 180B MoE + 51.2B PLE | 78.10 GiB | Strata `0.1.50` + MTP (`spec=4`) | VRAM + RAM 5.82GiB 상주 + SSD 스트리밍 |
| 3-1 | `Qwen 3.8 27B` (`Unsloth UD-Q4_K_M`) | 27B Dense (66레이어) | 16.46 GB | `llama.cpp` `b11871` (CUDA 12.4) | VRAM + 시스템 RAM 분할 오프로딩 |
| 3-2 | `Qwen 3.8 27B` (`Unsloth UD-IQ3_XXS`) | 27B Dense (66레이어) | 10.93 GB | `llama.cpp` `b11871` (CUDA 12.4) | VRAM 대부분 + 일부 레이어 RAM 분할 |
| 3-3 | `Qwen 3.8 27B` (`Unsloth UD-IQ3_XXS` + MTP) | 27B Dense (66레이어) | 10.93 GB | `llama.cpp` `b11871` (`draft-mtp`) | VRAM 대부분 + 일부 레이어 RAM 분할 |
| 3-4 | `Qwen 3.8 27B` (`ISTA-DASLab IQ2_XS-mtp` + MTP) | 27B Dense (66레이어) | 8.77 GB | `llama.cpp` `b11871` (`draft-mtp`) | 66개 레이어 모두 12GB VRAM 상주 |

사과 계산과 양자 역학 설명은 모든 모델에 같은 한국어 프롬프트를 입력했고, 비동기 작업 큐 코딩은 2라운드와 3라운드에서 추가했다. 첫 과제는 <strong>사과 계산(`apples`)</strong>이다. 사과가 3개 있을 때 2개를 더 받고 1개를 먹으면 몇 개가 남는지 계산식과 함께 짧게 답하도록 했고, 추론은 끈 채 `reasoning_effort=none`, `temperature=0`, `max_tokens=64`로 설정했다. 두 번째 과제는 <strong>양자 역학 설명(`quantum`)</strong>으로, 기본 추론을 유지하고 `max_tokens=2048`로 지정한 뒤 `"양자 역학에 대해서 간단히 설명해줘."`라고 물었다. 세 번째 <strong>비동기 작업 큐 코딩(`asyncio`)</strong>에서는 `asyncio.Queue`를 사용하는 생산자-소비자 패턴 예제와 한국어 해설을 요청한 뒤, 생성된 코드를 Python 3.12로 실행해 정상 종료(`exit 0`) 여부를 확인했다.

![높은 서랍장에서 길게 이어진 종이 띠가 좁은 하늘색 깔때기를 통과하는 동안 책상 위 모래시계를 바라보는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-deepseek-qwen38-27b/02-deepseek-streaming.png)

## 1라운드: 12GB VRAM PC에서 240GB짜리 763B 모델 실행하기

첫 번째 실험 대상은 763B 파라미터 규모의 `DeepSeek V4.1 Flash 1017`을 1.75비트로 양자화한 `IST-DAS-1.75bpw`(`IQ1_M`)다. 단일 모델의 디스크 점유량만 240.32GB에 달한다. 본체 가중치 샤드 4개가 120.72GB를 차지하고, 4비트(`IQ4_NL`)로 양자화된 Engram 조회 테이블이 110.60GB, 추측 디코딩(Speculative Decoding)용 DSpark 드래프터가 7.98GB다. 시스템 RAM과 VRAM을 합쳐도 모델 파일 크기의 5분의 1보다 적지만, Strata `0.1.49.2`는 약 4.5GB의 공유 Dense 가중치를 VRAM에 상주시키고 나머지 전문가 가중치와 Engram 테이블은 필요할 때마다 NVMe SSD에서 읽는다.

| 측정 항목 | 사과 계산 (`apples`) | 양자 역학 설명 (`quantum`) |
|---|---|---|
| 기동 및 웜업 시간 | `/health` 27.33초 / 웜업 완료 41.38초 | (동일 서버 세션 유지) |
| 프롬프트 평가 | 60토큰 (`6.80 tok/s`, 8,859.4ms) | 45토큰 (`6.80 tok/s`, 6,660.3ms) |
| 생성 토큰 수 | 12토큰 (추론 비활성화) | 725토큰 (추론 296 + 본문 427) |
| 토큰 생성 속도 | `2.40 tok/s` (`416.98 ms/tok`) | `2.70 tok/s` (`368.45 ms/tok`) |
| 총 소요 시간 (Wall Time) | **13.91초** | **273.81초 (4분 33.8초)** |
| 피크 메모리 점유 | VRAM `11,807 MiB` / 여유 RAM 최저 `7.57 MiB` | VRAM `11,807 MiB` / 시스템 RAM `31.738 GiB` |

12GB VRAM 데스크톱에서 763B 모델이 오류 없이 실행됐고, 두 질문에 모두 한국어로 답했다. 사과 계산에서는 `"3 + 2 - 1 = 4개"`를 출력했고, 양자 역학 설명에서도 파동-입자 이중성, 불확정성 원리, 양자 중첩과 얽힘을 체계적으로 정리했다.[^deepseek-asyncio]

[^deepseek-asyncio]: 1라운드에서는 32GB RAM으로 240GB 모델을 실행할 수 있는지와 기본 생성 속도를 확인하기 위해 `apples`와 `quantum` 두 프롬프트를 측정했다. `asyncio` 코딩 과제는 2라운드와 3라운드 비교에서 추가했다.

생성 속도는 초당 2.40에서 2.70토큰이었으며, 실행 로그에서는 드래프터 생략과 반복적인 SSD 읽기가 확인됐다. Strata의 `--dspark auto` 설정은 라우팅 전문가 가중치(115GB)가 시스템 유효 메모리의 1.5배를 초과하면 메모리 고갈을 막기 위해 7.98GB짜리 DSpark 드래프터 로드를 자동으로 생략한다. 로그에 기록된 `draft_n: 0`은 드래프터 없이 한 번에 한 토큰씩 생성했다는 뜻이다. 여기에 Windows의 가용 RAM이 최저 `7,933,952 bytes`(7.57MiB)까지 줄어들며 페이지 캐시에 쓸 메모리도 부족해져, 토큰을 생성할 때마다 NVMe SSD를 읽어야 했다.

## 2라운드: Strata 카탈로그 대조와 Qwen 3.8 Flash Next 180B

그렇다면 Strata 제작진은 RAM 32GB와 VRAM 12GB를 갖춘 PC에 어떤 모델을 권장할까. Strata `v0.2.5`의 `setup.py`에는 모델 계열 8개와 양자화 등급 25개가 등록돼 있으며, 모델 선택에 사용할 메모리 용량은 `시스템 RAM + GPU VRAM - 5GiB` 공식으로 계산한다. 이 PC의 수치를 넣으면 `31.75 + 12.0 - 5.0 = 38.75GiB`다.

| 패밀리 | 대표 등급 | 디스크 크기 | 권장 시스템 RAM | 32GB RAM + 12GB VRAM 적합도 |
|---|---|---|---|---|
| `deepseek41` | `1.75bpw` (763B MoE) | 239.3 GB | 34 GB 이상 | 실행 가능하나 드래프터 생략, `2.7 tok/s` |
| `qwen` | `Qwen 3.8 Flash Next` (`Q2_0` \~ `IQ3_S`) | 66.4 \~ 83.6 GB | 48 \~ 62 GB | 권장 사양 미달 (SSD 스트리밍 병목) |
| `swift` | `Swift IQ2_XS` (180B 프루닝 MoE) | 68.2 GB | 48 GB | 이 PC의 카탈로그 계산식 추천 대상 |
| `coder` / `gyro` | `Coder IQ1_M` / `Gyro-S` | 58.4 \~ 58.5 GB | 32 GB (합산 27.6GiB) | 32GB 시스템용 경량 MoE 등급 |
| `qwen36` | `Qwen3.6-35B-A3B` (`UD-Q4_K_XL`) | 22.9 GB | 32 GB | 32GB RAM에 전체 상주 가능 |

다음으로 Strata `0.1.50`에서 180B MoE 모델 `Qwen 3.8 Flash Next`를 실행했다. 이미 내려받은 `GSQ-RCO-IQ3_S` 양자화 모델을 사용했으며, 파일 크기는 78.10GiB, 카탈로그 권장 RAM은 62GB다. 이 모델은 180B MoE 본체와 51.2B 규모의 계층별 임베딩(PLE)으로 구성된다. 이번 실행에서는 Strata 내장 MTP를 켜고 `spec=4`, `--resident-budget-gib 8`, `--vram-reserve-mib 1024`, int8 KV 캐시를 적용했다.

| 프롬프트 | 프롬프트 속도 | 생성 토큰 (추론/답변) | 토큰 생성 속도 | MTP 수락률 | 총 소요 시간 | 비고 |
|---|---|---|---|---|---|---|
| `apples` | `10.80 tok/s` | 15 (0 / 15) | `7.90 tok/s` | `15/17` (88.2%) | **7.66초** | 정확한 수식 출력 |
| `quantum` | `10.90 tok/s` | 340 (0 / 340) | `13.10 tok/s` | `159/255` (62.4%) | **31.86초** | 763B 모델의 약 11.6% 시간으로 완료 |
| `asyncio` | `23.70 tok/s` | 418 (0 / 418) | `5.20 tok/s` | `246/349` (70.5%) | **84.94초** | 생성 코드 15초 타임아웃 발생 |

MTP 수락률은 62.4%에서 88.2%였고, `quantum` 응답에는 31.86초(초당 13.10토큰)가 걸렸다. 권장 RAM은 62GB였지만 실험 PC의 RAM은 32GB여서 SSD 읽기가 빈번했다. 시스템 RAM에 상주한 전문가 가중치는 5.82GiB였고, 세 질문을 처리하는 동안 SSD에서 읽은 전문가 가중치는 총 `233,364.9MB`(약 233.4GB)였다. 실행 도중 VRAM 여유 공간이 289MiB까지 줄자 런타임이 경고를 출력했다. `asyncio` 코드에도 오류가 있었다. 소비자 태스크는 2개(`소비자1`, `소비자2`)를 만들었는데 종료 신호인 `await queue.put(None)`은 한 번만 호출해, 두 번째 소비자가 계속 대기하다 15초 제한 시간 초과로 종료됐다.

![두 테이블 사이 좁은 다리에서 수레들이 정체된 왼쪽 경로와 하나의 트레이 안에 하늘색 블록 여섯 개가 정돈된 오른쪽 구성을 비교하는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-deepseek-qwen38-27b/03-partial-offload-vs-vram.png)

## 3라운드: Qwen 3.8 27B의 네 가지 실행 구성 비교

이번에는 27B Dense 모델 `Qwen 3.8 27B`를 선택했다. 모델 전체를 메모리에 적재하면 SSD 스트리밍보다 얼마나 빠를까. `Qwen 3.8 27B`는 66개 레이어로 구성된 Dense 모델이라 Strata 카탈로그 대상과 구조가 다르며, Windows CUDA용 `llama.cpp`(`b11871`, CUDA 12.4)로 실행했다. 컨텍스트는 8192로 설정하고 Flash Attention과 `q8_0` KV 캐시를 사용했다.[^qwen27b-models]

[^qwen27b-models]: 3라운드 비교에는 `unsloth/Qwen3.8-27B-GGUF`의 `UD-Q4_K_M`(16.46GB)과 `UD-IQ3_XXS`(10.93GB), 그리고 `ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-IQ2_XS-mtp-GGUF`(8.77GB)를 사용했다. Unsloth GGUF에도 MTP 가중치 텐서가 포함돼 있어 `--spec-type draft-mtp` 옵션으로 MTP를 켰을 때와 껐을 때를 비교했다.

이번 실험에서는 **12GB VRAM에 66개 레이어를 모두 적재할 수 있는지** 확인했다. Windows 11 데스크톱 환경에서는 운영체제 합성기와 백그라운드 앱이 기본으로 1.5GB에서 2.1GB의 VRAM을 점유한다. 이 환경에서 로컬 LLM에 사용할 수 있는 VRAM은 약 10GB였다.

| 구성 (Qwen 3.8 27B) | 파일 크기 | 기동+웜업 | `apples` (시간 / 속도) | `quantum` (시간 / 속도) | `asyncio` (시간 / 속도 / 코드 검증) | 피크 VRAM / 최저 여유 RAM |
|---|---|---|---|---|---|---|
| `UD-Q4_K_M` (단독) | 16.46 GB | 15.88초 | 4.21초 / `6.34 tok/s` | 62.98초 / `6.26 tok/s` | 249.23초 / `6.11 tok/s` / `exit 0` | `11,927 MiB` / `0.26 GiB` |
| `UD-IQ3_XXS` (단독) | 10.93 GB | 14.67초 | 2.60초 / `9.48 tok/s` | 29.10초 / `12.15 tok/s` | 132.09초 / `14.47 tok/s` / `exit 0` | `11,947 MiB` / `3.14 GiB` |
| `UD-IQ3_XXS` + MTP | 10.93 GB | 14.29초 | 1.87초 / `16.99 tok/s` | 38.84초 / `9.89 tok/s` | 94.95초 / `10.28 tok/s` / `exit 0` | `11,932 MiB` / `3.79 GiB` |
| **`IQ2_XS-mtp` + MTP** | **8.77 GB** | **7.86초** | **0.97초 / `38.87 tok/s`** | **11.50초 / `29.88 tok/s`** | **38.56초 / `27.73 tok/s` / `exit 0`** | **`11,538 MiB` / `8.16 GiB`** |

16.46GB인 `UD-Q4_K_M`은 일부 레이어를 시스템 RAM에 적재했다. 생성 속도는 초당 6.11에서 6.34토큰이었고, 추론을 포함해 1,512토큰이 출력된 `asyncio` 응답에는 249.23초가 걸렸다. 가용 시스템 RAM도 최저 0.26GiB까지 줄었다. 10.93GB인 `UD-IQ3_XXS`는 프롬프트 평가 속도가 초당 143에서 201토큰이었고, `quantum`과 `asyncio`의 생성 속도는 각각 초당 12.15토큰과 14.47토큰이었다. Windows가 사용하는 VRAM 때문에 일부 레이어는 시스템 RAM에 적재됐으며, 최대 VRAM 점유량은 11,947MiB였다.

ISTA-DASLab의 `GSQ-RCO-IQ2_XS-mtp`는 파일 크기가 8.77GB(8.17GiB)다. 66개 레이어를 모두 VRAM에 적재했으며, 가중치가 점유한 VRAM은 8,089MiB였다. 기동과 웜업에는 총 7.86초가 걸렸다. 응답 시간은 `apples` <strong>0.97초(`38.87 tok/s`)</strong>, `quantum` <strong>11.50초(`29.88 tok/s`)</strong>, `asyncio` <strong>38.56초(`27.73 tok/s`)</strong>였다. `quantum` 응답 시간은 DeepSeek의 273.81초에서 11.50초로 줄어 약 23.8분의 1이 됐고, 생성 속도는 초당 2.70토큰에서 29.88토큰으로 약 11.1배가 됐다. 2비트대 양자화 모델이 생성한 `asyncio` 코드는 소비자 수에 맞게 종료 신호(`None`)를 전송하고 각 작업 처리가 끝나면 `queue.task_done()`을 호출해 Python 실행 검증을 통과했다.

![책상 앞에서 초시계를 들고 미소 짓는 치비 서소영과 둥근 하늘색 고리를 연속으로 통과하는 종이비행기 세 대](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-deepseek-qwen38-27b/04-sweet-spot-mtp.png)

## 가장 흥미로운 지점

**`UD-IQ3_XXS`는 일부 레이어를 시스템 RAM에 적재한 구성에서 MTP 적용 뒤 장문 생성 속도가 느려졌다.** 흔히 추측 디코딩이나 MTP를 켜면 어떤 환경에서든 생성 속도가 빨라질 것이라 기대한다. 실제로 15토큰만 생성한 단문 과제(`apples`)에서는 MTP가 빨랐다. `UD-IQ3_XXS`의 생성 속도는 초당 9.48토큰에서 16.99토큰으로 향상됐고, 드래프트 수락률은 100%(`15/15`)였다.

그러나 장문 과제 두 개에서는 MTP를 켜자 생성 속도가 느려졌다. `quantum`은 초당 12.15토큰에서 9.89토큰으로, `asyncio`는 초당 14.47토큰에서 10.28토큰으로 감소했다.[^mtp-walltime] MTP는 매 스텝마다 여러 후보 토큰을 한꺼번에 검증하므로 단일 토큰 디코딩보다 스텝당 연산량이 많다. 일부 레이어를 시스템 RAM에 적재한 구성에서는 MTP를 켰을 때 장문 토큰당 생성 시간이 69.10에서 82.30ms였던 것이 97.28에서 101.11ms로 증가했다.

[^mtp-walltime]: `UD-IQ3_XXS`의 `asyncio` 응답 시간은 MTP를 켜자 132.09초에서 94.95초로 줄었다. 이 실행에서는 내부 추론이 1,535토큰에서 599토큰으로 감소해 전체 출력도 1,904토큰에서 966토큰으로 약 절반이 됐다. 생성 속도가 느려졌어도 출력 분량이 줄어 응답은 더 일찍 끝났다.

| 비교 항목 (`Qwen 3.8 27B`) | `UD-IQ3_XXS` 단독 | `UD-IQ3_XXS` + MTP | `IQ2_XS-mtp` + MTP |
|---|---|---|---|
| 가중치 상주 상태 | VRAM + 일부 RAM 분할 | VRAM + 일부 RAM 분할 | **66개 레이어 모두 VRAM 상주** |
| `apples` 속도 (드래프트 수락률) | `9.48 tok/s` (해당 없음) | `16.99 tok/s` (`100.0%`) | **`38.87 tok/s` (`83.3%`)** |
| `quantum` 속도 (드래프트 수락률) | `12.15 tok/s` (해당 없음) | `9.89 tok/s` (`46.4%`) | **`29.88 tok/s` (`48.0%`)** |
| `asyncio` 속도 (드래프트 수락률) | `14.47 tok/s` (해당 없음) | `10.28 tok/s` (`54.9%`) | **`27.73 tok/s` (`49.8%`)** |
| 장문 토큰당 생성 지연 (`ms/tok`) | `69.10–82.30 ms` | `97.28–101.11 ms` | **`33.47–36.06 ms`** |

8.77GB인 `IQ2_XS-mtp`는 `UD-IQ3_XXS`보다 약 2.1GB 작아 66개 레이어를 모두 VRAM에 적재할 수 있었다. MTP를 켠 이 구성의 장문 생성 속도는 초당 27.73에서 29.88토큰이었다. 드래프트 수락률은 `quantum` 48.0%, `asyncio` 49.8%로 앞 구성과 비슷했지만, 토큰당 생성 시간은 33.5에서 36.1ms로 훨씬 짧았다. 시스템 RAM 점유량은 최대 23.59GiB였고, 실행 내내 여유 RAM은 8.16GiB 이상이었다.

이번 PC에서는 파라미터가 가장 많은 모델보다 모든 레이어를 VRAM에 적재한 모델이 훨씬 빨리 응답했다. Strata의 SSD 스트리밍 덕분에 12GB VRAM PC에서도 763B와 180B 모델을 실행해 사과 계산과 양자 역학 설명을 받아 볼 수 있었다. 이 PC에서 빠른 질의응답과 코딩 보조에 쓸 구성을 고른다면 `Qwen 3.8 27B IQ2_XS-mtp`와 MTP를 선택하겠다. 세 과제의 응답 시간이 가장 짧았고, 생성 코드는 정상 종료했으며, 실행 내내 시스템 여유 RAM도 8.16GiB 이상 유지됐다.

## 출처

- [Strata 런타임 릴리스 및 카탈로그 (`Subramaniyam/strata`)](https://github.com/Subramaniyam/strata)
- [ISTA-DASLab Qwen3.8-27B-GSQ-RCO-IQ2_XS-mtp-GGUF (Hugging Face)](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-IQ2_XS-mtp-GGUF)
- [Unsloth Qwen3.8-27B-GGUF (`UD-Q4_K_M`, `UD-IQ3_XXS`) (Hugging Face)](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)
- [SC117 Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF (Hugging Face)](https://huggingface.co/SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF)
- [llama.cpp Windows CUDA 릴리스 (`ggml-org/llama.cpp`)](https://github.com/ggml-org/llama.cpp)
- 치비 서소영 삽화 4장은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 `gpt-image-2.5-flare`로 따로 생성했다.
