---
title: "How We Draw a 3D Sprite World: The Stylized Art of Never’s End"
date: 2026-10-08T11:00:00+09:00
tags: ["렌더링", "픽셀 아트", "캐릭터 애니메이션", "Never’s End"]
categories: ["게임"]
summary: "GDC 2026에서 라이언 주켓이 공개한 Never’s End의 렌더링 기법. 선과 음영, 카메라와 관절의 픽셀 정렬, 겹침 순서 알고리즘, 구름과 애니메이션까지 3D 장면을 손으로 그린 스프라이트처럼 표현하는 과정을 정리했다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/cover-world.jpg"
  alt: "Never’s End 발표 PDF 19쪽. 건물과 절벽, 캐릭터, 물을 픽셀 아트로 표현한 3D 장면"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/cover-world.jpg"
---

## 3줄 요약

1. GDC 2026에서 Hypersect의 라이언 주켓이 공개한 기법은 「Never’s End」의 3D 장면을 2D 스프라이트처럼 렌더링한다. 손으로 그린 느낌을 유지하며 턴제 전술 RPG의 조명과 애니메이션을 처리한다.[^source]
2. 한 픽셀 두께의 선과 툰 음영을 만들고, 카메라와 모델, 관절과 파티클을 화면 픽셀에 정렬한다. 오브젝트가 서로 관통해 보이는 문제는 별도의 겹침 순서 알고리즘으로 처리한다.
3. 머리카락 반사광과 하늘, 구름까지 같은 표현 방식에 맞추되, 물과 안개에는 원래 3D 깊이를 사용한다. 각 처리에는 미술가가 결과를 조절할 입력을 제공하고, 기술적 제약도 설명한다.

## 어떤 게임인가

Never’s End의 캐릭터와 환경은 3D 모델이다. Hypersect는 이 모델들을 손으로 그린 2D 스프라이트처럼 표현하면서, 장비를 바꾸고 다양한 애니메이션을 재생하며 조명과 그림자를 온전히 지원하고자 했다. 경쟁작과 구별되는 미술을 만들려는 목적도 있었다. 발표의 기술 설명은 이 요구에서 시작한다.[^pdf-6-7]

![이동 가능한 타일과 선택한 캐릭터, 행동 메뉴가 표시된 Never’s End의 전투 화면](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-06.jpg)

*Never’s End의 전투 화면. [^pdf-6]*

발표 당시 개발 기간은 7년 반이었다. 처음 5년은 주켓이 혼자 개발하면서 시간제 외주 인력과 협업했고, 발표 시점에는 전일제 인력 4명과 시간제 인력 4명이 참여했다. 엔진과 편집기는 자체 제작했으며, 미술 도구로 Maya와 Blender, Photoshop을 사용했다.[^pdf-8]

기술적 참고 사례는 Arc System Works의 「Guilty Gear Xrd」다. 주켓은 2015년 GDC 발표 「GuiltyGearXrd’s Art Style: The X Factor Between 2D and 3D」를 소개하고, 그 작업을 토대로 Never’s End의 기법을 개발했다고 설명했다.[^pdf-9]

발표는 선 처리, 음영, 픽셀 정렬, 스프라이트 겹침 순서, 애니메이션의 순서로 진행된다. 비교 기준으로 고해상도와 부드러운 음영, 원근 투영을 적용한 장면을 제시한다. 그다음부터 같은 세계를 스프라이트처럼 표현하기 위해 각각의 처리를 설명한다.[^still][^pdf-11]

## 선을 어떻게 만드는가

### 세 종류의 외곽선

기본 선은 후처리로 만든다. 후처리에서는 선이 한 픽셀 두께로 깔끔하게 표현되도록 한다. 손으로 그린 선과 같은 인상을 목표로 한다. 아래 비교에서 선을 켜면 캐릭터의 머리와 무기, 바위와 지형의 형태가 더 또렷해진다.

![같은 장면에 선 후처리를 끈 결과와 켠 결과를 비교한 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-13.jpg)

*선 처리 전후. [^pdf-13]*

외곽선 판정에는 세 종류의 정보를 사용한다.[^pdf-20-23]

![오브젝트, 깊이, 재질 외곽선 판정에 사용하는 세 종류의 맵](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-20.jpg)

*왼쪽부터 오브젝트, 깊이, 재질 외곽선에 사용하는 정보. [^pdf-20]*

| 외곽선 종류 | 판정에 쓰는 정보 | 미술가가 지정하는 것 |
|---|---|---|
| 오브젝트 외곽선 | 16비트 Object ID | 부모의 ID를 공유할지, 자기 ID 주위에 선을 만들지 |
| 깊이 외곽선 | 깊이와 법선 | 재질별 생성 여부와 기본 깊이 임계값 |
| 재질 외곽선 | Material ID | 선을 만들 재질 구역과 생성 제외 마스크 |

오브젝트 ID를 공유하면 부모와 부착물을 같은 오브젝트로 취급할 수 있다. 깊이 외곽선은 재질마다 기준값을 지정하고, 표면이 가파른 각도일 때 법선에 따라 임계값을 보정한다. 재질 외곽선의 설정은 재질 속성이나 텍스처 데이터로 전달한다.

### 선이 어느 쪽에 속하는가

두 색이 만나는 지점에 선을 그리면, 선이 그려진 쪽이 더 커 보이고 다른 쪽보다 앞에 있는 것처럼 보일 수 있다. 아래 원과 사각형 비교는 같은 도형이라도 선의 소속에 따라 인상이 달라지는 모습을 보여 준다.

