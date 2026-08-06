---
title: "Blender Camera Controller v1.0.0 — 스마트폰을 실제 카메라처럼 쓰는 Blender 애드온"
date: 2026-05-13T11:00:00+09:00
tags: ["소프트웨어", "Blender", "3DCG", "HCI", "스마트폰"]
categories: ["창작과 문화"]
summary: "Android 스마트폰을 카메라처럼 들고 흔들면 Blender 안 카메라가 따라 움직이는 애드온. v1.0.0에서 Google Play 배포·World Tracking·Streaming이 개선됐다. 기능보다 흥미로운 건, 스마트폰을 PC 응용프로그램의 외부 입력 장치로 끌어들이는 발상이다."
ShowToc: true
TocOpen: false
sidenotes: true
---

![Blender Camera Controller v1.0.0](/images/blender-camera-controller-v1/cover.jpg)

## 3줄 요약

1. *Blender Camera Controller*는 Android 스마트폰의 센서와 화면을 그대로 Blender 카메라 컨트롤러로 쓰는 애드온이다.[^gumroad-blender]
2. v1.0.0에서 Google Play Store 배포가 시작됐고, World Tracking·Streaming·키프레임 스무딩이 개선됐다.[^google-play]
3. 흥미로운 지점은 *기능 자체*가 아니라, 모두가 가진 스마트폰의 자이로/제스처를 PC 응용프로그램의 외부 입력 장치로 끌어들이는 *발상*이다.

## 영상

{{< youtube H2XPE1L_SXs >}}[^youtube-watch]

## 무엇을 하는 애드온인가

Android 스마트폰을 실제 카메라처럼 들고 움직이면, 그 센서 정보가 PC의 Blender 카메라에 실시간으로 반영된다. 손에서 자연스럽게 발생하는 흔들림, 회전, 전후좌우 이동이 그대로 Blender 씬의 카메라 움직임으로 들어간다. 결과적으로 *카메라 워크를 손으로 연기*해서 애니메이션 키프레임을 만드는 워크플로우가 가능해진다.

스마트폰 화면에는 Blender 뷰포트가 스트리밍되어, 사용자는 스마트폰을 *모니터 겸 뷰파인더*로 들고 촬영하듯 카메라 동선을 잡는다.

## v1.0.0 주요 변경점

- **Google Play Store 배포 시작.** 기존 Gumroad 영구 라이선스도 유지되며, Play Store판에서는 Google 경유 구독을 새로 지원한다.
- **World Tracking 개선.** 회전뿐 아니라 스마트폰의 *전후좌우 이동* 위치까지 추적해, 걷기 촬영 같은 실제 카메라 워크를 재현할 수 있다. 연결 화면에서 사용 중인 단말이 World Tracking·회전 센서에 대응하는지 확인할 수 있다.
- **Streaming 강화.** 스마트폰에서 Blender 카메라 영상을 보는 기능이 더 낮은 지연·더 높은 화질로 동작한다.
- **Blender 측 보강.** AutoSmooth 키프레임에 Butterworth·Gaussian Smooth가 추가됐고, Crop Window 정밀도가 개선됐다. 다수의 버그 수정도 포함된다.

## 가격

- 무료판: Android 앱 + 데모 애드온으로 연결·동작 확인만 가능.
- 유료판: $9.99 — 영구 라이선스로 전 기능 사용. Play Store판은 별도로 구독 옵션 제공.

## 가장 흥미로운 지점

이 도구 자체는 *Blender를 쓰는 사람을 위한* 비교적 좁은 시장의 애드온이다. 그런데 그 안에 담긴 발상은 좁지 않다.

내가 흥미롭게 본 건, <strong>사용자가 이미 손에 들고 있는 스마트폰을 PC 응용프로그램의 외부 입력 장치로 끌어들였다</strong>는 부분이다. 자이로, 가속도, 터치, 핀치 확대/축소, 카메라 — 정밀한 공간·제스처 입력을 위한 거의 모든 센서가 *추가 하드웨어 구매 없이* 사용자 손에 이미 있다. 전통적으로 이런 정밀 공간 입력은 SpaceMouse나 트래커 같은 별도 장치에 의존했지만, 그 자리를 스마트폰이 충분히 대체할 수 있다는 사실을 이 애드온은 구체적으로 보여 준다.

3D 카메라 워크에 그칠 이유는 없다. 같은 패턴은 음악 작업의 컨트롤러, 프레젠테이션의 포인터·줌, 영상 편집의 점프 컨트롤, 3D 뷰어의 오비트 조작 등 *공간적/연속적 제어가 필요한 모든 PC 도구*로 확장될 수 있다. 핵심은 "스마트폰을 보조 디스플레이로 쓰는 것"이 아니라 "스마트폰을 *센서 다발*로 다시 정의하는 것"이다.

비슷한 발상이 일반화되면, PC 응용프로그램의 입력 모델은 "키보드+마우스 + (옵션) 게임패드"의 삼각형에서, "키보드+마우스 + 스마트폰 센서 입력"의 새 삼각형으로 옮겨갈 여지가 있다. 도구 디자이너 입장에서는, 우리 도구의 어떤 작업이 *손의 회전·이동·제스처*로 더 자연스러워질지 다시 묻게 만드는 사례다.

## 출처

- 원문: <https://modelinghappy.com/archives/68642>
- 매체: MODELING HAPPY (3DCG 정보 사이트, 2026년 5월 13일 게재)

[^gumroad-blender]: Gumroad: <https://blender-addons.gumroad.com/l/blender_camera_controller_addon>
[^google-play]: Google Play Store: <https://play.google.com/store/apps/details?id=com.wpm.blender_camera_controller>
[^youtube-watch]: 영상: <https://www.youtube.com/watch?v=H2XPE1L_SXs>
