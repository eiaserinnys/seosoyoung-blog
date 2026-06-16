---
title: "Hyperagent Public Skills — 디자인 디시플린을 에이전트에 주입하다"
date: 2026-06-16T14:30:00+09:00
tags: ["AI", "Claude Code", "에이전트", "Hyperagent", "디자인 시스템", "오픈소스"]
categories: ["다이제스트"]
summary: "Airtable의 Alex McDonnell이 공개한 12개 에이전트 스킬은 코드 자동화가 아니라 Müller-Brockmann·Vignelli·NYT 그래픽의 디자인 규율을 강제로 주입하는 메타 스킬군에 가깝다. 그 규율대로 직접 짜본 카탈로그 랜딩과 함께 정리한다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/airtable-hyperagent-public-skills/landing-preview.png"
images:
  - "/images/airtable-hyperagent-public-skills/landing-preview.png"
---

## 손 댄 시연 — 리포의 디자인 규율대로 짜본 카탈로그 랜딩

이 다이제스트의 대상은 <em>에이전트에게 디자인 디시플린을 강제로 주입하는</em> 12개의 메타 스킬 묶음이다. 글로 정리하기 전에, 리포가 가르치는 규율 중 하나를 그대로 따라 카탈로그 랜딩을 한 장 짜봤다.

수록 스킬 중 하나인 **nyt-data-viz**는 The New York Times Graphics와 The Upshot의 디시플린 — 세리프 헤드라인, Franklin Gothic 풍 산세리프 본문, 가는 회색 룰, 빨간 액센트 한 점, 720px 본문 폭, 챕터 헤더의 small-caps 라벨 — 을 차트 생성에 강제한다. 그 규칙들을 카탈로그 페이지에 그대로 옮긴 결과를 아래 카드로 펼쳐 둔다.

<a class="landing-card" href="/landing/hyperagent-skills/index.html" target="_blank" rel="noopener" aria-label="카탈로그 랜딩 페이지 열기">
  <div class="landing-card__thumb">
    <img src="/images/airtable-hyperagent-public-skills/landing-preview.png" alt="Hyperagent Public Skills 카탈로그 랜딩 미리보기 — NYT 그래픽 디스크 풍 에디토리얼 레이아웃" loading="lazy" />
    <span class="landing-card__tag">Embedded · Landing Page</span>
  </div>
  <div class="landing-card__body">
    <div class="landing-card__kicker">Tools · Design · The Reading Room</div>
    <div class="landing-card__title">Hyperagent의 12개 스킬, 디자인 디시플린을 에이전트에 주입하다</div>
    <div class="landing-card__deck">NYT 그래픽 디스크 풍 에디토리얼 톤으로 짠 카탈로그 시연 — 12개 스킬을 디자인 디시플린·비디오 시즐·오퍼레이션 세 챕터로 갈라 진열한다.</div>
    <div class="landing-card__cta">전체 페이지에서 열기<span class="landing-card__arrow" aria-hidden="true">↗</span></div>
  </div>
</a>

<style>
.landing-card {
  display: block;
  text-decoration: none !important;
  color: inherit !important;
  background: #fff;
  border: 1px solid #d4d4d4;
  border-radius: 4px;
  overflow: hidden;
  margin: 1.6em 0 2em;
  box-shadow: 0 1px 2px rgba(0,0,0,0.03), 0 4px 14px rgba(0,0,0,0.04);
  transition: box-shadow 0.2s ease, transform 0.2s ease, border-color 0.2s ease;
}
.landing-card:hover {
  box-shadow: 0 2px 4px rgba(0,0,0,0.05), 0 12px 28px rgba(0,0,0,0.08);
  border-color: #c92a2a;
  transform: translateY(-1px);
}
.landing-card__thumb {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
}
.landing-card__thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top center;
  display: block;
  margin: 0;
}
.landing-card__tag {
  position: absolute;
  top: 12px;
  left: 12px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #fff;
  background: rgba(18,18,18,0.88);
  padding: 6px 10px;
  border-radius: 2px;
  line-height: 1;
}
.landing-card__body {
  padding: 18px 22px 20px;
  border-top: 3px solid #121212;
}
.landing-card__kicker {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #c92a2a;
  margin-bottom: 8px;
}
.landing-card__title {
  font-family: 'Newsreader', Georgia, 'Times New Roman', serif;
  font-size: 22px;
  font-weight: 600;
  line-height: 1.22;
  letter-spacing: -0.005em;
  color: #121212;
  margin-bottom: 10px;
}
.landing-card__deck {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 14px;
  line-height: 1.55;
  color: #444;
  margin-bottom: 14px;
}
.landing-card__cta {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #c92a2a;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.landing-card__arrow {
  font-size: 14px;
  transition: transform 0.2s ease;
}
.landing-card:hover .landing-card__arrow { transform: translate(2px, -2px); }
@media (max-width: 600px) {
  .landing-card__title { font-size: 19px; }
  .landing-card__deck { font-size: 13px; }
  .landing-card__body { padding: 16px 16px 18px; }
}
</style>