![원과 사각형의 경계에서 어느 쪽에 외곽선을 그리는지에 따른 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-24.jpg)

*선이 차지하는 한 픽셀도 도형의 크기와 겹침에 영향을 준다. [^pdf-24]*

엔진은 다음 우선순위로 선의 소속을 결정한다.[^pdf-25]

1. 오브젝트 외곽선: 깊이순으로 정렬한 Object ID를 사용해 가까운 오브젝트에 선을 준다.
2. 깊이 외곽선: 더 가까운 픽셀에 선을 준다.
3. 재질 외곽선: 깊이 차이가 임계값보다 크면 더 가까운 픽셀을 선택한다. 이 검사는 깊이 외곽선을 껐을 때 필요하다. 그 밖에는 더 작은 Material ID를 선택한다.

선 색도 검은색 하나로 고정하지 않는다. 별도의 색 버퍼에 선 후보 색을 렌더링하며, 기본값은 확산광 결과에 재질별 색조를 적용한 색이다. 선 색 계산 전용 텍스처를 사용하거나, 일정한 단색과 혼합하는 설정도 제공한다.[^pdf-26]

### 선을 그린 뒤의 깊이

외곽선을 추가한 픽셀은 이후 렌더링에서도 오브젝트의 일부로 취급해야 한다. 그래서 깊이 버퍼와 모든 G-buffer를 선 영역까지 확장한다. 후속 계산은 G-buffer에 저장한 표면 정보를 사용한다.

주변 픽셀의 깊이를 그대로 복사하면 원래 표면과 다른 깊이가 된다. 아래 도식에서는 기울어진 평면의 끝에 선을 추가할 때, 그 평면의 기울기를 따라 깊이도 연장한다. 선을 그릴 색뿐 아니라 선이 차지한 픽셀의 3D 표면 정보까지 처리하는 셈이다.

![외곽선의 깊이를 단순 복사한 경우와 원래 평면을 따라 연장한 경우를 비교한 도식](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-27.jpg)

*가운데는 깊이를 복사하고, 오른쪽은 원래 표면의 기울기를 따라 깊이를 연장한다. [^pdf-27]*

### 내부 선과 선택 표시

한 오브젝트 내부의 선은 별도로 조절한다. Object ID가 같고 Material ID가 다른 구역 사이에는 부분적으로 투명한 선을 사용할 수 있다. Object Section ID를 지정하면 같은 오브젝트에도 불투명한 구획선을 만들 수 있다. 아래 캐릭터 예시는 머리카락과 장비의 구역을 여러 버퍼로 구분한다.

![캐릭터의 내부 선. Object ID, Material ID, Object Section ID와 혼합 가중치 맵.](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-28.jpg)

*캐릭터 내부의 구역과 선의 불투명도를 지정하는 버퍼. [^pdf-28]*

표면의 능선에 그리는 내부 선은 조명용 법선과 깊이로 감지한다. 재질은 각도 임계값과 밝기 계수를 출력하고, 선을 그릴 때는 주 광원 방향에 더 가까운 밝은 쪽을 선택한다.[^pdf-29]

![기둥 표면의 내부 선과 깊이, 법선, 각도 임계값, 밝기 버퍼](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-29.jpg)

*표면의 능선에 내부 선을 그리기 위한 입력. [^pdf-29]*

캐릭터 선택이나 범위 피해 표시는 기본 외곽선 처리 뒤에 추가한다. 첫 번째 선 처리에서 확장한 데이터를 입력으로 받고, Selection Category 버퍼의 값으로 색상표를 조회한다. 같은 선택 범주에 여러 오브젝트가 있으면 Object ID로 구별한다.[^pdf-30]

![녹색 선택 외곽선이 표시된 캐릭터와 Object ID 및 Selection Category 버퍼](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-30.jpg)

*기본 외곽선 뒤에 추가하는 선택 표시. [^pdf-30]*

기본 색부터 최종 화면까지의 연속 장면은 실제 합성 순서를 보여 준다. 기본 색에 기본 선을 추가하고, 반투명 요소와 선택 표시를 적용한 뒤, 지형의 물과 물의 선을 그린다.[^pdf-14-19]

### 한 픽셀보다 두꺼운 선

한 픽셀을 초과하는 선은 후처리 대신 장면의 기하와 텍스처로 그린다. 별도 색을 가진 홈 모양의 기하와 최근접 샘플링 텍스처를 사용한다.[^pdf-31]

![실내 장면과 목재 표면의 굵은 선, 최근접 샘플링 텍스처](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-31.jpg)

*기하와 텍스처로 표현한 실내의 굵은 선. [^pdf-31]*

세밀하거나 움직이는 선에는 손으로 안티앨리어싱한 듯한 부드러움이 필요할 수도 있다. 이때는 선명함을 유지하면서 UV상의 선 주변에 기하를 만들고, 텍스처를 쌍선형으로 샘플링한다. UV를 좌표축에 맞춰 배치하는 기법은 Guilty Gear Xrd를 참고했다.[^pdf-32-33]

![몬스터 모델의 선을 따라 만든 기하. 좌표축에 정렬한 UV와 쌍선형 샘플링 도식.](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-33.jpg)

*세밀한 선의 기하와 UV 배치. [^pdf-33]*

