---
title: "OpenKB — Open LLM Knowledge Base"
date: 2026-04-30T14:35:00+09:00
tags: ["LLM", "knowledge-base", "RAG", "PageIndex", "wiki"]
categories: ["다이제스트"]
summary: "VectifyAI의 OpenKB는 문서를 한 번 컴파일하여 살아 있는 위키로 누적하는 오픈소스 지식 베이스 도구다. PageIndex로 긴 문서를 벡터 없이 검색하고, 결과물은 옵시디언 호환 마크다운으로 남긴다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. OpenKB는 VectifyAI가 공개한 CLI 기반 LLM 지식 베이스 도구로, Karpathy의 LLM Wiki 발상을 실제 패키지로 구현한 것이다.
2. 짧은 문서는 markitdown으로, 20페이지 이상의 긴 PDF는 자체 도구 PageIndex로 처리해 벡터 DB 없이 추론 기반 검색을 한다.
3. 출력물은 `[[wikilinks]]`가 박힌 평범한 마크다운이라 Obsidian에서 그대로 열리고, OpenKB가 사라져도 지식 자산은 남는다.

## 정체와 발신자

- **이름**: OpenKB (Open Knowledge Base)
- **개발사**: VectifyAI — PageIndex를 만든 팀
- **저자**: Kylin (`quanqi@pageindex.ai`), Ray (`ray@vectify.ai`)
- **라이선스**: Apache 2.0
- **버전**: `0.1.3` (Alpha)
- **언어/런타임**: Python 3.10+
- **링크**: <https://github.com/VectifyAI/OpenKB>

CLI 한 줄로 설치(`pip install openkb`)하고, 폴더 하나를 지식 베이스 루트로 잡아 `openkb init`으로 초기화하는 구조다. PageIndex 회사가 자기 검색 엔진을 자연스럽게 끼워 파는 디스트리뷰션 채널 성격도 있다.

## 무엇이 문제였나 — 전통 RAG의 한계

OpenKB는 README에서 자기 동기를 한 문장으로 정리한다.

> Traditional RAG rediscovers knowledge from scratch on every query. Nothing accumulates.

전통 RAG는 매 쿼리마다 청크를 임베딩 검색해 지식을 처음부터 다시 도출한다. 같은 코퍼스에 같은 질문을 백 번 던져도 시스템이 더 똑똑해지지 않는다. 위키처럼 합성·교차참조·모순 표시가 영구히 남는 자산이 만들어지지 않는 것이 RAG의 구조적 한계다.

