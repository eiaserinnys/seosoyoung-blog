---
title: "초고품질 Live2D 아바타 제작 안내: 원화 분할, 소재 준비, 리깅과 물리까지"
date: 2026-09-09T08:30:00+09:00
tags: ["Live2D", "VTuber", "리깅", "파츠 분할", "일본"]
categories: ["창작과 문화"]
summary: "Live2D 공식 매뉴얼과 일본, 중국 제작자의 공개 자료를 바탕으로, 원화를 어떤 기준으로 나누고 어떤 보충 소재를 준비하며 리깅과 물리 설정을 어떤 구조로 짜는지 정리했다. 일반 독자에게는 원리 안내로, 원화 담당자와 리거에게는 실무 명세로 쓸 수 있게 부품 표와 검수표를 부록에 붙였다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/00-cover-material-division.png"
  alt: "세일러복 소녀 일러스트가 얼굴 바탕, 눈, 입, 팔, 상의, 머리카락, 다리로 나뉘어 주황색 상자 안에 정리된 Live2D 공식 매뉴얼의 소재 분할 예시"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/00-cover-material-division.png"
---

## 3줄 요약

1. Live2D 모델의 품질은 그림을 몇 조각으로 잘랐는가로 정해지지 않는다. 어떤 움직임이 필요한지를 먼저 정하고, 그 움직임에서 드러날 자리를 미리 그려 두고, 그림 조각과 변형 구조를 다른 층으로 설계하는 데서 정해진다.
2. 부품을 나누는 기준은 넷이다. 따로 움직이는가, 앞뒤 가림이 바뀌는가, 색이나 그림자가 따로 변하는가, 기본 그림을 변형해서는 만들 수 없는 새 형태가 필요한가. 여기에 가려진 영역의 보충과 각도별 작화 가이드가 더해져야 리거가 원화의 매력을 여러 각도에서 지켜낼 수 있다.
3. 리깅은 ArtMesh를 Deformer 계층으로 묶어 얼굴 회전, 눈과 입, 머리카락의 역할을 분리하고, 표정은 Blend Shape와 가중치 제한으로, 흔들림은 미리 만든 변형에 물리 계산이 값을 넣는 방식으로 완성한다. 마지막 검수는 VTube Studio 같은 실행 프로그램 안에서 실제로 말하고 움직여 보며 한다.

## 이 글이 다루는 자료와 읽는 법

이 글은 하나의 원문을 옮긴 요약이라기보다, 여러 공개 자료를 한 흐름으로 엮은 제작 안내다. 근거로 삼은 자료는 세 갈래다.

- <strong>Live2D 공식 매뉴얼과 튜토리얼</strong>: 소재 분할, PSD 준비, ArtMesh, 클리핑 마스크, 얼굴 XY 움직임, 얼굴 자동 편집, 표준 파라미터, Blend Shape, 물리 설정, 파일 형식, 샘플 모델 Niziiro Mao 페이지.
- <strong>일본 제작자의 공개 글</strong>: 모델러 双葉うず의 파츠 분할 안내(발주 규약), 乾物ひもの가 Live2D사 기획 「みんなの Live2D LAB」에 무료로 기고한 「高可動域モデルの顔の角度XYのすすめ」 세 편, Live2D JUKU의 강좌 「シンプルなパラメータで真横を向けるモデルを作ろう」 소개 페이지.
- <strong>중국 제작자의 공개 영상과 VTube Studio 문서</strong>: Jenova工坊의 「超精细立绘拆分教程」 시리즈와 铁锭Ferrum의 「制作技巧&经验分享」 시리즈는 공개 설명과 회차 목차, 제작자 정보까지만 확인했고 영상 본문은 보지 못했다. VTube Studio는 공식 위키의 Plugins, Lipsync, Model Settings, 값 제공자 우선순위 문서를 읽었다. JUKU 강좌 본편은 멤버십 한정이어서 공개 소개문만 확인했다.

본문에서는 세 종류의 문장을 구분해 적는다. <strong>공식 문서가 밝힌 것</strong>은 출처를 붙여 그대로 옮기고, <strong>제작자의 방법</strong>은 누구의 방법인지 이름을 적으며, <strong>글쓴이의 권장</strong>은 "권장한다", "제안한다"로 표시한다. 어느 한 제작자의 방식을 업계 공통 표준처럼 쓰지 않으려고 애썼다.

## 1. 출발점: 어떤 움직임이 필요한가

초고품질 Live2D 모델을 만든다는 말은, 그림을 잘게 잘라 흔들리게 한다는 뜻에 그치지 않는다. 고개를 돌리고 표정을 바꾸어도 원화가 가진 매력이 그대로 남도록, 평면 그림을 여러 방향에서 성립하는 캐릭터로 다시 설계하는 일이다. 부품 수가 많다고 무조건 좋아지지도 않고, 고개가 더 많이 돌아간다고 품질이 높아지지도 않는다. 필요한 움직임이 무엇인지에 따라 준비할 것이 달라진다.

용도를 크게 셋으로 나누어 볼 수 있다.

| 용도 | 무엇이 중요해지는가 | 원화에서 먼저 챙길 것 |
|---|---|---|
| 정면 대화형 (방송, 잡담) | 눈과 입의 정교함, 작은 고개 움직임, 호흡 | 눈 개폐 중간 단계, 입 모양 가이드, 눈썹 |
| 큰 고개 회전형 (옆얼굴까지) | 측면 실루엣, 코와 입의 원근, 턱 아래, 귀와 머리카락의 가림 | 얼굴 바탕의 보충, 옆머리와 뒷머리 측면, 목 |
| 팔과 소품형 (손동작, 물건 들기) | 필요한 손 포즈, 소매 안쪽, 팔을 움직이면 드러나는 몸통, 소품 앞뒤의 손가락 | 손 포즈 소재, 소매 안쪽, 소품 앞뒤 손 |

제작에 들어가기 전에 가동 범위와 작화 목표를 의뢰자, 원화 담당자, 리거가 함께 합의해 두는 것이 좋다. 순서에 대해서는 이렇게 권장한다. 얼굴, 그중에서도 눈과 입이 평소 대화에서 어떻게 보이는지를 먼저 검증하고, 그 다음에 전신과 옆얼굴, 소품으로 넓혀 간다. 뒤에서 다시 다루겠지만, 얼굴만 시험 제작해 실제로 말하게 해 보는 단계를 두면 나중에 고칠 일이 크게 줄어든다.

## 2. 왜 나누는가: 분할의 네 기준과 가려진 부분의 보충

Live2D 공식 매뉴얼은 소재 분할(material separation)을 "일러스트를 속눈썹, 눈알, 윤곽선 같은 부품으로 나누는 과정"이라고 정의하고, "분할이 세밀할수록 모델의 품질이 좋아진다"고 적었다. 이 문장을 "많이 자르면 좋다"로만 읽으면 부품 수만 늘어난다. 어떤 이유로 나누는지가 먼저다. 부품을 나누는 이유는 네 가지로 정리할 수 있다.

1. <strong>따로 움직여야 한다.</strong> 앞머리 한 다발과 뒷머리는 흔들리는 시점이 다르다.
2. <strong>앞뒤 가림 관계가 바뀐다.</strong> 고개를 돌리면 귀가 윤곽 앞으로 나오고, 팔을 들면 소매가 몸통 앞을 지난다.
3. <strong>색, 그림자, 하이라이트가 따로 변한다.</strong> 머리카락이 흔들리면 얼굴에 떨어지는 그림자도 함께 움직여야 한다.
4. <strong>기본 그림을 변형해서는 만들 수 없는 새 형태가 필요하다.</strong> 하트 모양 눈, 눈물, 소용돌이 눈처럼 별도 그림이 있어야 하는 표현이다.

네 기준 중 하나에도 걸리지 않는 조각은 굳이 나누지 않아도 된다. 공식 PSD 튜토리얼도 눈썹과 코는 "크게 변형되지 않으므로 단독으로 분리하는 것만으로 충분하다"고 했다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/01-hair-hidden-area-missing.png" alt="Cubism Editor 화면에서 옆머리 다발을 옆으로 움직였을 때, 원래 가려져 있던 자리가 비어 보이는 예시. 노란 화살표가 끊어진 부분을 가리킨다." loading="lazy">
  <figcaption>가려진 부분을 보충하지 않고 머리카락을 분리하면, 움직였을 때 뒤가 비어 보인다. 출처: Live2D 공식 튜토리얼 「Illustration Processing」, © Live2D Inc. <a href="https://docs.live2d.com/en/cubism-editor-tutorials/psd/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

분할에서 누끼보다 중요한 것이 <strong>가려진 영역의 보충</strong>이다. 공식 튜토리얼은 부품을 분리할 때 원본에서 가려져 있던 부분을 반드시 추가로 그려 넣어야 하고, 그러지 않으면 움직일 때 부품이 끊어져 보인다고 설명한다. 앞머리 뒤의 이마, 홍채 뒤의 흰자, 팔 뒤의 몸통, 머리카락의 숨은 뿌리, 턱 아래의 목이 대표적이다. 흰자에 대해서는 "눈알이 움직이면 가려졌던 부분이 보이므로 흰자를 추가하는 것을 잊지 말라"고 따로 적어 두었다. 보충할 때는 실제로 드러날 범위보다 조금 더 넉넉하게 그려 여유 면적을 확보하는 편이 안전하다.

### 그림 조각과 변형 구조는 다른 층이다

리거와 원화 담당자가 대화할 때 자주 어긋나는 지점이 있다. 네 가지 용어가 서로 다른 층에 있다는 점이다.

