---
title: "qm: Multiplayer agent harness for work"
date: 2026-08-01T15:30:00+09:00
tags: ["AI", "AI 에이전트", "하네스", "오픈소스", "멀티에이전트"]
categories: ["에이전트와 코딩"]
summary: "yc-software가 MIT로 공개한 멀티플레이어 에이전트 하네스 QM. 사람마다·방마다 격리된 스코프를 두고, 하네스와 모델을 갈아끼우며, 슬랙과 웹에서 조직 전체가 함께 쓰도록 설계됐다."
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/qm-multiplayer-agent-harness/web-ui-hero.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/qm-multiplayer-agent-harness/web-ui-hero.png"
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. QM은 yc-software가 MIT 라이선스로 공개한 "일을 위한 멀티플레이어 에이전트 하네스"다. 슬랙과 웹에서 동작하며, 개인 비서형 에이전트가 아니라 스타트업 조직 전체가 함께 쓰도록 설계됐다.
2. 사람마다, 그리고 방(채널·그룹·프로젝트)마다 격리된 스코프를 가진다. 각 스코프는 자기만의 메모리·파일·키체인 뷰·권한·크론·웹앱·지속 샌드박스를 갖고, 서로를 밟지 않으면서 협업한다.
3. 코어는 제네릭하게 두고 조직 특화 부분은 별도 deployment 디렉토리나 private fork로 분리한다. 하네스와 모델은 Pi·OpenCode·Codex·Claude Code를 갈아끼울 수 있어 특정 벤더에 묶이지 않는다.

