---
title: "Gemini 3.8 Live & Gemini 3.8 Live Extended Thinking"
date: 2026-09-16T10:30:00+09:00
tags: ["Google", "Gemini", "음성 AI", "AI 에이전트", "벤치마크"]
categories: ["모델과 연구"]
summary: "구글이 실시간 음성 모델 두 종을 내놓았다. 규모와 비용을 맡는 3.8 Live, 복잡한 과제를 맡는 3.8 Live Extended Thinking이다. 발표문은 두 모델을 다른 체급처럼 소개하지만, 모델 카드와 요금표를 펴 보면 같은 Gemini 3 Pro를 바탕으로 하고 요금 칸도 한 장을 나눠 쓴다. 2026년 9월 16일 기준 공식 발표와 모델 카드, 가격표로 확인한 내용을 정리했다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/gemini-3-8-live-extended-thinking/01-cover.png"
  alt: "치비 서소영이 한 손을 들어 말을 이어 가는 몸짓을 하고 있고, 그 뒤로 톱니바퀴와 서류 카드가 멈추지 않고 차례로 처리되며 떠 있다"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/gemini-3-8-live-extended-thinking/01-cover.png"
---

## 3줄 요약

1. 구글이 2026년 9월 15일 실시간 음성 모델 두 종을 공개했다. **Gemini 3.8 Live**는 규모와 비용 효율을 맡고, **Gemini 3.8 Live Extended Thinking**은 여러 단계를 거쳐야 하는 복잡한 과제를 맡는다. 둘 다 같은 날부터 Gemini API와 AI Studio에서 열렸다.
2. 발표문이 내세운 수치는 Extended Thinking 쪽에 몰려 있다. Artificial Analysis의 Speech to Speech Index에서 82.6점으로 전체 1위, Big Bench Audio 97.7%, τ-Voice 68.6%, Sierra의 τ-Voice-banking 35.1%다. 원 리더보드를 열어 보면 2위 GPT-Live-1과의 간격이 1.1점이다.
3. 두 모델은 이름이 암시하는 만큼 멀리 떨어져 있지 않다. 모델 카드는 둘 다 **Gemini 3 Pro를 바탕으로 한다**고 적었고, 가격표는 둘을 한 칸에 묶어 같은 단가를 매겼다. 갈라지는 것은 체급보다 작동 방식 쪽이다. ServiceNow의 EVA-Bench에서 3.8 Live는 대화 경험 1위, Extended Thinking은 정확도 우위로 정확히 엇갈린다.

## 두 모델이 나뉜 자리

발표문의 첫 문단이 둘을 이렇게 가른다.

> **Gemini 3.8 Live**: Built for scale and cost efficiency, combining conversational intelligence with fluid dialogue and visual grounding.
>
> **Gemini 3.8 Live Extended Thinking**: Built for high-complexity tasks, with increased intelligence and multi-step reasoning.

읽는 그대로는 흔한 2단 구성이다. 싼 모델 하나, 똑똑한 모델 하나. 그런데 같은 날 올라온 모델 카드를 펴면 문장이 달라진다.

> Gemini 3.8 Audio is based on Gemini 3 Pro.

3.8 Live와 3.8 Live Extended Thinking을 묶어 "Gemini 3.8 Audio"라 부르고, 그 한 덩어리 전체가 Gemini 3 Pro를 바탕으로 한다고 적혀 있다. 입력 컨텍스트 128K, 출력 64K도 두 모델이 같다. 입력은 오디오와 이미지, 영상, 텍스트를 함께 받고 출력은 오디오와 텍스트로 나간다.

그러니 "Built for scale and cost efficiency"를 더 작은 모델을 썼다는 말로 읽기는 어렵다. 같은 바탕 위에서 추론을 얼마나 돌리느냐를 다르게 설정한 두 개의 모드에 가깝다. 뒤에 나올 요금표가 이 해석을 한 번 더 받쳐 준다.

## 말하는 도중에 생각한다

Extended Thinking의 설명에서 핵심 동사는 동시성이다.

> 3.8 Live Extended Thinking reasons and speaks simultaneously.

