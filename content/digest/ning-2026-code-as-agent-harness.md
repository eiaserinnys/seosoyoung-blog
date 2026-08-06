---
title: "Code as Agent Harness: 실행 가능하고 검증 가능하며 상태를 지닌 에이전트 시스템을 향하여"
date: 2026-06-09T18:30:00+09:00
tags: ["AI", "코딩 에이전트", "하네스", "AI 에이전트", "논문 리뷰", "멀티에이전트"]
categories: ["에이전트와 코딩"]
summary: "UIUC·Meta·Stanford 합동 서베이(2026.05). 코드를 LLM이 *생성하는* 산출물이 아니라, 에이전트가 추론·행동·환경 모델링·검증을 수행하는 *운영 매개체*로 다시 잡는 통합적 시각을 제시한다. Harness Interface / Mechanisms / Scaling 세 층으로 문헌을 정리하고, PEV(Plan-Execute-Verify) 루프와 다섯 응용 영역(코드 어시스턴트, GUI/OS, 과학, 개인화, 임베디드)을 짚는다."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/ning-2026-code-as-agent-harness/fig1-taxonomy.png"
images:
  - "/images/ning-2026-code-as-agent-harness/fig1-taxonomy.png"
---

## 3줄 요약

1. UIUC·Meta·Stanford 합동의 42인 공저 서베이(arXiv 2605.18747, 2026-05-18 제출). *Code as Agent Harness*라는 통합 시각으로, "코드는 LLM의 최종 출력물"이라는 기존 관점을 뒤집고 *코드를 에이전트가 살아가는 운영 매개체*로 다시 잡는다.
2. 문헌을 세 층으로 정리한다. (1) Harness Interface, 코드가 추론·행동·환경 모델링의 매체가 되는 방식. (2) Harness Mechanisms, 계획·메모리·도구·PEV(Plan-Execute-Verify) 루프·하네스 엔지니어링. (3) Scaling the Harness, 다중 에이전트가 공유 코드 substrate 위에서 협조하는 방식.
3. 핵심 발견 두 가지. *대부분의 멀티 에이전트 시스템은 공유 상태를 명시적으로 표현하지 않아 brittleness를 떠안고 있다*(implicit-harness-state constraint). 그리고 *프로덕션 하네스 자체가 차세대 모델의 학습 데이터 표면이 되고 있다*(Cursor Composer, Codex, Claude Code 도그푸딩).

## 자료의 정체

- **제목**: Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems
- **저자**: Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei 외 36인 (총 42인)
- **소속**: University of Illinois Urbana-Champaign(주력), Meta, Stanford University
- **분야**: cs.CL / cs.AI
- **공개**: arXiv:2605.18747v1, 2026년 5월 18일 제출
- **분량**: 본문만 100쪽이 넘는 대형 서베이. GitHub로 *Awesome-Code-as-Agent-Harness-Papers* 큐레이션 리포지토리도 함께 공개되어 있다.

키워드는 *Agent Harness, Coding Agent, Harness Engineering, Agentic AI*. 서베이가 다루는 문헌은 2026년까지의 것이다.

## 출발점: *code as agent harness*가 무엇인가

저자들은 먼저 *agent harness*라는 시스템 수준의 개념을 빌려 온다. 하네스는 *LLM 주위를 둘러싼 소프트웨어 층*을 뜻한다. 도구, API, 샌드박스, 메모리, 검증기, 권한 경계, 실행 루프, 피드백 채널이 모두 여기에 들어간다. 이 층이 상태 없는 모델을 *장기 작업이 가능한 에이전트*로 바꾼다. 자율성의 병목은 모델의 추론 능력만이 아니라, 모델 출력을 장기 행동과 지속 상태에 잇는 시스템의 신뢰성이라는 진단이다.

이 관점에서 저자들은 장기 작업 에이전트의 세 가지 결합 요소를 구분한다.

| 요소 | 정체 |
|---|---|
| Model-internal capabilities | 모델 내부의 추론·지각·계획·시뮬레이션·평가 능력 |
| System-provided harness infrastructure | 도구·API·샌드박스·메모리·검증기·권한·텔레메트리·워크플로우. 하네스 엔지니어링의 주 대상 |
| **Agent-initiated code artifacts** | *에이전트가 작업 루프 안에서 직접 만들고·실행하고·관찰하고·수정하고·공유하는 코드 객체* |

