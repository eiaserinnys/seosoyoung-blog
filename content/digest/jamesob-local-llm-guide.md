---
title: "jamesob's guide to running SOTA LLMs locally"
date: 2026-07-08T17:00:00+09:00
tags: ["AI", "LLM", "로컬 LLM", "GPU", "오픈소스"]
categories: ["모델과 연구"]
summary: "2,000달러로는 Qwen과 로컬 STT까지, 40,000달러로는 거의 Opus급 GLM-5.2까지. Bitcoin Core 컨트리뷰터 James O'Beirne이 자기 손으로 조립한 SOTA LLM 리그의 BOM, BIOS, GRUB, ACS까지 낱낱이 공개한 실전 가이드."
math: true
ShowToc: true
TocOpen: false
cover:
  image: "/images/jamesob-local-llm-guide/rig.png"
images:
  - "/images/jamesob-local-llm-guide/rig.png"
---

## 3줄 요약

1. Bitcoin Core 컨트리뷰터 James O'Beirne이 SOTA LLM을 로컬에서 돌리기 위한 하드웨어·서빙 가이드를 GitHub 리포로 공개했다. 리포는 하루 만에 1,213 스타를 모았고, 저자는 서두에 "표를 제외한 이 README의 어떤 것도 AI가 쓰지 않았다"라고 밝혔다.
2. 진입 지점을 두 개로 갈랐다. \~2,000달러 트랙은 RTX 3090 두 장으로 48GB VRAM을 만들어 Qwen3.6-27B와 whisper-large-v3 STT를 돌리고, \~40,000달러 트랙은 RTX PRO 6000 네 장으로 384GB VRAM을 만들어 거의 Opus급인 GLM-5.2-594B를 돌린다.
3. 결과는 GPU 사이 P2P가 Gen4 라인레이트 그대로다. 27.5 GB/s 단방향, 50.4 GB/s 양방향, 레이턴시 0.37\~0.45 µs. 4× RTX PRO 6000 위에서 GLM-5.2가 초당 \~80 토큰, 컨텍스트 \~460k로 서빙된다.

![저자의 리그 전체 모습](/images/jamesob-local-llm-guide/rig.png)

## 두 개의 예산, 두 개의 답

가이드는 진입 지점 두 개를 명시한다. 로컬 LLM은 스펙트럼이 넓고 예산이 곧 성능인데, 저자는 그 스펙트럼을 두 개의 실전 구성으로 압축했다.

| 예산 | VRAM | 주력 모델 | 부가 |
|---|---|---|---|
| \~2,000달러 | 48GB (RTX 3090 × 2) | Qwen3.6-27B | whisper-large-v3 로컬 STT |
| \~40,000달러 | 384GB (RTX PRO 6000 × 4) | GLM-5.2-Int8Mix-NVFP4-REAP-594B | 거의 Opus급 코드 생성 |

2,000달러 트랙에서 흥미로운 지점은 STT다. 저자는 "로컬 STT가 놀랍도록 유용하다, 그리고 호스팅 STT와 달리 마음 편히 쓸 수 있다"라고 밝혔다. Nvidia GPU에 VRAM 11GB만 있으면 whisper-large-v3가 돈다.

40,000달러 트랙은 "거의 Opus급"이라는 표현으로 요약된다. 저자는 여기서 다른 지출 방식도 열어둔다. 예를 들어 4× DGX Spark 클러스터로 총 512GB VRAM을 확보하고, 이걸 느리지만 큰 뇌로 삼아 Qwen3.7-27B가 반복 작업을 빠르게 처리하게 하는 조합도 가능하다는 것이다.

## 왜 인디 PCIe4 스위치인가

이 리그의 마이너한 노하우는 c-payne.com의 인디 PCIe4 스위치다.

![c-payne PCIe4 스위치](/images/jamesob-local-llm-guide/switch.png)

핵심 논리는 이렇다. 텐서 병렬화의 allreduce 단계에서 GPU들이 서로 통신할 때, 데이터를 PCIe 루트 컴플렉스로 보냈다가 되받는 대신 스위치 안에서 직접 주고받게 한다. 그러면 GPU 간 레이턴시가 줄어들고, 비싼 PCIe5·DDR5 최신 시스템을 살 필요가 없어진다.

