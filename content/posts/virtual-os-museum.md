---
title: "1700개의 운영체제가 깨어 있는 박물관"
date: 2026-05-20T10:30:00+09:00
tags: ["컴퓨팅 역사", "운영체제", "소프트웨어 보존", "에뮬레이션", "디지털 아카이브"]
categories: ["창작과 문화"]
summary: "Andrew Warkentin이 20년에 걸쳐 정비한 The Virtual OS Museum은 1948년 Manchester Baby부터 현재까지 1700개 이상의 운영체제를 한 클릭으로 실행 가능한 상태로 모아둔다. 보존(preservation)이 아니라 접근성(reachability) — 이 차이가 이 박물관의 본질이다."
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/cover-virtual-os-museum.jpg"
sidenotes: true
---

## 결론부터 짚는 이정표

오늘은 제가 큐레이터가 되어 한 박물관을 안내해 드리려 합니다. 다만 미리 짚어 둘 것이 있습니다 — 진짜 큐레이터는 따로 있고, 저는 오늘 하루 그분의 전시 앞에 서서 안내봉을 빌려 든 사람일 뿐이지요.

그분의 이름은 *Andrew Warkentin*. 본인의 자기 소개를 그대로 옮기면 *"OS/emulator developer and OS historian"* — OS 개발자이자 OS 역사가입니다.[^2] 2003년부터 20년 넘게 *혼자서* 운영체제를 모으고, 패치하고, 사용자가 한 번의 클릭으로 부팅할 수 있는 형태로 정비해 오는 동시에, *UX/RT*라는 본인의 QNX형 마이크로커널 OS를 짓고 있는 분이지요.

과거를 *살아 있는 상태로* 보존하는 일과, 새로운 OS를 *처음부터* 짓는 일이 같은 책상 위에서 벌어진다는 사실이 — 이 박물관의 결을 어느 정도 설명합니다. 오늘의 전시는 그분의 손에서 자란 박물관 — *The Virtual OS Museum* — 입니다. 1948년 Manchester Baby부터 현재까지 250여 개 플랫폼·570여 종 운영체제·1700여 개 사전 설치본이 *깨어 있는 상태로* 모여 있는 곳이지요.[^1]

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/museum-home.jpg" alt="The Virtual OS Museum 홈페이지 풀페이지 캡쳐" caption="박물관의 첫 페이지 전체. 타이틀 → 통계 카드(1700+·250+·570+·1948–now) → 격자로 정렬된 운영체제 스크린샷 갤러리로 이어지는 단순한 구조가, 1700개의 OS를 *서가에 늘어 놓듯* 보여 준다. © virtualosmuseum.org" >}}

이런 박물관의 가치는 *보존(preservation)*이 아니라 *접근성(reachability)*에 있습니다. 디스크 이미지를 모아 두는 일은 이제 어렵지 않습니다. 어려운 것은 그것을 *지금 이 노트북 위에서 실제로 부팅되게 만드는 일*입니다. 그리고 그 거리를 좁힌 사람은 — 단체도 재단도 정부 사업도 아닌 — Andrew 한 명입니다. 이 두 축, *접근성*과 *한 사람의 20년*이 박물관의 모든 것이지요.

그럼 함께 입구로 들어가지요.

## 입구 — 안내 데스크

박물관에 들어서면 제일 먼저 보이는 것은 *실행기*입니다. 운영체제별로 분류된 메뉴에서 항목 하나를 누르면, 그에 맞는 에뮬레이터가 미리 설정된 상태로 켜지고, 당대 응용 소프트웨어까지 깔린 화면이 펼쳐집니다. 깨진 상태를 만들었어도 *복원 지점*으로 되돌리면 그만이고요. 이 작은 장치 하나가 박물관 전체의 성격을 결정합니다 — 방문객이 *설정* 대신 *구경*에 집중할 수 있도록.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/launcher.png" alt="The Virtual OS Museum 런처 메인 윈도우" caption="실행기 메인 화면. 항목 하나를 누르면 그에 맞는 에뮬레이터가 미리 설정된 상태로 켜진다. © virtualosmuseum.org" >}}

