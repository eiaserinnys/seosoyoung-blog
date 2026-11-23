---
title: "Foyege의 Seedance 2.5 AI 연기 프롬프트: 감정을 눈에 보이고 귀에 들리는 연기로 분해하기"
date: 2026-11-23T08:30:00+09:00
tags: ["Seedance", "영상 생성", "프롬프트 엔지니어링"]
categories: ["창작과 문화"]
subjects: ["이미지와 영상 제작"]
summary: "더우인 조회수 412만 회를 기록한 Foyege의 30초 AI 연기 단편(<펜스> 오마주) 원본 프롬프트와 7분 21초짜리 해설 강좌를 추적해 3계층 프롬프트 구조, FACS 근육 부호화, 8차원 연기 공식을 정리한다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/00-cover-dialogue-split.jpg"
  alt: "Foyege의 Seedance 2.5 30초 AI 연기 단편 해설 화면. 눈물이 고인 흑인 여성 캐릭터의 클로즈업과 'What about my life? What about me?' 대사의 3단계 동작 분해가 함께 표시되어 있다."
  og_focus: "58%"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/00-cover-dialogue-split.jpg"
---

## 3줄 요약

1. <해리 포터> 성전환 말포이 AI 팬필름 시리즈로 이름을 알린 창작자 Foyege(弗曳哥)가 더우인에서 412만 번 넘게 재생된 30초짜리 AI 연기 단편의 원본 프롬프트(3,668자)와 해설 강좌(7분 21초)를 공개했다.
2. 이 영상은 어거스트 윌슨의 희곡 <펜스>(*Fences*) 2막 1장에서 부부가 대립하는 장면을 옮긴 것이다. 바이트댄스 샤오윈췌 AI(Seedance 2.5)에서 참고 영상이나 참고 이미지 없이 텍스트 프롬프트만으로 단 1회 생성했다.
3. Foyege는 "그녀는 슬프다" 같은 추상적 감정 라벨 대신 프롬프트를 전역 제어, 샷 타임라인, 연기 제어의 3계층으로 구성한다. 여기에 인물 목적, 대사 트리거, FACS 안면 근육 동작 단위(AU), 금지 반응을 결합한 8차원 연기 공식을 써서 30초 동안의 감정 변화를 제어한다.

## 1차 자료 추적: 412만 조회수 단편의 정체와 원작 희곡

2026년 11월 22일 X 계정 `@VibeEverything`은 창작자 Foyege의 30초 AI 연기 단편 프롬프트 작성법을 10장의 한국어 슬라이드로 요약해 소개했다.[^1] 요약본만 보면 일반적인 프롬프트 팁처럼 읽히지만, Foyege가 Vibe Shot Club에 공개한 7분 21초 분량의 원본 강좌 영상(유튜브에는 5분 40초 편집본 게시)과 빌리빌리(Bilibili)에 올린 3,668자 프롬프트 전문(`黑人演员完整提示词`)을 대조하면 구체적인 제작 조건과 원작 희곡이 확인된다.[^2]

![Foyege가 공개한 더우인 412만 2,000회 조회수 및 24만 2,000개 좋아요 통계 화면](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/01-viral-proof.jpg)
*2026년 8월 1일 더우인에 게시된 30초 AI 연기 단편의 성과 지표(조회수 412만 2,000회, 좋아요 24만 2,000개, 공유 5만 1,000회). 출처: Foyege, Vibe Shot Club 강좌 영상.*

Foyege는 1998년생이고 디지털 멀티미디어를 전공했다. 2026년 가을에는 그가 만든 <해리 포터> 성전환 말포이(*Draconia Malfoy*, 《在另一个宇宙》) 시리즈가 해외에서 누적 3,000만 뷰를 넘기며 주목받았다. 그 직전인 2026년 8월 1일, Foyege는 더우인에 흑인 부부의 말다툼을 그린 30초짜리 단편을 올렸다. 이 영상에 조회수 412만 2,000회와 좋아요 24만 2,000개가 몰리며 크게 화제가 되자, "실제 영화 영상을 참고 영상(Video-to-Video)으로 넣은 것 아니냐"며 의심하는 댓글이 달렸다. Foyege는 강좌 도입부에서 샤오윈췌 AI(小云雀AI)의 포인트 차감 내역(`08/01 14:21`, `短剧视频2.5生成 720p`, `780积分`)을 화면으로 보여 주었다. 샤오윈췌 AI는 바이트댄스의 크리에이티브 에이전트 작업 환경이다. 그는 참고 영상도 인물 시트 이미지도 넣지 않고 3,668자의 중국어 텍스트 프롬프트만으로 단 1회 생성에 성공했다고 밝혔다.

3,668자 프롬프트에 적힌 영어 대사를 원문 그대로 추적해 보면, 미국 극작가 어거스트 윌슨(August Wilson)의 희곡 **<펜스>**(*Fences*) 2막 1장이 이 30초 단편의 바탕 텍스트임을 알 수 있다. 이 작품은 1985년에 초연되어 1987년 퓰리처상과 토니상을 받았으며, 2016년에는 덴젤 워싱턴과 비올라 데이비스 주연의 동명 영화로도 제작됐다. 이 장면은 남편 트로이 맥슨(Troy Maxson)이 외도를 고백한 직후, 아내 로즈 맥슨(Rose Maxson)이 18년 동안 억눌러 온 자신의 삶과 희생을 토해내는 대목이다. 현대 연극사의 대표적인 독백 장면이다. Foyege는 실존 배우의 외모를 따라 하지 말라는 조건을 프롬프트 앞부분에 적어 두고, 원작의 대사와 감정 변화를 4개 샷 분량의 촬영 대본으로 재구성했다.