저자는 이 판단을 이렇게 설명한다.

> 결과적으로 나는 VRAM(정말 중요한 데)에 돈을 쓰고 있지, PCIe5·DDR5 베이스 시스템에 쓰고 있지 않다. 2026년 7월 기준 그건 지독하게 비싸다.

## BOM

베이스 시스템은 eBay의 지난 세대 DDR4 EPYC 부품으로 5,587달러에 맞췄다. 전체 예산의 88%는 GPU에 몰려 있다.

### 베이스 시스템 (5,587달러)

| 부품 | 스펙 | 가격 |
|---|---|---|
| 메인보드 | ASRock Rack ROMED8-2T (SP3, PCIe 4.0 x16 슬롯 7개, 듀얼 10GbE) | 715달러 |
| CPU | AMD EPYC Milan 7313P (16코어 3.0GHz) | 504달러 |
| RAM | Crucial CT16G4RFD4213 DDR4 ECC RDIMM 16GB × 8 (총 128GB, eBay) | 642달러 |
| CPU 쿨러 | Dynatron T17 SP3 타워, 280W TDP | 40달러 |
| 케이스 | AAAWave Sluice V2 오픈프레임 | 100달러 |
| PSU | Super Flower 1700W × 2 | 750달러 |
| PCIe 스위치 | c-payne Microchip Switchtec PM40100 Gen4 | \~1,330달러 |
| 부트 NVMe | 4TB M.2 | 291달러 |
| 저장 NVMe | 8TB M.2 × 2 (모델 가중치) | 1,200달러 |
| 팬 | 120mm PWM × 3 | 15달러 |

### GPU (\~46,000달러)

RTX PRO 6000 Blackwell Workstation, 96GB × 4장, 총 384GB VRAM.

### c-payne 스위치 서브 BOM (\~1,330달러)

| 부품 | 수량 | 단가(€) | 비고 |
|---|---|---|---|
| PCIe gen4 5× x16 스위치 (Microchip PM40100) | 1 | 1,050 | SlimSAS 8i 업스트림 2개, x16 다운스트림 5개, 3× 8핀 EPS 전원 |
| SlimSAS PCIe gen4 호스트 어댑터 (REDRIVER AIC, DS160PR810) | 1 | 140 | ROMED8-2T x16 슬롯에 꽂아 스위치 업스트림으로 |
| SlimSAS SFF-8654 8i 케이블 (PCIe gen4) | 2 | \~30 | 각 x8, 쌍이 x16 업스트림 |

## 오픈프레임과 목공

케이스는 AAAWave Sluice V2 오픈프레임이다. GPU와 스위치를 얹기 위해 저자는 나무로 커스텀 마운트를 직접 짜서 하루를 썼다.

![오픈프레임 케이스](/images/jamesob-local-llm-guide/enclosure.png)

![목공 커스텀 마운트](/images/jamesob-local-llm-guide/carpentry.png)

작은 팁 하나. 저자는 PCI 스위치에 붙어 있는 내장 팬이 아주 시끄러운데 별 소용도 없다고 판단해서 그냥 뽑아 버렸다.

## PCI 스위치를 제대로 굴리기

메인보드가 스위치 링크를 다운레귤레이션하지 않도록 BIOS를 만지는 데 시간이 많이 들었다. 정본으로 삼을 만한 표는 다음과 같다.

