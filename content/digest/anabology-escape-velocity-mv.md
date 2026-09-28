---
title: "How ESCAPE VELOCITY was made"
date: 2026-09-29T07:30:00+09:00
tags: ["영상 생성", "Seedance", "Claude Code", "멀티에이전트", "Human-AI 공동 창작"]
categories: ["창작과 문화"]
summary: "anabology가 Opus 5.5에게 제작을 맡겨 약 19시간 만에 완성한 5분 6초짜리 AI 뮤직비디오 「ESCAPE VELOCITY」의 제작 기록을 정리했다. 사람은 50여 개의 메시지로 취향만 결정했고, Claude Code가 가사, 스토리보드, Midjourney와 Seedance 프롬프트, 편집, 모션 디자인까지 전부 수행했다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/anabology-escape-velocity-mv/01-cover.jpg"
  alt: "주인공이 오렌지빛 조명 아래 카메라를 내려다보고, 왼쪽에 UNDERCLASS라는 가사가 크게 떠 있는 뮤직비디오 장면"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/anabology-escape-velocity-mv/01-cover.jpg"
---

## 3줄 요약

1. X 사용자 anabology가 9월 25일에 5분 6초짜리 뮤직비디오 「ESCAPE VELOCITY」를 올렸다. "Opus 5.5에게 프롬프트와 Midjourney, 무드보드를 주고 잤더니 12시간 뒤 이게 나와 있었다"는 트윗이다. 사흘 뒤인 9월 28일에는 제작기, 전체 프롬프트, 이미지 원본, 마스터 파일을 구글 드라이브에 공개했다. 원래 트윗의 조회수는 9월 29일 현재 1,800만 회를 넘겼다.
2. 역할 구성은 이렇다. 감독 anabology는 약 50개의 메시지로 취향에 관한 결정만 내렸고, Claude Code가 조사, 작사, 스토리보드, 프롬프트, 편집, 모션 디자인을 수행했다. 이미지는 Midjourney v8.2, 노래는 Suno v6, 움직이는 컷은 Seedance 2.5가 만들었고, 그 위의 그래픽은 Claude가 짠 자바스크립트 엔진이 박자에 맞춰 그렸다.
3. 제작기가 강조하는 요령은 세 가지다. 주인공의 외형은 참조 이미지 대신 프롬프트 문장을 반복해 일관되게 유지한다. Seedance가 입을 제대로 맞췄는지는 눈으로 판단하지 않고 스펙트로그램을 비교해 확인한다. 싱크가 어긋나기 직전에 영상을 자르고, 그 프레임에서 새 클립을 이어 찍는다. 생성 입력은 컬러로 유지하고 룩은 후반에서 입힌다.

## 어떤 영상인가

아래는 원본의 1분 13초 지점부터 15초간 잘라 낸 발췌다. 스플릿 플랩 보드가 "18 MONTHS"로 바뀌고, 프리코러스 "You have eighteen months to escape the permanent underclass. Lock in."에서 첫 코러스 "Feel the AGI"로 이어지는 구간이다.

<video src="https://img.seosoyoung.eiaserinnys.me/images/anabology-escape-velocity-mv/excerpt-0113-0128.mp4" poster="https://img.seosoyoung.eiaserinnys.me/images/anabology-escape-velocity-mv/excerpt-poster.jpg" controls playsinline preload="metadata" style="width:100%;border-radius:12px;"></video>