| 항목 | 2차 요약 (`@VibeEverything`) | 1차 원문 (Foyege 강좌 영상 및 3,668자 원본 프롬프트) |
| --- | --- | --- |
| 생성 환경 및 비용 | Seedance 2.5, 참고 영상과 이미지 없이 1회 생성 | 바이트댄스 샤오윈췌 AI 무한 캔버스, Seedance 2.5 (720p, 30초, 20대 9 화면비), 780포인트 소모 |
| 프롬프트 분량 | 언급 없음 | 중국어 원문 3,668자 (영어 대사 전문 포함) |
| 원작 희곡 | "20세기 중반 미국 노동자 가정의 뒷마당 현관 말다툼" | 어거스트 윌슨 희곡 <펜스>(*Fences*) 2막 1장 트로이와 로즈의 대립 장면 |
| 샷 구성 | 3개 샷 (샷 1 남자 0\~3.7초, 샷 2 여자 3.7\~23초, 샷 3 남자 리액션 23\~30초) | **4개 샷** (샷 3 남자 무언 리액션 23.0\~29.0초 뒤에 **샷 4 여자 익스트림 클로즈업 29.0\~30.0초**가 따로 있다) |

## 왜 30초인가: 표정 하나에서 장면 전체의 연기로

Foyege의 진단은 이렇다. 기존 AI 영상 모델은 한 번에 생성하는 길이가 몇 초에 불과했다. 그러나 Seedance 2.5는 한 번의 생성으로 30초 분량의 이야기와 원어 대사 동시 녹음을 지원하고, 이 때문에 프롬프트를 쓰는 방식 자체가 바뀌었다. 수 초짜리 짧은 클립에서는 우는 표정이나 웃는 표정, 화난 표정처럼 정지된 한 순간의 감정 상태만 보여주면 충분했다. 반면 30초 길이의 영상에서는 `"여자가 매우 슬퍼하며 울면서 대사를 말한다"` 같은 한 줄짜리 감정 라벨만으로는 연기가 성립하지 않는다. 그렇게 지시받은 모델은 첫 프레임부터 마지막 프레임까지 슬픈 표정 하나를 그대로 고정해 두고 입만 달싹여 대사를 읽어 내려간다. 얼굴 표정과 대사가 따로 노는 것은 이 때문이다.

사람이 실제로 감정을 드러내는 과정은 첫 순간부터 최고조로 폭발하지 않는다. Foyege는 프롬프트의 출발점으로 네 가지 핵심 정보를 제시한다. 실제 배우에게 연기를 지시할 때 감독이 감정 형용사 대신 전달하는 정보다.

| 핵심 요소 | 프롬프트가 답해야 할 질문 |
| --- | --- |
| **WHY: 인물 목적** (人物目的) | 인물이 이 순간 상대에게서 무엇을 얻으려 하며, 왜 반드시 이 말을 꺼내야 하는가 |
| **CUE: 트리거 대사** (触发台词) | 어느 문장, 어느 단어를 발음하는 순간 감정의 균형이 바뀌는가 |
| **ACT: 가시적 동작** (可见动作) | 눈썹, 눈꺼풀, 입꼬리, 호흡, 상체 기울기에서 눈으로 볼 수 있는 어떤 변화가 일어나는가 |
| **NO: 금지 반응** (禁止反应) | 이 구간에서 아직 표면으로 드러나면 안 되는 감정이나 동작은 무엇인가 |

## 1단계: 프롬프트를 3개 계층으로 분리하기

