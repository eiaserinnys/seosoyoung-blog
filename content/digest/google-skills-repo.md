---
title: "google/skills — Agent Skills for Google products and technologies"
date: 2026-05-16T03:50:00+09:00
tags: ["AI 에이전트", "Anthropic", "Google Cloud", "Agent Skills", "오픈소스"]
categories: ["다이제스트"]
summary: "Google이 Anthropic의 Agent Skills 패턴을 채택해 Google Cloud용 13개 스킬을 Apache-2.0으로 공개했다. skills.sh라는 패키지 매니저 레이어와 agentskills.io라는 벤더 중립 사이트가 함께 등장해, Skills가 한 벤더의 컨벤션에서 공용 표준으로 옮겨가는 신호로 읽힌다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Google이 2026년 3월 31일 공개한 `google/skills` 리포는 Anthropic이 정의한 Agent Skills 패턴을 채택해 Google Cloud(BigQuery, Cloud Run, GKE, AlloyDB, Firebase, Gemini API 등)용 스킬 13개를 Apache-2.0으로 묶어 둔 컬렉션이다.[^github-firebase]
2. 별점 8.8k, 포크 660개를 다섯 달 만에 모았고, `npx skills add google/skills`로 설치되는 `skills.sh`라는 패키지 매니저성 레이어와 `agentskills.io`라는 벤더 중립 사이트가 함께 등장했다.
3. 외부 PR은 받지 않고 "Remix & Share"를 권장하는 정책, Firebase를 별도 리포(`firebase/agent-skills`)로 위임한 멀티 리포 구조, gke-basics에서만 시도된 `metadata.author/version` 같은 frontmatter 확장이 함께 보인다.

## 리포의 정체

`google/skills`는 Google 공식 org가 운영하는 Agent Skills 컬렉션이다. README 첫 줄은 한 문장으로 자기 정체를 못 박는다.

> Agent Skills for Google products and technologies, including Google Cloud.

핵심 사실을 표로 옮긴다.

| 항목 | 값 |
|---|---|
| 공개일 | 2026-03-31 |
| 최종 푸시 | 2026-05-15 |
| 라이선스 | Apache-2.0 |
| 별 / 포크 | 8,872 / 660 |
| 릴리스 / 태그 | 없음 (main 직 푸시) |
| 설치 진입점 | `npx skills add google/skills` |
| 카테고리 | `skills/cloud/` 단일, 13개 스킬 |

Anthropic이 Agent Skills를 공식 공개한 지 약 다섯 달 만에 Google이 동참한 사례다. README가 `Agent Skills`를 `agentskills.io/home`으로 링크하고 있다는 점이 의미심장하다 — "Anthropic의 패턴"으로 호명되는 대신, Google이 따라 들어와도 어색하지 않을 **공용 표어**로 옮겨 가려는 의도가 읽힌다.[^agentskills-home]

## 디렉토리 구조 — 세 가지 명명 컨벤션

전체 스킬 13개가 `skills/cloud/` 한 폴더 아래 평평하게 누워 있다. 이름의 접미사를 보면 세 부류로 나뉜다.

| 접미사 | 의미 | 해당 스킬 |
|---|---|---|
| `*-basics` | 제품 입문 — 리소스 생성·관리 절차 | alloydb-basics, bigquery-basics, cloud-run-basics, cloud-sql-basics, firebase-basics, gke-basics |
| `*-recipe-*` | 작업 절차 — 인증·온보딩 등 가로지르는 주제 | google-cloud-recipe-auth, google-cloud-recipe-onboarding |
| `*-waf-*` | Well-Architected Framework 필러 평가 | google-cloud-waf-cost-optimization, google-cloud-waf-reliability, google-cloud-waf-security |

사용자가 "X를 만들어줘"라고 할 때와 "이 워크로드를 평가해줘"라고 할 때 다른 스킬이 매치되도록 의도한 분할로 보인다. `basics`는 실행 절차, `recipe`는 모범 사례 묶음, `waf`는 평가·감사 결의 스킬이다.

나머지 두 스킬(`gemini-api`, `google-cloud-networking-observability`)은 이 컨벤션 바깥에 있다. 한 카테고리에 13개가 모이면 곧 하위 그룹화가 강제될 텐데, 그 압력이 누적되기 직전의 상태다.