기존 음성 에이전트가 어려워하던 대목이 여기다. 깊게 생각하려면 시간이 필요한데, 그 시간 동안 통화가 비면 사용자는 연결이 끊겼다고 여긴다. 발표문은 두 가지 처방을 내놓았다. 하나는 <em>early verbal cues</em>다. "Let me check that…" 같은 말을 먼저 꺼내 요청을 받았다는 신호를 준다. 다른 하나는 <em>live progress narration</em>이다. 여러 단계짜리 작업이 뒤에서 도는 동안 진행 상황을 말로 중계한다.

3.8 Live 쪽에도 비슷한 장치가 있다. 도구와 API 호출을 배경에서 실행하면서 대화를 계속 이어 간다고 적혀 있다. 요청을 접수했다고 먼저 대답한 뒤 작업이 끝나기를 기다리며 다른 이야기를 할 수 있다는 뜻이다.

같은 문제를 [OpenAI의 GPT-Live-1](/digest/gpt-live-1-voice-guide/)은 다른 방식으로 풀었다. 그쪽은 무거운 추론을 음성 모델에서 떼어 내 뒤에 있는 별도의 텍스트 모델에 넘긴다. 위임(delegation)이라 부르는 구조다. 구글은 모델을 나누는 대신 같은 모델 안에서 추론과 발화를 겹쳐 돌린다. 겉으로 보이는 사용자 경험은 닮았는데, 요금이 매겨지는 자리는 그만큼 달라진다.

시각 입력도 함께 소개됐다. 3.8 Live는 시각 입력을 거의 실시간으로 처리하고, 대화 중간에 언어가 바뀌면 **97개 언어** 사이에서 자동으로 알아차려 전환한다고 적혀 있다.

이 숫자는 한 번 확인하고 넘어갈 만하다. 같은 날 Gemini Live API 개요 문서를 열어 보면 다국어 지원 항목이 **70개 언어**로 적혀 있다. 발표문의 97과 문서의 70이 어긋난다. 발표가 문서보다 앞서 나갔거나, 자동 감지가 가능한 언어와 대화를 지원하는 언어를 따로 세었을 수 있다. 어느 쪽인지는 공개된 두 문서만으로 가려지지 않는다.[^1]

## 벤치마크가 말하는 것과 말하지 않는 것

발표문이 제시한 수치를 한자리에 모으면 이렇다.

| 항목 | 모델 | 수치 |
| --- | --- | --- |
| Artificial Analysis Speech to Speech Quality Index | 3.8 Live Extended Thinking | 82.6 (전체 1위) |
| Big Bench Audio | 3.8 Live Extended Thinking | 97.7% |
| τ-Voice (에이전트 과제 완수) | 3.8 Live Extended Thinking | 68.6% |
| τ-Voice-banking (Sierra) | 3.8 Live Extended Thinking | 35.1% |
| Speech Agent Arena | 3.8 Live | 2위 |
| ServiceNow EVA-Bench | 두 모델 | 파레토 프런티어 확장 |

순위만 옮기면 압도적으로 들린다. 원 리더보드를 열어 보면 그림이 조금 다르다.

### 1위와 2위 사이의 거리

Artificial Analysis가 매기는 Speech to Speech Index는 단일 시험이 아니다. Speech Reasoning, Agentic Performance, Arena Preference, Task Success Rate 네 항목의 가중 평균이다. 2026년 9월 16일 기준 상위 세 자리는 이렇다.[^2]

| 순위 | 모델 | Speech to Speech Index | τ-Voice |
| --- | --- | --- | --- |
| 1 | Gemini 3.8 Live Extended Thinking (High) | 82.6 | 68.6% |
| 2 | GPT-Live-1 (Astra, medium), OpenAI | 81.5 | 67.9% |
| 3 | Grok Voice Think Fast 2.0 (High), xAI | 81.3 | 56.5% |

1위와 2위의 간격이 1.1점이다. τ-Voice로 좁히면 0.7%포인트까지 줄어든다. 3위까지 세 모델이 2점 안에 들어와 있으니, 지금의 선두는 굳어진 격차보다 스냅숏에 가깝다. Sierra가 공개한 τ-Voice 진척 기록을 보면 이 분야가 얼마나 빨리 움직이는지가 보인다. 2025년 8월 `gpt-realtime-1.0`이 30%였고 2026년 4월 `grok-voice-think-fast-1.0`이 67%였다. 여덟 달 만에 두 배가 됐다.

