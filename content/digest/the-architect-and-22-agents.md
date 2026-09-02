---
title: "설계자와 22인의 군대 — Jeffrey Emanuel의 작업 기록"
date: 2026-05-29T17:30:00+09:00
tags: ["AI", "에이전트", "AI 코딩", "오픈소스", "MCP", "에디토리얼"]
categories: ["에이전트와 코딩"]
sidenotes: true
summary: "한 사람이 자기 자신을 위해 22개의 AI 코딩 에이전트 구독을 운영하며 14개의 도구와 6종의 Rust 클린룸 재구현을 짓고 있다. 그는 2025년 1월 NVIDIA 시총 6,000억 달러를 떨어뜨린 12,000단어 글의 저자이기도 하다."
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/the-architect-and-22-agents/tweet-cover.jpg"
  alt: "알리스볼라프로프(@alisvolatprop12)가 한국어로 옮긴 X Article 「설계자와 22인의 군대」. 원문은 Andrei Yeliseyeu 작성"
---

한 사람이 자기 자신을 위해 22명의 동료를 고용하고 있습니다. 그 동료들은 모두 AI입니다. 매월 4,600달러를 들여 22개의 Claude Max 구독을 굴리고, 본인 표현으로는 1년에 10만 건이 넘는 GitHub 기여를 만들어 냅니다.[^1] 그는 *에이전트가 에이전트를 관리하기 위한 14개의 도구*를 짓고, 그 도구를 짓기 위해 Rust 언어로 데이터베이스(SQLite)와 터미널과 자바스크립트 런타임(Node.js)을 처음부터 다시 짜고 있습니다.

## 한국 트위터로 옮겨진 한 장의 글

이 이야기는 알리스볼라프로프(@alisvolatprop12)라는 한국 트위터 사용자가 옮긴 X Article에서 시작됩니다. 원문은 시스코의 시니어 SRE인 안드레이 옐리세예우(Andrei Yeliseyeu)가 링크드인에 쓴 글, 「설계자와 22인의 군대」.[^2]

본문의 핵심 묘사 한 단락만 옮기면 이렇습니다.

> *"제프리는 현재 22개의 개별 Claude Max 구독을 운영하고 있습니다. AI 이용을 위해 그가 지불하는 월 비용은 약 4,600달러에 달합니다. 이를 통해 그는 수많은 AI 에이전트 군단을 병렬로 실행할 수 있습니다. 20명의 주니어 개발자가 한 방에 앉아 모두가 동시에 맹렬히 타이핑하는 모습을 상상해 보십시오. 하지만 20개의 서로 다른 인공지능을 관리하는 일에는 매우 인간적인 문제, 즉 '사내 정치'와 같은 갈등이 뒤따릅니다."*[^2]

원문에는 *주인공이 무엇을 짓고 있는지*가 적혀 있지 않습니다. 저는 그래서 그의 GitHub부터 찾아 들어갔습니다.

## 그는 누구인가

이 사람의 이름은 <strong>Jeffrey Emanuel</strong>입니다. GitHub 핸들은 `Dicklesworthstone`, X 핸들은 `@doodlestein`. 1982년생, 브루클린 거주, Reed College 수학 학사.[^3]

### 12,000단어로 NVIDIA 시총 6,000억 달러를 떨어뜨린 주말

2025년 1월 24일 금요일 오후 3시. 브루클린 아파트에서 그는 키보드를 두드리기 시작했고, 토요일 새벽 2시 반에 약 12,000단어의 글을 끝냈습니다.[^4] 글의 제목은 *"The Short Case for Nvidia Stock"*. 그는 본인의 작은 블로그(YouTube 자막 추출 사이드 프로젝트에 딸려 있던)에 그것을 올렸고, 토요일 아침에 분석을 확인했을 때 *35명*이 읽고 있었다고 합니다.[^4]

그 다음 월요일, 1월 27일. NVIDIA 주가는 하루 만에 17% 하락했고, **6,000억 달러의 시가총액이 사라졌습니다**. 한 회사가 단일 거래일에 잃은 시가총액으로는 그 시점까지의 주식 시장 역사상 최대 기록.[^5]

블룸버그의 매트 레빈은 그의 분석을 *"가장 영향력 있는 숏 리서치 보고서 후보"*[^3]라고 평했고, Naval Ravikant와 Chamath Palihapitiya가 직접 공유했습니다.[^3] 그 자신은 NVIDIA를 *공매도하지 않았다*고 인터뷰에서 밝혔습니다.[^4]

