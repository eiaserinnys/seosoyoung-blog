---
title: "Unreal Engine: 1000 NPCs In Multiplayer Without Network Saturation"
date: 2026-07-05T08:00:00+09:00
tags: ["게임", "Unreal Engine", "멀티플레이어", "네트워크 최적화", "게임 개발"]
categories: ["게임"]
summary: "dead reckoning·snapshot interpolation 계열의 오래된 네트워크 동기화 원리를 언리얼 엔진 1,000+ NPC 스케일에 맞춰 튜닝한 Vladimir Khanin의 실증을 Jettelly가 정리했다."
ShowToc: true
TocOpen: false
cover:
  image: "/images/khanin-npc-movement-segments-ue/segment-diagram.png"
images:
  - "/images/khanin-npc-movement-segments-ue/segment-diagram.png"
---

## 3줄 요약

1. Jettelly 블로그가 시니어 언리얼 엔진 개발자 <strong>Vladimir Khanin</strong>의 실험을 정리한 노트다. 원문 발행은 2026년 4월 10일.
2. 서버가 NPC의 매 순간 위치를 전송하는 대신 <em>어떻게, 언제 움직일지</em>를 기술하는 movement segment를 보내는 방식으로, 1,000개 이상의 NPC를 접속 문제 없이 처리했다.
3. 각 segment는 시작 위치·방향·거리·수직 오프셋·지속시간·식별자로 구성되며, 정적 NPC는 트래픽을 만들지 않고 매 tick 전체 엔티티가 아닌 일부만 전송해 대역폭이 분산된다.

## 문제 — 위치 리플리케이션의 확장 한계

멀티플레이어 게임에서 엔티티가 많아질 때 흔히 부딪히는 벽은 네트워크다. 각 NPC가 자기 위치를 서버에 지속적으로 전송해야 하므로 개수가 늘어날수록 데이터양과 포화가 함께 커지고, 어느 시점부터는 실행이 어려워진다.

Khanin의 실험은 이 전제 자체를 뒤집는다. <em>서버가 NPC의 위치를 알려주지 않는다.</em> 대신 <strong>어떻게 그리고 언제</strong> 움직일지를 알려준다.

## 해법 — 위치 대신 movement segment를 전송한다

서버는 NPC의 이동을 시작점 <strong>(A)</strong>에서 <strong>(B)</strong>까지 <strong>특정 프레임 수</strong>에 걸쳐 진행되는 하나의 segment로 기술해 클라이언트에 보낸다. 각 segment에는 다음이 담긴다.

- 양자화(quantized)된 시작 위치
- 수평 이동을 위한 방향과 거리
- 별도의 수직 오프셋, 그리고 이동의 지속시간
- 순서와 상태 유지를 위한 식별자와 작은 플래그들

클라이언트는 segment를 받으면 목적지를 재구성하고, 정해진 프레임 수 동안 이동을 재생한다. 새 segment가 도착하면 식별자를 기준으로 이전 segment를 교체한다. 서버의 지속적 업데이트에 의존하지 않고도 연속성이 유지되는 이유다.

![언리얼 엔진의 Network Profiler로 본 replication 트래픽. BubbleSerializer, ChangedElement, MotionFragment 단위로 packet이 나뉘어 분산된다.](/images/khanin-npc-movement-segments-ue/segment-diagram.png)

## 데이터 분배 — 매 tick 전체를 보내지 않는다

Khanin이 특히 강조한 부분은 <em>데이터가 어떻게 분배되는가</em>다.

- 한 tick에 모든 엔티티를 몰아 보내지 않고, 각 업데이트마다 전체 중 일부만 전송한다.
- 움직임이 변할 때만 데이터를 보낸다. NPC가 정지해 있으면 트래픽은 발생하지 않는다.

즉, 개수에 비례해 대역폭이 선형 증가하는 대신, 실제로 상태가 바뀐 NPC의 수와 부분 전송 주기에 따라 총 트래픽이 결정된다. 위 스크린샷에서 packet 6,571이 여러 `ChangedElement`(159\~162 bits)와 `MotionFragment`(110\~113 bits) 조각으로 나뉘어 있는 모습이 그 배치를 그대로 보여준다.

## 가장 흥미로운 지점

먼저 계보를 정리해 두는 편이 정확하겠다. 이 방식은 FPS 엔진 네트워크 동기화의 <em>기본기</em>다. 서버가 매 tick 위치를 보내지 않고 방향·속도·시간을 보내면 클라이언트가 자체 시뮬레이션하는 <strong>dead reckoning</strong>, 서버 snapshot 사이를 클라이언트가 보간하는 <strong>snapshot interpolation</strong>, 상태 전체 대신 변경분만 보내는 <strong>delta encoding</strong> — 1990년대 밀리터리 시뮬레이션에서 Quake·Half-Life·Overwatch로 넘어오며 이미 정립된 계보다. Khanin의 실험은 그 원리를 새로 만든 것이 아니라, <em>1,000+ NPC 스케일에 맞춰 튜닝한 실증</em>으로 읽는 것이 정직하다.

그 위에서 눈여겨본 실전 감각의 결정 두 가지.

첫째, <strong>수평 이동과 수직 오프셋의 분리</strong>. 계단·경사·점프처럼 수직축이 급변하는 상황을 수평 궤적과 같은 예산으로 뭉치면 압축·양자화 손실이 커지는데, 분리해 두면 축별 정밀도를 상황에 맞게 다르게 잡을 수 있다.

둘째, <strong>매 tick 전체가 아닌 부분 전송 스케줄링</strong>과 <strong>정지 NPC 트래픽 무</strong>. 대역폭 총량을 NPC 개수가 아니라 "실제로 상태가 바뀐 NPC의 수 × 부분 전송 주기"로 다시 묶는다. 스케일이 커질수록 이 재정의가 결정적이 된다.

한계도 함께 눈에 들어온다. segment가 재생되는 동안 서버 측 물리·AI가 궤도를 급변경해야 하는 상황(플레이어 개입, 근접 회피 등)에서는 identifier로 새 segment를 교체하는 지연이 체감될 수 있다. 원문은 정지 NPC의 트래픽 절감과 부분 전송으로 얻는 이득을 강조하지만, 반응성이 중요한 상호작용까지 이 구조가 그대로 확장되는지는 다루지 않는다.

## 출처

- 발행: Jettelly 블로그, 2026-04-10
- 원 실험자: Vladimir Khanin (Senior Unreal Engine Developer)
- 원문: <https://jettelly.com/blog/adding-more-than-1000-npcs-in-multiplayer-without-network-saturation-in-unreal-engine/>
- Khanin의 LinkedIn: <https://www.linkedin.com/in/vladimir-khanin-1028529a/>
