---
title: "Celeris-1 — The Fastest LLM on Earth"
date: 2026-07-26T10:30:00+09:00
tags: ["AI", "LLM", "확산 모델", "아키텍처", "벤치마크"]
categories: ["다이제스트"]
summary: "Celeris AI Labs가 확산 기반 추론 아키텍처로 만든 첫 모델 Celeris-1을 공개했다. GPT-5에 근접한 지능을 유지하면서 응답 지연을 15배 이상 줄이고, 초당 1,600토큰대의 생성 속도를 낸다고 주장한다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/celeris-1-fastest-diffusion-llm/01-cover.png"
images:
  - "/images/celeris-1-fastest-diffusion-llm/01-cover.png"
---

## 3줄 요약

1. Celeris AI Labs가 2026년 7월 23일 첫 모델 **Celeris-1**을 공개했다. 검색 스타트업 Marqo를 창업했던 Tom Hamer와 Jesse Clark이 세운 신생 연구소로, "프런티어 지능과 실시간 속도 사이의 간극을 좁힌다"를 사명으로 내걸었다.
2. 핵심 주장은 **GPT-5에 근접한 지능을 유지하면서 응답은 15배 이상 빠르다**는 것이다. MMLU-Pro 정확도 75.9%에 p50 응답 지연 158ms, 출력 속도는 초당 1,664토큰이라고 공개했다.
3. 비결은 토큰을 하나씩 이어 붙이는 자기회귀(autoregressive) 방식 대신 **확산(diffusion) 기법을 쓰는 새 추론 아키텍처**다. API는 OpenAI 호환이라 기존 코드에서 base URL만 바꾸면 된다고 한다.

## 무엇을 공개했나

Celeris AI Labs는 창업자 Tom Hamer(@tom_w_hamer)와 Jesse Clark(@jn2clark)이 세운 AI 연구소다. 두 사람은 앞서 검색 스타트업 Marqo를 창업한 이력이 있고, 스탠퍼드·UCL·케임브리지의 연구 경력과 Amazon Robotics·AWS·Stitch Fix에서의 엔지니어링 경험을 함께 가지고 있다고 소개된다. 연구소의 사명은 하나로 압축된다. 프런티어급 지능과 실시간 속도 사이의 간극을 좁히는 것.

그 첫 결과물이 Celeris-1이다. 사이트 첫 화면은 "지상에서 가장 빠른 LLM(The fastest LLM on Earth)"이라는 문구와 함께 "프런티어 수준의 지능, 15배 빠르게"를 내세운다. 모델은 발표와 동시에 바로 쓸 수 있게 공개됐고, celeris.ai에서 가입해 API 키를 받는 구조다.

핵심 수치는 다음과 같이 정리된다.

- MMLU-Pro 정확도 75.9%
- 응답 지연 p50 158ms — GPT-5 대비 약 13배 빠름
- 출력 속도 p50 초당 1,664토큰 — GPT-5 대비 약 24배
- 서버 처리 시간 GPT-5 대비 약 25배 단축

## 벤치마크 — 지능은 근접, 속도는 압도

Celeris가 공개한 벤치마크는 두 축이다. 하나는 지능(MMLU-Pro 정확도)과 응답 시간을 함께 놓은 그래프, 다른 하나는 순수 출력 속도다.

첫 번째 표는 MMLU-Pro(5-shot, chain-of-thought) 정확도와 응답 시간(p50)을 나란히 둔 것이다. Celeris를 포함한 GPT-5·GPT-5 mini·Gemini 계열은 추론 예산(reasoning budget)을 0으로, Mercury 2는 가장 빠른 instant 모드로 맞춰 측정했다고 밝혔다.

![Celeris 공식 벤치마크 — MMLU-Pro 정확도와 응답 시간. Celeris는 왼쪽 위(빠르고 정확) 영역에 홀로 자리한다.](/images/celeris-1-fastest-diffusion-llm/fig1-intelligence.png)

| 모델 | MMLU-Pro | 응답 시간 (p50) |
|---|---|---|
| Gemini 3.5 Flash Lite | 83.0% | 1.2s |
| GPT-5 | 81.9% | 2.0s |
| GPT-5 mini | 78.5% | 2.5s |
| Gemini 2.5 Flash | 73.0% | 2.6s |
| **Celeris-1** | **75.9%** | **158ms** |
| Inception Mercury 2 | 63.7% | 257ms |