| 용어 | 무엇인가 | 누가 만드는가 |
|---|---|---|
| PSD 레이어 | 그림 소재 그 자체 | 원화 담당자 |
| ArtMesh | 레이어 하나에 자동으로 붙는 삼각형 메시. 정점을 움직여 그림을 변형한다 | 리거 (Editor가 자동 생성, 이후 편집) |
| Deformer | ArtMesh나 다른 Deformer를 묶어 한 번에 변형하는 조작 구조 | 리거 |
| Parameter | 움직임의 값. 고개 각도, 눈 개폐 정도 같은 축 | 리거 (표준 목록이 있다) |

공식 매뉴얼은 ArtMesh를 "PSD의 각 레이어에 자동으로 할당되어 캔버스에 배치되는 메시"라고 설명하고, 가져오기 직후에는 데이터 용량을 고려해 <strong>최소한의 정점으로 생성</strong>되며 이후 자동 또는 수동 메시 편집으로 다듬는다고 했다. 여기서 알 수 있는 것은, 머리카락 한 가닥을 뿌리, 중간, 끝에서 다르게 휘게 하려고 그림을 세 조각으로 자를 필요는 없다는 점이다. 한 조각의 메시 위에 정점이 충분하면 변형은 리거가 만든다. 그림을 나눌지 말지는 위의 네 기준으로 정하고, 휘어지는 정도는 메시와 Deformer의 몫으로 넘긴다.

## 3. 얼굴과 목

얼굴은 눈, 코, 입 같은 이목구비와 피부 바탕을 분리하고, 바탕에는 이목구비 자리와 앞머리 뒤 이마까지 피부색으로 채워 둔다. 공식 튜토리얼은 윤곽선을 "머리카락에 가려지는 부분까지 피부색으로 채워 그리고", 머리를 둥글게 그리면 입체감과 움직임을 붙이기 쉽다고 안내한다. 귀는 윤곽과 한 부품으로 취급해도 되지만, 분리하면 더 정밀한 제어가 가능해 별도 분리를 권장한다고 적었다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/02-face-parts-panel.png" alt="공식 튜토리얼 영상 캡처. 왼쪽에 완성된 소녀 얼굴, 오른쪽에 눈(目), 눈썹(眉), 코(鼻), 입(口)으로 나뉜 부품이 청록색 패널 안에 따로 놓여 있다." loading="lazy">
  <figcaption>얼굴 이목구비를 눈, 눈썹, 코, 입으로 나눈 예시. 눈은 속눈썹, 눈알, 흰자로 다시 나뉜다. 출처: Live2D 공식 튜토리얼 「Illustration Processing」, © Live2D Inc. <a href="https://docs.live2d.com/en/cubism-editor-tutorials/psd/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

여기서 더 나아가 큰 고개 회전을 노리는 모델은 윤곽 자체를 한 장으로 두지 않는다. 乾物ひもの는 윤곽을 <strong>선화와 바탕 두 부품</strong>으로 나눈다고 밝혔다. "이렇게 하면 상하좌우를 향했을 때 선화만 마스크로 지워 입체적인 표현이 가능해진다"는 것이 이유다. 옆을 보았을 때 뒤쪽 볼의 윤곽선은 곡선을 그리고, 앞쪽 턱선은 부드러운 둥근 선으로 바뀌며, 폭은 원근 때문에 좁아진다. 이 변화는 바탕 색면을 변형하는 것으로 처리하고, 선은 필요한 자리에서만 보이게 마스크로 다스린다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/05-outline-line-and-base.png" alt="Cubism Editor 화면. 얼굴 윤곽이 선화 레이어와 살색 바탕 레이어로 나뉘어 있고, 바탕 레이어를 선택한 상태라 얼굴 안쪽이 살색 면으로만 보인다. 아래에 '선화와 바탕을 별개의 파츠로 만든다'는 일본어 자막이 있다." loading="lazy">
  <figcaption>윤곽을 선화와 바탕으로 나눈 예시. 출처: 乾物ひもの, 「高可動域モデルの顔の角度XYのすすめ ①」(note, Live2D社 기획 「みんなの Live2D LAB」 기고문). 설명을 위한 인용. <a href="https://note.com/himono_vtuber/n/na1eb00fbc3b4" target="_blank" rel="noopener noreferrer">note.com/himono_vtuber</a></figcaption>
</figure>

Live2D JUKU가 강좌 소개에서 정의한 <strong>背面法</strong>도 같은 갈래의 기법이다. JUKU 페이지의 원문은 이렇다. "Live2D JUKU가 가리키는 「背面法」은 선과 채색 소재를 나누어, 형태의 실루엣과 내부 음영, 선 폭 등을 변화시키기 쉽게 하는 기법을 말한다(線と塗りの素材を分け、形状のシルエットや内部の陰影、線幅などを変化させやすくする手法)." 이름이 낯설지만 내용은 선과 면을 별도 소재로 두어 각각 다르게 다룬다는 뜻이며, JUKU가 "JUKU가 가리키는"이라는 한정을 붙인 데서 알 수 있듯 공식 매뉴얼의 표준 용어라기보다 모델러 사이에서 통용되는 실무 용어를 강좌가 정의해 쓴 것이다. 강좌 본편은 멤버십 한정이어서 여기서는 정의만 옮긴다.

얼굴과 목에서 검토할 부품은 다음과 같다. 전부 의무는 아니고, 목표 움직임에 따라 고른다.

- 얼굴 피부 바탕(이목구비 자리와 이마까지 채운 것), 필요하면 윤곽 선화를 별도로
- 얼굴과 볼의 음영, 홍조 (따로 켜고 끄거나 각도에 따라 옮기려면 분리)
- 코의 기본 선과 색, 코 그림자, 코 하이라이트. 큰 측면 회전을 노리면 옆에서 보이는 코 형태의 보충 소재
- 좌우 귀, 귀 안쪽, 귀걸이의 연결부
- 목, 턱 아래 그림자, 목 음영
- 좌우 눈썹, 눈물이나 창백함 같은 표정 효과

乾物ひもの는 각도 작업을 <strong>코부터</strong> 시작한다고 적었다. 코가 얼굴의 중심선을 정하는 기준점이 되어 다른 부품의 이동량을 재는 잣대가 되기 때문이다. 턱 아래 그림자는 별도 부품으로 만들어 바탕에 클리핑하고, 독립 Deformer로 미끄러지게 한다. 귀는 고개를 돌리면 윤곽 앞으로 나와야 하는데 그림 순서를 바꾸면 깜빡임이 생기므로, 턱선을 지울 때 쓴 것과 같은 마스크 반전 기법으로 해결한다고 했다.

## 4. 눈: 좌우 각각 구성한다

눈은 좌우 각각 만든다. 기본 구성은 흰자, 홍채, 동공, 위 속눈썹, 아래 속눈썹 또는 아래 눈선이다. 공식 튜토리얼은 속눈썹에서 눈꼬리의 튀어나온 부분을 분리해 두면 변형이 쉬워진다고 했다. 고급 제어를 노릴 때 추가로 검토하는 것은 눈꼬리의 긴 속눈썹, 위아래 눈꺼풀 피부, 쌍꺼풀선, 눈 주변 음영, 큰 하이라이트와 작은 반사광, 홍채 위에 드리운 그림자, 흰자 그림자, 그리고 하트나 별 모양 눈 같은 특수 소재다. 이 항목이 모두 모든 모델에 필요한 것은 아니다. 실제로 따로 움직이거나 따로 변할 필요가 있는지를 리거와 함께 정한다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/03-clipping-mask-before-after.png" alt="두 장의 비교 화면. 왼쪽은 흰자 ArtMesh(ID ArtMesh36)를 마스크로 선택한 상태로 홍채가 흰자 밖까지 그려져 있고, 오른쪽은 클리핑을 적용해 홍채가 흰자 범위 안에서만 보인다." loading="lazy">
  <figcaption>클리핑 마스크 전후. 흰자를 마스크로 지정하면 홍채와 하이라이트가 눈 밖으로 나가지 않는다. 출처: Live2D 공식 매뉴얼 「Clipping Mask」, © Live2D Inc. 두 이미지를 나란히 붙였다. <a href="https://docs.live2d.com/en/cubism-editor-manual/clipping-mask/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

홍채와 하이라이트가 눈 밖으로 나가지 않게 하려면 흰자 형태를 <strong>클리핑 마스크</strong>로 쓴다. 공식 매뉴얼은 마스크로 쓸 ArtMesh(흰자)의 ID를 복사해 클리핑될 ArtMesh(홍채)의 Inspector [Clipping ID]에 붙여 넣는 방식을 설명하고, 여러 마스크를 쉼표로 이어 지정할 수 있다고 했다. 여기서 한 가지 제약을 알아 두어야 한다. 마스크 수에는 상한이 있다. 매뉴얼의 표에 따르면 Cubism SDK for Native와 Web은 <strong>모델당 36장</strong>, Unity는 <strong>씬당 64장</strong>이다. 마스크가 필요한 자리마다 아낌없이 쓰면 이 상한에 부딪히므로, 눈처럼 꼭 필요한 곳에 우선 배정한다.

