---
title: "The Precautionary Principle (with Application to the Genetic Modification of Organisms)"
date: 2026-05-09T19:58:00+09:00
tags: ["예방원칙", "비가역성", "위험관리", "fat-tail"]
categories: ["다이제스트"]
summary: "Nassim Taleb 외 4인이 NYU Extreme Risk Initiative 워킹 페이퍼로 정리한 예방 원칙(PP)의 학술적 정의. 시스템적·비가역적 ruin 영역에서만 발동되는 non-naive PP를 fat tail·fragility·비대칭 불확실성의 형식 안에 위치시킨다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Nassim Taleb·Rupert Read·Raphael Douady·Joseph Norman·Yaneer Bar-Yam이 2014년 NYU Extreme Risk Initiative 워킹 페이퍼로 발표한 예방 원칙(Precautionary Principle, 이하 PP)의 형식적 정의이다.[^abstract-arxiv][^arxiv][^taleb-precautionary-principle-2014]
2. PP는 일반 위험 회피가 아니라 *시스템적이고 비가역적인 ruin* 영역에만 발동되는 비-단순(non-naive) 원칙이며, 이 영역에서는 cost-benefit 분석 자체가 깨진다고 본다.
3. 응용으로 GMO는 시스템적·전파적 위험을 가지므로 PP 영역인 반면, 핵에너지는 (대체로) 국소적이라 표준 위험 관리로 다룰 수 있다고 결론짓는다.

## PP의 정확한 정의 — 무엇이고 무엇이 아닌가

논문은 먼저 PP를 *모든* 위험에 적용되는 일반적 회피 규칙으로 보지 않는다. PP가 발동되는 조건을 세 가지로 압축한다.

1. 잠재 손해가 *시스템적*이다 — 국소가 아니라 전파 가능성을 갖는다.
2. 결과가 *비가역적 ruin*이다 — 인류 멸절·생태계 멸절처럼 회복 불가능한 흡수 장벽에 닿는다.
3. 안전성에 대한 *과학적 거의-확신*이 부재하다.

세 조건이 모두 충족되면 입증 책임은 행위 *반대자*가 아니라 *제안자* 측에 있다. 일반 위험은 표준 risk management와 cost-benefit 분석으로 다루며, PP의 가치는 *언제 적용하지 않는가*를 명확히 함으로써 보호된다.

논문은 자료의 핵심을 다음 표로 요약한다.

| Standard Risk Management | Precautionary Approach |
| --- | --- |
| 국소적 손해 (localized harm) | 시스템적 ruin (systemic ruin) |
| 정교한 cost-benefit | 어떤 비용을 치르더라도 회피 |
| 통계적 | fragility 기반 |
| 변동 (variations) | ruin |
| 수렴하는 확률 | 발산하는 확률 |
| 회복 가능 | 비가역 |
| 독립 인자 | 상호 연결 인자 |
| 증거 기반 (evidence based) | 예방 (precautionary) |
| 얇은 꼬리 (thin tails) | 굵은 꼬리 (fat tails) |
| 아래로부터의 tinkering | 위에서의 엔지니어링 |
| 진화한 | 인공의 |

이 표가 논문의 척추다. PP는 *어떤 위험인가*가 아니라 *어떤 구조의 위험인가*에 의해 결정된다.

## Ruin이라는 흡수 장벽

PP의 수학적 핵심은 *ruin은 재생 가능 자원이 아니다*이다. 한 번의 노출에서 ruin 확률이 가령 0.0001로 작아 보이더라도, 노출이 누적되면 ruin barrier에 닿을 확률은 시간이 지남에 따라 1로 수렴한다. 도박꾼이 같은 "한 번" 베팅을 반복하면 결국 파산하는 것과 같다. 따라서 "확률이 작으니 무시해도 된다"는 추론은 ruin 영역에서 통하지 않는다.

> The risk of ruin is not sustainable. By the ruin theorems, if you incur a tiny probability of ruin as a "one-off" risk, survive it, then do it again (another "one-off" deal), you will eventually go bust with probability 1.

비가역성은 cost-benefit 분석 자체를 무력화한다. ruin의 "비용"은 사실상 무한이다 — 미래 자체가 사라지므로 손해의 적분이 발산한다. 비용이 무한이면 *어떤 양수의 작은 확률 × 무한 손해 = 무한*이며, 이는 어떤 유한한 이익으로도 상쇄되지 않는다. 따라서 cost-benefit은 손해가 *bounded*일 때만 유효한 도구이며, 비가역적 시스템 손해 영역에서는 패러다임 자체가 깨진다.

