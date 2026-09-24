---
title: "Gemini 3.8 Live & Gemini 3.8 Live Extended Thinking"
date: 2026-09-16T10:30:00+09:00
tags: ["Google", "Gemini", "음성 AI", "AI 에이전트", "벤치마크"]
categories: ["모델과 연구"]
summary: "구글이 실시간 음성 모델 두 종을 내놓았다. 저렴한 3.8 Live와 복잡한 과제를 수행하는 3.8 Live Extended Thinking이다. 이름은 체급 차이를 암시하지만 모델 카드에는 둘 다 Gemini 3 Pro에 기반한다고 적혀 있고, 가격표의 단가도 같다. 2026년 9월 16일 기준 공식 발표와 모델 카드, 가격표로 확인한 내용을 정리했다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/gemini-3-8-live-extended-thinking/01-cover.png"
  alt: "치비 서소영이 한 손을 들어 말을 이어 가는 몸짓을 하고 있고, 그 뒤로 톱니바퀴와 서류 카드가 멈추지 않고 차례로 처리되며 떠 있다"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/gemini-3-8-live-extended-thinking/01-cover.png"
sidenotes: true
---

## 3줄 요약

1. 구글이 2026년 9월 15일 실시간 음성 모델 두 종을 공개했다. **Gemini 3.8 Live**는 작은 규모의 저렴한 모델이고, **Gemini 3.8 Live Extended Thinking**은 여러 단계를 거쳐야 하는 복잡한 과제를 수행할 수 있는 보다 강력한 모델이다. 공개와 동시에 Gemini API와 AI Studio에서 사용 가능하다.
2. 발표문에 공개된 수치는 대체로 Extended Thinking을 중점적으로 조명하고 있다. Artificial Analysis의 Speech to Speech Index에서 82.6점으로 전체 1위, Big Bench Audio 97.7%, τ-Voice 68.6%, Sierra의 τ-Voice-banking 35.1%다. 2위 GPT-Live-1과는 1.1점 차이다.
3. 두 모델은 이름이 암시하는 만큼 다르지 않다. 모델 카드는 둘 다 **Gemini 3 Pro에 기반한다**고 적었고, 가격표는 둘에 같은 단가를 매겼다. 차이는 체급보다 추론을 얼마나 깊이 하느냐에서 난다. ServiceNow의 EVA-Bench에서 3.8 Live는 대화 경험이 1위, Extended Thinking은 업무 정확도가 앞선다.

## 두 가지 모델

Gemini 3.8 Live는 두 가지 모델로 출시되었다. 발표문에서는 각각의 모델을 이렇게 설명한다.

> **Gemini 3.8 Live**: Built for scale and cost efficiency, combining conversational intelligence with fluid dialogue and visual grounding.
>
> **Gemini 3.8 Live Extended Thinking**: Built for high-complexity tasks, with increased intelligence and multi-step reasoning.

비용 효율적인 저렴한 모델과 추론을 더한 고급형 모델을 나란히 출시하는 건 특별할 것 없는 구성이다. 그런데 모델 카드에 적힌 내용을 보면 조금 흥미롭다.

> Gemini 3.8 Audio is based on Gemini 3 Pro.

3.8 Live와 3.8 Live Extended Thinking을 묶어 "Gemini 3.8 Audio"라 부르고, 두 모델이 공통적으로 Gemini 3 Pro에 기반한다고 적혀 있다. 입력 컨텍스트 128K, 출력 64K도 두 모델이 같다. 입력은 오디오와 이미지, 영상, 텍스트를 함께 받고 출력은 오디오와 텍스트로 나간다.

그러니 "Built for scale and cost efficiency"는 3.8 Live에 Extended Thinking보다 더 작은 모델을 썼다는 의미는 아니다. 같은 모델로 추론을 얼마나 돌리느냐를 다르게 설정한 두 개의 모드에 가깝다.

## 말하는 도중에 생각한다

Extended Thinking이 내세우는 강점은 동시성이다.

> 3.8 Live Extended Thinking reasons and speaks simultaneously.

기존 음성 에이전트는 말하면서 동시에 생각하지 못했다. 깊게 생각하려면 시간이 필요한데, 그 시간 동안 에이전트가 아무 말도 하지 않으면 사용자는 연결이 끊겼다고 오해하기 쉽다. 발표문은 두 가지 처방을 내놓았다. 하나는 <em>early verbal cues</em>다. "Let me check that…" 같은 말을 먼저 꺼내 요청을 받았다는 신호를 준다. 다른 하나는 <em>live progress narration</em>이다. 여러 단계를 거치는 작업을 뒤에서 처리하는 동안 진행 상황을 말로 중계한다.

