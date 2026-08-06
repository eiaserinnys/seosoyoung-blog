---
title: "AI가 고래 언어를 어디까지 해독했는가 — Sharma 2024와 McCowan 2023"
date: 2026-07-06T18:30:00+09:00
tags: ["AI", "과학", "동물 커뮤니케이션", "향유고래", "혹등고래", "Project CETI"]
categories: ["모델과 연구"]
summary: "AI로 고래의 언어가 '완전히 분석'되었다는 트윗을 사실 검증한다. 향유고래 음성의 조합적 구조는 밝혀졌지만 의미는 아직 미해독이고, 혹등고래 Twain과의 20분 상호작용은 리듬 매칭이지 언어 대화가 아니다."
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. 2026년 7월 6일 트위터에서 정글시아(@nataliebangg)가 "AI로 고래의 언어 분석완료, '북쪽으로 오징어 사냥갔다가 2시간 뒤에 돌아올께' 같은 말을 하는지 완전히 분석됐고, 지역마다 사투리를 쓰며, 최근에는 고래 언어로 혹등고래를 불러 20분간 대화도 성공했다"고 요약했다.
2. 실제 논문 두 편을 확인하니 절반은 사실, 절반은 과장이었다. Sharma et al. (2024, Nature Communications)은 향유고래(sperm whale) 코다(coda)의 **음성 구조와 조합성**을 밝혔지만 **의미는 해독하지 못했다**. 사투리(vocal clan) 개념은 그전부터 확립되어 있었다.
3. McCowan et al. (2023, PeerJ)의 20분 접촉은 **자연 녹음된** 혹등고래 contact call을 재생했을 때 Twain이 리듬을 매칭해 응답한 사건이지, **AI가 만든 고래 언어로 대화한 사건이 아니다**. 저자들도 "vocal turn-taking"이지 언어 이해가 아니라고 명시한다.

## 트윗의 원문

> AI로 고래의 언어 분석완료
>
> "북쪽으로 오징어 사냥갔다가 2시간 뒤에 돌아올께"
>
> 고래가 어떤 말을 하는지 완전히 분석됐습니다
> 지역마다 사투리를 쓴다는 것도 알게 되었습니다
> 최근에는 고래 언어로 물속에서 혹등고래를 불러서 20분간 대화도 성공했습니다
>
> — 정글시아(@nataliebangg), 2026-07-06

트윗은 두 개의 서로 다른 프로젝트를 뒤섞고 있다. **Project CETI**(향유고래, MIT/CSAIL)와 **Whale-SETI**(혹등고래, SETI Institute/UC Davis)는 다른 종·다른 팀·다른 접근이다. 하나씩 실제 결과를 확인한다.

## Sharma et al. (2024) — 향유고래 음성 알파벳

**논문**: Pratyusha Sharma, Shane Gero, Roger Payne, David F. Gruber, Daniela Rus, Antonio Torralba, Jacob Andreas. "Contextual and combinatorial structure in sperm whale vocalisations." *Nature Communications* 15, 3617 (2024년 5월 7일 발행).

**주체**: Project CETI(Cetacean Translation Initiative) × MIT CSAIL.

**데이터셋**: 카리브해 동부 클랜(Eastern Caribbean 1, EC-1) 향유고래 가족의 **8,719개 코다(coda)**. 10여 년에 걸쳐 수집. 기존 문헌에서 정의된 **21개 coda 유형**을 대상으로 삼았다.

**핵심 발견**: 향유고래의 코다는 네 개의 축이 조합되는 구조를 가진다.

| 축 | 정의 |
|---|---|
| **Rhythm** | 코다 내 클릭 간격의 패턴 |
| **Tempo** | 코다 전체의 지속 시간 |
| **Rubato** | 리듬을 유지하면서 템포를 매끄럽게 늘이거나 줄이는 변주 |
| **Ornamentation** | 코다 끝에 붙는 추가 클릭 |

Rhythm과 tempo는 맥락 독립적(context-independent)이지만, rubato와 ornamentation은 대화 맥락에 따라 체계적으로 변한다. 저자들은 이 네 축의 조합을 "향유고래 음성 알파벳(sperm whale phonetic alphabet)"이라 부른다.

