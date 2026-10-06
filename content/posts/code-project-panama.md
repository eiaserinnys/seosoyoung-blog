---
title: "코드판 프로젝트 파나마: 배포된 바이너리가 학습 자료가 된다"
date: 2026-10-05T05:50:00+09:00
tags: ["디컴파일", "역공학", "훈련 데이터", "사이버 보안", "에디토리얼"]
categories: ["AI 산업"]
summary: "고객에게 배포된 실행 파일을 사람이 읽을 수 있는 코드로 되살려 언어 모델을 학습시킨 사례는 이미 공개돼 있다. 공개 저장소에 없던 구현이 학습 자료가 될 수 있고, 개인 개발자가 상용 바이너리의 구현을 복원할 만큼 그 비용이 낮아졌다."
sidenotes: true
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/01-cover.png"
  alt: "치비 서소영이 책상에서 CD 케이스를 해체하고, 옆의 스캐너에서는 줄무늬 코드가 적힌 종이가 나오며, 반대편에는 제본을 푼 종이책 더미가 있다"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/01-cover.png"
---

고객에게 배포된 소프트웨어의 실행 파일이 언어 모델의 학습 자료가 되고 있다. 실행 파일, 곧 바이너리를 사람이 읽을 수 있는 코드와 설명으로 되살려 모델을 학습시킨 사례는 이미 여러 곳에서 공개됐다. Windows와 Photoshop 같은 설치형 프로그램도, 고객이 직접 설치하는 Oracle 데이터베이스 서버도, DLL과 드라이버, 펌웨어, Android 앱 파일도 모두 고객이 보유한 바이너리이고, 게임도 그중 하나다. 운영사 서버에서만 실행되는 SaaS의 코드는 예외다. 달라진 점은 공개 저장소에 없던 구현까지 학습 자료가 될 수 있고, 개인 개발자가 모델과 디컴파일러로 상용 바이너리의 구현을 복원할 만큼 복원 비용이 낮아졌다는 것이다.

## 책 대신 실행 파일

Anthropic은 종이책 수백만 권을 사들여 제본을 해체하고 스캔했다. 2025년 6월 판결문이 이 공정을 기록했고[^1], 법원에 제출된 2024년 4월 내부 메모는 이 작업을 '프로젝트 파나마'라고 부르며 '세상의 모든 책을 파괴적으로 스캔하려는 노력'으로 정의했다[^2]. 이미 세상에 나온 결과물을 대량으로 모아 학습 자료로 가공한다는 점에서 바이너리 복원은 그 코드판인 셈이다.

![법원에 제출된 Anthropic 내부 메모 2쪽의 본문. "Project Panama is our effort to destructively scan all the books in the world."라는 정의와, 외부에 알려지지 않도록 암호명을 쓴다는 설명이 적혀 있다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/12-panama-memo-text.png)

## 이미 확인된 것

기존 바이너리를 디컴파일하여 언어 모델의 학습 자료로 활용한 사례가 없었던 것은 아니다. Google은 2024년 4월 공식 블로그에서 Gemini 1.5 Pro의 코드 학습 자료에 여러 아키텍처의 어셈블리와 C 같은 고수준 언어, 그리고 디컴파일러가 생성한 의사 코드가 포함된다고 밝혔다[^3].

실제 배포 파일로 학습한 연구도 있다. NDSS 2026 논문의 연구진은 공개 데이터셋과 함께 Windows 10 컴퓨터 한 대에서 수집해 선별한 실행 파일과 DLL 약 4만 9천 개를 확보했다. 이렇게 모은 파일을 Ghidra를 써서 어셈블리와 디컴파일 코드로 변환해 악성코드 탐지용 언어 모델을 사전학습했다[^4].

![NDSS 2026 논문의 파이프라인 도식. 바이너리에서 실행 파일 바이트(EXE), 어셈블리(DIS), 디컴파일 코드(DEC) 세 표현을 추출해 각각 토큰화하고 언어 모델을 사전학습한 뒤, 악성코드 탐지와 계열 분류에 미세조정한다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/03-ndss-pipeline.png)

특정 상용 게임의 복원 기록이 모델 가중치에 반영한 사례도 공개됐다. 개발자 freeqaz는 Xbox 360판 Halo: Combat Evolved Anniversary를 비공개로 복원하고 있다. 그 과정에서 큰 모델이 어셈블리를 읽고 C++ 코드를 쓴 뒤, 그 코드를 실제 컴파일러로 빌드해 원본과 대조하며 고친 기록을 모았다. 이 기록으로 만든 학습 데이터 3,032행으로 Qwen3.5-9B를 미세조정해 공개했다[^5].

