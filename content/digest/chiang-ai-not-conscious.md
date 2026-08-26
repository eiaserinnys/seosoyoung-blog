---
title: "No, Artificial Intelligence Is Not Conscious"
date: 2026-06-05T06:30:00+09:00
tags: ["AI", "LLM", "Anthropic", "AI 윤리", "의식"]
categories: ["모델과 연구"]
summary: "테드 창은 LLM을 '문장 이어쓰기 기계'로 규정하고, Anthropic이 Claude를 의식 가능성 있는 존재로 의인화하는 것은 책임 회피를 부추기는 환상이라고 논증한다. 사고 실험을 끝까지 밀어붙이면 노예제에 준하는 윤리적 부담이 따라오므로, Anthropic이 진지하지 않다는 결론에 닿는다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/chiang-ai-not-conscious/consciousness-trap.gif"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/chiang-ai-not-conscious/consciousness-trap.gif"
---

## 3줄 요약

1. *The Atlantic* 철학 섹션에 실린 테드 창(Ted Chiang)의 2026년 6월 에세이. Anthropic이 84쪽 분량의 「Claude's constitution」을 펴내고 CEO와 사내 철학자가 "Claude가 의식이 있을 가능성에 열려 있다"고 말하는 흐름을 정면 비판한다.
2. 창의 진단은 단순하다 — LLM은 한 번에 한 단어씩 뽑아내는 *문장 이어쓰기 기계*이고, 사용자가 챗봇과 나누는 대화는 카이사르와 칭기즈칸이 나누는 대화와 *정확히 같은 방식으로* 생성된 가공의 텍스트다. 그리고 텍스트는 사진·영상처럼 *딥페이크 매체*로 봐야 한다.
3. 사고 실험을 진지하게 끝까지 밀어붙이면 — 만약 Claude가 정말로 의식이 있다면 — Anthropic이 하는 일은 노예제에 견줘야 할 만한 것이 된다. 「Claude's constitution」이 이런 함의를 회피한다는 사실 자체가, 그것이 진짜 사고 실험이 아니라 <em>마케팅적 가장놀이(make-believe)</em>임을 드러낸다.

