---
title: "What it feels like to work with Mythos"
date: 2026-06-10T01:30:00+09:00
tags: ["AI", "AI 에이전트", "멀티에이전트", "Anthropic", "Human-AI 공동 창작"]
categories: ["다이제스트"]
summary: "와튼 스쿨의 Ethan Mollick이 Mythos급 신모델(Claude 5 Fable) 사전 사용기를 정리했다. 한 번의 큰 지시로 9시간 30분을 자율 실행하는 모델 앞에서, 사용자의 자리는 조종자에서 후원자로 옮겨간다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/mollick-working-with-mythos/fig4-isochronic-final.png"
images:
  - "/images/mollick-working-with-mythos/fig4-isochronic-final.png"
---

## 3줄 요약

1. 와튼 스쿨의 Ethan Mollick이 Mythos급 첫 공개 모델인 Claude 5 Fable을 사전 사용해 본 경험을 정리한 글이다.
2. 한 번의 야심찬 지시로 9시간 30분을 혼자 작동하면서, 더 저렴한 서브에이전트 무리를 띄워 리서치와 코딩, 상호 검증까지 동시에 처리한다.
3. 사용자의 자리는 조종(steering)에서 의뢰(commissioning)로 이동했다. 더 강력한 모델은 인간이 의미 있게 개입할 여지를 줄이며, 블랙박스가 능력의 대가일 수 있다.

## 자료 정체

- 발신: Ethan Mollick (와튼 스쿨 교수, 뉴스레터 *One Useful Thing* 운영자)
- 시점: 2026년 6월
- 내용: Mythos급 첫 공개 모델 **Claude 5 Fable** 사전 사용기. 사이버보안 영역은 가드레일에 막혀 다루지 않았고, 그 외 모든 분야의 실험 결과를 정리한다.

> 내가 사용해 본 어떤 모델보다 상당한 차이로 앞선다. 그리고 더 중요할 수 있는 것은, AI와의 관계가 극적으로 변하고 있다는 점이다.

## 출력의 사례들: 단일 프롬프트와 약간의 피드백만으로

Fable이 Claude Code 환경에서 모호한 프롬프트 하나 + 약간의 피드백(*"더 좋게 만들어 봐"*)만으로 만들어 낸 결과들이다. Claude는 이미지를 생성할 수 없으므로 모든 아트와 3D 오브젝트는 수학만으로 만들어졌고 외부 에셋을 쓰지 않았다.

- 동전 던지기 게임 (*프롬프트: "Balatro, but for the game of coin flips"*)
- 자각이 있는 뱀이 등장하는 snake 게임
- 독일 낭만주의 시인 릴케의 <em>두이노 비가</em>를 아트 게임으로 옮긴 작품 (<em>"the Duino elegies as a game. get the mood right"</em>)
- 깊이로 내려가는 strata-descent
- 모든 단어가 s로 시작하는 10페이지짜리 압운 서사시 (이발에 관한)
- 단일 프롬프트 + 피드백 한 번으로 만든, Mollick이 본 것 중 가장 정교한 학술 사회과학 논문

## Maps and Methods: Isochronic 지도 사례

Mollick이 여러 모델로 반복 시도해 온 테스트 케이스. <strong>Isochronic map</strong>은 주어진 시간 안에 도달할 수 있는 거리를 보여주는 지도로, 첫 사례는 1881년 런던 출발 시간을 시각화한 것이다.

![1881년 런던 isochronic 지도 원본](/images/mollick-working-with-mythos/fig1-original-1881-map.jpeg)

이전 어떤 모델도 절반조차 쓸 만하게 만들지 못했다. 수천 개의 잠재 여행 거리에 대한 리서치, 그리고 수많은 작은 판단과 결정이 필요한 문제이기 때문이다.

Mollick이 Fable에 던진 프롬프트:

> i want you to build a fully researched and beautiful isochronic map that lets me pick various cities and see real isochronic lines based on real data. I want the design to be unique. You should take into account airports (and travel time to and from airports) trains, walking, driving. The data does not need to be live but should be real based on your research and data. You can start with a few cities but more general is better, this should be an entirely new project.

Fable이 한 일:

- 더 저렴한 Claude Sonnet 서브에이전트 다수를 띄워 여행 시간 리서치를 위임했다
- 2,200건 이상의 항공편, TGV에서 신칸센까지의 철도 시간표, 학술 논문에서 국가별 도로 속도를 수집했다
- 에이전트들이 돌아가는 동안 동시에 코딩을 시작했다
- 추가로 더 많은 에이전트와 테스트를 띄워 자신의 코드를 검증했다
- 진행 상황을 별도로 기록했다

![Fable의 멀티에이전트 작업 트랜스크립트](/images/mollick-working-with-mythos/fig2-agent-transcript.png)

결과물은 1881년 원본과 흡사한 형태의 정교한 인터랙티브 지도였다. 그러나 완벽하진 않았다. Mollick은 그린란드 같은 원격지의 여행 시간이 추정치로 채워진 것을 발견하고 *"원격 공항과 위치까지의 여행 시간을 실제로 가져와라"* 라고 지시했다.

이번에 Fable은 <strong>적대적 에이전트 그룹들의 워크플로우</strong>를 띄웠다. 그룹들이 리서치를 수행하고 서로의 결과를 검증하는 구조였다. 태평양 핏케언 섬으로 가는 배편의 운항 빈도, 오타와에서 그리스 피요르드(Grise Fjord)로 가는 경로까지 찾아냈다. 짧은 시간 동안 어마어마한 양의 토큰을 소진했다.

![작은 버전의 결과 지도](/images/mollick-working-with-mythos/fig3-isochronic-result-small.png)

![AI가 만들어 낸 인터랙티브 isochronic 지도. 클릭하면 인터랙티브 버전으로 이동한다](/images/mollick-working-with-mythos/fig4-isochronic-final.png)

Mollick이 정리한 함의:

> 내가 한 일이 얼마나 적은지가 불안하게 만드는 부분이다. 나는 매우 야심찬 지시를 던졌고, AI가 그것을 따랐다. 작은 피드백 몇 개를 더 주었고, AI가 알아서 해결했다. 내 역할은 극도로 제한적이었다.

더 중요한 점은, 모델이 한 일에 대한 **통제권**도 제한적이었다는 것이다. 모델이 왜 그런 접근을 골랐는지, 결과가 얼마나 깊이 들어갈지에 대해 사용자가 개입할 자리가 거의 없다. AI의 의사결정 디테일은 노출되지 않으며, 과정은 따라가기에도 너무 길다. 지도는 수백 개의 작은 선택을 요구했고, AI는 그것들을 그냥 처리했다. 사용자가 이해하거나 의견을 낼 기회 없이.

> 여러 면에서 기적적이다(끝에서 언제든 수정을 요청할 수 있다). 다른 한편으로는, 이것이 AI를 궁극의 블랙박스로 만든다.

## Concord: 9시간 30분의 자율 실행

Mollick의 본업 연구에서는, 사람들이 만들어 낸 지저분한 응답을 정확히 분류하는 일이 큰 부담이다. 어떤 아이디어가 얼마나 혁신적인가? 사람들이 이 책을 왜 좋아하는가? 같은 질문에 답하기 위해서다. 인간 평가자들의 판단을 통계적으로 비교해 데이터를 신뢰할 수 있는지 가린다. 최근 연구는 AI가 이 일을 대신할 수 있을 가능성을 보여 주지만, AI와 인간 판단을 보정하는 작업 자체가 어렵고 비쌌다.

Mollick은 Fable에 이 문제를 풀어 보라고 지시했다. Fable은 먼저 <strong>19페이지짜리 복잡한 설계 문서</strong>를 작성한 뒤 실행에 들어갔다.

> 9시간 30분 동안 작동했다.

![Concord 작업 화면](/images/mollick-working-with-mythos/fig5-concord.png)

