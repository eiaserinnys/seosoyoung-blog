---
title: "Induction of cortical on/off periods in awake mice fulfills sleep functions"
date: 2026-06-09T17:30:00+09:00
tags: ["신경과학", "수면", "시냅스 항상성", "광유전학", "기억 통합"]
categories: ["모델과 연구"]
summary: "위스콘신 대학 Tononi·Cirelli 팀의 Nature Neuroscience 논문(2026.06.08). 깨어 있는 쥐의 대뇌 피질에 광유전학으로 NREM 수면 같은 on/off 패턴을 인위적으로 만들면, 단순한 발화 감소로는 불가능한 수면의 핵심 기능(국소 수면 압력 해소, 시냅스 다운셀렉션, 기억 통합)이 깨어 있는 동안에도 일어난다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/driessen-awake-on-off-periods-2026/fig1.png"
  alt: "Fig. 1: Chronic recording and optogenetic manipulation of local cortical networks."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/driessen-awake-on-off-periods-2026/fig1.png"
---

## 3줄 요약

1. 위스콘신 대학 Tononi·Cirelli 그룹이 2026년 6월 8일 *Nature Neuroscience*에 발표한 논문이다. 깨어 있는 쥐의 한쪽 대뇌 피질에 광유전학으로 NREM 수면 같은 on/off 신경 활동을 강제로 유도하고, 그 결과 수면의 핵심 기능 세 가지(서파 활동·동기성 감소, 시냅스 강도 분자 마커 감소, 기억 통합)가 그 회로에서 일어나는지를 검증했다.
2. 자극받은 쪽 반구는 이후 NREM 수면에서 서파 활동(SWA)과 신경 동기성이 반대쪽 대조 반구보다 유의하게 낮아졌고, 시냅스 강도 마커인 GluA1 함유 AMPA 수용체와 그 845번 인산화 수준도 같이 떨어졌다. 같은 정도로 발화율만 누른 비교군(halorhodopsin)은 두 효과가 모두 없었다.
3. 학습 직후 1시간 동안 수면 박탈을 하면서 운동·감각피질 양쪽에 off period를 함께 유도한 쥐는, 정상적으로 잠을 잔 쥐와 같은 수준으로 24시간 후 새 바닥 질감 회상 과제를 통과했다. 수면이 시냅스에 하는 일은 *어두움*이 아니라 *on/off 교차* 그 자체가 한다는 직접적 증거가 된다.

## 자료 정보

- 제목: *Induction of cortical on/off periods in awake mice fulfills sleep functions*
- 저자: Kort Driessen, Fabio Squarcio, Giulio Tononi, Chiara Cirelli (University of Wisconsin–Madison)
- 저널: *Nature Neuroscience*
- 게재: 2026년 6월 8일
- 원문: <https://www.nature.com/articles/s41593-026-02318-9>
- 분석 코드: <https://github.com/CSC-UW/OFF_PERIOD_INDUCTION_MATERIALS>

## 배경 — SWA·on/off·시냅스 항상성

NREM 수면의 정의 자체가 *대규모 동기 활동*과 *on/off 교차*다. 피질 신경 집단의 발화가 높은 활성(on period)과 거의 침묵(off period) 사이를 수백 밀리초 단위로 오가고, 이 패턴이 EEG에서 0.5\~4 Hz 서파(SWA)로 잡힌다. SWA는 잠들 필요(sleep need)의 직접적 지표로, 깨어 있는 시간이 길수록 올라가고 잠을 자면 내려간다.

같은 시간의 깨어 있음 동안 피질 흥분성 시냅스의 평균 강도가 강해진다는 가설이 *시냅스 항상성 가설*(SHY, Tononi·Cirelli)이다. 잠은 그 강해진 시냅스를 *균등하게 약화*시켜 회로의 신호 대 잡음비를 회복시키고, 그 부산물로 기억이 *선별적으로* 통합된다. SWA가 그 다운셀렉션의 *원인적 매개*인지, 단순히 *부수 신호*인지는 오래 열려 있던 질문이었다.

이 논문은 그 질문에 직접 답하기 위해, 깨어 있는 쥐에게 on/off 패턴만 분리해 *주입*해 본다. on/off가 시냅스 항상성의 원인 매개라면, 잠을 자지 않아도 효과가 나와야 한다.

## 실험 설계

