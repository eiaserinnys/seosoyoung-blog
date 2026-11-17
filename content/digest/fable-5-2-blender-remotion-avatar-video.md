---
title: "Higgsfield も HeyGen も使っていないFable 5.2のAIアバター動画、えぐい"
date: 2026-11-17T15:00:00+09:00
tags: ["Claude", "Blender", "Remotion", "영상 생성", "영상 자동화"]
categories: ["창작과 문화"]
subjects: ["이미지와 영상 제작"]
summary: "일본의 AI 자동화 크리에이터 소(@so_ainsight)가 상용 아바타 도구와 영상 편집 프로그램을 쓰지 않고 31.9초(954프레임) 분량의 일본어 AI 아바타 영상을 제작했다. Claude Fable 5.2, Blender 5.2.1, Python 파형 합성, Remotion 4를 코드로 연결한 파이프라인과 로컬 재현 사례를 정리한다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/fable-5-2-blender-remotion-avatar-video/01-cover.jpg"
  alt: "어두운 편집실 데스크에 앉은 AI 여성 발표자. 좌우로 Fable 5.2와 편집 주체를 알리는 일본어 타이포그래피가 놓인 1번 컷 화면"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/fable-5-2-blender-remotion-avatar-video/01-cover.jpg"
---

## 3줄 요약

1. 일본의 AI 자동화 크리에이터 소(そう, `@so_ainsight`)가 2026년 11월 15일 X에 일본어 AI 아바타 영상을 공개했다.[^1] 31.9초(16:9, 30fps, 954프레임) 분량이며, 상용 아바타 서비스(HeyGen, Higgsfield)와 영상 편집 소프트웨어를 한 번도 쓰지 않고 만들었다.
2. 이 파이프라인에서 Claude Fable 5.2가 대본과 연출을 설계하고, 이미지 생성 모델과 립싱크 모델이 인물화 4장과 배경 사진 3장, 입 모양 구동 영상 5개를 만든다. Blender 5.2.1은 벽면 패널 18장의 조명 연출을, Python은 84 BPM 8소절 배경음악의 직접 합성을 맡고, 이 요소들을 Remotion 4가 코드로 조립한다.
3. 이튿날 댓글에서는 다른 개발자(`@aisnote`)가 같은 구성을 따라 자택의 GPU 한 대만으로 31.6초(948프레임, 11컷) 분량의 재현 영상을 만들어 올렸다. 올인원 아바타 도구 없이도 개별 모듈을 코드로 연결해 전 과정을 로컬에서 다시 구현했다.

