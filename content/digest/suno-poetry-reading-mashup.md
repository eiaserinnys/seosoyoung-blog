---
title: "Suno로 만드는 포에트리 리딩"
date: 2026-06-12T00:00:00+09:00
tags: ["AI", "창작·미디어", "음악 생성", "Suno", "ElevenLabs"]
categories: ["창작과 문화"]
summary: "Suno 단독으로는 일본어 포에트리 리딩 곡을 만들 수 없었던 크리에이터가, ElevenLabs로 낭독 트랙을 따로 생성한 뒤 Suno v5의 Mashup 기능으로 음악 트랙과 융합해 문제를 해결한 제작기."
ShowToc: true
TocOpen: false
cover:
  image: "/images/suno-poetry-reading-mashup/suno-mashup-setting.png"
images:
  - "/images/suno-poetry-reading-mashup/suno-mashup-setting.png"
---

## 3줄 요약

1. 일본의 음악 크리에이터 tapehead.lab이 2026년 6월 note에 올린 제작기로, Suno로 포에트리 리딩(낭독 퍼포먼스) 곡을 만드는 우회 방법을 다룬다.
2. Suno는 모든 출력을 음악으로 성립시키려는 방향으로 균형을 잡기 때문에 `[spoken word]` 메타태그를 써도 완전한 낭독이 나오지 않고, 일본어 인토네이션도 약하다는 한계가 있다.
3. 해결책은 분업이다. ElevenLabs로 낭독 음성 트랙을 생성하고, Suno로 음악 트랙을 따로 만든 뒤, Suno v5의 Mashup 기능으로 두 트랙을 융합하면 낭독의 목소리와 인토네이션을 유지한 채 음악에 얹힌 결과물이 나온다.

## 이번 글에서 다루는 곡

완성곡은 "ゴミみたいなマスターピース(쓰레기 같은 마스터피스)"라는 제목의 포에트리 리딩 곡이다.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/uFvqL6bJprE" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen title="ゴミみたいなマスターピース (music video)"></iframe>

## Suno 단독으로는 안 되는 이유

저자가 목표한 것은 포에트리 리딩, 즉 시나 말을 비트에 얹어 감정을 실어 전달하는 낭독 퍼포먼스다. 낭독 같은 목소리를 자연스럽게 음악에 얹어 "무감정 속에서 솟아오르는 감정" 같은 표현을 하고 싶었다고 밝힌다.

그런데 이것을 Suno에서 구현하기가 매우 어려웠다. 저자가 정리한 장벽은 두 가지다.

- **음악 우선 균형**: `[spoken word]` 같은 메타태그가 있긴 하지만, Suno는 기본적으로 출력을 음악으로 성립시키는 쪽으로 균형을 잡는다. 그래서 낭독이 되지 않는다. 반대로 완전한 낭독을 노리고 강하게 유도하면 음악적 연출이 사라진다.
- **일본어 인토네이션 취약**: Suno의 일본어 억양 처리가 약해서, 메타태그와 프롬프트를 아무리 손봐도 만족스러운 포에트리 리딩이 나오지 않았다.

원문에는 방향을 잡지 못하던 시기의 중간 출력 두 개가 실려 있다.

<iframe width="100%" height="275" src="https://note.com/embed/sounds/e66f1ff71dc8403885b4ed3048c8b4da" frameborder="0" scrolling="no" style="border:none;" title="미완 출력 1"></iframe>
<iframe width="100%" height="275" src="https://note.com/embed/sounds/a67332bf832b91705bd738b38a3bc47f" frameborder="0" scrolling="no" style="border:none;" title="미완 출력 2"></iframe>

## 전환점: Suno v5의 Mashup

방침을 바꾼 계기는 Suno v5부터 탑재된 **Mashup** 기능이다. 원문이 인용한 설명에 따르면, Mashup은 자신이 만든 서로 다른 두 곡을 조합해 완전히 새로운 한 곡을 자동 생성하는 기능이다. 두 곡을 단순히 겹쳐 재생하는 DJ식 매시업과 달리, AI가 양쪽 곡의 멜로디·템포·분위기·보컬 요소를 융합해 처음부터 새 곡 구조를 만들어 낸다.

<iframe width="100%" height="315" src="https://www.youtube.com/embed/_iytIBY_EaA" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen title="Suno Mashup: Combine Songs Like Never Before"></iframe>

저자의 가설은 단순했다. "보컬 낭독 트랙을 따로 준비해서 음악과 조합하면 되지 않을까?" 그리고 본인 표현으로는, 시험해 보니 거짓말처럼 잘 됐다.

