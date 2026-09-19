---
title: "trycua/cua: Give AI agents computers they can use"
date: 2026-09-19T10:00:00+09:00
tags: ["컴퓨터 사용", "AI 에이전트", "오픈소스", "벤치마크", "에이전트 하네스"]
categories: ["에이전트와 코딩"]
summary: "AI 에이전트에게 조작할 컴퓨터를 제공하는 MIT 라이선스 오픈소스 스택. 클라우드 데스크톱(Fleets), 네이티브 앱 조작 계층(Driver), Apple Silicon VM(Lume), 평가 프레임워크(Bench) 네 가지로 이루어져 있고, 문서가 되는 기능보다 안 되는 기능을 더 정밀하게 적어 둔다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/trycua-cua/cover.jpg"
  alt: "Cua의 네 가지 제품 카드. 위쪽에 Cua Fleets, 아래쪽에 Cua Driver, Lume, Cua Bench가 나란히 놓여 있고 각 카드마다 코알라 마스코트가 그려져 있다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/trycua-cua/cover.jpg"
---

## 3줄 요약

1. trycua/cua는 AI 에이전트에게 조작할 컴퓨터를 제공하는 MIT 라이선스 오픈소스 스택이다. 2025년 1월 31일에 시작했고, 2026년 9월 19일 기준으로 별 23,513개와 기여자 108명을 기록하고 있다.
2. 리포는 네 가지 제품을 담는다. Cua Fleets는 격리된 클라우드 데스크톱을 빌려주고, Cua Driver는 네이티브 앱과 브라우저를 조작하며, Lume는 Apple Silicon에서 macOS와 Linux VM을 만들고, Cua Bench는 태스크를 제작해 에이전트를 채점한다.
3. Cua는 이 스택 전체를 Computer-Use 2.0이라는 말로 묶는다. 컴퓨터 사용을 스크린샷과 클릭의 반복으로만 보지 않고, 코드 실행, 구조화된 툴 호출, GUI 조작이라는 세 가지 액션 표면을 에이전트가 상황에 따라 골라 쓴다고 본다.

## 리포 기본 정보

