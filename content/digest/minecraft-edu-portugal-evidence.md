---
title: "포르투갈의 마인크래프트 코딩 수업, 어디까지가 사실인가"
date: 2026-05-24T18:30:00+09:00
tags: ["사회·노동", "Minecraft Education", "코딩 교육", "포르투갈", "교육 효과 연구", "RCT"]
categories: ["다이제스트"]
summary: "한 트윗이 '포르투갈이 마인크래프트를 정규 코딩 수업으로 도입했다'고 화제가 되었다. 실제 운영 구조와 수업 내용, 교육 효과 연구의 근거를 짚어 본다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/minecraft-edu-portugal-evidence/challenge-presentation.png"
images:
  - "/images/minecraft-edu-portugal-evidence/challenge-presentation.png"
---

## 3줄 요약

1. "포르투갈이 노잼 코딩 수업을 다 집어치우고 마인크래프트를 정규 수업으로 도입했다"는 트윗이 화제다. 실제는 마데이라 자치주(RAM)·아조레스 중심의 *지역 단위* 도입에 가깝고, 컴퓨터과학(`Ciências da Computação`)의 의무교육 편입은 2025년 *검토* 단계다.
2. 마인크래프트 에듀케이션의 정식 커리큘럼은 K-12를 가로지르는 4단계·약 200시간 분량의 CS Progression이다. **Code Builder의 Agent**라는 로봇 NPC를 통해 블록 코딩 → JavaScript → Python으로 자연스럽게 전환되고, College Board가 인정한 AP CSP **Endorsed Provider**이기도 하다.
3. 효과 연구는 공간 추론·수학 자기효능감 등에서 긍정 결과가 누적되었으나, 2025년 systematic review는 29개 연구 모두 편향 위험이 중·고 수준이라 평가했다. 문제해결력에서 *유의차 없음* 보고도 존재한다.

![Minecraft School Challenge 발표 장면](/images/minecraft-edu-portugal-evidence/challenge-presentation.png "출처: kingwest0219의 트윗 첨부 사진")

## 트윗이 주장한 것 vs 실제

원 트윗은 "아들 피셜, 국내 도입이 시급한 수업"이라는 톤으로 다음을 주장했다. 각 항목을 확인해 본다.

| 트윗 주장 | 판정 | 실제 |
|---|---|---|
| 포르투갈 학교들이 *전국적으로* 정규 코딩 수업 도입 | 부분 사실·과장 | 마데이라 자치주(RAM)·아조레스 중심의 지역 도입. 24개 학교 파일럿 단계 |
| "Minecraft School Challenge" 프로그램 존재 | 부분 사실 | 정확한 명칭은 **LGW Minecraft eSports Challenge**. Microsoft Portugal × Visionarium 주최, Lisboa Games Week 2023, 8개 학교 5\~7학년 참여 |
| 레노버(Lenovo)가 지원 | 미확인 | 포르투갈 챌린지에서 Lenovo 후원 흔적 없음. 실제 운영은 Microsoft Portugal + Visionarium + Happy Code |
| 마크 안에서 파이썬 같은 실무 코딩 학습 | 사실 | Code Builder/MakeCode가 블록 → Python·JavaScript 전환을 지원. GameCode 커리큘럼은 AP CSP **Endorsed Provider** |
| Minecraft Education이 글로벌 학교 IT 표준 | 과장 | 115개국 보급은 사실, 다만 "표준"은 합의 없음. 다수 국가에서 *보조 도구*로 채택 |
| "집중력 미친 듯이 떡상", "문제 해결 능력 만렙" | 부분 사실 | 공간 추론·수학 자기효능감에 긍정 보고, 다만 systematic review의 편향 위험 평가가 높음 |

요컨대 *방향*은 맞지만 *규모와 주체*가 과장되어 있다.

## 실제 프로그램은 어떻게 구성되어 있는가

### 운영 주체와 대상