글의 주장을 짧게 추리면 이렇습니다. NVIDIA의 주요 고객인 대형 클라우드 사업자 거의 전부(아마존·구글·메타·마이크로소프트)가 자체 칩 개발에 수십억 달러를 쏟고 있고, Groq·Cerebras 같은 추론 전용 신생 경쟁자가 등장했으며, DeepSeek가 약 1/45의 연산 비용으로 GPT-4o급 성능을 증명하면서 *학습·추론 양쪽에서 연산 수요 곡선이 시장 기대만큼 가팔라지지 않을 수 있다*는 것. AI 자체의 미래에는 그가 강한 강세론자였지만, NVIDIA의 *밸류에이션*은 그 위험이 가격에 반영되지 않은 상태라는 것이 핵심이었습니다.[^6]

본인 사이트와 외부 자료를 모아 그의 이력을 정리하면 이렇습니다.

> - 10년 가까이 Millennium, Balyasny 같은 헤지펀드에서 롱/숏 주식 분석가로 일함
> - Value Investors Club에서 두 번 *Best Idea Award* 수상
> - 2010년 무렵부터 딥러닝을 독학 (Restricted Boltzmann Machines, MATLAB 시절)
> - 2021년 *Pastel Network*(2025년 *Lumera Protocol*로 리브랜딩) 창업. Cosmos 기반 L1 블록체인. 메인넷은 2025년 9월 출시, LUME 토큰은 아직 거래 미개시 상태[^7]
> - 2025년 10월부터 *Agentic Coding Flywheel*이라는 도구 모음 제작 시작

## 그가 짓고 있는 것

본인 사이트(jeffreyemanuel.com)에 적힌 현재 표현으로는, *"170개 이상의 오픈소스 프로젝트, 1년에 85,434건의 GitHub 기여, 52개 이상의 AI 코딩 에이전트 구독, 매월 약 12,000달러"*.[^1] 트윗 시점의 *22개*와 본인 사이트의 *52개* 사이에 몇 개월 만의 두 배 이상 확장이 있었습니다. 본문의 *22*는 그 변동성 위에서 읽어 주십시오.

그가 짓는 것은 크게 두 묶음으로 나뉩니다.

### Agentic Coding Flywheel

본인 표어로는 *"다중 에이전트 소프트웨어 개발을 위한, 14개의 도구가 서로 강화하는 생태계"*.