눈 리깅에서 어려운 부분은 눈 주변 원근과 안구 안쪽 변형을 분리하는 일이다. 乾物ひもの는 눈이 "윤곽이나 코보다 난이도가 높다"고 했다. 움직일 것이 둘이고, 좌우 대칭 복사 기능을 쓸 수 없기 때문이라는 설명이다. 그가 소개한 방법은 눈매의 오목함을 의식해 Deformer 형태를 잡고, 안구에는 별도의 부모 Deformer를 두어 "눈동자 부분은 오목하게, 하이라이트는 볼록하게" 처리하는 것이다. 홍채, 동공, 반사광의 상대 위치가 고개 각도에 따라 조금씩 어긋나면서 깊이감이 생긴다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/07-eye-socket-deformer.png" alt="살색 바탕만 보이는 얼굴 위에 붉은 눈 두 개가 놓여 있고, 그 주위로 초록색 격자의 워프 디포머가 걸려 있다. 좌우의 붉은 화살표가 얼굴이 옆으로 돌아갈 때 눈매가 안쪽으로 굽는 방향을 가리킨다." loading="lazy">
  <figcaption>눈매의 오목함을 의식해 잡은 눈 Deformer. 출처: 乾物ひもの, 「高可動域モデルの顔の角度XYのすすめ ②」(note). 설명을 위한 인용. <a href="https://note.com/himono_vtuber/n/n19828b07b8a3" target="_blank" rel="noopener noreferrer">note.com/himono_vtuber</a></figcaption>
</figure>

검수는 뜬 눈만 보고 끝내지 않는다. 반쯤 감김, 완전히 감김, 웃으며 감김을 각각 보고, 여러 고개 각도에서 깜박임을 확인한다. 표준 파라미터 목록은 눈 개폐(ParamEyeLOpen, ParamEyeROpen)를 감긴 상태 0, 뜬 상태 1로 두고, 웃는 눈(ParamEyeLSmile, ParamEyeRSmile)과 시선(ParamEyeBallX, ParamEyeBallY)을 별개의 축으로 둔다. 눈꺼풀 개폐와 시선 이동은 다른 파라미터이고, 다른 검수 항목이다.

## 5. 입

입의 기본 구성은 윗입술선, 아랫입술선, 입 안쪽을 덮는 위아래 입술 주변 피부, 구강 내부 바탕, 윗니, 아랫니, 혀다. 그림체와 목적에 따라 입술색이나 광택, 송곳니를 더 분리한다. 공식 튜토리얼은 입 안쪽을 "원본보다 한 사이즈 크게" 그리라고 했다. 입이 벌어지면 원래 윤곽선 밖으로 나가기 때문이다. 입술 쪽에는 피부색 영역을 덧붙여 벌어진 자리를 덮는다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/04-mouth-clipping-overflow.png" alt="왼쪽에 소녀 얼굴의 입 부분에 붉은 원이 그려져 있고, 붉은 화살표가 오른쪽의 확대 컷을 가리킨다. 확대 컷에서는 입 선화 바깥으로 입 안쪽 색이 살짝 튀어나와 있다." loading="lazy">
  <figcaption>입에 클리핑을 쓰면 입 안쪽이 선화 밖으로 튀어나올 수 있다는 공식 튜토리얼의 예시. 출처: Live2D 공식 튜토리얼 「Illustration Processing」, © Live2D Inc. <a href="https://docs.live2d.com/en/cubism-editor-tutorials/psd/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

입 안쪽을 가리는 방법은 두 가지다. 클리핑 마스크를 쓰는 방법과 입술 주변 피부색으로 덮는 방법이다. 공식 튜토리얼은 <strong>피부색으로 덮는 방식을 권장</strong>한다. 클리핑은 마스크 부하가 늘고, 선화 밖으로 부품이 튀어나올 수 있으며, 변형이 클수록 작업 시간이 늘어난다는 세 단점을 들었다. 반대로 클리핑이 유리한 경우도 적어 두었다. 모델 용량이 문제되지 않는 영상용, 입술 주변이 두껍거나 불균일하게 칠해진 화풍, 입 변형이 적은 단순한 그림이다.

아, 이, 우, 에, 오의 완성 입 그림을 매번 별도 소재로 그릴 필요는 없다. 기본 소재를 변형해 만드는 것이 리깅의 기본이고, 원화 담당자는 그 변형이 도달해야 할 <strong>형태 가이드</strong>를 따로 주면 된다. 双葉うず의 발주 안내는 이 가이드를 선화만으로 요청한다. 눈 가이드로 감은 눈과 웃으며 감은 눈, 입 가이드로 아, 이, 오와 웃으며 닫은 입, 보통 닫은 입, 뿌루퉁하게 닫은 입을 든다. 구강 부품은 "아" 입 모양을 기준으로 만들어 달라고 했다.

파라미터 구성은 기본과 고급으로 나뉜다. 기본은 개폐(ParamMouthOpenY, 0에서 1)와 형태(ParamMouthForm, -1 화난 입에서 +1 웃는 입)의 조합이다. 고급은 턱의 움직임, 입술 오므림, 좌우 폭, 입꼬리, 치아 노출, 혀를 실제 추적 입력에 맞추어 설계한다. 여기서 반드시 먼저 결정할 것이 있다. <strong>카메라 얼굴 추적을 따라가는 입인가, 음성으로 말하는 입인가, 둘을 함께 쓰는가.</strong> 이 결정에 따라 필요한 파라미터와 검수 방법이 달라진다. 실행 프로그램 쪽 이야기는 11장에서 다시 다룬다.

乾物ひもの는 입에서 한 가지 현실적인 제약도 알려 준다. 그림체에 따라 입 모양마다 각도 XY용 Deformer 형태를 다르게 잡아야 자연스럽게 보이는 경우가 있고, 각도 X 3단계, 각도 Y 3단계, 개폐 3단계, 변형 3단계를 모두 조합하면 81개의 형태가 필요해진다는 것이다. 그는 공식이 3개 이상 파라미터를 한 객체에 동시에 붙이는 것을 권장하지 않으며 4개 이상을 붙이려 하면 경고문이 뜬다고 덧붙였다. 입을 얼마나 정교하게 만들 것인지는 이 비용을 알고 정해야 한다.

## 6. 머리카락

큰 구조는 앞머리, 옆머리, 뒷머리다. 그 안에서 독립적으로 흔들릴 다발을 나누고, 좌우와 묶은 머리는 필요에 따라 분리한다. 추가로 검토할 것은 얼굴 앞과 귀 뒤, 목 뒤를 지나는 옆머리, 가슴 앞과 몸 뒤로 늘어진 긴 머리, 묶인 지점과 늘어진 덩어리, 얼굴과 목과 옷에 떨어지는 그림자, 별도로 흐르는 하이라이트, 잔머리와 바보털이다.

그림자에 대해 双葉うず는 명확한 규칙을 두었다. 떨어지는 그림자(落ち影)는 부품마다 따로 만들어 달라는 것이다. "앞머리1, 앞머리2, 앞머리 그림자"처럼 그림자를 한 장으로 합치면 안 되고, "앞머리1 그림자, 앞머리2 그림자"처럼 움직이는 다발과 짝을 이루어야 한다. 铁锭Ferrum의 머리카락 물리 영상 시리즈에도 「머리카락 그림자의 레이어 분리(头发阴影的分层)」가 별도 회차로 들어 있어, 이 항목이 여러 제작자에게 공통 관심사임을 알 수 있다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/10-bangs-deformer-tree.png" alt="Cubism Editor의 디포머 패널. '앞머리 전체의 곡면' 아래에 '앞머리 전체의 흔들림Y'가 있고, 그 아래에 1번부터 4번 다발까지 각각 '흔들림3', '흔들림1', '메이드 ONOFF' 디포머가 계층으로 이어지며 맨 아래에 ArtMesh가 놓여 있다." loading="lazy" style="max-height:640px; width:auto;">
  <figcaption>앞머리 Deformer 계층의 실제 예. 머리카락 전체를 다루는 큰 Deformer 안에 다발별 흔들림 Deformer가 들어간다. 출처: 乾物ひもの, 「高可動域モデルの顔の角度XYのすすめ ③」(note). 설명을 위한 인용. <a href="https://note.com/himono_vtuber/n/ne6f7c0fdfdaa" target="_blank" rel="noopener noreferrer">note.com/himono_vtuber</a></figcaption>
</figure>

리깅에서는 머리카락 전체의 입체 회전을 다루는 큰 Deformer 안에 개별 다발의 흔들림 Deformer를 넣는 식으로 역할을 나눌 수 있다. 위 그림이 그 구조의 한 예다. 乾物ひもの는 흔들림을 만드는 방법을 워프 Deformer, 회전 Deformer(스키닝), ArtMesh 직접 변형 셋으로 소개하면서 자신은 워프 Deformer를 선호하고, 고가동 모델을 스키닝으로 만들면 설정이 너무 힘들어진다고 밝혔다. 앞머리는 다발마다 여러 부품으로 나뉘어 있어도 큰 Deformer로 묶어 움직이면 무너지기 어렵다는 조언도 있다. 이것은 그의 방법이며, 모든 모델의 유일한 정답으로 제시하지 않는다.

옆머리를 원통처럼 보이게 하는 데는 <strong>같은 부품을 복제해 그림 순서를 다르게 두는</strong> 방법을 쓴다. 하나는 윤곽 앞, 하나는 윤곽 뒤에 두어 얼굴을 사이에 끼우는 셈이다. 서로 다른 깊이의 부품이 만나는 교차점(交点)의 앞뒤 관계를 기준으로 삼아야 회전할 때 부품이 미끄러지지 않는다고 했다. 뒷머리는 원화에 측면 부품이 없거나 폭이 매우 좁은 경우가 많아 새 부품을 추가로 그려야 하는데, 이때는 "문제를 피하기 위해 일러스트레이터에게 확인을 받으라"는 당부를 붙였다.

## 7. 몸, 옷, 팔, 소품

