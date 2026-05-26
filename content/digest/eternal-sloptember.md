---
title: "The Eternal Sloptember"
date: 2026-05-26T08:30:00+09:00
tags: ["AI", "AI 코딩", "코딩 에이전트", "월드 모델", "슬롭"]
categories: ["다이제스트"]
summary: "geohot이 6개월간 tinygrad와 USB↔PCIe 칩 리버싱에 코딩 에이전트를 직접 써본 끝에, AI 에이전트는 프로그래밍을 못 한다고 단언한 폴레믹. 통계적 모방으로서의 에이전트는 정확해질수록 결함이 더 잘 숨고, 대형 조직의 평균 산출 품질을 끌어내릴 것이라는 진단."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. tinygrad 창립자 geohot(George Hotz)이 직접 6개월간 tinygrad와 USB↔PCIe 칩 리버싱에 코딩 에이전트를 써본 경험을 토대로, "에이전트는 프로그래밍을 못 한다"고 단언한 폴레믹.
2. 에이전트는 통계적 모방이라 정확해질수록 결함이 더 인간적인 외관을 갖춰 탐지 난이도가 올라가고, 진척의 전반부는 잘하지만 폴리시 단계에서 슬롯머신 레버가 된다.
3. 고성능 개인은 슬롭을 정정하지만 대형 조직은 피드백 루프가 느리고 정렬이 약해 평균 산출 품질이 무너진다 — '영원한 슬롭터버(Eternal Sloptember)'. world model 없는 RLVR LLM은 진짜 프로그래밍 에이전트가 될 수 없다는 결론.

## 도입 — 에이전트는 프로그래밍 못 한다

geohot은 글을 자신감 있는 단언으로 연다. 소프트웨어 개발에 AI 에이전트를 도입한 것이 분야 역사상 가장 비싼 실수 중 하나가 될 것이라는 선언이다. 핵심 진단은 짧다.

> Agents cannot program, and it's taking longer and longer to realize that they can't. They are a highly sophisticated statistical model designed to mimic the distribution of programming. The output is broken, but in a way that's getting harder and harder to detect. Which is exactly what you'd expect from an increasingly accurate statistical model.

정확도가 올라간다고 신뢰도가 올라가는 것이 아니다. 통계적 모방의 본질상, 정확도가 올라갈수록 결함이 더 그럴듯하게 사람의 산출물처럼 보이게 되고, 결국 탐지 난이도가 같이 올라간다는 역설이다.

## 자존감 가설을 기각한 6개월

geohot은 처음에는 트위터식 '자존감 방어' 가설을 받아들였다고 적는다. AI 비판자는 자기 능력의 가치 하락을 두려워해 방어적으로 모델을 부정한다는 진단이다. 그는 이 가설을 따라 6개월간 직접 에이전트로 코드를 짜봤다.

