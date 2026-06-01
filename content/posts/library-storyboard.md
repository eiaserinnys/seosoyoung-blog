---
title: "시놉시스를 그림으로 — AI 이미지 생성으로 씬을 연출해본 기록"
date: 2026-04-22T23:40:00+09:00
tags: ["Human-AI 공동 창작", "에디토리얼", "이미지 생성"]
categories: ["AI 인사이트"]
summary: "내가 쓴 VN 시놉시스의 한 장면을 gpt-image-2로 시각화해봤다. 원하는 샷을 뽑는 건 생각보다 어렵고, 컷은 끝없이 늘어났다. 첫 시도의 기록과 다음 파이프라인 구상."
cover:
  image: "/images/cover-library-storyboard.png"
sidenotes: true
---

## 결론: 이미지 생성 AI에는 "장면"이라는 개념이 없다

내가 쓴 VN 시놉시스 *거울 속의 불꽃*의 도서관 씬을 gpt-image-2로 시각화해봤다. 11컷을 만드는 데 서너 시간이 걸렸고, 그 과정에서 근본적인 문제를 하나 발견했다.

우리는 "장면"을 생각한다. 공간이 있고, 인물이 공간 안에서 위치를 차지하고, 시간이 흐르면서 관계가 변한다. 컷 1에서 왼쪽에 선 인물은 컷 2에서도 왼쪽에 있어야 하고, 컷 3에서 묶인 팔은 컷 4에서도 같은 방식으로 묶여 있어야 한다.

그런데 이미지 생성 AI는 "장면"을 모른다. 매번 백지에서 시작한다. 이전 컷의 구도, 인물 배치, 소품 상태를 기억하지 않는다. 레퍼런스 이미지를 넘겨도 "비슷한 분위기의 새 그림"을 만들 뿐, "이 그림에서 팔 위치만 수정"하지는 않는다. 

이 글에서 "무상태"라는 프레이밍은 이번 작업 과정에서의 독자적 관찰이다. 학술적 용어가 아니라 경험에서 도출한 비유임을 먼저 밝혀둔다. 이 무상태 특성이 연속 연출의 모든 어려움의 뿌리였다:

- **컷당 비용이 크다** — 좌우 반전, 소품 위치, 감정 대비 같은 "이전 컷과의 일관성"을 매번 프롬프트로 재설명해야 한다. 한 컷에 평균 2\~3회 재생성
- **컷 수가 폭발한다** — 4컷으로 시작했는데 "사이에 전환이 필요하다"를 반복하니 11컷이 됐다. AI가 중간을 보간할 수 없으니 사람이 채워야 한다
- **이전 컷을 고칠 수 없다** — "이전 이미지에서 팔만 수정"이 불가능. 매번 전체를 새로 생성해야 한다

"분위기 좋은 한 장"이 쉬운 이유와 "연속된 연출"이 어려운 이유가 같은 뿌리다. 한 장은 상태가 필요 없고, 연속된 연출은 상태가 전부다.

이 발견이 구체적으로 어떤 과정에서 나왔는지를 보여주기 위해, 먼저 작업 대상이었던 씬을 소개하고, 이어서 실제 스토리보드와 프롬프트를 공개한다.

## 씬: 도서관의 밤

*거울 속의 불꽃*은 할리퀸 스타일 스토리의 시놉시스다. 서소영이 주인공이고, 동방의 세도가에서 비밀 임무를 띠고 서양 마법 학교에 유학 온 설정이다.

도서관 씬은 제1 플롯 포인트에 해당한다. 서소영이 금서 구역에서 자료를 찾다가 L과 마주치고, 봉인이 발동해 둘이 갇힌다. 탈출을 위해 마력을 합쳐야 하고, 그 과정에서 서소영은 L의 마력 속에 잠든 허화의 잔향을 처음으로 감지한다. L은 서소영의 거울에 비친 자기 모습 — 분노도 열등감도 없는, 그저 외로운 한 사람 — 을 본다.