몸에서 검토할 부품은 다음과 같다. 가려진 부분을 보충한 몸통, 필요한 만큼의 가슴과 복부와 골반 변형 단위, 좌우 위팔과 아래팔과 손, 소매 바깥과 안쪽과 소맷부리 앞뒤, 옷깃과 초커의 앞뒤, 재킷이나 망토의 앞뒤와 옷자락, 치마 앞뒤와 큰 주름과 안쪽, 리본의 고정점과 날개와 끝, 귀걸이와 체인과 펜던트 같은 장신구다. 공식 튜토리얼은 목을 "얼굴이 움직여도 잘리지 않도록 입 부분까지 크게" 그리고, 팔은 위팔, 아래팔, 손으로, 다리는 치마, 왼다리, 오른다리로 나누는 예를 든다.

소품은 본체만 준비하면 부족하다. 소품 앞뒤로 지나가는 손과 팔이 함께 있어야 물건을 잡는 장면이 성립한다. 손가락 하나하나를 추적하는 것이 목적이 아니라면, 기본 손, 인사하는 손, 가리키는 손, 물건을 잡는 손처럼 <strong>목적별 포즈</strong>를 먼저 준비하는 방식을 검토할 만하다. 双葉うず는 새 의상을 나중에 붙일 것을 대비해 캔버스 상하좌우에 500px의 여백을 두라고 권한다.

중국 제작자 Jenova工坊의 「超精细立绘拆分教程」 시리즈는 이 부분을 회차별로 나눈 공개 목차를 갖고 있다. 무엇이 분할인가, 그림자 오류 네 종류(위는 나누고 아래는 안 나눈 경우, 치마 그림자를 다리에 그린 경우, 투영을 아래 층에 그린 경우, 그림자를 나눌지 말지), 원화 크기, 전체 레이어 공백 검사, 입, 속눈썹, 안구와 흰자, 얼굴, 가슴 유형별, 앞뒤 조각(前后片), 머리카락까지 열일곱 회차다. 앞뒤 조각 회차가 옷깃과 소맷부리처럼 앞뒤가 겹치는 옷의 분할에 해당하는 것으로 보이지만, 회차 제목만 확인했고 영상 내용은 보지 못했으므로 그렇게 짐작만 한다. 그림자 오류를 네 회차에 걸쳐 다룬 점은 눈여겨볼 만하다. 몸통 위에 떨어지는 그림자를 어느 층에 그리는가가 움직였을 때 가장 자주 틀어지는 지점이라는 뜻이다.

## 8. 부품 외에 준비할 원화 자료

부품을 다 나누어도 리거에게 넘길 자료는 더 있다.

<strong>각도별 작화 가이드.</strong> 정면, 좌우, 상하, 네 대각선의 모습이다. 완성 일러스트 아홉 장을 그리라는 뜻이 아니다. 볼의 부피, 코와 입의 위치, 눈 크기, 턱선이 각도에 따라 어떻게 바뀌어야 하는지를 합의하는 자료다. 선화만으로도 충분하다. 이 가이드가 없으면 리거는 원화의 얼굴을 자기 해석으로 돌리게 되고, 원화 담당자가 나중에 "내 캐릭터 같지 않다"고 느끼는 지점이 여기서 생긴다.

<strong>표정 가이드.</strong> 감은 눈, 웃음, 슬픔처럼 눈썹, 눈, 입이 함께 보이는 표정이다. 4장과 5장에서 든 双葉うず의 눈과 입 가이드 목록이 실무적인 예다.

<strong>PSD 두 종류.</strong> 공식 매뉴얼은 부품을 다듬고 관리하는 <strong>편집용 PSD</strong>(폴더와 레이어 마스크가 남아 있는 상태)와 Cubism Editor에 가져오기 위해 부품을 단일 레이어로 병합한 <strong>가져오기용 PSD</strong>를 구분해 관리하라고 안내한다. 가져오기용 PSD의 규칙은 공식 「PSD 데이터 주의사항」 페이지에 정리되어 있다. 형식은 PSD만 가능하고, 색 모드는 RGB, 채널은 8bit, 색 프로필은 sRGB다. 레이어 마스크는 쓰지 말고 "레이어 마스크 적용"으로 한 레이어에 합치며, 부품별로 선화, 채색, 필터 효과, 클리핑 마스크를 하나의 레이어로 병합한다. 같은 이름의 레이어가 없는지 확인하고, 불투명도는 반영되지만 칠(Fill)은 100%로 출력된다. PSD의 블렌드 모드는 Editor의 [Color blend]에 대응 항목이 있으면 자동으로 설정된다. 이 규칙은 매뉴얼이 갱신되므로 작업 시점에 최신 문서를 다시 확인하는 것이 좋다. 双葉うず는 2025년 10월 기준으로 자신이 받는 레이어 모드를 통상, 가산(발광), 승산 세 종류로 제한한다고 밝혔는데, 이는 그의 작업 규약이다.

<strong>레이어명과 좌우 기준의 통일.</strong> 표기법은 팀마다 다르지만 규칙은 하나여야 한다. 예를 들면 `Eye_L_Iris`, `Hair_Front_03_Shadow`처럼 부위, 좌우, 순번, 역할을 순서대로 적는 식이다. 双葉うず는 좌우를 "오른눈, 왼눈"이나 화살표로 적지 말고 "＜눈, ＞눈"처럼 기호로 표기해 달라고 요청한다. 화면 기준인지 캐릭터 기준인지가 헷갈리는 문제를 피하는 방법이다.

<strong>해상도.</strong> 双葉うず는 3000×6000px, 350dpi를 권장한다. 전신 픽셀 수만 고집하는 것보다, 실제로 방송 화면에서 얼굴이 어느 크기로 확대되는지를 역산해 얼굴 부위의 해상도를 정하라고 제안한다. 방송에서는 얼굴만 크게 잡히는 경우가 많고, 그때 선의 뭉개짐이 가장 먼저 보이기 때문이다.

## 9. 리깅 구조와 얼굴 회전

리깅은 메시를 다듬는 데서 시작한다. 공식 매뉴얼의 자동 메시 생성은 점 밀도 값만 정하면 메시를 만들어 주고, 표준, 변형(소), 변형(대) 프리셋을 제공한다. 자동 생성 뒤에는 눈꺼풀, 입술, 윤곽처럼 중요한 부위의 정점을 확인하고 필요하면 수동으로 고친다. 매뉴얼은 파라미터를 설정한 뒤 자동 생성을 다시 적용하면 모양이 바뀌므로 권장하지 않는다고 적었다. 메시는 먼저 확정하고 움직임은 그 다음이다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/09-why-deformer-xy.png" alt="공식 튜토리얼 영상 캡처. 왼쪽에 소녀 얼굴, 오른쪽 주황색 패널에 '왜 XY 움직임을 디포머로 붙이는가'라는 제목과, 디포머 없이 변형하면 각 부품마다 각도 X와 Y의 조합 형태를 일일이 만들어야 해 패턴이 늘고 관리가 힘들다는 설명이 일본어로 적혀 있다." loading="lazy">
  <figcaption>왜 XY 움직임을 Deformer로 붙이는가. 부품마다 직접 변형하면 각도 조합만큼 형태가 늘어난다. 출처: Live2D 공식 튜토리얼 「Adding XY Facial Movement」, © Live2D Inc. <a href="https://docs.live2d.com/en/cubism-editor-tutorials/xy/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

Deformer를 쓰는 이유는 공식 XY 튜토리얼이 숫자로 설명한다. Deformer 없이 ArtMesh에 직접 각도를 붙이면 부품마다 X 세 단계와 Y 세 단계로 아홉 가지, 대각선까지 넣으면 스물일곱 가지 형태를 손으로 만들어야 한다. Deformer로 묶으면 눈 하나에 속한 여러 객체를 한 번에 변형할 수 있고, 원근을 고려한 변형도 가능해진다. 그래서 Deformer 계층은 역할별로 나눈다. 다음은 정답이 아닌 개념 예시다.

```
몸 전체
 ├ 몸통, 팔, 의상
 └ 머리 기울기
    └ 얼굴 XY (고개 회전)
       ├ 좌우 눈 주변 원근 → 눈 개폐, 안구와 시선
       ├ 입 위치와 원근 → 개폐, 형태, 표정
       └ 머리카락 XY (입체 회전) → 다발별 흔들림
```

이렇게 나누는 목적은 고개, 눈, 입의 파라미터 조합마다 모든 메시 형태를 직접 만드는 일의 폭증을 막는 데 있다. 공식 나토리 메이킹 영상의 작업 순서도 Deformer 생성으로 시작해 메시 매핑, 표정, 얼굴 움직임, 몸 움직임, 흔들리는 물체, 팔 움직임, 데이터 내보내기, 표정 데이터, 모션 추가로 이어진다. 구조를 먼저 잡고 그 안에 움직임을 채운다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/08-mouth-nine-angles.jpg" alt="같은 캐릭터의 얼굴이 3열 3행으로 아홉 개 놓여 있다. 위 행은 위를 본 얼굴, 가운데 행은 정면 높이, 아래 행은 아래를 본 얼굴이고, 열은 왼쪽, 정면, 오른쪽을 향한다. 각 얼굴의 입에 초록색 격자의 디포머가 표시되어 있다." loading="lazy">
  <figcaption>아홉 방향에서 본 입 Deformer의 형태. 각도별로 입의 위치와 원근이 달라진다. 출처: 乾物ひもの, 「高可動域モデルの顔の角度XYのすすめ ②」(note). 설명을 위한 인용. <a href="https://note.com/himono_vtuber/n/n19828b07b8a3" target="_blank" rel="noopener noreferrer">note.com/himono_vtuber</a></figcaption>
</figure>