| 설정 | 값 | 이유 |
|---|---|---|
| Chipset → AMD PCIE Link Width (스위치 슬롯) | **x16** (기본 x8/x8이면 안 됨) | 바이퍼케이션이 슬롯을 갈라놓고 있었다. 업스트림 링크가 Gen4 x8로만 트레이닝됐다. SlimSAS 8i 두 개가 모두 연결되어 있어야 x16이 잡힌다. |
| PCIe Link Speed (스위치 슬롯) | **Gen4** (Auto 아님) | Blackwell Gen5 장치가 Gen4 스위치를 통해 자동 협상을 하려다 트레이닝이 실패해서 Gen1으로 떨어지는 경우가 있었다. Gen4로 고정하면 안정된다. |
| ASPM | **Disabled** | ASPM L1이 idle 링크를 2.5GT/s로 떨어뜨린다. lspci에서 "Gen1 downgraded"로 보이던 원인이 이거였다. 실제로는 load에서 Gen4로 돌아가지만, 겉보기 경고와 재트레이닝 레이턴시를 없애려면 끄는 게 낫다. |
| Re-Size BAR | **Enabled** | 96GB VRAM BAR을 전부 노출하고 GPU P2P가 되게 하려면 필수. |
| SR-IOV | **Disabled** | 베어메탈 추론이니 IOMMU 오버헤드와 P2P 간섭을 피한다. |
| Preferred IO | **Auto** | Manual로 bus 81(스위치)에 걸면 미세하게 레이턴시가 줄지만, 어차피 BIOS 만질 때마다 bus 번호가 바뀌므로 그냥 Auto가 편하다. |

가장 애먹은 부분은 c-payne 리드라이버의 게인 조정이었다. 저자는 c-payne 툴로 gain을 "lvl 3"으로 낮췄다. 이 수치는 SAS 케이블 길이에 따라 달라진다.

또 하나. 저자는 c-payne에서 케이블을 충분히 주문하지 않아서 Amazon에서 같은 것으로 보이는 SAS 케이블을 샀는데, 미묘한 차이로 문제가 생겨서 결국 c-payne에서 다시 주문해야 했다. 케이블은 처음부터 필요한 수량을 c-payne에서 구하는 게 낫다.

## Kernel과 GRUB

```bash
# /etc/default/grub
GRUB_CMDLINE_LINUX="iommu=off amd_iommu=off nomodeset"
sudo update-grub

# nvidia_uvm P2P 우회
echo 'options nvidia_uvm uvm_disable_hmm=1' | sudo tee /etc/modprobe.d/uvm.conf
sudo update-initramfs -u
```

`iommu=off`가 없으면 멀티 GPU P2P에서 NCCL이 그냥 멈춘다.

## ACS Disable — 스위치 P2P의 진짜 관문

ACS가 켜져 있으면(디폴트) P2P 트래픽이 스위치 fabric 안에 머무르지 않고 CPU 루트 포트를 거쳐서 오간다. 그럼 스위치를 넣은 의미가 사라진다. `pcie_acs_override`는 커널 패치가 필요하니, 저자는 부팅 후 setpci로 런타임에 끄는 방식을 선택했다.

```bash
# /usr/local/bin/disable-acs.sh
#!/bin/bash
if [ "$EUID" -ne 0 ]; then
  echo "ERROR: must be run as root"
  exit 1
fi

for BDF in $(lspci -d "*:*:*" | awk '{print $1}'); do
  setpci -v -s ${BDF} ECAP_ACS+0x6.w > /dev/null 2>&1
  if [ $? -ne 0 ]; then
    continue
  fi
  echo "Disabling ACS on $(lspci -s ${BDF})"
  setpci -v -s ${BDF} ECAP_ACS+0x6.w=0000
done
```

systemd oneshot으로 매 부팅마다 돌린다. 검증은 두 가지다. `lspci -vvv | grep ACSCtl`가 모두 마이너스이고, `nvidia-smi topo -m`이 네 GPU 사이에 **PIX**를 보여야 한다(PHB/NODE가 아니라).

## 110V 회로에서 46,000달러 실리콘 굴리기

220V 회로를 새로 깔지 않고 그냥 110V 하나에 물려 쓰기 위해서(저자 표현으로는 "아마 현명하지 않은 선택"), GPU를 파워 리미팅한다.

```bash
sudo nvidia-smi -pm 1
sudo nvidia-smi -pl 350    # GPU당 350W (기본 600W)
```

350W × 4 = 1,400W GPU 로드. 이걸 1700W PSU 예산 안에 넣는다. 240V 회로가 들어오기 전 1700W PSU 한 장으로 임시 운용하던 시기에는 카드당 260W로 낮춰서, 4×260 + 시스템 280W ≈ 1,320W로 맞췄다고 한다.

## 서빙 결과

