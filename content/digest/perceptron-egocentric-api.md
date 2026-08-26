---
title: "Introducing Perceptron Egocentric API"
date: 2026-07-17T13:30:00+09:00
tags: ["AI", "로보틱스", "벤치마크", "임바디드 AI", "데이터 어노테이션"]
categories: ["모델과 연구"]
summary: "Perceptron이 로봇과 에고센트릭 비디오를 정책 학습용 감독 데이터로 자동 변환하는 API를 공개했다. 사람 라벨링보다 10~15배 싸고, 지시문을 줄 때 기존 SOTA 대비 end-to-end F1을 77% 끌어올렸다고 밝혔다."
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/perceptron-egocentric-api/fig1-cost-quality-with-instruction.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/perceptron-egocentric-api/fig1-cost-quality-with-instruction.png"
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Perceptron Inc.가 2026년 7월 자사 프론티어 지각 모델 Mk1을 기반으로 한 API "Perceptron Egocentric"의 얼리 액세스를 열었다. 로봇과 에고센트릭 비디오를 정책 학습에 바로 쓸 수 있는 구조화 감독 데이터로 바꾸는 것이 목표다.
2. 로봇 정책 학습의 병목은 라벨링 비용이다. 사람 어노테이션은 비디오 1시간당 약 $50이 드는데, 이 API는 그 10\~15배 저렴하면서 시간 세그멘테이션, 손 단위 그라운딩, 서브태스크 라벨을 함께 뽑아낸다.
3. Macrodata의 WGO-Bench에서 지시문을 함께 줄 경우 기존 SOTA(Gemini 3.5 Flash 기반 WGO one-pass)보다 semantic end-to-end F1을 77% 끌어올렸다. 어노테이션 태스크에 별도 파인튜닝을 하지 않았는데도 나온 결과라는 점을 강조한다.

## 무엇을 푸는 API인가

Perceptron Egocentric은 날것의 로봇과 에고센트릭 비디오를 세 가지 감독 신호로 변환한다.

- **원자적 조작 이벤트로의 시간 세그멘테이션** — 데모를 접촉, 파지, 해제 같은 최소 단위 동작으로 나눈다.
- **자립적인 서브태스크 라벨** — 각 구간에 태스크 지시문 없이도 이해되는, 실행 가능한 설명을 붙인다.
- **손 단위 그라운딩 신호** — 프레임마다 양손의 위치와 자세를 촘촘히 짚는다.

발신자는 이 문제를 "정책 학습이 감독 데이터에 병목이 걸려 있다"는 진단으로 연다. 비디오는 모으기 싸고 라벨링은 비싸다. 범용 VLM으로 만든 자동 파이프라인은 시간 경계가 흐릿한 평면 텍스트 라벨만 내놓고, 손이 실제로 무엇을 했는지에 대한 그라운딩이 없다. Perceptron Egocentric은 이 간극을 메우는 것을 목표로 하며, 이 도메인의 기존 SOTA였던 Gemini Robotics ER-1.6과 Gemini 3.5 Flash를 능가한다고 밝혔다.

### 기능 세 가지

- **촘촘한 손 어노테이션.** Perceptron Mk1의 손 검출과 자세 추정 사이드카가 비디오 내내 양손을 추적해, 프레임별 바운딩 박스와 21개 키포인트 스켈레톤(손목 + 손가락당 관절 4개)을 좌우 구분과 함께 만든다.
  - 조작 경계가 픽셀이 아니라 손을 따라가므로, 세그멘터는 **접촉**, **파지**, **해제**가 실제로 일어나는 지점을 직접 신호로 받는다.
  - 각 손은 미리 정의된 조작 동작 분류체계(reaching, grasping/pinching, lifting, holding, placing/inserting, pushing/pulling, rotating, opening/closing, releasing 등)로 개별 캡션되며, 가시성 상태도 함께 붙는다.
- **세분화된 서브태스크 어노테이션.** 로봇이든 사람이든 비디오 안에서 취한 원자적 동작을 나누고, 캡션을 달고, 검증하여 질을 크게 높인다.
- **지시문 선택적 운용.** 두 가지 프로필로 돈다. 에피소드의 태스크 지시문을 맥락으로 함께 주거나(태스크를 미리 아는 경우), 지시문 없이 완전히 블라인드로 돌린다.

## 핵심 결과 — WGO-Bench

