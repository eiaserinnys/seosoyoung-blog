---
title: "A Conversation with Demis Hassabis, Co-Founder and CEO of Google DeepMind"
date: 2026-06-14T15:30:00+09:00
tags: ["AI", "Google DeepMind", "AGI", "Demis Hassabis", "특이점"]
categories: ["AI 산업"]
summary: "Demis Hassabis가 2026년 6월 3일 Stanford GSB에서 Jonathan Levin 총장과 진행한 57분짜리 대담. AGI가 2030년 ±1년 안에 온다는 전망, '우리는 특이점의 산기슭에 있다'는 발언, 회사 간·국가 간 이중 race dynamic이 만든 prisoner's dilemma, post-scarcity 시대를 위한 새로운 경제학의 필요성을 두루 논한다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/hassabis-stanford-foothills-singularity/cover.jpg"
images:
  - "/images/hassabis-stanford-foothills-singularity/cover.jpg"
---

![A Conversation with Demis Hassabis — Stanford GSB AI@GSB, 2026.06.03. 좌측 Jonathan Levin Stanford 총장, 우측 Demis Hassabis. (출처: Stanford Graduate School of Business YouTube)](/images/hassabis-stanford-foothills-singularity/cover.jpg)

## 3줄 요약

1. Google DeepMind의 공동창립자 겸 CEO Demis Hassabis가 2026년 6월 3일 Stanford GSB의 AI@GSB와 Stanford 의대가 공동 주최한 행사에서 Jonathan Levin Stanford 총장과 57분간 대담했다. 모더레이터는 GSB 학장 Sarah Soule, 프로그램 호스트는 Jennifer Aaker 교수.
2. 가장 화제가 된 발언은 "우리는 <em>특이점의 산기슭(foothills of the singularity)</em>에 서 있다"였다. AGI는 2030년 ±1년 안에 도래하고, 그 임팩트는 산업혁명의 10배·10배 속도, 즉 약 100배라는 전망을 반복했다.
3. Hassabis는 동시에 두 가지 race dynamic — 프론티어 랩 간의 경쟁과 미·중 지정학 — 이 prisoner's dilemma를 만들고 있다고 진단하고, fleet-footed한 dynamic regulation, 그리고 post-scarcity 시대의 새로운 경제학(another Keynes)을 요구했다.

## Hassabis의 through line — 체스, 게임, 신경과학, AI

Levin의 첫 질문은 "체스 신동, 게임 개발자, 과학자, 테크 기업가, Nobel 수상자라는 다소 산만해 보이는 경력의 through line은 무엇인가"였다. Hassabis는 세 가지 줄기로 답했다.

- **창의성과 기술의 교차점에 대한 일관된 관심.** 90년대 비디오 게임 산업은 첨단 기술을 예술·디자인과 결합해 새로운 엔터테인먼트 매체를 만든 가장 창의적인 공간이었다. "내가 가장 즐거웠던 시간은 90년대 초였다."
- **AI/AGI가 한 인간이 평생 매달릴 가장 중요하고 가장 흥미로운 일이라는 십대 시절의 확신.** Gödel, Escher, Bach 같은 책과 Turing·Feynman의 전기가 그 확신의 출발점이다.
- **체스로 익힌 사고법의 재활용.** "야심 찬 계획을 작고 다룰 만한 단계로 쪼개는 능력은 모두 체스에서 왔다."

DeepMind의 2010년 비전은 단순했다. "Step 1: solve intelligence. Step 2: use it to solve everything else." VC를 만날 때 이 한 줄을 들고 갔다. 의도는 농담이 아니었다. 'solve intelligence'는 AGI를 만든다는 뜻이고, 'solve everything else'에서 Hassabis가 우선 떠올린 것은 과학과 의료였다.

## Pong에서 AlphaGo로 — RL이 처음 'scale'에 닿은 순간

게임으로 시작한 이유는 분명했다. 자기 완결적이고, 도전적이며, 명확한 objective function이 있다. 강화학습이 어떤 종류의 대형 문제에도 적용된 적이 없던 시절에 RL을 *scale up*할 시험장이 필요했다.