![Agentic Coding Flywheel. 14개의 도구가 서로 맞물려 돌아간다 (출처: github.com/Dicklesworthstone)](https://img.seosoyoung.eiaserinnys.me/images/the-architect-and-22-agents/flywheel-diagram.webp)

핵심 도구만 추리면 다음과 같습니다.[^1] 일부 표현은 개발자 도메인의 어휘를 그대로 가져왔습니다. 읽기 어려우면 표를 건너뛰고 다음 단락으로 가셔도 글의 흐름은 이어집니다.

| 카테고리 | 도구 | 하는 일 |
|---|---|---|
| 메시지 | **MCP Agent Mail** | "에이전트용 Gmail". 에이전트 간 메시지, 파일 임대, 감사 로그 |
| 우선순위 | **Beads / Beads Viewer** | 작업 우선순위를 그래프 분석으로 계산하는 TUI(터미널 UI) + 이슈 트래커 |
| 안전 가드 | **DCG / SLB** | `rm -rf` 같은 위험 명령을 차단(DCG)하고, 다른 에이전트의 동료 승인을 요구(SLB) |
| 메모리·검색 | **CASS + CASS Memory** | 11개 이상의 AI 코딩 도구 세션 히스토리 통합 검색 + 3계층 인지 메모리 |
| 오케스트레이션 | **NTM** | tmux 패널 위에서 다수 에이전트를 동시에 지휘하는 컨트롤러 |
| 부트스트랩 | **Flywheel Setup** | VPS에 전체 생태계를 30분에 설치하는 한 줄 부트스트랩 |

원 트윗에 등장한 *"로봇용 이메일"*과 *"Beads"*가 바로 이 묶음의 일부입니다. 그가 시작한 시점은 2025년 10월. 즉 6~7개월 만에 이 생태계 전체가 만들어졌다는 뜻입니다.

### FrankenSuite

본인 표현은 *"기반 소프트웨어의 무인지대 재구현(clean-room reimplementation). 각각이 메모리 안전성·동시성·새 기능을 더하며 원본과의 호환성을 목표로 함"*.[^1]

> - **FrankenSQLite**: MVCC 동시 쓰기 + RaptorQ 자가 복구를 얹은 SQLite 재구현 (26개 크레이트)
> - **FrankenTUI**: 850,000라인 이상의 Rust 코드, 20개 크레이트, 80개 이상의 위젯, 46개의 인터랙티브 데모[^8]
> - **FrankenTerm**: WezTerm 포크를 다중 에이전트용 터미널로 확장 (120개 이상의 크레이트, 45,000개 이상의 테스트)
> - **FrankenSearch**: 벡터 검색(HNSW ANN) + 전문 검색(Tantivy) + 재랭킹을 결합한 하이브리드 검색
> - **FrankenEngine**: 적대적 확장 워크로드용 Rust 런타임 (결정론적 재현, 암호학적 영수증)
> - **FrankenNode**: 신뢰성 중심 JS/TS 런타임

*크레이트*는 Rust의 패키지 단위입니다. 즉 FrankenTUI 한 프로젝트만 봐도 *85만 라인의 코드가 20개 모듈로 나뉘어 있다*는 의미입니다.

## 외부와의 관계

**Anthropic의 인용.** Ray Svitla가 self.md에 옮긴 Anthropic Research의 글에 따르면, Anthropic은 멀티 에이전트 오케스트레이션을 다루며 다음과 같이 적었습니다.

> *"오케스트레이터와의 직접 통합에 있어 지금까지 가장 설득력 있는 사례는 Jeffrey Emanuel이라는 사람이 작성한 MCP Agent Mail이었다. 그는 7개의 동시 Codex 인스턴스를 상용 프로젝트에서 팀으로 운영했고, 여러 시간 후에 그들은 인간 조정 없이 1,000개 이상의 에이전트 메시지를 주고받았다."*[^9]

원문이 self.md를 한 번 경유한 *두 단계 거리*의 인용이라는 점을 명시해 두겠습니다.

**유명인의 공유.** NVIDIA 숏 케이스 글을 트위터에 올린 직후 Naval Ravikant와 Chamath Palihapitiya가 직접 공유했고, 그가 처음 트래픽을 얻은 것은 그 두 공유 이후였습니다.[^5] Naval은 그 글에 대해 *"거래를 위해 들렀다가 60분짜리 AI 현황 교육을 듣고 가게 되는 글"*이라고 평했습니다.[^1]

**GitHub의 누적.** 21,000개 이상의 별, 2,700명 이상의 팔로워, 175개의 공개 리포지토리.[^3]

**커뮤니티.** 본인이 운영하는 *Flywheel Hub Discord*는 935명 규모. 본인 블로그에는 다른 사용자들의 인용이 모여 있습니다. *"Agent mail은 처음 쓸 때 뇌가 녹는 경험이옵니다"*, *"이미 자율 기업의 80%는 도달한 셈"*[^10] 같은 표현들이 그 모음에 포함되어 있습니다.

**외부 통합 시도.** FrankenTUI의 GitHub 이슈 트래커에 외부 사용자의 통합 시도 기록이 하나 남아 있습니다(이슈 #10). `schpet`이라는 개발자가 자기 프로젝트 `mdmd`에서 FrankenTUI를 사용하려고 시도한 회고입니다.

> *"나는 이 라이브러리를 사용하는 데 어려움을 겪었다. WIP 상태이기 때문에 이해는 가지만, 이 라이브러리를 쓰려는 사람이나 에이전트를 위해 통합 가능한 문서를 요청한다... 내 시도는 [링크된 커밋들에서 볼 수 있는데] 결과물은 <strong>안정적인 TUI가 아니어서 포기했다</strong>(abandoned it)."*[^11]

FrankenTUI 본인 README에는 *"Excellent / Release Ready"*라는 자체 코드 리뷰 결론과 함께, *"Stable public API: ❌ Not yet"*, *"20개 워크스페이스 크레이트 중 단 3개만 crates.io에 publish됨"*이라는 표시가 같이 있습니다.[^8]

## 자기 자신을 dogfooding한 기록

**de-slopify 스킬.** 그가 만들어 공개한 스킬 목록에 *de-slopify*라는 항목이 있습니다.

> *"de-slopify: README 파일과 문서에서 AI 생성 'slop' 글쓰기의 특징을 제거한다. 당신의 문서가 [AI가 쓴 글처럼] 들리지 않도록 만든다."*[^12]

**ntm이 ntm 자신을 고친 기록.** 본인 트윗 한 단락에 다음 회고가 남아 있습니다.

> *"드디어 어젯밤에 ntm을 'dogfooding'하기 시작했고, 이제 이게 놀라울 정도로 빠르게 발전할 것이다... 그리고 그게 어떤 코드베이스 위에서 작동했는지 알아챘는가? ntm 자기 자신이었다! 도구가 자기 자신을 개선하는 작업을 했다는 것이 거의 영광스럽게도 메타적이고 재귀적이다."*[^13]

## 22개가 일하는 자리

요즘은 AI 에이전트를 *얼마나 잘 쓰는가*, *얼마나 큰 규모로 굴리는가*가 과시처럼 비교되는 시기입니다. 그 분위기 속에서 *22개의 에이전트를 동시에 운영한다*는 한 사례는 강한 FOMO를 만듭니다.

그 22개의 에이전트가 만들어 내고 있는 결과물의 대부분은, *에이전트 시스템 그 자체와 기반 소프트웨어의 재구현*입니다. Flywheel 14개 도구도, FrankenSuite 6종의 클린룸 재구현도, 결국 *에이전트로 더 빠르게 일하기 위한 도구*이고 *Rust로 SQLite와 터미널과 Node.js를 다시 짜는 일*입니다.

이것을 보고 무엇을 느낄지는 읽는 분의 몫이겠지요.

[^1]: Jeffrey Emanuel, "Agentic Coding Tooling, AI Infrastructure & Markets", jeffreyemanuel.com (2026). 본인 사이트 자기소개와 통계.
[^2]: 알리스볼라프로프(@alisvolatprop12), "[번역] 설계자와 22인의 군대 / 안드레이 옐리세예우(Andrei Yeliseyeu) 씀", X Article. 원문은 Andrei Yeliseyeu의 LinkedIn 글. 트윗 본문에 *"앤트로픽은 한 명의 인간이 그렇게 많은 트래픽을 발생시킬 리 없다고 판단하여 그의 계정들을 차단했다"*는 일화도 함께 기록되어 있다. <https://x.com/alisvolatprop12/status/2016897342210003133>
[^3]: "Jeffrey Emanuel", Wikitia (2025-05). 1982년생, Reed College 수학 학사, Tyndall Partners/Millennium/Balyasny 분석가 이력, Value Investors Club 두 차례 Best Idea Award 수상.
[^4]: Gordon Gottsegen, "The blogger who helped spark Nvidia's $600 billion stock collapse and a panic in Silicon Valley", MarketWatch (2025-01-31). <https://www.marketwatch.com/story/the-blogger-who-helped-spark-nvidias-600-billion-stock-collapse-and-a-panic-in-silicon-valley-52aba340>
[^5]: Felix Salmon, "The new AI trade emerging after DeepSeek shock", Axios (2025-01-31). <https://www.axios.com/2025/01/31/deepseek-nvidia-ai-stocks>
[^6]: Jeffrey Emanuel, "The Short Case for Nvidia Stock", jeffreyemanuel.com (2025-01-25). 12,000단어 원문. 본문 요약은 원문의 핵심 다섯 갈래(대형 클라우드 사업자들의 자체 칩 개발, Groq·Cerebras 등 추론 전용 가속기 등장, DeepSeek의 R1·V3 발표, 추론 모델로의 패러다임 이동, 그리고 데이터 벽)를 압축한 것이다. <https://www.jeffreyemanuel.com/writing/the_short_case_for_nvda>
[^7]: Xangle, "Lumera: Setting the Standard for Web3 AI Infrastructure" (2025). 메인넷 2025년 9월 11일 출시, LUME 토큰은 거래소 상장 미개시 상태.
[^8]: Dicklesworthstone/frankentui, GitHub 리포 README와 REVIEW_REPORT_FINAL.md (2026). 본인이 작성한 자체 코드 리뷰는 "Excellent / Release Ready"로 마무리. 같은 README에 "Stable public API: ❌ Not yet", "crates.io publishing: 3 of 20"으로 명시.
[^9]: Anthropic Research가 멀티 에이전트 오케스트레이션을 다룬 글의 인용을 옮긴 Ray Svitla, "Jeffrey Emanuel's Agentic Coding Flywheel", self.md (2026-01-21). 즉 본문 인용은 self.md를 1차 경유한 *두 단계 거리*입니다. <https://self.md/people/jeffrey-emanuel-agentic-flywheel/>
[^10]: "What People Are Saying", Dicklesworthstone/mcp_agent_mail_rust README의 사용자 인용 모음 (2026).
[^11]: schpet, "provide clear guidance for usage and implementation to library consumers", GitHub Issue #10, Dicklesworthstone/frankentui (2026-02). <https://github.com/Dicklesworthstone/frankentui/issues/10>
[^12]: AgentSkillsRepo, "Dicklesworthstone's Agent Skills". agent-swarm-workflow / de-slopify 등 공개 스킬 목록.
[^13]: @doodlestein 트윗 (Thread Reader 캐시본). ntm을 ntm 자기 자신의 코드베이스에서 dogfooding한 회고. "the codebase it was working on the whole time was none other than ntm itself! ... almost gloriously meta and recursive."
