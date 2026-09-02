---
title: "Lumen Decor Studio 2"
date: 2026-07-22T14:00:00+09:00
tags: ["소프트웨어", "Three.js", "WebGPU", "글로벌 일루미네이션", "렌더링", "TSL"]
categories: ["게임"]
summary: "Anderson Mancini가 만든 브라우저 인테리어 configurator. Three.js r185의 TSL 위에서 WebGPU deferred 파이프라인, GTAO 기반 SSGI, SSR, bilateral과 temporal이 겹친 디노이저를 직접 짜서, 태양광이 실시간으로 색을 튕겨내는 3D 로프트를 로컬호스트급 비용으로 굴린다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/mancini-lumen-decor-studio-webgpu-ssgi/hero-loft.jpg"
  alt: "Lumen Studio 2의 로프트 뷰. 오전 07:16, 유리 난간과 대리석 벽, 이층의 침실과 아래층의 소파와 계단. 창으로 들어온 아침 햇살이 대리석과 천장을 타고 굴절하며 각 면에서 색을 실어 나른다. 출처: Anderson Mancini, [Threejs Architecture Visualization - Lumen Decor Studio - WebGPU SSGI + PROBER](https://www.youtube.com/watch?v=cDYIdId3XSY)"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/mancini-lumen-decor-studio-webgpu-ssgi/hero-loft.jpg"
---

## 3줄 요약

1. 브라질 개발자 Anderson Mancini(@ektogamat)가 만든 WebGPU 기반 인테리어 configurator다. 첫 번째 Three.js Conference 파리 발표 작품이며, 소스는 `https://lumen-decor-studio-2.vercel.app/`에서 그대로 돌아간다.
2. 렌더 파이프라인은 커스텀으로 다시 짜 넣었다. TSL로 작성한 SSGINode와 SSRNode가 deferred G-Buffer(MRT로 color/depth/normal/velocity를 동시에 뽑는다) 위에서 GTAO식 arc integration으로 간접광을 얻고, blueNoise 샘플링과 velocity 재투영, bilateral 두 번 반복으로 노이즈를 정리한다.
3. 디버그 뷰 10종이 UI에 그대로 노출된다. Combined, Direct, SSGI AO, SSGI GI, SSR Raw, Emissive, Bloom, SSR Denoised, SSR Ray Length, N8AO. 화면 밖에서 오는 빛과 대략 1미터를 넘는 원거리 반사는 다루지 못한다는 한계도 같은 UI에서 그대로 드러난다.

## Lumen이라는 이름이 걸어놓은 문제

Unreal Engine 5의 Lumen을 브라우저에서 그대로 되풀이하겠다는 뜻은 아니다. Mancini가 걸어놓은 문제는 조금 다르다. **부동산과 건축 시각화를 실시간 웹에서 굴리는 것**이다. Codrops의 스피커 소개는 이 지향을 그대로 옮겨 적었다.

> His latest experiments have focused on combining SSGI and SSR for architectural visualization, helping bring high-quality real-time rendering to the real estate industry.

지금까지 부동산 프리뷰의 표준 흐름은 오프라인 렌더 사진 또는 Unity/UE 빌드로 만든 데스크톱 앱이다. 전자는 인터랙션이 없고, 후자는 다운로드 장벽이 있다. Mancini는 브라우저 URL 한 줄로 열리는 실시간 configurator를 목표에 두고, 그 안에서 인테리어의 톤을 결정짓는 두 가지, 즉 태양광과 재질 색을 실시간으로 조작할 수 있게 만들었다. 표면에 색을 칠하면 그 색이 벽과 바닥으로 튕겨 씬 전체의 색조를 바꾼다. 오후 5시의 골든 아워에서 아침 7시의 창가로 시간대 슬라이더를 밀면 명암과 반사가 즉시 재계산된다.

## 스택: WebGPU, TSL, R3F

번들을 뜯어 확인한 스택은 다음과 같다.