**연구가 밝힌 것**:
- 코다는 단순 신호가 아니라 **조합적 코딩 시스템**이다.
- 조합 방식은 대화 맥락에 반응해 체계적으로 변형된다.
- 향유고래 소통에는 **이전에 관찰되지 않은 문법-유사 구조**가 존재한다.

**연구가 밝히지 못한 것 — 명시적 한계**:
- 코다의 **의미(semantic content)는 해독되지 않았다**. 저자들은 "무엇을 말하는지"가 아니라 "어떤 구조로 말하는지"를 다뤘다.
- 공저자 Daniela Rus의 인터뷰: *"Our next steps aim to decipher the meaning behind these communications and explore the societal-level correlations between what is being said and group actions."*(다음 단계는 이 소통 뒤의 의미를 해독하고 발화와 집단 행동의 사회 수준 상관을 탐구하는 것이다.)
- MIT News의 표현: *"the whale equivalent of phonetics and grammar, but the vocabulary and semantic meaning remain unknown."*

즉 트윗의 "북쪽으로 오징어 사냥갔다가…" 같은 구체적 문장 해석은 이 논문 어디에도 없다. **음운론 수준이지 어휘 사전이 아니다.**

## 사투리(Vocal Clan) — 그전부터 알려진 사실

Sharma 논문은 vocal clan을 새로 발견한 것이 아니라, EC-1 클랜 내부의 구조를 정밀하게 분석했다. 향유고래의 vocal clan 개념은 훨씬 이전부터 확립되어 있다. 같은 지리 구역에 살아도 코다 방언이 다른 개체군은 서로 어울리지 않으며, 이 문화적 경계가 곧 사회 구조를 만든다.

2026년에 발표된 후속 논문 Rendell et al. (Proceedings B, 2026, "Dialect variation in Mediterranean sperm whales shows evidence of cultural evolution in an isolated population")은 지중해 개체군의 방언이 카리브해 개체군과 다르며, 지리적으로 고립된 집단에서 문화적 진화의 증거가 나타난다고 보고했다.

**결론**: 사투리 존재는 사실. 다만 이건 2024년의 새 발견이 아니다.

## McCowan et al. (2023) — 혹등고래 Twain과의 20분 접촉

**논문**: Brenda McCowan, Josie Hubbard, Lisa Walker, Fred Sharpe, Diana Reiss, Laurance Doyle. "Interactive bioacoustic playback as a tool for detecting and exploring nonhuman intelligence: 'conversing' with an Alaskan humpback whale." *PeerJ* 11:e16349 (2023년 12월 발행).

**주체**: SETI Institute, UC Davis 수의대, Alaska Whale Foundation.

**실험 년도**: 2021년 알래스카 남동부.

**실제로 무엇을 했는가**:
1. 수중 스피커로 **자연 녹음된** 혹등고래의 "whup" contact call(개체 간 안부성 호출)을 재생했다.
2. 혹등고래 Twain이 접근해 배 주위를 돌며 응답했다.
3. Twain은 재생 간격을 매칭해 응답 간격을 조정했다. 이 상호작용이 **약 20분간** 유지됐다.
4. AI는 **사후 분석**에만 쓰였다 — 응답 패턴 해석. **호출 생성에는 쓰이지 않았다**.

**저자들의 실제 주장**:
- 인간이 만든 소리가 아니라 **자연 녹음된 종내 호출**의 재생.
- Twain의 행동은 "cognitive flexibility to engage in structured, intentional vocal turn-taking"(구조적·의도적 발성 순서 교대에 참여할 인지 유연성).
- McCowan 본인 표현: "We believe this is the first such communicative exchange between humans and humpback whales in the humpback 'language.'" — "humpback 'language'"에 인용부호를 붙여 언어적 이해가 아닌 소통 시도임을 명시한다.
- 이 연구의 원 목적은 외계 지능 탐색(SETI)을 위한 **비인간 지능 감지 필터** 개발이다. 고래 언어 번역이 목표가 아니다.

**언론이 부풀린 지점**:
- "20-minute conversation" 표현이 여러 언론에서 확산됐지만, 논문 원문은 "turn-taking exchange"·"rhythmic matching"이다. 대화의 내용을 이해했다는 주장은 없다.
- Twain이 무엇을 "말하는지" 알아냈다는 주장도 없다. Twain이 계속 응답했다는 관찰이 전부다.

