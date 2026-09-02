---
title: "LiteReality-Agent: 상호작용 가능한 3D 실내 씬 재구성 에이전트"
date: 2026-08-09T13:30:00+09:00
tags: ["코딩 에이전트", "3D 재구성", "LiDAR", "오픈소스"]
categories: ["에이전트와 코딩"]
summary: "아이폰 LiDAR 스캔 한 번을 편집 가능한 3D 실내 씬으로 바꾸는 오픈소스 에이전트 시스템. 씬 전체를 하나의 파이썬 프로그램으로 두고, 에이전트가 raw 메시가 아니라 코드를 고쳐 가며 실제 촬영본에 맞춰 나간다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/teaser.jpg"
  alt: "LiteReality-Agent 티저. 실내 스캔이 편집 가능한 3D 씬으로 재구성된다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/teaser.jpg"
---

## 3줄 요약

1. 케임브리지·임페리얼 칼리지 연구진이 공개한 **LiteReality-Agent**는 아이폰·아이패드 LiDAR 스캔 한 번을 상호작용 가능한 실내 3D 씬으로 재구성하는 오픈소스 엔드투엔드 에이전트 시스템이다.
2. 핵심은 씬 전체를 하나의 파이썬 프로그램(`Room.py`)으로 표현한다는 점이다. 에이전트는 메시를 직접 주무르지 않고 코드를 편집하며, 렌더링 결과를 실제 촬영본과 대조해 품질 검증(QC)을 통과할 때까지 고쳐 나간다.
3. 씬이 곧 프로그램이라 평문 요청이 그대로 코드 편집이 된다. 리텍스처링, 가구 재배치, 데코, 세그멘테이션·깊이·노멀·알베도 같은 intrinsics 무료 렌더까지 같은 파이프라인에서 나온다.

## 무엇을 만들었나

LiteReality-Agent는 "방을 한 번 스캔하면 그래픽스에 바로 쓸 수 있는 씬이 나온다"를 목표로 한 도구다. 아이폰이나 아이패드로 방을 걸어 다니며 찍으면, 전용 iOS 스캐너 앱이 하나의 번들을 내보낸다. 그 번들에는 posed RGB 프레임, LiDAR 깊이, ARKit 카메라 포즈, 그리고 RoomPlan 레이아웃이 함께 담긴다. 파이프라인이 필요로 하는 입력이 이 한 묶음에 다 들어 있다.

저자는 Zhening Huang과 Yueyan Li(공동 1저자)를 비롯해 Johnathan Chiu, Xiaoyang Lyu, Matt Zhou, Yuxin Yao, Joan Lasenby, Shangzhe Wu 여덟 명이다. 소속은 케임브리지 대학교, 임페리얼 칼리지 런던, 그리고 독립 연구자다. 기술 보고서는 아직 공개 전(BibTeX 기준 2026년 예정)이며, 프로젝트 페이지와 GitHub 저장소, iOS 앱이 먼저 공개됐다.

## 파이프라인은 결정론과 에이전트의 하이브리드

전체 흐름은 다섯 단계다. 앞쪽은 결정론적으로 뼈대를 세우고, 뒤쪽은 에이전트가 붙여 나가는 구조다.

| 단계 | 종류 | 하는 일 |
|---|---|---|
| 입력 | Scan | iOS 앱이 내보낸 posed RGB와 LiDAR |
| 초기화 | 결정론 | 벽·개구부·카메라를 빈 방으로 복원 |
| 저작 | 에이전트 루프 | `Room.py`를 편집하며 촬영본에 맞춰 다듬는다 |
| 게이트 | QC | 출하 전 자동 품질 검사 |
| 출력 | Scene | 사실적이고 상호작용 가능하며 아티큘레이션이 있는 씬 |

빈 방 복원까지는 결정론적 패스가 맡는다. 벽과 문·창 같은 개구부, 카메라 위치가 스캔으로부터 다시 세워진다. 그 위에서부터 에이전트가 등장해 방을 채우고 다듬는다.

## 씬이 곧 프로그램이다

이 시스템의 중심 결정은 씬 표현 방식이다. 지오메트리와 머티리얼, 아티큘레이션이 전부 하나의 파이썬 프로그램으로 기술된다. 에이전트는 raw 메시를 편집하지 않고 코드의 줄을 고친다.

이 선택이 주는 이점은 세 가지로 정리된다. 모든 변경이 사람이 읽을 수 있고(legible), 다시 실행해 재현할 수 있으며(replayable), Blender나 glTF, 시뮬레이터로 곧장 export된다. 씬을 편집한다는 것이 곧 프로그램을 편집한다는 뜻이 되면서, 결과물이 검은 상자가 아니라 열어 볼 수 있는 산출물이 된다.

## 저작 루프와 도구

에이전트의 작업은 하나의 순환으로 돈다.

> edit → render → compare → critique ↻

코드를 고치고, 렌더링하고, 실제 촬영본과 비교하고, 스스로 비평한 뒤 다시 고친다. 이 루프를 QC가 통과할 때까지 반복한다. 에이전트가 쓰는 도구는 렌더링과 촬영본을 나란히 대조하는 `render_and_compare`, 시점을 고르는 `select_view`, 격자 뷰 `grid`, 실제 머티리얼을 가져오는 `fetch_materials`, 자기 비평 `critic`, 그리고 `compile`이다. 여기에 일반적인 코딩 도구인 bash, glob, read, edit이 더해진다. 3D 저작 전용 도구와 코드 편집 도구를 한 손에 쥔 셈이다.

