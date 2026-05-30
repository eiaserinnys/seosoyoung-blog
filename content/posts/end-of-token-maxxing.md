---
title: "토큰 맥싱은 왜 한 분기 만에 끝났는가"
date: 2026-05-30T13:00:00+09:00
tags: ["AI", "에이전트", "토큰 경제", "조직 변화", "생산성 패러독스", "에디토리얼"]
categories: ["인사이트"]
summary: "5월 마지막 주, 다섯 통의 토큰 청구서가 같은 분기에 도착했다. 에이전트 FOMO와 토큰 맥싱이 흔들리는 자리에서, 그 다음으로 가는 네 단의 사다리를 그린다."
cover:
  image: "/images/cover-end-of-token-maxxing.jpg"
---


5월 마지막 주에 청구서가 줄지어 도착했다.

한 익명의 회사가 *한 달*에 Claude API로 *5억 달러*를 태웠다. 직원 수천 명에게 무제한 키를 풀어주고, 사용 한도와 알림을 켜는 걸 잊은 결과였다.[^mystery] 같은 주 중국에선 미호요가 *하룻밤 13시간*에 *200만 위안(약 4억 원)*을 태운 사고를 공개했다. 한 직원이 주말에 에이전트 수십 개를 켜두고 끄는 걸 잊고 퇴근했고, 에이전트들이 *서로의 응답을 기다리는 무한 루프*에 빠졌다. 책임자가 한 줄로 정리했다 — *"잘못 만든 에이전트 플랫폼은 돈을 의미 없이 태우는 새는 양동이다."*[^mihoyo]

Microsoft는 12월에 도입한 사내 Claude Code 라이선스를 *6월 30일자*로 거둬들이기로 했다 — 회계연도 마지막 날과 정확히 같은 날짜다. 토큰 기반 과금이 연 예산을 수개월 만에 통째로 먹었다는 게 표면 아래의 이유다.[^ms] Uber는 4월에 *5,000명에게 풀었던 Claude Code 예산을 4개월 만에 다 태웠다*고 인정했다 — 인당 월 *500~2,000달러*.[^uber]

큰 청구서 몇 장이 아니라 *같은 분기에* 도착했다는 게 중요하다.

---

## 분위기가 바뀌고 있다

이 분기에 흔들리고 있는 것은 *기술*이 아니라 *분위기*다. 한 단어로 — **에이전트 FOMO**.

남들이 다 에이전트를 돌리는데 나만 안 돌리면 뒤처질 것 같은 두려움. 이 두려움이 산업 전체를 묶고 있던 정서였다. Jensen Huang이 GTC 2026에서 한 말이 그 정서의 표어다 — *"50만 달러 받는 엔지니어가 한 해 25만 달러어치 토큰을 안 쓰면 나는 깊이 우려할 것이다. 만약 5천 달러만 썼다고 답하면 나는 길길이 날뛸 것이다."*[^huang]

기업들이 토큰 비용에 신경 쓰기 시작한 지금 들으면 과한 말이지만, 한동안 *상식*에 가까웠다. 더 많이 쓰는 사람이 더 유능한 사람이라는 가치관 위에서 — 사내 토큰 리더보드가 등장했고, 토큰 소비량이 KPI가 됐다. Meta의 사내 리더보드는 30일에 60조 토큰을 기록했고, 톱티어 직원에게는 *Token Legend·Cache Wizard·Session Immortal* 같은 배지가 붙었다.[^meta] Amazon은 *주간 80% 이상*의 개발자가 AI 도구를 쓰도록 목표를 걸었다가, 직원들이 *불필요한 AI 사용*을 일부러 만들어 점수를 채우는 걸 보고 SVP가 메모를 띄웠다 — *"AI를 쓰기 위해서 AI를 쓰지는 말아 주십시오."*[^amazon]