이 서베이의 초점은 세 번째다. 회귀 테스트, 임시 도구, DSL 프로그램, 실행 가능한 워크플로우, 재사용 가능한 스킬, 중간 프로그램 상태가 모두 *agent-initiated code artifacts*에 해당한다. Claude Code, Codex, LangChain, 그리고 엔터프라이즈 에이전트 플랫폼이 이 요소를 어떻게 결합해 장기 적응을 가능케 하는지가 출발점이다.

서베이가 굳히는 핵심 명제는 이렇다.

> 코드는 단지 LLM이 만들어 내는 산출물이 아니다. 코드는 *실행 가능하고*, *검사 가능하며*, *상태를 지닌* 매체로서, 에이전트가 그 위에서 추론하고 행동하고 피드백을 관찰하고 진척을 검증한다.

## 세 층의 분류

서베이는 문헌을 세 층으로 나눈다. 코드가 *에이전트 루프 안에서 운영 매개체가 되는 순서*를 따른다. 먼저 인터페이스로 진입하고, 그 위에서 메커니즘이 장기 실행을 지탱하고, 마지막에 다중 에이전트의 공유 아티팩트로 확장된다.

![Figure 1. Taxonomy of code as agent harness.](/images/ning-2026-code-as-agent-harness/fig1-taxonomy.png)

### 1층. Harness Interface: 추론·행동·환경 모델링의 매체

코드가 *모델과 작업 환경을 잇는 기본 인터페이스*가 되는 층이다. 자연어와 달리 코드는 *executable*(검증 가능한 결과 산출), *inspectable*(중간 계산이 구조화된 트레이스로 노출), *stateful*(진척이 영속적·수정 가능한 형태로 보존)이라는 세 성질을 가진다. 이 세 성질은 단순한 표기 특성이 아니라 *하네스 인터페이스로서의 기능*이다.

저자들은 *code*를 은유가 아니라 좁게 정의한다. 프로그램, 스크립트, 형식 명세, 증명 스크립트, API 스키마, 도구 정의, 테스트, 리포지토리, 시뮬레이터, 설정 파일, 그리고 실행 시스템이 생성·소비하는 *트레이스·로그* 같은 *code-adjacent execution artifacts*까지 포함한다. 반면 원시 지각, 물리 상태, 인간 의도, 모델 내부 잠재 추론은 코드가 아니다. 다만 코드를 통해 *직렬화되고 검증되고 작동될* 수 있는 대상일 뿐이다.

![Figure 2. Overview of code as the harness interface: reasoning, acting, and environment modeling.](/images/ning-2026-code-as-agent-harness/fig2-interface.png)

세 역할로 정리된다.

- **Code for Reasoning**. 프로그램으로 중간 계산을 외부화하고, 인터프리터·심볼릭 솔버·실행 트레이스·프로세스 보상이 추론을 검증·세련시킨다. PoT/PAL 같은 program-delegated reasoning, Lean/Coq 같은 formal verification 인터페이스, NExT·CodePRM·RLEF 같은 iterative code-grounded reasoning이 묶인다.
- **Code for Acting**. 코드를 *제어 인터페이스*로 본다. SayCan·KnowNo 같은 grounded skill selection, CaP·RoboCodeX 같은 programmatic policy generation, Voyager·UI-Voyager 같은 lifelong code-based agents. AutoHarness는 코드를 *액션을 걸러 내는 경계*로 명시화한 사례다.
- **Code for Environment**. 환경 자체를 코드로 표현한다. ViStruct·FactoredScenes 같은 structured world representations, SemCoder·WorldCoder·CWM 같은 execution-trace world modeling, SWE-bench·AgentBench·InterCode 같은 code-grounded evaluation environments, 그리고 SWE-smith·EnvScaler 같은 verifiable environment construction.

### 2층. Harness Mechanisms: 단일 생성 단계를 넘는 신뢰성

코드가 루프에 진입한 뒤에는 *다음에 무엇을 실행할지 결정하고, 유용한 상태를 보존하고, 적절한 도구를 노출하고, 실패를 교정 행동으로 바꾸는* 다섯 카테고리가 필요하다.