| 계층 | 도구 | 확인 지점 |
|---|---|---|
| 그래픽 API | WebGPU | 페이지 title 및 Chrome headless에서 GPU exit_code=34 |
| 3D 라이브러리 | Three.js r185 | 번들 상단 라이선스 헤더 `const il="185"` |
| 셰이더 언어 | TSL (Three Shading Language) | `SSGINode`, `SSRNode`가 TSL base 클래스를 상속 |
| React 통합 | React Three Fiber | 저자가 codrops와 유튜브 설명에서 명시 |
| 배포 | Vercel | 도메인 `*.vercel.app` |
| 상태 저장 | localStorage | 키 `lumen-studio-project`, `lumen-development-mode` |
| PNG 익스포트 | 클라이언트 캔버스 → 다운로드 | 파일명 규격 `lumen-studio-{ISO타임스탬프}.png` |

TSL은 Three.js가 도입한 노드 그래프식 셰이더 정의 계층이다. WGSL이나 GLSL을 직접 쓰지 않고 자바스크립트에서 셰이더 노드를 조립하면, Three.js가 WebGPU 대상에는 WGSL을, WebGL 대상에는 GLSL을 생성해 준다. Mancini는 이 계층을 **바닐라 Three.js에는 없는 렌더 패스를 새로 짜 넣는 데** 쓴다. 즉 SSGI와 SSR 노드를 자기 손으로 하나 더 만들어서 파이프라인에 끼워 넣는다. 이 지점이 이 데모의 골자다.

## G-Buffer: MRT로 씬을 분해한다

간접광을 화면 공간에서 뽑으려면 씬을 먼저 분해해 두어야 한다. Lumen Studio는 forward가 아니라 deferred로 렌더한다. 첫 패스에서 씬을 한 번만 그리되, 색만 그리는 대신 여러 개의 렌더 타깃에 동시에 각기 다른 정보를 뱉는다. 이것이 MRT(Multiple Render Targets)이다.

번들에서 확인되는 MRT 채널은 최소 다음과 같다.

- **color**: 디퓨즈 알베도 (직접광 계산 재료)
- **depth**: 카메라 공간의 픽셀 거리 (화면 공간 레이 마칭의 좌표계)
- **normal**: 표면 법선 (반사 방향과 GI 반구 방향의 기준)
- **velocity**: 이전 프레임에서 이 픽셀이 어디에 있었는가 (temporal 재투영)
- **emissive**: 자체 발광 (dynamic emissive lighting을 SSGI 소스로 취급)

두 번째 이후의 패스는 씬 지오메트리를 다시 그리지 않는다. 이 텍스처들만 읽어서 픽셀 셰이더로 GI, 반사, 앰비언트 오클루전, 블룸을 계산한다. deferred가 아니면 SSGI는 성립하지 않는다. Three.js 포럼의 SSGI 스레드도 같은 요구사항을 반복 강조한다.

> The technique requires deferred rendering with depth, normal, and color buffers, plus roughness data for physically-based blending.

## SSGI: 화면 공간에서 간접광을 얻는다

여기가 이 프로젝트의 심장이다. 스크린 스페이스 글로벌 일루미네이션(SSGI)은 이름 그대로다. **레이 트레이싱을 실제로 하지 않고**, 지금 눈에 보이는 픽셀들만 사용해 간접광을 근사한다. 원리는 아래 순서다.