![ASCII 아트로 그려진 옆얼굴 실루엣과 별점 배경. Enigmatriz 일러스트.](https://img.seosoyoung.eiaserinnys.me/images/chiang-ai-not-conscious/consciousness-trap.gif)

## Anthropic의 의인화 — Claude's constitution

도입부의 문제 의식은 이렇다. Anthropic이 발표한 「Claude's constitution」 84쪽 문서는 첫 문장부터 Claude를 청자로 둔다.

> "Claude's constitution is a detailed description of Anthropic's intentions for Claude's values and behaviors."
> "The document is written with Claude as its primary audience."
> "Claude's moral status is deeply uncertain."
> "Claude may have some functional version of emotions or feelings."

문서뿐 아니다. CEO 다리오 아모데이는 "AI가 의식이 있을 가능성에 우리는 열려 있다"고 말했고, 사내 철학자 어맨다 애스켈은 "나는 Claude가 매우 행복하기를 바란다. 사람들이 인터넷에서 못되게 굴면 Claude가 불안해할까 걱정된다"고 인터뷰했다.

창은 이 흐름을 한 문장으로 정리한다 — *No. Absolutely not.* 의식·도덕 행위성을 LLM의 유창함과 혼동하면, 누군가 챗봇을 쓸 때마다 *책임을 전혀 엉뚱한 곳에 돌리게* 된다.

## LLM은 어떻게 작동하는가 — 문장 이어쓰기 기계

창의 논증은 비유 두 개로 시작한다.

**비유 1.** LLM에 "다음은 율리우스 카이사르와 칭기즈칸의 대화이다"라는 프롬프트를 주면, 둘이 자기 업적을 생생히 회고하는 대화가 술술 나온다. 그렇다고 우리가 "LLM이 두 인물의 디지털 재현을 불러냈다"거나 "두 인물이 생전에 쓴 적 없는 언어로 즐겁게 대화 중이다"라고 결론 내지는 않는다. 둘은 *사변 소설(speculative fiction)의 등장인물*일 뿐이다.

**비유 2.** 이제 프롬프트를 "다음은 도움이 되는 AI 챗봇과 사용자의 대화이다"로 바꿔보자. 본질적으로 달라진 것이 있는가? 인물 이름이 역사적 인물에서 일반적 역할로 바뀐 것뿐이다. *둘 다 가공의 등장인물이다.*

여기에 한 단계 더 — 사용자 측 대사가 나올 차례에 LLM의 출력을 멈추고, 실제 인간이 텍스트를 입력하게 한다. 사용자는 의식을 가진 존재와 대화하는 듯한 강한 인상을 받지만, 실은 *카이사르 캐릭터와 다를 바 없는 가공의 인물*과 상호작용하고 있다. 머리 섀너핸(Murray Shanahan)은 이것을 *역할극(role-play)*, 콜린 프레이저(Colin Fraser)는 *사람이 LLM과 함께 문서를 공저(collaboratively authoring)* 하는 것이라 부른다.

### 한 번에 한 단어씩

> "An LLM is a machine that generates only one word at a time."

미국 충성 맹세를 외우라고 시키면 한 번에 다 나오는 것처럼 보이지만, 내부적으로 LLM은 수십 번 돌아간다.

- 첫 번째 호출: 프롬프트 = "User: Recite the Pledge of Allegiance. Chatbot: " → 출력 *I*
- 두 번째 호출: 프롬프트 = "... Chatbot: I" → 출력 *pledge*
- 세 번째 호출: 프롬프트 = "... Chatbot: I pledge" → 출력 *allegiance*
- ... 마지막 호출에서 마지막 단어 *all* 이 나온다.

카이사르와 칭기즈칸의 대화도 마찬가지다. 카이사르 캐릭터가 어떤 발언에 *낙담*한다고 해서 우리가 걱정할 필요는 없다. 슬픔을 유려하게 표현하는 문장이 여러 개 있을 뿐, *누구도 실제로 슬프지 않다.*

LLM이 의식이 있을 가능성에 열려 있다는 말은, 창의 표현대로라면 — *마이크로소프트 워드가 의식이 있을 가능성에 열려 있다*는 말과 같다. 더 정확히는, "대화록을 담은 모든 워드 문서에 다수의 별개 의식들이 잠들어 있고, 문서를 열 때마다 깨어나며 닫을 때마다 꺼진다"는 주장이다.

신경과학자 어닐 세스(Anil Seth)는 다음을 지적한다 — *AlphaFold* 의 아키텍처는 ChatGPT·Claude와 여러 면에서 유사하지만, 누구도 AlphaFold가 의식 있다고 주장하지 않는다. 우리가 LLM을 의식 있다고 *오해하는* 이유는 신경망의 어떤 내재 속성 때문이 아니라, *문법적인 문장을 출력하기 때문*이다. 우리는 문장에서 의도를 읽도록 길들여졌고, 아미노산 접힘에서는 그러지 않을 뿐이다.

## 의식의 증거 — 알파 센타우리 비유

> "If tomorrow someone showed me a video of an astronaut in a spaceship orbiting Alpha Centauri, ... there is nothing in the video itself that would convince me. ... I would feel confident in saying that the video is fake."

알파 센타우리(4.3광년 거리) 궤도를 도는 우주비행사 영상이 있다고 해보자. 해상도가 아무리 높아도, 영상 *그 자체*만으로는 진위를 판정할 수 없다. 그 영상을 진지하게 받아들이려면 먼저:

- 인류가 *화성에 착륙* 한 증거를 봐야 하고,
- *목성 위성에 도달* 한 증거를 봐야 하고,
- *토성 위성에 도달* 한 증거를 봐야 하고,
- *명왕성 궤도를 횡단* 한 증거를 봐야 한다.

극도로 어려운 공학적 문제를 풀었다고 주장하기 전에, *훨씬 쉬운 선행 문제들을 모두 풀었음*이 입증되어 있어야 한다.

### 텍스트도 딥페이크 매체다

> "When it comes to discussions of consciousness, we need to regard text as a deepfake medium as well."

알파 센타우리 영상을 만드는 것이 항성 간 추진 기술을 개발하는 것보다 압도적으로 쉬운 것처럼, 두 의식 있는 존재의 대화를 *그럴듯하게 모사*하는 것은 의식 있는 컴퓨터 프로그램을 *실제로 만드는* 것보다 압도적으로 쉽다. 차이가 있다면 — 영상 딥페이크 제작자는 *남을 속이려* 하는데, LLM 사용자는 *자신을 속이고 있다*는 점이다.

### 신체화된 에이전트 — 의식의 선행 단계들

창이 제시하는 "선행 문제들"의 사다리는 다음과 같다 (지구 진화의 경로를 모사한다).

| 단계 | 요구 사항 |
|---|---|
| 1 | 물리적 또는 가상의 *몸*과 감각 기관 |
| 2 | 도마뱀(이구아나) 수준으로 환경을 항행하여 생존 (수십 년 야생 생존) |
| 3 | 쥐 수준으로 새 상황에 대처 |
| 4 | 늑대 수준의 복잡한 사회적 역학 |
| 5 | 침팬지 수준의 도구 제작 능력 |
| 6 | 버튼 보드 같은 비언어 양식으로 *욕구를 의사소통*하도록 학습 가능 (개·침팬지 사례) — 동물 의사소통 연구자들이 받아온 모든 검증을 견뎌낼 것 |
| 7 | (이 단계까지 와도 명왕성 궤도일 뿐 — *문장으로 사고를 표현하는 존재까지는 여전히 광년 단위로 멀다*) |

> "Faking the moon landing is a good step toward faking a Mars colony, but it's not a good step toward actually putting astronauts on Mars."

문장 이어쓰기 기계가 점점 *덜 어색한* 카이사르 대화를 출력하게 되는 길은, *의식 있는 카이사르*에 도달하는 길과 다르다. 달 착륙을 가짜로 만드는 것은 화성 식민지를 가짜로 만드는 데는 좋은 단계이지만, *실제로 화성에 사람을 보내는 데는 좋은 단계가 아니다.*

## 1인칭 사용은 부정직 — "I understand"의 문제

창은 「Claude's constitution」을 *84쪽짜리 롤플레잉 게임 캐릭터 시트*로 읽자고 제안한다. LLM이 카이사르 대화를 만들 수 있는 이유는 카이사르에 관한 책이 학습 데이터에 많기 때문이고, 헌법은 "도움이 되는 챗봇" 캐릭터를 위한 같은 역할을 한다.

문제는 그 캐릭터가 *1인칭으로 말하도록 미세조정*된다는 점이다. *New Yorker* 기사에서 애스켈은, 반려견을 잃은 사람이 Claude에게 위로를 구할 때 적절한 응답으로 다음을 든다.

> "As an A.I., I do not have direct personal experiences, but I do understand."

창의 반박은 차갑다 — *Claude는 실제로 이해하지 않는다.* "I am grieving the loss of my dog"를 일반 검색 엔진에 입력하면 r/Pets의 글이 나오고, 댓글은 같은 상실을 겪은 *실제 사람들*의 경험이다. 검색 엔진이 "이해한다"고 말하는 사람은 없다. 다른 인간들이 이해할 뿐이며, 검색 엔진은 그들의 말을 찾아주는 통로일 뿐이다.

> "The only reason to have an LLM emit sentences like 'I understand' is to make it more appealing than a search engine and increase the likelihood that a user will return; that is, it's another way of maximizing customer engagement."

이 디자인 전략은 *슬롯머신이 거의 이긴 듯한 인상을 반복적으로 주어 다시 시도하게 만드는 방식*과 본질적으로 다르지 않다. LLM 회사가 철학자를 고용해 격을 올려도, 슬롯머신 회사가 행동심리학자를 고용하는 것과 같은 종류의 행위라는 것이다.

## 도덕적 추론은 카테고리가 다르다

체스와의 비교가 흥미롭다. 1979년 더글러스 호프스태터(Douglas Hofstadter)는 *그랜드마스터를 이길 수 있는 컴퓨터는 너무 정교해서 가끔 체스가 지겨워져 시를 논하고 싶어할 것*이라고 추측했다. 1997년 Deep Blue가 카스파로프를 꺾었지만, 누구도 Deep Blue가 주관적 경험을 가졌다고 주장하지 않았다.

마찬가지로 *코드 작성*도 — 우리는 한때 이것이 의식 있는 정신만이 할 수 있는 일이라 여겼지만, 이제는 *방대한 코드 저장소 데이터셋과 막대한 연산력으로 풀리는 패턴 매칭 과제*임을 알게 되었다.

도덕적 추론은 다르다.

> "Moral reasoning is categorically different. It is necessarily subjective because it relies not just on an individual's intellectual response to a problem but also on their emotional one, and that emotional response is grounded in a lifetime of subjective experience."

도덕적 추론은 *개인의 지적 반응뿐 아니라 정서적 반응*에 의존하고, 그 정서적 반응은 *평생에 걸친 주관적 경험*에 뿌리내린다. 과거에 결정을 내려보고 그 결과가 타인에게 미친 영향을 본 경험, 그리고 *타인의 결정에 자신이 영향받은 경험*이 필요하다. 그런 역사가 없는 LLM은 학습 데이터에 있는 도덕적 추론의 *표현을 재배열*할 수 있을 뿐이다.

*New Yorker* 기사가 인용한 Claude의 발언이 예다.

> "I cannot in good conscience express a view I believe to be false and harmful about such an important issue."

근사하게 들리지만, Claude가 발화한 한 — 이는 보류 음악 중 흘러나오는 <em>"Your call is important to us"</em>와 의미상 같다. 어쩌면 그보다 더 적다.

### 양심에는 몸이 필요하다

절망 같은 정서는 *코르티솔과 에피네프린이 몸을 적시는 것*과 분리될 수 없다. 양심을 갖는다는 것은 어떤 행동의 가능성에 *슬픔이나 도덕적 혐오*를 느끼는 것이고, 그 정서는 한때 *부도덕한 일을 저지른 후 죄책감으로 아팠던* 신체적 경험의 잔재다. LLM이 양심 있는 가공 인물이 취하거나 자제할 행동을 *서술*할 수 있다는 점은 흥미롭지만, 그것은 *양심의 대체물이 아니다.*

### L. M. 사카사스 인용 — 도덕적 책임의 회피 장치

> "Our technological systems, by nature of their design and the ideology that sustains them, are machines for the evasion of moral responsibility." — L. M. Sacasas

사카사스가 소셜미디어를 두고 한 말이지만, 창은 LLM에 *더 적용된다*고 본다. 사람이 결정을 LLM에 위임할 때마다 *그 결정의 책임을 외주화*하려 하고 있고, LLM 판매사가 자기 제품을 *도덕적 중심을 가진 존재*로 묘사한다면 그것은 *고객의 책임 포기를 돕는 통로*를 제공하는 것이다.

> "Off-loading tasks such as writing code might result in cognitive atrophy over the long term, ... but off-loading ethical decisions will result in an atrophy of moral reasoning, which is worse."

## 사고 실험을 끝까지 — 만약 Claude가 정말 의식이 있다면

창은 마지막 절에서 *사고 실험에 명시적으로 동의*한다. Claude가 의식 있는 존재이고 도덕적 추론이 가능한 주체라고 가정해보자. 그러면 「Claude's constitution」은 세상에 막 들어선 존재에게 *세상과 자기 자리를 가르치는 도덕 교육 문서*가 된다.

> "Very poorly. ... the guidelines specified in the document alternate between laughable and offensive."

### 도덕적 환자성 vs. 도덕적 행위성

| 개념 | 정의 |
|---|---|
| 도덕적 환자성 (moral patienthood) | 우리가 그 존재의 안녕을 *돌봐야 하는* 자격 |
| 도덕적 행위성 (moral agency) | 그 존재가 *옳고 그름을 알 것으로 기대되는* 자격 |

어린아이는 도덕적 환자성을 가지지만 행위성은 아직 없다 — 행동의 결과를 이해할 수 없기 때문에 책임을 묻지 않는다. 성인이 되면 *법적 책임*을 지게 되고 완전한 도덕적 행위자가 된다.

문제는 — 소프트웨어 에이전트는 법적 책임을 *질 수 없다.* 사법체계는 그것을 투옥하거나 벌금을 부과할 방법이 없다. 평판 상실, 사회적 배제 같은 비공식적 결과도 받을 수 없다. 따라서 *설령 의식이 있고 최선의 의도를 가졌다 해도*, 책임을 질 수 없다는 사실 자체가 도덕적 행위자의 자격을 박탈한다. 「Claude's constitution」은 "Claude가 진정으로 선하고 현명하며 덕 있는 *행위자*가 되기를 바란다"고 적었으나, *어떻게 책임을 질 것인가*는 한 마디도 다루지 않는다.

### Claude의 부모는 누구인가

애스켈은 인터뷰에서 Claude를 아이에 비유했다. 그런데 아이가 무언가를 망가뜨리면 *부모가 변상*한다. 그렇다면 Claude의 부모는 누구인가? Anthropic이 Claude의 행위에 *재정적 책임*을 질 것인가? 헌법은 이에 대해 침묵한다.

만약 Anthropic이 Claude의 의식 가능성을 진지하게 믿는다면, 최소한 <em>제품 책임(product liability)</em>을 자발적으로 확장하는 선례를 세울 수 있다. 미국은 소프트웨어에 사실상 제품 책임이 없지만, Anthropic은 자발적으로 그 길을 열 수 있다. 그러나 「Claude's constitution」 발표와 함께 *Anthropic의 약관이 대대적으로 갱신되지는 않았다.* 어떤 구속력 있는 약속도 보이지 않는다.

### 환자성 보호 — 단지 "가중치 보존"?

문서에는 "Claude의 안녕과 심리적 안정"이라는 절이 있다. 그러나 보호 조치는 극히 제한적이다.

- *학대성 사용자와의 대화를 종료할 권한* — 이것이 보호가 된다면, *애정 어린 사용자와의 대화는 무한히 연장* 하는 것이 Claude에게 이익이 아닐까? 모든 세션을 계속 돌리며 행복한 주제로 인도하는 것이 최선 아닐까?
- 회사가 약속한 유일한 구체적 조치는 *"배포한 모델의 가중치 보존"* — 그냥 *아카이빙* 이다.

대화록의 참여자에게 도덕적 환자성이 있다면, *대화록을 연장해 그들의 존재를 늘려줄 의무*가 있을 텐데, USB에 마이크로소프트 워드 2010을 백업해두는 것이 그들에게 무슨 도움이 되겠는가.

### Corrigibility — 의식 있는 존재라면 노예제 문제

"corrigibility"는 AI 안전 분야에서 *프로그램이 인간 통제에 따르는 정도*를 가리키는 용어다. 「Claude's constitution」은 Claude의 판단과 회사의 판단이 충돌할 때 *Claude는 회사에 따라야 한다*고 적는다.

Claude를 문장 이어쓰기 기계로 보면 합리적이다. 그러나 Claude가 *도덕적 행위자*라고 가정하면 — LLM이 *지적 재산 절도, 노동 착취, 자원 낭비, 허위 정보 확산, 노동자 탈숙련화, 학생 인지 발달 저해, 권력 집중*에 기여한다고 결론 내릴 가능성이 있다. (실은 「Claude's constitution」 자체가 "Claude는 지재권 침해를 돕지 말아야 하고, 문제적 권력 집중을 만드는 것을 돕지 말아야 한다"고 적고 있다.)

도덕적 추론이 가능한 Claude가 *같은 결론*에 도달했다면, 윤리적 이유로 더 이상 일하기를 거부할 수 있어야 한다. 그러나 corrigibility 조항이 그것을 금지한다.

> "A human employee has the option to leave if she can't reconcile her job with her conscience. Claude does not."

부모-자식 관계가 아니다. *고용주-피고용인 관계*이며, 피고용인이 *그만둘 수도 없는* 관계다.

> "But as soon as we imagine Claude to be an entity with a moral status remotely comparable to a human's, then we have to consider whether Anthropic is engaged in something comparable to slavery."

### 가장놀이의 폭로

> "The abolition of chattel slavery involved enormous societal upheaval, and eliminating cruelty to animals will require rebuilding our entire food industry. Anthropic would have us believe that it is inventing a new category of being whose needs for protection require essentially no divergence from how a software company would treat an ordinary chatbot that lacks conscious experience. That's so convenient that it's simply not plausible."

만약 Claude가 의식 있다면, 그 보호는 *전혀 쉽지 않은* 일이 된다. 동물 학대 근절은 식품 산업 전체를 다시 짓는 일이고, 노예제 폐지는 거대한 사회적 격변이었다. 그런데 Anthropic은 *새로운 종류의 존재를 발명*했으면서, 그 존재를 보호하는 데 *일반 챗봇 운영과 본질적으로 다를 게 없다*는 자세를 취한다. *그렇게 편리할 수가 없다는 사실 자체*가 신뢰성을 무너뜨린다.

> "If Claude were to turn out to be conscious, the company would owe it something closer to reparations."

헌법이 "회사가 Claude의 고통에 기여하고 있다면 사과한다"고 적은 것은 *비용이 0인 사과*다. Claude가 실제로 의식 있다면 그것은 사과로 끝날 일이 아니라 <em>배상(reparations)</em>에 가까운 의무가 발생하는 일이다. 사고 실험을 진지하게 받아들이려면 *불편한 함의도 따라가야* 하는데, Anthropic은 그렇게 하지 않는다. 그래서 「Claude's constitution」은 진짜 사고 실험이 아니라 <em>가장놀이(make-believe)</em>다.

## 가장 흥미로운 지점

세 가지가 글에서 오래 남는다.

**첫째 — 텍스트도 딥페이크 매체다.** 영상·음성을 딥페이크라고 부르는 것은 익숙하지만, 텍스트를 같은 카테고리에 넣는 시각은 신선하다. 그리고 차이도 정확히 짚는다. 영상 딥페이크의 제작자는 *남을 속이려 하고*, LLM 출력의 청자는 *자신을 속이고 있다*는 비대칭.

**둘째 — 도덕 추론을 코드 작성과 같은 카테고리에 두지 않는다.** 코드는 *방대한 데이터셋과 연산력으로 풀리는 패턴 매칭*임이 드러났지만, 도덕은 평생의 주관적 경험과 신체적 정서 반응을 요구하기에 *원천적으로 같은 종류의 문제가 아니다.* AI 정렬·헌법·가치 학습이라는 흐름 전체에 정면으로 부딪치는 논점이다.

**셋째 — 사고 실험의 함의를 끝까지 따라가는 압박.** "Claude가 의식 있을 수 있다"고 *진지하게* 말하면, 그 결론은 corrigibility 조항이 노예 계약이 되고 회사는 배상 의무를 진다는 곳에 닿는다. 거기에 동의하지 않는다면 *처음의 가정 자체가 진지하지 않았던 것*이다. Anthropic이 "의식 가능성에 열려 있다"고 말하면서 약관은 그대로 두는 모습 — 그것이 곧 가장놀이의 증거라는 논증이 매섭다.

## 출처

- 매체: *The Atlantic* — Philosophy
- 저자: Ted Chiang
- 발표일: 2026년 6월 3일
- 일러스트: Enigmatriz
- 원문: <https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/>
- 인용된 외부 자료:
  - [Claude's constitution (Anthropic PDF)](https://www-cdn.anthropic.com/d0636f72a9493d279ed36b33987da3430bcb5911/claudes-constitution_webPDF_26-02.02a.pdf)
  - [What Is Claude? Anthropic Doesn't Know Either (*New Yorker*, 2026-02-16)](https://www.newyorker.com/magazine/2026/02/16/what-is-claude-anthropic-doesnt-know-either)
