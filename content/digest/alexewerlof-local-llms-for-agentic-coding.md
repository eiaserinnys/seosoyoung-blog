---
title: "Using local LLMs for agentic coding"
date: 2026-06-15T10:00:00+09:00
tags: ["AI", "LLM", "코딩 에이전트", "Copilot", "로컬 LLM"]
categories: ["에이전트와 코딩"]
summary: "GitHub Copilot이 사용량 기반 과금으로 전환된 시점에, 로컬 LLM과 무료 클라우드 모델로 비용 부담 없이 에이전틱 코딩 환경을 꾸리는 실용 가이드. Gemma 4·LM Studio·Copilot Custom Endpoint·Pi·OpenRouter 무료 모델까지 단계별로 다룬다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/alexewerlof-local-llms-for-agentic-coding/lm-studio-interface.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/alexewerlof-local-llms-for-agentic-coding/lm-studio-interface.png"
---

## 3줄 요약

1. Alex Ewerlöf의 2026년 6월 4일자 글로, GitHub Copilot이 사용량 기반 과금으로 전환되고 Gemini Flash 3.5·GPT 5.5가 3배씩 비싸진 시점에 *로컬 LLM*으로 에이전틱 코딩 환경을 구축하는 방법을 다룬다. 본문 첫머리에 "*No AI is used in this entire article.*"라고 명시한 것이 인상적이다.
2. 모델은 Gemma 4 계열(특히 26B A4B MoE)을 추천하고, 구동은 LM Studio 위에서 한다. 핵심 함정은 *기본 컨텍스트 윈도우가 4K*라는 점과 *KV 캐시 양자화로 VRAM 28.75GB → 22.45GB까지 줄일 수 있다*는 점이다.
3. VS Code Copilot은 Custom Endpoint로, Pi는 별도 설정 파일로 연결한다. 하드웨어가 부족하면 OpenRouter의 무료 모델을 쓰되, *반드시 가드레일과 0달러 API 키로 비용 사고를 차단*한다.

## 가격 인상이 끝낸 허니문

GitHub은 4일 전 사용량 기반 과금으로 전환했다. 저자는 "Microsoft가 세계 최대 기업 중 하나가 된 것은 자선 사업을 해서가 아니다"라고 한 줄 짚는다. 무료였던 모델들도 더 이상 무료가 아니다.

플래그십 모델들의 가격은 성능 향상 속도와 무관하게 뛰어올랐다.

- **Google Flash 3.5**는 Flash 2.5보다 +3배 비싸다.
- **GPT 5.5**는 GPT 5보다 +3배 비싸다.
- **Claude**는 이미 너무 비쌌던 탓에 오히려 가격을 *내렸다.*

