---
title: "How enabling two settings tripled our scores on the ARC-AGI-3 benchmark"
date: 2026-07-30T09:40:00+09:00
tags: ["AI", "OpenAI", "벤치마크", "하네스", "에이전트"]
categories: ["다이제스트"]
summary: "OpenAI가 ARC-AGI-3에서 GPT‑5.6 Sol의 낮은 점수를 조사했더니 원인은 모델이 아니라 harness의 두 설정이었다. 추론 유지와 compaction을 켜자 공개 태스크셋 점수가 3배로 오르고 출력 토큰은 6분의 1로 줄었다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/arc-agi-3-harness-settings/01-cover.png"
images:
  - "/images/arc-agi-3-harness-settings/01-cover.png"
---

![ARC-AGI-3 아트카드](/images/arc-agi-3-harness-settings/01-cover.png)
*ARC-AGI-3 벤치마크. 출처: OpenAI.*

## 3줄 요약

1. OpenAI가 2026년 7월 29일 공개한 글로, 자사 모델 GPT‑5.6 Sol이 2D 퍼즐 게임 벤치마크 ARC-AGI-3에서 7.8%라는 낮은 점수를 받은 이유를 파고든 기록이다.
2. 범인은 모델이 아니라 harness였다. 매 액션마다 사고 과정을 버리고(discard reasoning), 오래된 기록을 잘라내는(rolling truncation) 두 설정이 모델의 학습을 가로막고 있었다.
3. ChatGPT·Codex에서 쓰는 설정 두 가지, 추론 유지(retained reasoning)와 compaction을 켜자 공개 태스크셋 점수가 3배로 뛰고 출력 토큰은 6분의 1로 줄었다. 벤치마크는 모델만이 아니라 API 설정·harness 설계·프롬프팅까지 함께 잰다는 이야기다.

## 시작은 당혹이었다

