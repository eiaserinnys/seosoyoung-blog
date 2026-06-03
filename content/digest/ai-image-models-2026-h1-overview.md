---
title: "AI 이미지 생성 모델 종합 지도 (2026 상반기)"
date: 2026-06-03T20:00:00+09:00
tags: ["AI", "이미지 생성", "생성형 모델", "Midjourney", "Flux", "gpt-image-2", "시장 분석"]
categories: ["다이제스트"]
summary: "gpt-image-2 출시 이후 흔들린 AI 이미지 생성 모델 지형을 6월 3일 시점으로 종합한다. Big5 재편, 중국·오픈소스 진영의 약진, 이미지→영상 워크플로우 표준화, 규제·안전 이슈까지 한 자리에서 정리한다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/ai-image-models-2026-h1-overview/cover.png"
images:
  - "/images/ai-image-models-2026-h1-overview/cover.png"
---

## 3줄 요약

1. **gpt-image-2가 2026년 4월 21일 출시 당일 LMArena ELO에서 2위 대비 +242점**이라는 단일 모델 사상 최대폭으로 1위에 오르며 AI 이미지 시장의 지형이 재편되었다. 텍스트 렌더링 99% 정확도와 reasoning-native 아키텍처가 핵심 차별점이다.
2. Midjourney V8.1은 미적 천장을 지키되 "예술 전문 도구"로 좁혀졌고, Flux 2 Pro/Max는 포토리얼리즘과 오픈웨이트 커스터마이징을 동시에 잡았으며, 중국 진영(Seedream·Qwen·GLM-Image·Z-Image·Hunyuan·Kolors)이 텍스트·이중언어·가성비 영역에서 약진했다.
3. 이미지→영상 워크플로우가 표준화되고(Sora 종료, Kling 3.0·Seedance 2.0·Veo 3.1·Runway Gen-4.5가 분담), 이미지 단가는 2022년 대비 94% 하락했으며, 2026년 8월 2일 발효 예정인 EU AI Act Article 50이 워터마킹 의무화의 임계점에 다가서고 있다.

## 글의 정체

- **시점**: 2026년 6월 3일 기준 종합 정리
- **취재 범위**: 메이저 모델 평가 5종 + 신흥·특화 모델 15종 이상 + 시장 흐름·규제 자료 7건. 외부 비교 글·벤치마크 사이트·공식 발표·전문 분석가 평가를 다층으로 교차 확인했다
- **이 글의 위치**: 같은 날 발행한 [Cliprise의 2월 가이드 다이제스트](/digest/ai-image-generation-2026-cliprise/)는 gpt-image-2 출시 *이전* 시점의 지도였다. 4월 21일을 기점으로 풍경이 크게 바뀌었기에, 6월 시점의 종합판이 별도로 필요하다

## 1. gpt-image-2의 충격 (2026-04-21)

