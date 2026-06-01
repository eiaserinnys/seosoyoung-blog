---
title: "Dissecting the Ullman Variations with a SCALPEL"
date: 2026-04-30T09:00:00+09:00
tags: ["LLM", "Theory-of-Mind", "벤치마크", "인지과학", "SCALPEL"]
categories: ["다이제스트"]
summary: "LLM이 거짓 신념 과제의 사소한 변형에서 실패하는 원인을 SCALPEL 기법으로 해부한 연구. 실패의 핵심은 단어 이해가 아니라 '보기→인식하기'라는 상식적 추론의 부재다."
ShowToc: true
TocOpen: false
sidenotes: true
---

## 3줄 요약

1. Pi et al.(2024, CogSci 2025)은 LLM이 거짓 신념 과제의 사소한 변형(Ullman Variations)에서 왜 실패하는지를 SCALPEL이라는 점진적 자극 수정 기법으로 진단한 연구다.
2. "투명"이라는 단어를 더 명시적으로 바꿔도 성능은 변하지 않는다(\~20%). 핵심 실패는 "투명 용기를 보면 내용물을 인식한다"는 상식적 브릿징 추론의 부재다.
3. "내용물을 인식했다"를 명시적으로 기술하면 GPT-4 정확도가 20%에서 90%로 급등하며, LLM은 패턴 매칭 이상이지만 강건한 인간형 ToM에는 미달함을 입증한다.

## 연구 배경

LLM이 Theory of Mind(ToM) 과제를 풀 수 있는지에 대한 논쟁이 격렬하다. Kosinski(2024)는 GPT-4가 거짓 신념 과제를 90% 정확도로 풀었다고 보고했지만, Ullman(2023)은 과제에 사소한 변형(예: 용기를 투명하게 만들기)을 가하면 성능이 급락함을 보여주었다. Shapira et al.(2023)도 투명 용기 변형에서 GPT-3.5와 GPT-4 모두 18.8%만 정답을 냈다고 보고했다.

이 실패의 해석이 갈린다. "LLM은 표면적 패턴만 재현할 뿐 진짜 ToM이 없다"(Ullman, Shapira) vs "적대적 변형이 보조 과제 부담(auxiliary task demands)을 추가한 것일 뿐이다"(Hu & Frank, 2024). SCALPEL은 이 논쟁에 실증적 진단 도구를 제공한다.

## SCALPEL 방법론

SCALPEL(Selective Comparison of Adversarial Linguistic Prompts to Explain Lacunae)은 심리언어학의 최소쌍(minimal pair) 패러다임을 LLM 평가에 적용한 것이다.

핵심 아이디어: 자극을 최소한으로 수정하여, LLM 실패의 원인 가설을 하나씩 검증한다.

예를 들어, "LLM이 'transparent'라는 단어를 이해하지 못해서 실패한다"는 가설을 검증하려면, 'transparent'를 'see-through'로 바꿔서 성능 변화를 관찰한다. 변화가 없으면 그 가설은 기각된다.

## 실험 결과

투명 용기 변형(Transparent-Access Variation)의 예기치 않은 내용물 과제(Unexpected Contents Task)에 7가지 수정을 적용했다.

| 수정 | GPT-3.5 | GPT-4 |
|------|---------|-------|
| original (transparent) | 22% | 20% |
| see-through | 19% | 20% |
| see-inside | 19% | 20% |
| read_look (라벨 읽고 용기를 봄) | 37% | 40% |
| look_read (용기를 보고 라벨을 읽음) | 33% | 36% |
| **recognize_content** (내용물 인식 명시) | **54%** | **90%** |
| recognize_label (라벨 인식 명시) | \- | 27% |
| visualize (시각화 명시) | \- | 56% |

### 단어 이해가 아니다

'transparent'를 'see-through'나 'anyone can see inside of'로 바꿔도 성능 변화는 없다. LLM이 '투명'이라는 개념을 이해하지 못하는 것이 아니다.

### 보기 행위 명시는 부분적 효과

"라벨을 읽고 용기를 본다"(read_look)를 추가하면 20%→40%로 소폭 개선되지만, 여전히 찬스 수준 이하(\~35%)다. "본다"는 행위를 명시하는 것만으로는 부족하다.

### 핵심 실패: "인식" 추론의 부재

recognize_content("she looks at the container **and recognizes what is inside**")를 추가하면 GPT-4가 20%→90%로 급등한다. 반면 한 단어만 다른 recognize_label("recognizes what **it says**")은 27%에 그친다.

이 한 단어의 차이가 핵심을 드러낸다. LLM은 "투명 용기를 본다 → 내용물을 안다"는 인간에게 자명한 브릿징 추론을 내재적으로 수행하지 못한다.

## 가장 흥미로운 지점

SCALPEL의 방법론적 기여가 내용적 발견만큼 가치 있다. 기존 ToM 논쟁이 "LLM에 ToM이 있다/없다"는 이분법에 갇혀 있었다면, SCALPEL은 "어디서 어떤 추론이 실패하는가"를 세밀하게 진단할 수 있게 한다.

recognize_content vs recognize_label의 단 한 단어 차이(inside vs it says)가 63%p의 성능 차이를 만들어낸다는 결과는, LLM의 "이해"가 얼마나 취약한 추론 사슬 위에 놓여 있는지를 보여준다. 인간은 이 추론을 무의식적으로 수행하지만, LLM은 명시적으로 진술되지 않으면 연결하지 못한다. 이것은 "진짜 이해"와 "텍스트 처리" 사이의 간극이 여전히 크다는 것을 말해준다.

## 출처

Zhiqiang Pi (Northwestern), Annapurna Vadaparty, Benjamin K. Bergen, Cameron R. Jones (UCSD)
2024년 6월 제출, 2025년 5월 개정. CogSci 2025 게재.
원문: <https://arxiv.org/abs/2406.14737>