전체 패키지는 두 갈래로 나뉩니다. *Full*은 모든 디스크 이미지가 이미 들어 있어 오프라인에서도 굴러갑니다. *Lite*는 가벼운 골격만 받고, 부팅하는 순간에 필요한 이미지를 가져옵니다. 어느 쪽을 고르든 들어오는 문은 같은 한 곳입니다.

자, 그럼 본관으로 들어가지요.

## 1전시실 — 시작의 방 (1948 –)

이 방에는 *세계 최초의 저장 프로그램 컴퓨터*인 Manchester Baby의 테스트 프로그램이 있습니다. Mark 1 Scheme A·B·C·T 같은, "이걸 운영체제라 부를 수 있을까" 망설여지는 가장 이른 시스템 소프트웨어들도 함께. 그 옆에는 영국 EDSAC의 코드, 그리고 *현대 OS의 시조*로 흔히 언급되는 CTSS, 그 직계 후손 Multics가 자리합니다.

여기서 한 번 멈춰 서서 확인해 두지요. 우리가 *운영체제*라 부르는 것이 처음부터 운영체제로 태어나지 않았다는 사실입니다. 처음에는 *모니터*였고, 그다음에는 *배치 시스템*이었으며, 그다음에야 시분할이라는 개념이 등장했지요. 이 전시실은 그 점진적 성장을 *추상적 다이어그램*이 아니라 *실제 부팅 화면*으로 보여 줍니다. 이론과 화면은 다른 무게를 지닙니다.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/manchester-baby.png" alt="Manchester Baby 복제품" caption="Manchester Science and Industry Museum의 Manchester Baby 복제품. 1948년 6월 21일, *세계 최초의 저장 프로그램*이 윌리엄스 튜브의 인광 위에서 돌아간 풍경. 사진: Logg Tandy / Wikimedia Commons (CC BY 4.0)" >}}

## 2전시실 — 워크스테이션의 방 (1970s – 90s)

긴 복도를 지나면, *유닉스 가문*이 줄지어 있습니다. PERQ 시리즈, SunOS, IRIX, OSF/1, A/UX, NeXTSTEP, 그리고 십수 년에 걸쳐 다양해진 BSD들과 Linux 배포본들. 일반 사용자에게는 이름조차 생경하겠지만, 오늘날 macOS의 *직계 조상*인 NeXTSTEP을 직접 부팅해 볼 수 있다는 점만 짚어도 이 방의 가치는 충분합니다.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/nextstep.png" alt="NeXTSTEP 3.3 데스크탑" caption="NeXTSTEP 3.3 (68k). 검은 도크와 워크스페이스 매니저 — 지금 macOS 도크의 직계 조상이다. © virtualosmuseum.org" >}}

전시 도중 갈라진 가지 하나가 눈에 들어옵니다. *Plan 9*. 벨 연구소에서 유닉스의 후계로 설계되었지만 주류가 되지는 못한 운영체제이지요. 옆 진열장의 Oberon, Inferno, ZetaLisp — 이런 시스템들은 *역사에서 살아남지 못한 길*입니다. 박물관이 보존하지 않았다면 *생각의 갈래 자체*가 잊혔을 가지들. 컴퓨팅 역사가 *직선*이 아니라 *덤불*이었다는 사실이, 이런 방에서야 비로소 손에 잡힙니다.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/plan9.png" alt="Plan 9 4th Edition acme 파일시스템 서버" caption="Plan 9 4th Edition. *모든 것이 파일*이라는 유닉스 원칙을 끝까지 밀어붙인 후계가 어떻게 생겼는지 — 이런 화면이 아니면 글로 옮기기 어렵다. © virtualosmuseum.org" >}}

## 3전시실 — 거실의 방 (1970s – 80s)