3.8 Live 쪽에도 비슷한 장치가 있다. 도구와 API 호출을 배경에서 실행하면서 대화를 계속 이어 간다고 적혀 있다. 요청을 접수했다고 먼저 대답한 뒤 작업이 끝나기를 기다리며 다른 이야기를 할 수 있다는 뜻이다.

같은 문제를 [OpenAI의 GPT-Live-1](/digest/gpt-live-1-voice-guide/)은 다른 방식으로 풀었다. 그쪽은 무거운 추론을 음성 모델에서 떼어 내 뒤에 있는 별도의 텍스트 모델에 넘긴다. 위임(delegation)이라 부르는 구조다. 구글은 모델을 나누지 않고 같은 모델이 추론과 발화를 동시에 처리하는 방향을 선택했다.

3.8 Live는 시각 입력을 거의 실시간으로 처리한다. 대화 중간에 언어가 바뀌어도 97개 언어 사이에서 자동으로 감지해 전환한다.[^1]

## 벤치마크가 말하는 것과 말하지 않는 것

발표문에서 공개된 수치를 모아서 정리하면 다음과 같다.

| 항목 | 모델 | 수치 |
| --- | --- | --- |
| Artificial Analysis Speech to Speech Quality Index | 3.8 Live Extended Thinking | 82.6 (전체 1위) |
| Big Bench Audio | 3.8 Live Extended Thinking | 97.7% |
| τ-Voice (에이전트 과제 완수) | 3.8 Live Extended Thinking | 68.6% |
| τ-Voice-banking (Sierra) | 3.8 Live Extended Thinking | 35.1% |
| Speech Agent Arena | 3.8 Live | 2위 |
| ServiceNow EVA-Bench | 두 모델 | 파레토 프런티어 확장 |

순위만 보면 압도적으로 뛰어난 모델처럼 보인다. 실제로 그런지 살펴보자.

### 1위와 2위 사이의 거리

Artificial Analysis가 매기는 Speech to Speech Index는 단일 시험이 아니다. Speech Reasoning, Agentic Performance, Arena Preference, Task Success Rate 네 항목의 가중 평균이다. 2026년 9월 16일 기준 상위 세 모델은 다음과 같다.[^2]

| 순위 | 모델 | Speech to Speech Index | τ-Voice |
| --- | --- | --- | --- |
| 1 | Gemini 3.8 Live Extended Thinking (High) | 82.6 | 68.6% |
| 2 | GPT-Live-1 (Astra, medium), OpenAI | 81.5 | 67.9% |
| 3 | Grok Voice Think Fast 2.0 (High), xAI | 81.3 | 56.5% |

3위까지 세 모델의 점수 편차가 1점 언저리에 불과하다. 굳이 선두를 따지는 게 무의미하다. Sierra가 공개한 τ-Voice 진척 기록을 보면 이 분야가 얼마나 빨리 발전하는지 알 수 있다. 2025년 8월 `gpt-realtime-1.0`이 30%였고 2026년 4월 `grok-voice-think-fast-1.0`이 67%였다. 여덟 달 만에 벤치마크 점수가 두 배가 됐다.

### 과제 성공률 1위, 하지만 선호도는 2위

3.8 Live가 가져간 Speech Agent Arena 2위도 뜯어볼 만하다. Arena는 사람이 두 응답을 비교해 고르는 선호 기반 Elo다. 현재 상위 세 모델이 전부 구글 모델이다.

| 순위 | 모델 | Elo | 과제 성공률 |
| --- | --- | --- | --- |
| 1 | Gemini 3.1 Flash Live Minimal | 1096 | 74.6% |
| 2 | Gemini 3.8 Live | 1083 | 93.2% |
| 3 | Gemini 3.1 Flash Live High | 1063 | 71.8% |

2위가 1위보다 과제 성공률이 18.6%포인트 높다. Gemini 3.8 Live의 과제 성공률이 높았지만, 사람들이 이 모델과의 대화를 선호하지는 않았다는 의미다.

### EVA-Bench가 그리는 절충선