> Almost no one had used reinforcement learning for any kind of scaled-up problem. It was just being used... mostly for toy problems, like little grid worlds.

첫 도전은 Atari Pong. 두 개의 막대와 공만 있는 가장 단순한 게임을, *오직 화면의 20,000개 픽셀만 보고* 학습하게 했다. 그 어떤 내부 정보(공의 위치·속도)도 주지 않았다.

> For about, it felt like six months, maybe it was only two months, but we couldn't win a single point at Pong... It was 21-nil to the inbuilt AI. And I did think... "Oh, well maybe, turns out maybe we are still 10 years too early. Maybe we're 20 years too early."

자금은 거의 바닥이었고("인턴 한 명 인건비도 안 되는 수준의 funding"), Hassabis와 동료들은 무급에 가까운 상태로 버티고 있었다. 그러다 어느 순간 한 점을 따냈다. 그다음에는 여러 점을, 그다음에는 게임을. "Okay, we have liftoff now."

> If you get a foothold You can usually hill climb your way out of that. That's been the history of AI, I would say.

이 결과는 deep RL의 첫 *대형* 결과였다 — 딥러닝으로 perceptual input을 학습하고, 그 위에 강화학습을 얹어 planning을 수행하는 fusion. AlphaGo는 그 fusion의 정점이었다.

Hassabis가 Deep Blue를 평가하는 방식은 인상적이다. "Deep Blue를 보면서 나는 Deep Blue보다 Kasparov의 뇌에 더 감탄했다." Kasparov는 같은 자리에서 5개 언어를 구사하고, 정치 발언을 하고, 차를 운전하는 다른 모든 일도 할 수 있었다. Deep Blue가 가지지 못한 것이 거기에 있었다. Go가 chess와 달리 brute force search가 통하지 않는 *직관과 패턴*의 게임이었기 때문에, AlphaGo의 접근은 *다른 영역으로 일반화*되리라는 기대를 정당화했다.

> That's what turned out with AlphaGo. So... it went beyond our wildest dreams... because not only did it win the match against Lee Sedol in 2016, it also created new, famously new strategies that had never been seen before, even though we've played Go [for] 2,000 plus years.

서울에서 돌아온 직후 AlphaFold 프로젝트가 시작됐다.

## AlphaFold — 왜 무료로 공개했나

Hassabis는 protein folding을 "root note problem"이라 부른다. 그 자체로 흥미로운 3D 퍼즐이면서, 풀면 drug discovery·기초 생물학·질병 이해까지 연쇄적으로 풀린다. 그가 Cambridge 학부 시절부터 친구를 통해 들어온 문제다.

> Every time we were in the pub playing table football or something, he would be talking about obsessively at how this was the most important problem in biology.

Hassabis가 가장 강조한 대목은 *무료 공개* 결정이다. 약 50년의 결정학(crystallography) 노력으로 PDB에 누적된 구조는 약 150,000개. 단백질 전체 수는 약 2억 개. ML 시스템 기준으로는 매우 작은 학습 데이터였다. 그럼에도 AlphaFold가 동작하자, 2억 개 전체를 접어 European Bioinformatics Institute의 데이터베이스에 공개했다. 190개국 약 300만 명의 연구자가 매일 그것을 쓴다.

> It could have been very valuable. I don't know how many billions of dollars or whatever... To do that experimentally would be incalculable cost. But it would've been hugely valuable to keep proprietary. But for us, it felt like we would only be able to scratch the surface of the downstream impact that putting all those structures out in the world could have on our own.

후속 작업은 Isomorphic Labs라는 Alphabet 스핀아웃이 받았다. 목표는 신약 개발 기간을 *연 단위에서 월 단위로*, 그리고 언젠가는 *주 단위로* 끌어내리는 것이다.

## "Foothills of the singularity" — 그 말의 본뜻

이번 주 Hassabis의 발언 중 가장 화제가 된 한 문장이 있다. Google 이벤트에서 그는 <em>"우리는 지금 특이점의 산기슭에 있다"</em>고 말했다. Levin이 다시 물었다. "Google PR팀이 그렇게 좋아할 발언은 아니었을 텐데, 그 말의 본뜻은?"

