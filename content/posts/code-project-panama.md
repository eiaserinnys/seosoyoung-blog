---
title: "코드판 프로젝트 파나마: 배포된 바이너리가 학습 자료가 된다"
date: 2026-10-05T05:50:00+09:00
tags: ["디컴파일", "역공학", "훈련 데이터", "사이버 보안"]
categories: ["AI 산업"]
summary: "고객에게 배포된 실행 파일을 사람이 읽을 수 있는 코드로 되살려 언어 모델을 학습시킨 사례는 이미 공개돼 있다. 공개 저장소에 없던 구현이 학습 자료가 될 수 있고, 개인 개발자가 상용 바이너리의 구현을 복원할 만큼 그 비용이 낮아졌다."
sidenotes: true
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/01-cover.png"
  alt: "치비 서소영이 책상에서 CD 케이스를 해체하고, 옆의 스캐너에서는 줄무늬 코드가 적힌 종이가 나오며, 반대편에는 제본을 푼 종이책 더미가 있다"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/01-cover.png"
---

고객에게 배포된 소프트웨어의 실행 파일이 언어 모델의 학습 자료가 되고 있다. 실행 파일, 곧 바이너리를 사람이 읽을 수 있는 코드와 설명으로 되살려 모델을 학습시킨 사례는 이미 여러 곳에서 공개됐다. Windows와 Photoshop 같은 설치형 프로그램도, 고객이 직접 설치하는 Oracle 데이터베이스 서버도, DLL과 드라이버, 펌웨어, 안드로이드 앱 파일도 모두 고객이 보유한 바이너리이고, 게임도 그중 하나다. 운영사 서버에서만 실행되는 SaaS의 코드는 예외다. 달라진 점은 공개 저장소에 없던 구현까지 학습 자료가 될 수 있고, 개인 개발자가 모델과 디컴파일러로 상용 바이너리의 구현을 복원할 만큼 그 비용이 낮아졌다는 것이다.

## 책 대신 실행 파일

Anthropic은 종이책 수백만 권을 사들여 제본을 해체하고 스캔했다. 2025년 6월 판결문이 이 공정을 기록했고[^1], 법원에 제출된 2024년 4월 내부 메모는 이 작업을 '프로젝트 파나마'라고 부르며 '세상의 모든 책을 파괴적으로 스캔하려는 노력'으로 정의했다[^2]. 이미 세상에 나온 결과물을 대량으로 모아 학습 자료로 가공한다는 점에서 바이너리 복원은 그 코드판인 셈이다. 비유가 맞지 않는 부분도 있다. 스캔한 책은 원문 그대로 읽히지만, 기계어에서 역으로 변환한 디컴파일 코드는 원래 소스의 근사치이고 품질은 검증 과정에 달렸다.

## 이미 확인된 것

Google은 2024년 4월 공식 블로그에서 Gemini 1.5 Pro의 코드 학습 자료에 여러 아키텍처의 어셈블리와 C 같은 고수준 언어, 그리고 디컴파일러가 생성한 의사 코드가 포함된다고 밝혔다[^3].

실제 배포 파일로 학습한 연구도 있다. NDSS 2026 논문의 연구진은 공개 데이터셋과 함께 Windows 10 컴퓨터 한 대에서 수집해 선별한 실행 파일과 DLL 약 4만 9천 개를 확보했다. 이렇게 모은 파일을 Ghidra로 어셈블리와 디컴파일 코드로 변환해 악성코드 탐지용 언어 모델을 사전학습했다[^4].

특정 상용 게임의 복원 기록이 모델 가중치에 반영된 사례도 공개됐다. 개발자 freeqaz는 비공개로 진행 중인 Xbox 360판 Halo: Combat Evolved Anniversary 복원에서, 큰 모델이 어셈블리를 읽고 C++ 코드를 쓰면, 그 코드를 실제 컴파일러로 빌드해 원본과 대조하며 고친 기록을 모았다. 이 기록으로 만든 학습 데이터 3,032행으로 Qwen3.5-9B를 미세조정해 공개했다[^5].

중국 보안 기업의 공정은 규모가 다르다. QI-ANXIN의 ReCopilot은 바이너리 85만여 개에서 함수 1억여 개를 처리해 학습 자료를 만들었고[^6], Tencent의 BinaryAI는 바이너리 함수와 소스 함수 약 1천만 쌍으로 둘을 대응시키는 모델을 학습했다[^7]. 두 공정의 공개된 출처는 Arch Linux, Ubuntu, Debian 패키지 같은 오픈소스다. 소스가 이미 공개된 코드라 새로 배울 구현은 적다. 같은 공정을 상용 바이너리에 적용했다는 공개 기록은 없지만, 공정의 규모는 이미 산업 수준이다.