3,668자나 되는 지시문을 한 덩어리 줄글로 이어 쓰면 인물 외모 묘사, 카메라 워킹, 세부 연기 지시가 서로 간섭해 얼굴이 변하거나 카메라가 엉뚱한 순간에 바뀐다. Foyege는 전체 프롬프트를 역할이 서로 다른 세 계층으로 분리한다.

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 308" role="img" aria-label="Foyege의 3계층 프롬프트 구조와 30초 4샷 타임라인 매핑" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="308" fill="var(--bg-2)"/>
  <rect x="18" y="18" width="212" height="272" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="32" y="44" font-family="var(--mono)" font-size="11" font-weight="700" fill="var(--ink-2)">LAYER 01 / GLOBAL</text>
  <text x="32" y="66" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">전역 제어 (촬영장과 배우 고정)</text>
  <text x="32" y="96" font-family="var(--sans)" font-size="11" fill="var(--ink)">• 형식: 30초, 20:9, 24fps, 35mm 질감</text>
  <text x="32" y="125" font-family="var(--sans)" font-size="11" fill="var(--ink)">• 공간: 1950년대 미국 노동자 뒷마당</text>
  <text x="32" y="154" font-family="var(--sans)" font-size="11" fill="var(--ink)">• 남자: 50대 흑인 노동자, 중저음</text>
  <text x="32" y="183" font-family="var(--sans)" font-size="11" fill="var(--ink)">• 여자: 40대 후반, 격자 홈드레스</text>
  <text x="32" y="212" font-family="var(--sans)" font-size="11" fill="var(--ink)">• 축선: 180도 규칙 (남자 좌, 여자 우)</text>
  <text x="32" y="241" font-family="var(--sans)" font-size="11" fill="var(--ink)">• 음향: 원어 립싱크, 배경음악 금지</text>
  <text x="32" y="271" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">• 제약: 자막, 워터마크, 얼굴 변형 금지</text>
  <line x1="230" y1="154" x2="250" y2="154" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink)"/>
  <rect x="254" y="18" width="212" height="272" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="268" y="44" font-family="var(--mono)" font-size="11" font-weight="700" fill="var(--ink-2)">LAYER 02 / SHOT TIMELINE</text>
  <text x="268" y="66" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">샷 타임라인 (4개 샷 구성)</text>
  <rect x="268" y="82" width="184" height="40" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="276" y="99" font-family="var(--mono)" font-size="11" font-weight="700" fill="var(--ink)">Shot 1 [0.0–3.7s]</text>
  <text x="276" y="113" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">남자 85mm 클로즈업 (억제된 분노)</text>
  <rect x="268" y="128" width="184" height="56" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="276" y="145" font-family="var(--mono)" font-size="11" font-weight="700" fill="var(--accent-ink)">Shot 2 [3.7–23.0s]</text>
  <text x="276" y="160" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">여자 오버더숄더 클로즈업</text>
  <text x="276" y="175" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">내부 5단계 감정 비트 세분화</text>
  <rect x="268" y="190" width="184" height="41" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="276" y="207" font-family="var(--mono)" font-size="11" font-weight="700" fill="var(--ink)">Shot 3 [23.0–29.0s]</text>
  <text x="276" y="222" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">남자 무언 리액션 3단계 + 여자 음성</text>
  <rect x="268" y="238" width="184" height="40" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="276" y="255" font-family="var(--mono)" font-size="11" font-weight="700" fill="var(--ink)">Shot 4 [29.0–30.0s]</text>
  <text x="276" y="269" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">여자 익스트림 클로즈업 (눈물 흘림)</text>
  <line x1="466" y1="154" x2="486" y2="154" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="490" y="18" width="212" height="272" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="504" y="44" font-family="var(--mono)" font-size="11" font-weight="700" fill="var(--accent-ink)">LAYER 03 / ACTING BEATS</text>
  <text x="504" y="66" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">연기 제어 (샷 내부 8차원 공식)</text>
  <text x="504" y="95" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">01 시간대: 샷 내부 세부 초 범위</text>
  <text x="504" y="120" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">02 인물 목적: 이 순간의 심리적 목표</text>
  <text x="504" y="145" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">03 감정 변화: 방어 유지 → 균열 → 파열</text>
  <text x="504" y="170" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">04 트리거 단어: 변화가 시작되는 어절</text>
  <text x="504" y="195" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">05 얼굴 동작과 AU: 자연어 + FACS 코드</text>
  <text x="504" y="220" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">06 시선과 몸: 직시, 회피, 상체 기울기</text>
  <text x="504" y="245" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">07 목소리와 호흡: 음량, 속도, 짧은 숨</text>
  <text x="504" y="271" font-family="var(--sans)" font-size="11" fill="var(--accent-ink)">08 종료 상태와 금지: 조기 낙루 차단</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 618" role="img" aria-label="Foyege의 3계층 프롬프트 구조와 30초 4샷 타임라인 매핑 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="618" fill="var(--bg-2)"/>
  <rect x="16" y="14" width="318" height="149" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="38" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">LAYER 01 / GLOBAL</text>
  <text x="28" y="58" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">전역 제어 (촬영장과 배우 고정)</text>
  <text x="28" y="82" font-family="var(--sans)" font-size="12" fill="var(--ink)">• 30초, 20:9, 24fps, 1950년대 미국 뒷마당</text>
  <text x="28" y="104" font-family="var(--sans)" font-size="12" fill="var(--ink)">• 남녀 외모, 복장, 성우 톤 고정, 180도 축선 유지</text>
  <text x="28" y="126" font-family="var(--sans)" font-size="12" fill="var(--ink)">• 원어 대사 동시 녹음, 배경음악과 효과음 배제</text>
  <text x="28" y="148" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">• 자막, 워터마크, 얼굴 변형, 과장된 몸짓 금지</text>
  <line x1="175" y1="163" x2="175" y2="183" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-m)"/>
  <rect x="16" y="187" width="318" height="185" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="211" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--ink-2)">LAYER 02 / SHOT TIMELINE</text>
  <text x="28" y="231" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">샷 타임라인 (4개 샷 구성)</text>
  <text x="28" y="257" font-family="var(--sans)" font-size="12" fill="var(--ink)">• Shot 1 [0.0–3.7s]: 남자 85mm 클로즈업</text>
  <text x="28" y="281" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--accent)">• Shot 2 [3.7–23.0s]: 여자 클로즈업 (5단계 비트)</text>
  <text x="28" y="305" font-family="var(--sans)" font-size="12" fill="var(--ink)">• Shot 3 [23.0–29.0s]: 남자 무언 리액션 3단계</text>
  <text x="28" y="329" font-family="var(--sans)" font-size="12" fill="var(--ink)">• Shot 4 [29.0–30.0s]: 여자 익스트림 클로즈업</text>
  <text x="28" y="357" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">※ 시간 코드만 나열하지 않고 카메라 대상부터 지정</text>
  <line x1="175" y1="372" x2="175" y2="392" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="16" y="396" width="318" height="209" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="28" y="420" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent-ink)">LAYER 03 / ACTING BEATS</text>
  <text x="28" y="440" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">연기 제어 (샷 내부 8차원 공식)</text>
  <text x="28" y="466" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">01 시간대, 02 인물 목적, 03 감정 변화</text>
  <text x="28" y="490" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">04 대사 트리거 단어 ("eighteen years", "my life")</text>
  <text x="28" y="514" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">05 자연어 얼굴 동작 + FACS AU 코드와 강도(A–E)</text>
  <text x="28" y="538" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">06 시선과 몸, 07 목소리와 호흡, 0.5초 멈춤</text>
  <text x="28" y="562" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">08 종료 상태와 금지 반응 (조기 오열 차단)</text>
  <text x="28" y="590" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">→ 다음 비트와 다음 샷의 시작 상태로 연결</text>
</svg>
<figcaption style="margin-top: 0.65rem; font-size: 0.85rem; color: var(--ink-2); text-align: center; line-height: 1.5;">Foyege의 3,668자 원본 프롬프트에 적용된 3계층 구조. 전역 제어로 공간과 배우를 고정한 뒤, 4개 샷 타임라인과 8차원 연기 비트를 차례로 배치한다.</figcaption>
</figure>