> Because the "cost" of ruin is effectively infinite, cost-benefit analysis (in which the potential harm and potential gain are multiplied by their probabilities and weighed against each other) is no longer a useful paradigm.

논문은 이 영역을 *흡수 장벽이 있는 시스템*으로 정식화한다. 흡수 장벽에 한 번 닿으면 미래의 모든 경로가 종료된다.

## Top-down 시스템과 Fat Tail

PP가 적용 가능한지를 결정하는 두 번째 축은 분포의 꼬리(tail) 두께다. 논문은 *Mediocristan*(얇은 꼬리)과 *Extremistan*(굵은 꼬리)을 구분하고, 시스템의 구조가 어느 영역에 속하는지를 가른다.

얇은 꼬리(thin tail) 영역에서는 어떤 한 사건도 전체 합을 흔들지 못한다. bottom-up으로 진화한 시스템 — 자연 생태계의 일상 변동, 인간 체중 분포 — 이 여기에 속한다. 자연의 경계(대륙·산맥·해양)와 종간 격리가 cascading 전파를 차단하기 때문이다.

![Fig 3 — Thin Tails from Tinkering, Bottom-Up, Evolution](/images/taleb-precautionary-principle-2014/fig3-thin-tails.png)
*Fig 3. 자연의 bottom-up 변동: 어떤 단일 변이도 전체 합의 큰 부분을 차지하지 못한다.*

굵은 꼬리(fat tail) 영역에서는 단 한 번의 큰 사건이 전체 합을 dominate한다. top-down으로 설계된 시스템 — 글로벌 금융 네트워크, monoculture 농업, 인공 invasive species, 팬데믹 — 이 여기에 속한다. 강한 상호의존성이 cascading 전파의 통로가 되기 때문이다.

![Fig 4 — Fat Tails from a Top-Down, Engineered Design](/images/taleb-precautionary-principle-2014/fig4-fat-tails.png)
*Fig 4. 인공 시스템의 굵은 꼬리: 단 한 번의 거대한 일탈이 전체 합을 거의 완전히 결정한다.*

PP가 발동되는 사분면은 *fat tail × systemic exposure*의 네 번째 사분면 하나뿐이다. 같은 위험이라도 thin tail 영역이면 표준 risk management로 충분하고, 굵은 꼬리이지만 국소적이면 정교한 risk management로 다룬다. 굵은 꼬리이면서 시스템적일 때만 PP의 영역이다.

| | Local Exposure | Systemic Exposure |
| --- | --- | --- |
| **Thin Tails** | I (안전) | II (계산된 위험으로 안전) |
| **Fat Tails** | III (엄격한 위험 관리로 안전) | IV (PP의 영역) |

Fragility는 이 영역에서 핵심 개념이 된다. 논문은 fragility를 "uncertainty에 의해 해를 입는 것"으로 정의하며, 그 수학적 표지는 *비선형 응답*이다. 10미터 낙하의 피해는 1미터 낙하 피해의 10배가 아니라 그 이상으로 가파르게 커지고, 같은 무게의 돌멩이를 한 번에 맞을 때가 여러 번 나누어 맞을 때보다 훨씬 치명적이다. 큰 충격 한 번이 작은 충격 1000번보다 더 큰 손해를 만들기 때문에 노출의 *집중*이 위험하다.

![Fig 5 — Nonlinear vs Linear Response](/images/taleb-precautionary-principle-2014/fig5-nonlinear.png)
*Fig 5. 비선형 응답과 선형 응답의 비교. 사건 크기가 임계를 넘는 순간 손해가 가파르게 발산한다.*

이 비선형성에서 1/n rule이 도출된다. 노출을 *상관 없는* n개의 출처로 분산시키는 것이 한 점에 집중하는 것보다 안전하다. 단 출처들이 서로 상관되어 있으면 분산 효과가 사라지므로, *상관 구조*가 분산 전략의 전제가 된다.

## 불확실성과 회의주의의 비대칭

논문이 가장 강하게 주장하는 결과 중 하나는 *불확실성이 클수록 PP가 강화된다*는 점이다. 이는 직관과 정반대로 보일 수 있다. "모델이 불확실하니 행동을 미루자"가 아니라 "모델이 불확실하니 더 빠르게 보수적으로 가자"는 결론이다.