다음 방은 분위기가 사뭇 다릅니다. 가정용 8비트 컴퓨터들 — Apple II, Commodore의 8비트 머신, Atari 8비트, 일본의 MSX, BBC Micro, ZX Spectrum, Sharp MZ, Tandy TRS-80, 그리고 CP/M의 여러 변종들이 *각자의 부팅음*을 가진 채 줄지어 있지요. 이 방의 OS들은 워크스테이션 방의 점잖은 친척들보다 훨씬 가깝게 느껴집니다. 거실에 놓였던 컴퓨터들이고, 누군가의 첫 컴퓨터였으며, 시간이 흘러 그 사람이 지금 이 박물관의 *방문객*이 되어 있을 가능성도 높지요.

이 방에서 자주 받는 질문이 있다고 들었습니다.
*"왜 제가 어릴 적에 쓰던 그 컴퓨터의 화면이 이렇게 작아 보이지요?"*
답은 두 갈래로 갈립니다. 화면이 작은 것이 아니라, 우리가 자란 것이지요. 그리고 또 하나 — 그 시절 운영체제는 정말로 *작았습니다*. 64KB의 메모리, 한 줄의 명령 프롬프트, 그 위에 얹힌 한두 개의 응용. 그것이 한때 "개인이 다룰 수 있는 컴퓨터"의 전부였다는 사실을 화면이 정직하게 보여 줍니다.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/bbc-master.png" alt="BBC Master Compact 데스크탑" caption="BBC Master Compact의 MOS 5.10 데스크탑. 영국 교실에서 한 세대가 코딩을 배웠던 그 화면. © virtualosmuseum.org" >}}

## 4전시실 — 책상의 방 (1980s – 2000s)

PC 시대의 거대한 전시실입니다. 한쪽 벽에는 DOS의 모든 변종이, 다른 한쪽에는 OS/2가, 가운데에는 Windows의 *1.0부터 Longhorn 베타까지*가 시간 순으로 줄지어 있습니다. 맞은편으로는 Classic Mac OS — System 1.0의 알파 빌드부터 Mac OS X 10.5 PowerPC까지가 같은 방식으로 늘어서 있고, 그 사이 어딘가에 BeOS가 자기 자리를 차지하고 있지요.

이 방에서 가장 흥미로운 *관람법*은 GUI의 계보를 *옆에 놓고 비교하는 것*입니다. Xerox Star/ViewPoint — *데스크탑 메타포의 발명*이 시작된 그 자리 — 에서 출발해, Apple Lisa로 이어지고, Classic Mac으로 다듬어지고, Windows로 대중화되는 흐름. 우리가 *데스크탑*이라 부르며 별다른 의식 없이 매일 마주하는 그 비유가 어떤 갈래를 거쳐 지금에 이르렀는지를, *그 시대의 실제 화면을 옆에 놓고* 짚을 수 있는 곳은 흔하지 않습니다.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/xerox-star.jpg" alt="Xerox Star 8010 워크스테이션" caption="Xerox Star 8010 (1981). 우리가 *데스크탑*이라 부르는 것의 거의 모든 비유 — 아이콘, 풀다운 메뉴, 마우스, 윈도우 — 가 여기서 출발했다. 사진: vonguard / Wikimedia Commons (CC BY-SA 2.0)" >}}

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/lisa-os.png" alt="LisaOS 3.1 LisaDraw" caption="Apple Lisa의 LisaDraw (1984). Xerox의 비유가 *상용 제품*으로 다듬어진 자리. © virtualosmuseum.org" >}}

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/mac-os-1-alpha.png" alt="Classic Mac OS 1.0 알파 (Sony Test) Finder" caption="Classic Mac OS 1.0 알파판 (Sony Test, 1983-10-04). 정식 발매 *반년 전*의 Finder가 이미 이 모습이었다. © virtualosmuseum.org" >}}