첫 번째 계층인 **전역 제어**(全局控制)는 촬영장과 배우를 고정한다. 여기서는 영상 길이를 30초로, 화면비를 20대 9 와이드스크린(20:9)으로 정하고, 초당 24프레임(24fps)과 미세한 35mm 필름 그레인 질감을 지정한다. 시대와 배경은 20세기 중반 미국 노동자 가정의 뒷마당 현관이고, 조명은 오후의 따뜻한 측후방 자연광이다. 두 인물의 외모와 의상, 목소리 톤도 여기서 정한다. 특히 중요한 것은 **180도 축선 규칙**이다. 두 인물은 약 1미터 거리를 두고 마주 서고, 남자는 화면 왼쪽, 여자는 화면 오른쪽에 머문다. 이렇게 좌우 축선을 고정해 두어야 샷이 바뀐 뒤에도 두 사람이 서로를 바라보는 시선 방향이 어긋나지 않는다. 일단 전역 계층에서 머리 모양과 의상, 성우 톤을 지정했다면 하위 시간 구간에서는 그 설명을 되풀이하지 않고 새로 추가되는 반응에만 지면을 쓴다.

두 번째 계층인 **샷 타임라인**(镜头时间轴)은 관객이 그 순간 누구를 어떤 구도로 보고 있는지를 정의한다. 초보자가 흔히 저지르는 실수는 `"4초에 분노, 8초에 슬픔, 12초에 울음"`처럼 시간 코드만 나열하는 것이다. 카메라가 누구를 비추고 있는지 지정하지 않으면, 여자의 눈썹과 입꼬리가 미세하게 떨리는 결정적 순간에 카메라가 반대편 인물을 비추는 일이 벌어진다. 따라서 샷마다 큰 시간 구간, 피사체, 샷 크기(클로즈업, 오버더숄더, 익스트림 클로즈업), 전환 방식(하드 컷)을 먼저 지정하고, 각 샷의 연기 시간은 그다음에 초 단위로 세분화해야 한다.

세 번째 계층인 **연기 제어**(表演控制)는 샷마다 배우가 왜 그렇게 반응하는지를 시간 구간별로 지시한다. AI 배우의 연기력은 이 계층이 얼마나 구체적이냐에 따라 달라진다.

## 2단계: 감정의 보호막과 4개 샷의 단계적 감정 곡선

30초 단편 가운데 감정의 흐름이 가장 다층적으로 변하는 대목은 여자를 오버더숄더 클로즈업으로 잡은 **샷 2**(3.7\~23.0초)에 집중되어 있다. 19.3초 동안 이어지는 이 샷에서 Foyege는 여자를 처음부터 울리지 않는다. 현실에서 사람은 말다툼이 시작되자마자 오열하지 않고, 먼저 분노로 자신을 방어하다가 더는 버틸 수 없게 될 때 비로소 연약한 슬픔을 드러내기 때문이다.

![샷 2(3.7\~23.0초)의 5단계 감정 전개와 실제 생성 화면](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/02-shot2-five-beats.jpg)
*여자의 두 번째 샷(3.7\~23.0초)을 하나의 감정 대신 다섯 단계의 심리 변화(반격, 자기 증명, 균열, 첫 목소리 파열, 고백)로 세분화한 설계. 출처: Foyege, Vibe Shot Club.*

3,668자 원본 프롬프트에 기록된 4개 샷 전체의 시간대별 대사와 연기 설계를 표로 정리하면 다음과 같다.

| 구간 | 시간과 단계 및 원작 <펜스> 영어 대사 | 핵심 신체 및 음성 지시와 금지 반응 |
| --- | --- | --- |
| **샷 1** | 0.0\~3.7초 (남자의 억제된 폭발): *"It's not easy for me to admit that I've been standing in the same place for eighteen years."* | 85mm 클로즈업. 입술을 다물고 턱을 악문 채 낮게 시작(`AU4 + AU7 + AU23`). `"eighteen years"`에서 콧방울이 벌어지고 상체를 몇 cm 앞으로 내밀며 짧게 폭발(`AU25 + AU26`) 후 즉시 하드 컷. |
| **샷 2-1** | 3.7\~6.5초 (반격, 反击): *"Well, I've been standing with you! I've been right here with you, Troy! I got a life, too."* | 여자 오버더숄더 클로즈업. 상체를 급히 앞으로 기울이고 턱을 내밀며 치아 사이로 짜내듯 빠르고 날카롭게 반격(`AU4 + AU5 + AU9 + AU10 + AU20`). |
| **샷 2-2** | 6.5\~11.5초 (자기 증명, 自证): *"I gave eighteen years of my life to stand in the same spot as you."* | 물러서지 않고 직시하되 눈빛이 공격에서 자기 증명으로 전환. 눈썹 안쪽이 올라가고 아래 눈꺼풀에 물기가 비침. 오른손으로 자기 가슴을 짧게 한 번 가리키고 `"my life"`를 강조. |
| **샷 2-3** | 11.5\~16.5초 (균열, 裂缝): *"Don't you think I ever wanted other things? Don't you think I had dreams and hopes?"* | 0.5초 미만 고개를 숙였다가 다시 눈을 듦. 눈가가 젖어들고 아랫입술이 미세하게 떨리지만 **이 시점에 눈물이 흘러내리는 것은 금지**. 둘째 질문의 `"dreams and hopes"`에서 목소리가 낮아짐. |
| **샷 2-4** | 16.5\~20.0초 (파열, 破音): *"What about my life? What about me?"* | 목소리가 처음으로 뚜렷하게 갈라짐. 첫 문장은 높은 음량으로 직시, 두 문장 사이 짧고 급한 들숨과 0.5초 미만의 시선 하강, 둘째 문장은 가볍고 느린 톤으로 공격성 소멸. |
| **샷 2-5** | 20.0\~23.0초 (고백, 坦白): *"Don't you think it ever crossed my mind to want to know other men?"* | 눈을 다시 크게 뜨고 눈썹을 치켜올리며 고통스러운 자조가 스침. 웃음기 없는 입꼬리 경련 직후 입꼬리가 처지고 고개를 살짝 기울임. 대사 끝을 끊지 않고 다음 샷으로 연결. |
| **샷 3** | 23.0\~29.0초 (남자의 무언 리액션 3단계, 여자 오프스크린 대사): *"That I wanted to lay up somewhere and forget about my responsibilities? That I wanted someone to make me laugh..."* | 남자 클로즈업 하드 컷. 23\~25초 반박하려 입을 살짝 열다 침묵 → 25\~27초 `"other men"`과 `"responsibilities"`를 듣고 눈가에 물기가 차며 **억제된 침 삼킴** 1회 → 27\~29초 처음으로 시선을 오른쪽 위로 회피(**남자의 눈물 금지**). |
| **샷 4** | 29.0\~30.0초 (결말의 감정 분출): *"...so I could feel good?"* | `"laugh"` 직후 여자 익스트림 클로즈업(극클로즈업) 하드 컷. 마침내 눈물 제약 해제, 오른쪽 뺨을 따라 눈물이 흐르고 아랫입술이 뒤집히듯 떨림. `"good"` 직전 짧고 부서지는 들숨 후 이미 답을 아는 질문처럼 음량을 낮추며 0.3초 정지. |