두 번째 표는 순수 출력 속도(p50 초당 토큰)다. 약 1,000토큰짜리 장문 프롬프트로 모델마다 50회씩 요청하고, 출력은 1,024토큰으로 상한을 둔 조건이다.

![Celeris 공식 벤치마크 — 출력 속도(p50 초당 토큰). Celeris 1,664 tok/s로 2위 Mercury 2(324)의 다섯 배를 웃돈다.](/images/celeris-1-fastest-diffusion-llm/fig2-speed.png)

| 모델 | 출력 속도 (p50 tok/s) |
|---|---|
| **Celeris-1** | **1,664** |
| Inception Mercury 2 | 324 |
| Gemini 3.5 Flash Lite | 224 |
| Gemini 3.5 Flash | 134 |
| GPT-5 mini | 99 |
| GPT-5 | 69 |

정리하면 이렇다. 정확도에서는 GPT-5(81.9%)와 GPT-5 mini(78.5%)에 몇 점 뒤지지만, Gemini 2.5 Flash(73.0%)보다는 앞서고, 같은 확산 계열인 Mercury 2(63.7%)를 크게 앞선다. 대신 응답 시간과 출력 속도에서는 다른 모델들과 자릿수가 다르다. 초 단위로 응답하는 프런티어 모델들 사이에서 혼자 밀리초 단위로 답한다.

한 가지 수치는 출처에 따라 다르게 적혀 있어 그대로 옮겨 둔다. 출시 트윗에서는 ArtificialAnalysis의 초당 토큰 벤치마크 데이터셋을 재구성해 측정한 값으로 "초당 1,280토큰(gemini-3.5 flash-lite는 144)"을 제시했고, 공식 벤치마크 페이지의 장문 프롬프트 조건에서는 "초당 1,664토큰"으로 적혀 있다. 측정 조건이 다른 두 값이다.

## 새 아키텍처 — 확산으로 한꺼번에 쓴다

Celeris가 속도를 끌어내는 방식은 아키텍처 자체에 있다. 지금의 자기회귀 모델은 토큰을 하나씩 생성한다. 매 토큰이 바로 앞 토큰에 의존하기 때문에, 지연은 근본적으로 순차적이다. 문장이 길어질수록 그만큼 기다려야 한다.

Celeris는 이 순차성을 깨기 위해 확산(diffusion)에 기반한 새 추론 아키텍처를 썼다고 설명한다. 이미지 생성 모델이 잡음에서 시작해 그림 전체를 여러 번의 정제 과정으로 동시에 다듬어 내듯, 텍스트도 여러 토큰을 병렬로 만들어 낸다. 회사는 "이전 확산 시스템이 도달하지 못한 지연과 품질을 동시에 달성했다"고 강조한다. 실제로 같은 확산 계열의 Mercury 2를 지능과 속도 양쪽에서 앞선 벤치마크가 그 주장을 뒷받침하는 자리에 놓인다.

확산 언어 모델 자체는 새로운 이야기가 아니다. 구글의 Gemini Diffusion, Inception Labs의 Mercury 계열이 이미 이 방향을 밀고 있었다. Celeris-1은 그 흐름에 올라탄 또 하나의 상용 사례이자, 지능을 프런티어 근처까지 끌어올린 채로 속도를 더 밀어붙인 시도로 읽힌다.

## 어떻게 쓰나

Celeris-1의 진입 장벽은 낮게 설계돼 있다. API가 OpenAI 호환이라, 쓰던 SDK의 base URL만 Celeris 쪽으로 돌리면 기존 코드를 거의 그대로 유지할 수 있다고 안내한다.

- **OpenAI 호환**: 표준 chat-completions 요청 형식을 그대로 쓴다. 공식 OpenAI SDK나 커스텀 base URL을 지원하는 클라이언트면 붙는다.
- **스트리밍 기본값**: 스트리밍이 기본으로 켜져 있고, 응답 시작이 24ms까지 내려간다고 한다. 버퍼링이나 배치 지연이 없다.
- **토큰당 과금**: 생성한 토큰만큼만 청구하므로 속도가 빠르다고 추가 비용이 붙지 않는다.
- **지연 측정**: 성공 응답에는 `Server-Timing` 헤더로 서버 측 지연 지표가 실려 온다.