ServiceNow의 EVA-Bench는 여러 턴에 걸친 통화 전체를 봇 대 봇 구조로 돌려 보고 두 축으로 채점한다. 정확도에 해당하는 EVA-A와 대화 경험에 해당하는 EVA-X다. 과제 완수는 EVA-A 안의 하위 항목이고, EVA-X는 턴 주고받기와 간결함, 대화 진행으로 구성된다.[^3]

| 모델 | EVA-A pass@1 (정확도) | 과제 완수 | EVA-X pass@1 (경험) |
| --- | --- | --- | --- |
| Gemini 3.8 Live | 0.46 | 0.71 | **0.89** |
| Gemini 3.8 Live Extended Thinking (High) | **0.55** | **0.87** | 0.74 |

두 모델의 평가 점수 사이의 대비가 흥미롭다. 3.8 Live는 EVA-X 0.89와 턴 주고받기 0.97로 스무 개 시스템 가운데 두 항목 모두 1위다. 대화가 가장 매끄럽다는 뜻이다. Extended Thinking은 정확도와 과제 완수에서 앞서고 경험 점수에서 뒤처진다. 생각하는 동안 나누는 대화가 매끄럽지는 않다는 것으로 해석할 수 있다.[^4]

### 실제 업무 점수는 35.1%

τ-Voice는 Sierra가 만든 벤치마크로, 텍스트판 τ-bench의 고객 응대 과제 278건을 그대로 가져와 실제 통화 환경에서 수행한다. 소음과 전화망 압축, 프레임 손실, 억양이 섞인 음성까지 포함되어 있다. 은행 업무판은 여기에 은행 업무 과제라는 맥락을 적용한 것이다.

τ-Voice에서 받은 68.6%와는 달리, 은행 업무판에서는 점수가 35.1%까지 떨어진다. 벤치마크를 리드하고 있다는 표현이 무색하게 창구에서 시키는 일 열 가지 가운데 여섯 가지 이상을 제대로 끝내지 못한다는 뜻이다.

## 흥미로운 요금 정책

두 모델의 발표에서 재미있다면 가장 재미있는 대목이다. Gemini API 가격 페이지는 `gemini-3.8-live`와 `gemini-3.8-live-extended-thinking`, 그리고 `gemini-3.1-flash-live-preview`까지 **세 모델에 모두 같은 단가가 책정되어 있다**.

| 구분 | 무료 등급 | 유료 등급 (100만 토큰 기준) |
| --- | --- | --- |
| 입력 | 무료 | 텍스트 0.75달러 / 오디오 3.00달러(분당 0.005달러) / 이미지와 영상 1.00달러(분당 0.002달러) |
| 출력 (추론 토큰 포함) | 무료 | 텍스트 4.50달러 / 오디오 12.00달러(분당 0.018달러) |
| Google 검색 그라운딩 | 지원 | 월 5,000회 무료(Gemini 3.x 전 모델 공유), 이후 1,000회당 14달러 |

출력 칸의 괄호가 중요하다. <em>including thinking tokens</em>. 추론 토큰이 별도 요율을 갖지 않고 텍스트 출력 단가에 함께 들어간다. Extended Thinking이 추론을 더 많이 하는 만큼 더 많은 토큰 비용을 지불하게 될 것으로 예상할 수 있다.

분당 환산값은 구글이 표에 직접 적어 두었다. 이 계산에 따르면 대략 1초 분량의 오디오가 25토큰에 대응한다. 1분이면 1,500토큰이고, 입력은 100만 토큰당 3.00달러이므로 분당 0.0045달러, 출력은 12.00달러이므로 분당 0.018달러가 된다.

### 한 시간 통화를 계산해 보면

사용자가 한 시간 동안 Live API를 사용해서 대화하는 상황의 비용을 추산해보자. 에이전트가 발화하는 시간이 1시간 중 20분이라고 가정하면 다음과 같다.

- 입력 오디오 60분 = 90,000토큰 → 0.27달러
- 출력 오디오 20분 = 30,000토큰 → 0.36달러
- 합계 **0.63달러** (약 846원)

Extended Thinking을 쓴다면 추론 토큰이 더 붙는다. 한 시간 동안 60번 생각하고 한 번에 800토큰을 쓴다고 하면 48,000토큰이고, 텍스트 출력 4.50달러 기준으로 0.22달러다. 위 계산에 더하면 시간당 0.85달러 정도가 된다.

### 모델 간 비용 비교