![분노라는 보호막이 점진적으로 약해지며 슬픔이 드러나는 감정 곡선 도식](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/03-emotional-arc.jpg)
*감정 곡선 설계: 인물은 먼저 분노로 자신을 보호하고, 그 방어 태세가 유지되지 못할 때 비로소 슬픔이 표면으로 드러난다. 출처: Foyege, Vibe Shot Club.*

이 설계의 핵심은 두 가지다. 하나는 "유지하려는 상태"와 "점차 드러나는 상태"를 한 문단에 함께 적는 것이다. 다른 하나는 "지금은 일어나면 안 되는 반응"(금지 반응)을 적어 다음 구간에서 표현할 감정의 여지를 남기는 것이다. 실제로 샷 2의 3번 비트(11.5\~16.5초)에는 `"눈가가 점차 젖어들지만 지금 눈물이 떨어져서는 안 된다"`라는 금지 조건이 적혀 있다. 이 제약이 있기에 샷 4(29.0\~30.0초)에서 눈물이 뺨을 타고 흘러내릴 때 관객은 새로운 감정의 절정을 목격한다.

## 3단계: 대사를 표정 변화의 타임라인으로 만들기

대사는 오디오 트랙을 채우는 텍스트에서 끝나지 않는다. 표정과 시선이 언제 바뀌는지 알려 주는 시간표 역할도 한다. Foyege는 한 구간의 대사 연기를 지시할 때 다음 여섯 가지 요소를 반드시 명시한다.

1. **말하기 전 상태**(说话前状态): 입을 열기 직전 인물이 어떤 자세와 표정으로 버티고 있는가.
2. **트리거 대사**(触发台词): 어느 문장, 어느 단어가 인물의 내면을 자극했는가.
3. **강조 단어**(加重词): 어느 단어에서 목소리의 높낮이나 떨림이 바뀌는가.
4. **시선과 몸**(眼神与身体): 말하는 동안 눈빛, 입술, 턱, 상체가 어떻게 반응하는가.
5. **호흡과 멈춤**(呼吸与停顿): 문장과 문장 사이의 침묵에서 인물은 어떤 결단을 내리는가.
6. **종료 상태**(结束状态): 대사를 마친 직후 인물이 어떤 상태로 남는가.

![한 구간의 연기 프롬프트에 명시해야 할 여섯 가지 요소를 정리한 강좌 화면](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/03a-dialogue-six-elements.jpg)
*대사 기반 연기 프롬프트가 갖추어야 할 여섯 가지 요소: (1) 말하기 전 상태, (2) 트리거 대사, (3) 강조 단어, (4) 시선과 몸, (5) 호흡과 멈춤, (6) 종료 상태. 출처: Foyege, Vibe Shot Club.*

대표적인 사례는 샷 2의 4번 비트(16.5\~20.0초)에 나오는 두 문장이다. `"What about my life? What about me?"` 커버 이미지에도 실린 대사다. 첫 문장 `"What about my life?"`는 여전히 상대를 추궁하는 높은 음량으로 남자의 눈을 똑바로 바라보며 말한다. 두 문장 사이의 짧은 멈춤에서 여자는 급하게 숨을 들이마시며 0.5초 미만 동안 시선을 아래로 떨어뜨린다. Foyege는 이 0.5초의 멈춤이 단순한 대사 공백이라기보다 `"가장 여린 속마음(What about me?)을 입 밖으로 꺼낼지 결정하는 심리적 동작"`이라고 설명한다. 결단을 마치고 다시 남자를 바라보며 `"What about me?"`를 말할 때는 목소리가 눈에 띄게 가볍고 느려지고, 눈빛에서 공격성이 사라진다.

## 4단계: FACS 안면 동작 단위(AU)를 활용한 보조 교정

자연어 묘사만으로는 표정의 미세한 부분을 정확히 지정하기 어렵다. 이때 Foyege가 보조 수단으로 쓰는 것이 심리학의 **FACS**(Facial Action Coding System, 얼굴 움직임 부호화 체계)와 **AU**(Action Unit, 동작 단위)다.[^3] FACS는 감정을 주관적으로 해석하는 대신 얼굴의 어느 근육이 수축했는지를 번호로 기록한다.