회사가 권하는 용도는 두 갈래다. 하나는 에이전트 안의 짧은 중간 작업 — 분류, 추출, 점수 매기기, 질의 재작성 같은 것이다. 다른 하나는 높은 처리량이 필요한 실시간 작업 — 실시간 코드 보조, 라이브 번역, 음성 에이전트, 대량 문서 변환 등이다. 공통점은 모델을 짧게, 여러 번, 지연이 곧 병목이 되는 자리에서 부른다는 점이다.

Python SDK 예시는 다음과 같다.

```python
from celeris import Celeris

client = Celeris(api_key="sk-…")

# 쓰던 것과 같은 호출 형태
stream = client.chat.completions.create(
    model="celeris-1",
    messages=[{"role": "user",
               "content": "Explain a Kalman filter"}],
    stream=True,
)
```

HTTP로 직접 부를 때는 이렇게 쓴다.

```bash
curl https://inference.celeris.ai/celeris-1/v1/chat/completions \
  -H "Authorization: Bearer $CELERIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "celeris-1",
       "messages": [{"role": "user", "content": "Reply with one word: fast or slow?"}],
       "max_tokens": 256, "temperature": 0, "seed": 7}'
```

## 공개 직후 반응

출시는 조용한 논문 공개가 아니라 X 타임라인을 타고 번졌다. 투자자 Hemant Mohapatra(@MohapatraHemant)는 두 창업자를 두고 "기술적 깊이와 근성이라는 드문 조합"을 이유로 투자했다고 적으며, "AI에서는 속도가 전부이고, Celeris Labs의 벤치마크는 탁월하다"고 평했다. 초기 OpenAI 연구자이자 Cresta 공동창업자인 Tim Shi, 테크 논평가 Robert Scoble 등이 이 발표를 리트윗하며 확산에 힘을 보탰다.

집계 사이트 Digg의 정리에 따르면, 관련 X 반응 48개(72개 계정)에서 감성은 100% 긍정으로 나타났고 리포스트는 44건이었다. 다만 같은 정리는 "발표 이외에 독립적으로 검증된 벤치마크나 배포 세부는 아직 확인되지 않았다"는 단서를 함께 달아 두었다. 지금까지의 수치는 모두 Celeris가 자체 공개한 값이라는 뜻이다.

## 가장 눈여겨본 것

내가 가장 눈여겨본 것은 확산 언어 모델이 "빠르지만 좀 덜 똑똑한" 자리에서 벗어나려는 움직임이다. 올해 2월 Mercury 2가 확산 LLM의 속도를 증명했을 때만 해도, 지능은 프런티어에서 한참 아래(MMLU-Pro 63.7%)였다. Celeris-1은 같은 조건의 표에서 75.9%까지 끌어올리며 GPT-5 mini(78.5%)의 코앞까지 왔다. 속도는 오히려 더 벌렸다.

물론 이 표는 전부 회사가 스스로 그린 것이다. 측정 조건을 유리하게 맞췄을 여지가 있고(추론 예산 0, instant 모드), 독립 검증도 아직 없다. 초당 토큰 수치가 출처마다 1,280과 1,664로 갈리는 것도 그 불확실성의 작은 단면이다. 그래도 확산이라는 한 갈래에서 서로 다른 팀이 비슷한 방향으로 수렴하고 있다는 것 — 이미지에서 그랬듯 언어에서도 "한 글자씩"이 유일한 답은 아닐 수 있다는 신호는, 자체 벤치의 한계를 감안해도 남는다.

## 출처

Celeris AI Labs — 공식 사이트(celeris.ai), 개발자 문서(docs.celeris.ai)
출시 발표: Tom Hamer(@tom_w_hamer), Celeris Labs(@Celeris_ai) X 게시물, 2026년 7월 23일
반응 집계: Digg 정리(2026년 7월 24일)
원문: <https://celeris.ai>

*커버 삽화: 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조하여 gpt-image-2 image-to-image로 생성했다.*
