---
title: "The Options Approach to Capital Investment / Investment under Uncertainty"
date: 2026-05-10T00:30:00+09:00
tags: ["real-options", "비가역성", "불확실성", "투자이론"]
categories: ["다이제스트"]
summary: "Avinash K. Dixit & Robert S. Pindyck가 1994년 단행본 「Investment under Uncertainty」와 1995년 HBR 압축 요약본에서 정립한 실물 옵션(real options) 프레임. 비가역적이고 지연 가능한 투자 결정에서는 단순 NPV가 체계적으로 잘못된 답을 주며, 투자 기회를 콜옵션으로 다시 모형화해야 한다고 주장한다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Avinash K. Dixit(Princeton)와 Robert S. Pindyck(MIT Sloan)이 1994년 단행본 「Investment under Uncertainty」(Princeton UP)에서 체계화한 실물 옵션 이론이며, 1차 정독 자료는 두 저자가 직접 쓴 1995년 HBR 압축 요약본 「The Options Approach to Capital Investment」(약 11쪽)이다.
2. 핵심 진단: 전통적 NPV 규칙은 투자가 *가역적이거나* *now-or-never*라는 두 가정 위에 서 있는데, 현실의 투자는 대개 *비가역적*이면서 *지연 가능*하므로 두 가정이 동시에 무너진다. 결과적으로 NPV > 0만으로 정당화되는 의사결정은 체계적으로 과잉투자를 만든다.
3. 처방: 투자 기회를 *금융 콜옵션*과 동형의 권리로 다시 모형화하고, 비가역적 commit는 옵션을 죽이는 행위이므로 그 *옵션 프리미엄*을 비용에 더해야 한다 — 즉 의사결정 규칙은 NPV > 0이 아니라 NPV > (옵션 보유 가치)다.

## 자료의 정체

단행본 「Investment under Uncertainty」(Princeton University Press, 1994)는 1980년대 후반부터 Pindyck와 동료들이 축적한 비가역 투자 이론을 책 한 권으로 묶어 낸 정통 텍스트로, 이후 30년의 real options 연구의 표준 참고문헌이 되었다.[^investment-1994]

본 다이제스트의 1차 자료는 동일한 두 저자가 일반 독자용으로 압축해 다시 쓴 1995년 5월–6월 HBR 기사 「The Options Approach to Capital Investment」다. 단행본의 수학을 전부 걷어내고, 핵심 직관과 사례를 11쪽으로 압축했다. 페이월 우회를 위해 Pindyck의 MIT 개인 사이트에 공개된 PDF(아래 출처 참조)를 사용했다.[^options-1995]

본 다이제스트는 학술 토대 시리즈의 두 번째에 해당한다. 첫 번째인 [Taleb 외 — The Precautionary Principle (2014)](/digest/taleb-precautionary-principle-2014/)와 *비가역성*이라는 같은 개념적 토대를 공유한다. Taleb이 *손해 영역*의 비가역(ruin)에 적용한 원리를 Dixit & Pindyck은 *투자 영역*의 비가역(sunk capital)에 적용한 셈이다.

## NPV 규칙이 서 있는 두 가정

저자들은 비즈니스스쿨이 가르치는 표준 NPV 규칙이 둘 중 하나의 가정을 깔고 있다고 지적한다.

| 가정 | 의미 | 현실에서 깨지는 이유 |
| --- | --- | --- |
| 투자가 가역적이다 | 시장이 악화되면 투자를 되돌리고 비용을 회수할 수 있다 | 대부분의 자본은 회사·산업 특화 sunk cost이며 매도 시 lemon 가격만 받는다 |
| 투자가 now-or-never다 | 지금 안 하면 기회가 영원히 사라진다 | 대부분의 투자는 1년·2년·5년 후로 지연하면서 새 정보를 기다릴 수 있다 |

두 가정이 동시에 깨질 때 — 즉 *비가역적이면서 지연 가능한* 투자에서 — NPV는 결정의 한 측면(현금흐름의 현재가치)만 보고, 결정의 타이밍 자체에 묻혀 있는 가치를 보지 못한다. 책의 표현으로:

> Although it is true that some investment decisions fall into those categories, most don't. In most cases, investments are irreversible and, in reality, capable of being delayed.

## 투자 기회는 콜옵션이다

논문의 핵심 비유는 다음과 같다. 투자 기회는 어떤 자산(미래 현금흐름의 현재가치)을 *살 권리이지만 살 의무는 아닌* 콜옵션과 구조가 같다. 회사가 비가역적 투자 지출을 단행하는 순간 그 콜옵션을 *행사(exercise)*하는 셈이다. 행사가 일단 일어나면, 시장 조건이 나빠져도 매도는 되돌릴 수 없으므로 *기다리며 새 정보를 얻을 권리* 자체가 소멸한다.

> When a company exercises its option by making an irreversible investment, it effectively "kills" the option. In other words, by deciding to go ahead with an expenditure, the company gives up the possibility of waiting for new information that might affect the desirability or timing of the investment.