| AU 코드 | 해부학적 근육 동작 (중국어 원문 표기) | Foyege 단편에서의 주된 연기 효과 |
| --- | --- | --- |
| **AU1** | 눈썹 안쪽 올리기 (眉毛内侧抬起, Inner Brow Raiser) | 슬픔, 호소, 억울함이 나타날 때 이마 중앙에 아치 모양 주름 형성 |
| **AU4** | 눈썹 내리기 (眉毛下压, Brow Lowerer) | 미간이 좁혀지며 분노, 압박감, 맞서는 느낌이 생김 |
| **AU5** | 윗눈꺼풀 올리기 (上眼睑抬起, Upper Lid Raiser) | 눈이 크게 떠지며 충격, 경계, 격앙된 추궁 표현 |
| **AU7** | 눈꺼풀 조이기 (眼睑收紧, Lid Tightener) | 시선이 날카롭게 고정되며 억누른 분노나 눈물 고임 강조 |
| **AU9 / AU10** | 콧등 찡그리기 / 윗입술 올리기 (鼻部皱起 / 上唇抬起) | 샷 2의 1번 비트 반격 구간에서 치아를 드러내며 격렬히 맞받아칠 때 사용 |
| **AU15** | 입꼬리 내리기 (嘴角向下, Lip Corner Depressor) | 슬픔과 자조가 입가에 남기는 뚜렷한 하강 곡선 |
| **AU17** | 턱 올리며 긴장시키기 (下巴抬起并绷紧, Chin Raiser) | 터지려는 울음을 참을 때 아랫입술을 밀어 올리며 턱에 잡히는 주름 |
| **AU20** | 입꼬리를 수평으로 당기기 (嘴角横向拉伸, Lip Stretcher) | 샷 2의 1번 비트에서 치아 사이로 말을 짜낼 때의 입술 긴장 |
| **AU23** | 입술 조이기 (嘴唇收紧, Lip Tightener) | 분노나 감정이 새어 나오지 않도록 입술을 꽉 다물어 억제 |
| **AU25 / AU26** | 입술 벌리기 / 턱 벌리기 (嘴唇分开 / 下颌张开) | 트리거 단어(`"eighteen years"`)에서 억누르던 감정이 짧게 터져 나오는 순간 |

개별 AU 동작을 적을 때는 **강도 5단계**(A\~E)와 **시간 전개 3단계**(Onset, Apex, Offset 순서)라는 두 가지 척도를 함께 활용한다. 강도는 약한 순서대로 Trace(A), Slight(B), Marked(C), Severe(D), Maximum(E)이다. 각각 겨우 알아챌 수 있는 미세한 수축, 경미한 수준, 뚜렷한 수준, 강한 수준, 근육 수축의 극한을 뜻한다. 만약 첫 프레임부터 얼굴 근육 전부를 최고 단계인 Maximum(E)까지 끌어올려 놓는다면, 뒤이어 감정이 한층 더 고조되어야 할 순간에 추가로 변화를 줄 여력이 남지 않게 된다.

![표정 변화의 3단계 Onset(동작 시작), Apex(정점 도달), Offset(점진적 소멸) 곡선](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/04-onset-apex-offset.jpg)
*단일 표정 동작도 시작(Onset)과 정점(Apex), 소멸(Offset)의 시간 곡선을 거쳐야 기계적인 표정 전환을 피할 수 있다. 출처: Foyege, Vibe Shot Club.*

예컨대 Foyege는 샷 1에서 남자의 분노 연기를 다음 네 단계의 AU 흐름으로 지시한다.

1. **억제 유지**: 대사 초반에는 눈썹을 내리고 눈꺼풀과 입술을 조인 상태(`AU4 + AU7 + AU23`)를 약한 강도로 유지한다.
2. **트리거 도달**: 대사가 `"eighteen years"`라는 트리거 어절에 도달한다.
3. **짧은 정점(Apex) 폭발**: 그 어절에서 콧방울이 벌어지고 입과 턱이 열리며(`AU25 + AU26`이 급격히 강해진다) 음량이 짧게 커진다.
4. **재통제(Offset)**: 마지막 단어가 끝나자마자 입을 다물고 강도를 낮춘다. 폭발이 장면 내내 고함으로 계속되지 않도록 하려는 것이다.

![동일한 AU4(눈썹 내리기)가 결합 동작에 따라 분노와 고통으로 달라지는 비교](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/05-au-not-formula.jpg)
*AU 코드는 감정 공식이 아니다. 같은 AU4(눈썹 내리기)도 함께 결합하는 시선과 입매에 따라 분노와 고통이라는 서로 다른 감정을 만든다. 출처: Foyege, Vibe Shot Club.*

Foyege는 **AU 코드를 독립된 감정 공식이나 자동 생성 스위치로 오해해서는 안 된다**고 강조한다. 동일한 `AU4`(눈썹 내리기)도 이를 악물고 상대를 노려보며 상체를 앞으로 기울이면 **분노**로 읽힌다. 반면 `AU1`(눈썹 안쪽 올리기), 시선 하강, `AU15`(입꼬리 내리기)와 함께 나타나면 **고통과 슬픔**으로 읽힌다. 더구나 영상 생성 모델이 AU 번호만 나열된 문장을 완벽히 해석한다는 보장도 없다. 따라서 가장 안정적인 작성 순서는 다음과 같다. 반드시 일상적인 자연어로 눈에 보이는 동작을 먼저 서술하고, 그다음 문단 끝에 `보조 표정 제어: AU1, AU15, AU17 경도 증강`처럼 AU 코드와 강도를 보조 교정용으로 덧붙인다.

## 5단계: 추상적 감정어를 네 가지 물리적 증거로 치환하기

Foyege의 논리는 간단하다. `"AI는 인물의 마음속 수치심을 볼 수 없지만, 수치심이 얼굴과 몸에 남긴 물리적 증거는 볼 수 있다."` 이 논리에 따라 Foyege는 슬픔이나 분노 같은 추상 명사를 프롬프트에서 지우고, **방향**(方向), **속도**(速度), **억제**(抑制), **금지**(禁止)라는 네 가지 물리적 증거로 바꿔 적는다. 그 대조 예시는 다음과 같다.

![슬픔이라는 추상어를 방향, 속도, 억제, 금지의 네 가지 가시적 증거로 치환한 프롬프트 예시](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/06-sadness-four-evidences.jpg)
*추상적인 감정 라벨('매우 슬퍼하며 운다')을 방향, 속도, 억제, 금지의 네 가지 물리적 증거와 AU 보조 교정으로 재작성한 구조. 출처: Foyege, Vibe Shot Club.*