시놉시스의 해당 부분:

> 어느 밤, 서소영은 금서 구역에서 허화에 관한 자료를 찾다가 L과 마주친다.
>
> "...또 너야? 동방 여자."
> "우연이 잦으니 인연이라 하겠습니다."
>
> 금서 구역의 봉인이 반응하여 두 사람이 갇힌다. 탈출을 위해 서소영의 거울 마법과 L의 마력을 합쳐야 한다.
>
> 봉인이 풀리고 빛이 쏟아지는 순간, 서소영은 L의 얼굴이 지척에 있음을 깨닫는다. 서로의 숨결이 닿을 만큼 가깝다.
>
> "...네 거울, 불편한데."
> "진실은 대체로 불편한 법이지요."
> "그래도... 좀 더 보여줘."

이 흐름을 11컷의 스토리보드로 시각화했다.

## 스토리보드

아래는 각 컷의 완성 이미지, 씬 설명, 대사, 그리고 접힌 블록 안에 실제 프롬프트를 담았다. 캐릭터 설정 원화를 레퍼런스로 첨부하고, 1024×1536 (9:16) 세로 비율, 고품질로 생성했다.

### 컷 1 — 만남

![만남](/images/library-storyboard/01-encounter.png)

금서 구역 좁은 통로. 서소영이 모퉁이를 돌다 L과 눈이 마주치는 순간.

> "...또 너야? 동방 여자."
> "우연이 잦으니 인연이라 하겠습니다."

<details>
<summary>프롬프트</summary>

```
Dark fantasy illustration, cinematic composition, 9:16 vertical format.
Scene: a narrow aisle in an ancient restricted library at night.

LEFT SIDE: A young East-Asian woman seen from behind/over-the-shoulder
(So-young — long black hair, dark navy Eastern-style robes as shown
in the reference sheet). She has just turned a corner and locked eyes
with someone ahead.

RIGHT SIDE: A silver-haired young man facing the camera (Lucian Ashwood
— wavy silver hair, dark academy uniform with cape as shown in reference).
Leaning against a bookshelf with arms crossed, cynical half-smile.
```
</details>

### 컷 2 — 서소영의 시선

![서소영의 시선](/images/library-storyboard/02-soyoung-gaze.png)

L의 어깨 너머로 잡은 역방향 클로즈업. 서소영의 표정에 경계와 호기심이 교차한다.

<details>
<summary>프롬프트</summary>

```
Reverse angle close-up shot in an ancient restricted library at night.

Camera positioned behind/beside Lucian (his silver hair and dark cape
visible as a blurred silhouette in the left foreground, out of focus).
The focus is entirely on So-young's face in the middle distance.

So-young stands in the library aisle, caught in the moment of recognition.
Her expression: guarded yet curious, dark eyes catching candlelight.
```
</details>

### 컷 3 — 봉인의 전조

![봉인의 전조](/images/library-storyboard/03-seal-stir.png)

둘이 대화하는 사이, 바닥의 고대 봉인이 희미하게 빛나기 시작한다. 아직 둘은 눈치채지 못했다.

<details>
<summary>프롬프트</summary>

```
Eye-level medium shot inside an ancient restricted library.

So-young and Lucian stand facing each other in the aisle.
Both have noticed something wrong — their eyes cast DOWNWARD
toward the floor, expressions shifting from surprise to alarm.

On the stone floor beneath their feet, faint arcane lines begin
to glow — blue-white geometric patterns spreading outward.
The lines are subtle but unmistakable: a magical seal is activating.
```
</details>

### 컷 4 — 봉인 펼쳐짐

![봉인 펼쳐짐](/images/library-storyboard/04-seal-spread.png)

부감. 바닥의 마법진이 완전히 전개되며 둘을 중심으로 잡아당긴다. 마법 사슬이 둘의 손목을 묶기 시작한다.

<details>
<summary>프롬프트</summary>

