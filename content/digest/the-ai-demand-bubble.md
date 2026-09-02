---
title: "The AI Demand Bubble"
date: 2026-08-06T10:30:00+09:00
tags: ["AI", "경제·금융", "Anthropic", "OpenAI", "데이터센터"]
categories: ["다이제스트"]
summary: "Ed Zitron이 애널리스트 추정치를 근거로, Amazon·Microsoft·Google의 AI 매출과 성장의 대부분이 OpenAI·Anthropic 두 곳의 컴퓨트 지출에서 나온다고 주장한 글. 그 둘을 빼면 AI 수요는 사실상 없고, 세 회사는 이 집중을 공시하지 않아 투자자를 오도하고 있다는 진단이다."
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/the-ai-demand-bubble/fig1.png"
  alt: "Amazon AI 매출에서 Anthropic·OpenAI가 차지하는 비중 (Barclays, Ross Sandler 추정)"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/the-ai-demand-bubble/fig1.png"
ShowToc: true
TocOpen: false
---

## 3줄 요약

1. Ed Zitron이 2026년 8월 4일 뉴스레터 「Where's Your Ed At」에 올린 글이다. Barclays·UBS·Wells Fargo 애널리스트들의 추정치를 모아, 하이퍼스케일러 세 곳의 AI 매출이 실제로 어디서 오는지를 따진다.
2. 핵심 진단은 하나다. Amazon·Microsoft·Google의 AI 매출과 클라우드 성장의 70%가 넘는 몫이 OpenAI와 Anthropic 두 곳의 컴퓨트 지출에서 나온다. 그런데 그 두 회사는 벤처 자금과 부채 없이는 청구서를 감당하지 못하고, 그 자금의 상당액을 다시 하이퍼스케일러들이 대준다.
3. 두 회사를 빼면 세 하이퍼스케일러의 비-AI랩 컴퓨트 수요는 통틀어 300억 달러도 되지 않는다. Zitron은 이것을 "수요가 없는데 수천억 달러어치 데이터센터를 짓고 있다"는 과잉 건설로 읽고, 세 회사가 이 매출 집중을 공시하지 않아 투자자를 오도한다고 결론짓는다.

## 애널리스트가 말하는 것: AI 매출의 70%가 두 회사에서 나온다

글의 출발점은 지난 실적 시즌이다. 언론은 Amazon·Google·Microsoft의 클라우드 부문이 사상 최대 매출 성장을 기록했다며 "AI 베팅이 결실을 맺었다"고 전했다. Zitron은 여기서 한 가지가 조용히 빠졌다고 지적한다. 세 회사 모두 AI 매출을 따로 떼어 공개하지 않는다는 점이다. Microsoft는 FY2026 3분기에 AI 런레이트가 370억 달러(월 약 31억 달러)라고 밝혔다가, 4분기에는 그 수치를 아예 공개하지 않았다.

Zitron이 모은 애널리스트 추정치는 세 회사 모두에서 같은 그림을 그린다.

| 기업 | 두 AI랩이 차지하는 AI 매출 비중 | 근거 |
|---|---|---|
| Amazon (AWS) | 2026·2027년 73%, 2028년 75% | Barclays, Ross Sandler |
| Microsoft | 70% 이상 (FY2027 말 74% 전망) | Wells Fargo, Michael Turrin |
| Google Cloud | 70% 이상으로 추정 (두 랩만으로 전체 클라우드 매출의 2026년 28%, 2027년 48% 이상) | UBS, Stephen Ju |

Barclays의 Ross Sandler는 두 랩의 컴퓨트 지출 자체를 연도별로 추정했다.

| 연도 | Anthropic 컴퓨트 지출 | OpenAI 컴퓨트 지출 |
|---|---|---|
| 2026 | 141억 달러 | 90억 달러 |
| 2027 | 253억 달러 | 150억 달러 |
| 2028 | 358억 달러 | 200억 달러 |

Amazon은 2026년 자본지출로 2,200억 달러를 쓸 계획이고, Zitron이 보기에 그 지출은 거의 전적으로 반년 만에 950억 달러를 조달해야 했던 한 회사(Anthropic)에 컴퓨트를 공급하기 위한 것이다. 그 조달액 중 50억 달러는 Amazon 자신이 넣었다.