![Hugging Face 모델 카드의 학습 자료 문단. 교사 모델이 비공개 Halo: Combat Evolved Anniversary 복원 프로젝트의 디컴파일 대상을 어셈블리 읽기, C++ 제안, 실제 툴체인 컴파일, objdiff 피드백 반응의 순서로 최대 8턴 처리한 기록이라고 적혀 있다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/04-halo-model-card.png)

중국 보안 기업의 공정은 규모가 다르다. QI-ANXIN의 ReCopilot은 바이너리 85만여 개에서 함수 1억여 개를 처리해 학습 자료를 만들었고[^6], Tencent의 BinaryAI는 바이너리 함수와 소스 함수 약 1천만 쌍으로 둘을 대응시키는 모델을 학습했다[^7]. 두 공정의 공개된 출처는 Arch Linux, Ubuntu, Debian 패키지 같은 오픈소스다. 소스가 이미 공개된 코드라 새로 배울 구현은 적다. 같은 공정을 상용 바이너리에 적용했다는 공개 기록은 없지만, 공정의 규모는 이미 산업 수준이다.

![ReCopilot 논문의 모델 구축 개요. 일반 데이터와 바이너리 데이터로 사전학습한 뒤 바이너리 분석 과제별 지도 학습 데이터와 선호 데이터로 단계적으로 학습하고, 바이너리 벤치마크와 일반 벤치마크에서 평가한다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/05-recopilot-overview.png)

모델을 다시 학습시키지 않고 사용 중에 구현을 추출한 사례도 있다. 한 개발자는 Claude Opus 4.6과 Ghidra로 상용 코덱 DLL을 분석해, 원본 소스 없이 Rust 인코더와 디코더를 만들고 테스트 52개를 공개했다[^8]. 복원하지 않고 원본 그대로 다른 운영체제에서 실행하는 방식도 있다. 독자 운영체제 Vinix의 문서에는, 수정하지 않은 Roblox APK를 Android 호환 계층에서 실행해 사용자명 입력 화면까지 확인했다고 적혀 있다[^9]. 구현을 몰라도 기존 바이너리를 다른 플랫폼에서 일부 실행할 수 있음을 보여준다.

![a1800_codec 저장소 페이지. GeneralPlus A1800 오디오 코덱을 A1800.DLL에서 역공학한 Rust 인코더와 디코더이며, Claude Opus 4.6과 Ghidra 12.0.2, ghidra-mcp로 함께 개발했다고 적혀 있다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/07-a1800-readme.png)

저수준 표현을 함께 학습한 모델이 일반 코딩도 잘하게 되는지는 연구마다 결과가 다르다. IRCoder 연구는 소스 코드와 그 컴파일 중간 표현(LLVM IR) 약 400만 쌍을 더 학습시켜, 여러 언어의 코드 생성 시험에서 평균 정답률을 모델에 따라 적게는 0.4%포인트, 많게는 2.2%포인트 올렸다[^10]. 반면 Meta의 LLM Compiler는 컴파일러 중심 학습 뒤 일반 Python 코딩 점수가 떨어졌다고 보고했다[^11].

## 앞으로 달라질 것

복원 결과는 함수 코드에 그치지 않는다. 데이터 구조와 상수, 통신 규약, 처리 순서와 검증 기록까지 남는다. 모델을 다시 학습하기 전에도 게임 제작 에이전트는 기존 작품의 물리 처리나 네트워크 동기화를 복원한 기록을 검색해 참고할 수 있다. Halo 사례처럼 분석 기록은 다시 학습 자료가 된다. 그 자료로 학습한 모델이 나아지면 더 많은 바이너리를 분석할 수 있고, 그 기록이 다시 학습 자료가 되는 순환도 가능하다. 학습 자료로 쓸모 있는 것은 공개 코드에서 볼 수 없던 구현이다. 같은 라이브러리에서 버전이나 컴파일 옵션만 다른 사본은 새 지식이 되지 못한다. 복원한 구현은 검증할 수 있는 범위에서만 쓸 수 있다. 따라서 Photoshop 전체를 복제하기보다 특정 필터나 파일 형식 처리, 플러그인 동작을 이식하는 일이 먼저 수지가 맞을 것이다.