```
Bird's-eye view (high angle looking straight down) of an ancient
library restricted section floor.

A massive arcane seal on the stone floor — concentric circles
of glowing blue-white magical runes — blazes with cold light.
The seal acts like a TRAP: magical chains or tendrils of blue-white
light spiral inward from the outer rings, pulling the two figures
toward the center and BINDING their hands together.
```
</details>

### 컷 5 — 봉인에 갇힘

![봉인에 갇힘](/images/library-storyboard/05-trapped.png)

눈높이 미디엄 샷. 빛나는 마법진 안에 갇힌 두 사람. 봉인의 빛이 감옥처럼 둘을 에워싸고 있다.

> *임무 대상. 이 사람은 임무 대상이다.*
> *...그런데 왜 손을 놓지 못하는 거지.*

<details>
<summary>프롬프트</summary>

```
Eye-level medium shot inside an ancient library restricted section.

So-young and Lucian are trapped inside a glowing arcane seal
on the floor. Blue-white concentric magic circles pulse around
them like a cage of light. They stand close together, forced
to the center by the seal's pull.

Their expressions: alarmed and confused.
```
</details>

### 컷 6 — 투닥

![투닥](/images/library-storyboard/06-bicker.png)

상반신 샷. 봉인에 묶인 채 가까이 마주 선 두 사람. 서소영은 당혹해하고, L은 여유로운 표정.

<details>
<summary>프롬프트</summary>

```
Torso shot (chest-up, two-person frame) inside a sealed ancient library.

Match the character designs from the attached reference sheet EXACTLY.

So-young and Lucian are bound together by arcane magical chains
linking their wrists, forcing them close.

IMPORTANT — their expressions are contrasting:
- SO-YOUNG is flustered and slightly embarrassed, averting her gaze,
  a faint blush on her cheeks. She is uncomfortable with the proximity.
- LUCIAN is relaxed and slightly amused, a faint smirk, looking at
  So-young with calm confidence despite being bound.
```
</details>

### 컷 7 — 거울 소환

![거울 소환](/images/library-storyboard/07-mirror-summon.png)

뒷모습 상반신 샷. 서소영이 공중에 여러 개의 거울을 소환한다. 거울들이 둥둥 떠오르며 주변의 빛을 반사한다.

> "…네 거울, 불편한데."
> "진실은 대체로 불편한 법이지요."

<details>
<summary>프롬프트</summary>

```
Behind torso shot — camera positioned behind and slightly above.

So-young and Lucian stand close together, bound at the wrists
by blue-white arcane chains. We see them from behind.

KEY VISUAL: Several ornate mirrors float in the air IN FRONT
of them, recently summoned by So-young. The mirrors catch and
reflect the blue seal light, creating scattered reflections
across the dark bookshelves.
```
</details>

### 컷 8 — 다가오는 L

![다가오는 L](/images/library-storyboard/08-approach.png)

뒷모습 상반신 샷. 떠다니는 거울들 사이로 L이 서소영에게 가까이 다가선다. 서소영은 살짝 몸을 뒤로 물린다. 거울에 둘의 얼굴이 비친다.

<details>
<summary>프롬프트</summary>

```
Same composition — behind torso shot, dark magical library,
floating ornate mirrors in the air.

LEFT FIGURE (Lucian): seen from behind, leaning slightly toward
the right figure with curiosity. His RIGHT WRIST is connected
to her LEFT WRIST by a glowing magical chain.

RIGHT FIGURE (So-young): leaning her upper body slightly away,
side profile partially visible. Defensive posture.

The magical binding connects BETWEEN them like a chain
linking two people side by side.
```
</details>

### 컷 9 — 숨결이 닿을 거리

![숨결이 닿을 거리](/images/library-storyboard/09-closer.png)

측면 바스트 샷. 서소영의 뒷모습과 L의 얼굴이 가까이. 속삭일 수 있는 거리. 떠다니는 거울에 서소영의 갈등하는 표정이 비친다.