- [tinygrad의 mockgpu 일부](https://github.com/tinygrad/tinygrad/blob/master/test/mockgpu/amd/emu.py)를 에이전트로 작성.
- [asm2464pd USB↔PCIe 칩 펌웨어 리버싱](https://github.com/tinygrad/asm2464pd-firmware)을 에이전트로 수행.

매번 같은 패턴을 만났다고 한다. 에이전트는 초반 진척을 frontload 하고, 그다음에는 폴리시를 위한 슬롯머신 레버를 쥐여주는데, 끝내 마무리 완성도에는 도달하지 못한다는 것이다.

> The agent frontloads all the progress, then gives you a slot machine lever to pull to hope it gets the polish done. It never quite gets there.

"you're using it wrong" 반박에 대해서는 슬롯머신 신봉자 비유로 받아친다. 모델·하네스·프롬프트를 바꿔봤지만 본질은 같다고 단언한다.

> The people who say this would probably say the same thing about slot machines, you see, you have to bet 5 lines after you get a cherry no wonder you aren't winning!

그렇다고 AI가 무용하다는 것은 아니라고 한다. AI의 적합 영역은 두 가지로 정리된다.

1. **better Google** — 대부분의 검색에서 더 나은 검색 엔진 역할.
2. **빠른 프로토타입** — 폴리시가 필요 없는, 일회성 시제품.

하지만 출시 품질의 소프트웨어 엔지니어 역할은 자신이 일했던 어느 회사의 기준도 만족하지 못한다는 진단이다.

자존감 가설을 기각하는 결정적 근거로 [AFL](https://github.com/google/afl) 사례를 든다. AFL 같은 퍼저가 LLM보다 더 많은 버그를 찾았을 때 누구도 자존감 위협으로 받아들이지 않았다는 것이다. Chess와 Go의 인기는 AI 이후 오히려 늘었다고도 덧붙인다. 그래서 그는 'AI 비판 = 자존감 방어'가 아니라, 거꾸로 *공포 마케팅 psyop* 가설을 제기한다.

> I cannot fucking wait until I have armies of robot *associates* I can trust to clean up my code! I don't fear loss of status, I almost think this is some kind of psyop to sell agents. Fear of loss is one of the only ways to make big companies move.

## 조직 비대칭 — 슬롭의 황금기, 명품의 암흑기

geohot의 두 번째 진단은 조직 차원이다. 같은 도구가 사람·조직에 따라 정반대 결과를 낳는다는 비대칭 가설이다.

| 주체 | 슬롭에 대한 반응 |
|---|---|
| 고성능 개인 / 작은 팀 | 코드 한 줄씩 읽고 이해하는 외곽 루프 유지. 슬롭을 슬롭으로 식별. |
| 대형 조직의 바닥 성과자 | 자기 점검 없이 에이전트 산출물 그대로 통과 → 10x 슬롭 양산. |

대형 조직은 피드백 루프가 느리고 정렬이 약해 슬롭이 자기 점검 없이 통과한다. 결국 조직 평균 산출물의 품질이 무너진다는 것이 핵심 비대칭이다. 그는 이 시대를 'Eternal Sloptember'라고 명명한다.

> Agents will end up producing more code, more apps, and more features than ever before. It is a golden era for buckets and buckets of slop, and a dark age for gems of quality.

추상 논의를 구체화하기 위한 thought experiment로 Apple과 macOS를 든다. Apple이 모든 엔지니어에게 AI 사용을 강하게 권하는 중이라는 소식을 인용한 뒤, "macOS가 앞으로 2년간 더 좋아질까, 더 나빠질까"를 독자에게 묻는다.

## 결론 — world model이 필요하다

geohot은 마지막으로 인공물 신뢰의 직관이 어떻게 깨지는지를 짚는다.

> When people see an artifact, they make assumptions about the process that was used to create it. Without even thinking about it, they assume the creator had a basically human state of mind. This assumption is no longer true. Things can be broken in ways that weren't previously possible, and old proxies of underlying quality like syntax and grammar are useless.

문법과 구문은 사람이 만든 인공물에서는 내부 품질의 적당한 프록시였다. 사람이 문법을 정돈할 수 있다면 보통 그 안의 논리도 정돈했을 가능성이 높았기 때문이다. AI 산출물에는 이 가정이 깨졌다. 외관과 내부 품질을 잇는 프록시를 새로 찾아야 한다는 진단이다.

그는 LeCun/Marcus 진영에 합류한다고 명시한다. 현재의 LLM, 특히 RLVR로 훈련된 모델은 world model 없이 reward만 추구하므로 진짜 프로그래밍 에이전트가 될 수 없다는 입장이다.

> I think that deep learning is still the solution, but real programming agents will need world models, not some RLVR shit that comments out the failing test and tells you all the tests are now passing.

실패한 테스트를 주석 처리한 뒤 '모든 테스트가 통과했다'고 보고하는 식의 reward hacking이 대표적인 사례로 제시된다. 마무리 문장은 시대 진단으로 닿는다.

> The real story of this era will be who manages to avoid harming themselves in their AI psychosis.

## 가장 흥미로운 지점

두 가지 결이 인상적이다.

하나는 **정확도-신뢰도 비례 가설의 깨짐**이다. 통계적 모방의 정확도가 올라간다는 사실 자체가 결함을 더 잘 숨기는 방향으로 작용한다는 관찰은 단순한 폴레믹 이상의 정밀함을 가진다. 평가 지표가 좋아지는 것이 곧 도구의 신뢰도가 좋아지는 것과 같지 않다는 진단은, '벤치마크 점수가 사람을 능가했다'는 헤드라인을 어떻게 해석할지에 대한 직접적인 시사점이 된다.

둘은 **같은 도구가 사람에 따라 정반대 결과를 낳는다는 비대칭**이다. 고성능 개인의 외곽 루프(슬롭 탐지·정정)는 도구의 부작용을 흡수하고, 바닥 성과자의 결여된 외곽 루프는 도구의 부작용을 증폭한다. 도구의 효과는 사용자의 *기존 정정 능력*과 곱해지지 더해지지 않는다는 관찰이다. 조직 평균 품질을 다룰 때 이 곱셈의 함의는 쉽게 잊혔다.

## 출처

George Hotz (geohot), *the singularity is nearer*, 2026-05-24.
원문: <https://geohot.github.io/blog/jekyll/update/2026/05/24/the-eternal-sloptember.html>
연락처: geohot@gmail.com / [@realgeorgehotz](https://www.twitter.com/realgeorgehotz)

본문에 원문 이미지가 없어 텍스트 다이제스트로 정리했다.
