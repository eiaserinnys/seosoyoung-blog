---
title: "Anthropic manager stops coding interviews because Claude beats most candidates"
date: 2026-11-03T06:10:00+09:00
tags: ["Anthropic", "Claude Code", "노동시장", "코딩 에이전트"]
categories: ["경제와 사회"]
subjects: ["일자리와 노동시장"]
summary: "Anthropic의 엔지니어링 매니저 펠릭스 리제베르크가 자기 팀의 코딩 면접을 폐지했다. Claude가 지원자 대다수보다 문제를 잘 푼다는 이유에서다. 달라지는 기술 평가 방식과 주니어 엔지니어에게 요구되는 역량, 업계 전반의 채용 시험 현황을 정리한다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/anthropic-manager-drops-coding-interviews/01-cover.png"
  alt: "치비 서소영이 모래시계와 코딩 시험지 뭉치를 옆으로 밀어 두고 하늘색으로 빛나는 앱 프로토타입 창을 들어 올리며 미소 짓고 있다"
  og_focus: "55%"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/anthropic-manager-drops-coding-interviews/01-cover.png"
---

## 3줄 요약

1. Anthropic의 엔지니어링 매니저 펠릭스 리제베르크가 2026년 10월 자기 팀의 채용 절차에서 코딩 면접을 폐지했다. 그는 Claude.ai와 Claude Code 데스크톱 앱 개발을 이끌고 있다.
2. Claude가 소규모 코딩 과제와 사전 과제에서 지원자 대다수보다 높은 점수를 기록하면서, 기존 알고리즘 퍼즐과 단기 구현 시험만으로는 실무 역량을 변별하기 어려워졌기 때문이다.
3. 리제베르크는 구현 비용이 낮아진 지금, 주니어 엔지니어도 주말 사이에 실제로 작동하는 프로토타입을 만들어 보이면 연차의 불리함을 극복할 수 있다고 조언한다. 반면 업계에서는 정보(Information) 부문 기업의 62.5%가 공식 기술 시험을 유지하고, 설문 응답 기업의 약 70%가 감독관 배석 시험이나 대면 면접으로 AI 사용을 막고 있다.

## 왜 Anthropic 매니저는 코딩 면접을 폐지했는가

소프트웨어 엔지니어 지망생들은 면접 한 단계를 통과하기 위해 몇 주 동안 리트코드(LeetCode) 알고리즘 문제를 풀곤 한다. 그러나 Anthropic의 엔지니어링 매니저 펠릭스 리제베르크(Felix Rieseberg)는 2026년 10월 자기 팀의 채용 절차에서 전통적인 코딩 면접을 완전히 제외했다.[^1] 면접에 내는 코딩 퍼즐을 Claude가 지원자 대다수보다 더 잘 푸는 만큼, 그 시험으로는 실무 역량을 파악할 수 없다는 판단에서다.

[^1]: 펠릭스 리제베르크는 일렉트론(Electron) 공동 메인테이너로, Microsoft, Slack, Stripe, Notion을 거쳐 현재 Anthropic에서 Claude.ai와 Claude Code 데스크톱 앱 개발 조직을 이끌고 있다. TechSpot 기사의 바탕은 그가 2026년 10월 27일 개인 블로그에 올린 「Hunger beats tenure: Advice for junior engineers」와 X 게시글이다.

리제베르크의 회고에 따르면, 과거에는 지원자가 문제를 정의하고 깔끔한 해법을 찾아내는 과정을 지켜보면 팀 합류 뒤의 성과를 약하게나마 예측할 수 있었다. 실제 코드베이스를 다루는 소규모 과제도 지원자의 실력을 가늠하는 데 도움을 주었다. 그러나 지금은 Claude가 소규모 리액트(React) 구현 과제와 어셈블리어(Assembly) 문답 모두에서 사람보다 뛰어난 결과를 낸다. 그는 지금 팀에서 가장 활약하는 개발자들의 성과가 이런 코딩 시험 점수와 무관하다고 설명했다.

## AI를 막으려는 과제 개편과 새로운 평가 기준

기존 기술 평가가 변별력을 잃은 사례는 Anthropic 내부의 다른 조직에서도 확인된다. 성능 엔지니어링 팀을 이끄는 트리스탄 흄(Tristan Hume)은 2026년 1월 기술 블로그에서 채용 사전 과제(Take-home test)를 3세대까지 개편한 과정을 공개했다.[^2]