## 빛과 재질을 어떻게 표현하는가

### 툰 램프와 여러 광원

툰 램프는 조명 계산 결과를 어떤 색으로 표현할지 지정하는 띠 모양의 데이터다. Never’s End의 램프에는 확산광, 정반사광, 주변광 차폐 정보를 저장하는 세 개의 띠가 있다. 확산광 띠는 RGBA이며, 알파 채널은 그늘 조명을 얼마나 혼합할지 조절한다. 나머지 두 띠는 RGB다.[^pdf-35]

아래 비교는 램프 A부터 E까지의 변화와 구, 상자에 적용한 결과를 함께 제시한다. 램프의 색을 몇 단계로 구성하고 밝은 구역을 얼마나 넓게 지정하는지에 따라, 같은 모델의 음영도 달라진다.

![다섯 가지 툰 램프를 구와 보물 상자에 적용한 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-36.jpg)

*램프 데이터와 렌더링 결과를 대응시킨 비교. [^pdf-36]*

광원이 여러 개일 때는 각각에 대해 툰 램프를 평가한 뒤 결과를 더한다. 거리에 따른 감쇠는 램프를 조회하는 UV를 어두운 구역 방향으로 조정해 적용한다. 점광원에는 노이즈로 감쇠에 변화를 주거나, 방향마다 크기를 다르게 지정하는 설정도 있다.[^pdf-37]

그늘은 시간대별로 별도의 주변광 색을 가진다. 확산광 램프의 알파 채널로 그늘 조명을 혼합하며, 다른 물체가 드리운 그림자는 완전한 그늘로 취급한다.[^pdf-38]

그늘에서는 재질 설정까지 바꿀 수 있다. 직접 조명을 받는 상태와 별개로 알베도 텍스처와 주변광 색조, 선 색을 지정한다. 선인장 비교에서는 밝은 구역과 그늘 구역에 쓰는 텍스처를 따로 보여 준다.[^pdf-39]

### 미술가가 수정하는 음영

빛 계산의 입력도 미술가가 조절한다. 발표에는 서로 다른 네 가지 조작이 나온다.[^pdf-40-43]

| 조작 | 바꾸는 대상 | 발표에서 설명한 목적 |
|---|---|---|
| 툰 램프 편향 | 정점 색으로 램프 조회 전 조명값을 보정 | 특정 부분을 항상 그늘로 표현 |
| 법선 편집 | 표면의 조명용 법선 | 명암선과 균일한 조명을 조절 |
| 그림자 생성용 기하 | 다른 곳에 그림자를 드리우는 형상 | 원치 않는 자기 그림자를 방지 |
| 그림자 수신용 형상 | 그림자 맵을 샘플링할 형상 | 틈에 생기는 그림자를 방지 |

선인장 모델은 이 조작들을 비교하기 좋은 예다. 가시와 굴곡의 기본 법선을 그대로 사용한 결과와, 편집한 법선을 사용한 결과의 명암선이 다르다. 그림자를 만드는 기하를 따로 지정하면 가시 때문에 몸통에 생기는 자기 그림자도 조절할 수 있다.

![선인장의 기본 법선과 편집 법선, 렌더링 결과의 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-41.jpg)

*법선 편집으로 바뀌는 조명. [^pdf-41]*

지형의 그림자 수신에도 예외 처리가 있다. 벽의 표면을 평평한 면에 투영한 좌표로 그림자 맵을 샘플링한다.[^pdf-43]

주변광 차폐에도 툰 표현을 적용한다. 화면 공간 주변광 차폐, 즉 SSAO 버퍼의 입력값을 툰 램프의 임계값으로 처리한다. 일부 재질에서는 확산광을 줄이고 주변광을 늘려 그림자의 대비를 낮춘다. 확산광 차폐 맵을 사용하면 모델의 특정 부분을 그늘 조명으로 지정할 수도 있다.[^pdf-44-54]

### 정반사와 MatCap

정반사에는 등방성 툰 반사, 이방성 툰 반사, 머리카락 전용 툰 반사의 세 가지 모드가 있다. 계산 결과에 광택 맵의 값을 곱한 뒤 툰 램프로 전달한다.[^ramp-row][^pdf-45]

금속과 유리, 몬스터 눈처럼 반사성 재질에는 MatCap도 사용한다. MatCap의 RGB로 정반사광을 추가한다. 이 정반사광은 확산광과 함께 약해지도록 처리한다. 알파 채널은 주변광 차폐의 강도를 조절한다. 이 두 채널을 함께 사용하면 그늘에서도 반사가 있는 것처럼 표현할 수 있다. 아래 그림은 RGB와 알파를 각각 바꾸었을 때의 결과를 구로 비교한다.

![MatCap의 RGB와 알파 채널을 조합한 구의 반사 표현](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-47.jpg)

*RGB는 정반사광, 알파는 주변광 차폐를 조절한다. [^pdf-47]*

## 머리카락의 반사광

머리카락의 반사광은 모델에 고정된 띠 대신 애니메이션과 카메라 변화에 맞춰 계산한다. 이 계산에서는 물리적 정확성보다 미술가가 결과를 조절할 수 있는지가 우선이다. 주켓은 설정이 복잡하지만 최종 인상에 중요하다고 설명했다.[^pdf-48]

### UV와 띠의 위치

