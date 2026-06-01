---
title: "센트럴 도그마는 깨졌는가 — DRT3·DRT9 발견 팩트체크"
date: 2026-05-13T10:30:00+09:00
tags: ["과학", "분자생물학", "센트럴 도그마", "팩트체크", "과학 커뮤니케이션"]
categories: ["다이제스트"]
summary: "한 트윗이 '40억 년 깨지지 않았던 생물학의 규칙이 한 달에 두 번 깨졌다'고 알렸다. 원논문 두 편과 분자생물학자들의 비평을 대조해 보니, 새로운 메커니즘은 실재하나 도그마 붕괴는 과장이었다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. 한 트윗(All Day Astronomy, @forallcurious, 2026-05-13)이 "단백질이 템플릿도 지시도 없이 자기 모양만으로 DNA를 쓴다"며 분자생물학의 중심 원리가 한 달에 두 번 깨졌다고 주장했다.
2. 트윗이 암시한 두 논문은 실재하나, 하나(DRT9, Tang et al., *Nature* 2025-05)는 여전히 RNA를 템플릿으로 쓰고, 다른 하나(DRT3, Deng et al., *Science* 2026-04)도 AC 두 글자만 반복하는 매우 특화된 효소다.
3. 분자생물학자들의 평가는 일치한다 — 흥미로운 항파지 면역 메커니즘이긴 하나, 센트럴 도그마는 깨지지 않았다.

## 트윗의 주장

> 🚨: Biology's most unbreakable rule that held for 4 billion years just broke twice in one month. Scientists just found a protein that writes DNA from scratch. No template. No instructions. Just its own shape.

천문학 계정(@forallcurious)이 올린 단일 트윗이다. 원논문 인용 없이 두 개의 발견을 암시했고, 5월 13일 기준 678건의 인용·재게시·좋아요를 기록 중이다.

## 트윗이 암시한 두 논문

### DRT9 — Tang et al., *Nature* 2025