![QM 웹 UI: 두 개의 동시 세션, 개인 파일 사이드바, 크론·키체인·배포·메모리·스킬](https://img.seosoyoung.eiaserinnys.me/images/qm-multiplayer-agent-harness/web-ui-hero.png)

## QM이란

대부분의 에이전트는 개인 비서처럼 설계된다. 하나를 회사 전체가 쓰도록 만들 수는 있지만 금세 복잡해진다. QM은 스타트업을 겨냥해 설계됐다. 직원은 저마다 격리된 워크스페이스를 받아 서로 영향을 주지 않고 독립적으로 일하고, 동시에 채널·그룹 메시지·프로젝트에서 에이전트와 협업한다.

핵심은 스코프(scope)라는 단위다. 사람 한 명, 방 하나가 각각 자기만의 메모리·파일·키체인 뷰·권한·크론·웹앱·지속 샌드박스를 갖는다.

오픈소스를 염두에 두고 만들어졌다. 하네스와 모델을 직접 골라 갈아끼울 수 있는데, Pi·OpenCode·Codex·Claude Code가 모두 같은 코어를 구동하므로 배포가 단일 벤더에 종속되지 않는다.

## 기능

원문이 정리한 기능은 다음과 같다.

- **개인 스코프와 공유 스코프.** 사람들은 에이전트를 <em>자기 것</em>으로 커스터마이즈하면서도, 슬랙 채널과 프로젝트에서 협업으로 함께 쓴다.
- **슬랙과 웹.** 동일한 정체성과 설정이 슬랙과 웹앱 사이를 그대로 이어진다.
- **관리자 제어.** 조직 단위 설정, 보안 태세(security posture), 사용 가능한 하네스와 모델을 관리자가 정한다.
- **웹앱.** 내부용 커스텀 앱을 띄워 필요한 사람에게 배포한다.
- **공유 스킬.** 스킬은 스코프가 소유하며 권한 부여로 공유된다. 관리자 승인을 거치면 조직 전체로 승격되고, git 리포에서 스킬 팩을 가져올 수 있다.
- **백그라운드 작업.** 크론과 워치(watch)가 아무도 보지 않는 사이에 일을 돌린다.

## 이것으로 할 수 있는 일

원문은 실제 활용 시나리오를 이렇게 나열한다.

- 내부 노트·이메일·문서·데이터베이스·웹을 함께 검색한다.
- 회사의 두뇌(company brain)에서 정보를 끌어온다.
- 내부 앱을 만들어 필요한 사람에게 배포하고, 그 데이터를 최신으로 유지한다.
- 과거에 보낸 글에서 사용자의 문체를 학습한 뒤, 일정에 맞춰 받은편지함을 분류한다. 라벨과 답장 초안까지 포함된다.
- 기존 리포지토리 안에서 일한다. 테스트를 돌리고, PR을 열고, CI를 지켜보고, 시스템 로그를 확인한다.
- 공유 채널에서 프로젝트를 추적하고, 진행 상황과 후속 조치를 게시한다.

## 아키텍처

QM은 헤드리스 코어(headless core)를 중심에 둔다. 모든 턴은 중앙 코어를 거치며, 코어는 여러 모델과 하네스를 써서 응답을 생성한다.

<figure style="text-align:center;margin:1.6rem 0">
<svg viewBox="0 0 760 250" role="img" aria-label="QM 아키텍처: Postgres 지속 계층, 헤드리스 코어(API와 에이전트 루프), 스코프별 샌드박스가 화살표로 연결된 구성도" style="width:100%;max-width:720px;height:auto;font-family:inherit">
  <defs>
    <marker id="qmArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="20" y="80" width="150" height="90" rx="10" fill="currentColor" fill-opacity="0.04" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="95" y="118" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor">Postgres</text>
  <text x="95" y="140" text-anchor="middle" font-size="11.5" fill="currentColor" opacity="0.72">세션 · 메모리 · 큐</text>
  <rect x="235" y="35" width="280" height="180" rx="12" fill="currentColor" fill-opacity="0.04" stroke="currentColor" stroke-width="1.5"/>
  <text x="375" y="60" text-anchor="middle" font-size="13" font-weight="600" fill="currentColor" opacity="0.7">헤드리스 코어</text>
  <rect x="258" y="74" width="234" height="48" rx="8" fill="currentColor" fill-opacity="0.07" stroke="currentColor" stroke-width="1"/>
  <text x="375" y="103" text-anchor="middle" font-size="12.5" fill="currentColor">API · 정체성 · 정책 · 스케줄러</text>
  <rect x="258" y="150" width="234" height="52" rx="8" fill="currentColor" fill-opacity="0.07" stroke="currentColor" stroke-width="1"/>
  <text x="375" y="172" text-anchor="middle" font-size="12.5" fill="currentColor">에이전트 루프</text>
  <text x="375" y="190" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.72">Pi · OpenCode · Claude Code</text>
  <line x1="375" y1="122" x2="375" y2="150" stroke="currentColor" stroke-width="1.4" marker-start="url(#qmArrow)" marker-end="url(#qmArrow)"/>
  <rect x="580" y="80" width="160" height="90" rx="10" fill="currentColor" fill-opacity="0.04" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="660" y="110" text-anchor="middle" font-size="13" font-weight="600" fill="currentColor">스코프별 샌드박스</text>
  <text x="660" y="132" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.72">파일 · 도구</text>
  <text x="660" y="148" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.72">로그인된 서비스</text>
  <line x1="172" y1="125" x2="233" y2="125" stroke="currentColor" stroke-width="1.4" marker-start="url(#qmArrow)" marker-end="url(#qmArrow)"/>
  <line x1="517" y1="125" x2="578" y2="125" stroke="currentColor" stroke-width="1.4" marker-start="url(#qmArrow)" marker-end="url(#qmArrow)"/>
</svg>
<figcaption style="font-size:0.85em;opacity:0.7;margin-top:0.6rem">QM 아키텍처 — 모든 턴이 코어를 거쳐, 스코프마다 격리된 샌드박스에서 실행된다.</figcaption>
</figure>

- **Postgres 지속 계층** — 세션·메모리·큐, 즉 사용자 데이터와 세션 이력, 그 밖의 지속 상태를 담는다.
- **코어(API + 에이전트 루프)** — 정체성·정책·스케줄러를 다루는 API와, Pi·OpenCode·Claude Code 등을 구동하는 에이전트 루프가 서로 맞물린다.
- **스코프별 샌드박스** — 파일·도구·로그인된 서비스가 들어 있는, 각 스코프의 "지속되는 컴퓨터"다.

에이전트가 쥔 도구 표면은 작고 고정돼 있다. 그중 하나가 `execute`인데, 스코프 자신의 격리 샌드박스에서 명령을 실행한다. 한 번 설치한 도구가 계속 남아 있는 그 스코프의 지속 컴퓨터가 여기다.

웹 UI, 관리자 패널, 공개 포털은 코어의 HTTP API 위에 얹히는 선택적 플러그인이다. 슬랙은 코어가 직접 시작하고 감독하는 인프로세스(in-process) 플러그인이다.

코어는 TypeScript를 Node에서 직접 실행하고 HTTP는 Fastify를 쓴다. 슬랙 플러그인은 Bolt를, 웹 UI는 Vite로 빌드하고 Lit로 렌더한다.

코어 자체는 제네릭하다. 한 회사에 특화된 모든 것(조직 설정, 커스텀 도구와 스킬, 샌드박스 이미지, 인프라)은 `qm` CLI가 검증하고 배포하는 <em>deployment 디렉토리</em>에 들어간다. 하네스·세션 저장소·샌드박스·메모리 같은 모든 기반(substrate)은 인터페이스 뒤에 놓여, 프로덕션 구현은 배선 파일(wiring file) 하나로 교체된다.

## 샌드박스를 들여다보면

README는 샌드박스를 "스코프의 지속되는 컴퓨터"라는 한 줄로 소개하고 지나간다. 어떻게 만들었는지 궁금해 소스를 열어 봤더니, 핵심은 "겉은 하나, 속은 둘"이었다.

겉에서 보면 샌드박스는 어디서나 똑같이 생겼다. 명령을 실행하고, 파일을 읽고 쓰고, 다 쓰면 정리하는 공통 창구 하나로 감싸 두었다. 그 뒤의 실제 몸통은 환경에 따라 갈린다. 개발자 노트북에서는 사람마다 도커 컨테이너를 하나씩 띄우고, 실제 서비스에서는 AWS가 굴리는 경량 가상머신(microVM)을 스코프마다 띄운다. 같은 도구를 부르는데 한쪽은 컨테이너가, 다른 쪽은 가상머신이 답하는 셈이다.

"지속되는 컴퓨터"라는 말이 지켜지는 방식도 두 갈래다. 노트북 쪽은 볼륨에 파일을 그대로 남겨 두면 끝이다. 서비스 쪽은 가상머신이 오래 살지 않으므로, 자리를 비우기 전에 홈 디렉터리를 통째로 묶어 S3에 넣어 두었다가 다음에 깨어날 때 되살린다. 한 번 설치한 도구가 다음에도 남아 있는 비결이 여기 있다. 오래 놀고 있는 스코프는 저장만 해두고 아예 꺼서 비용을 아낀다.

세부로 들어가도 결이 실용적이다. 여럿이 함께 쓰는 읽기 전용 파일(공유 스킬 같은 것)은 복잡한 파일시스템 기교 없이 통째로 얹되, 내용이 바뀌었을 때만 다시 밀어 넣는다. 에이전트가 명령을 돌릴 때는 샌드박스 안에 상주하는 작은 접수 프로그램에게 말을 거는 구조이고, 개발 서버처럼 오래 도는 작업도 그 접수원이 뒤에서 계속 지켜본다. 무겁게 두르기보다, 있는 재료로 단정하게 엮은 인상이다.

## 보안과 시크릿

QM의 접근은 OpenCode·Codex·Claude Code 같은 로컬 코딩 에이전트를 따른다. 에이전트는 자신이 일하는 사람으로서, 그 사람의 자격증명과 권한으로 행동하며, 하는 일은 전부 감사(audit)된다. 조직은 하나의 보안 태세를 고르고, 더 좁은 스코프는 그것을 조이기만 할 수 있다.

| 태세 | 동작 |
| --- | --- |
| **Strict** | 무효과인 두 턴 종료 도구를 빼면, 모든 하네스 도구 호출이 사람 승인을 기다린다. |
| **Auto** (기본값) | 분류기가 출처 라벨이 붙은 외부 데이터와 도구 결과를 모델에 닿기 전에 선별한다. 배포는 이를 자체 선별 프록시로 돌릴 수 있다. |
| **Dangerous** | 콘텐츠 선별도, 도구 호출 사이의 멈춤도 없다. |

재귀 삭제나 파괴적 SQL처럼 미리 선언된 명령 정책(승인 규칙과 강한 거부)은 Dangerous를 포함한 모든 태세에서 적용된다. 위협 모델과 운영자 가정, 알려진 한계는 저장소의 `SECURITY.md`에 정리돼 있다.

## 배포와 커스터마이즈 — 두 갈래

조직에 QM을 올리는 길은 둘로 갈린다.

**deployment 리포지토리.** `@yc-software/qm`에 의존하는 조직 소유 배포 리포를 만든다. `qm init`이 에이전트용 배포 스킬을 실체화하고 인프라·웹 로그인·커넥터 자격증명·슬랙 접근·배포·라이브 검증까지 안내한다. 소스 체크아웃이 필요 없다. 각 배포는 운영자 자신의 클라우드 계정에서 돌아간다.

**private fork.** 어떤 조직은 반대 트레이드오프를 원한다. 엔지니어와 코딩 에이전트가 코어와 커스터마이즈를 함께 읽도록 코드베이스 전체를 한곳에 두되, 커스터마이즈만 비공개로 유지하는 방식이다. 이때는 GitHub의 Fork 버튼이 아니라 <em>일반 clone</em>으로 독립 비공개 리포를 만든다. 원문은 그 이유를 분명히 밝힌다. GitHub 포크는 원본의 가시성을 물려받아 공개 리포의 포크를 비공개로 만들 수 없고, 하나의 객체 네트워크를 공유해 포크에 올린 커밋이 공개 쪽에서 SHA로 조회된다. 일반 clone에는 이 문제가 없다.

조직 특화된 모든 것은 `deploy/layers/<org>/`에 둔다. 코어는 업스트림과 바이트 단위로 동일하게 유지되고, 이것이 병합을 작게 만든다. 두 방향의 경계는 두 스킬이 지킨다. `update-qm`은 업스트림 qm을 private fork로 병합해 동기화 PR을 열고, `upstream-pr`은 조직 중립적 수정을 qm으로 돌려보내되 나가는 diff·커밋 메시지·스크린샷에서 조직 식별자를 걸러낸 뒤 푸시한다.

## 기여

QM은 기여를 코드가 아니라 <em>사람이 쓴</em> 텍스트로 받는다. `adrs/` 아래 `.txt`나 `.md` 파일에 원하는 변경을 비공식적으로 서술하고, 방향이 맞으면 구현은 프로젝트 쪽이 처리한다. 취약점은 공개 이슈가 아니라 비공개로 보고한다.

## 가장 눈여겨본 것은

멀티플레이어 협업 에이전트를 실제로 운영해 본 입장에서, 가장 눈에 들어온 설계는 "스코프별 격리"를 1급 개념으로 끌어올린 대목이다. 사람과 방을 각각 독립된 메모리·파일·키체인·샌드박스로 나누고, 그 위에서 채널·프로젝트 협업을 얹는다. 개인 비서 하나를 조직에 억지로 늘리는 대신, 격리를 기본값으로 두고 공유를 권한 부여로 여는 순서를 택한 셈이다.

또 하나는 하네스 중립성이다. Pi·OpenCode·Codex·Claude Code가 같은 코어를 구동한다는 것은, 모델·하네스를 인프라 세부로 내려두고 정체성·정책·스케줄러를 코어에 남긴다는 뜻이다. 여기에 코어를 업스트림과 바이트 단위로 동일하게 유지하면서 조직 특화는 `deploy/layers/`로 밀어내는 구조가 겹친다. 오픈소스 코어와 사설 커스터마이즈가 오래 공존하도록 병합 비용을 처음부터 낮춰 둔 판단이 인상적이다.

## 출처

yc-software, `qm` — Multiplayer agent harness for work. MIT License.
원문: <https://github.com/yc-software/qm>