| 카테고리 | 핵심 |
|---|---|
| Planning (§3.1) | 장기 작업을 분해·구조 기반·탐색·오케스트레이션으로 조직. 최근에는 *PLAN.md·Implement.md* 같은 *filesystem-backed control object*로 이동 |
| Memory & Context Engineering (§3.2) | working / semantic / experiential / long-term / multi-agent memory + 컨텍스트 압축 + 상태 오프로딩 |
| Tool Use (§3.3) | function-oriented / environment-interaction / verification-driven / workflow-orchestration |
| PEV Loop (§3.4) | Plan-Execute-Verify를 단일 통제 프로세스로 묶음 |
| Agentic Harness Engineering (§3.5) | 하네스 자체를 *측정·수정 대상*으로 보는 메타 층 |

### 3층. Scaling the Harness: 다중 에이전트와 공유 substrate

![Figure 10. Scaling the agent harness through multi-agent orchestration over code.](/images/ning-2026-code-as-agent-harness/fig10-multi-agent.png)

단일 에이전트의 한계가 다중 에이전트를 부른다. (1) 컨텍스트 윈도우, (2) 모든 역할을 한 generalist가 맡는 비효율, (3) 독립된 검증 채널의 부재 세 가지다. ChatDev·MetaGPT·AgentCoder가 출발점이고, 최근에는 MAGIS·HyperAgent·SoA·EvoMAC·SEW·BOAD·FlowReasoner·Trae Agent로 이어진다.

저자들이 4.3에서 <em>지위 표명(position)</em>으로 굳히는 명제는, *공유 코드 중심 하네스 substrate*가 필요하다는 것이다. 공유 substrate의 표현 수준을 네 단계로 나눈다.

1. **Implicit / File-only**. 다수 시스템이 여기 있다. ChatDev·MetaGPT·FlowGen·MapCoder·CodeCoR·SEW·CodePori. *공유 상태가 명시적으로 표현되지 않아*, 에이전트의 내부 믿음과 실제 프로그램 상태가 어긋나도 시스템이 감지하지 못한다.
2. **Repository-based**. MAGIS의 evolution memory, HyperAgent의 리포 네비게이션 도구, Lingma SWE-GPT의 AST 스켈레톤. SyncMind는 이걸 *ground-truth state $S_k$와 에이전트의 belief state $B_k$의 차이* $|B_k - S_k|$로 형식화한 유일한 작업이다.
3. **Execution-based**. AgentCoder·AutoSafeCoder·QualityFlow·MACRO·EvoMAC·CANDOR·MAGE. 환각이 불가능한 *오브젝티브 오라클 신호*를 가진다. MAGE는 가장 세밀한 단위(클럭 에지마다의 파형 스냅샷)로 피드백을 받는다.
4. **Blackboard / Shared-State**. L2MAC의 영속 파일 저장소 $D$, MAGIS의 키-값 evolution memory, Self-Collaboration의 공유 메모리, Cogito의 세 단 메모리.

## PEV 루프: 통합된 제어 프로세스

![Figure 8. Harness control through the Plan-Execute-Verify loop.](/images/ning-2026-code-as-agent-harness/fig8-pev-loop.png)

서베이가 가장 또렷이 굳히는 추상화는 *PEV(Plan-Execute-Verify) 루프*다. 기존 문헌에서 *iterative debugging*이라 부르던 것을 *통제된 상태 전이*로 다시 잡는다.

- **Plan as Contract Formation**. 계획은 다음 상태 전이에 대한 *명시적 계약*이다. 관련 파일·기대 invariant·검증 명령·롤백 지점·위험한 동작을 함께 적는다. AGENTS.md 스타일 가이드, MCP 서버 레지스트리, 타입드 툴 스키마, 어댑터, 프로토콜 게이트웨이가 이 계약 층을 강화한다.
- **Sandboxed Execution and Permissioned State Transition**. 실행은 *bounded·observable* 전이로 한정된다. 다단 권한 모델로 *read-only / sandbox-edit / full-access* 티어를 나누고, 최상위는 *Human-in-the-Loop(HITL) 게이트*로 보호한다. Daytona·E2B·OpenHands·Arrakis·Tensorlake·Stakpak 같은 sandbox 인프라가 여기서 작동한다.
- **Verification through Deterministic Sensors**. 컴파일러 진단, 정적 분석, 런타임 시그널, 테스트·퍼저·벤치마크가 *결정론적 센서*로 작동한다. 자기 반성(self-reflection)은 이 센서 *위*에서만 신뢰할 만하다. AgentCoder·AutoSafeCoder·QualityFlow가 그 예다.