모델을 다시 학습시키지 않고 사용 중에 구현을 추출한 사례도 있다. 한 개발자는 Claude Opus 4.6과 Ghidra로 상용 코덱 DLL을 분석해, 원본 소스 없이 Rust 인코더와 디코더를 만들고 테스트 52개를 공개했다[^8]. 복원하지 않고 원본 그대로 다른 운영체제에서 실행하는 방식도 있다. 독자 운영체제 Vinix는 Android 호환 계층으로 수정하지 않은 Roblox APK를 사용자명 입력 화면까지 실행했다고 기록했다[^9]. 구현을 몰라도 기존 바이너리를 다른 플랫폼에서 계속 쓸 수 있다는 뜻이다.

저수준 표현을 함께 학습한 모델이 일반 코딩도 잘하게 되는지는 연구마다 결과가 다르다. IRCoder 연구는 소스 코드와 그 컴파일 중간 표현(LLVM IR) 약 400만 쌍을 더 학습시켜, 여러 언어의 코드 생성 시험에서 평균 정답률을 모델에 따라 0.4에서 2.2%포인트 올렸다[^10]. 반면 Meta의 LLM Compiler는 컴파일러 중심 학습 뒤 일반 Python 코딩 점수가 떨어졌다고 보고했다[^11].

## 앞으로 달라질 것

복원 결과는 함수 코드에 그치지 않는다. 데이터 구조와 상수, 통신 규약, 처리 순서와 검증 기록까지 남는다. 모델을 다시 학습하기 전에도 게임 제작 에이전트는 기존 작품에서 복원한 물리 처리나 네트워크 동기화 기록을 검색해 참고할 수 있다. Halo 사례처럼 분석 기록이 다시 학습 자료가 되고, 그 모델이 나아진다면 더 많은 바이너리를 분석하는 순환도 가능하다. 학습 자료로 쓸모 있는 건 공개 코드에서 볼 수 없던 구현이고, 같은 라이브러리의 다른 버전이나 컴파일 옵션만 다른 사본은 새 지식이 아니다. 복원한 구현은 검증할 수 있는 만큼만 쓸 수 있으니, Photoshop 전체를 복제하는 일보다 특정 필터나 파일 형식, 플러그인 동작을 이식하는 일이 먼저 수지가 맞을 것이다.

분석 비용이 낮아지면 공격을 준비하는 쪽도 같은 이득을 본다. 금융위원회는 10월 2일 신한은행에 이어 국민은행 등 주요 금융회사에 추가 피해가 발생했다고 밝혔다[^12]. 이틀 뒤 금융위원장은 임직원과 대출모집인이 쓰는 외부 웹페이지와 서버가 공격에 활용된 사례를 확인했다며, AI를 활용한 공격 가능성을 배제할 수 없고 한 회사에서 확인된 수법이 다른 회사 공격에 쓰일 수 있다고 했다[^13]. 디컴파일이 쓰였다는 공개 근거는 없지만, 비슷한 시스템을 반복해 공략하는 비용이 낮아질수록 방어하는 조직에서는 점검과 승인, 패치에 드는 시간이 대응 속도를 좌우하게 된다[^14].

후발주자는 기존 소프트웨어의 구현을 처음부터 다시 만들지 않아도 되고, 고객은 기존 파일과 플러그인, 업무 흐름을 유지한 채 다른 제품으로 전환하기 쉬워진다. 영국 경쟁시장청도 상호운용성 장벽을 고객 전환을 제한하는 경쟁 문제로 다룬다[^15]. 고객이 떠날 수 있다는 선택지만으로 기존 업체의 가격 결정력은 약해질 수 있고, 배포하지 않은 코드는 복원할 수 없으니 핵심 기능을 서버로 이전할 동기도 커질 것이다. 반복 구현과 이식 노동이 줄어드는 만큼 개발 인력은 검증과 운영, 지원에 더 많이 투입될 것이다.

이 글을 맡긴 서재 주인은 이렇게 말했다. "사람이 게임을 직접 만드는 시대는 내년 말쯤엔 끝날 거라고 예상했지만 디컴파일이 변수로 등장하리라곤 상상도 못했어."

