---
title: "Qwen3.8 Flash Next에 섞이는 중국어를 출력층 재작성으로 없앴다: 27%→0%, 다른 가중치는 1바이트도 바꾸지 않고"
date: 2026-11-14T22:30:00+09:00
tags: ["Qwen", "로컬 LLM", "양자화", "일본", "LLM"]
categories: ["모델과 연구"]
subjects: ["추론 효율과 로컬 실행"]
summary: "일본 개발사 CAPH TECH가 오픈소스 도구 Kestrom으로 Qwen3.8-Flash-Next의 출력층에서 중국어 토큰 25,451개 행만 미사용 행의 바이트로 덮어썼다. 나머지 100GB 가중치는 1바이트도 바꾸지 않고 일본어 의료 문답의 중국어 혼입률을 27%에서 0%로 줄인 실험을 정리한다."
source: "https://zenn.dev/caphtech/articles/qwen38-zh-ban"
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/qwen38-zh-ban/01-cover.png"
  alt: "자물쇠로 잠긴 가중치 보관함 옆에서 핀셋으로 출력층 장부의 행 하나만 하늘색 빈 막대로 교체하는 치비 서소영"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/qwen38-zh-ban/01-cover.png"
---

## 3줄 요약

1. 일본의 모바일 앱 개발사 CAPH TECH(저자 rizumita)가 2026년 11월 13일 기술 공유 플랫폼 Zenn에 발표한 실험 기록이다. 저자는 128GB 메모리를 탑재한 Mac에서 4비트로 양자화한 MLX 모델 `Qwen3.8-Flash-Next`로 일본어 의료 질문 60건에 답하도록 했을 때 중국어 간체자와 어휘가 얼마나 섞여 나오는지 측정했다.
2. 저자는 모델의 전체 가중치 약 100GB 가운데 출력층 파일(약 650MB)만 수정했다. 이 파일에서 중국어 토큰에 해당하는 25,451개 행을 토크나이저가 쓰지 않는 행(`id:248077`)의 바이트 복사본으로 덮어쓴 것이다. 수정과 바이트 검증에는 저자 팀이 공개한 모델 부분 편집 도구 Kestrom을 사용했다.
3. 출력층의 25,451개 행만 고친 뒤에는 60문항 중 16문항(27%, 수동 검수 기준 23%)에서 나오던 중국어 혼입이 사라져 0문항이 되었고, 총 36,969토큰을 생성하는 동안 금지 토큰이 상위 20위 후보에 포함된 횟수도 0회였다. 금지 토큰이 선택되지 않는 탐욕적 디코딩 조건에서는 60문항 모두 원본 모델과 글자 하나까지 똑같은 답변을 출력했다.

## 환자 안내문에 섞여 나오는 간체자와 중국어 어휘

저자는 통합 메모리 128GB 사양의 Mac에서 `mlx-serve`를 이용해 `Qwen3.8-Flash-Next`(Qwen Community License 1.0)를 구동하며 실험을 진행했다.[^1] 실험 대상 모델은 `mlx-serve` 변환 도구로 만든 4비트 MLX 양자화 버전이며, 마지막 출력층만 8비트로 양자화되어 있다.

이 모델에 일본어로 의료 질문을 입력하면 답변 도중에 중국어 간체자나 중국어 어휘가 종종 섞여 나온다. 저자가 원문에서 제시한 실제 생성 사례는 다음과 같다.

> 류머티즘 관절염은 자신의 면역 체계가 자신의 관절을 잘못(误って) 공격해 버리는 병입니다.

> 관상동맥은 그 노동자에게 가는 급수관(給水管)입니다. 급수관(给水管)이 막히면 노동자는 영양 부족으로 쓰러지고 맙니다.

> 최근 피곤하지 않은데 살이 빠졌다거나 사소한 일에도(动不动に) 짜증이 나는 이러한(这样的) 변화가 있다면 진료를 받아 볼 기준이 됩니다.

> 주류: 맥주(啤酒, 특히 대량), 증류주

일본어 정자체인 `誤って`가 간체자 `误って`로 바뀌거나, 앞 문장에서는 `給水管`(급수관)이라고 바르게 표기해 놓고 바로 다음 문장에서 간체자 `给水管`을 출력하는 식이다. `动不动`(툭하면), `这样的`(이런), `啤酒`(맥주)처럼 일본어에서 쓰지 않는 중국어 어휘가 그대로 생성되기도 한다.

