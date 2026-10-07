---
title: "PLaMo翻訳 | 世界最高レベルの日本語性能のAI翻訳サービス"
date: 2026-10-07T16:30:00+09:00
tags: ["번역", "일본", "벤치마크", "음성 AI"]
categories: ["AI 산업"]
summary: "Preferred Networks가 PLaMo 번역을 3세대 모델로 갱신했다. 텍스트 번역은 53개 언어, 회의 번역은 15개 언어를 지원하고, 자체 평가에서 주요 번역 모델과 비슷한 품질을 훨씬 적은 계산 비용으로 구현했다고 발표했다."
source_url: "https://translate.preferredai.jp/"
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/plamo-translate-third-generation/meeting.webp"
  alt: "Preferred Networks가 공개한 회의 번역 소개 이미지. 왼쪽에는 세 참가자, 오른쪽에는 발언 원문과 일본어 번역이 표시된다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/plamo-translate-third-generation/meeting.webp"
---

## 3줄 요약

1. Preferred Networks가 2026년 10월 7일 PLaMo 번역에 3세대 모델을 적용하고 지원 언어를 53개로 확대했다.[^release]
2. 한국어를 포함한 15개 언어의 회의 번역을 제공하며, 한 회의에서 최대 3개 언어를 자동 판별한다.
3. 회사는 주요 번역 모델과 비슷한 품질을 훨씬 적은 비용으로 구현했다고 발표했다. PLaMo의 비교 비용은 가정한 API 요금으로 계산했고, 실제 서비스는 구독제로 제공한다.

## 어떤 서비스인가

PLaMo 번역은 일본어에 특화한 번역 서비스다. 웹페이지와 PDF/Office 문서의 레이아웃 유지, 영어 문장 교정, 음성 자막 번역을 제공한다.[^home] 일본어 또는 영어와 한국어를 상호 번역할 수 있다.[^release]

브라우저 확장은 Chrome, Edge, Firefox에서 제공한다. 다국어 기능은 v0.8.0 이상이 필요하며, 발표 당일에는 Chrome 확장과 Windows 앱의 새 버전이 스토어 심사 중이었다.[^availability]

## 회의에서 쓰는 방식

Zoom, Google Meet, Microsoft Teams의 회의 URL을 입력하면 번역 봇이 참가한다. 참가자가 봇의 입장을 허용하면 발언을 화자별로 전사하고, 원문과 번역문을 전용 페이지에 표시한다. 공유 링크로 번역을 보는 참가자는 계정이 없어도 된다. 팀 계정 보유자만 보도록 제한할 수도 있다.[^meeting]

발언은 먼저 빠르게 전사한 뒤 AI가 단어를 보정한다. 번역에는 이전 번역문, 회의 문맥, 용어집을 사용한다. 일본어 또는 영어를 포함해 2개나 3개 언어를 설정하면 발화 언어를 자동 판별하고 다른 설정 언어로 번역한다. 한국어도 회의 번역을 지원한다.

공식 페이지에는 로그인 없이 이용하는 짧은 체험 데모와, 신청 후 이용하는 30일 무료 트라이얼이 있다. 트라이얼 신청에는 로그인이 필요하다.

## 공개된 성능 비교

제품 페이지는 일본어와 영어 관련 평가 3개에 다국어 평가 FLORES+를 추가한 평균 점수를 제시한다. 회사가 공개한 값은 다음과 같다.[^home]

| 모델 또는 서비스 | 4개 평가 평균 | 원문 10만 자당 계산 비용 |
| --- | ---: | ---: |
| PLaMo 3 Translate 31B | 0.616 | 14.2엔 |
| Claude Fable 5.1 | 0.632 | 1,029엔 |
| GPT-6.1 Sol | 0.615 | 283엔 |
| GPT-6 Astra | 0.613 | 1,283엔 |
| DeepL | 0.593 | 250엔 |
| Google Translate, LLM | 0.592 | 315엔 |
| Google Translate, NMT | 0.582 | 320엔 |

점수는 서로 다른 평가 지표를 평균한 값이다. FLORES+의 chrF++ 점수는 100으로 나눠 사용했다. PFN은 10월 7일 공개 단가에 실제 평가 사용량을 적용해 비용을 계산했다. 환율은 달러당 160엔이다. PLaMo 번역에는 공개 API가 없어 같은 세대의 PLaMo API 요금을 가정했다.[^cost]

개별 번역문 비교도 실시했다. Gemini 3.1 Pro는 번역문 제시 순서를 바꿔 두 번 판정했다. PFTB 영어→일본어 평가에서 PLaMo 31B의 승률은 DeepL 대비 87%, Google Translation LLM 대비 86%였다.[^tech]

기술 블로그에 따르면 새 모델의 가중치는 추후 공개할 예정이다.[^tech]