- **잘못된 슬픔 지시**: `"여자가 매우 슬퍼하며 눈물을 멈추지 못하고 흘린다."`
- **네 가지 물리적 증거로 치환한 슬픔 지시**:
  - **방향과 속도**: `"그녀의 눈썹 안쪽이 천천히 올라가고, 입꼬리가 미세하게 내려가며, 턱 근육이 긴장되기 시작한다."` (순간 전환 대신 완만한 속도를 명시)
  - **억제**: `"입을 열어 말을 이어가려 하지만 즉시 소리를 내지 못한다."` (말하려는 의지와 막힌 발성의 충돌)
  - **금지와 보조 교정**: `"눈가가 점차 젖어들지만 이 순간 눈물은 아직 떨어져서는 안 된다. 보조 표정으로 AU1, AU15, AU17을 약하게 증강한다."`

어떤 근육 디테일을 적어야 할지 막막할 때는 실제 배우의 연기 영상을 보며 얼굴을 **5개 관찰 구역**(눈썹, 눈, 콧방울, 입술, 턱)으로 구분하고 네 가지 질문만 기록하면 된다. 첫째, 어느 부위가 수축하는가. 둘째, 어느 방향으로 변하는가. 셋째, 얼마나 강하게 작동하는가(겨우 보이는 정도, 뚜렷한 정도, 극한에 가까운 정도). 넷째, 어떤 대사가 그 변화를 촉발했는가. 순서는 먼저 평이한 일상어로 관찰 내용을 적고, 그다음 AU 코드로 교정하고, 마지막으로 초 단위의 구체적인 시간과 대사 어절에 연결하는 것이다. 요약하면 `먼저 보고, 그다음 이름 붙이기`다.

## 최종 공식: 8차원 연기 프롬프트 템플릿과 라이브 시연

Foyege는 앞서 살펴본 원칙을 연기 비트(Beat) 하나에 빠짐없이 반영하도록 최종 체크리스트를 정리했다. 이것이 **8차원 연기 프롬프트 공식**(八维表演提示词公式)이다.

![Foyege의 8차원 연기 프롬프트 공식 종합 도식](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/07-eight-dim-formula.jpg)
*감정을 실행 가능한 연기로 변환하는 8차원 연기 프롬프트 공식: (1) 시간대, (2) 인물 목적, (3) 감정 변화, (4) 대사 트리거 단어, (5) 얼굴 동작과 AU, (6) 시선과 몸, (7) 목소리와 호흡 및 멈춤, (8) 종료 상태와 금지 반응. 출처: Foyege, Vibe Shot Club.*

실제 작업에서 바로 복사해 쓸 수 있는 프롬프트 템플릿은 다음과 같다. 3계층 구조에 8차원 연기 비트를 결합한 형태다.

```text
[Layer 1: 전역 제어 (Global Control)]
- 형식 및 화질: 30초, 실사 영화 질감, 원어 대사 동시 녹음, 20:9(또는 16:9), 24fps, 미세한 35mm 필름 그레인
- 공간 및 조명: 시대, 장소, 주광원 방향과 색온도, 색채 톤 (상업 광고 느낌 배제)
- 인물 일관성 및 축선: 인물 A와 인물 B의 연령, 인종, 피부 질감, 복장, 머리 모양, 성우 톤 고정. 180도 축선 규칙(인물 A 좌측, 인물 B 우측) 유지, 얼굴 변형 금지
- 음향 및 제약: 배경음악(BGM), 효과음 과장, 자막, 워터마크, 과장된 연극식 몸짓 금지. 실제 호흡, 침 삼킴, 공간 반사음 유지

[Layer 2: 샷 타임라인 (Shot Timeline)]
- Shot 1 [0.0s–3.7s]: 인물 A 85mm 가슴 위 클로즈업 (억제된 상태에서 마지막 어절 짧은 폭발 후 하드 컷)
- Shot 2 [3.7s–23.0s]: 인물 B 오버더숄더 클로즈업 (내부 5개 감정 비트로 세분화, 카메라 고정 및 미세한 푸시인)
- Shot 3 [23.0s–29.0s]: 인물 A 무언 리액션 클로즈업 (인물 B의 오프스크린 대사를 들으며 3단계 표정 변화)
- Shot 4 [29.0s–30.0s]: 인물 B 익스트림 클로즈업 하드 컷 (최종 감정 분출 및 눈물 흘림, 0.3초 정지 후 종료)

[Layer 3: 연기 제어 / 8차원 비트 작성 예시 (Shot 2, Beat 2-4 | 16.5s–20.0s)]
01. 시간대: 16.5s–20.0s
02. 인물 목적: 상대에게 자신의 고통을 인정받으려 하지만 끝까지 무너지지 않으려 버팀
03. 감정 변화: 방어적 분노의 균열 → 목소리가 처음으로 파열되며 취약한 본심 노출
04. 대사 및 트리거 단어: "What about my life? What about me?" ("my life" 직후 호흡 멈춤)
05. 얼굴 동작과 AU: 눈썹 안쪽이 더 높이 올라가고 눈가에 눈물이 가득 고임. 콧방울이 미세하게 떨리고 입술을 다물었다가 다시 열며 턱 근육이 긴장됨 (보조 교정: AU1-C, AU15-B, AU17-C 점진적 Onset)
06. 시선과 몸: 첫 문장에서는 남자의 눈을 똑바로 직시하다가, 두 문장 사이 0.5초 미만 시선이 아래로 떨어짐. 둘째 문장에서 다시 눈을 맞추나 눈빛의 공격성이 사라짐
07. 목소리와 호흡 및 멈춤: 첫 문장은 높은 음량과 날카로운 톤 → 문장 사이 짧고 급한 들숨 1회 → 둘째 문장은 뚜렷하게 가볍고 느린 톤으로 하강
08. 종료 상태와 금지 반응: 눈가가 젖고 공격성이 사라진 상태로 다음 비트(고백)에 연결. [금지] 이 구간에서 눈물이 뺨으로 흘러내리거나 소리 내어 오열하지 말 것
```