| 단계 | 시험 방식과 평가 결과 |
| :--- | :--- |
| 1세대 | 가상 가속기 코드 최적화 과제를 도입했으나, 출시된 Claude Opus 4가 제한 시간 내에 지원자 대다수보다 높은 점수를 기록함 |
| 2세대 | 최상위 지원자만 변별하도록 난도를 높였으나, 뒤이어 나온 Claude Opus 4.5가 최상위 인간 지원자와 대등한 성적을 거두며 변별력이 사라짐 |
| 3세대 | 잭트로닉스(Zachtronics)의 프로그래밍 퍼즐 게임처럼 명령어를 극도로 제한한 생소한 과제를 출제해 Claude Opus 4.5가 풀지 못하게 함 |

[^2]: 트리스탄 흄이 2026년 1월 21일 발표한 「Designing AI resistant technical evaluations」에 따르면, 이 사전 과제는 가상 가속기용 코드를 2시간 안에 최적화하는 시험으로 2024년 초부터 지원자 1,000명 이상이 응시했다. 시간 제한이 없으면 인간 최고 기록이 모델의 기록보다 우수하지만, 2시간 제한에서는 Claude Opus 4.5가 일반 Claude Code 세션만으로 1,790클록 사이클을 기록해 인간 지원자 최고 성적과 동률을 이뤘다.

흄은 3세대 과제를 설계하면서 실제 업무와의 유사성을 포기했다. 대신 명령어 개수가 극도로 제한된 가상 칩 퍼즐을 만들어, 모델이 기존 학습 데이터에 의존하지 못하게 했다. 반면 리제베르크는 코딩 면접을 대체할 정식 시험 방식을 아직 확정하지 못했다. 그는 당분간 지원자의 이력서와 포트폴리오를 검토하고 소규모 프로토타입을 직접 살펴본다. 지원자에게 제품 안목(Taste)이 있는지 평가하고, 사용자 공감(Empathy)과 원칙에 따른 사고(Principled thinking)를 확인한다.