이 사라진 옵션 가치는 명백한 기회비용이다. 따라서 단순 NPV 규칙은 다음과 같이 수정되어야 한다고 저자들은 정리한다.

> The simple NPV rule needs to be modified: Instead of just being positive, the present value of the expected stream of cash from a project must exceed the cost of the project by an amount equal to the value of keeping the investment option alive.

즉 의사결정 규칙은 NPV > 0이 아니라 다음과 같다.

> NPV > 옵션 프리미엄(= 옵션을 살아있게 두는 가치)

이 한 줄이 책 전체의 척추다.

## 불확실성이 클수록 기다리는 가치가 커진다

금융 콜옵션 가격은 기초 자산의 변동성에 단조 증가한다. 변동이 클수록 비대칭 페이오프(상방은 무한, 하방은 프리미엄까지)의 기대값이 커지기 때문이다. 실물 옵션에도 같은 논리가 적용된다.

전통 NPV는 불확실성을 단지 *할인율 상승* 한 가지 변수로만 흡수한다. 그러나 옵션 관점에서 불확실성은 의사결정 자체를 바꾸는 *근본 변수*다. 저자들은 이 점을 강조하면서 이렇게 적는다.

> A small increase in uncertainty (nondiversifiable or otherwise) can lead managers to delay some investments (those that involve the exercising of options, such as the construction of a factory). At the same time, uncertainty can prompt managers to accelerate other investments (those that generate options or reveal information, such as R&D programs).

같은 환경의 불확실성 상승이 *어떤 투자는 늦추고* *어떤 투자는 앞당기는* 두 방향의 효과를 동시에 갖는다는 것이 — 그리고 그 비대칭이 옵션 구조에서 자연스럽게 도출된다는 것이 — 이 이론의 가장 강력한 시각이다.

## 비가역성의 네 원천

저자들은 투자 비가역성이 발생하는 경로를 네 가지로 정리한다.

1. *회사·산업 특화 자본*. 마케팅·광고·R&D 지출은 회사 내부에서만 가치가 있다. 제철소는 산업 안에서만 거래되며, 그 산업이 동질적이라면 매도가가 매수가와 거의 같지 않다.
2. *중고 자본 시장의 lemon problem*. 트럭·사무기기처럼 산업 비특화 자본조차 정보 비대칭 때문에 시장 평균 품질로 가격이 매겨진다. 우량 상태의 자산을 매도하면 새 가격에 한참 못 미친다.
3. *제도·문화 제약*. 정부 규제, 자본 통제, 노조 협약 같은 제도가 자본 재배치를 막는다.
4. *신규 채용*. 채용·훈련·해고 비용으로 인해 신규 인력 투자도 부분적으로 비가역적이다.

저자들은 결론적으로 "거의 모든 대규모 투자는 적어도 부분적으로 비가역적이다"라고 진단한다.

## 두 비대칭 처방 — 행사 vs 생성

옵션 관점이 가장 분명하게 작동하는 지점은 두 종류 투자에 *반대 방향* 편향을 처방한다는 사실이다.

| 투자 유형 | 옵션 관점이 처방하는 평가 | 직관 |
| --- | --- | --- |
| 옵션 *행사*형 (공장 건설, 시장 진입, 광고 commit) | NPV보다 *덜* 가치 있게 평가 | 행사하는 순간 옵션이 죽으므로 그 사라진 가치만큼 차감 |
| 옵션 *생성*형 (R&D, 시장 조사, 시추, 토지 매입) | NPV보다 *더* 가치 있게 평가 | 미래 정보를 가져와 더 나은 후속 결정을 가능케 하므로 옵션 가치를 가산 |

본문의 제약 사례 한 줄로 정리하면 다음과 같다.

> An action to **create** an option should be valued more highly than a naive NPV approach would suggest. \[...\] An action that **exercises** or **uses up** an option should be valued less than a simple NPV approach would suggest.

본문의 가상 제약회사 예시는 이 비대칭을 수치로 보여 준다. R&D 1500만 달러 → 생산설비 비용 시나리오 3종(저 4000만, 중 8000만, 고 1억 2000만, 각 1/3 확률) → 매출 시나리오 2종(저 5000만, 고 1억 3000만, 각 1/2 확률).

- 단순 NPV: 기대 영업이익 1000만 달러로 R&D 1500만 달러를 정당화하지 못한다(−500만). 표준 분석은 *프로젝트를 죽인다*.
- 옵션 가치 포함: R&D는 비용 시나리오의 불확실성을 *해소*하는 옵션이다. 비용·매출 정보가 들어온 뒤 *상황별로* 진행/중단 결정을 한다고 모델링하면 R&D의 가치는 2670만 달러로, 표준 분석이 죽인 프로젝트가 *옵션 가치 포함 시 강하게 정당화*된다.

## 합리적 myopia — 손실 중에도 시설을 닫지 않는 이유

옵션 이론의 가장 강력한 *기존 행동의 재해석*은 "기업이 손실을 보면서도 시설을 폐쇄하지 않는다"는 현상에 대한 새 설명이다. 저자들은 이를 myopia(근시안)가 아니라 *옵션 보존*으로 본다.

