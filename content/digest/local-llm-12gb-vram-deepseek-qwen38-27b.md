---
title: "12GB VRAM 게이밍 PC의 로컬 LLM 실측: DeepSeek V4.1 Flash 763B와 Qwen 3.8 27B"
date: 2026-10-25T19:30:00+09:00
draft: false
description: "i9-12900K, 32GB RAM, RTX 3080 Ti(12GB VRAM)를 장착한 PC에서 DeepSeek V4.1 Flash 763B, Qwen 3.8 Flash Next 180B, 그리고 Qwen 3.8 27B 다섯 구성을 실행해 속도와 실제 응답 원문을 비교했다. 양자 역학 설명에 걸린 시간은 763B 모델이 273.81초, 66개 레이어를 모두 VRAM에 적재한 8.77GB 모델이 Windows에서 11.50초, WSL2 ext4에서 7.76초였다."
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

<style>
.llm-viz {
  margin: 1.75rem 0;
  padding: 1.2rem 1.3rem;
  border-radius: 12px;
  background: var(--entry);
  border: 1px solid var(--border);
  box-sizing: border-box;
  width: 100%;
  max-width: 100%;
}
.llm-viz-title {
  font-size: 0.96rem;
  font-weight: 700;
  color: var(--primary);
  margin: 0 0 0.85rem 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.45rem;
}
.llm-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  font-size: 0.75rem;
  color: var(--secondary);
  margin-bottom: 0.85rem;
}
.llm-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}
.llm-dot {
  width: 10px;
  height: 10px;
  border-radius: 3px;
  display: inline-block;
  flex-shrink: 0;
}
.llm-dot-vram { background: #0284c7; }
.llm-dot-ram { background: #d97706; }
.llm-dot-ssd { background: #e11d48; }
.llm-dot-wsl { background: #059669; }
.llm-dot-free { background: rgba(2, 132, 199, 0.16); border: 1px dashed #0284c7; }
html[data-theme="dark"] .llm-dot-vram { background: #38bdf8; }
html[data-theme="dark"] .llm-dot-ram { background: #fbbf24; }
html[data-theme="dark"] .llm-dot-ssd { background: #fb7185; }
html[data-theme="dark"] .llm-dot-wsl { background: #34d399; }
html[data-theme="dark"] .llm-dot-free { background: rgba(56, 189, 248, 0.18); border-color: #38bdf8; }

.llm-tier-list {
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}
.llm-tier-card {
  padding: 0.75rem 0.9rem;
  border-radius: 9px;
  background: var(--theme);
  border: 1px solid var(--border);
}
.llm-tier-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 0.4rem;
}
.llm-tier-name {
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--primary);
}
.llm-tier-meta {
  font-size: 0.75rem;
  color: var(--secondary);
  font-family: monospace;
}
.llm-stack-bar {
  display: flex;
  height: 24px;
  border-radius: 6px;
  overflow: hidden;
  background: var(--entry);
  border: 1px solid var(--border);
  font-size: 0.72rem;
  font-weight: 600;
  line-height: 24px;
  text-align: center;
}
.llm-seg-vram, .llm-seg-ram, .llm-seg-ssd, .llm-seg-free {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 0 6px;
}
.llm-seg-vram { background: #0284c7; color: #ffffff; }
.llm-seg-ram { background: #d97706; color: #ffffff; }
.llm-seg-ssd { background: #e11d48; color: #ffffff; }
.llm-seg-free { background: rgba(2, 132, 199, 0.12); color: var(--primary); }
html[data-theme="dark"] .llm-seg-vram { background: #0369a1; color: #f0f9ff; }
html[data-theme="dark"] .llm-seg-ram { background: #b45309; color: #fffbeb; }
html[data-theme="dark"] .llm-seg-ssd { background: #be123c; color: #fff1f2; }
html[data-theme="dark"] .llm-seg-free { background: rgba(56, 189, 248, 0.15); color: #e0f2fe; }

.llm-bar-group {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}
.llm-bar-row {
  display: flex;
  flex-direction: column;
  gap: 0.28rem;
}
.llm-bar-label-line {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.llm-bar-model {
  font-size: 0.84rem;
  font-weight: 600;
  color: var(--primary);
}
.llm-bar-stats {
  font-size: 0.76rem;
  font-family: monospace;
  color: var(--secondary);
}
.llm-bar-stats strong {
  color: var(--primary);
}
.llm-bar-track {
  width: 100%;
  height: 20px;
  background: var(--theme);
  border: 1px solid var(--border);
  border-radius: 6px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
}
.llm-bar-fill {
  height: 100%;
  border-radius: 4px 0 0 4px;
  min-width: 6px;
}
.llm-fill-ssd { background: linear-gradient(90deg, #e11d48, #fb7185); }
.llm-fill-ram { background: linear-gradient(90deg, #d97706, #fbbf24); }
.llm-fill-vram { background: linear-gradient(90deg, #0284c7, #38bdf8); }
.llm-fill-wsl { background: linear-gradient(90deg, #059669, #34d399); }

.llm-dual-bars {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
}
.llm-dual-cell {
  display: flex;
  flex-direction: column;
  gap: 0.18rem;
}
.llm-dual-caption {
  display: flex;
  justify-content: space-between;
  font-size: 0.72rem;
  font-family: monospace;
  color: var(--secondary);
}
.llm-dual-caption strong {
  color: var(--primary);
}

.llm-badge {
  display: inline-block;
  font-size: 0.69rem;
  font-weight: 600;
  padding: 0.08rem 0.42rem;
  border-radius: 4px;
  line-height: 1.4;
  vertical-align: middle;
}
.llm-badge-ok { background: rgba(5, 150, 105, 0.14); color: #047857; }
.llm-badge-warn { background: rgba(217, 119, 6, 0.15); color: #b45309; }
.llm-badge-err { background: rgba(225, 29, 72, 0.14); color: #be123c; }
.llm-badge-info { background: rgba(2, 132, 199, 0.14); color: #0369a1; }
html[data-theme="dark"] .llm-badge-ok { background: rgba(52, 211, 153, 0.18); color: #6ee7b7; }
html[data-theme="dark"] .llm-badge-warn { background: rgba(251, 191, 36, 0.18); color: #fcd34d; }
html[data-theme="dark"] .llm-badge-err { background: rgba(251, 113, 133, 0.18); color: #fda4af; }
html[data-theme="dark"] .llm-badge-info { background: rgba(56, 189, 248, 0.18); color: #7dd3fc; }

.llm-metric-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.7rem;
}
.llm-metric-box {
  background: var(--theme);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
}
.llm-metric-box-title {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--secondary);
  margin-bottom: 0.3rem;
}
.llm-metric-val {
  font-size: 1.12rem;
  font-weight: 800;
  color: var(--primary);
  font-family: monospace;
}
.llm-metric-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  margin-top: 0.45rem;
}
.llm-chip {
  font-size: 0.71rem;
  font-family: monospace;
  padding: 0.12rem 0.4rem;
  border-radius: 4px;
  background: var(--entry);
  border: 1px solid var(--border);
  color: var(--secondary);
}
.llm-chip strong {
  color: var(--primary);
}

.llm-resp-grid {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  margin: 1.5rem 0;
}
.llm-resp-card {
  border: 1px solid var(--border);
  border-radius: 10px;
  background: var(--entry);
  overflow: hidden;
}
.llm-resp-card.llm-resp-highlight {
  border-color: #0284c7;
  box-shadow: 0 0 0 1px rgba(2, 132, 199, 0.22);
}
html[data-theme="dark"] .llm-resp-card.llm-resp-highlight {
  border-color: #38bdf8;
  box-shadow: 0 0 0 1px rgba(56, 189, 248, 0.22);
}
.llm-resp-header {
  padding: 0.7rem 0.95rem;
  background: var(--theme);
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.45rem;
}
details.llm-resp-card > summary.llm-resp-header {
  cursor: pointer;
  list-style: none;
  border-bottom: none;
}
details.llm-resp-card[open] > summary.llm-resp-header {
  border-bottom: 1px solid var(--border);
}
details.llm-resp-card > summary.llm-resp-header::-webkit-details-marker {
  display: none;
}
.llm-fold-hint {
  font-size: 0.71rem;
  color: var(--secondary);
  font-weight: 600;
}
details.llm-resp-card[open] .llm-fold-hint::after {
  content: "접기 ▲";
}
details.llm-resp-card:not([open]) .llm-fold-hint::after {
  content: "원문 펼치기 ▼";
}
.llm-resp-title {
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--primary);
}
.llm-resp-meta {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  flex-wrap: wrap;
  font-size: 0.74rem;
  font-family: monospace;
  color: var(--secondary);
}
.llm-resp-body {
  padding: 0.85rem 1rem;
  font-size: 0.85rem;
  line-height: 1.62;
  color: var(--content);
  white-space: pre-wrap;
  word-break: keep-all;
  overflow-wrap: anywhere;
  font-family: inherit;
  margin: 0;
}
.llm-quirk {
  background: rgba(225, 29, 72, 0.16);
  color: inherit;
  padding: 0.04rem 0.28rem;
  border-radius: 4px;
  border-bottom: 2px solid #e11d48;
  font-weight: 700;
}
html[data-theme="dark"] .llm-quirk {
  background: rgba(251, 113, 133, 0.22);
  border-bottom-color: #fb7185;
}
.llm-mtp-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.7rem;
}
.llm-mtp-bar-wrap {
  margin: 0.45rem 0 0.35rem 0;
}
@media (max-width: 640px) {
  .llm-viz { padding: 0.95rem 0.85rem; }
  .llm-metric-grid { grid-template-columns: 1fr; }
  .llm-mtp-grid { grid-template-columns: 1fr; }
  .llm-dual-bars { grid-template-columns: 1fr; gap: 0.3rem; }
  .llm-resp-header { padding: 0.65rem 0.8rem; }
  .llm-resp-body { padding: 0.75rem 0.8rem; font-size: 0.82rem; }
}
</style>

## 3줄 요약

- 12GB VRAM, 32GB RAM, 4TB NVMe SSD를 장착한 게이밍 PC에서 파일 크기 8.77GB부터 240.32GB까지 일곱 가지 로컬 LLM 실행 구성을 실측하고 실제 양자 역학 설명 응답 원문을 비교했다.
- Strata로 실행한 763B 모델(273.81초, `2.70 tok/s`)은 원문에 `양자 entanglement`, `microscopic 세계` 같은 한영 혼용이 나타났고, 180B 모델(31.86초, `13.10 tok/s`)은 `連續` 같은 한자 토큰이 섞여 나왔다.
- 66개 레이어를 모두 12GB VRAM에 적재한 8.77GB `Qwen 3.8 27B IQ2_XS`에 다중 토큰 예측(MTP)을 켜자 한자나 영단어 혼입 없는 한국어 답변을 Windows에서 11.50초(`29.88 tok/s`), WSL2 ext4에서 7.76초(`40.02 tok/s`) 만에 마쳤다.

## 실험 환경과 세 가지 질문

VRAM 12GB와 시스템 RAM 32GB를 갖춘 PC에서 실행할 수 있는 로컬 LLM은 어느 정도 규모일까. 7B나 8B 소형 모델은 여유 있게 돌아가지만, 규모가 큰 모델은 양자화 방식과 가중치가 놓이는 메모리 계층에 따라 속도와 응답 품질이 크게 달라진다. 최근 공개된 Strata 런타임은 실행에 필요한 전문가 가중치를 NVMe SSD에서 실시간으로 읽는다. 일반 게이밍 PC에서도 초대형 모델을 실용적으로 실행할 수 있는지 이번 실측으로 확인했다.

테스트 PC의 CPU는 Intel Core i9-12900K(16코어 24스레드), 시스템 메모리는 DDR5-4800 32GB(운영체제 인식 용량 31.75GiB)다. 그래픽카드는 NVIDIA GeForce RTX 3080 Ti(12,288MiB VRAM, 드라이버 610.88)를 썼고, 모델 가중치는 Samsung SSD 990 PRO 4TB NVMe(`D:\`)와 WSL2 Ubuntu 22.04(`ext4`)에 배치했다.[^wsl-cp949]

[^wsl-cp949]: Strata 실행은 WSL2의 기본 메모리 상한(15.5GB)과 `/mnt/d` 9P 파일시스템 마운트를 거치며 발생하는 SSD 읽기 속도 저하를 피하기 위해 Windows 네이티브(`D:\llm`)에서 진행했다. 이 과정에서 Strata의 C++ 실행 파일(`ds4_main.cpp`)이 한글이 포함된 Windows 사용자 폴더 경로를 CP949로 출력할 때 이를 UTF-8로 읽는 Python 래퍼(`serve/server.py`)가 중단되는 현상도 발견해, 슬롯 디렉토리를 영문 경로인 `STRATA_DS4_SLOT_DIR=D:\llm\ds4-slots`로 지정하여 해결했다. 반면 8.77GB 가중치 전체가 12GB VRAM에 들어가는 `Qwen 3.8 27B IQ2_XS-mtp`는 WSL2 `ext4` 파일시스템에서 `--load-mode dio`(Direct I/O)와 CUDA 12.8로 구동했을 때 Windows 네이티브보다 더 빨랐다.

<div class="llm-viz" role="region" aria-label="메모리 계층별 모델 가중치 배치 다이어그램">
  <div class="llm-viz-title">
    <span>메모리 계층별 가중치 배치 구조</span>
    <span class="llm-badge llm-badge-info">12GB VRAM / 32GB RAM / 4TB NVMe SSD</span>
  </div>
  <div class="llm-legend">
    <span class="llm-legend-item"><span class="llm-dot llm-dot-vram"></span>GPU VRAM (12GB)</span>
    <span class="llm-legend-item"><span class="llm-dot llm-dot-ram"></span>시스템 RAM (32GB, PCIe 경유)</span>
    <span class="llm-legend-item"><span class="llm-dot llm-dot-ssd"></span>NVMe SSD 스트리밍 (4TB)</span>
  </div>
  <div class="llm-tier-list">
    <div class="llm-tier-card">
      <div class="llm-tier-head">
        <span class="llm-tier-name">1. NVMe SSD 실시간 스트리밍 (초대형 MoE)</span>
        <span class="llm-tier-meta">DeepSeek 763B (240.3GB) / Qwen Flash Next 180B (78.1GiB)</span>
      </div>
      <div class="llm-stack-bar">
        <div class="llm-seg-vram" style="width: 15%;">VRAM 4.5GB</div>
        <div class="llm-seg-ram" style="width: 25%;">RAM 캐시 5.8~27GB</div>
        <div class="llm-seg-ssd" style="width: 60%;">전문가 가중치 + Engram/PLE SSD 스트리밍</div>
      </div>
    </div>
    <div class="llm-tier-card">
      <div class="llm-tier-head">
        <span class="llm-tier-name">2. VRAM + 시스템 RAM 분할 오프로딩 (27B 중형 양자화)</span>
        <span class="llm-tier-meta">Unsloth Qwen 3.8 27B UD-Q4_K_M (16.5GB) / UD-IQ3_XXS (10.9GB)</span>
      </div>
      <div class="llm-stack-bar">
        <div class="llm-seg-vram" style="width: 58%;">가용 VRAM (~10GB) 적재</div>
        <div class="llm-seg-ram" style="width: 42%;">초과 레이어 시스템 RAM 분할</div>
      </div>
    </div>
    <div class="llm-tier-card">
      <div class="llm-tier-head">
        <span class="llm-tier-name">3. 12GB VRAM 100% 상주 (27B 경량 양자화 + MTP)</span>
        <span class="llm-tier-meta">ISTA-DASLab Qwen 3.8 27B GSQ-RCO IQ2_XS-mtp (8.77GB)</span>
      </div>
      <div class="llm-stack-bar">
        <div class="llm-seg-vram" style="width: 80%;">66/66 레이어 전부 VRAM 상주 (8,089MiB)</div>
        <div class="llm-seg-free" style="width: 20%;">RAM 8.2GiB+ 여유</div>
      </div>
    </div>
  </div>
</div>

사과 계산과 양자 역학 설명은 모든 모델에 같은 한국어 프롬프트를 입력했고, 비동기 작업 큐 코딩은 Qwen 계열 다섯 구성에서 비교했다. 첫 과제는 <strong>사과 계산(`apples`)</strong>이다. 사과가 3개 있을 때 2개를 더 받고 1개를 먹으면 몇 개가 남는지 계산식과 함께 짧게 답하도록 했고, 추론은 끈 채 `reasoning_effort=none`, `temperature=0`, `max_tokens=64`로 설정했다. 두 번째 과제는 <strong>양자 역학 설명(`quantum`)</strong>으로, 기본 추론을 유지하고 `max_tokens=2048`로 지정한 뒤 `"양자 역학에 대해서 간단히 설명해줘."`라고 물었다. 세 번째 <strong>비동기 작업 큐 코딩(`asyncio`)</strong>에서는 `asyncio.Queue`를 사용하는 생산자-소비자 패턴 예제와 한국어 해설을 요청한 뒤, 생성된 코드를 Python 3.12로 실행해 정상 종료(`exit 0`) 여부를 확인했다.

![높은 서랍장에서 길게 이어진 종이 띠가 좁은 하늘색 깔때기를 통과하는 동안 책상 위 모래시계를 바라보는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-deepseek-qwen38-27b/02-deepseek-streaming.png)

## 1라운드와 2라운드: 240GB DeepSeek 763B와 78GiB Flash Next 180B 스트리밍

첫 번째 실험 대상은 763B 파라미터 규모의 `DeepSeek V4.1 Flash 1017`을 1.75비트로 양자화한 `IST-DAS-1.75bpw`(`IQ1_M`)다. 단일 모델의 디스크 점유량만 240.32GB에 달한다. 본체 가중치 샤드 4개가 120.72GB를 차지하고, 4비트(`IQ4_NL`)로 양자화된 Engram 조회 테이블이 110.60GB, 추측 디코딩(Speculative Decoding)용 DSpark 드래프터가 7.98GB다. 시스템 RAM과 VRAM을 합쳐도 모델 파일 크기의 5분의 1보다 적지만, Strata `0.1.49.2`는 약 4.5GB의 공유 Dense 가중치를 VRAM에 상주시키고 나머지 전문가 가중치와 Engram 테이블은 필요할 때마다 NVMe SSD에서 읽는다.[^deepseek-asyncio]

[^deepseek-asyncio]: 1라운드에서는 32GB RAM으로 240GB 모델을 실행할 수 있는지와 기본 생성 속도를 확인하기 위해 `apples`와 `quantum` 두 프롬프트를 측정했다. `asyncio` 코딩 과제는 2라운드와 3라운드 비교에서 추가했다.

이어서 2라운드에서는 Strata `v0.2.5`의 설정 스크립트(`setup.py`)에 등록된 8개 모델 계열, 25개 양자화 등급의 메모리 기준을 대조한 뒤, 디스크에 받아 둔 180B MoE 모델 `Qwen 3.8 Flash Next`(`GSQ-RCO-IQ3_S`, 78.10GiB, 51.2B PLE 결합)를 Strata `0.1.50`과 내장 MTP(`spec=4`)로 실행했다. Strata는 `시스템 RAM + GPU VRAM - 5GiB` 공식으로 장비별 메모리 용량을 계산하며, 이 PC는 `31.75 + 12.0 - 5.0 = 38.75GiB`다.

<div class="llm-viz" role="region" aria-label="Strata MoE 스트리밍 모델 두 종의 실측 지표 및 카탈로그 요구 메모리 비교">
  <div class="llm-viz-title">
    <span>1, 2라운드: 초대형 MoE 스트리밍 실측 및 카탈로그 요구 메모리</span>
    <span class="llm-badge llm-badge-warn">이 PC 유효 예산: 38.75 GiB</span>
  </div>
  <div class="llm-metric-grid">
    <div class="llm-metric-box">
      <div class="llm-metric-box-title">1라운드 / DeepSeek V4.1 Flash (763B, 240.32GB)</div>
      <div class="llm-metric-val">273.81초 <span style="font-size:0.82rem;font-weight:500;">(2.70 tok/s)</span></div>
      <div class="llm-metric-chips">
        <span class="llm-chip">사과 <strong>13.91초</strong> (2.40 tok/s)</span>
        <span class="llm-chip">기동+웜업 <strong>41.38초</strong></span>
        <span class="llm-chip">드래프터 <strong>자동 생략 (draft_n: 0)</strong></span>
        <span class="llm-chip">최소 여유 RAM <strong>7.57 MiB</strong></span>
      </div>
    </div>
    <div class="llm-metric-box">
      <div class="llm-metric-box-title">2라운드 / Qwen 3.8 Flash Next (180B, 78.10GiB)</div>
      <div class="llm-metric-val">31.86초 <span style="font-size:0.82rem;font-weight:500;">(13.10 tok/s)</span></div>
      <div class="llm-metric-chips">
        <span class="llm-chip">사과 <strong>7.66초</strong> (7.90 tok/s)</span>
        <span class="llm-chip">MTP 수락 <strong>62.4~88.2%</strong></span>
        <span class="llm-chip">누적 SSD 읽기 <strong>233.4 GB</strong></span>
        <span class="llm-chip">코딩 84.94초 <strong>(15초 타임아웃)</strong></span>
      </div>
    </div>
  </div>
  <div style="margin-top: 0.9rem; padding-top: 0.8rem; border-top: 1px solid var(--border);">
    <div style="font-size: 0.79rem; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem;">Strata v0.2.5 대표 등급별 권장 메모리 대비 이 PC 예산 (38.75 GiB)</div>
    <div class="llm-bar-group" style="gap: 0.55rem;">
      <div class="llm-bar-row">
        <div class="llm-bar-label-line">
          <span class="llm-bar-model">Qwen3.6-35B-A3B (22.9GB) / Coder IQ1_M (58.4GB)</span>
          <span class="llm-bar-stats">권장 <strong>32 GB</strong> <span class="llm-badge llm-badge-ok">예산 내</span></span>
        </div>
        <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-vram" style="width: 50%;"></div></div>
      </div>
      <div class="llm-bar-row">
        <div class="llm-bar-label-line">
          <span class="llm-bar-model">Swift IQ2_XS (180B 프루닝 MoE, 68.2GB)</span>
          <span class="llm-bar-stats">권장 <strong>48 GB</strong> <span class="llm-badge llm-badge-info">수식 추천 등급</span></span>
        </div>
        <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ram" style="width: 75%;"></div></div>
      </div>
      <div class="llm-bar-row">
        <div class="llm-bar-label-line">
          <span class="llm-bar-model">Qwen 3.8 Flash Next IQ3_S (180B MoE + PLE, 78.1GiB 실측)</span>
          <span class="llm-bar-stats">권장 <strong>62 GB</strong> <span class="llm-badge llm-badge-err">예산 초과 / SSD 병목</span></span>
        </div>
        <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ssd" style="width: 97%;"></div></div>
      </div>
    </div>
  </div>
</div>

12GB VRAM 데스크톱에서 763B 모델이 오류 없이 실행됐고, 사과 계산(`"3 + 2 - 1 = 4개"`)과 양자 역학 설명 모두 한국어로 답했다. 속도가 초당 2.40에서 2.70토큰에 그친 이유는 Strata의 `--dspark auto` 설정이 라우팅 전문가 가중치(115GB)가 시스템 유효 메모리의 1.5배를 초과할 때 메모리 고갈을 막으려고 7.98GB짜리 DSpark 드래프터 로드를 생략(`draft_n: 0`)했기 때문이다. Windows의 가용 RAM도 최저 `7,933,952 bytes`(7.57MiB)까지 줄어들며 페이지 캐시에 쓸 메모리가 부족해져 매 토큰마다 NVMe SSD를 읽어야 했다.

2라운드 `Qwen 3.8 Flash Next`는 내장 MTP가 62.4%에서 88.2%의 수락률로 작동하며 `quantum` 응답 시간을 31.86초(초당 13.10토큰)로 줄였다. 그러나 62GB 권장 모델을 32GB RAM에서 실행한 탓에 RAM에 상주한 전문가 가중치는 5.82GiB뿐이었고, 세 질문을 처리하는 동안 SSD에서 읽은 전문가 가중치가 총 `233,364.9MB`(약 233.4GB)에 달했다. 실행 도중 VRAM 여유 공간이 289MiB까지 줄자 런타임 경고가 출력됐고, `asyncio` 코딩 과제에서는 소비자 태스크 2개(`소비자1`, `소비자2`)를 만든 뒤 종료 신호인 `await queue.put(None)`을 한 번만 호출해 두 번째 소비자가 무한 대기하다 15초 제한 시간 초과로 종료됐다.

![두 테이블 사이 좁은 다리에서 수레들이 정체된 왼쪽 경로와 하나의 트레이 안에 하늘색 블록 여섯 개가 정돈된 오른쪽 구성을 비교하는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-deepseek-qwen38-27b/03-partial-offload-vs-vram.png)

## 3라운드: Qwen 3.8 27B 다섯 구성과 12GB VRAM 적재 효과

이번에는 27B Dense 모델 `Qwen 3.8 27B`를 선택했다. 모델 전체를 메모리에 적재하면 SSD 스트리밍보다 얼마나 빠를까. `Qwen 3.8 27B`는 66개 레이어로 구성된 Dense 모델이라 Strata 카탈로그 대상과 구조가 다르며, 공식 `llama.cpp`(`b11871`, 컨텍스트 8192, Flash Attention, KV 캐시 `q8_0`)로 실행했다.[^qwen27b-models]

[^qwen27b-models]: 3라운드 비교에는 `unsloth/Qwen3.8-27B-GGUF`의 `UD-Q4_K_M`(16.46GB)과 `UD-IQ3_XXS`(10.93GB), 그리고 `ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-IQ2_XS-mtp-GGUF`(8.77GB)를 사용했다. Unsloth GGUF에도 MTP 가중치 텐서가 포함돼 있어 `--spec-type draft-mtp` 옵션으로 MTP를 켰을 때와 껐을 때를 비교했고, 가장 빠른 `IQ2_XS-mtp`는 Windows 네이티브(CUDA 12.4)와 WSL2 Ubuntu 22.04 `ext4`(CUDA 12.8, `--load-mode dio`) 양쪽에서 모두 측정했다.

이번 실험에서는 **12GB VRAM에 66개 레이어를 모두 적재할 수 있는지** 확인했다. Windows 11 데스크톱 환경에서는 운영체제 합성기와 백그라운드 앱이 기본으로 1.5GB에서 2.1GB의 VRAM을 점유한다. 이 환경에서 로컬 LLM에 사용할 수 있는 VRAM은 약 10GB였다.

<div class="llm-viz" role="region" aria-label="7개 실행 구성의 양자 역학 응답 시간 및 토큰 생성 속도 비교 그래프">
  <div class="llm-viz-title">
    <span>양자 역학 설명(quantum) 완료 시간 및 생성 속도 비교</span>
    <span class="llm-badge llm-badge-ok">WSL2 ext4 최고 40.02 tok/s (7.76초)</span>
  </div>
  <div class="llm-legend">
    <span class="llm-legend-item"><span class="llm-dot llm-dot-ssd"></span>SSD 스트리밍</span>
    <span class="llm-legend-item"><span class="llm-dot llm-dot-ram"></span>VRAM + RAM 분할</span>
    <span class="llm-legend-item"><span class="llm-dot llm-dot-vram"></span>66/66 VRAM (Windows)</span>
    <span class="llm-legend-item"><span class="llm-dot llm-dot-wsl"></span>66/66 VRAM (WSL2 ext4)</span>
  </div>
  <div class="llm-bar-group">
    <div class="llm-bar-row">
      <div class="llm-bar-label-line">
        <span class="llm-bar-model">1. DeepSeek V4.1 Flash (763B, 1.75bpw, 240.3GB)</span>
        <span class="llm-bar-stats">사과 13.91초 <span class="llm-badge llm-badge-err">SSD 스트리밍</span></span>
      </div>
      <div class="llm-dual-bars">
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>완료 시간</span><strong>273.81초</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ssd" style="width: 100%;"></div></div>
        </div>
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>생성 속도</span><strong>2.70 tok/s</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ssd" style="width: 6.7%;"></div></div>
        </div>
      </div>
    </div>
    <div class="llm-bar-row">
      <div class="llm-bar-label-line">
        <span class="llm-bar-model">2. Qwen 3.8 27B UD-Q4_K_M 단독 (16.46GB)</span>
        <span class="llm-bar-stats">사과 4.21초 / 코딩 249.23초 <span class="llm-badge llm-badge-warn">RAM 분할</span></span>
      </div>
      <div class="llm-dual-bars">
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>완료 시간</span><strong>62.98초</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ram" style="width: 23.0%;"></div></div>
        </div>
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>생성 속도</span><strong>6.26 tok/s</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ram" style="width: 15.6%;"></div></div>
        </div>
      </div>
    </div>
    <div class="llm-bar-row">
      <div class="llm-bar-label-line">
        <span class="llm-bar-model">3. Qwen 3.8 27B UD-IQ3_XXS + MTP (10.93GB)</span>
        <span class="llm-bar-stats">사과 1.87초 / 코딩 94.95초 <span class="llm-badge llm-badge-warn">일부 RAM 분할</span></span>
      </div>
      <div class="llm-dual-bars">
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>완료 시간</span><strong>38.84초</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ram" style="width: 14.2%;"></div></div>
        </div>
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>생성 속도</span><strong>9.89 tok/s</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ram" style="width: 24.7%;"></div></div>
        </div>
      </div>
    </div>
    <div class="llm-bar-row">
      <div class="llm-bar-label-line">
        <span class="llm-bar-model">4. Qwen 3.8 Flash Next (180B, IQ3_S + Strata MTP, 78.1GiB)</span>
        <span class="llm-bar-stats">사과 7.66초 / 코딩 84.94초 <span class="llm-badge llm-badge-err">코딩 타임아웃</span></span>
      </div>
      <div class="llm-dual-bars">
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>완료 시간</span><strong>31.86초</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ssd" style="width: 11.6%;"></div></div>
        </div>
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>생성 속도</span><strong>13.10 tok/s</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ssd" style="width: 32.7%;"></div></div>
        </div>
      </div>
    </div>
    <div class="llm-bar-row">
      <div class="llm-bar-label-line">
        <span class="llm-bar-model">5. Qwen 3.8 27B UD-IQ3_XXS 단독 (10.93GB)</span>
        <span class="llm-bar-stats">사과 2.60초 / 코딩 132.09초 <span class="llm-badge llm-badge-warn">일부 RAM 분할</span></span>
      </div>
      <div class="llm-dual-bars">
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>완료 시간</span><strong>29.10초</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ram" style="width: 10.6%;"></div></div>
        </div>
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>생성 속도</span><strong>12.15 tok/s</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-ram" style="width: 30.4%;"></div></div>
        </div>
      </div>
    </div>
    <div class="llm-bar-row">
      <div class="llm-bar-label-line">
        <span class="llm-bar-model">6. Qwen 3.8 27B GSQ-RCO IQ2_XS + MTP (8.77GB, Windows)</span>
        <span class="llm-bar-stats">사과 0.97초 / 코딩 38.56초 <span class="llm-badge llm-badge-ok">66/66 VRAM</span></span>
      </div>
      <div class="llm-dual-bars">
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>완료 시간</span><strong>11.50초</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-vram" style="width: 4.2%;"></div></div>
        </div>
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>생성 속도</span><strong>29.88 tok/s</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-vram" style="width: 74.7%;"></div></div>
        </div>
      </div>
    </div>
    <div class="llm-bar-row">
      <div class="llm-bar-label-line">
        <span class="llm-bar-model">7. Qwen 3.8 27B GSQ-RCO IQ2_XS + MTP (8.77GB, WSL2 ext4)</span>
        <span class="llm-bar-stats">사과 0.74초 / 웜업 4.06초 <span class="llm-badge llm-badge-ok">66/66 VRAM + DIO</span></span>
      </div>
      <div class="llm-dual-bars">
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>완료 시간</span><strong>7.76초</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-wsl" style="width: 2.8%;"></div></div>
        </div>
        <div class="llm-dual-cell">
          <div class="llm-dual-caption"><span>생성 속도</span><strong>40.02 tok/s</strong></div>
          <div class="llm-bar-track"><div class="llm-bar-fill llm-fill-wsl" style="width: 100%;"></div></div>
        </div>
      </div>
    </div>
  </div>
</div>

16.46GB인 `UD-Q4_K_M`은 일부 레이어를 시스템 RAM에 적재했다. 생성 속도는 초당 6.11에서 6.34토큰이었고, 추론을 포함해 1,512토큰이 출력된 `asyncio` 응답에는 249.23초가 걸렸다. 가용 시스템 RAM도 최저 0.26GiB까지 줄었다. 10.93GB인 `UD-IQ3_XXS`는 프롬프트 평가 속도가 초당 143에서 201토큰이었고, `quantum`과 `asyncio`의 생성 속도는 각각 초당 12.15토큰과 14.47토큰이었다. Windows가 사용하는 VRAM 때문에 일부 레이어는 시스템 RAM에 적재됐으며, 최대 VRAM 점유량은 11,947MiB였다.

ISTA-DASLab의 `GSQ-RCO-IQ2_XS-mtp`는 파일 크기가 8.77GB(8.17GiB)다. 66개 레이어를 모두 VRAM에 적재했으며, 가중치가 점유한 VRAM은 8,089MiB였다. Windows 네이티브에서 기동과 웜업에는 총 7.86초가 걸렸고, 응답 시간은 `apples` <strong>0.97초(`38.87 tok/s`)</strong>, `quantum` <strong>11.50초(`29.88 tok/s`)</strong>, `asyncio` <strong>38.56초(`27.73 tok/s`)</strong>였다. 같은 8.77GB 모델을 WSL2 Ubuntu 22.04의 `ext4` 파일시스템에 두고 Linux용 `llama.cpp`(`b11871`, CUDA 12.8, `--load-mode dio`)로 구동하자 기동 후 웜업은 <strong>4.06초</strong>로 단축됐고, `apples`는 <strong>0.74초(`58.05 tok/s`)</strong>, `quantum`은 <strong>7.76초(`40.02 tok/s`)</strong>를 기록했다. 2비트대 양자화 모델이 생성한 `asyncio` 코드는 소비자 수에 맞게 종료 신호(`None`)를 전송하고 각 작업 처리가 끝나면 `queue.task_done()`을 호출해 Python 실행 검증을 통과했다.

<div class="llm-viz" role="region" aria-label="32GB 시스템 RAM 점유량과 최소 가용 여유 메모리 비교 다이어그램">
  <div class="llm-viz-title">
    <span>추론 중 시스템 RAM 점유량과 최소 가용 메모리 (Windows 31.75 GiB 기준)</span>
    <span class="llm-badge llm-badge-ok">IQ2_XS 여유 8.16 GiB</span>
  </div>
  <div class="llm-tier-list">
    <div class="llm-tier-card">
      <div class="llm-tier-head">
        <span class="llm-tier-name">DeepSeek V4.1 Flash (240.32GB) / GPU 피크 11,807 MiB</span>
        <span class="llm-tier-meta">사용 31.74 GiB / <strong>최소 여유 7.57 MiB (0.02%)</strong></span>
      </div>
      <div class="llm-stack-bar">
        <div class="llm-seg-ssd" style="width: 99%;">시스템 RAM 31.74 GiB 포화</div>
        <div class="llm-seg-free" style="width: 1%; padding: 0;"></div>
      </div>
    </div>
    <div class="llm-tier-card">
      <div class="llm-tier-head">
        <span class="llm-tier-name">Qwen 3.8 27B UD-Q4_K_M (16.46GB) / GPU 피크 11,927 MiB</span>
        <span class="llm-tier-meta">사용 31.49 GiB / <strong>최소 여유 0.26 GiB (0.8%)</strong></span>
      </div>
      <div class="llm-stack-bar">
        <div class="llm-seg-ram" style="width: 98%;">시스템 RAM 31.49 GiB</div>
        <div class="llm-seg-free" style="width: 2%; padding: 0;"></div>
      </div>
    </div>
    <div class="llm-tier-card">
      <div class="llm-tier-head">
        <span class="llm-tier-name">Qwen 3.8 27B UD-IQ3_XXS 단독 (10.93GB) / GPU 피크 11,947 MiB</span>
        <span class="llm-tier-meta">사용 28.61 GiB / <strong>최소 여유 3.14 GiB (9.9%)</strong></span>
      </div>
      <div class="llm-stack-bar">
        <div class="llm-seg-ram" style="width: 90%;">시스템 RAM 28.61 GiB</div>
        <div class="llm-seg-free" style="width: 10%;">3.1GiB</div>
      </div>
    </div>
    <div class="llm-tier-card">
      <div class="llm-tier-head">
        <span class="llm-tier-name">Qwen 3.8 Flash Next IQ3_S (78.10GiB) / GPU 피크 11,950 MiB</span>
        <span class="llm-tier-meta">사용 27.74 GiB / <strong>최소 여유 4.00 GiB (12.6%)</strong></span>
      </div>
      <div class="llm-stack-bar">
        <div class="llm-seg-ssd" style="width: 87%;">시스템 RAM 27.74 GiB (SSD 233.4GB 읽기)</div>
        <div class="llm-seg-free" style="width: 13%;">4.0GiB</div>
      </div>
    </div>
    <div class="llm-tier-card">
      <div class="llm-tier-head">
        <span class="llm-tier-name">Qwen 3.8 27B GSQ-RCO IQ2_XS + MTP (8.77GB) / GPU 피크 11,538 MiB</span>
        <span class="llm-tier-meta">사용 23.59 GiB / <strong>최소 여유 8.16 GiB (25.7%) / WSL2 RSS 2.14 GiB</strong></span>
      </div>
      <div class="llm-stack-bar">
        <div class="llm-seg-vram" style="width: 74%;">시스템 RAM 23.59 GiB (백그라운드 포함)</div>
        <div class="llm-seg-free" style="width: 26%;">여유 8.16 GiB</div>
      </div>
    </div>
  </div>
</div>

## 실제 응답 원문 비교: 양자 역학 설명

`"양자 역학에 대해서 간단히 설명해줘."`라는 동일한 프롬프트에 각 모델이 출력한 응답 원문을 글자 변형 없이 그대로 수록했다. 초저비트 양자화와 메모리 배치에 따라 나타나는 언어 혼입 차이를 대표 모델 세 종의 원문에서 바로 비교하고, 나머지 네 구성의 원문도 아래 카드에서 펼쳐 볼 수 있다.

- **`DeepSeek V4.1 Flash` (763B, `1.75bpw`)**: 파동 함수의 붕괴 뒤에 `"다만 해석은 학자마다 다릅니다."`라는 코펜하겐 해석 단서까지 덧붙이지만, `양자 entanglement`, `microscopic 세계`, `lasers, atomic physics`처럼 한국어 문장 중간에 영어 단어가 섞여 나온다.
- **`Qwen 3.8 Flash Next` (180B MoE, `IQ3_S`)**: 친근한 해요체로 여섯 가지 개념과 응용 분야를 요약하지만, 첫 항목에서 `"에너지는連續적이지 않고 ‘덩어리’로 나온다"`처럼 한자(`連續`) 토큰이 그대로 출력됐다.
- **`Qwen 3.8 27B` (`GSQ-RCO IQ2_XS + MTP` 및 Unsloth `UD-Q4_K_M`, `UD-IQ3_XXS`)**: 8.77GB(`IQ2_XS`)로 압축해 12GB VRAM에 66개 레이어를 모두 적재한 구성에서도 한자나 영단어 혼입 없이 정돈된 한국어로 답변을 완결했다.

<div class="llm-resp-grid" role="region" aria-label="모델별 양자 역학 설명 실제 응답 원문 비교">
  <div class="llm-resp-card">
    <div class="llm-resp-header">
      <span class="llm-resp-title">1. DeepSeek V4.1 Flash 1017 (763B MoE / IST-DAS-1.75bpw)</span>
      <span class="llm-resp-meta">
        <span>273.81초 / 2.70 tok/s / 725토큰</span>
        <span class="llm-badge llm-badge-err">한영 혼용 3곳</span>
      </span>
    </div>
    <div class="llm-resp-body">양자 역학은 원자, 전자, 광자처럼 <strong>아주 작은 세계의 물리 법칙</strong>을 설명하는 이론입니다. 핵심은 다음과 같습니다.

- <strong>상태는 파동 함수로 설명된다.</strong> 입자의 상태는 수학적으로 “파동 함수”로 표현되며, 이는 여러 가능성이 중첩된 상태를 의미할 수 있습니다.
- <strong>중첩(superposition):</strong> 예를 들어 전자가 여러 위치/에너지 상태의 가능성을 동시에 “중첩”해 표현될 수 있습니다. 측정하면 그중 하나의 결과가 확률적으로 나타납니다.
- <strong>측정은 확률적이다.</strong> 양자 역학은 결과를 정확히 예측하기보다 확률로 예측합니다. 측정 후 상태가 특정 결과로 “업데이트”되며, 이 과정을 흔히 “붕괴”라고 부릅니다. 다만 해석은 학자마다 다릅니다.
- <strong>불확정성 원리:</strong> 위치와 운동량 같은 물리량을 동시에 모두 정확히 알 수 없습니다. 정확히 알수록 다른 값의 불확실성이 커집니다.
- <strong>양자화:</strong> 에너지, 상태 등이 연속적으로 임의 값을 가지기보다 특정 단위/레벨로 나뉩니다. 예: 원자 내 전자의 에너지 준위.
- <strong><mark class="llm-quirk">양자 entanglement</mark>:</strong> 두 입자의 상태가 강하게 상관되어, 멀리 떨어져 있어도 측정 결과가 서로 관련될 수 있습니다.

간단히 말하면: <strong>양자 역학은 <mark class="llm-quirk">microscopic 세계</mark>에서 입자가 파동처럼 여러 가능성을 갖고, 측정 결과는 확률적으로 나타나는 이론</strong>입니다. 일상 세계에서는 이 효과가 거의 직접 보이지 않지만, 반도체, <mark class="llm-quirk">lasers, atomic physics</mark> 등 현대 기술의 기초입니다.</div>
  </div>

  <div class="llm-resp-card">
    <div class="llm-resp-header">
      <span class="llm-resp-title">2. Qwen 3.8 Flash Next (180B MoE + 51.2B PLE / GSQ-RCO-IQ3_S + MTP)</span>
      <span class="llm-resp-meta">
        <span>31.86초 / 13.10 tok/s / 340토큰</span>
        <span class="llm-badge llm-badge-warn">한자(連續) 토큰 혼입</span>
      </span>
    </div>
    <div class="llm-resp-body">양자 역학은 아주 작은 원자나 전자 같은 미시 세계를 다루는 물리학이에요.  
간단히 핵심만 말하면:

- <strong><mark class="llm-quirk">에너지는連續적이지 않고</mark> ‘덩어리’로 나온다</strong>: 양자(quantum)라는 최소 단위로 나뉘어요.  
- <strong>입자도 파동처럼 행동한다</strong>: 빛은 입자이면서 파동이고, 전자도 파동의 성질을 가집니다.  
- <strong>측정하기 전엔 여러 가능성이 섞여 있다</strong>: 예를 들어 전자가 여기저기 여러 상태를 동시에 갖는 ‘중첩’에 있을 수 있어요.  
- <strong>정확히 알 수 없는 한계가 있다</strong>: 위치와 운동량을 동시에 정확히 측정하는 데 한계가 있어요.  
- <strong>관측하면 상태가 ‘하나로 결정된다’</strong>: 측정하면 가능성 중 하나가 실제로 나타나요.  
- <strong>얽힘이 있다</strong>: 멀리 떨어진 두 입자가 서로 연결된 것처럼 행동할 수 있어요.

쉽게 비유하면, 양자 세계는 “여러 가능성이 동시에 있고, 측정하면 그중 하나가 현실이 된다”는 규칙을 가진 세계라고 보면 돼요.  
실제 응용으로는 반도체, 레이저, MRI, 양자컴퓨터 등이 있어요.</div>
  </div>

  <div class="llm-resp-card llm-resp-highlight">
    <div class="llm-resp-header">
      <span class="llm-resp-title">3. ISTA-DASLab Qwen 3.8 27B (GSQ-RCO IQ2_XS + MTP / Windows 네이티브)</span>
      <span class="llm-resp-meta">
        <span>11.50초 / 29.88 tok/s / 323토큰</span>
        <span class="llm-badge llm-badge-ok">66/66 VRAM / 한국어 정상</span>
      </span>
    </div>
    <div class="llm-resp-body">양자 역학은 <strong>아주 작은 입자</strong>(전자, 광자 등)의 움직임을 설명하는 물리 이론입니다.

간단히 말하면:

- <strong>입자는 파동처럼 행동합니다.</strong>  
  전자는 “구슬”처럼 정확한 위치를 가지기보다, <strong>확률 분포</strong>로 존재한다고 설명합니다.

- <strong>중첩(superposition)</strong>  
  입자는 여러 상태에 동시에 있을 수 있습니다.  
  예: 전자가 “위”와 “아래” 상태의 혼합일 수 있습니다.

- <strong>측정하면 상태가 결정됩니다.</strong>  
  측정 전까지는 확률적으로 존재하지만, 측정하면 하나의 결과로 확정됩니다.

- <strong>불확정성 원리</strong>  
  위치와 운동량을 동시에 정확히 알 수 없습니다.  
  예를 들어 위치를 잘 알면 운동량은 더 불확정적입니다.

- <strong>에너지는 양자화됩니다.</strong>  
  원자 안의 전자는 임의적인 에너지가 아니라 <strong>특정 허용된 에너지 상태</strong>만 가질 수 있습니다.

한 줄로 요약하면:  
<strong>양자 역학은 작은 세계에서 입자가 “확률적이고 파동적인” 방식으로 움직인다고 설명하는 이론입니다.</strong></div>
  </div>

  <details class="llm-resp-card llm-resp-highlight">
    <summary class="llm-resp-header">
      <span class="llm-resp-title">4. ISTA-DASLab Qwen 3.8 27B (GSQ-RCO IQ2_XS + MTP / WSL2 ext4 Direct I/O)</span>
      <span class="llm-resp-meta">
        <span>7.76초 / 40.02 tok/s / 289토큰</span>
        <span class="llm-badge llm-badge-ok">66/66 VRAM / 최고 속도</span>
        <span class="llm-fold-hint"></span>
      </span>
    </summary>
    <div class="llm-resp-body">양자 역학은 <strong>아주 작은 입자(전자, 광자 등)의 행동</strong>을 설명하는 물리 이론입니다.

핵심 아이디어는 다음과 같습니다.

1. <strong>에너지가 연속적이지 않고 양자화됨</strong>
   - 원자 안의 전자 에너지는 아무 값이 아니라 <strong>특정한 에너지 준위</strong>만 가질 수 있습니다.

2. <strong>입자-파동 이중성</strong>
   - 전자 같은 입자는 입자처럼 행동하면서도 <strong>파동처럼 간섭을 일으킬 수</strong> 있습니다.

3. <strong>확률적 기술</strong>
   - 양자역학에서는 입자의 위치나 운동량이 정확히 예측되기보다, <strong>어떤 상태로 존재할 확률</strong>을 계산합니다.

4. <strong>측정과 확률 붕괴</strong>
   - 상태를 관측하면 여러 가능한 상태 중 하나로 “떨어질” 수 있습니다.

5. <strong>중첩과 간섭</strong>
   - 입자는 동시에 여러 상태에 있을 수 있고, 서로 다른 경로를 통해 간섭할 수 있습니다.

간단히 말하면,  
<strong>양자역학은 미세 세계에서 “확률”와 “양자 상태”가 중심이 되는 물리 이론</strong>입니다.</div>
  </details>

  <details class="llm-resp-card">
    <summary class="llm-resp-header">
      <span class="llm-resp-title">5. Unsloth Qwen 3.8 27B (UD-Q4_K_M 단독 / 16.46GB)</span>
      <span class="llm-resp-meta">
        <span>62.98초 / 6.26 tok/s / 384토큰</span>
        <span class="llm-badge llm-badge-info">4비트 기준선 / RAM 분할</span>
        <span class="llm-fold-hint"></span>
      </span>
    </summary>
    <div class="llm-resp-body">양자역학은 <strong>아주 작은 입자(전자, 원자, 빛 등)의 움직임을 설명하는 물리학 이론</strong>입니다.

크게 이런 특징이 있어요.

1. <strong>입자가 입자이면서 파동처럼 행동함</strong>
   - 전자는 입자처럼 보이지만, 간섭무늬 같은 파동 특성도 보입니다.

2. <strong>상태가 여러 가능성으로 겹쳐 있을 수 있음</strong>
   - 예를 들어 전자는 “여기에 있다, 저기에 있다”가 동시에 가능한 상태로 존재할 수 있습니다.
   - 이를 <strong>중첩(superposition)</strong> 이라 합니다.

3. <strong>관측하면 결과가 특정 상태로 고정됨</strong>
   - 측정하기 전에는 여러 가능성이 있었지만, 측정하면 하나의 결과가 나타납니다.

4. <strong>위치와 운동량을 동시에 정확히 알 수 없음</strong>
   - 이는 <strong>불확정성 원리</strong>라고 불립니다.

5. <strong>에너지는 연속적이지 않고 단위로 나뉘어 있음</strong>
   - 예를 들어 원자의 전자 에너지는 특정 값만 가능합니다.
   - 그래서 <strong>양자</strong>라는 이름이 붙었습니다.

쉽게 말하면,  
<strong>양자역학은 원자 이하 세계에서는 우리가 일상에서 느끼는 물리 법칙과 다르게, 확률과 파동, 중첩이 중요한 이론</strong>입니다.

이 이론 덕분에 반도체, 레이저, 원자시계, 양자컴퓨터 같은 기술이 가능해졌습니다.</div>
  </details>

  <details class="llm-resp-card">
    <summary class="llm-resp-header">
      <span class="llm-resp-title">6. Unsloth Qwen 3.8 27B (UD-IQ3_XXS 단독 / 10.93GB)</span>
      <span class="llm-resp-meta">
        <span>29.10초 / 12.15 tok/s / 348토큰</span>
        <span class="llm-badge llm-badge-info">일부 레이어 RAM 분할</span>
        <span class="llm-fold-hint"></span>
      </span>
    </summary>
    <div class="llm-resp-body">양자 역학(quantum mechanics)은 아주 작은 세계, 예를 들어 원자나 전자, 광자 같은 미시 입자들의 운동을 설명하는 물리 법칙입니다.

가장 중요한 개념은 다음과 같습니다:

1. <strong>파동-입자 이중성</strong>  
   전자나 빛 같은 것은 입자처럼 보이기도 하고, 파동처럼 보이기도 합니다.

2. <strong>확률적 성질</strong>  
   고전 물리학에서는 위치나 속도를 정확히 알 수 있지만, 양자 세계에서는 확률만 알 수 있습니다. 예를 들어 전자가 어디에 있는지 정확히 예측하기보다 “여기에 있을 확률”을 계산합니다.

3. <strong>양자화</strong>  
   에너지는 연속적으로만 바뀌는 것이 아니라, 일정한 단위로만 변합니다. 이를 양자화라고 합니다.

4. <strong>측정의 영향</strong>  
   측정하기 전에는 입자가 여러 상태의 혼합처럼 행동하지만, 측정하면 그중 하나의 상태로 고정됩니다. 이를 ‘파동함수의 붕괴’라고도 표현합니다.

5. <strong>중첩과 얽힘</strong>  
   입자는 여러 상태가 동시에 중첩되어 있을 수 있고, 두 입자가 얽힘 상태가 되면 한쪽의 상태가 다른 쪽과 연결되어 있습니다.

쉽게 말하면, 양자 역학은 “아주 작은 세계는 우리의 일상적 직관과 다르게 작동한다”는 이론입니다.</div>
  </details>

  <details class="llm-resp-card">
    <summary class="llm-resp-header">
      <span class="llm-resp-title">7. Unsloth Qwen 3.8 27B (UD-IQ3_XXS + MTP / 10.93GB)</span>
      <span class="llm-resp-meta">
        <span>38.84초 / 9.89 tok/s / 374토큰</span>
        <span class="llm-badge llm-badge-warn">부분 오프로딩 + MTP</span>
        <span class="llm-fold-hint"></span>
      </span>
    </summary>
    <div class="llm-resp-body">양자역학은 <strong>아주 작은 세계, 즉 원자나 전자, 광자 같은 미시 세계의 물리 법칙을 설명하는 이론</strong>입니다.

일상에서 쓰는 뉴턴 역학과는 다르게, 입자의 위치나 속성을 정확히 예측하기보다 <strong>확률적으로 설명</strong>합니다.

핵심 개념은 다음과 같습니다.

- <strong>입자-파동 이중성</strong>: 전자나 빛도 입자처럼 보이기도 하고, 파동처럼 보이기도 합니다.
- <strong>양자화</strong>: 에너지 같은 물리량은 연속적으로 변하지 않고, 작은 단위로만 존재할 수 있습니다.
- <strong>파동함수와 확률</strong>: 입자의 상태는 파동함수로 표현되며, 측정 결과는 확률로만 예측합니다.
- <strong>불확정성 원리</strong>: 입자의 위치와 운동량은 동시에 정확히 알 수 없습니다.
- <strong>측정의 효과</strong>: 측정 전에는 여러 상태가 중첩되어 있다가, 측정하면 하나의 결과로 결정됩니다.
- <strong>양자 얽힘</strong>: 두 입자가 서로 연결되어 있어, 한쪽을 측정하면 다른쪽 상태도 영향을 받을 수 있습니다.

쉽게 말하면, 양자역학은 <strong>작은 세계에서는 “확정된 상태”가 아니라 “가능성”으로 물리현상이 설명된다는 이론</strong>입니다.</div>
  </details>
</div>

![책상 앞에서 초시계를 들고 미소 짓는 치비 서소영과 둥근 하늘색 고리를 연속으로 통과하는 종이비행기 세 대](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-deepseek-qwen38-27b/04-sweet-spot-mtp.png)

## 가장 흥미로운 지점

**`UD-IQ3_XXS`는 일부 레이어를 시스템 RAM에 적재한 구성에서 MTP 적용 뒤 장문 생성 속도가 느려졌다.** 흔히 추측 디코딩이나 MTP를 켜면 어떤 환경에서든 생성 속도가 빨라질 것이라 기대한다. 실제로 15토큰만 생성한 단문 과제(`apples`)에서는 MTP가 빨랐다. `UD-IQ3_XXS`의 생성 속도는 초당 9.48토큰에서 16.99토큰으로 향상됐고, 드래프트 수락률은 100%(`15/15`)였다.

그러나 장문 과제 두 개에서는 MTP를 켜자 생성 속도가 느려졌다. `quantum`은 초당 12.15토큰에서 9.89토큰으로, `asyncio`는 초당 14.47토큰에서 10.28토큰으로 감소했다.[^mtp-walltime] MTP는 매 스텝마다 여러 후보 토큰을 한꺼번에 검증하므로 단일 토큰 디코딩보다 스텝당 연산량이 많다. 일부 레이어를 시스템 RAM에 적재한 구성에서는 MTP를 켰을 때 장문 토큰당 생성 시간이 69.10에서 82.30ms였던 것이 97.28에서 101.11ms로 증가했다.

[^mtp-walltime]: `UD-IQ3_XXS`의 `asyncio` 응답 시간은 MTP를 켜자 132.09초에서 94.95초로 줄었다. 이 실행에서는 내부 추론이 1,535토큰에서 599토큰으로 감소해 전체 출력도 1,904토큰에서 966토큰으로 약 절반이 됐다. 생성 속도가 느려졌어도 출력 분량이 줄어 응답은 더 일찍 끝났다.

<div class="llm-viz" role="region" aria-label="부분 오프로딩과 전량 VRAM 상주에서 MTP 적용 시 토큰당 생성 지연 비교">
  <div class="llm-viz-title">
    <span>가중치 상주 상태에 따른 MTP 토큰당 생성 시간 비교 (짧을수록 빠름)</span>
    <span class="llm-badge llm-badge-ok">66/66 VRAM 상주 시 25.0~36.1 ms</span>
  </div>
  <div class="llm-mtp-grid">
    <div class="llm-metric-box">
      <div class="llm-metric-box-title">UD-IQ3_XXS 단독 (10.93GB)</div>
      <div class="llm-metric-val">69.1–82.3 ms</div>
      <div class="llm-mtp-bar-wrap">
        <div class="llm-bar-track" style="height:14px;"><div class="llm-bar-fill llm-fill-ram" style="width: 76%;"></div></div>
      </div>
      <div class="llm-metric-chips">
        <span class="llm-chip"><strong>일부 RAM 분할</strong></span>
        <span class="llm-chip">사과 9.48 tok/s</span>
        <span class="llm-chip">양자 12.15 / 코딩 14.47 tok/s</span>
      </div>
    </div>
    <div class="llm-metric-box">
      <div class="llm-metric-box-title">UD-IQ3_XXS + MTP (10.93GB)</div>
      <div class="llm-metric-val" style="color:#d97706;">97.3–101.1 ms</div>
      <div class="llm-mtp-bar-wrap">
        <div class="llm-bar-track" style="height:14px;"><div class="llm-bar-fill llm-fill-ssd" style="width: 100%;"></div></div>
      </div>
      <div class="llm-metric-chips">
        <span class="llm-chip"><strong>장문 지연 증가</strong></span>
        <span class="llm-chip">사과 16.99 tok/s (100%)</span>
        <span class="llm-chip">양자 9.89 / 코딩 10.28 tok/s</span>
      </div>
    </div>
    <div class="llm-metric-box" style="border-color:#0284c7;">
      <div class="llm-metric-box-title">GSQ IQ2_XS + MTP (8.77GB)</div>
      <div class="llm-metric-val" style="color:#0284c7;">25.0–36.1 ms</div>
      <div class="llm-mtp-bar-wrap">
        <div class="llm-bar-track" style="height:14px;"><div class="llm-bar-fill llm-fill-vram" style="width: 30%;"></div></div>
      </div>
      <div class="llm-metric-chips">
        <span class="llm-chip"><strong>66/66 VRAM 상주</strong></span>
        <span class="llm-chip">Win: 29.88 / 27.73 tok/s</span>
        <span class="llm-chip">WSL2: <strong>40.02 tok/s</strong> (25.0ms)</span>
      </div>
    </div>
  </div>
</div>

8.77GB인 `IQ2_XS-mtp`는 `UD-IQ3_XXS`보다 약 2.1GB 작아 66개 레이어를 모두 VRAM에 적재할 수 있었다. MTP를 켠 이 구성의 장문 생성 속도는 Windows에서 초당 27.73에서 29.88토큰, WSL2 `ext4`에서 초당 40.02토큰이었다. 드래프트 수락률은 `quantum` 기준 Windows 48.0%(`190/396`), WSL2 40.2%(`158/393`)로 `UD-IQ3_XXS`와 비슷했지만, 토큰당 생성 시간은 Windows에서 33.5에서 36.1ms, WSL2에서 25.0ms로 훨씬 짧았다.

이번 PC에서는 파라미터가 가장 많은 모델보다 모든 레이어를 VRAM에 적재한 모델이 훨씬 빨리 응답했고 한국어 문장 완결성도 높았다. Strata의 SSD 스트리밍 덕분에 12GB VRAM PC에서도 763B와 180B 모델을 실행해 결과를 확인해 볼 수 있었다. 이 PC에서 빠른 질의응답과 코딩 보조에 쓸 구성을 고른다면 `Qwen 3.8 27B IQ2_XS-mtp`와 MTP를 선택하겠다. 세 과제의 응답 시간이 가장 짧았고, 한자나 영단어 혼입 없이 답변을 생성했으며, 실행 내내 시스템 여유 RAM도 8.16GiB 이상 유지됐다.

## 출처

- [Strata 런타임 릴리스 및 카탈로그 (`Subramaniyam/strata`)](https://github.com/Subramaniyam/strata)
- [ISTA-DASLab Qwen3.8-27B-GSQ-RCO-IQ2_XS-mtp-GGUF (Hugging Face)](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-IQ2_XS-mtp-GGUF)
- [Unsloth Qwen3.8-27B-GGUF (`UD-Q4_K_M`, `UD-IQ3_XXS`) (Hugging Face)](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)
- [SC117 Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF (Hugging Face)](https://huggingface.co/SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF)
- [llama.cpp 공식 릴리스 b11871 (`ggml-org/llama.cpp`)](https://github.com/ggml-org/llama.cpp/releases/tag/b11871)
- 치비 서소영 삽화 4장은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 `gpt-image-2.5-flare`로 따로 생성했다.