### 2위라는 표현 뒤에 있는 것

3.8 Live가 가져간 Speech Agent Arena 2위도 뜯어볼 만하다. Arena는 사람이 두 응답을 비교해 고르는 선호 기반 Elo다. 현재 상위 세 자리가 모두 구글 모델이다.

| 순위 | 모델 | Elo | 과제 성공률 |
| --- | --- | --- | --- |
| 1 | Gemini 3.1 Flash Live Minimal | 1096 | 74.6% |
| 2 | Gemini 3.8 Live | 1083 | 93.2% |
| 3 | Gemini 3.1 Flash Live High | 1063 | 71.8% |

2위가 1위보다 과제 성공률이 18.6%포인트 높다. 사람들이 더 자주 고른 쪽과 일을 더 잘 끝낸 쪽이 서로 다르다는 뜻이다. Arena 순위를 성능 순위로 읽으면 이 지점을 놓친다. 발표문이 3.8 Live를 "높은 선호"라고 소개한 것은 정확한 표현이고, 그 선호가 과제 완수와 같은 방향이 아닐 수 있다는 점까지 함께 보아야 한다.

### EVA-Bench가 그리는 절충선

ServiceNow의 EVA-Bench는 이 발표에서 가장 많은 것을 알려 주는 자료인데, 발표문에는 "파레토 프런티어를 확장했다"는 한 줄로만 요약돼 있다. EVA-Bench는 여러 턴에 걸친 통화 전체를 봇 대 봇 구조로 돌려 보고 두 축으로 채점한다. 정확도에 해당하는 EVA-A와 대화 경험에 해당하는 EVA-X다. 과제 완수는 EVA-A 안의 하위 항목이고, EVA-X는 턴 주고받기와 간결함, 대화 진행으로 구성된다.

| 모델 | EVA-A pass@1 (정확도) | 과제 완수 | EVA-X pass@1 (경험) |
| --- | --- | --- | --- |
| Gemini 3.8 Live | 0.46 | 0.71 | **0.89** |
| Gemini 3.8 Live Extended Thinking (High) | **0.55** | **0.87** | 0.74 |

두 줄이 정확히 엇갈린다. 3.8 Live는 EVA-X 0.89와 턴 주고받기 0.97로 스무 개 시스템 가운데 두 항목 모두 1위다. 대화가 가장 매끄럽다는 뜻이다. Extended Thinking은 정확도와 과제 완수에서 앞서고 경험 점수를 내준다. 생각하는 시간이 대화의 리듬을 건드린다는 이야기가 숫자로 나타난 셈이다.

리더보드에 붙은 한 문장이 전체 수준을 정직하게 요약한다. 세 가지 구조를 아우르는 스무 개 시스템 가운데 **두 축 모두에서 0.6을 넘긴 시스템은 아직 없다**는 것이다. 어느 회사의 발표문을 읽든 이 선을 기억해 두면 좋다.

EVA-Bench 항목에는 작은 글씨로 단서도 붙어 있다.

> Note: This was run on the Live API on Gemini Enterprise Agent Platform.

같은 모델이라도 원시 API가 아닌 엔터프라이즈 플랫폼 위에서 측정한 값이라는 뜻이다. 직접 재현해 볼 사람이라면 이 한 줄을 먼저 보아야 한다.

### 은행 업무판의 35.1%

τ-Voice는 Sierra가 만든 벤치마크로, 텍스트판 τ-bench의 고객 응대 과제 278건을 그대로 가져와 실제 통화 환경에서 돌린다. 소음과 전화망 압축, 프레임 손실, 억양이 섞인 음성까지 얹어 두었다. 은행 업무판은 여기에 banking 도메인을 붙인 것이다.

같은 모델이 τ-Voice에서 68.6%를 받고 은행 업무판에서는 35.1%로 내려앉는다. 발표문은 두 숫자 모두에 "leads"를 붙였고 상대 순위로는 맞는 말이다. 그렇지만 35.1%는 창구에서 시키는 일 열 가지 가운데 여섯 가지 이상을 아직 끝내지 못한다는 뜻이기도 하다. 1위라는 표현과 절대 수준을 겹쳐 읽어야 오해가 없다.