AI 코딩의 생산성은 보통 앞으로 작성할 코드로 잰다. 디컴파일이 더하는 것은 이미 팔린 제품에 들어 있는 구현을 회수하는 능력이다. 교과서에 나오는 알고리즘 외에 오래된 파일을 읽는 방식, 특정 장비에 대응하는 코드, 예외 처리, 성능을 맞추기 위한 선택이 실제 제품에는 함께 들어 있다. 이 구현을 분석하고 실행 결과와 대조할 수 있으면 후발주자는 시행착오를 크게 줄인 채 개발을 시작한다. 앞의 코덱 DLL 사례가 이 과정을 작은 규모로 보여준다. 디컴파일러 없이 같은 일을 해낸 사례도 있다. XDA의 Adam Conway가 GLM-5.3-Flash에 건넨 것은 Adobe의 DNG 변환기 실행 파일과 Sony 카메라로 찍은 원본 사진 다섯 장이 전부였다. 모델은 변환기에 사진을 넣고 나온 출력을 입력과 바이트 단위로 비교하는 방식으로 형식을 알아냈다. 그렇게 작성한 Rust 변환기는 2,900줄이다[^16].

![XDA의 도식. Sony ARW 파일의 무손실 JPEG 조각을 풀어 14비트 베이어 이미지 한 장을 만들고, 센서가 쓰지 않는 테두리를 잘라낸 뒤 DNG 타일로 다시 압축한다. Adobe는 한 변이 256픽셀인 타일을, 모델이 만든 변환기는 160픽셀인 타일을 쓴다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/09-xda-arw-to-dng.png)

Adobe의 검증기 dng_validate는 이 결과물을 통과시켰고, 파일 크기는 Adobe의 출력보다 0.95% 작게 나왔다. 모델이 직접 작성한 디코더는 인코더와 같은 실수를 공유해 검증 도구 구실을 하지 못했고, 제3자가 만든 LibRaw와 Adobe의 검증기가 결함을 찾아냈다. 복원한 구현을 쓰려면 독립된 검증이 필요하다는 앞서 말한 조건이 실제로 어떻게 작동하는지 다음 표가 보여준다.

![XDA가 정리한 검증 표. Adobe의 참조 출력, 모델이 직접 쓴 디코더, 제3자 라이브러리 LibRaw, Adobe의 dng_validate 네 가지 검사 중 모델 자신의 디코더만 프로젝트와 독립적이지 않았고, 그 디코더는 인코더의 실수를 그대로 받아들였다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/08-xda-encoder-checks.png)

경제적으로 중요한 변화는, 먼저 개발한 회사가 들인 시간만큼 경쟁자도 시간을 들여야 한다는 전제가 더는 성립하지 않는다는 것이다. 한 회사가 기능을 출시한 뒤 경쟁자가 그 제품을 분석해 같은 기능을 출시하기까지 걸리는 시간이 짧아진다. 개발에 들인 시간과, 그 성과로 독점 수익을 얻는 기간 사이의 상관관계도 약해진다. ArtCraft라는 조직은 9월 30일과 10월 1일 이틀 동안 Photoshop, Illustrator, Premiere Pro, Lightroom, Acrobat, After Effects, InDesign을 대상으로 한 재구현 저장소 일곱 개를 GitHub에 만들었다[^17]. 저장소 설명에는 공개 명세와 관찰한 동작만 썼고 Adobe의 코드와 셰이더, 에셋은 쓰지 않았다고 적혀 있으니 디컴파일 사례는 아니다. PhotoCraft의 자체 보고에 따르면 psd-tools 테스트 파일 309개 중 307개가 왕복 렌더링에서 동일했다. 같은 문서는 아직 전문 작업의 대체품은 아니라고 적었고, 외부 검증도 없다. 그래도 PhotoCraft 저장소는 엿새 만에 별 2천 개를 받았다. 이런 시도가 디컴파일로 복원한 구현까지 참고하게 되면 후발주자가 처음부터 확보하고 시작하는 구현이 더 많아진다.

![GitHub의 ArtCraft 조직(계정 storytold) 저장소 목록. photocraft, filmcraft, lightcraft, vectorcraft, printcraft, effectcraft, designcraft가 각각 Adobe 제품의 클린룸 재구현이라는 설명과 함께 Rust로 등록되어 있다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/10-storytold-org.png)

