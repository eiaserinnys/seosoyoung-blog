---
title: "SpudCell — 완전한 세포주기를 처음부터 조립한 인공 세포"
date: 2026-07-02T22:00:00+09:00
tags: ["과학", "합성생물학", "세포공학", "오픈소스", "SpudCell"]
categories: ["다이제스트"]
summary: "미네소타대학 아다말라 랩이 90kbp 게놈과 36개 정제 효소, 지질막만으로 조립한 인공 세포 SpudCell이 섭식, 성장, 게놈 복제, 분열, 선택까지 완전한 세포주기를 실증했다. 라이트 형제의 첫 비행기 같은 성취라 표현되지만, 자체 리보솜을 만들지 못해 5세대에서 멈추고 진화라 부르기엔 멀다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/spudcell-first-full-cell-cycle/spudcell-6frame-biotic.jpg"
images:
  - "/images/spudcell-first-full-cell-cycle/spudcell-6frame-biotic.jpg"
---

## 3줄 요약

1. 미네소타대학 케이트 아다말라 교수 팀이 살아있는 세포를 깎아내는 대신, 정제된 화학 성분만으로 처음부터 조립한 인공 세포 **SpudCell**의 프리프린트를 2026년 7월 1일 공개했다. 오픈소스 합성생물학을 위해 새로 설립된 비영리 기관 **Biotic**의 첫 결과물이다.
2. 이 시스템은 90kbp 게놈을 7개의 플라스미드에 나눠 담고, 지질막 안에서 섭식, 성장, 게놈 복제, 분열, 선택까지 세포의 다섯 가지 핵심 행위를 하나의 사이클로 이어냈다. 상향식으로 조립한 시스템이 완전한 세포주기를 돌린 것은 처음이다.
3. 그러나 이 세포는 살아있지 않다. 리보솜을 스스로 만들지 못해 5세대에서 멈추고, 분열을 여러 번 반복하려면 사람이 기계적으로 눌러 짜야 하며, 자연 발생 돌연변이가 없어 다윈적 진화도 관찰되지 않았다. 저자들은 이를 "라이트 형제의 첫 비행기"에 비유한다.

![SpudCell이 6프레임에 걸쳐 자라고 분열하는 형광 현미경 시퀀스](/images/spudcell-first-full-cell-cycle/spudcell-6frame-biotic.jpg)
*SpudCell의 성장과 분열을 담은 형광 현미경 시퀀스 6프레임. Credit: Kate Adamala, Adamala Lab / Biotic*

## SpudCell이란 무엇인가