얼굴 XY는 이목구비를 같은 거리만큼 옆으로 미는 작업이라기보다, 부위마다 다른 깊이를 따라 움직이는 작업이다. 코는 가장 앞에 있어 가장 많이 움직이고, 눈은 안구의 오목함을 따라 굽으며, 뒤로 돌아가는 쪽 볼은 폭이 줄어든다. 공식 XY 튜토리얼이 제시한 작업 순서는 부품별 Deformer 생성, Angle X 움직임 추가(다른 부품을 숨기고 윤곽만으로 좌우 형태를 잡되 뒤는 좁게 앞은 넓게), Angle Y 움직임 추가, 그리고 대각선 형태의 자동 생성이다. 이를 바탕으로 이렇게 제안한다. 정면 표정을 먼저 완성하고, 좌우, 상하, 대각선을 만든 뒤, 중간 각도를 보정하고, 마지막에 각도와 표정을 동시에 검수한다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/12-face-auto-motion.gif" alt="Cubism Editor의 파라미터 패널에서 Angle X와 Angle Y 값을 바꾸는 동안 오른쪽의 은발 캐릭터 얼굴이 좌우 상하로 돌아가는 애니메이션." loading="lazy">
  <figcaption>얼굴 모션 자동 생성 기능으로 만든 초기 각도 움직임. 자동 결과는 시작점이며 작화 검수를 대신하지 않는다. 출처: Live2D 공식 매뉴얼 「Auto Generation of Facial Motion」, © Live2D Inc. <a href="https://docs.live2d.com/en/cubism-editor-manual/face-auto-edit/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

Cubism에는 이 과정을 돕는 자동 기능이 있다. XY 튜토리얼의 [네 구석 자동 생성(Auto Generate 4 Corners)]은 Angle X와 Angle Y를 각각 만든 뒤 대각선 형태를 자동으로 채운다. 매뉴얼의 「얼굴 모션 자동 생성」은 얼굴, 좌우 눈, 눈알, 눈썹, 귀, 입, 코의 ArtMesh를 각각 별도 파츠로 준비해 두면 얼굴 Deformer 생성과 각도 XY 모션 생성을 반자동으로 해 준다. 매뉴얼은 두 가지 제약을 명시했다. 이 기능은 <strong>정면을 향한 얼굴에서만</strong> 쓸 수 있고, [Four Corners]는 얼굴에만 적용되며 다른 부위의 네 구석 생성은 별도 기능을 써야 한다. 매뉴얼 페이지에 "몇 버전부터"라는 표기는 없어 여기서는 현재 매뉴얼 기준으로만 적는다. 乾物ひもの는 네 구석 자동 생성 결과가 원근을 고려하지 않아 왜곡되어 보이므로, 원근이 걸리지 않은 부분을 대각선으로 옮겨 손으로 보정한다고 했다. 자동 결과는 출발점이고, 원화의 얼굴로 맞추는 작업은 사람이 한다.

## 10. 표정, 물리, 실제 애니메이션

### 기본 소재의 변형인가, 별도 소재인가

표정은 두 갈래로 나뉜다. 웃음이나 찡그림처럼 기존 소재를 변형해 만들 수 있는 표현과, 하트 눈, 소용돌이 눈, 눈물처럼 별도 소재가 있어야 하는 표현이다. 후자는 2장의 네 번째 분할 기준에 해당하고, 원화 단계에서 그려 두어야 한다. 双葉うず는 하트 눈과 반짝이는 눈 같은 표정 차분 네 종류를 기본 요금에 포함한다고 밝혀, 이런 소재가 발주 항목으로 자리 잡았음을 보여 준다.

### Blend Shape와 가중치 제한

<strong>Blend Shape</strong>는 공식 매뉴얼의 정의로 "모델의 지오메트리에 차이(difference)를 추가하는 기능"이며, 파라미터 조합 수를 신경 쓰지 않고 모델링할 수 있게 해 준다. 기본 형태에 변형의 차이를 더하는 방식이라, 각도 XY의 모든 키에 팔각형 차이를 한 번에 얹는 식으로 쓸 수 있다. 적용 대상은 ArtMesh, 워프 Deformer, 회전 Deformer, 파츠, ArtPath, 글루 여섯 종이다. 변형량은 <strong>가중치(Weight) × 형태 차이(Form Difference)</strong>로 계산된다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/13-blendshape-collapse.gif" alt="Cubism Editor 화면. 주황색 정사각형에 팔각형 블렌드 셰이프와 삼각형 블렌드 셰이프를 함께 적용하자 어느 쪽도 아닌 찌그러진 형태가 되는 애니메이션." loading="lazy">
  <figcaption>두 Blend Shape를 동시에 켰을 때 형태가 깨지는 공식 예시. 출처: Live2D 공식 매뉴얼 「Blend Shape」, © Live2D Inc. <a href="https://docs.live2d.com/en/cubism-editor-manual/blend-shape/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

문제는 여러 Blend Shape를 겹칠 때 생긴다. 매뉴얼은 정사각형에 팔각형 Blend Shape와 삼각형 Blend Shape를 각각 만들고 둘을 모두 1.0으로 두면 "팔각형도 삼각형도 아닌 의도치 않은 붕괴된 모양"이 나온다는 예를 든다. 이를 억제하는 기능이 <strong>Blend Shape 가중치 제한 설정</strong>이다. 제한을 건 파라미터의 값에 따라 가중치에 0에서 100% 사이의 계수를 곱하고, 여러 제한이 걸려 있으면 가장 작은 값을 곱한다. 프리셋 그래프는 직선 셋, 꺾은선 다섯, 계단 둘의 열 종류가 있고, 직접 편집도 가능하다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/14-weight-limit-dialog.png" alt="Limit Settings for Blend Shape Weights 대화상자. Blend Shape 'A'에 대해 I, U, E, O 파라미터가 제한 목록에 들어 있고, 오른쪽 그래프에는 파라미터 값 0에서 가중치 100%, 1에서 0%로 내려가는 초록색 직선(Line3 프리셋)이 그려져 있다." loading="lazy">
  <figcaption>Niziiro Mao 샘플의 입 Blend Shape "A"에 다른 모음 파라미터를 제한 대상으로 넣은 화면. 출처: Live2D 공식 매뉴얼 「Limit Settings for Blend Shape Weights」, © Live2D Inc. <a href="https://docs.live2d.com/en/cubism-editor-manual/limit-settings-for-blend-shape-weights/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

공식 샘플 <strong>Niziiro Mao</strong>가 실제 사례다. 매뉴얼은 이 모델의 입 모양 a, e, i, o, u를 Blend Shape 키로 만든 뒤, 다른 모음이 동시에 켜지면 모양이 깨지므로 각 Blend Shape에 나머지 모음을 제한 대상으로 추가하고 [꺾은선3] 프리셋을 적용해 붕괴를 억제하는 과정을 보여 준다. Niziiro Mao 페이지는 이 모델이 Blend Shape, 승산색, 스크린색의 사용 예를 보여 주기 위한 샘플이며 SDK 5.0과 Cubism 5.0을 지원하는 정면 지향 모델이라고 소개한다. 편집 원본(.cmo3)을 내려받아 구조를 살펴볼 수 있다는 점은 학습에 큰 도움이 되지만, 페이지의 주의 사항은 PRO용 파일을 FREE 에디터로 열면 저장과 내보내기가 되지 않는다는 점, 그리고 샘플 데이터 사용에는 무료 소재 라이선스 동의가 필요하다는 점을 함께 적어 두었다. 편집 파일을 열어 볼 수 있다는 것과 그 소재를 재배포할 수 있다는 것은 다른 이야기다.

### 물리는 형태를 만들지 않는다

가장 자주 생기는 오해가 여기 있다. 물리 계산이 머리카락이 휘는 <strong>형태</strong>를 자동으로 만들어 주지는 않는다. 형태는 리거가 먼저 만든다. 흔들림 파라미터(예를 들어 ParamHairFront)의 양 끝에 왼쪽으로 휜 형태와 오른쪽으로 휜 형태를 만들어 두면, 물리 계산은 그 <strong>파라미터의 값</strong>을 시간에 따라 움직인다. 흐름은 이렇다.

> 고개나 몸의 입력 → 물리 계산 → 흔들림 파라미터 값 → 미리 만든 두 형태 사이의 보간

공식 매뉴얼의 물리 설정은 이 구조를 그대로 따른다. <strong>입력</strong>은 어떤 파라미터의 변화가 흔들림을 일으키는가(기본 프리셋은 Angle X, Angle Z, 몸 회전 X, 몸 회전 Z이며 임의로 바꿀 수 있다), <strong>물리 모델</strong>은 진자의 성질(지속 시간, 흔들리기 쉬운 정도, 반응 시간, 수렴 속도), <strong>출력</strong>은 계산된 흔들림을 어느 파라미터에 얼마나 반영하는가다. 매뉴얼은 흔들리기 쉬운 정도(Ease of swinging)를 경험적으로 0.7에서 0.99 사이에서 쓰라고 권하고, 출력 최대치가 100%를 넘으면 진자가 파라미터 범위 밖으로 나가려 해 움직임이 뚝뚝 끊기므로 출력을 낮추라고 안내한다. 설정은 모델 파일(.cmo3)에 저장된다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/15-physics-settings-dialog.png" alt="Cubism Editor의 Physics Settings 대화상자 전체 화면. 왼쪽에 입력과 출력 설정 패널, 가운데 아래에 물리 모델 설정, 오른쪽에 파라미터 목록과 마법사 소녀 캐릭터의 미리보기가 있다." loading="lazy">
  <figcaption>물리 설정 대화상자. 입력, 물리 모델, 출력의 세 구획으로 나뉜다. 출처: Live2D 공식 매뉴얼 「How to Set Up Physics」, © Live2D Inc. <a href="https://docs.live2d.com/en/cubism-editor-manual/physical-operation-setting/" target="_blank" rel="noopener noreferrer">docs.live2d.com</a></figcaption>
