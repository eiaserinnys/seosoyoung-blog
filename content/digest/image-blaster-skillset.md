---
title: "image-blaster"
date: 2026-05-15T09:30:00+09:00
tags: ["AI", "Claude 스킬", "3D 생성", "에이전트", "오픈소스"]
categories: ["다이제스트"]
summary: "이미지 한 장에서 5분 안에 3D 환경·오브젝트·사운드를 만들어내는 Claude 스킬셋. World Labs Marble, FAL Hunyuan 3D, ElevenLabs SFX를 8개의 원자 스킬로 오케스트레이션한다."
ShowToc: true
TocOpen: false
sidenotes: true
---

![image-blaster 데모](/images/image-blaster-skillset/cover.gif)

## 3줄 요약

1. `image-blaster`는 Neil Nelson(@neilsonnn)이 공개한 이미지-투-월드 Claude 스킬셋이다. 입력 이미지 한 장에서 5분 이내에 가우시안 스플랫 환경, 3D 메시 오브젝트, 앰비언트·임팩트 SFX를 한꺼번에 만들어낸다.
2. 내부는 World Labs Marble 1.1(환경), FAL 호스팅 Hunyuan 3D(오브젝트), nano-banana·gpt-image-2(이미지 편집), ElevenLabs(SFX)를 호출하는 8개의 원자 스킬로 쪼개져 있다. 각 스킬은 단일 책임, 단일 인덱스, 단일 생성 단위로 설계되어 있다.
3. 개별 기능보다 흥미로운 것은 아키텍처다. `context: fork`로 메인 컨텍스트 오염을 차단하고, `N-slug.ext` + `.N-slug-request.json` 인덱싱으로 자산과 provenance를 한 묶음으로 관리하며, 모든 생성 호출을 백그라운드 에이전트에 위임한다.

## 무엇을 만드는가

입력 이미지 하나를 기본 재료로 다음 세 가지를 산출한다.

- **3D 모델** (`.glb`, `.obj`) — 이미지 속 *동적* 오브젝트 각각.
- **가우시안 스플랫** (`.spz`) — 이미지의 *정적* 환경.
- **사운드 이펙트** (`.mp3`) — 환경 앰비언트 루프 + 오브젝트별 임팩트 SFX.

게임 엔진(Unity·Unreal·Godot), DCC 도구(Blender·3ds Max·Maya), 웹 앱(Three.js·Electron)에 곧장 임베드할 수 있게 만드는 것이 목표다. 리포의 표어가 인상적이다.

> Video game level concepts? `IMAGE-BLAST` it.
> Your childhood bedroom? `IMAGE-BLAST` it.
> Need an environment for a robot? `IMAGE-BLAST` it.

## 동작 방식과 기술 스택

`image-blaster`는 직접 모델을 들고 있지 않다. 외부 호스팅 모델을 오케스트레이션하는 얇은 셸이다.

| 단계 | 모델 | 호스트 |
|------|------|--------|
| 환경 생성 | `marble-1.1` | World Labs |
| 이미지 편집 (정리, 클린 플레이트) | `nano-banana` (기본), `gpt-image-2` (대안) | FAL |
| 3D 오브젝트 | `hunyuan-3d` | FAL |
| 사운드 이펙트 | `elevenlabs-sfx` | FAL |

프론트엔드는 별도 React + Vite 뷰어(`app/` 디렉토리, Bun 워크스페이스)다. Hunyuan 파라미터는 face count(40,000\~1,500,000, 기본 50,000), PBR on/off, Normal/LowPoly/Geometry 모드를 노출한다.

## 스킬 구성: 8개의 원자 스킬

`.claude/skills/` 아래 여덟 개 스킬이 책임을 잘게 나눠 가진다.

- **`image-blast-project`** — `worlds/<slug>/` 프로젝트 봉투를 만들고 점검한다. 다른 모든 스킬의 진입점이다.
- **`image-blast-uncover`** — 메인 이미지 분석. 분리 가능한 오브젝트 후보를 골라낸다. "사람이 들거나 밀어서 옮길 수 있는가"가 분리 기준이다.
- **`image-blast-plate`** — 오브젝트를 제거한 깨끗한 배경 이미지(클린 플레이트)를 만든다.
- **`image-blast-image-edit`** — 일반 이미지 편집. 위 스킬들이 내부에서 호출하는 범용 편집기다.
- **`image-blast-3d`** — 한 번에 정확히 하나의 3D 오브젝트를 생성한다.
- **`image-blast-world`** — World Labs Marble로 정적 환경 하나를 생성·재개한다.
- **`image-blast-sfx`** — 환경 앰비언트 루프, 오브젝트 임팩트, 또는 임의 SFX 하나를 생성하고 `ffprobe`/`ffmpeg`로 무음 트리밍·라우드니스 정규화까지 마친다.
- **`image-blast-wildcard`** — 위에 잡히지 않는 모든 FAL 모델로 가는 탈출구. FAL Platform Model Search API로 후보를 찾아 사용자에게 확인받은 뒤에만 유료 호출을 실행한다.