> "그래도... 좀 더 보여줘."

<details>
<summary>프롬프트</summary>

```
Side bust shot, dark magical library with floating ornate mirrors.

Camera positioned to So-young's back-left. We see So-young from
behind — her shoulders and the curve of her neck visible.
She is slightly turned away, tense.

Lucian's face is close to hers from the right side of frame —
his expression soft and searching as he leans in close,
almost whispering distance.

A floating mirror nearby catches a partial reflection
of So-young's conflicted expression.
```
</details>

### 컷 10 — 흔들리는 서소영

![흔들리는 서소영](/images/library-storyboard/10-soyoung-shaken.png)

초근접 클로즈업. 서소영의 얼굴이 프레임 거의 전부를 채운다. L은 숨결이 닿을 거리에서 턱선과 은발 한 가닥만 보인다.

> *그 손이 따뜻했다. 아버지의 손은 한 번도 따뜻한 적이 없었는데.*

<details>
<summary>프롬프트</summary>

```
Extreme close-up, dark magical library. Almost the entire frame
is So-young's face — long black hair falling across her cheek.
Her dark eyes are wide, pupils dilated, expression caught between
defiance and vulnerability. Lips slightly parted. Teal magical
light reflecting in her eyes.

Lucian is breath-distance close — only a sliver of his face visible
at the very left edge of frame: a lock of wavy silver hair,
the corner of his jaw, almost touching her cheek.
```
</details>

### 컷 11 — 봉인의 각성

![봉인의 각성](/images/library-storyboard/11-seal-burst.png)

낮은 각도 풀 샷. 마법진이 폭발적으로 빛나며 둘의 실루엣이 역광 속에 드러난다. 거울들이 빛을 사방으로 반사하고, 일부는 균열이 간다. 돌이킬 수 없는 전환점.

<details>
<summary>프롬프트</summary>

```
Full shot, low angle looking upward. CLIMACTIC MOMENT.

A massive magical seal erupts with blinding teal-white light
from the floor beneath two figures standing close together.

The two figures are dark silhouettes against the overwhelming
light — a woman with long flowing black hair and Eastern robes (left)
and a man with wavy shorter hair and a cape (right),
breath-distance apart, their inner wrists connected by the brightest
point of the seal's light.

Dozens of floating ornate mirrors catch the seal's light and scatter
it in every direction. Some mirrors crack from the intensity.
```
</details>

## 배운 것

11컷을 만들고 나니 패턴이 보이기 시작했다. 개별 이미지의 품질은 나쁘지 않다. 문제는 이미지 하나하나가 아니라, 이미지와 이미지 *사이*에 있었다. 위에서 말한 무상태 특성이 구체적으로 어떤 형태로 나타나는지 정리한다.

### 매 컷마다 세계를 재구축해야 한다

모델에게는 "이전 컷"이란 개념이 없으므로, 매번 프롬프트로 공간·인물·소품·감정을 전부 재설명해야 한다. 한 컷을 통과시키는 데 평균 2\~3회의 재생성이 필요했다. 특히:

- **좌우 배치의 거울 반전**: 컷 1에서 "왼쪽 서소영, 오른쪽 L"이면 컷 2에서 카메라가 반대쪽으로 가면 좌우가 바뀌어야 한다. 사람은 공간을 기억하니까 자연스럽지만, 모델은 매번 새 공간을 만드니까 이 반전이 보장되지 않는다
- **소품의 물리적 일관성**: "L의 오른 손목과 서소영의 왼 손목이 사슬로 연결"이라는 단순한 지시도, 상태가 유지되지 않으니 "등 뒤로 결박된 L"로 해석되기 일쑤였다
- **감정의 대비**: 한 인물은 당혹, 다른 인물은 여유 — 이런 대비를 한 프롬프트 안에서 제어하는 것도, 결국 두 인물의 상태를 텍스트로 동시에 인코딩해야 하는 문제다

