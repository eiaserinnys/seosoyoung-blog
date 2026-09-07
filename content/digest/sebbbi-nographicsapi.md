---
title: "NoGraphicsAPI"
date: 2026-09-07T19:20:00+09:00
tags: ["그래픽스", "Vulkan", "GPU", "렌더링", "오픈소스"]
categories: ["게임"]
summary: "세바스티안 알토넨은 2025년 말에 최소 그래픽 API를 제안했다. 2026년 9월에는 그 제안을 Vulkan 1.4 위에 실제로 구현해 MIT 라이선스로 공개했다. 버퍼 객체와 디스크립터 셋과 파이프라인 레이아웃을 모두 없애고 64비트 GPU 포인터로 대체했으며, 공개 헤더는 726행이다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/sebbbi-nographicsapi/01-cover.png"
  alt: "치비 서소영이 산더미처럼 쌓인 두꺼운 명세서 탑 옆에서 얇은 종이 한 장만 들어 올리고 있고, 바닥의 GPU 칩에서 뻗은 하늘색 실 한 줄이 그 종이로 이어진다"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/sebbbi-nographicsapi/01-cover.png"
---

## 3줄 요약

1. 그래픽스 엔지니어로 30년을 일한 세바스티안 알토넨은 2025년 12월 「No Graphics API」에서 현대 GPU에 맞춘 최소 그래픽 API를 제안했다. 그리고 2026년 9월 4일에는 그 제안을 Vulkan 1.4 위에 구현한 `NoGraphicsAPI`를 MIT 라이선스로 공개했다.
2. 이 구현은 버퍼 객체와 디스크립터 셋, 디스크립터 레이아웃, 파이프라인 레이아웃, 샘플러 객체를 공개 API에서 모두 제거했다. 그 자리를 64비트 GPU 포인터와 애플리케이션이 직접 소유하는 디스크립터 힙, 그리고 리소스 목록이 없는 전역 배리어가 채운다.
3. 그런데 이 API를 지금 당장 실행할 수 있는지는 기기와 드라이버 조건에 따라 다르다. AMD RDNA 3과 RDNA 4, 그리고 NVIDIA 튜링 이후 세대는 필요한 확장을 모두 노출하지만, 윈도우의 RDNA 2와 인텔 Arc는 그렇지 않다.

## 무엇이 공개됐는가

`sebbbi/NoGraphicsAPI`는 2026년 8월 31일에 만들어졌고, 공개된 커밋 이력은 9월 4일 "Add README"에서 시작한다. 그 뒤 사흘 동안 30개 커밋이 쌓였고, 9월 7일 기준으로 별 1,027개와 포크 28개가 붙었다. 라이선스는 MIT다.

구현체는 Vulkan 1.4를 백엔드로 쓰고 셰이더는 Slang으로 작성한다. 예제는 세 개가 들어 있다.

| 예제 | 줄 수 | 내용 |
| --- | ---: | --- |
| `triangle` | 66 | 정점과 픽셀 셰이더로 삼각형 하나를 그려 화면에 표시하는 최소 경로 |
| `cube` | 240 | 타입이 붙은 GPU 포인터로 정점을 읽고, 애플리케이션이 소유한 텍스처와 샘플러 힙을 쓴다 |
| `deferred_renderer` | 388 | 컴퓨트 시뮬레이션과 메시 셰이더 렌더링을 여러 패스로 엮고, 패스 사이에 배리어를 두고 타임라인으로 CPU와 GPU를 겹친다 |

리포지토리는 스스로를 프로토타입이라고 밝힌다. 의도적으로 단일 스레드로 동작하고 큐도 하나만 쓴다. 레이트레이싱, 태스크 셰이더, 스파스 메모리, 파이프라인 캐싱, MSAA, Win32 이외 환경의 화면 표시, Metal 백엔드는 아직 구현 범위 밖이다. Metal 4 이식은 `docs/metal-porting.md`에 설계와 미해결 과제만 기록되어 있다.

## 원 제안이 겨눈 문제