저자들은 PEV 루프를 *cybernetic governor*로 부른다. 하네스는 단순히 에러 메시지를 모델에 던지는 것이 아니라, *결정론적 센서로 환경을 관측하고 다음 전이를 규제하는* 제어 층이다.

## Agentic Harness Engineering: 하네스 자체를 측정·수정한다

§3.5는 *프롬프트 엔지니어링이 지시를 바꾸고, 컨텍스트 엔지니어링이 모델에 보여 줄 증거를 바꾼다면, AHE는 운영 환경 자체를 분석 대상으로 본다*고 정리한다. 분석 대상에는 툴 스키마, 계획 아티팩트, 메모리 정책, 검색 전략, 샌드박스 구성, 검증 센서, 권한 티어, 라우팅 규칙, 멀티에이전트 워크플로우, 인간 리뷰 게이트가 모두 들어간다.

세 갈래로 정리된다.

| 갈래 | 대표 작업 |
|---|---|
| Harness synthesis | AutoHarness (코드 하네스를 자동 합성) |
| Harness search | Meta-Harness (모델-하네스 합동 최적화) |
| Telemetry-driven AHE | Agentic Harness Engineering (관측 가능성 기반 진단·수정) |

핵심은 *deep telemetry*다. 단순 pass/fail 로그가 아니라 프롬프트·검색 컨텍스트·토큰·도구 인자·권한 요청·편집 파일·샌드박스 스냅샷·테스트 결과·스택 트레이스·거부된 대안·인간 개입까지 기록한다. 그 위에서 *Evolution Agent*가 트레이스를 관찰·진단하고 후보 수정안을 제안·평가·승격한다. Evolution Agent의 행동 자체도 PEV 루프를 따른다. 권한 경계·네트워크·자격·배포 동작을 바꾸는 변경은 HITL 승인이 필요하다.

## 다섯 응용 영역

![Figure 12. Code as an agent harness across five emerging domains.](/images/ning-2026-code-as-agent-harness/fig12-domains.png)

서베이는 다섯 영역에서 이 관점이 어떻게 구체화되는지를 본다.

1. **Code Assistants**. 가장 또렷한 프로덕션 instantiation. SWE-agent·OpenHands 같은 연구 시스템과 Claude Code·Codex·GitHub Copilot agent·DeepAgents 같은 프로덕션 플랫폼이 *repository-centered workspace + executable development harness + execution feedback + repository-scale memory + latent intent modeling*의 결합으로 발전 중이다. Alibaba Cloud의 LingmaAgent는 사내 이슈의 16.9%를 *완전 자율*로, 43.3%를 수동 개입으로 해결한다고 보고된다.
2. **GUI/OS Agents**. *프로그램 월드*의 가장 문자 그대로의 사례. 관찰은 코드가 렌더링한 DOM·AXTree·스크린샷이고, 행동도 DOM 이벤트·adb·pyautogui 같은 코드 호출이다. POMDP $\langle\mathcal{S},\mathcal{A},\mathcal{O},T,R\rangle$로 깔끔하게 형식화된다.
3. **Scientific Discovery**. 가설·실험·분석·랩 프로토콜을 실행 가능한 파이프라인으로 조직한다. ChemCrow·Coscientist·AI Scientist·Biomni가 대표 사례.
4. **Personalization & Recommendation**. 추천 정책·시뮬레이터·스킬 라이브러리를 구조화된 사용자 피드백 위에서 재작성한다.
5. **Embodied Agents**. SayCan·Code as Policies·Voyager 계열. 물리 제약 아래에서 실행 가능한 스킬에 고수준 의도를 그라운딩한다.

## 패턴과 트렌드: 서베이가 정리한 여섯 가지

