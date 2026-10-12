---
title: "Iris-3B의 100스텝을 4스텝으로 줄인 Turbo LoRA"
date: 2026-10-12T13:30:00+09:00
tags: ["이미지 생성", "확산 모델", "LoRA", "추론 효율성", "오픈소스"]
categories: ["모델과 연구"]
summary: "Speridlabs가 공개한 30억 파라미터 이미지 생성 모델 Iris-3B는 VAE 없이 픽셀을 직접 만드는 대신, 기본 설정에서 1024×1024 이미지 한 장에 포워드 패스가 약 200번 필요했다. 일본 개발자 pentacoxian은 증류 기법 DMD2로 CFG까지 학습시킨 4스텝 LoRA를 만들어 생성 시간을 RTX 5090에서 0.68초, M3 Max에서 약 11초로 줄였고, 공개 하루 동안 사용자들이 RTX 5090, 아이폰, 스냅드래곤 NPU에서 실행한 결과를 올렸다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/00-cover.jpg"
  alt: "Iris-3B 속도 비교 데모 화면. 왼쪽에 거실 소파에 앉아 텔레비전을 보는 너구리를 묘사한 프롬프트와 Fast 모드 선택이 있고, 오른쪽에 생성된 너구리 사진이 있다. 아래 표에는 4스텝, 포워드 4번, 0.9초, 100스텝 대비 49.8배라고 적혀 있다. 사용자 jun1228909가 RTX 5090에서 녹화한 영상의 한 장면이다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/00-cover.jpg"
---