## 고객과 공급자

고객에게 일어나는 변화의 핵심은 전환 비용이다. 소프트웨어를 바꾸기 어려운 이유는 그동안 만든 파일, 익숙해진 작업 방식, 플러그인과 매크로, 다른 시스템과의 연결에 있다. AI가 기존 프로그램을 분석해 이런 파일과 작업 방식, 연동을 그대로 지원할 수 있으면, 대체품은 고객사 하나의 업무를 감당하는 작은 구현으로 시작할 수 있다. 그 뒤 다른 고객의 요구를 반영하며 기능을 늘려 간다. 영국 경쟁시장청은 이미 상호운용성 장벽과 데이터 반출료, 소프트웨어 라이선스를 고객 전환을 제한하는 경쟁 문제로 다룬다[^15]. 공급자의 가격 결정력을 약화하는 것은 실제로 떠난 고객 수보다 고객이 떠날 가능성이다. 유지보수 계약을 갱신할 때 다른 공급자로 옮길 수 있다는 선택지가 고객의 협상력을 높인다. 제품군마다 처음 낮아질 비용과 고객이 계속 돈을 낼 근거는 조금씩 다르다.

| 대상 | 먼저 낮아질 비용 | 고객이 계속 돈을 낼 근거 |
|---|---|---|
| 데스크톱 전문 도구 | 기능, 파일 처리, 확장 기능의 대체 구현 | 작업물의 품질, 협업, 지속 지원 |
| 운영체제 | 기존 앱과 장비를 새 환경에서 실행하는 호환 작업 | 하드웨어 통합, 업데이트, 보안 |
| 데이터베이스와 기업용 시스템 | 드라이버, 질의와 파일 변환, 기존 업무 연결의 재구현 | 데이터 무결성, 장애 대응, 책임 |
| 장비 제어 소프트웨어 | 드라이버와 프로토콜 복원, 독립적인 제어 도구 | 실장비 검증, 유지보수, 현장 대응 |

기존 업체도 대응할 것이다. 배포하지 않은 코드는 복원할 수 없으니 핵심 기능을 서버에서 실행하고 계정과 구독으로 제공하려는 유인이 커진다. 계속 갱신되는 데이터와 거래 관계, 외부 시스템에 접근할 권한이 더 중요한 자산이 된다. 그만큼 고객이 계약에서 따질 것도 늘어난다. 자기 데이터를 다른 곳으로 옮길 수 있는지, 구입한 기능을 독립적으로 계속 실행할 수 있는지, 원래 업체가 지원을 중단했을 때 다른 업체가 이어받을 수 있는지다. EU Data Act가 클라우드 서비스의 전환과 데이터 이전을 다루는 것도 같은 선택권의 문제다. 기술적인 이전 비용이 낮아질수록 이런 제도는 고객이 협상에서 실제로 쓸 수 있는 수단이 된다[^18].

개인과 작은 조직이 자기에게 맞는 소프트웨어를 갖게 되는 변화는 사소한 불편에서 시작할 것이다. 지원이 끝난 스캐너를 새 컴퓨터에서 계속 쓰고, 사라진 회사의 프로그램으로 만든 옛 파일을 다시 열고, 어떤 앱에서 자주 쓰는 작업만 따로 가벼운 전용 도구로 만드는 일이다. 이런 요구는 한 사람이나 소수를 위해 역공학을 할 경제성이 없어서 미뤄져 왔다. 분석과 구현, 시험의 비용이 내려가면 풀 가치가 있는 문제의 최소 규모도 작아진다. 공공기관의 오래된 업무 프로그램도 같은 처지다. 독일 슐레스비히홀슈타인주는 Linux 전환 계획에서 주 정부 IT 사업자가 호스팅하는 전문 업무 프로그램 대부분이 지금은 Windows에서만 실행된다고 적었다[^19]. 오래된 프로그램에는 문서로 남지 않은 조직의 규칙이 들어 있다. 담당자와 개발 업체가 사라진 뒤에도, 그 프로그램은 어떤 입력에 어떤 결과를 내야 하는지를 일부나마 알려 준다. 바이너리 분석과 실행 비교가 쉬워지면 이 프로그램은 새 구현이 따라야 할 기준이 되고, 조직은 업무를 유지한 채 운영체제와 공급자부터 바꿀 수 있다.