[^1]: 중국어권 AI 블로거 TechVerser(`@realfxw`)가 2026년 11월 16일 X 게시물(<https://x.com/realfxw/status/2122253361927827961>)에서 이 영상을 소개하면서 널리 알려졌다. 이 게시물에 첨부된 영상의 원본은 소(`@so_ainsight`, 『n8nの教科書』(n8n 교과서) 저자)가 2026년 11월 15일에 올린 일본어 X 게시물(<https://x.com/so_ainsight/status/2121970275353010214>)이다.

## 올인원 아바타 도구를 쓰지 않는 모듈형 코드 파이프라인

AI 아바타 영상은 올인원 상용 서비스로 만드는 경우가 많다. 인물의 입 모양과 음성을 한 번에 처리해 주는 HeyGen, 카메라 연출 템플릿을 제공하는 Higgsfield가 대표적이다. 이런 도구는 마우스 클릭 몇 번으로 결과를 빠르게 얻기 좋다. 그러나 완성된 영상에 기성 템플릿 특유의 인상이 드러나기 쉽고, 부분적인 조명이나 공간 연출, 자막 타이밍은 세밀하게 고치기 어렵다.

소(`@so_ainsight`)가 공개한 31.9초짜리 일본어 영상은 올인원 아바타 서비스를 쓰지 않았고, Premiere Pro나 CapCut 같은 타임라인 편집 프로그램도 한 번 열지 않았다. 대신 인물 화면, 음성, 입 모양 구동, 스톡 영상 없이 제작한 3D 공간 연출, 음원 라이브러리를 쓰지 않은 배경음악, React 코드로 작성한 자막과 장면 전환을 각각 다른 도구와 스크립트로 따로 만든 뒤 마지막에 코드로 합쳤다.

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 310" role="img" aria-label="Claude Fable 5.2 기획부터 4개 에셋 모듈을 거쳐 Remotion 4로 954프레임을 조립하는 파이프라인 도식" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="310" fill="var(--bg-2)"/>
  <rect x="20" y="98" width="165" height="114" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="34" y="124" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 대본 및 연출 설계</text>
  <text x="34" y="148" font-family="var(--mono)" font-size="12" fill="var(--accent)">Claude Fable 5.2</text>
  <text x="34" y="172" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">11개 컷 구성안 작성</text>
  <text x="34" y="192" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">발화 문장 및 리듬 확정</text>
  <rect x="225" y="18" width="250" height="60" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="239" y="42" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2A. 인물화 및 배경 사진</text>
  <text x="239" y="62" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">화자 인물 4장 + 5번 컷 배경 사진 3장</text>
  <rect x="225" y="90" width="250" height="60" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="239" y="114" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2B. 음성 및 입 모양 구동</text>
  <text x="239" y="134" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">일본어 음성 합성 + 입 모양 클립 5개</text>
  <rect x="225" y="162" width="250" height="60" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="239" y="186" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2C. 3D 공간 연출 (Blender 5.2.1)</text>
  <text x="239" y="206" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">6, 7번 컷: 벽면 패널 18장 조립 및 조명</text>
  <rect x="225" y="234" width="250" height="60" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="239" y="258" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2D. 배경음악 합성 (Python)</text>
  <text x="239" y="278" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">파형 직접 합성 (84 BPM, 8소절 멜로디)</text>
  <rect x="515" y="85" width="185" height="140" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="529" y="115" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">3. 최종 코드 조립</text>
  <text x="529" y="139" font-family="var(--mono)" font-size="12" font-weight="700" fill="var(--accent-ink)">Remotion 4</text>
  <text x="529" y="163" font-family="var(--sans)" font-size="12" fill="var(--ink)">자막, 색보정, 배경 분리, 전환</text>
  <text x="529" y="183" font-family="var(--sans)" font-size="12" fill="var(--ink)">16:9, 30fps, 11컷</text>
  <text x="529" y="203" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--accent-ink)">954프레임 (31.9초)</text>
  <line x1="185" y1="130" x2="221" y2="52" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink)"/>
  <line x1="185" y1="145" x2="221" y2="120" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink)"/>
  <line x1="185" y1="165" x2="221" y2="192" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink)"/>
  <line x1="185" y1="180" x2="221" y2="262" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink)"/>
  <line x1="475" y1="52" x2="511" y2="125" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <line x1="475" y1="120" x2="511" y2="145" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <line x1="475" y1="192" x2="511" y2="165" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <line x1="475" y1="262" x2="511" y2="185" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 486" role="img" aria-label="Claude Fable 5.2 기획부터 에셋 모듈을 거쳐 Remotion 4로 조립하는 파이프라인 도식 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="486" fill="var(--bg-2)"/>
  <rect x="16" y="16" width="318" height="65" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="42" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 대본 및 연출 설계 (Claude Fable 5.2)</text>
  <text x="30" y="64" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">11개 컷 구성안 작성 및 발화 문장, 리듬 확정</text>
  <line x1="175" y1="81" x2="175" y2="101" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-m)"/>
  <rect x="16" y="105" width="318" height="247" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="131" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">2. 모듈별 에셋 제작 및 합성</text>
  <text x="30" y="159" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2A. 인물화 및 배경 사진</text>
  <text x="30" y="179" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">화자 인물 4장 + 5번 컷 배경 사진 3장</text>
  <text x="30" y="211" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2B. 음성 및 입 모양 구동</text>
  <text x="30" y="231" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">일본어 음성 합성 + 입 모양 클립 5개</text>
  <text x="30" y="263" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2C. 3D 공간 연출 (Blender 5.2.1)</text>
  <text x="30" y="283" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">6, 7번 컷: 벽면 패널 18장 조립 및 조명</text>
  <text x="30" y="315" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2D. 배경음악 합성 (Python)</text>
  <text x="30" y="335" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">파형 직접 합성 (84 BPM, 8소절 멜로디)</text>
  <line x1="175" y1="352" x2="175" y2="372" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="16" y="376" width="318" height="92" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="30" y="402" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent-ink)">3. 최종 코드 조립 (Remotion 4)</text>
  <text x="30" y="426" font-family="var(--sans)" font-size="12" fill="var(--ink)">자막, 색보정, 배경 분리, 전환</text>
  <text x="30" y="450" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--accent-ink)">16:9, 30fps, 11컷 / 954프레임 (31.9초)</text>