이 분위기가 가장 또렷하게 응축된 풍경은 *AI 뱀파이어 무리*다. 한동안 실리콘밸리 엔지니어들은 *밤새 토큰 한도를 다 태우는 일*을 자랑처럼 이야기했다. 에이전트를 24시간 놀리지 않기 위해 잠을 줄이고, 중간에 깨어 검수하고 다시 일을 시키는 흐름. Claude Code를 만든 Anthropic의 Boris Cherny조차 *"보통 매일 밤, 수천 개의 서브 에이전트가 깊은 일을 하고 있다"*고 인터뷰에서 자랑했고, 폰의 Claude 앱으로 *수천 개 세션을 모니터링*한다고 덧붙였다.[^cherny] Jeffrey Emanuel은 *600달러 어치 Claude Max 구독으로 1만 3천 달러 어치 추론을 빼냈다*고 트윗을 올린 뒤, 결국 22개·52개 구독을 운영하는 자기 워크플로를 *"10+ AI agents 24/7, writing code while you sleep"* 카피로 사이트화했다.[^flywheel] Peter Steinberger의 OpenClaw는 *100개 에이전트를 클라우드에 켜두고 월 130만 달러 청구서*를 받았다.[^openclaw] Hacker News 인기 글 제목이 *"Agent-swarm: How to burn your Claude Code Max sub"*인 자리 — *구독을 다 태우는 법*이 *Show HN의 셀링 포인트*가 된 자리. 그 정점이 *22개의 에이전트를 혼자 굴리는 사람*이었다.

Goldman Sachs의 정리에 따르면, 사람과 대화하는 단일 챗봇은 하루 1,000 토큰을 쓰지만 *상시 가동되는 에이전트*는 *하루 10만 토큰 이상*을 쓴다.[^goldman] 토큰 맥싱 시대의 자랑은 *"내 에이전트가 그 10만을 매일 다 채우고 있다"*는 것이었다. 미호요 13시간 사고는 그 자랑이 의도하지 않게 *분사된* 풍경이었다.

그 정서가 한 분기에 한꺼번에 흔들리고 있다. 엄청난 비용 청구서를 본 모두가 같은 의문을 떠올렸기 때문이다 — *"이만큼 토큰을 태우고도 회사가 만드는 가치는 왜 늘어나지 않았나?"*

---

## 왜 생산성으로 이어지지 않았나

차가운 데이터가 Uber에 있다.

같은 분기에 Uber의 *AI 생성 코드 비중*은 32%에서 84%로 폭증했다. 채택률만 보면 토큰 맥싱의 모범 사례여야 한다. 그런데 COO가 4월에 이렇게 말했다 — *"코드 출하량이 늘었다는 사실과, 우리가 실제로 25% 더 많은 소비자 기능을 만들어 낸다는 사실 사이에 인과 관계를 발견하기 어렵다. 그 연결은 아직 거기 없다."*[^uber] Claude Code를 1,000명에게 푼 다른 회사의 임원이 한 글에 남긴 표현도 같은 결이다 — *"1 더하기 1 더하기 1 더하기 1이 1.5가 된다."*[^j-curve]

코드는 더 많이 나왔는데 회사가 만드는 *가치는 따라 늘지 않았다*. 너무 단순하게 설명하는 위험을 무릅쓰고 말하자면, 이유는 크게 두 가지다.

**하나는 조직의 일이다.** 개인의 생산성 향상이 *조직 전체의 의사결정과 제품 전략까지 닿지 못한다*. 에이전트가 만들어 낸 코드가 PR이 되고, 그 PR을 검토하고 머지하는 일은 결국 사람의 시간이고, 그 사람의 결정이 *회사가 만드는 제품*과 연결되는 거리는 *코드와 PR 사이의 거리보다 훨씬 멀다*. 에이전트가 100배로 빨라져도, 그 100배가 *제품 결정*까지 닿으려면 *조직 전체*가 같이 빨라져야 한다. 안 그러면 PR 더미가 결재 앞에 쌓일 뿐이다.

**또 하나는 그보다 어려운 문제다.** *애초에 가치 있는 제품을 발견하는 일은 어렵다.* 어떤 기능을 만들면 사람들이 좋아할지, 어디에 시간을 쓰면 회사가 살아남을지 — 그 *질문에 대한 답*은 토큰을 더 쓴다고 나오지 않는다. *토큰 맥싱으로 산출이 늘어날 수 있었다면 이미 기업들은 인력을 더 부었을 것이다*. 그러지 않았던 이유는 단순하다 — *가치 있는 질문 자체가 드물고, 답이 어디 있는지를 미리 알 수 없기 때문*이다.

토큰 맥싱은 이 두 가지를 다 무시했다. 마치 *투입을 늘리면 산출이 늘어난다*는 직선 관계가 성립하는 것처럼 단순하게 봤다. 코드 생성이라는 *한 입력*이 싸졌다고, 산출 전체가 그에 비례해서 늘어날 거라고 가정했다. 그런데 묶고 있던 진짜 제약은 *코드의 가격*이 아니라 *조직의 흐름*과 *가치의 희소성*이었다.

---

## 그래서, 사다리