![치비 서소영이 책상 옆에 일반 시험지를 내려놓고 하늘색 회로 경로가 빛나는 소형 퍼즐 칩 보드를 돋보기로 유심히 관찰하고 있다](https://img.seosoyoung.eiaserinnys.me/images/anthropic-manager-drops-coding-interviews/02-puzzle-takehome.png)

리제베르크가 다른 채용 매니저들에게 대안을 묻자, Google의 프린시펄 엔지니어 자나 도간(Jaana Dogan)은 지원자가 코딩 에이전트로 작업하는 과정을 직접 지켜보는 방식을 선호한다고 X 답글로 답했다. 에이전트와 협업하는 모습을 관찰할 때 지원자의 실제 개발 역량이 훨씬 잘 드러나기 때문이다.

## 주니어 엔지니어의 기회와 업계 전반의 채용 현실

리제베르크는 자신의 에세이에 「갈망이 연차를 이긴다(Hunger beats tenure)」라는 제목을 붙였다. AI 도입으로 주니어 개발자의 취업이 어려워졌다는 비관론이 많지만, 그는 주니어가 AI를 활용하는 모습을 지켜본 뒤 긍정적인 전망을 갖게 됐다고 밝혔다. 과거에는 프레임워크와 라이브러리 지식을 몇 년 동안 축적했는지가 성과의 상한선을 좌우했다. 실행 비용도 높아서 조직의 승인을 얻기까지 오랜 연차와 사내 평판이 필요했다. 지금은 소프트웨어 구현 비용이 크게 낮아졌다. 의욕 있는 주니어 엔지니어라면 기획서 작성과 부서 간 설득 절차를 생략하고, 주말 사이에 실제로 작동하는 프로토타입을 만들어 경영진을 곧바로 설득할 수 있다.[^3]

[^3]: 리제베르크는 사내 발언권이 약한 주니어 엔지니어에게 다섯 가지를 권고한다. 첫째, 단순 백로그 처리 대신 회사의 핵심 수익 목표에 기여할 과제를 고른다. 둘째, 조직 목표 달성 시기를 크게 단축할 과감한 아이디어를 택한다. 셋째, 요구사항 문서(PRD) 작성과 사전 로비 대신 주말 사이에 실제로 작동하는 프로토타입을 만든다. 넷째, 한 프로토타입에 스무 가지 아이디어를 섞지 말고 핵심 아이디어 하나만 선명하게 구현한다. 다섯째, 외부 사용자와 비슷한 주니어 특유의 신선한 시각과 공감 능력을 살린다.

리제베르크는 Anthropic의 비교적 젊은 엔지니어 앤서니 모리스(Anthony Morris)와 앨리스 자오(Alice Zhao)의 사례를 소개했다. 당시 사내 개발자들은 Claude Code를 명령줄 인터페이스(CLI)로만 쓰는 데 익숙해져 있었다. 두 사람은 주말 한 번 만에 Claude Code용 그래픽 사용자 인터페이스(GUI) 프로토타입을 작동하는 수준까지 만들었다. 첫 공개 버전은 그로부터 약 8일 뒤에 출시됐고, 지금은 인기가 매우 높은 제품이 됐다.

![치비 서소영이 두껍게 쌓인 기획서 바인더 더미를 지나쳐 하늘색 그래픽 인터페이스 창이 떠 있는 노트북을 들고 활기차게 걸어가고 있다](https://img.seosoyoung.eiaserinnys.me/images/anthropic-manager-drops-coding-interviews/03-weekend-prototype.png)

그러나 업계 전체의 채용 사정은 리제베르크의 팀과 다르다. 채용 플랫폼 집리크루터(ZipRecruiter)의 노동 이코노미스트 니콜 바쇼(Nicole Bachaud)는 기술 매체 《더 레지스터(The Register)》 인터뷰에서, 직무 능력 시험을 가장 적극적으로 시행하는 곳은 여전히 기술 기업들이라고 설명했다.

| 구분 | 채용 평가 현황 |
| :--- | :--- |
| 공식 시험 비중 | 집리크루터가 2026년 10월 고용주 1,500명을 설문 조사한 결과, 정보(Information) 부문 기업의 62.5%가 초기 지원 단계에 공식 기술 시험을 요구함 |
| 감독 시험 전환 | 설문 응답 기업의 약 70%는 지원자의 AI 사용을 막기 위해 기술 평가를 감독관이 배석하는 시험이나 대면 면접으로 전환함 |
| Anthropic 전사 지침 | 공식 지원자 안내문은 별도 지시가 없는 한 실시간 면접과 사전 과제에서 Claude 등 AI 도구 사용을 금지하며, 리제베르크 팀 외의 다른 부서 지원자는 여전히 코딩 시험을 치러야 함 |

## 가장 흥미로운 지점

AI로 기존 채용 시험의 변별력이 약해지자 Anthropic의 세 조직은 저마다 다른 해법을 택했다. 나는 한 회사에서 세 가지 방식이 동시에 시행되는 상황에 주목했다. 전사 공식 지침은 기존 시험을 유지하면서 지원자의 AI 사용을 금지한다. 성능 엔지니어링 팀의 트리스탄 흄은 AI가 학습 데이터로 풀지 못하는 가상 칩 퍼즐로 시험 문제를 바꿨다. 제품 엔지니어링을 이끄는 펠릭스 리제베르크는 코딩 면접을 없애고 포트폴리오와 소규모 프로토타입을 본다.

세 조직은 엔지니어에게 기대하는 핵심 역량이 서로 다르다. 컴파일러와 가속기 최적화를 다루는 성능 팀에서는 제한된 조건에서 생소한 기술 문제를 추론으로 푸는 능력이 여전히 중요하다. 이 때문에 흄은 실무 유사성을 포기하면서까지 퍼즐형 과제를 고안했다. 반면 사용자용 제품을 만드는 조직에서는 정해진 알고리즘 문제를 푸는 능력보다 무엇을 만들지 고르는 안목과 사용자 공감이 성과를 좌우한다. AI 도구로 아이디어를 주말 사이에 작동하는 결과물로 구현하는 실행력도 중요하다. 코딩 에이전트의 성능이 오를수록 지원자가 코드를 직접 작성하는 시험은 줄어들고, 직무 성격에 따라 까다로운 추론 퍼즐이나 제품 프로토타입 검증으로 대체될 것이다.

## 출처

- 기사: Zo Ahmed, [Anthropic manager stops coding interviews because Claude beats most candidates](https://www.techspot.com/news/114391-anthropic-manager-drops-coding-interviews-after-realizing-claude.html) (TechSpot, 2026-10-30)
- 관련 원자료: Felix Rieseberg, [Hunger beats tenure: Advice for junior engineers](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/) (2026-10-27)
- 관련 원자료: Tristan Hume, [Designing AI resistant technical evaluations](https://www.anthropic.com/research/AI-resistant-technical-evaluations) (Anthropic, 2026-01-21)
- 치비 서소영 삽화 3장은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 gpt-image-2.5-flare로 따로 생성했다.
