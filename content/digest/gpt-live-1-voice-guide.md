---
title: "GPT-Live-1 음성 가이드"
date: 2026-09-13T12:00:00+09:00
tags: ["OpenAI", "음성 AI", "AI 비용", "AI 에이전트"]
categories: ["에이전트와 코딩"]
summary: "GPT-Live-1은 듣는 동안 동시에 말하는 실시간 음성 모델이다. 기본 음성은 22종이고, 자격을 받으면 자기 목소리도 등록할 수 있다. 요금은 토큰으로 매기지 않고 세션이 열려 있는 시간으로 매기며, 아무도 말하지 않는 침묵 구간도 똑같이 과금된다. 2026년 9월 13일 기준 공식 문서로 확인한 내용을 정리했다."
ShowToc: true
TocOpen: true
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/gpt-live-1-voice-guide/01-cover.png"
  alt: "헤드폰을 쓴 치비 서소영이 나란히 늘어선 작은 마이크 가운데 하나에 손을 뻗고, 다른 손에는 초침이 도는 회중시계를 들고 있다"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/gpt-live-1-voice-guide/01-cover.png"
sidenotes: true
---

## 3줄 요약

1. GPT-Live-1은 OpenAI가 2026년 7월 8일 ChatGPT에, 9월 10일 API에 내놓은 실시간 음성 모델이다. 듣기와 말하기를 동시에 하고, 깊은 추론은 뒤에 있는 다른 모델에 넘긴 채로 대화를 계속 이어 간다.
2. 세션에서 고를 수 있는 기본 음성은 **22종**이다. 이 가운데 12종은 9월 10일 API 공지가 직접 "New voice options"라고 부른 신규 음성이고, 나머지 10종은 Realtime API 시절부터 쓰이던 것들이다. 조직이 자격을 받으면 자기 목소리를 등록해 쓸 수도 있다.
3. 요금은 토큰이 아니라 **세션이 열려 있던 시간**으로 매겨진다. 분당 0.05달러이고 초 단위로 정산한다. 한 시간을 계속 열어 두면 음성 세션 요금만 3달러이고, 여기에 백엔드 모델 요금이 따로 붙는다. 서로 말하지 않고 있는 시간도 똑같이 과금된다.

## GPT-Live-1이 무엇인가

전화 통화를 떠올리면 된다. 상대가 말하는 중에도 나는 "응", "그렇구나" 하고 끼어들 수 있고, 내가 말을 하다가 상대가 끼어들면 멈춘다. 사람끼리는 당연한 이 일이 음성 AI에서는 오랫동안 어려운 문제였다.

이전 방식은 두 갈래였다. 하나는 세 모델을 사슬처럼 잇는 방식이다. 말을 받아 적는 모델, 답을 만드는 모델, 그 답을 소리로 바꾸는 모델을 차례로 통과시킨다. 단계마다 정보가 새고 응답이 느렸다. 다른 하나는 하나의 모델이 음성을 직접 다루되 말할 차례를 나눠 쓰는 방식이다. 내가 말을 멈춰야 상대가 답을 시작한다. 침묵으로 차례 끝을 판단하다 보니, 잠깐 생각하려고 멈추면 말을 끊고 들어왔다.

GPT-Live는 이 구조를 바꿨다. 입력을 계속 받으면서 동시에 출력을 만든다. OpenAI는 이 모델이 초당 여러 번 결정을 내린다고 설명한다. 말할지, 계속 들을지, 멈출지, 끼어들지, 도구를 부를지를 그때그때 고른다.[^1]

두 번째 변화가 더 실용적이다. 깊은 작업을 음성 모델에서 떼어 냈다. 검색이 필요하거나 복잡한 추론이 필요한 질문이 오면, GPT-Live는 그 일을 뒤에 있는 다른 모델에게 넘긴다. 이것을 위임(delegation)이라고 부른다. 위임한 일이 도는 동안에도 대화는 끊기지 않는다. 사용자는 "지금 주문 상태를 확인하고 있어요"라는 말을 들으면서 다른 이야기를 덧붙일 수 있다.[^2]

어학 앱 Speak는 초기 평가 결과를 이렇게 전했다. 학습자가 생각하느라 잠깐 멈추는 구간이 있는데, 그때 모델이 끼어드는 일이 이전 턴 기반 시스템보다 80% 가까이 줄었다고 한다. 의료 예약 서비스를 만드는 한 회사는 사슬형 구조를 GPT-Live-1으로 바꾸면서 코드베이스가 80% 줄고 2만 3천 줄이 사라졌다고 했다.[^3]

ChatGPT 쪽에서는 7월 8일부터 Go, Plus, Pro 사용자의 기본 음성 모델이 GPT-Live-1이고, 무료 사용자는 GPT-Live-1 mini를 쓴다. API에는 9월 10일에 `gpt-live-1` 하나만 공개됐다. 2026년 9월 13일 기준 API 모델 목록과 가격표 어디에도 mini 변형은 없다.[^4]