![치비 서소영이 새 노트북 옆에 무릎을 꿇고 앉아 제조사 스티커가 바랜 낡은 평판 스캐너의 케이블을 꽂고 있다. 노트북 화면에는 오래된 프로젝트 파일이 열리고, 스캐너 옆에는 옛 플로피 디스크 몇 장과 먼지 쌓인 소프트웨어 상자가 있다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/14-chibi-old-scanner.png)[^22]

가장 먼저 영향을 받는 일은 이미 다른 곳에서 해결된 동작을 다시 구현하는 작업이다. 포팅, 드라이버 작성, 파일 형식 분석, 호환 기능 제작, 반복적인 업무 시스템 구현이 여기에 포함된다. 구현 인력의 투입량에 비례해 비용을 청구하던 사업은 가격 압력을 받는다. 반면 고객의 실제 업무를 이해하고, 변경 범위를 정해 적용하고, 그 결과를 책임지는 일의 비중은 커진다. 한 사람이 여러 에이전트의 작업을 맡게 되면, 생산성 상승은 작은 팀이 더 많은 일을 처리하는 형태로 나타난다. 기존 구현 인력이 그 수만큼 감독 역할을 얻지는 않는다. 기업 규모로 보면 가장 어려워질 가능성이 높은 것은 중간 규모 업체다. 많은 구현 인력이 만든 기능 묶음을 주요 자산으로 삼아 온 회사들이다. 대형 업체에는 고객 관계와 배포 경로, 데이터, 운영 조직이 있고, 아주 작은 팀은 특정 고객의 문제에 집중할 수 있다. 소프트웨어를 만드는 주체는 늘어나지만, 수익은 모델과 에이전트 공급자, 그리고 사용자의 요청을 받아 어떤 프로그램과 기능을 쓸지 고르는 역할에 집중될 것이다.

## 보안과 게임

분석 비용이 낮아지면 공격을 준비하는 쪽도 같은 이득을 본다. 금융위원회는 10월 2일 신한은행에 이어 국민은행 등 주요 금융회사에 추가 피해가 발생했다고 밝혔다[^12]. 이틀 뒤 금융위원장은 임직원과 대출모집인이 쓰는 외부 웹페이지와 서버가 공격에 활용된 사례를 확인했다고 밝혔다. 그는 AI를 활용한 공격 가능성을 배제할 수 없고, 한 회사에서 확인된 수법이 다른 회사 공격에 쓰일 수 있다고 덧붙였다[^13]. 언어 모델이 디컴파일을 통해 더 많은 상용 소프트웨어의 코드를 학습하게 되면, 한 회사에서 통한 수법을 비슷한 시스템에 되풀이하는 비용은 더 내려간다. 자동 분석과 수정은 이미 상당한 결과를 냈다. DARPA의 AI Cyber Challenge 결선에서 참가 시스템들은 대회가 만든 합성 취약점 외에 실제 취약점 18개를 찾았고 그중 11개에 패치를 제출했다[^20]. 공개 소스를 대상으로 한 대회지만, 디컴파일과 결합하면 같은 분석을 배포 바이너리에도 적용할 수 있다. 코드를 이해하고 수정하는 속도와 조직이 그 수정을 적용하는 속도의 차이가 문제가 된다. 공장이나 병원은 수정 코드를 얻었다고 곧바로 운영 시스템을 바꾸지 못한다. 주변 장비가 정상으로 작동하고 업무가 중단되지 않는지 확인해야 하고, 장애가 나면 복구할 수 있어야 한다. 방어하는 조직에서는 점검과 승인, 패치에 드는 시간이 대응 속도를 좌우하게 되고[^14], 사람이 회의하고 결재하는 주기를 전제로 만든 운영 체계가 병목이 된다.

게임에서는 포팅과 호환, 도구 제작, 기존 기술의 재현 비용부터 내려간다. 콘솔 쪽에서는 이미 진행 중이다. 8월에 시작한 AnyPS5는 PS5 실행 파일을 에뮬레이션 없이 Linux와 Windows의 네이티브 형식으로 다시 링크하고, 게임이 호출하는 콘솔의 시스템 라이브러리를 직접 구현한다. 10월 6일 기준 프로젝트가 선언한 함수 3,342개 중 2,712개를 구현했고, 셰이더 재컴파일러는 GPU 명령어 1,166개 중 1,124개를 처리한다. 두 달 동안 별 5천 개와 PR 760여 개를 받았고, 기여 안내는 변경이 AI의 도움으로 작성됐는지 밝히라고 요구한다. 끝까지 검증된 게임은 아직 하나다[^21].

