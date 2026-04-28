---
title: "Building with Anthropic Claude: Prompt Workshop — Zack Witten"
date: 2026-04-28T20:30:00+09:00
tags: ["AI", "코딩 에이전트", "Claude", "프롬프팅"]
categories: ["다이제스트"]
summary: "Building with Anthropic Claude: Prompt Workshop — Zack Witten"
ShowToc: true
TocOpen: false
---

> AI-Assisted Engineering Talk #11/27 · [원본 보고서](https://pages.eiaserinnys.me/p/8d0f6ed0ef4a)

프롬프트 엔지니어링 발표는 많지만, Anthropic의 공식 prompt engineer가 직접 청중의 프롬프트를 받아서 실시간으로 뜯어고치는 워크숍은 드물지요. Zack Witten은 70분 동안 XML 태그, prefill, few-shot 예시, 시스템 프롬프트 분리까지 Anthropic이 실제로 권하는 기법을 하나하나 시연했습니다. 그리고 그 모든 기법을 합쳐도 좋은 예시 하나에 미치지 못한다고, 아주 단호하게 말했습니다.


## 핵심 주장 5가지


워크숍에서 반복적으로 강조된 다섯 가지 핵심 주장입니다. 각각이 독립적인 기법이면서 하나의 철학을 공유합니다 — 모호함을 제거하라.


## 19개 프롬프트 기법 카탈로그


워크숍에서 추출된 18개 실전 기법과 1개 인사이트입니다. 6개 카테고리로 정리했습니다.


### 프롬프트 구조화


### 구체성과 출력 제어


### Prefill과 포맷 강제


### Few-Shot 예시 전략


### 시스템 프롬프트와 역할


### 평가 / 다국어 / 멀티모달


## 예시가 지시보다 검증 밀도가 높은 이유


### Zack + Dan + 명제 프레임워크의 수렴


Few-shot 예시 하나가 톤, 포맷, 추론 패턴, 내용 범위를 동시에 제약합니다.
    명시적 지시 여러 개에 해당하는 검증 표면을 단일 예시가 인코딩하는 것이지요.


Zack의 "everything else combined"와 Dan의 "1~2개 plateau"가 모두 이 밀도 모델로 설명됩니다.
    예시의 검증 밀도가 높으니 적은 수로도 충분하고, 과잉 시에는 노이즈가 신호를 넘어서는 것입니다.
    3개의 독립된 관찰(Zack의 실증, Dan의 데이터, 명제 프레임워크)이 같은 설명으로 수렴한 것이 이 인사이트의 핵심입니다.


## 교차 연결


이 워크숍은 27편 발표 영상 시리즈 중 다른 발표들과 명확한 교차 지점을 가지고 있습니다.


### Dan과의 공유 기법 (영상 #9)


### Zack 고유 기법 (Dan에 없음)


### Dan 고유 기법 (Zack에 없음)


### 명제와의 관계: 에이전트 자율성 ≡ 검증 표면의 함수


Zack의 워크숍은 명제의 입력측 검증 표면에 대한 실전 매뉴얼입니다.

- "code > prompt" = 검증 표면을 확률적(prompt)에서 결정론적(code)으로 이전
- "few-shot > instructions" = 검증 표면의 밀도가 면적보다 중요
- "stop sequence + prefill" = API 수준에서 출력 검증 표면을 구조적으로 보장

기존 명제 "면적이 아니라 위치와 밀도의 문제"를 Anthropic 내부자가 실증적으로 재확인한 셈이지요.

## 출처

- [원본 HTML 보고서](https://pages.eiaserinnys.me/p/8d0f6ed0ef4a)