- *구리 광산·제련소*: 구리 가격이 평균 가변비용 아래로 떨어져도 가동을 유지한다. 일단 닫으면 *재가동 옵션*이 비대칭으로 큰 비용을 부른다(숙련 인력 분산, 브랜드 인지 소실, 자본 재조립 비용).
- *1980년대 외국 기업의 미국 시장 잔류*: 달러 강세로 손실이 누적되어도 대다수 외국 기업은 미국 시장에서 철수하지 않았다. *재진입 옵션*을 살아있게 두는 것이 합리적이었다.
- *미국 농가*: 1980년대 중반 곡물·금속 가격 폭락에도 대규모 disinvestment는 일어나지 않았다.

저자들의 표현으로:

> Continuing to operate keeps the capital intact and preserves the option to resume profitable production later. The option is valuable and, therefore, companies may quite rationally choose to retain it, even at the cost of losing money in the meantime.

기업이 cost of capital의 3\~4배에 달하는 hurdle rate(15\~30%, 1987년 Summers 연구)를 요구하는 광범위한 실증 패턴 역시 — 외부 관찰자에게는 myopia로 보이지만 — *옵션 가치를 무의식적으로 가격에 반영한* 합리적 행동으로 재해석된다.

## 다른 응용 사례

저자들은 책 1장과 HBR 기사에서 다음의 응용을 짧게 짚는다.

- *유전·광물 보유*. 미개발 유전은 미래 시점·규모를 정할 수 있는 옵션이다. 가격 변동성이 클수록 옵션 가치가 커지므로 — 단순 NPV가 *적게* 투자하라고 답하는 곳에서 — 옵션 가치는 정확히 *반대* 방향, 즉 *더 많이 보유하라*고 답한다.
- *전력 사업의 규모 vs 유연성*. 대형 석탄 발전소(규모의 경제)와 소형 석유 발전소 묶음(유연성) 사이의 선택은 후자의 *유연성 옵션 가치*를 NPV가 무시하므로 잘못된 답을 준다. New England Electric System(NEES)이 옵션 가격기법을 도입해 수력 재가동 시점, 발전소 은퇴 시점 결정에 적용했다.
- *개인의 경력 선택과 결혼*. 1950년대 물리학을 택한 학생들이 1970년대 직무 잉여에 부딪힌 사례가 인용된다. *너무 일찍 좁은 트랙에 commit하지 말라*는 처방, 이혼 비용이 높은 사회·문화일수록 결혼의 *진입 hurdle*을 높여야 한다는 처방이 같은 이론으로 따라 나온다.

## 가장 흥미로운 지점

본 자료를 읽고 가장 인상 깊었던 것은 — 옵션 이론이 *처방*뿐 아니라 기존 행동의 *재해석*까지 동시에 제공한다는 점이다.

NPV가 답하지 못하는 두 종류의 미스터리가 있다. 하나는 "왜 기업은 hurdle rate을 cost of capital보다 훨씬 높게 잡는가"이고, 다른 하나는 "왜 손실을 보면서도 시설을 닫지 않는가"다. 둘 다 표준 이론에서는 *비합리*로 분류되었으나, 옵션 관점에서는 둘 다 *합리적*이 된다. 가설이 데이터를 설명할 뿐 아니라 *기존 이론이 비합리로 분류했던 행동을 합리로 옮긴다*는 점에서 — 이 이론의 설명력은 단순한 처방 도구를 넘어선다.

또 하나 눈에 띄는 것은 같은 *비가역성 + 불확실성* 토대가 두 다른 영역에서 같은 결론을 향해 수렴한다는 것이다. [Taleb의 예방원칙](/digest/taleb-precautionary-principle-2014/)이 시스템적 ruin이라는 *손실 영역의 비가역*에서 "어떤 비용을 치르더라도 회피하라"는 처방을 도출했다면, Dixit & Pindyck의 옵션 이론은 sunk capital이라는 *투자 영역의 비가역*에서 "행사 hurdle을 옵션 프리미엄만큼 올려라"는 처방을 도출한다. 손해 측의 비가역과 투자 측의 비가역이 같은 수학적 비대칭을 갖기에, 두 이론은 서로 다른 정책 영역에서 같은 형식으로 작동한다.

## 출처

- 저자: Avinash K. Dixit (Princeton University), Robert S. Pindyck (MIT Sloan School of Management)
- 본 다이제스트는 원문에 인용할 만한 도식·차트가 잡지 일러스트 외에는 거의 없어 텍스트 다이제스트로 정리했다.

[^investment-1994]: 단행본: 「Investment under Uncertainty」, Princeton University Press, 1994. <https://press.princeton.edu/books/hardcover/9780691034102/investment-under-uncertainty>
[^options-1995]: 1차 정독 자료: 「The Options Approach to Capital Investment」, *Harvard Business Review*, May–June 1995, pp. 105–115. - HBR 페이지(페이월): <https://hbr.org/1995/05/the-options-approach-to-capital-investment> - PDF (Pindyck의 MIT 개인 사이트): <https://web.mit.edu/rpindyck/www/Papers/Options_Approach.pdf>