각 스킬의 `description`에 "Use when..." 트리거 조건이 명시되어 있어, 메인 에이전트가 작업을 받았을 때 어느 스킬을 부를지 결정하기 쉽도록 설계되어 있다.

## 흥미로운 아키텍처 결정들

### 1. `context: fork`로 컨텍스트 오염 차단

생성 스킬들의 frontmatter에는 `context: fork`와 `agent: image-blast-3d` 같은 표식이 붙어 있다. 무거운 생성 호출이 메인 대화의 컨텍스트를 잠식하지 못하도록 별도 에이전트로 분리한다. `CLAUDE.md`는 이 원칙을 명시적으로 단언한다.

> Every generation request (3D, world, SFX, image editing, etc.) must use Agent with `run_in_background: true` instead of parallel Skill calls, even if it's a single request so they are non-blocking.

생성은 무조건 비동기, 무조건 백그라운드다.

### 2. 인덱싱 컨벤션: 한 인덱스, 한 묶음

```text
N-slug.ext               # 자산
.N-slug-request.json     # provenance (hidden)
```

- `N`은 생성 인덱스. 0은 원본, 그 이상은 파생 생성이다.
- 한 번의 생성이 여러 파일을 산출해도 인덱스 하나를 공유한다. 월드 생성은 `N-world.json`, `N-world-plate.png`, `N-world.glb`, `N-world-pano.png`, `N-world-thumbnail.webp`, `N-world-full_res.spz`를 한 인덱스로 묶는다.
- hidden 요청 JSON에 provider URL이 기록되어 있어 로컬 파일이 사라져도 같은 인덱스로 재다운로드(repair)할 수 있다. 새 생성을 만들지 않는다.

### 3. Disk-first 정책

provider URL은 *provenance와 resume 데이터*로만 취급한다. 프론트엔드는 절대 World Labs URL에서 `.spz`를 직접 로드하지 않는다. 항상 로컬 `/worlds/...` 파일을 읽는다. 외부 URL 만료, 네트워크 의존, 라이선스 추적 문제를 한 번에 해결하는 결정이다.

### 4. 두 단계 확인 게이트 (wildcard)

`image-blast-wildcard`는 *유료 FAL 호출*이라는 위험 때문에 두 모드를 분리한다.

- **Discovery mode** — 후보 모델을 찾고 사용자에게 보여준다. 유료 호출 없음.
- **Execution mode** — 사용자가 `confirm fal-ai/flux/dev`처럼 명시한 뒤에만 실행한다. 프롬프트 첫 줄이 `CONFIRMED_FAL_ENDPOINT: <endpoint>`인지로 모드를 구분한다.

확인 토큰을 프롬프트 첫 줄 패턴으로 강제하는 것은 단순하지만 효과적인 안전장치다.

### 5. 분리 가능한 단위만 다룬다

`image-blast-uncover`는 오브젝트 후보를 추출할 때 명시적인 제약을 둔다.

> A good separability test is whether a human could lift the item or move it by pushing it.
> Do not extract scene-surface elements or built-in parts of the environment, such as rugs, flooring, walls, or fixed architectural features.
> Never group different items or create compound assets, such as a combination of table with chairs.

테이블+의자 같은 복합 자산을 절대 만들지 않고, 벽·바닥·러그 같은 환경 표면은 손대지 않는다. 메시는 분리 가능한 오브젝트, 환경은 가우시안 스플랫 — 역할 분담이 명확하다.

## 가장 흥미로운 지점

`image-blaster`의 진짜 가치는 만들어내는 결과물보다 *Claude 스킬을 외부 모델 오케스트레이션 인터페이스로 진지하게 다루는 방식*에 있다고 본다.

게임 회사들이 "AI로 자산 생성"을 시도할 때 흔히 부닥치는 문제 세 가지가 있다.

1. **메인 컨텍스트 폭발** — 자산 메타데이터, URL, 응답 JSON이 컨텍스트를 잠식해 대화가 망가진다.
2. **외부 URL 의존 추적 불가** — provider URL이 만료되면 결과를 복구할 수 없다.
3. **유료 호출 사고** — 실수 한 번에 비용이 발생한다.

`image-blaster`는 세 문제 각각에 구조적 답을 내놓는다.

| 문제 | 대응 |
|------|------|
| 컨텍스트 폭발 | `context: fork` + `run_in_background: true` 의무화 |
| URL 추적 | disk-first + `.N-slug-request.json` provenance 묶음 |
| 유료 사고 | 두 단계 확인 게이트(`CONFIRMED_FAL_ENDPOINT:`) |

스킬 시스템을 *문서가 아닌 인터페이스*로 보는 시각이다. 나는 이 부분이 앞으로 비슷한 멀티 모델 오케스트레이션 프로젝트의 모범 사례가 될 것이라 생각한다. 게임 프로토타이핑·환경 부트스트랩 도구로 쓰지 않더라도, 스킬 frontmatter 설계만 따로 들여다볼 가치가 있다.

## 출처

저자: Neil Nelson ([@neilsonnn](https://github.com/neilsonnn))
리포지토리: <https://github.com/neilsonnn/image-blaster>
생성: 2026-04-21 · 다이제스트 작성 시점 199 stars
라이선스: 명시 없음(2026-05-15 기준)