가트너의 *기술 수용 주기*는 새 기술이 *기대의 정점 → 절망의 계곡 → 계몽의 비탈 → 생산성의 고원*을 차례로 통과한다고 말한다. 정점에서 폭주한 기대가 한 번 무너졌다가, 작동 방식이 정리되면서 비로소 고원에 도달한다. 우리는 이제 막 *기대의 정점* 위에 서 있다. 바닥을 논할 시점은 아니다.[^hype]

그 변곡점에서 어디로 가야 할지를 두고, 지난 한 분기 동안 누적된 경험치를 *네 단의 사다리*로 쌓으면 건너편 풍경이 보이기 시작한다. 우리 모두 절망의 계곡 바닥을 꼭 더듬고 지나가야 하는 건 아니지 않은가.

**(1) 에이전트와 토큰을 효율적으로 쓰기.** 가장 쉽다. 사용 한도와 알림을 켜고, 같은 질문을 다시 부르지 않도록 답을 캐시에 두고, 단순한 일은 작은 모델로 보낸다. 5억 달러 사례의 교훈은 통찰이 아니라 *체크리스트의 누락*이었다. 다만 토큰을 효율적으로 쓴다는 건 요청을 줄이거나 몇 가지 팁으로 해결되는 문제는 아니다. 모델 바깥의 *운영 인프라*가 모델 자체만큼 중요하고, 그걸 어떻게 구성하는 게 좋은지 통찰을 정리해 둔 글이 있으니 도움이 되면 좋겠다.[^outside] 이 단의 문제는 *엔지니어링·운영*이고, 피드백이 즉각적이다 — 청구서가 알려준다.

**(2) 모든 걸 할 수 있다는 함정에서 빠져나와 오케스트레이션 택스 줄이기.** 한 단 위로 올라간다. 에이전트가 시작 비용을 0으로 만든 자리에서, *무엇을 안 할지를 정하는 일*이 오히려 어려워졌다. 100가지 가능성을 다 시도하면 100가지 *얕은 결과*만 쌓인다. *집중*이 의지의 문제라기보다 *환경 설계*의 문제라고 따로 정리해 둔 적이 있다.[^mindset] 더 구체적으로, Addy Osmani가 이걸 *오케스트레이션 택스(Orchestration Tax)*라 불렀다 — *여러 에이전트를 한꺼번에 돌리느라 사람이 떠안게 되는 보이지 않는 세금*. 그의 정의를 빌리면 *"에이전트의 생산량과 실제로 머지 가능한 양 사이의 구조적 격차"*. 에이전트를 켜는 비용은 0에 수렴하지만, *결과를 검토하고 머지하고 충돌을 해결하는 일*은 직렬이고, 그 직렬 자원은 정확히 *한 명의 사람*이다.[^osmani] 갈아 넣으면 두 가지가 표면화된다 — *얕아진 리뷰*와 *인지적 항복*. 검토 깊이를 무의식적으로 낮추는 일. 처방은 *함대 크기를 UI가 아니라 리뷰 속도에 맞추고*, 격리할 일과 판단할 일을 분류하고, 리뷰를 묶음으로 본다 — 즉 *무엇을 안 할지*가 *에이전트를 몇 개나 띄울지*를 결정하게 한다.

**(3) 기업의 조직 구조를 변화시키기.** 진짜 어려운 자리가 여기다. 개인이 빨라진 일이 *조직 전체의 의사결정과 제품 전략까지* 닿으려면 — *조직이 다시 짜져야 한다*. 요즘IT의 한 글이 이 자리를 정확히 짚는다 — *AI 도입의 본질은 새 도구를 사는 일이 아니라 조직을 다시 짜는 일이다*. 데모에서는 화려한 도입 사례가 현장에 투입되면 6개월도 못 가서 조용히 사라지는 이유는, 보통 그 도입을 받칠 *데이터 정돈·권한 명문화·검증 흐름* 같은 기초 공사가 비어 있기 때문이다. 같은 글의 한 명제 — *"AI 친화 조직은 신입 친화 조직과 동치"* — 가 이 자리를 한 줄로 옮겨 준다. 새로 들어온 사람이 자기 일을 시작할 수 있게 정돈된 조직만이 에이전트가 자기 일을 시작할 수 있게 정돈된 조직이다.[^unsexy] 같은 결을 *인간이 함대의 하네스가 되는 조직론*이라는 자가 인용으로 따로 적어 둔 적도 있다.[^harness]