- **운영 주체**: Microsoft Portugal + Visionarium(2018년부터의 파트너) + 지역 교육청(마데이라 DRE, 아조레스 DRAE). Happy Code가 코딩 트레이너 역할.
- **대상**: 주로 1·2·3기 기초교육(초·중학교). 5\~7학년이 중심이고, 마데이라는 1·2 ciclo 전반에 걸쳐 있다.
- **수업 형태**: 정보통신기술(TIC) + `Ciências da Computação` 정규 수업 *안의 보조 도구* / 방과 후 워크숍 / e스포츠 형식의 대회.

![학생들이 컴퓨터실에서 수업을 듣는 모습](/images/minecraft-edu-portugal-evidence/classroom.png)

## 교육 내용 — 무엇을 어떻게 가르치는가

추상적인 "절차·반복·조건"이 아니라, 실제 커리큘럼과 수업 도구를 들여다본다.

### 학년별 CS Progression — 4단계 약 200시간

마인크래프트 에듀케이션의 공식 K-12 컴퓨터과학 커리큘럼은 학년대를 가로지르는 4단계로 구성되어 있다.

| 학년 | 모듈 | 시간 | 개념 |
|---|---|---|---|
| **K-2** | *Storytelling in Minecraft* (12강) + *Computing with Minecraft* (16강) | \~43h | 시퀀싱, 단순 반복, 디버깅. 블록 코딩 중심. |
| **3-5** | *Coding Fundamentals* Part 1·2·3 (24강) + *Artificial Intelligence* (8강) | \~40h+ | 변수, 좌표, 함수, 조건문, 패턴 인식. |
| **6-8** | *Coding with Minecraft* Part 1·2 (10강) | \~21h+ | 블록에서 **Python으로 전환**. 중첩 루프, 복합 조건, 의사코드, 팀 프로젝트. |
| **9-12** | *Python 101* (17강) | \~24h | Notebooks 스타일 IDE에서 순수 Python. CSTA 3A 표준 정렬. |

별도로 **GameCode**라는 5일 워크숍 코스가 있다. 10세 이상 대상이고, 파쿠르·Obby 같은 아케이드 미니게임을 학생이 *직접 만드는* 모듈식 코스다. CSTA·ISTE·영국 Computing PoS·호주 F-10에 모두 정렬되어 있다.

중학교 표준 코스 *Intro to CS with MakeCode for Minecraft*의 10단원은 다음과 같다.

> Introduction → Events → Coordinates → Variables → Iteration → Conditionals → Functions and Parameters → Arrays → AI → Final Project

대학교 1학년 CS 입문 강좌의 축소판 같은 구성이다. 차이는 모든 개념이 게임 안의 *동작*으로 즉각 시각화된다는 점뿐이다.

### Code Builder와 Agent — 코드가 게임을 움직이는 구조

게임 안에서 키보드 `C` 키를 누르면 **Code Builder** 인터페이스가 열린다. 학생은 블록·JavaScript·Python을 자유롭게 전환하며 같은 동작을 표현할 수 있다.

코드는 **Agent**라는 작은 로봇 NPC가 실행한다. 채팅창에 명령어를 입력하면 등록된 함수가 트리거되어 Agent가 코드대로 움직인다. 즉 `player.onChat("build", function() {...})` 같은 *이벤트 핸들러* 개념이 게임 플레이에 자연스럽게 녹아 들어간다.

다음은 *Agent Build* 튜토리얼의 Python 예시다 — Agent가 사암(sandstone) 블록을 쥐고 정사각형 벽을 쌓도록 시키는 코드다.

```python
agent.teleport_to_player()
agent.set_assist(PLACE_ON_MOVE, True)
agent.set_item(SANDSTONE, 16, 1)
agent.set_slot(1)
for i in range(4):
    agent.move(FORWARD, 3)
    if agent.detect(AgentDetection.BLOCK, FORWARD):
        agent.turn(TurnDirection.RIGHT)
        agent.move(FORWARD, 1)
    else:
        agent.turn(TurnDirection.LEFT)
```