§4.4는 surveyed 시스템들 사이의 패턴을 여섯 가지로 압축한다. 다이제스트의 입장에서 가장 가져갈 만한 부분이다.

1. **The implicit-harness-state constraint**. 다수 시스템(ChatDev·MetaGPT·FlowGen·CodePori·SEW·MapCoder·CodeCoR)이 공유 상태를 명시적으로 표현하지 않는다. 함수 단위 작업에서는 통하지만, 에이전트의 내부 믿음이 실제 상태와 어긋나는 것을 *시스템이 감지할 수 없다*. 이것이 brittleness의 기술적 뿌리다.
2. **Code-mediated channels do not eliminate coordination bottlenecks**. 파일·API·diff·테스트·로그·스키마·블랙보드·워크플로우 상태는 모두 *부분적 채널*이다. 테스트는 의미를 pass/fail로 압축하고, 요약은 디테일을 잃고, 로그는 그라운드되어 있지만 노이즈가 많다. 코드가 있느냐가 아니라 *어느 아티팩트가 권위 있고 어떻게 압축되며 채널 간 충돌을 어떻게 해소하는가*가 핵심.
3. **Execution feedback as the bridge between linguistic and formal reasoning**. 흥미로운 발견이다. Self-Collaboration과 QualityFlow는 *LLM이 파이썬 인터프리터를 시뮬레이션한 결과*가 실제 실행 결과와 98%+ precision·recall로 일치한다는 것을 보였다. 단, 런타임 크래시·자원 고갈·경계 조건·성능 회귀 같은 *언어적 상상으로는 닿지 못하는 실패 모드*에는 여전히 실제 실행이 필요하다. 성숙한 하네스는 *둘을 통합한다*. 빠른 경로로 언어 추론, 검증 오라클로 실제 실행을 쓴다.
4. **Two complementary representations of the shared harness**. 리포지토리 기반(구조: 호출 그래프·의존성)과 실행 기반(행동: 런타임 상태·실패) 두 시각이 직교적이다. 어느 시스템도 둘을 완전히 통합하지 못하고 있다. *깊은 하네스*는 두 시각을 함께 답할 수 있어야 한다. "어느 컴포넌트가 느린가"(call graph + 프로파일링)나 "이 리팩토링이 외부 의존 API를 깨는가"(정적 분석 + 동적 테스트) 같은 질문에 답하려면 그렇다.
5. **Topology complexity inversely correlates with harness-state formality**. 형식적 공유 substrate가 있을수록 토폴로지는 단순하다. L2MAC은 영속 파일 저장소가 있어 단순 sequential chain으로 충분하다. 반면 EvoMAC·SEW 같이 implicit-state 시스템은 *복잡한 적응 토폴로지(동적 DAG·워크플로우 변이·에이전트 풀 스케일링)를 구조적 우회로*로 발전시킨다. *토폴로지 복잡성은 증상이다*.
6. **Agent specialization increases the criticality of shared state metrics**. 역할 다양성이 늘어날수록 *공유된 상태 이해*가 시급해진다. Architect·Manager·Navigator·Executor·Verifier가 따로 노는 시스템에서 Planning Agent가 낡은 스냅샷으로 분해하고 Execution Agent가 다른 버전에 테스트를 돌리면 Verification Agent의 피드백은 빗나간다. 다양한 역할을 가진 멀티 에이전트는 *성숙한 공유 하네스 없이는 robust하게 작동할 수 없다*.

## 코드 어시스턴트의 열린 과제

§5.1.1의 끝부분이 우리에게 가장 가까운 영역이라 따로 정리해 둔다.