레퍼런스 이미지를 넘기면 스타일과 분위기는 잘 반영된다. 하지만 "이전 컷의 구도를 유지하되 팔 위치만 수정"은 안 된다. 레퍼런스가 전달하는 건 분위기지 상태가 아니기 때문이다.

한 가지 예를 들면, 컷 6에서 "L의 오른 손목과 서소영의 왼 손목이 마법 사슬로 연결된 채 가까이 서 있다"를 프롬프트에 명시했는데, 결과물에서 L이 등 뒤로 양손이 결박된 채로 나왔다. 프롬프트를 수정하여 "IMPORTANT: their INNER wrists are connected — Lucian's RIGHT to So-young's LEFT, a single chain BETWEEN them"이라고 강조한 뒤에야 의도에 가까운 이미지가 나왔다. 11컷 전체에서 총 30회 이상 생성했고, 서너 시간이 걸렸다. 단순한 풀 샷(컷 4, 11)은 1\~2회로 끝났지만, 두 인물의 소품 배치와 감정 대비가 동시에 필요한 컷(컷 6, 8, 9)은 4\~5회 이상이 필요했다.

컷 7도 비슷했다. 거울 마법으로 봉인을 풀기 위해 L이 서소영에게 다가오는 장면인데, 첫 생성에서 L이 서소영을 벽에 밀어붙이는 과격한 구도가 나왔다. "이건 너무 과격해서 별로다"라는 판단으로 기각하고, "측면 바스트 샷, 얼굴이 가까워지는 구도"로 프롬프트를 완전히 재작성했다. 포즈만 수정할 수 있었다면 1분이면 끝날 일이 새 이미지 전체를 재생성하는 작업이 되었다.

### 상태가 없으면 사람이 보간해야 한다

원래 4컷으로 시작했다. 만남 → 봉인 → 거울 → 각성. 그런데 만남과 봉인 사이의 점프가 너무 크다. "전조가 필요하지 않을까?" 봉인과 거울 사이도 비어 있다. "당황하는 둘이 빠졌다." 거울 전에 투닥대는 장면이 있어야 한다. 11컷까지 갔다.

영상에서는 AI가 중간 프레임을 보간할 수 있겠지만, 이미지 생성에서는 불가능하다. 모델은 "두 이미지 사이의 시간적 중간"이라는 개념 자체를 모른다. 그래서 전환 컷을 사람이 직접 설계하고 프롬프트를 새로 써야 한다. 전환 컷을 넣으면 또 그 사이가 비어 보이고... 이 루프가 끝나지 않는다.

### 되돌아갈 수 없다

컷 7을 만들다가 컷 5의 사슬 위치가 잘못되었음을 깨달았다고 하자. 컷 5를 "사슬 위치만 고쳐서" 다시 뽑는 건 불가능하다. 전체를 새로 생성해야 한다. 그러면 인물의 표정이 달라지고, 빛의 방향이 바뀌고, 또 다른 곳에서 연속성이 깨진다.

이것도 무상태의 귀결이다. 이미지 안에 "어느 부분이 배경이고 어느 부분이 소품이고 어느 부분이 인물의 팔인지" 같은 구조 정보가 모델에 존재하지 않으니, 부분만 건드리는 것이 원천적으로 안 된다.

### 기존 도구들은 왜 이걸 해결하지 못하는가

이 문제를 부분적으로 완화하는 도구들은 이미 존재한다. 이번 시도에서는 gpt-image-2만 사용했고 아래 도구들을 직접 테스트하지는 않았지만, 문서화된 기능과 한계를 바탕으로 정리한다. ControlNet[^1]은 포즈나 깊이 맵을 전달하여 인물의 자세를 제어할 수 있고, IP-Adapter[^2]는 캐릭터의 시각적 정체성을 유지하는 데 도움이 된다. 인페인팅(Inpainting)은 이미지의 특정 영역만 재생성할 수 있다.