## 워크플로우: ElevenLabs 낭독 + Suno 음악 → Mashup

제작 절차는 세 단계다.

**1단계 — 낭독 트랙 생성 (ElevenLabs).** 텍스트 원고를 넘기면 다양한 캐릭터 음성 중에서 골라 내레이션 보이스를 생성할 수 있다. 저자는 출력이 매우 자연스러웠다고 평가한다.

![ElevenLabs UI](/images/suno-poetry-reading-mashup/elevenlabs-ui.png)

<iframe width="100%" height="275" src="https://note.com/embed/sounds/e2a5028f41856a58c7da6badef421ccd" frameborder="0" scrolling="no" style="border:none;" title="ElevenLabs로 생성한 낭독 트랙"></iframe>

**2단계 — 음악 트랙 생성 (Suno).** Mashup에 넣을 음악 트랙을 평소처럼 Suno로 생성한다.

<iframe width="100%" height="275" src="https://note.com/embed/sounds/d229b57936c29176b55f8ff42b7bc378" frameborder="0" scrolling="no" style="border:none;" title="Suno로 생성한 음악 트랙"></iframe>

**3단계 — 두 트랙을 Mashup으로 융합.** ElevenLabs에서 만든 낭독 파일은 Upload Audio로 Suno에 올려서 지정한다. 이때 낭독의 가사를 Lyrics 칸에도 넣어 두면 출력이 안정된다.

![Suno Mashup 지정 화면](/images/suno-poetry-reading-mashup/suno-mashup-setting.png)

두 트랙을 Mashup한 결과가 아래다.

<iframe width="100%" height="275" src="https://note.com/embed/sounds/85a0def9401487cfd1575074256aab30" frameborder="0" scrolling="no" style="border:none;" title="두 트랙을 Mashup한 결과"></iframe>

결과물에 대해 저자는 낭독 트랙의 보이스와 인토네이션을 유지하면서 곡에 맞춰 정돈해 준다는 점을 핵심 성과로 든다. 여기까지 되면 나머지는 평소의 Suno 작업과 같다. Mashup 단계에서 Styles와 Lyrics의 프롬프트·메타태그를 조정해 취향의 음악으로 마무리한다.

## 마무리: v5.5의 안정성과 편집 조합

Mashup 자체는 v5.5로 수행했다. v5.5는 "출력이 안정적이라 재미가 없다"는 평을 듣곤 하는데, 저자는 거꾸로 그 안정성 덕분에 여러 출력 후보에서 좋은 부분만 골라 편집해도 곡이 성립한다는 점을 장점으로 꼽는다.

이번 곡도 4개의 출력과 STEM(분리 트랙)을 Premiere에서 편집해 조합했다.

![4곡과 STEM을 Premiere에서 편집](/images/suno-poetry-reading-mashup/premiere-editing.png)

저자는 포에트리 리딩에 국한되지 않고 Mashup에 다양한 활용법이 있을 것이라는 전망으로 글을 맺는다.

## 가장 흥미로운 지점

이 글의 요점은 생성 모델의 한계를 프롬프트로 돌파하려 하지 않고, **모델 바깥에서 분업 구조를 설계해 우회**했다는 데 있다. Suno가 낭독을 못 하는 것은 프롬프트가 부족해서가 아니고 모델 자체가 "음악으로 성립시키는" 방향으로 균형을 잡도록 만들어졌기 때문이다. 저자는 그 균형 자체와 싸우는 대신, 낭독은 TTS 전문 모델(ElevenLabs)에 맡기고 Suno에는 융합과 음악적 연출만 시켰다. 각 모델이 잘하는 것만 시키고 접합부를 Mashup이라는 공식 기능으로 처리한 것이다.

또 하나, v5.5의 "안정적이라 재미없다"는 세간의 평을 편집 관점에서 뒤집는 시각도 눈에 띈다. 출력이 안정적이면 후보 간 편차가 작아 여러 출력을 잘라 붙여도 이질감 없이 성립한다. 생성 결과를 완성품으로 보는 사람에게는 단점이, 생성 결과를 편집 소재로 보는 사람에게는 장점이 된다.

## 출처

저자: tapehead.lab, note 게시일 2026년 6월 10일.
본문의 오디오는 원문 note 임베드 플레이어를, 영상은 YouTube를 인용했다.

원문: <https://note.com/tapehead/n/nbe9758abf186>