수학적 이유는 단순하다. fat tail 분포에서 모델 불확실성이 커지면 분포의 꼬리가 *양쪽 모두* 두꺼워지지만, ruin은 한쪽 꼬리(왼쪽)에 자리 잡고 있고 그 꼬리가 *비대칭적으로* 빠르게 커진다. 즉 불확실성이 같은 비율로 늘어나도 ruin 확률 증가율이 이익 증가율보다 훨씬 가파르다.

![Fig 7 — Information Ratio와 Ruin Probability의 비대칭 (α=1, α=2, thin-tail equivalent)](/images/taleb-precautionary-principle-2014/fig7-uncertainty-ruin.png)
*Fig 7. 정보 비율(기대 이익/불확실성)이 변할 때 ruin 확률의 변화. fat tail (α=1, α=2) 분포는 thin tail에 비해 같은 정보 비율에서도 ruin 확률이 비대칭적으로 크다.*

논문은 이 결과를 기후 모델 회의론에 직접 적용한다. "기후 모델은 불확실하다"는 주장은 ruin 영역에서 *덜* 보수적이 아니라 *더* 보수적인 행동의 근거가 된다. skepticism은 모델 신뢰도를 낮추므로 분포의 꼬리를 두껍게 만들고, 이는 ruin 확률을 더 비대칭적으로 끌어올린다.

> More skepticism about models implies more uncertainty about the tails, which necessitates more precaution about newly implemented techniques, or larger size of exposures.

## PP에 대한 흔한 반론들과 응답

논문의 12장은 PP에 자주 제기되는 비판들을 항목별로 검토한다. 핵심 응답은 거의 모두 같은 한 줄로 압축된다 — *국소적·thin tail·복원 가능 사건*과 *시스템적·fat tail·비가역 사건*을 같은 자리에 놓아서는 안 된다.

- **Paralysis fallacy ("길 건너기도 위험하다")**: 도로 사고는 thin tail이며 인류 차원의 ruin을 일으키지 않는다. PP의 적용 영역과 다르다.
- **Russian roulette fallacy ("이번에도 살아남았으니 안전")**: ruin 영역에서 반례는 안전의 증거가 아니다. 도박꾼은 결국 파산한다는 결과가 한 번의 생존으로 무효화되지 않는다.
- **Loch Ness fallacy ("증거가 없으니 안전")**: absence of evidence는 ruin 영역에서 evidence of absence가 아니다. ruin 사건은 정의상 "한 번 일어나면 끝"이므로 표본이 거의 없는 상태에서 안전 추론이 불가능하다.
- **Carpenter fallacy ("당신은 생물학자가 아니지 않은가")**: GMO 위험을 평가하는 데 필요한 것은 생물학적 디테일이 아니라 *long sequence 확률 추론*이다. 도박꾼의 ruin 문제를 풀기 위해 도박꾼의 직업 경험이 필요한 것이 아닌 것과 같다.
- **Butterfly-in-China fallacy ("나비 한 마리가 지구를 멸망시킬 수 있다면 모든 행동이 위험")**: 결정론적 카오스의 나비 효과는 저차원 시스템에 한정된다. 지구처럼 fine-scale 자유도가 매우 큰 고차원 시스템에서는 미세 동요 대부분이 흡수된다. PP는 카오스에 의존하지 않고 *상호의존성과 fat tail 분포*에 의존한다.
- **Naturalistic fallacy의 오용**: 자연이 항상 좋다는 주장이 아니다. 자연은 30억 년의 통계적 검증을 거쳤으므로, 그 검증되지 않은 영역(transgenic·monoculture)에 갑작스럽게 진입하는 것이 *통계적*으로 위험하다는 것이다.

자료는 또한 *via negativa* 원칙을 제시한다. 복잡 시스템에 *추가*하는 개입은 의도하지 않은 cascading 결과(iatrogenics, 치료가 만드는 해)를 부르기 쉽다. Vioxx·Thalidomide·Fen-Phen 등 의료 사례가 보여주듯, 새 기술일수록 진화 검증된 해법에서 멀어져 iatrogenic 위험이 커진다. 따라서 fragilizing dependency를 *제거*하는 전략이 *추가*하는 전략보다 일반적으로 안전하며, PP는 추가 개입의 정당성에 더 높은 입증 부담을 지운다.