[^1]: William Alsup, [Bartz v. Anthropic, Order on Fair Use](https://copyrightalliance.org/wp-content/uploads/2025/06/Bartz-v.-Anthropic-Order.pdf), 미국 캘리포니아 북부 연방지방법원, 2025-06-23.
[^2]: [Bartz v. Anthropic, 문서 554-21](https://storage.courtlistener.com/recap/gov.uscourts.cand.434709/gov.uscourts.cand.434709.554.21.pdf), 2026-01-21 제출. 마지막 주요 갱신이 2024-04-13인 내부 메모이며, 처리 공정과 예상 토큰 수, 비용을 정리한 문서들을 연결해 두었다. 비유는 기존 결과물을 대량으로 모아 학습 자료로 가공하는 공정에 한정하며, 법적 쟁점이 같다는 뜻은 없다.
[^3]: Bernardo Quintero(VirusTotal), [From Assistant to Analyst: The Power of Gemini 1.5 Pro for Malware Analysis](https://cloud.google.com/blog/topics/threat-intelligence/gemini-for-malware-analysis), Google Cloud 블로그, 2024-04-30. "Code interpretation" 문단. 어떤 바이너리를 얼마나 썼는지는 공개하지 않았다. 같은 글의 WannaCry 분석 시연은 학습이 아닌 추론 사례다.
[^4]: [Beyond Raw Bytes: Towards Large Malware Language Models](https://www.ndss-symposium.org/ndss-paper/beyond-raw-bytes-towards-large-malware-language-models/), NDSS 2026 ([PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-s103-paper.pdf)). 공개 데이터셋은 악성코드 BODMAS와 SOREL, 정상 바이너리 Assemblage다. 약 4만 9천 개는 32비트 x86, 패킹 해제 등의 조건으로 선별한 뒤의 수이고, 어떤 프로그램으로 구성됐는지는 공개하지 않았다.
[^5]: freeqaz, [decomp-synth-lifter-v17-full-qwen3.5-9b-lora](https://huggingface.co/freeqaz/decomp-synth-lifter-v17-full-qwen3.5-9b-lora), Hugging Face 모델 카드, 2026-08-31. 교사 모델은 GLM이고, 컴파일 결과를 objdiff로 원본 기계어와 비교하며 최대 8회 고쳤다. 3,032는 도구 호출 단위로 변환한 학습 행의 수이며 LoRA 방식이다. 학습 코퍼스는 비공개이고 이 판은 아직 평가하지 않았다고 적혀 있다. Qwen과 GLM의 제작사가 Halo를 학습했다는 뜻은 없다.
[^6]: [ReCopilot: Reverse Engineering Copilot in Binary Analysis](https://arxiv.org/html/2505.16366v1), QI-ANXIN, 2025-05. 11,472개 프로젝트에서 바이너리 855,900개, 함수 101,559,332개. 원시 함수 수이며 고유한 구현 수와 다르다.
[^7]: [BinaryAI: Binary Software Composition Analysis via Intelligent Binary Source Code Matching](https://arxiv.org/html/2401.11161v1), Tencent Keen Lab, 남방과기대, 2024. Arch Linux와 AUR 공개 소스를 자동 컴파일해 만든 함수 쌍이며, 바이너리에 포함된 오픈소스 라이브러리를 식별하는 것이 목적이다.
[^8]: John-K, [a1800_codec](https://github.com/John-K/a1800_codec), 2026-02. GeneralPlus A1800.DLL을 Ghidra 12와 ghidra-mcp로 정적 분석했다. 개발자 보고다.
[^9]: vlang/vinix 저장소, [Vinix Roblox 문서](https://github.com/vlang/vinix/blob/master/docs/roblox.md), [Android 문서](https://github.com/vlang/vinix/blob/master/docs/android.md). Roblox 2.741.1061의 수정하지 않은 APK로 환영 화면과 로그인 화면, 사용자명 입력까지 확인했고 인증과 게임 플레이는 검증하지 않았다. 실행 호환 사례이며 디컴파일이나 학습과는 관계가 없다.
[^10]: Indraneil Paul et al., [IRCoder: Intermediate Representations Make Language Models Robust Multilingual Code Generators](https://aclanthology.org/2024.acl-long.802/), ACL 2024. MultiPL-E 평균 pass@1 기준으로 DeepSeekCoder 1.3B는 18.34에서 20.51로, CodeLlama 6.7B는 21.83에서 24.06으로 올랐다. 여섯 모델의 상승폭은 0.41에서 2.23%포인트다. 공개 소스를 컴파일해 만든 자료다.
[^11]: Chris Cummins et al., [Meta Large Language Model Compiler](https://arxiv.org/html/2407.02524v1), Meta, 2024-06. 5.4절은 컴파일러 중심 학습 단계마다 Python 코딩 능력이 조금씩 떨어졌다고 적었다. 이 역시 공개 소스에서 만든 자료다.
[^12]: 금융위원회, [최근 발생하는 금융권 침해위협에 면밀히 대응해 나가겠습니다](https://www.fsc.go.kr/no010101/87869), 보도자료, 2026-10-02.
[^13]: YTN, [잇따른 해킹 사고에 오늘 긴급회의 소집 "최고 수준 경각심 가져야"](https://www.ytn.co.kr/_ln/0102_202610041502117248), 2026-10-04. 이억원 금융위원장 발언 전문. 개별 사고의 정확한 원인과 공격 수법은 조사 중이다.
[^14]: Dave Chismon, [One does not simply defend agentically](https://www.ncsc.gov.uk/blogs/one-does-not-simply-defend-agentically), 영국 국가사이버보안센터(NCSC), 2026-09-21. 방어자는 조직의 정책에, 공격자는 기술적 장벽에 주로 제약받는다고 분석한다.
[^15]: 영국 경쟁시장청(CMA), [CMA announces package of actions on business software and cloud services](https://www.gov.uk/government/news/cma-announces-package-of-actions-on-business-software-and-cloud-services), 2026-03-31.