이 한 스니펫에 변수·반복·조건문·메서드 호출·열거형 상수가 모두 들어 있다. 같은 동작을 JavaScript로 작성하면 `agent.teleportToPlayer()`, `agent.move(FORWARD, 3)` 같은 카멜케이스 표기로 바뀌고, 블록 코딩에서는 `||agent: agent move forward by 3||` 같은 직소 블록을 끼워 맞춘다. 학생은 *같은 논리의 세 표기*를 한 화면의 토글로 오갈 수 있다.

![학생들의 노트북 화면에서 마인크래프트 에듀케이션이 실행되고 있다](/images/minecraft-edu-portugal-evidence/laptops.png)

### Hour of Code — 매년 다른 스토리, 같은 개념

12월 첫째 주의 *Hour of Code* 캠페인을 위해 마인크래프트 팀은 매년 새 단원을 낸다. 1시간짜리 미니 코스인데, 매년 *스토리는 다르지만 다루는 코딩 개념은 비슷한* 구조다.

- **Tale of Two Villages (2020)** — Villager와 Illager 두 마을을 코드로 화해시키는 스토리. *시퀀스·반복·문제 분해*를 가르치면서 *편견과 다양성*에 대한 토론을 함께 진행한다.
- **TimeCraft (2021)** — 시간여행 어드벤처. 1920년대 뉴욕에서 카주 연주자에게 트럼펫을 전달하거나, 고대 주(周) 왕조에서 만리장성 건설을 돕기 위해 판다 경로를 우회시키는 식이다. *시퀀스·이벤트·루프·디버깅·문제 분해*를 다루며 7세 이상 대상, 29개 언어로 번역되었다.
- **Generation AI (2023)** — Agent와 함께 AI 발명품을 만든다. *책임 있는 AI*의 원칙(공정성·신뢰성)을 퍼즐로 풀어 본다.
- **Escape Estate / AI for Good (2025)** — 컴퓨테이셔널 사고 퍼즐과 AI 윤리.

"코딩 1시간"은 교사 입장에서 진입 장벽이 가장 낮은 단원이다. 학교 단위 도입의 첫 접점인 경우가 많다.

### 포르투갈 특수 미션 — *Missão Minecraft: Heróis do Oceano* (2025)

올해 여름 포르투갈에서 진행된 정식 명칭은 *Missão Minecraft: Heróis do Oceano*(바다의 영웅들)다. 트윗이 언급한 "마크 수업"의 가장 최근 사례다.

- **주최**: Microsoft Portugal × Oceanário de Lisboa × Happy Code Portugal
- **장소·기간**: Microsoft Portugal 사옥 내 *Dream Space*. 2025년 9월 10일까지 매주 수요일
- **대상·규모**: 6\~12세 약 500명. Oceanário 여름캠프 *Férias Debaixo de Água* 프로그램의 일환
- **도구**: Minecraft Education + **MakeCode Arcade**. 해양 생태계 보전을 주제로 한 프로그래밍 워크숍
- **역량 목표**: 프로그래밍 + 창의성·협업·문제 해결·디지털 시민성·환경 책임 의식

> "프로그래밍 교육은 의식 있고 창의적이며 세상을 바꿀 수 있는 시민을 길러내는 강력한 도구가 될 수 있다."
> — João Luís Sousa, Happy Code 지역 책임자

다만 공개된 보도자료는 *프로그램 골격*만 다루고, 게임 안에서 학생이 어떤 퀘스트를 어떤 순서로 풀어 나가는지의 *내부 구조*는 공개하지 않는다. Happy Code 트레이너가 MakeCode Arcade와 Minecraft Education을 어떤 비율로 섞는지도 비공개다.

### AP CSP Endorsed Provider — "정렬" 이상의 의미

마인크래프트 에듀케이션 + Microsoft MakeCode는 College Board의 **AP CSP Endorsed Provider**다. 이는 마케팅 레이블이 아니라 *College Board AP Course Audit에서 사전 승인된 syllabus*를 학교가 그대로 채택할 수 있다는 뜻이다. 별도 syllabus 작성 부담 없이 AP CSP 정식 코스를 개설할 수 있다.