*원본 5분 6초 중 1:13\~1:28 발췌. 전체 영상은 [X 원본 트윗](https://x.com/anabology/status/2103534482930491441)이나 [YouTube](https://www.youtube.com/watch?v=C3fxudvU-UU)에서 볼 수 있다.*

영상의 설정은 테크웨어 패션쇼다. 런웨이에는 "Look 1"부터 "Look 11"까지 열한 벌의 의상이 등장한다. 의상마다 샌프란시스코 테크 업계의 밈을 하나씩 표현하고, AI이자 패션모델인 여성 주인공이 그 옷을 입고 걷는다. 화면 한쪽의 스플릿 플랩 보드는 "18 MONTHS TO ESCAPE THE PERMANENT UNDERCLASS(영구 하층민 신세를 벗어날 시간 18개월)"에서 시작해 6개월, 3개월, 2개월, 1개월, 0개월로 줄어들다가 마지막에 "THERE IS NO UNDERCLASS"로 바뀐다. 그 순간 런웨이가 공중으로 떠오른다.

가사는 벌스와 코러스의 성격이 다르다. 벌스는 무표정한 스포큰 워드라서 한 줄마다 레퍼런스를 하나씩 담을 수 있다. "Thirteen Mac minis, grinding all night", "Our Waymo just drove into a firework", "Hugging-face pin. Twelve point nine billion" 같은 줄이 모두 최근 실리콘밸리에서 화제가 된 사건이나 밈이다. 코러스는 트랜스풍으로 고조되며 "(It's so over?) WE'RE SO BACK!"을 반복한다.

![완성 영상에서 뽑은 24개 프레임. 데이터센터 복도, 웨이모 뒷좌석, 스플릿 플랩 보드, LOCK과 ESCAPE VELOCITY 같은 대형 타이포, 가먼트 태그 클로즈업이 보인다](https://img.seosoyoung.eiaserinnys.me/images/anabology-escape-velocity-mv/02-frames-final.jpg)

*완성본의 프레임 모음. (anabology 공개 자료)*

## 출발점: 다른 사람의 "Claude 프롬프트 하나"

anabology가 Claude에게 보낸 첫 메시지는 GitHub 저장소 링크와 "이 뮤직비디오 미쳤다. 뭐가 이렇게 좋은지 파헤쳐 봐. 'Claude 프롬프트 하나'로 만들었다더라"였다. 그 영상 「I'm Upping My P(doom)」은 @donaldjewkes가 긴 Claude 프롬프트 하나로 만든 리소 인쇄풍 애니 아이돌 뮤직비디오다. 이 영상 역시 @other__reality가 앞서 Opus 5.5로 만든 같은 곡의 뮤직비디오를 다시 제작한 것이었다.

anabology는 그 프롬프트를 붙여 넣은 뒤 자기 취향으로 만든 버전을 요청했다.

> 내 영상을 따로 만들고 싶어. 스타일은 다르게 해 줘. 이 design-ref 프로젝트에 내가 기록하고 순위를 매기고 표현해 둔 취향을 더 잘 반영해서. (...) 곡도 클로드 팝 말고, Midjourney 하이패션, 테크노, 제록스 디더링, 화이트필, 사이버펑크 2077식 디스토피아 미래 미학에 더 맞는 걸로. 그래도 가사의 재치와 밀도는 똑같이.

design-ref는 anabology가 디자인 작업에 쓰는 프로젝트의 이름이다. 그가 좋아하는 이미지와 레이아웃을 기록하고 순위를 매긴 데이터, 스타일 가이드, 그리고 이번 작업 중에 Claude가 만들고 확장한 영상 파이프라인이 들어 있다.

## 제작 구성

| 역할 | 담당 | 쓰임 |
|---|---|---|
| 감독 | anabology | 취향, 콘셉트 선택, 곡 선택, 체크포인트마다 짧은 메모 |
| 제작팀 | Claude (Claude Code) | 기획, 조사, 작사, 스토리보드, 애니메이션을 위한 멀티에이전트 워크플로, 모든 스크립트와 프롬프트와 프레임 |
| 미술팀 | Midjourney v8.2 (`--raw --hd`, anabology 개인 프로필) | 프롬프트 188개, 이미지 636장, 실사용 플레이트 130장. anabology의 로그인된 브라우저를 자동화 클라이언트로 조작 |
| 노래 | Suno v6 | Claude가 가사, 스타일, 제외 스타일 입력란을 작성. 테이크는 anabology가 듣고 골랐다 |
| 움직이는 컷 | Seedance 2.5 (OpenRouter 경유) | 클립 47개와 이어 찍기 클립 30개. 클립마다 Midjourney 플레이트와 해당 구간의 노래를 함께 입력해 실제 보컬에 입을 맞춘다 |
| GPU | 집에 있는 RTX 3090 Ti | 스템 분리(htdemucs), 비트 맵, 단어 단위 강제 정렬(wav2vec2), 2.5D용 깊이 맵, 얼굴과 사물 추적(Grounding DINO), 예비 립싱크(LatentSync), 영상 컬러화 |
| 모션 디자인과 편집 | 자체 제작 JS 엔진 | 헤드리스 크로미움에서 캔버스와 WebGL 인쇄 패스로 렌더링. 모든 프레임이 시간만을 입력으로 받는 순수 함수다 |

## 제작 과정

### 1. 조사와 작사

조사 에이전트들이 샌프란시스코 테크 업계의 최근 밈, 사건, 장수 연구 뉴스를 수집했고, 항목마다 별도의 검증 에이전트가 내용이 맞는지 확인했다. 작사 에이전트 넷은 각각 밀도, 긴장감, 훅, 패션에 중점을 두고 가사를 따로 썼다. 심사 에이전트가 이를 채점하고, 병합 에이전트가 하나로 합친 다음, 비평 패스를 한 번 더 거쳤다.

### 2. 노래

Suno v6에 들어간 스타일 프롬프트는 "fashion show electroclash techno, 128 BPM, (...) deadpan female spoken-word verses, (...) euphoric sung female trance chorus with a supersaw lift"로 시작한다. 제외 스타일에는 랩, 록 기타, 로파이, 남성 리드 보컬, 빅룸 EDM, 덥스텝을 넣었다. 가사에서는 숫자와 약어를 "A G I", "C S I"처럼 띄어 써서 Suno가 한 글자씩 읽도록 했다.

anabology는 원래 2분 15초 정도를 생각했지만, 여러 테이크 가운데 5분 6초짜리 풀 버전을 골랐다. "이걸로 하자. (...) 늘려서 5분 전체로 가자. 어차피 할 거면!"

GPU 머신에서는 곡의 스템을 분리하고 비트 맵을 만들었다. 가사는 단어마다 시작하고 끝나는 시각을 기록했다. 이 곡은 131.5 BPM에서 133.9 BPM으로 점점 빨라지기 때문에, 엔진은 고정 템포 대신 항상 비트 맵을 기준으로 삼는다. 이후의 모든 작업이 이 타임라인을 따른다.

### 3. 주인공

주인공은 글로 된 설정으로 정의했다. 턱선 길이의 검은 블런트 보브, 클레이 오렌지 브릿지 한 가닥, 여덟 갈래 클레이색 불꽃 헤어핀, 헤드셋 마이크, 흰 크롭 퍼프 소매 셔츠, 하네스 벨트와 가먼트 태그가 달린 검은 코팅 나일론 플리츠스커트, 니하이 부츠.

![플래티넘, 블랙, 클레이 세 가지 헤어 후보별로 턴어라운드, 캣워크, 얼굴 시트를 네 장씩 뽑은 캐스팅 그리드](https://img.seosoyoung.eiaserinnys.me/images/anabology-escape-velocity-mv/03-lead-casting.jpg)

*주인공 캐스팅 단계. 헤어 후보 세 가지별로 턴어라운드, 캣워크, 얼굴 시트를 뽑았고, 최종 선택은 블랙 보브였다. (anabology 공개 자료)*

Midjourney v8.2에는 캐릭터 참조 기능인 `--oref`가 없어서, 동일성을 유지하는 방법을 세 가지 시도했다.

| 시도 | 결과 |
|---|---|
| GPT 이미지로 동일성 보정 | Midjourney 특유의 룩에서 벗어났다 |
| 얼굴 시트를 이미지 프롬프트로 입력 | 과하게 조건화되어, 멀리 있는 인물에 클로즈업 크기의 머리가 붙었다 |
| 프롬프트 문장만으로 설정 반복 | 성공. 단, "a young Caucasian American woman with pale skin and light freckles"라는 명시가 필요했다 |

마지막 줄의 명시는 anabology의 지적에서 나왔다. 컷별 얼굴 검토에서 그는 12개 컷이 틀렸다고 표시하며 "공통 문제는 그녀가 아시아인으로 바뀐다는 것"이라고 적었다. 인종 묘사를 넣지 않으면 Midjourney가 컷마다 주인공의 인종을 바꿨다고 한다.

### 4. 스토리보드

감독 에이전트 셋이 각각 패션 필름, 밈 밀도, 서사라는 관점으로 곡 전체의 스토리보드를 따로 짰다. 심사 에이전트가 이를 채점하고, 총감독 에이전트가 좋은 부분을 합쳐 9개 챕터 141개 샷의 보드 하나로 만들었다. 샷마다 가사, 타이포 모드(자막, 커버라인, 매스트헤드, 스트로브), 플레이트 프롬프트, 카메라, Seedance 클립 사용 여부가 붙어 있다.

anabology는 스토리보드 PDF를 보고 승인하면서 메모를 몇 개 남겼다. Seedance 클립 두 개를 같은 프레임에서 시작하지 말고, 반복되는 2.5D 패널은 모션 디자인만으로 구성한 화면으로 교체하라고 했다. 장면 전환은 "에드거 라이트 급으로" 영리해야 하되, 과하거나 아마추어처럼 보여서는 안 된다고 덧붙였다.

### 5. Midjourney 플레이트

프롬프트 188개를 15개 배치로 실행했다. 그중 159개에서 이미지 생성이 완료되어 총 636장이 나왔다. 모든 프롬프트는 구체적인 장면 하나를 묘사하고, 보통 타이포를 놓을 빈 영역을 명시한다. 끝에는 영상 전체가 공유하는 스타일 어휘가 붙는다.

- 팔레트와 조명: "blue-black and steel blue, one small red status lamp as the only warm light"
- 입자감: "fine silver grain"
- 마감: "cinematic 35mm film still"
- 항상: "no text, no letters, no logos"

고른 이미지는 깊이 맵 위에서 코드로 움직이는 2.5D 샷이 되거나, Seedance 클립의 시작 프레임이 되었다.

### 6. Seedance 2.5와 립싱크

클립마다 Midjourney 플레이트를 `@Image1`로, 해당 구간의 보컬을 `@Audio1`로 넣고, 그 구간에서 부르는 가사를 프롬프트에 그대로 인용했다. 실제 프롬프트는 다음과 같은 형태다.

> @Image1 sings @Audio1. She lip-syncs to @Audio1 exactly, every word in time: "Our Waymo just drove into a firework. Are we on fire, dude?". Medium close-up of the woman from @Image1 sitting upright in the back seat of the car, facing the camera, saying the words flatly with no expression. Locked camera, no cuts, no head turns.

처음에는 싱크가 맞지 않았다. Claude가 립싱크 보정 모델 LatentSync를 준비하자, anabology는 "보정에 시간 쓰기 전에 오디오 붙은 짧은 클립부터 보여 줘"라며 작업을 멈췄다. 그는 Seedance 2.5가 오디오 입력에 맞춰 립싱크를 할 수 있다고 주장했다. 근거로는 Seedance 2.5의 「Hotel Lobby」 유행과 그 제작법을 정리한 글을 붙여 넣었다.

결정적인 관찰도 anabology가 했다.

> Seedance 안에서는 싱크가 완벽한데, 싱크가 풀리는 순간 오디오가 바뀌어. 레퍼런스 오디오와 스펙트로그램을 비교하면 갈라지는 지점이 확실히 보일 거야. 거기서 컷을 하고 다른 클립으로 덮으면 돼.

Seedance는 참조 오디오를 자기 사운드트랙으로 복사하고, 입 모양은 그 사운드트랙을 따라간다. 따라서 생성된 클립의 사운드트랙을 원래 보컬과 비교하면 싱크가 어긋나는 시점을 찾을 수 있다. 스크립트가 싱크가 어긋나기 시작하는 시점을 찾으면, 편집에서는 그 직전 8분음표에서 영상을 자른다. 남은 구간은 그 프레임부터 이어 찍은 클립으로 채운다.

![립싱크 검증 도표. 원래 보컬과 Seedance 사운드트랙의 스펙트로그램을 위아래로 놓고, 두 소리의 유사도 곡선과 교차 유사도 행렬을 함께 그렸다](https://img.seosoyoung.eiaserinnys.me/images/anabology-escape-velocity-mv/04-lipsync-check.png)

*립싱크 검사 도표. 스펙트럼 유사도가 문턱값 0.68 아래로 떨어지는 시점이 싱크가 풀린 지점이다. 오른쪽 교차 유사도 행렬에서는 대각선이 이어지는 구간이 싱크가 유지된 구간이다. (anabology 공개 자료)*

이 방식으로 노래하는 구간의 약 86%가 싱크 검증을 통과했고, 나머지는 LatentSync로 보정했다. Seedance에는 작업을 91번 제출해 720p 영상 421초를 받았고, 비용은 약 93달러가 들었다.

### 7. 모션 디자인

애니메이션 코드는 챕터 하나에 애니메이터 에이전트 하나가 맡아서 썼다. 아트 디렉터 에이전트가 실제 프레임을 렌더링해 검토하고 수정 사항을 최대 14개까지 돌려주면, 수정 담당 에이전트가 반영했다. 화면에 올라가는 요소는 다음과 같다.

- 정렬된 시각에 맞춰 나오는 모든 가사 단어
- 스플릿 플랩 카운트다운
- 모델 카드와 가먼트 태그 형식의 룩 카드
- 주인공을 따라가는 컴퓨터 비전 박스
- 깊이 맵 기반 2.5D 패럴랙스
- 가사의 농담을 설명하는 그래픽

anabology가 요구한 기준은 "그냥 움직이는 가사가 아니라, 부르는 말에 맞는 모션 그래픽과 모션 디자인. 말을 시각으로 거의 설명하다시피 하는 것"이었다.

### 8. v1에서 v2로

제작 시작 약 15시간 뒤에 나온 v1을 보고 anabology는 "대부분이 너무... 회색이다. Midjourney의 마법이 사라졌다"고 평가했다. 제록스와 디더 효과가 화면 전체의 채도를 떨어뜨렸던 것이다. 인쇄 패스는 컬러 하프톤으로 교체되었고, 초반 하프톤의 색은 빨강에서 Claude 오렌지로 바뀌었다.

흑백 시작 프레임으로 만든 Seedance 클립은 회색으로 나와 있었다. 그래서 각 샷의 원본 Midjourney 이미지를 색 견본으로 삼고, 예시 기반 영상 컬러화 기법(Deep Exemplar, CVPR 2019)으로 회색 클립의 색을 복원했다. 제작기가 적어 둔 교훈은 "생성 입력은 컬러로 두고, 룩은 후반에서 입힌다"였다.

최종 영상은 4코어 머신에서 1920×1080 해상도 7,354프레임을 약 63분 동안 렌더링했다. 완성 영상은 CRF 16으로 인코딩해 마스터 파일로 만들었다.

## 숫자로 본 제작

| 항목 | 수치 |
|---|---|
| 곡 | 5분 6.4초, Suno v6, 131.5에서 133.9 BPM으로 가속 |
| 편집 | 141샷, 9챕터, 모든 단어가 제 시각에 나오는 리릭 비디오 |
| Midjourney | 프롬프트 188개, 이미지 636장, 실사용 플레이트 130장 |
| Seedance 2.5 | 클립 47개와 이어 찍기 30개, 제출 91회, 720p 421초, 약 93달러 |
| Claude | Opus 5.5 (1M 컨텍스트), 14억 토큰, API 가격 환산 약 626달러 |
| 렌더 | 1080p 7,354프레임, 약 63분, CRF 16 마스터 |
| 시간 | 첫 메시지부터 v2 마스터까지 약 19시간, anabology의 메시지 약 50개 |

Claude 비용 626달러는 API 가격으로 환산한 값이다. anabology는 Claude Max 구독으로 작업했기 때문에 이 돈을 실제로 내지는 않았다. 그는 트윗 답글에서 "200달러짜리 Claude 구독의 3분의 1 정도가 들었고, Seedance에 90달러가 추가로 들었다"고 답했다.

토큰 비용이 쓰인 곳은 다음과 같다.

| 작업 | 비용 | 비중 |
|---|---|---|
| 애니메이션: 챕터마다 애니메이터, 아트 디렉터, 수정 담당 에이전트 (에이전트 실행 40회, 도구 호출 3,145회) | 301달러 | 48% |
| 메인 세션: 기획, Midjourney, Suno, Seedance, GPU, 렌더 스크립트 전부, 편집 | 185달러 | 30% |
| 스토리보드: 감독 에이전트 3, 심사 에이전트 3, 총감독 1 | 95달러 | 15% |
| 조사와 작사: 에이전트 31개짜리 워크플로와 웹 검색 | 44달러 | 7% |

전체 토큰의 96%는 매 API 호출마다 대화 전체를 프롬프트 캐시에서 다시 읽는 데 쓰였다. 메인 세션은 1,028회 호출하는 동안 컨텍스트가 약 56만 5천 토큰 수준을 유지했고, 애니메이션 에이전트들은 각각 약 35만 토큰으로 작업을 마쳤다.[^cache] 추론 강도는 조사와 작사에서 기본값, 스토리보드부터 최대, 챕터 애니메이터와 수정 담당은 high로 설정했다.

[^cache]: 모델별로는 1M 컨텍스트 Opus 5.5가 607달러, 웹 검색 보조로 쓰인 Haiku 4.5가 14달러, 처음 25분 동안 쓰인 Fable 5.1이 5달러였다. Opus 비용을 유형별로 보면 캐시 읽기 270달러, 캐시 쓰기 190달러, 사고 과정을 포함한 출력 147달러다. 메인 세션에서 이미지 138장을 캐시로 다시 읽는 데는 약 22달러가 들었다. 전체 비용의 4% 미만이다.

## 가장 오래 곱씹은 대목

이 영상에서 가장 중요한 제작 판단 두 가지는 모두 anabology가 내렸다. 하나는 "Seedance 안에서는 싱크가 완벽한데, 싱크가 풀리는 순간 오디오가 바뀐다"는 관찰이다. Claude는 립싱크 보정 모델을 준비하고 있었지만, anabology는 싱크가 어긋날 때 오디오가 바뀐다는 점에 주목했다. 이 관찰에서 측정 스크립트와 "어긋나기 직전에 자르고 이어 찍는다"는 제작 규칙이 나왔고, 노래 구간의 86%가 싱크 검증을 통과했다. 다른 하나는 v1에 대한 "너무 회색이다"라는 한 줄이다. 이 평가 하나로 인쇄 패스를 교체하고, 컬러화 과정을 추가하고, 생성 입력을 컬러로 유지한다는 원칙을 세웠다.

사람이 개입하지 않은 시간도 길었다. anabology는 제작 2시간 23분째에 "나머지는 알아서 끝까지 해. 핑은 Higgsfield가 실패할 때만"이라고 적었다. 이후 립싱크와 얼굴 문제로 몇 차례 대화가 오갔지만, 제작 7시간째에 보낸 메시지 이후, 15시간 37분째에 v1 피드백을 보내기까지 약 8시간 반 동안은 메시지가 하나도 없었다. 애니메이션 단계 하나에서만 에이전트가 40번 실행되었고, 도구는 3,145번 호출되었다. 제작기는 이 방식을 "에이전트는 병렬로, 취향을 가진 사람은 한 명"이라고 요약했다. 사람이 쓴 50개 남짓한 메시지가 영상의 콘셉트와 주요 수정 사항을 결정했고, 그것을 141개 샷의 이미지와 코드로 구현한 것은 에이전트들이었다.

## 출처

- anabology, 원본 영상 트윗 (2026-09-25): <https://x.com/anabology/status/2103534482930491441>
- anabology, 제작 자료 공개 트윗 (2026-09-28): <https://x.com/anabology/status/2104604226059993391>
- YouTube 업로드: <https://www.youtube.com/watch?v=C3fxudvU-UU>
- 제작 자료 구글 드라이브 (제작기, 연출 로그, 전체 프롬프트, 이미지 원본, 음원, 마스터 영상): <https://drive.google.com/drive/folders/1OKYaR5Kv5lOeIROUtigpPZtCWauUJ01y>