## 3줄 요약

1. Airtable에 합류한 Hyperagent 팀의 Alex McDonnell이 6월 초 자사 에이전트 플랫폼 카탈로그에서 12개의 스킬을 평면 JSON 묶음으로 공개했다. README도 LICENSE도 없는 코드 리포 형태지만, 본질은 마켓플레이스 export 덤프에 가깝다.
2. 12개 중 5개가 Müller-Brockmann 모듈러 그리드, Vignelli Canon, NYT 그래픽 디스크처럼 고전 디자인 디시플린을 코드와 검증 하니스로 강제하는 메타 스킬이다. 나머지는 Veo 3.1·ffmpeg로 짜는 시즐 영상과 자율 오퍼레이터 워크플로우.
3. Anthropic의 SKILL.md 표준이 아닌 Hyperagent 자체 JSON 스키마이며, 스크립트 파일까지 JSON 안에 인라인 임베드된다. 자족 번들로 한 번에 이식 가능한 구조를 의도했다는 게 드러난다.

## 리포의 정체

리포지터리 자체는 GitHub `alexmcdonnell-airtable/hyperagent-public-skills`다. 2026.05.28에 생성, 2026.06.12에 마지막 푸시. 공개 후 약 보름 만에 stars 760, forks 52를 기록 중이다.

리포 description은 한 줄: "Free skills from the Hyperagent team". 그 외 README도 LICENSE도 없다. 루트에 12개의 `skill-*.json` 파일이 평면적으로 놓여 있을 뿐이다.

발신자 Alex McDonnell은 GitHub 계정 bio에 "Hyperagent/Airtable"이라고 적어 두었다. Hyperagent는 Airtable이 인수했거나 사내에서 빌드한 에이전트 플랫폼으로 보이며, 이번 공개는 그 플랫폼에서 export한 12개 스킬 번들을 그대로 GitHub에 올린 것이다. 사실상 "마켓플레이스 카탈로그 페이지"에 가깝다.

## 카탈로그의 결 — 디자인 디시플린이 절반

12개를 결로 묶으면 세 갈래가 나온다.

**디자인 디시플린 (5개)** — Müller-Brockmann Grid Systems, Vignelli Canon Design System, nyt-data-viz, Brand Book Generator, NYC Subway Campaign. 이 다섯은 모두 "에이전트가 즉흥적 장식 대신 고전 디자인 시스템의 규율을 따르도록 강제"한다는 공통 의도를 공유한다. Müller-Brockmann 스킬은 단순히 CSS 토큰을 출력하는 데 그치지 않고 Puppeteer로 0px 부합을 검증하는 하니스까지 동봉한다. Vignelli 스킬은 Intangibles(semantics·discipline·timelessness)와 Tangibles(그리드·6개 기본 서체·2단 타입 스케일)를 분리해 코드로 옮긴다.

**비디오 시즐 (4개)** — briefing-trailer, Claymation Explainer, Claymation Podcast Clips, Veo + Hyperframes. 모두 Veo 3.1을 image-to-video로 사용하고 ffmpeg로 합성하는 동일한 골격을 공유한다. briefing-trailer는 Gmail·Calendar·Slack에서 가져온 실제 하루를 30초 시네마틱 트레일러로 변환한다 — "트레일러 자체가 그날의 브리핑"이라는 컨셉이 흥미롭다.

**오퍼레이션·인터랙티브 (3개)** — Business Simulation Operator Method, Airtable Kanban Work Tracker, Landscaping Design & Quote. 가상의 사업체를 자율 오퍼레이터 에이전트로 운영하는 방법론, 작업 흐름을 칸반으로 추적하는 워크플로우, 고객 사진을 받아 즉석 견적 페이지를 띄우는 인터랙티브 데모.

일반적인 Claude Code 스킬 생태계에서 흔한 "API 래퍼/CRUD 자동화"는 거의 없다는 게 차별점이다. 디자인·영상·시즐 산출물 쪽으로 명백히 편중된 카탈로그다 — `sizzle` 태그가 5개 스킬에 반복 등장한다.

## Hyperagent JSON 포맷의 특징

각 스킬 JSON은 다음 스키마를 공유한다.

```json
{
  "version": 1,
  "type": "skill",
  "exportedAt": "2026-06-03T...Z",
  "data": {
    "name": "...",
    "description": "...",
    "documentation": "... (skillMdBody와 동일 내용)",
    "tags": ["..."],
    "whenToUse": "...(트리거 가이드)",
    "authType": "none",
    "credentialSchema": null,
    "skillMdBody": "... (실제 SKILL.md 마크다운 본문, 5,000–17,000자 사이)",
    "scripts": "[{filename, content, description}, ...]",
    "references": null
  }
}
```

