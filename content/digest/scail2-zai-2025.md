---
title: "SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning"
date: 2026-06-09T23:30:00+09:00
tags: ["AI", "비디오 생성", "캐릭터 애니메이션", "디퓨전 모델", "오픈소스"]
categories: ["모델과 연구"]
summary: "Z.ai가 공개한 SCAIL-2는 포즈 스켈레톤·인페인팅 마스크 같은 중간 표현을 거치지 않고 driving 비디오 latent를 시퀀스에 직접 이어 붙여 캐릭터 애니메이션을 end-to-end로 합성한다. 60K motion pair 데이터셋, in-context mask conditioning, mode-specific RoPE, Bias-Aware DPO를 결합하여 동물 driving과 egocentric 같은 제로샷 능력까지 끌어냈다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/scail2-zai-2025/teaser.png"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/scail2-zai-2025/teaser.png"
---

## 3줄 요약

1. Z.ai(zai-org)가 SCAIL-2를 공개했다. 14B 비디오 디퓨전 모델 기반의 캐릭터 애니메이션 프레임워크로, 추론 코드·체크포인트·기술 보고서·프로젝트 페이지가 모두 공개돼 있다.
2. 핵심 주장은 *중간 표현 의존을 끊는다* 한 가지다. 포즈 스켈레톤, 인페인팅 마스크 같은 intermediate 대신 driving 비디오의 latent를 시퀀스에 직접 결합하여 motion을 옮긴다. 다중 캐릭터 상호작용에서 깊이가 모호한 스켈레톤 겹침이 사라지고, body shape 제약도 풀린다.
3. End-to-end 데이터가 부족한 문제는 *합성 파이프라인*으로 푼다. SCAIL-Preview, Wan-Animate, MoCha를 데이터 제너레이터로 묶어 MotionPair-60K를 만들고, 손가락처럼 미세 영역의 합성 편향은 Bias-Aware DPO로 보정했다. 동물 driving과 egocentric driving 같은 제로샷 일반화가 emergent하게 따라온다.

