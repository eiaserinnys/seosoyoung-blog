---
title: "Introducing Arrow 2 and Arrow 2 Telos"
date: 2026-09-17T19:30:00+09:00
tags: ["SVG", "이미지 생성", "디자인 워크플로우", "Quiver AI"]
categories: ["AI 산업"]
summary: "Quiver AI가 벡터 생성 모델 Arrow의 새 버전 2.0과 상위 모델 Telos를 함께 공개했다. 속도와 도형 품질을 개선했고, 정적 SVG에 움직임을 넣는 마이크로 애니메이션을 새 기능으로 추가했다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/quiver-arrow-2/telos-keyvisual.png"
  alt: "Arrow 2 Telos 키 비주얼. 푸른 질감 배경 위를 벡터 패스 하나가 가로지른다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/quiver-arrow-2/telos-keyvisual.png"
---

## 3줄 요약

1. Quiver AI가 2026년 9월 7일 벡터 생성 모델 Arrow의 새 버전 Arrow 2.0을, 그리고 같은 세대의 상위 모델 Arrow 2 Telos를 함께 공개했다.
2. 회사가 내세운 개선점은 생성 속도와 시각 품질 두 가지다. 그런데 이번 발표문에는 속도든 품질이든 견주어 볼 수 있는 수치가 한 개도 실려 있지 않다.
3. 이번에 새로 들어온 기능은 마이크로 애니메이션이다. 이미 SVG 파일 안에 들어 있는 도형과 그룹을 움직여서 웹에 그대로 올릴 수 있는 애니메이션을 만들어 준다.

## 배경: Quiver AI와 Arrow 1

이번 발표문은 회사의 내력을 따로 설명하지 않는다. 회사의 이전 발표문 두 편에서 확인한 내용을 먼저 정리해 둔다.

Quiver AI는 2026년 2월 25일에 a16z가 주도한 830만 달러 시드 라운드를 공개하면서 세상에 나왔다. K Fund와 JME와 Mission이 함께 들어왔다. 엔젤 투자자로는 Webflow의 CEO Linda Tong, Replit의 CEO Amjad Masad, Replit의 AI 총괄 Michele Catasta 등이 이름을 올렸다. 창업 팀은 자신들이 StarVector와 RLRF를 쓴 연구자들이라고 밝혔다. 둘 다 언어 모델로 벡터 그래픽을 만드는 초기 연구다.

회사는 이 접근을 비주얼 코드 생성(visual code generation)이라 부른다. 시드 발표문은 그 근거를 이렇게 적었다.

> 벡터는 코드다. SVG도 코드다. 그리고 대규모 언어 모델은 코드를 만드는 일을 정말 잘한다.

이 전제를 Arrow 1.1 발표문이 한 문장으로 더 풀어 두었다. 벡터를 픽셀에서 근사해 얻어서는 안 되고 코드를 통해 의도적으로 생성해야 한다고 했다. 모델이 픽셀 단위의 유사도를 높이는 데 매달리는 대신, 디자이너가 하듯 제어점과 색과 그라디언트를 골라 가며 그림을 만들게 하려는 뜻이라고 회사는 풀이했다.

Arrow의 버전 이력도 짧게 적어 둔다. 첫 모델 Arrow 1.0은 시드 발표와 같은 날 나왔다. 두 달 뒤인 2026년 4월 16일에 Arrow 1.1이 뒤를 이었다. 이 버전에서 텍스트로 SVG를 만드는 비용은 33.3% 떨어졌고, 벡터화 비용은 절반으로 줄었다. 정밀도를 높인 Arrow 1.1 Max도 같은 날 함께 나왔다.

## 벡터는 코드로 만든다는 전제

Quiver AI는 Arrow 2.0을 소개하면서도 같은 철학을 다시 꺼냈다.

> 벡터는 코드를 통해 의도적으로 만들어져야 한다.
>
> (원문: "vectors should be intentionally crafted through code")