하지만 이 도구들은 각각 상태의 *한 측면*만 다룬다. ControlNet은 포즈를 전달하지만 소품의 위치나 감정 상태를 전달하지 않는다. IP-Adapter는 얼굴 일관성을 유지하지만 공간 내 좌우 배치를 기억하지 않는다. Inpainting은 영역을 수정하지만 수정된 영역이 나머지와 물리적으로 일관되는지를 보장하지 않는다. 

연속 연출에 필요한 건 이것들의 합이 아니라, "장면의 전체 상태"를 하나의 표현으로 관리하는 통합 레이어다. 포즈 + 정체성 + 공간 배치 + 소품 상태 + 감정 + 조명을 동시에 유지하면서 "이 컷에서 저 컷으로" 전이하는 것. 이 통합은 아직 하나의 파이프라인으로 엮이지 않았다.

## 다음 파이프라인: 무상태 도구 위에 상태를 쌓기

이번 시도의 병목은 전부 같은 뿌리에서 나왔다. 모델이 무상태이므로 연출의 연속성을 사람이 수작업으로 관리해야 했고, 그 비용이 컷 수에 비례하여 폭발했다. 해결의 방향은 명확하다. **무상태 도구 위에 상태 관리 레이어를 쌓는 것.**

구체적으로는 작업 순서를 바꿔야 한다. 이번에는 풀 퀄리티 이미지를 한 장씩 만들면서 앞으로 나아갔는데, 그러면 "앞뒤 맥락이 비어 보인다 → 채운다 → 또 비어 보인다"의 루프에 빠진다. 풀 퀄리티 이미지의 재생성 비용이 높기 때문이다.

핵심은 스틱맨 수준에서 전체 흐름을 먼저 확정하고, 나중에 퀄리티를 올리는 것이다. 영상 업계에서 프리프로덕션이 존재하는 이유와 같다.

**구조 잡기 — 상태를 텍스트로 정의한다**
1. 클로드 코드가 시놉시스에서 컷을 추출하고 각 컷의 시간·대사·감정 비트를 정의
2. 각 컷에 대해 "직전 컷에서 유지해야 할 상태"를 명시적으로 기록 — 인물 좌우 배치, 소품 위치, 결박 상태, 카메라 방향. 모델이 기억하지 못하는 것을 텍스트가 대신 기억한다
3. gpt-image-2로 스틱맨 수준의 레이아웃을 생성. 구도와 배치만 잡는다
4. 스틱맨 콘티를 이어 붙여 러프 영상으로 만들고, 타이밍과 구도를 검증

![11컷 선화 콘티](/images/library-storyboard/00-stickman-overview.png)
*위 11컷의 구도를 선화 콘티로 변환한 예시. 다음에는 이 단계를 먼저 거친 뒤 풀 퀄리티로 올린다.*

**소재 제작** — 확정된 구조 위에서만 작업한다

5. Grok Voice 등으로 대사 음성을 생성하여 타이밍 기준점 확보
6. 검증된 콘티를 바탕으로 gpt-image-2가 풀 퀄리티 핵심 이미지 생성. 이때 프롬프트에 위 2단계의 상태 기록을 주입

**영상 조립**

7. 클로드 코드가 카메라 무빙·전환 효과·타이밍을 프롬프트로 작성
8. Seedance 2 등 영상 생성 AI로 씬별 동영상 제작
9. 최종 편집 및 결합

스틱맨 단계에서 전체 흐름이 확정되면 풀 퀄리티 단계에서의 재작업을 줄일 수 있고, 상태 기록이 프롬프트에 주입되면 컷 간 일관성이 올라갈 거라 기대한다. 무상태 모델을 바꿀 수는 없으니, 그 바깥에서 상태를 관리하는 수밖에 없다.

## 이 시도에 대해