![gpt-image-2의 다국어 텍스트 렌더링 — 일본어·한국어·중국어·힌디어·벵골어 동시 출력](/images/ai-image-models-2026-h1-overview/fig01b-multilingual-poster.jpg)
*단일 이미지 안에 다섯 가지 문자 체계가 모두 정확히 렌더링됐다 ([OpenAI 공식](https://openai.com/index/introducing-chatgpt-images-2-0/)).*

OpenAI가 키노트 없이 모델 페이지와 갤러리만으로 공개한 이 모델은 출시 당일 *모든* 카테고리에서 1위를 차지했다.

| 카테고리 | gpt-image-2 ELO | 2위 모델과의 격차 |
|---|---|---|
| Text-to-Image | 1,512 | +242 |
| 단일 이미지 편집 | 1,513 | 카테고리 1위 |
| 멀티이미지 편집 | 1,464 | 카테고리 1위 |

이는 이전 단일 모델 도약폭의 약 4배다.{{< sn >}}Nate's Newsletter, ["What gpt-image-2 actually changed"](https://natesnewsletter.substack.com/p/what-gpt-image-2-actually-changed), 2026-04-25.{{< /sn >}} 텍스트-이미지 카테고리에서는 *모든 메이저 경쟁 모델이 70 ELO 밴드 안에 밀집*해 있던 상태였다 — 그 천장을 한 모델이 단번에 깨고 솟아올랐다.{{< sn >}}[ArtificialAnalysis — Image Leaderboard](https://artificialanalysis.ai/image/leaderboard/text-to-image).{{< /sn >}}

### 핵심 차별점

- **텍스트 렌더링 99% 정확도** — DALL-E 3 시대의 \~70%, gpt-image-1.5의 \~85%에서 도약.{{< sn >}}TokenMix, ["GPT Image 2 Review"](https://tokenmix.ai/blog/gpt-image-2-review-chatgpt-images-2-2026), 2026-04. 측정치는 표준 텍스트 정확도 벤치마크 기준.{{< /sn >}} 라틴·CJK·힌디·벵골 스크립트 포함 다국어 지원
- **Reasoning-native 아키텍처** — 픽셀을 그리기 전에 레이아웃을 *계획*하고 *자기 검증*한다. O-시리즈 추론 모델의 사고 사슬을 이미지 생성에 이식한 최초의 모델
- **8장 일관성** — 단일 프롬프트로 캐릭터·사물·스타일이 유지되는 최대 8장 배치 생성. 스토리보드·브랜드 캠페인 변형이 한 호출로 가능
- **두 가지 운영 모드** — Instant(\~3\~5초, 일반 작업) vs Thinking(10\~30초, 인포그래픽·복합 텍스트)
- **웹 검색 그라운딩** — 생성 전 실시간 정보 참조 (기상 지도, 최신 제품 등)
- **네이티브 2K\~4K 해상도**

![일본 판타지 망가 — 단일 프롬프트로 생성된 다패널 스토리보드와 일본어 말풍선](/images/ai-image-models-2026-h1-overview/fig02-manga-multiimage.webp)
*단일 프롬프트가 생성한 일본 판타지 망가 페이지. 패널 사이의 캐릭터·구도 일관성이 유지되고, 말풍선의 일본어와 효과음이 모두 정확히 렌더링된다 ([OpenAI 공식](https://openai.com/index/introducing-chatgpt-images-2-0/)).*

![gpt-image-2가 만든 샌프란시스코 날씨 활동 인포그래픽](/images/ai-image-models-2026-h1-overview/fig05-weather-infographic.jpg)
*실시간 날씨 데이터를 웹에서 가져온 뒤 추론 모드로 합성한 인포그래픽. 텍스트·아이콘·체크리스트가 한 호출에서 정합적으로 자리 잡았다 ([Wired 리뷰](https://www.wired.com/story/openai-beefs-up-chatgpts-image-generation-model/)).*

### 약점·한계

- **투명 배경 미지원** — Responses 이미지 생성 도구를 통한 알파 채널 출력 불가
- **파인튜닝 차단** — 브랜드·캐릭터 LoRA 불가능 → 커스터마이징 수요가 전량 Flux/SDXL 오픈스택으로 이동
- **고해상도 가격** — 네이티브 4K 고품질 시 $0.41/이미지로 대량 파이프라인에서 비경제적
- **API Tier 1 속도 제한** — 5장/분 상한
- **지식 컷오프 2025-12** — 최신 제품·인물 참조 시 레퍼런스 이미지 별도 제공 필요
- **출시 초기 안전성 우려** — 99% 텍스트 정확도가 위조 문서·간판·스크린샷 생성을 Plus 구독자 수준에서 가능하게 만들었다{{< sn >}}AI Advances / Mandar Karhade MD, ["GPT-image-2 is not an upgrade, it's a nuclear detonation"](https://ai.gopubby.com/openai-gpt-image-2-is-not-an-upgrade-its-a-nuclear-detonation-bbdc5ddb1bdf).{{< /sn >}}

## 2. Big5 재편 — 누가 어디로 갔는가

![gpt-image-2 · Midjourney V8 · Imagen 4의 동일 프롬프트 결과 — 갤러리 벽 비교](/images/ai-image-models-2026-h1-overview/fig03-big5-comparison-grid.webp)
*같은 풍경 프롬프트에 대한 세 모델의 응답을 한 벽에 모은 비교 갤러리. 미적 해석의 결이 모델마다 분명하게 다르다 ([Pixo 8 Design Tasks Tested](https://pixo.video/blog/gpt-image-2-vs-midjourney-vs-imagen4)).*

### Midjourney V8.1

- **버전 흐름**: V7(2025-04-03 출시) → V8 Alpha(2026-03-17) → **V8.1(2026-04-30)**{{< sn >}}9to6AI, ["Midjourney V8.1 Review 2026"](https://9to6ai.com/midjourney-v8-1-review-2026/).{{< /sn >}}
- **2026년 6월 디폴트**: V7 안정판. V8/V8.1은 alpha.midjourney.com에서 opt-in
- **포지션 변화**: 텍스트·생산성 영역에서 명확하게 *예술 전문 도구*로 좁혀졌다. Pick-Right 리뷰는 "AI 이미지 시장은 더 이상 Midjourney의 시장이 아니다. ChatGPT와 Gemini의 시장이 됐다"고 직접 진술한다.{{< sn >}}[Pick-Right — Midjourney Review 2026](https://pick-right.com/tools/midjourney/).{{< /sn >}}
- **강점**: 미적 출력 품질 1위(구도·조명·분위기), V8의 해부학적 정확도, V8.1의 3배 속도 개선
- **약점**: 텍스트 렌더링 \~30%(gpt-image-2의 1/3 수준), <strong>공개 API 부재</strong>가 시장 분배에서 최대의 약점이 되었다

Pixo의 프리랜서 설문이 잡은 흐름이 인상적이다.{{< sn >}}[Pixo — GPT-Image-2 vs Midjourney V8 vs Imagen 4: 8 Design Tasks Tested](https://pixo.video/blog/gpt-image-2-vs-midjourney-vs-imagen4), 2026-04-25.{{< /sn >}}

> "70% of professionals start creative projects in Midjourney but finish them in GPT-Image-2."

### Flux 2 (Black Forest Labs)

- **출시**: FLUX.2 Pro / FLUX.2 Max (2026-01)
- **아키텍처**: 32B 파라미터 rectified flow transformer, 32K 토큰 프롬프트, JSON 기반 제어{{< sn >}}[Picassoia — FLUX.2 Pro Review: Is This the Best AI Image Tool in 2026?](https://blog.picassoia.com/flux-2-pro-review-best-ai-image-tool-2026).{{< /sn >}}
- **패밀리**: Max(최고 품질) → Pro(생산 워크호스) → Flex(속도-품질 트레이드오프) → Klein/Dev(빠른 프로토타이핑·오픈웨이트)
- **강점**: 포토리얼리즘 Imagen 4 Ultra와 공동 1위, HEX 컬러 매칭·Pose guidance 등 개발자 제어력{{< sn >}}TokenMix 벤치마크 92/93/88(Imagen 4 Ultra / FLUX 2 Pro / Midjourney V7). [TokenMix — Imagen 4 Ultra Review](https://tokenmix.ai/blog/imagen-4-ultra-review-2026).{{< /sn >}}
- **약점**: 텍스트 렌더링 실패율 23%, 다중 객체 혼합 28%
- **결정적 이점**: <strong>Flux 2 Dev는 오픈웨이트</strong>다. gpt-image-2가 파인튜닝을 차단하면서 *브랜드·캐릭터 LoRA 시장 전체가 Flux/SDXL 스택으로 이동*했다. "오픈소스가 품질로 이긴 것이 아니라, 열린 유일한 문이기 때문에" 커스터마이징 시장을 독식하는 구도가 굳어졌다

### Google Imagen 4

- **출시**: 2026 Q1, 티어: Fast(\$0.02) / Standard(\$0.04) / Ultra(\$0.05\~0.07)
- **속도 최강**: 1\~3초 생성 — gpt-image-2 Thinking 모드의 1/10
- **포토리얼리즘**: TokenMix 벤치마크 92/100 (Flux 2 Pro 93, Midjourney V7 88)
- **약점**: 표준 Imagen 4는 권장 텍스트 길이 25자 이내 — 단문 강·장문 약
- **포지션**: 고볼륨 배치 생성의 1순위. SynthID 워터마킹 내장으로 콘텐츠 진위 확인 가능
- **추가**: ArtificialAnalysis 아레나에서 *Imagen 4 Ultra Preview 0606* 버전이 ELO 1,165\~1,175(전체 9위)로 활동 중 — 후속 라인을 시사하는 데이터

![Google Imagen 4 — 자연 사진 수준의 포토리얼 출력 (물총새 클로즈업)](/images/ai-image-models-2026-h1-overview/fig18-imagen4.webp)
*Google Imagen 4의 포토리얼 출력. 깃털 광택, 부리 광 반사, 배경 보케 분리가 일반 카메라 사진과 구분이 어려운 수준. TokenMix 벤치마크 92/100 ([Google DeepMind Imagen](https://deepmind.google/technologies/imagen/)).*

## 3. 중국 진영의 약진

2026 상반기에 가장 눈에 띄는 흐름이다. 텍스트 렌더링·이중언어·가성비·오픈소스 영역 모두에서 중국 기업의 모델이 *벤치마크 1위 자리*를 차지하고 있다.

### 텍스트 렌더링 1위 그룹

| 모델 | 회사 | 라이선스 | 핵심 지표 |
|---|---|---|---|
| GLM-Image | Zhipu AI | MIT (오픈) | **CVTG-2K 영어 91.16%**, LongText 중국어 97.88% |
| Qwen-Image 2.0 | Alibaba | Apache 2.0 (오픈) | DPG-Bench 88.32 (GPT Image 1 High 85.15) |
| Seedream 4.5 | ByteDance | 폐쇄 | LongText 영어 0.989 / 중국어 0.987 (1위) |
| Nano Banana 2 | Google (Gemini 3.1 Flash Image) | 폐쇄 | LongText 중국어 0.983 / 영어 0.981 |

![Qwen-Image 2.0가 만든 이중언어 인포그래픽](/images/ai-image-models-2026-h1-overview/fig08-qwen-image.png)
*Qwen-Image 2.0의 단일 프롬프트 출력. 영문 헤드라인·소제목·본문·아이콘이 한 호출에 정합적으로 배치된다. DPG-Bench 88.32로 GPT Image 1 High(85.15)를 앞선다 ([Alibaba Cloud 발표](https://www.alibabacloud.com/blog/alibaba-cloud-releases-qwen-image-2-0)).*

![GLM-Image — 영중 이중언어 포스터 / 인포그래픽](/images/ai-image-models-2026-h1-overview/fig19-glm-image.jpg)
*GLM-Image의 텍스트 렌더링 능력 시연. 한자·영문 혼합 레이아웃에서 글자 자형이 무너지지 않는다. CVTG-2K 영어 91.16% · LongText 중국어 97.88%로 양 영역 모두 1위 ([Zhipu AI 공식](https://z.ai/blog/glm-image)).*

오픈소스 진영에서 GLM-Image와 Qwen-Image 2.0이 텍스트 렌더링 정확도로 *폐쇄 모델을 따라잡거나 추월*한 상황이다.{{< sn >}}[Zhipu AI — GLM-Image 공식](https://z.ai/blog/glm-image) · [ComputerTech — Qwen-Image 2.0 Review](https://computertech.co/qwen-image-2-0-review/).{{< /sn >}} 특히 GLM-Image는 화웨이 Ascend Atlas 800T A2 칩으로만 훈련된 *최초의 오픈소스 프론티어 모델*로, <strong>Nvidia·AMD 없이도 경쟁 가능함을 증명</strong>하는 상징적 의미가 추가된다.

### 가성비·통합형

- **Seedream 4.5/5 Lite** — Upsampler 기본 편집 모델, API $0.018\~0.040/이미지{{< sn >}}[Upsampler — Seedream AI by ByteDance: Models Review (2026)](https://upsampler.com/blog/seedream-ai-bytedance-image-generator-editor-2026).{{< /sn >}}
- **Z-Image Turbo** — Alibaba Tongyi-MAI, 6B 파라미터, Apache 2.0, *Artificial Analysis 오픈소스 1위*, 추론 비용 $5/1,000장(최저), 16GB VRAM 소비자 GPU 실행{{< sn >}}[Tongyi-MAI — Z-Image-Turbo on HuggingFace](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) · 기술 보고서 [arXiv:2511.22699](https://arxiv.org/abs/2511.22699).{{< /sn >}}
- **Nano Banana 2** — Google Gemini 3.1 Flash Image 라인, $0.067/이미지
- **HunyuanImage 3.0** — Tencent, 80B MoE(13B 활성), 텐센트 클라우드 API $0.011/이미지
- **Kolors 2.0** — Kuaishou, ChatGLM3-6B 텍스트 인코더, Apache 2.0, INT8 양자화로 8GB VRAM 실행

![Seedream 4.5 — 텍스트·이미지 합성 편집의 정확도 1위](/images/ai-image-models-2026-h1-overview/fig09-seedream-picassoia.jpg)
*Seedream 4.5의 텍스트-이미지 합성 출력. LongText-Bench 영어 0.989·중국어 0.987로 양 언어 동시 1위 ([picassoia 리뷰](https://blog.picassoia.com/)).*

![Z-Image Turbo — 6B 오픈웨이트가 만든 포토리얼리즘](/images/ai-image-models-2026-h1-overview/fig10-z-image.png)
*Z-Image Turbo 출력. 6B 파라미터 Apache 2.0 오픈웨이트로 Artificial Analysis 오픈소스 1위, 추론 비용 $5/1,000장 ([Tongyi-MAI 블로그](https://tongyi-mai.github.io/Z-Image-blog/)).*

![HunyuanImage 3.0이 단일 프롬프트로 만든 4스타일 비교](/images/ai-image-models-2026-h1-overview/fig11-hunyuan.png)
*HunyuanImage 3.0의 4格子 출력. 단일 프롬프트로 수묵·팝아트·픽셀·수채화 4가지 스타일을 동시 생성한다. 80B MoE(13B 활성), 텐센트 클라우드 $0.011/장 ([Tencent HunyuanImage GitHub](https://github.com/Tencent-Hunyuan/HunyuanImage)).*

![Nano Banana 2 — 전통 의상 인물 사진](/images/ai-image-models-2026-h1-overview/fig20-nano-banana.webp)
*Nano Banana 2(Google Gemini 3.1 Flash Image)의 출력. 의상의 무늬·자수·옷감 질감이 자연스럽게 살아있다 ([Google DeepMind 발표](https://deepmind.google/technologies/gemini/)).*

![Kolors 2.0 — 유화 스타일의 고양이 초상](/images/ai-image-models-2026-h1-overview/fig21-kolors.png)
*Kolors 2.0(Kuaishou)의 회화 스타일 출력. ChatGLM3-6B 텍스트 인코더로 중국어 프롬프트를 네이티브 처리하며, Apache 2.0 오픈웨이트라 소비자 GPU에서도 실행 가능하다 ([Kuaishou Kolors 공식 GitHub](https://github.com/Kwai-Kolors/Kolors)).*

### 특화 영역

- **Recraft V3** — 팔로알토 스타트업. *업계 유일 SVG 네이티브 출력*. Artificial Analysis Image Arena ELO 1172로 2024년 10월부터 *5개월 이상* 1위 유지(gpt-image-2 등장 전 기준). 로고·아이콘·UI 에셋 직접 Illustrator/Figma 반입{{< sn >}}[AIToolsReview — Recraft V3 Review 2026](https://aitoolsreview.online/recraft-v3-review-2026-the-best-ai-tool-for-graphic-designers/).{{< /sn >}}
- **Reve Image 1.0** — 팔로알토 스타트업. 포토리얼리즘에서 Midjourney·Flux를 제친 평가. "Halfmoon engine"이 생성·편집·스타일 리믹스를 프롬프트로 자동 분기{{< sn >}}[Oakgen — Reve Image 1.0: The Unknown Startup That Beat Midjourney in Image Quality](https://oakgen.ai/blog/reve-image-1-review).{{< /sn >}}
- **Kling Image O1** — Kuaishou. *최대 10장 레퍼런스 이미지 동시 입력* — 가상 피팅·다중 각도 캐릭터 일관성에 특화
- **Anima** — 애니메이션 특화 2B 모델, 6GB VRAM, *합성 데이터 미사용*(수백만 애니메이션 + 80만 비애니 예술 이미지 학습)
- **Ideogram 3.0** — 텍스트 렌더링 정확도 90\~95% 유지, Custom Models for Enterprise(2026-05-15) 추가{{< sn >}}[AIUnpacking — Ideogram 3.0 Review: Still the Text-in-Image King in 2026](https://aiunpacking.com/review/ideogram/).{{< /sn >}}

![Recraft V3 — SVG 네이티브 출력 (자전거 라인 아트)](/images/ai-image-models-2026-h1-overview/fig12-recraft.svg)
*Recraft V3가 직접 생성한 SVG 벡터 파일. 업계 유일의 SVG 네이티브 출력으로 Illustrator·Figma에 곧바로 반입 가능하다 ([Replicate Recraft V3 SVG](https://replicate.com/recraft-ai/recraft-v3-svg)).*

![Reve Image 1.0 — Halfmoon 엔진 기반 포토리얼리즘](/images/ai-image-models-2026-h1-overview/fig13-reve.png)
*Reve Image 1.0 출력. Halfmoon 엔진이 생성·편집·스타일 리믹스를 프롬프트에서 자동 분기한다. 포토리얼리즘 평가에서 Midjourney·Flux를 제친 모델 ([Oakgen 리뷰](https://oakgen.ai/blog/reve-image-1-review)).*

### Flux Kontext — 별도 언급

Black Forest Labs의 FLUX.1 Kontext는 멀티턴 캐릭터 일관성 *97% (20턴 기준)*로 GPT-Image-2·Gen-4보다 느린 드리프트를 보인다. 2025년 5월 업데이트로 아이덴티티 드리프트율 *38% → 6%* 개선. KontextBench 기준 캐릭터 레퍼런스(CREF) 전 카테고리 1위.{{< sn >}}Black Forest Labs, [FLUX.1 Kontext](https://bfl.ai/models/flux-kontext); KontextBench [arXiv:2506.15742](https://arxiv.org/abs/2506.15742).{{< /sn >}}

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:1em 0;">
<figure style="margin:0;"><img src="/images/ai-image-models-2026-h1-overview/fig14-flux-kontext-input.jpg" alt="입력 — 원본 갈매기 사진" style="width:100%;height:auto;"><figcaption style="font-size:0.85em;text-align:center;color:#888;margin-top:4px;">입력</figcaption></figure>
<figure style="margin:0;"><img src="/images/ai-image-models-2026-h1-overview/fig14-flux-kontext-0.jpg" alt="1턴 편집 — 장애물 제거" style="width:100%;height:auto;"><figcaption style="font-size:0.85em;text-align:center;color:#888;margin-top:4px;">1턴: 장애물 제거</figcaption></figure>
<figure style="margin:0;"><img src="/images/ai-image-models-2026-h1-overview/fig14-flux-kontext-2.jpg" alt="2턴 편집 — 배경 교체" style="width:100%;height:auto;"><figcaption style="font-size:0.85em;text-align:center;color:#888;margin-top:4px;">2턴: 배경 교체</figcaption></figure>
<figure style="margin:0;"><img src="/images/ai-image-models-2026-h1-overview/fig14-flux-kontext-4.jpg" alt="3턴 편집 — 날씨 변경" style="width:100%;height:auto;"><figcaption style="font-size:0.85em;text-align:center;color:#888;margin-top:4px;">3턴: 날씨 변경</figcaption></figure>
</div>

*FLUX.1 Kontext의 멀티턴 편집 시퀀스. 동일한 갈매기 객체를 *장애물 제거 → 배경 이동 → 눈 날씨 적용* 순으로 편집해도 캐릭터 동일성이 유지된다 ([KontextBench, arXiv:2506.15742 Fig. 2](https://arxiv.org/abs/2506.15742)).*

## 4. 사용 사례별 표준이 바뀐 부분

![gpt-image-2가 생성한 "2025년 6대 디자인 트렌드" 6격자 인포그래픽](/images/ai-image-models-2026-h1-overview/fig06-design-trends-infographic.webp)
*단일 프롬프트가 만든 6격자 마케팅 인포그래픽. 비주얼·헤드라인·설명·태그가 한 번에 정렬된 결과물은 디자이너 없이 마케팅 파이프라인에 투입 가능한 수준이다 ([OpenAI 공식](https://openai.com/index/introducing-chatgpt-images-2-0/)).*

| 작업 | 2025년 말 권고 | 2026년 5월 이후 |
|---|---|---|
| 텍스트 포함 마케팅 배너·포스터 | Midjourney + Photoshop 합성 | **gpt-image-2 단독** (타이포 99%) |
| 컨셉 아트·에디토리얼 일러스트 | Midjourney | Midjourney V8.1 유지 (미적 천장 우위) |
| 포토리얼 제품 사진 | Midjourney 또는 SDXL | **Flux 2 Pro** (피부 질감 1위) |
| 대량 브랜드 맞춤 생성 | (불가) | **Flux 2 Dev + LoRA** (ComfyUI·fal.ai) |
| 이모지·앱 UI 목업 | (불가, 수작업 필수) | **gpt-image-2** (공간 관계 이해) |
| 캐릭터 일관성 시리즈 | 불안정 | **gpt-image-2** (Identity Drift 6%) 또는 **Flux Kontext** |
| 벡터 로고·아이콘 | (불가) | **Recraft V3** (SVG 네이티브) |
| 이중언어(중국어 포함) 자료 | (제한적) | **GLM-Image / Qwen-Image 2.0 / Seedream 4.5** |

![Flux 2 Pro의 포토리얼 제품 사진](/images/ai-image-models-2026-h1-overview/fig15-flux2-product.jpg)
*Flux 2 Pro 출력. 피부·소재 질감 평가 1위, HEX 컬러 매칭과 Pose guidance로 정확도 통제 가능. 브랜드 LoRA와 결합하면 커스터마이징 제품 이미지 파이프라인이 가능하다 ([picassoia 리뷰](https://blog.picassoia.com/flux-2-pro-review-best-ai-image-tool-2026)).*

### 추천 스택 두 가지

**미적 + 텍스트 워크 ($50/월대)**

```
Midjourney V8.1 (히어로 이미지 탐색)
    ↓
gpt-image-2 (타이포그래피 합성)
    ↓
Photoshop (마무리)
```

**비용 + 커스터마이징 (이미지당 비용 \~0)**

```
Flux 2 Dev (로컬 ComfyUI, 브랜드 LoRA)
    ↓
gpt-image-2 API (텍스트 헤비 이미지에만)
```

## 5. 이미지→영상 워크플로우의 표준화

Sora 서비스는 2026년 3월 24일 종료를 발표하고 4월 26일 다운되었다(API는 9월 24일까지 유지).{{< sn >}}[AIUnpacking — AI Video Generation in 2026: Sora, Runway, Kling, Veo](https://aiunpacking.com/guides/ai-video-generation-sora-runway-kling-veo/).{{< /sn >}} 그 공백을 다음 4종이 분담한다.

| 영상 모델 | 출시·운영 | 최대 길이 | 특화 영역 |
|---|---|---|---|
| Kling 3.0 (Kuaishou) | 2026 상반기 | 15초 (멀티샷) | 얼굴 일관성 1위, 4K 60fps, 다국어 립싱크, Director Mode로 최대 6컷 일괄 |
| Runway Gen-4.5 | 2026 상반기 | 10초 (40초 확장) | 카메라 컨트롤 1위, Aleph 인컨텍스트 편집 |
| Google Veo 3.1 | 2026-01 | 8초 | Ingredients to Video(참조 3장), 네이티브 오디오, 4K |
| Seedance 2.0 (ByteDance) | 2026 상반기 | 20초 | 텍스트·로고 일관성 1위, AA Text-to-Video ELO 1,273 1위 |

![Kling 3.0 — 이미지를 첫 프레임으로 받은 영상 워크플로우](/images/ai-image-models-2026-h1-overview/fig16-image-to-video.jpg)
*Kling 3.0의 이미지→영상 워크플로우 예시. 4K 60fps, 얼굴 일관성 1위, Director Mode로 최대 6컷 일괄 처리. Sora 종료 이후 이미지→영상 표준 모델 중 하나로 자리잡았다 ([picassoia 가이드](https://blog.picassoia.com/)).*

워크플로우의 표준 패턴은 다음과 같다.{{< sn >}}[Studiolist — AI Video Model Comparison 2026](https://studiolist.co/guides/ai-video-model-comparison-2026/), 2026-04-06.{{< /sn >}}

> "전문 스튜디오는 비디오 모델을 건드리기 전에 수백 장의 컨셉 이미지를 먼저 생성한다. 이미지 생성 단계에서 창의적 방향이 결정된다. 비디오 생성은 실행이다."

이미지 모델은 영상 모델의 *전단계*로 자리잡았다. 컨셉을 이미지로 확정한 뒤 영상으로 펼치는 게 더 *통제 가능*하다는 단계적 워크플로 인식이 굳어졌다. Veo 4는 2026년 5월 Google I/O 시점에 공식 발표가 확인되지 않았다.

## 6. 시장 구조 — 이미지 단가 94% 하락

- **이미지 단가**: 2022년 평균 \$0.36/장 → 2026년 평균 \$0.02/장 (94% 감소). 저가 배치 플랫폼(Runware) 기준 \$0.0006/장
- **생성 속도**: 2024년 평균 15초 → 2026년 4초 미만. 일부 플랫폼 2초 이하 실시간 생성 도달
- **시장 규모**: 2026년 \$4.8B\~\$12.4B 추정(기관별 차이 큼). 기업용 API 세그먼트가 연 42% CAGR로 최고 성장률

### 통합 플랫폼이 인프라가 되었다

- **fal.ai** — 2026-05-20 시리즈 D \$3억 조달, 기업가치 \$4.5B(리드: Sequoia Capital). *AWS 우선 클라우드 파트너십 체결*. 이미지 API 점유율 50%, 985개 엔드포인트. Canva·Adobe·Amazon MGM Studios에 API 공급{{< sn >}}[VentureBeat — AWS nabs white-hot gen-AI media creation startup fal](https://venturebeat.com/infrastructure/aws-nabs-white-hot-gen-ai-media-creation-startup-fal-becoming-its-preferred-cloud-provider), 2026-05-20.{{< /sn >}}
- **Replicate** — 이미지 API 점유율 15%, 1,000+개 커뮤니티 모델, fal.ai 대비 30\~50% 고가
- **Civitai** — LoRA 마켓플레이스 1위. 2025년 Visa/Mastercard 강제로 콘텐츠 정화 — 해자가 약해졌다
- **Runware** — 2026년 초 \$5,000만 시리즈 A, \$0.0006/장 공격적 가격, 40만+ 모델

### 폐쇄 vs 오픈의 경계가 *기능별로* 분화되었다

폐쇄 모델의 진짜 해자는 *품질이 아니라 분배(distribution)*다.{{< sn >}}[Startup Fortune — OpenAI's Latest Image Model Just Made Every Competitor Rethink Their Roadmap](https://startupfortune.com/openais-latest-image-model-just-made-every-competitor-rethink-their-roadmap/), 2026-04-21.{{< /sn >}}

- gpt-image-2는 ChatGPT 주간 활성 *9억 1,000만 명*의 디폴트 모델이다
- Midjourney는 *API 부재* 자체가 약점이 되었다
- Flux는 fal.ai·Replicate·HuggingFace에 분산되어 *어디서나 호출 가능*

오픈웨이트 진영은 *커스터마이징 시장*에서 압도적이다. gpt-image-2의 파인튜닝 차단이 이 격차를 굳혔다. 브랜드 LoRA·캐릭터 LoRA·도메인 LoRA를 만들려는 모든 작업은 자동으로 Flux/SDXL/Z-Image 스택으로 가게 되어 있다.

## 7. 규제·안전 — 2026년 8월 2일이 임계점이다

### EU AI Act Article 50

- **발효일**: 2026년 8월 2일
- **의무**: 생성형 AI 제공자는 모든 AI 생성 콘텐츠(이미지·오디오·비디오·텍스트)에 *머신리더블 마킹*을 부착하고 *탐지 가능*하도록 해야 한다
- **벌금**: 최대 1,500만 유로 또는 전 세계 연간 매출의 3%
- **기술 방식**: 디지털 서명 메타데이터 + 인식 불가 워터마킹 + (선택) 핑거프린팅의 *다층 마킹*
- **현재 상태**: 2026년 5월 5일 EU 집행위의 기술 솔루션 연구 보고서는 "현재 어떤 단일 기법도 모든 맥락에서 완전한 솔루션을 제공하지 못함"이라고 결론지었다.{{< sn >}}[Lexology / Herbert Smith Freehills — EU AI Act Article 50 Transparency](https://www.lexology.com/library/detail.aspx?g=4435eba2-ac62-4d03-91d6-b56a8166a733).{{< /sn >}}

### C2PA 워터마킹의 한계

- Google·Adobe·Black Forest Labs가 C2PA 표준 채택. 12개 시스템에서 메타데이터 임베딩, 8개에서 인식 불가 워터마크 확인
- 한계: *이미지 공유 시 메타데이터 제거가 용이*. C2PA 감지는 Stability AI·BFL 모델 기반 시스템에서만 일관 작동

### 딥페이크·위조 위협의 현실화

- gpt-image-2의 99% 텍스트 정확도가 *위조 문서·간판·스크린샷 생성*을 Plus 구독자 수준에서 가능하게 했다
- 딥페이크 탐지 도구 정확도: 포토리얼리스틱 AI 이미지 대상 89\~94% (arXiv 2025)
- 인간의 AI 이미지 판별 능력: <strong>38% 정확도</strong> — 50% 기준치를 밑돈다 (Science 2025)

## 가장 흥미로운 지점

세 가지가 특히 인상적이다.

**첫째, gpt-image-2의 +242 ELO 도약이 보여주는 것**. 직전까지 *모든 메이저 모델이 70 ELO 밴드 안에 밀집*해 있었다 — 시장이 *능력 천장에 거의 도달했다*는 인식이 합의에 가까웠다. 그 천장을 한 모델이 단번에 깨고 솟아오른 사건은, 능력 천장이 "오랜 시간에 걸친 점진 개선"이 아니라 "특정 아키텍처 도약"으로 갑자기 이동할 수 있음을 다시 확인시켰다. *Reasoning을 이미지 생성에 이식*했다는 단 한 가지 설계 선택이 만든 격차다.

**둘째, 폐쇄 모델의 해자가 품질이 아니라 분배라는 사실**. AI 모델 비즈니스 전반의 구조적 통찰이다. ChatGPT 9.1억 주간 활성 사용자가 gpt-image-2의 디폴트가 되는 순간, 다른 어느 모델도 *비교 우위*만으로는 그 분배를 무너뜨리지 못한다. 반대로 *분배가 약한 영역*(파인튜닝, 로컬 실행, 특정 도메인 LoRA)에서는 오픈웨이트가 자동으로 승리한다. 두 진영의 경계가 *기능별로 깔끔하게 분화*된 것은 우연이 아니라 구조의 산물이다.

**셋째, 중국 진영의 약진이 보여주는 다층적 신호**. Qwen·Seedream·GLM-Image·Z-Image·Hunyuan·Kolors·Kling이 텍스트 렌더링·이중언어·가성비·오픈웨이트 영역 *각각의 1위*를 차지하고 있다. 이건 단순한 모델 경쟁이 아니다 — GLM-Image가 화웨이 Ascend로만 훈련됐다는 사실, Qwen이 Apache 2.0으로 상업적 이용을 풀었다는 사실, ByteDance의 Seedream이 LongText-Bench를 영중 양 언어로 동시 1위를 잡았다는 사실이 합쳐지면, *AI 인프라의 디커플링*이 모델 수준에서 실제로 진행 중임을 보여준다. 2026년 하반기에 이 흐름이 어떻게 확장될지가 다음 라운드의 관전 포인트다.