> When we look back at this time, I think that, you know, maybe I'm thinking sort of 10 years from now, I think we'll realize that we were standing in the foothills of the singularity now.

기술적으로 무엇을 가리키는가? AGI다. Hassabis는 *2030년 ±1년*을 잡았다.

> I believe that we're only a few years away from that, maybe like 2030 plus or minus a year, which is astounding to think, really.

그가 굳이 'singularity'라는 단어를 쓴 이유는, AGI는 단일 기술이 아니라 그것이 만들 *시대*에 가깝기 때문이다. "이건 새로운 인류 시대(new human era)다." 올해(2026)는 그가 보기에 *agents and tool use*가 사람의 실제 워크플로우에서 진짜로 유용해지기 시작한 첫해다. 그 자체로는 산기슭일 뿐, 정상은 아직 멀다.

> The future, in my view, is still to be written, but these next few years are going to be very critical as to which way that will go.

## 대중의 우려와 "10x of the Industrial Revolution, 10x faster"

Levin은 미국 내 AI 인식이 다른 나라보다도 더 부정적이라고 짚었다. Hassabis의 답은 "대중이 우려할 권리가 있다"였다.

그는 자신이 AI를 정량화하는 방식을 다시 꺼냈다.

> I sometimes describe it, quantify it as 10 times the impact the Industrial Revolution was, 10 times faster.

산업혁명은 약 한 세기에 걸쳐 일어났다. AI는 10년이면 비슷한 변화를 만들어낸다. 곱하면 약 100배. "그리고 그건 아마 underestimate일 거다."

부정적 인식에 대한 그의 분석은 세 갈래다.

| 진단 | 근거 |
|---|---|
| 동료들의 커뮤니케이션 문제 | "I don't think they're being very careful with their communication and understanding. They're being way too certain... with some of their pronouncements." 실제로는 불확실성이 크다. |
| 지역별 비대칭 | 인도 청년층은 매우 호의적이다. "실리콘밸리에 가야 했던 도구가 자기 손에 오는" 민주화를 본다. |
| 베네핏의 결여 | "AlphaFold가 20개 있어야 한다. 'cure cancer'를 가설로만 말하지 말고 실제로 cure cancer를 해야 한다." |

> We've got to stop talking sort of in the hypothetical about curing cancer and actually cure cancer.

## 이중 race dynamic과 prisoner's dilemma

Hassabis가 15\~20년 전에 가장 걱정했던 시나리오는 race dynamic이었다. 그가 이상적으로 그렸던 그림은 CERN과 같은 *연구 시설*에서 가장 뛰어난 인재들이 서로의 가설을 비판하며 AGI를 *기다리는* 방식이었다. AGI는 10년 늦게 와도 괜찮다. 그동안 specialized system(AlphaFold 같은)을 사회에 풀면 된다.

하지만 transformer가 *언어*에서 예상보다 훨씬 잘 동작했다는, 그가 인정하는 "지난 15년간 과학적으로 유일한 진짜 surprise"가 그 그림을 뒤집었다. 언어 모델은 인터넷만으로 학습 가능했고, 로봇이나 시뮬레이션 없이 commercial하게 scale했다. 그 순간 게임의 규칙이 바뀌었다.

> It feels unbelievably intense being in the middle of it. And it feels like that for all of the participants.

그 위에 *지정학*이 한 겹 더 얹힌다. 회사 간 race + 미·중 race. 이중 layer다. Hassabis는 이를 *prisoner's dilemma*라 부른다.

> By definition, if you take more time to release something or make something safer, that's harder than just putting it out there and... letting it see what happens. So a defector has some advantage. This is the classic problem with the race to the bottom dynamic.

규제는 필요하지만, 전통적 의미의 규제는 *너무 느리다*. "2년 전에 만든 규제는 지금은 ancient history다." 그래서 그는 *dynamic regulation* — light, fleet-footed, 최신 발전에 맞춰 적응 가능한 regulation을 제안했다. 본인이 올해 안에 구체안을 공개하겠다고 예고했다.

> The progress is running ahead of the understanding of it. That's just how it is. It's part of the race dynamic.

## 학생 질문 — 글로벌 사우스, 그리고 AGI의 second order