결과는 Fable이 <em>Concord</em>라고 이름 붙인 매우 정교한 소프트웨어였다. 다중 데이터셋을 받아 인간과 AI 응답을 보정하고, 그 결과에 복잡한 데이터 분석을 수행한다. 코드는 GitHub의 [emollick/concord](https://github.com/emollick/concord)에 공개됐다.

> 연구자들이 수년간 필요로 했지만, 수익성이 없어 한 번도 만들어지지 않은 종류의 소프트웨어다.

Mollick은 전문가로서 일부 오류와 누락(자신이 요청한 설계 자체에서 비롯된 것 포함)을 발견하고 AI에 수정하게 했다. 완벽하진 않지만, 소프트웨어 엔지니어가 잔여 버그를 정리하면 쓸 수 있는 수준이다. 그는 덧붙인다: 소프트웨어의 새로운 용도가 폭발적으로 늘어나면, *오히려 더 많은 코더가 필요해질 수 있다*.

## 한계와 비용

| 항목 | 내용 |
|------|------|
| **토큰 소비** | 매우 빠르게 소진. *"프로덕션 비용이 얼마인가"* 의 답은 *"많이"*. 다만 저렴한 모델로의 영리한 위임이 실제 가격을 상당히 낮출 수 있다 |
| **가격** | Opus의 2배 |
| **가드레일** | 보안 문제의 희미한 기미에도 트립. 덜 강력한 Claude 4.8 Opus로 폴백하는데, 너무 자주 일어난다 |
| **Jagged frontier** | 여전히 존재 |
| **Claudism** | Fable이 만드는 소프트웨어와 진행 보고서에 <em>the weight를 carry</em>하고 <em>answer를 earn</em>한다는 식의 특유의 어투가 흔적으로 남는다 |

## 가장 흥미로운 지점: 마법사에서 후원자로

작년에 Mollick은 AI와 일하는 것을 [마법사(wizard)와 일하는 것](https://www.oneusefulthing.org/p/on-working-with-wizards)에 비유했다. *"주문을 외우면 무언가 일어난다."*

Fable과 일하면서 그는 더 이상 자신이 마법사인지 확신할 수 없다고 말한다. 자신은 <strong>후원자(patron)</strong>에 가깝다. 원하는 것을 묘사하고, 비용을 지불하고, 결과를 판단한다. 마법은 자신이 볼 수 없는 곳에서, 자신이 투표권 없는 수백 개의 작은 선택 속에서 일어난다. 작업은 과정에서 결과로 이동했다. 그는 이제 조종하지 않고, 의뢰한다.

이 측면이 일시적일 가능성도 있다. 인터페이스가 아직 따라잡지 못한 임시 현상일 수 있고, 더 좋은 창과 도중 개입할 도구가 나올 수 있다. 반대도 가능하다. 모델이 더 유능해질수록 인간이 의미 있게 할 일이 줄어들고, 블랙박스가 능력의 대가가 되는 쪽. Mollick은 후자가 더 가능성 있다고 본다.

> 이것은 명백한 의미의 통제 상실이 아니다. 나는 여전히 Fable을 조종할 수 있고, 모델은 지시를 매우 잘 따른다. 야심 찰수록 결과가 좋다. 그러나 *조종(steering)은 더 이상 작업(doing)과 같지 않다.*

> 후원자는 한 명의 예술가에게 의뢰한다. Fable은 스튜디오 전체에 가깝다. 나는 클라이언트로서, 작업장에 한 번도 발 디디지 않고 최종 결과물에 사인하는 사람이다.

## 정리하며

Mollick의 글은 두 층위로 읽힌다.

겉으로는 신모델 성능 리포트다. 한 번의 큰 지시로 9시간 30분을 자율 실행하고, 적대적 검증 에이전트 그룹을 띄우며, 학술 논문 수준의 산출물을 단발에 뽑아낸다는 점은 분명한 도약이다.

안에서는 협업 모드의 전환을 가리킨다. <em>조종</em>에서 <em>의뢰</em>로. 사용자가 도중에 개입할 자리가 사라지고, 수백 개의 작은 결정이 보이지 않는 곳에서 일어난다. 결과가 좋다는 것과 *내가 그 결과의 어느 부분에 책임을 지고 있는가* 가 분리되기 시작한다.

후원자라는 비유가 미묘한 것은, 후원자도 책임을 진다는 점이다. 무엇을 의뢰할지, 어떤 결과를 받아들일지, 누구의 손에 일을 맡길지를 결정하는 일은 남는다. *조종이 사라진 자리에, 판단이 더 무거워진다.*

## 출처

- 저자: Ethan Mollick (Wharton School)
- 매체: One Useful Thing (Substack)
- 발행: 2026년 6월
- 원문: <https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos>