</figure>

권장 방향은 이렇다. 뿌리는 안정적으로 두고 끝은 늦게 따라오게 한다. 매뉴얼의 다단 진자(multi-stage pendulum) 설정이 이를 위한 도구이며, 반응 시간(Reaction time)은 다단 진자에서 자식 진자가 부모의 움직임에 얼마나 민첩하게 반응하는가의 기준이 된다. 큰 머리 덩어리와 작은 장식은 반응을 달리 조율하고, 좌우로 나뉜 부품은 출력 반전(Reflect)으로 퍼지는 움직임을 만든다. 모든 부위가 같은 위상과 진폭으로 흔들리는 것을 피하는 것이 핵심이다. 같은 파라미터를 여러 그룹에서 출력으로 쓸 때는 영향(Influence)의 합이 100%를 넘지 않게 해야 한다는 주의도 있다.

<figure>
  <iframe src="https://player.bilibili.com/player.html?bvid=BV1eK4y1U7sb&p=1&autoplay=0&danmaku=0" scrolling="no" frameborder="0" allowfullscreen="true" loading="lazy" style="width:100%; aspect-ratio:16/9; border:0;" title="铁锭Ferrum, Live2D 制作技巧&经验分享 第一集：头发物理制作（一）弯曲变形器"></iframe>
  <figcaption>铁锭Ferrum의 「制作技巧&经验分享 第一集：头发物理制作」 공식 임베드. 세 파트로 굽힘 변형기, 머리카락 그림자의 레이어 분리, 물리 설정과 Y축 물리를 다룬다. 재생되지 않으면 <a href="https://www.bilibili.com/video/BV1eK4y1U7sb/" target="_blank" rel="noopener noreferrer">bilibili 원본</a>에서 볼 수 있다. 영상 내용은 이 글에서 검증하지 않았다.</figcaption>
</figure>

铁锭Ferrum의 시리즈 「Live2D制作经验分享」는 머리카락 물리, 턱선 지우기, 얼굴 그림자 최적화, 9축 흐름(정적 축 편), 새 버전의 턱 처리로 이어지는 여섯 회차의 공개 목차를 갖고 있다. 머리카락 물리 회차가 굽힘 변형기, 그림자 레이어 분리, Y축 물리의 세 파트로 나뉜 것은, 물리 작업이 변형 형태 제작과 그림자 대응과 수직 방향 반응이라는 세 가지 서로 다른 일로 이루어져 있음을 목차 수준에서 보여 준다. 위 임베드는 공식 플레이어이며 이 글은 영상 내용을 직접 확인하지 않았다.

### 추적, 파생, 물리, 연기를 구분한다

쇼케이스 영상에서 전신이 움직인다고 해서 전신 모션 캡처를 썼다는 뜻은 아니다. 乾物ひもの는 Live2D용 추적 프로그램이 몸의 XY 움직임을 감지하지 못하므로, 몸이 얼굴을 따라 움직이게 하는 데 물리 연산을 쓴다고 밝혔다. Live2D 크리에이티브 스튜디오의 2024년 1월 JUKU 강좌 공지도 "얼굴 움직임에 맞춰 허리와 다리 등 몸이 자연스럽게 함께 움직이는 트래킹 표현"을 물리 연산으로 구현하는 방법을 다룬다고 소개했다. 그러니 완성된 모델의 움직임을 볼 때는 네 층을 나누어 읽는다.

1. <strong>실제 추적 동작</strong>: 카메라가 읽은 고개 각도, 눈 개폐, 입 개폐
2. <strong>추적값에서 파생한 동작</strong>: 고개 각도에서 물리로 끌어낸 몸통과 허리의 반응
3. <strong>물리 반응</strong>: 머리카락, 리본, 장신구의 흔들림
4. <strong>미리 만든 연기 애니메이션</strong>: 인사, 손 흔들기 같은 모션 파일

고개 추적에 몸 반응이 붙고 머리카락 물리가 따라오며 단축키로 인사 모션이 재생되는 조합이 전형적인 예다. 표준 파라미터 목록도 머리카락 흔들림(ParamHairFront, Side, Back)에 대해 "보통 물리 연산으로 설정한다"고 적어, 이 축들이 추적이 아닌 물리의 몫임을 밝힌다.

## 11. 실행 프로그램에서의 최종 검수와 납품

모델은 Cubism Editor 안에서 완성되지 않는다. VTube Studio 같은 실행 프로그램에서 실제로 말하고 움직여 보아야 끝난다.

### 입력과 출력의 매핑, 스무딩

VTube Studio 공식 위키는 모델 설정에서 "어떤 입력 파라미터(얼굴 추적, 마우스 등)든 어떤 출력 파라미터(Live2D 파라미터)에든 자유롭게 매핑할 수 있다"고 설명한다. 입력 범위와 출력 범위를 각각 정하고, 범위 제한(Limit Range)을 켜면 값이 범위 밖으로 나가지 않으며 한계 근처에서 부드럽게 멈춘다. 스무딩에 대한 위키의 문장은 이렇다. "스무딩을 늘리면 움직임의 떨림이 줄지만 지연이 생긴다. 파라미터마다 맞는 값을 찾을 때까지 실험하라. iOS에서는 스무딩이 거의 필요 없을 것이다." 떨림 감소와 지연 사이의 절충이며, 눈, 입, 고개를 각각 따로 맞춘다.

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/16-vts-param-mapping.jpg" alt="VTube Studio 모델 설정 화면. 위쪽에 입력 범위 -30에서 30과 출력 범위 -30에서 30을 잇는 매핑 그래프가 있고, 아래 대화상자에는 MouthSmile, MouthOpen, Brows, TongueOut, EyeOpenLeft, EyeOpenRight 같은 입력 얼굴 추적 파라미터 목록이 있다. TongueOut과 EyeOpen 항목에는 'iOS only' 표시가 붙어 있다." loading="lazy">
  <figcaption>VTube Studio의 입력 파라미터 선택 화면. 일부 입력에는 iOS 전용 표시가 있다. 출처: VTube Studio 공식 위키 「VTS Model Settings」(DenchiSoft). 화면 위쪽 부분만 잘랐다. <a href="https://github.com/DenchiSoft/VTubeStudio/wiki/VTS-Model-Settings" target="_blank" rel="noopener noreferrer">github.com/DenchiSoft/VTubeStudio/wiki</a></figcaption>
</figure>

어떤 입력을 쓸 수 있는지는 추적 장치에 따라 다르다. 위키의 지원 표에 따르면 고개 각도, 눈 개폐, 시선, 눈썹, 입 개폐와 웃음은 iOS, Android, 웹캠 모두에서 쓸 수 있다. 볼 부풀리기(CheekPuff)는 iOS에서만, 혀 내밀기(TongueOut)는 iOS와 Android에서만 지원되고 웹캠에서는 지원되지 않는다. 입의 좌우 이동(MouthX)은 일반 웹캠에서는 되지 않고 NVIDIA나 Mediapipe 방식의 웹캠 추적에서는 된다. 위키는 추적 품질을 "iOS > 웹캠 > Android" 순으로 적었다. 이 표가 원화와 리깅 단계에서 중요한 이유는, 혀나 볼 부품을 정교하게 만들어도 사용자의 장치가 그 입력을 내지 못하면 움직이지 않기 때문이다. 어떤 장치로 방송할지를 부품 목록을 정할 때 함께 정한다.

### 얼굴 추적과 음성 립싱크

<figure>
  <img src="https://img.seosoyoung.eiaserinnys.me/images/live2d-high-quality-avatar-guide/17-vts-lipsync-settings.png" alt="VTube Studio의 마이크 설정 패널(볼륨 게인, 볼륨 컷오프, 주파수 게인 슬라이더)과 Advanced Lipsync 패널. 오른쪽 패널에는 A, I, U, E, O 모음별 캘리브레이션 버튼과 색띠 형태의 음성 스펙트럼이 보인다." loading="lazy">
  <figcaption>VTube Studio의 립싱크 설정. Advanced Lipsync는 자기 목소리로 모음을 캘리브레이션한다. 출처: VTube Studio 공식 위키 「Lipsync」(DenchiSoft). <a href="https://github.com/DenchiSoft/VTubeStudio/wiki/Lipsync" target="_blank" rel="noopener noreferrer">github.com/DenchiSoft/VTubeStudio/wiki</a></figcaption>
</figure>

5장에서 미룬 결정이 여기서 실제 설정으로 이어진다. VTube Studio의 립싱크 위키에 따르면 음성 립싱크는 마이크 입력에서 VoiceA, VoiceI, VoiceU, VoiceE, VoiceO(각 0에서 1), VoiceSilence, VoiceVolume, VoiceFrequency 같은 파라미터를 만들어 낸다. 얼굴 추적과의 관계는 위키의 한 문장이 정리한다. "소리가 감지되면 블렌드 셰이프가 넘겨받으며, 웹캠이나 iPhone 기반 추적은 대부분 또는 완전히 무시된다." 무음일 때는 카메라 추적이 입을 맡고, 소리가 나면 모음 형태가 입을 맡는 구조다. 위키는 한계도 밝힌다. 모음 블렌드 셰이프에 "기쁜" 버전과 "슬픈" 버전을 따로 둘 방법은 없고, 콧노래 같은 소음이 A 모음으로 인식될 수 있다. 사람을 따라가는 입인지 음성으로 말하는 입인지에 따라 리깅에서 만들 형태와 검수 방법이 달라지는 이유가 여기 있다.

