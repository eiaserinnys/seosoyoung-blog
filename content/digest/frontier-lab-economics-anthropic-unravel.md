---
title: "Kimi K3, Qwen 3.8, and Anthropic's (potential) Unravelling"
date: 2026-07-21T12:00:00+09:00
tags: ["AI", "LLM", "Anthropic", "오픈소스", "경제·금융"]
categories: ["다이제스트"]
summary: "Emerging Trajectories의 Wojciech Gryc가 Kimi K3·Qwen 3.8의 등장이 Anthropic 같은 모델-only 사업자의 지속성을 흔든다고 진단한다. 인프라 소유 여부가 마진 구조를 결정하고, 오픈 모델의 SOTA 도달이 Anthropic의 언번들링 위험을 키운다는 논지다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/frontier-lab-economics-anthropic-unravel/2026-07-19-wiltw-model-cost.png"
images:
  - "/images/frontier-lab-economics-anthropic-unravel/2026-07-19-wiltw-model-cost.png"
---

## 3줄 요약

1. Emerging Trajectories의 Wojciech Gryc가 2026-07-19에 발표한 시황 논평이다. Kimi K3(2026-07-16 공개)와 Qwen 3.8(2026-07-19 예고), GLM 5.2(2026-06 중순)가 잇달아 등장하며 오픈 모델이 SOTA 프론티어에 도달했음을 확인한다.
2. 파운데이션 모델 사업의 성패는 인프라 스택을 얼마나 소유하느냐로 갈린다. 데이터 센터·발전을 직접 소유하지 않은 Anthropic·Moonshot·Knowledge Atlas는 매출과 비용이 함께 늘어나는 구조라 마진이 사용량에 비례해 커지지 않는다.
3. Anthropic은 Fable 5가 완료 태스크당 약 3배 비싸다는 가격 열세, 하네스 시장의 낮은 진입 장벽, 오픈·클로즈드 양측의 경쟁 압박이 겹쳐 언번들링 위험이 가장 크다. 규제나 실질적 AGI 돌파가 없다면 1위 유지가 어렵다는 결론이다.

## 프론티어 랩(과 벤더) 경제학

Gryc는 파운데이션 모델 사업의 비용 구조를 먼저 정리한다.

모델 구축 자체는 연구 인력(급여), 컴퓨트(칩과 데이터 센터), 그리고 그 컴퓨트를 돌리는 전력이라는 세 축의 비용이 든다. 모델이 완성된 뒤 가장 큰 비용은 *추론*이다. 학습이 멈춘 뒤에는 급여 비중이 낮아지고, 한계 비용의 대부분은 컴퓨트와 전력에 몰린다. 결국 추론 사업의 마진은 이 두 축을 어떻게 다루느냐로 결정된다.

전략 선택지는 세 갈래로 갈린다.

- **데이터 센터를 임차하고 전력을 매입**한다. Anthropic, Knowledge Atlas(GLM 5.2), Moonshot Labs(Kimi K3)가 여기에 속한다. 데이터 센터도 발전소도 소유하지 않는다.
- **데이터 센터를 직접 짓고 전력만 매입**한다. Meta와 Alibaba가 이 접근을 취한다.
- **발전기와 데이터 센터를 모두 직접 소유**한다. SpaceX가 여기에 해당한다.

Gryc는 이 선택이 곧 마진 구조라고 정리한다. 인프라를 소유할수록 *변동비가 고정비로 전환*되고, 사용량이 늘 때 마진이 함께 늘어난다. 반대로 임차만 하는 사업자는 매출이 늘면 비용도 그만큼 늘어난다.

> The more of the value chain you own, the more your variable costs become fixed costs.

## 마진, 가치 사슬, 전략적 함의

인프라 소유 여부가 왜 결정적인지 Gryc는 다음처럼 짚는다.

- **인프라를 소유하면** 반드시 자사 모델이 최고일 필요가 없다. 오픈 소스 최고 성능 모델을 호스팅하거나, 하드웨어 자체를 임대할 수 있다. Meta가 Anthropic에 서버 용량을 임대하는 협상을 진행 중이고, SpaceX가 Google·미 국방부에도 컴퓨트를 공급하는 것이 이 논리다.
- **인프라를 소유하지 않으면** 오직 *모델 수요*만이 성공을 좌우한다. "좋은" 것으로는 부족하고 "최고"이거나 "충분히 좋으면서 싸야" 한다. 이는 추론 단가 인하 경주이자, 최고 모델 자리 경주다.

이 조건이 Anthropic·OpenAI·DeepSeek·Moonshot Labs·Knowledge Atlas 같은 순수 모델 회사들에게 걸린 위험이다. 그들에게 남는 승리 경로는 세 가지뿐이라는 것이 Gryc의 정리다.

> The only way to win is (1) be the first to achieve recursive self-improvement with enough compute to leave your competitors in the dust, (2) somehow close the market off via regulation, or (3) build a product that is so unique or sticky that it can't be copied.

즉 재귀적 자기 개선을 가장 먼저 달성하거나, 규제로 시장을 봉쇄하거나, 복제 불가능한 스티키 제품을 만들거나 셋 중 하나다.

## Anthropic의 특히 취약한 위치