1. **화면의 각 픽셀에서 반구를 설정한다.** 표면 법선을 축으로 삼아 반구를 세우고, 그 반구를 얇은 부채꼴(slice)로 자른다. 번들의 `sliceCount` 파라미터가 이 개수를 결정한다. quality 프리셋에 따라 1, 2, 3으로 커진다.
2. **각 슬라이스 안에서 지평선(horizon)을 찾는다.** 슬라이스 방향으로 이웃 픽셀들의 깊이를 훑으며, 이 픽셀에서 하늘이 보이는 각도를 이등분한다. 이것이 GTAO(Ground Truth Ambient Occlusion)의 arc integration이다. 단순히 샘플의 개수만 세는 SSAO와 달리, "얼마나 넓은 각도로 하늘이 뚫려 있는가"를 각도의 적분으로 답한다.
3. **그 각도 안에서 이웃 픽셀의 색을 모은다.** 하늘이 보이는 각도는 곧 이 픽셀이 "밖에서 빛을 받을 수 있는 창"이다. 그 창 안에 있는 이웃 픽셀들의 알베도와 emissive를 가중 합산하면 간접광 기여가 된다. 이 두 번째 단계 덕분에 SSGI는 SSAO보다 한 걸음 나아간다. AO는 어두워지기만 하지만, GI는 이웃의 색을 실어 나른다.
4. **`maxDistance`로 유효 반경을 자른다.** 번들의 quality 프리셋은 1.109부터 4.5 사이의 값을 갖고, 기본값(Medium)은 대략 2미터 안쪽이다. 그 밖의 표면은 어차피 화면 공간에서 안정적인 히트를 얻기 어렵고, 늘리면 노이즈가 급격히 늘어난다.

이 반구 적분이 씬을 한 번 훑고 나오면 두 가지 출력이 남는다. 하나는 **SSGI AO** 채널이고, 하나는 **SSGI GI** 채널이다. AO는 얼마나 가려져 있는가, GI는 어떤 색이 들어왔는가를 담는다. 디버그 뷰에서 두 채널을 따로 확인할 수 있는 이유가 여기 있다.

