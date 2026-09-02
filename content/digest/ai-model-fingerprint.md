---
title: "AI 모델 랜덤 넘버 지문 데이터셋"
date: 2026-07-03T07:30:00+09:00
tags: ["AI", "LLM", "LLM 평가", "벤치마크", "해석가능성", "Anthropic"]
categories: ["모델과 연구"]
summary: "1부터 355 사이의 랜덤한 수를 뽑으라는 프롬프트를 대량 반복시켜 얻은 통계 분포로 24개 AI 모델의 지문을 만들고, 그 지문으로 제3자 API 중계의 모델 위조까지 잡아낸 실측 데이터셋."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/ai-model-fingerprint/overview.png"
  alt: "24개 모델 지문 종합 개요"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/ai-model-fingerprint/overview.png"
---

## 3줄 요약

1. GitHub 사용자 `qqqqqf-q`가 2026년 6월 말부터 7월 초 사이에 공개한 오픈소스 리포. OpenRouter로 상용·오픈 모델 24개에 「1부터 355 사이의 수를 하나 무작위로 골라라」라는 프롬프트를 각각 300회씩 던져, 응답 분포를 지문 벡터로 뽑아 두었다. 원안은 [hlwy-ai-checker](https://github.com/hanlinwenyuan/hlwy-ai-checker)에서 착안했다.
2. 대형 언어모델은 진짜 난수 생성기가 아니다. 학습 데이터·아키텍처·RLHF·토크나이저 차이가 응답 분포에 남는다. 지문은 시스템 프롬프트로 잘 덮이지 않고, 같은 세대 내에서는 놀랄 만큼 안정적이며, 세대·후훈련 경계에서는 극적으로 갈린다.
3. 지문은 상용 모델의 세대 관계를 되짚는 도구가 되기도 하고, 제3자 API 중계상이 광고와 다른 모델을 서빙하는 위조(掺假)를 잡아내는 실용적 감사 수단이 되기도 한다.

## 원리 — 왜 지문이 남는가

LLM에게 랜덤한 수를 하나 뽑아 달라고 하면, 그 답은 진짜 균등분포에서 오는 게 아니라 학습된 잠재 분포에서 온다. 같은 프롬프트·같은 파라미터(고정 문장, `temperature=1.0`)로 수백 번 반복하면 모델마다 특정 숫자에 몰리는 경향이 드러난다. 학습 데이터·아키텍처·RLHF·토크나이저가 다르면 그 경향도 달라진다. 이 분포 벡터를 지문으로 삼는다. 지문은 시스템 프롬프트로 잘 덮이지 않아, 제3자 API가 광고와 다른 모델을 몰래 서빙하는 위조(掺假, 찬자)를 검출하는 데도 쓸 수 있다.

## 채집 방법

- OpenRouter API를 경유해 24개 모델에 접근한다. README에는 17개 모델이 적혀 있지만, 커밋 이력을 따라가면 sonnet-5, seed-2.0-mini, gemini-3-flash-preview, gemini-3.5-flash, claude-fable-5까지 순차로 확장됐다.
- 모델당 유효 샘플 약 300개. minimax 계열은 후처리로 622개까지 복구한다.
- 프롬프트는 고정, `max_tokens=32`. 대부분 모델은 `reasoning.enabled=false`로 추론을 끈다. `grok-build-0.1`과 `kimi-k2.7-code`는 추론 강제 모델이라 `max_tokens=2048`로 늘려 잡는다.
- 매 요청마다 raw response body, `system_fingerprint`, `usage`(비용 포함), 요청 파라미터, latency, http_status를 그대로 JSONL로 남긴다. 재현이 최우선이다.
- 중단 재개, 병렬, 429 백오프 재시도까지 구현되어 있다.

전체 채집 비용은 대략 $1.03로 저렴하다. grok의 강제 reasoning이 요청당 637 output 토큰을 쓰면서 비용의 대부분을 차지한다.

## 데이터 구조

| 경로 | 내용 |
|---|---|
| `data/raw_*.jsonl` | 모델별 원 요청·응답 전량. 요청 1개당 한 줄, response body 통째로. |
| `data/summary.json` | 지문 벡터 + 통계량 + 17×17(현재는 24×24) 유사도 매트릭스 + 전체 숫자 시퀀스 |
| `figures/` | 분포·통계량·유사도 히트맵·박스플롯·종합 overview 시각화 |

24개 모델의 raw JSONL이 각각 500KB에서 2MB 사이. `data/summary.json`이 지문 분석의 정본이다.

## 실측 모델 (24개)

Claude 계열: opus 4.6 / 4.7 / 4.8, sonnet 4.6 / 5, haiku 4.5, claude-fable-5.
OpenAI 계열: gpt-5.5 / 5.4 / 4o-mini.
Google Gemini: gemini-3-flash-preview / gemini-3.5-flash.
DeepSeek: v3.2 / v4-flash / v4-pro.
Moonshot Kimi: k2.6 / k2.7-code.
Qwen: 3.6-plus / 3.7-plus / 3.7-max.
그 외: minimax-m3, glm-5.2(z-ai), grok-build-0.1(x-ai), seed-2.0-mini(bytedance).

opus 4.6·4.7·4.8 계열은 이미 지난 두어 세대의 상용 라인이고, sonnet-5·claude-fable-5까지 포함돼 있어 채집 시점 기준으로 최신에 가까운 스냅샷이다.

![코사인 유사도 매트릭스](https://img.seosoyoung.eiaserinnys.me/images/ai-model-fingerprint/similarity_cosine.png)

## 핵심 발견

### Claude opus 4.6 ≈ 4.7이지만 4.8은 완전히 다르다

- opus 4.6과 4.7의 지문 코사인 유사도는 **0.997**. 사실상 같은 모델이거나, 같은 base에서 아주 얕게 후훈련한 사이로 보인다.
- 반면 opus 4.8은 완전히 다른 지문을 갖는다. 코사인은 **약 0.04**. 게다가 `unique=2`. 300번 요청에 응답이 사실상 하나(거의 237)로 붕괴해 있다. 준고정 출력이다.

세대 안에서는 정렬 목표를 크게 바꾸지 않고, 세대 경계에서 정렬·디코딩·프롬프트 처리가 뒤집혔다는 뜻으로 읽힌다. 특히 4.8의 붕괴는 정상적인 랜덤 요청 분포가 아니라 특정 응답으로 캘리브레이션된 결과에 가깝다.

### Kimi k2.6 → k2.7-code: 후훈련 한 번이면 지문이 갈린다

- k2.6과 k2.7-code는 같은 base에서 k2.7이 코드 후훈련을 얹은 관계. 유사도는 **0.631**.
- 같은 base라도 후훈련 한 라운드로 지문이 상당 폭 이동한다는 실증. 후훈련의 지문 변화량을 정량으로 볼 수 있는 몇 안 되는 데이터다.

### DeepSeek 동일 스택, 다른 코퍼스

- v3.2 / v4-flash / v4-pro는 서로 코사인이 **0.15에서 0.31 사이**. 같은 회사·아키텍처 계열이라도 학습 코퍼스와 사이즈가 다르면 지문은 크게 달라진다.

### 크로스 벤더 유사도 — 정렬 가족이 벤더 가족보다 크다

- haiku 4.5 ≈ sonnet 4.6: 코사인 **0.997**. 같은 회사의 다른 크기 라인이지만, 지문이 사실상 같은 판에 앉는다.
- kimi k2.7-code ≈ glm-5.2: 코사인 **0.916**. 서로 다른 회사·서로 다른 언어권의 모델이 비슷한 지문을 낸다.

리포 저자는 커밋 메시지에서 이 관찰을 「정렬 가족(alignment family)이 벤더 가족(vendor family)보다 크다」로 요약한다. gemini도 같은 회사의 두 라인이 각각 다른 어트랙터 족에 붙는다. gemini-3-flash-preview는 217 족 언저리, gemini-3.5-flash는 247 족 언저리다.

![217 어트랙터 족](https://img.seosoyoung.eiaserinnys.me/images/ai-model-fingerprint/attractor_217.png)

### 217 어트랙터 족과 247 어트랙터 족

- 24개 모델의 응답 분포에서 두 개의 큰 어트랙터가 관찰된다. 하나는 217 부근에 몰리는 무리, 다른 하나는 247 부근에 몰리는 무리.
- 벤더가 아니라 정렬·후훈련 결이 어느 족에 붙는지를 결정한다. 위의 gemini 관찰이 그 예.

![24개 모델 박스플롯](https://img.seosoyoung.eiaserinnys.me/images/ai-model-fingerprint/boxplot.png)

박스플롯은 각 모델의 응답 분포 폭·중앙값·이상치를 한눈에 보여준다. opus 4.8이 사실상 한 점에 붕괴한 반면, 대부분의 모델은 넓게 퍼진 분포에 여전히 어트랙터를 갖는다는 대조가 잘 드러난다.

## 응용 — 제3자 API 위조 탐지

- 저자는 dasuapi라는 제3자 중계상에서 「claude-opus-4-6」이라고 라벨링해 서빙하는 API를 함께 지문 채집했다.
- 그 API의 지문과 공식 opus 4.6의 지문 코사인은 **0.207**. 사실상 다른 모델이다.
- 이 대체품의 mode는 187 (공식 opus-4.6는 217 어트랙터). 24개 실측 모델 중 가장 유사한 지문은 **gemini-3.5-flash (0.700)**. 즉 광고와 다르게 gemini 계열로 추정되는 모델을 서빙하고 있을 가능성이 높다.

![dasuapi 위조 탐지 결과](https://img.seosoyoung.eiaserinnys.me/images/ai-model-fingerprint/dasuapi_verification.png)

7월 1일 커밋 `f0906c5`에서 저자는 dasuapi 데이터를 지문 대조군에서 배제하고 raw만 로컬에 남겼다. 공개 리포에는 위조 탐지 원리와 그림만 남아 있다. 이 응용 자체가 흥미로운 것은, 지문 벡터만으로 라벨 검증이 가능하다는 실증이 이만큼 저렴하고 재현 가능하게 나온 사례가 드물다는 점이다.

## 복원 방법

리포는 몇 줄로 재현 절차를 제시한다.

```bash
pip install -r requirements.txt
cp config.example.yaml config.yaml   # OpenRouter 키 입력
python run.py --samples 300          # 채집
python check_data.py                 # 무결성 검증
python analyze.py                    # 통계 + 시각화
python estimate.py                   # 토큰·비용 예측
```

OpenRouter 계정과 대략 $1 정도의 예산이면 24개 모델 지문을 처음부터 다시 뜰 수 있다.

## 가장 흥미로운 지점

나를 가장 오래 붙잡은 것은 opus 4.8이 `unique=2`로 붕괴한 대목이다. 300번 요청에 실제 서로 다른 응답이 두 종류밖에 없고, 그중 거의 전량이 237이다. 「1부터 355 사이의 수를 무작위로 골라라」에 이렇게 뾰족한 응답이 나올 이유는 랜덤 샘플링 파라미터로는 설명되지 않는다. 정렬·디코딩 어딘가에서 특정 응답으로 캘리브레이션되었거나, 이 프롬프트 클래스에 특화된 규정 응답이 들어갔거나, 랜덤 요청 자체를 특정 카노니컬 응답으로 흡수하도록 훈련됐다는 가설이 나올 수 있다.

두 번째는 「정렬 가족이 벤더 가족보다 크다」는 관찰이다. 우리가 관습적으로 모델을 「Anthropic 계열」, 「OpenAI 계열」, 「Google 계열」로 묶어 생각하지만, 지문 지표에서는 그 계열보다 정렬·후훈련의 결이 더 강한 클러스터 축이 된다. Anthropic의 haiku와 sonnet이 같은 판 위에 있고, Moonshot의 kimi와 Zhipu의 glm이 같은 판 위에 있다. 이건 오픈 웨이트 생태계와 상용 정렬 파이프라인의 상호 참조가 우리 예상보다 훨씬 넓다는 신호다.

## 출처

저자: GitHub 사용자 [`qqqqqf-q`](https://github.com/qqqqqf-q)
프로젝트: [`ai-model-fingerprint`](https://github.com/qqqqqf-q/ai-model-fingerprint)
원안 참조: [`hlwy-ai-checker`](https://github.com/hanlinwenyuan/hlwy-ai-checker)
공개 시점: 2026년 6월 26일 초판, 7월 초까지 지속 확장
라이선스: 명시되지 않음 (공개 리포지만 재사용 조건 불명확)