SpudCell은 미네소타대학 생명과학대 부교수 케이트 아다말라(Kate Adamala)와 아론 엥겔하트(Aaron Engelhart)의 연구팀이 개발한 인공 세포 시스템이다. 명칭은 아다말라의 학생들이 붙인 별명에서 왔다. 지도교수의 이름을 따 "아다말라 세포"라 부르려는 학생들에게 그는 "차라리 감자(spud)라고 불러라"라고 말했고, 스푸트니크(Sputnik)의 어감까지 겹쳐 그대로 굳었다고 [Science AAAS 인터뷰](https://www.science.org/content/article/lab-created-spudcell-marks-major-step-toward-building-life-scratch)에서 밝혔다.

이 시스템의 구성은 다음과 같다.

| 요소 | 내용 |
|---|---|
| 게놈 | 90 kbp (9만 염기쌍). 이론상 최소 게놈 크기로 추정되던 113 kbp보다 작다. |
| 게놈 분할 | 7개의 원형 DNA 플라스미드 (논문 표 S6에서는 8개로도 표기, 대다수 매체는 7개로 정리) |
| 유전자 수 | 36개. 대장균, 박테리오파지, 해파리(GFP)에서 왔다. |
| 단백질 합성 | PURE(Protein synthesis Using Recombinant Elements) 시스템 — 대장균에서 정제한 36개 효소와 리보솜의 정의된 혼합물 |
| 외피 | 지질 이중층으로 이루어진 리포솜 |

대장균 게놈이 대략 4,600 kbp임을 고려하면, SpudCell의 게놈은 그것의 약 1/50에 해당한다.

## 무엇을 실증했는가

논문 초록에 따르면 SpudCell은 다음 다섯 가지를 하나의 세포주기 안에서 시연한다.

- **섭식(feeding)** — 세포 자신의 DNA가 만든 α-헤몰라이신(α-hemolysin) 단백질이 막 관통형 pore로 자리 잡고, 그 바깥의 히스티딘 태그가 Ni-NTA 지질을 함유한 "먹이 리포솜(feeder liposome)"과 결합해 융합한다. 융합을 통해 지질, 뉴클레오티드, 아미노산, 심지어 리보솜까지 세포 내부로 넘어온다.
- **성장(growth)** — 융합이 반복되면 세포는 부피가 커지고, 새 지질이 막에 편입된다.
- **게놈 복제(genome replication)** — 파지 Phi29 DNA 중합효소가 7개 플라스미드를 모두 복제한다. 5세대 후 완전한 게놈 세트를 가진 세포는 약 30% 수준이다.
- **분열(division)** — 자연 세포는 세포골격(cytoskeleton)의 정교한 동원에 의존하지만, SpudCell은 세포골격을 완전히 우회한다. FLAG 태그를 단 대형 단백질들이 막 표면에 몰려들며 서로 반발하고, 그 기계적 응력이 막을 갈라 새 리포솜을 싹처럼 떨어뜨린다. "가장 멍청한 방법"이라고 아다말라는 Science 인터뷰에서 표현했다.
- **선택(selection)** — 융합 단백질을 더 많이 발현하도록 유전자를 조작한 변이체를 원본과 함께 배양하면, 5세대 후 변이체 게놈이 60%를 차지한다. 영양이 부족한 조건에서 격차는 더 벌어진다.

![붉은 지질 염색으로 표시한 SpudCell 단일 세포](/images/spudcell-first-full-cell-cycle/spudcell-red-newscientist.jpg)
*지질 염색을 붉은색으로 입힌 SpudCell 단일 세포. Credit: Orion Venero, Adamala Lab / New Scientist*

## 살아있지 않은 이유

New Scientist, Science AAAS, Quanta Magazine 세 매체가 공통으로 지적한 한계는 크게 세 가지다.

**첫째, 리보솜을 스스로 만들지 못한다.** 리보솜은 외부에서 공급되는 먹이 리포솜에 실려 들어온다. 세대가 반복되면 세포 안의 리보솜은 열화되고, 대략 5세대에서 10세대 사이에 세포는 활동을 멈춘다. 아다말라는 "리보솜의 실패 때문일 것으로 추정한다"고 밝혔고, 스스로 리보솜을 조립하는 능력을 갖추면 "무한 분열도 곧 도달 가능할 것"이라 [New Scientist 인터뷰](https://www.newscientist.com/article/2532689-have-scientists-really-made-a-living-cell-from-scratch-not-quite/)에서 말했다.

**둘째, 분열이 비효율적이다.** 분열은 균등하지 않다. 한 세포에서 작은 방울이 떨어지는 방식이라 딸세포에는 7개 플라스미드가 무작위로 분배된다. 5세대 후 완전한 게놈을 가진 세포는 30% 수준이며, 여러 세대에 걸쳐 분열을 유도하려면 연구자들이 세포를 미세한 구멍이 뚫린 막에 압출(extrusion)해서 물리적으로 눌러 짜야 한다.

**셋째, 다윈적 진화가 아니다.** 선택 실험에서 관찰된 우세 확산은 실제 자연선택이 아니다. 유익한 변이는 연구자가 인위적으로 게놈에 삽입했고, 분열도 기계적 개입으로 촉진되었다. Phi29 DNA 중합효소는 정확도가 지나치게 높아 의미 있는 자발적 돌연변이를 만들지 못한다. 아다말라는 이 지점을 "질서와 혼돈의 경계", 즉 스튜어트 카우프만(Stuart Kauffman)이 말한 "카오스의 가장자리(edge of chaos)"에 있는 오차율의 중합효소를 찾는 과제로 정의했다.

시카고대 잭 조스택(Jack Szostak)은 이 시스템이 "생물학적 성분으로 인공 세포를 만들려는 어떤 노력보다도 멀리 나아갔다"고 Quanta에 평가했고, 스탠퍼드대 드루 엔디(Drew Endy)는 "촉매의 순간"이라 표현했다. 반면 애리조나주립대 마이클 린치(Michael Lynch)는 "합성생물학의 걸작(tour de force)"이지만 자기유지가 아직 없다며 과대 해석을 경계했다.

## 발표 방식과 Biotic

논문 발표 경로는 학계 관례에서 크게 벗어났다. Science AAAS 보도에 따르면 논문은 원래 *Cell* 저널에 투고됐다가 한 리뷰어가 "SpudCell은 진짜 생물학이 아니다"라며 게재를 거절했고, 아다말라는 새 저널에 재투고하기 전에 190쪽 원고를 프리프린트 서버(bioRxiv)에 올리기도 전에 언론에 엠바고 배포했다. 하이델베르크대 케르스틴 괴프리히(Kerstin Göpfrich)는 이 방식을 "이례적인 진행 방법"이라 표현했다.

같은 날 아다말라와 엔디, 다른 두 연구자는 비영리 공공 이익 연구 기관 <strong>[Biotic](https://biotic.org)</strong>을 공식 출범했다. Biotic은 시드 자금 약 1천만 달러를 확보했고, 9월부터 대부분을 연구 보조금으로 분배할 예정이다. 미네소타대학이 SpudCell 특허를 소유하되 Biotic에 독점 라이선스를 부여했으며, 조직의 목표는 "합성 세포 공학을 위한 공유 기술 인프라"를 오픈소스 형태로 세계 연구자들에게 개방하는 것이다.

아다말라는 [미네소타대학 보도자료](https://twin-cities.umn.edu/news-events/worlds-first-synthetic-cell-complete-life-cycle-could-revolutionize-biological)에서 그 취지를 이렇게 요약했다.

> "공개된 형태로 구축되지 않은 인프라 기반은 결국 누군가에게 통행료를 걷을 위치를 넘겨주는 것에 지나지 않는다."

파이낸셜타임스와의 인터뷰에서 그는 산업적 지향을 이렇게 표현했다.

> "우리는 지구를 해치지 않는 방식으로, 그리고 실제로 재생 가능한 방식으로 물건을 제조할 수 있어야 한다. 지구에는 원자가 충분하며, 우리는 그 원자들을 더 지속 가능하고 분산된 방식으로 옮길 필요가 있을 뿐이다."

![연구를 이끈 케이트 아다말라](/images/spudcell-first-full-cell-cycle/adamala-portrait.webp)
*아다말라 랩을 이끄는 케이트 아다말라 부교수. 2016년 자기 연구실을 열 때부터 스스로 세포주기를 완성하는 인공 세포를 목표로 삼았다. Courtesy of Kate Adamala / Quanta Magazine*

## 산업적 지향과 안전 우려

발표 자료들이 그리는 잠재적 응용은 다음과 같다.

- **의약품 생산** — 진화가 시도한 적 없는 아미노산까지 포함하는 정밀 치료 분자
- **재료 산업** — 화석연료 없이 만드는 플라스틱, 성장시키는 재료
- **기후 대응** — 탄소 제거, 생분해성 화학물질
- **식품** — 미세 생물 공장 형태의 성분 제조

산업 화학이 요구하는 고온·고압 대신 상온의 생물학적 조건에서 분자 변환이 이뤄지는 "재배 가능한(engineerable)" 제조 플랫폼이 이들이 그리는 그림이다. 이미 인슐린이나 생분해성 플라스틱 같은 산물이 유전공학 미생물로 생산되고 있으나, 원본 세포의 대사가 낯선 화학 반응을 견디지 못하는 것이 그동안의 벽이었다. SpudCell처럼 처음부터 정의된 세포는 자연이 만든 세포가 견디지 못하는 반응을 감내하도록 설계할 여지가 있다.

동시에 우려도 있다. 연합뉴스가 정리한 바에 따르면 학계에서는 인공 세포가 유출되어 예상 밖 결과를 낳거나 생화학 무기로 오용될 가능성을 지적한다. 다만 New Scientist는 이 우려를 상대화한다. 리보솜을 스스로 만들지 못하고 실험실 밖에서 5세대만에 죽는 세포는 "숟가락으로 먹여줘야 하는 침대에 누운 프랑켄슈타인"에 가깝다. 자연에 이미 존재하는 박테리아가 훨씬 큰 위협이라는 것이 그들의 정리다.

## 남은 과제

Biotic이 후속 로드맵으로 제시한 세 가지 과제는 SpudCell이 "라이트 플라이어" 단계에서 벗어나기 위해 필요한 조건이기도 하다.

1. **자체 리보솜 조립** — 유전자 지시로부터 리보솜을 스스로 만드는 기능. 이것이 없으면 5세대에서 활동이 멈춘다.
2. **게놈 통합과 분배 개선** — 7개 플라스미드를 하나의 안정된 게놈으로 통합하고, 세포골격에 준하는 정교한 분배 기구를 갖추는 것.
3. **외부 급식 의존도 축소** — 대사 경로를 세포 내부에 심어 단순한 출발 물질에서 필요한 성분을 스스로 합성하도록 만드는 것.

아다말라의 표현을 빌리면 이 세포는 "현대 세포라는 드림라이너"에 견주면 "라이트 플라이어"에 불과하다. 그러나 [Quanta Magazine 인터뷰](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/)에서 그가 강조한 지점은 "완전한 화학 재료 목록과 청사진을 가진 첫 세포"라는 사실이다. 기존 세포를 개조해 무언가를 만들려는 연구자는 "청사진 없는 드림라이너를 받은 엔지니어"에 비유되지만, SpudCell을 다루는 연구자는 부품 하나하나까지 파악한 상태에서 개선할 수 있다.

## 가장 흥미로운 지점

내가 곱씹은 대목은 "세포골격을 우회한 분열"이었다. 자연 세포가 세포골격을 조립하는 데 수십 개의 유전자와 정교한 시공간 조정이 필요하다. 이걸 처음부터 재구성한다는 목표는 지난 십 수년간 합성생물학의 대표적 병목이었다. 아다말라 팀의 답은 우회다. 반발력을 가진 태그를 막에 잔뜩 붙여서 그 표면 응력이 막을 갈라지게 만든다는 발상이 SpudCell 세포주기의 마지막 조각이 됐다. "가장 멍청한 방법"이라는 표현은 겸양이 아니라 설계 철학처럼 들린다. 세포가 진화 과정에서 도달한 정교한 해법을 그대로 재현하려는 대신, 그것이 왜 어려운지 인정하고 다른 축으로 우회한다. Wright Flyer가 새의 날갯짓을 흉내내지 않고 고정익과 스크루로 갈아탄 것과 같은 결의 선택이다.

두 번째로 마음에 남은 것은 발표의 방식이다. Cell 저널에서 리뷰어 한 명이 "진짜 생물학이 아니다"라며 거절한 원고를, 프리프린트 서버에 올리기도 전에 언론에 엠바고 배포하고 같은 날 오픈소스 재단을 출범시킨 흐름은 "이 성과가 학술지의 게이트를 기다릴 종류의 것이 아니다"라는 판단을 담고 있다. 시대의 발화 지점은 학술지가 아니라 프리프린트 + 언론 + 공동 자원 재단이 되는가에 대한 하나의 사례로 지켜볼 만하다.

## 출처

- 원 논문: Adamala et al., *A Chemically Defined Synthetic Cell Capable of Growth and Replication*, [Biotic 프리프린트 PDF](https://biotic.org/research/spudcell/spudcell-manuscript.pdf) (2026-07-01, bioRxiv 게시)
- Biotic 프로젝트 개요: <https://biotic.org/research/spudcell/>
- 미네소타대학 보도자료 (2026-07-01): <https://twin-cities.umn.edu/news-events/worlds-first-synthetic-cell-complete-life-cycle-could-revolutionize-biological>
- Quanta Magazine, Yasemin Saplakoglu (2026-07-01): <https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/>
- Science AAAS, Kai Kupferschmidt (2026-07-01): <https://www.science.org/content/article/lab-created-spudcell-marks-major-step-toward-building-life-scratch>
- New Scientist, Michael Le Page (2026-07-01): <https://www.newscientist.com/article/2532689-have-scientists-really-made-a-living-cell-from-scratch-not-quite/>
- Phys.org / University of Minnesota (2026-07-01): <https://phys.org/news/2026-07-world-synthetic-cell-life-revolutionize.html>
- 연합뉴스, 김아람 (2026-07-02): <https://www.yna.co.kr/view/AKR20260702025900009>