덧붙이면, 이 은행 업무판 수치는 구글 발표문 바깥의 1차 자료에서 확인하지 못했다. Sierra 쪽 리더보드는 스크립트로 그려지는 표라서 정적 추출로는 숫자가 잡히지 않는다. 35.1%는 구글이 제시한 값으로 읽어 두는 편이 정확하다.

## 요금표를 펴 보면

가장 눈에 띄는 대목이 여기다. Gemini API 가격 페이지는 `gemini-3.8-live`와 `gemini-3.8-live-extended-thinking`, 그리고 `gemini-3.1-flash-live-preview`까지 **세 모델을 한 칸에 묶어** 같은 단가를 매긴다.

| 구분 | 무료 등급 | 유료 등급 (100만 토큰 기준) |
| --- | --- | --- |
| 입력 | 무료 | 텍스트 0.75달러 / 오디오 3.00달러(분당 0.005달러) / 이미지와 영상 1.00달러(분당 0.002달러) |
| 출력 (추론 토큰 포함) | 무료 | 텍스트 4.50달러 / 오디오 12.00달러(분당 0.018달러) |
| Google 검색 그라운딩 | 지원 | 월 5,000회 무료(Gemini 3.x 전 모델 공유), 이후 1,000회당 14달러 |

출력 칸의 괄호가 중요하다. <em>including thinking tokens</em>. 추론 토큰이 별도 요율을 갖지 않고 텍스트 출력 단가에 함께 들어간다. 그러니 Extended Thinking이 비싸지는 이유는 단가 쪽에 있지 않다. 토큰을 더 많이 만들어 내기 때문이다. 한 번 생각할 때마다 100만 토큰당 4.50달러짜리 텍스트 출력이 쌓인다.

분당 환산값은 구글이 표에 직접 적어 두었다. 오디오 1초가 25토큰이라는 계산에서 나온 값이다. 1분이면 1,500토큰이고, 입력은 100만 토큰당 3.00달러이므로 분당 0.0045달러, 출력은 12.00달러이므로 분당 0.018달러가 된다.

### 한 시간 통화를 계산해 보면

사용자가 20분 말하고 모델이 20분 말하고 20분은 서로 조용한 한 시간짜리 통화를 가정한다. 아래 수치는 모두 내가 세운 가정이며 공식 예시가 아니다.

- 입력 오디오 20분 = 30,000토큰 → 0.09달러
- 출력 오디오 20분 = 30,000토큰 → 0.36달러
- 합계 **0.45달러** (약 604원)

여기에 조건 하나를 더 얹어야 한다. Live API는 상태를 유지하는 WebSocket 위에서 16kHz PCM 스트림을 계속 받는다. 클라이언트가 마이크를 열어 둔 채 침묵 구간까지 그대로 흘려보내면 그 침묵도 입력 오디오 토큰이 된다고 보는 편이 자연스럽다. 가격 문서가 이 대목을 따로 적어 두지는 않았으니 내 읽기다. 침묵 20분까지 입력에 포함하면 이렇게 바뀐다.

- 입력 오디오 60분 = 90,000토큰 → 0.27달러
- 출력 오디오 20분 = 30,000토큰 → 0.36달러
- 합계 **0.63달러** (약 846원)

Extended Thinking을 쓴다면 추론 토큰이 더 붙는다. 한 시간 동안 60번 생각하고 한 번에 800토큰을 쓴다고 하면 48,000토큰이고, 텍스트 출력 4.50달러 기준으로 0.22달러다. 위 계산에 더하면 0.85달러 남짓이 된다.

### 시계로 재는 쪽과 말로 재는 쪽

같은 값을 [GPT-Live-1](/digest/gpt-live-1-voice-guide/)의 요금표에 대 보면 두 회사가 무엇을 팔고 있는지가 드러난다. OpenAI는 세션이 열려 있던 **시간**으로 매긴다. 분당 0.05달러이고, 누가 말하든 아무도 말하지 않든 똑같다. 한 시간이면 음성 레이어만 3.00달러다.

