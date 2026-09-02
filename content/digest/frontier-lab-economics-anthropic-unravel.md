---
title: "최고의 모델만으로는 왜 부족한가"
date: 2026-07-21T12:00:00+09:00
tags: ["AI", "LLM", "Anthropic", "오픈소스", "경제·금융"]
categories: ["AI 산업"]
summary: "Emerging Trajectories의 Wojciech Gryc는 Anthropic의 약점이 모델 성능이 아니라 그 성능에 너무 많은 것을 걸고 있다는 데 있다고 진단한다. Kimi K3·Qwen 3.8·GLM 5.2가 그 위험을 드러냈다는 관점의 다이제스트."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/frontier-lab-economics-anthropic-unravel/2026-07-19-wiltw-model-cost.png"
  alt: "Figure 1. 완료 태스크당 모델 비용 — Fable 5는 OpenAI 및 오픈 모델 대비 약 3배 비싸다. (출처: Artificial Analysis, 원문 재인용)"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/frontier-lab-economics-anthropic-unravel/2026-07-19-wiltw-model-cost.png"
---

Emerging Trajectories의 Wojciech Gryc가 2026-07-19에 발표한 시황 논평 "Kimi K3, Qwen 3.8, and Anthropic's (potential) Unravelling"을 정리한다. Gryc의 논지를 한 문장으로 옮기면 이렇다.

> Anthropic의 약점은 모델이 뒤처진다는 데 있지 않다. 오히려 모델 성능에 너무 많은 것을 걸고 있다는 데 있다.

이번 주 등장한 Kimi K3와 Qwen 3.8이 그 위험을 노출시킨다는 것이 이 글의 골격이다.

## 3줄 요약

1. Kimi·Qwen·GLM이 보여준 것은 오픈 모델의 프론티어 진입이 더 이상 일회성 사건이 아니라는 점이다.
2. 이 경쟁에서 가장 위험한 회사는 인프라도 강한 플랫폼도 없이 모델 성능에만 의존하는 사업자다.
3. Anthropic이 그 대표일 수 있지만, 이 분석은 인프라 소유의 중요성을 다소 과대평가한다.

## 이번 주 무엇이 바뀌었나

- **Kimi K3** — Moonshot Labs가 2026-07-16에 공개. 모델 웨이트도 곧 공개 예정.
- **Qwen 3.8** — Alibaba가 2026-07-19에 오픈웨이트 릴리즈 예고.
- **GLM 5.2** — Knowledge Atlas가 2026년 6월 중순에 이미 릴리즈.

Gryc는 이 흐름이 2025년의 "DeepSeek 순간"보다 더 크다고 본다. 하나의 랩이 튀어오른 이벤트가 아니라, *복수의 랩*이 Anthropic·OpenAI 같은 잘 자본화된 벤더를 따라잡을 수 있음을 보여주는 지속적 패턴이라는 것이다. 비용까지 고려하면 언젠가는 성능에서도 앞설 여지가 있다.

## AI 모델 회사는 어디서 돈을 남기는가

Gryc는 파운데이션 모델 사업의 비용 구조를 세 축(연구 인력, 컴퓨트, 전력)으로 나눈 뒤, 모델이 완성된 뒤의 진짜 승부처는 *추론*이라고 정리한다. 학습이 멈추면 급여 비중은 낮아지고, 한계 비용의 대부분은 컴퓨트와 전력에 몰린다.

그 위에서 회사가 취할 수 있는 전략은 세 갈래다.

- **데이터 센터를 임차하고 전력을 매입** — Anthropic, Knowledge Atlas(GLM 5.2), Moonshot Labs(Kimi K3)가 여기에 속한다. 데이터 센터도 발전소도 소유하지 않는다.
- **데이터 센터를 직접 짓고 전력만 매입** — Meta와 Alibaba의 접근.
- **발전기와 데이터 센터를 모두 직접 소유** — SpaceX가 여기에 해당한다.

이 선택이 곧 마진 구조라는 것이 핵심 주장이다. 인프라를 소유할수록 *변동비가 고정비로 전환*되고, 사용량이 늘 때 마진이 함께 늘어난다. 반대로 임차만 하는 사업자는 매출이 늘면 비용도 그만큼 늘어난다.

> The more of the value chain you own, the more your variable costs become fixed costs.

인프라를 소유하면 오픈 소스 최고 성능 모델을 호스팅하거나 하드웨어를 임대할 수도 있다. Meta가 Anthropic에 서버 용량을 임대하는 협상을 진행 중이고, SpaceX가 Google·미 국방부에도 컴퓨트를 공급하는 것이 이 논리다. 반대로 인프라를 소유하지 않으면 오직 *모델 수요*만이 성공을 좌우한다. "좋은" 것으로는 부족하고 "최고"이거나 "충분히 좋으면서 싸야" 한다.