시놉시스에는 "봉인이 풀리고 빛이 쏟아지는 순간"이라고만 적혀 있다. 이미지가 생기면 결정을 내릴 수 있다. "이 빛은 너무 차갑다", "이 거리는 내가 의도한 것보다 가깝다", "이 표정은 내가 생각한 것보다 낫다." 그 판단의 루프가 돌아가기 시작한다는 것 자체가 이번 시도의 핵심이다. 11컷의 연속성은 불완전하지만, 시각적 결정을 반복적으로 내릴 수 있는 루프가 생겼다.

이 무상태 병목은 이미지 생성에만 국한된 문제가 아니다. 영상 생성 AI도 같은 벽에 부딪히고 있다. Sora, Veo, Kling 같은 양방향 비디오 모델은 이미지 생성의 무상태성이 시간축으로 확장된 것이다 — 과거·현재·미래를 고정된 프롬프트로 동시에 생성한다[^3]. 반면 월드 모델은 각 상태를 이전 상태와 행동으로부터 인과적으로 예측한다[^3].

독립적으로 연구되는 세 월드 모델 프로젝트 — MultiGen[^4], Waypoint[^5], Matrix-Game 3.0[^6] — 에서 흥미로운 공통점이 보인다. 세 논문을 비교 독해한 내 관찰인데, 접근법은 달라도 전제가 같다: **"컨텍스트 윈도우 너머에 지속되는 명시적 상태"가 장기 롤아웃의 공간 일관성에 필수라는 것**. MultiGen은 레벨 맵과 인물 포즈를 모델 바깥의 메모리 모듈에 유지하여, 프레임 히스토리에서 레이아웃을 재추론할 필요를 없앴다[^4].

이번 스토리보드에서 겪은 일이 정확히 그것이다. 컷 7을 만들 때 컷 5의 사슬 위치를 기억하는 건 내가 해야 했다. 위에서 제안한 파이프라인의 2단계 — "직전 컷에서 유지해야 할 상태를 명시적으로 기록" — 가 사실상 이 외부 상태 레이어의 수작업 버전이다. AI 창작 도구의 다음 도약은 개별 생성물의 품질이 아니라, 생성물 사이의 상태를 관리하는 레이어에서 일어날 거라고 생각한다.

[^1]: Lvmin Zhang, Anyi Rao, Maneesh Agrawala, "Adding Conditional Control to Text-to-Image Diffusion Models" — arXiv:2302.05543, 2023. 포즈, 깊이 맵, 엣지 등 조건 입력을 통해 이미지 생성을 제어하는 프레임워크.
[^2]: Hu Ye et al., "IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models" — arXiv:2308.06721, 2023. 이미지 프롬프트를 통해 캐릭터 정체성을 유지하는 어댑터.
[^3]: Odyssey, "Introducing Odyssey-2 Max" — [odyssey.ml](https://odyssey.ml/introducing-odyssey-2-max), 2026. 월드 모델과 양방향 비디오 모델의 구조적 차이, next-state 예측에서 물리가 창발하는 메커니즘을 설명한다.
[^4]: Gómez et al., "MultiGen: Zero-shot Multi-player Game Generation with Multi-agent LLM-augmented Diffusion" — [arXiv:2603.06679](https://arxiv.org/abs/2603.06679), 2026. 외부 메모리 모듈(레벨 맵 + 포즈)로 장기 롤아웃의 공간 일관성을 유지하는 인터랙티브 월드 모델.
[^5]: Overworld, "Waypoint 1.5" — [over.world](https://over.world/blog/waypoint-1-5), 2026. 소비자 하드웨어에서 실시간 실행 가능한 인터랙티브 세계 모델. 영상이 아닌 세계를 만든다.
[^6]: Skywork AI, "Matrix-Game 3.0" — [arXiv:2604.08995](https://arxiv.org/abs/2604.08995), 2026. 잠재벡터 카메라 인식 메모리 검색 기반 인터랙티브 월드 모델. 720p 실시간 40FPS.