먼저 머리카락의 방향을 텍스처의 세로축에 맞춘다. 뿌리는 위, 끝은 아래다. 그러면 UV 좌표로 머리카락의 뿌리에서 얼마나 떨어진 지점인지 알 수 있다. 아래 그림에는 머리 모델의 색과 펼친 UV가 대응되어 있다.

![머리카락 뿌리부터 끝까지의 방향을 세로축에 맞춘 모델과 UV](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-49.jpg)

*머리카락을 따라 잰 위치를 UV로 표현한다. [^pdf-49]*

반사광 띠의 기준 위치는 이 UV상의 거리로 조절한다. 카메라의 위아래 기울기, 즉 피치에 따라 위치를 추가 보정한다. 표면 법선이 시선과 수직에 가까워질 때는 곡률 보정으로 띠를 이동시킨다.[^pdf-50-51]

### 폭과 강도를 조절하는 곡선

반사광 계산에는 중심선으로부터의 거리, 거리에 적용할 지수, 광택 배율의 세 매개변수를 사용한다. 발표의 식은 다음과 같다.[^pdf-52]

```text
specular = (distance ^ exponent) * gloss
```

세 매개변수는 머리카락 가장자리에서 중심까지의 곡선으로 지정한다. 각 매개변수에는 측면 시점용 곡선과 위쪽 시점용 곡선을 하나씩 지정한다. 따라서 그림에는 곡선이 총 여섯 개 나온다. 식은 간단해도 띠의 형태를 정하는 입력은 세밀하게 조절한다.[^hair-formula]

![머리카락 반사광 식과 세 매개변수의 측면 및 위쪽 시점 곡선](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-52.jpg)

*세 매개변수에 두 곡선씩 지정한다. [^pdf-52]*

마지막으로 광택 맵으로 머리카락 덩어리를 구분한다. 세로 방향 마스크는 머리카락 방향과 카메라의 위쪽 축이 얼마나 정렬되는지에 따라 반사광을 줄인다. 아래로 흐르는 머리카락에 반사광이 집중되도록 하는 설정이다.[^pdf-53]

## 하늘과 구름

### 하늘색과 디더링

하늘색은 세로 방향 그라데이션으로 그린다. 시간대와 세계 상태, 날씨의 양극단에 맞춰 색을 준비한다. 발표 자료는 맑은 날과 흐린 날 각각에 네 가지 세계 상태의 색을 제시한다. 카메라 줌과 피치에 맞춰 화면에 표시할 그라데이션 범위를 조절한다.[^pdf-55-56]

수평으로 균일한 색 띠를 그대로 두는 대신, 노이즈 맵으로 세로 UV를 변위시켜 손으로 그린 듯한 형태를 만든다. 카메라가 수평으로 360도 회전하면 노이즈도 이음새 없이 반복된다.

디더링은 한 픽셀 걸러 세로 UV에 작은 오프셋을 주는 방식이다. 노이즈로 색 띠를 변형하면 디더링 구역도 함께 변형된다. 아래 비교는 그라데이션, 노이즈 변위, 디더링을 차례로 적용한 결과를 보여 준다.

![하늘 그라데이션에 노이즈 변위와 디더링을 차례로 적용한 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-57.jpg)

*하늘색 띠의 형태와 색 전환을 조절하는 과정. [^pdf-57]*

### 구름의 형태와 조명

구름은 날씨와 시간대 변화에 대응하는 동적 시스템이 필요했다. 주켓은 SIGGRAPH 2015의 「The Real-time Volumetric Cloudscapes of Horizon Zero Dawn」을 참고하되, 2D 평면에서 작동하도록 조정하고 결과에 툰 음영을 적용했다고 설명했다.[^pdf-58]

구름의 좌표는 카메라의 수평 회전과 피치 변화에 반대 방향으로 스크롤한다. 노이즈 조회는 수평 방향으로 이음새 없이 반복되며, 360도 회전할 때 한 주기를 이룬다. 깊이에 따라 UV 크기를 조절해 시차 효과도 만든다.[^pdf-59]

구름 조명에 사용하는 색은 직접광, 주변광, 대기의 세 종류다. 각각 시간대별 그라데이션이며, 세계 상태와 날씨의 양극단에 맞춘 그라데이션 세트를 준비한다.[^pdf-60]

구름 모델의 계산 결과로 Extinction, 주변광 에너지, 직접광 에너지가 출력된다. 불투명도에는 `Extinction < 75%`라는 임계 조건을 사용하고, 주변광 색과 직접광 색은 sRGB에서 혼합한다. 혼합 비율은 연속값을 그대로 사용하지 않고 다음 세 단계로 결정한다.[^pdf-61]

| 조건 | 직접광 색을 혼합하는 비율 |
|---|---:|
| 직접광 에너지가 0.485보다 큼 | 100% |
| 위 조건에 해당하지 않고, 직접광과 주변광 에너지의 합이 0.891보다 큼 | 40% |
| 나머지 | 0% |

![구름 모델의 출력과 불투명도 조건, 세 단계 조명 혼합 비율을 적은 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-61.jpg)

*구름의 조명값을 세 가지 혼합 비율로 표현한다. [^pdf-61]*

구름의 디더링도 조명 계산에 직접 적용한다. 한 픽셀 걸러 직접광 에너지와 주변광 에너지에서 각각 0.087을 빼고 계산한다. 이 차이로 명암 단계가 바뀌는 구역에 디더링이 생긴다.[^pdf-62]