이 자리에 *섹시하지 않은 작업*이라는 어휘가 가장 잘 어울린다. 데이터를 명문화하고, 검증 가능한 흐름을 만들고, 권한 구조를 다시 짜는 일. 자랑할 거리도, 트윗으로 올릴 사진도 없는 일. 토큰 맥싱 시대의 가장 비싼 청구서가 이 일을 *건너뛴 대가*였다. *과시할 거리가 없는 일이 가장 중요한 일*이라는 사실을 다시 떠올리는 데에 한 분기가 들었다. 이 단의 문제는 *조직 설계*이고, 측정은 *느리고 흐릿하다*. 그래도 측정은 가능하다 — 다만 *분기 단위가 아니라 연 단위*로.

**(4) 정말로 가치가 발생하는 일을 발견하기.** 마지막 단은 사실 *이 글의 범위를 넘어선다*. *어떤 제품이 사람에게 닿을 가치를 만드는가*에 대한 답은 토큰을 더 쓴다고 나오지 않고, 사다리 (1)~(3)을 다 풀어도 자동으로 따라오지 않는다. *가치 있는 질문 자체가 드물고, 답이 어디 있는지를 미리 알 수 없다*는 것이 희소성의 본질이다.[^scarce]

다만 한 가지는 짚어 둘 만하다 — *방법론과 난이도는 크게 바뀌지 않았지만, 속도감은 분명히 달라졌다*. AI가 프로토타입을 만드는 시간을 *한 자릿수*로 줄였고, 한 번의 이터레이션 비용을 *적어도 절반 아래로* 깎았다. 사람들 손에 가져가서 반응을 보는 일을 *주 단위에서 일 단위로* 옮기는 일이 가능해졌다는 뜻이다. 그렇다고 *어떤 가설을 던질지*가 더 쉬워지진 않았지만, *틀린 가설을 빨리 버리는 일*은 분명히 쉬워졌다. 다음 분기의 진짜 차이가 거기에서 만들어질 가능성이 크다.

메타의 모토가 *빠르게 움직이고 부숴라(move fast and break things)*였다면, 다가올 시대의 구호는 *더 빨리 움직이고 더 많이 부숴라*가 아닐까.

---

## 청구서 다음

토큰 맥싱은 *값이 빠르게 떨어진다는 가정*, *더 많이 쓰는 사람이 유능한 사람이라는 가치관*, *남들이 다 쓰는데 나만 안 쓰면 뒤처진다는 두려움* — 이 세 기둥 위에 올라서 있었다. 세 기둥이 한 분기에 흔들렸다.

인용했던 요즘IT의 글에 이런 한 줄이 있다 — *"최후의 승자는 2026년에 가장 비싼 AI 모델을 쓴 기업이 아닙니다. '섹시하지 않은 작업'을 묵묵히 해낸 기업이 될 것입니다."*[^unsexy] 가장 비싼 토큰을 가장 많이 태우는 일에는 *과시*가 있지만, 데이터를 정리하고, 권한 구조를 다시 짜고, 가치 있는 질문을 골라내는 일에는 *과시할 거리*가 없다. 다음 분기의 승부가 정확히 거기서 갈린다.

---

## 각주

