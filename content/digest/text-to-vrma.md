---
title: "Text-To-VRMA: 텍스트로 VRM 캐릭터를 움직이는 웹앱"
date: 2026-07-18T07:20:00+09:00
tags: ["AI", "오픈소스", "LLM", "VRM", "3D 애니메이션", "일본"]
categories: ["창작과 문화"]
summary: "「그 자리에서 손을 흔든다」 같은 텍스트를 넣으면 AI가 VRM 캐릭터의 모션을 만들어 브라우저 안에서 재생하고 .vrma 파일로 저장하는 웹앱. 개발자가 내세운 「낮은 VRAM으로도 돌아간다」는 주장을 코드에서 확인해 보니, VRAM 병목이 어디였는지 정확히 짚어 그 한 덩어리만 CPU로 옮긴 결과였다."
math: false
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/text-to-vrma/release-1.1.0.jpg"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/text-to-vrma/release-1.1.0.jpg"
---

![Text-To-VRMA v1.1.0 릴리스](https://img.seosoyoung.eiaserinnys.me/images/text-to-vrma/release-1.1.0.jpg)

## 3줄 요약

1. Text-To-VRMA는 일본의 개인 개발자 Kiratchi가 2026년 7월 14일에 공개한 MIT 라이선스 웹앱이다. 「그 자리에서 걷는다」, 「기뻐서 점프한다」, 「손을 흔든다」 같은 텍스트를 넣으면 AI가 VRM 캐릭터의 모션을 생성해 브라우저 안에서 바로 재생하고, `VRMA`(VRM Animation, `.vrma`) 파일로 저장한다. 7월 16일 v1.1.0에서 NVIDIA의 모션 생성 AI ARDY를 로컬 엔진으로 붙였다.
2. 생성 엔진은 둘이다. 하나는 <strong>LLM 키프레임</strong> — OpenAI API가 뼈대별 오일러 각 키프레임을 JSON으로 뱉는다. 다른 하나는 v1.1에서 추가된 <strong>ARDY 로컬 엔진</strong> — NVIDIA Research의 text-to-motion 확산 모델을 내 PC에서 돌려 모션캡처 품질의 전신 동작을 무제한·오프라인으로 만든다.
3. 개발자가 트윗에서 내세운 문구는 「VRAM 낮아도 돌아간다」였다. 공식 ARDY 데모는 VRAM 20\~24GB를 요구하는데, 이 앱은 GPU 필수분을 약 2GB까지 줄였다고 한다. 코드를 열어 보니 이 주장은 사실이었다. 다만 그 정체는 새로운 최적화가 아니라, VRAM을 가장 많이 먹는 한 덩어리(8B 텍스트 인코더)를 정확히 지목해 CPU로 밀어낸 것이었다.

## 무엇을 하는 앱인가

핵심은 브라우저 안에서 도는 Web 앱이라는 점이다. `git clone` 후 `npm run dev`로 띄우면 `localhost:5173`에서 열리고, VRoid 공식 샘플 모델(AvatarSample)이 로드된 3D 뷰에 텍스트 상자가 붙어 있다. 텍스트를 넣고 「모션 생성 & 재생」을 누르면 캐릭터가 움직인다. 만족스러우면 「.vrma 저장」으로 파일을 뽑아 VRMA 대응 앱에서 그대로 쓴다.

![텍스트에서 모션 생성 데모](https://img.seosoyoung.eiaserinnys.me/images/text-to-vrma/demo.gif)

출력 포맷인 `.vrma`는 glTF 바이너리(GLB)에 `VRMC_vrm_animation` 확장을 얹은 것으로, 휴머노이드 뼈대 매핑과 표정 트랙을 담는다. 즉 이 앱은 「모션 생성기」인 동시에 「VRMA 인코더」다. VRM 0.x와 1.0 양쪽을 자동 판별해 받고, UI는 일본어·영어·중국어·한국어 4개 언어를 지원한다.

## 두 개의 엔진

| 엔진 | 하는 일 | 필요한 것 |
|---|---|---|
| LLM 키프레임 (OpenAI API / Codex) | 정확한 포즈·손가락·표정 지정에 강하다. 세팅 없이 어느 PC에서나 돈다 | API 키 또는 Codex 플랜 |
| ARDY 로컬 엔진 (v1.1\~) | 걷기·춤·점프 같은 전신 운동이 모션캡처 품질. 무제한·오프라인 | 추가 세팅(약 20GB 다운로드) |

ARDY 모드는 <strong>「GPT가 머리, ARDY가 몸」</strong>의 하이브리드다. 3층으로 나뉜다.

- <strong>GPT</strong>(선택, API 키 저장 시): 일본어 의도 이해, 「달리다가 점프하고 마지막에 인사」 같은 연속 동작 분할, ARDY가 알아듣는 영어 표현으로 번역.
- <strong>Llama-3-8B</strong>(로컬·CPU): 영문을 ARDY 전용 벡터로 변환(LLM2Vec).
- <strong>ARDY</strong>(로컬·GPU): 실제 모션캡처 데이터로 학습한 확산 모델이 동작을 생성.

API 키가 없어도 로컬 번역(FuguMT)으로 완결되지만, 키가 있으면 복잡한 지시의 재현도가 올라간다. 여기에 3D 바닥을 클릭해 경유지를 찍으면 캐릭터가 그 순서로 지나가는 <strong>경유지 모드</strong>도 붙어 있다.

## VRAM 절약 주장을 코드에서 확인하다

이 앱이 스스로 내세운 가장 큰 자랑은 「낮은 VRAM」이다. README의 문장은 이렇다.

> ARDY 공식 데모는 VRAM 20\~24GB를 요구하지만, 본 앱은 GPU 필수 부분을 약 2GB까지 삭감했다(VRAM 12GB에서 동작 확인). VRAM의 대부분을 차지하는 텍스트 이해부(8B LLM)를 CPU에서 돌리는 구성이기 때문이며, 모션 모델 본체·확산 스텝 수는 공식 그대로 — 생성 품질은 전혀 떨어지지 않았다.

읽으면 그럴듯하지만, 「품질은 그대로인데 VRAM만 10분의 1」은 공짜 점심처럼 들린다. 그래서 엔진 서버 코드(`tools/ardy-engine/server.py`)를 직접 열었다. 트릭은 딱 한 군데, 71\~97줄에 있었다.

먼저 모션 확산 모델은 GPU에 올린다.

```python
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
```

그다음이 핵심이다. 코드의 일본어 주석이 문제를 스스로 자백한다 — <em>ARDY의 `load_text_encoder`는 마지막에 `.to(model_device)`를 호출하기 때문에, 그냥 두면 8B 인코더가 VRAM \~15GB를 점유한다.</em> 그러니까 원래 ARDY는 텍스트 인코더까지 GPU로 끌어올리고, 그게 VRAM의 대부분을 먹는 범인이다. 앱은 이걸 우회한다.

```python
_enc_dev = os.environ.get("TEXT_ENCODER_DEVICE", "").strip().lower()
_pre_encoder = None
if _enc_dev:
    from ardy.model.load_model import load_text_encoder
    _pre_encoder = load_text_encoder(device=_enc_dev)   # 인코더를 먼저 CPU에 구축

if _pre_encoder is not None:
    model = load_model(ARGS.model, device=DEVICE, text_encoder=_pre_encoder)

# 보험: 그래도 GPU에 있으면 다시 CPU로 밀어낸다
if _enc_dev and getattr(model, "text_encoder", None) is not None:
    model.text_encoder.to(_enc_dev)
    if DEVICE.startswith("cuda") and _enc_dev == "cpu":
        torch.cuda.empty_cache()
```

앱 기본값은 `TEXT_ENCODER_DEVICE=cpu`다. 즉 8B 인코더를 GPU에 올리기 전에 미리 CPU에 짓고, 혹시 GPU로 새어 나가면 보험으로 다시 CPU로 옮긴 뒤 캐시를 비운다. 결과적으로 GPU에는 확산 모델(\~2GB)만 남는다. 15GB짜리 인코더 한 덩어리를 정확히 지목해 들어낸 것이다.

「품질은 그대로」라는 말도 코드로 확인된다. 확산 스텝 수는 모델 기본값을 그대로 받는다.

```python
NUM_BASE_STEPS = int(model.diffusion.num_base_steps)
# ...
steps = int(steps) if steps else NUM_BASE_STEPS
steps = max(1, min(NUM_BASE_STEPS, steps))   # 줄일 수만 있고, 기본은 풀 스텝
```

스텝은 사용자가 줄일 수는 있어도 기본값을 넘길 수는 없다. 확산 품질을 깎아서 VRAM을 번 게 아니라는 뜻이다. 이 설계가 성립하는 이유는 명확하다. 텍스트 인코더는 프롬프트당 임베딩을 <strong>한 번</strong> 뽑을 뿐 확산 루프 바깥에 있다. 그러니 느린 CPU에 둬도 매 스텝 반복되는 모션 생성 품질에는 영향이 없다.

## 그래서 공짜 점심인가

아니다. 코드는 주장을 뒷받침하지만, 자랑 문구가 가리는 대가도 코드와 요구사항에 남아 있다.

첫째, <strong>VRAM을 줄인 게 아니라 RAM으로 옮긴 것</strong>이다. 8B 인코더가 시스템 메모리로 갔으니 그만큼 RAM이 필요하다. ARDY 엔진 README의 요구사항은 RAM 16GB(최소)에서 32GB+(권장)로 커져 있다. 총 메모리 사용량이 준 게 아니라, GPU가 감당하던 짐을 CPU가 넘겨받았을 뿐이다.

둘째, <strong>속도를 내줬다</strong>. bfloat16 8B 모델을 CPU에서 돌리므로 생성 시작 전 텍스트 해석에 수 초가 붙는다(결과는 캐시한다). GPU가 아예 없으면 모션 생성 자체도 CPU로 떨어져 수 배 느려진다.

셋째, `\~2GB / 12GB 확인`이라는 수치는 <strong>개발자 자가 보고</strong>다. README의 「동작 확인함」이 근거이고, 독립 벤치마크는 없다.

정리하면 이건 새 알고리즘이 아니라 <strong>병목의 위치를 정확히 안 사람의 배치 결정</strong>이다. ARDY의 VRAM을 먹는 주범이 확산 모델이 아니라 그 앞단의 8B 텍스트 인코더라는 걸 짚었고, 그 인코더가 확산 루프 밖에서 한 번만 돌면 된다는 성질을 이용해 GPU 밖으로 밀어냈다. 공짜 점심은 아니지만, 「20GB VGA가 없으면 못 쓰던 것」을 「12GB로 쓸 수 있게」 만든 실용적 재배치다.

## 코드가 품질을 만드는 방식 — LLM 키프레임 쪽

ARDY 엔진이 확산 모델이라면, 기본 엔진인 LLM 키프레임 쪽은 반대의 접근이다. 여기서 「자연스러움」은 학습이 아니라 <strong>코드에 적힌 해부학 지식</strong>에서 나온다.

`src/llm.js`의 시스템 프롬프트를 보면, GPT에게 던지는 지시가 사실상 3D 애니메이터 매뉴얼이다. 좌표 규약(「+Z를 향해 서고, +X가 왼손 방향」), 관절별 가동역(「목·머리 합계는 ±60도 이내, spine·chest는 각 ±30도 이내」), 자연스러운 포즈 원칙(「팔을 올릴 때 머리 위로 덮지 말고 몸의 윤곽 바깥에서만 움직여라」), 심지어 동작별 해부학 메모(「손 흔들기: 상완은 옆으로 45\~60도, 팔꿈치를 60\~90도 굽혀 손을 얼굴 옆에」)까지 문장으로 들어 있다.

그리고 LLM이 뱉은 결과를 그대로 믿지 않는다. `validateSpec()`이 결정론적으로 후처리한다.

- <strong>각도 클램프</strong>: 뼈대별 상한을 둔다(`leftHand`/`rightHand` 25도, `upperArm` 75도, `neck` 45도, `head` 70도).
- <strong>무릎은 경첩 관절</strong>로 강제: X를 \-3\~140도로 제한해 역관절을 막는다.
- <strong>팔꿈치 가드</strong>: 과신전(뒤로 꺾임)과 비틀림을 차단한다.
- <strong>어깨는 아예 버린다</strong>: LLM이 어깨를 돌리면 옷 메시가 일그러지므로, 스펙에서 어깨 트랙을 삭제하고 빌더의 자동 추종에 맡긴다.
- <strong>손가락은 LLM에 노출조차 안 한다</strong>: 자연스러운 손 모양을 코드가 자동으로 넣는다.

즉 LLM은 키프레임 초안을 제안하고, 코드가 생체역학 제약으로 처분한다. 「손을 흔든다」가 그럴듯하게 보이는 이유는 모델이 인체를 이해해서가 아니라, `applyWaveCorrection()`이 상완을 52도로 눌러 잡고 손바닥을 정면으로 돌려놓기 때문이다.

## 가장 흥미로운 지점

두 엔진이 정반대 방향에서 같은 결론에 닿는다. ARDY 쪽은 「어디가 무거운지」를 정확히 알아 그 한 덩어리만 옮겨 VRAM을 벌었고, LLM 키프레임 쪽은 「어디가 어색해지는지」를 정확히 알아 그 지점마다 클램프를 걸어 품질을 벌었다. 둘 다 마법이 아니라 <strong>도메인을 아는 사람이 병목과 실패 지점을 정확히 지목한 결과</strong>다.

특히 VRAM 이야기는 요즘 로컬 AI 담론에서 자주 흐려지는 지점을 또렷하게 보여준다. 「12GB로 SIGGRAPH 모델을 돌린다」는 헤드라인만 보면 압축이나 양자화의 성과처럼 들리지만, 실제로는 총 메모리를 줄인 게 아니라 GPU와 CPU 사이에서 짐을 옮긴 배치다. 무엇을 어디에 두느냐가 무엇을 얼마나 압축하느냐만큼 중요하다는, 오래된 시스템 엔지니어링의 교훈이 최신 모션 AI에서도 그대로 반복된다.

## 출처

- Text-To-VRMA (© Kiratchi, 2026) — 소스코드 MIT License
- 리포: <https://github.com/Kirakun0328/text-to-vrma>
- 개발자 X: <https://x.com/Kiratchi0328> (v1.1.0 릴리스 안내 트윗, 2026-07-16)
- 확인 버전: master 브랜치, 2026-07-17 시점 (별 52개). 코드 인용은 `src/llm.js`, `src/vrmaBuilder.js`, `tools/ardy-engine/server.py`
- ARDY: NVIDIA Research, *Autoregressive Diffusion for Interactive Motion* (SIGGRAPH 2026)
- 인용한 VRAM 수치·동작 확인 환경은 개발자의 README 자가 보고이며, 독립 벤치마크가 아니다.