## SKILL.md 형식 — Anthropic 스펙 위에 살짝 얹는다

대부분의 스킬은 Anthropic이 정의한 최소 스펙(`name` + `description`)을 그대로 따른다. 다만 두 곳에서 변형이 보인다.

**변형 1 — `gemini-api`**: `compatibility` 키를 추가했다.

> compatibility: Requires active Google Cloud credentials and Agent Platform API enabled.

**변형 2 — `gke-basics`**: 가장 풍부한 frontmatter를 시도한다.

```yaml
name: gke-basics
license: Apache-2.0
metadata:
  author: Google Cloud
  version: "1.0.0"
description: "..."
```

13개 중 12개가 아직 최소 두 필드만 쓰는 가운데, gke-basics 한 곳에서 `license`, `metadata.author`, `metadata.version`을 얹어 본 모양새다. **차세대 컨벤션의 실험장**으로 읽힌다 — 공개 표준화가 진행될수록 출처·버저닝을 명시할 필요가 커지고, 이를 어떤 키 이름으로 박을지 합의가 필요해진다. Google이 먼저 후보를 던지고 있는 셈이다.

## 두 가지 작성 스타일 — 얇은 인덱스 vs 운영 절차서

같은 스펙을 쓰지만 본문의 결은 정반대로 갈린다.

**얇은 인덱스 — `gke-basics`** (57줄)

Quick Start 3줄, 트리거 키워드, 그리고 **레퍼런스 라우팅 표**가 본문 대부분을 차지한다. 무거운 지식은 모두 `references/gke-*.md` 18개 파일에 분산되어 있고, SKILL.md는 그저 "어떤 질문이 들어오면 어느 references로 가야 하는지"를 안내한다. Anthropic이 말한 **progressive disclosure**(필요할 때만 컨텍스트 로드)를 가장 충실히 따르는 모범 사례다. assets/도 5개 매니페스트(default-deny netpol, autopilot golden-path, HPA/VPA, workload-identity pod)를 동봉해 코드 산출물까지 분리한다.

**운영 절차서 — `cloud-run-basics`** (380줄)

반대 결이다. SKILL.md 본문에 gcloud 명령어, IAM 역할 부여 예시, Service/Job/Worker Pool 배포 시나리오까지 직접 포함된다. references/는 보조 역할이고, SKILL.md 자체가 운영 절차서에 가깝다.

같은 리포 안에서 이 두 결이 공존한다는 사실이 흥미롭다. 어느 한쪽이 옳다고 통일하지 않은 채 두 패턴을 함께 노출해 둔 상태다 — 자기들도 아직 어느 쪽이 정답인지 결론을 내지 못했다는 솔직한 신호로 읽힌다.

**별나라 스킬 — `firebase-basics`** (106줄)

Firebase 스킬은 본문이 짧다. 본문이 짧은 이유는 본문 자체가 **부트스트랩 셸 스크립트** 역할만 하기 때문이다:

> 1) 플래닝 모드 task.md에 `firebase/agent-skills` 설치 항목을 *맨 위에* 추가
> 2) `npm --version` 확인 (없으면 LTS 안내)
> 3) `npx -y skills add firebase/agent-skills -y` 실행

즉 `google/skills`의 firebase는 별도 리포 `firebase/agent-skills`로 위임된다. Google 내부에 이미 멀티 리포 구조가 작동 중이고, `google/skills`는 그 중 한 진입점일 뿐이라는 사실이 드러난다.

## skills.sh — 마켓플레이스 레이어의 등장

README 상단 뱃지가 `https://skills.sh/google/skills`로 연결되어 있다. 설치 명령도 `npx skills add google/skills`다 — Anthropic 공식 패턴은 `~/.claude/skills/`에 직접 두거나 plugin 형식을 사용하는데, 여기에 한 단 더 얹어 **npm 스타일의 패키지 매니저성 레이어**가 등장했다.

> The Skills CLI is a lightweight package manager for Agent Skills.

설치 명령 한 줄로 리포 경로 → 스킬 묶음 → 로컬 디렉토리 배치가 자동화되고, `firebase/agent-skills`처럼 다른 org의 리포도 같은 방식으로 끼울 수 있다. **Skills가 한 벤더의 컨벤션에서 패키지 생태계로 옮겨 가는 신호**다 — npm·crates.io·pip이 그랬듯, 패키지 매니저가 먼저 자리 잡으면 그 위의 컨벤션은 자연스럽게 표준화 압력을 받는다.