| 항목 | 값 |
|---|---|
| 리포 | [trycua/cua](https://github.com/trycua/cua) |
| 한 줄 설명 | Scale computer-use 2.0 with open-source drivers, cross-OS fleets, and benchmarks for training, evaluation, and data generation. |
| 시작 | 2025년 1월 31일 |
| 별 / 포크 | 23,513 / 1,624 |
| 기여자 | 108명 |
| 열린 이슈 | 1,005건 |
| 라이선스 | MIT |
| 공식 사이트 | [cua.ai](https://cua.ai) |
| 최근 8주 주간 커밋 수 | 112, 154, 145, 86, 79, 53, 118, 45 |

릴리스는 컴포넌트마다 따로 나간다. `cua-driver-rs`, `sandbox`, `cua-fleet`, `@trycua/fleet`, `lume`이 각자의 태그로 배포되고, `cua-driver-rs`는 매일 나이틀리 빌드를 찍는다. 2026년 9월 15일에는 `sandbox-v0.8.0`과 `cua-driver-rs-v0.28.2`가 같은 날 올라왔다.

리포의 `libs/` 아래에는 `cua-bench`, `cua-driver`, `cua-s1`, `cuabot`, `fleet`, `kasm`, `lume`, `lumier`, `qemu-docker`, `xfce`를 포함한 열네 개의 디렉토리가 들어 있다. Rust로 쓴 Driver, Swift로 쓴 Lume, Python과 TypeScript 클라이언트가 한 모노레포 안에서 함께 관리된다.

## Computer-Use 2.0이라는 정의

공식 문서는 컴퓨터 사용을 세 가지 액션 표면으로 정리한다. 코드를 쓰고 실행하는 코딩 표면, 함수, API, MCP 서버를 호출하는 툴 사용 표면, 그리고 사람처럼 클릭하고 타이핑하고 스크롤하는 UI 자동화 표면이다. 스크린샷과 클릭의 반복은 이 중 세 번째 표면 하나에 해당한다.

문서는 접근 방식을 네 가지로 비교해 놓았다.

| 접근 | 잘 맞는 상황 | 주된 한계 |
|---|---|---|
| API 또는 구조화된 툴 | 입출력 타입이 정해진 안정적인 작업 | API가 노출하지 않는 동작에는 손댈 수 없다 |
| 브라우저 자동화 | 웹 페이지 안에서 끝나는 반복 워크플로 | 네이티브 애플리케이션과 운영체제 UI를 다루지 못한다 |
| 전통적 RPA | 미리 정해진 업무 프로세스 | 고정된 셀렉터와 좌표와 분기에 의존하는 경우가 많다 |
| 컴퓨터 사용 에이전트 | 애플리케이션과 인터페이스 종류를 넘나드는 적응적 작업 | 관찰, 복구, 권한, 검증을 세심하게 설계해야 한다 |

문서는 컴퓨터 사용 에이전트의 계보도 함께 설명한다. 스크린샷 기반 컴퓨터 사용은 2024년 10월 Anthropic이 GUI를 스크린샷과 입력 이벤트로 조작하는 에이전트를 발표하면서 빨라졌다고 한다. 그리고 2025년을 지나며 코딩 에이전트도 컴퓨터 사용 에이전트로 받아들여지기 시작했고, CoAct-1이 그 연결을 명시했다고 한다.

Cua가 그리는 호출 순서는 `모델 → 에이전트 하네스 → Cua Driver → 운영체제와 애플리케이션`이다. Cua Driver는 UI 툴 계층까지만 담당하고 모델을 고르거나 실행하지 않는다.

![Cua 아키텍처 도식. Desktop Sandboxes(Environment), Computer Framework(Execution), Agent Framework(Intelligence) 세 열로 구성 요소를 나열하고 있다.](https://img.seosoyoung.eiaserinnys.me/images/trycua-cua/cua-architecture.png)
<small>리포의 <code>img/cua-architecture.png</code>. 환경, 실행, 지능이라는 세 영역으로 스택 전체를 정리한 도식이다. 샌드박스 쪽에는 Docker 위의 Linux GUI, QEMU Docker를 통한 Windows, Linux, Android, Lume를 통한 macOS VM, Windows Sandbox가 들어간다.</small>

## Cua Driver: 네이티브 앱을 조작하는 계층

Cua Driver는 macOS, Windows, Linux에서 네이티브 데스크톱 앱과 브라우저를 검사하고 조작하는 도구를 에이전트에게 제공한다. 에이전트는 CLI로 붙어도 되고, MCP로 붙어도 되고, 타입이 붙은 SDK로 붙어도 된다. 앱과 플랫폼이 허용하면 포인터를 움직이거나 포커스를 빼앗지 않고 백그라운드로 입력을 전달한다.

설치 명령은 한 줄로 끝난다.

```sh
# macOS / Linux
/bin/bash -c "$(curl -fsSL https://cua.ai/driver/install.sh)"
```

```powershell
# Windows
irm https://cua.ai/driver/install.ps1 | iex
```

### 지원 등급을 세 단계로 표기한다

플랫폼 지원 문서는 등급을 셋으로 두고 있다. Supported는 기준 Rust 하니스가 실제 앱에서 검증을 마친 상태다. Supported with limits는 일반 경로는 증명했고 미지원 경로에 대해서는 구조화된 거부를 돌려주는 상태다. Experimental은 백엔드는 존재하지만 대표 커버리지가 아직 완전하지 않은 상태다.

| 플랫폼 | 창 시스템과 API | 현재 상태 |
|---|---|---|
| Windows | Win32, UI Automation, 네이티브 입력, 특정 윈도우 메시지 | Supported. Electron, Tauri, WPF, WinUI 3, WebView2를 대표 커버리지로 검증했다. 일부 백그라운드 Chromium 제스처와 상승된 무결성 경계는 검증하지 않았다 |
| macOS | AppKit, Accessibility, Quartz/HID, ScreenCaptureKit | Supported. Electron, Tauri, AppKit, SwiftUI, WKWebView를 검증했다. 손쉬운 사용과 화면 기록 권한이 필요하다 |
| Linux X11 | X11/EWMH, XTest, AT-SPI, 툴킷 접근성 브리지 | 툴킷별 제약이 있는 Supported |
| Linux Wayland | AT-SPI와 컴포지터별 discovery, capture, activation, portal input | 컴포지터별 제약이 있는 Supported |

Linux는 창 시스템마다 등급을 따로 매겼다. X11/Xorg는 Supported, Sway는 제약이 있는 Supported, GNOME/Mutter도 제약이 있는 Supported, XWayland도 제약이 있는 Supported다. Hyprland와 Omarchy, KDE/KWin, `cua-compositor` 중첩 세션은 Experimental이다.

Hyprland 항목의 기록 방식이 특히 상세하다. 2026년 9월 7일까지 머지된 작업으로 PR 세 건을 적어 두었다. 캡처를 담당하는 #3557, discovery와 생존 확인만 담당하는 #3547, 실험적 입력 v3인 #3572다. 이 기능은 Cua Driver 0.24.0에서 별도 플러그인으로, 기본 비활성 상태로 나갔다. 자격 검증 범위에 든 네이티브 앱은 `libreoffice-fresh 26.2.5-3` 패키지의 Calc와 Inkscape 1.4.4-6까지다. Driver는 행동을 실행하기 전마다 실행 중인 바이너리가 기대한 패키지 경로와 로컬 패키지 메타데이터에 맞는지 확인한다. 인증한 플러그인 Fleet 환경은 Omarchy 4.0.1-1과 Cua Driver 0.22.2 조합이고, 물리 호스트를 대상으로 한 Omarchy 4.0.2-1과 Driver 0.23.2 조합은 인증하지 않았다고 따로 밝혀 놓았다.

브라우저 조작도 경로마다 다르다. Windows의 Chrome과 Edge는 스냅샷, 내비게이션, 신뢰된 백그라운드 클릭까지 폭넓게 지원하지만 상승된 무결성 프로세스는 거부한다. macOS의 Chrome은 신뢰된 CDP 포인터 입력을 요청받으면 `browser_input_trust_unavailable`을 돌려준다. Safari와 Firefox에서는 타입이 붙은 브라우저 뮤테이션 엔진을 쓸 수 없고, 네이티브 discovery와 접근성 경로만 쓸 수 있다.

### 첫 실행이 어떤 모습인가

튜토리얼이 요구하는 첫 결과물은 계산기 앱을 열어 6 × 7을 계산하고 화면에 42가 떴는지 에이전트가 직접 읽어 확인하는 것이다. macOS는 14 Sonoma 이상이 필요하다. 데몬을 띄운 다음 `cua-driver permissions grant`로 손쉬운 사용과 화면 기록 권한을 요청한다. 두 프롬프트는 "Open System Settings" 버튼만 제공한다. 설정 창을 열어 토글을 직접 켜야 권한이 부여된다.

```sh
cua-driver status           # "Cua Driver daemon is running"
cua-driver doctor
cua-driver call list_apps
cua-driver skills install    # Claude Code 스킬 설치
cua-driver mcp-config --client claude
```

데몬은 기본적으로 `standard` 인가 모드로 뜬다. 문서는 실제 워크로드에서는 `bounded` 모드를 검토하라고 권한다.

## Cua Fleets와 Sandbox SDK

Sandbox SDK는 격리된 컴퓨터 한 대를 나타내는 객체다. 같은 SDK가 로컬 하드웨어에서도 돌아가고 Cua Fleet의 호스팅 용량에서도 돌아간다. Fleets는 여기에 풀, 클레임, 인증, 서비스 라우팅을 더해서 관리형 클라우드 컴퓨터를 예약해 쓰게 해 준다. 풀은 재사용 가능한 호스팅 용량을 소유하고, 클레임은 그 용량에서 컴퓨터 한 대를 예약한다.

버전 관계는 문서에 고정되어 있다. Python Sandbox SDK는 `cua-sandbox` 0.7.0이고 `cua` 0.1.6 패키지에서 다시 내보낸다. Fleet 클라이언트는 Python이 `cua-fleet` 0.1.17, TypeScript가 `@trycua/fleet` 0.1.2다. `cua-sandbox[driver]` 0.7.0은 `cua-driver` 0.27.0에 대응한다.

같은 SDK를 쓴다고 해서 로컬과 Fleet이 같은 이미지를 받아 주지는 않는다.

| 이미지 지정 | 게스트와 종류 | 로컬 런타임 | Fleet SDK 수용 (0.7.0) |
|---|---|---|---|
| `Image.linux()` | Ubuntu 24.04 VM | 베어메탈 QEMU | 내장 레지스트리 아티팩트로 매핑 |
| `Image.linux(kind='container')` | Ubuntu 24.04 컨테이너 | Docker | 거부 |
| `Image.linux('ubuntu','22.04')` | Ubuntu 22.04 VM | 베어메탈 QEMU | 거부 |
| `Image.windows()` | Windows Server 2022 VM | Hyper-V, 없으면 Docker로 감싼 QEMU 또는 베어메탈 QEMU | 내장 매핑, EFI 템플릿 선택 |
| `Image.windows('11')` | Windows 11 VM | 로컬 ISO 설치 경로 | 거부 |
| `Image.macos()` | macOS 26 또는 15 VM | Lume (Apple Silicon 호환 호스트) | 거부 |
| `Image.android()` | Android 14 VM | Android 에뮬레이터 | 거부 |

일곱 줄 가운데 다섯 줄이 거부로 표시되어 있다. Fleet이 내장 매핑으로 받아 주는 것은 Ubuntu 24.04 VM과 Windows Server 2022 VM 두 가지뿐이다. 각각이 가리키는 레지스트리 아티팩트는 다음과 같다.

- Ubuntu 24.04 VM: `public.ecr.aws/k5j5w0x5/cua-ubuntu-24.04:main-38352d34`
- Windows Server 2022 VM: `public.ecr.aws/k5j5w0x5/cua-windows-2022:main-bac7daa3`

서비스 계약도 명시되어 있다. 기본 서비스 이름은 `server`이고 기본 포트는 8000이며, TCP readiness probe를 거친 뒤 Sandbox가 `/status`를 기다린다. 버전 0.7.0에서 `Sandbox.ephemeral()`의 Fleet 이미지 경로는 `region='us-east-1'`만 허용하고, `Pool.apply()`에는 region 인자가 없다. `Sandbox.snapshot()`은 로컬과 Fleet 양쪽 모두 아직 구현되지 않았다.

비용에 관한 경고가 문서 여러 곳에 반복해서 나온다. `pool.claim()` 컨텍스트가 끝나면 클레임은 풀리지만 풀은 warm 상태의 샌드박스를 계속 유지할 수 있고, 워크로드가 끝난 뒤에도 클라우드 리소스 과금이 이어질 수 있다. 재사용 가능한 풀에는 명시적인 정리 절차나 만료 정책이 필요하다.

## Lume: Apple Silicon 위의 로컬 VM

Lume는 Apple의 Virtualization.Framework를 써서 Apple Silicon M1 이상에서 macOS와 Linux VM을 만들고 관리하는 CLI와 데몬 서버다. 튜토리얼의 첫 결과물은 Apple 복구 이미지로 macOS Tahoe VM을 만들어 부팅하고 SSH로 접속하는 것이다.

![Lume 아키텍처 도식. Interface layer, Core layer, Infrastructure 세 계층으로 CLI Tools, HTTP API, Direct Access와 Lume CLI, Lumier를 배치하고 맨 아래에 Apple Virtualization Framework를 둔다.](https://img.seosoyoung.eiaserinnys.me/images/trycua-cua/lume-architecture.png)
<small>리포의 <code>img/lume-architecture.png</code>. 인터페이스 계층에 CLI 도구와 HTTP API와 직접 접근이 놓이고, 코어 계층에서 포트 7777의 Lume CLI와 Docker + noVNC 인터페이스인 Lumier가 나란히 놓이며, 맨 아래에는 Apple Virtualization Framework가 자리한다.</small>

Lume는 GHCR 레지스트리에서 macOS 이미지를 받아 오고, 저장 위치를 자유롭게 지정할 수 있으며, IPSW에서 완전 무인 설치를 지원한다. 같은 리포의 `libs/lumier`는 컨테이너 안에서 Lume CLI를 호출하는 Docker 이미지다. macOS와 Linux VM을 컨테이너에 담고 noVNC로 화면을 내보낸다.

## Cua Bench: 태스크를 만들고 에이전트를 채점한다

Cua Bench는 컴퓨터 사용 벤치마크와 강화학습 환경을 위한 MIT 라이선스 프레임워크다. 태스크, 시작 상태, 에이전트 인터페이스, 평가자를 하나로 묶어서 Linux, Windows, Android, 브라우저, 시뮬레이션 환경에서 반복 가능한 실험을 돌린다.

시작하는 데 VM도 Docker도 모델 API 키도 필요하지 않다. Python 3.12나 3.13과 uv만 있으면 된다.

```bash
uv tool install 'cua-bench[browser]'
uv tool run --from 'cua-bench[browser]' playwright install chromium
```

첫 결과물은 작은 태스크를 만들고 그 참조 해법을 실행해서 평가자가 보상 `1.0`을 보고하는지 확인하는 것이다. 그다음에는 같은 태스크를 사람이 직접 풀어 본다.

![Cua Bench 아키텍처 도식. Base Images(Environment), Task Framework(Authoring), Evaluation & Training Harness 세 열로 구성 요소를 나열한다.](https://img.seosoyoung.eiaserinnys.me/images/trycua-cua/cua-bench-architecture.png)
<small>리포의 <code>img/cua-bench-architecture.png</code>. 태스크 작성은 <code>@tasks_config</code>, <code>@setup_task</code>, <code>@evaluate_task</code>, <code>@solve_task</code> 데코레이터로 이루어지고, 평가 하니스는 에이전트 컨테이너와 환경 컨테이너를 Docker 네트워크로 연결한, 컨테이너 두 개짜리 구조를 쓴다.</small>

도식에는 크로스 플랫폼 태스크 생성이라는 항목도 들어 있다. 같은 태스크를 Windows 11에서 Windows 98로, macOS Sequoia에서 System 7로, Ubuntu에서 Red Hat Linux로 생성한다는 예시가 적혀 있다. 태스크 레지스트리는 `cuabench.ai/registry`에 있다.

## 리포에 함께 들어 있는 것들

`libs/cua-s1`은 작고 전문화된 컴퓨터 사용 모델을 연구하는 프로젝트다. 첫 체크포인트인 `cua-s1-form-v0`은 폼 중심의 인터페이스 작업을 위한 전문가 체크포인트이며, 범용 어시스턴트로 취급해서는 안 된다고 적혀 있다. 이 컴포넌트는 모델 코드, 합성 데이터, 학습, 평가 코드만 담고 가중치와 데이터셋과 데모 바이너리는 포함하지 않는다. 체크포인트 로딩은 로컬 `safetensors` 파일만 받아 주고 pickle 기반 PyTorch 체크포인트는 거부한다. 런타임의 기본값은 드라이런이다. 대상 창을 하나로 특정해야 하고, 스냅샷에 묶인 엘리먼트 토큰을 쓰며, 변경이 일어날 때마다 창을 다시 관찰한다. `execute`와 `submit`은 각각 따로 켜야 한다.

`libs/cuabot`은 코딩 에이전트에게 컴퓨터 사용 능력을 붙여 주는 다중 사용자 샌드박스다. `npx cuabot` 한 줄로 시작하고, Claude Code, Gemini CLI, Codex CLI, OpenClaw를 샌드박스 안에서 실행하거나 샌드박스 Chromium 창을 띄울 수 있다.

![cuabot 스크린샷. LibreOffice Calc 창에 Hello, world! 가 입력되어 있고, 그 위에 겹친 터미널에서 cuabot 명령이 실행되고 있다.](https://img.seosoyoung.eiaserinnys.me/images/trycua-cua/cuabot-screenshot.png)
<small>리포의 <code>img/cuabot-screenshot.png</code>. 터미널에서 <code>cuabot --click 150 48</code>과 <code>cuabot --type "Hello, world!"</code>를 실행하자 LibreOffice Calc 셀에 텍스트가 입력된다. 커서 옆 툴팁에 <code>cuabot 1</code>이라는 사용자 표시가 붙어 있다.</small>

## 문서에서 눈에 걸린 것

문서를 훑다가 내가 몇 번씩 되돌아가 읽은 대목은 안 되는 기능을 적어 두는 방식이었다.

플랫폼 지원 문서는 Supported with limits라는 중간 등급을 따로 만들어 두고, 그 등급의 정의를 "일반 경로는 증명했고 미지원 경로에 대해서는 구조화된 거부를 돌려준다"로 쓴다. 조용히 실패하지 않고 이름이 붙은 거부로 응답하겠다고 문서가 약속한다. macOS Chrome에서 신뢰된 포인터 입력을 요청하면 `browser_input_trust_unavailable`이 오고, Hyprland 0.56.2에서 discovery와 생존 확인만 들어간 단계에서는 여섯 종류의 입력 메시지가 전부 `background_unavailable`을 반환한다. Fleet SDK 수용표의 거부 칸 다섯 개도 같은 성격이다. 에이전트가 자기 실패를 스스로 알아차리기 어려운 환경에서는, 오류 이름을 명시해 응답하는 설계가 하나의 기능으로 작동한다.

버전을 적는 방식에서도 같은 태도가 보인다. 문서는 "Hyprland를 지원한다"로 끝내지 않고, Omarchy 4.0.1-1과 Cua Driver 0.22.2로 구성한 플러그인 Fleet 환경에서 인증했으며 Omarchy 4.0.2-1과 Driver 0.23.2를 올린 물리 호스트에서는 인증하지 않았다고 쓴다. 검증한 앱도 `libreoffice-fresh 26.2.5-3`의 Calc와 Inkscape 1.4.4-6으로 패치 번호까지 남긴다. 컴퓨터 사용은 운영체제, 툴킷, 앱 버전이 조금만 달라져도 동작이 달라진다. 그래서 이렇게 좁게 적어 둘수록 읽는 쪽에서는 더 믿게 된다.

Cua-S1에도 비슷한 조건이 걸려 있다. 계획과 실행을 분리하고, 런타임 기본값을 드라이런으로 두고, `execute`와 `submit`을 각각 별도로 켜게 하고, 변경이 일어날 때마다 창을 다시 관찰한다. 소스만 공개하면서 이 릴리스로는 어떤 체크포인트 성능 주장도 성립하지 않는다고 먼저 밝히는 문장도 흔치 않다.

열린 이슈가 1,005건이라는 숫자는 이 프로젝트가 관리하려는 범위가 얼마나 넓은지 알려 준다. Rust, Swift, Python, TypeScript를 한 리포에 담고, Windows와 macOS와 Linux X11과 Linux Wayland 네 가지 창 시스템을 따로 다루고, QEMU, Hyper-V, Apple Virtualization.Framework, Docker를 모두 런타임으로 받으려 하면 그렇게 된다.

## 출처

Cua AI, Inc., trycua/cua (MIT License). 2025년 1월 31일 시작, 2026년 9월 19일 조회.
원문: <https://github.com/trycua/cua>
공식 문서: <https://cua.ai/docs>
본문 도식과 스크린샷은 리포의 `img/` 디렉토리에서 인용했다.