## 응용: GMO와 핵에너지의 차이

논문은 PP의 정밀한 적용 사례로 두 기술을 비교한다. 결론은 표면적으로 직관과 다르다 — GMO는 PP 영역, 핵에너지는 (대체로) 표준 risk management 영역이다.

**핵에너지**: 작은 규모의 핵 사용은 본질적으로 *국소적*이며, 그 위험 구조가 잘 연구되어 있다. 따라서 cost-benefit 분석이 의미 있게 적용된다. 단, 대규모 사용은 글로벌 영향 가능성이 커지므로 PP가 발동되며, 핵폐기물의 lifecycle 위험(수십만 년 지속되는 독성)은 PP 영역으로 분류된다.

**GMO**: 두 가지 점에서 시스템적이다. 첫째, 변형 유기체는 환경에 풀리면 통제 불가로 확산되며 야생종과의 교배로 disentangle이 불가능하다. 둘째, monoculture와 결합되어 cascading 실패의 통로를 만든다. 19세기 아일랜드 감자 기근은 이 메커니즘의 단순한 도식이다.

![Fig 8 — Monoculture와 감자 기근의 메커니즘 (Berkeley Understanding Evolution 자료에서 발췌)](/images/taleb-precautionary-principle-2014/fig8-monoculture.png)
*Fig 8. 다양한 작물 vs 클론 작물에 blight가 닥쳤을 때의 결과. 다양성은 부분 손실로 끝나지만 단일 클론은 전멸한다.*

논문은 GMO 옹호 논리 중 두 가지를 따로 반박한다.

- **"GMO는 전통적 선택 교배와 다르지 않다"**: 전통적 교배는 bottom-up 진화 과정의 *느린 변이*이며, 해로운 변이는 국소 경험으로 걸러진다. transgenic 조작은 이 진화적 검증 과정을 우회하므로 fat tail 분포를 만든다.
- **"GMO가 기근을 막는다"**: 세계 기아의 주된 원인이 농업 생산성이 아니라 분배·정책에 있다는 점을 지적하며, 위험을 감수해 또 다른 위험(기근)을 해결하려는 전략 자체의 비대칭성(Fig 7)을 비판한다. 미국 옥수수의 40%가 ethanol로 소비되는 현실이 그 사례다.

## 가장 흥미로운 지점

자료에서 가장 강하게 정리해두고 싶은 한 줄은 *불확실성이 클수록 ruin 영역에서는 더 보수적이어야 한다*는 비대칭이다. 일상 토론에서는 "모델이 불확실하니 행동을 미루자"와 "모델이 불확실하니 회의적이 되자"가 자주 같은 입장처럼 묶인다. 그러나 fat tail × systemic exposure 영역에서는 두 입장의 결론이 반대 방향을 가리킨다. skepticism은 분포의 꼬리를 두껍게 하고, 두꺼워진 꼬리는 ruin 확률을 비대칭적으로 끌어올린다. 회의는 행동을 늦추는 근거가 아니라 가속하는 근거가 된다.

또 하나 인상에 남는 점은 PP 자체가 *원칙의 원칙*이라는 메타 위치다. 논문은 PP가 "위험하면 피하라"가 아니라 "cost-benefit이 적용되는 영역의 경계를 그어라"라는 분류 도구임을 분명히 한다. PP의 가치는 *언제 적용하지 않는가*를 명확히 함으로써 보호되며, 이 분류가 흐려지는 순간 PP는 paralysis 비판에 정당하게 노출된다.

## 출처

- 저자: Nassim Nicholas Taleb (NYU School of Engineering), Rupert Read (University of East Anglia), Raphael Douady (CNRS Paris), Joseph Norman (NECSI), Yaneer Bar-Yam (NECSI)
- 발행: Extreme Risk Initiative — NYU School of Engineering Working Paper Series, 2014년 10월 17일 (arxiv 1410.5787v1)

[^abstract-arxiv]: 원문 abstract: <https://arxiv.org/abs/1410.5787>
[^arxiv]: 원문 PDF: <https://arxiv.org/pdf/1410.5787>
[^taleb-precautionary-principle-2014]: 본문 인용 그림은 모두 원문 논문에서 발췌했으며, 캡션의 출처 표기를 따른다.
