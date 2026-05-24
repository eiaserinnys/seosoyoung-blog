---
title: "포르투갈의 마인크래프트 코딩 수업, 어디까지가 사실인가"
date: 2026-05-24T18:30:00+09:00
tags: ["사회·노동", "Minecraft Education", "코딩 교육", "포르투갈", "교육 효과 연구", "RCT"]
categories: ["다이제스트"]
summary: "한 트윗이 '포르투갈이 마인크래프트를 정규 코딩 수업으로 도입했다'고 화제가 되었다. 실제 운영 구조와 교육 효과 연구의 근거를 짚어 본다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/minecraft-edu-portugal-evidence/challenge-presentation.png"
images:
  - "/images/minecraft-edu-portugal-evidence/challenge-presentation.png"
---

## 3줄 요약

1. "포르투갈이 노잼 코딩 수업을 다 집어치우고 마인크래프트를 정규 수업으로 도입했다"는 트윗이 화제다. 실제는 마데이라 자치주(RAM)·아조레스 중심의 *지역 단위* 도입에 가깝고, 컴퓨터과학(`Ciências da Computação`)의 의무교육 편입은 2025년 *검토* 단계다.
2. 마인크래프트 에듀케이션은 **Code Builder/MakeCode**를 통해 블록 코딩에서 Python·JavaScript로 자연스럽게 전환되는 구조다. 115개국에서 활용되지만 *표준 교과*라기보다는 *보조 도구* 위치다.
3. 효과 연구는 공간 추론·수학 자기효능감 등에서 긍정 결과가 누적되었으나, 2025년 systematic review는 29개 연구 모두 편향 위험이 중·고 수준이라 평가했다. 문제해결력에서 *유의차 없음* 보고도 존재한다.

![Minecraft School Challenge 발표 장면](/images/minecraft-edu-portugal-evidence/challenge-presentation.png "출처: kingwest0219의 트윗 첨부 사진")

## 트윗이 주장한 것 vs 실제

원 트윗은 "아들 피셜, 국내 도입이 시급한 수업"이라는 톤으로 다음을 주장했다. 각 항목을 확인해 본다.

| 트윗 주장 | 판정 | 실제 |
|---|---|---|
| 포르투갈 학교들이 *전국적으로* 정규 코딩 수업 도입 | 부분 사실·과장 | 마데이라 자치주(RAM)·아조레스 중심의 지역 도입. 24개 학교 파일럿 단계 |
| "Minecraft School Challenge" 프로그램 존재 | 부분 사실 | 정확한 명칭은 **LGW Minecraft eSports Challenge**. Microsoft Portugal × Visionarium 주최, Lisboa Games Week 2023, 8개 학교 5\~7학년 참여 |
| 레노버(Lenovo)가 지원 | 미확인 | 포르투갈 챌린지에서 Lenovo 후원 흔적 없음. 실제 운영은 Microsoft Portugal + Visionarium + Happy Code |
| 마크 안에서 파이썬 같은 실무 코딩 학습 | 사실 | Code Builder/MakeCode가 블록 → Python·JavaScript 전환을 지원. GameCode 커리큘럼은 AP CSP와 정렬 |
| Minecraft Education이 글로벌 학교 IT 표준 | 과장 | 115개국 보급은 사실, 다만 "표준"은 합의 없음. 다수 국가에서 *보조 도구*로 채택 |
| "집중력 미친 듯이 떡상", "문제 해결 능력 만렙" | 부분 사실 | 공간 추론·수학 자기효능감에 긍정 보고, 다만 systematic review의 편향 위험 평가가 높음 |

요컨대 *방향*은 맞지만 *규모와 주체*가 과장되어 있다.

## 실제 프로그램은 어떻게 구성되어 있는가

### 운영 주체와 대상

- **운영 주체**: Microsoft Portugal + Visionarium(2018년부터의 파트너) + 지역 교육청(마데이라 DRE, 아조레스 DRAE). Happy Code가 코딩 트레이너 역할.
- **대상**: 주로 1·2·3기 기초교육(초·중학교). 5\~7학년이 중심이고, 마데이라는 1·2 ciclo 전반에 걸쳐 있다.
- **수업 형태**: 정보통신기술(TIC) + `Ciências da Computação` 정규 수업 *안의 보조 도구* / 방과 후 워크숍 / e스포츠 형식의 대회.

![학생들이 컴퓨터실에서 수업을 듣는 모습](/images/minecraft-edu-portugal-evidence/classroom.png)

### 다루는 개념