## 응용 네 가지

씬이 프로그램이기 때문에, 평문으로 던진 요청 하나가 코드 편집으로 번역된다. 아래 네 클립은 모두 동일하게 저작된 사무실 하나를 대상으로 한다.

**텍스트 기반 편집.** 타이핑한 요청으로 벽과 바닥을 다시 텍스처링한다. 노출 벽돌, 월넛 패널, 세이지 그린 페인트 같은 지시가 그대로 반영되며, 이때 지오메트리는 전혀 움직이지 않는다.

![텍스트 요청으로 벽과 바닥을 리텍스처링한다.](https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/app-text.jpg)

**재배치.** 프롬프트로 방 배치를 다시 짠다. 이때도 모든 물체가 바닥에 붙어 있고 서로 충돌하지 않으며, 아무것도 삭제되지 않는다.

![프롬프트로 가구를 재배치한다. 충돌 없이 바닥에 붙어 있다.](https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/app-rearrange.jpg)

**데코.** 에이전트가 실제 에셋을 가져오고 절차적 지오메트리를 직접 작성한다. 펜던트 조명, 배너, 파티 세팅 같은 소품을 문이 열리는 반경을 피해 배치한다.

![실제 에셋과 절차적 지오메트리로 방을 꾸민다.](https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/app-decor.jpg)

**Intrinsics.** 완전히 저작된 씬은 intrinsics를 공짜로 렌더한다. 같은 카메라에서 픽셀 단위로 정확한 세그멘테이션, 깊이, 노멀, 알베도가 나온다. 학습 데이터가 필요한 쪽에서 특히 반가운 대목이다.

![저작된 씬에서 세그멘테이션·깊이·노멀·알베도를 무료로 렌더한다.](https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/app-intrinsics.jpg)

## 갤러리와 뷰어

프로젝트 페이지는 재구성한 씬들을 브라우저에서 직접 걸어 다닐 수 있게 공개했다. Studio Office, Private Office, Boardroom, Meeting Room, Seminar Room, Kitchenette, Garden Room, Bedroom, Library 같은 사무·주거 공간이 목록에 있다. 씬을 클릭하면 궤도 회전, 그룹 분리, 렌더링과 실제 촬영본 비교, 1인칭 워크스루가 모두 브라우저 안에서 된다.

![Studio Office. 실제 촬영본과 재구성 결과를 대조한다.](https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/studio-office.jpg)

![The Library. 선반과 책이 있는 공간의 재구성.](https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/gallery-library.jpg)

![The Garden Room. 유리창이 있는 선룸.](https://img.seosoyoung.eiaserinnys.me/images/litereality-agent/gallery-garden-room.jpg)

## 스캐너 앱

캡처 프론트엔드인 iOS·iPadOS LiDAR 스캐너 앱 **LiteReality**는 앱스토어에 올라와 있다. 방을 걸어 다니며 찍으면 파이프라인이 필요로 하는 모든 것을 한 번에 내보낸다는 점이 이 앱의 역할이다. 재구성 도구와 캡처 도구를 함께 배포해, 스캔부터 편집 가능한 씬까지의 경로를 하나로 이었다.

## 관련 연구

이 프로젝트는 두 갈래의 선행 작업 위에 서 있다. 하나는 **LiteReality**(원조 파이프라인)로, 평범한 휴대폰 스캔을 그래픽스에 쓸 수 있는 아티큘레이션 씬으로 바꾸는 작업이며 이번 시스템이 확장한 토대다. 다른 하나는 **Articraft**로, 코딩 에이전트가 LLM 친화적인 SDK를 상대로 프로그램을 작성해 텍스트로부터 시뮬레이션 가능한 아티큘레이션 에셋을 만들어 내는 연구다. 코드로 3D를 저작한다는 발상이 이 계보에서 이어진다.

## 가장 눈여겨본 것

가장 눈여겨본 것은 "씬을 코드로 둔다"는 한 수가 응용을 갈라 놓는 방식이다. 리텍스처링, 재배치, 데코, intrinsics 렌더는 언뜻 서로 다른 기능처럼 보이지만, 이 시스템에서는 전부 같은 뿌리에서 나온다. 씬이 편집 가능한 프로그램이니, 사용자의 평문 요청을 코드 변경으로 옮기기만 하면 네 가지가 모두 같은 파이프라인의 파생이 된다. 별도의 전용 모듈을 넷 만드는 대신, 표현 방식 하나를 바꿔 네 문제를 동시에 여는 설계다.

코드로 두었기에 딸려 오는 것도 분명하다. 사람이 읽을 수 있고, 다시 돌려 재현할 수 있고, 표준 포맷으로 곧장 내보낼 수 있다. 재구성이라는 지각 문제를 "코드를 고쳐 촬영본에 맞추는" 반복 문제로 바꿔 놓은 셈이라, 에이전트가 잘하는 자리로 문제를 끌어온 접근으로 읽힌다.

## 출처

LiteReality-Agent: An Agentic System for Interactable 3D Indoor Scene Reconstruction. Zhening Huang, Yueyan Li 외 6인 (University of Cambridge · Imperial College London). 기술 보고서 공개 예정(2026).

원문: <https://litereality.github.io/Litereality-agent-site/>
GitHub: <https://github.com/LiteReality/LiteReality-Agent/>

본 다이제스트의 이미지는 프로젝트 페이지의 데모 클립 포스터와 갤러리 캡처를 인용했다.