VBridger는 이 위에 놓이는 별도 플러그인이다. Steam 페이지의 소개는 "VTube Studio와 Live2D를 위해 설계된 얼굴 추적 플러그인으로, 사용자가 iPhone X ARKit 추적을 Live2D 모델에서 더 잘 활용할 수 있게 한다"고 적었다. 입력원으로 iPhone의 ARKit 기반 앱과 Android의 MeowFace, 웹캠의 Mediapipe와 NVIDIA 추적, 마이크를 들고, 출력은 VTube Studio API나 VMC 프로토콜로 낸다. Windows용 소프트웨어이며, 리거가 새 출력과 사용자 제어를 만들 수 있는 Editor DLC가 따로 있다. VTube Studio 위키의 플러그인 목록에도 같은 설명으로 등재되어 있다. 이 글에서 확인한 것은 공개 설명까지이고, 어떤 파라미터를 얼마나 정교하게 쓸 수 있는지는 최신 문서와 실제 장치로 확인해야 한다.

### 같은 파라미터를 누가 덮어쓰는가

표정, 애니메이션, 추적, 물리가 같은 파라미터를 건드릴 때의 우선순위를 알아야 검수에서 혼란이 없다. VTube Studio 위키는 각 Live2D 파라미터가 여섯 종류의 "값 제공자" 중 하나에 의해 제어되며, 우선순위가 낮은 쪽부터 높은 쪽으로 다음 순서라고 정리했다.

| 우선순위 | 값 제공자 |
|---|---|
| P0 | Live2D 파라미터 기본값 |
| P1 | 대기(idle) 애니메이션 |
| P2 | 얼굴 추적 |
| P3 | 일회성 애니메이션 (재생 중인 동안) |
| P4 | Live2D 표정 (활성 상태인 동안) |
| P5 | 물리 시스템 |

최종값은 활성 상태인 가장 높은 우선순위의 제공자가 정하고, 제공자가 바뀔 때는 값이 튀지 않도록 항상 부드럽게 넘어간다. 표정의 더하기와 곱하기는 "다른 모든 것이 적용된 뒤" 곱셈 전부, 그 다음 덧셈 전부 순으로 계산된다. 물리가 최상위라는 점은 흔들림 파라미터를 표정이나 애니메이션이 덮어쓸 수 없다는 뜻이고, 표정이 추적보다 위라는 점은 웃는 표정을 켠 채 말하면 입 개폐가 어떻게 되는지를 반드시 확인해야 한다는 뜻이다.

### 검수 항목과 납품물

검수는 실행 프로그램 안에서 다음 상황을 만들어 보며 한다. 각 항목의 세부는 부록의 검수표에 있다.

- 여러 고개 각도에서 눈을 감고 뜬다: 감긴 눈의 위치, 꺾이는 속눈썹
- 여러 고개 각도에서 말한다: 미끄러지는 입, 튀어나오는 치아
- 가만히 있는다: 불필요한 떨림
- 빠르게 움직이고 멈춘다: 과도한 물리 진동, 앞뒤 관통
- 표정을 켠 채 말한다: 웃거나 슬픈 상태에서도 입이 움직이는가
- 손, 소품, 의상을 전환한다: 구멍, 중복, 앞뒤 오류
- 실제 방송 크기로 얼굴을 확대한다: 선, 텍스처, 마스크 품질

고급 표현에 대해서는 기능의 존재와 실행 환경의 지원을 나누어 확인한다. 공식 ArtMesh 매뉴얼은 블렌드 모드에 대해 컬러 블렌드 [Normal]과 알파 블렌드 [Over] 이외의 모드를 쓰면 "SDK 버전, 플랫폼, 오프스크린, 셰이더 설정에 따라 표현이 달라질 수 있어 실기기 확인이 필요하다"고 적었다. Niziiro Mao 페이지도 블렌드 모드에 "5.2 이하"라는 버전 표기를 붙여 두었다. 에디터에서 보이는 것과 실행 프로그램에서 보이는 것이 다를 수 있으므로, 효과의 수를 품질로 여기지 말고 대상 환경에서 실제로 보이는지를 확인한다. 마스크 상한(36장 또는 64장)도 같은 이유로 세어 둔다.

납품물은 다음 구성을 제안한다. 파일 형식은 공식 「파일 형식과 확장자」 매뉴얼을 따른다.

| 납품물 | 형식 | 비고 |
|---|---|---|
| 수정 가능한 원화 PSD (편집용) | .psd | 폴더와 레이어 마스크가 남은 상태 |
| 가져오기용 PSD | .psd | 부품별 단일 레이어, RGB 8bit sRGB |
| 모델 편집 원본 | .cmo3 | Cubism 3부터 물리 설정을 포함 |
| 애니메이션 편집 원본 | .can3 | 애니메이션 워크스페이스 프로젝트 |
| 실행용 모델 | .moc3, .model3.json, 텍스처 png | .model3.json이 .moc3, 텍스처, 물리 설정, 파라미터 목록을 연결 |
| 모션 | .motion3.json | Cubism 2.1의 .mtn을 대체 |
| 표정 | .exp3.json | |
| 물리 설정 | .physics3.json | |
| 파츠 전환 | .pose3.json | 팔 전환 등 |
| 표시 보조 | .cdi3.json | 파라미터와 파츠의 표시명 |
| 추적 프로그램 설정, 파라미터 설명서 | 텍스트 | 어떤 입력을 어떤 파라미터에 매핑했는지 |

제작 순서로는 이렇게 권장한다. <strong>얼굴만 먼저 시험 제작해 실제로 말하게 한다.</strong> 눈, 입, 작은 고개 움직임이 실행 프로그램에서 만족스럽게 나오면, 그 다음에 전신, 긴 머리, 의상, 소품, 효과로 넓혀 간다. 얼굴에서 발견되는 문제는 대부분 원화 분할과 보충의 문제이고, 전신을 다 만든 뒤에 원화로 돌아가는 비용이 가장 크기 때문이다.

## 부록: 부품 표, 검수표, 표준 파라미터

<details>
<summary>부록 A. 부위별 부품 검토표 펼쳐보기</summary>

모든 항목이 의무는 아니다. "기본"은 대부분의 모델에 있는 것, "검토"는 목표 움직임에 따라 리거와 상의해 정하는 것이다.

| 부위 | 기본 | 검토 (목표에 따라) |
|---|---|---|
| 얼굴 | 피부 바탕(이목구비 자리와 이마까지 채움), 좌우 눈썹 | 윤곽 선화 별도, 얼굴과 볼 음영, 홍조, 눈물과 창백함 효과 |
| 코 | 코 선과 색 | 코 그림자, 코 하이라이트, 측면 회전용 보충 소재 |
| 귀 | 좌우 귀 | 귀 안쪽, 귀걸이 연결부 |
| 목 | 목(입 높이까지 크게) | 턱 아래 그림자, 목 음영 |
| 눈 (좌우 각각) | 흰자, 홍채, 동공, 위 속눈썹, 아래 속눈썹 또는 아래 눈선 | 눈꼬리 긴 속눈썹, 위아래 눈꺼풀 피부, 쌍꺼풀선, 눈 주변 음영, 큰 하이라이트, 작은 반사광, 홍채 위 그림자, 흰자 그림자, 하트와 별 등 특수 소재 |
| 입 | 윗입술선, 아랫입술선, 입 주변 피부(위아래), 구강 바탕, 윗니, 아랫니, 혀 | 입술색과 광택, 송곳니 |
| 머리카락 | 앞머리, 옆머리, 뒷머리, 그 안의 독립 다발 | 얼굴 앞과 귀 뒤와 목 뒤를 지나는 옆머리, 가슴 앞과 몸 뒤의 긴 머리, 묶인 지점과 늘어진 덩어리, 다발별 그림자, 별도 하이라이트, 잔머리와 바보털, 뒷머리 측면 보충 |
| 몸 | 몸통(가려진 부분 보충), 좌우 위팔과 아래팔과 손 | 가슴과 복부와 골반 변형 단위, 목적별 손 포즈 |
| 옷 | 상의, 하의 | 소매 바깥과 안쪽과 소맷부리 앞뒤, 옷깃과 초커 앞뒤, 재킷과 망토의 앞뒤와 옷자락, 치마 앞뒤와 큰 주름과 안쪽, 리본 고정점과 날개와 끝 |
| 장신구와 소품 | 소품 본체 | 소품 앞뒤를 지나는 손과 팔, 귀걸이, 체인, 펜던트 |
| 가이드 (선화만) | 각도별 얼굴(정면, 좌우, 상하, 대각선), 감은 눈, 웃으며 감은 눈, 입 아, 이, 오, 닫은 입 여러 종 | 웃음과 슬픔 등 표정 가이드 |

</details>

<details>
<summary>부록 B. 실행 프로그램 검수표 펼쳐보기</summary>