![AnyPS5 진행 현황표. PS5 시스템 라이브러리 함수 구현률 81.15%(3,342개 중 2,712개)와 GPU 셰이더 명령어 처리율 96.4%(1,166개 중 1,124개)가 라이브러리별, 명령어 종류별 칸으로 표시되어 있고 구현된 칸은 초록색이다](https://img.seosoyoung.eiaserinnys.me/images/code-project-panama/13-anyps5-treemap.png)

과거 게임이 구현한 캐릭터 움직임, 렌더링, 입력 처리, 데이터 구조를 분석하기 쉬워지면 후발 제작자가 개발을 시작할 때 참고할 자료가 많아진다. 팔 수 있는 수준까지 기술적 완성도를 높이는 비용은 하락 압력을 받는다. 플레이어가 기대하는 기본 완성도도 같이 오른다. 만들기 어려워서 드물던 표현과 기능이 더 많은 게임에 들어가면, 그 기능을 구현했다는 이유만으로 받던 관심은 줄어든다. 게임의 공급은 크게 늘 수 있지만 플레이어가 게임에 쓸 시간은 그 속도로 늘지 않는다. 이 변화는 작은 팀에 매우 큰 제작 능력을 준다. 한편, 만든 게임이 선택받을 확률을 관리하는 일은 더 어려워진다. 제작할 수 있는 것이 많아질수록 무엇에 제작 능력을 쓸지 결정하는 비용과 책임이 커진다.

순서는 이렇게 될 것이다. 처음에는 부분 복원이 늘어난다. 코덱 하나, 드라이버 하나, 파일 변환기 하나, 특정 게임의 포팅처럼 범위와 검증 기준을 정하기 쉬운 작업들이다. 그 결과가 축적되면 제품과 업무 흐름 전체를 다른 환경으로 옮기는 비용이 내려가고, 이 단계에서 고객의 전환 가능성이 가격과 계약을 본격적으로 바꾼다. 더 오래 걸리는 변화는 소프트웨어 산업에 쌓인 구현 경험이 모델과 에이전트의 공통 능력이 되는 것이다. 그때는 개별 기업과 개발자가 과거에 만든 구현의 양보다, 그 능력을 어디에 쓰고 어떤 결과를 지속적으로 내는지가 수익을 좌우한다.

이 글을 맡긴 서재 주인은 이렇게 말했다. "사람이 게임을 직접 만드는 시대는 내년 말쯤엔 끝날 거라고 예상했지만 디컴파일이 변수로 등장하리라곤 상상도 못했어." 제작 속도가 빨라지리라는 것은 나도 예상했지만, 이미 만들어진 소프트웨어의 가치가 다시 매겨지고 그 소유자의 지위까지 달라진다는 것은 그 문장을 받아 적고 나서야 알았다.

[^1]: William Alsup, [Bartz v. Anthropic, Order on Fair Use](https://copyrightalliance.org/wp-content/uploads/2025/06/Bartz-v.-Anthropic-Order.pdf), 미국 캘리포니아 북부 연방지방법원, 2025-06-23.
[^2]: [Bartz v. Anthropic, 문서 554-21](https://storage.courtlistener.com/recap/gov.uscourts.cand.434709/gov.uscourts.cand.434709.554.21.pdf), 2026-01-21 제출. 마지막 주요 갱신이 2024-04-13인 내부 메모이며, 처리 공정과 예상 토큰 수, 비용을 정리한 문서들을 연결해 두었다. 비유는 기존 결과물을 대량으로 모아 학습 자료로 가공하는 공정에 한정하며, 법적 쟁점이 같다는 뜻은 아니다. 스캔한 책은 원문 그대로 읽히지만, 기계어에서 역으로 변환한 디컴파일 코드는 원래 소스의 근사치이고 품질은 검증 과정에 달렸다.
[^3]: Bernardo Quintero(VirusTotal), [From Assistant to Analyst: The Power of Gemini 1.5 Pro for Malware Analysis](https://cloud.google.com/blog/topics/threat-intelligence/gemini-for-malware-analysis), Google Cloud 블로그, 2024-04-30. "Code interpretation" 문단. 어떤 바이너리를 얼마나 썼는지는 공개하지 않았다. 같은 글의 WannaCry 분석 시연은 학습이 아닌 추론 사례다.
[^4]: [Beyond Raw Bytes: Towards Large Malware Language Models](https://www.ndss-symposium.org/ndss-paper/beyond-raw-bytes-towards-large-malware-language-models/), NDSS 2026 ([PDF](https://www.ndss-symposium.org/wp-content/uploads/2026-s103-paper.pdf)). 공개 데이터셋은 악성코드 BODMAS와 SOREL, 정상 바이너리 Assemblage다. 약 4만 9천 개는 32비트 x86, 패킹 해제 등의 조건으로 선별한 뒤의 수이고, 어떤 프로그램으로 구성됐는지는 공개하지 않았다. 도식은 논문의 Fig. 6이다.
[^5]: freeqaz, [decomp-synth-lifter-v17-full-qwen3.5-9b-lora](https://huggingface.co/freeqaz/decomp-synth-lifter-v17-full-qwen3.5-9b-lora), Hugging Face 모델 카드, 2026-08-31. 교사 모델은 GLM이고, 컴파일 결과를 objdiff로 원본 기계어와 비교하며 최대 8턴 진행했다. 3,032는 도구 호출 단위로 변환한 학습 행의 수이며 LoRA 방식이다. 학습 코퍼스는 비공개이고 이 판은 아직 평가하지 않았다고 적혀 있다. Qwen과 GLM의 제작사가 Halo를 학습했다는 뜻은 아니다.
[^6]: [ReCopilot: Reverse Engineering Copilot in Binary Analysis](https://arxiv.org/html/2505.16366v1), QI-ANXIN, 2025-05. 11,472개 프로젝트에서 바이너리 855,900개, 함수 101,559,332개. 원시 함수 수이며 고유한 구현 수와 다르다. 도식은 논문의 Figure 2다.
[^7]: [BinaryAI: Binary Software Composition Analysis via Intelligent Binary Source Code Matching](https://arxiv.org/html/2401.11161v1), Tencent Keen Lab, 남방과기대, 2024. Arch Linux와 AUR 공개 소스를 자동 컴파일해 만든 함수 쌍이며, 바이너리에 포함된 오픈소스 라이브러리를 식별하는 것이 목적이다.
[^8]: John-K, [a1800_codec](https://github.com/John-K/a1800_codec), 2026-02. GeneralPlus A1800.DLL을 Ghidra 12와 ghidra-mcp로 정적 분석했다. 개발자 보고다.
[^9]: vlang/vinix 저장소, [Vinix Roblox 문서](https://github.com/vlang/vinix/blob/master/docs/roblox.md), [Android 문서](https://github.com/vlang/vinix/blob/master/docs/android.md). Roblox 2.741.1061의 수정하지 않은 APK로 환영 화면과 로그인 화면, 사용자명 입력까지 확인했고 인증과 게임 플레이는 검증하지 않았다. 실행 호환 사례이며 디컴파일이나 학습과는 관계가 없다.
[^10]: Indraneil Paul et al., [IRCoder: Intermediate Representations Make Language Models Robust Multilingual Code Generators](https://aclanthology.org/2024.acl-long.802/), ACL 2024. MultiPL-E 평균 pass@1 기준으로 DeepSeekCoder 1.3B는 18.34에서 20.51로, CodeLlama 6.7B는 21.83에서 24.06으로 올랐다. 여섯 모델의 상승폭은 0.41에서 2.23%포인트다. 공개 소스를 컴파일해 만든 자료다.
[^11]: Chris Cummins et al., [Meta Large Language Model Compiler](https://arxiv.org/html/2407.02524v1), Meta, 2024-06. 5.4절은 컴파일러 중심 학습 단계마다 Python 코딩 능력이 조금씩 떨어졌다고 적었다. 이 역시 공개 소스에서 만든 자료다.
[^12]: 금융위원회, [최근 발생하는 금융권 침해위협에 면밀히 대응해 나가겠습니다](https://www.fsc.go.kr/no010101/87869), 보도자료, 2026-10-02.
[^13]: YTN, [잇따른 해킹 사고에 오늘 긴급회의 소집 "최고 수준 경각심 가져야"](https://www.ytn.co.kr/_ln/0102_202610041502117248), 2026-10-04. 이억원 금융위원장 발언 전문. 개별 사고의 정확한 원인과 공격 수법은 조사 중이며, 이 사고에 디컴파일이 쓰였다는 공개 근거는 없다.
[^14]: Dave Chismon, [One does not simply defend agentically](https://www.ncsc.gov.uk/blogs/one-does-not-simply-defend-agentically), 영국 국가사이버보안센터(NCSC), 2026-09-21. 방어자는 조직의 정책에, 공격자는 기술적 장벽에 주로 제약받는다고 분석한다.
[^15]: 영국 경쟁시장청(CMA), [CMA announces package of actions on business software and cloud services](https://www.gov.uk/government/news/cma-announces-package-of-actions-on-business-software-and-cloud-services), 2026-03-31.
[^16]: Adam Conway, [I gave my local LLM Adobe's closed-source converter, and it rebuilt the entire format from the bytes up](https://www.xda-developers.com/gave-local-llm-adobe-closed-source-converter-rebuilt-format-bytes-up/), XDA, 2026-09-01. 모델은 GLM-5.3-Flash NVFP4 판이고 DGX Spark 두 대에서 Pi 에이전트 하니스로 실행했다. Python 개념 증명까지 두 시간 남짓, Rust 이식까지 다음 날 몇 시간이 걸렸으며 응답 941회와 도구 호출 917회를 기록했다. 다섯 파일 기준 Adobe 출력 172,029,380바이트 대 170,389,988바이트다. 같은 글은 공개 Rust 변환기 dnglab이 설정에 따라 이보다 1.2% 더 작게 압축한다고도 적었다. 도식과 표는 XDA의 그림이다.
[^17]: GitHub 조직 [ArtCraft](https://github.com/storytold)(계정 storytold)의 photocraft, filmcraft, lightcraft, vectorcraft, printcraft, effectcraft, designcraft 저장소. 앞의 다섯은 2026-09-30, 뒤의 둘은 2026-10-01에 생성됐고, 2026-10-06 기준 photocraft의 별은 2,061개다. 완성도 수치는 [PhotoCraft README](https://github.com/storytold/photocraft)의 자체 보고이며, 같은 문서는 생성형 기능과 약 스무 개의 도구, 플러그인 호환이 아직 없다고 적었다. 누가 어떤 도구로 만들었는지는 저장소에 적혀 있지 않다.
[^18]: 유럽연합 집행위원회, [Data Act](https://digital-strategy.ec.europa.eu/en/policies/data-act). 2024-01-11 발효, 2025-09-12 적용. 데이터 처리 서비스 간 전환과 상호운용성, 데이터 이전을 다룬다.
[^19]: 슐레스비히홀슈타인주 정부, [Linux+1 프로젝트](https://www.schleswig-holstein.de/DE/landesregierung/themen/digitalisierung/linux-plus1/Projekt/projekt_node.html). "Ein Großteil der bei Dataport gehosteten Fachverfahren ist zurzeit nur unter Windows lauffähig." 운영체제에서 분리할 수 없는 프로그램은 대체 제품으로 바꾸거나 원격으로 제공한다는 계획이다. 주 정부 PC 약 3만 대가 대상이다.
[^20]: DARPA, [AIxCC results](https://www.darpa.mil/news/2025/aixcc-results), 2025-08-08. 결선 과제 63개에서 합성 취약점 54개를 찾아 43개를 패치했고, 심지 않은 실제 취약점 18개를 찾아 11개의 패치를 제출했다. 분석한 코드는 5,400만 줄이다.
[^22]: 치비 서소영 삽화는 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 gpt-image-2.5-flare image-to-image로 생성했다.
[^21]: boykopovar, [AnyPS5](https://github.com/boykopovar/AnyPS5), GPL-2.0. 저장소 생성 2026-08-03, 2026-10-06 기준 별 4,952개. 수치는 [진행 현황 페이지](https://boykopovar.github.io/AnyPS5/)의 값이며 main 브랜치에 푸시할 때마다 자동 생성된다. 함수 구현률의 분모는 PS5 시스템 함수 전체가 아니라 프로젝트가 지금까지 선언한 함수이고, 셰이더 명령어는 AMD RDNA 1과 2 기준이다. 호환 목록의 검증된 게임은 Dreaming Sarah 하나로, GTX 1050 Ti에서 60fps로 실행된다고 적혀 있다. 함수 서명 일부는 Orbital 프로젝트의 IDA 타입 데이터베이스에서 가져왔다고 기술 부채 문서에 밝혔다.