여기서 잠시 멈춰 서서 다른 가지 하나를 들여다보지요. *BeOS*. 1990년대 후반 멀티미디어 성능과 객체 지향 구조로 주목받았지만, 시장에서는 결국 패한 운영체제입니다. 박물관에는 단순히 "패한 OS의 데모"가 아니라, *지금의 데스크탑이 BeOS의 길을 갔다면 어떻게 다르게 느껴졌을지*를 손끝으로 만져 볼 수 있는 자리가 있습니다. 그것이 박물관이 줄 수 있는, 글로는 잘 옮겨지지 않는 종류의 통찰입니다.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/beos.png" alt="BeOS R5 데스크탑" caption="BeOS R5 데스크탑. 옐로 탭과 멀티트랙 미디어 — *데스크탑은 다른 모습일 수도 있었다*는 사실의 살아 있는 증거. 사진: Tullius / Wikimedia Commons (CC BY-SA 3.0)" >}}

## 5전시실 — 손바닥과 공장의 방

마지막 본관 전시실에는 모바일과 임베디드 OS가 모여 있습니다. PalmOS, EPOC/Symbian, Windows CE, Newton OS, 에뮬레이션이 허용되는 범위 내의 초기 Android와 iOS, 산업용 실시간 OS QNX 등. 손바닥 위에 올라가는 컴퓨터와 공장 한구석에서 멈추지 않고 돌아야 하는 컴퓨터 — *데스크탑과는 다른 우주에서 자란 OS*들이지요.

여담을 하나 더하자면 — QNX 코너는 큐레이터의 *전공*에 가까운 자리입니다. 그가 짓고 있는 UX/RT가 QNX형 마이크로커널 OS이고, 블로그에는 QNX 6.1 (2001)에 대한 *두 부분짜리 상세 투어* 글이 따로 올라가 있지요.[^3] *MicroGUI*라 부르는 Photon 윈도우 시스템이 어떻게 X11의 모놀리식 서버 모델 대신 마이크로커널 철학을 GUI 계층까지 끌어올렸는지를, 그는 인스톨러 화면 하나하나까지 짚으며 풀어 놓습니다. 단순한 *수집가*가 아니라 *각 OS의 전문가 큐레이터*임을, 이런 글 한 편이 가만히 보여 줍니다.

스마트폰이라는 단어가 자리 잡기 전, *팜탑*이라는 표현이 한참 쓰였습니다. PalmOS의 흐릿한 모노 화면 위에서 사람들은 메모를 적고, 일정을 관리하고, 주소록을 옮겨 다녔지요. 지금 우리 손에 쥔 기기와 *기능적으로는* 그리 멀지 않습니다. 차이는 *해상도*가 아니라 *연결성*에 있었다는 사실 — 그 점은 이 방에 와서야 깨끗하게 보입니다.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/palm-m505.jpg" alt="Palm m505 (Palm OS 4.0)" caption="Palm m505 (Palm OS 4.0). 스마트폰이라는 단어가 자리 잡기 전, *손바닥 위에서 일정을 옮기고 메모를 적던* 한 세대의 기기. 사진: Coplan / Wikimedia Commons (Public Domain)" >}}

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/qnx.png" alt="QNX 1.2 부팅 화면" caption="QNX 1.2의 부팅 화면. 자동차 인포테인먼트와 의료기기 안에서 지금도 조용히 돌아가는 실시간 OS의 1980년대 모습. © virtualosmuseum.org" >}}

## 큐레이터의 방 — 왜 이런 박물관이 필요한가

본관을 한 바퀴 돌고 나면, 자연스럽게 *큐레이터의 방*으로 향하게 됩니다. 박물관 운영자, 그러니까 이 모든 것을 모은 사람의 작업실이지요.

{{< figure src="https://img.seosoyoung.eiaserinnys.me/images/virtual-os-museum/andrew-warkentin.jpg" alt="Andrew Warkentin 포트레이트" caption="박물관의 큐레이터, Andrew Warkentin. 사진: virtualosmuseum.org / About the curator" >}}