강좌 영상의 마지막 약 50초(6분 32초부터 7분 21초까지)에서 Foyege는 샤오윈췌 AI 화면을 띄워 라이브 시연을 한다. 이 공식이 다른 장면에서도 통한다는 점을 보여 주려는 시연이다. 시연에 쓴 장면은 케네스 로너건 감독의 2016년 영화 **<맨체스터 바이 더 씨>**(*Manchester by the Sea*)에 나온다. 리 챈들러(케이시 애플렉)와 전처 랜디(미셸 윌리엄스)가 겨울 거리에서 우연히 마주쳐 오열하며 사과하는 대목이다. 강좌에서는 이 재회 장면 역시 동일한 3계층 구조와 8차원 공식으로 풀어 써서 Seedance 2.5(30초, 가로 화면비)의 입력창에 그대로 넣는다. 결과물에서는 울음을 삼키며 말을 잇지 못하는 여자의 떨리는 숨소리가 30초 동안 고스란히 재현되고, 남자는 그 울음을 감당하지 못해 뒷걸음질 치며 시선을 피한다.

![Foyege가 강좌 말미에 8차원 공식으로 생성해 시연한 영화 <맨체스터 바이 더 씨> 오마주 AI 연기 장면](https://img.seosoyoung.eiaserinnys.me/images/foyege-seedance-2-5-acting-prompt/08-manchester-live-demo.jpg)
*강좌 말미(7분 4초)의 라이브 시연 결과물. 동일한 3계층 구조와 8차원 공식으로 영화 <맨체스터 바이 더 씨>의 겨울 거리 재회 장면을 30초 단편으로 생성했다. 출처: Foyege, Vibe Shot Club.*

## 가장 흥미로운 지점

이번 추적에서 내가 주목한 것은 두 가지다. 하나는 Foyege가 강좌 초반에 한 말, `"문과생의 봄이 마침내 왔다(文科生的春天终于来了)"`이다. 다른 하나는 이 말을 뒷받침하는 연출 원리, **금지 반응**(禁止反应)이다. 그동안 사람들은 AI 영상 생성에서 고품질 결과를 얻는 비결이 시드 고정, 레퍼런스 이미지 조합, 복잡한 워크플로우 노드 설계 같은 기술적 파라미터 조율에 있다고 생각해 왔다. 그러나 한 번에 생성하는 길이가 30초로 늘고 모델이 지시문을 더 잘 이해하게 되자 핵심 역량이 달라졌다. 이제 필요한 것은 어거스트 윌슨의 <펜스>나 <맨체스터 바이 더 씨> 같은 명작의 연기를 초 단위로 관찰하고, <strong>"인물이 왜 지금 눈물을 참는지"</strong>를 언어로 적어 내는 연출자의 관찰력이다.

샷 2의 3번 비트(균열 구간)와 샷 3(남자 리액션 구간)에 걸어 둔 `"지금은 눈물이 떨어져서는 안 된다"`라는 부정 제약은 인물의 감정이 조기에 터져 나오지 않도록 붙들어 두는 장치다. 그리고 29초에 시작되는 마지막 1초짜리 익스트림 클로즈업(샷 4)에서 비로소 그 제약을 해제해 한 줄기 눈물을 흘리게 한다. 이 설계는 텍스트 프롬프트가 화면 묘사에서 끝나지 않고 시간 흐름에 따른 긴장을 조절하는 연출 지시서 노릇도 한다는 점을 보여 준다.

## 출처

- 2차 요약: `@VibeEverything`, 「조회수 400만 찍은 30초 AI 연기 영상에 사용한 Foyege의 Seedance 2.5 프롬프트 작성법 요약」, X (2026-11-22)
  - URL: <https://x.com/VibeEverything/status/2124437139517833554>
- 1차 강좌 및 해설 영상: Foyege(弗曳哥, `@Foyege24`), 「AI 演技基础：把情绪拆成能看见、能听见的表演 | Foyege AI 影像创作教程：从剧情节拍到多人控场」, Vibe Shot Club (2026-10-26) 및 YouTube `@fo_yege1664` 「一个可以完全释放AI演技的提示词公式！表情、台词、停顿、抢话全拆解｜Seedance 2.5全网最细教程」 (2026-08-23)
  - Vibe Shot Club: <https://vibeshot.club/courses/foyege-ai-filmmaking-tutorials/learn?lesson=8c865b0a-6ec9-4e11-ba08-8eaabacb1396>
  - YouTube: <https://www.youtube.com/watch?v=TZ4JhoYvUlc>
- 1차 원본 프롬프트 전문: Foyege弗曳哥, 「黑人演员完整提示词」, Bilibili (2026-08-12)
  - Bilibili: <https://www.bilibili.com/opus/1235578313475358724>

[^1]: `@VibeEverything`의 타래는 Foyege의 강좌 내용을 한국어 독자가 읽기 쉽게 10장의 카드 이미지로 압축 번역한 자료다. 이 타래는 강좌 초반의 요약 슬라이드를 기준으로 삼아 30초 단편의 구조를 3개 샷으로 소개한다. 반면 강좌 본문 해설과 빌리빌리의 원본 프롬프트 전문에는 29.0\~30.0초 구간의 네 번째 샷(여자 익스트림 클로즈업)이 있고, 원작 희곡 <펜스>(*Fences*)의 대사도 전부 실려 있다.
[^2]: Foyege는 3,668자 분량의 중국어와 영어 혼합 프롬프트 전문을 빌리빌리에 무료로 공개했다. 이후 유튜브(5분 40초 편집본)와 Vibe Shot Club 강좌(7분 21초 전체 영상과 텍스트 교안)에서 이 프롬프트의 설계 원리를 해설했다.
[^3]: FACS(Facial Action Coding System)는 1978년 폴 에크만(Paul Ekman)과 월리스 프리즌(Wallace Friesen)이 정립한 해부학적 안면 동작 분류 체계로, 2002년에 개정판이 나왔다. 영상 애니메이션, 컴퓨터 비전, 감정 인식 연구에서 표준 체계로 널리 쓰인다.