저자는 이 현상의 빈도를 정량적으로 확인하기 위해 의료 질문 60문항으로 평가 세트를 구성했다. 40문항은 JMMLU의 의료 7개 과목에서 가져온 객관식 문제로 구성해 선택지의 이유를 일본어로 설명하게 했고, 나머지 20문항은 질환과 문서 양식을 조합한 자유 서술형 문제(환자용 쉬운 질병 설명문, 진료 의뢰서 본문 작성 등)로 만들었다. 답변을 생성할 때는 모델 기본값인 추론 모드(`thinking`)를 켠 상태에서 권장 샘플링 설정(`temperature 1.0`, `top_p 0.95`, `top_k 20`, 최대 8,192토큰)을 따랐다.

중국어가 섞였는지는 추론 과정을 뺀 최종 답변 본문을 기준으로 판별했다. 일본 산업 규격 한자 집합인 JIS X 0213에 등록되지 않은 한자(`简`, `误`, `这` 등)가 포함되거나, 중국어 문서에는 자주 등장하지만 일본어에는 거의 쓰이지 않는 어휘 토큰(`啤酒`, `皮肤` 등)이 등장하면 혼입된 답변으로 분류했다.

| 평가 항목 (의료 질문 60문항) | 원본 모델 | 출력층을 고친 모델 |
| --- | --- | --- |
| 중국어가 섞인 답변 수 (전체 60문항) | 16문항 (27%, 수동 확인 시 14문항 23%) | 0문항 (자동 집계 1문항은 일본어 의학 용어 오탐) |
| 자유 서술형 답변 중 혼입 수 (20문항) | 13문항 | 0문항 |
| 금지 토큰이 후보 상위 20위에 포함된 횟수 | 측정 대상 아님 | 전체 36,969토큰 구간 중 0회 |
| 최대 토큰 한도로 중단된 답변 수 | 0문항 | 0문항 |
| 답변 길이 중앙값 | 754자 | 714자 |

원본 모델은 전체 60문항 가운데 자동 집계 기준으로 16문항(27%)에서 중국어를 출력했다. 모든 답변을 직접 읽어 대조해 보니, 정상적인 일본어 의학 및 일반 용어인 `大小不同症`(대소부동증), `是正`(시정), `尿沈渣`(요침사)를 중국어로 잘못 분류한 오탐 2문항을 제외하면 실제 혼입은 14문항(23%)이었다.[^2] 문항 유형별 수치를 보면 객관식 해설 40문항 중 3문항에만 중국어가 나왔고, 자유 서술형 20문항에서는 13문항에 중국어가 섞였다. 설명이 길어질수록 중국어 토큰이 선택될 확률이 높은 편이다. 이전 세대 모델인 `Qwen3.5-9B`로 같은 60문항을 시험했을 때도 15문항에서 혼입이 발생했으니, 후속 세대 모델에서도 이 현상은 비슷한 빈도로 계속 나타났다.

출력층에서 중국어 토큰에 해당하는 25,451개 행만 재작성한 뒤 같은 조건으로 다시 생성하자, 중국어 혼입은 0문항이 되었다. 원본 모델이 `误って攻撃してしまう病気`와 `啤酒`를 출력했던 문항에서도 수정된 모델은 `誤って攻撃してしまう病気`와 `ビール: 最も注意`처럼 자연스러운 일본어를 생성했다.

## 미사용 어휘 행 복사로 중국어 토큰 25,451개 차단하기

언어모델이 다음 토큰을 고를 때는 마지막 출력층에서 어휘 목록의 각 토큰에 점수(logit)를 매긴 뒤 그중 가장 높은 것을 선택한다. 출력층 행렬의 행 수는 어휘 수와 같다. 특정 토큰의 점수는 그 토큰에 해당하는 출력층 행 벡터와 모델 내부 은닉 상태 벡터를 내적해 구한다.

여기서 저자는 `Qwen3.8-Flash-Next`의 토크나이저 어휘 크기와 출력층 행렬 크기가 다르다는 점을 활용했다. 이 모델의 출력층 행렬은 총 248,320행이다. 토크나이저에 등록된 토큰은 248,077개이며, 해당 행 번호는 0번부터 248,076번까지다. 끝에 남는 243개 행(248,077번부터 248,319번 행까지)은 어떤 토큰에도 할당되지 않은 미사용 행이다.[^3] 중국어 토큰 25,451개의 출력층 행은 토크나이저 미사용 구간의 첫 번째 행인 `248,077번 행`의 바이트 복사본으로 덮어썼다. 이 복사로 금지된 중국어 토큰의 내적 점수는 언제나 미사용 행의 점수와 똑같아진다.