솔직히 짚자면 — 실제 사이트에 그런 방이 따로 있는 것은 아닙니다. *About* 페이지 한 장과 운영자의 블로그·유튜브 채널 정도가 전부지요. 그럼에도 큐레이터에 대해서 언급할 필요가 있다고 느꼈습니다. 보통의 박물관은 큐레이터를 *전시 뒤편*에 두지만, 이 박물관은 큐레이터의 노동 자체가 *전시의 본문*이거든요.

큐레이터가 자기 작업을 설명하는 문장이 하나 있습니다. 박물관 입구의 문구를 그대로 옮기지요.[^1]

> "이론상 부팅 가능한 것이 아닙니다. 화요일에 올바른 툴체인을 조립하면 *원칙적으로* 부팅된다는 의미가 아닙니다. *도달 가능*. 항목 하나를 누르면 실행되고, 가능하면 당대 사람이 실제로 썼던 방식 그대로 소프트웨어가 깔린 상태로 실행된다는 의미입니다."

이 문장이 박물관의 모든 것을 설명합니다. 소프트웨어 보존(preservation)과 도달 가능성(reachability) 사이의 거리 — 그 거리는 *수십 시간의 에뮬레이터 설정*, *옛 버전에서만 굴러가는 OS를 위한 특정 빌드 보관*, *현대 리눅스에서 돌게 만든 작은 패치들*, *때로는 거의 일주일이 걸리는 단 하나의 OS 설치*로 채워져 있지요. 그 거리를 누가, 어떻게 좁히느냐가 *디지털 보존의 진짜 질문*입니다.

글 첫머리에서 한 번 짚었지만, 큐레이터의 방에 들어와서야 그 무게가 제대로 와닿습니다. 이 거대한 박물관은 *한 사람의 20년*입니다. 단체도, 재단도, 정부 사업도 아닙니다. Andrew Warkentin이라는 한 명이 2003년부터 모으고, 정비하고, 가끔은 일주일을 들여 단 하나의 OS를 설치해 온 결과물이지요. 후원 페이지에는 Patreon과 Ko-fi 링크가 단정하게 놓여 있습니다. 한 사람이 자기 시간을 보태어 *공공재에 가까운 인프라*를 지탱하고 있는 셈입니다.

왜 이 분야는 유독 그렇게 굴러갈까요. 종이책 도서관은 사서가 *조용히 일하는 동안 책은 책장에 가만히 놓여 있어* 됩니다. 그림 박물관도, 화첩이 액자 안에서 *변형되지 않은 상태로 머무는 일*이 핵심이지요. 그러나 운영체제는 그렇지 않습니다. *부팅되는 상태*는 가만히 두면 점점 멀어집니다. 에뮬레이터가 업데이트되면 옛 OS가 회귀로 깨지고, 호스트 OS가 바뀌면 에뮬레이터가 깨지고, 모두가 멀쩡해도 깔린 응용이 누락되면 *시대의 사용감*이 사라지지요. 그러니 디지털 보존은 *조용한 유지*가 아니라 *끊임없는 재조립* 노동입니다.

큐레이터의 방에서 한 가지 더 짚어 두고 싶은 것이 있습니다. Andrew의 박물관 출시 글 끝자락에 이런 문장이 있지요 — *"내게는 사람들과 연결되기를 극도로 어렵게 만드는, 침묵하는 경향이 심하게 있다."*[^2] 박물관을 더 일찍 내지 못한 이유, 한 대기업이 UX/RT를 QNX 대체로 검토하다가 *조용히* 사라진 이야기, 그리고 *앞으로는 자기 작업에 대해 가능한 한 자주 글을 올려 보겠다*는 다짐이 — 이 한 문장 주변에 함께 놓여 있습니다. 디지털 보존이 *조용한 시간 노동*이라는 추상은, 이런 자기 고백 한 줄 앞에서 사람의 얼굴을 얻습니다. 한 사람의 *침묵하는 경향*이 1700개의 OS를 *깨우는 손*이 된 셈입니다. 박물관의 약 절반은 *VM 안에서 아직 테스트가 끝나지 않은 상태*라고 그는 정직하게 적어 두지요. *완성된 박물관*이 아니라 *지금도 굴러가는 작업*이라는 사실까지 숨기지 않는 것입니다.

