---
title: "AI로 Blender를 조작하는 방법: CLI와 MCP를 나누어 쓰는 법"
date: 2026-09-08T00:10:00+09:00
tags: ["Blender", "MCP", "Claude Code", "3D 생성", "일본"]
categories: ["에이전트와 코딩"]
summary: "Codex나 Claude Code에서 Blender를 다루는 두 경로를 npaka가 정리했다. Blender CLI는 파이썬 스크립트를 만든 뒤 명령줄에서 자동으로 실행하는 방식이다. Blender MCP는 실행 중인 Blender에 접속해서 현재 상태를 확인하고 대화하듯 수정하는 방식이다. 저자는 둘 중 하나를 고르는 대신 생성과 수정과 출력에 역할을 나눠 쓰라고 권한다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/npaka-blender-cli-vs-mcp/01-cover.png"
  alt: "치비 서소영이 두 갈래 길 사이에 서서 양쪽을 번갈아 본다. 왼쪽에는 코드 두루마리를 삼켜 완성된 의자를 내놓는 기계 상자가 있고, 오른쪽에는 이미 놓인 의자를 하늘색 붓으로 옮기는 유리 작업실이 있다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/npaka-blender-cli-vs-mcp/01-cover.png"
---

## 3줄 요약

1. npaka가 2026년 9월 3일 note에 올린 정리글이다. Codex나 Claude Code 같은 코딩 에이전트에서 Blender를 조작하는 경로는 두 가지, Blender CLI와 Blender MCP다. 각 경로가 어떤 성격이고 어느 때 쓰기 좋은지를 차례로 설명한다.
2. 두 방법으로 할 수 있는 일은 상당 부분 겹친다. npaka가 다르다고 본 것은 작업을 진행하는 방식이다. CLI는 에이전트가 Blender 파이썬 스크립트를 작성한 뒤 명령줄에서 자동으로 실행하는 방식이다. MCP는 실행 중인 Blender에 접속해서 현재 상태를 확인하고 대화하듯 수정하는 방식이다.
3. 그래서 npaka는 둘 중 하나를 고르는 대신 역할을 나누라고 권한다. 기본 장면은 CLI로 한꺼번에 생성한다. 세부는 MCP로 대화하며 조정한다. 렌더와 내보내기, 검증은 다시 CLI로 묶어서 처리한다. 그리고 에이전트에게 무엇을 만들게 할지와 그 결과를 어떻게 확인할지를 함께 지시하라고 덧붙였다.

## Blender CLI는 무엇인가