> Tang, S., Žedaveinytė, R., Burman, N. et al. **Protein-primed homopolymer synthesis by an antiviral reverse transcriptase.** *Nature* 643, 1352–1362 (2025-05-28).
> DOI: [10.1038/s41586-025-09179-5](https://doi.org/10.1038/s41586-025-09179-5)

DRT9(Defense-associated Reverse Transcriptase 9)은 박테리아의 항파지 면역계 일부다. 파지가 감염되면 DRT9 헥사머 복합체가 poly-dA(아데닌 호모폴리머) 사슬을 길게 합성해 세포 성장 정지를 유발하고, 이로써 집단 수준 면역을 만든다.

이 시스템에서 단백질의 타이로신 잔기(Y496, Y498)는 DNA 합성의 **개시(priming)** 만을 담당한다. 어떤 염기를 넣을지는 비코딩 RNA(ncRNA)의 보존된 poly-U 영역이 결정한다. 즉 DRT9은 **여전히 RNA를 템플릿으로 사용한다.**

트윗의 "no template" 표현은 DRT9에는 맞지 않는다.

### DRT3 — Deng et al., *Science* 2026

> Deng, P., Lee, H., Armijo, C., Wang, H., Gao, A. **Protein-templated synthesis of dinucleotide repeat DNA by an antiphage reverse transcriptase.** *Science* (2026-04).
> DOI: [10.1126/science.aed1656](https://doi.org/10.1126/science.aed1656)

스탠퍼드 Alex Gao 연구실이 보고한 DRT3 시스템에는 두 효소가 있다. Drt3a는 RNA를 템플릿으로 GT 가닥을 만드는 평범한 역전사효소다. **Drt3b가 트윗이 말하는 진짜 발견이다.**

Drt3b의 활성 부위는 자기 단백질 구조에 의해 물리적으로 막혀 있어 핵산 템플릿이 들어올 공간이 없다. 대신 두 개의 아미노산 잔기가 다음 염기를 결정한다.

- **Glu26** — 아데닌(A)의 안정한 도입을 돕는다.
- **Arg253** — 시토신(C)을 교대 위치에 강제한다.

여기에 Drt3b의 C-말단과 내부 루프가 DNA를 비틀어 세 염기를 두 염기의 공간에 압축하는 "kinked backbone"을 만든다. 그 기하학적 왜곡이 protein-templated 합성의 핵심 트릭이다.

결과적으로 <strong>단백질의 모양이 그대로 서열 정보로 작동한다</strong>는 점에서 새로운 분자 메커니즘이다. kilobase 단위로 작동하는 본격적 사례는 이전에 없었다.

## 트윗이 틀리거나 과장한 다섯 가지

| 항목 | 트윗의 주장 | 실제 |
|---|---|---|
| 시점 | "한 달에 두 번 깨졌다" | DRT9 2025-05, DRT3 2026-04 — **1년 간격** |
| 템플릿 부재 | "no template" | DRT9은 여전히 ncRNA 템플릿 사용 |
| 서열 정보 | "writes DNA from scratch" | Drt3b는 AC 두 글자 반복만 합성 |
| 유전 정보 갱신 | (도그마 붕괴 함의) | 만들어진 DNA는 박테리아 게놈에 통합되지 않음 |
| 도그마 자체 | "4 billion year rule broken" | 역전사·텔로머라제·TdT·Rev1 등 보완은 수십 년 전부터 알려져 있음 |

특히 마지막 항목은 중요하다. Crick이 1958년·1970년에 정식화한 센트럴 도그마의 정확한 진술은 **"단백질 서열에서 핵산 서열로 정보가 역류하지 않는다"** 였다. DNA→RNA→단백질의 단방향 흐름은 "기본형"일 뿐, 역전사효소(retrovirus, HIV)·텔로머라제·말단 전이효소(TdT)·Rev1 폴리머라제 등 도그마의 *예외 또는 보완*은 이미 교과서에 들어가 있다.

## 분자생물학계의 평가

이번 발견을 가장 차분하게 정리한 글은 CRISPeR FRENZY 블로그(Anna Meldolesi, 2026-04-21)다. 핵심 인용을 옮긴다.

> 어떤 도그마도 깨지지 않았다. DNA의 중심 원리는 이제 수사적 장치에 가깝다 — RNA가 메신저 외에 얼마나 많은 일을 하는지 떠올려보면. 또한 핵산 서열에 몇 글자 더하는 특화 분자는 이미 여럿 알려져 있다.

Northeastern University의 Nikolai Slavov는 같은 글에서 더 직설적으로 말한다.

> 이것은 단백질이 자기 자신을 '읽어' 복잡한 메시지를 만드는 게 아니라, 매우 특화된 구조적 제약이다. 단백질의 폴드(fold)에 단 하나의 방어 임무가 하드코딩된 'stuttering machine'이다. 다용도 유전 정보 매체가 아니다.

논문의 1저자 Alex Gao 본인도 같은 톤이다 — Drt3b가 합성하는 것은 단 하나의 특정 반복 서열이며, 단백질이 임의의 유전 코드를 쓰는 일반 메커니즘이 아니라는 점을 신중히 단서로 달았다(biotechnologyguy.com 인터뷰, 2026-04-22).

## 가장 흥미로운 지점

새로움이 있는 곳을 가려내자면 두 가지다.

첫째, <strong>항파지 면역의 분자적 다양성</strong>이다. CRISPR-Cas가 바이러스 RNA를 가위로 잘랐다면, DRT 계열은 거꾸로 DNA를 <strong>새로 합성하는 방식</strong>으로 면역을 구현한다. Drt3b의 protein-as-template, DRT9의 protein-primed RNA-templated 합성, 그리고 DRT2의 de novo 유전자 조립까지, 박테리아는 같은 문제에 서로 다른 분자 전술로 답하고 있다.

둘째, **"단백질 폴드가 정보 매체가 될 수 있다"** 는 *원리적 가능성*이다. 매우 좁고 특화된 형태로 — AC 두 글자 반복으로 — 그 가능성이 실증되었다. 임의 정보 매체로 일반화될 가능성은 거의 없지만, 합성생물학·DNA 제작 도구의 새 카드가 한 장 늘었다는 사실은 변하지 않는다.

도그마가 깨졌다는 흥분 대신 이 두 결을 살피는 편이 글의 가치를 더 높이는 길이라고 본다.

## 출처

- 원문 트윗: <https://x.com/forallcurious/status/2054376900299292832>
- Tang et al. *Nature* 643, 1352–1362 (2025): <https://www.nature.com/articles/s41586-025-09179-5>
- Deng et al. *Science* (2026): <https://doi.org/10.1126/science.aed1656>
- CRISPeR FRENZY 비평 (Anna Meldolesi, 2026-04-21): <https://mycrispr.blog/2026/04/21/template-free-dna-and-no-dogma-broken/>
- 후속 해설 (biotechnologyguy.com, 2026-04-22): <https://www.biotechnologyguy.com/2026/04/a-bacterial-enzyme-just-made-dna.html>

원문 트윗에는 단백질-RNA 복합체 3D 렌더와 DNA 이중나선 시각화 이미지가 첨부되어 있으나 출처가 확인되지 않아 본문에는 인용하지 않았다.
