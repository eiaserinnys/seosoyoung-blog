---
title: "Introducing FrontierCode"
date: 2026-06-09T22:30:00+09:00
tags: ["AI", "벤치마크", "코딩 에이전트", "LLM 평가", "Cognition", "오픈소스"]
categories: ["모델과 연구"]
summary: "Cognition이 공개한 신규 코딩 벤치마크. 정답 여부가 아니라 '메인테이너가 실제로 머지하겠는가'를 측정한다. Diamond 50문항에서 최강 모델 Claude Opus 4.8도 13.4%에 그쳤다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/frontier-code-benchmark/cover.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/frontier-code-benchmark/cover.png"
---

## 3줄 요약

1. Cognition은 코드의 *정답 여부* 대신 <em>병합 가능성(mergeability)</em>을 측정하는 신규 벤치마크 FrontierCode를 공개했다. 36개 플래그십 오픈소스 리포의 메인테이너 20여 명이 태스크당 40시간 이상을 투입했다.
2. 가장 어려운 50문항(Diamond) 기준 최강 모델 Claude Opus 4.8이 13.4%, GPT-5.5가 6.3%에 그쳤다. 다만 GPT-5.5는 토큰을 4배 적게 써 비용-지능 트레이드오프 면에서는 더 낫다고 평가됐다.
3. SWE-Bench Pro 대비 오분류율(false positive)을 81% 낮췄다. 정답 테스트 위주 채점에서 벗어나, 역방향 테스트(reverse-classical), 스코프 제한, mutagent 기반 적응형 채점 등 신규 기법을 더했다.

## 무엇을 측정하는가 — "메인테이너가 머지하겠는가"

기존 코딩 벤치마크(SWE-Bench Verified·Pro 등)는 *기능적 정확성*만 본다. Cognition은 모델이 정답을 적어 내는 수준은 이미 넘어섰다고 본다. 다음 질문은 "이 PR이 실제 프로덕션 코드베이스에 병합될 만한가"이다.

FrontierCode가 평가하는 6개 축은 다음과 같다.

| 축 | 의미 |
|---|---|
| Behavioral correctness | 패치가 문제를 실제로 해결하는가 |
| Regression safety | 기존 코드베이스에 회귀를 일으키지 않는가 |
| Mechanical cleanliness | 빌드·린트·스타일 체크를 통과하는가 |
| Test correctness | 에이전트가 작성한 테스트가 실제로 의도를 잡아내는가 |
| Scope | 패치가 필요한 부분만 건드리는가 |
| Code quality | 코드베이스 컨벤션·설계 패턴·가독성을 따르는가 |

각 채점 항목은 **blocker**(머지 차단 사유)와 **non-blocker**(품질 신호)로 나뉜다. blocker를 하나라도 통과하지 못한 솔루션은 점수 0점이다.

## 세 난이도 등급의 결과

FrontierCode는 난이도가 다른 세 묶음을 중첩 구조로 제공한다.

- **Diamond**: 가장 어려운 50문항
- **Main**: 가장 어려운 100문항 (Diamond 포함)
- **Extended**: 전체 150문항

각 모델을 추론 강도별로 5회씩 돌려 평균을 낸 뒤, 가장 잘 나오는 추론 강도의 점수를 보고한다.

| 모델 | Diamond | Main | Extended |
|---|---|---|---|
| Claude Opus 4.8 | **13.4%** | **34.3%** | **51.8%** |
| GPT-5.5 | 6.3% | — | — |
| Gemini 3.1 Pro | 4.7% | — | — |
| Kimi K2.6 (최고 오픈소스) | 3.8% | 16% | 37% |

Diamond는 여전히 포화되지 않았다. 최고 모델조차 87%의 태스크에서 머지 가능한 PR을 만들어 내지 못한다는 뜻이다. 한편 GPT-5.5는 Opus 4.8 대비 토큰을 4배 적게 쓰면서도 일정 수준을 유지해 비용-지능 트레이드오프에서는 더 낫다고 명시됐다.

오픈소스와 프런티어 모델 사이 격차도 두드러진다. Kimi K2.6은 Diamond에서 3.8%, Main에서 16%로 격차가 크다.

## 81% 더 정확한 채점 — 오분류 감소

기존 벤치마크의 가장 큰 약점은 *오분류*다. METR은 SWE-Bench에서 높은 점수를 받은 모델의 패치 중 상당수가 실제로는 메인테이너가 머지하지 않을 코드라는 점을 보고했다.

오분류는 두 갈래로 나뉜다.