## 어디서 들어 볼 수 있는가

공식 미리듣기는 **API 출시 공지 페이지 안에 들어 있다.** 「New voice options」 절의 "Listen to the new voices" 탭을 누르면 신규 12종을 하나씩 재생할 수 있다.

- 공식 페이지: <https://openai.com/index/introducing-gpt-live-1-in-the-api/>

아래 재생기는 그 페이지가 쓰는 것과 같은 OpenAI 공식 샘플 파일을 그대로 가리킨다. 파일을 이 블로그로 옮겨 오지 않았고, 재생을 누르면 OpenAI 자산 서버에서 바로 내려받는다. 링크가 바뀌면 위 공식 페이지에서 들으면 된다.

<div>
<p><strong>Quartz</strong>, 호주 영어 계열 (en-AU)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/1PFbTZw8zqwIUUkcRicjRX/4bf434689dd541cc9db0c97fe55b0198/09-quartz-en-AU.wav"></audio></p>
<p><strong>Ripple</strong>, 호주 영어 계열 (en-AU)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/76qMZnK0JWBzeTvQ8K0bIH/b47969e72b1caf496b98f1678a029150/01-ripple-en-AU.wav"></audio></p>
<p><strong>Vesper</strong>, 영국 영어 계열 (en-GB)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/1NMR9b8Ne4v2Ud81l1odbi/bdd651671ece12ac7ee908f5b9377f5d/02-vesper-en-GB.wav"></audio></p>
<p><strong>Willow</strong>, 아일랜드 영어 계열 (en-IE)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/5UkWYwYetfl4KObT2EWa1g/6c6006064c71993fe904dcae405d6242/03-willow-en-IE.wav"></audio></p>
<p><strong>Stone</strong>, 아일랜드 영어 계열 (en-IE)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/7ki21O7xR0neO1pVbgqjei/9867fcf088fedb813f248b062ada43fa/04-stone-en-IE.wav"></audio></p>
<p><strong>Meridian</strong>, 북미 영어 계열 (en-US)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/5Yez0vxl4ZJwmyCLr7V54u/754bd2814443fc398e5923dc1c95442b/05-meridian-en-US.wav"></audio></p>
<p><strong>Gleam</strong>, 북미 영어 계열 (en-US)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/4LtEN6YDjAZe1ToQHIzI72/c278fbd258dd560695ee5d77bdf893d8/06-gleam-en-US.wav"></audio></p>
<p><strong>Bossa</strong>, 브라질 포르투갈어 계열 (pt-BR)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/5s9AVTrpCSFH4Ig44aou94/89217d80051656d6a33576579b3d1e3f/07-bossa-pt-BR.wav"></audio></p>
<p><strong>Tempo</strong>, 브라질 포르투갈어 계열 (pt-BR)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/2R2C0kUh8R5R76SvvWZd5J/6c50f1bb7f6c9c9cae42f16b2d7de240/08-tempo-pt-BR.wav"></audio></p>
<p><strong>Beacon</strong>, 필리핀 영어 계열 (en-PH)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/503aEoumNzR2tdEmDCO5cs/72697c87ff192da198b580388e93a9eb/11-beacon-en-PH.wav"></audio></p>
<p><strong>Delta</strong>, 미국 남부 영어 계열 (en-US)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/1xp2o3XyW8DzgoueK7SN3Z/95771e125ac40ee30ea56fd31df6c9d9/12-delta-en-US.wav"></audio></p>
<p><strong>Cinder</strong>, 미국 남부 영어 계열 (en-US)<br>
<audio controls preload="none" src="https://assets.ctfassets.net/kftzwdyauwt9/VmkCwriUTcdTqu1s5ndIV/9d80f316e7a88f90f91ed8046cb1860b/13-cinder-en-US.wav"></audio></p>
</div>

나머지 10종에는 GPT-Live 전용 공식 샘플이 없다. openai.fm은 텍스트 음성 변환 모델 데모라고 스스로 밝히고 있어 GPT-Live 음성을 그대로 들려주는지 확인하지 못했다. 결국 이 10종은 직접 세션을 열어 들어 보는 수밖에 없었다.

## 기본 음성 22종

언론 보도는 신규 12종만 나열하고, 커뮤니티 글은 22종이라고 하면서 근거를 밝힌 곳이 없었다. 그래서 공식 스펙을 직접 확인했다.

`gpt-live-1` 세션의 음성 필드가 받는 문자열은 세 곳에서 똑같이 22개다.

- `openai/openai-openapi`의 `openapi.yaml`, 스키마 `LiveInitialSessionAudioOutputParam`의 `enum`
- `openai/openai-node`의 `src/resources/live/live.ts`, `BuiltInVoice` 타입
- `openai/openai-python`의 `src/openai/types/live/built_in_voice.py`