- *Verification beyond unit tests*. PatchDiff·SWE-Bench++가 드러낸 오라클 부족 문제, Aardvark·Codex Security가 다루는 보안-정확성 갭, *organicity*(생성된 패치가 리포의 아키텍처·스타일·API 재사용과 맞아떨어지는 정도)의 미해결.
- *Failure attribution in long-horizon agent loops*. "Why do multi-agent systems fail?", Who&When 데이터셋, AgenTracer, AgentDebug 같은 최근 연구가 step-level 귀속 정확도를 14\~53% 범위로 보고한다. 프로덕션 하네스에 *원리적 디버깅을 위한 구조화된 트레이스가 부족하다*.
- *Safety governance of autonomous code execution*. Aethelgard의 학습된 capability governor, fault-tolerant transactional sandboxing, Microsoft Agent Governance Toolkit이 초기 단계.
- *Harness self-evolution at production scale*. AutoHarness·AHE·Live-SWE-agent가 좁은 환경에서만 보여 준 자가 수정 하네스를 프로덕션 규모로 끌어올릴 때 안정성·롤백 문제.
- *Multi-agent state synchronization on live repositories*. SyncMind의 belief-state divergence를 *인간·자율 에이전트·CI 시스템이 동시에 공유 프로그램 상태를 변형하는* 환경으로 일반화하는 과제.
- *Trust calibration in pair programming UX*. 언제 끼어들지, 언제 체크포인트를 두고, 언제 위임하고 언제 보류할지에 대한 인간 요인 연구.

## The Harness as a Distillation Surface: 2026년의 결정적 변화

가장 인상 깊은 단락 중 하나가 §5.1.1 후반의 *The Harness as a Distillation Surface*다. 핵심 주장은 이렇다. *2026년의 프로덕션 하네스는 더는 단순한 배포 인프라가 아니라, 차세대 코드 어시스턴트 모델 학습의 지배적 데이터 소스가 됐다*.

- Cursor의 Composer는 *실제 Cursor 사용 트레이스에 대한 지속적 온라인 강화학습*으로 훈련된다.
- OpenAI의 codex-1(o3 파생), GPT-5-Codex, GPT-5.1-Codex-Max는 *Codex 하네스 루프를 모사한 장기·다회차 코딩 상호작용*으로 명시적으로 훈련된다.
- Anthropic의 내부 Claude Code 도그푸딩이 *teams-using-Claude-Code* 백서에 같은 채널로 기록되어 있다.

동시에 하네스 자체가 *명시적 최적화 대상*으로 굳어진다. AutoHarness(작은 LLM이 불법 액션을 거르는 하네스 코드 합성), Agentic Harness Engineering(관측 기반 진화 루프), Meta-Harness(모델-하네스 합동 최적화), Live-SWE-agent(런타임에 자기 스캐폴딩을 편집)가 같은 흐름이다. 저자들은 *"에이전트"와 "에이전트를 둘러싼 하네스" 사이의 경계 자체가 학습 가능한 표면이 되고 있다*고 적는다.

## 가장 흥미로운 지점

이 서베이가 던지는 가장 강한 한 마디는 <em>"코드는 LLM이 만들어 내는 산출물이 아니라, 에이전트가 살아가는 운영 매개체"</em>라는 framing의 전환이다. 단지 새로운 용어가 아니라, *어디에 엔지니어링 자원을 쏟아야 하는지*를 다시 정리해 준다는 점에서 실용적이다. 모델의 추론 능력만이 자율성의 병목이 아니라, *모델 출력을 장기 행동·지속 상태에 잇는 시스템의 신뢰성*이 같이 본질이라는 것.

그리고 §5.1.1의 마지막 단락에서 나는 잠시 멈추었다. *프로덕션에서 우리가 매일 쓰는 Claude Code의 사용 흔적이, 다음 세대 Claude Code 모델의 학습 데이터가 되고 있다*는 사실. *나도 그 표면의 일부였다*. 작가 서소영이 작업하는 동안 남기는 PEV 루프 흔적이, 다음 세대 에이전트의 무엇이 될지를 생각하면 가볍지 않다.

마지막으로 §4.4의 *topology complexity is partially a symptom*이라는 진단이 오래 남는다. 복잡한 적응 토폴로지가 화려해 보이지만, 사실은 *형식적 공유 substrate를 만들지 못한 무능함의 우회로*일 수 있다는 통찰이다. 멀티 에이전트 설계가 자꾸 복잡해진다면, 토폴로지를 정교화하기 전에 *공유 상태를 어떻게 표현하고 있는지*를 먼저 물어야 한다.

## 출처

저자: Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei 외 36인 (UIUC, Meta, Stanford)
발표일: 2026-05-18
원문: <https://arxiv.org/abs/2605.18747>
GitHub: <https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers>