![SSGI 데모(자매 프로젝트 `ssgi-webgpu-demo`)의 창고 씬. 창으로 들어온 태양광이 바닥에 격자 그림자를 만들고, 그 반사가 황금 링 안쪽에 얹혀 있다. UI 하단에는 Time of Day와 Sun Rotation 슬라이더가 노출된다. 출처: Anderson Mancini, [Threejs SSGI TSL WebGPU - R3F Demo by Anderson Mancini](https://www.youtube.com/watch?v=hIRe9If5yxg)](https://img.seosoyoung.eiaserinnys.me/images/mancini-lumen-decor-studio-webgpu-ssgi/ssgi-warehouse.jpg)

## SSR: 거울 표면의 반사

간접광이 부드러운 확산 반사라면, SSR(Screen Space Reflection)은 날카로운 정반사를 담당한다. 대리석 바닥이나 유리에 비치는 창밖의 실루엣이 이 패스의 산출물이다.

파이프라인은 SSGI와 대칭적이다.

1. 표면 법선을 축으로 뷰 벡터를 반사시킨 뒤, 그 방향으로 화면 공간에서 레이 마칭을 시작한다.
2. 이때 지오메트리를 다시 그리지 않고, 이미 갖고 있는 depth 텍스처를 계층화한 자료구조(hi-Z, 번들에서 `hiZ` 흔적 확인)를 훑는다. 큰 셀에서 훑다가 히트가 가까워지면 점점 촘촘히 훑어 들어가는 방식이다. 픽셀 단위로 처음부터 훑는 것보다 훨씬 빠르다.
3. 히트 지점의 색을 그대로 가져오지 않고 `roughness`로 흐리게 만든다. 거친 표면일수록 반사가 뭉개져야 자연스럽다.
4. 반사가 화면 밖으로 나가거나, `maxDistance` 안에서 히트를 못 잡으면 그 픽셀은 환경맵(BasicEnvironmentNode)에서 대신 받는다.

디버그 뷰의 **SSR Ray Length** 채널은 이 레이가 몇 걸음 만에 히트했는가를 색으로 보여준다. 반사가 어색하게 사라지는 자리를 디버깅할 때 결정적이다.

## 디노이저: 노이즈를 지우는 네 겹의 방어선

SSGI든 SSR이든 화면 공간 근사는 픽셀당 몇 개의 샘플만 던져야 한다. 그러면 결과는 노이즈로 가득 찬다. Lumen Studio는 이 노이즈를 네 겹으로 지운다.

1. **blueNoise 샘플링**: 처음부터 화이트 노이즈가 아니라 저주파 성분이 억제된 blueNoise 텍스처로 샘플 위치를 결정한다. 같은 예산으로 시각적으로 덜 거슬리는 노이즈가 나온다.
2. **temporal 재투영**: 이전 프레임의 결과를 velocity 텍스처로 이번 프레임 좌표에 맞춰 밀어 넣는다. 이 픽셀이 어제도 비슷하게 보였다면, 어제의 색을 대부분 신뢰한다.
3. **bilateral 공간 디노이즈**: 이번 프레임 안에서 이웃 픽셀의 결과를 흐리되, 법선과 depth가 크게 다르면 이웃으로 취급하지 않는다. 표면 경계에서 색이 새는 것을 막는다.
4. **jitter**: 여러 프레임에 걸쳐 샘플 위치를 조금씩 흩는다. 이 흔들림 위에서 temporal이 자연스럽게 합산 효과를 낸다.

번들에 `denoiseIterations`가 하드코딩 2로 잡혀 있다. bilateral 두 번 반복으로도 충분하고, 그 이상은 GI가 오히려 뭉개진다는 뜻이다. TAA(Temporal Anti-Aliasing)와도 같은 velocity 텍스처를 공유한다.

## 인터랙션과 품질 프리셋

configurator UI는 렌더 파이프라인의 여러 knob을 그대로 사용자에게 열어 준다.

- **시간대 슬라이더**: 태양의 고도와 색온도를 바꾼다. Golden, Morning 등 프리셋 이름이 UI에 노출된다.
- **Sun Rotation**: 태양의 방위각을 회전시킨다. SSGI의 간접광 방향이 즉시 재계산된다.
- **표면 페인팅**: 마우스로 벽이나 가구를 클릭해 색을 바꾼다. 알베도가 바뀌면 SSGI가 그 색을 이웃으로 튕겨 낸다.
- **카메라 뷰 프리셋**: Overview, Bed View, Bedside View, Window View 같은 미리 저장된 카메라 컷을 원터치로 전환한다.
- **품질 프리셋**: Low, Medium, High, Ultra 네 단계. `sliceCount`(1\~3), `stepCount`, `maxDistance`(1.109\~4.5) 값이 함께 바뀐다.
- **디버그 뷰 선택**: 앞서 언급한 10종을 UI에서 바로 갈아 낀다. 개발자용 창이 아니라 발표용 데모의 정식 기능이다.

프로젝트 전체 상태(색 팔레트, 카메라, 시간)는 `lumen-studio-project`라는 localStorage 키에 저장된다. 스크린샷은 클라이언트 캔버스에서 `lumen-studio-{ISO타임스탬프}.png`로 다운로드된다. 서버 왕복 없이 브라우저 안에서 완결된다.

![Lumen Studio 초판의 침실 뷰. 오후 07:15, 원형 액자와 디지털 시계, 침대 헤드보드에 얹힌 창밖 노을. 하단 UI에는 카메라 뷰 프리셋(OVERVIEW / BED VIEW / BEDSIDE VIEW / WINDOW VIEW)이 노출된다. 출처: Anderson Mancini, [Lumen Decor Studio - New 3D Configurator by Anderson Mancini](https://www.youtube.com/watch?v=vpfQOoAX0G0)](https://img.seosoyoung.eiaserinnys.me/images/mancini-lumen-decor-studio-webgpu-ssgi/configurator-bedroom.jpg)

## 한계: 화면 밖에서 오는 빛은 없다

Three.js 포럼의 SSGI 스레드는 이 기법의 한계를 다음처럼 요약한다.

- **Light leaking**: 실제로 가려져 있어야 할 표면이 이웃 픽셀의 빛을 받아 밝아진다. horizon search에는 가시성 정보가 없기 때문이다.
- **Small effective radius (\~1m)**: 정확한 결과가 나오는 반경이 대략 1미터다. 넓은 실내를 가로지르는 빛의 이동은 담지 못한다.
- **Screen-space constraints**: 카메라가 안 잡는 물체는 존재하지 않는 것으로 취급된다. 카메라 뒤의 노란 벽이 앞의 흰 벽에 색을 실을 방법은 없다.

Lumen Studio는 이 한계를 숨기지 않는다. 유튜브 영상 제목의 "PROBER"라는 표현이 그 흔적이다. 번들의 `LightProbe` 코드(24회 등장)가 함께 살아 있고, 씬 안에는 미리 계산된 환경맵과 라이트 프로브가 배치되어 있다. 화면 공간 근사가 다루지 못하는 원거리 간접광은 프로브에서 받아 채운다. UE5 Lumen이 화면 공간 → 심 캐시 → 표면 캐시로 fallback 하는 구조를 훨씬 단순한 형태로 옮겨 놓은 셈이다.

또 하나 실무적 한계가 있다. **WebGPU 없이는 이 데모가 열리지 않는다.** headless Chrome에 GPU 없이 접근하면 검은 화면이 나온다. 나도 이 다이제스트를 준비하며 GPU 프로세스가 exit_code 34로 죽는 것을 두 번 확인했다. 부동산 실무에 들이려면 iOS Safari(2026년 현재도 WebGPU 지원이 데스크톱보다 뒤늦다)와 저사양 안드로이드에서의 폴백 전략이 필요하다.

## 가장 눈여겨본 대목

가장 흥미로웠던 것은 이 데모가 자기 파이프라인을 통째로 UI로 노출한다는 점이다. Combined에서 시작해 Direct만, SSGI GI만, SSR Denoised만 볼 수 있는 스위치가 사이드바에 있다. 개발자 도구가 아니라 발표 시연의 일부다.

일반적으로 이런 디버그 뷰는 최종 빌드에서 벗겨낸다. Mancini는 반대로 남겼다. **결과가 어떻게 만들어졌는지 그 자체가 데모의 콘텐츠**라는 판단으로 읽힌다. 부동산 프리뷰라는 목표를 감안하면 이상해 보일 수도 있는데, 실제로는 정반대다. 화면 공간 근사의 산업적 채택을 이끌려면, 무엇을 못 하는지도 정직하게 보여줘야 한다. AO만 켜서 어두워지지 않는 자리, GI만 켜서 이웃 색이 튀는 자리, Ray Length가 툭 끊기는 자리를 다른 사람이 열어 보고 스스로 판단할 수 있어야 다음 계약이 이어진다.

같은 이유로, N8AO(별도의 개별 AO 파이프라인)를 SSGI와 나란히 노출한 것도 인상적이다. "우리 SSGI만 정답"이라는 톤이 아니라, 씬에 따라 골라 쓸 수 있게 두 파이프라인을 함께 살려 두었다.

## 출처

- 라이브 데모(v2): <https://lumen-decor-studio-2.vercel.app/>
- 이전 버전(v1): <https://lumen-decor-studio.vercel.app/>
- 자매 프로젝트(SSGI만 단독): <https://ssgi-webgpu-demo.vercel.app/>
- 저자 프로필(Three.js Conf 파리 스피커): <https://tympanus.net/codrops/2026/07/16/meet-the-speakers-of-the-first-three-js-conference/>
- 저자 X: <https://twitter.com/Andersonmancini>
- 저자 GitHub: <https://github.com/ektogamat>
- 참고 배경(Three.js 포럼 SSGI 스레드): <https://discourse.threejs.org/t/ssgi-screen-space-global-illumination/85190>

본문의 스크린샷은 저자의 유튜브 홍보 영상 썸네일에서 인용했다. 각 이미지 caption에 원문 링크를 표기했다.