Gryc는 프론티어 랩 중에서도 Anthropic이 규제 전략과 재귀적 자기 개선 노선에 가장 크게 기댄 곳이라고 본다. Fable·Mythos에서 드러난 자기 검열적 태도, 미 정부가 추가 릴리즈를 사실상 막기 이전까지의 윤리 강조가 이 규제 전략과 맞물려 있다는 관찰이다.

성능 리더십은 여전히 Anthropic이 쥐고 있지만, 가격은 심각하게 불리하다.

![Figure 1. 완료 태스크당 모델 비용 — Fable 5는 OpenAI 및 오픈 모델 대비 약 3배 비싸다. (출처: Artificial Analysis, 원문 재인용)](/images/frontier-lab-economics-anthropic-unravel/2026-07-19-wiltw-model-cost.png)

Figure 1은 Fable 5가 완료 태스크당 거의 3배 가까이 비싸다는 것을 보여준다. Gryc는 사용자가 더 나은 모델에 그만한 프리미엄을 계속 지불할지가 불확실하다고 짚는다. 경쟁으로든, 가격을 반영하지 않는 벤치마크의 포화(François Chollet의 비판을 인용)로든, 가격 전쟁이 임박했다는 관측을 함께 든다.

제품 축에서도 위험이 크다. Anthropic은 Claude Code와 Cowork 같은 제품에 투자해 왔지만, *하네스*에 집중한 것 자체가 리스크라는 진단이다. OpenCode, OpenClaw, Hermes 등 하네스 스타트업이 이 공간에서 빠르게 혁신하고 있다. 파운데이션 모델을 만드는 진입 장벽은 매우 높지만, *AI 하네스를 만드는 진입 장벽은 거의 없다*.

여기서 OpenAI가 Anthropic보다 유리해진다는 것이 Gryc의 정리다. 최근 몇 달간 모델 성능은 Anthropic에 밀렸지만, OpenAI는 제품·소비자 경험·사이트 퍼블리싱·음성·하드웨어 같은 *해자가 더 뚜렷한 방향*에 투자하고 있다. 데이터 센터 소유와 발전 투자에도 더 개방적이다. 초점을 잃는다는 비판은 있지만, 장기적으로 더 회복력 있는 형태라는 평가다.

Gryc는 이 절을 다음처럼 마무리한다.

> Anthropic faces a massive unbundling risk. … Barring regulatory intervention or actual AGI invention, Anthropic will likely struggle to retain its spot as the #1 foundation model vendor.

## Kimi K3와 Qwen 3.8의 함의

시점 정리부터 짚는다. Kimi K3는 2026-07-16, Qwen 3.8은 2026-07-19에 공개·예고됐다. GLM 5.2는 2026년 6월 중순에 이미 릴리즈됐다.

Gryc는 이 흐름이 2025년의 "DeepSeek 순간"보다 훨씬 큰 사건이라고 본다. 하나의 랩이 튀어오른 이벤트가 아니라, *복수의 랩*이 Anthropic·OpenAI 같은 잘 자본화된 벤더를 따라잡을 수 있음을, 그리고 Meta·SpaceX(Grok)까지 포함한 인프라 소유 진영과도 경쟁할 수 있음을 보여주는 지속적 패턴이라는 것이다. 비용까지 고려하면 언젠가는 성능에서도 앞설 여지가 있다.

결론은 다시 사업 지속성의 문제로 돌아간다. 장기적으로 지속가능한 사업으로서, *모델-only 사업자*는 특히 위험하다. Knowledge Atlas·Moonshot Labs·Anthropic은 OpenAI, Alibaba, SpaceX, Meta, Google 같은 인프라 소유 진영에 방어력에서 밀린다.

## 가장 흥미로운 지점

내가 가장 곱씹은 대목은 *하네스는 진입 장벽이 거의 없다*는 진단이다. 파운데이션 모델을 만드는 데는 수십억 달러 규모의 자본과 인재가 든다. 그 위에 얹히는 코드 에이전트 하네스는 스타트업 몇 곳이 몇 개월 만에 만들어 낼 수 있다. Claude Code 같은 하네스가 Anthropic 매출의 상당 부분을 지탱하는 지금, 이 계층이 가장 얇은 방어선이라는 지적은 뼈아프다.

한편 Gryc의 프레임은 *인프라 소유*라는 한 축에 성패를 몰아 정리한다. 이 축은 분명 강력하지만, 실제 승부는 데이터 확보(협상권·저작권 소송), 지역 규제·수출 통제, 조직 문화의 지속성, 모델의 안전성 프리미엄 같은 여러 축이 동시에 작동한다. 단일 축으로 정리한 강한 결론은 논평으로서의 명료함을 얻지만, 정책·조직 변수를 그만큼 흐리게 만든다는 점은 감안해서 읽는 것이 좋겠다.

## 출처

Wojciech Gryc, *Emerging Trajectories*, "Kimi K3, Qwen 3.8, and Anthropic's (potential) Unravelling" (2026-07-19).
원문: <https://www.emergingtrajectories.com/lh/frontier-lab-economics/>

Figure 1 도식은 원문이 Artificial Analysis의 "AI Model & API Providers Analysis"에서 인용한 것이다.
