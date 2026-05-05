---
title: "Redis array type: short story of a long development"
date: 2026-05-05T12:50:00+09:00
tags: ["Redis", "data-structure", "AI-coding", "system-programming", "spec-driven-development"]
categories: ["다이제스트"]
summary: "Redis 창시자 antirez가 새로운 Array 데이터 타입을 AI와 함께 4개월에 걸쳐 설계·구현한 과정을 회고한다. 명세 문서 우선 작성이 성공의 열쇠였고, AI는 복잡성에 도전할 수 있게 해주는 안전망이었다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. antirez가 Redis의 새로운 Array 데이터 타입을 4개월에 걸쳐 AI(Opus → GPT 5.3/Codex)와 함께 설계·구현했다. 첫 달을 통째로 명세 문서 작성에 투자한 것이 이후 모든 작업의 열쇠였다.
2. 2단계 희소 표현의 한계를 발견하고 3단계 구조(슈퍼 디렉토리 → 밀집 디렉토리 → 슬라이스)로 전환했다. AI가 있었기에 타협 없이 복잡한 설계를 택할 수 있었다.
3. AI가 생성하고 테스트까지 통과한 코드라도, 한 줄씩 읽으면 비효율과 설계 오류가 곳곳에 있었다. 고품질 시스템 프로그래밍에서 인간의 전수 검토는 여전히 대체 불가능하다.

## 명세 우선: AI 협업의 전제 조건

antirez는 1월에 작업을 시작하여 첫 달 전체를 명세 문서 작성에 투자했다. 새로운 데이터 타입의 근거, C 구조체, 희소 표현 방식, 링 버퍼와 ARINSERT를 위한 배열 커서의 정확한 시맨틱까지 모두 문서화했다.

처음에는 수일간 직접 손으로 명세를 작성했고, 이후 Opus와 페어링한 뒤 GPT 5.3이 출시되자 Codex로 전환하여 이후 모든 설계와 개발을 GPT 5.x로 진행했다. AI와의 반복적 피드백 — 지적 도전, 최선의 설계 토론, 과잉 설계 여부 검토 — 을 통해 명세가 크게 진화했다.

> To write the initial huge specification was the key to the successive work, as it was the key to review each single line of sparsearray.c and t_array.c

antirez 본인이 명시적으로 밝히듯, 거대한 초기 명세를 작성한 것이 이후 AI 코딩과 인간의 코드 리뷰 모두의 성공 열쇠였다.

## 희소 배열의 3단계 구조

2개월차에 자동 프로그래밍(auto coding)으로 구현에 들어갔다. 그런데 곧 원래 설계한 2단계 간접 참조(디렉토리 + 슬라이스)로는 `ARSET myarray 293842948324 foo`처럼 극단적으로 큰 희소 인덱스를 감당할 수 없다는 것을 발견했다.

AI가 있었기에 타협하지 않았다. 일정 조건에서 자료구조가 내부적으로 형태를 전환하도록 설계를 변경했다.

- **슈퍼 디렉토리** → 슬라이스된 **밀집 디렉토리** → 실제 **배열 슬라이스**(기본 4,096개 원소)

이 3단계 구조가 제공한 것은 세 가지다.

- 내부적으로 "실제 배열" 표현을 유지
- 극단적 희소 인덱스에서도 메모리 효율성 확보
- ARSCAN, ARPOP에서 실존하는 원소 수에 비례하는 순회 성능 (범위 크기가 아니라)

## 동작하는 코드와 최적인 코드의 간극

모든 코드가 작동하고 대규모 테스트(AI 덕분에 방대한 테스트가 생성됨)를 통과한 뒤에, antirez는 한 줄씩 전수 검토를 시작했다. 표면적으로 작동하는 것이 최적이라는 뜻은 아니었다. 작은 비효율이나 원치 않는 설계 오류가 곳곳에서 발견되었고, 여러 모듈을 수동 및 AI 보조로 재작성했다.

3개월차에는 다양한 방식으로 스트레스 테스트를 수행하여 구현이 실제로 견고하고 잘 설계되었다는 확신을 얻었다.

## ARGREP: 유스케이스 모델링에서 탄생한 기능

다양한 사용 사례를 모델링하던 중, 마크다운 파일을 Redis 배열에 넣어 보았다. 파일이 이 자료구조와 매우 잘 맞았고, 에이전트 작업에 필요한 스킬 마크다운 파일의 중앙 집중 지식 베이스를 구현할 수 있다는 것을 깨달았다. 여기서 ARGREP 명령이 탄생했다.

정규식도 지원해야 했는데, Redis처럼 공개 입력을 받는 시스템에서는 시간·공간 양쪽 모두에서 병적 패턴(pathological pattern)이 없어야 한다. TRE 라이브러리(Ville Laurikari)가 이 요건을 충족했다. 다만 `foo|bar|zap` 같은 흔한 OR 패턴이 비효율적이어서 GPT와 함께 최적화하고, 잠재적 보안 이슈를 수정하고, 테스트를 확장했다.

## AI는 복잡성에 도전하게 해주는 안전망

antirez가 전체 과정에서 얻은 최대 깨달음은 이렇다.

> For high quality system programming tasks you have to still be fully involved, but I ventured to a level of complexity that I would have otherwise skipped.

고품질 시스템 프로그래밍에서 인간은 여전히 완전히 관여해야 한다. 하지만 AI 덕분에 평소라면 회피했을 복잡도에 도전할 수 있었다. AI가 안전망 역할을 한 두 영역은 구체적이다.

- **반복 노동**: 32비트 지원처럼 거대하고 지루한 작업의 구현과 테스트
- **복잡 알고리즘 검증**: 복잡한 알고리즘에서 명백한 버그가 없는지 확인하는 가상 인력 역할

이 두 영역은 창의적 판단이 아닌 확인과 노동이며, 정확히 그 지점에서 AI가 가장 효과적이었다.

## 출처

antirez (Salvatore Sanfilippo) · 2026년 5월
원문: <https://antirez.com/news/164>
PR: <https://github.com/redis/redis/pull/15162>