- **False Positive**: 채점기가 *틀린* 솔루션을 통과시키는 경우. 테스트 커버리지가 불완전할 때 발생.
- **False Negative**: 채점기가 *맞는* 솔루션을 떨어뜨리는 경우. 테스트가 함수명·에러 문자열을 너무 좁게 검사하거나, 명세에 없는 동작을 요구할 때 발생.

![Trajectory false positive and false negative rates by benchmark](https://img.seosoyoung.eiaserinnys.me/images/frontier-code-benchmark/false-positive-negative-rates.svg)

FrontierCode는 에이전트 trajectory 분석을 통해 SWE-Bench Pro 대비 오분류 발생률을 81% 낮췄다고 보고한다. Cognition은 이 수치가 "현재 가장 정확한 모델 순위"의 근거라고 주장한다.

## 다양성 — 언어·태스크 형태·프롬프트 길이

기존 벤치마크는 단일 PR을 프로그래밍 방식으로 스크래핑해 만들었다. FrontierCode는 메인테이너가 다중 PR 체인과 자유형 요청에서 직접 골라냈다. 표현 언어 수는 SWE-Bench Pro의 3배.

![Language composition by benchmark, normalized for task count](https://img.seosoyoung.eiaserinnys.me/images/frontier-code-benchmark/language-composition.svg)

프롬프트 길이도 다르다. 기존 벤치마크는 과도하게 상세한 안내를 주어 모델이 받아쓰기에 가까운 작업을 한다. FrontierCode의 프롬프트는 SWE-Bench Pro의 1/3 길이이며, 메인테이너의 의도를 *추론*해야 한다.

![FrontierCode prompt length distribution](https://img.seosoyoung.eiaserinnys.me/images/frontier-code-benchmark/prompt-length.svg)

난이도는 패치 크기를 키워서 올리지 않았다. 오히려 DeepSWE 등보다 패치가 더 작아도, *품질 루브릭*으로 난이도가 올라간다.

![FrontierCode patch size distribution](https://img.seosoyoung.eiaserinnys.me/images/frontier-code-benchmark/patch-size.svg)

## 신규 채점 기법 3종

FrontierCode는 정답 테스트만으로 잡히지 않는 품질 신호를 위해 세 가지 신규 채점 기법을 도입했다.

**Reverse-Classical** — 에이전트가 작성한 테스트를 *원래의 깨진 코드베이스*에 돌렸을 때 반드시 실패해야 한다. 통과해 버리면 그 테스트는 문제를 실제로 검증하지 못한다는 뜻이다. 에이전트가 문제를 이해했는지 결정론적으로 확인하는 장치다.

**Code Scope** — 좋은 PR은 *절제*한다. 필요한 곳만 건드린다. scope 채점은 세 종류의 제약을 묶는다.

- `files`: 어느 파일을 허용·금지·삭제 대상으로 둘지 결정론적으로 검사
- `size`: 변경 라인 수, 순증 라인 수, 변경 파일 수 상한
- `semantic`: 변경이 특정 함수 안에 머무는지 등 LLM 기반의 *지역성* 검사

**Adaptive Classical Grading (mutagent)** — 열린 문제는 유효한 해가 여러 갈래다. 정답 함수명이나 에러 문구가 살짝 다르다는 이유로 좋은 해가 떨어지는 일을 막기 위해, Cognition은 LLM이 *테스트 환경이나 애플리케이션 코드*를 에이전트의 구현 디테일에 맞춰 외과 수술하듯 손보는 도구 `mutagent`를 만들었다. 그 뒤 결정론적 테스트를 돌린다.

| 채점 방법 | 어떻게 동작하는가 | 통과 조건 |
|---|---|---|
| classical | 테스트 파일을 리포에 주입·실행·정리 | 모든 주입 테스트 통과 |
| command | 셸 명령 실행 | 종료 코드 0 |
| reverse-classical | 에이전트의 테스트를 base commit에 실행 | 테스트가 *실패* |
| adaptive classical | LLM이 레퍼런스 테스트를 에이전트 구현에 맞춰 조정 | 조정된 테스트 통과 |
| scope | 파일·diff 크기·의미적 locality 제약 검사 | 제약 내 |
| prompt | LLM이 자연어 루브릭으로 diff 리뷰 | LLM 점수가 임계값 이상 |

## 예제 — jsonschema 리포의 `LOG_WARNING`

벤치마크 글은 C++ 리포 jsonschema의 한 태스크를 사례로 든다.

> `src/logger.h`에 새 메서드 `auto LOG_WARNING() -> std::ostream &`를 만들어, 모든 경고 로그를 그것으로 감싸라. 경고는 `--verbose`와 무관하게 항상 stderr로 출력되고, `warning:` 접두어가 자동으로 붙어야 한다.

겉보기엔 단순하다. 그러나 한 blocker 기준이 "여러 줄 경고 메시지가 관용적으로 `LOG_WARNING`을 통해 흘러야 한다"는 점을 요구한다. 메인테이너가 기대하는 관용 코드는 다음과 같다.

```cpp
LOG_WARNING() << "You are opting in to remove schema identifiers... \n"
              << "The only legit use case...\n"
              << "non-compliant...\n" << ... ;
```

반면 Claude Opus 4.8은 일관되게 다음 패턴을 고른다.

```cpp
LOG_WARNING() << "You are opting in to remove schema identifiers...\n";
    std::cerr << "The only legit use case...\n";
    std::cerr << "non-compliant...\n";
```

행동상으로는 같다. 두 코드 모두 stderr로 출력한다. 하지만 호출부에서 `LOG_WARNING()`과 `std::cerr`가 동일한 스트림이라는 가정을 굳혀 버린다. 이는 추후 `LOG_WARNING()`이 다른 동작을 갖도록 수정될 가능성을 막는 설계 결함이다. 메인테이너의 시각에서는 머지가 어렵다.

## 루브릭을 어떻게 단단하게 만드는가

이진 채점은 비교적 쉽다. 정답·오답 두 통으로 나뉘니, 통마다 솔루션을 들여다보고 테스트를 강화하면 된다. 루브릭은 다르다. 두 솔루션이 모두 기능상 맞아도 다른 점수를 받을 수 있으니, *상대 평가*가 작동해야 한다.

![Rubric hardening pipeline](https://img.seosoyoung.eiaserinnys.me/images/frontier-code-benchmark/rubric-hardening-pipeline.svg)

Cognition의 루브릭 단단하게 만들기 파이프라인은 5단계다.

1. **Design** — 결정론적으로 확인 가능한 부분은 classical 테스트, 구현 디테일 차이에 견뎌야 하는 부분은 행동 테스트, 관용성·가독성·아키텍처 선호 같은 *부드러운 품질*은 LLM 채점.
2. **Hack report** — 태스크 작성자가 *나태하거나 적대적인 프로그래머*를 흉내내어 일부러 부실한 솔루션으로 점수를 따려 시도한다(False Positive 탐지). 반대로, 정답이지만 정본과 다른 대안 솔루션을 작성해 떨어지는지 본다(False Negative 탐지). 여기에 Devin이 새로운 해킹 방식을 추가로 시도한다.
3. **Calibration** — 작성자는 0%~100% 범위에 분포하는 네 개의 솔루션을 직접 작성해 루브릭의 해상도를 검증한다.
4. **Review** — 풀 리드 → Cognition 연구원 다단 리뷰. 일부 태스크는 연구원이 직접 풀어 보면서 지시문이 명확한지, 채점이 공정한지 확인한다.
5. **Re-Review** — 어느 단계든 되돌릴 수 있다. 대부분의 태스크는 여러 회차의 반복을 거친다.

## 가장 흥미로운 지점

가장 인상적인 부분은 `LOG_WARNING` 예제다. 두 코드가 *행동상 동일*하다는 점이 핵심이다. 정답 여부만 보면 둘 다 통과한다. 그러나 메인테이너의 눈에서 한쪽은 "내일 `LOG_WARNING()`을 다른 스트림으로 바꿔야 할 때 호출부 전체를 다시 손봐야 한다"고 읽힌다. 행동 동일성과 설계 적합성은 별개의 게이트인데, 지금까지의 벤치마크는 앞쪽만 보고 있었던 셈이다.

또 하나, Cognition이 36개 플래그십 오픈소스 리포의 메인테이너에게 *태스크당 40시간*을 들이게 했다는 점이 눈에 띈다. Celery·Budibase·uppy·Mattermost의 코어 메인테이너가 자기 리포의 머지 기준을 루브릭으로 풀어 두었다는 의미다. 평가의 정본이 *모델 제공자가 아닌 코드베이스 소유자* 쪽으로 옮겨가는 흐름이다.

테스트셋 자체는 오염 방지를 위해 공개하지 않는다. 평가 접근은 모든 모델 제공자에게 열어 둔다는 입장이다.

## 출처

발신: Cognition (Devin 개발사)
원문: <https://cognition.ai/blog/frontier-code>
참고: METR, "Many SWE-Bench-passing PRs would not be merged into main" (2026.03)