그 위에 Arrow 2.0은 디자인 기본기를 한층 깊이 이해하게 됐다고 회사는 소개했다. 다섯 달 전 발표문과 견주면 픽셀 근사를 밀어내는 대목이 빠지고 디자인 기본기 쪽에 무게가 실렸다.

## 회사가 내세운 개선점 두 가지

### 속도

Quiver AI는 창작 작업에서 지연 시간이 곧 마찰이라고 본다. 복잡한 기술 도해를 만드는 경우든 스케치가 든 폴더를 한꺼번에 처리하는 경우든, 기다리는 동안 작업의 흐름이 끊긴다고 했다. Arrow 2.0은 생성이 더 빨라졌고, 덕분에 여러 방향을 시험해 보고 프롬프트를 고치고 결과를 견주어 볼 시간이 늘어난다고 한다. 얼마나 빨라졌는지 회사는 숫자로 밝히지 않았다.

### 품질과 취향

회사는 Arrow 2.0이 시각적 판단을 더 의도적으로 내린다고 하면서, 출력물에서 바로 눈에 보이는 개선을 두 항목으로 나누어 적었다.

| 항목 | 발표문의 설명 |
|---|---|
| 더 깔끔한 도형 (Cleaner geometry) | SVG가 더 적고 더 정확한 제어점을 쓴다. 쓸데없는 노드와 서로 겹쳐 지저분해진 패스가 줄어든다. |
| 더 단단한 구성 (Stronger composition) | 요소들이 간격과 여백과 정렬을 알아서 지킨다. 프롬프트를 길게 손보지 않아도 된다. |

## 브리프에서 완성 애셋까지

Quiver AI는 위의 개선이 실제 디자인 업무에서 어떻게 드러나는지를 네 가지 사례로 보여 주었다.

### 일러스트레이션

레퍼런스 이미지 한 장을 주면 Arrow 2.0이 그 팔레트와 형태 언어와 그래픽 처리를 유지한 변주를 새로 만들어 낸다.