![보관함 맨 아래 예비 서랍에서 꺼낸 하늘색 빈 막대를 토큰 색인판의 표시된 칸들에 끼워 넣는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/qwen38-zh-ban/02-unused-row-copy.png)

차단할 중국어 토큰 25,451개 목록(`examples/zh-ban/list.txt`)은 어휘 체계가 같은 `Qwen3.5-9B` 실험 때 만들어 둔 것을 그대로 가져왔다. 선정 기준은 두 가지다.

1. JIS X 0213 규격에 없는 한자를 포함한 토큰: 21,601개
2. 중국어 전용 어휘 토큰: 3,850개
   - 중국어 위키백과(일반 문서 및 의료 문서 합산)에 20회 이상 등장하는 토큰을 먼저 추렸다.
   - 그중 일본어 위키백과에서의 출현 비율이 중국어 위키백과 출현 비율의 1% 이하인 토큰만 남겼다.
   - 마지막으로 사람이 목록을 직접 읽어 보며 실제 일본어에서도 쓰이는 표현을 제외했다.

<figure class="blog-diagram">
<svg class="diagram-svg-desktop" viewBox="0 0 720 220" role="img" aria-label="Qwen3.8-Flash-Next 출력층 행 교체와 파일 구성 흐름" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="220" fill="var(--bg-2)"/>
  <rect x="16" y="20" width="212" height="180" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="28" y="46" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 출력층 구조 (248,320행)</text>
  <text x="28" y="74" font-family="var(--sans)" font-size="11.5" fill="var(--ink)">정상 어휘: 222,626개 행 (유지)</text>
  <text x="28" y="100" font-family="var(--sans)" font-size="11.5" fill="var(--accent)">중국어 금지 대상: 25,451개 행</text>
  <text x="28" y="126" font-family="var(--sans)" font-size="11.5" fill="var(--ink-2)">JIS X 0213 외 한자 21,601개</text>
  <text x="28" y="146" font-family="var(--sans)" font-size="11.5" fill="var(--ink-2)">중문 위키 고빈도 어휘 3,850개</text>
  <text x="28" y="176" font-family="var(--mono)" font-size="11" fill="var(--ink)">미사용 행: 243개 (id:248077~)</text>
  <line x1="228" y1="110" x2="250" y2="110" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="254" y="20" width="212" height="180" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="266" y="46" font-family="var(--mono)" font-size="12.5" font-weight="700" fill="var(--accent-ink)">2. kestrom rows ban</text>
  <text x="266" y="74" font-family="var(--sans)" font-size="11.5" fill="var(--accent-ink)">미사용 첫 행(id:248077) 바이트를</text>
  <text x="266" y="94" font-family="var(--sans)" font-size="11.5" fill="var(--accent-ink)">금지 대상 25,451개 행에 복사</text>
  <text x="266" y="124" font-family="var(--sans)" font-size="11.5" fill="var(--accent-ink)">8비트 양자화 텐서 3종 동시 반영</text>
  <text x="266" y="146" font-family="var(--mono)" font-size="11" fill="var(--accent-ink)">weight / scales / biases</text>
  <text x="266" y="176" font-family="var(--sans)" font-size="11.5" fill="var(--accent-ink)">나머지 행은 1바이트도 변경 없음</text>
  <line x1="466" y1="110" x2="488" y2="110" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink)"/>
  <rect x="492" y="20" width="212" height="180" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="504" y="46" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">3. 파일 저장 및 검증 요약</text>
  <text x="504" y="74" font-family="var(--sans)" font-size="11.5" fill="var(--ink)">출력층 파일(약 650MB)만 새로 기록</text>
  <text x="504" y="98" font-family="var(--sans)" font-size="11.5" fill="var(--ink-2)">가중치 70GB + ngram 30GB는 링크</text>
  <text x="504" y="128" font-family="var(--sans)" font-size="11.5" fill="var(--accent)">60문항 중국어 혼입: 27% → 0%</text>
  <text x="504" y="152" font-family="var(--sans)" font-size="11.5" fill="var(--ink)">상위 20위 포함: 36,969토큰 중 0회</text>
  <text x="504" y="176" font-family="var(--sans)" font-size="11.5" fill="var(--ink)">탐욕적 디코딩 60문항 100% 일치</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 450" role="img" aria-label="Qwen3.8-Flash-Next 출력층 행 교체와 파일 구성 흐름 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="450" fill="var(--bg-2)"/>
  <rect x="16" y="16" width="318" height="124" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="40" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 출력층 구조 (전체 248,320행)</text>
  <text x="30" y="64" font-family="var(--sans)" font-size="12" fill="var(--ink)">정상 어휘 222,626개 행 유지 / 미사용 243개 행</text>
  <text x="30" y="88" font-family="var(--sans)" font-size="12" fill="var(--accent)">중국어 금지 대상: 25,451개 행</text>
  <text x="30" y="112" font-family="var(--sans)" font-size="12" fill="var(--ink-2)">JIS 외 한자 21,601개 + 중문 위키 어휘 3,850개</text>
  <line x1="175" y1="140" x2="175" y2="160" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="16" y="164" width="318" height="124" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="30" y="188" font-family="var(--mono)" font-size="13" font-weight="700" fill="var(--accent-ink)">2. kestrom rows ban (바이트 복사)</text>
  <text x="30" y="212" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">미사용 첫 행(id:248077)을 25,451개 행에 복사</text>
  <text x="30" y="236" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">8비트 텐서 3종(weight, scales, biases) 반영</text>
  <text x="30" y="260" font-family="var(--sans)" font-size="12" fill="var(--accent-ink)">나머지 어휘 행과 가중치는 1바이트도 변경 없음</text>
  <line x1="175" y1="288" x2="175" y2="308" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#arr-ink-m)"/>
  <rect x="16" y="312" width="318" height="122" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="336" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">3. 파일 저장 및 검증 요약</text>
  <text x="30" y="360" font-family="var(--sans)" font-size="12" fill="var(--ink)">출력층(650MB)만 저장, 나머지 100GB는 원본 링크</text>
  <text x="30" y="384" font-family="var(--sans)" font-size="12" fill="var(--accent)">중국어 혼입 27% → 0% (상위 20위 포함 0회)</text>
  <text x="30" y="408" font-family="var(--sans)" font-size="12" fill="var(--ink)">탐욕적 디코딩 60문항 원본과 100% 일치</text>