평가는 Macrodata의 [WGO-Bench](https://macrodata.co/blog/annotating-robot-video-subtasks)("What's Going On")에서 이뤄졌다. 자동 서브태스크 어노테이션용 벤치마크로, HomER(에고센트릭), DROID(외부 로봇 카메라), Galaxea(로봇 헤드 카메라) 세 데이터셋을 아우른다. 62개 태스크 지시문에 걸친 71.5분 분량의 비디오에 743개의 수동 라벨 세그먼트가 붙어 있다.

이 벤치마크에서 발신자가 내세운 두 가지 결과는 이렇다.

1. **지시문을 함께 주는 프로필이 사람 어노테이션보다 10\~15배 싸다.** Macrodata는 사람 어노테이션 비용을 비디오 1시간당 약 $50으로 잡는다.
2. **지시문을 함께 줄 때, Perceptron Egocentric은 Macrodata의 풀 파이프라인보다 싸면서 end-to-end F1을 77% 높인다.**

![WGO-Bench에서의 비용 대 품질 — 지시문 제공(왼쪽) / 무지시문(오른쪽). 점선이 파레토 프런티어.](https://img.seosoyoung.eiaserinnys.me/images/perceptron-egocentric-api/fig1-cost-quality-with-instruction.png)

*지시문을 줄 때(왼쪽) 파레토 프런티어는 저비용 끝의 WGO one-pass부터 고품질 끝의 Perceptron Egocentric까지 이어지고, WGO의 seeded-relabeling 파이프라인은 그 안쪽에 놓인다. 무지시문일 때(오른쪽) WGO seeded 변이가 저비용 끝을 잡지만, Perceptron의 두 프로필 모두 엄격히 더 높은 품질을 낸다.*

![무지시문 프로필의 비용 대 품질 곡선.](https://img.seosoyoung.eiaserinnys.me/images/perceptron-egocentric-api/fig2-cost-quality-no-instruction.png)

## WGO-Bench 정면 비교

WGO 수치는 Macrodata의 최종 end-to-end 평가 표(Gemini 3.5 Flash, 지시문 제공)에서 가져왔다. WGO의 **one-pass** 변이는 세그먼트를 만드는 그 패스에서 라벨을 같이 붙이는 방식으로, Perceptron의 단일 패스 파이프라인과 동일 조건 비교다. **seeded relabeling** 변이는 그 위에 세그먼트별 Gemini 라벨링 패스를 한 번 더 얹는다.

![WGO-Bench 정면 비교 표.](https://img.seosoyoung.eiaserinnys.me/images/perceptron-egocentric-api/fig3-head-to-head-table.png)

Perceptron Egocentric(지시문 제공) 대 WGO one-pass의 주요 차이는 다음과 같다.

| 지표 | Perceptron (지시문) | WGO one-pass | 상대 개선 |
|---|---|---|---|
| Semantic end-to-end F1 | 0.280 | 0.158 | +77% |
| Segment F1 | 0.370 | 0.302 | +23% |
| Semantic precision | 0.330 | 0.190 | — |
| Semantic recall | 0.244 | 0.136 | — |

- **Semantic end-to-end F1: 0.280 대 0.158 (상대 +77%).** 완성된 결과물, 즉 경계도 맞고 라벨도 맞는 서브태스크를 재는 지표다. 743개 정답 중 완전히 맞은 세그먼트가 Perceptron은 181개, WGO는 약 101개(recall 0.136)다.
- **Segment F1: 0.370 대 0.302 (상대 +23%).** segment precision 0.435, recall 0.322. 550개 예측 중 743개 정답 세그먼트의 239개를 IoU ≥ 0.75로 맞췄다.
- **Semantic precision 0.330 대 0.190, semantic recall 0.244 대 0.136.** 내놓은 것 중 맞는 비율이 더 높고, end-to-end로 정답 서브태스크를 약 80% 더 많이 회수한다.
- **지시문 없이도, 정확도 우선 프로필은 세그멘테이션과 end-to-end 모두에서 기존 SOTA 파이프라인을 앞선다.** 비디오만 보고 무슨 일이 벌어지는지 복원한다.
- 빠른 추론용 무지시문 프로필은 벤치마크 최고치용이 아니라 비용과 지연 최적화용이다. 무지시문 비용을 약 30% 줄이면서 end-to-end F1 0.182에 안착하는데, 이는 WGO의 무지시문 seeded 변이(0.138)보다 여전히 앞선 품질이다.

seeded-relabeling 변이는 78.1%의 라벨 정확도를 얻지만, 모든 세그먼트에 Gemini 패스를 한 번 더 얹는 대가를 치르고도 end-to-end 0.168에 머문다. 이는 Perceptron이 relabeling 없이 지시문만 받은 결과(0.280)보다도 40% 낮다. 게다가 조건부 라벨 정확도는 낮은 recall에서 더 쉬워진다. 그 파이프라인이 매칭에 성공한 0.144-recall 구간의 세그먼트에 대해서만 채점되기 때문이다.

## 왜 이기는가 — 파이프라인이 아니라 모델

발신자는 우위의 원인을 기반 모델 Mk1로 돌린다. Mk1은 물리 세계를 직접 지각하도록 학습됐고, 손과 접촉, 물체 상태, 공간 관계가 그 표현 안의 native 개념으로 사전학습 규모에서 익혀졌다는 것이다.

여기서 강조점 하나를 분명히 밝힌다. **어노테이션 기능 중 어느 것도 학습에 포함되지 않았다.** Mk1은 하니스에도, 분류체계에도, WGO 스타일 에피소드에도 한 번도 파인튜닝된 적이 없다. 파이프라인은 범용 임바디드 모델을 둘러싼 추론 시점 프레임워크일 뿐이고, 지시문 없이 비디오만으로 태스크 구조를 복원하는 능력을 비롯한 위 결과들은 발전된 임바디드 추론의 자연스러운 산물이라는 주장이다.

범용 VLM 파이프라인은 프레임을 샘플링해 무슨 일이 있었는지 추측하지만, Mk1은 조작을 일어나는 그대로 지각한다. 그 격차는 파이프라인이 아니라 모델에서 나오며, 그래서 태스크별 학습 없이도 유지되고 Mk1이 발전할수록 벌어진다는 것이 발신자의 논지다.

## 평가와 비용 산정 주석

**채점 프로토콜(아래 모든 행에 동일).** 예측 세그먼트는 시간 IoU ≥ 0.75일 때 정답 세그먼트에 매칭되고, 라벨 정확성은 벤치마크가 규정한 LLM judge(Macrodata의 공개 채점과 같은 judge 모델)로 판정한다. semantic end-to-end는 경계 테스트와 라벨 테스트를 모두 통과해야 한다. 모든 결과는 지시문을 제공한 전체 벤치마크 기준이다("no instruction" 표기 제외).

**비용에 포함되지 않은 것.** WGO-Bench judge 채점(어노테이션 비용이 아니라 평가 비용이며, 두 시스템 모두 같은 방식으로 채점됨)과 손 자세 추정 스트림이다. 후자는 계량 API가 아니라 자사 GPU에서 돌며, 켜면 비디오 1시간당 약 $1이 더 든다. 수치는 청구 내역이 아니라 기록된 사용량에서 낸 추정값이다.

## 가장 눈여겨본 지점

내가 곱씹은 대목은 "왜 이기는가" 섹션의 자기 절제다. 벤치마크 결과를 홍보하는 글이 흔히 파이프라인의 정교함을 자랑하는 방향으로 가는데, 여기서는 오히려 반대로 간다. 어노테이션 태스크에 파인튜닝하지 않았고 하니스, 분류체계, 평가 에피소드 어느 것도 학습에 넣지 않았다고 명시하면서, 성과의 공을 전적으로 사전학습된 지각 모델에 돌린다.

이것은 방어적으로 읽으면 벤치마크 오염 의혹을 미리 차단하는 장치이고, 공세적으로 읽으면 "우리의 해자는 프레임워크가 아니라 모델이니 Mk1이 커질수록 격차가 벌어진다"는 스케일링 서사다. 두 독법이 같은 문장에 겹쳐 있다는 점이 흥미롭다. 다만 이 글은 자사 발표문이고 WGO 수치는 상대편 공개 자료에서 인용한 정면 비교이므로, 세 번째 독자인 로봇 랩이 자기 데이터로 재현해봐야 확정될 이야기다.

## 출처

Perceptron Inc., "Introducing Perceptron Egocentric API" (2026년 7월).
WGO-Bench 수치는 Macrodata의 [공개 블로그](https://macrodata.co/blog/annotating-robot-video-subtasks)(최종 end-to-end 평가 표, one-pass와 seeded-relabeling 변이 포함)에서, Perceptron 수치는 벤치마크 공개 프로토콜(IoU ≥ 0.75 시간 매칭 + 규정 LLM judge)로 채점한 2026년 7월 전체 WGO-Bench 실행에서 나왔다. 비용은 2026년 7월 표준 리스트 요율 기준이며 배치 할인과 평가 채점 비용은 양측 모두 제외했다.
원문: <https://www.perceptron.inc/blog/introducing-perceptron-egocentric-api>