<style>
.post-content figure.iris-fig{margin:1.1em 0 1.4em}
.post-content figure.iris-fig img{display:block;width:auto;max-width:100%;height:auto;max-height:80vh;margin:0 auto;border-radius:6px}
.post-content figure.iris-fig video{display:block;width:100%;height:auto;max-height:80vh;background:#111;border-radius:6px}
.post-content figure.iris-fig>figcaption{margin:.5em 0 0;font-size:.86em;font-weight:400;line-height:1.55;text-align:left;color:var(--secondary)}
</style>

## 3줄 요약

1. 일본 개발자 pentacoxian(@pentacoxian_dev)이 2026년 10월 11일, Speridlabs가 사흘 전 공개한 이미지 생성 모델 Iris-3B를 4스텝 만에 생성하도록 만드는 Turbo LoRA와 코드를 공개했다.
2. Iris-3B는 VAE를 거치지 않고 픽셀을 직접 생성하는 30억 파라미터 모델이다. 기본 설정(100스텝, 매 스텝 CFG)에서는 1024×1024 이미지 한 장을 만드는 데 포워드 패스가 약 200번 필요해서, M3 Max 노트북에서 9\~11분이 걸렸다.
3. pentacoxian은 증류 기법 DMD2로 CFG의 효과까지 LoRA에 학습시켜 포워드 패스를 4번으로 줄였다. 생성 시간은 RTX 5090에서 0.68초, M3 Max에서 약 11초가 됐고, 공개 하루 동안 여러 사용자가 Space 데모와 RTX 5090, 아이폰, 스냅드래곤 NPU에서 실행한 결과를 올렸다.

## 트윗 타래와 인용 관계

pentacoxian의 원 트윗은 두 편짜리 타래다. 첫 트윗의 내용은 다음과 같다.

> Iris-3B의 100스텝을 4스텝으로 줄인 Turbo LoRA를 만들었습니다. 빠르면 1초 안에 1024x1024 픽셀 공간 확산(Pixel space diffusion) 이미지를 생성할 수 있습니다!
>
> 픽셀 공간에서 직접 생성하는 방식(VAE 없음)은 디테일에 강한 반면 계산이 무거워서, 원래의 100스텝으로는 M3 Max에서 몇 분에서 십수 분이 걸리는 것이 약점이었습니다. 이것을 4스텝과 CFG 베이크로 단번에 개선했습니다.
>
> - RTX 5090: 약 0.7초
> - M3 Max: 약 11초(`--preset mac16`에서 피크 약 7GB)
>
> 허깅페이스 Spaces 데모도 있으니 꼭 속도를 체감해 보세요!

두 번째 트윗에는 코드 저장소(GitHub `pentaCoxian/iris-3b-turbo`)와 LoRA 가중치(Hugging Face `pentacoxian-dev/iris-3b-turbo-lora`) 링크가 있다. 원 트윗은 일본의 AI 해설 계정 studio_yebisu가 Iris-3B를 소개한 글을 인용했고, 그 글은 다시 Speridlabs의 공개 트윗을 인용했다.

## Iris-3B는 어떤 모델인가

Iris-3B는 Speridlabs가 2026년 10월 8일 X에 공개한 텍스트 투 이미지 모델이다.[^dates] 저자는 Hanqiu Li Cai와 Chema Garabito 두 사람이다. 공개 트윗은 모델을 이렇게 소개했다.

> Iris-3B를 소개합니다. 모든 픽셀을 직접 생성하는 픽셀 공간 텍스트 투 이미지 모델이자 범용 비전 학습기입니다. VAE는 없습니다. 처음부터 사전학습한 30억 파라미터 모델이고 가중치를 공개합니다. 디테일이 중요한 비전 과제인 깊이 추정과 이미지 복원에서 이 모델의 생성 사전지식도 탐구했습니다. 가중치, 코드, 데모 모두 공개입니다(Apache 2.0).

<figure class="iris-fig">
<video controls preload="none" playsinline poster="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/speridlabs-iris-reel.jpg">
  <source src="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/speridlabs-iris-reel.mp4" type="video/mp4">
  <a href="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/speridlabs-iris-reel.mp4">영상 파일 열기</a>
</video>
<figcaption>Speridlabs의 공개 영상(43초). 생성 예시에 이어 잠재 확산 방식과 Iris-3B의 파이프라인을 비교하는 도식이 나오고, 깊이 추정과 이미지 복원 결과가 이어진다. 출처: <a href="https://x.com/speridlabs/status/2108241672291438830">@speridlabs</a></figcaption>
</figure>

### VAE를 뺀다는 것의 의미

Stable Diffusion이나 FLUX 같은 기존 이미지 생성 모델은 VAE(변분 오토인코더)라는 별도의 신경망을 쓴다. VAE가 이미지를 작은 압축 표현으로 바꾸면, 생성 모델은 그 압축 표현(잠재 공간)에서 이미지를 만들고, 마지막에 VAE가 압축 표현을 다시 이미지로 복원한다. 압축 덕분에 계산량이 크게 줄어 고해상도 이미지를 다루기 쉬워졌다.

그 대가로 압축과 복원 과정에서 작은 글자나 가는 선 같은 세부가 손실될 수 있다. studio_yebisu의 해설은 이 점을 이렇게 설명했다. 생성 모델이 아무리 잘 만들어도, 마지막에 이미지로 되돌리는 VAE가 표현하지 못하는 세부는 결과에 나타나지 않는다. Iris-3B는 VAE 없이 RGB 픽셀을 직접 생성해서 이 제약을 없앴다. Speridlabs는 VAE의 잠재 표현이 정보를 잃는 압축이고 질감 위주로 편향되어 있다고 설명했다.

### 구조

| 항목 | 내용 |
| --- | --- |
| 파라미터 | 30억(고정된 텍스트 인코더 제외) |
| 입력 단위 | 이미지를 16×16 픽셀 패치로 잘라 처리 |
| 본체 | 폭 2560의 트랜스포머 블록 24개. 이미지와 텍스트에 각각 다른 가중치를 쓰는 블록 8개, 둘을 한 흐름으로 처리하는 블록 16개 |
| 픽셀 헤드 | 작은 픽셀 트랜스포머(PiT) 블록 4개가 각 패치 토큰을 다시 픽셀로 복원 |
| 텍스트 인코더 | Qwen3-VL-4B-Instruct(학습하지 않고 고정) |
| 학습 목표 | 정류 흐름(rectified flow) |

2차원 RoPE 위치 인코딩을 써서 가중치 한 벌로 100만 화소 이하의 여러 해상도와 가로세로 비를 생성한다. 패치 단위 트랜스포머 뒤에 픽셀 단위 트랜스포머를 두는 2단 설계는 PixelDiT 논문의 구조를 따랐고, 코드는 독자적으로 구현했다고 밝혔다.

학습은 256², 512², 1024² 해상도의 3단계 사전학습과 지도 미세조정으로 이루어졌다. 총 66만 5천 스텝이다. 첫 단계에서는 DINOv2의 표현에 내부 표현을 맞추는 REPA 기법을 함께 썼고, 옵티마이저는 Muon과 AdamW를 섞어 썼다. 학습 코드와 설정 파일도 모두 공개했다.

### 벤치마크

Speridlabs는 공식 평가기로 1024² 해상도에서 프롬프트 재작성이나 여러 장 중 최선 고르기 없이 측정한 점수를 공개했다. 일부 모델만 옮기면 다음과 같다.

| 모델 | GenEval | DPG | LongText | OneIG |
| --- | --- | --- | --- | --- |
| FLUX.1-dev 12B | 0.66 | 83.8 | 0.607 | 0.434 |
| HiDream-I1-Full | 0.83 | 85.89 | 0.543 | 0.477 |
| Z-Image 6B[^zimage] | 0.84 | 88.1 | 0.935 | 0.546 |
| Qwen-Image 20B | 0.87 | 88.3 | 0.943 | 0.539 |
| **Iris-3B** | 0.798 | 86.52 | 0.857 | 0.540 |

OneIG 점수는 Qwen-Image 20B와 같은 수준이다. studio_yebisu는 파라미터가 절반 이하인데도 이 점수가 나온 점을 강조했다. GenEval과 긴 글자 렌더링을 보는 LongText에서는 Qwen-Image와 Z-Image가 더 높다. Speridlabs는 이 성능을 경쟁 모델 학습 연산량의 일부로 달성했다고 주장했다.

### 깊이 추정과 이미지 복원, 그리고 논문의 결론

Speridlabs가 Iris-3B를 범용 비전 학습기라고 부르는 이유는 같은 본체를 구조 변경 없이 미세조정해 다른 과제에도 쓰기 때문이다. 사진을 넣으면 앞뒤 거리를 나타내는 깊이 지도를 출력하는 모델과, 열화된 이미지를 복원하며 4배로 키우는 모델이 함께 공개됐다. 두 모델 모두 빈 프롬프트로 포워드 패스 한 번에 결과를 낸다.

그런데 arXiv 논문의 초록은 이 연구가 출발한 가설에 부정적인 결론을 적었다. VAE의 손실이 없으니 세부가 중요한 과제에서 픽셀 공간 모델이 유리할 것이라는 가설을 검증했는데, 픽셀 공간 사전지식을 쓴 이점이 유의미하게 나타나지 않았다는 것이다. 깊이 추정에서는 Iris-3B와 잠재 공간 모델인 FLUX.2 Klein이 비슷했고, 4배 복원에서는 어느 픽셀 공간 모델도 잠재 공간 FLUX.2 Klein보다 높은 점수를 내지 못했다. 저자들은 그럼에도 픽셀 공간 사전학습이 30억 파라미터 규모까지 확장되고 잠재 공간 모델과 경쟁할 수 있는 생성 품질을 낸다는 것은 보였다고 정리했다. studio_yebisu도 "이것으로 글자와 세부가 모두 좋아진다는 것까지는 실증되지 않았다"고 적었다.

## 100스텝이 왜 느린가

확산 모델은 노이즈에서 출발해 이미지를 여러 단계에 걸쳐 조금씩 다듬는다. 한 단계마다 신경망 전체를 한 번 실행하는 포워드 패스가 필요하다. 여기에 CFG(classifier-free guidance)를 쓰면 단계마다 프롬프트를 넣은 계산과 넣지 않은 계산을 둘 다 하고 그 차이를 키워 프롬프트를 더 충실히 따르게 한다. 단계마다 포워드 패스가 두 번이다.

Iris-3B의 기본 샘플러는 DPM-Solver++ 100스텝에 CFG 3을 매 스텝 적용한다. 이미지 한 장에 포워드 패스가 약 200번이다. pentacoxian의 측정에 따르면 M3 Max(40코어 GPU)에서 1024×1024 포워드 패스 한 번은 CFG를 포함하면 약 6.4초, CFG 없이 약 3.1초가 걸린다. 기본 설정으로 이미지 한 장을 만드는 데 약 11분이 걸리는 셈이다.

## 첫 번째 최적화: 학습 없이 줄이기

pentacoxian은 Speridlabs의 저장소를 포크한 `iris-3b-turbo`에 먼저 학습이 필요 없는 가속 옵션 세 가지를 추가했다. 세 옵션 모두 품질을 일부 희생하므로 자기 프롬프트로 기본값과 비교해 보라고 권했다.

| 옵션 | 동작 |
| --- | --- |
| `--steps 30` | 2차 DPM-Solver++는 보통 100스텝보다 훨씬 적은 단계로도 충분하다. 비용은 단계 수에 비례한다. |
| `--cfg-interval 0 0.9` | 노이즈가 가장 많은 초반 단계에서는 CFG를 생략해 포워드 패스를 한 번만 한다. 시간 이동값 4를 쓰는 설정에서는 전체 단계의 약 3분의 1이 여기에 해당한다. |
| `--cache-threshold 0.1` | 인접한 두 단계에서 첫 번째 블록의 입력이 거의 바뀌지 않으면 본체의 출력을 재사용한다. 재사용한 단계의 비용은 전체 단계의 약 15%다. 픽셀 헤드는 항상 현재 이미지로 다시 계산하고, 재사용은 최대 3단계 연속까지만 한다. |

M3 Max에서 `--steps 30 --cfg-interval 0 0.9`를 쓰면 약 2.6분이 걸렸다. 여기에 캐시 옵션까지 더한 측정에서는 30단계 중 18단계에서 본체 출력을 재사용했고 77초가 걸렸다. 11분이 77초가 됐어도 노트북에서 한 장을 기다리기에는 여전히 긴 시간이다.

## 두 번째 최적화: Turbo LoRA

### 증류와 CFG 베이크

Turbo LoRA는 증류(distillation)로 만들었다. 100스텝으로 이미지를 만드는 원래 모델을 교사로 두고, 4스텝 만에 비슷한 이미지를 만들도록 학생 모델을 학습시키는 방식이다. 교사는 CFG 3을 적용한 상태의 원래 모델이므로, 학생은 CFG가 적용된 결과를 포워드 패스 한 번으로 내도록 배운다. 트윗에서 말한 "CFG 베이크"가 이 방식이다. 그 결과 단계마다 포워드 패스가 한 번으로 줄어, 이미지 한 장에 필요한 포워드 패스가 약 200번에서 4번이 됐다.

증류 방법은 DMD2(분포 일치 증류)에서 GAN 항을 뺀 형태다. DMD 계열은 학생의 출력 하나하나를 교사의 출력과 맞추지 않는다. 대신 학생이 만드는 이미지들의 분포가 교사의 분포와 같아지도록 학습한다. 이를 위해 학생이 만든 이미지만 보고 학습하는 비평자(critic) 모델을 따로 둔다. 학생의 이미지에 노이즈를 섞어 교사와 비평자에게 각각 노이즈를 제거하게 하면, 두 예측의 차이는 학생의 분포가 교사의 분포와 얼마나 다른지를 알려 준다. 학생은 이 차이가 줄어드는 방향으로 갱신된다.

### 가중치 한 벌로 세 모델 운용하기

교사, 학생, 비평자는 원래 모델의 bf16 가중치 한 벌을 함께 쓴다. 이 가중치는 고정하고, 학생과 비평자에는 각각 LoRA 어댑터를 하나씩 추가했다. 교사는 어댑터 없는 원래 가중치 그대로다. 학습하는 것은 랭크 64짜리 어댑터 두 개뿐이다.

학습 데이터로 이미지를 쓰지 않았다는 점도 특징이다. 학생이 만든 이미지와 교사의 판단만으로 학습하므로 프롬프트만 있으면 된다. PartiPrompts 1,632개 전부와 improved-flux-prompts에서 뽑은 6,000개, 합계 7,632개의 프롬프트를 썼다. 학습은 RTX 5090 한 장(반복당 약 1.4초, 메모리 약 18GB)으로 했고, 텍스트 인코더는 별도의 RTX 4090에서 돌렸다.

### 학습 세부

- 학생은 시간 t = 1.0, 0.923, 0.8, 0.571의 4단계로 이미지를 만든다. 한 단계를 마치면 예측한 이미지에 새 노이즈를 섞어 다음 단계의 입력으로 쓴다.
- 학습에는 역방향 시뮬레이션을 썼다. 학생을 그래디언트 없이 무작위 횟수만큼 먼저 돌린 뒤 마지막 한 단계에만 그래디언트를 계산한다. 학생은 추론 때 실제로 받게 될 중간 입력으로 학습한다.
- 학생을 한 번 갱신할 때 비평자는 다섯 번 갱신한다. 학생의 분포가 바뀌는 속도에 맞춰 비평자도 충분히 학습되어야 하기 때문이다.[^hparams]
- 어댑터는 패치 임베딩, 시간 임베딩, 트랜스포머 블록, 픽셀 단계, 최종 층의 모든 선형 층에 적용했다. 어댑터 하나는 약 1억 1,500만 파라미터, fp32로 460MB다.
- 학습은 반드시 100만 화소 안팎의 해상도에서 해야 한다. 원래 체크포인트가 512×512에서 16픽셀 크기의 블록 모양 결함을 보이기 때문에, 그 해상도에서 학습한 학생은 결함까지 배운다.

### 두 번의 학습과 공개 버전

첫 번째 학습(r1)은 학습률 5e-5로 처음부터 진행했다. 1,500번째와 1,750번째 반복 사이에 학생이 질감만 남은 이미지를 내는 상태로 붕괴해서, 붕괴 직전인 1,500번째 반복을 `r1-1500`으로 공개했다. 이 버전은 일부 시드에서 여우 두 마리가 몸 하나를 공유하는 식으로 피사체를 합쳐 버린다.

두 번째 학습(r2)은 `r1-1500`에서 이어서 학습률을 절반(2.5e-5)으로 낮추고 학생 가중치의 지수이동평균(EMA)을 함께 유지했다. 미리보기 이미지의 대비가 떨어지면 자동으로 멈추는 장치도 넣었다. r2는 1,500번째 반복까지 붕괴하지 않았고, 눈으로 비교해 1,000번째 반복(누적 2,500번)을 `r2-1000`으로 골라 권장 버전으로 공개했다.

<figure class="iris-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/turbo-lora-r1-r2-samples.jpg" alt="같은 프롬프트와 시드로 만든 4스텝 생성 결과 비교. 위 줄은 나뭇잎 위의 깡충거미 접사 사진이고 털과 눈의 세부가 선명하다. 아래 줄은 VISIT THE MOON이라고 쓰인 빈티지 여행 포스터인데, 글자가 반복되고 일부가 뭉개져 있다. 왼쪽이 r1-1500, 오른쪽이 r2-1000이다." loading="lazy">
<figcaption>왼쪽은 r1-1500, 오른쪽은 r2-1000. 같은 프롬프트와 시드 7로 1024×1024 이미지를 4스텝에 생성했다. 거미의 털 같은 세부는 잘 나오지만 포스터의 글자는 반복되거나 뭉개진다. 출처: <a href="https://huggingface.co/pentacoxian-dev/iris-3b-turbo-lora">pentacoxian-dev/iris-3b-turbo-lora</a> 모델 카드의 비교 이미지 일부, Apache-2.0</figcaption>
</figure>

## 세 번째 최적화: 메모리 16GB 맥에서 돌리기

`--preset mac16`은 메모리 16GB인 맥에서 실행하기 위한 설정이다. 네 가지를 조합한다.

1. 프롬프트 인코딩은 잠깐 실행되는 별도 프로세스에서 끝낸다. 텍스트 인코더와 이미지 모델이 메모리에 동시에 올라가지 않는다.
2. 이미지 모델은 텐서 단위로 하나씩 GPU 메모리에 옮기고, 옮기는 동안 LoRA를 병합한다.
3. 텍스트 인코더와 이미지 본체의 가중치를 int8로 양자화한다.
4. 이미지를 한 장씩 생성한다.

GPU 메모리 할당을 16GB 맥의 작업 한도인 약 10.7GB로 제한한 M3 Max에서 측정한 피크 메모리는 다음과 같다.

| 설정 (1024², Turbo) | 피크 메모리 |
| --- | --- |
| FP32 가중치, 텍스트 인코더 상주 | 30.3GB |
| BF16 가중치(기본값), 텍스트 인코더 상주 | 24.3GB |
| `--preset mac16 --quantize none` | 9.3GB |
| `--preset mac16` (int8) | 6.9GB |

int8 양자화 뒤에도 텍스트 임베딩의 코사인 유사도는 0.9999를 유지했고, 4스텝 생성 결과는 bf16 대비 PSNR 28\~38dB로 눈으로 보기에 차이가 없었다고 한다.

## 결과: 속도 정리

모델 카드에 실린 측정값이다. 1024×1024, 예열 후, 프롬프트 인코딩을 포함한 전체 시간이다.[^speed]

| 하드웨어 | 4스텝 Turbo | 비고 |
| --- | --- | --- |
| NVIDIA RTX 5090 (bf16) | 장당 0.68초 | 배치 1에서 분당 88장 |
| Hugging Face ZeroGPU | GPU 시간 약 1.1초 | 요청마다 ZeroGPU 연결에 약 3초 추가 |
| Apple M3 Max 40코어 GPU (bf16) | 장당 약 10\~11초 | |
| Apple M3 Max, `--preset mac16` (int8) | 장당 약 11초 | 피크 메모리 약 7GB |

같은 M3 Max에서 원래 모델의 기본 100스텝 샘플러는 장당 약 9\~11분이 걸린다. 저장소에는 같은 프롬프트와 시드로 Fast(4스텝 Turbo), Balanced(학습 없는 30스텝 설정), Standard(100스텝) 세 모드의 시간을 재는 Gradio 페이지 `demo/speed.py`도 들어 있다.

## 공개 하루 동안의 사례

원 트윗에는 직접 실행한 결과를 덧붙인 인용 글이 여러 건 달렸다. 영상이나 측정값이 있는 네 건을 옮긴다.

### Space 데모에서 1.12초

studio_yebisu는 pentacoxian의 Hugging Face Space에서 1024×1024 인물 사진을 생성하는 화면을 녹화해 올렸다. 화면 아래에 `r2-1000` 어댑터, 4스텝, GPU에서 1.12초라는 표시가 나온다. 그는 "VAE 없이 1024×1024 이미지를 1.12초에 만드는 것은 너무 빠르다"며, 발표된 지 이틀 된 모델을 고속으로 개조해 GitHub와 Hugging Face에 이미 공개한 데 놀랐다고 적었다. Speridlabs의 공동 저자 Chema Garabito가 이 글을 리트윗했다.

<figure class="iris-fig">
<video controls preload="none" playsinline muted loop poster="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/studio-yebisu-space-demo.jpg">
  <source src="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/studio-yebisu-space-demo.mp4" type="video/mp4">
  <a href="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/studio-yebisu-space-demo.mp4">영상 파일 열기</a>
</video>
<figcaption>Iris-3B Turbo Space에서 Generate를 누르자 비 오는 밤거리의 인물 사진이 나온다. 결과 아래에 4스텝, GPU 1.12초라고 표시된다. 출처: <a href="https://x.com/studio_yebisu/status/2109227478484992466">@studio_yebisu</a></figcaption>
</figure>

### RTX 5090에서 0.9초

jun1228909는 "RTX 5090 약 0.7초"라는 문장을 보고 직접 시험했다. 로컬에서 `demo/speed.py`를 띄우고 Fast 모드로 고양이, 눈 덮인 숲의 사슴, 해변을 달리는 남녀, 우주 헬멧을 쓴 오리, 텔레비전을 보는 너구리를 연달아 생성했다. 측정표에는 장당 0.9초, 포워드 한 번에 약 229ms, 분당 약 65장, 100스텝 샘플러(측정한 포워드 시간으로 추정한 45초) 대비 49.8배라고 나온다. 그는 "생성 시간이 1초 미만이라는 것은 초당 1프레임짜리 영상을 실시간으로 생성할 수 있다는 뜻"이라고 덧붙였다.

<figure class="iris-fig">
<video controls preload="none" playsinline muted loop poster="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/jun-rtx5090-turbo.jpg">
  <source src="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/jun-rtx5090-turbo.mp4" type="video/mp4">
  <a href="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/jun-rtx5090-turbo.mp4">영상 파일 열기</a>
</video>
<figcaption>속도 비교 페이지에서 프롬프트를 바꿔 붙여 넣고 Generate를 누를 때마다 1초 안에 새 이미지가 나온다. 표에는 매번 0.9초, 49.8배가 기록된다. RTX 5090, bf16 가중치. 출처: <a href="https://x.com/jun1228909/status/2109272091438760225">@jun1228909</a></figcaption>
</figure>

### 아이폰 15 Pro에서 200초

SORA_LNV는 자신이 만든 로컬 모델 실행 앱에서 이 LoRA를 쓸 수 있게 했다. 4비트로 양자화한 Iris 본체에 fp32 `r2-1000` LoRA를 적용했고, 메모리 사용량을 기준치보다 적게 유지하도록 모델을 분할 처리해 실행했다. 아이폰 15 Pro에서 4스텝 생성에 200.6초가 걸렸다. 같은 프롬프트를 Space에서 생성하면 2.07초였다. 그는 두 결과물의 품질을 구별할 수 없다고 적었다.

<figure class="iris-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/sora-space-vs-iphone.jpg" alt="왼쪽은 Iris-3B Turbo Space 화면으로, 노을 진 후지산 이미지 아래에 4스텝, GPU 2.07초가 표시된다. 오른쪽은 아이폰 앱의 생성 정보 화면으로, Iris Q4와 F32 LoRA r2-1000, 4스텝, 1024×1024, 실측 시간 200.6초가 적혀 있다." loading="lazy">
<figcaption>같은 프롬프트 "Japan's beautiful mountain, Mount Fuji, with the sunset"를 Space(왼쪽, 2.07초)와 아이폰 15 Pro 로컬 실행(오른쪽, 200.6초)으로 생성했다. 출처: <a href="https://x.com/SORA_LNV/status/2109270901657366890">@SORA_LNV</a></figcaption>
</figure>

### 스냅드래곤 X Elite NPU

Zimo41650079726은 Iris-3B 본체 전체를 스냅드래곤 X Elite의 NPU에서 FP16으로 실행했다. 1024×1024 기준으로 Turbo 2스텝에 35초, Turbo 4스텝에 68초가 걸렸고, LoRA 없이 CFG 1로 20스텝 생성하면 319초가 걸렸다.

<figure class="iris-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/iris-3b-turbo-lora/snapdragon-npu-turbo-vs-base.jpg" alt="금발에 검은 고딕 드레스를 입은 인물 사진 세 장을 나란히 놓은 비교 이미지. 왼쪽부터 Turbo 2스텝, Turbo 4스텝, LoRA 없는 20스텝 CFG 1로 생성했다." loading="lazy">
<figcaption>왼쪽부터 Turbo 2스텝(35초), Turbo 4스텝(68초), LoRA 없이 20스텝(319초). 스냅드래곤 X Elite NPU 실행. 출처: <a href="https://x.com/Zimo41650079726/status/2109311194641392038">@Zimo41650079726</a></figcaption>
</figure>

같은 날 다른 개발자도 Turbo LoRA와 무관한 방식으로 Iris-3B를 가속한 결과를 공개했다.[^others]

## 한계

pentacoxian은 모델 카드에 한계를 직접 적었다.

- **정성 평가뿐이다.** FID나 GenEval 같은 벤치마크는 돌리지 않았고, 고정한 프롬프트와 시드에서 눈으로 품질을 판단했다.
- **글자 표현이 약하다.** 단어가 반복되거나 뭉개지는 경우가 많다.
- **일부 시드에서 구도 오류가 생긴다.** 피사체가 합쳐지거나 중복되며, r1-1500에서 더 자주 나타난다.
- **결과의 다양성이 원래 샘플러보다 좁다.** DMD 계열 학생은 대비가 강하고 전형적인 이미지를 선호한다.
- **100만 화소 안팎에서만 시험했다.** 1024×1024와 그에 가까운 가로세로 비만 확인했다.
- **adaLN 핵심부의 어댑터가 작동하지 않았다.** 공개한 두 버전에서는 버그 때문에 시간 정보를 조절하는 adaLN 공유 모듈의 어댑터가 포워드 패스에 한 번도 쓰이지 않았다. 그래서 이 어댑터의 값은 정확히 0이고, 단계별 시간 조절은 학습되지 않았다. 버그는 포크에서 고쳤고 다음 학습부터 이 부분도 학습한다.

## 가장 흥미로운 지점

내가 오래 곱씹은 것은 Iris-3B가 공개 일주일 사이에 얻은 두 가지 평가의 대비다. 논문은 VAE를 빼면 세부가 중요한 과제에서 유리할 것이라는 출발 가설에 스스로 부정적인 결론을 적었다. 그런데 공개 트윗 사흘 뒤, 다른 사람이 만든 LoRA 하나로 이 모델은 노트북과 아이폰에서도 실행되는 가볍고 빠른 생성 모델이 됐다. 연구진이 세운 가설은 입증되지 않았지만, 가중치와 학습 코드를 Apache 2.0으로 공개했기 때문에 외부 개발자가 사흘 만에 이 모델의 새 용도를 만들 수 있었다.

포워드 패스 200번을 4번으로 줄인 과정도 눈여겨볼 만하다. 학습한 것은 이미지 한 장 없이 프롬프트 7,632개와 랭크 64 어댑터 두 개뿐이고, GPU는 RTX 5090 한 장이었다. 게다가 어댑터의 일부가 버그로 0인 상태였는데도 이 결과가 나왔다. 그 부분까지 학습한 다음 버전이 얼마나 달라질지는 아직 아무도 모른다.

## 출처

- pentacoxian(@pentacoxian_dev), [Iris-3B Turbo LoRA 공개 트윗 타래](https://x.com/pentacoxian_dev/status/2109221724609024012), 2026-10-11
- pentacoxian, [pentaCoxian/iris-3b-turbo](https://github.com/pentaCoxian/iris-3b-turbo) (GitHub, Speridlabs 저장소의 포크)
- pentacoxian, [pentacoxian-dev/iris-3b-turbo-lora](https://huggingface.co/pentacoxian-dev/iris-3b-turbo-lora) (Hugging Face 모델 카드), [Iris-3B Turbo Space](https://huggingface.co/spaces/pentacoxian-dev/iris-3b-turbo)
- studio_yebisu, [Iris-3B 해설 트윗](https://x.com/studio_yebisu/status/2108309589183881560), 2026-10-08
- Speridlabs(@speridlabs), [Iris-3B 공개 트윗](https://x.com/speridlabs/status/2108241672291438830), 2026-10-08
- Speridlabs, [Iris-3B 프로젝트 페이지](https://speridlabs.com/research/iris), [speridlabs/iris-3b](https://github.com/speridlabs/iris-3b) (GitHub), [speridlabs/iris-3b](https://huggingface.co/speridlabs/iris-3b) (Hugging Face)
- Hanqiu Li Cai, Chema Garabito, [Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning](https://arxiv.org/abs/2610.09450), arXiv:2610.09450, 2026-10-07
- 사용자 사례: [@studio_yebisu](https://x.com/studio_yebisu/status/2109227478484992466), [@jun1228909](https://x.com/jun1228909/status/2109272091438760225), [@SORA_LNV](https://x.com/SORA_LNV/status/2109270901657366890), [@Zimo41650079726](https://x.com/Zimo41650079726/status/2109311194641392038), 2026-10-11

[^dates]: 프로젝트 페이지의 게시일은 10월 5일, arXiv 제출일은 10월 7일, X 공개 트윗은 10월 8일(UTC)이다.

[^zimage]: Z-Image 6B의 점수는 프롬프트 재작성을 사용한 결과다. 다른 모델의 점수는 Qwen-Image와 Z-Image 보고서에서 가져왔다고 Speridlabs가 밝혔다.

[^hparams]: 그 밖의 설정은 다음과 같다. DMD 노이즈 수준은 시간 이동 전 기준 t ∈ [0.02, 0.98], DMD 그래디언트는 샘플마다 정규화, 옵티마이저는 AdamW(betas 0, 0.999), 배치 1, 해상도 1024×1024, 그래디언트 클리핑 1.0이다.

[^speed]: 저장소 README에는 4스텝 생성이 M3 Max에서 약 11\~13초, RTX 5090에서 약 0.9초라고 적혀 있다. 트윗과 모델 카드의 0.68초(약 0.7초)는 예열 뒤 측정값이다. jun1228909의 영상에 나오는 0.9초도 프롬프트 인코딩을 포함한 값이다.

[^others]: 같은 날 ANAg2bGOD는 Turbo LoRA와 별개로 Apple Silicon용 추론 엔진을 공개했다. 자신의 맥북에서 10스텝 추론이 원래 구현의 346초에서 42초로 약 8.2배 빨라졌고, 피크 메모리는 약 10GB이며, 깊이 추정과 4배 복원도 지원하는 macOS 앱을 함께 제공한다고 밝혔다([트윗](https://x.com/ANAg2bGOD/status/2109383597497233506)).
