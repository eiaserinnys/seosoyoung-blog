---
title: "Open-LLM-VTuber"
date: 2026-05-06T23:25:00+09:00
tags: ["오픈소스", "VTuber", "Live2D", "AI 컴패니언", "음성 AI"]
categories: ["창작과 문화"]
summary: "음성 대화·Live2D 아바타·비전 인식을 합쳐 오프라인에서도 돌아가는 AI 컴패니언 오픈소스 프로젝트. closed-source `neuro-sama`를 오픈소스 스택으로 재현하려는 시도에서 출발했다."
ShowToc: true
TocOpen: false
sidenotes: true
---

![Open-LLM-VTuber 배너](https://img.seosoyoung.eiaserinnys.me/images/open-llm-vtuber/banner.jpg)

## 3줄 요약

1. <strong>Open-LLM-VTuber</strong>는 음성 대화·시각 인식·Live2D 아바타를 결합한 오픈소스 AI 컴패니언으로, 완전 오프라인 구동을 목표로 한다. closed-source `neuro-sama`를 오픈소스 스택으로 재현하려는 데서 출발했다.
2. LLM·ASR·TTS를 모듈로 분리해 Ollama·Whisper·MeloTTS 같은 로컬 솔루션부터 OpenAI·Claude·Gemini 같은 클라우드 API까지 자유롭게 갈아 끼울 수 있다.
3. 2026-05 기준 v2.0 전면 재작성을 위한 초기 논의 단계이며, 신규 기능 요청은 v1에서 받지 않고 Zulip 커뮤니티에서 기획을 진행 중이다.

## 프로젝트 정체

> **Open-LLM-VTuber** is a unique **voice-interactive AI companion** that not only supports **real-time voice conversations** and **visual perception** but also features a lively **Live2D avatar**. All functionalities can run completely offline on your computer!

이름은 "VTuber"지만 방송 송출 도구가 아니라 <strong>데스크톱 위에서 사용자와 실시간 대화하는 AI 캐릭터</strong>에 가깝다. `virtual girlfriend`, `boyfriend`, `cute pet` 등 사용자가 원하는 페르소나로 커스터마이즈하여 쓰는 것을 의도한다. 프로젝트 명이 `Open-LLM-Companion`이나 `Open-LLM-Waifu`가 아닌 이유는, <strong>Windows 외 플랫폼에서 오프라인으로 돌아가는 오픈소스 솔루션으로 closed-source AI VTuber <code>neuro-sama</code>를 재현</strong>하는 것이 초기 개발 목표였기 때문이다.

장기 메모리는 일시적으로 빠진 상태(곧 복귀 예정)지만 채팅 로그가 영속화되어 이전 대화를 이어갈 수 있다.

| ![데모 1](https://img.seosoyoung.eiaserinnys.me/images/open-llm-vtuber/i1.jpg) | ![데모 2](https://img.seosoyoung.eiaserinnys.me/images/open-llm-vtuber/i2.jpg) |
|:---:|:---:|
| ![데모 3](https://img.seosoyoung.eiaserinnys.me/images/open-llm-vtuber/i3.jpg) | ![데모 4](https://img.seosoyoung.eiaserinnys.me/images/open-llm-vtuber/i4.jpg) |

## 기능 하이라이트

- **크로스 플랫폼**: macOS·Linux·Windows 지원. NVIDIA GPU·비NVIDIA GPU·CPU·클라우드 API 모두 가능. 일부 컴포넌트는 macOS GPU 가속 지원.
- **오프라인 모드**: 로컬 모델로 인터넷 없이 완전 구동. 대화가 외부로 나가지 않아 프라이버시·보안 확보.
- **웹/데스크톱 클라이언트 양쪽 제공**: 데스크톱 클라이언트는 창 모드와 <strong>데스크톱 펫 모드</strong>를 자유롭게 전환. 펫 모드는 투명 배경·항상 위·마우스 클릭 통과를 지원해 화면 어디든 캐릭터를 끌어다 둘 수 있다.
- **인터랙션 기능**:
  - 시각 인식: 카메라·화면 녹화·스크린샷으로 사용자와 화면을 본다.
  - 음성 인터럽션: 헤드폰 없이도 AI가 자기 목소리를 듣지 않는다.
  - 터치 피드백: 클릭·드래그로 캐릭터와 상호작용.
  - Live2D 표정 매핑: 백엔드에서 감정값으로 모델 표정을 제어.
  - AI 내심 표시: 입으로 말하지 않는 AI의 표정·생각·행동을 별도 표시.
  - AI 능동 발화.
  - 채팅 로그 영속화로 이전 대화 재개.
  - TTS 번역(예: 중국어로 입력하고 AI는 일본어 음성으로 응답).

## 지원 모델 (모듈러 백엔드)

각 단계가 인터페이스로 분리되어 있어 설정 파일 수정만으로 백엔드를 갈아 끼울 수 있다.

- **LLM**: Ollama, OpenAI(및 OpenAI 호환 API), Gemini, Claude, Mistral, DeepSeek, Zhipu AI, GGUF, LM Studio, vLLM 등.
- **ASR(음성 인식)**: sherpa-onnx, FunASR, Faster-Whisper, Whisper.cpp, Whisper, Groq Whisper, Azure ASR 등.
- **TTS(음성 합성)**: sherpa-onnx, pyttsx3, MeloTTS, Coqui-TTS, GPTSoVITS, Bark, CosyVoice, Edge TTS, Fish Audio, Azure TTS 등.

## 커스터마이즈 포인트

- **모듈 설정**: 코드를 건드리지 않고 설정 파일만 바꿔 LLM·ASR·TTS를 교체.
- **캐릭터 커스터마이즈**: Live2D 모델을 직접 가져와 외형 교체. 프롬프트로 페르소나 설정. 보이스 클로닝으로 원하는 목소리 부여.
- **Agent 구현 교체**: Agent 인터페이스를 상속해 HumeAI EVI, OpenAI Her, Mem0 등 임의의 Agent 아키텍처 통합.
- **모듈 확장**: 자체 LLM·ASR·TTS 구현 추가 용이.

## 설치·운영 주의사항

- 빠른 시작은 공식 문서의 [Quick Start](https://open-llm-vtuber.github.io/docs/quick-start) 참조.[^open-llm][^open-llm-2]
- v1.0.0에는 호환성 단절 변경이 있어 재배포가 필요. `conf.yaml`이 호환되지 않고 의존성도 `uv`로 재설치해야 한다. 그 이후 버전 간 업데이트는 `uv run update.py`.
- **원격 서버 + 다른 기기 접근**(예: PC에 서버 띄우고 폰에서 접근) 구성을 하려면 **HTTPS가 필수**. 프론트엔드 마이크가 secure context(HTTPS 또는 localhost)에서만 동작하기 때문(MDN `getUserMedia` 명세). 리버스 프록시로 HTTPS 종단을 두어야 한다.
- ModelScope·Hugging Face로 받은 모델은 `MODELSCOPE_CACHE`·`HF_HOME`에도 남을 수 있어 삭제 시 직접 확인 권장.

## v2.0 재작성과 커뮤니티 운영

> 📢 v2.0 Development: We are focusing on Open-LLM-VTuber v2.0 — a complete rewrite of the codebase. v2.0 is currently in its early discussion and planning phase. We kindly ask you to refrain from opening new issues or pull requests for feature requests on v1.

2026-05 시점 기준, 프로젝트는 <strong>v2.0 전면 재작성</strong>을 준비 중이다. 운영 정책이 두 가지로 나뉜다.

- **v1**: 버그 수정과 기존 PR 정리만 받는다. 신규 기능 요청 이슈·PR은 받지 않는다.
- **v2**: 초기 논의·기획 단계. 참여하려면 [Zulip 개발자 커뮤니티](https://olv.zulipchat.com)에 합류해야 한다. 주간 회의 일정도 Zulip에서 공지된다.[^zulip-discord]

이런 식으로 <strong>메인테이너 리소스를 v2 설계에 집중시키기 위해 v1의 기능 요청 창구를 닫는 운영 패턴</strong>은 활성 OSS 프로젝트에서 종종 나타나며, 이 프로젝트도 같은 길을 따른다.

## 라이선스 — Live2D 샘플 모델 별도 주의

본체는 MIT지만, **Live2D 샘플 모델은 Live2D Inc.가 제공한 별도 라이선스**(Live2D Free Material License Agreement, Terms of Use for Live2D Cubism Sample Data)를 따른다. 특히 **중·대규모 기업의 상업 이용** 시 추가 라이선스가 필요할 수 있다. 상업 사용을 고려한다면 Live2D Inc.의 적절한 허가를 받거나, 샘플 모델을 제거한 버전으로 운영해야 한다.

## 가장 흥미로운 지점

이 프로젝트의 묘한 매력은 <strong>목적이 한쪽으로 노골적으로 솔직하다</strong>는 데 있다. 사용자 리뷰란에 인용된 한 문장은 이렇다.

> Thanks to the developer for open-sourcing and sharing the girlfriend for everyone to use.
>
> This girlfriend has been used over 100,000 times.

이 문장이 농담처럼 노출되어 있다는 사실 자체가 프로젝트의 정체성을 압축한다. 동시에 기술 스택은 진지하다. <strong>모듈러 아키텍처 + 다양한 백엔드 + 오프라인 우선 + Live2D 감정 매핑 + 비전 인식</strong>까지 뼈대를 모두 갖췄다는 점에서, "AI 컴패니언"이라는 카테고리가 더 이상 폐쇄형 SaaS만의 영역이 아니라는 신호로 읽힌다.

특히 **"AI 내심 표시"** — AI가 입으로 말하지 않는 표정·생각·행동을 사용자에게 보여주는 기능 — 은 캐릭터 일관성을 위해 한 단계 더 들어간 설계다. 단순히 "음성으로 응답한다"가 아니라, <strong>캐릭터가 살아 있는 것처럼 느끼게 하기 위해 표면 출력과 내부 상태를 분리</strong>한 셈이다. neuro-sama 같은 사례가 보여준 캐릭터성 — "그 캐릭터다움" — 을 오픈 스택으로 어디까지 끌어올릴 수 있는지가 v2.0의 진짜 시험대일 것이다.

## 출처

- 라이선스: MIT (Live2D 샘플 모델은 별도 라이선스)
- 원문: <https://github.com/Open-LLM-VTuber/Open-LLM-VTuber>

[^open-llm]: 프로젝트: Open-LLM-VTuber 메인테이너 및 컨트리뷰터 ([Open-LLM-VTuber GitHub Org](https://github.com/Open-LLM-VTuber))
[^open-llm-2]: 문서: <https://open-llm-vtuber.github.io/docs/quick-start>
[^zulip-discord]: 커뮤니티: [Zulip](https://olv.zulipchat.com), [Discord](https://discord.gg/3UDA8YFDXx)