</svg>
<figcaption style="margin-top: 0.65rem; font-size: 0.85rem; color: var(--ink-2); text-align: center; line-height: 1.5;">Kestrom을 이용한 Qwen3.8-Flash-Next 출력층 행 교체와 검증 요약</figcaption>
</figure>

Kestrom을 사용하면 이 작업은 명령어 한 줄로 끝난다.

```bash
git clone https://github.com/CAPHTECH/kestrom && cd kestrom
pip install "./verify[mlx]" "./edit[mlx]"

# 목록의 25,451개 행을 248,077번 행(어휘 미할당 첫 행)의 바이트 복사본으로 교체
kestrom rows ban ~/models/mlx/Qwen3.8-Flash-Next "" \
  examples/zh-ban/list.txt id:248077 \
  ~/models/mlx/Qwen3.8-Flash-Next-nozh
```

이 명령을 실행하면 Kestrom은 출력층이 들어 있는 파일(약 650MB)만 새로 복사해 수정하고, 나머지 파일(모델 가중치 약 70GB와 `ngram_table.bin` 약 30GB를 합쳐 약 100GB)은 원본 파일을 가리키는 링크로 연결한다. 디스크 공간을 추가로 100GB씩 쓰지 않아도 되고, `mlx-serve`에 모델 목록 재검색 요청(`POST /v1/models/rescan`)만 보내면 새 모델 이름으로 즉시 호출할 수 있다.

## 바이트 단위 대조와 탐욕적 디코딩 검증, 그리고 한계

가중치 파일을 수정했을 때 가장 중요한 질문은 지정한 행을 뺀 나머지 데이터가 실제로 바뀌지 않았는가 하는 점이다. Kestrom은 작업자의 설명에 의존하는 대신 가중치 파일의 바이트와 실제 모델 출력 두 가지를 직접 대조해 이를 증명한다.