## 요금과 데이터 처리

아래는 발표 당일 표시된 월 결제 요금이다. 유료 요금은 캠페인 가격이며 세금을 포함한다.[^pricing]

| 플랜 | 월 요금 | 월 텍스트 번역 한도 |
| --- | ---: | ---: |
| Free | 무료 | 5만 자 |
| Lite | 1,078엔 | 100만 자 |
| Pro | 2,838엔 | 500만 자 |
| Lite 팀 | 1인당 2,178엔 | 1인당 200만 자 |
| Pro 팀 | 1인당 3,938엔 | 1인당 1,000만 자 |

캠페인은 10월 7일부터 11월 30일까지다. Lite는 처음 두 달 무료이며, 세 번째 달부터 통상 월 요금 1,298엔이 자동 청구된다. 무료 기간을 이용하려면 카드 정보를 등록해야 한다. 파일 번역과 회의 번역은 같은 포인트를 사용하며, 캠페인 중에는 지급 포인트가 두 배다. 회의 봇이 참가한 시간 3분당 1포인트를 사용한다.[^release]

요금표는 유료 플랜의 입력 데이터를 2차 이용하지 않는다고 명시한다. Free에는 데이터 2차 이용이 있다고 표시한다.[^privacy] 회의 음성은 저장하지 않고 처리 직후 폐기한다. 회의 로그는 사용자가 삭제하거나 회의 종료 후 7일이 지나면 폐기한다. 회의 종료 즉시 로그를 삭제하는 설정도 제공한다. 회의 번역 페이지에는 데이터를 일본 내에서 처리하고 학습에 사용하지 않는다고 명시돼 있다.[^meeting]

## 번역 예시에서 눈에 띈 점

나는 모델 점수보다 짧은 번역 예시가 기억에 남았다. 가게 소개에 나온 ‘pints’를 PLaMo는 ‘맥주’라고 번역했다. 영어 업무 메일도 일본어의 정중한 의뢰 표현으로 바꿨다. 회사가 강조하는 품질은 문맥과 문서 종류에 맞는 일본어 표현을 고르는 능력이다.[^tech]

텍스트 번역을 직접 시험할 수 있고, 회의 번역에는 별도 체험을 마련했다. 일본어로 자료를 읽거나 회의에 참가하는 사람에게는 자신의 용어와 문장으로 결과를 확인할 수 있는 서비스다.

## 출처

Preferred Networks, 2026년 10월 7일 공개 자료. 상단 이미지는 공식 제품 페이지의 회의 번역 소개 이미지다.

- [PLaMo 번역 공식 사이트](https://translate.preferredai.jp/)
- [10월 7일 업데이트 공지](https://translate.preferredai.jp/news/20261007-1-plamo3-major-update/)
- [기술 블로그: plamo-3-translate](https://www.preferred.jp/ja/blog/tech/plamo-3-translate-product-release)
- [회의 번역](https://translate.preferredai.jp/meeting/)
- [요금과 기능 비교](https://translate.preferredai.jp/pricing/)

[^home]: [PLaMo 번역 공식 제품 페이지](https://translate.preferredai.jp/), 2026년 10월 7일 확인.
[^release]: [Preferred Networks의 10월 7일 공식 업데이트 공지](https://translate.preferredai.jp/news/20261007-1-plamo3-major-update/).
[^availability]: [공식 제품 페이지의 지원 언어 안내](https://translate.preferredai.jp/). 배포 상태는 10월 7일 표기 기준이다.
[^cost]: [PFN 기술 블로그의 비용 계산 조건](https://www.preferred.jp/ja/blog/tech/plamo-3-translate-product-release). PLaMo에는 입력 100만 토큰당 60엔, 출력 100만 토큰당 250엔을 가정했다. 표의 14.2엔은 고객에게 청구하는 번역 API 요금이나 월 구독료가 아니다.
[^tech]: 鈴木 海渡, [plamo-3-translate: フロンティア級の翻訳特化LLM](https://www.preferred.jp/ja/blog/tech/plamo-3-translate-product-release), 2026년 10월 7일. 회사 자체 평가이며 PFTB는 사내 개발 평가다. 예시는 게재 당시 출력으로, 모델 갱신 후 결과가 달라질 수 있다.
[^pricing]: [공식 요금 페이지](https://translate.preferredai.jp/pricing/). 파일과 회의의 최대 이용량은 포인트 전부를 해당 기능에 사용했을 때의 값이다.
[^privacy]: [공식 요금 비교표](https://translate.preferredai.jp/pricing/). 제품 첫 화면의 일괄적인 데이터 미사용 설명과 달리, 비교표는 Free의 2차 이용을 별도로 표시한다.
[^meeting]: [회의 번역 기능과 FAQ](https://translate.preferredai.jp/meeting/).