세 파일의 목록이 문자 그대로 일치했다. **22종이라는 숫자는 맞다.**

<img src="https://img.seosoyoung.eiaserinnys.me/images/gpt-live-1-voice-guide/02-voices.png" alt="이름표와 깃발이 달린 마이크들이 줄지어 서 있고 치비 서소영이 그중 하나에 귀를 바짝 대고 듣는다">

| 음성 | 공지에서의 분류 | 공식 샘플 로케일 | 비고 |
| --- | --- | --- | --- |
| `alloy` | 이전부터 있던 음성 | 없음 | |
| `ash` | 이전부터 있던 음성 | 없음 | |
| `ballad` | 이전부터 있던 음성 | 없음 | |
| `beacon` | 신규 | en-PH | 필리핀 영어 계열 |
| `bossa` | 신규 | pt-BR | 브라질 포르투갈어 계열 |
| `cedar` | 이전부터 있던 음성 | 없음 | 품질 권장 음성 |
| `cinder` | 신규 | en-US | 미국 남부 영어 계열 |
| `coral` | 이전부터 있던 음성 | 없음 | |
| `delta` | 신규 | en-US | 미국 남부 영어 계열 |
| `echo` | 이전부터 있던 음성 | 없음 | |
| `gleam` | 신규 | en-US | 북미 영어 계열 |
| `marin` | 이전부터 있던 음성 | 없음 | 품질 권장 음성 |
| `meridian` | 신규 | en-US | 북미 영어 계열 |
| `quartz` | 신규 | en-AU | 호주 영어 계열 |
| `ripple` | 신규 | en-AU | 호주 영어 계열 |
| `sage` | 이전부터 있던 음성 | 없음 | |
| `shimmer` | 이전부터 있던 음성 | 없음 | |
| `stone` | 신규 | en-IE | 아일랜드 영어 계열 |
| `tempo` | 신규 | pt-BR | 브라질 포르투갈어 계열 |
| `verse` | 이전부터 있던 음성 | 없음 | |
| `vesper` | 신규 | en-GB | 영국 영어 계열 |
| `willow` | 신규 | en-IE | 아일랜드 영어 계열 |

### 신규와 기존이라는 구분은 절반만 공식이다

이 분류에는 단서가 붙는다. OpenAI는 12종을 "New voice options"라는 절 제목으로 분명히 묶었고, 본문에서도 "작은 실시간 음성 집합에서 더 넓은 선택지로 확장한다"고 적었다. 이쪽은 공식 분류가 맞다.

그런데 나머지 10종을 "기존(existing)"이라고 부르는 공식 문서는 찾지 못했다. 이 10종은 Realtime API 가이드의 "Current voice options" 목록과 같은 집합이다. 그래서 사람들이 자연스럽게 기존으로 묶어 부른다. 나도 위 표에서 그렇게 적었지만, 그것은 두 문서를 대조해 얻은 추론이지 OpenAI가 붙인 이름표가 아니다.

등급을 매기는 공식 표현도 Live 문서에는 없다. 텍스트 음성 변환 가이드와 Realtime 가이드에 "최상의 품질을 원하면 marin이나 cedar를 권한다"는 문구가 있을 뿐이고, 이것도 GPT-Live 전용 서술은 아니다.

### 음성 이름이 억양을 보장하지는 않는다

위 표의 로케일 열은 OpenAI가 공개한 샘플 파일 이름에서 나온 것이다. 파일 이름에 `en-AU`, `pt-BR` 같은 태그가 들어 있어서 각 음성이 어느 말씨로 녹음됐는지 알 수 있다.

그런데 GPT-Live 프롬프팅 가이드는 정반대 방향의 문장을 하나 적어 두었다.

> A voice choice does not guarantee a regional accent.

음성을 고른다고 그 지역 억양이 나온다는 보장이 없다는 뜻이다. 실제로 커스텀 음성 문서는 억양을 원하면 세션 지시문에 직접 적으라고 안내한다. "Speak British English" 또는 "Speak Irish English"처럼 쓰면 된다. 이름만 고르고 끝낼 일은 아닌 셈이다. 원하는 말씨가 있으면 지시문에도 함께 적어야 한다.

## 내 목소리를 등록하는 법

커스텀 음성은 아무나 쓸 수 없다. 공식 문서의 첫 제한이 이것이다.

> Custom voices are limited to eligible customers.

자격을 받은 조직만 쓸 수 있고, 영업팀을 통해 문의해야 한다. 승인되면 대시보드의 Audio 항목 아래에 Voices 탭이 생긴다. 그래도 실제 생성은 지금까지 API 요청으로만 가능하다.