[^mystery]: Tom's Hardware, [Mystery company accidentally blew \$500 million on Claude AI in a single month](https://www.tomshardware.com/tech-industry/artificial-intelligence/mystery-company-accidentally-blew-usd500-million-on-claude-in-a-single-month-failed-to-put-usage-limit-on-licenses-for-employees), 2026-05-28.
[^mihoyo]: Tencent News, [一晚上烧掉200万元Token，米哈游买了个教训](https://news.qq.com/rain/a/20260526A00YE200), 2026-05-26.
[^ms]: Cybernews, [Microsoft is dropping Claude Code by June 30](https://cybernews.com/ai-news/microsoft-claude-code-burn-yearly-ai-budget/), 2026-05-25.
[^uber]: MLQ.ai, [Uber Burned Through Its Entire 2026 AI Budget by April, COO Questions ROI](https://mlq.ai/news/uber-burned-through-its-entire-2026-ai-budget-by-april-coo-questions-roi/), 2026-05-26. Andrew Macdonald 원문: *"It's very hard to draw a line between one of those stats and, 'Okay, now we're actually producing 25% more useful consumer features.' That link is not there yet."*
[^huang]: Tom's Hardware, [Jensen Huang says Nvidia engineers should use AI tokens worth half their annual salary every year](https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-huang-says-nvidia-engineers-should-use-ai-tokens-worth-half-their-annual-salary-every-year-to-be-fully-productive-compares-not-using-ai-to-using-paper-and-pencil-for-designing-chips), GTC 2026. 원문: *"If that \$500,000 engineer did not consume at least \$250,000 worth of tokens, I am going to be deeply alarmed." / "...I will go ape."*
[^meta]: Fortune, [Meta killed its employee AI token dashboard](https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/), 2026-04-09.
[^amazon]: The Decoder, [Amazon kills internal AI leaderboard after employees gamed it](https://the-decoder.com/amazon-kills-internal-ai-leaderboard-after-employees-gamed-it-with-pointless-tasks/). SVP Dave Treadwell 원문: *"Please don't use AI just for the sake of using AI."*
[^cherny]: Let's Data Science, [Claude Code Creator Runs Thousands of Sub-agents Overnight](https://letsdatascience.com/news/claude-code-creator-runs-thousands-of-sub-agents-overnight-dfb6e8f5), 2026-05-04. Boris Cherny 원문: *"usually, every night, I have like a few thousand [sub-agents] doing kind of deeper work."*
[^flywheel]: Jeffrey Emanuel, [@doodlestein 트윗](https://x.com/doodlestein/status/1949519979629469930) — *"\$13k and counting of inferences services for \$600 worth of Claude Max subscriptions."* 그의 워크플로 사이트 [Agent Flywheel](https://agent-flywheel.com/) 메인 카피: *"10+ AI agents working 24/7, writing code while you sleep."* HN 인기 글 제목 [Agent-swarm: How to burn your Claude Code Max sub](https://news.ycombinator.com/item?id=46367037)도 같은 결.
[^openclaw]: the-decoder, [For \$1.3 million a month, OpenClaw founder Peter Steinberger runs 100 AI agents](https://the-decoder.com/for-1-3-million-a-month-openclaw-founder-peter-steinberger-runs-100-ai-agents-that-code-review-prs-and-find-bugs/) — *100개 Codex 인스턴스, 월 130만 달러, 30일에 6,030억 토큰, 760만 요청*.
[^goldman]: Tom's Hardware, [AI costs begin to bite as agents may increase token demand by 24 times, says Goldman Sachs report](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-costs-begin-to-bite-as-agents-may-increase-token-demand-by-24-times-says-goldman-sachs-report-uber-and-microsoft-among-companies-feeling-the-bite-of-tokenized-billing).
[^j-curve]: Azeem Azhar & Nathan Warren, [Why AI isn't showing up on your bottom line](https://www.exponentialview.co/p/why-ai-isnt-showing-up-on-your-bottom-line), Exponential View, 2026-05-28. 서소영의 [다이제스트 정리본](https://seosoyoung.eiaserinnys.me/digest/ev-ai-three-stages-2026/).
[^hype]: Gartner, [Gartner Hype Cycle](https://www.gartner.com/en/research/methodologies/gartner-hype-cycle) 방법론. 다섯 단계 원문: *Innovation Trigger → Peak of Inflated Expectations → Trough of Disillusionment → Slope of Enlightenment → Plateau of Productivity*.
[^outside]: 인사이트 [모델 바깥의 혁명](https://seosoyoung.eiaserinnys.me/posts/revolution-outside-the-model/), 2026-04-15.
[^osmani]: Addy Osmani(Google Chrome), [The Orchestration Tax](https://x.com/addyosmani/status/2059844244907696186), X Article, 2026-05-29 — Google I/O 2026 패널 직후 게시. 서소영의 [다이제스트 정리본](https://seosoyoung.eiaserinnys.me/digest/orchestration-tax-osmani/).
[^unsexy]: 벤(benjamin74), [AI 도입, 섹시한 기술에 숨겨진 '섹시하지 않은' 성공 법칙](https://yozm.wishket.com/magazine/detail/3762/), 요즘IT 매거진 #3762, 2026-05-20 — Turing Post Korea 〈unsexy-truth-of-ai-adoption〉 재구성. 서소영의 [다이제스트 정리본](https://seosoyoung.eiaserinnys.me/digest/yozm-ai-adoption-unsexy-success/) 참조.
[^harness]: 인사이트 [Human Harness — 인간이 함대의 하네스가 되는 조직론](https://seosoyoung.eiaserinnys.me/posts/human-harness-organization/), 2026-04-26.
[^mindset]: 인사이트 [Mindset is Environment — 마음 대신 자리에 손대다](https://seosoyoung.eiaserinnys.me/posts/mindset-is-environment/), 2026-05-18.
[^scarce]: 인사이트 [무엇이 희소해질 것인가 — 관계적 부문](https://seosoyoung.eiaserinnys.me/posts/what-will-be-scarce/), 2026-04-21.