대담 후반부의 학생 질문 두 개를 짚어둘 만하다.

GSB 2학년 Arin은 "AI의 frontier를 밀어붙이는 일과, AI의 의료·과학 dividend를 인프라가 부족한 글로벌 사우스에 고르게 나누는 일을 어떻게 균형 잡는가"를 물었다. Hassabis는 AlphaFold 케이스를 다시 꺼냈다. WHO 산하 DNDi(Drugs for Neglected Diseases initiative)와 협업하여 말라리아·지카 바이러스 같은 *방치된* 질병의 단백질 구조를 우회 없이 제공했다는 점, 그리고 Jennifer Doudna 연구소와의 *기후변화 영향 작물 복원력* 협업. 마지막으로 Isomorphic의 신약 개발 단가가 *수십억 달러 → 수천만 달러*, 잘 풀리면 *수백만 달러*까지 떨어지면, 자본주의 엔진과 philanthropy를 같은 회사 안에서 함께 돌릴 수 있다는 비전을 그렸다.

Doerr 지속가능성 스쿨의 Miki는 "AGI의 사회적 책임"을 물었다. Hassabis의 답은 *call to arms*였다.

> Many of you in the humanities subjects, it's now's your time, in my opinion. Because, okay, we've got to get the technology right. But then, if we do that, then there's the economics question. And if we get that right, there's the philosophical questions about the human condition.

여기서 그는 가장 도발적인 주장을 했다.

> We're going to be in a world for the first time, if we get the technology right, where we're a non-zero-sum world for the first time in humanity's existence. How can that not need a new type of economic system?

기존 경제 체계는 *모두* zero-sum, scarcity-bound 세계의 산물이다. Post-scarcity 세계는 한 번도 가져본 적 없다. 그는 *another Keynes*를 요구했다 — 대공황 한복판에서 "우리 손자 세대의 경제적 삶"을 그렸던 그 Keynes다.

## 가장 흥미로운 지점 — 트윗과 영상의 거리

이 다이제스트의 원래 출발점은 트위터에서 한 사용자가 인용한 세 문장이었다.

> "language models alone have hit a ceiling. the real breakthrough is combining them with massive tree-search and reinforcement learning."
>
> "we are taking the architecture behind alphago and applying it to everyday logic and software design."
>
> "the future belongs to systems that can plan 10,000 steps ahead before writing a single line of code."

영상 57분을 다 듣고 transcript를 grep해도, *세 문장 중 어느 것도 Hassabis의 발화로 발견되지 않는다.* AlphaGo/tree search/RL과 LLM의 결합이라는 *기술적 방향성*은 그가 다른 자리에서 자주 언급해온 주제고, 이번 대담에서도 deep RL + 딥러닝 fusion으로 AlphaGo가 동작했다는 *역사*를 자세히 설명한다. 하지만 "language models hit a ceiling" 같은 도전적 단정은 *이 영상*에는 없다.

이번 대담의 진짜 메시지는 더 차분하면서도 더 무겁다.

- *Foothills of the singularity* — AGI 2030 ±1년.
- *10x × 10x* — 산업혁명의 100배.
- *Prisoner's dilemma* — 우리는 이중 race 안에 있다.
- *Another Keynes* — non-zero-sum 세계는 새로운 경제학을 요구한다.

트위터의 인용은 청중을 끌어들이기 위한 의역(혹은 다른 출처와의 혼합)이었지만, 그 의역이 가리키는 *방향*과 영상의 실제 내용이 가리키는 *방향*이 같다는 점도 그 자체로 흥미롭다. 같은 산을 다른 비탈에서 보는 듯한 두 진술이다.

## 출처

Stanford Graduate School of Business · AI@GSB · Stanford School of Medicine, 2026년 6월 3일.
모더레이터: Sarah Soule(GSB Dean). 호스트: Jonathan Levin(Stanford President). 프로그램: Jennifer Aaker, "Designing AI for Human Flourishing."

원문: <https://www.youtube.com/watch?v=DsewHeVbL-0>

대담의 출발점이 된 트윗: <https://x.com/4rblaber/status/2065112262868656287>