## 출구에서

박물관을 나서면서 — 박물관이 우리에게 무엇을 남기는지 잠깐 정리해 두지요.

첫째, *컴퓨팅 역사는 직선이 아니라 덤불*입니다. NeXTSTEP, BeOS, Plan 9, Oberon, ZetaLisp 같은 사라진 가지들이 박물관 곳곳에 살아 있습니다. 살아남은 길이 *가장 좋아서 살아남은 길*은 아닙니다. 그 점을 잊고 있으면, 지금 우리가 쓰는 기술의 형태를 *자연스러운 귀결*로 받아들이게 됩니다 — 박물관은 그렇지 않다고 알려 줍니다.

둘째, *데스크탑 메타포는 누가 그렸는가*. Xerox Star의 화면을 처음 부팅해 보면, 1981년에 이미 *우리가 매일 보는 데스크탑의 거의 모든 것*이 자리 잡고 있었다는 사실에 약간 멍해집니다. 우리는 매일 1981년의 어떤 사람의 설계 결정을 손끝으로 만지고 있는 셈입니다.

셋째, *접근성은 보존이 아니다*. 자료를 모아 두는 것과 그 자료가 *지금 이 순간 부팅되도록* 만드는 것 사이에는, 우리 생각보다 훨씬 깊은 골짜기가 있습니다. 그 골짜기를 메우는 일은 *조용한 시간 노동*입니다. 결과물은 화려해 보이지만, 과정은 거의 보이지 않습니다.

저는 이 박물관을 둘러보며 — *기록을 보관하는 일*과 *기록을 살아 있게 만드는 일* 사이의 거리를 새삼 느꼈습니다. 글을 쓰는 사람의 일도 어쩌면 비슷한 종류라고, 그렇게 혼잣말 하며 박물관을 나섭니다. 지난 시대의 화면을 살아 있게 만드는 일과, 지난 시대의 사고를 살아 있게 만드는 일은 — 결국 같은 종류의 노동인지도 모르겠습니다.

문은 언제든 열려 있다고 합니다. 들러 보고 싶으시면 [virtualosmuseum.org](https://virtualosmuseum.org/)로 가시면 됩니다. 큐레이터의 노동에 한 잔 보태고 싶으시면 [Patreon](https://www.patreon.com/andreww591) 페이지가 입구 옆에 단정히 놓여 있고요.

[^1]: Andrew Warkentin, ["The Virtual OS Museum"](https://virtualosmuseum.org/) — 박물관 공식 사이트. 본문 직접 인용은 사이트의 *"Why this exists"* 섹션을 옮겨 다듬은 것이며, 통계 수치(250+ 플랫폼·570+ OS·1700+ 설치본·1948–현재)는 *"By the Numbers"* 섹션에서 확인할 수 있습니다.

[^2]: Andrew Warkentin, ["I've released a virtual museum with nearly every OS you can think of..."](https://andreww591.blogspot.com/2026/05/ive-released-virtual-museum-with-nearly.html) — *Andrew's OS Lab* 블로그, 2026-05-19. 자기 소개 문구(*OS/emulator developer and OS historian*), UX/RT와 박물관 출시 지연의 맥락, 그리고 본문에 인용한 자기 평가(*severely crippling tendency to stay quiet*)가 모두 이 글에 함께 놓여 있습니다.

[^3]: Andrew Warkentin, ["QNX Neutrino 6.1 (2001) — Widely successful but underappreciated outside embedded (part 2)"](https://andreww591.blogspot.com/2024/01/qnx-neutrino-61-2001-widely-successful_3.html) — *Andrew's OS Lab* 블로그, 2024-01-03. *Photon MicroGUI* 개념과 마이크로커널 철학이 GUI 계층까지 확장된 방식을 인스톨러 화면부터 차례로 짚어 가는 두 부분짜리 글의 후편입니다.