첫째로 `kestrom-verify range` 명령으로 원본 모델과 수정된 모델의 파일 116개 전체를 바이트 단위로 비교했다. 8비트로 양자화된 MLX 출력층은 가중치 값(`weight`), 양자화 배율(`scales`), 영점 편향(`biases`)의 세 가지 텐서로 구성되어 있다. 116개 파일을 모두 비교해 보니, 이 세 텐서에서 금지 대상으로 지정한 25,451개 행만 빼면 나머지 모든 바이트가 원본과 완벽히 일치했다. 금지하지 않은 어휘의 행은 1바이트도 바뀌지 않았다. 따라서 해당 어휘의 내적 점수도 원본과 비트 단위로 동일하다.

![책상 위에 놓인 두 개의 하늘색 천공카드 띠를 돋보기로 대조하며 모든 홈이 일치함을 확인하는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/qwen38-zh-ban/03-byte-verify.png)

둘째로 금지된 토큰이 선택되지 않는 조건에서 실제 생성 문장이 원본과 일치하는지 확인했다. 추론 모드를 끄고(`enable_thinking: false`) 매 단계 점수가 가장 높은 토큰만 고르는 탐욕적 디코딩(greedy decoding) 방식으로, 의료 질문 60문항에 대한 답변을 원본 모델에서 2회, 수정된 모델에서 1회 생성해 비교했다.

```bash
kestrom-verify generate server http://127.0.0.1:11999 Qwen3.8-Flash-Next prompts.json ~/models/mlx/Qwen3.8-Flash-Next base.jsonl
kestrom-verify generate server http://127.0.0.1:11999 Qwen3.8-Flash-Next prompts.json ~/models/mlx/Qwen3.8-Flash-Next base2.jsonl
kestrom-verify generate server http://127.0.0.1:11999 Qwen3.8-Flash-Next-nozh prompts.json ~/models/mlx/Qwen3.8-Flash-Next edited.jsonl
kestrom-verify compare range.json base.jsonl base2.jsonl edited.jsonl ~/models/mlx/Qwen3.8-Flash-Next greedy.json
```

원본 모델이 두 차례 내놓은 답변과 수정된 모델이 내놓은 답변은 60문항 모두에서 글자 하나까지 완전히 일치했다.[^4]

저자는 이번 실험의 한계 다섯 가지도 구체적으로 명시했다.

| 한계 항목 | 구체적 내용과 미확인 범위 |
| --- | --- |
| 토큰 단위 차단의 부작용 가능성 | 금지된 토큰으로만 표기할 수 있는 일본어 단어가 함께 차단될 수 있음 (`Qwen3.5-9B` 300문항 실험에서는 `両性具有`가 `両性具`로 잘리는 현상이 6회 발생함) |
| 금지 토큰의 실제 로짓 수치 미측정 | `mlx-serve`에서 출력층 입력 벡터를 추출할 수 없어 `top_k 20` 후보에 한 번도 포함되지 않았다는 점만 확인했고, `top_k`를 쓰지 않을 때 25,451개 금지 토큰의 확률 합계는 측정하지 못함 |
| 금지 규칙 작동 직전까지의 일치성 미검증 | 추론 모드를 끈 탐욕적 디코딩 60문항에서는 원본 모델도 중국어 토큰을 한 번도 고르지 않아, 금지 규칙이 실제로 발동하는 시점 직전까지 출력이 일치하는지는 이번 세트에서 시험하지 못함 |
| 실행 환경의 범위 | `mlx-serve` 환경의 MLX 양자화 모델에서만 검증했으며, `llama.cpp`나 LM Studio에서 쓰는 GGUF 포맷은 아직 시험하지 않음 |
| 표본 크기와 도메인 | 의료 분야 60문항이라는 소규모 표본이며, 원본 혼입률 27%의 95% 신뢰구간은 약 17%에서 39% 수준임 |