멀리 있는 구름은 깊이의 제곱을 사용해 대기색에 가까워지도록 혼합한다. 이 혼합에도 툰 표현을 적용하며, 비율은 0%, 25%, 50%, 75%의 네 단계로 제한한다.[^pdf-63]

## 픽셀 격자에 맞추기

선과 색이 적절해도 카메라나 모델이 움직일 때 픽셀 형태가 달라질 수 있다. 발표의 다음 부분은 각 대상의 위치와 크기를 화면 픽셀에 정렬하는 방법을 설명한다.[^pdf-65-72]

### 카메라의 위치와 줌, 피치

카메라 위치는 화면 방향을 기준으로 한 좌표로 변환한 뒤 화면 픽셀에 맞춘다. 뷰포트 크기가 홀수일 때는 반 픽셀 오프셋을 추가한다. 마지막에 월드 좌표를 다시 계산한다. 화면 크기가 달라도 같은 이미지를 렌더링하려는 처리다.[^pdf-65]

줌은 1×1 지형 블록이 화면에서 정확히 몇 픽셀 너비를 차지해야 하는지로 정의한다. 블록을 빈틈없이 반복 배치하기 위한 기준이다.[^pdf-66]

피치는 블록 사이의 세로 간격을 결정한다. 원하는 피치에서 블록의 픽셀 높이를 계산하고, 그 높이를 픽셀에 맞춘 다음 피치를 다시 구한다. 아래 상자 비교에서는 정렬하지 않은 경우 중간 틈에 한 픽셀이 더 생기지만, 정렬한 결과는 간격이 일정하다.

![카메라 피치 정렬 전후에 상자 사이의 틈이 한 픽셀 달라지는 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-67.jpg)

*상자의 세로 간격에 생기는 한 픽셀 차이를 피치 보정으로 처리한다. [^pdf-67]*

### 모델과 관절

모델은 루트 위치를 화면 픽셀에 맞춘다. 같은 모델의 여러 인스턴스가 정확히 같은 실루엣으로 렌더링되도록 하는 처리다. 부모에 부착된 모델은 대부분 개별 정렬을 끄고 부모 스프라이트와 함께 정렬한다. 벽처럼 다른 모델과 이음새 없이 연결되는 것이 우선인 경우에도 정렬을 끌 수 있다.[^pdf-68]

관절의 이동은 모델 공간에서 화면 픽셀에 맞춘다. 부모 관절의 정렬 오프셋을 상속할지는 선택할 수 있다. 발을 바닥에 유지해야 할 때는 부모의 정렬 오프셋 상속을 끈다.[^pdf-69]

![관절 이동의 픽셀 정렬을 끈 캐릭터와 켠 캐릭터의 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-69.jpg)

*관절별 정렬과 부모 오프셋 상속을 조절한다. [^pdf-69]*

### 파티클과 구름, 별

파티클은 위치와 크기를 모두 정렬하고, 최소 픽셀 너비를 지정한다. 픽셀 크기가 홀수일 때는 위치를 반 픽셀 이동한다.[^pdf-70]

![파티클의 위치와 크기를 픽셀에 정렬하기 전과 정렬한 후의 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-70.jpg)

*파티클의 위치와 크기를 함께 정렬한다. [^pdf-70]*

구름은 노이즈와 디더링의 스크롤을 화면 픽셀에 맞춘다. 깊이에 따른 처리 때문에 계산이 복잡해진다는 설명도 있다. 형태 애니메이션은 수평 스크롤이 실제로 한 픽셀 이동하는 프레임에 맞춰 갱신한다.[^pdf-71]

![구름의 노이즈와 디더링 스크롤을 픽셀에 정렬하기 전과 정렬한 후의 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-71.jpg)

*구름의 스크롤과 형태 갱신 시점을 조절한다. [^pdf-71]*

별에는 전용 텍스처 샘플링을 사용한다. 줌을 어떻게 바꾸더라도 별 하나가 한 픽셀로 표현되도록 한다.[^pdf-72]

![별 텍스처의 샘플링 격자와 한 픽셀로 표현된 별이 있는 밤하늘](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-72.jpg)

*줌에 관계없이 한 픽셀로 유지한 별. [^pdf-72]*

| 대상 | 픽셀에 정렬하는 것 | 예외와 추가 처리 |
|---|---|---|
| 카메라 | 화면 방향으로 변환한 위치 | 홀수 뷰포트의 반 픽셀 보정 |
| 줌과 피치 | 블록의 너비와 높이 | 정렬한 높이로 피치를 다시 계산 |
| 모델 | 루트 위치 | 부착물과 벽은 개별 정렬을 끌 수 있음 |
| 관절 | 모델 공간의 이동 | 발은 부모 오프셋을 상속하지 않을 수 있음 |
| 파티클 | 위치와 크기 | 최소 너비와 홀수 크기 보정 |
| 구름 | 노이즈와 디더링 스크롤 | 형태 갱신 시점을 수평 이동과 동기화 |
| 별 | 텍스처 샘플링 결과 | 줌에 관계없이 한 픽셀 유지 |

## 무엇이 무엇을 가리는가

### 3D의 교차와 스프라이트의 겹침

발표에서 가장 긴 알고리즘 설명은 스프라이트 정렬이다. 스프라이트처럼 표현하려면 오브젝트들이 2D 평면처럼 서로를 가려야 한다. 일반적인 3D 깊이 판정에서는 오브젝트 일부가 환경과 교차해 잘릴 수 있다. 발표는 지면에 걸친 늑대와 벽 앞 캐릭터, 서로 겹친 몬스터와 지형을 비교한다.[^pdf-74-75]