<img src="https://img.seosoyoung.eiaserinnys.me/images/gpt-live-1-voice-guide/03-custom-voice.png" alt="치비 서소영이 펼친 두루마리를 소리 내어 읽고 그 목소리가 앞의 작은 상자로 들어가며, 옆에는 모래가 얼마 남지 않은 모래시계가 놓여 있다">

### 준비물과 한도

| 항목 | 값 |
| --- | --- |
| 조직당 음성 개수 | 최대 20개 |
| 오디오 샘플 길이 | 30초 이하 |
| 업로드 한 건 크기 | 10 MiB 이하 |
| 허용 포맷 | `mpeg`, `wav`, `ogg`, `aac`, `flac`, `webm`, `mp4` |
| 필요한 녹음 | 동의 녹음 1개, 샘플 녹음 1개 |
| 필요한 권한 | 동의 문구 조회와 음성 사용은 `api.voices.read`, 동의와 음성 생성은 `api.voices.write` |

두 녹음은 **같은 사람의 목소리여야 한다.** 다르면 거부된다. 프로젝트 범위의 API 키를 쓰고, 모든 요청도 같은 프로젝트에서 보내야 한다. 키는 서버에 두고 브라우저로 내보내면 안 된다.

샘플 조건은 GPT-Live 절에 따로 나와 있다. 실제 발화가 5초 이상이어야 하고, 전사된 텍스트 토큰이 15개 이상이어야 한다. 침묵은 세지 않는다. 문서는 완전한 문장 여러 개가 담긴 10초에서 30초 사이의 녹음을 권한다.

녹음 품질에 대한 조언도 구체적이다. 문서는 조용하고 울림이 적은 공간에서 전문 XLR 마이크를 쓰고, 팝 필터를 사이에 둔 채 마이크와의 거리를 7\~8인치로 일정하게 유지하라고 권한다. 모델이 톤과 속도, 활기, 쉼, 버릇을 그대로 베끼므로 원하는 목소리를 그대로 녹음하라는 문장도 있다. 작은 차이가 결과를 바꾸니 여러 번 시도해 고르라고 권한다.

### 1단계. 동의 문구를 확인한다

동의 녹음에는 **정해진 문장만** 담겨야 한다. 대본에서 벗어나면 실패한다. 현재 지원되는 문구 목록은 API로 조회할 수 있다.

```bash
curl https://api.openai.com/v1/audio/consent_phrases \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

한국어(`ko`) 문구는 2026년 9월 13일 기준 다음과 같다. 문서에서 그대로 옮겼다.

> 나는 이 음성의 소유자이며 OpenAI가 이 음성을 사용하여 음성 합성 모델을 생성할 것을 허용합니다.

문서에는 16개 언어의 문구가 표로 실려 있다. 독일어, 영어, 스페인어, 프랑스어, 힌디어, 인도네시아어, 이탈리아어, 일본어, 한국어, 네덜란드어, 폴란드어, 포르투갈어, 러시아어, 우크라이나어, 베트남어, 중국어가 들어 있다. 영어 문구는 "I am the owner of this voice and I consent to OpenAI using this voice to create a synthetic voice model."이다.

### 2단계. 동의 녹음을 올린다

```bash
curl https://api.openai.com/v1/audio/voice_consents \
  -X POST \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "name=test_consent" \
  -F "language=ko" \
  -F "recording=@consent_recording.wav;type=audio/x-wav"
```

성공하면 `cons_`로 시작하는 동의 ID를 돌려준다. 이 동의는 같은 성우가 여러 번 시도할 때 다시 쓸 수 있다. 음성을 만들 때마다 새로 녹음하지 않아도 된다.

### 3단계. 음성을 만든다

동의 ID와 샘플 녹음을 함께 넘긴다.

```bash
curl https://api.openai.com/v1/audio/voices \
  -X POST \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "name=test_voice" \
  -F "audio_sample=@audio_sample_recording.wav;type=audio/x-wav" \
  -F "consent=cons_123abc"