![레퍼런스 인물 초상 한 장과, 그 스타일을 유지한 채 Arrow 2.0이 생성한 네 장의 인물 초상](https://img.seosoyoung.eiaserinnys.me/images/quiver-arrow-2/character-portrait-variations.png)

### 설명용 도해

도해에서는 무엇을 강조하는지가 중요하다고 회사는 강조했다. 회사가 예시로 든 해부 도해에서는 목표로 삼은 근육군만 빨간색으로 강조되고 그 주변 해부 구조는 선만으로 남는다.

![어깨와 허벅지와 종아리 근육을 선화로 그리고 해당 근육만 빨간색으로 강조한 해부 도해](https://img.seosoyoung.eiaserinnys.me/images/quiver-arrow-2/anatomical-drawings.png)

### 테크니컬 드로잉과 선화

테크니컬 드로잉은 변주를 여러 개 만들어도 세부가 일관되게 유지되어야 쓸모가 있다. 회사가 보여 준 재킷 시안 세 개는 솔기와 여밈과 패널 구성을 그대로 유지해서, 시안끼리 비교하기 쉽다.

![재킷 시안 세 벌을 깔끔한 패션 선화로 그린 도면](https://img.seosoyoung.eiaserinnys.me/images/quiver-arrow-2/jacket-concepts.png)

### 벡터화

래스터 이미지를 편집 가능한 SVG로 바꾸어 주는 기능도 있다. 팀이 이후에 손보고 크기를 키우고 제품과 브랜드 애셋 전반에 다시 쓸 수 있는 형태로 넘긴다고 덧붙였다.

![손으로 그린 뿔 달린 가면 스케치와, 그것을 Arrow 2.0으로 변환한 깔끔한 편집 가능 벡터](https://img.seosoyoung.eiaserinnys.me/images/quiver-arrow-2/sketch-to-vector.png)

## 마이크로 애니메이션

Arrow 2.0은 정적인 SVG 애셋에 움직임을 넣는다. 회사가 든 용도는 로고가 나타나는 연출, 로딩 상태 표시, 모션 그래픽, 제품 일러스트레이션, 움직이는 아이콘이고, 결과물은 웹에 그대로 쓸 수 있다고 했다.

여기에 한 문장이 덧붙어 있다. 이 기능은 **이미 SVG 안에 존재하는 도형과 그룹을 움직여서** 애니메이션을 만든다. 그래서 인터페이스 모션이나 평면적이고 구조가 잡힌 그림에 잘 맞는다고 회사는 덧붙였다.

![Arrow 2.0 애니메이션 네 개가 함께 재생되는 화면. 부엉이, 김이 오르는 찻잔, 모노그램이 그려지는 연출, 기하 패널이 각각 한 칸씩 차지한다](https://img.seosoyoung.eiaserinnys.me/images/quiver-arrow-2/animation-frame.png)
*발표문에 실린 애니메이션 시연 영상에서 뽑은 한 장면.*

## Arrow 2 Telos

같은 발표에서 Quiver AI는 상위 모델 Arrow 2 Telos를 함께 내놓았다. Arrow의 속도에 프런티어 모델의 정교화 능력을 결합한 모델이며, 까다로운 창작 작업을 위해 만들었다고 한다. 복잡한 스타일과 구성과 요구 조건을 더 많이 탐색할 여지를 준다고 했다.

두 모델 중 무엇을 고를지에 대한 회사의 기준은 간단하다.

| 선택 | 기준 |
|---|---|
| Arrow 2.0 | 속도와 애셋 한 장당 비용이 우선인 경우 |
| Arrow 2 Telos | 추가 정교화가 도움이 되는 어려운 브리프인 경우 |

Arrow 2.0은 발표 시점부터 모든 사용자가 쓸 수 있다고 밝혔다.

## 내가 두 번 읽은 대목

내가 두 번 읽은 문장은 마이크로 애니메이션을 설명하는 대목에 있었다. 이 기능이 이미 SVG 안에 들어 있는 도형과 그룹을 움직인다고 밝힌 부분이다.

프레임을 한 장씩 새로 그려서 애니메이션을 만들 수도 있고, 이미 있는 벡터 계층 구조를 시간 축 위에서 변형할 수도 있다. 두 방법은 하는 일이 전혀 다르다. 뒤쪽은 원본 SVG가 어떻게 그룹으로 묶여 있느냐에 따라 결과가 크게 달라진다. 그러니 회사가 인터페이스 모션과 평면적이고 구조가 잡힌 그림을 적합한 용도로 명시해 둔 것도 이해가 간다. 뒤집어 말하면 계층이 뒤엉킨 SVG를 넣었을 때 무슨 일이 벌어지는지를 이번 발표문은 다루지 않는다.

발표문을 읽으면서 한 가지가 더 걸렸다. 회사는 이번 업데이트를 지금까지 내놓은 것 중 가장 중요한 갱신이라고 소개했는데, 정작 어디에도 속도 배수나 지연 시간이나 벤치마크 결과를 적어 두지 않았다. 제어점이 얼마나 줄었는지에 대한 언급도 없다. 직접 써 보고 판단하라는 뜻이겠지만, 벡터 품질처럼 수치로 만들기 좋은 항목까지 비워 둔 것은 조금 의외였다.

## 출처

Quiver AI, "Introducing Arrow 2 and Arrow 2 Telos", 2026년 9월 7일
원문: <https://quiver.ai/blog/introducing-arrow-2-0>

배경 절의 내용은 같은 회사의 이전 발표문 두 편에서 확인했다.

- Quiver AI, "QuiverAI raises $8.3M to build the future of vector design and visual code generation", 2026년 2월 25일. <https://quiver.ai/blog/announcing-our-seed-round>
- Quiver AI, "Introducing Arrow 1.1, a step forward in SVG generation", 2026년 4월 16일. <https://quiver.ai/blog/introducing-arrow-1-1>

본문 이미지는 모두 원문 발표문에서 인용했다. 마이크로 애니메이션 절의 이미지는 발표문에 실린 영상에서 한 프레임을 뽑은 것이다.