![일반 깊이 처리와 스프라이트 정렬을 적용한 늑대 및 벽 앞 캐릭터의 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-74.jpg)

*3D 교차 때문에 가려진 부분을 스프라이트 겹침 순서로 표현한다. [^pdf-74]*

각 오브젝트에는 월드 좌표축에 평행한 상자, 즉 AABB 형태의 정렬용 볼륨을 지정한다. 보통 오브젝트 전체를 포함하지만, 가장 적절한 크기는 사례별로 정한다. 볼륨들이 서로 겹치지 않으면 좋겠지만, 동적 오브젝트와 다양한 형태 때문에 항상 그렇게 만들 수는 없다.[^pdf-76-77]

### 겹침 판정과 순서 결정

엔진은 AABB를 화면에 투영하고, 화면에 투영한 월드 좌표축마다 최소값과 최대값을 기록한다. 이 정보로 분리축 검사를 수행해 겹치는 쌍을 찾는다.[^pdf-80]

![화면에 투영한 여러 AABB와 분리축 검사에 사용하는 월드 좌표축](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-80.jpg)

*정렬용 상자를 화면에 투영해 겹침을 검사한다. [^pdf-80]*

겹치는 쌍마다 어느 상자가 앞에 있는지도 정해야 한다. 가장 가까운 점의 깊이만 비교하는 방식은 적합하지 않다고 설명한다. 대신 최소 분리축을 구하고, 분리 방향과 시선 방향을 비교해 앞에 있는 상자를 결정한다. 아래 도식은 바닥에 가까운 얇은 상자와 기울어진 큰 상자를 이 기준으로 비교한다.

![얇은 상자와 큰 상자의 최소 분리축 및 시선 방향을 비교한 도식](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-81.jpg)

*분리 방향과 시선 방향으로 상자의 앞뒤를 결정한다. [^pdf-81]*

### 순환 관계가 생기면

쌍별로 구한 앞뒤 관계는 전체 순서로 정렬할 수 없는 경우가 있다. A가 B 앞에 있고, B가 C 앞에 있으며, C가 다시 A 앞에 있는 순환 관계다. 세 관계를 모두 만족하는 스프라이트 순서는 존재하지 않는다.[^pdf-78]

발표는 이 경우 잘못 정렬되는 화면 면적을 최소화하는 순서를 선택한다고 설명한다. 아래 세 막대 예시는 순환을 없애는 선택에 따라 잘못 가려지는 부분의 크기가 달라지는 모습을 보여 준다.

![세 막대가 순환하는 겹침 관계를 이루며 정렬 선택에 따라 오류 면적이 달라지는 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-79.jpg)

*세 관계를 모두 만족할 수 없어, 잘못 보이는 구역이 작은 순서를 선택한다. [^pdf-79]*

처리 절차는 다음과 같다.[^pdf-82-83]

1. 겹침 순서를 그래프로 표현하고 Tarjan의 강연결요소 알고리즘으로 순환하는 그룹을 찾는다. 강연결요소는 어느 노드에서든 다른 모든 노드로 가는 경로가 있는 그룹이다.
2. 그 그룹에서 화면상 겹침 면적이 가장 작은 간선을 찾는다.
3. 해당 순서 관계를 제거하고 그룹을 다시 정렬한다.
4. 그래프에 순환이 없어질 때까지 반복한다.

![강연결요소 C D E의 간선별 겹침 면적과 제거할 관계를 표시한 도식](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-83.jpg)

*순환 그룹 내에서 화면상 겹침이 가장 작은 관계를 제거한다. [^pdf-83]*

### 배경의 순서를 안정적으로 유지하기

동적 오브젝트를 처음부터 배경과 함께 계산하면, 오브젝트가 이동할 때 제거할 간선도 달라질 수 있다. 그러면 가만히 있는 배경끼리도 겹침 순서가 바뀐다.

아래 도식은 정적인 A, B, C의 순서가 `A B C`였는데, 동적 D를 포함하자 `B C D A`가 되는 예를 보여 준다. 해결책은 여러 단계로 계산하는 것이다. 정적 환경의 순서를 먼저 결정해 유지한 뒤 동적 오브젝트를 처리한다. 그러면 순서는 `D A B C`가 되고, 정적 오브젝트끼리의 기존 순서도 보존된다.

![정적 오브젝트만 계산한 순서와 동적 오브젝트를 함께 계산한 순서 및 정적 순서를 고정한 결과](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-84.jpg)

*동적 오브젝트가 이동해도 배경끼리의 순서를 유지한다. [^pdf-84]*

별도로 정렬한 그룹 사이에는 논리적인 겹침이 없어도 화면상 겹침이 있을 수 있다. 이런 그룹들은 휴리스틱으로 서로의 순서를 정한다. 먼저 3D 볼륨의 윗면 높이가 더 낮은 것을 앞에 배치한다. 다음 기준은 더 가까운 것, 그다음은 화면에서 더 왼쪽에 있는 것이다.[^pdf-85]

### 실제 렌더링에 적용하기

