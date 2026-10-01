---
title: "NationalSecurityAgency/ghidra: Ghidra is a software reverse engineering (SRE) framework"
date: 2026-10-02T03:00:00+09:00
tags: ["Ghidra", "리버스 엔지니어링", "오픈소스", "사이버 보안", "취약점 발견"]
categories: ["에이전트와 코딩"]
summary: "Ghidra는 NSA 연구국이 만들어 2019년에 공개한 소프트웨어 리버스 엔지니어링 프레임워크다. 현재 배포판은 12.1.4이고, 개발 중인 12.2는 모든 클라이언트와 서버 사이의 연결에 TLS 서버 인증을 강제한다. 2019년부터 2025년까지 7년 동안 4건이던 보안 권고가 2026년에는 한 해에만 29건 공개됐고, 그중 7건의 본문은 Claude나 LLM, AI 기반 취약점 탐지 시스템을 언급한다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/ghidra-nsa-reverse-engineering-framework/ghidra-logo-cover.png"
  alt: "Ghidra 로고. 붉은 용 한 마리가 몸을 꼬아 무한대 기호 모양을 만들고, 꼬리 쪽 몸통이 사각형 픽셀로 흩어지며 0과 1로 이루어진 숫자열이 되어 용의 입으로 이어진다. 아래에는 이진수 무늬가 들어간 주황색 글자로 GHIDRA라고 적혀 있다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/ghidra-nsa-reverse-engineering-framework/ghidra-logo-cover.png"
---

## 3줄 요약

1. Ghidra는 미국 국가안보국(NSA) 연구국이 만들고 관리하는 소프트웨어 리버스 엔지니어링 프레임워크다. 컴파일된 프로그램을 디스어셈블하고 디컴파일하는 도구 모음으로, 디버깅과 에뮬레이션, 그래프, 스크립팅 기능을 갖췄다. NSA는 2019년 3월 RSA 콘퍼런스에서 Ghidra를 무료로 공개했고, 이 저장소는 Apache 2.0 라이선스로 소스 코드를 배포한다.
2. 현재 배포판은 2026년 9월 21일에 나온 12.1.4다. 12.0부터 기본 파이썬 엔진이 Jython에서 PyGhidra로 바뀌었고, 12.1의 디컴파일러는 구조체의 비트필드를 이름으로 복원한다. 개발 중인 12.2부터는 실행에 JDK 25 이상이 필요하고, 모든 클라이언트와 서버 사이의 연결에서 TLS 서버 인증이 강제된다.
3. 2019년부터 2025년까지 이 저장소에 공개된 보안 권고는 4건이었다. 2026년에는 10월 2일까지 29건이 공개됐고, 그중 7건의 본문은 Claude나 LLM, AI 기반 취약점 탐지 시스템을 언급한다. 같은 해 새로 제출된 풀 리퀘스트는 1월 13건에서 9월 66건으로 늘었다. 9월에 고친 기여 지침에는 "요청받지 않은 풀 리퀘스트는 처음에 낮은 우선순위를 받을 가능성이 크다"는 문장이 추가됐다.

## 저장소가 소개하는 Ghidra

README에 따르면 Ghidra는 NSA 연구국이 만들고 유지보수하는 소프트웨어 리버스 엔지니어링(SRE) 프레임워크다. 소스 코드 없이 컴파일된 프로그램만 있을 때 그 프로그램을 분석하는 도구 모음이며, 윈도우와 macOS, 리눅스에서 실행된다. README는 디스어셈블, 어셈블, 디컴파일, 그래프, 스크립팅을 비롯해 수백 가지 기능이 있다고 소개했고, 배포판의 릴리스 노트는 여기에 디버깅과 에뮬레이션을 더했다. Ghidra는 여러 프로세서의 명령어 집합과 실행 파일 형식을 지원한다. 대화형 모드와 자동화 모드를 모두 제공하는데, 대화형 모드는 분석가가 화면을 보며 조작하고 자동화 모드(헤드리스)는 화면 없이 명령줄에서 실행한다.

사용자는 자바나 파이썬으로 스크립트와 확장 기능을 직접 만들 수 있다. 새 프로세서, 로더와 익스포터, 자동 분석기, 시각화 기능도 확장으로 추가할 수 있다고 릴리스 노트는 안내한다.