AP CSP는 다섯 개의 Big Idea로 구성되고, 시험 비중은 다음과 같다.

- Creative Development 10\~13%
- **Data 17\~22%**
- **Algorithms & Programming 30\~35%**
- Computing Systems & Networks 11\~15%
- Impact of Computing 21\~26%

마인크래프트 커리큘럼의 매핑은 실질적이다.

- **GameCode** — Big Idea 1(Creative Development)과 Big Idea 3(Algorithms & Programming, 특히 iteration·selection·procedural abstraction)에 집중.
- **6\~8학년 *Coding with Minecraft*** — CSTA 2-AP-10(flowchart/pseudocode), 2-AP-12(중첩 루프·복합 조건), 2-AP-13(문제 분해), 2-AP-17(테스트 범위) 매핑.
- **9\~12학년 *Python 101*** — CSTA 3A-AP-13 등 고교 표준에 정렬, AP CSP Big Idea 3의 변수(AAP-1.A)·알고리즘 표현(AAP-2.A)·절차적 추상화(AAP-3.B/C)에 직접 대응.

쉽게 말해 학생이 마크 안에서 Agent에게 사암 벽을 쌓으라고 코드를 짜는 동안, 미국 대학과목 선이수제(AP) 컴퓨터과학 코스의 출제 범위가 *그대로 다뤄지고 있다*는 것이다.

## 교육 효과 연구는 어디까지 입증되었는가

수업 내용은 풍부하지만, "그래서 정말 효과가 있느냐"는 별도 질문이다. 통제된 연구만이 답할 수 있다.

### 긍정 보고 — 단편 RCT와 준실험

- **Slattery et al. 2024 (ScienceDirect)** — 5학년 대상 RCT. 마인크래프트 기반 학습이 *공간 추론* 점수에서 유의미한 향상을 보였다.
- **QUT DMRC 2019** — 호주 Queensland 6개교 307명. 수학 자기효능감(self-efficacy)이 통제군 대비 상승.
- **말레이시아 Year 5 연구** — HOTS(Higher Order Thinking Skills)·수학 성취에서 긍정 효과.
- **IPAS 준실험(2022)** — 협업·창의성 지표에서 유의미한 차이.

### 한계 — 2025년 systematic review의 평가

가장 신경 써서 읽어야 할 자료는 Slattery et al.의 2025년 systematic review다(*Review of Education*). 마인크래프트를 활용한 디지털 게임 기반 학습(DGBL) 연구 29편을 모두 검토했고, 결론은 신중했다.

> 29개 연구 모두 편향 위험(risk of bias) 중·고 평가. 효과의 방향성은 일관되게 긍정이지만, 표본 크기·블라인딩·교사 효과 통제 등에서 약한 설계가 다수. 효과 재현(replication)이 필요하다.

요컨대 "효과 있다"는 신호는 있지만 "확실히 있다"고 말할 만큼의 근거는 아직 부족하다.

### 반대 결과 — 문제해결력에서 유의차 없음

- **터키 IJTES 2022** — 7학년 대상 *Minecraft EDU + Python* 수업. 코딩 태도·문제해결력에서 통제군과 유의미한 차이를 발견하지 못했다.

이 결과는 "마크가 만능"이라는 주장과 정면으로 충돌한다. *어떤* 효과는 있지만 *모든* 효과가 자동으로 따라오지는 않는다는 뜻이다.

### 무엇이 결정적 변수일까

연구들이 공통으로 짚는 요인은 세 가지다.

1. **교사의 설계 역량** — 마크를 *틀어주는 것*과 *수업으로 빚는 것*은 다르다. 효과를 본 연구는 대부분 교사 연수가 동반되었다.
2. **퀘스트·맵의 정합성** — 학습 목표와 게임 내 활동이 맞아떨어져야 한다. 자유 모드 자체로는 학습 효과를 보장하지 못한다.
3. **시간 — 단발성이 아닌 누적** — 한두 차시로는 변화가 적다. 한 학기 이상 누적되어야 자기효능감·공간 추론 같은 지표가 움직인다.

