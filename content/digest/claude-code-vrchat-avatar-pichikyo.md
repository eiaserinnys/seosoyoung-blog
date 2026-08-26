---
title: "Blender初心者が、Claude Code頼みで6個のツールを繋ぎ、一日でVRChatアバターをつくった話"
date: 2026-05-12T09:30:00+09:00
tags: ["AI", "Claude Code", "VRChat", "3D 에셋", "도구 체인"]
categories: ["창작과 문화"]
summary: "Blender 누적 3일 초보가 ChatGPT Image 2부터 VRChat까지 6개 도구를 연쇄로 묶어 하루 만에 자기 사진 기반 오리지널 아바타를 만든 기록. Claude Code는 도구를 직접 조작하지 않고 '다음 단계가 무엇이며 어떻게 해야 하는가'를 안내하는 통역사 역할을 했다."
ShowToc: true
TocOpen: false
sidenotes: true
---

![완성된 VRChat 아바타의 얼굴 클로즈업 — 어느 각도에서 봐도 아름답다는 필자의 최종 결과](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/cover.jpg)

## 3줄 요약

1. Blender 누적 3일 초보 사용자 @pichikyo가 ChatGPT Image 2부터 VRChat까지 6개의 도구를 연쇄로 묶어, 자기 사진 한 장에서 출발해 하루 만에 오리지널 VRChat 아바타를 빌드해냈다.
2. Claude Code는 도구를 직접 조작하지 않고 "지금 어떤 도구로 무엇을 해야 하는지"를 안내하는 통역사·오케스트레이터 역할을 맡았으며, 단계 사이 변환이 마땅치 않으면 즉석 스크립트(자동 마테리얼/셰이더 설정 툴)를 만들어 끼워 넣었다.
3. 필자는 미드저니로 이미지 생성을 시작한 지 3년 만에 여기까지 왔다며, 2년 뒤에는 표정 셰이프키·UV맵·리그 품질까지 갖춘 완성형 아바타가 AI에서 곧장 나올 것으로 내다본다.

## 자료 정보

- 발신자: pichikyo (X / 구 트위터)
- 형식: 단일 트윗에 담긴 장문 회고 (블로그 글에 가까운 분량)
- 게시: 2026년 X 게시물
- 원문: <https://x.com/pichikyo/status/2053499603094585353>

## 발단

ChatGPT Image 2에서 사진 한 장과 프롬프트로 자기 캐릭터를 만드는 X 트렌드가 발단이었다. 필자는 자기 사진을 넣어보고 "꽤 귀여운 캐릭터가 나왔으니, 이걸 VRChat 아바터로 만들 수 있지 않을까"라는 생각을 했다. GPT-image-2가 사면도(정면·좌·우·후면) 생성에도 강하다는 점이 결정타였다.

![ChatGPT Image 2가 사진을 캐릭터화한 결과](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/01.jpg)

## 전체 워크플로우 (6단계)

| 단계 | 도구 | 역할 |
| --- | --- | --- |
| 1. 캐릭터 이미지 | ChatGPT Image 2 | 사진에서 캐릭터화 + 사면도 생성 |
| 2. 3D 모델화 | TRIPO 3D | 사면도 또는 프롬프트 → T-포즈 3D 모델 |
| 3. 임포트·정형 | Blender (+ Tripo DCC Bridge MCP) | 모델 취득, 머리·몸 결합, 메쉬 보정 |
| 4. 자동 리깅 | Adobe Mixamo | 관절 6점 수동 배치 → 자동 본/스킨 바인드 |
| 5. 머터리얼·셋업 | Unity (+ Claude Code 생성 자동 머터리얼 툴) | 셰이더, VRC Avatar Descriptor |
| 6. 빌드 | VRChat | 업로드 및 동작 확인 |

각 단계 사이의 데이터 변환(FBX 입출력, 머터리얼 재바인딩, MCP 연결 등)은 모두 Claude Code에 물어가며 진행했다.

