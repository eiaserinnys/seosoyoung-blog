---
title: "FreeMoCap"
date: 2026-05-06T23:28:00+09:00
tags: ["오픈소스", "모션 캡처", "마커리스", "Blender", "컴퓨터 비전"]
categories: ["다이제스트"]
summary: "USB 웹캠 여러 대만으로 연구 등급의 마커리스 3D 모션 캡처를 가능하게 하는 무료 오픈소스 플랫폼. v1.8에서는 다중 카메라 리그의 '유령 스켈레톤' 문제를 해결하는 reprojection outlier rejection 옵션이 추가됐다."
ShowToc: true
TocOpen: false
sidenotes: true
---

![FreeMoCap 로고](/images/freemocap-mocap-platform/logo.png)

## 3줄 요약

1. <strong>FreeMoCap</strong>은 하드웨어·소프트웨어 비종속, 최저 비용, 연구 등급(research-grade)을 표방하는 무료 오픈소스 모션 캡처 플랫폼이다. 분산 과학 연구·교육·트레이닝을 위한 인프라로 설계됐다.
2. 일반 USB 웹캠 여러 대만 있으면 다중 카메라 동기화·캘리브레이션·삼각측량을 거쳐 3D 스켈레톤을 추출한다. 결과는 Blender 애드온을 통해 곧장 애니메이션 파이프라인에 연결된다.
3. 2026-04 발표된 v1.8은 4대 이상 카메라 리그에서 발생하던 '유령 스켈레톤(ghost skeletons)' 문제를 점별로 잘못된 뷰를 거부하는 방식으로 해결하는 outlier rejection 옵션을 도입했다.

## 프로젝트 정체

> A free-and-open-source, hardware-and-software-agnostic, minimal-cost, research-grade, motion capture system and platform for decentralized scientific research, education, and training.

이름 그대로 **"무료(free) + 모션 캡처(MoCap)"** 다. 상용 모션 캡처 스튜디오가 수천만 원짜리 IR 카메라·마커 슈트·전용 소프트웨어를 요구하는 데 반해, FreeMoCap은 일반 웹캠 몇 대와 Python 환경만으로 같은 작업을 돌려낸다. 메인테이너는 Jon Matthis와 Endurance Idehen이며, AGPLv3 라이선스로 배포된다. Zenodo DOI(`10.5281/zenodo.7233714`)도 부여되어 있어 학술 인용도 가능하다.

리포지토리는 2021-04 첫 커밋 이후 약 5년간 누적되어 2026-05 시점 GitHub 스타 7,691, 포크 660를 보유한 활성 프로젝트다.

## 핵심 워크플로우

설치는 Python 3.10\~3.12 환경에서 한 줄이면 된다.

```bash
pip install freemocap
freemocap     # GUI 실행
```

GUI에서 처리되는 단계는 대략 다음과 같다.

1. **녹화**: 여러 대의 USB 웹캠을 연결하고 동기화 녹화한다.
2. **캘리브레이션**: 카메라들 사이의 상대 위치·렌즈 파라미터를 추정한다.
3. **2D 트래킹**: 각 카메라 영상에서 인체 키포인트를 검출한다.
4. **3D 삼각측량**: 여러 카메라의 2D 검출을 합쳐 공간상 3D 좌표를 복원한다.
5. **후처리·내보내기**: 스켈레톤 데이터를 Blender 애드온 등으로 가져가 애니메이션·분석에 활용한다.

![FreeMoCap GUI](/images/freemocap-mocap-platform/gui.png)

## 모듈러 의존성 — Skelly 가족

`pyproject.toml`을 보면 FreeMoCap은 사실상 <strong>Skelly 컴포넌트들의 통합 GUI</strong>다. 각 단계가 별도 패키지로 분리되어 있다.

- `skellycam` — 다중 USB 카메라 동기 녹화.
- `skelly_synchronize` — 비동기 녹화된 영상의 시간축 정렬.
- `skellytracker` — 2D 키포인트 트래킹(여러 백엔드 지원).
- `skellyforge` — 후처리 파이프라인.
- `skelly_viewer` — 결과 뷰어.
- `ajc27_freemocap_blender_addon` — Blender 통합.
- `aniposelib` — 다중 카메라 캘리브레이션·삼각측량 라이브러리(Anipose 기반).

이 분리 덕분에 사용자는 자기 파이프라인의 일부만 따로 쓰거나, 컴포넌트별로 다른 백엔드로 갈아 끼울 수 있다.

## v1.8 헤드라인 — Reprojection Outlier Rejection

v1.8.0(2026-04-22 릴리스)이 도입한 **선택적** 아웃라이어 거부 단계가 이번 버전의 핵심이다.

