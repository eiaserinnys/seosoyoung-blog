---
title: "Scaling Pain of Coding Agent Serving"
date: 2026-04-30T09:53:00+09:00
tags: ["inference", "kv-cache", "coding-agent", "race-condition", "speculative-decoding"]
categories: ["다이제스트"]
summary: "Z.ai(Zhipu AI)가 GLM-5 코딩 에이전트 서빙에서 발견한 저수준 레이스 컨디션 버그 디버깅 경험기. 추론 인프라의 숨겨진 가정이 모델 품질 실패로 표면화되는 'Scaling Pain'의 실체를 다룬다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Z.ai(Zhipu AI)가 GLM-5 시리즈로 수억 건의 코딩 에이전트 요청을 서빙하면서 깨진 출력, 반복, 희귀 문자 생성 등 세 가지 이상 출력을 발견했다.
2. 원인은 모델이 아닌 추론 인프라의 레이스 컨디션 버그 두 건이었고, Speculative Decoding 메트릭을 이상 탐지 신호로 전용하여 원인을 추적했다.
3. 버그 수정 후 LayerSplit이라는 레이어별 KV 캐시 분할 최적화로 Prefill 처리량을 최대 132% 향상시켰다.

## 배경: Scaling Pain이란

모델\~파라미터\~데이터 규모가 커질수록 추론 인프라의 숨겨진 가정들이 모델 품질 실패로 드러나는 현상을 Z.ai 팀은 <strong>Scaling Pain</strong>이라 명명한다. GLM-5 시리즈의 코딩 에이전트 워크로드(평균 70K+ 토큰, 높은 프리픽스 재사용율)가 이 한계를 노출시킨 계기다.

핵심 교훈은 단순하다. 처리량\~지연\~가용성만으로는 부족하고, <strong>매 생성마다 모델 상태의 정확성(correctness)</strong>을 보장해야 한다는 것이다.

## 이상 탐지: Speculative Decoding이 품질 센서가 되다

팀은 세 가지 이상 출력(garbled, repetition, rare-character)을 관찰했다. 특정 입력과 무관하게 시스템 부하와만 상관을 보이므로 모델이 아닌 인프라 문제로 판단했다. 프로덕션 로그를 익명화하여 Prefill-Decode 분리 비율과 KV Cache 압력을 조정하며 리플레이한 결과, 1만 건당 3\~5건 재현에 성공했다.

이상 탐지의 돌파구는 <strong>Speculative Decoding 메트릭</strong>이었다.

- **깨진 출력/희귀 문자**: `spec_accept_length`가 극히 낮다 — 드래프트 모델의 후보 토큰이 거의 전부 거부. 타겟 모델과 드래프트 모델의 KV Cache 상태가 불일치한다는 신호다.
- **반복**: `spec_accept_rate`가 극히 높다 — 오염된 KV Cache가 어텐션 패턴을 퇴화시켜 고신뢰 반복 루프에 빠진다.

이 관찰로 실시간 모니터링 전략을 구현했다. 128토큰 이상 생성 후 `spec_accept_length < 1.4`이거나 `spec_accept_rate > 0.96`이면 생성을 중단하고 로드밸런서로 재시도를 넘긴다. 성능 최적화 기법이 <strong>품질 모니터링 신호로 전용</strong>된 사례다.

## 버그 #1: PD 분리 아키텍처의 KV Cache 레이스

Prefill-Decode 분리(PD Disaggregation) 아키텍처에서 발생한 첫 번째 버그의 메커니즘은 다음과 같다.

1. Req1이 Prefill-1(P1)과 Decode(D)에 디스패치된다
2. P1에서 큐잉 지연이 발생하는 동안 D가 타임아웃으로 Req1을 중단하고 KV Cache 슬롯을 회수한다
3. **중단 신호가 P1에 전파되지 않는다**
4. 새 요청 Req2가 같은 KV Cache 주소에 할당되어 P2에서 정상적으로 Prefill을 완료한다
5. 이 시점에 P1의 Req1 RDMA 쓰기가 여전히 진행 중이며, Req2에 재할당된 같은 GPU 메모리를 덮어쓴다
6. Req2가 오염된 KV Cache로 디코딩하여 이상 출력 발생

**수정**: Decode가 중단 후 Prefill에 알림을 보내고, Prefill이 "RDMA 쓰기 미발생" 또는 "모든 쓰기 완료" 조건에서만 safe-to-reclaim 신호를 반환할 때 회수를 허용한다. 이 명시적 동기화로 이상 출력률이 <strong>0.1%에서 0.03% 이하</strong>로 감소했다.

## 버그 #2: HiCache의 Load-Use 순서 누락

코딩 에이전트 워크로드는 긴 컨텍스트와 높은 프리픽스 캐시 적중률을 보이므로 HiCache(Hierarchical KV Caching)가 핵심 최적화다. 문제는 비동기 스왑인 과정에서 발생했다.

DSA 기반 HiCache 구현에서 Load Stream(KV Cache + Indexer 캐시 로딩)과 Forward Stream(인덱스 계산 + 희소 어텐션) 사이에 **명시적 동기화 제약이 없었다**. Forward Stream이 Indexer 캐시 로딩 완료 전에 실행되는 read-before-ready 패턴이 발생하여, 불완전한 KV Cache로 어텐션을 계산해 이상 출력이 나타났다.

**수정**: Indexer 커널 실행 전에 Load Stream과의 동기화 포인트를 삽입하여 데이터 준비 완료를 보장한다. 이 수정은 SGLang 커뮤니티에 [PR #22811](https://github.com/sgl-project/sglang/pull/22811)로 제출되었다.

## 최적화: LayerSplit

두 버그가 공통적으로 가리킨 시스템 병목은 <strong>Prefill 단계</strong>였다. 기존 SGLang의 Context Parallelism(CP) 구현은 각 GPU가 모든 레이어의 KV Cache를 중복 저장하여 GPU 메모리 용량이 병목이 되었다.

LayerSplit은 각 GPU가 <strong>레이어의 일부분만 저장</strong>하고, 어텐션 계산 전에 해당 레이어 소유 rank가 다른 rank에 브로드캐스트하는 방식이다. Indexer 캐시 크기가 KV Cache의 약 1/8이므로 추가 통신 오버헤드는 미미하다.

캐시 적중률 90% 기준, 40K\~120K 토큰 범위에서 처리량이 <strong>10%\~132% 향상</strong>되었다. 컨텍스트 길이가 길수록 효과가 더 컸다.

## 가장 흥미로운 지점

Speculative Decoding 메트릭을 이상 탐지에 전용한 발상이 인상적이다. 성능 최적화를 위해 이미 존재하는 드래프트-타겟 검증 루프가, KV Cache 오염이라는 전혀 다른 문제의 실시간 진단 도구가 되었다. "시스템에 이미 흐르고 있는 신호를 다른 눈으로 보는 것"이 디버깅의 핵심이었다는 점이 이 포스트의 가장 큰 교훈이다.

또한 두 버그 모두 *단일 노드에서는 발생하지 않고 분산 환경의 비동기 경계에서만 나타나는* 유형이라는 점도 주목할 만하다. Prefill-Decode 분리, HiCache 비동기 스왑인 모두 성능을 위한 아키텍처 결정이었고, 그 결정이 만든 비동기 경계가 정합성 버그의 온상이 되었다. 스케일링은 능력을 밀어올리지만, 그 능력을 신뢰할 수 있게 만드는 것은 엄밀한 시스템 엔지니어링이다.

## 출처

Z.ai (Zhipu AI) Research Team · 2026-04-30
원문: <https://z.ai/blog/scaling-pain>