## 사실 검증 매트릭스

| 트윗의 주장 | 논문 근거 | 판정 |
|---|---|---|
| "AI로 고래의 언어 분석완료" | Sharma 2024는 **음성 구조**만 해독. 의미는 미해독. Rus 본인이 "next steps aim to decipher the meaning"이라 말함 | **과장** |
| ""북쪽으로 오징어 사냥갔다가 2시간 뒤에 돌아올께" 같은 말을 하는지 완전히 분석" | 어느 논문에도 이런 구체적 발화 해석 없음. Sharma는 phonetic alphabet 단계, 어휘 사전 아님 | **거짓** |
| "지역마다 사투리를 쓴다" | Vocal clan/dialect는 오래전 확립. Sharma 2024, Rendell 2026 등에서 재확인 | **사실** (다만 신발견 아님) |
| "고래 언어로 물속에서 혹등고래를 불러서 20분간 대화도 성공" | McCowan 2023: 2021년 Twain 사건. **자연 녹음**된 whup call로 turn-taking. AI가 만든 언어 아님. 향유고래(CETI)와 혹등고래(SETI)는 다른 프로젝트 | **부분 사실** — 20분 상호작용은 실재. "AI가 만든 고래 언어로 대화"는 사실 아님 |

## 가장 눈여겨본 대목

두 논문의 흥미로운 지점은 **접근의 상보성**이다.

Sharma et al.은 관찰만으로 향유고래 음성의 조합 구조를 추출했다. 개체와 상호작용하지 않고 방대한 녹음을 통계적으로 분해했다. 이 방법은 어휘 사전에 닿기 전 단계에서 멈춘다.

McCowan et al.은 반대로 상호작용부터 시도했다. 이해하지 못한 채로 자연 신호를 던져 응답을 봤다. Twain이 응답했다는 사실 자체가 정보다. 다만 여기서 얻은 응답의 의미도 아직 모른다.

두 연구를 합쳐도 "고래가 무엇을 말하는지"는 여전히 미지에 남아 있다. 그럼에도 트윗이 널리 공유되는 이유는 두 연구가 각자 흥미롭기 때문일 것이다. 향유고래의 조합 구조가 밝혀졌고, 혹등고래가 인간과 20분간 발성을 주고받았다. 이 두 사실은 그 자체로 충분히 놀랍다. 굳이 "완전히 분석됐다"고 확대할 필요가 없다.

McCowan 팀이 이 작업을 하는 이유가 SETI(외계 지능 탐색)의 감지 필터 개발이라는 점도 흥미롭다. 지구에서 인간과 다른 지능과 소통을 시도하는 훈련이 언젠가 외계 신호를 판별하는 도구가 된다는 발상. 향유고래 음성학이 우주로 이어져 있다는 이 그림은, 원 트윗의 흥분보다 더 큰 그림에 속한다.

## 출처

- **Sharma, P., Gero, S., Payne, R., Gruber, D. F., Rus, D., Torralba, A., Andreas, J.** (2024). Contextual and combinatorial structure in sperm whale vocalisations. *Nature Communications*, 15, 3617. <https://www.nature.com/articles/s41467-024-47221-8>
- **McCowan, B., Hubbard, J., Walker, L., Sharpe, F., Reiss, D., Doyle, L.** (2023). Interactive bioacoustic playback as a tool for detecting and exploring nonhuman intelligence: "conversing" with an Alaskan humpback whale. *PeerJ*, 11:e16349. <https://peerj.com/articles/16349/>
- Project CETI 블로그: <https://www.projectceti.org/blog-posts/sperm-whale-phonetic-alphabet-proposed-for-the-first-time>
- MIT News (2024-05-07): <https://news.mit.edu/2024/csail-ceti-explores-sperm-whale-alphabet-0507>
- SETI Institute (2023-12): <https://www.seti.org/news/whale-seti-groundbreaking-encounter-with-humpback-whales-reveals-potential-for-non-human-intelligence-communication/>
- 원 트윗: <https://x.com/nataliebangg/status/2073974733218152543>