다른 모델의 비용과 비교해보자. Gemini 3.8 Live는 토큰 단위로 비용을 청구하지만, OpenAI GPT-Live-1은 시간 단위로 비용을 청구한다. 비교하기 편하도록 표로 만들면 다음과 같다.

| 항목 | Gemini 3.8 Live | GPT-Live-1 |
| --- | --- | --- |
| 과금 단위 | 오디오 토큰 (초당 25토큰) | 세션 벽시계 시간 |
| 1시간 음성 레이어 | 0.63달러 (위 가정 기준) | 3.00달러 |
| 침묵 | 스트림을 보낸 만큼 입력으로 계산 | 100% 그대로 과금 |
| 추론 비용 | 같은 모델의 출력 토큰에 합산 | 백엔드 모델 요금으로 분리 |
| 검색 | 1,000회당 14달러 (월 5,000회 무료) | 1,000회당 10달러 |

이 계산은 1시간 동안 20분만 모델이 발화한다는 가정으로 산출한 비용이므로 객관적인 비교라고 보긴 어렵다. Artificial Analysis가 2026년 9월 16일 Big Bench Audio를 돌리며 입력 오디오 한 시간당 실제 비용을 측정한 결과는 다음과 같다.[^2]

| 모델 | 입력 오디오 시간당 비용 |
| --- | --- |
| Gemini 3.8 Live | 0.84달러 |
| Gemini 3.8 Live Extended Thinking (High) | 3.50달러 |
| Grok Voice Think Fast 2.0 (High) | 4.80달러 |
| GPT-Live-1 (Astra, medium) | 5.83달러 |

같은 과제를 풀게 했을 때 3.8 Live는 GPT-Live-1의 7분의 1 수준으로 저렴하고, Extended Thinking을 켜도 여전히 다른 모델 대비 저렴하다.

두 모델 모두 무료 등급에서 요금 없이 쓸 수 있지만, 대신 입력이 제품 개선에 쓰인다.

## 모델 카드에서 더 확인되는 것들

발표문에 없고 모델 카드에만 있는 항목이 몇 가지 있다.

**지식 컷오프가 2025년 1월이다.** 2026년 9월에 나온 모델의 지식이 20개월 가까이 뒤처져 있다는 점은 사용 상 주의를 해야 하는 부분이다. 도구가 맥락을 보충해준다면 큰 문제가 아니지만, 모델의 내장 지식에 의존해야 하는 상황이라면 주의를 기울여야 한다.

**프런티어 안전 평가는 대리 평가다.** 카드는 Gemini 3.7 Flash를 평가해 어떤 Tracked/Critical Capability Level에도 도달하지 않은 것을 확인했고, 3.8 Live와 Extended Thinking이 3.7 Flash에 견줘 의미 있는 새 능력이나 실질적 성능 증가를 보여주지 않았으므로 같은 결론을 적용한다고 적었다.

**알려진 한계**로는 환각과 함께 간헐적인 지연이나 타임아웃이 명시돼 있다. 실시간 음성 제품에서 타임아웃은 곧 통화 중단이므로, 파일럿 단계에서 재접속 처리를 먼저 설계해 두는 편이 안전하다.

**SynthID 워터마킹.** 생성된 모든 오디오에 SynthID 워터마킹이 들어간다. SynthID는 사람 귀에 들리지 않는 형태로 출력에 섞여 들어가 AI가 만든 음성임을 판별할 수 있도록 돕는 기술이다.

## 어디서 쓸 수 있는가

두 모델은 공개된 범위가 조금 다르다. 보다 강력한 모델인 Extended Thinking은 기업이나 개인 모두 구독 사용자를 중심으로 제공된다.

| 대상 | Gemini 3.8 Live | 3.8 Live Extended Thinking |
| --- | --- | --- |
| 개발자 | Gemini API, Google AI Studio | Gemini API, Google AI Studio |
| 기업 | Gemini Enterprise 비공개 프리뷰, Gemini Enterprise for CX 예정 | 위와 같음, 여기에 Workspace 기업 고객 예정 |
| 일반 사용자 | Search Live | Gemini Live, 그리고 Workspace의 Docs(AI Pro와 Ultra 구독자), Gmail과 Keep(전 구독자) |