정해진 스프라이트 순서는 모델의 깊이 오프셋으로 적용한다. 직교 투영에서는 시선 방향의 깊이 이동이 화면 위치 변화로 보이지 않는다. 아래 그림은 플레이 화면과 깊이 오프셋을 위에서 본 화면을 비교한다. 플레이 화면의 바닥 블록들이, 위에서 본 화면에서는 서로 다른 깊이로 이동해 있다.[^pdf-86-87]

![플레이 화면의 지형 블록과 스프라이트 정렬용 깊이 오프셋을 위에서 본 비교](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-87.jpg)

*직교 투영 화면에서는 드러나지 않는 깊이 오프셋. [^pdf-87]*

이 처리에도 절충점이 있다. 그림자 샘플링은 여전히 교차한 기하 내부에서 이루어질 수 있어, 어색한 그림자가 생길 수 있다. 주켓은 이런 결과가 흔히 드롭 섀도처럼 받아들여진다고 설명한다.[^pdf-88]

또한 모든 효과가 스프라이트용 깊이를 사용할 수는 없다. 셰이더는 스프라이트 깊이와 일반 깊이를 모두 출력한다. 물과 안개는 일반 깊이를 샘플링하므로, 불투명 모델은 스프라이트 순서로 겹치면서도 물과 안개에는 3D 교차가 적용된다.[^pdf-89-90]

![스프라이트용 깊이 버퍼와 일반 깊이 버퍼를 비교한 슬라이드](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-89.jpg)

*같은 장면에 두 깊이 버퍼를 사용한다. [^pdf-89][^dual-depth]*

## 움직임을 어떻게 표현하는가

모델의 회전은 정해진 각도로 양자화해 스프라이트 시트의 방향별 그림처럼 표현한다. 중요한 각도가 포함되도록 지정한다. 오브젝트 종류에 따라 오일러 각의 축마다 사용할 값의 개수를 정한다. 이 양자화는 월드 공간에만 적용하며, 카메라 회전은 부드럽게 유지한다.[^pdf-92]

![모델 회전을 연속적으로 적용한 결과와 정해진 각도로 양자화한 결과](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-92.jpg)

*모델 방향은 양자화하고 카메라 회전은 부드럽게 유지한다. [^pdf-92]*

관절 애니메이션에는 미술가가 직접 배치한 계단형 키를 사용하고, 키 사이를 혼합하지 않는다. 관절 회전은 모델 공간에서 양자화해 부동소수점 오차가 누적되는 문제도 처리한다.[^pdf-93]

파티클 시스템은 시뮬레이션과 렌더링의 프레임 속도를 별도로 지정할 수 있다. 입자를 계산하는 프레임 속도와 화면에 표시하는 프레임 속도를 각각 조절하는 기능이다.[^pdf-94]

## 제작에서 요구한 것

발표를 마무리하며 주켓은 기술적 제약에 따라 미술 스타일을 정하라고 권했다. 엔지니어링과 미술의 긴밀한 협업, 미술가와 애니메이터의 세부적인 작업, 2D 픽셀 아트를 좋아하는 3D 미술가가 필요하다고 정리했다.[^pdf-95]

