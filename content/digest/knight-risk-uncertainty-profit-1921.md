---
title: "Risk, Uncertainty, and Profit"
date: 2026-05-10T00:45:00+09:00
tags: ["knightian-uncertainty", "위험", "불확실성", "기업가-이론"]
categories: ["다이제스트"]
summary: "Frank H. Knight가 1921년 단행본 「Risk, Uncertainty, and Profit」에서 정립한 *측정 가능한 위험(risk)*과 *측정 불가능한 불확실성(uncertainty)*의 결정적 구분. 측정 가능한 위험은 보험·통계로 비용에 흡수되지만, 진짜 불확실성은 원리적으로 계량되지 않으며, 바로 그 영역의 부담을 짊어지는 대가가 기업가 이윤이라는 100년 된 명제."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Frank H. Knight(시카고대)가 1916년 박사학위 논문(코넬대)을 1921년 Houghton Mifflin에서 단행본으로 묶어 낸 「Risk, Uncertainty, and Profit」이며, *Knightian uncertainty* 명제의 정수가 압축된 단원은 Pt.III, Ch.VII "The Meaning of Risk and Uncertainty"다.[^meaning-1921]
2. 핵심 진단: 일상에서 'risk'라 부르는 개념은 사실 *확률 분포가 알려진 측정 가능한 위험*과 *확률 분포 자체가 알려질 수 없는 불확실성* 두 가지를 뭉뚱그린 용어다. 두 영역은 경제 조직 안에서 인과적 역할이 범주적으로 다르므로 분리해서 다루어야 한다.
3. 결론: 측정 가능한 위험은 보험·통계 처리를 거쳐 *고정 비용*으로 흡수되어 사실상 불확실성으로 작동하지 않는다. 완전 경쟁이 이윤을 0으로 수렴시키지 못하는 이유는 *측정 불가능한* 진짜 불확실성이 남아 있기 때문이며, 기업가가 받는 이윤은 바로 이 *true uncertainty*의 보상이다.

## 자료의 정체

「Risk, Uncertainty, and Profit」은 시카고대 경제학자 Frank H. Knight(1885–1972)가 코넬대에서 쓴 1916년 박사학위 논문 "A Theory of Business Profit"을 1921년 단행본으로 출간한 책이다. Hart, Schaffner & Marx 경제 에세이 공모전 2등 수상작이 그 전신이다. 출판 후 100년이 지난 지금도 미시경제학·기업가 이론·의사결정 이론의 표준 참고문헌으로 살아 있고, 책의 핵심 구분 자체가 *Knightian uncertainty*라는 고유명사로 굳었다.

본문은 14개 장이며, *Knightian* 명제의 정수가 가장 압축적으로 등장하는 단원은 Pt.III, Ch.VII "The Meaning of Risk and Uncertainty"다. 책 전체의 thesis 선언은 Pt.I, Ch.I 서론에서 이미 이루어진다.