<small>Fig. 1. 양반구 대뇌 피질에 16채널 실리콘 프로브 + 광섬유(optrode)를 이식한다. 한쪽은 자극·기록, 반대쪽은 동형(homotopic) 대조군으로 작동한다. (출처: Driessen et al., 2026, Nature Neuroscience, CC BY 4.0)</small>

쥐의 양쪽 피질 동일 부위에 실리콘 프로브를 이식하고, 한쪽에만 광섬유를 붙여 *광유전학으로 같은 동물 안에서 자극측·대조측을 동시에 비교*하는 구조다. 세 가지 광유전학 모델을 비교해 효과의 *원인 변수*를 분리한다.

| 모델 | 표적 뉴런 | 자극 시 효과 | 검증 목적 |
|---|---|---|---|
| **SOM+** (Sst-Cre × Ai32) | 소마토스타틴 발현 억제 뉴런 | 양극 서파 + 피라미드 뉴런 침묵 | 자연 NREM 슬로우 웨이브와 가장 유사한 on/off 유도 |
| **ACR** (CaMKIIα-Cre × stGtACR1) | 피라미드 뉴런 직접 억제 | 음극 서파 + 발화 침묵 | 다른 기전으로도 같은 효과가 나오는지 |
| **Halorhodopsin** (CaMKIIα-Cre × eNpHR3.0) | 피라미드 뉴런 지속 억제 | 발화율 *지속* 감소, on/off 없음 | "발화 감소 자체"가 원인인지 분리 |

자극 프로토콜은 표준화되어 있다. 라이트 켜진 시각 직후 5시간 동안 새 물건을 넣어 강제로 깨운 다음(SD), 마지막 30분 동안 한쪽 반구에만 on/off 또는 지속 억제를 가하고, 이후 1시간 동안의 NREM 회복 수면을 양반구에서 동시에 기록한다.

## 발견 1 — 깨어 있을 때 만든 off period가 *그 반구의* 수면 압력을 미리 푼다