![SCAIL-2 teaser](https://img.seosoyoung.eiaserinnys.me/images/scail2-zai-2025/teaser.png)

## 무엇을 푸는 모델인가

캐릭터 애니메이션은 driving 시퀀스의 모션을 reference 캐릭터로 옮기는 작업이다. 지금까지의 production-grade 접근은 거의 모두 *중간 표현*을 거쳤다.

- **Pose skeleton** — driving 동작에서 키포인트를 뽑아 reference 캐릭터에 입힌다. 단순 동작에는 잘 통하지만, 손이 겹치거나 카메라가 회전하는 복잡한 장면에서 골격이 ambiguous해진다. driving source가 사람의 외부 시점 동영상으로 묶이고, 동물처럼 골격 정의가 다른 source는 입력에 쓸 수 없다.
- **Inpainting mask** — 캐릭터 교체에서 배경을 보존하기 위해 채워 넣는다. 마스크 모양이 곧 신체 모양을 제약하여 체형 변화가 제한되고, 마스크 자체가 또 다른 intermediate 부담이 된다.
- **Overlapping skeleton** — 다중 캐릭터가 가까이 상호작용하면 골격이 겹친다. 깊이 정보가 없어 모델이 잘못 해석하기 쉽다.

SCAIL-1은 *어떻게 포즈를 표현하고 어떻게 주입할 것인가*에 답을 내놓았지만, 여전히 intermediate에 묶여 있었다. SCAIL-2는 이 의존을 *over reliance on intermediates*라고 이름 붙이고 정면으로 끊어내는 길을 택했다.

![중간 표현의 한계](https://img.seosoyoung.eiaserinnys.me/images/scail2-zai-2025/preteaser.png)

## 어떻게 끊어내는가 — End-to-end In-Context Conditioning

핵심 아이디어는 단순하다. driving 비디오의 latent를 시퀀스에 직접 concatenate한다. 모델은 입력에서 필요한 모든 시각 정보를 *그 자체로* 가져간다. 골격을 추출하고 다시 렌더링하는 손실 단계가 사라진다.

여기에 두 가지 통합 장치를 얹는다.

- **In-Context Mask Conditioning** — 마스킹 채널을 두 종류로 분리한다. 하나는 *environment switch*(배경을 살릴지 교체할지), 다른 하나는 *character binding slots*(어느 latent 영역이 어느 캐릭터에 묶이는지). 두 채널의 조합만으로 애니메이션·교체·다중 캐릭터를 한 인터페이스에 모은다.
- **Mode-Specific RoPE** — 태스크 모드별로 별도의 회전 위치 인코딩을 둔다. 같은 backbone이 모드에 따라 시공간 attention을 다르게 라우팅하도록, 위치 정보 수준에서 모드를 알린다.

![데이터 합성 파이프라인](https://img.seosoyoung.eiaserinnys.me/images/scail2-zai-2025/pipeline.png)

![네트워크 구조](https://img.seosoyoung.eiaserinnys.me/images/scail2-zai-2025/network.png)

## 데이터 — MotionPair-60K

End-to-end로 학습하려면 *동일 동작을 다른 캐릭터가 수행한 비디오 쌍*이 필요하다. 그런 데이터는 자연계에 거의 없다. 그래서 합성한다.

세 종류의 off-the-shelf 모델을 데이터 제너레이터로 묶었다.

- **SCAIL-Preview** — pose-driven 단일 캐릭터.
- **Wan-Animate** — 캐릭터 애니메이션과 교체.
- **MoCha** — 캐릭터 교체.

이들을 *Unified Motion Transfer Interface*(두 마스킹 채널과 dedicated RoPE)로 통합 학습 가능한 형태로 가공한다. *reverse driving* 기법을 적용하여, 모델이 데이터 제너레이터의 성능 천장을 넘는 능력을 학습하게 한다. 최종적으로 60K motion pair를 얻는다 — 애니메이션, 교체, 다중 캐릭터를 가로지르는 heterogeneous한 데이터셋이다.

합성 데이터는 거시 동작에서는 충분하지만, 손가락 같은 미세 영역에서 편향이 누적된다. 이 부분은 사후 학습 단계에서 **Bias-Aware DPO**로 보정한다. fine-grained 영역에 초점을 둔 DPO 스킴이다.

## 결과 — 샘플 영상

원문 프로젝트 페이지의 비교 영상에서 일부를 가져온다. 각 영상은 SCAIL-2와 기존 SOTA(상용 서비스 포함)의 결과를 나란히 보여준다.

### 단일 캐릭터 애니메이션 — Studio-Bench cross-identity

<video controls src="https://teal024.github.io/SCAIL-2/static/videos/Single_Compare/hard_004_comparison.mp4" style="max-width:100%;"></video>

복잡한 동작에서 cross-identity 전이가 어떻게 작동하는지 보여주는 비교. 골격 기반 접근들이 손과 팔이 겹칠 때 어떤 식으로 무너지는지 함께 보인다.

### 다중 캐릭터 상호작용 — depth-ambiguous overlap

<video controls src="https://teal024.github.io/SCAIL-2/static/videos/Multi_Compare/multi_009_comparison.mp4" style="max-width:100%;"></video>

두 사람이 가까이 상호작용할 때, 골격 표현 기반은 identity를 섞기 쉽다. End-to-end는 시각 컨텍스트로 직접 분리한다.

### 캐릭터 교체 — 배경 인페인팅 마스크 없이

<video controls src="https://teal024.github.io/SCAIL-2/static/videos/replacement_Compare/000_comparison.mp4" style="max-width:100%;"></video>

기존 교체 방식들은 배경 인페인팅 마스크에 의존한다. SCAIL-2는 그 단계를 생략하고도 환경과의 통합이 자연스럽다 — 데이터 제너레이터인 MoCha 자체보다도 낫다고 주장한다.

### 제로샷 — 동물 driving / egocentric driving

<video controls src="https://teal024.github.io/SCAIL-2/static/videos/Zero-shot/001_gt_overlay.mp4" style="max-width:100%;"></video>

동물 캐릭터의 동작을 실제 동물에 옮긴다. 학습 데이터에는 없는 driving source다.

<video controls src="https://teal024.github.io/SCAIL-2/static/videos/Zero-shot/001_gt_overlay_2.mp4" style="max-width:100%;"></video>

1인칭 시점의 비디오를 driving으로 사용한다. 마찬가지로 학습 분포 바깥이다. 원저자는 *완전한 제로샷이며 OOD라 아티팩트가 있을 수 있다*고 명시한다.

## 사용 — 추론 워크플로우

체크포인트는 Hugging Face와 ModelScope 양쪽에 올라가 있다. 무게는 Wan VAE와 T5 모듈까지 통합된 형태로 묶여 있어 추가 다운로드 없이 추론을 시작할 수 있다.

```bash
hf download zai-org/SCAIL-2
```

체크포인트는 `sat` 브랜치 용도이며, `wan` 브랜치에서 쓰려면 `safetensors`로 변환해야 한다.

```bash
python convert.py --scail-dir /path/to/SCAIL-2 --save-path /path/to/SCAIL-2.safetensors
```

입력 준비는 SCAIL-Pose 서브모듈이 담당한다. 포즈 추출, 포즈 렌더링, reference 마스크, driving 마스크를 한 엔트리포인트로 처리한다.

```bash
# end-to-end 모드 — driving 비디오 복사본과 SAM3 마스크에서 생성한 mask 비디오
python NLFPoseExtract/process_animation_aio.py --subdir /path/to/input --e2e_mode

# pose-driven 모드 — NLF + DWPose로 스켈레톤 렌더
python NLFPoseExtract/process_animation_aio.py --subdir /path/to/input
```

추론은 `generate.py` 한 줄이다.

```bash
python generate.py \
    --model SCAIL-14B \
    --ckpt_dir /path/to/SCAIL-2 \
    --scail_path /path/to/SCAIL-2.safetensors \
    --target_w 896 --target_h 512 \
    --image examples/001/ref.jpg \
    --mask_image examples/001/ref_mask.jpg \
    --pose examples/001/rendered_v2.mp4 \
    --mask_video examples/001/rendered_mask_v2.mp4 \
    --prompt "The girl is dancing" \
    --save_file output.mp4
```

캐릭터 교체는 `--replace_flag`를 켜고 동일한 입력 구조를 쓴다. 프롬프트는 *교체 이후의* 비디오를 묘사해야 하며, 등장하는 옷차림과 소품을 명시적으로 적는 게 결과 품질을 끌어올린다. 짧은 instruction을 Gemini에 넣어 긴 영어 프롬프트로 풀어주는 `prompt_enhancer.py`도 함께 제공된다.

속도 최적화를 위해 Lightx2v LoRA를 끼우면 sampling step을 8까지 줄일 수 있다 — `sample_shift=1`, `guide_scale=1.0`이 권장 조합이다.

| 항목 | 값 |
| --- | --- |
| 모델 크기 | SCAIL-14B |
| 권장 해상도 | 512p / 704p (H·W 모두 32의 배수, 예 704×1280) |
| 기본 sampling step | 40 |
| LoRA 결합 시 step | 8 |
| 기본 solver | UniPC |
| 기본 guide scale | 5.0 |

## 가장 흥미로운 지점

데이터 제너레이터 세 개를 묶어 60K 쌍을 합성하고, *reverse driving*으로 모델이 그 제너레이터의 성능 한도를 넘게 만든다는 발상이다. 이 구도는 두 가지 함의를 끌고 온다.

첫째, *합성 데이터를 어떻게 만들었는가*가 *모델이 무엇을 할 수 있는가*보다 더 큰 변수가 된다. 동물 driving이나 egocentric 같은 zero-shot 일반화도, 데이터 자체의 분포 설계와 reverse driving이라는 학습 레시피에서 emergent하게 따라 나온다.

둘째, 손가락 같은 fine-grained 영역의 합성 편향을 별도의 사후 학습 단계(Bias-Aware DPO)로 분리한 점이다. 합성 데이터의 거시·미시 결함을 *한 단계*에서 잡으려 하지 않고, 사전학습은 거시 패턴에, DPO는 fine-grained 편향에 각각 담당을 나눈 셈이다. 합성 데이터 기반 비디오 모델 전반에 적용할 수 있는 분업이다.

## 출처

- 발신자: Z.ai (zai-org)
- 저자: Wenhao Yan, Fengjia Guo, Zhuoyi Yang, Jie Tang
- 발표 시점: 2025년 (BibTeX 기준)
- 리포: <https://github.com/zai-org/SCAIL-2>
- 프로젝트 페이지: <https://teal024.github.io/SCAIL-2/>
- 모델 체크포인트: <https://huggingface.co/zai-org/SCAIL-2>
- 기술 보고서: [resources/technical_report.pdf](https://github.com/zai-org/SCAIL-2/blob/wan-scail2/resources/technical_report.pdf)
- 선행 작업: [SCAIL-1 (arXiv:2512.05905)](https://arxiv.org/abs/2512.05905)