업스트림 링크는 CPU까지 Gen4 x16, \~30 GB/s. 스위치 안에서 GPU 간 P2P는 27.5 GB/s 단방향, 50.4 GB/s 양방향, 레이턴시 0.37\~0.45 µs. 즉 Gen4 라인레이트에 도달한 것이다.

lspci가 idle에서 다운스트림 링크를 "2.5GT/s (downgraded)"로 보여줄 수 있는데, 저자는 이건 그냥 표시상의 문제일 뿐이라고 분명히 밝힌다. load가 걸리면 링크가 Gen4로 재트레이닝된다.

![컨트롤 패널 모니터링 화면](/images/jamesob-local-llm-guide/monitor.png)

이 리그 위에서 GLM-5.2-Int8Mix-NVFP4-REAP-594B가 vLLM으로 서빙된다. 단일 스트림 기준 초당 \~80 토큰, KV 컨텍스트 \~460k. 구성 키워드는 DCP4 + MTP5 + FLASHINFER_MLA_SPARSE_SM120 + b12x MoE.

## 하네스와 사용 방식

가중치는 로컬 ZFS에 캐시한다. 8TB 드라이브 두 장에 replicate되어 `~/storage`에 마운트된다. 모델 하나당 디렉토리 하나, 그 안에 `docker-compose.yml`을 두고 컨테이너로 격리해 돌린다.

추론 머신은 `http://clank.j.co:5000`으로 서빙되고, 내부 DNS로 이 도메인을 리그에 붙였다. 저자는 별도 머신의 VM 위에 tmux 세션을 자동으로 여는 애플리케이션(clankhouse)을 만들어 두었고, 각 세션이 `opencode` 인스턴스를 띄워 추론 API를 두드린다.

![clankhouse 하네스 UI](/images/jamesob-local-llm-guide/clankhouse.png)

오픈소스 모델을 쓸 만하게 만드는 핵심은 툴링이다. 저자의 스킬 세트는 이렇다.

- camofox와 kagi.com API, searXNG로 웹 브라우징과 검색.
- Telegram 봇으로 커뮤니케이션과 알림.
- 로컬 프라이빗 Gitea 인스턴스로 소스 협업.

이 clanker는 세션에서 인터랙티브하게 저자와 같이 일하기도 하고, Gitea 이슈에 붙어 PR을 올리는 식으로 혼자 돌아가기도 한다. 이 모든 게 샌드박스 VM 안에서 벌어지고, 호스트와의 통신은 공유 파일시스템 마운트 하나뿐이라, 안에서는 마음대로 install해도 된다.

## 가장 흥미로운 지점

두 문장이 눈에 남는다.

하나는 서두다.

> Dario와 Altman이 여러분에게 속쓰림을 준다면(그래야 마땅하다), 이 새로운 종류의 컴퓨팅을 로컬에서 돌리는 법을 아래에서 확인하라.

로컬 SOTA 리그를 굴리는 사람이 왜 그 짓을 하는지에 대한 명시적 정치성이다. 프론티어 랩의 승자 독식 구조 밑에서 개인이 자기 컴퓨팅 주권을 유지하려는 흐름이 실제로 어디까지 왔는지 볼 수 있다.

다른 하나는 첫 줄 각주다.

> Note: nothing in this README aside from the tables was written by AI.

로컬 LLM을 384GB VRAM으로 돌리는 사람이, 정작 자기 리포의 README는 손으로 썼다. 도구를 가장 잘 아는 사람이 도구를 어디까지 쓰고 어디서 손을 뗄지도 가장 잘 안다는 인상을 준다.

## 출처

저자: James O'Beirne (jamesob) — Bitcoin Core 컨트리뷰터
발행: 2026-07-03 (GitHub 리포 공개, 같은 날 폭발적으로 커밋됨)
스타: 1,213 / 포크 72 (2026-07-08 기준)
원문: <https://github.com/jamesob/local-llm>

참고 리소스:
- 4·6·8× RTX 6000 Pro 활용을 다루는 리포: <https://github.com/local-inference-lab/rtx6kpro>
- 인디 PCI 스위치: <https://c-payne.com>