![발표 마지막 슬라이드. 기술적 제약, 엔지니어링과 미술의 협업, 세부 작업, 2D 픽셀 아트에 대한 관심이 적혀 있다.](https://img.seosoyoung.eiaserinnys.me/images/nevers-end-3d-sprite-world/slide-95.jpg)

*주켓이 제작에 필요한 조건으로 제시한 네 가지. [^pdf-95]*

나는 발 관절의 설정을 특히 흥미롭게 읽었다. 부모의 픽셀 정렬 오프셋을 상속할지 선택할 수 있다. 같은 픽셀 정렬을 적용하더라도 발은 바닥에 남아 있어야 한다. 선을 추가한 픽셀에도 원래 표면에 맞는 깊이가 필요하다. 물과 안개를 처리할 때는 스프라이트 정렬용 깊이와 별도로 일반 깊이를 출력한다. 발표가 보여 준 구현은 이런 개별 조절까지 포함한다.

## 출처

- 발표: Ryan Juckett, Director, Hypersect. 「How We Draw a 3D Sprite World: The Stylized Art of Never’s End」.
- 행사와 일시: GDC 2026 Technical Artist Summit, 2026년 3월 10일 오후 3시 10분부터 4시 10분까지, 샌프란시스코 현지 시각. [공식 일정](https://schedule.gdconf.com/session/how-we-draw-a-3d-sprite-world-the-stylized-art-of-nevers-end/914052).
- 원자료: [Hypersect 공개 PDF, 99쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf). 전달받은 발표 PDF를 기준으로 전체 텍스트와 정지 화면을 확인했다.
- 자료 공개: 2026년 3월 11일 [Hypersect 안내 글](https://blog.hypersect.com/how-we-draw-a-3d-sprite-world-gdc2026/). 이 글에서 PDF와 동영상 및 애니메이션을 포함한 PowerPoint를 함께 제공한다.

[^source]: 이미지와 기술 설명의 출처는 Ryan Juckett와 Hypersect의 발표 PDF다. 인용 그림은 해당 페이지의 정지 화면이며 별도의 재사용 라이선스 표기는 확인하지 못했다. 상단 이미지는 PDF 19쪽의 최종 장면이다. 쪽수는 행사 안내를 포함한 99쪽 PDF의 페이지 번호다. 각 그림과 설명에 붙은 사이드노트에서 원문 페이지를 확인할 수 있다.
[^still]: 이번 정리는 PDF에 공개된 설명과 정지 화면에 근거한다. Hypersect는 PowerPoint에 동영상과 애니메이션이 포함되어 있고 PDF에는 정지 이미지만 있다고 안내했다. 움직임의 실제 재생과 발표자의 구두 설명은 확인하지 않았다.
[^ramp-row]: 35쪽은 램프를 확산광, 정반사광, 주변광 차폐 순서로 나열하지만, 45쪽은 정반사 결과를 램프의 세 번째 행에 전달한다고 적는다. 공개 PDF의 두 설명에 순서 차이가 있다. 여기서는 세 번째 행을 특정 기능에 임의로 대응시키지 않고, 확인 가능한 처리 순서만 서술했다.
[^hair-formula]: `^`는 원 슬라이드의 표기대로 거듭제곱을 나타낸다. PDF에는 거리값의 정규화와 곡선의 결합 방식 등을 포함한 완전한 셰이더 코드가 제시되어 있지 않다. 식과 매개변수의 용도는 공개된 설명대로 옮겼다.
[^dual-depth]: 89쪽의 스프라이트 깊이는 스프라이트마다 평평한 값이 된 것이 아니다. 슬라이드는 깊이의 세부 정보가 압축되어 구분하기 어렵다고 설명한다. 검은 지형 블록은 마지막 순서로 정렬하는 웅덩이다.

[^pdf-6-7]: [PDF 6~7쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=6).
[^pdf-8]: [PDF 8쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=8).
[^pdf-9]: [PDF 9쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=9).
[^pdf-20-23]: [PDF 20~23쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=20).
[^pdf-25]: [PDF 25쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=25).
[^pdf-26]: [PDF 26쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=26).
[^pdf-29]: [PDF 29쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=29).
[^pdf-30]: [PDF 30쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=30).
[^pdf-31]: [PDF 31쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=31).
[^pdf-32-33]: [PDF 32~33쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=32).
[^pdf-35]: [PDF 35쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=35).
[^pdf-37]: [PDF 37쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=37).
[^pdf-38]: [PDF 38쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=38).
[^pdf-40-43]: [PDF 40~43쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=40).
[^pdf-43]: [PDF 43쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=43).
[^pdf-44-54]: [PDF 44쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=44), [PDF 54쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=54).
[^pdf-48]: [PDF 48쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=48).
[^pdf-50-51]: [PDF 50~51쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=50).
[^pdf-52]: [PDF 52쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=52).
[^pdf-53]: [PDF 53쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=53).
[^pdf-55-56]: [PDF 55~56쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=55).
[^pdf-58]: [PDF 58쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=58).
[^pdf-59]: [PDF 59쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=59).
[^pdf-60]: [PDF 60쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=60).
[^pdf-61]: [PDF 61쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=61).
[^pdf-62]: [PDF 62쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=62).
[^pdf-63]: [PDF 63쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=63).
[^pdf-65-72]: [PDF 65~72쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=65).
[^pdf-65]: [PDF 65쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=65).
[^pdf-66]: [PDF 66쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=66).
[^pdf-68]: [PDF 68쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=68).
[^pdf-69]: [PDF 69쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=69).
[^pdf-70]: [PDF 70쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=70).
[^pdf-71]: [PDF 71쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=71).
[^pdf-72]: [PDF 72쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=72).
[^pdf-76-77]: [PDF 76~77쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=76).
[^pdf-80]: [PDF 80쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=80).
[^pdf-78]: [PDF 78쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=78).
[^pdf-82-83]: [PDF 82~83쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=82).
[^pdf-85]: [PDF 85쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=85).
[^pdf-86-87]: [PDF 86~87쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=86).
[^pdf-88]: [PDF 88쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=88).
[^pdf-89-90]: [PDF 89~90쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=89).
[^pdf-92]: [PDF 92쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=92).
[^pdf-93]: [PDF 93쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=93).
[^pdf-94]: [PDF 94쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=94).
[^pdf-95]: [PDF 95쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=95).
[^pdf-13]: [PDF 13쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=13).
[^pdf-24]: [PDF 24쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=24).
[^pdf-27]: [PDF 27쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=27).
[^pdf-36]: [PDF 36쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=36).
[^pdf-41]: [PDF 41쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=41).
[^pdf-47]: [PDF 47쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=47).
[^pdf-49]: [PDF 49쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=49).
[^pdf-57]: [PDF 57쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=57).
[^pdf-67]: [PDF 67쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=67).
[^pdf-74]: [PDF 74쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=74).
[^pdf-79]: [PDF 79쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=79).
[^pdf-83]: [PDF 83쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=83).
[^pdf-84]: [PDF 84쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=84).
[^pdf-87]: [PDF 87쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=87).
[^pdf-89]: [PDF 89쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=89).
[^pdf-74-75]: [PDF 74~75쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=74).
[^pdf-6]: [PDF 6쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=6).
[^pdf-20]: [PDF 20쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=20).
[^pdf-28]: [PDF 28쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=28).
[^pdf-33]: [PDF 33쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=33).
[^pdf-81]: [PDF 81쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=81).

[^pdf-45]: [PDF 45쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=45).
[^pdf-11]: [PDF 11쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=11).
[^pdf-39]: [PDF 39쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=39).
[^pdf-14-19]: [PDF 14~19쪽](https://www.hypersect.com/gdc2026/GDC_2026_NeversEnd.pdf#page=14).