</svg>
<figcaption>올인원 아바타 SaaS와 편집 소프트웨어를 쓰지 않고 6개 작업 모듈을 코드로 연결한 31.9초 영상 제작 흐름</figcaption>
</figure>

## 에셋 제작과 3D 공간 연출: 브라우저 3D에서 Blender 5.2.1로 바꾼 과정

화면에 등장하는 여성 발표자는 기성 아바타 템플릿 없이 만들었다. 먼저 이미지 생성 모델로 인물 이미지를 네 가지 구도로 만들었다. 어두운 편집실 데스크 정면, 세이지 그린 벽면 정면, 크림색 배경에서 양손을 쓰는 제스처, 세이지 그린 벽면에서 손짓하는 구도다. 이어서 발표자가 말하는 구간에 맞춰 입 모양 구동 영상 다섯 개를 만들어 각 컷에 배치했다.[^2]

[^2]: 원문 게시물은 HeyGen과 Higgsfield를 쓰지 않았다는 점만 명시하고, 인물 이미지 4장과 입 모양 클립 5개를 어떤 모델로 만들었는지는 본문에 적지 않았다. 상세한 제작 방법은 작성자가 LINE 오픈채팅에서 공유한다.

![세이지 그린 배경 앞에 선 AI 발표자. 왼쪽에 색보정을 뜻하는 일본어 타이포그래피가 크게 놓인 3번 컷 화면](https://img.seosoyoung.eiaserinnys.me/images/fable-5-2-blender-remotion-avatar-video/02-color-grade.jpg)
*3번 컷(`COLOR / AUTO GRADE`). 채도가 낮은 화면에서 시작해 따뜻한 색보정이 적용되는 과정을 보여준다. 출처: [@so_ainsight 원문 영상](https://x.com/so_ainsight/status/2121970275353010214)*

3번 컷부터 5번 컷까지는 영상 편집 기능을 코드로 시연한다. 3번 컷(`COLOR / AUTO GRADE`)에서는 색감을 정돈하고, 4번 컷(`CUTOUT / LIVE MATTE`)에서는 발표자를 배경에서 오려낸다. 5번 컷(`PLACE / ANYWHERE`)에서는 주황색 아치형 프레임 안에 발표자를 배치한다. 이때 화면 오른쪽 아래에는 폴라로이드 사진 3장이 펼쳐진다. 5번 컷용으로 만든 석양 지는 해변, 야간 역 승강장, 설산 풍경이다.

![크림색 배경 왼쪽 주황색 아치 프레임 안에 발표자가 서 있고 오른쪽 아래에 해변, 승강장, 설산 배경 사진 3장이 겹쳐 놓인 5번 컷 화면](https://img.seosoyoung.eiaserinnys.me/images/fable-5-2-blender-remotion-avatar-video/03-place-anywhere.jpg)
*5번 컷(`PLACE / ANYWHERE`). 배경에서 분리한 발표자와 배경 사진 3장을 한 화면에 조합했다. 출처: [@so_ainsight 원문 영상](https://x.com/so_ainsight/status/2121970275353010214)*

6번 컷(`B-ROLL / SET BUILD`)과 7번 컷(`SOUND / FROM ZERO`)의 3D 공간 연출에서는 한 차례 도구를 바꿨다. 작성자는 처음에 과정을 단순화하려고 웹 브라우저에서 동작하는 간이 3D 도구로 두 컷을 시험 삼아 렌더링했다. 그러나 웹 브라우저의 간이 3D 렌더링으로는 표면 질감과 반사광의 표현이 부족해 1080p 전체 화면에 쓸 만한 화질을 내기 어려웠다.

![어두운 3D 공간의 반사 바닥 위에서 민트색과 산호색 조명을 받은 벽면 패널들이 맞물려 벽체를 이루는 6번 컷 화면](https://img.seosoyoung.eiaserinnys.me/images/fable-5-2-blender-remotion-avatar-video/04-blender-wall-panels.jpg)
*6번 컷(`B-ROLL / SET BUILD`). 오른쪽 위에 `BLENDER 5.2 / EEVEE / 0 STOCK FOOTAGE`라는 표기가 있고, 벽면 패널 18장이 맞물려 스튜디오 배경을 이룬다. 출처: [@so_ainsight 원문 영상](https://x.com/so_ainsight/status/2121970275353010214)*

작성자는 두 컷을 Blender 5.2.1(EEVEE 렌더러)로 다시 만들었다. 6번 컷에서는 반사 재질의 바닥 위로 벽면 패널 18장이 날아와 맞물리고 조명이 켜진다. 7번 컷은 다채로운 3D 블록 구조물 사이로 카메라가 전진하는 장면이고, 피사계 심도(아웃포커싱)가 걸려 있다.

![주황색, 청록색, 파란색 3D 블록들 사이로 얕은 피사계 심도가 적용된 카메라가 통과하며 음악 합성을 알리는 7번 컷 화면](https://img.seosoyoung.eiaserinnys.me/images/fable-5-2-blender-remotion-avatar-video/05-sound-from-zero.jpg)
*7번 컷(`SOUND / FROM ZERO`). Blender 5.2.1로 렌더링한 3D 블록 장면과 Python 파형 합성 배경음악이 어우러진다. 출처: [@so_ainsight 원문 영상](https://x.com/so_ainsight/status/2121970275353010214)*

배경음악 역시 외부 음원 사이트나 스톡 오디오 라이브러리를 쓰지 않았다. Python 코드로 기초 파형부터 직접 합성해 84 BPM, 8소절 멜로디를 만들고, 이를 30fps 프레임 타이밍에 맞춰 영상의 배경음악으로 입혔다.

## Remotion 4로 구현한 11컷 954프레임 조립 구조

단계별로 만든 인물 영상, 배경 사진, Blender 렌더링 시퀀스, Python 합성 음원은 마지막에 Remotion 4 프로젝트에서 하나의 영상으로 합친다.[^3] 화면 왼쪽 위의 상태 배지, 일본어 세리프와 산세리프 타이포그래피 애니메이션, 프롬프트 입력창 효과, 컷 간 전환을 모두 React 코드로 작성했다.

[^3]: Remotion은 오픈소스 영상 프레임워크다. React와 TypeScript로 프레임 번호(`useCurrentFrame`)에 따른 화면 상태를 함수로 정의하면, 헤드리스 브라우저와 FFmpeg가 각 프레임을 렌더링해 MP4 영상으로 출력한다.

완성된 31.9초(954프레임) 영상의 11개 컷 구성을 시간순으로 정리하면 다음과 같다.

| 컷 | 시간 | 일본어 내레이션 및 문구 (한국어 뜻) | 화면 연출 및 에셋 |
| :--- | :--- | :--- | :--- |
| **1** | 0.0\~5.8초 | この動画、人は作っていません。編集したのは Fable 5.2 です。 (이 영상, 사람은 만들지 않았습니다. 편집한 것은 Fable 5.2입니다.) | 어두운 편집실 배경의 발표자(인물화 1) 정면 발화 |
| **2** | 5.9\~6.7초 | Fable 5.2 | 산호색 전체 화면 타이틀 카드 전환 |
| **3** | 6.8\~9.7초 | まず、色を整えて。 (먼저, 색을 정돈하고.) | 세이지 그린 벽면 앞 발표자(인물화 2) 색보정 전환 |
| **4** | 9.8\~12.6초 | 次に、私を背景から切り抜いて (다음으로, 저를 배경에서 오려내어) | 크림색 단색 배경 위 발표자(인물화 3) 양손 제스처 |
| **5** | 12.7\~14.5초 | 好きな場所へ。 (원하는 장소로.) | 왼쪽 아치 프레임 안 발표자와 오른쪽 배경 사진 3장 |
| **6** | 14.6\~16.5초 | 背景も、ゼロから。 (배경도, 처음부터.) | 반사 바닥 위 벽면 패널 18장 조립 및 조명 점등 |
| **7** | 16.6\~18.5초 | 音楽まで。 (음악까지.) | 입체 블록 사이 카메라 이동과 84 BPM 멜로디 결합 |
| **8** | 18.6\~21.8초 | 編集ソフトは 一度も 開いていません。 (편집 소프트웨어는 단 한 번도 열지 않았습니다.) | 오른쪽 발표자(인물화 2), 왼쪽 3줄 타이포그래피 노출 |
| **9** | 21.9\~25.1초 | ついでに、この私も AIです。 (덧붙이면, 지금 이 저도 AI입니다.) | 오른쪽 발표자(인물화 4) 손짓과 붉은색 강조 문구 표시 |
| **10** | 25.2\~28.3초 | 人がやったのは 最初の一言だけ / かっこいい動画を1本つくって (사람이 한 일은 처음 한마디뿐 / 멋진 영상을 한 편 만들어 줘) | 편집실 배경(인물화 1) 왼쪽 입력창에 지시문 타이핑 |
| **11** | 28.4\~31.9초 | 次は、あなたの一言で。 (다음은, 당신의 한마디로.) | 입력창이 YOU 대기 커서로 바뀌며 954프레임 페이드아웃 |

8번과 9번 컷에서 발표자는 편집 소프트웨어를 한 번도 열지 않았다고 말한 데 이어, 자신도 AI로 생성한 캐릭터라고 밝힌다. 10번과 11번 컷은 다시 처음의 편집실 데스크 장면으로 돌아온다. 사람이 한 일은 프롬프트 입력창에 적은 첫 한마디, "멋진 영상을 한 편 만들어 줘(`かっこいい動画を1本つくって`)"뿐이라는 메시지로 영상이 끝난다.

![세이지 그린 배경 오른쪽에 발표자가 미소 지으며 서 있고 왼쪽에 발표자 자신도 AI라는 일본어 문구가 표시된 9번 컷 화면](https://img.seosoyoung.eiaserinnys.me/images/fable-5-2-blender-remotion-avatar-video/06-cast-generated-ai.jpg)
*9번 컷(`CAST / GENERATED`). 발표자 캐릭터 자체도 AI 생성물이라고 밝히는 장면이다. 출처: [@so_ainsight 원문 영상](https://x.com/so_ainsight/status/2121970275353010214)*

![어두운 편집실 배경의 발표자 왼쪽에 USER 프롬프트 입력창이 떠 있고 멋진 영상을 1편 만들어 달라는 일본어 지시문이 입력된 10번 컷 화면](https://img.seosoyoung.eiaserinnys.me/images/fable-5-2-blender-remotion-avatar-video/07-prompt-one-sentence.jpg)
*10번 컷. 왼쪽 프롬프트 입력창(`USER`)에 초기 지시문이 타이핑되는 연출은 코드로 구현했다. 출처: [@so_ainsight 원문 영상](https://x.com/so_ainsight/status/2121970275353010214)*

## 댓글로 이어진, GPU 한 대짜리 로컬 재현 사례

소(`@so_ainsight`)의 게시물이 올라온 이튿날인 2026년 11월 16일, 다른 개발자(`@aisnote`)가 원문 댓글로 자신의 로컬 환경에서 재현한 31.6초짜리 영상을 공유했다.[^4] 유료 클라우드 아바타 API 없이 자택의 단일 GPU 한 대로 전 과정을 로컬에서 돌렸다. 인물 이미지 제작, 음성 복제, 립싱크, Blender 3D 렌더링, Python 음악 합성, 코드로 작성한 자막과 전환의 조립까지 모두 포함한다.

[^4]: 재현 사례 답글은 <https://x.com/aisnote/status/2122116358586634363>이며, 완성된 32초 분량의 로컬 재현 영상(「HeyGenなしのAIアバター動画を全部ローカルで再現｜32秒・11カット・編集ソフト0回」)은 <https://youtu.be/xsXanuN_ZYY>에 공개됐다.

| 비교 항목 | 원문 제작 영상 (`@so_ainsight`) | 로컬 재현 영상 (`@aisnote`) |
| :--- | :--- | :--- |
| **영상 규격 및 길이** | 16:9, 30fps, 11컷, 954프레임 (31.9초) | 16:9, 30fps, 11컷, 948프레임 (31.6초) |
| **인물 및 배경 에셋** | 인물화 4장 + 배경 사진 3장 + 입 모양 5개 | 인물 사진 1장에서 4개 장면 생성 + 배경 사진 3장 + 입 모양 5개 |
| **음성 합성 및 검증** | 일본어 내레이션 | 동일 인물 음성 복제 후 음성 인식(ASR)으로 11개 문장 전수 일치 확인 |
| **3D 및 오디오** | Blender 5.2.1 벽면 패널 18장 + Python 84 BPM 8소절 합성 | Blender 벽면 패널 18장 및 조명 + Python 84 BPM 8소절 파형 합성 |
| **조립 방식** | Remotion 4 코드 조립 (편집 소프트웨어 0회) | 자막, 배경 분리, 전환 전부 코드로 작성 (편집 소프트웨어 0회) |

## 가장 흥미로운 지점

6번과 7번 컷에서 웹 브라우저용 간이 3D 도구를 버리고 Blender 5.2.1로 전환한 선택은 코드로 영상을 만들 때의 현실적인 분업 기준을 보여준다. 코드로 영상을 자동 생성하면서 모든 장면을 웹 브라우저 렌더링(CSS나 간이 WebGL)만으로 처리하려 하면, 입체 공간과 조명 장면에서 화면 밀도가 급격히 떨어진다. 자막과 2D 레이아웃은 깔끔하게 나오더라도 그렇다. 작성자는 인물과 자막 배치는 Remotion 4에 맡기고, 공간감과 반사광이 필요한 두 컷만 Blender의 EEVEE 렌더러로 따로 만들었다.

이 영상을 중국어권에 소개한 TechVerser(`@realfxw`)도 후속 답글 두 건에서 같은 맥락의 진단을 덧붙였다. 그는 올인원 템플릿 도구가 내부를 바꿀 수 없는 블랙박스여서 화면 일부의 조명이나 연출 호흡을 손보기 어렵다고 지적했다. 생성형 AI와 3D 렌더러, 오디오 합성기를 코드로 연결해 파이프라인을 모듈화해 두면, 마음에 들지 않는 컷만 골라 Blender로 가져가 조명을 다시 잡거나 스크립트 수치를 고칠 수 있다. 또한 음악과 화면의 감정선을 실시간으로 맞추는 세밀한 연출까지 터미널에서 코드 수정만으로 처리하는 것은 비효율적이므로, 대량 자동화나 정밀한 제어가 필요한 영역과 실시간 편집 도구의 역할을 구분해야 한다고 보았다.

## 출처

- 원문 저자: 소 (`そう`, `@so_ainsight`)
- 원문 발표일: 2026-11-15
- 원문 (일본어 X 게시물): <https://x.com/so_ainsight/status/2121970275353010214>
- 소개 및 해설 (중국어 X 게시물, TechVerser `@realfxw`, 2026-11-16): <https://x.com/realfxw/status/2122253361927827961>
- 로컬 재현 영상 (`@aisnote`, 2026-11-16): <https://youtu.be/xsXanuN_ZYY> (<https://x.com/aisnote/status/2122116358586634363>)