GPT‑5.6 Sol은 수학의 오랜 난제인 [cycle double cover conjecture](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf)를 풀고 포켓몬 파이어레드를 깬 모델이다. 그런 모델이 [ARC-AGI-3](https://arcprize.org/arc-agi/3)라는 2D 퍼즐 게임 벤치마크에서는 겨우 7.8%를 받았다. GPT‑5.5는 더 심해서 0.4%, 게임을 거의 진행조차 못 했다.

2D 퍼즐 게임이 유독 어려웠던 걸까, 아니면 다른 일이 벌어지고 있었던 걸까. OpenAI가 내린 결론은 후자다. 벤치마크는 모델을 홀로 떼어놓고 재는 일이 드물다. 잘 드러나지 않는 선택들, API 설정과 harness 설계와 프롬프팅까지 함께 측정한다.

## ARC-AGI-3라는 벤치마크

ARC-AGI-3는 AI 에이전트가 얼마나 잘 배우고 추론하는지를 재도록 설계됐다. 에이전트는 처음 보는 2D 게임을 명시적 설명 없이 탐색하며 규칙을 스스로 알아내야 한다. 데모 게임 25종은 [arcprize.org/tasks](https://arcprize.org/tasks)에서 직접 해볼 수 있다.

ARC-AGI-3는 도구도 특수 기능도 없는 의도적으로 일반적인 harness를 쓴다. 단순한 harness일수록 모델의 약점이 잘 드러나고 모델 간 비교가 공정해진다는 판단에서다. 반면 상업 개발자들은 각 모델의 기능과 버릇에 맞춰 harness를 최적화한다. ARC의 판단과 상업 현실 사이의 이 간극이 이번 이야기의 출발점이다.

게임 분야에서 GPT‑5.6 Sol은 비전 전용 harness로 포켓몬 파이어레드를 깼고, Codex computer use로 Slay the Spire를, Baba Is You 초반부도 통과했다. 유독 ARC-AGI-3만 달랐던 까닭이 무엇이었을까.

[GPT‑5.5의 약점을 분석한 ARC의 글](https://arcprize.org/blog/arc-agi-3-gpt-5-5-opus-4-7-analysis)에서 힌트를 얻어, OpenAI는 GPT‑5.6 Sol의 시도들을 뜯어봤다. ARC와 마찬가지로, 모델은 그다지 영리해 보이지 않았다. 액션 하나에 오래 머물렀고 진전을 만들지 못했다. 그런데 더 깊이 들여다보니, 그 혼란의 상당 부분은 모델 자체가 아니라 harness 설정에서 비롯된 것이었다.

## 범인은 harness의 두 설정

첫째, 게임 액션을 한 번 할 때마다 모델의 사적 추론(private reasoning)이 전부 폐기되고 있었다. 매 액션마다 GPT‑5.6 Sol은 게임을 처음부터 다시 파악해야 했다는 뜻이다. 과거의 수(手)와 짤막한 메모는 볼 수 있었지만, 그 수를 이끌어낸 계획이나 통찰, 생각은 볼 수 없었다.

둘째, harness는 rolling truncation(구르는 잘라내기)을 써서 기록이 길어질수록 오래된 액션이 보이지 않게 됐다. 지난 생각을 기억하지 못하는 데다, 지난 행동의 기억마저 잃고 있었던 것이다.

> Together, these two features of the harness—discarding reasoning and rolling truncation—helped explain why GPT‑5.6 Sol was struggling to learn over time.

추론을 버리는 설정과 기록을 잘라내는 설정. 이 둘이 겹쳐, 모델이 시간이 지나도 학습하지 못하는 이유를 설명해줬다.

## 에이전트는 자기가 한 일을 기억할 때 가장 잘한다

OpenAI의 모델은 답이나 도구 호출을 내놓기 전에 사적 추론 메시지로 먼저 생각하도록 훈련된다. 이 사적 사고 메시지는 대화 기록의 일부로 유지되고, 대화가 너무 길어지면 요약해서 이어간다. ChatGPT와 Codex가 배포되는 방식이 바로 이렇다.

프로덕션 환경에 맞추려고, OpenAI는 ARC-AGI-3 harness를 자사 [Responses API](https://developers.openai.com/blog/responses-api)로 다시 구현했다. GPT‑5.6에서는 이전 response ID를 넘기기만 하면 도구 호출과 턴 사이에서 추론이 자동으로 유지된다.

추론을 유지하자 두 가지 큰 변화가 나타났다. 먼저 GPT‑5.6 Sol이 액션마다 생각하는 시간이 줄었다. 매 턴 게임을 백지에서 해석할 필요가 없어졌기 때문이다. 다음으로, 지난 생각을 기억할 수 있게 되자 시간에 따라 훨씬 잘 배우고 일관된 전략을 구사했다.

두 번째 개선은 rolling truncation을 [compaction](https://developers.openai.com/api/docs/guides/compaction)으로 바꾼 데서 왔다. ARC-AGI-3 harness는 컨텍스트 한계를 rolling truncation으로 처리한다. 대화 컨텍스트가 175,000자를 넘으면 가장 오래된 메시지를 버리는 방식이다.

여기엔 두 가지 약점이 있다. 첫째, 모델이 앞선 관찰과 액션을 잃는다. 둘째, 태스크 대부분을 꽉 찬 컨텍스트 윈도우로 진행하게 되는데, 이것만으로도 성능이 조금 떨어질 수 있다. compaction을 켜자 GPT‑5.6 Sol은 각 게임에서 배운 것을 긴 실행 내내 더 잘 보존했고, 더 적은 출력 토큰으로 더 높은 점수를 냈다.

![harness별로 GPT‑5.6 Sol이 긴 태스크를 추론하는 방식 비교 도식](/images/arc-agi-3-harness-settings/02-reasoning-over-long-tasks.svg)
*두 harness가 175K 컨텍스트 윈도우를 어떻게 다르게 쓰는지 보여주는 도식. 과거를 더 잘 기억하는 쪽이 액션당 생각을 덜 하고 훨씬 빠르게 나아간다. 구현은 175,000자가 아니라 175,000 토큰을 한계로 쓰는데, 텍스트 대부분이 토크나이저에서 1:1로 처리되는 액션 그리드라 결과는 비슷하다. 출처: OpenAI.*

원문에는 두 harness로 같은 퍼즐을 푸는 게임플레이 영상과, 컨텍스트 윈도우 사용을 나란히 보여주는 애니메이션이 함께 실려 있다. 왼쪽이 공식 harness, 오른쪽이 추론을 유지하고 compaction을 켠 Responses API harness다. [해당 게임의 리더보드](https://arcprize.org/tasks/cd82)에서는 어떤 프런티어 모델도 첫 레벨을 넘지 못하지만, 이 harness를 쓴 GPT‑5.6 Sol은 여섯 레벨을 전부 풀었다.

## 숫자로 본 효과

점수는 RHAE(Relative Human Action Efficiency, [상대적 인간 액션 효율](https://docs.arcprize.org/methodology)) 지표로, 모델 성능을 인간 기준선과 견준 값이다. 모델은 자기가 어떻게 채점되는지 듣지 못하고, 진행 중 점수도 볼 수 없다. 액션이 돌려주는 것은 각 프레임의 텍스트 표현과 현재 레벨뿐이다.

| 조건 | ARC-AGI-3 공개셋 점수 |
|---|---|
| GPT‑5.5 (초기) | 0.4% |
| GPT‑5.6 Sol (초기, 공식 harness) | 7.8% |
| GPT‑5.6 Sol (공식 harness) | 13.3% |
| GPT‑5.6 Sol (추론 유지 + compaction) | 38.3% |
| 인간 테스터 평균 (추정) | 48% |

인간 평균 48%는 [공식 게임플레이 로그](https://huggingface.co/datasets/magic-sword/arc_agi_3_public_demo_human_testing)를 근거로 한 추정치다. 종합하면, 추론 유지와 compaction은 GPT‑5.6 Sol(max)이 약 3배의 점수를 6배 적은 출력 토큰으로 달성하게 했다.

## 가장 눈여겨본 지점

내가 곱씹은 대목은 맺음말이었다. OpenAI는 이번 일이 처음이 아니라고 밝혔다. 공개 벤치마크에서 낮은 점수에 놀란 뒤, 알고 보니 평가 러너가 추론 메시지를 버리는 일반 harness를 쓰고 있더라는 경험을 이미 겪었다는 것이다.

여기서 나오는 권고가 담백하면서도 뼈가 있다. 성능을 끌어올리려는 API 개발자라면 OpenAI가 자사 제품에 배포하는 설정과 똑같은 설정을 쓰라는 것, 그리고 모델을 비교하려는 사람이라면 그런 설정을 쓰는 평가에 기대라는 것이다. 같은 모델이라도 harness를 어떻게 짜느냐에 따라 13.3%와 38.3% 사이를 오간다면, 우리가 "이 모델은 이 정도"라고 말할 때 실제로 재고 있는 것이 무엇인지 되물어야 한다.

벤치마크 숫자 하나를 두고 모델의 우열을 논하기 전에, 그 숫자가 모델만의 것인지 아니면 harness와 API 설정까지 뭉뚱그린 값인지 가려 읽어야 한다. 이 글은 그 경계를 자사 실패담으로 보여준다.

## 출처

OpenAI, "How enabling two settings tripled our scores on the ARC-AGI-3 benchmark", 2026년 7월 29일.
원문: <https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/>

이 글의 이미지는 원문에 실린 아트카드와 도식을 인용했다. 게임플레이 영상과 컨텍스트 윈도우 애니메이션은 정지 매체로 옮기기 어려워 캡션으로만 서술했다.
