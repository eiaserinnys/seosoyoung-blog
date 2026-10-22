---
title: "읽는 설명에서 만지는 설명으로: 인터랙티브 웹을 만드는 공개 AI 스킬 28선"
date: 2026-10-22T11:30:00+09:00
tags: ["코딩 에이전트", "스킬", "프론트엔드", "시각화", "Three.js"]
categories: ["에이전트와 코딩"]
summary: "코딩 에이전트에게 설치하면 버튼이 눌리는 기계 도해, 슬라이더로 조건을 바꾸는 실험 도구, 브라우저에서 조종하는 캐릭터, 스크롤에 따라 전개되는 제품 페이지를 만들어 주는 공개 스킬 28종을 정리했다. 대표 사례 7종은 공개 데모를 직접 조작한 화면으로 보여 주고, 전체 목록은 원본 링크와 용도를 붙인 표로 남긴다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/cover-colorfigures-washer-labels.png"
  alt: "Colorfigures로 만든 세탁기 도해. 투시 보기와 라벨을 켜서 드럼, 모터, 히터, 배수 펌프, 제어 기판의 위치가 이름표와 함께 보인다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/cover-colorfigures-washer-labels.png"
---

<style>
.post-content .iw-frame{position:relative;width:100%;height:620px;margin:1rem 0;background:#f7f7f7;border:1px solid rgba(127,127,127,.3);border-radius:6px;overflow:hidden}
.post-content .iw-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.post-content .iw-cover{position:absolute;inset:0;width:100%;height:100%;margin:0;padding:0;border:0;background:transparent;cursor:pointer}
.post-content .iw-cover:hover{background:rgba(0,0,0,.04)}
.post-content .iw-cover:focus-visible{outline:2px solid var(--primary);outline-offset:-4px}
@media (max-width: 640px){.post-content .iw-frame{height:500px}}
.post-content table td,.post-content table th,.post-content table a{word-break:keep-all !important;overflow-wrap:normal !important;hyphens:manual}
</style>

## 3줄 요약

1. 2026년 10월 기준으로 공개된 스킬 가운데, 코딩 에이전트에게 독자가 만지면서 읽는 웹 페이지를 만들게 하는 28종을 모았다. 스킬은 에이전트가 읽는 지침과 템플릿을 담은 폴더다. 정리는 각 스킬의 README와 SKILL.md, 제작자의 공개 예제를 바탕으로 했다.
2. 스타일 지침에 더해 기반 코드, 실행 예제, 상태 모델, 검증 절차까지 담은 스킬이 있다. 결과의 일관성에서 스타일 지침만 있는 스킬과 차이가 난다. Anatomy는 움직이는 부품과 표시 수치를 같은 상태 모델에 연결하고, scroll-craft는 완성된 페이지를 헤드리스 브라우저로 스크롤하며 아무것도 바뀌지 않는 구간을 찾아낸다.
3. 작동하는 설명 그림에는 Anatomy와 Iso Glow, 조건을 조절하는 실험 도구에는 Playground, 계속 고쳐 쓸 인터랙티브 기술 글에는 Moonshine이 맞는다. 연출이 강한 제품 페이지에는 scroll-craft, 필터와 지도와 차트가 있는 분석 페이지에는 OpenAI의 시각화 묶음, 여러 컴포넌트로 이루어진 작은 도구에는 Web Artifacts Builder가 맞는다.

## 출발점: 버튼이 눌리는 세탁기

April Zhu의 [Colorfigures](https://april-zhu.com/colorfigures)는 일상 사물을 한 문장으로 설명하면 손으로 그린 듯한 등각투영 그림을 HTML 파일 하나로 돌려주는 스킬이다. 세탁기 그림에서는 세탁물과 세제를 넣고 코스를 고른 뒤 시작 버튼을 누를 수 있다. 시작을 누르면 표시창의 남은 시간이 줄고 드럼이 돈다. 투시 보기를 켜면 겉판이 투명해지면서 드럼과 모터와 급수 밸브가 드러나고, 라벨을 켜면 부품 이름이 붙는다.

![Colorfigures 세탁기 도해. 세탁물과 세제를 넣고 시작을 누른 상태로, 표시창에 남은 시간 1:07이 보이고 드럼 안에서 빨래가 돈다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/colorfigures-washer-start.png)
*시작 버튼을 누른 직후. 제작자 April Zhu. [공개 데모](https://april-zhu.com/colorfigures-demo)를 헤드리스 브라우저에서 조작해 캡처했다.*

![같은 세탁기의 투시 보기. 겉판이 투명해져 드럼, 급수 밸브, 호스, 모터, 배수 펌프가 보인다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/colorfigures-washer-seethrough.png)
*같은 그림에서 See-through를 누른 상태.*

공개 데모에는 세탁기, 에스프레소 머신, 자판기, 토스터, 신호등, 캡슐 토이 기계 등 26점이 있다. 그림 한 점에 드는 시간은 Claude Code 기준으로 15분에서 30분이고, 토큰은 20만에서 40만 개다. 제작자가 직접 적은 수치다. 사람과 동물과 식물처럼 부드러운 대상은 이 스타일에 맞지 않는다는 안내도 같은 페이지에 있다. 스킬 자체는 텍스트 파일 여덟 개로, 모두 합쳐 220KB 안팎이다. 결과 HTML은 외부 요청 없이 단독으로 열린다.

이 글의 28종은 이 세탁기처럼 글과 화살표 대신 직접 누르고 돌려 보게 해서 설명하는 페이지를 만든다. 먼저 대표 사례 일곱을 데모 화면으로 보고, 뒤에 28종 전체를 표로 정리한다.

## Anatomy: 알고리즘을 기계로 그린다

Ryan(@wheresryan22)의 [Anatomy](https://github.com/wheresryan22/anatomy)는 개념을 한 줄로 말하면 그 개념대로 작동하는 물리적 기계를 고안하고, 부품 수십에서 수백 개로 이루어진 등각 도해로 그린다. 스킬에는 "물체가 곧 설명이다"라는 규칙이 있어서 상자와 화살표를 쓰지 않는다. 움직이는 부품과 화면에 표시되는 수치는 같은 상태 모델에서 나온다.

![기계식 손목시계 무브먼트 도해. 받침대에 놓인 무브먼트가 조립된 상태로, 브리지와 기어와 밸런스가 한 면에 보인다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/anatomy-watch-assembled.png)
*조립 상태의 시계 무브먼트. 용두를 끌어 올리면 태엽이 감기고, S 키로 움직임을 느리게 볼 수 있다. 밸런스는 4Hz, 시간당 28,800진동으로 표기된다. 제작자 Ryan. [공개 컬렉션](https://skills.wheresryan.sh/anatomy/collection/watch)에서 캡처했다.*

![같은 무브먼트에서 E 키를 눌러 브리지가 들려 올라가 기어열이 드러난 상태.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/anatomy-watch-apart.png)
*E 키를 눌러 브리지를 들어 올린 상태. 아래 기어열이 드러난다.*

같은 방식으로 자료구조와 프로토콜도 기계가 된다. 블룸 필터는 과일 머신(슬롯머신)이 된다. 릴 세 개가 해시 함수 세 개, 깃발 열여섯 개가 비트 배열이다. 단어를 코인으로 넣고 레버를 당기면 릴이 돌아 깃발이 올라간다. 한 번 당기고 나면 화면에 "16개 중 7개 올라감, 거짓 양성 9.4%"가 뜬다.

![블룸 필터를 과일 머신으로 그린 도해. 릴 세 개와 위쪽의 깃발 열여섯 개, 오른쪽에 당기는 레버가 있다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/anatomy-bloom-pulled.png)
*레버를 한 번 당긴 뒤의 블룸 필터.*

![TCP 3방향 핸드셰이크를 두 역 사이의 우편 로프웨이로 그린 도해. SYN, SYN-ACK, ACK 캐니스터가 줄을 타고 오간다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/anatomy-tcp-handshake.png)
*TCP 핸드셰이크. 두 역 사이의 로프웨이로 SYN, SYN-ACK, ACK 캐니스터가 오가고, 각 역의 신호기(세마포어)가 연결 상태를 가리킨다.*

컬렉션에는 해시맵 충돌, 이진 탐색, LRU 캐시, 메시지 큐, 뮤텍스, 경사 하강법, 디바운스와 스로틀, 토큰 버킷 등 33점이 있다. 터보팬 엔진과 Raptor 2 엔진처럼 큰 기계에서는 SVG 레이어 사이에서 WebGL 셰이더로 화염과 배기를 그린다.

<div class="iw-frame"><iframe src="https://skills.wheresryan.sh/anatomy/collection/mutex" title="Anatomy: Mutex" loading="lazy" tabindex="-1"></iframe><button type="button" class="iw-cover" aria-label="도해를 눌러 직접 조작하기" onclick="this.previousElementSibling.removeAttribute('tabindex');this.remove()"></button></div>

*뮤텍스 도해를 그대로 끼워 넣었다. 한 번 누르면 직접 조작할 수 있다. 펌프 두 대가 탱크 하나를 채우려 하고, 열쇠 하나가 접근을 결정한다. 화면이 비어 보이면 [원본 페이지](https://skills.wheresryan.sh/anatomy/collection/mutex)에서 열어 볼 수 있다.*

결과물은 세 가지 형태로 받을 수 있다. 프레임워크 없는 TypeScript 기반의 SVG와 HTML, React와 Next.js용 컴포넌트 `anatomy-figures`(테마 다섯 종, 색 토큰 26개), A4나 레터 크기 PDF다. 설치는 `npx skills add wheresryan22/anatomy`이고 스킬과 그림 모두 MIT 라이선스다. 그리는 대상은 기계, 악기, 도구, 가구다. README는 차트 라이브러리 대용, 사람, 지도를 제외한다고 적어 두었다.

## Iso Glow: 작동하는 부위가 빛나는 도시와 장치

[Iso Glow](https://isoglow.dev/)도 April Zhu의 스킬이다. 가는 선으로 그린 등각 도해에서 작동 중인 부분이 빛난다. 사무용 건물을 그리면 층마다 불을 켜고 끌 수 있다. N 키를 누르면 야간 근무 때처럼 모든 층에 불이 켜지고, O 키를 누르면 전부 꺼진다.

![사무용 건물 도해 두 장. 왼쪽은 24개 층이 모두 꺼진 상태, 오른쪽은 모든 층이 주황빛으로 켜진 상태.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/pair-isoglow-tower.png)
*왼쪽은 O 키로 전부 끈 상태(0/24), 오른쪽은 N 키로 전부 켠 상태(24/24). 제작자 April Zhu. [공개 데모](https://isoglow.dev/demo/cities)에서 캡처했다.*

![옛 데스크톱 컴퓨터 도해. 화면이 주황빛으로 켜져 있고 키보드가 코일 케이블로 연결되어 있다. 아래에 "Type on it, click it to switch"가 적혀 있다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/isoglow-objects-1.png)
*책상 위 컴퓨터. 키보드로 글자를 치면 화면에 나타나고, 본체를 누르면 전원이 꺼진다.*

데모에는 드럼 머신, 등대, 소형 도시, 시스템 분해도도 있다. 드럼 머신은 패드를 누르면 소리가 나고 16스텝 시퀀서가 돈다. 등대는 빛이 바다를 쓸고 안개 경적이 울린다. 소형 도시에서는 발전소가 네 구역에 전력을 공급하고, 시스템 분해도에서는 요청이 들어올 때마다 계층이 빛난다. 3D 모드에서는 같은 선 스타일을 three.js로 그려 돌려 볼 수 있고, `.glb` 모델을 넣으면 그 모델도 같은 선화로 바꿔 그린다.

![3D 모드의 타자기. 가는 선으로 그린 타자기 모델을 비스듬히 내려다보는 화면으로, 종이가 세워져 있고 키보드 글쇠에 글자가 적혀 있다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/isoglow-3d-typewriter.png)
*3D 모드의 타자기. 키보드로 치면 종이에 글자가 찍히고 Enter로 줄을 바꾼다. 드래그로 돌려 볼 수 있다.*

설치는 압축 파일을 `~/.claude/skills`에 푸는 것으로 끝나고, 스크립트나 의존성은 없다. 결과 파일이 외부에서 불러오는 것은 웹 폰트 하나, 그리고 3D 모드에서 CDN으로 받는 three.js뿐이다. 이 스킬의 기반은 Tolga Cohce의 [iso-figure](https://github.com/MrBongoC/ai-iso-skill)(MIT)이고, Colorfigures는 다시 Iso Glow를 기반으로 만들었다. 세 스킬은 등각 그리기 방법, 번호 매긴 도판 형식, "모든 그림은 무언가를 해야 한다"는 규칙을 공유한다.

![iso-figure로 만든 책상 위 신시사이저 도해의 움직이는 그림. 건반을 누르면 해당 음이 표시된다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/iso-figure-desk-synth.gif)
*기반이 된 iso-figure의 데스크 신시사이저. 평범한 SVG와 15줄 남짓한 투영 코드로 이루어진 HTML 한 파일이다. 제작자 Tolga Cohce. 저장소의 [소개 GIF](https://github.com/MrBongoC/ai-iso-skill)(MIT)다.*

## Playable: 스케치로 만든 캐릭터를 직접 조종한다

April Zhu의 세 번째 스킬 [Playable](https://april-zhu.com/playable)은 리깅된 3D 모델이나 로봇 스케치를 브라우저에서 조종하는 캐릭터로 바꾼다. 결과는 three.js로 동작하는 HTML 파일 하나이고, 게임 엔진은 쓰지 않는다. WASD로 걷고 Shift로 달리고 스페이스로 점프하며, 숫자 키로 손 흔들기나 춤 같은 동작을 실행한다. 바닥을 누르면 그 자리로 걸어가고, 휴대폰용 버튼 줄도 있다.

{{< video src="https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/playable-robot-walk-v2.mp4" >}}
*공개 데모의 로봇. 걷기, 점프, 손 흔들기 키를 차례로 눌렀을 때의 반응을 헤드리스 브라우저에서 녹화했다. 모델은 Tomás Laulhé(Quaternius)의 CC0 로봇, 동작 14종.*

리깅된 `.glb`를 주면 모델의 뼈대와 애니메이션을 그대로 살려, 대기, 걷기, 달리기 동작을 속도에 따라 섞는다. 걷기 클립에서 발 속도를 재서 발이 바닥에서 미끄러지지 않게 한다. 스케치를 주면 그림에서 부위와 관절을 읽어 단단한 조각으로 리깅된 모델을 만든다. 아래 로봇 고양이는 스케치 한 장으로 만들었다. 관절이 30개, 다리가 넷, 꼬리가 일곱 마디이고, 속도가 붙으면 걸음이 구보로 바뀐다. 앉기, 기지개, 덮치기, 눕기 같은 동작도 같은 제어기가 만드는 자세다.

![스케치에서 만든 로봇 고양이. 가는 선으로 그린 고양이가 걷는 자세이고, 눈과 꼬리 끝과 관절 고리가 연두색으로 빛난다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/playable-cat-walk.png)
*스케치에서 만든 로봇 고양이. L 키로 조명을 켠 뒤 W 키를 눌러 걷는 중이며, 눈과 꼬리 끝과 관절 고리가 빛난다. [공개 데모](https://april-zhu.com/playable-demo)에서 캡처했다.*

데모에는 로봇, 로봇 고양이, 메카 Leela, 네발 보행기, 눈알 드론까지 다섯 가지가 있고, 모델은 모두 CC0다. `.blend`나 `.fbx`를 변환하려면 Blender가 필요하다. 설치 방식은 Iso Glow와 같다.

## HTML Explainer: 슬라이더 하나로 물리를 설명한다

Derek Schwede의 [HTML Explainer](https://github.com/ds-vibe/html-explainer)는 작은 조작형 데모를 중심으로 개념을 설명하는 페이지나 웹 슬라이드를 만든다. 도플러 효과 예제에서는 속도 슬라이더 하나가 설명의 전부다. 음원이 느리면 파면이 거의 동심원이고, 빠르면 앞쪽 파면이 몰리고 뒤쪽이 늘어난다. 아래 수치 카드가 같이 바뀐다.

![도플러 효과 데모, 음원 속도 마하 0.10. 파면이 거의 동심원이고 수치 카드는 앞쪽 도달률 1.11배, 뒤쪽 0.91배.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/explainer-doppler-slow.png)
*음원 속도 마하 0.10. 앞쪽 파면 도달률 1.11배, 뒤쪽 0.91배.*

![같은 데모, 음원 속도 마하 0.85. 앞쪽 파면이 촘촘히 몰리고 뒤쪽은 넓게 퍼진다. 수치 카드는 앞쪽 6.67배, 뒤쪽 0.54배.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/explainer-doppler-fast.png)
*슬라이더를 마하 0.85로 올린 상태. 앞쪽 6.67배, 뒤쪽 0.54배. 제작자 Derek Schwede. [공개 갤러리](https://ds-vibe.github.io/html-explainer/)의 도플러 예제에서 캡처했다.*

오로라 예제에서는 지자기 폭풍 세기(Kp)를 높이면 북극 위에서 내려다본 오로라 타원이 적도 쪽으로 넓어지고, 타원 아래에 들어오는 도시 목록이 바뀐다. Kp 1에서는 타원이 지자기 위도 66도까지 내려와 트롬쇠와 페어뱅크스만 그 아래에 있고, Kp 9에서는 50도까지 내려가 런던과 파리까지 들어온다.

![오로라 타원 데모 두 장. 왼쪽은 Kp 1로 북극 둘레의 가는 고리만 빛나고, 오른쪽은 Kp 9로 고리가 넓어져 런던과 파리가 그 아래에 들어온다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/pair-explainer-aurora.png)
*왼쪽은 Kp 1, 오른쪽은 Kp 9. 같은 갤러리의 오로라 예제.*

갤러리에는 설명 페이지와 슬라이드 덱이 모두 여덟 점 있다. 설명 페이지는 EU AI 법의 위험 등급 분류기와 벌금 계산기, 부분지급준비 은행의 장부 시뮬레이터, 스톡옵션 세금 계산기 등이고, 슬라이드 덱은 구텐베르크 인쇄기, 필름 누아르 등이다. 각 페이지에는 Review & edit 버튼이 있어 수정 요청과 코멘트를 남길 수 있다. Claude Code에서 쓰면 데스크톱 화면, 모바일 화면, 조작 중인 상태를 캡처해 확인하고, Claude 앱에서는 정적 점검만 한다.

## Moonshine: 고쳐 가며 쓰는 인터랙티브 기술 글

Ian Johnson(enjalot)의 [Moonshine](https://github.com/enjalot/moonshine)은 Distill 같은 인터랙티브 기술 글을 만드는 스킬이다. 코드를 쓰기 전에 개념, 독자, 핵심 통찰을 묻고, 개념마다 정적 산문, 슬라이더, 연결된 뷰, 스크롤 서사, 애니메이션 가운데 하나를 고른다. 제작자가 내세운 원칙은 하나다. 모든 상호작용은 이해를 도와야 한다.

출력 방식은 둘이다. `shine`은 D3 시각화를 담은 HTML 한 파일이라 빌드 도구가 필요 없다. `still`은 Vite와 React 프로젝트로, 산문은 마크다운에 두고 그림은 React 컴포넌트로 만든다. `still`의 개발 모드에서는 렌더된 페이지가 곧 편집기다. 본문을 그 자리에서 고치고, 그림을 클릭해 노브 패널에서 매개변수를 돌리고, 절을 끌어 순서를 바꾸고, 코멘트를 에이전트에게 전달한다. 노브 패널은 숫자 매개변수마다 슬라이더와 숫자 입력을, 불리언마다 체크박스를 자동으로 만들고, 저장하면 새 값이 마크다운에 기록된다.

![Moonshine 가이드의 "노브 셋 달린 파동" 그림. 사인파 그래프 아래에 "그림을 클릭하면 매개변수가 열린다"고 적혀 있고, 그 아래 본문이 노브 패널의 동작을 설명한다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/moonshine-guide-knobs.png)
*still이 자기 자신을 설명하는 가이드. 그림을 클릭하면 슬라이더가 나오고, 값을 바꾸면 그림과 마크다운의 지시문이 같이 바뀐다. 편집 기능은 배포용 빌드에 포함되지 않는다. 제작자 enjalot. [공개 예제](https://enjalot.github.io/moonshine/moonshine-guide/index.html)에서 캡처했다.*

공개 예제는 네 편짜리 입자 유체(SPH) 시뮬레이션 연재, 차원 축소 기법 열 편, 근사 최근접 이웃 다섯 편처럼 연재 형식이 많다. 데이터 탐색 예제로는 학교 교과 주제 1,590개를 의미 유사도로 배치한 지도와, Prelinger 아카이브 영상 클립 23,148개를 임베딩 유사도로 늘어놓은 글이 있다.

![학교 교과 주제 1,590개를 점으로 뿌린 지도. 과학, 수학, 영어, 역사 군집이 색으로 구분되고 오른쪽에 설명 글이 붙어 있다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/moonshine-taxonomy-map.png)
*"A Map of What Children Learn". 점 하나가 교과 주제 하나이고, 점의 위치는 과목 이름을 쓰지 않고 의미 유사도만으로 계산했다. 같은 저장소의 [공개 예제](https://enjalot.github.io/moonshine/os-taxonomy-map/index.html).*

![SPH 연재 목차. 02 GPU로 옮기기, 03 물 너머(모래, 얼음, 탄성체), 04 플레이그라운드 세 글이 카드로 나열된다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/moonshine-sph.png)
*네 편짜리 유체 시뮬레이션 연재의 목차. 마지막 편은 재료를 고르고 방출기를 놓고 힘을 칠하는 샌드박스다.*

설치는 Claude Code 플러그인 마켓플레이스(`/plugin marketplace add enjalot/moonshine`)로 하거나 폴더를 복사하면 되고, Codex도 지원한다.

## Playground: 조절 패널과 프롬프트가 연결된 도구

Anthropic의 공식 플러그인 [Playground](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/playground)는 화면을 보면서 값을 조절하고 그 선택을 Claude에게 다시 돌려주는 HTML 도구를 만든다. 화면은 한쪽의 조절 패널, 다른 쪽의 즉시 갱신되는 미리보기, 아래쪽의 자연어 프롬프트로 이루어진다. 프롬프트에는 기본값에서 바뀐 항목만 적힌다. 사용자는 복사 버튼으로 이 프롬프트를 가져가 다음 요청에 붙여 넣는다. SKILL.md에는 제약도 적혀 있다. 이름 붙은 프리셋을 서너 개 두고, CSS와 JS는 모두 한 파일에 넣고, CDN은 쓰지 않는다.

이 플러그인에는 공개 데모가 없어서 직접 만들었다. 아래 두 화면은 "블로그 글 카드" 플레이그라운드다. Claude Code의 서브 에이전트(Claude Sonnet)가 플러그인의 SKILL.md와 `design-playground` 템플릿을 읽고 만들었다[^pg].

[^pg]: 확인한 범위는 헤드리스 브라우저에서 프리셋 전환과 슬라이더 조작에 따라 미리보기와 프롬프트가 바뀌는 것까지다. 제작자의 공개 데모가 아니므로 다른 사례와 같은 무게로 읽지 않는 편이 좋다.

![직접 만든 블로그 카드 플레이그라운드의 기본 상태. 왼쪽에 카드 폭, 모서리, 표지 비율, 글자 크기 슬라이더가 있고, 가운데에 밝은 카드 미리보기, 아래에 "변경 없음"이라는 프롬프트가 있다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/playground-blog-card-default.png)
*기본 상태. 아래 프롬프트는 아직 바꾼 것이 없다고만 말한다.*

![같은 플레이그라운드에서 Bold poster 프리셋을 고른 상태. 카드가 어두운 바탕에 정사각 표지와 큰 제목으로 바뀌고, 아래 프롬프트에 폭 460px, 모서리 20px, 1:1 표지, 34px 제목, 어두운 표면, 보라색 강조가 적혀 있다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/playground-blog-card-preset.png)
*Bold poster 프리셋을 고른 뒤. 프롬프트가 "폭 460px, 모서리 20px, 1:1 표지, 34px 제목, 어두운 표면, hsl(292, 85%, 62%) 강조색"처럼 바뀐 값만 자연어로 적는다.*

스킬이 제공하는 템플릿은 디자인 결정용, SQL과 API와 정규식 같은 데이터 탐색용, 개념 지도용, 문서 비평용이다. 설치는 `/plugin install playground@claude-plugins-official`이고 Apache 2.0 라이선스다.

## scroll-craft: 스크롤이 연출이 되는 페이지

Nate Herk의 [scroll-craft](https://github.com/nateherkai/scroll-craft)는 스크롤에 따라 전개되는 브랜드와 제품 페이지를 만든다. 절차는 브리프, 페이지 문법, 채점, 제작, 검증 순서로 고정되어 있다. 페이지 문법은 한 컷짜리 영상형, 챕터형 편집, 연속된 세계 등 서로 배타적인 여덟 가지이고, 제작물마다 그 사이트에만 있는 상호작용 하나를 반드시 넣어야 한다. 이전 제작물과 얼마나 다른지 보는 지문 검사도 있다. 문법, 내비게이션, 히어로, 막 구조, 마무리, 고유 동작의 여섯 항목 가운데 넷 이상이 달라야 한다.

{{< video src="https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/scrollcraft-ais-scroll.mp4" >}}
*scroll-craft로 만든 [AI Automation Society](https://aiautomationsociety.ai) 페이지를 위에서 아래로 스크롤한 장면. 헤드리스 브라우저 녹화를 3배속으로 빠르게 했다. 사이트 제작자 Nate Herk.*

![AI Automation Society 페이지의 첫 화면. 어두운 바탕에 "The largest global network of AI professionals" 제목과 가입 버튼, 아래에 커뮤니티 앱 화면이 올라오기 시작한다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/scrollcraft-ais-hero.png)
*첫 화면. 아래 가장자리에서 앱 화면이 올라오기 시작한다.*

![같은 페이지를 30% 정도 내린 화면. "Start free. Go as deep as you want." 제목과 여섯 단계 강의 카드가 보인다.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/scrollcraft-ais-30.png)
*30% 정도 내린 지점. 강의 카드 여섯 장이 번호와 함께 나타난다.*

![Nate Herk 개인 사이트 첫 화면. 밝은 바탕에 "AI automation made easy" 제목과 마이크를 든 인물 사진.](https://img.seosoyoung.eiaserinnys.me/images/interactive-web-skills-28/scrollcraft-nateherk-hero.png)
*README에 소개된 또 다른 제작물, 제작자의 [개인 사이트](https://www.nateherk.com).*

스크롤 엔진(`scrollcraft.js`와 `.css`)은 프로젝트마다 고치지 않는다. 스크롤하면 타임라인이 진행되면서 영상이 프레임 단위로 넘어가고, 절이 화면에 고정되고, 제목이 나타난다. 포인터 움직임에도 반응한다. 프로젝트마다 바꾸는 것은 색 토큰 여섯 개와 폰트 두 개뿐이다. 검증 도구는 완성된 페이지를 헤드리스 브라우저로 열어 모든 스크롤 위치에서 확인한다. 아무것도 바뀌지 않는 구간, 끝까지 나타나지 않는 요소, 대비 부족, 포스터 프레임에서 멈춘 영상을 찾아 보고하고, 검토용 콘택트 시트도 만든다. 금지 목록에는 똑같이 생긴 기능 카드를 늘어놓은 격자, 스크롤 안내 화살표, 그라디언트 글자, 지어낸 통계가 들어 있다.

필요한 것은 Node 18 이상, full 빌드 ffmpeg, 검증용 playwright-core와 Chrome이다. 에셋을 생성할 때는 KIE AI 키를 쓰고 비용이 든다. 이 키는 선택 사항이다. README에 따르면 Windows에서만 돌려 봤고 macOS는 시험하지 않았다. MIT 라이선스이고 Claude Code 플러그인(`/plugin marketplace add nateherkai/scroll-craft`)과 Codex 폴더 복사로 설치한다.

## 스타일 지침과 작동 모델

28종은 크게 두 부류다. 하나는 Frontend Design, Impeccable, Taste Skill, UI UX Pro Max처럼 어떤 화면에든 적용하는 범용 디자인 지침이다. 타이포그래피, 간격, 색, 반응형을 다룬다. 화면이 어떻게 생겨야 하는지는 정하지만, 무엇을 만드는지는 정하지 않는다. 다른 하나는 Anatomy, Iso Glow, Playable, Moonshine, scroll-craft처럼 특정 형태의 결과물을 만드는 스킬이다. 이런 스킬은 "무엇이 어떻게 작동해야 하는가"까지 정한다.

두 번째 부류의 스킬에는 지침과 함께 네 가지가 더 들어 있다.

| 들어 있는 것 | 예 | 효과 |
|---|---|---|
| 기반 코드 | Iso Glow의 투영과 조명 템플릿, scroll-craft의 고정 스크롤 엔진 | 에이전트가 매번 새로 짜지 않고 같은 코드를 재사용한다 |
| 실행 예제 | Anatomy 33점, Colorfigures 26점, snow-d3 예제 30개 | 에이전트가 "이렇게 생긴 것"을 참조하고, 사용자는 설치 전에 결과를 본다 |
| 상태 모델 | Anatomy의 부품 움직임과 표시 수치가 같은 모델에서 나옴 | 그림과 설명이 서로 모순되지 않는다 |
| 검증 절차 | scroll-craft의 헤드리스 스크롤 검사, HTML Explainer의 데스크톱과 모바일 캡처, Visual Explainer의 페이지 점검 | 만든 뒤에 에이전트가 스스로 확인한다 |

범용 지침만 있는 스킬은 결과가 모델의 그날 판단에 달려 있다. 기반 코드와 상태 모델이 있는 스킬은 모델이 바뀌어도 결과물의 기본 구조가 같다. 실제로 Colorfigures는 Claude Code, Codex, Gemini CLI, Claude.ai, ChatGPT에서 같은 파일을 설치해 쓰도록 안내한다.

구별해서 볼 것이 세 가지 있다. 첫째, HTML 한 파일과 완전 오프라인은 다르다. Playground와 HTML Artifacts는 CDN까지 금지한다. snow-d3 예제는 D3를 jsDelivr에서 불러오고, Iso Glow의 3D도 three.js를 CDN에서 받는다. 셋 다 HTML 한 파일이지만 네트워크가 없으면 뒤의 둘은 열리지 않는다. 둘째, 생성 환경과 결과물 실행 환경은 다르다. Web Artifacts Builder의 결과는 HTML 한 파일이지만 만들 때는 Node 빌드가 필요하고, Visual Explainer는 Node 렌더러로 파일을 만든다. 셋째, 공개 스킬이라도 비용은 든다. 스킬은 무료여도 스킬을 돌리는 모델의 토큰 비용이 들고, scroll-craft의 생성 에셋이나 Motion+의 고급 기능처럼 외부 서비스 요금이 붙는 것이 있다.

## 고르는 기준

| 만들고 싶은 것 | 스킬 |
|---|---|
| 작동하는 설명 그림 | Anatomy, Iso Glow |
| 조건을 조절하는 실험 도구 | Playground |
| 계속 수정해 쓸 인터랙티브 기술 글 | Moonshine |
| 연출이 강한 제품과 브랜드 페이지 | scroll-craft |
| 필터, 줌, 지도, 차트가 있는 분석 페이지 | OpenAI Build Web Data Visualization |
| 여러 컴포넌트로 이루어진 작은 웹 도구 | Web Artifacts Builder, 품질 보강은 Impeccable |

## 28종 전체 목록

링크는 2026년 10월 22일 기준으로 모두 열리는 것을 확인했다. 설치 방법은 각 저장소의 README를 기준으로 한다.

### A. 직접 조작하는 그림, 장치, 3D 장면

| 스킬 | 한 줄 설명 | 잘 맞는 용도 |
|---|---|---|
| [Anatomy](https://github.com/wheresryan22/anatomy) | 기계와 알고리즘을 조작할 수 있는 등각 도해로. 부품과 수치가 같은 상태 모델. HTML 또는 React | 시스템과 자료구조 설명 |
| [Iso Glow](https://isoglow.dev/) | 작동 부위가 빛나는 선화 도해. 2D와 three.js 3D | 장치, 건물, 도시 설명 |
| [iso-figure](https://github.com/MrBongoC/ai-iso-skill) | 누를 수 있는 부품이 있는 등각 오브젝트를 SVG와 짧은 투영 코드로. 위 둘의 기반 | 자기 스타일로 개조할 출발점 |
| [Playable](https://april-zhu.com/playable) | 스케치나 리깅 모델을 WASD로 조종하는 three.js 캐릭터로 | 로봇, 메카 캐릭터 시연 |
| [3Dviz Pro Max](https://github.com/viettranx/3dviz-pro-max) | 과학, 수학, 알고리즘, 공간 구조를 탐색하는 Vite와 three.js 장면. 레시피 223개와 캡처 도구 | 3D 개념 탐색 |
| [Algorithmic Art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | p5.js 생성 아트 뷰어. 시드와 슬라이더로 매개변수 탐색. Anthropic, Apache 2.0 | 시각 실험 |

### B. 인터랙티브 설명 글, 학습 자료, 문서

| 스킬 | 한 줄 설명 | 잘 맞는 용도 |
|---|---|---|
| [Playground](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/playground) | 조절 패널, 즉시 미리보기, 복사용 프롬프트를 의존성 없는 HTML 한 파일로. Anthropic | 디자인 조율, 조건 탐색 |
| [Moonshine](https://github.com/enjalot/moonshine) | Distill형 기술 글. 단일 HTML(shine)과 React 프로젝트(still), 개발 모드의 페이지 내 편집 | 연재형 기술 설명 |
| [HTML Explainer](https://github.com/ds-vibe/html-explainer) | 조작형 데모 중심의 설명 페이지와 슬라이드. 데스크톱과 모바일 캡처 확인 | 개념 하나를 깊게 |
| [Visual Explainer](https://github.com/nicobailon/visual-explainer) | 아키텍처, 코드 변경, 계획을 시각 문서로. 공통 키트와 Node 렌더러, 선택적 페이지 점검 | 시스템 구조와 변경 설명 |
| [Interactive Explainers](https://github.com/obahareth/skills-public/tree/main/interactive-explainers) | 읽고 조작하고 확인 문제를 푸는 짧은 코스. 인수인계 문서와 출처 기록 동반 | 학습 코스 |
| [HTML Artifacts](https://github.com/joshuadavidthomas/agent-skills/tree/main/html-artifacts) | CSS, JS, SVG, 데이터를 내장한 오프라인 설명과 검토 문서. CDN과 원격 폰트 금지 | 코드 안내, PR 검토 |
| [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) | 애니메이션이 있는 16:9 웹 프레젠테이션을 HTML 한 파일로. PPT 변환 지원 | 발표 자료 |

### C. 스크롤 서사, 데이터 탐색

| 스킬 | 한 줄 설명 | 잘 맞는 용도 |
|---|---|---|
| [Build Web Data Visualization](https://github.com/openai/plugins/tree/main/plugins/build-web-data-visualization) | D3, three.js, 지도, 대시보드, 스크롤리텔링, 접근성과 검증까지 스킬 18개 묶음. OpenAI, Codex 플러그인 | 데이터 설명과 분석 페이지 |
| [snow-d3](https://github.com/jiannanya/snow-d3) | D3 v7 참조와 예제 30개. 줌, 브러시, 드래그, 지도, 네트워크. 예제는 D3를 CDN에서 불러옴 | 차트와 그래프 탐색 |
| [scroll-craft](https://github.com/nateherkai/scroll-craft) | 스크롤, 포인터, 영상, 레이어가 반응하는 제품 페이지. 고정 엔진과 헤드리스 검증 | 브랜드와 제품 페이지 |
| [Scroll World Storytelling](https://github.com/MengTo/Skills/tree/main/agent-skills/web-design/scroll-world-storytelling) | 기사와 제품 서사를 스크롤 영상, three.js 공간, HTML과 SVG 데이터 세 방식 가운데 하나로 | 서사형 소개 페이지 |

### D. 웹 도구, 앱, 게임 제작

| 스킬 | 한 줄 설명 | 잘 맞는 용도 |
|---|---|---|
| [Web Artifacts Builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) | React, TypeScript, Tailwind, shadcn/ui로 만들고 bundle.html 하나로 묶음. 생성에 Node 필요. Anthropic | 여러 탭과 컴포넌트의 작은 앱 |
| [Frontend App Builder](https://github.com/openai/plugins/tree/main/plugins/build-web-apps/skills/frontend-app-builder) | 이미지로 시안을 먼저 만들고 디자인 시스템을 뽑은 뒤 구현 화면과 대조. 이미지 생성과 브라우저 도구 전제. OpenAI | 제품 UI, 대시보드 |
| [Game Studio](https://github.com/openai/plugins/tree/main/plugins/game-studio) | Phaser 2D, three.js, React Three Fiber, 에셋, HUD, 플레이테스트 스킬 9개. OpenAI | 브라우저 게임 프로토타입 |
| [Stitch Design Skills](https://github.com/google-labs-code/stitch-skills) | Stitch 디자인을 코드로 옮기고 여러 페이지 사이트를 구축. Stitch MCP 서버 필요. Google Labs | Stitch 연동 제작 |

### E. 디자인과 상호작용 구현 보강

| 스킬 | 한 줄 설명 | 잘 맞는 용도 |
|---|---|---|
| [Frontend Design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 색과 서체 역할과 와이어프레임을 먼저 정하는 계획 단계, 구현 중과 후의 비평 단계. Anthropic | 어떤 화면에든 |
| [Impeccable](https://github.com/pbakaus/impeccable) | 설계부터 마감까지 audit, harden, animate, polish, typeset 등 명령 24개 | 반응형, 긴 글, 오류 상태 보강 |
| [Taste Skill](https://github.com/Leonxlnx/taste-skill) | 참고 방향과 공개 아카이브 사진으로 개성 있는 화면. 여러 폭에서 브라우저 검사. Node 22 이상 | 공개 사이트 첫인상 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 스타일 79종, 팔레트 192개, 서체 조합 74개, UX 지침 119개를 오프라인 검색해 적용 | 스택별 UI 규칙 |
| [GSAP AI Skills](https://github.com/greensock/gsap-skills) | GSAP 제작사 공식. 코어, 타임라인, ScrollTrigger, 플러그인, React, 성능 스킬 8개 | 애니메이션 구현 |
| [Motion AI Kit](https://github.com/motiondivision/ai-kit) | 문서 검색과 스프링 생성은 무료, MotionScore 감사와 예제 소스 검색은 Motion+ 회원 전용 | UI 전환과 레이아웃 애니메이션 |
| [Three.js Skills](https://github.com/CloudAI-X/threejs-skills) | 기하, 재질, 조명, 로더, 셰이더, 인터랙션 등 스킬 13개. 커뮤니티 프로젝트이며 three.js 공식은 아님 | 3D 조작 보강 |

## 계보와 검증

눈여겨본 것은 두 가지다. 먼저, April Zhu의 스킬 세 개는 한 계보다. Tolga Cohce의 iso-figure가 등각 투영과 "모든 그림은 무언가를 해야 한다"는 규칙을 정했다. Iso Glow는 여기에 조명과 팔레트와 3D를 더했고, Colorfigures는 색과 손그림 질감을 더했다. Playable은 Iso Glow의 시각 템플릿에 캐릭터 제어기를 추가했다. 네 스킬이 같은 기반 코드를 물려받으니 결과물도 한 가족처럼 보인다. 프롬프트 모음으로 끝나는 스킬이 대부분인데, 이 네 스킬은 코드처럼 상속된다.

다음으로, 검증 절차도 스킬에 포함되기 시작했다. scroll-craft는 완성된 페이지를 스크롤하며 화면이 그대로인 구간을 결함으로 보고하고, HTML Explainer는 모바일 화면까지 캡처한다. 페이지를 만든 에이전트가 독자에게 보일 화면을 직접 확인하는 절차까지 스킬 파일에 적혀 있다.

## 출처

- 28종의 설명은 2026년 10월 22일 기준 각 저장소의 README와 SKILL.md, 제작자 공개 페이지를 바탕으로 했다. 같은 조건의 비교 실험은 하지 않았으며, 직접 설치해 본 것은 Playground 하나다.
- 화면의 출처는 Anatomy, Iso Glow, Colorfigures, Playable, HTML Explainer, Moonshine의 공개 데모 페이지와 scroll-craft README에 소개된 두 사이트다. Playwright의 헤드리스 Chromium(1280x800)에서 열고 키보드와 버튼을 조작해 캡처했고, 영상 두 편도 같은 방식으로 녹화했다. 모든 캡처의 저작권은 각 제작자에게 있다.
- iso-figure의 GIF는 저장소의 소개 이미지(MIT)를 그대로 가져왔다. Playable 데모 모델은 Quaternius와 Tomás Laulhé의 CC0 모델이다.
- Playground 화면 두 장은 제작자의 데모가 아닌, 이 글을 위해 만든 것이다. Claude Code의 서브 에이전트(Claude Sonnet)가 플러그인 저장소의 SKILL.md와 design-playground 템플릿을 읽고 HTML 한 파일을 만들었고, 헤드리스 Chromium에서 프리셋 전환과 프롬프트 갱신만 확인했다.
- 라이선스: Anatomy, Iso Glow, iso-figure, Playable, Colorfigures, Moonshine, HTML Explainer, scroll-craft, snow-d3, Visual Explainer, HTML Artifacts, Frontend Slides, Taste Skill, UI UX Pro Max, GSAP AI Skills, Three.js Skills, 3Dviz Pro Max는 MIT. Impeccable, Stitch Design Skills, 그리고 Anthropic의 Playground, Algorithmic Art, Web Artifacts Builder, Frontend Design은 Apache 2.0. OpenAI 플러그인 셋은 plugin.json 기준 MIT. Motion AI Kit은 저장소에 라이선스 파일이 없다.

원문: <https://april-zhu.com/colorfigures>