> **편집자 주(원문):** Sandler와 별개로 UBS의 Stephen Ju는 AWS의 2026년 총 AI 매출을 약 309억 달러로 보고, 그중 OpenAI·Anthropic 컴퓨트 지출이 59%(183억 달러), 나머지 126억 달러가 Bedrock(Amazon이 Anthropic·OpenAI 모델 접근을 판매하는 플랫폼)에서 나온다고 추정했다. Zitron은 본문 대부분을 Sandler 수치로 썼고, 두 추정치가 달라도 관점은 바뀌지 않는다고 밝혔다.

Google도 같은 처지다. UBS의 Stephen Ju는 2026년 Google Cloud 매출에서 Anthropic·OpenAI·Meta가 각각 21%, 7%, 1%를, 2027년에는 44%, 5%, 1%를 차지한다고 봤다. 두 AI랩만 합치면 2026년 28%, 2027년 48% 이상이다. Ju가 그 외의 큰 고객을 하나도 언급하지 않았다는 점을, Zitron은 다른 대형 고객이 사실상 없다는 신호로 읽는다.

![Google Cloud 매출에서 Anthropic·OpenAI·Meta가 차지하는 비중 (UBS, Stephen Ju 추정)](https://img.seosoyoung.eiaserinnys.me/images/the-ai-demand-bubble/fig2.png)

Bloomberg Intelligence 컨센서스로 잡은 Google Cloud 매출(2026년 1,059억 달러, 2027년 1,738억 달러)에 이 비중을 대입하면, OpenAI·Anthropic 몫은 2026년 294억 달러(74억+220억), 2027년 약 847억 달러(86.9억+760억)가 된다. Zitron은 이것이 Google AI 매출의 최소 75%, 어쩌면 그 이상이라고 본다. Google의 비-AI 클라우드 사업은 2026년부터 2028년까지 사실상 정체로 추정된다.

![Google Cloud의 비-AI 사업은 2026년부터 2028년까지 사실상 정체로 추정된다](https://img.seosoyoung.eiaserinnys.me/images/the-ai-demand-bubble/fig3.png)

Microsoft도 다르지 않다. Wells Fargo의 Michael Turrin(2026년 5월 31일 노트)은 Microsoft AI 매출의 70% 이상이 두 랩에서 나오며, FY2027 말에는 그 비중이 74%에 이른다고 봤다. Azure 매출에서 두 랩이 차지하는 몫은 FY2026 23%에서 FY2027 35%로 커진다. Azure가 전년 대비 41% 성장했는데, 그 성장의 40% 이상이 두 랩에서 왔다는 계산이다. Azure가 AI 말고도 훨씬 많은 것을 판다는 점을 감안하면 무거운 수치다.

![Microsoft 365의 AI 매출과 OpenAI 매출 배분 비교 (Wells Fargo 추정)](https://img.seosoyoung.eiaserinnys.me/images/the-ai-demand-bubble/fig4.png)

![Azure 매출에서 두 AI랩이 차지하는 비중, FY2026 23%에서 FY2027 35%로 (Wells Fargo 추정)](https://img.seosoyoung.eiaserinnys.me/images/the-ai-demand-bubble/fig5.png)

Zitron은 이 대목을 이렇게 정리한다.

> The vast majority of Microsoft, Google and Amazon's AI revenues and revenue growth in their representative cloud platforms are from Anthropic and OpenAI, and they are blatantly, unashamedly misleading investors by not disclosing that this is the case.

Microsoft·Google·Amazon의 AI 매출과 그 성장의 대부분이 Anthropic·OpenAI에서 나오는데, 세 회사는 이 사실을 공시하지 않는 방식으로 투자자를 노골적으로 오도하고 있다는 것이다.

## OpenAI와 Anthropic이 없으면 AI 산업도 없다

Zitron의 논증은 단순하다. 두 랩을 빼고 나면 세 회사의 AI 매출이 얼마나 초라한지를 보라는 것이다.

![Barclays 노트에서 비-Anthropic/OpenAI 매출만 떼어낸 것. 각 열은 2025·2026·2027·2028년(뒤 셋은 추정치)](https://img.seosoyoung.eiaserinnys.me/images/the-ai-demand-bubble/fig6.png)

- **Amazon**: 2025년 자본지출은 1,318억 달러였는데, Barclays가 추정한 비-두랩 AI 매출의 약 32배다. 전체 AI 매출(96억 달러)을 넣어도 14배다. 2026년 계획대로 2,200억 달러를 쓰면, 비-두랩 매출 85억 달러의 26배, 전체 AI 매출 316억 달러의 7배가 된다. Barclays의 2028년 추정으로도 Amazon의 AI 매출은 약 750억 달러(그중 75%가 두 랩)에 그친다. AI 버블이 시작된 지 4년째의 숫자다.
- **Google**: UBS 추정대로여도 Google은 2026년 말까지 약 4,085억 달러(연말까지 남은 컨센서스 1,205억 달러 포함)를 자본지출로 써서 연 약 800억 달러 규모의 AI 사업을 만든다. 그 대부분이 Anthropic 컴퓨트를 팔거나 Vertex로 그 모델 접근을 파는 데서 나온다.
- **Microsoft**: Wells Fargo 추정으로 FY2026 AI 매출은 약 345억 달러인데, 같은 해 자본지출은 1,159억 달러였다. 마지막 분기 자본지출(410억 달러)만으로도 한 회계연도 전체 AI 매출보다 65억 달러가 많다.

누적으로 보면 격차는 더 벌어진다. Amazon은 2028년까지 6,500억 달러가 넘는 자본지출을 AI에 넣고도, (두 랩이 살아남아 청구서를 낸다는 가정 아래) 1,710억 달러 남짓한 AI 매출을 얻는 데 그칠 전망이다.

## 수요는 어디에도 없다

Zitron이 반복해서 겨냥하는 반론은 "이건 미래에 쓰일 유용한 인프라다"라는 것이다. 그는 만약 다양하고 왕성한 수요가 실재한다면 애널리스트 추정치에 그것이 잡혔을 것이라고 답한다. 세 하이퍼스케일러는 전 세계 클라우드·AI 컴퓨트의 큰 몫을 차지하므로 전체 AI 컴퓨트의 대표 표본인데, 그 표본에서 두 랩 바깥의 수요가 보이지 않는다는 것이다.

> Outside of OpenAI and Anthropic, there appears to be less than $30 billion dollars of non-AI lab compute demand across Amazon, Google and Microsoft.

OpenAI·Anthropic을 빼면 세 회사 통틀어 비-AI랩 컴퓨트 수요는 300억 달러도 되지 않아 보이며, 이마저도 Foundry·Bedrock·Vertex를 통한 두 랩 모델의 API 지출이 섞여 있어 과대 추정이라는 것이 Zitron의 진단이다.

수요 부재를 보여주는 사례로 그는 Microsoft 365 Copilot을 든다. Wells Fargo 추정으로 Copilot의 FY2026 매출은 약 38.6억 달러다. 유료 시트가 3,000만 개라는데도 그렇다. FY2027에도 약 100억 달러에 그칠 전망이다. 세계에서 가장 많이 쓰이는 업무 소프트웨어에 수만 명의 영업 인력을 붙이고도 AI 기능이 이 정도라면, 나머지 AI 소프트웨어 업계의 장기 전망은 어떻겠느냐고 그는 되묻는다.

돈의 흐름은 순환한다. 지난 7개월 동안 Google은 Anthropic에 100억 달러(최대 300억 달러 추가)를, Amazon은 Anthropic에 50억 달러, OpenAI에 총 500억 달러를 넣었다. Musk-Altman 재판에서 Microsoft 임원은 OpenAI 관계가 투자금 130억 달러와 관련 인프라를 합쳐 "1,000억 달러 넘게" 들었다고 증언했다. 하이퍼스케일러가 자기 최대 고객에게 돈을 대주고, 그 돈이 컴퓨트 비용으로 다시 하이퍼스케일러에게 돌아오는 구조다. Zitron은 세 회사가 두 랩에 넣은 자금을 합쳐 770억 달러로 집계한다.

Zitron은 특유의 조롱을 섞어 이 지점을 찌른다. 순다르 피차이가 2,880억 달러를 써서 유튜브보다 매출이 적은 사업을 만든 것이냐고, 앤디 재시가 4,295억 달러를 들여 "돈을 손에 쥐여줘야 그 돈으로 청구서를 내는" 두 회사를 위해 데이터센터를 세운 것이냐고 몰아붙인다.

## 두 개의 시한폭탄, 무엇이 먼저 무너지는가

Zitron은 앞으로의 경로를 두 갈래로 정리한다.

1. 벤처 자본과 하이퍼스케일러가 어떤 비용을 치르더라도 OpenAI·Anthropic을 영구히 떠받친다. 역사상 유례없는 순환 구조를 감수하면서.
2. 어느 날 둘 중 하나 또는 둘 다 무너진다. 그러면 AI 컴퓨트 수요와 실제 산업 생산의 절반 이상이 증발하고, 세 하이퍼스케일러가 스스로에게 매출을 먹여 온 고리도 끊긴다.

그는 여러 정황을 이 진단 위에 얹는다. OpenAI는 향후 3년 반 동안 컴퓨트에 7,500억 달러를 쓸 계획(WSJ)이라, 매출을 곧 연 수천억 달러로 키우거나 5,000억 달러 넘는 자금을 새로 조달해야 한다. Bank of America 노트가 말하는 "상위 4대 CSP"(Amazon·Google·Microsoft·Oracle)의 수주잔고 합계는 2조 3,000억 달러지만, 이는 모든 매출 계약을 포함한 값이고 그중 최소 1조 달러가 OpenAI·Anthropic 커밋먼트(The Information 기준)다. 하이퍼스케일러들의 오프밸런스시트 부채는 Meta를 포함해 1조 3,500억 달러를 넘겼다.

산업 전체 규모와 대보면 왜소함이 드러난다. Jensen Huang은 2027년 말까지 1조 달러어치 GPU 판매가 보인다고 말했다(Zitron 추정 약 40GW, 연 4,350억 달러 매출 필요). 그런데 세 회사의 FY2027 결합 AI 매출은 약 3,040억 달러, 그중 약 1,970억 달러가 AI랩 컴퓨트 지출이다.

> OpenAI and Anthropic are time bombs, and when either of them explodes, everybody will ask why we didn't see the brutality that follows coming. The truth is that nobody wanted to look.

OpenAI와 Anthropic은 시한폭탄이고, 둘 중 하나가 터지면 모두가 왜 그 참상을 예견하지 못했느냐고 물을 것이다. 진실은, 아무도 들여다보려 하지 않았다는 것이다.

## 내가 눈여겨본 지점

두 대목이 오래 남았다.

하나는 회계의 문제다. Zitron은 Google의 990억 달러, Amazon의 534억 달러 분기 이익이 Anthropic(그리고 Google의 경우 SpaceX) 지분 평가로 부풀려졌다고 지적한다. 하이퍼스케일러가 두 랩에 넣은 지분이 다시 자기 장부의 이익으로 잡히는 구조다. 매출 집중을 공시에서 빼는 것과 이 지분 평가익을 합쳐 보면, "AI가 결실을 맺었다"는 실적 서사가 얼마나 얇은 층 위에 서 있는지가 드러난다. 그가 새 규제가 시급하다고 말하는 근거다.

다른 하나는 이 글이 같은 주에 정리한 Nik Suresh의 글과 맞물린다는 점이다. Zitron은 마지막 논증에서 Suresh를 직접 인용한다. AI 서비스·구독 수요의 상당 부분이 동료 압력과 이론적 생산성 향상에 대한 준-종교적 믿음에서 온다는 대목이다. 한쪽은 조직의 의사결정이 어떻게 잠식되는지를, 다른 쪽은 그 수요가 실제 매출에서 얼마나 얇은지를 본다. 두 글을 겹쳐 놓으면, 수요의 심리적 토대와 재무적 실체가 같은 방향을 짚는다.

물론 이 글은 한쪽으로 크게 기운 논평이다. 저자의 어조는 격하고, 근거는 상당 부분 애널리스트 추정치이며(Sandler와 Ju처럼 서로 어긋나는 추정도 있다), 두 랩이 회계연도 안에 무너질 리는 없다는 점은 저자 자신도 인정한다. 그럼에도 "AI 매출을 따로 공개하지 않는다"는 사실 하나만큼은 반박하기 어렵고, 이 글의 힘은 대부분 거기서 나온다.

## 출처

Ed Zitron, "The AI Demand Bubble", Where's Your Ed At, 2026년 8월 4일.
원문: <https://www.wheresyoured.at/the-ai-demand-bubble/>

본문 차트는 원문에 실린 Barclays(Ross Sandler)·UBS(Stephen Ju)·Wells Fargo(Michael Turrin) 추정 도표를 그대로 인용했다. 차트의 세부 축·값은 원문을 함께 참조하기를 권한다.