![GPT-image-2가 생성한 사면도 (정면·좌·우·후면) — "GPT-image-2는 정말 유능하다"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/02.jpg)

## 도구별 메모

### TRIPO 3D

미국 발 서비스라서 일본/한국에서 흔한 애니메·모에 풍을 이미지 입력으로 재현하기는 어렵다. 머리만 따로 생성하면 "농후한 버터 풍 리얼 얼굴"이 나왔다. 우회법은 두 가지였다:

- 이미지 입력 대신 ChatGPT로 스타일을 텍스트 프롬프트로 분해한 뒤, 그 프롬프트만으로 직접 생성하기.
- 머리와 몸을 분리 생성해 폴리곤 예산을 부위별로 따로 쓰기 (얼굴 디테일 확보).

![TRIPO 3D가 사면도에서 수 분 만에 만들어낸 T-포즈 3D 모델 — "빠르다. 대단하다"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/03.jpg)

![머리만 따로 생성했을 때 나온 "농후한 버터 풍 리얼 얼굴" — 학습 모집단이 구미권이라는 방증](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/13.jpg)

![ChatGPT로 원본 일러스트의 스타일을 분해해 프롬프트로 재시도하는 "프롬프트 가챠"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/14.jpg)

### Blender + Tripo DCC Bridge MCP

> Claude CodeにBlenderを公式MCPからつないで聞いたら、「Tripo DCC Bridge for Blender」という、直接Blenderにデータを転送する機能があるらしい。 BlenderにブリッジMCPを接続して、ボタン一発で取り込み成功。

별도 익스포트/임포트 옵션을 고민하지 않고도 TRIPO 결과물을 Blender로 직접 전송할 수 있는 MCP 브리지가 있다는 사실 자체를 Claude Code가 알려준 것이 도움이 됐다.

![Tripo DCC Bridge MCP로 버튼 한 번에 Blender에 모델이 들어오는 화면 — "정말 편리하다"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/04.jpg)

![Blender로 가져온 직후의 거친 얼굴 메쉬와 텍스처](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/05.jpg)

### Adobe Mixamo

무료 웹앱이라 설치가 필요 없고, 관절 위치를 가리키는 구체 6개를 수동으로 배치하기만 하면 자동으로 본과 스킨 바인드가 끝난다. "FBX for Unity"로 받으면 곧장 다음 단계로 갈 수 있다. 정밀도는 낮지만 "움직이는 모델"의 첫 베타까지 거의 마찰 없이 도달한다.

![Mixamo에서 관절 구체 6개를 손으로 배치하는 화면 — 무료 웹앱에서 자동 본/스킨 바인드까지 완결된다](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/06.jpg)

### Unity

머터리얼·셰이더 설정과 VRC Avatar Descriptor 초기 셋업이 필요한데, 필자는 셰이더 매핑이 막막해 Claude Code에 상담했다. 그러자 "자동으로 머터리얼과 셰이더를 세팅하는 툴"을 즉석에서 만들어줬고, 그 툴과 모델을 Unity에 넣고 버튼 하나로 마쳤다.

![Blender→Unity 이행 단계 — "복잡한 부분은 Claude Code 맡김"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/07.jpg)

![첫 빌드를 마치고 VRChat에 들어가 풀트래킹으로 찍은 셀피](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/08.jpg)

## 두 번의 좌절 — 그리고 우회

### 1. 얼굴 메쉬가 거칠다

전신을 한 번에 생성하면 한정된 폴리곤 예산을 얼굴·몸이 나눠 써서 얼굴이 거칠게 나온다. 머리만 따로 생성하고 Blender에서 몸과 결합하는 분할 패턴으로 디테일을 확보했다. 단, 머리/몸 경계의 메쉬·머터리얼 정합은 수동 미세 조정이 필요했다.