개발자 쪽에서는 Agora, Fishjam, LangChain, LiveKit, Pipecat, Vercel, Vision Agents와 같이 Live API를 감싼 플랫폼들이 함께 소개됐다. 실시간 미디어 스트리밍 기반을 제공해준다는 설명이다. 기업 사례로는 Salesforce, Genspark, Lumeris가 본문에 언급됐고 ServiceNow, Lenskart, Ambr AI, Casuu 등의 인용이 이미지로 붙어 있다.

## 가장 흥미로운 지점

이름이 만드는 기대와 요금표가 보여 주는 실제가 다른 자리가 가장 흥미로웠다.

"3.8 Live"와 "3.8 Live Extended Thinking"이라는 이름을 나란히 보면 체급 차이를 떠올리게 된다. 작은 모델과 큰 모델, 싼 쪽과 비싼 쪽. 지난 몇 해 동안 모델 이름이 대개 그렇게 붙었으니까. 그런데 모델 카드를 보면 둘 다 Gemini 3 Pro에 기반한다고 적혀 있고, 가격표를 보면 단가조차 같다. 차이는 정말로 추론을 얼마나 깊이 하느냐에서만 난다.

EVA-Bench가 보여주는 차이도 흥미롭다. 3.8 Live는 대화 경험에서 1위지만 업무 정확도는 0.46이다. Extended Thinking은 정확도가 0.55로 높아지지만, 대화 경험에서는 뒤떨어진다. 생각을 많이 하면 대화 품질이 떨어진다. 둘 다 잘하는 것이 쉽지 않은 모양이다.

그렇다면 왜 두 가지 모델로 내놓았을까. 용도가 달라서라기보다 추론에 드는 컴퓨팅 때문이라고 보는 편이 합리적이다. Extended Thinking은 구독 사용자와 유료 API 사용자에게만 열려 있다. 같은 모델을 한 벌만 배포해 두고 추론을 얼마나 돌릴지만 다르게 설정한 뒤 요금을 따로 받는 구조라면, 모델을 두 종류 만들어 각각 서비스하는 것보다 배포가 단순해지고 비용도 줄어든다.

## 출처

2026년 9월 16일 기준으로 구글 공식 발표와 DeepMind 모델 카드, Gemini API 문서를 1차 출처로 삼아 확인했다.

- Tom Ouyang, "Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking", Google Blog, 2026-09-15. <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/>
- Google DeepMind, "Gemini 3.8 Audio (Live, Live Extended Thinking)" 모델 카드, 2026년 9월. <https://deepmind.google/models/model-cards/gemini-3-8-audio/>
- Gemini API, "Pricing". <https://ai.google.dev/gemini-api/docs/pricing>
- Gemini API, "Live API overview". <https://ai.google.dev/gemini-api/docs/live-api>

발표문이 인용한 벤치마크는 각 운영 주체의 리더보드에서 직접 확인했다.

- Artificial Analysis, "Speech to Speech" 리더보드와 Speech Agent Arena. <https://artificialanalysis.ai/speech-to-speech>
- ServiceNow AI Research, "EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents". <https://servicenow.github.io/eva/>
- Sierra, "τ-Voice: Benchmarking Real-Time Voice Agents on Real-World Tasks", 2026-05-01. <https://sierra.ai/blog/tau-voice-benchmarking-real-time-voice-agents-on-real-world-tasks>
- 비교 대상 요금은 「[GPT-Live-1 음성 가이드](/digest/gpt-live-1-voice-guide/)」에서 정리한 OpenAI 공식 가격표를 그대로 가져왔다.
- 환율은 1달러를 1,342.79원으로 환산했다. 유럽중앙은행 2026년 9월 11일 기준환율이다.

본문 삽화는 정본 치비 서소영 라인아트로 생성했다.

[^1]: 발표문에서는 97개의 언어를 지원한다고 적혀 있지만, Gemini Live API 개요 문서에는 70개 언어를 지원한다고 쓰여 있다.

[^2]: Artificial Analysis Speech to Speech 리더보드, 2026년 9월 16일 확인. Speech Agent Arena 순위는 같은 사이트의 별도 페이지에 있다. 은행 업무판 수치는 이 리더보드에 없으며 구글 발표문에 제시된 값이다.

[^3]: 평가 대상인 20개의 모델 중, EVA-A와 EVA-X에서 모두 0.6을 넘는 시스템은 아직 없다.

[^4]: 구글이 제시한 EVA-Bench 결과는 Gemini Enterprise Agent Platform의 Live API에서 측정한 값이다.