원 글은 2025년 12월 16일에 발행됐다. 알토넨은 자기 소개 페이지에서 30년 동안 그래픽스 코드를 써 왔고 1999년에 3D 가속 게임을 처음 출시했다고 밝힌다. 그 뒤 그는 유비소프트의 사내 엔진 여러 개를 만들었다. 언리얼 엔진 4를 최적화했고, 유니티의 DOTS 그래픽스 팀을 이끌었다. 지난 4년 동안은 하이프하이프의 새 렌더러를 WebGPU와 Metal, Vulkan을 겨냥해 만들고 있다. 그리고 그는 Vulkan 자문 패널의 일원이자 Arm 앰배서더다. 이 글은 2026년 SIGGRAPH의 ARM Moving Mobile Graphics 코스에서 「Reducing graphics API complexity: A clean slate API design for modern hardware」라는 제목의 발표로도 이어졌다.

알토넨은 첫 문단부터 파이프라인 상태 객체, 즉 PSO의 순열 폭발을 문제로 지목했다.

> 파이프라인 상태 객체(PSO) 폭발이 손을 벗어났다. 어쩌다 우리는 100GB짜리 로컬 셰이더 파이프라인 캐시와 그것을 호스팅하는 거대한 클라우드 서버에 이르게 되었나?