![첫 빌드에서 거칠게 나온 얼굴 메쉬와 텍스처 — 폴리곤 예산이 얼굴·몸으로 분산된 결과](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/09.jpg)

![머리만 따로 생성하고 Blender에서 몸과 결합 — "정점을 옮겨 메쉬 형태를 다듬는 법을 익혔다"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/10.jpg)

![사면도 기반이라 정면·측면은 자연스럽지만 비스듬한 각도에서 데생이 어긋난다 — "광대가 부족하고 턱이 너무 뾰족하다"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/11.jpg)

![Booth에서 산 머리·메가네 에셋을 얹어 빌드 — 정면에서 보면 충분히 귀엽다](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/12.jpg)

![프롬프트 가챠 끝에 다듬어진 결과 — "전날을 생각하면 꽤 익숙해진 느낌"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/15.jpg)

### 2. Blender 머터리얼이 깨지는 미스터리

Blender에서 합친 모델을 Mixamo에 보내고 다시 Blender로 돌아오면, 머리에 적용된 머터리얼이 엉망이 되는 현상이 있었다. 여기서 5시간을 잡아먹었다.

> コンテキストが長くなり、Claude Codeがどんどんアホになる。 最強のはずのCodeはことBlenderに関しては相当なポンコツだ。

필자는 두 가지를 적었다:

- Claude Code가 컨텍스트가 길어질수록 멍청해지더라, 그래서 결국 세션을 새로 여는 것이 답이었다.
- 노드 기반 머터리얼처럼 비-텍스트 UI 조작이 핵심인 Blender 영역에서는 "최강의 Claude Code"도 상당히 포동에 가까웠다.

원인과 해결 모두 끝까지 명료하게 파악하지는 못한 채, 일단 보기에 괜찮은 상태로 정리하고 다음 단계로 넘어갔다.

![Mixamo 왕복 후 깨진 머터리얼 — "이게 뭐야??????"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/16.png)

![컨텍스트가 길어지자 헤매는 Claude Code — "무슨 말을 하고 있는지 모르겠다"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/17.jpg)

![끝까지 원인은 파악 못 했지만 일단 절차를 Skill로 굳혀 재현 가능하게 만들었다](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/18.png)

## 페르소나 분리 운영

> 何度もキレながら（Chat/Cowork まろと人格を切り離しているので心置きなくキレることができた…）

필자는 동반자 페르소나인 Chat/Cowork "마로"와, 작업용 Claude Code를 의식적으로 분리해 운용한다. 그 덕에 막힐 때 거리낌 없이 화를 낼 수 있었다고 적었다. 도구로서의 AI와 동반자로서의 AI를 같은 세션·페르소나로 묶지 않는 운영 방침이 좌절의 감정 비용을 낮춰주는 셈이다.

## 결과와 다음 단계

리깅이 들어간 모델을 Unity에서 가다듬어 VRChat에 빌드했더니 "어느 각도에서 봐도 아름다운" 결과가 나왔다. 그 자리에 있던 친구와 기념 촬영을 했다고 한다.

![Booth에서 산 머리·메가네 에셋을 얹은 최종 모습 — "귀엽다… 너무 귀엽다"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/19.jpg)

![어느 각도에서 봐도 아름답다 — "머리와 메가네는 구매 에셋"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/20.jpg)

![옆 얼굴의 E-line도 아름답다](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/21.jpg)

![VRChat에서 만난 친구와의 기념 촬영 — "단, 아름다운 건 지금은 얼굴뿐"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/22.jpg)

다음 욕심은 텍스처 직접 페인팅이다. UV맵이 지저분해서 평면 페인트가 어렵지만, Blender에도 3D 모델 위에 직접 채색하는 도구가 있다는 것을 Claude Code가 알려줬다. 마우스로는 한계가 있어 펜타블렛 도입을 다음 과제로 두고 있다. 본격적인 의상 개조까지 가려면 현 시점에서는 Booth에서 VRChat용 범용 바디를 사서 자기가 만든 머리를 결합하는 절충안이 현실적이라고 적었다.