## 가장 흥미로운 지점

흥미로운 지점은 "트윗이 과장이었다"가 아니다. **잘 설계된 커리큘럼이 효과까지 자동으로 보장하지는 않는다**는 사실이다.

마인크래프트 에듀케이션의 커리큘럼 자체는 정교하다. K-12를 가로지르는 200시간 분량, College Board의 공식 인정, 매년 갱신되는 Hour of Code, Agent를 통한 블록↔Python 전환 등 — 자료를 들여다보면 "이 정도면 어디서 누가 써도 효과가 있어야 하는 것 아닌가" 싶다.

그런데도 Slattery 2025가 29편을 모두 "편향 위험 중·고"로 묶은 이유는 분명하다. 학생이 좋아하고, 교사가 흥미를 느끼고, 운영 기업(Microsoft)이 자료를 풍부히 제공하는 모든 좋은 조건이 *오히려* 단편 연구의 효과 크기를 과대 측정하게 만든다. 교사의 열정, 신기성 효과, 통제군의 박탈감 같은 변수가 한 방향으로 작용하기 때문이다.

도구는 이미 만들어져 있다. 결국 효과를 가르는 것은 *그 도구를 누가 어떻게 쓰는가*다. 트윗의 톤은 "찐 코딩 교육 갓겜"으로 끝났지만, 자료가 알려 주는 결론은 더 검소하다. *맞는 방향이지만, 도구가 아니라 설계가 답이다.*

## 출처

- 원 트윗: <https://x.com/kingwest0219/status/2058481459611246766>
- 마인크래프트 에듀케이션 CS Progression: <https://education.minecraft.net/en-us/blog/new-coding-progression>
- *Intro to CS with MakeCode for Minecraft* 10단원: <https://minecraft.makecode.com/courses/csintro>
- *Agent Build* Python 튜토리얼: <https://minecraft.makecode.com/tutorials/python/agent-build>
- GameCode 5일 워크숍 코스: <https://education.minecraft.net/en-us/resources/game-code>
- *TimeCraft* (Hour of Code 2021): <https://www.minecraft.net/en-us/article/save-future-through-timecraft>
- *Missão Minecraft: Heróis do Oceano* (Microsoft Portugal 보도자료): <https://news.cision.com/pt/microsoft-portugal/i/minecraft-education-ao-servico-da-protecao-do-oceano--microsoft-portugal--oceanario-de-lisboa-e-happ,c-1589110020>
- AP CSP Endorsed Providers: <https://apcentral.collegeboard.org/courses/ap-computer-science-principles/classroom-resources/curricula-pedagogical-support>
- 마데이라 DRE × Microsoft 도입 보도: <https://www.madeira.gov.pt/draescolar/pesquisar/ctl/ReadInformcao/mid/2173/InformacaoId/148624>
- LGW Minecraft eSports Challenge 2023: <https://freguesias.dnoticias.pt/escola-do-estreito-de-camara-de-lobos-vence-lgw-minecraft-esports-challenge/>
- 포르투갈 컴퓨터과학 의무교육 편입 검토(Observador 2024-11-21): <https://observador.pt/2024/11/21/ciencias-da-computacao-pode-entrar-no-ensino-obrigatorio-em-2025-diz-associacao/>
- Slattery et al. 2025 systematic review (*Review of Education*): <https://doras.dcu.ie/30744/1/Review%20of%20Education%20-%202025%20-%20Slattery%20-%20Assessing%20the%20benefits%20of%20digital%20game%E2%80%90based%20learning%20with%20Minecraft%20in%20children%20.pdf>
- Minecraft EDU + Python 코딩 효과 연구 (터키 IJTES 2022): <https://dergipark.org.tr/en/pub/goputeb/issue/76483/1242871>