![Gemini Flash 3.5는 2.5보다 3배 비싸다 (출처: OpenRouter)](https://img.seosoyoung.eiaserinnys.me/images/alexewerlof-local-llms-for-agentic-coding/gemini-pricing.png)

GitHub은 토큰 재판매업자라서 가격 인상의 충격을 더 직접적으로 흡수해야 했다. 같은 글에 GitHub이 따로 ["AI 크레딧 사용을 최적화하는 팁"](https://code.visualstudio.com/docs/copilot/guides/optimize-usage)을 공유했다는 사실까지 인용된다.

## 로컬 모델은 어디까지 왔나

저자는 *로컬 모델이 SOTA 클라우드 모델을 따라잡지는 못한다*는 사실을 부정하지 않는다. 다만 다음 네 가지 미묘함을 강조한다.

- **가격/성능 비율** — 클라우드 SOTA 모델은 성능 향상에 비해 가격이 *지수적*으로 비싸다.
- **결정론적 하네스** — 도구·지시·구조로 약한 모델의 품질을 *최대 6배*까지 끌어올릴 수 있다. 클라우드 모델은 *raw form*에서 강하지만, 하네스가 그 격차를 상당히 메운다.
- **벤치마크 함정** — 모델을 스칼라 숫자 하나로 환원하는 것은 본질적으로 어렵다. 각 AI 랩은 *자기 모델이 잘 보이는 벤치마크*를 골라 발표한다. 결국 자기 워크로드로 직접 시험해 봐야 한다.
- **지정학 효과** — 미국 랩이 무료로 공개하는 것은 자신들의 최고작이 아니다. gpt-oss-20b는 이미 낡았고, Anthropic은 open weight를 내놓은 적이 없다. Gemma 4가 그나마 진지한 미국발 오픈 모델이다. 그래서 *Qwen, Kimi, GLM* 같은 중국 모델이 의미가 크다.

저자는 여기에 *brain rot*이라는 개념을 덧붙인다. 약한 모델은 사용자가 더 깊이 개입해야 하므로 *지적 운동*이 된다. 자전거를 타는 것과 자동차를 타는 것의 차이다.

> Our goal is not to maximize automation and offload our thinking to the machine. That would be a blunt confession that our job is automatable.

> If you do what everyone else is doing, you're gonna get the results that are average.

## Gemma 4 — 어떤 버전을 골라야 하는가

코딩 워크로드에서는 [Huggingface 리더보드](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard) 기준 중국 모델들이 대체로 상위에 있다. 저자는 그중에서도 [Gemma 4](https://deepmind.google/models/gemma/gemma-4/)를 권장한다. 버전 라인업은 다음과 같다.

| 버전 | 특징 | 권장 시점 |
|---|---|---|
| **E2B** | 2B 파라미터. 거의 모든 하드웨어에서 동작하지만 환각·중단 위험이 높다 | 극단적으로 가벼운 환경 |
| **E4B** | 4B. 시작점으로 추천 — 다운로드와 설정 비용이 낮다 | 입문 |
| **12B** | "E" 접두사가 빠졌다. *이미지를 네이티브로 이해*한다. 프론트엔드·시각 코딩 워크로드에 유리 | 스크린샷을 자주 모델에 보내는 경우 |
| **26B A4B** | 저자의 최애. 26B 중 *4B만 활성*인 MoE(전문가 혼합) 구조. 8\~12GB VRAM 카드에 들어간다 | 일반 추천 |
| **31B** | 구글의 최대 open weight 모델. MoE가 아니라 VRAM 요구량이 크다 | 충분한 VRAM 보유 시 |

QAT(Quantization-Aware Training) 변형(E4B QAT 등)은 메모리는 덜 쓰면서 품질을 거의 유지한다. Unsloth가 바닐라 Google 모델 위에 더 효율적인 [추가 작업](https://unsloth.ai/docs/models/gemma-4/qat)을 한 변형도 있다.

## 로컬 모델 구동의 4가지 구성 요소

저자는 용어 정리에 한 섹션을 할애한다. *Deep learning, Attention, LLM, SLM, Huggingface, Inference, CPU/GPU/TPU/NPU/APU/Apple Silicon* 등이 풀린다. 핵심은 SLM(Small Language Model)이 *소비자 GPU에 들어가는 LLM의 부분집합*이라는 정의와, 의미 있는 코딩 워크로드에는 *최소 4B 모델*은 필요하다는 가이드다.

실제 구동에는 네 가지 구성 요소가 필요하다.

- **하네스** — VS Code Copilot, Copilot CLI, Pi 같은 것. *결정론적 코드*가 *확률적 모델*을 둘러싼다.
- **모델** — 가중치 파일. *양자화*(Q8, Q4 등)는 이미지의 해상도에 비유할 수 있다. 형식은 GGUF, MLX 등 런타임에 따라 다르다.
- **런타임(추론 엔진)** — 모델을 실제로 돌려 토큰을 생성한다.
  - **Llama.cpp** — 가장 인기 있는 오픈소스. Meta의 Llama 모델과는 무관. LM Studio가 내부적으로 이걸 쓴다.
  - **MLX** — Apple Silicon용 런타임.
  - **ONNX Runtime** — transformers.js 등 브라우저·모바일에서 LLM을 돌릴 때.
  - **vLLM** — UC Berkeley 발 오픈소스. 주로 강력한 서버용.
- **모델 매니저(선택)** — 하드웨어와 런타임을 추상화해 GUI로 모델을 찾고 받고 돌린다. OpenAI 호환 API를 제공하는지가 중요하다.

모델 매니저로는 *Ollama, LM Studio, Jan* 세 가지가 흔히 거론된다. Ollama는 CLI 출신의 오픈소스, LM Studio는 무료지만 *오픈소스 아님*에 더 풍부한 기능, Jan은 LM Studio와 비슷하지만 오픈소스 대안이다.

![LM Studio가 저자의 Linux 노트북에서 동작하는 모습](https://img.seosoyoung.eiaserinnys.me/images/alexewerlof-local-llms-for-agentic-coding/lm-studio-interface.png)

## LM Studio 서버 설정의 함정

LM Studio 사이드바의 "Developer"에서 서버를 켜는 것까지는 쉽다. 함정은 그 다음에 있다.

**JIT 로딩과 콜드 스타트** — LM Studio는 요청이 들어와야 모델을 로드하는 *Just-In-Time* 방식이다. 첫 요청에서 10\~30초가 걸린다(*TTFT* 지연). TTL 설정으로 메모리 점유 시간을 조절할 수 있다.

**기본 컨텍스트 윈도우가 4K** — 이것이 가장 큰 함정이다. VS Code Copilot의 클라우드 모델들은 200\~400K 컨텍스트를 가정한다. 수동으로 늘려야 한다.

| Context Length | VRAM 요구량 |
|---|---|
| 262,144 (max) | 25.74 GB |
| 4,096 (default) | 18.16 GB |
| 150,000 (저자 권장) | 22.45 GB |

![Gemma 4 26B 모델의 LM Studio 고급 설정 — Context Length·GPU Offload·KV 캐시 양자화가 한 화면에 있다](https://img.seosoyoung.eiaserinnys.me/images/alexewerlof-local-llms-for-agentic-coding/gemma-4-26b-settings.png)

100K 토큰 이상을 못 올리면 VS Code Copilot에서 쓰기 어렵다. *시스템 프롬프트만 20\~40K*가 빠지기 때문이다. 그렇다고 너무 키워도 안 된다. 컨텍스트 사용량이 늘면 토큰 생성 속도가 느려진다. *하네스가 자동으로 컨텍스트를 압축하는 지점*이 스위트 스폿이다.

저자가 추천하는 비율은 LM Studio의 컨텍스트 길이 $C$, Copilot의 입력 한도 $I$, 출력 한도 $O$ 사이의 관계로 표현된다.

$$C = I + O$$

저자의 기본 설정은 $I=100\text{K}$, $O=50\text{K}$, $C=150\text{K}$다.

## KV 캐시 양자화 트릭

가장 실용적인 팁은 *KV 캐시 양자화*다.

- **K Cache Quantization Type** → `Q8_0`
- **V Cache Quantization Type** → `Q4_0`

![KV 캐시 양자화 설정 — 키는 고해상도, 값은 저해상도로](https://img.seosoyoung.eiaserinnys.me/images/alexewerlof-local-llms-for-agentic-coding/kv-cache-quantization.png)

KV 캐시는 LLM의 어텐션 메커니즘이 메모리를 다루는 방식이다. 양자화는 이미지의 해상도에 해당한다. *키는 고해상도, 값은 저해상도*가 되도록 설정한다는 것이 이 트릭의 요지다.

저자가 Gemini Pro와의 대화에서 얻은 이 조합으로, GPU 메모리 요구량은 **28.75GB → 22.45GB**까지 줄었다. 이 설정은 반드시 *저장*해야 한다 — LM Studio는 다음 로드 시 기본값으로 되돌아간다.

저자는 LM Studio 채팅창에서 <em>TPS(Token Per Second)</em>를 미리 측정해 보길 권한다. **TPS 10 미만이면 코딩 용도로는 고통스럽게 느리다.**

## Copilot Custom Endpoint 연결

VS Code 1.122.1 이상에서 Copilot Custom Endpoint를 추가한다.

![Copilot의 "Add Models" → "Custom Endpoint" 진입 화면](https://img.seosoyoung.eiaserinnys.me/images/alexewerlof-local-llms-for-agentic-coding/copilot-add-models.png)

1. Copilot 채팅창에서 모델 선택기 옆 *기어* 아이콘 클릭.
2. "Add Models" → "Custom Endpoint".
3. 이름 입력(예: *Local LM Studio*), API 키(LM Studio에서 설정한 경우만), API 형태 선택.
4. **Chat Completions** 만이 안정적으로 동작했다(저자 관찰).
5. 새로 추가된 엔트리의 톱니바퀴 → "settings in JSON"에서 `url`, `maxInputTokens`, `maxOutputTokens`, `thinking`, `vision`, `toolCalling` 등을 명시한다.

저자의 4B / 26B(MoE) 설정 예시(원문에서 그대로 인용):

```json
{
  "name": "Local LM Studio",
  "vendor": "customendpoint",
  "apiType": "chat-completions",
  "models": [
    {
      "id": "google/gemma-4-e4b",
      "name": "Gemma 4 4B (chat-completions)",
      "url": "http://localhost:1234",
      "thinking": true,
      "streaming": true,
      "toolCalling": true,
      "vision": true,
      "maxInputTokens": 64000,
      "maxOutputTokens": 16000,
      "reasoningEffortFormat": "chat-completions",
      "supportsReasoningEffort": ["off", "on"]
    },
    {
      "id": "google/gemma-4-26b-a4b",
      "name": "Gemma 4 26B MoE (chat-completions)",
      "url": "http://localhost:1234",
      "thinking": true,
      "streaming": true,
      "toolCalling": true,
      "vision": true,
      "maxInputTokens": 100000,
      "maxOutputTokens": 50000,
      "reasoningEffortFormat": "chat-completions",
      "supportsReasoningEffort": ["none","minimal","low","medium","high","xhigh"]
    }
  ]
}
```

**첫 요청의 무게** — 모델 로딩(30초) 뒤에도, Copilot의 거대한 시스템 프롬프트와 툴 정의를 처리하는 데 *2\~5분*이 걸린다. LM Studio는 프롬프트 캐싱을 존중하므로 이건 세션당 한 번이다. 클라우드 제공자는 흔한 프롬프트를 미리 캐시해 둬서 이 비용을 가려 준다. 로컬엔 그 사치가 없다.

> Tip: 남반구 거주자라면 로컬 AI 서버를 *친환경 실내 난방기*로 활용할 수 있다.

저자는 [Gemma 4 26B A4B로 만든 스네이크 게임 데모](https://github.com/alexewerlof/gemma-snake)를 곁들인다. 하드웨어는 Lenovo Thinkpad L16 Gen 2, AMD Ryzen 7 PRO 250 APU, 64GB DDR5, Aurora Linux 조합이다.

## Pi 설정 — 더 단순한 형식

Pi는 `contextWindow` 설정이 LM Studio와 잘 맞물려서 오히려 단순하다.

```json
{
  "providers": {
    "lm-studio": {
      "baseUrl": "http://host.containers.internal:1234/v1",
      "api": "openai-completions",
      "apiKey": "test",
      "models": [
        {
          "id": "google/gemma-4-e4b",
          "name": "Gemma 4 4B",
          "contextWindow": 64000,
          "maxTokens": 16000,
          "reasoning": true,
          "thinkingLevelMap": { "off": "off", "minimal": "on" }
        },
        {
          "id": "google/gemma-4-26b-a4b",
          "name": "Gemma 26B MoE",
          "input": ["text", "image"],
          "contextWindow": 150000,
          "maxTokens": 50000,
          "reasoning": true,
          "thinkingLevelMap": {
            "off": "none", "minimal": "minimal", "low": "low",
            "medium": "medium", "high": "high", "xhigh": "xhigh"
          }
        }
      ]
    }
  }
}
```

Pi는 Copilot의 거대한 시스템 프롬프트가 없어 첫 요청에서 2\~5분 대기가 없다.

## 로컬 모델 — 장단점 정리

**장점**

- 오프라인 동작
- 프라이버시
- 응답 시간(하드웨어·워크플로우·모델·설정에 따라 다름)

**단점**

- Open weight 모델은 플래그십 폐쇄 모델만큼 똑똑하지 않다. 다만 *하네스·린트·테스트·`AGENTS.md`*로 코딩 워크플로우의 정확도는 상당히 끌어올릴 수 있다.
- 같은 머신에서 개발과 추론을 같이 돌리면 *느려짐*을 체감한다.
- 콜드 스타트.
- 첫 프롬프트 입력 처리(캐시 미스).
- 하드웨어 초기 투자(Apple Silicon Mac을 쓰는 개발자에겐 큰 문제는 아니다).

저자는 *LM Studio에 익숙해진 뒤에는 GUI를 떼고 Llama.cpp를 직접 써도 된다*고 덧붙인다.

## OpenRouter 무료 모델 — 비용 사고 방지 장치

하드웨어가 부족하면 [OpenRouter](https://openrouter.ai/)의 무료 모델을 쓸 수 있다. Copilot, Zed, Pi 모두 OpenRouter를 네이티브로 지원한다.

저자는 첫 시도에서 *"농담 하나 해줘"* 프롬프트에 Opus 4.6을 골라 *비싼 농담*을 경험했다. 그 경험에서 나온 권장 절차는 다음과 같다.

![OpenRouter는 사전에 크레딧을 충전해야 동작한다](https://img.seosoyoung.eiaserinnys.me/images/alexewerlof-local-llms-for-agentic-coding/openrouter-guardrail.png)

1. **커스텀 가드레일**을 만들고 *월 1달러 상한*을 둔다.
2. 무료 모델만 *allow-list*에 둔다.
3. **새 API 키 생성 시 max credit을 0으로** 둔다. 이미 생성한 키도 설정에서 0으로 바꿀 수 있다.
4. 그 가드레일을 *코딩용 API 키*에 부착한다.

이 방식의 한계도 정리되어 있다.

- 프롬프트와 데이터가 학습에 쓰일 수 있다(ZDR 설정이 있긴 하다).
- 인터넷 연결이 필요하다.
- OpenRouter가 무료 제공을 중단할 수 있다.

대신, 모델을 받아 설정할 필요가 없고 로컬 머신이 느려지지 않는다.

**Update 2026-06-09:** 저자는 [DeepSeek V4 Pro](https://deepseek.ai/blog/claude-opus-4-8-vs-deepseek-v4)로 전환했다고 추가한다. Claude Opus 4.8에 거의 필적하면서 컨텍스트가 5배 크고, 가격은 약 17\~86배 저렴하다. 다만 OpenRouter를 통하면 GMICloud 같은 더 비싼 엔드포인트로 라우팅되어 3배쯤 비싸지는 현상을 발견하고 DeepSeek 계정을 직접 열어 충전했다. 복잡한 작업은 거기서, 단순 작업·관찰 가능성·프라이버시가 중요한 경우는 여전히 로컬 모델을 쓴다.

## 가장 흥미로운 지점

두 가지가 인상에 남는다.

첫째, *brain rot* 논의는 다른 글들에서 보기 어려웠던 자기 정직성이다. "AI에 더 위임할수록 내가 자동화 대상임을 더 정직하게 고백하는 셈"이라는 문장은 *생산성의 단기 극대화*와 *장기 적합성*의 긴장을 한 줄로 압축한다. 약한 모델을 길들이는 일이 *큰 모델을 더 잘 다루기 위한 훈련*이라는 관점은 호기심을 자극한다.

둘째, *기본 컨텍스트 윈도우 4K* 같은 디테일이다. 클라우드의 200\~400K 가정으로 같은 워크플로우를 던지면 침묵 속에서 잘려 나간다. *시스템 프롬프트만 20\~40K*라는 수치, KV 캐시 양자화로 *28.75GB → 22.45GB*까지 줄어든다는 수치 — 이런 수치들이 *로컬 추론은 본질적으로 자원 회계의 문제*라는 사실을 환기시킨다.

본문 첫머리의 *"No AI is used in this entire article."* 면책 고지도 글의 정체성을 보여 준다. AI 도구를 다루는 글이 *손으로 쓰였다*고 명시할 때, 그것 자체가 한 시대의 신호다.

## 출처

저자: Alex Ewerlöf
발행: 2026-06-04 (Update: 2026-06-09)
원문: <https://blog.alexewerlof.com/p/local-llms-for-agentic-coding>