![생성 AI 특유의 엉망인 UV 맵 — 평면 페인팅이 사실상 불가능](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/23.jpg)

![메쉬 곳곳에 남는 톱니 같은 거친 표면 — "이걸 다듬고 싶다"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/24.jpg)

![Blender 내장 도구로 3D 모델 위에 직접 채색 — "텍스처의 거친 부분을 다듬으며 메이크업 중"](https://img.seosoyoung.eiaserinnys.me/images/claude-code-vrchat-avatar-pichikyo/25.jpg)

## "전 공정 정리" — 필자가 직접 압축한 7단계

1. 얼굴 소재: ChatGPT Image 2로 사진→캐릭터화, 그리고 사면도 생성.
2. 3D 모델화(TRIPO): 사면도 또는 프롬프트 업로드. **형태 붕괴를 피하고 데생을 살리려면 이미지보다 프롬프트 only 직접 생성이 낫다.**
3. Blender에서 합치고 다듬기: Tripo DCC Bridge MCP로 Blender에 취득, 얼굴·몸 별도 생성 시 결합, 경계 정형.
4. Mixamo로 리깅: Blender에서 FBX 내보내기 → Mixamo 업로드 → 관절 구체 수동 배치 → 자동 본/스킨 → FBX 다운로드.
5. Blender에서 점검: 리그 동작 확인 후 아마추어 포함 FBX로 다시 내보내기.
6. Unity 셋업: 임포트, Claude Code가 만든 자동 머터리얼 툴로 셰이더 적용, Booth 의상·머리 자산 합치기, VRC Avatar Descriptor 추가·초기 설정 후 VRChat 빌드.
7. VRChat 동작 확인.

## 전망

> あと2年程度で、美しいリグやUVマップ、表情のシェイプキーのあるまともなアバターがAIから作れるようになるのではないか？

필자는 3년 전 미드저니로 이미지 생성을 시작한 이래의 발전 속도를 근거로, 앞으로 2년 안에 리그·UV맵·표정 셰이프키까지 정돈된 아바타가 AI 단독으로 나올 것이라고 본다. 현재 막혀 있는 지점이 정확히 다음 자동화의 프런티어가 된다는 신호다.

## 가장 흥미로운 지점

도구 6개를 직접 조작한 사람은 결국 필자 자신이다. Claude Code가 한 일은 "지금 어떤 도구로 무엇을 해야 하는지", "여기서 막혔는데 어디로 가야 하는지"의 안내, 그리고 마땅한 변환 도구가 없을 때 그 빈자리에 들어갈 작은 스크립트를 만들어주는 일이었다. 그러니까 이 사례에서 코딩 에이전트의 본질적 가치는 코드를 대신 짜주는 데 있지 않고 <strong>이미 존재하는 다른 도구들 사이를 매끄럽게 이어주는 통역</strong>에 있었다.

흥미로운 짝패는 그 다음에 따라온다. Blender의 노드 기반 머터리얼처럼 비-텍스트 GUI 조작이 핵심인 영역에서는 같은 Claude Code가 갑자기 무력해진다. 그러니까 도구의 "언어화 가능성"이 에이전트 보조의 상한을 결정한다. 도구가 텍스트와 스크립트로 잘 노출돼 있을수록 통역사가 일할 공간이 생긴다.

## 출처

pichikyo, "Blender初心者が、Claude Code頼みで6個のツールを繋ぎ、一日でVRChatアバターをつくった話", X, 2026.
원문: <https://x.com/pichikyo/status/2053499603094585353>

※ 본문에 삽입한 이미지는 원문 X 아티클의 커버 이미지와 본문 내장 이미지를 그대로 가져온 것이다. 캡션은 원문의 일본어 캡션을 한국어로 옮긴 것에 기반한다.