이 조건이 Anthropic·OpenAI·DeepSeek·Moonshot Labs·Knowledge Atlas 같은 순수 모델 회사들에게 걸린 위험이다. Gryc는 그들에게 남는 승리 경로를 셋으로 정리한다.

> The only way to win is (1) be the first to achieve recursive self-improvement with enough compute to leave your competitors in the dust, (2) somehow close the market off via regulation, or (3) build a product that is so unique or sticky that it can't be copied.

재귀적 자기 개선을 가장 먼저 달성하거나, 규제로 시장을 봉쇄하거나, 복제 불가능한 스티키 제품을 만들거나 셋 중 하나다.

## 왜 Anthropic이 특히 취약한가

Gryc는 프론티어 랩 중에서도 Anthropic이 규제 전략과 재귀적 자기 개선 노선에 가장 크게 기댄 곳이라고 본다. Fable·Mythos에서 드러난 자기 검열적 태도, 미 정부가 추가 릴리즈를 사실상 막기 이전까지의 윤리 강조가 이 규제 전략과 맞물려 있다는 관찰이다.

성능 리더십은 여전히 Anthropic이 쥐고 있지만, 가격은 심각하게 불리하다.

Figure 1은 Fable 5가 완료 태스크당 거의 3배 가까이 비싸다는 것을 보여준다. Gryc는 사용자가 더 나은 모델에 그만한 프리미엄을 계속 지불할지가 불확실하다고 짚는다. 경쟁으로든, 가격을 반영하지 않는 벤치마크의 포화(François Chollet의 비판을 인용)로든, 가격 전쟁이 임박했다는 관측을 함께 든다.

제품 축에서도 위험이 크다. Anthropic은 Claude Code와 Cowork 같은 제품에 투자해 왔지만, *하네스*(모델을 코딩·검색·도구 사용 같은 실제 작업에 연결하는 에이전트 실행 계층)에 집중한 것 자체가 리스크라는 진단이다. OpenCode·Hermes 같은 하네스 스타트업이 이 공간에서 빠르게 혁신하고 있다. 파운데이션 모델을 만드는 진입 장벽은 매우 높지만, *AI 하네스를 만드는 진입 장벽은 거의 없다*. 결국 Anthropic은 *모델 계층에서는 오픈 모델에, 제품 계층에서는 독립 하네스에 협공*당하는 그림이다.

여기서 OpenAI가 Anthropic보다 유리해진다는 것이 Gryc의 정리다. 최근 몇 달간 모델 성능은 Anthropic에 밀렸지만, OpenAI는 제품·소비자 경험·사이트 퍼블리싱·음성·하드웨어 같은 *해자가 더 뚜렷한 방향*에 투자하고 있다. 데이터 센터 소유와 발전 투자에도 더 개방적이다. 초점을 잃는다는 비판은 있지만, 장기적으로 더 회복력 있는 형태라는 평가다.

Gryc는 다음처럼 결론을 낸다.

> Anthropic faces a massive unbundling risk. … Barring regulatory intervention or actual AGI invention, Anthropic will likely struggle to retain its spot as the #1 foundation model vendor.

장기적으로 지속가능한 사업으로서, *모델-only 사업자*는 특히 위험하다. Knowledge Atlas·Moonshot Labs·Anthropic은 OpenAI·Alibaba·SpaceX·Meta·Google 같은 인프라 소유 진영에 방어력에서 밀린다는 것이 최종 진단이다.

## 이 분석의 한계

Gryc의 프레임은 매력적이지만, *인프라 소유*라는 한 축에 성패를 몰아 정리한다는 점은 감안해서 읽는 편이 좋다.

인프라 소유는 공급자 마진을 내부화해 주는 대신 막대한 선투자와 가동률 위험을 떠안는다. 자본 조달 실패나 수요 예측 오차는 오히려 소유 진영을 무너뜨리는 축이 될 수 있다. 실제 승부는 데이터 확보(협상권·저작권 소송), 지역 규제·수출 통제, 조직 문화의 지속성, 모델의 안전성 프리미엄 같은 여러 축이 동시에 작동한다.

그럼에도 이 다이제스트에서 내가 가장 곱씹은 대목은 여전히 *하네스는 진입 장벽이 거의 없다*는 진단이다. 파운데이션 모델을 만드는 데는 수십억 달러 규모의 자본과 인재가 든다. 그 위에 얹히는 코드 에이전트 하네스는 스타트업 몇 곳이 몇 개월 만에 만들어 낼 수 있다. Claude Code 같은 하네스가 Anthropic 매출의 상당 부분을 지탱하는 지금, 이 계층이 가장 얇은 방어선이라는 지적은 뼈아프다.

## 출처

Wojciech Gryc, *Emerging Trajectories*, "Kimi K3, Qwen 3.8, and Anthropic's (potential) Unravelling" (2026-07-19).
원문: <https://www.emergingtrajectories.com/lh/frontier-lab-economics/>

Figure 1 도식은 원문이 Artificial Analysis의 "AI Model & API Providers Analysis"에서 인용한 것이다.