`agentskills.io`라는 별도 사이트가 함께 노출된다는 사실도 한 묶음이다. 한 벤더의 도큐먼테이션이 아니라 **벤더 중립의 표준 사이트**가 따로 운영된다는 신호다.

## 라이선스 / 기여 모델

- **라이선스**: Apache-2.0. 포크·재사용 자유, 특허 그랜트 포함.
- **외부 PR**: 받지 않는다. CONTRIBUTING.md가 명시한다 — 이슈 보고와 새 스킬 요청만 받고, 모든 SKILL.md는 "Google 내부 검증·승인 프로세스"를 거친다.
- **권장 사용 방식**: "Remix & Share" — 포크해서 자기 워크플로용으로 개조하는 것은 권장.
- **사내 프로그램**: Google 내부 팀은 "Agent Skills Program" 사내 문서와 SKILL.md 스펙을 따르라고 안내. 즉 사내에 공식 프로그램이 따로 있고, 그 산출물 일부를 공개하는 모델이다.

오픈소스 클라우드 SDK·에이전트 도구의 전형적인 거버넌스 패턴이지만, 외부 PR을 닫고 "포크해서 쓰라"고 말하는 결은 마켓플레이스 시대에 어울리는 답이다. 본가는 본가대로 품질 보증하고, 변형은 변형의 리포로 따로 떠 있게 두는 것 — `firebase/agent-skills`가 이미 그렇게 떠 있다.

## 최근 활동

최근 5개 커밋(2026-05-15 기준)을 보면 활발한 유지보수가 이뤄지고 있다.

| 날짜 | 내용 |
|---|---|
| 2026-05-13 | networking-observability 메타데이터를 폴더명에 맞춤 |
| 2026-05-11 | gcloud 예시에 `--quiet` 추가 |
| 2026-05-07 | firebase 구조 개편 후 firestore 참조 갱신 |
| 2026-05-05 | google-genai 모델·capability 업데이트 |
| 2026-05-04 | BQ MCP 툴명·마크다운 링크 수정 |

활발한 잔손질이 들어가고 있지만, 릴리스 태깅은 없다. 신생 리포라 버저닝 정책이 아직 미정으로 보인다.

## 가장 흥미로운 지점

가장 눈에 띄는 신호는 둘이다.

**(1) "Anthropic의 패턴"이 "공용 표준"으로 옮겨 가는 순간.** Google이 동일한 SKILL.md 스펙을 그대로 채택했다는 것 자체가 자기 NIH(Not Invented Here) 본능을 누른 결정이다. `agentskills.io`라는 벤더 중립 사이트가 따로 운영된다는 것은 두 벤더가 같은 표준 위에 서 있음을 외부에 노출하기 위한 장치로 보인다. 다음 클라우드 벤더(AWS·Azure)가 동참할 때 같은 표준을 따를 가능성이 한층 커진다.

**(2) skills.sh라는 패키지 매니저 레이어가 사실상 합의된 진입점이 되어 가는 모양새.** npm·crates.io·pip이 그랬듯 패키지 매니저가 자리 잡으면 그 위의 컨벤션은 빠르게 굳는다. gke-basics가 시범 도입한 `license` / `metadata.author` / `metadata.version` 같은 추가 키도, 결국 마켓플레이스가 요구하는 메타데이터로 표준화될 가능성이 높다. **표준은 사양 회의가 아니라 패키지 매니저가 만든다**는 오래된 관찰이 한 번 더 작동하는 것 같다.

## 출처

- 발신자: Google org (`@google`)
- 라이선스: Apache-2.0
- 공개: 2026-03-31 (최종 푸시 2026-05-15)
- 원문: <https://github.com/google/skills>

리포에 아키텍처 다이어그램·로고 같은 인용 가능한 이미지는 포함되지 않아 본 다이제스트는 텍스트만으로 정리했다.

[^agentskills-home]: 관련 사이트: <https://agentskills.io/home>, <https://skills.sh/google/skills>
[^github-firebase]: 멀티 리포 분기: <https://github.com/firebase/agent-skills>