```

성공하면 `voice_`로 시작하는 음성 ID가 나온다. 대시보드 Audio 탭에도 올라온다.

브라우저 녹음기를 쓰면 걸리는 함정이 따로 있다. 브라우저 녹음기는 녹음 파일에 `audio/webm;codecs=opus`라는 MIME 타입을 붙인다. 업로드 엔드포인트는 이 타입을 거부한다. 오디오 바이트는 그대로 두고 MIME 타입만 `audio/webm`으로 바꿔 올려야 한다. 전사 토큰을 직접 올리지 말고, 디코더를 지정하지 말고, 사용자 정의 헤더도 붙이지 말라는 지시가 함께 나와 있다. 참조 전사는 서비스가 알아서 뽑는다.

### 4단계. 세션에 붙인다

세션을 만들 때 음성을 지정한다. **기본 음성과 커스텀 음성은 표기 방식이 다르다.**

- 기본 음성은 문자열로 쓴다: `"marin"`
- 커스텀 음성은 객체로 쓴다: `{ "id": "voice_123" }`

`gpt-live-1`은 영어 억양의 커스텀 음성을 지원한다. 억양을 쓰려면 세션 지시문에도 적어야 한다.

```json
{
  "model": "gpt-live-1",
  "instructions": "You are a helpful voice assistant. Speak British English.",
  "audio": { "output": { "voice": { "id": "voice_123" } } }
}
```

WebRTC로 연결할 때는 신뢰할 수 있는 서버가 이 설정을 JSON `session` 필드에 넣어 `transport`와 함께 보낸다. Live 엔드포인트는 JSON만 받는다. multipart 요청이나 그대로 보낸 SDP는 거부한다. 응답에서 세션 ID는 `session.id`에, SDP 응답은 `transport.sdp`에 들어 있다.

WebSocket으로 붙을 때는 첫 `session.start` 이벤트에 같은 설정을 넣는다. 쿼리 파라미터 없이 접속하고, `session.started`를 받은 뒤에 오디오를 흘려보낸다. 오디오는 `session.input_audio.append`로 보낸다. `session.close`를 보낸 뒤에도 `session.closed`가 최종 사용량을 줄 때까지 계속 받아야 한다.

### 주의할 것들

- **세션이 시작된 뒤에는 출력 음성을 바꿀 수 없다.** 다른 음성을 쓰려면 세션을 새로 열어야 한다.
- 삭제되거나 회수된 음성, 다른 프로젝트의 동의, 커스텀 음성 접근 권한 누락은 모두 `404`로 나타날 수 있다. 오류 코드만 보고 원인을 짐작하기 어렵다는 뜻이다.
- 잘못된 오디오, 화자 불일치, 프로젝트 범위가 아닌 키는 거부된다.
- 텍스트 음성 변환 보충 약관이 따로 적용된다.
- ChatGPT 쪽 GPT-Live는 정해진 음성만 쓰고 실제 사람의 목소리를 흉내 내지 못하도록 안전장치를 두었다고 밝혔다. 커스텀 음성은 API에서 자격을 받은 조직에만 열리는 별도의 길이다.

## 그래서 얼마 드는가

널리 퍼진 전제를 하나 바로잡고 시작하겠다. **GPT-Live-1은 음성 토큰으로 과금하지 않는다.**

가격표의 GPT-Live 항목은 단 두 칸이다.

| 모델 | 분당 가격 |
| --- | --- |
| `gpt-live-1` | 0.05달러 |

설명 문장은 이렇다.

> GPT-Live 1 voice sessions are billed per second, without rounding up to a whole minute. Backend model and tool usage is charged separately.

초 단위로 과금하고 분 단위로 올림하지 않는다. 오디오 입력 토큰이나 출력 토큰이라는 항목 자체가 없다. 토큰으로 매기는 쪽은 Realtime API 계열이고, 그쪽은 완전히 다른 요금표를 쓴다. 뒤에서 비교하겠다.

<img src="https://img.seosoyoung.eiaserinnys.me/images/gpt-live-1-voice-guide/04-cost.png" alt="치비 서소영과 맞은편 빈 의자 사이에 아무 말풍선도 없는데 옆의 큰 모래시계는 계속 흐르고 아래 접시에 동전이 쌓인다">

### 무엇이 과금 시간에 들어가는가

비용 최적화 문서가 이 부분을 분명히 적어 두었다.

> Active session time includes time when the user speaks, the assistant speaks, both are silent, or the backend is working.

사용자가 말하는 시간, 어시스턴트가 말하는 시간, **양쪽 다 침묵인 시간**, 백엔드가 일하는 시간이 모두 들어간다. 마이크를 음소거해도 세션은 닫히지 않는다. 세션이 열려 있는 한 요금은 흐른다.

이 문장에서 두 가지가 따라 나온다.

첫째, **입력과 출력의 발화 비율은 음성 세션 요금을 전혀 바꾸지 못한다.** 내가 90% 말하든 모델이 90% 말하든, 세션이 10분 열려 있었으면 똑같이 0.5달러다. 발화 비율이 바꾸는 것은 백엔드 쪽이다. 사용자가 요청을 많이 던지면 위임이 늘고 백엔드 토큰이 늘어난다.

둘째, **침묵은 음성 세션 요금을 100% 그대로 먹는다.** 대화가 비어 있는 구간을 줄이는 방법은 하나뿐이다. 세션을 닫는 것이다. 문서도 같은 결론을 적었다. 유휴 상태인 세션을 1분 일찍 닫으면 0.05달러를 아낀다는 문장이 있다.

WebRTC로 세션을 만들 때 한 가지가 더 붙는다. `POST /v1/live/sessions` 요청은 세션이 초기화되는 동안 **15초 분량의 음성 시간을 먼저 청구한다.** 세션이 실제로 돌기 시작하면 그 금액은 이후 시간 요금에서 상쇄된다. 그러니 이미 돌기 시작한 세션에 15초를 더 얹어 계산하면 안 된다. 반대로, 사용자가 말을 시작하기도 전에 세션을 만들어 두었다가 버리는 설계라면 그 15초가 그대로 비용이 된다.

### 공식 계산식

문서가 계산식을 그대로 제시한다.

> Total cost = (billable voice seconds ÷ 60 × voice rate per minute) + backend costs

문서의 예시는 90초 세션이다. 90 ÷ 60 × 0.05 = 0.075달러. 백엔드 모델과 도구 비용이 0.02달러면 대화 하나가 0.095달러다.

### 백엔드 요금표

위임을 받는 모델은 평범한 텍스트 요금으로 따로 과금된다. 2026년 9월 13일 기준, 표준 처리의 100만 토큰당 가격이다.

| 모델 | 입력 | 캐시된 입력 | 캐시 쓰기 | 출력 |
| --- | --- | --- | --- | --- |
| `gpt-6-astra` | 10.00달러 | 1.00달러 | 12.50달러 | 50.00달러 |
| `gpt-5.6-sol` | 4.00달러 | 0.40달러 | 5.00달러 | 20.00달러 |
| `gpt-5.6-terra` | 2.00달러 | 0.20달러 | 2.50달러 | 12.00달러 |
| `gpt-5.6-luna` | 0.20달러 | 0.02달러 | 0.25달러 | 1.20달러 |

캐시된 입력은 입력 가격의 10분의 1이다. 네 모델 모두 같은 비율이다. 반대로 캐시에 처음 쓸 때는 입력 요금의 1.25배가 붙는다. 재사용할 지시문과 도구 정의를 프롬프트 앞쪽에 고정해 두라는 조언이 여기서 나온다. 한 번 쓰고 마는 내용을 캐시 구간에 넣으면 손해다.

가격표를 그대로 믿기 전에 확인할 것이 둘 있다. `gpt-5.6-sol`의 위 가격은 프로모션가다. 적어도 2026년 11월 21일까지 유지된다고 나와 있다. `gpt-6-astra`는 입력이 27만 2천 토큰을 넘어서면 그 요청 전체의 요금이 달라진다. 입력과 캐시 요금은 2배, 출력 요금은 1.5배가 붙는다. 긴 대화를 통째로 백엔드에 넘기는 설계라면 이 선을 넘는지 확인해야 한다.

웹 검색을 쓰면 호출 1천 건당 10달러가 붙고, 검색해 온 내용이 프롬프트에 들어가면서 그만큼의 토큰 요금도 따로 든다.

### 한 시간이면 얼마인가

음성 세션 요금만 보면 답이 하나로 떨어진다. 60분에 0.05달러를 곱하면 **3.00달러**다. 여기까지는 가정이 필요 없다.

문제는 백엔드다. 이쪽은 위임이 몇 번 일어나는지, 한 번에 몇 토큰이 오가는지에 따라 자릿수가 달라진다. 그래서 단일 숫자 대신 가정을 밝힌 세 가지 경우를 계산했다. 아래 수치는 모두 내가 세운 가정이며, 공식 수치가 아니다. 계산식을 함께 적었으니 각자의 사용량으로 바꿔 다시 계산하면 된다.

| 가정 | A 가벼운 잡담 | B 업무 상담 | C 추론 중심 |
| --- | --- | --- | --- |
| 백엔드 모델 | `gpt-5.6-luna` | `gpt-5.6-terra` | `gpt-6-astra` |
| 시간당 위임 횟수 | 12회 | 60회 | 90회 |
| 위임당 새 입력 토큰 | 600 | 1,500 | 2,400 |
| 위임당 캐시 적중 토큰 | 2,400 | 4,500 | 5,600 |
| 위임당 출력 토큰 | 200 | 400 | 1,000 |
| 웹 검색 | 없음 | 없음 | 10회 |

계산은 이렇게 한다. 새 입력은 (횟수 × 토큰 ÷ 100만 × 입력 단가), 캐시 적중은 같은 식에 캐시 단가, 출력도 같은 식에 출력 단가를 쓴다. B의 경우를 펼쳐 보면 이렇다.

- 새 입력: 60 × 1,500 ÷ 1,000,000 × 2.00달러 = 0.180달러
- 캐시 적중: 60 × 4,500 ÷ 1,000,000 × 0.20달러 = 0.054달러
- 출력: 60 × 400 ÷ 1,000,000 × 12.00달러 = 0.288달러
- 백엔드 합계 0.522달러, 음성 3.000달러, 총 **3.522달러**

세 경우의 결과를 모으면 이렇다.

| 사용 시간 | A 가벼운 잡담 | B 업무 상담 | C 추론 중심 |
| --- | --- | --- | --- |
| 1시간 | 3.00달러 (약 4,035원) | 3.52달러 (약 4,729원) | 10.26달러 (약 13,782원) |
| 8시간 | 24.04달러 (약 32,280원) | 28.18달러 (약 37,834원) | 82.11달러 (약 110,259원) |
| 24시간 | 72.12달러 (약 96,839원) | 84.53달러 (약 113,503원) | 246.34달러 (약 330,778원) |

원화는 1달러를 1,342.79원으로 환산했다. 2026년 9월 11일 금요일 유럽중앙은행 기준환율이다. 이 글의 기준일인 9월 13일은 일요일이라 9월 11일이 가장 최근 영업일이다.

세 열을 나란히 놓으면 음성 세션 요금의 성격이 드러난다. A와 B의 차이는 시간이 늘어도 크지 않다. 백엔드가 워낙 싸서 음성 요금 3달러가 거의 전부다. C에서는 순서가 뒤집힌다. 한 시간에 백엔드만 7.26달러가 나가서 음성 요금을 두 배 넘게 앞지른다.

### 켜 두는 것과 쓰는 것은 다르다

가장 비싼 실수가 이 지점에서 나온다. 세션을 24시간 열어 두고 실제로는 두 시간만 대화했다고 하자. B의 페이스라면 이렇게 된다.

- 음성 세션 1,440분 × 0.05달러 = 72.00달러
- 백엔드 두 시간 분량 = 1.04달러
- 합계 **73.04달러** (약 98,083원)

같은 두 시간을 대화하면서 필요할 때만 세션을 열었다면 7.04달러다. 약 9,459원이다. 대화량은 똑같은데 **열 배 차이**가 난다. 유휴 시간이 곧 청구서라는 말이 이런 뜻이다.

이 계산에는 빠뜨린 것이 있다. 세션 하나를 24시간 유지하는 일 자체가 애초에 불가능하다. 세션이 만료되면 `session.closed`가 `expired` 사유로 닫히는데, 그 한도 시간은 공개돼 있지 않다. 24시간을 채우려면 중간에 다시 붙어야 하고, WebRTC로 다시 붙을 때마다 세션 생성 청구가 발생한다. 위 24시간 계산은 그 재접속 비용을 빼고 시간만 이어 붙인 값이다.

### 아끼는 방법

문서가 제시하는 방향은 토큰 시대와 다르다. 요약하면 **빨리 끝내는 것이 절약이다.**

- **세션을 열기 전에 이미 아는 정보를 넣는다.** 주문 번호와 현재 상태를 이미 알고 있다면 세션을 열기 전에 넣어 둔다. 사용자가 다시 말하거나 조회를 기다릴 이유가 없어진다.
- **도구를 기다리는 시간을 줄인다.** 독립적인 도구 호출을 병렬로 돌리고 빠른 처리 모드를 쓴다. 사용자가 1분 일찍 끊으면 0.05달러를 아낀다. 그 절약보다 추가 백엔드 비용이 작으면 총액이 내려간다.
- **긴 작업 중에는 세션을 닫는다.** 클라이언트 위임을 쓰면 백엔드 작업자는 음성 세션이 닫혀 있어도 계속 돌 수 있다. 작업 상태와 대화 맥락을 저장해 두었다가, 끝나면 새 세션을 열어 결과를 알려 주는 설계가 가능하다.
- **프롬프트 캐싱을 쓴다.** 재사용할 지시문과 도구 정의를 프롬프트 앞쪽에 둔다. 캐시 적중분은 10분의 1 가격이다.
- **더 비싼 백엔드가 총액을 낮출 수 있다.** 문서가 직접 적어 둔 대목이다. 큰 모델이 과제를 빨리 끝내서 음성 시간을 줄이면, 늘어난 토큰 값보다 아낀 음성 값이 클 수 있다. 반대로 싼 모델이 도구 호출을 반복하거나 실패하면 총액이 오른다. 성공한 과제당 비용으로 비교하라고 권한다.

사용량을 볼 때 함정이 하나 있다. GPT-Live는 `session.usage.updated` 이벤트로 누적 음성 시간을 초 단위로 보낸다. 각 갱신은 이전 값을 **대체한다.** 스냅샷을 더하면 안 된다. `session.close`를 보낸 뒤 `session.closed`가 주는 최종 값을 한 번만 기록해야 한다.

### Realtime API와 비교하면

같은 회사의 음성 API인데도 요금 체계가 정반대다. Realtime 계열은 토큰으로 매긴다. 사용자 오디오는 100밀리초당 1토큰, 어시스턴트 오디오는 50밀리초당 1토큰이다. `gpt-realtime-2.1`의 오디오 요금은 100만 토큰당 입력 32달러, 캐시된 입력 0.40달러, 출력 64달러다.

대충 환산해 보면 어시스턴트가 1분 말할 때 오디오 출력 토큰이 1,200개 남짓 생긴다. 여기에 64달러를 곱하고 100만으로 나누면 0.077달러다. 게다가 Realtime은 매 응답마다 대화 전체를 다시 입력으로 넣기 때문에, 대화가 길어질수록 입력 쪽이 불어난다.

그래서 두 요금 체계는 최적화의 방향이 갈린다. Realtime을 쓰면 모델이 말을 줄일수록 아낀다. GPT-Live에서는 대화를 일찍 끝낼수록 아낀다. 앞쪽에서 요금을 만드는 것은 발화 비율이고, 뒤쪽에서 요금을 만드는 것은 벽시계다.

## 가장 흥미로운 지점

과금 단위가 바뀌면 무엇을 아껴야 하는지가 바뀐다. 이 당연한 문장의 결과가 생각보다 넓었다.

토큰으로 매기던 시절의 최적화는 대체로 "덜 말하게" 하는 쪽이었다. 출력을 짧게 잡고, 장황한 설명을 지우고, 맥락을 잘라 넣는다. 그런데 시간으로 매기기 시작하면 그 손질이 오히려 손해가 될 수 있다. 모델이 설명을 아끼는 바람에 사용자가 한 번 더 되묻는다면, 아낀 토큰 값보다 늘어난 통화 시간 값이 크다.

OpenAI 문서가 이것을 에둘러 말하지 않고 그대로 적어 둔 대목이 인상적이었다. 더 비싼 모델이 총액을 낮출 수 있다고, 실패와 재시도를 포함해 성공한 과제당 비용으로 비교하라고 적혀 있다. 모델 값을 파는 쪽이 모델 값만 보지 말라고 쓴 셈이다.

내가 가장 오래 생각한 것은 침묵이었다. 사람의 대화에서 침묵은 비용이 아니다. 생각할 자리를 내주는 시간이기도 하다. GPT-Live-1이 내세우는 개선점도 거기에 있었다. 학습자가 멈춰 있을 때 끼어들지 않는 것, Speak가 80% 가까이 줄었다고 한 대상이 바로 이것이다. 그런데 요금표를 펴 놓고 보면 그 기다림이 초당 얼마로 환산된다. 잘 기다리는 모델을 만들어 놓고, 그 기다림에 초당 요금을 매긴다. 이 둘이 모순이라는 말은 아니다. 그래도 대화를 설계하는 사람이라면 이제 두 개의 시계를 나란히 놓고 봐야 한다.

## 출처

2026년 9월 13일 기준으로 OpenAI 공식 발표와 개발자 문서, API 레퍼런스, 가격표를 1차 출처로 삼아 확인했다.

- OpenAI, "Introducing GPT‑Live", 2026-07-08. <https://openai.com/index/introducing-gpt-live/>
- OpenAI, "Build more natural voice experiences with GPT‑Live‑1 in the API", 2026-09-10. <https://openai.com/index/introducing-gpt-live-1-in-the-api/>
- OpenAI API, "GPT-Live 1 Model". <https://developers.openai.com/api/docs/models/gpt-live-1>
- OpenAI API, "Getting started with GPT-Live". <https://developers.openai.com/api/docs/guides/live>
- OpenAI API, "Custom voices". <https://developers.openai.com/api/docs/guides/custom-voices>
- OpenAI API, "Cost optimization". <https://developers.openai.com/api/docs/guides/voice-latency-cost>
- OpenAI API, "Pricing". <https://developers.openai.com/api/docs/pricing>
- 음성 목록 교차 확인: `openai/openai-openapi`의 `openapi.yaml`, `openai/openai-node`의 `src/resources/live/live.ts`, `openai/openai-python`의 `src/openai/types/live/built_in_voice.py`
- 환율: 유럽중앙은행 기준환율 2026-09-11, 1달러 = 1,342.79원

본문 삽화는 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조하여 gpt-image-2 image-to-image로 생성했다.

[^1]: OpenAI, "Introducing GPT‑Live", 2026-07-08.
[^2]: OpenAI API, "Getting started with GPT-Live".
[^3]: OpenAI, "Build more natural voice experiences with GPT‑Live‑1 in the API", 2026-09-10. 인용된 발언은 Speak의 공동 창업자 겸 CTO Andrew Hsu와 의료 음성 서비스 공동 창업자 겸 CTO Tony Stoyanov의 것이다.
[^4]: 2026-09-13 기준 <https://developers.openai.com/api/docs/models> 목록과 <https://developers.openai.com/api/docs/pricing> 가격표에 `gpt-live-1`과 `gpt-live-transcribe`만 있고 mini 변형은 없다.