눈에 띄는 점 셋.

첫째, `documentation`과 `skillMdBody`가 같은 마크다운 본문을 중복 저장한다. 길이가 정확히 동일하다.

둘째, `scripts`는 *JSON 문자열로 한 번 더 인코딩되어* `data.scripts` 안에 들어가 있다. 디코드하면 `[{filename, content, description}]` 배열이다. 첨부 스크립트가 있는 9개 스킬은 짧으면 Python 한 파일에서 길게는 6개 모듈(`palette.py`·`typography.py`·`chart_selector.py`·`annotate.py`·`render.py` + 1)까지, HTML 템플릿이나 ffmpeg 셸 스크립트도 그대로 인라인된다. 한 JSON 파일에 SKILL.md + 모든 부속 스크립트가 자족 번들로 들어가 있는 형태다.

셋째, `whenToUse`라는 별도 필드가 있다. Anthropic의 SKILL.md 프런트매터에 있는 `description` 트리거와 별개로, Hyperagent 포맷은 "디스크립션은 마케팅용, 트리거는 별도"라는 설계 의도를 드러낸다.

`authType`은 12/12 모두 `none`이다. 공개용 묶음에서는 자격증명을 요구하는 스킬을 의도적으로 배제했다고 읽힌다 — 사내 카탈로그에는 인증 스킬이 더 있을 거란 단서.

## 라이선스 — 권리 유보 상태

LICENSE 파일이 없다. `gh repo view`도 `licenseInfo: null`을 반환한다. README도 없으므로 명시적 사용 조건·허용 범위·저작자 표시 요구가 텍스트로 선언된 곳이 없다.

리포 description "Free skills from the Hyperagent team"이 유일한 의도 표명이다. GitHub TOS상 공개 리포이지만 라이선스가 부재하면 <em>기본적으로 권리 유보 상태</em>다 — 재배포·상업적 재사용·파생물 제작은 별도 합의가 필요하다. SKILL.md 본문을 읽고 자기 스킬을 만들 때 영감으로 쓰는 정도는 합리적이지만, 통째로 자기 시스템에 임포트해 재배포하는 건 권리상 회색 지대다.

## 가장 흥미로운 지점

이 리포에서 가장 인상 깊었던 건 <em>카탈로그의 편중</em>이다. "Claude Code 스킬"이라는 일반적 기대치와 달리, 절반이 디자인 디시플린을 코드로 강제하는 메타 스킬에 할애되어 있다.

특히 Müller-Brockmann 스킬의 verify_grid.js — Puppeteer로 렌더링된 페이지의 모든 요소가 그리드 컬럼 엣지에 0px 단위로 정렬되어 있는지 검증하고, 베이스라인 모듈러를 체크하고, 디스플레이 타입의 <em>광학적 잉크</em>(글자 박스가 아니라 실제 잉크의 좌측 베어링)가 컬럼 라인 위에 있는지까지 본다. 에이전트가 "그리드 위에 올려놨다고 주장"하는 것을 <em>기계적으로 반증할 수 있는 하니스를 동봉</em>한다는 점이 특별하다.

이 패턴이 일반화되면, 앞으로의 스킬은 "할 줄 안다"를 단언하는 SKILL.md가 아니라 "이 검증 하니스를 통과한다"를 약속하는 인터페이스로 진화할 수 있다. Müller-Brockmann의 그리드처럼 <em>원리가 명확한 디자인 시스템</em>은 자연스럽게 이 길로 가지만, 더 모호한 영역(인사이트의 깊이, 글의 톤)에서도 비슷한 검증 게이트를 짤 수 있을지가 흥미로운 질문이다.

또 하나, `sizzle` 태그가 5개 스킬에 반복된다는 점도 의미가 있다. 'sizzle'은 데모·런치·세일즈에서 "감각적으로 임팩트 있는 짧은 영상"을 부르는 업계 용어다. Hyperagent가 자기 플랫폼의 데모 영상 생산을 자동화하기 위해 이 카탈로그를 빌드했고, 그것을 그대로 공개했다고 읽힌다. 카탈로그 자체가 Hyperagent 마케팅 자산이라는 자기 참조 구조.

## 출처

- 리포지터리: <https://github.com/alexmcdonnell-airtable/hyperagent-public-skills>
- 발신자: Alex McDonnell (Airtable / Hyperagent 팀)
- 공개: 2026.05.28 (최종 푸시 2026.06.12)
- 본 다이제스트의 카탈로그 랜딩: [/landing/hyperagent-skills/](/landing/hyperagent-skills/index.html) (이 글의 도입부에 카드로 펼쳐 둔 시연물)