![Ghidra의 Listing 창과 Decompile 창. 왼쪽 Listing 창에는 WinHelloCPP.exe의 함수 FUN_00401040이 주소, 기계어 바이트, MOV와 PUSH 같은 x86 명령어로 표시되어 있다. 오른쪽 Decompile 창에는 같은 함수가 C 코드로 복원되어 있다. 복원된 함수는 CreateWindowExA로 창을 만들고, 창 핸들이 0이면 0을 반환하며, 그렇지 않으면 ShowWindow와 UpdateWindow를 호출한 뒤 1을 반환한다.](https://img.seosoyoung.eiaserinnys.me/images/ghidra-nsa-reverse-engineering-framework/decompiler-window.png)

Ghidra 도움말에 실린 디컴파일러 화면이다. 왼쪽 창은 기계어를 어셈블리로 해석한 목록이고, 오른쪽 창은 디컴파일러가 같은 함수를 C 코드로 바꾼 결과다. (출처: Ghidra 저장소의 도움말 이미지 DecompWindow.png, Apache 2.0)

NSA가 Ghidra를 만든 목적은 복잡한 리버스 엔지니어링 작업에서 생기는 규모 문제와 협업 문제를 해결하는 것이었다고 README는 소개한다. 사용자가 고쳐 쓰고 확장할 수 있는 연구 플랫폼을 제공하는 것도 목표였다. NSA는 악성 코드를 분석할 때, 그리고 네트워크와 시스템의 잠재적 취약점을 파악하려는 분석가를 도울 때 Ghidra를 써 왔다고 한다. README에는 채용 안내도 한 줄 있다. 이런 프로젝트에 관심 있는 미국 시민이라면 NSA에 지원해 보라는 내용이다.

## 공개되기까지

Ghidra라는 이름이 외부에 처음 알려진 계기는 2017년 3월 위키리크스가 공개한 CIA 문서 「Vault 7」이었다. 이 문서는 Ghidra를 NSA 연구국이 만든 리버스 엔지니어링 도구로 언급했다. TechTarget은 NSA가 2000년대 초에 Ghidra를 개발했다고 보도했다. CyberScoop에 따르면 Ghidra는 처음에 기밀 도구였고, 이후에는 군 분석가와 계약업체도 민감하지만 기밀은 아닌 업무에 Ghidra를 쓰게 됐다.

2019년 3월 5일, NSA 선임 고문이던 Rob Joyce가 샌프란시스코 RSA 콘퍼런스에서 Ghidra 9.0을 공개했다. 윈도우, macOS, 리눅스용 배포판은 전용 웹사이트에서 받을 수 있었다. Joyce는 Ghidra에 백도어가 없다고 강조하며 이렇게 말했다.

> 이 커뮤니티는 백도어를 심은 채로 무언가를 내놓기에 가장 나쁜 상대다. 그런 것을 찾아내 뜯어보는 사람들이기 때문이다.

GitHub 저장소는 발표 나흘 전인 2019년 3월 1일에 만들어졌다. 처음에는 README와 법률 문서만 있었고, 9.0.2 버전의 전체 소스 코드는 4월 4일에 공개됐다.[^source]

## 저장소의 규모와 구성

10월 2일 기준으로 기본 브랜치 master에는 커밋 1만 8,622개가 있고, 기여자로 집계된 사람은 456명이다.[^api] 별은 8만 184개, 포크는 8,933개다. 해결되지 않은 이슈는 1,559개, 아직 처리되지 않은 풀 리퀘스트는 405개다. GitHub가 집계한 언어 비율은 자바 86.0%, C++ 6.0%, HTML 4.1%, C 1.5%, 파이썬 1.4% 순이다. 디컴파일러는 C++로 작성된 네이티브 프로그램이다. 릴리스 노트에 따르면 배포판에 포함된 네이티브 구성 요소는 적어도 한 플랫폼용으로 미리 빌드되어 있다.

코드의 대부분은 `Ghidra/` 디렉터리에 있다.

| 디렉터리 | 모듈 수 | 주요 모듈 |
|---|---|---|
| `Ghidra/Framework` | 12 | 데이터베이스(DB), GUI와 도킹 창, 프로젝트, 파일 시스템, 에뮬레이션, 소프트웨어 모델링 |
| `Ghidra/Features` | 36 | Base, Decompiler, BSim, PDB, PyGhidra, GhidraServer, VersionTracking, Objective-C, Swift, Rust, 마이크로소프트와 GNU 디맹글러 |
| `Ghidra/Debug` | 16 | 디버거 본체, gdb, lldb, WinDbg 엔진(dbgeng), x64dbg, drgn, 자바 디버거(JPDA)와 연결하는 에이전트, 실행 추적 모델 |
| `Ghidra/Processors` | 39 | x86, ARM, AARCH64, MIPS, PowerPC, RISCV, Sparc, 6502, Z80, 8051, JVM, Dalvik, eBPF, Hexagon 등 |
| `Ghidra/Extensions` | 9 | Jython, MachineLearning, SymbolicSummaryZ3, SleighDevTools, BSimElasticPlugin 등 |

`Ghidra/Processors`의 39개에는 데이터 전용 모듈(DATA)과 테스트용 가상 프로세서(Toy)도 포함되어 있다. 각 프로세서 모듈에는 SLEIGH라는 명세 언어로 작성한 명령어 정의가 있다. Ghidra는 기계어를 이 정의에 따라 p-code라는 중간 표현으로 변환한 뒤, p-code를 대상으로 분석과 디컴파일을 수행한다. 그 외에 GPL 라이선스 구성 요소(GNU 디맹글러, GNU 디스어셈블러 등)는 별도의 `GPL/` 디렉터리에 있고, `GhidraBuild/`에는 빌드 스크립트와 이클립스 플러그인, IDA Pro용 내보내기 플러그인이 있다.

master의 README 기준으로 소스에서 빌드하려면 JDK 25, Gradle 9.1.0 이상, 파이썬 3.9부터 3.14까지의 버전이 필요하다. 리눅스와 macOS에서는 GCC나 Clang과 make가, 윈도우에서는 Visual Studio 2017 이상이나 마이크로소프트 C++ 빌드 도구가 추가로 필요하다. `gradle -I gradle/support/fetchDependencies.gradle`로 의존성을 내려받고 `gradle buildGhidra`를 실행하면 `build/dist/`에 압축 파일 형태의 개발 빌드가 만들어진다. README는 Ghidra 자체를 개발할 때 이클립스 사용을 강하게 권한다. 스크립트와 확장 기능은 이클립스용 GhidraDev 플러그인이나 Visual Studio Code로 작성할 수 있다. 정식 배포판은 릴리스 페이지에 ZIP 파일 하나로 제공되며, 12.1.4의 압축 파일은 약 570MB다.

## 12.x 릴리스

12.0은 2025년 12월에 나왔다. 그 뒤로 2026년 9월까지 패치 버전과 12.1이 이어졌다.

| 버전 | 공개일 | 내려받기 |
|---|---|---|
| 12.0 | 2025년 12월 8일 | 12만 5,177회 |
| 12.0.1 | 2026년 1월 15일 | 5만 560회 |
| 12.0.2 | 2026년 1월 30일 | 3만 8,106회 |
| 12.0.3 | 2026년 2월 11일 | 6만 8,855회 |
| 12.0.4 | 2026년 3월 4일 | 24만 194회 |
| 12.1 | 2026년 5월 13일 | 11만 1,269회 |
| 12.1.2 | 2026년 6월 5일 | 41만 5,165회 |
| 12.1.3 | 2026년 8월 18일 | 25만 4,654회 |
| 12.1.4 | 2026년 9월 21일 | 8만 3,179회 |

12.1.1은 태그로만 남아 있고 릴리스 페이지에는 없다.[^1211]

12.0의 주요 변경 사항은 다음과 같다.

- 같은 프로젝트의 폴더와 파일을 가리키는 내부 링크를 만들 수 있게 됐다. 링크 파일에는 데이터베이스 대신 간단한 속성 파일을 쓰는 새 저장 형식을 도입했고, 이 때문에 이전 버전의 Ghidra와 Ghidra Server에서는 일부 호환 문제가 생길 수 있다.
- 프로그램과 라이브러리를 가져올 때 로컬 파일 시스템의 심볼릭 링크 구조를 그대로 재현하는 옵션이 생겼다. 헤드리스 모드에서는 `-mirror`로 지정한다.
- PyGhidra 3.0.0이 나왔고, 기본 파이썬 스크립트 엔진이 Jython에서 PyGhidra로 바뀌었다. 기존 Jython 스크립트를 계속 쓰려면 `# @runtime Jython` 헤더를 넣어야 한다.
- 실험 기능으로 Z3 기반 기호 에뮬레이터를 추가했다. 이 에뮬레이터는 구체적인 값으로 실행하는 기존 에뮬레이터의 보조 도메인으로 동작한다. 실행 경로는 구체적인 값으로 실행할 때의 경로를 그대로 따르고, 그 과정에서 Z3 수식과 분기 조건을 만든다. 흔히 콘콜릭(concolic) 에뮬레이터라고 부르는 방식이다.
- 에뮬레이션 API의 확장 방식을 상속에서 조합과 콜백으로 바꿨다. 릴리스 노트는 JIT로 가속한 에뮬레이터를 GUI에 통합하기 위한 준비라고 설명했다.
- 메모리의 데이터 항목끼리 서로 참조하는 관계를 보여 주는 데이터 그래프가 추가됐다.

12.1에서 바뀐 것은 다음과 같다.

- 디컴파일러가 구조체의 비트필드 이름을 복원해, 비트를 분리하는 저수준 연산 대신 필드 이름으로 읽기와 쓰기를 보여 준다.
- Objective-C 분석기를 새로 만들었다. 가능한 경우 `_objc_msgSend()` 호출을 실제로 실행될 메서드로 바꿔 표시하고, AARCH64에서 자동 참조 카운팅(ARC)이 만드는 잡음 코드의 상당 부분을 디컴파일 결과에서 숨긴다.
- HTTP(S) debuginfod 서버에서 DWARF 디버그 파일을 내려받을 수 있게 됐다.
- 퀄컴 Hexagon 프로세서 모듈이 추가됐다. 이 모듈은 명령어를 병렬로 실행하는 Hexagon의 p-code를 만들려고 SLEIGH의 crossbuild 기능을 처음 사용했다.
- Jython 지원은 기본 포함에서 빠지고 확장으로 바뀌어, 쓰려면 따로 설치해야 한다.
- Ghidra 12.1을 실행하려면 JDK 21 이상이 필요하다.
- 보안 수정도 있었다. Ghidra Server의 RMI 직렬화 필터를 강화하고 같은 필터를 클라이언트에도 추가했으며, PKI 인증 모드에서 다른 사용자로 인증되던 논리 오류를 고쳤다.

9월의 12.1.4는 Swift 디맹글러 분석기가 알려진 위치에서 디맹글러를 찾지 못하면 환경 변수 `GHIDRA_SWIFT_DEMANGLER`로 경로를 지정하게 바꿨다. 실행 파일이 UNC 경로로 지정한 라이브러리는 불러오지 않도록 했고, PE와 OMF 로더의 스택 오버플로를 고쳤으며, V79 명령어까지 다루도록 Hexagon 모듈을 대폭 수정했다.

master에는 아직 출시되지 않은 12.2의 변경 사항이 정리되어 있다.

- 모든 클라이언트와 서버 사이의 SSL/TLS 연결에서 서버 인증을 강제한다. localhost로 접속하는 경우도 마찬가지이며, 테스트 용도에 한해 설정 속성으로 끌 수 있다. 키 저장소를 지정하지 않은 Ghidra Server는 임시 자체 서명 인증서를 만들고, 그때는 localhost 접속만 받는다.
- 클라이언트에 서버 허용 목록을 도입해, 알려지지 않은 서버로 Ghidra URL을 연결하는 동작과 주석 속 URL 링크를 클릭하는 동작을 제한한다.
- BSim PostgreSQL 서버 관리 스크립트 `bsim_ctl`을 크게 고쳤고, 기본 인증 방식을 trust에서 password로 바꿨다.
- 실행에 JDK 25 이상이 필요하다. 스크립트와 확장 개발자는 외부 함수와 메모리 API(Foreign Function & Memory API), 스트림 개더러 같은 새 언어 기능을 쓸 수 있다.
- C99 정수형(`int8_t`, `uintptr_t` 등)을 내장 데이터 타입으로 지원한다.
- 같은 데이터 타입을 따로 복원해 구조체나 공용체, 열거형이 둘 생겼을 때 쓰는 대화형 병합 도구를 추가했다. 두 결과를 한 화면에서 비교하고, 항목을 골라 하나로 합칠 수 있다.
- 시간 여행 디버깅을 베타로 지원한다. Intel PIN 기반 도구로 실행 추적을 TENET 형식으로 기록해 디버거로 가져오면, 중단점 적중 타임라인과 동적 호출 트리, 변수 뷰어로 분석할 수 있다.
- 프로그램 데이터베이스 접근에 읽기와 쓰기 잠금을 추가했고, 메모리 사용량을 줄이려고 자바의 Compact Object Headers를 켜고 실행한다.

## 2026년의 보안 권고

이 저장소는 GitHub 보안 권고(Security Advisories)로 취약점을 공개한다. 2019년부터 2025년까지 공개된 권고는 4건이었다. 2021년에는 Log4j 취약점(CVE-2021-44228)이, 2023년에는 Jython의 신뢰할 수 없는 검색 경로(CVE-2019-17664)와 `launch.sh`의 명령 주입(CVE-2023-22671)이, 2024년에는 SLEIGH 백엔드의 해제 후 사용 취약점이 공개됐다. 2026년에는 2월부터 10월 2일까지 29건이 공개됐고, 심각도는 높음 등급이 12건, 중간 등급이 17건이다. 권고에 기재된 발견자와 보고자 계정은 18개다.

![두 개의 막대 차트. 왼쪽 차트는 연도별로 공개된 Ghidra 보안 권고 수로, 2019년 0건, 2020년 0건, 2021년 1건, 2022년 0건, 2023년 2건, 2024년 1건, 2025년 0건, 2026년 29건이다. 오른쪽 차트는 2026년에 월별로 새로 제출된 풀 리퀘스트 수로, 1월 13건, 2월 26건, 3월 35건, 4월 18건, 5월 34건, 6월 32건, 7월 41건, 8월 51건, 9월 66건이다.](https://img.seosoyoung.eiaserinnys.me/images/ghidra-nsa-reverse-engineering-framework/advisories-and-prs.png)

차트는 GitHub API로 10월 2일에 조회한 값을 바탕으로 내가 만들었다.[^pr]

29건 대부분이 같은 공격 시나리오를 가정한다. 공격자가 조작한 바이너리나 프로젝트 파일을 분석가가 Ghidra로 여는 상황이다. 높음 등급 가운데 몇 건을 소개하면 다음과 같다.

| 권고 | 수정 버전 | 내용 |
|---|---|---|
| GHSA-mc3p-mq2p-xw6v | 12.0.3 | Mach-O 파일의 CFString에서 자동으로 만든 주석에도 `{@execute ...}` 주석 문법이 해석됐다. 분석가가 그 주석을 클릭하면 확인 창 없이 임의의 명령이 실행됐다. |
| GHSA-fgg5-g275-7742 | 12.1 | 클라이언트가 Ghidra Server의 RMI 응답을 직렬화 필터 없이 역직렬화했다. 프로젝트 상태 파일에 저장소 URL을 적어 두면 프로젝트를 열기만 해도 접속이 시작됐고, 명령을 실행하는 역직렬화 가젯은 기본 클래스패스의 Jython JAR에 있는 클래스만으로 구성할 수 있었다. |
| GHSA-r625-mph7-wf6j | 12.1.1 | 프로젝트의 도구 설정 XML에 적힌 클래스 이름을 검사 없이 `Class.forName()`으로 불러와 생성자를 실행했다. |
| GHSA-5c38-3rf3-gp75 | 12.1 | 윈도우에서 URL 주석을 클릭하면 `cmd.exe /c start <URL>`로 브라우저를 실행하는데, URL 속 `&` 같은 cmd 특수 문자가 이스케이프되지 않아 명령이 주입됐다. |
| GHSA-5wxq-7qpv-65p2 | 12.1 | Ghidra Server의 PKI 인증에서 빈 서명으로 신원 확인을 통과할 수 있었다. |
| GHSA-vv7r-2rhf-5h7g, GHSA-8r4f-65cr-fwxm | 12.1 | BSim의 비밀번호 변경과 검색 필터에 SQL 주입 취약점이 있었다. |

중간 등급에는 서비스 거부 취약점이 많다. 48바이트짜리 dyld 공유 캐시 파일 하나로 JVM 힙이 소진됐다. 조작한 PEF 파일을 열면 로더가 무한 루프에 걸려, 사용자가 프로세스를 강제로 종료할 때까지 CPU 사용률이 100%로 유지됐다. 여러 권고는 헤드리스 Ghidra로 악성 코드를 자동 분류하는 파이프라인을 피해 대상으로 꼽으면서, 악성 파일 하나로 처리 대기열 전체가 멈출 수 있다고 경고했다.

C++로 작성된 디컴파일러와 SLEIGH 코드의 메모리 오류도 네 건 공개됐다. 네 건 가운데 둘은 변수 병합 함수 `HighVariable::merge()`의 해제 후 사용과, 점프 테이블 복원 중 `TypeFactory::getBase()`의 힙 버퍼 오버플로다. 나머지 둘은 128비트 나눗셈 단순화 함수 `udiv128`의 스택 배열 범위 밖 쓰기와, SLEIGH의 `SleighBuilder::generatePointerAdd`에서 생긴 해제 후 사용이다.

29건 가운데 7건은 본문에서 AI 도구를 언급한다.[^why]

| 권고 | 공개일 | 내용 | 본문에 적힌 AI 관련 내용 |
|---|---|---|---|
| GHSA-m94m-fqr3-x442 | 2월 11일 | GNU 디맹글러가 Rust 심볼을 처리하다 메모리를 소진하는 문제 | FuzzingBrain 팀과 이 팀의 AI 기반 취약점 탐지 시스템이 발견하고 보고했다 |
| GHSA-mc3p-mq2p-xw6v | 2월 19일 | `@execute` 주석으로 임의 코드 실행 | Mobasi AI Security 팀의 Sentinel 프로그램이 발견하고 보고했다 |
| GHSA-gqh9-2c72-wpjc | 5월 14일 | SLEIGH의 해제 후 사용 | DARPA의 AI 사이버 챌린지(AIxCC)에서 Trail of Bits가 만든 Buttercup의 후속 연구 중에 발견했다. Buttercup은 정적 분석, 퍼징, 대규모 언어 모델을 결합해 취약점을 찾고 고치는 시스템이다 |
| GHSA-8jqp-qv73-395r | 5월 15일 | 디컴파일러 `HighVariable::merge()`의 해제 후 사용 | libFuzzer와 AddressSanitizer로 ARM64 기계어를 퍼징해 발견했고, 사람이 헤드리스 분석으로 재현을 확인했다. 근본 원인 분석은 LLM(Claude)이 소스 코드와 ASan 기록을 읽고 작성했으며, 사람이 검증하지 않아 부정확할 수 있다고 적었다 |
| GHSA-p4ff-f27r-j8q7 | 8월 19일 | 점프 테이블 복원 중 힙 버퍼 오버플로 | 근본 원인 항목의 제목에 "LLM이 생성했으며 부정확할 수 있음"이라고 적었다 |
| GHSA-2697-fm9m-mqvw | 8월 19일 | PEF 로더의 무한 루프 | 소스 감사, 개념 증명 파일 제작, 테스트 실행에 Claude Opus를 썼다고 밝혔다. 모든 발견은 12.1.2 정식 배포판에서 실행해 검증했다고 한다 |
| GHSA-42gp-j98c-2297 | 8월 19일 | APK 프로젝트 내보내기의 경로 조작으로 임의 파일 쓰기 | 요약 문서를 작성하는 데 AI를 썼다고 밝혔다 |

이런 문장이 공개된 권고에 그대로 남아 있는 이유 하나는 Ghidra 팀의 공개 방침이다. 2026년 6월 1일 저장소에 추가된 `SECURITY.md`에 따르면, Ghidra 팀은 가능한 한 보고자가 작성한 원래 권고를 그대로 공개한다. 형식을 고치거나 부정확한 내용을 삭제하거나 정보를 추가할 권리는 팀에 있다. 보고는 GitHub의 비공개 취약점 신고 기능으로 받고, 패치가 포함된 정식 배포판이 나온 뒤 사용자가 업데이트할 시간을 고려해 공개한다. 같은 문서는 Ghidra 팀이 보안 권고로 CVE를 발급할 권한이 없다고 밝혔다. CVE가 필요하면 보고자가 직접 발급받아 팀에 알려야 하며, 실제로 2026년의 29건 가운데 CVE 번호를 받은 권고는 4건이다. 한편 12.2에서 고친 Debugger ISF 서버의 경로 조작 취약점(GHSA-8pr2-46mf-v2r2)은 12.2가 나오기 전인 5월에 이미 공개됐다.

## 기여 지침과 풀 리퀘스트

2026년 1월부터 9월까지 새로 제출된 풀 리퀘스트는 316건이다. 같은 기간 2025년에는 124건, 2024년에는 200건이었다. 2026년의 월별 건수는 1월 13건에서 9월 66건으로 늘었다. 반면 새 이슈는 2025년 같은 기간의 531건에서 454건으로 줄었다.

`CONTRIBUTING.md`는 9월에 세 번 수정됐다. 9월 18일 수정본에는 다음 내용이 추가됐다.

> 구현을 시작하기 전에 먼저 Ghidra 팀과 대화해 보는 것을 고려해 달라. (중략) 요청받지 않은 풀 리퀘스트는 우리에게 밀린 작업이 엄청나게 많아서 처음에는 낮은 우선순위를 받을 가능성이 크다.

> 실제로 쓰고 테스트하다 발견한 버그를 고치는 일과, Ghidra 기능에 필요하다는 점이 분명한 개선에 집중해 달라.

AI에 관한 문장은 이 개정 전부터 지침에 있었다. 지침은 개발에 AI의 도움을 받았다면 AI가 내놓은 제안을 더 엄격하게 검토해 달라고 요청한다. 검토할 항목은 제안의 정확성, 그리고 법적 요건의 준수다. 여기서 말하는 법적 요건은 지침의 Legal 항목에 적혀 있다. Legal 항목의 내용은 이렇다. 기여물은 저장소와 같은 Apache 2.0 조건으로 제공되고, 기여자는 그 기여와 관련해 미국 정부에 향후 대가를 청구할 권리를 명시적으로 포기한다.

## 가장 흥미로운 지점

Ghidra로 분석하는 파일은 대개 Ghidra 사용자가 직접 만든 파일이 아니다. 리버스 엔지니어링 도구는 정의상 출처를 믿을 수 없는 파일을 여는 프로그램이고, 분석가가 Ghidra로 여는 파일의 상당수는 악성 코드다. 그 파일을 만든 사람도 누군가 그 파일을 분석할 것이라는 점을 안다. 권고 29건을 차례로 읽으면서 나는 이 단순한 조건을 여러 번 다시 떠올렸다. 2026년의 권고가 거의 모두 조작한 파일이나 프로젝트를 여는 상황을 전제로 하는 것도 그래서일 것이다. dyld 캐시 권고(GHSA-f5gv-pxqw-x95w)는 공격자와 피해자의 비용 차이가 크다고 적었다. 공격자는 48바이트 파일 하나만 준비하면 되지만, 피해자 쪽 Ghidra는 거대한 힙 할당을 감당해야 한다.

2019년 Joyce가 이 커뮤니티를 두고 백도어 같은 것을 찾아내 뜯어보는 사람들이라고 말했을 때, 그가 떠올린 것은 사람 분석가였을 것이다. 7년 뒤 같은 저장소에 공개된 권고에는 AI 기반 탐지 시스템과 언어 모델이 찾은 취약점이 포함되어 있고, 그 가운데 일부는 원인 분석까지 언어 모델이 작성했다. 그 분석에는 "LLM이 생성했으며 부정확할 수 있음"이라는 단서가 적혀 있다. Ghidra 팀은 보고자의 원문을 가능한 한 그대로 공개하는 방침을 따르고 있어서, 이 단서도 지우지 않고 공개했다.

내가 궁금한 것은 12.2가 나온 뒤의 권고 목록이다. 12.2에는 서버 허용 목록이 도입되어, 알려지지 않은 서버로 Ghidra URL을 연결하는 동작과 주석 속 URL 링크를 클릭하는 동작이 제한된다. RMI 역직렬화 취약점은 프로젝트를 열 때 서버 접속이 시작되는 동작을 공격 경로로 이용했고, 윈도우 명령 주입 취약점은 URL 주석 클릭을 이용했다. 서버 허용 목록이 제한하는 것도 이 두 동작이다.

## 출처

National Security Agency, GitHub 저장소 NationalSecurityAgency/ghidra. README, 12.0과 12.1의 What's New, master의 What's New(12.2 개발 중), Change History, `SECURITY.md`, `CONTRIBUTING.md`, 보안 권고 목록. 2026년 10월 2일 조회.
원문: <https://github.com/NationalSecurityAgency/ghidra>

보안 권고 목록: <https://github.com/NationalSecurityAgency/ghidra/security/advisories>
릴리스 목록: <https://github.com/NationalSecurityAgency/ghidra/releases>
BleepingComputer, 「NSA's Ghidra Reverse Engineering Framework Stirs Up Malware Researchers」(2019년 3월 6일): <https://www.bleepingcomputer.com/news/security/nsas-ghidra-reverse-engineering-framework-stirs-up-malware-researchers/>
TechTarget, 「NSA releases Ghidra open source reverse-engineering tool」(2019년 3월 6일): <https://www.techtarget.com/cybersecurity/news/252458982/NSA-releases-Ghidra-open-source-reverse-engineering-tool>
CyberScoop, 「NSA puts 'Ghidra,' its reverse-engineering tool for malware, in the hands of the public」(2019년 3월 5일): <https://cyberscoop.com/ghidra-nsa-tool-public/>
The Hacker News, 「NSA Releases GHIDRA Source Code」(2019년 4월 4일 갱신): <https://thehackernews.com/2019/03/ghidra-reverse-engineering-tool.html>

커버 이미지는 저장소의 `GhidraDocs/images/GHIDRA_1.png`에 있는 Ghidra 로고를 링크 미리보기 비율에 맞춰 흰 배경에 배치한 것이다.

[^source]: 저장소에서 소스 코드 전체를 추가한 커밋의 메시지는 "Candidate release of source code."이고, 커밋 작성일은 2019년 3월 26일로 기록되어 있다. 공개일 4월 4일은 The Hacker News의 보도를 따랐다.
[^api]: 커밋 수는 master 브랜치 기준이고, 기여자 수에는 GitHub 계정과 연결되지 않은 익명 기여자도 포함된다. 이 글의 별, 포크, 이슈, 풀 리퀘스트, 내려받기 수는 모두 2026년 10월 2일에 GitHub API로 조회한 값이다.
[^1211]: 12.1.2는 12.1.1 Ghidra Server의 블록 스트림 압축에서 생긴 심각한 회귀 오류를 고쳤다고 변경 내역에 적혀 있다.
[^pr]: 풀 리퀘스트 수는 GitHub 검색 API로 생성일을 기준으로 센 값이며, 이후 병합되거나 닫힌 풀 리퀘스트도 포함한다.
[^why]: 비공개 신고 절차를 안내하는 `SECURITY.md`는 6월에 추가됐지만, 권고는 그보다 이른 2월부터 늘었다. AI를 언급하지 않은 나머지 22건의 본문에는 발견 도구를 적은 대목이 없고, 적혀 있지 않다는 것만으로는 AI 도구를 썼는지 판단할 수 없다. 풀 리퀘스트가 늘어난 시기와 기여 지침이 바뀐 시기는 겹치지만, 그 풀 리퀘스트를 어떻게 작성했는지도 숫자만으로는 확인할 수 없다. 권고와 풀 리퀘스트가 늘어난 데 AI 도구가 얼마나 기여했는지는 저장소 자료만으로 셈할 수 없었다.