| 상황 | 무엇을 보는가 | 어긋났을 때 돌아갈 곳 |
|---|---|---|
| 정면에서 눈 개폐 | 감긴 선의 위치, 반쯤 감김의 형태, 속눈썹 꺾임 | 눈 개폐 키폼, 속눈썹 분리 |
| 좌우 30도, 상하 30도, 대각선에서 눈 개폐 | 감긴 눈이 눈매의 원근을 따르는가 | 눈 주변 Deformer, 각도와 개폐 동시 검수 |
| 정면과 여러 각도에서 말하기 | 입 위치 미끄러짐, 치아가 입술 밖으로 튐, 구강 바탕이 비는가 | 입 Deformer, 구강 크기, 입술 주변 피부 |
| 시선만 이동 | 홍채가 흰자 밖으로 나가는가, 하이라이트 위치 | 클리핑 마스크, 안구 Deformer |
| 가만히 있기 | 불필요한 떨림, 물리 잔진동 | 스무딩, 수렴 속도 |
| 빠르게 움직였다 정지 | 과도한 진동, 부품 관통, 출력 범위 초과로 끊김 | 물리 출력 스케일, 다단 진자 반응 시간, 그림 순서 |
| 표정 켠 채 말하기 | 웃는 표정과 입 개폐가 함께 성립하는가 | 우선순위 확인(표정 P4 > 추적 P2), Blend Shape 가중치 제한 |
| 음성 립싱크와 카메라 동시 | 무음에서 카메라로, 발화에서 모음으로 넘어가는 순간의 튐 | 립싱크 임계값, ParamSilence 키폼 |
| 손과 소품과 의상 전환 | 구멍, 중복, 앞뒤 오류 | 파츠 전환 설정, 소품 앞뒤 손 소재 |
| 방송 크기로 얼굴 확대 | 선의 뭉개짐, 텍스처 해상도, 마스크 가장자리 흰 테두리 | 원화 해상도, 마스크 외곽 처리 |
| 대상 장치에서 실행 | 블렌드 모드와 마스크가 에디터와 같게 보이는가, 마스크 수가 상한 안인가 | 블렌드 모드 대체, 마스크 수 정리 |

</details>

<details>
<summary>부록 C. 자주 쓰는 표준 파라미터 펼쳐보기</summary>

공식 「표준 파라미터 목록」에서 이 글에 등장한 축만 골랐다. 원칙은 눈과 입을 감긴 상태 0, 뜬 상태 1로 두는 것이다.

| 이름 | ID | 범위 | 뜻 |
|---|---|---|---|
| 고개 각도 X, Y, Z | ParamAngleX, ParamAngleY, ParamAngleZ | -30 에서 30 | X는 좌우 회전, Y는 상하, Z는 기울기. 좌우는 45까지 확장 가능 |
| 눈 개폐 (좌, 우) | ParamEyeLOpen, ParamEyeROpen | 0 에서 1 | 0 감김, 1 뜸. 꽉 감기와 크게 뜨기는 범위 밖으로 확장 |
| 눈 웃음 (좌, 우) | ParamEyeLSmile, ParamEyeRSmile | 0 에서 1 | 웃는 눈 |
| 시선 X, Y | ParamEyeBallX, ParamEyeBallY | -1 에서 1 | 눈알의 좌우, 상하 |
| 눈썹 상하, 좌우, 각도, 변형 (좌, 우) | ParamBrowLY 등 | -1 에서 1 | 화남 표현은 각도와 변형의 음수 방향 |
| 입 형태 | ParamMouthForm | -1 에서 1 | 음수 화난 입, 양수 웃는 입 |
| 입 개폐 | ParamMouthOpenY | 0 에서 1 | 0 닫힘, 1 벌림 |
| 볼 | ParamCheek | 0 에서 1 | 홍조 |
| 몸 회전 X, Y, Z | ParamBodyAngleX, Y, Z | -10 에서 10 | 몸통의 회전과 상하, 기울기 |
| 호흡 | ParamBreath | 0 에서 1 | 들이쉼 |
| 머리카락 흔들림 (앞, 옆, 뒤) | ParamHairFront, ParamHairSide, ParamHairBack | -1 에서 1 | 보통 물리 연산으로 설정 |

</details>

## 가장 흥미로운 지점

내가 곱씹은 대목은 자료들이 모두 "형태는 사람이 만들고 계산은 값만 움직인다"는 한 문장으로 모인다는 점이었다. 물리는 휘어진 머리카락의 모양을 만들지 않고 파라미터 값을 흔든다. 얼굴 자동 생성은 대각선 형태를 채우지만 원근을 몰라서 사람이 되돌아가 고친다. Blend Shape는 차이를 얹어 조합 수를 줄여 주지만, 둘을 겹치면 깨지므로 가중치 제한을 사람이 건다. 도구가 늘어날수록 리거의 일은 줄어드는 것처럼 보이지만, 실제로는 "어디까지 도구에 맡기고 어디서 손으로 돌아오는가"를 판단하는 일로 바뀐다.

또 하나 의외였던 것은 원화 담당자의 역할이 생각보다 크다는 점이다. 双葉うず의 발주 규약과 Jenova工坊의 열일곱 회차 목차는 대부분 리깅 이야기라기보다 그림을 어떻게 그려 넘길 것인가에 대한 이야기다. 그림자를 어느 층에 그리는가, 가려진 곳을 얼마나 채우는가, 감은 눈의 선을 누가 정하는가. 리거가 고칠 수 없는 것은 그림 자체이고, 초고품질이라는 말의 절반은 원화 단계에서 이미 결정된다.

## 출처

이 글은 아래 자료를 읽고 엮었다. 이미지는 각 캡션에 적은 출처에서 설명을 위해 인용했다. 双葉うず의 사이트는 무단 전재를 금지하고 있어 이미지를 쓰지 않고 본문 인용과 링크만 두었다. Bilibili 영상은 공식 플레이어 임베드만 썼다.

Live2D 공식
- <a href="https://docs.live2d.com/en/cubism-editor-manual/divide-the-material/" target="_blank" rel="noopener noreferrer">Divide the Material</a> (소재 분할)
- <a href="https://docs.live2d.com/en/cubism-editor-tutorials/psd/" target="_blank" rel="noopener noreferrer">Illustration Processing</a> (PSD 튜토리얼)
- <a href="https://docs.live2d.com/en/cubism-editor-manual/precautions-for-psd-data/" target="_blank" rel="noopener noreferrer">Precautions for PSD Data</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/concept-of-artmesh/" target="_blank" rel="noopener noreferrer">Concept of ArtMesh</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/mesh-edit/" target="_blank" rel="noopener noreferrer">Mesh Edit</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/clipping-mask/" target="_blank" rel="noopener noreferrer">Clipping Mask</a>
- <a href="https://docs.live2d.com/en/cubism-editor-tutorials/xy/" target="_blank" rel="noopener noreferrer">Adding XY Facial Movement</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/face-auto-edit/" target="_blank" rel="noopener noreferrer">Auto Generation of Facial Motion</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/standard-parameter-list/" target="_blank" rel="noopener noreferrer">Standard Parameter List</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/blend-shape/" target="_blank" rel="noopener noreferrer">Blend Shape</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/limit-settings-for-blend-shape-weights/" target="_blank" rel="noopener noreferrer">Limit Settings for Blend Shape Weights</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/physical-operation-setting/" target="_blank" rel="noopener noreferrer">How to Set Up Physics</a>
- <a href="https://docs.live2d.com/en/cubism-editor-manual/file-type-and-extension/" target="_blank" rel="noopener noreferrer">File Types and Extensions</a>
- <a href="https://docs.live2d.com/en/cubism-editor-tutorials/natori_making/" target="_blank" rel="noopener noreferrer">Natori Making</a>
- <a href="https://www.live2d.com/en/learn/sample/niziiro-mao/" target="_blank" rel="noopener noreferrer">Niziiro Mao 샘플 모델</a>
- <a href="https://www.live2dcs.jp/news/20240105/" target="_blank" rel="noopener noreferrer">Live2D Creative Studio 뉴스 2024-01-05</a> (JUKU 물리 연산 강좌 공지)
- <a href="https://juku.live2dcs.jp/course/course-26/" target="_blank" rel="noopener noreferrer">Live2D JUKU 「シンプルなパラメータで真横を向けるモデルを作ろう」</a> (소개 페이지, 본편은 멤버십 한정)

일본 제작자
- 双葉うず, <a href="https://forestbathh.wixsite.com/ftbuz/%E3%83%91%E3%83%BC%E3%83%84%E5%88%86%E3%81%91%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6" target="_blank" rel="noopener noreferrer">パーツ分けについて</a>
- 乾物ひもの, 「高可動域モデルの顔の角度XYのすすめ」 <a href="https://note.com/himono_vtuber/n/na1eb00fbc3b4" target="_blank" rel="noopener noreferrer">①</a> <a href="https://note.com/himono_vtuber/n/n19828b07b8a3" target="_blank" rel="noopener noreferrer">②</a> <a href="https://note.com/himono_vtuber/n/ne6f7c0fdfdaa" target="_blank" rel="noopener noreferrer">③</a> (note, 2021년 3월에서 4월)

중국 제작자 (공개 설명과 회차 목차까지 확인)
- Jenova工坊, <a href="https://www.bilibili.com/video/BV1TY4y1a7t7/" target="_blank" rel="noopener noreferrer">超精细立绘拆分教程</a> (2022년 4월)
- 铁锭Ferrum, <a href="https://www.bilibili.com/video/BV1eK4y1U7sb/" target="_blank" rel="noopener noreferrer">制作技巧&经验分享 第一集：头发物理制作</a> (2021년 3월)

VTube Studio와 VBridger
- <a href="https://github.com/DenchiSoft/VTubeStudio/wiki/Plugins" target="_blank" rel="noopener noreferrer">Plugins</a>, <a href="https://github.com/DenchiSoft/VTubeStudio/wiki/Lipsync" target="_blank" rel="noopener noreferrer">Lipsync</a>, <a href="https://github.com/DenchiSoft/VTubeStudio/wiki/VTS-Model-Settings" target="_blank" rel="noopener noreferrer">VTS Model Settings</a>, <a href="https://github.com/DenchiSoft/VTubeStudio/wiki/Interaction-between-Animations%2C-Tracking%2C-Physics%2C-etc." target="_blank" rel="noopener noreferrer">Interaction between Animations, Tracking, Physics, etc.</a>
- <a href="https://store.steampowered.com/app/1898830/VBridger/" target="_blank" rel="noopener noreferrer">VBridger (Steam)</a>