OpenKB의 해결책은 단순하다. **지식을 한 번 컴파일하여 영구 위키로 만들고, 새 문서가 들어오면 그 위키를 갱신한다.** 쿼리는 이미 정제된 위키 위에서 LLM이 답한다. 발상 자체는 [Andrej Karpathy의 트윗](https://x.com/karpathy/status/2039805659525644595)에서 가져왔다고 명시한다.

## 위키 구조

OpenKB가 만드는 `wiki/` 폴더는 다음과 같이 짜인다 (`openkb/schema.py`).

- `index.md` — 지식 베이스 카탈로그. 모든 페이지의 한 줄 요약이 자동 유지된다.
- `log.md` — append-only 운영 타임라인 (ingest, query, lint).
- `AGENTS.md` — 위키 스키마 자체를 LLM에게 설명하는 매뉴얼.
- `sources/` — 원문을 마크다운(짧은 문서)이나 JSON(긴 문서, 페이지 단위)으로 저장.
- `summaries/` — 문서별 요약. 1 source ↔ 1 summary.
- `concepts/` — **여러 문서를 가로지르는 합성 페이지.** OpenKB가 자랑하는 "the good stuff".
- `explorations/` — 의미 있는 쿼리 결과를 영구 보존.
- `reports/` — 린트 결과.

핵심은 `concepts/`다. summaries가 1:1 매핑이라면 concepts는 N:M으로, 새 문서가 들어올 때마다 기존 컨셉 페이지가 갱신되거나 새 페이지가 생긴다. 한 소스가 추가되면 위키에서 평균 10\~15개 페이지가 영향을 받는다고 README는 적는다.

## 짧은 문서 vs 긴 문서

문서 길이에 따라 처리 경로가 갈리는 것이 OpenKB의 또 다른 설계 결정이다.

| | 짧은 문서 | 긴 문서 (PDF ≥ 20페이지) |
|---|---|---|
| **변환** | markitdown → 마크다운 | PageIndex → 트리 인덱스 + 요약 |
| **이미지** | pymupdf로 인라인 추출 | PageIndex가 추출 |
| **LLM이 읽는 것** | 본문 전문 | 문서 트리 |
| **결과** | summary + concepts | summary + concepts |

긴 PDF를 통째로 LLM에 욱여넣지 않고, PageIndex가 만든 계층적 트리만 LLM에 보여준다. 컨텍스트 한도, 컨텍스트 부패(context rot), 요약 손실을 우회하는 전략이다.

## PageIndex 통합

PageIndex는 같은 회사가 만든 별도 오픈소스로, <strong>벡터 DB 없이 PDF 구조 트리를 LLM이 추론으로 탐색</strong>하는 검색 엔진이다.

- 기본은 로컬 실행. 외부 의존성 없이 동작한다.
- 옵션으로 `PAGEINDEX_API_KEY`를 설정하면 클라우드 모드로 OCR(스캔 PDF), 고속 구조 생성, 대규모 인덱싱을 쓸 수 있다.

벡터 검색이 의미 유사도로 청크를 끌어오는 동안, PageIndex는 "이 질문에 답하려면 목차의 어느 가지로 내려가야 하는가"를 LLM이 직접 추론한다. 트레이드오프가 분명한 접근이지만, 위키 컴파일이라는 맥락에서는 구조적 맥락(섹션 위계)을 보존한다는 장점이 있다.

## 컴파일 파이프라인

`openkb add some.pdf`를 실행하면 내부적으로 다음 5단계가 돌아간다 (`openkb/agent/compiler.py` 주석 발췌).

1. 베이스 컨텍스트 A를 만든다 — 스키마(AGENTS.md) + 문서 내용. 이 A를 프롬프트 캐시에 고정한다.
2. A로 요약 페이지를 생성한다.
3. A + 요약으로 컨셉 플랜을 짠다 — 어떤 컨셉을 새로 만들고(create), 어떤 컨셉에 합칠지(update), 어떤 컨셉에 링크만 걸지(related).
4. 동시 LLM 호출로 신규 컨셉을 작성하고 기존 컨셉을 재작성한다. A가 캐싱되어 있어 비용이 절감된다.
5. 코드가 교차참조 링크를 추가하고 `index.md`를 갱신한다.

LLM에게 "한 번에 다 해줘"라고 시키지 않고, 캐시 친화적으로 단계를 쪼갠 점이 인상적이다. 컨셉 플랜 단계는 다음 규칙으로 LLM을 명시적으로 가둔다.

> - For the first few documents, create 2-3 foundational concepts at most.
> - Do NOT create a concept that overlaps with an existing one — use "update".
> - Do NOT create concepts that are just the document topic itself.

지식 베이스가 개념 중복으로 부풀어 오르지 않게 하려는 가드레일이다.

## AGENTS.md — 위키 스키마를 데이터로 외재화

위키의 디렉토리 구조, 페이지 유형, 인덱스 포맷, 로그 포맷, 작성 규약은 코드에 박혀 있지 않고 `wiki/AGENTS.md`라는 마크다운 파일에 적혀 있다. OpenKB는 매 LLM 호출마다 이 파일을 디스크에서 다시 읽어 시스템 프롬프트에 끼워 넣는다.

```python
def get_agents_md(wiki_dir: Path) -> str:
    agents_file = wiki_dir / "AGENTS.md"
    if agents_file.exists():
        return agents_file.read_text(encoding="utf-8")
    return AGENTS_MD
```

사용자가 `AGENTS.md`를 편집하면 다음 호출부터 즉시 새 정책이 적용된다. 위키 정책을 코드 배포 없이 바꿀 수 있는 구조다. LLM의 행동 규약을 데이터로 외재화하는 패턴은 점점 표준이 되어가고 있다.

## CLI와 운영

| 명령 | 설명 |
|---|---|
| `openkb init` | 지식 베이스 초기화(인터랙티브) |
| `openkb add <file_or_dir>` | 문서 추가 + 위키 컴파일 |
| `openkb query "..."` | 위키에 질문(원샷). `--save`로 결과를 `explorations/`에 저장 |
| `openkb chat` | 멀티턴 대화. `--resume`, `--list`, `--delete`로 세션 관리 |
| `openkb watch` | `raw/` 폴더 감시 → 새 파일 자동 컴파일 |
| `openkb lint` | 위키 헬스체크 |
| `openkb list` / `openkb status` | 인덱스/통계 |

`openkb chat` 안에서는 슬래시 명령으로 `/add`, `/save`, `/lint` 등을 호출할 수 있다. 멀티 LLM 지원은 LiteLLM에 위임되어 있고, `provider/model` 포맷으로 OpenAI·Anthropic·Gemini 등을 자유롭게 선택한다.

## Lint — 위키 부패 방지

`openkb/lint.py`는 위키가 시간이 지나며 무너지지 않도록 다음을 검사한다.

- 깨진 `[[wikilinks]]` — 존재하지 않는 타깃을 가리키는 링크
- 고아 페이지 — 인커밍·아웃고잉 링크가 없는 페이지
- 누락된 위키 엔트리 — `raw/`에 있지만 `sources/`나 `summaries/`에 없는 파일
- 인덱스 동기화 — `index.md`의 링크와 디스크 실제 파일의 일치

지식 자산이 누적될수록 부패하기 쉽다는 점을 인정하고, 구조적 점검을 1급 명령으로 넣은 점이 단단하다.

## 옵시디언 호환과 이식성

OpenKB가 만드는 `wiki/`는 별도 데이터베이스나 포맷 없이 평범한 마크다운 + Obsidian 위키링크다. `wiki/` 폴더를 그대로 Obsidian Vault로 열면 그래프 뷰, 백링크, 웹 클리퍼가 동작한다.

이 결정의 함의는 크다. **OpenKB가 단종되어도 지식 자산은 사용자의 마크다운으로 남는다.** 출력 포맷이 곧 락인 회피 전략이다.

## 기술 스택

- [PageIndex](https://github.com/VectifyAI/PageIndex) — 벡터리스 추론 기반 문서 인덱싱·검색
- [markitdown](https://github.com/microsoft/markitdown) — 범용 파일 → 마크다운 변환 (Microsoft)
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) — 에이전트 프레임워크
- [LiteLLM](https://github.com/BerriAI/litellm) — 멀티 프로바이더 LLM 게이트웨이
- [Click](https://click.palletsprojects.com/) — CLI 프레임워크
- [watchdog](https://github.com/gorakhargosh/watchdog) — 파일시스템 감시

## 로드맵

README가 적은 다음 단계는 다음과 같다.

- 긴 문서 처리를 PDF 외 포맷으로 확장
- 폴더 중첩 지원으로 대규모 컬렉션 스케일링
- 거대 지식 베이스를 위한 계층적 컨셉(토픽) 인덱싱
- DB 백엔드 스토리지 엔진
- 위키 브라우징·관리용 웹 UI

지금 단계는 명백히 알파다. 컨셉 페이지의 N:M 갱신이 정말로 무너지지 않고 누적되는지는 큰 코퍼스에서 검증이 필요하다.

## 가장 흥미로운 지점

OpenKB의 진짜 베팅은 <strong>"위키 컴파일은 LLM이 더 잘하는 작업"</strong>이라는 가설이다.

전통 RAG는 검색을 LLM이 아닌 임베딩 공간에 맡긴다. 컨텍스트가 부족하면 더 많은 청크를 끌어오고, 모델이 그걸 매번 읽고 합성한다. OpenKB는 정반대다. **합성·교차참조·중복 제거를 컴파일 시점에 LLM이 한 번 끝내고**, 쿼리 시점에는 이미 사람이 읽을 만한 형태의 위키를 LLM이 다시 읽는다.

이 발상이 흥미로운 이유는 결과물이 LLM 전용이 아니라 <strong>인간도 그대로 쓸 수 있는 마크다운</strong>이라는 점이다. RAG 시스템의 청크와 임베딩은 인간이 들여다봐도 무의미하지만, OpenKB의 위키는 인간 지식 노동의 결과물이기도 하다. 같은 자산이 두 사용자(LLM·인간)에게 동시에 가치를 가지는 설계다.

다만 한 발 떨어져 보면 의문도 남는다. 위키 컴파일은 *읽기 시점*이 아니라 *쓰기 시점*에 비용을 몰아넣는 전략인데, 코퍼스가 빠르게 변하는 상황(예: 매일 수백 건의 문서가 들어오는 회사 위키)에서 컴파일 비용이 폭발하지 않을지, 컨셉 페이지의 N:M 갱신이 일관성을 어떻게 유지할지는 실측이 필요하다. PageIndex 팀이 자사 검색 엔진의 디스트리뷰션 채널로 OpenKB를 푸는 측면도 있어서, 동기와 기술적 우월성을 분리해서 볼 필요가 있다.

## 출처

VectifyAI / PageIndex 팀 (Kylin, Ray), 2026, Apache 2.0
원문: <https://github.com/VectifyAI/OpenKB>