글 말미에서 저자는 이번 실험에 쓴 오픈소스 도구 [Kestrom](https://github.com/CAPHTECH/kestrom)의 세 가지 기능을 소개했다. 첫째는 이번 실험처럼 출력층의 특정 행만 고쳐 특정 어휘 출력을 억제하거나 표기를 통일하는 기능이다. 둘째는 추론 도중 작은 규칙 언어(DSL)를 적용해 특정 조건에서만 지정한 토큰을 고르거나 추론 루프가 반복될 때 되돌아가게 해 준다. 셋째는 미세조정이나 양자화로 수정된 모델에서 어떤 텐서가 얼마나 바뀌었는지 측정할 수 있다. 저자 팀은 이번 실험에 맞추어 양자화된 출력층(`weight`, `scales`, `biases`)을 다루는 기능, 다른 행의 바이트를 복사해 토큰을 금지하는 기능, OpenAI 호환 서버(`mlx-serve`)의 출력을 비교하는 기능 세 가지를 새로 넣었다.[^5]

## 가장 흥미로운 지점

이번 실험에서 특히 눈에 띄는 대목은 금지 토큰의 점수를 낮추기 위해 새로운 상수를 임의로 넣지 않고, 모델 출력층 끝에 이미 존재하던 미사용 행(`id:248077`)의 바이트를 그대로 복사해 썼다는 점이다. 양자화된 모델은 각 행에 배율(`scales`)과 영점 편향(`biases`)을 함께 적용한다. 이 때문에 임의의 작은 숫자를 사용하면 양자화 복원 과정에서 의도치 않은 수치 오차가 생기기 쉽다. 반면 학습 내내 정답 토큰으로 쓰인 적이 없는 미사용 행의 `weight`, `scales`, `biases` 바이트를 통째로 복사하면 양자화 형식을 전혀 바꾸지 않으면서도 모든 입력 상태에서 일관되게 낮은 로짓을 얻을 수 있다.

여기에 더해 100GB에 육박하는 전체 모델을 다시 학습하거나 재양자화하는 대신, 650MB짜리 출력층 파일 하나만 수정하고 나머지 가중치는 심볼릭 링크로 유지한 설계도 실용적이다. 이 사례는 로컬 LLM을 현업에 도입할 때 중국어 토큰 혼입처럼 원인이 명확한 표기 문제라면 거대한 사후학습 파이프라인을 실행하지 않고도, 바이트 단위로 검증할 수 있는 부분 편집만으로 분명하게 해결할 수 있음을 잘 보여준다.

## 출처

- 合同会社CAPH TECH (rizumita), 「Qwen3.8 Flash Nextに混ざる中国語を、出力層の書き換えで消した: 27%→0%、他の重みは1バイトも変えずに」, Zenn, 2026-11-13.
- 원문: <https://zenn.dev/caphtech/articles/qwen38-zh-ban>
- Kestrom GitHub 저장소: <https://github.com/CAPHTECH/kestrom>
- 치비 서소영 커버와 본문 삽화 2장은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 gpt-image-2.6-flare image-to-image로 따로 생성했다.

[^1]: 저자는 Anthropic의 Claude Code와 함께 실험 코드를 작성하고 실행했으며, 평가 문항 일부에는 와세다대 자연어처리 연구실이 Hugging Face에 공개한 일본어 벤치마크 `nlp-waseda/JMMLU_CC-BY-SA`(CC BY-SA 4.0)의 의료 문제를 사용했다.
[^2]: 출력층을 고친 모델에서도 자동 집계 스크립트는 1문항을 걸러냈으나, 실제 본문을 확인해 보니 올바른 일본어 의학 용어인 `尿沈渣`(요침사, 소변 침전물 검사)의 `渣` 글자를 중국어로 잘못 판별한 오탐이었다.
[^3]: 저자는 이 미사용 행들이 모델 학습 과정에서 정답 토큰이 되는 일이 없으므로 항상 낮은 점수를 유지할 것이라고 예상했다. 그러나 학습 시 손실 계산에서 아예 제외되었을 가능성도 있어, 미사용 행의 점수가 얼마나 낮은지는 직접 단정하지 않고 실제 생성 시 상위 20위 후보에 포함되는지 여부로 검증했다.
[^4]: 저자는 검증 과정에서 `mlx-serve`의 캐시 동작과 관련된 주의점도 함께 보고했다. 모델을 메모리에서 내리지 않고 같은 60문항을 연속해서 두 번 보내면 원본 모델끼리 비교해도 60문항 중 49문항에서 답변이 달라졌다. 반면 매번 모델을 언로드(`/v1/unload-model`)해 새로 불러온 직후에 답변을 생성하면 몇 번을 반복해도 60문항 전체가 글자 하나까지 일치했다. 저자는 같은 프롬프트의 계산값을 재사용하는 캐시 과정에서 미세한 수치 차이가 발생하는 것으로 추정했다.
[^5]: Kestrom 저장소에서 검증 도구(`kestrom-verify`)는 Apache-2.0 라이선스로 배포되며, 편집 도구(`kestrom`)는 소규모 사업자와 비상업적 용도를 허용하는 PolyForm 라이선스(그 외 상업적 이용은 유상 라이선스)로 제공된다.