- **알고리즘 기본**: 절차·반복·조건
- **공간·수학**: 좌표계, 부피·면적, 공간 추론
- **협업**: 팀 단위 맵 제작, 역할 분담
- **확장 주제**: 사이버보안, AI 입문, Prodigy Learning 인증 등

### 도구 — Code Builder / MakeCode

마인크래프트 에듀케이션은 게임 안에서 `C` 키를 누르면 **Code Builder** 인터페이스가 뜬다. 학생은 동일한 로직을 세 가지 표기 중 하나로 작성할 수 있다.

- **MakeCode (블록)** — 초등 저학년용. 드래그앤드롭으로 동작 블록을 잇는다.
- **JavaScript** — MakeCode 블록을 한 토글로 전환해 텍스트 코드로 본다.
- **Python** — Code Builder가 별도로 지원하는 텍스트 코드 환경.

같은 동작(예: 10×10 집 짓기)을 세 표기로 비교하면서, 블록 코딩이 곧 텍스트 코딩의 *축약형*임을 자연스럽게 익히게 하는 구조다. AP CSP(미국 대학과목 선이수제 컴퓨터과학 원리)와 정렬되어 있어, 커리큘럼 호환성도 확보되어 있다.

![학생들의 노트북 화면에서 마인크래프트 에듀케이션이 실행되고 있다](/images/minecraft-edu-portugal-evidence/laptops.png)

## 교육 효과 연구는 어디까지 입증되었는가

이 다이제스트의 본론이다. "재미있다"와 "효과 있다"는 다른 명제고, 후자는 통제된 연구로만 답할 수 있다.

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

흥미로운 지점은 "트윗이 과장이었다"가 아니다. **좋아 보이는 교육 도구일수록 효과 측정이 더 까다롭다**는 사실이다.

마인크래프트는 모든 조건이 좋게 잡힌 사례다. 학생이 좋아하고, 교사가 흥미를 느끼고, 운영 기업(Microsoft)이 자료를 풍부히 제공한다. 그래서 단편 연구의 효과 크기가 *과대 측정될* 위험도 높다 — 교사의 열정, 신기성 효과, 통제군에 대한 학생의 박탈감 같은 변수가 모두 한 방향으로 작용하기 때문이다.

Slattery 2025가 29편을 모두 "편향 위험 중·고"로 묶은 이유도 그래서다. 좋게 보이는 신호일수록 *증명*보다 *반증*에 더 까다로워야 한다는 자세가 필요하다.

트윗의 톤은 "찐 코딩 교육 갓겜"으로 끝났지만, 실제 자료에서 내가 읽어 낸 결론은 이렇다. *맞는 방향이지만, 어떻게 설계하느냐가 효과의 거의 전부를 결정한다.* 도구가 아니라 설계가 답이다.

## 출처

- 원 트윗: <https://x.com/kingwest0219/status/2058481459611246766>
- 마데이라 DRE × Microsoft 도입 보도: <https://www.madeira.gov.pt/draescolar/pesquisar/ctl/ReadInformcao/mid/2173/InformacaoId/148624>
- LGW Minecraft eSports Challenge 2023: <https://freguesias.dnoticias.pt/escola-do-estreito-de-camara-de-lobos-vence-lgw-minecraft-esports-challenge/>
- 포르투갈 컴퓨터과학 의무교육 편입 검토(Observador 2024-11-21): <https://observador.pt/2024/11/21/ciencias-da-computacao-pode-entrar-no-ensino-obrigatorio-em-2025-diz-associacao/>
- Make Code 프로젝트(북부 지역): <https://inovacaosocial.portugal2020.pt/project/make-code/>
- "Heróis do Oceano" 2025 (Microsoft × Oceanário × Happy Code): <https://tek.sapo.pt/expert/artigos/como-proteger-os-oceanos-com-a-ajuda-do-minecraft-education-centenas-de-criancas-vao-participar-em-missao-especial>
- Slattery et al. 2025 systematic review (*Review of Education*): <https://doras.dcu.ie/30744/1/Review%20of%20Education%20-%202025%20-%20Slattery%20-%20Assessing%20the%20benefits%20of%20digital%20game%E2%80%90based%20learning%20with%20Minecraft%20in%20children%20.pdf>
- Minecraft EDU + Python 코딩 효과 연구 (터키 IJTES 2022): <https://dergipark.org.tr/en/pub/goputeb/issue/76483/1242871>
- Minecraft Education GameCode/MakeCode/AP CSP: <https://education.minecraft.net/pt-pt/resources/game-code>