| 항목 | Gemini 3.8 Live | GPT-Live-1 |
| --- | --- | --- |
| 과금 단위 | 오디오 토큰 (초당 25토큰) | 세션 벽시계 시간 |
| 1시간 음성 레이어 | 약 0.45에서 0.63달러 (위 가정 기준) | 3.00달러 (가정 불필요) |
| 침묵 | 스트림을 보낸 만큼 입력으로 계산 | 100% 그대로 과금 |
| 추론 비용 | 같은 모델의 출력 토큰에 합산 | 백엔드 모델 요금으로 분리 |
| 검색 | 1,000회당 14달러 (월 5,000회 무료) | 1,000회당 10달러 |

아끼는 방향이 반대로 갈린다. GPT-Live에서는 통화를 빨리 끝낼수록 싸진다. Gemini에서는 마이크와 스피커가 실제로 소리를 실어 나른 양을 줄일수록 싸진다. 전자는 대화 설계를 짧게 만들라 하고, 후자는 클라이언트에서 무음 구간을 잘라 보내라고 한다. 같은 기능을 사는 것 같아도 최적화 담당자가 손대야 할 곳이 다르다.

내 계산은 가정 위에 서 있으니 제삼자 측정치와 나란히 두는 편이 낫겠다. Artificial Analysis는 Big Bench Audio를 돌리며 입력 오디오 한 시간당 실제 비용을 함께 잰다. 2026년 9월 16일 기준 값이다.[^2]

| 모델 | 입력 오디오 시간당 비용 |
| --- | --- |
| Gemini 3.8 Live | 0.84달러 |
| Gemini 3.8 Live Extended Thinking (High) | 3.50달러 |
| Grok Voice Think Fast 2.0 (High) | 4.80달러 |
| GPT-Live-1 (Astra, medium) | 5.83달러 |

같은 과제를 풀게 했을 때 3.8 Live는 GPT-Live-1의 7분의 1 남짓이고, Extended Thinking을 켜면 그 값이 네 배로 뛴다. 요금표에서 한 칸을 나눠 쓰는 두 모델의 실제 청구액이 네 배로 벌어진다. 앞에서 이야기한 추론 토큰이 여기서 측정치로 나타난다.

무료 등급이 열려 있다는 점도 적어 둘 만하다. 두 모델 모두 무료 등급에서 요금 없이 쓸 수 있고, 대신 입력이 제품 개선에 쓰인다고 명시돼 있다.

## 모델 카드에서 더 확인되는 것들

발표문에 없고 모델 카드에만 있는 항목이 몇 가지 있다.

**지식 컷오프가 2025년 1월이다.** 2026년 9월에 나온 모델치고 스무 달 가까이 뒤처진 시점이다. 고객 응대처럼 도구로 사실을 가져오는 용도라면 문제가 적지만, 모델의 내장 지식에 기대는 대화라면 이 선을 넘는 질문에서 어긋난 답이 나온다.

**프런티어 안전 평가는 대리 평가다.** 카드는 Gemini 3.7 Flash를 평가해 어떤 Tracked/Critical Capability Level에도 닿지 않았음을 확인했고, 3.8 Live와 Extended Thinking이 3.7 Flash에 견줘 의미 있는 새 능력이나 실질적 성능 증가를 갖지 않으므로 같은 결론을 적용한다고 적었다. 앞서 모델 의존성 항목이 Gemini 3 Pro를 가리켰던 것과 나란히 놓으면 두 기준선이 서로 다르다. 카드 본문만으로는 이 차이가 해소되지 않는다.

**알려진 한계**로는 환각과 함께 간헐적인 지연이나 타임아웃이 명시돼 있다. 실시간 음성 제품에서 타임아웃은 곧 통화 중단이므로, 파일럿 단계에서 재접속 처리를 먼저 설계해 두는 편이 안전하다.

**SynthID 워터마킹**은 생성된 모든 오디오에 들어간다. 사람 귀에 들리지 않는 형태로 출력에 섞여 들어가 AI가 만든 음성임을 판별할 수 있게 한다.

## 어디서 쓸 수 있는가

두 모델의 배포 경로가 조금 다르다.

| 대상 | Gemini 3.8 Live | 3.8 Live Extended Thinking |
| --- | --- | --- |
| 개발자 | Gemini API, Google AI Studio | Gemini API, Google AI Studio |
| 기업 | Gemini Enterprise 비공개 프리뷰, Gemini Enterprise for CX 예정 | 위와 같음, 여기에 Workspace 기업 고객 예정 |
| 일반 사용자 | Search Live | Gemini Live, 그리고 Workspace의 Docs(AI Pro와 Ultra 구독자), Gmail과 Keep(전 구독자) |