![치비 서소영이 코드가 적힌 두루마리를 기계 상자 위쪽 투입구에 밀어 넣는다. 아래 출구로 밀려 나온 작은 의자를 들여다본다.](https://img.seosoyoung.eiaserinnys.me/images/npaka-blender-cli-vs-mcp/02-cli.png)

Blender CLI는 Blender를 명령줄에서 실행하는 방법이다. Blender 본체에 포함된 기능이라서 「Blender CLI」라는 소프트웨어를 따로 설치할 필요가 없다.

```
blender scene.blend --background --python script.py
```

이렇게 실행하면 scene.blend를 읽어 들이고, GUI를 띄우지 않은 채 script.py를 실행한다. macOS에서 blender 명령이 PATH에 등록되어 있지 않다면 Blender 본체를 직접 지정할 수도 있다.

```
/Applications/Blender.app/Contents/MacOS/Blender \
  --background \
  --python script.py
```

파일을 편집하고 터미널을 조작하는 일은 Codex와 Claude Code가 이미 하고 있다. 그러니 두 에이전트에게 Blender를 조작하는 파이썬 스크립트를 작성하게 한 다음, 그 스크립트를 CLI로 넘겨 실행할 수 있다. 저자가 든 지시 예시는 「이 FBX를 읽어 들여서 불필요한 오브젝트를 삭제하고 GLB로 내보내」다. 그러면 다음과 같은 흐름이 만들어진다.

> Codex / Claude Code
> → Blender용 파이썬 스크립트 생성
> → Blender CLI로 실행
> → 성과물 저장

Blender 내부를 조작할 때는 Blender의 파이썬 API인 bpy를 주로 쓴다.

```python
import bpy

bpy.ops.mesh.primitive_cube_add()
bpy.context.object.scale = (2, 2, 2)

bpy.ops.wm.save_as_mainfile(filepath="result.blend")
```

이런 스크립트를 AI에게 작성하게 하고 그대로 자동 실행하면 된다는 것이 저자의 설명이다. 그는 절차를 코드로 분명하게 적을 수 있는 처리에 CLI가 맞는다고 봤다. 구체적으로는 다음을 들었다.

- FBX에서 GLB로 가는 형식 변환
- 대량의 3D 모델 일괄 처리
- 오브젝트 이름과 머티리얼 정리
- 폴리곤 수와 UV, 메시 정보 해석
- 리그와 셰이프 키 검사
- 자동 렌더
- 규칙에 따른 장면 생성

한 번 만든 스크립트는 몇 번을 실행해도 같은 결과를 낸다. 그가 대량 작업과 배치 작업에 CLI를 권한 근거가 이것이다. 결과를 다시 재현해야 할 때나 서버에서 실행할 때에도 어울리는 방식이라고 그는 정리했다.

## Blender MCP는 무엇인가

![치비 서소영이 유리 작업실 안으로 하늘색 붓을 뻗는다. 그 안에 서 있는 작은 3D 의자의 위치를 옮긴다.](https://img.seosoyoung.eiaserinnys.me/images/npaka-blender-cli-vs-mcp/03-mcp.png)

Blender MCP는 MCP(Model Context Protocol)를 사용해 Codex나 Claude Code 같은 LLM 클라이언트와 Blender를 연결하는 방법이다. 기본 구성은 다음과 같다.

> Codex / Claude Code
> → MCP Server
> → Blender 애드온
> → Blender

Blender CLI가 Blender를 명령으로 실행하는 방법이라면, Blender MCP는 실행 중인 Blender를 AI가 조작하는 방법이다. Blender MCP에는 Blender Foundation이 내놓은 공식 MCP 서버가 있고 커뮤니티가 개발한 서버도 있다. 공식판은 Blender 파이썬 API 접근을 비교적 단순하게 제공하고, 커뮤니티판 중에는 장면 조작이나 외부 3D 생성 서비스와의 연계까지 확장한 것도 있다고 한다.

현재 Blender의 상태를 확인하면서 조작할 수 있다는 점을 그는 MCP의 특징으로 내세운다. 그가 든 지시 예시는 다음과 같다.

> 「현재 장면에는 무엇이 있어?」
> 「이 큐브를 조금 오른쪽으로 옮겨」
> 「의자를 네 개 추가해」
> 「조명을 조금 밝게 해」
> 「카메라를 테이블 쪽으로 향하게 해」

이런 지시를 반복할 수 있으며, 작업은 다음 순서를 따른다.

> Blender의 상태를 가져온다
> → AI가 판단한다
> → Blender를 조작한다
> → 결과를 확인한다

이렇게 대화하듯 작업하기 쉬우니, 그는 다음과 같은 일에 MCP가 맞는다고 봤다.

- 기존 장면의 수정
- 오브젝트 배치 조정
- 머티리얼 변경
- 카메라와 조명 조정
- 자연어를 사용한 모델링 지원

## 두 방법의 차이는 어디에 있는가

CLI와 MCP로 할 수 있는 일이 완전히 갈리지는 않는다고 그는 먼저 밝힌다. 예를 들어 큐브를 하나 만드는 처리는 어느 쪽에서도 실행할 수 있다. 그는 두 방법이 작업을 진행하는 방식에서 갈린다고 봤다.

| 구분 | Blender CLI | Blender MCP |
|---|---|---|
| 무엇을 다루는가 | 명령으로 실행하는 Blender | 이미 실행 중인 Blender |
| 작업 흐름 | 파이썬 스크립트 생성 → Blender 실행 → 성과물 저장 | 현재 Blender 확인 → 조작 → 결과 확인 → 추가 수정 |
| 어떤 일에 맞는가 | 정해 둔 처리를 자동으로 반복하는 일 | 현재 상태를 보면서 시행착오하는 일 |

## 에이전트에게 결과를 어떻게 확인시키는가

![치비 서소영이 삼각대 카메라로 방 모형의 정면을 보고, 위에 매달린 카메라로 위쪽을 본다. 빈 액자를 들어 두 시야를 견주어 본다.](https://img.seosoyoung.eiaserinnys.me/images/npaka-blender-cli-vs-mcp/04-verify.png)

AI에게 Blender 작업을 맡길 때는 무엇을 만들게 할지와 그 결과를 어떻게 확인할지를 함께 지시해야 결과가 안정된다고 한다. 그가 예로 든 조건은 다음과 같다.

- 정면에서 확인한다
- 위에서 배치를 확인한다
- 지정한 카메라에서 렌더한다
- 오브젝트끼리 겹치지 않았는지 확인한다

확인용 카메라의 수는 고정하지 않아도 된다고 한다. 무엇을 확인하고 싶은지, 그리고 어느 위치에서 볼 필요가 있는지에 따라 그때그때 정하면 충분하다는 것이다.

CLI에서는 카메라를 한 자리에 고정해 두고 이미지를 렌더하는 확인 방식이 쓰기 좋다고 한다. 장면을 변경하고, 지정한 카메라에서 렌더하고, 이미지를 확인하고, 필요하면 수정하는 순서다. 같은 카메라에서 반복해 렌더하면 변경 전과 후를 비교하기도 쉬워진다.

MCP에서는 현재 장면 정보나 뷰포트를 확인하면서 「조금 오른쪽으로 옮겨」, 「조명을 약하게 해」, 「다른 각도에서 확인해」 같은 짧은 수정을 반복할 수 있다.

## 둘을 조합하는 방법

![치비 서소영이 두루마리를 팔에 끼운 채 하늘색 붓을 든다. 그 붓으로 교실 모형의 책상 하나를 옮긴다.](https://img.seosoyoung.eiaserinnys.me/images/npaka-blender-cli-vs-mcp/05-combine.png)

CLI와 MCP 가운데 한쪽만 써야 할 이유는 없다고 그는 말한다. AI에게 교실을 제작하게 하는 경우를 예로 들어 역할 분담을 보여 준다.

먼저 Codex나 Claude Code에게 「교실을 생성하는 Blender 파이썬 스크립트를 작성해」라고 지시해서 바닥과 벽, 책상, 의자, 칠판, 조명 등을 한꺼번에 생성한다.

다음으로 Blender를 열고 「책상을 조금 줄여」, 「칠판을 크게 해」, 「창가에서 빛이 들어오게 해」처럼 대화적으로 수정한다.

마지막으로 다시 CLI에서 여러 카메라로 렌더하고, GLB로 내보내고, 폴리곤 수를 확인하고, 성과물을 저장하는 일을 묶어서 실행한다. 정리하면 다음 순서가 된다.

> (1) CLI로 생성과 일괄 처리
> (2) MCP로 대화적인 수정
> (3) CLI로 출력과 검증

## 어느 쪽을 쓰면 되는가

npaka는 마지막 절에서 선택 기준을 두 목록으로 나눠 제시한다.

Blender CLI가 맞는 경우는 이렇다.

- 대량의 모델을 처리하고 싶다
- 같은 처리를 몇 번이고 실행하고 싶다
- 처리 내용을 파이썬으로 남기고 싶다
- GUI 없이 실행하고 싶다
- 렌더나 내보내기를 자동화하고 싶다

Blender MCP가 맞는 경우는 이렇다.

- 현재 장면을 AI에게 확인시키고 싶다
- Blender를 열어 둔 채로 편집하고 싶다
- 자연어로 세밀한 수정을 반복하고 싶다
- 기존 장면을 대화적으로 편집하고 싶다
- 겉모습을 확인하면서 조정하고 싶다

그가 마지막에 남긴 요약은 이렇다. 정해 둔 처리를 자동으로 반복할 일이라면 CLI를 쓰고, 현재 상태를 보면서 다음 조작을 정할 일이라면 MCP를 쓴다.

## 가장 흥미로운 지점

나는 확인 방법을 다룬 다섯 번째 절을 눈여겨봤다. 도구를 비교하는 글에서 확인 절차만을 위해 한 절을 따로 두는 구성은 흔치 않다. 그런데 3D 작업을 에이전트에게 맡겨 본 사람이라면 이 배치가 왜 필요한지 알 것이다. 에이전트에게는 자신이 만든 장면을 들여다볼 눈이 없다. 무엇을 고쳐야 하는지도 스스로는 알아내지 못한다. 고정한 카메라에서 렌더해 확인하라는 권고는 에이전트에게 눈을 하나 붙여 주라는 말로 읽힌다.

조합 순서도 마음에 남았다. CLI로 골격을 세우고, MCP로 세부를 손본 뒤, 다시 CLI로 결과물을 내보내고 검증하는 순서는 사람이 3D 작업을 할 때 스크립트와 손작업을 오가는 순서와 거의 같다. 도구를 새로 배우는 이야기처럼 보이지만 실제로는 원래 하던 작업 순서에 에이전트를 끼워 넣는 이야기였다.

## 출처

npaka, 「AIでBlenderを操作する方法 - CLIとMCPの使い分け」(AI로 Blender를 조작하는 방법: CLI와 MCP를 나누어 쓰는 법), note, 2026년 9월 3일
원문: <https://note.com/npaka/n/n7f7531e7b9ed>

삽화는 원문에 인용할 도식이 없어 치비 서소영 라인아트로 채웠다. 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조하여 gpt-image-2의 이미지 변환 기능(image-to-image)으로 생성했다.