![Fig. 2: Off-period induction during wake reduces SWA and synchrony in subsequent sleep.](https://img.seosoyoung.eiaserinnys.me/images/driessen-awake-on-off-periods-2026/fig2.png)
<small>Fig. 2. 자극측(파랑) vs 대조측(주황)의 회복 NREM 1시간 동안 SWA와 동기성 지표 비교. (출처: 같은 논문)</small>

SD 마지막 30분 동안 한쪽 반구에만 NREM 같은 off period를 유도한 결과:

- **자극 시점**: 자극받은 반구의 SWA는 자연 NREM에 가까운 수준까지 올라가고, 반대쪽은 깨어 있는 상태 그대로다.
- **자극 종료 후 1시간 NREM**: 자극받은 반구의 SWA는 반대쪽보다 *낮다*. 즉 이 반구는 *이미 잠을 잔 것처럼* 수면 압력이 풀려 있다.
- **수면 구조 자체는 그대로**: NREM·REM 비율, 수면 분절 길이, 마이크로각성 빈도는 차이 없다. 떨어진 것은 *서파 깊이*뿐이다.
- **동기성 세 지표 모두 감소**: off period 시작 기울기, 서파 피크 진폭, off period 종료 기울기 모두 자극측에서 낮다. spike-time tiling coefficient(STTC)로 잰 페어와이즈 동기성도 자극측에서 떨어졌다.
- **회복 시간**: SWA 격차는 몇 시간 안에 좌우가 다시 같아진다. 영구 변화가 아니라 *그날 분의 수면 빚을 미리 갚은* 수준이다.

쥐 행동에는 변화가 없었다. 멈추는 빈도, 좌우 회전 선호 모두 그대로다. 즉 자극받는 동안에도 쥐는 정상적으로 깨어 행동하고 있었다.

## 발견 2 — *발화 감소*만으로는 효과가 없다 (가장 중요한 분리 실험)

![Fig. 3: Tonic inhibition using halorhodopsin does not reduce SWA or synchrony in subsequent sleep.](https://img.seosoyoung.eiaserinnys.me/images/driessen-awake-on-off-periods-2026/fig3.png)
<small>Fig. 3. halorhodopsin으로 같은 정도의 발화율 감소를 만들었을 때는 회복 NREM의 SWA·동기성·발화 모두 좌우 차이가 없다. (출처: 같은 논문)</small>

halorhodopsin 모델은 같은 30분 동안 자극측 발화율을 SOM+/ACR과 *같은 폭으로* 눌렀다. 차이는 단 하나, on/off 교차가 일어나지 않고 발화가 지속적으로 가라앉아 있다는 것이다.

결과는 깨끗하게 갈렸다. 자극측과 대조측 사이에 SWA, off period 빈도·지속, 슬로우 웨이브 진폭, 발화율, 스파이크 동기성, 어느 지표에서도 유의한 차이가 나오지 않았다. 같은 SOM+ 쥐들에게 지속적인 사인파 자극으로 발화를 *지속* 감소시킨 추가 실험에서도 결과는 동일했다.

저자들은 이 비교를 통해 *발화 감소 자체가 수면 압력을 푸는 것이 아니다*라는 결론에 도달한다. on/off 교차의 *교차* 그 자체가 시냅스에 작용하는 신호로 보인다. 회복 SWA를 같은 쥐 안에서 on/off 유도와 발화 감소로 각각 시도한 짝지은 비교에서, 모든 쥐에서 on/off가 더 효과적이었다.

## 발견 3 — 시냅스 강도 분자 마커가 자연 수면 후만큼 감소한다

![Fig. 4: Off-period induction during wake reduces molecular markers of cortical excitatory synaptic strength.](https://img.seosoyoung.eiaserinnys.me/images/driessen-awake-on-off-periods-2026/fig4.png)
<small>Fig. 4. 자극 직후 바로 안락사한 쥐의 양반구 두정엽 피질 시냅토뉴로솜에서 GluA1·pGluA1(845) 수준 비교. (출처: 같은 논문)</small>

전기생리 외에 *분자* 증거도 확보했다. 두정엽 위에 4개 광섬유를 1mm 간격으로 이식한 쥐들로 동일 SD + 30분 off 유도 프로토콜을 돌리고, *잠을 자지 않은 상태에서* 즉시 양반구 피질을 채취해 시냅토뉴로솜을 분리한 다음 흥분성 시냅스 강도의 두 표준 마커를 측정했다.

- **GluA1 함유 AMPA 수용체** — 자극받은 반구에서 유의하게 감소
- **GluA1 serine 845 인산화** — 자극받은 반구에서 유의하게 감소

두 마커의 변화 방향과 크기가 *6\~7시간의 자연 NREM 수면 후* 관찰되는 변화와 일치한다. 잠을 한 번도 자지 않았는데도 시냅스 다운셀렉션의 분자 흔적이 그 반구에서만 따로 일어난 것이다. 야생형 대조군에서는 변화 없음.

## 발견 4 — 양측 off 유도로 SD 후 기억 통합을 *회복*시킨다

![Fig. 5: Bilateral off induction during SD recovers memory performance in a novel FTR task.](https://img.seosoyoung.eiaserinnys.me/images/driessen-awake-on-off-periods-2026/fig5.png)
<small>Fig. 5. 새 바닥 질감 인식(FTR) 과제 결과. SD + 양측 off 유도 그룹(보라)이 정상 수면 그룹(파랑) 수준으로 회복. (출처: 같은 논문)</small>

마지막 실험은 *기능* 수준이다. 새 바닥 질감 인식(novel floor texture recognition, FTR) 과제는 학습 후 잠을 자면 24시간 후 새 질감 쪽에 더 오래 머무는 행동이 강화되고, 학습 직후 1시간 잠을 박탈하면 그 효과가 사라지는 것으로 알려져 있다.

저자들은 SOM+ 쥐에게 운동피질 M2와 1차 감각피질 S1 양쪽에 광섬유 4개를 이식하고, 학습 직후 1시간 SD를 가하면서 *그 SD 동안 양측 off 유도를 동시에 진행*했다. 결과:

| 그룹 | 회상기(24h 뒤) 새 질감 쪽 체류 시간 |
|---|---|
| 학습 후 정상 수면 | 정상 회상 |
| 학습 후 1시간 SD | 회상 실패 |
| 학습 후 1시간 SD + 양측 off 유도 | 정상 수면군과 동등 수준으로 회복 |

이 그룹들 사이에 1시간 후·6시간 후 누적 수면량이나 활동량 차이는 없었다. 즉 *후속 수면이 더 들어가서* 회복된 게 아니라, *SD 동안 강제 주입한 on/off 자체가* 기억 통합을 일으켰다는 해석이 가능하다.

## Discussion 요점

- SOM+ 인터뉴런은 자연 NREM에서도 슬로우 웨이브를 일으키는 *마스터 조절자*다. 다른 모든 세포 유형을 억제하면서 자기 자신은 억제하지 않는 구조라, 일정 임계점 이상 SOM+ 발화가 모이면 회로 전체가 off로 떨어진다. 깨어 있는 동안 SOM+를 직접 켜서 이 임계점을 인공적으로 넘기는 것이 이 논문의 핵심 도구다.
- 한쪽 반구만 잠을 자는 *단반구 수면*이 돌고래·물개·일부 새 종에서 진화한 사실이 이 연구의 진화적 정당화 근거다. 사람은 그 능력을 잃었지만, *기술적으로 on/off만 외부에서 주입*할 수 있다면 비슷한 이득을 끌어올 여지가 있다.
- 다만 저자들도 단서를 명확히 단다. 이 실험으로 약화된 것은 *국소 회로 수준*의 시냅스 강도와 기억이다. 뇌 전체 수준의 통합(systems consolidation), 자발적 광역 회로 재활성을 통한 *원격 기억* 형성, 노폐물 제거 같은 *진짜 잠* 동안만 일어나는 기능들은 여전히 잠 그 자체가 필요할 가능성이 높다.
- 자극 자체가 자연 NREM과 완벽히 같지는 않다. 유도 off period 후에는 자연 off보다 *수면 방추파(spindle)가 적게* 따라온다. 시상-피질 루프가 그대로 작동하지 않는다는 신호로 읽힌다.
- 노르아드레날린·아세틸콜린이 깨어 있는 동안에는 높지만, 그 상태에서도 on/off 주입으로 AMPA 수용체가 줄었다는 사실은 시냅스 약화의 분자 경로가 *낮은 신경조절물질만 필요로 하는 게 아니라* 활동 폭발(activity bursts) 자체로 트리거될 수 있음을 시사한다.

## 가장 흥미로운 지점

연구의 진정한 의미는 *halorhodopsin 음성 결과*에 있다. 두 그룹의 평균 발화율은 정확히 같다. 다른 점은 *시간 구조*뿐이다. 한쪽은 활동이 매끄럽게 눌려 있고, 한쪽은 같은 평균 위에서 수백 밀리초 단위로 켜졌다 꺼졌다 한다. 시냅스는 그 *시간 구조*에 반응한다.

시냅스가 *얼마나 활성되었는가*가 아니라 *어떤 리듬으로 활성되었는가*를 듣고 있다는 뜻이다. 이는 수면의 본질을 *휴식*이나 *활동량 감소*로 보던 직관에 균열을 낸다. 잠은 활동을 *멈추는* 것이 아니라 *특정 리듬으로 다시 짜는* 일이다. 그래서 SHY가 "잠을 못 자면 뇌가 피곤해진다"가 아니라 "잠을 못 자면 회로의 신호 대 잡음비가 떨어진다"고 말해 온 것이 이번 실험으로 직접 증명되었다.

이 결론을 진지하게 받으면, 의료·수면 부족 사회에서 BCI나 비침습 자극(tACS, 경두개 자기자극)으로 *깨어 있는 동안에도 on/off 리듬을 인위적으로 주입*하는 응용을 상상해 볼 수 있다. 저자들도 토론에서 그 방향을 짚는다. 단, 광역 systems consolidation은 여전히 잠이 필요하므로 잠을 *대체*하는 기술이 아니라 *수면 부채를 부분 상환*하는 기술이 될 가능성이 높다.

또 하나 흥미로운 지점은 단일 뉴런 분석에서 약 1/3의 뉴런 쌍은 이 항상성 조절에 *참여하지 않는다*는 관찰이다. 자연 NREM의 초기·후기 사이에서도 STTC 변화가 없는 이 1/3 그룹은 *시냅스 다운셀렉션을 면제받는* 회로로 보인다. 어떤 뉴런이 면제되고 어떤 뉴런이 약화되는지가 곧 기억의 *무엇이 남고 무엇이 사라지는지*를 결정한다면, 이 1/3의 정체가 다음 질문이 된다.

## 출처

Driessen, K., Squarcio, F., Tononi, G., & Cirelli, C. (2026). Induction of cortical on/off periods in awake mice fulfills sleep functions. *Nature Neuroscience*. Published online June 8, 2026.

원문: <https://www.nature.com/articles/s41593-026-02318-9>
분석 코드 리포: <https://github.com/CSC-UW/OFF_PERIOD_INDUCTION_MATERIALS>

이미지 인용은 모두 Driessen et al. (2026), *Nature Neuroscience*, CC BY 4.0 라이선스에 따른다.