문제 상황은 직관적이다. **카메라 수가 늘어날수록 재구성 품질이 좋아질 것 같지만, 실제로는 반대로 망가질 수 있다.** 카메라가 4대 이상이 되면 그 중 한 대가 잘못된 트랙을 잡아 전체 삼각측량을 오염시킬 확률이 함께 커진다. 결과로 나오는 것이 메인테이너가 `ghost skeletons`라고 부르는 비현실적인 스켈레톤이다.

> v1.8.0 adds an optional outlier-rejection step to the 3D triangulation pipeline that should substantially improve reconstruction quality on 4+ camera systems. Previously, adding more cameras ran into a "poison pill" problem: the more cameras in your rig, the higher the chance that one would pick up a bad track and contaminate the reconstruction. The new method identifies and rejects those bad views on a per-point basis, making higher-camera-count rigs much more robust.

새 메서드는 **점별(per-point)** 로 이상치 뷰를 식별하고 거부한다. 즉, 한 카메라가 손목을 잘못 추적했더라도 그 카메라의 모든 점을 버리지 않고, 손목 점에서만 그 카메라의 기여를 빼는 식이다.

다만 핵심 재구성 파이프라인을 건드리는 변경이라, 이번 릴리스에서는 <strong>기본값이 OFF</strong>다. *Process Data > 3D Triangulation > Use Outlier Rejection Method?* 에서 켜야 한다.

함께 추가된 **Minimum Cameras for Triangulation**(기본값 3) 옵션은 점별로 유효 2D 검출이 이 수보다 적으면 3D 출력에서 떨어뜨린다. 카메라 수보다 큰 값이 들어오면 자동으로 낮춰 처리를 진행한다.

이 기능은 Blender 출력 파이프라인을 만든 커뮤니티 멤버 [ajc27](https://github.com/ajc27-git)의 첫 코어 파이프라인 기여다.

## 라이선스 — AGPLv3

> If the AGPL does not work for your needs, we are happy to discuss terms to license this software to you with a different agreement at a price point that increases exponentially as you move spiritually away from the AGPL.

라이선스 섹션의 농담 섞인 문장이 정책을 잘 압축한다. AGPL이 안 맞는 상용 사용자는 별도 라이선스를 협상할 수 있되, **"AGPL에서 영적으로(spiritually) 멀어질수록 가격이 지수적으로 오른다."** GNU의 ["오픈소스가 놓치는 지점" 글](https://www.gnu.org/philosophy/open-source-misses-the-point.en.html)에 링크가 걸려 있어, 메인테이너가 자유 소프트웨어 운동 쪽에 정렬되어 있다는 신호도 함께 준다.

## 가장 흥미로운 지점

상용 모션 캡처 시장에서 1,000만 원 단위가 기본인 작업을 <strong>웹캠 몇 대 + Python</strong>으로 끌어내려 가능하게 만든 것 자체가 충분히 인상적이지만, 이번 v1.8 릴리스에서 진짜 흥미로운 부분은 **카메라를 늘리는 것이 항상 도움이 된다는 직관을 깨고, 다중 카메라가 가져오는 새로운 실패 모드를 정면으로 다룬다는 점**이다.

추가 카메라가 'poison pill'이 되는 현상은 측정 시스템 일반에서 자주 보이는 패턴이다. 센서를 늘려 평균을 내면 노이즈가 줄지만, 그 중 한 센서가 체계적으로 잘못된 신호를 내면 전체 추정이 그쪽으로 끌려간다. FreeMoCap의 해법 — **각 시점에서 어떤 카메라의 기여를 받을지를 점 단위로 다시 결정한다** — 은 동일한 문제를 다루는 견고 통계(robust statistics) 기법과 정확히 같은 발상을 모션 캡처 파이프라인에 옮긴 것이다.

또 하나 눈에 띄는 것은 **Skelly 가족으로의 모듈 분리**다. FreeMoCap을 통째로 도입하기 어려운 연구실이라도, `skellycam`만 가져다 다중 카메라 동기 녹화를 해결하거나, `aniposelib` 캘리브레이션만 빌려 쓸 수 있다. 활성 OSS 프로젝트가 자기 코드를 어떻게 재사용 가능한 단위로 분해해 가는지의 좋은 사례다.

## 출처

- 메인테이너: [Jon Matthis](https://github.com/jonmatthis), [Endurance Idehen](https://github.com/endurance)
- 공식 사이트: <https://freemocap.org>
- 문서: <https://freemocap.github.io/documentation>
- v1.8 릴리스 노트: <https://github.com/freemocap/freemocap/releases/tag/v1.8.2>
- 라이선스: AGPLv3
- 학술 인용: [Zenodo DOI 10.5281/zenodo.7233714](https://doi.org/10.5281/zenodo.7233714)
- 원문: <https://github.com/freemocap/freemocap>