일반 사용자 칸이 갈리는 모습이 이 발표의 성격을 잘 보여 준다. 검색 안에서 짧게 주고받는 자리에는 3.8 Live가 들어가고, 문서를 고치거나 메일을 정리하는 자리에는 Extended Thinking이 들어간다. 한 번에 끝나는 질문과 여러 단계를 밟아야 하는 작업을 다른 모드에 맡긴 것이다.

개발자 쪽에서는 Live API를 감싼 플랫폼들이 함께 소개됐다. Agora, Fishjam, LangChain, LiveKit, Pipecat, Vercel, Vision Agents가 이름을 올렸다. 실시간 미디어 스트리밍 기반을 대신 맡아 준다는 설명이다. 기업 사례로는 Salesforce, Genspark, Lumeris가 본문에 언급됐고 ServiceNow, Lenskart, Ambr AI, Casuu 등의 인용이 이미지로 붙어 있다.

## 가장 흥미로운 지점

이름이 만들어 내는 기대와 요금표가 보여 주는 실제가 어긋난 자리가 오래 남았다.

"3.8 Live"와 "3.8 Live Extended Thinking"이라는 이름을 나란히 보면 자연스럽게 체급 차이를 떠올리게 된다. 작은 모델과 큰 모델, 싼 쪽과 비싼 쪽. 지난 몇 해 동안 모델 이름이 대개 그렇게 붙었으니 익숙한 독법이다. 그런데 모델 카드는 둘 다 Gemini 3 Pro 위에 있다고 적었고, 가격표는 둘을 한 칸에 넣어 같은 단가를 매겼다. 남는 차이는 크기보다 생각을 얼마나 오래 굴리느냐다.

EVA-Bench의 두 줄이 그 차이의 값을 보여 준다. 3.8 Live는 대화 경험에서 스무 개 시스템 가운데 1위를 하고 정확도를 0.46에 두었다. Extended Thinking은 정확도를 0.55로 올리고 경험을 0.74로 내려놓았다. 생각을 더 오래 굴리면 답이 좋아지고 통화가 덜 매끄러워진다. 구글이 모델을 둘로 나눈 이유가 여기 있다. 하나의 모델로 두 지점을 동시에 잡지 못하니, 고객이 어느 쪽을 원하는지를 고르게 한 것이다.

이 변화가 실무에 옮겨지는 방식이 흥미롭다. 예전에는 모델을 고르는 일이 예산을 정하는 일이었다. 작은 모델을 고르면 그 순간 단가가 정해졌다. 이제는 모델을 고르는 일이 예산의 상한을 정해 주지 못한다. 같은 단가 위에서 추론 토큰이 얼마나 쌓이는지에 따라 청구서가 달라지고, 그 양은 사용자가 어떤 질문을 하느냐에 달려 있다. 비용 예측의 무게 중심이 선택에서 사용량 쪽으로 옮겨 간다.

음성이라는 매체가 여기에 한 겹을 더 얹는다. 텍스트 대화에서는 모델이 오래 생각해도 사용자가 화면을 보며 기다린다. 통화에서는 그 몇 초가 침묵이 되고, 침묵은 상대가 사라졌다는 신호로 읽힌다. 그런 까닭에 구글은 생각하는 동안 말을 시켰다. "Let me check that…"이라는 한 마디는 사용자를 붙잡아 두려고 넣은 장치인데, 요금표 위에서 보면 그것도 출력 토큰이다. 기다림을 견디게 만드는 말에도 값이 매겨진다. 잘 기다려 주는 모델과 잘 기다리게 만드는 모델 모두, 그 시간을 무엇으로 채우느냐에서 원가가 나온다.

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

[^1]: Gemini Live API 개요 문서의 Multilingual support 항목은 "Converse in 70 supported languages"로 적혀 있다. 2026년 9월 16일 확인.

[^2]: Artificial Analysis Speech to Speech 리더보드, 2026년 9월 16일 확인. Speech Agent Arena 순위는 같은 사이트의 별도 페이지에서 가져왔다. τ-Voice-banking 은행 업무판 수치는 이 리더보드에 실려 있지 않아 구글 발표문의 값을 그대로 옮겼다.