![치비 서소영이 서랍장에서 쏟아져 나온 똑같은 상태 카드 무더기 앞에서 개수를 세다가 손을 들고 당황하는 모습](https://img.seosoyoung.eiaserinnys.me/images/sebbbi-nographicsapi/02-pso.png)

알토넨의 진단은 이렇다. DirectX 12와 Vulkan, Metal은 흔히 "모던 API"로 불리지만 이제 열 살이 됐고, 설계 당시 지원해야 했던 GPU는 지금 기준으로 열세 살이다. 당시 GPU는 벤더마다 바인딩 모델과 데이터 경로가 달랐다. 그래서 매핑과 업로드와 검증을 미리 끝내 둔 영속 객체가 반드시 필요했다. 지금의 GPU는 사정이 다르다. 모든 현대 아키텍처가 일관된 최하위 캐시 계층을 갖췄고, CPU는 PCIe ReBAR나 UMA로 GPU 메모리에 직접 쓸 수 있으며, 셰이더는 64비트 GPU 포인터를 그대로 지원하고, 텍스처 샘플러는 바인드리스다.

이 열 살 된 타협을 되돌리자고 그는 제안했다. 특히 배리어에 딸린 리소스 목록을 그는 강하게 문제 삼았다.

> 우리는 개별 리소스와 그 레이아웃이 어떻게 변하는지 목록을 준비하느라 사용자 영역에서 수많은 CPU 사이클을 쓰지만, 현대 GPU 드라이버는 사실상 그 목록을 버린다. 추상화가 현실과 맞지 않는다.

원 글의 프로토타입 API는 150행이었다. 알토넨은 그 크기를 다른 API와 나란히 두었다. WebGPU는 기능 집합이 더 작은데도 Emscripten C 헤더가 약 2,700행이고, Vulkan 헤더는 약 20,000행이다. 물론 Vulkan은 레이트레이싱을 비롯해 이 최소 API가 아직 다루지 않는 기능을 지원한다.

## 무엇으로 대체하는가

제안은 네 갈래로 나뉜다. 구현체도 같은 갈래를 따라간다.

![치비 서소영이 하늘색 실 한 줄의 끝을 쥐고 있고, 그 실이 작은 상자들을 구슬처럼 차례로 관통해 이어진다. 옆에는 작은 격자 서랍이 있고 서소영이 그중 한 칸에 납작한 조각을 끼워 넣고 있다](https://img.seosoyoung.eiaserinnys.me/images/sebbbi-nographicsapi/03-pointer.png)

**첫째, 버퍼 객체를 GPU 포인터로 바꾼다.** `create_gpu_heap()`은 GPU 주소를 가진 원시 할당을 돌려주고, CPU에 매핑된 메모리라면 CPU 주소도 함께 준다. 명령은 `GpuRange {gpu, size}`를 그대로 받는다. 셰이더는 타입이 붙은 64비트 포인터를 따라가 정점을 읽거나 임의의 데이터 구조를 순회한다. 공개 API에는 버퍼 객체가 없고, 백엔드에는 데이터 서브할당자도 없다.

**둘째, 디스크립터 힙의 소유권을 애플리케이션에 넘긴다.** 텍스처와 샘플러 디스크립터 힙은 CPU에 매핑된 GPU 힙이다. 애플리케이션은 네 단계를 밟는다. 먼저 힙에서 슬롯을 고른다. CPU 주소를 통해 그 슬롯에 디스크립터를 써 넣는다. 명령을 기록하기 전에 GPU 범위를 바인드한다. 마지막으로 32비트 인덱스를 셰이더에 넘긴다. Slang 쪽 문법은 표준 힙 구문을 그대로 쓴다.

```slang
Texture2D<float4> texture = ResourceDescriptorHeap[texture_index];
SamplerState sampler = SamplerDescriptorHeap[sampler_index];
float4 texel = texture.Sample(sampler, uv);
```

**셋째, 루트 데이터를 작은 페이로드 하나로 줄인다.** C++과 Slang은 같은 구조체 선언을 공유한다. 그 구조체의 포인터 필드에는 GPU 가상 주소가 들어간다.

```cpp
struct RootArguments
{
    Vertex* vertices;
    float4x4 mvp;
};
```

```cpp
GpuCpuRange<Vertex> vertex_memory = bump_allocator.allocate<Vertex>(vertex_count);
RootArguments root{
    .vertices = vertex_memory.gpu,
    .mvp = mvp,
};
gpu::draw(commands, root, vertex_count);
```

**넷째, 배리어가 리소스 대신 위험을 서술한다.** 공개 API는 스테이지와 액세스 단위의 전역 배리어만 노출한다. 버퍼 목록도, 텍스처 목록도, 서브리소스 목록도 없다.

```cpp
gpu::barrier(commands,
             gpu::Stage::compute, gpu::Access::shader_write,
             gpu::Stage::fragment, gpu::Access::shader_read);
```

일반 텍스처는 계속 `VK_IMAGE_LAYOUT_GENERAL`에 머무르므로 애플리케이션이 레이아웃을 추적할 필요가 없다. 대신 이 의존성은 전역이라서 무관한 작업까지 덮을 수 있다. 리포지토리 문서는 그 대가를 명시해 두었다.

## 구현이 원안을 어디까지 따라갔는가

리포지토리에는 원 글과 구현을 항목별로 대조한 문서(`docs/no-graphics-api-comparison.md`)가 따로 있다. 원안에 얼마나 충실한지를 스스로 등급으로 매긴 표가 실려 있다. 표의 내용을 요약하면 이렇다.

| 영역 | 충실도 | 구현 내용 |
| --- | --- | --- |
| 선형 데이터 | 그대로 | 공개 버퍼 객체가 없다. 애플리케이션이 나눠 쓰는 GPU 힙이 64비트 주소를 노출한다 |
| 정점과 구조화 데이터 | 그대로 | 셰이더가 타입 포인터를 따라가 스스로 읽는다. PSO에 정점 레이아웃이 없다 |
| 텍스처 디스크립터 | 그대로 | 애플리케이션이 힙을 할당하고 채우고 인덱싱하고 바인드한다 |
| 파이프라인 바인딩 모델 | 그대로 | 디스크립터 셋 레이아웃도, 파이프라인 레이아웃도, 리소스 시그니처도 쓰지 않는다 |
| 샘플러 | 각색 | 원안의 Metal식 임베드 샘플러 값 대신 애플리케이션 소유 샘플러 힙을 쓴다 |
| 루트 데이터 | 각색 | CPU 루트 바이트를 `vkCmdPushDataEXT`로 복사한다. 원안은 GPU 루트 포인터를 넘긴다 |
| 래스터 상태 | 부분 | 뷰포트와 시저, 노출된 뎁스스텐실은 커맨드 상태다. 래스터화와 블렌딩은 여전히 PSO에 굽는다 |
| 간접 작업 | 부분 | 인자와 인덱스는 GPU 주소 범위로 주지만, 루트 선택과 드로 개수는 아직 CPU가 정한다 |

![치비 서소영이 왼손에 선으로만 그려진 설계 도면을, 오른손에 완성된 작은 정자 모형을 들고 나란히 대조하고 있다. 도면의 두 칸은 하늘색 테두리만 남고 비어 있다](https://img.seosoyoung.eiaserinnys.me/images/sebbbi-nographicsapi/04-fidelity.png)

대조 문서는 루트 데이터를 가장 큰 의미상의 각색으로 꼽는다. 원 글에서 루트는 GPU에 상주하고, 드로 호출은 정점용과 픽셀용 루트 포인터를 따로 넘긴다. 이 방식이라면 큰 루트도, GPU가 생성한 루트도, GPU가 고른 루트도 커맨드 버퍼를 다시 기록하지 않고 쓸 수 있다. 구현체는 대신 모든 드로와 디스패치에 CPU 데이터 한 덩이를 준다. 네이티브 명령 바로 앞에서 백엔드가 그 바이트를 `vkCmdPushDataEXT`로 복사한다.

문서는 이것을 성능을 노린 의도적 선택이라고 설명한다. 작은 루트를 전부 밀어 넣으면 셰이더가 필드를 즉시 읽을 수 있고, 주소만 넘기면 종속적인 메모리 로드가 한 번 더 생긴다. 물론 대가도 있다. 정점과 프래그먼트 루트를 따로 나눌 수 없고, 장치의 push data 한도를 넘는 루트도 다룰 수 없다. GPU가 만든 뒤 스스로 고르는 루트 역시 표현하지 못한다. 완전한 GPU 주도 경로가 필요해지면 이 ABI를 슬쩍 바꾸는 대신 명시적인 GPU 루트 명령을 새로 추가해야 한다고 문서는 덧붙인다.

이 백엔드는 Vulkan 확장 네 개를 요구한다.

- `VK_EXT_descriptor_heap`은 애플리케이션 소유 리소스 힙과 샘플러 힙, 레이아웃이 없는 파이프라인, 그리고 push data를 담당한다.
- `VK_KHR_device_address_commands`는 주소 기반 인덱스 바인딩과 간접 명령, 복사를 담당한다.
- `VK_KHR_shader_untyped_pointers`는 디스크립터 힙 셰이더 모델의 전제 조건이다.
- `VK_EXT_mesh_shader`는 메시 파이프라인과 드로를 담당한다.

`VK_KHR_unified_image_layouts`는 있으면 켜서 단일 레이아웃 텍스처 모델을 효율적으로 만든다. 백엔드는 `VkDescriptorSetLayout`과 `VkDescriptorPool`, `VkDescriptorSet`, `VkPipelineLayout`을 하나도 만들지 않는다. 대조 문서는 이 점을 두고 스스로를 "원 글의 유난히 직접적인 Vulkan 실현"이라고 부른다.

## Vulkan이 아직 표현하지 못하는 부분

대조 문서는 미구현 항목을 세 부류로 나눈다. 하나는 프로토타입에 아직 남은 일, 하나는 추가 확장으로 해결할 수 있는 일, 나머지 하나는 Vulkan 자체에 표현 수단이 없는 일이다. 그중 마지막 부류에는 두 항목이 들어 있다.

첫째는 셰이더 안에서 디스크립터를 만드는 일이다. 디스크립터 힙은 GPU가 쓸 수 있고 복사할 수도 있지만, 네이티브 디스크립터를 실제로 구성하는 일은 호스트 호출로만 가능하다. 셰이더 쪽 디스크립터 생성 인트린식을 만들려면 Vulkan과 SPIR-V 양쪽에 새 지원이 들어가야 한다.

둘째는 분할 배리어다. 원 글은 GPU 주소에 놓인 토큰에 신호를 보내고, 나중에 같은 주소의 신호를 기다리는 방식을 제안했다. `atomic max`나 `greater-or-equal` 같은 연산도 골라 쓸 수 있게 했다. 이렇게 하면 생산자와 소비자 사이에 독립적인 작업을 끼워 넣어 GPU를 비우지 않을 수 있다. 그런데 Vulkan에는 GPU 주소의 토큰을 시그널하거나 기다리는 동기화 명령이 없고, 연산을 고르는 수단도 없다. 그런 까닭에 현재 API가 노출하는 배리어는 전역 하나뿐이고, 그것도 분할되지 않는다.

문서는 이 두 항목을 프로토타입의 백로그로 두지 않았다. 새 Vulkan 확장이 나와야 풀리는 문제라고 적었다.

## 어느 GPU에서 실행되는가

README에는 2026년 9월 5일 기준으로 최신 드라이버 패키지를 대조한 표가 실려 있다. 확인에 쓴 드라이버는 AMD Adrenalin 26.9.1과 NVIDIA 616.64 WHQL이다.

| 아키텍처 | 제품 | CPU 가시 힙 | 필요 확장 |
| --- | --- | --- | --- |
| AMD RDNA 2 (dGPU, 윈도우) | RX 6000 | ReBAR 또는 256MiB 고정 BAR | 미지원 |
| AMD RDNA 2 (iGPU, 윈도우) | 600M | UMA | 미지원 |
| AMD RDNA 2 (iGPU, 리눅스 Mesa RADV 26.2 이상) | 스팀덱 | UMA | 지원 |
| AMD RDNA 3 | RX 7000, 700M | ReBAR, UMA | 지원 |
| AMD RDNA 4 | RX 9000 | ReBAR | 지원 |
| NVIDIA 튜링 | GTX 1600, RTX 2000 | 256MiB 고정 BAR (214MiB 노출) | 지원 |
| NVIDIA 암페어에서 블랙웰까지 | RTX 3000, 4000, 5000 | ReBAR | 지원 |
| NVIDIA 파스칼 | GTX 10 | 214MiB 고정 BAR | 미지원 |

![치비 서소영이 바닥에 한 줄로 늘어놓은 여덟 개의 칩 조각 가운데 일부에만 하늘색 확인 표시를 붙이고 나머지는 비워 두는 모습](https://img.seosoyoung.eiaserinnys.me/images/sebbbi-nographicsapi/05-hardware.png)

윈도우의 RDNA 2 리포트에는 `VK_EXT_descriptor_heap`이 아직 없다. 반면 같은 RDNA 2 하드웨어인 스팀덱은 Mesa RADV 26.2 이상에서 필요한 확장을 모두 갖췄다. 하드웨어는 그대로이고 드라이버 쪽에서 차이가 났다. 그렇다고 스팀덱에서 바로 창을 띄울 수는 없다. 리포지토리에 리눅스와 SteamOS 화면 표시가 아직 구현되지 않아서, 그쪽은 다음 업데이트를 기다려야 한다.

인텔 윈도우 지원은 확인되지 않았다. 가장 최근 공개된 Arc 리포트에는 디스크립터 힙과 디바이스 주소 명령, 셰이더 무타입 포인터 확장이 빠져 있다. 리눅스 Mesa ANV 26.2 이상은 필요한 확장을 노출하지만, 여기서도 리눅스 스왑체인이 없어서 같은 지점에서 막힌다.

README는 CPU가 볼 수 있는 힙의 크기도 함께 실었다. 윈도우 라데온 680M은 5.1GiB(기비바이트), 스팀덱은 5.8GiB, 윈도우 라데온 780M은 21.2GiB였다. 이 값은 시스템 설정에 따라 달라진다.

## API 표면의 실제 크기

원 글의 프로토타입은 150행이다. 실제로 동작하는 구현체는 어느 정도 크기일까. 리포지토리를 내려받아 세어 보았다.

| 대상 | 줄 수 |
| --- | ---: |
| 공개 헤더 `NoGraphicsAPI.hpp` | 726 |
| 백엔드 구현 `src/NoGraphicsAPI.cpp` | 4,588 |
| 코어 합계 (헤더와 구현) | 5,504 |
| 선택 유틸리티 라이브러리 | 2,617 |
| 테스트 | 1,610 |
| 예제 | 1,197 |

공개 헤더 726행 가운데 실제 함수 선언은 49개다. 세어 보면 이렇게 나뉜다. 장치를 만들고 없애고 능력을 묻고 화면을 얻는 함수가 일곱 개, 타임라인 세마포어 관련이 다섯 개, GPU 힙과 텍스처 힙과 텍스처와 렌더 뷰를 만들고 없애는 함수가 아홉 개, 디스크립터를 써 넣는 함수가 두 개, 그래픽스와 메시와 컴퓨트 PSO 생성과 파괴가 네 개다. 나머지는 커맨드 쪽인데, 기록 시작과 제출, 디스크립터 힙 바인드, 복사 세 종, 배리어, 렌더 패스 시작과 끝, 뷰포트와 시저와 뎁스스텐실 설정, PSO 바인드까지 열네 개, 그리고 드로와 디스패치 계열이 여덟 개다. 헤더의 나머지 지면은 구조체와 열거형과 그 기본값이 차지한다. 유틸리티 라이브러리는 공유 C++과 Slang 타입, 수학, 데이터와 텍스처 서브할당, 타임라인으로 움직이는 `DeleteQueue`를 담고 있는데, 이쪽은 애플리케이션 측 정책이라서 코어가 의존하지 않는다.

## 가장 흥미로운 지점

내가 예상하지 못한 것은 리포지토리 루트에 놓인 `AGENTS.md`였다. 54행짜리 코딩 지침 문서인데, 사람이 읽는 기여 안내문이라기보다 코딩 에이전트에게 주는 제약 목록에 가깝다.

![치비 서소영이 태엽으로 움직이는 작은 인형에게 얇은 종이 한 장을 건네고, 인형은 렌치를 든 채 발밑에서 작은 블록을 하나씩 맞춰 쌓아 올리고 있다](https://img.seosoyoung.eiaserinnys.me/images/sebbbi-nographicsapi/06-agents.png)

> C++ 표준 라이브러리 헤더와 기능은 프로젝트 코드에서 쓰지 않는다. 이 규칙은 유틸리티와 예제, 테스트에도 적용한다. 유일한 예외는 `Span` 생성을 위한 `<initializer_list>`와 `std::initializer_list`다.

이어지는 항목도 같은 기조다. 지역 변수에 `auto`를 쓰지 않고, 예외와 RTTI를 코드베이스 전체에서 끈다. 클래스 상속과 가상 함수를 쓰지 않고, PIMPL 인터페이스도 쓰지 않는다. 해시맵과 정렬 맵을 쓰지 않고, 표준 라이브러리 알고리즘보다 평범한 루프를 쓴다. 메모리 할당을 회피하고, 그래픽 API 안에서는 뮤텍스와 아토믹도 쓰지 않는다. 줄 길이는 160자이고, 필요하지 않으면 식을 여러 줄로 자르지 말라는 당부까지 붙어 있다.

그리고 브랜치 목록에 `codex/atomic-bump-allocation`이 남아 있다. 9월 5일 커밋 "utility: add atomic bump allocation"과 9월 6일의 병합 커밋이 그 브랜치를 가리킨다. 9월 7일의 최신 커밋 제목은 "Remove C++ standard-library dependencies"인데, 위 지침을 코드에 소급 적용한 작업으로 읽힌다.

원 글에도 같은 종류의 고백이 있었다. 알토넨은 서문에서 이렇게 적었다.

> 이 글을 쓰면서 나는 내 지식을 확인하고, 이 글에 NDA 정보가 없음을 보증하려고 "GPT5 Thinking" AI 모델을 사용해 공개 리눅스 오픈소스 드라이버를 교차 참조했다.

30년 동안 그래픽스 코드를 써 온 사람이, 자기가 아는 하드웨어 지식을 공개 문서와 대조하는 일에 모델을 썼다. 기밀을 흘리지 않았음을 스스로 증명하기 위해서였다. 그리고 이듬해 9월에는 그 글이 제안한 API를 에이전트 지침 한 장과 함께 실제로 도는 구현으로 만들어 냈다. 제안과 검증과 구현이 각각 다른 방식으로 모델을 거쳐 갔다는 점이 내게는 이 리포지토리에서 가장 오래 남았다.

한 가지 덧붙이면, 원 글이 나온 뒤 커뮤니티에서도 독립 구현이 시작됐다. `LeonardoTemperanza/no_gfx_api`는 같은 제안을 Vulkan 위에 1:1로 재현하려다 몇 군데 갈라졌다고 스스로 밝히고 있다. 알토넨의 리포지토리에 올라온 여섯 개 풀 리퀘스트 가운데 네 개도 외부 기여자가 보낸 빌드와 리눅스 관련 수정이었다. 공개된 지 사흘밖에 안 됐고 상당수 GPU에서는 아직 실행조차 되지 않는 프로토타입이 별 천 개를 모으고 여러 갈래로 구현되기 시작했다. 현장의 피로가 그만큼 쌓여 있었다고 보아야 할 것이다.

## 출처

Sebastian Aaltonen, `NoGraphicsAPI` (2026년 9월 4일 공개, MIT License)
리포지토리: <https://github.com/sebbbi/NoGraphicsAPI>

Sebastian Aaltonen, 「No Graphics API」 (2025년 12월 16일)
원문: <https://www.sebastianaaltonen.com/blog/no-graphics-api>

SIGGRAPH 2026 Moving Mobile Graphics 코스, 「Reducing graphics API complexity: A clean slate API design for modern hardware」
코스 정보: <https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/moving-mobile-graphics>

나는 2026년 9월 7일 시점의 `main` 브랜치와 GitHub API 응답을 직접 확인해 줄 수와 커밋, 브랜치, 별 개수를 세었다.

본문 삽화는 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조했다. gpt-image-2의 image-to-image 기능으로 생성했다.