본 다이제스트는 1921년 초판이 public domain이므로 [Library of Economics and Liberty(Econlib)](https://www.econlib.org/library/Knight/knRUP.html)의 텍스트(Liberty Fund 디지털판)를 1차 자료로 사용했다. 보조 자료로는 Knight의 명제를 100년 후 시점에서 학술적으로 정리·재평가한 Amar Bhidé(HBS) 2021년 워킹페이퍼 「Renewing Knightian Uncertainty: A Pragmatic Prospectus and Demonstration」(WP 21-129)을 함께 읽었다.[^renewing-2021]

본 다이제스트는 학술 토대 시리즈의 세 번째이자 마지막에 해당한다. 시간 순으로 역행하면서 *비가역성 × 불확실성* 명제의 가장 깊은 학술 뿌리에 도달한다. 시리즈의 앞 두 글은 [Taleb 외 — The Precautionary Principle (2014)](/digest/taleb-precautionary-principle-2014/), [Dixit & Pindyck — The Options Approach to Capital Investment (1995/1994)](/digest/dixit-pindyck-real-options-1994/)다. Knight의 *risk vs uncertainty* 구분이 D&P가 옵션 가치를 정의하는 *불확실성* 차원의 학술 토대이고, Taleb의 예방 원칙이 *측정 불가능한 ruin*에 대해 적용한 행동 원칙이라는 점에서, 1921 → 1994 → 2014의 시간 역행이 한 사슬에 묶인다.

## 책의 출발점 — risk와 uncertainty의 분리

Knight는 책의 첫 장에서부터 자기 명제의 척추를 세운다. 이윤을 진지하게 설명하려면 'risk'라는 용어 안에 두 종류가 섞여 있다는 사실을 풀어야 한다는 선언이다.

> But Uncertainty must be taken in a sense radically distinct from the familiar notion of Risk, from which it has never been properly separated. The term "risk," as loosely used in everyday speech and in economic discussion, really covers two things which, functionally at least, in their causal relations to the phenomena of economic organization, are categorically different. ... It will appear that a *measurable* uncertainty, or "risk" proper, as we shall use the term, is so far different from an *unmeasurable* one that it is not in effect an uncertainty at all. (Pt.I, Ch.I)

이 선언이 책 전체의 출발점이다. *측정 가능한* 부류는 risk라 부르고, *측정 불가능한* 부류는 uncertainty라 부른다. 둘은 경제 현상에서 작동 방식이 본질적으로 다르므로 분리하지 않으면 이윤을 설명할 수 없다.

## 세 가지 확률 — a priori, 통계, 추정

Pt.III, Ch.VII에서 Knight는 실무에서 마주치는 확률 판단을 셋으로 가른다. 이 분류가 *Knightian uncertainty*의 자리를 정확히 짚는 분석 도구다.

| 유형 | 동질성의 근거 | 사례 | 확률 산출 방식 |
| --- | --- | --- | --- |
| (1) *A priori* probability | 사례들이 진정으로 동질적 | 주사위, 룰렛, 카드 | 일반 원리로 *계산* |
| (2) Statistical probability | 사례들이 실용적으로 비슷 | 화재율, 사망률 | 경험적 *빈도* |
| (3) Estimates | 사례를 분류할 *어떤 타당한 근거도 없음* | 공장 증설 결정, 신제품 출시 | 직관·판단(*비계량적*) |

> Taking, then, the classification point of view, we shall find the following simple scheme for separating three different types of probability situation: ... 3. Estimates. The distinction here is that there is *no valid basis of any kind* for classifying instances. (Pt.III, Ch.VII)

(1)과 (2)는 모두 *measurable risk*에 속한다. (3)이 *Knightian uncertainty*다.

Knight는 동질성을 가르는 잣대가 결국 *분류 가능성*임을 강조한다. 주사위의 던짐들은 이론적으로 동질적인 그룹을 이루지만, 화재의 사례는 어쩔 수 없는 개별 차이가 있고, 사업 의사결정의 사례는 너무 고유해서 의미 있는 동질군 자체가 형성되지 않는다.

## 추정의 자리 — 분류 자체가 불가능한 영역

세 번째 유형, 추정(estimate)이 책 전체에서 가장 비중 있게 다루어진다. Knight가 든 대표 사례는 공장 규모 확대 결정이다.

> Take as an illustration any typical business decision. A manufacturer is considering the advisability of making a large commitment in increasing the capacity of his works. He "figures" more or less on the proposition, taking account as well as possible of the various factors more or less susceptible of measurement, but the final result is an "estimate" of the probable outcome of any proposed course of action. ... It is manifestly meaningless to speak of either calculating such a probability *a priori* or of determining it empirically by studying a large number of instances. The essential and outstanding fact is that the "instance" in question is so entirely unique that there are no others or not a sufficient number to make it possible to tabulate enough like it to form a basis for any inference of value about any real probability in the case we are interested in. (Pt.III, Ch.VII)

여기서 Knight의 통찰은 두 단계다.

첫째, 그래도 사람은 결정을 한다. 통계적 빈도가 의미를 잃은 영역에서도 사업가는 직관·"unconscious induction"으로 판단을 형성한다. 둘째, 그 위에 *추정의 추정*이라는 한 층이 더 붙는다. 즉 자기 판단이 옳을 확률 자체에 대한 또 다른 직관적 평가가 행동을 결정한다.

> Fidelity to the actual psychology of the situation requires, we must insist, recognition of these two separate exercises of judgment, the formation of an estimate and the estimation of its value. (Pt.III, Ch.VII)

판단력 자체에 대한 평가가 실은 사업가에게 가격이 매겨지는 능력이고, 이 능력의 사회적 분포가 기업·고용·임금의 큰 그림을 만든다고 Knight는 본다.

## 측정 가능한 risk는 사라진다 — consolidation의 원리

Knight의 두 번째 핵심 통찰은, 측정 가능한 risk는 적절한 조직 장치를 만나면 사실상 *사라진다*는 점이다.

샴페인 병이 보관 중에 일정 비율로 터진다고 하자. 큰 비율이든 작은 비율이든 *비율이 일정하면* 생산자에게는 더 이상 위험이 아니다. 손실은 정해진 비율의 *고정 비용*으로 변환되어 가격에 전가된다. 화재 손실도 마찬가지다. 단일 건물 소유자에게는 발화 여부가 불확실하지만, 보험사가 다수 사례를 묶으면 손실은 통계적 평균으로 수렴하며 다시 *고정 비용*이 된다.

> The business world has evolved several organization devices for effectuating this consolidation, with the result that when the technique of business organization is fairly developed, measurable uncertainties do not introduce into business any uncertainty whatever. (Pt.III, Ch.VII)

이 명제는 보험 시장이 왜 존재하는지에 대한 정의이자, *어디서부터가 진짜 불확실성인지*를 가르는 잣대다. 사례들을 동질적인 큰 그룹으로 묶을 수만 있다면 그 위험은 보험화되어 비용에 흡수된다. 그 영역은 정의상 *진짜 불확실성*이 아니다.

## 기업가 이윤의 해명

이제 책 전체의 thesis가 한 줄로 모인다. 기업가는 생산 요소를 *현재의 고정 가격*으로 미리 계약해 묶고, *미래의 시장 가격*으로 산출물을 판다. 그 사이의 격차가 이윤(또는 손실)이다.

> For profit arises from the fact that entrepreneurs contract for productive services in advance at fixed rates, and realize upon their use by the sale of the product in the market after it is made. ... Hence it is our imperfect knowledge of the future, a consequence of change, not change as such, which is crucial for the understanding of our problem. (Pt.III, Ch.VII)

Knight의 추론은 이렇게 닫힌다. 만일 모든 변화가 *측정 가능*하다면, 그 변화는 사전에 가격에 반영되어 격차가 사라진다. 격차가 남는 까닭은 변화 가운데 *측정 불가능한* 부분이 남기 때문이다. 따라서 이윤의 원천은 risk가 아니라 *true uncertainty*다.

> It is this *true uncertainty* which by preventing the theoretically perfect outworking of the tendencies of competition gives the characteristic form of "enterprise" to economic organization as a whole and accounts for the peculiar income of the entrepreneur. (Pt.III, Ch.VII)

이 한 문장이 책의 결론이자, 이후 100년 동안 *Knightian uncertainty*라는 이름으로 인용되는 명제의 원본이다.

## 100년 후 — 세 가지 재해석

Bhidé 2021은 출판 100주년을 맞아 이 책의 학술적 위상을 다시 정리한다. Knight의 구분을 둘러싼 현대 경제학의 세 갈래 입장이 명확히 드러나는 정리다.

### Friedman의 거부 (1976)

Milton Friedman은 Leonard J. Savage의 주관 확률 이론에 기대 Knight의 risk/uncertainty 구분을 단호히 거부한다.

> In his seminal work, Frank Knight drew a sharp distinction between risk, as referring to events subject to a known or knowable probability distribution and uncertainty, as referring to events for which it was not possible to specify numerical probabilities. I have not referred to this distinction because I do not believe it is valid. I follow L. J. Savage in his view of personal probability, which denies any valid distinction along these lines. We may treat people as if they assigned numerical probabilities to every conceivable event. (Friedman 1976, Bhidé 2021에서 재인용)

이 입장에서 의사결정자는 *모든 사건*에 주관 확률을 할당하므로, 측정 가능/불가능의 경계는 사라진다.

### LeRoy & Singell의 deconstruction (1987)

Stephen F. LeRoy & Larry D. Singell은 *Journal of Political Economy* 논문에서 Knight의 본의가 사실 다른 곳에 있다고 주장한다. 그들이 보기에 Knight가 말한 uncertainty는 *주관 확률의 부재*가 아니라 *도덕적 위험·역선택*으로 보험 시장이 붕괴하는 상황이다.

> The received interpretation of Knight's classic risk-uncertainty distinction—as concerning whether or not agents have subjective probabilities—constitutes a misreading of Knight. ... By uncertainty, Knight instead meant situations in which insurance markets collapse because of moral hazard or adverse selection. (LeRoy & Singell 1987 abstract)

이 해석은 Knight를 *정보경제학·대리인 이론의 선구자*로 자리매김하는 효과가 있다.

### Bhidé의 pragmatic prospectus (2021)

Amar Bhidé는 양쪽 모두를 비판한다. Friedman의 거부는 *가격 이론* 안에서는 무해하지만 기업가 활동의 *고유한 결정* 영역을 설명하지 못한다고 본다. LeRoy & Singell의 재해석은 Knight의 "in this first approximation"이라는 단서를 잘라낸 무리한 독해라고 본다. Bhidé는 Knight의 원래 정의 — *비계량적·주관적 추정*이 불가피한 의사결정 영역 — 을 그대로 살리되, 시장의 빈도주의적 처리가 닿지 않는 *기업가적 의사결정*에 한정해 적용하자고 제안한다.

> Knight distinguished between uncertainty and risk to specify the true nature of profit, but this specification never caught on and I see no prospects for renewed research in this direction. As it happens, Knight also used uncertainty to specify the distinctive role of the entrepreneur (not just entrepreneurial profit). Using uncertainty along similar lines, I suggest, offers more promising prospects. (Bhidé 2021, p. 1)

세 입장은 결국 *Knightian uncertainty*의 학술적 운명을 보여 준다. 가격 이론은 그것 없이도 굴러가지만, *고유한 결정·신생 시장·기업가 활동*을 다루는 순간 Knight의 구분은 다시 살아난다.

## Knight vs Keynes — 두 1921의 차이

Bhidé가 Bernstein 「Against the Gods」를 인용해 짚는 흥미로운 우연. Knight의 「Risk, Uncertainty, and Profit」과 John Maynard Keynes의 「A Treatise on Probability」가 같은 1921년에 출간되었다. 두 사람 모두 *빈도주의 확률을 의사결정의 안내자*로 삼는 데 회의적이었다는 점이 같다.

다만 두 사람의 *uncertainty*는 결이 다르다. Keynes의 *radical uncertainty*는 30년 후 사유재산 위치, 유럽 전쟁의 향방, 미래의 이자율 같은 *거대하고 예외적인* 미지의 영역이다.

> By "uncertain" knowledge ... I do not mean merely to distinguish what is known for certain from what is only probable. ... The sense in which I am using the term is that in which the prospect of a European war is uncertain, or the price of copper and the rate of interest twenty years hence ... About these matters there is no scientific basis on which to form any calculable probability whatever. We simply do not know. (Keynes 1937, Bhidé 2021에서 재인용)

Knight의 uncertainty는 그것보다 *훨씬 일상적*이다. 공장 증설처럼 *반복되지만 통계화되지 않는* 평범한 사업 판단까지 포함한다.

> Ignorance is not as extreme (or consequences as grand) as the prospects of the expropriation of private wealth after thirty years, as in Keynes's example. ... Conversely, factory expansions and other routine, yet idiosyncratic choices demand estimates and choices. A "do not know" shrug of the shoulders impelled by total ignorance lies outside the boundaries of Knightian uncertainty. (Bhidé 2021, p. 5–6)

Bhidé는 이 차이가 흐려질 때 Knight 명제의 실용적 용처가 사라진다고 짚는다. Keynes의 *radical uncertainty*는 거시경제 대규모 개입의 정당화로 동원되지만, Knight의 uncertainty는 *매일 의사결정을 내리는 평범한 기업가*의 자리에 적용된다.

## 가장 흥미로운 지점

본 자료를 읽고 가장 인상 깊었던 것은 — Knight의 가장 결정적인 통찰이 *측정 가능성*이 아니라 *분류 가능성*에 매여 있다는 점이다.

세 가지 확률 유형은 결국 "사례들을 동질적인 그룹으로 묶을 수 있는가"를 묻는 질문에 대한 세 가지 답이다. 묶을 수 있으면 (1)·(2)이고, 묶을 수 없으면 (3)이다. 여기서 결정적인 것은 *확률 분포가 존재하느냐*가 아니라 *사례들이 서로 충분히 비슷해서 한 그룹으로 다룰 수 있느냐*다. 그래서 Knight의 명제는 단순히 "분포가 알려졌느냐"의 문제가 아니라 *고유성(uniqueness)*의 문제로 다시 읽힌다. 사례가 너무 고유해 통계적 묶음 자체가 의미를 잃는 영역, 그 영역이 *Knightian uncertainty*다.

이 관찰을 토대 시리즈의 다른 두 글과 나란히 두면 사슬이 보인다. Knight 1921의 *true uncertainty*는 [Dixit & Pindyck 1994](/digest/dixit-pindyck-real-options-1994/)의 옵션 가치 모형이 작동하기 위한 전제 — *불확실성*의 정의 — 가 되고, Dixit & Pindyck의 *비가역성 × 불확실성* 결합은 [Taleb 2014](/digest/taleb-precautionary-principle-2014/)가 *시스템적 ruin*의 영역에서 비대칭 위험으로 일반화한 토대가 된다. 1921 → 1994 → 2014의 시간 역행은 하나의 명제 — *측정 불가능한 영역에서의 비가역적 결정은 cost-benefit의 표준 프레임으로 다룰 수 없다* — 가 점점 더 깊은 학술 뿌리로 옮겨가는 과정이다.

## 출처

- 저자: Frank H. Knight (1885–1972, 시카고대 경제학과)
- 본 다이제스트는 원문에 인용할 만한 도식·차트가 없는 순수 텍스트 자료이므로 텍스트 다이제스트로 정리했다.

[^meaning-1921]: 단행본: 「Risk, Uncertainty, and Profit」, Houghton Mifflin Co., Boston 1921. 1916년 코넬대 박사학위 논문이 모태이며, Hart, Schaffner & Marx 경제 에세이 공모전 수상작이 그 전신이다. - 1차 정독 자료(전문, public domain): <https://www.econlib.org/library/Knight/knRUP.html> - 정수 단원 Pt.III Ch.VII "The Meaning of Risk and Uncertainty": <https://www.econlib.org/library/Knight/knRUP.html?chapter_num=9> - thesis 선언 Pt.I Ch.I: <https://www.econlib.org/library/Knight/knRUP.html?chapter_num=3>
[^renewing-2021]: 보조 자료: Amar Bhidé, "Renewing Knightian Uncertainty: A Pragmatic Prospectus and Demonstration", Harvard Business School Working Paper 21-129, 2021. - PDF: <https://www.hbs.edu/ris/Publication%20Files/21-129_3a817910-dfb9-4fc9-b913-164151c27b4e.pdf>
