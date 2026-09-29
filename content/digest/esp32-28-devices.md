---
title: "ESP32로 만든 28가지 장치: 탁상 로봇부터 위성 수신국까지"
date: 2026-09-29T13:15:00+09:00
tags: ["ESP32", "마이크로컨트롤러", "메이커", "오픈소스"]
categories: ["창작과 문화"]
summary: "Wi-Fi와 블루투스를 갖춘 마이크로컨트롤러 ESP32로 만든 공개 프로젝트 28개를 사진과 시연 영상으로 소개한다. 대부분의 장치에서 ESP32는 센서와 모터, 화면, 스피커, 무선을 직접 다루고, 음성 인식이나 언어모델 같은 무거운 계산은 서버나 PC가 처리한다. 칩 세대에 따라 블루투스 Classic과 PSRAM 지원이 달라서, 따라 만들려면 프로젝트가 지정한 보드를 먼저 확인해야 한다."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/00-cover.jpg"
  alt: "ESP32로 만든 장치 사진 여섯 장. 표정을 띄운 탁상 로봇, 조명이 켜진 모래 무늬 테이블, 전자종이 날씨판, 열화상 카메라, 인터넷 라디오, 감열 프린터."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/00-cover.jpg"
---

<style>
.post-content figure.esp-fig{margin:1.1em 0 1.4em}
.post-content figure.esp-fig img{display:block;width:auto;max-width:100%;height:auto;max-height:80vh;margin:0 auto;border-radius:6px}
.post-content figure.esp-fig video{display:block;width:100%;height:auto;max-height:80vh;background:#111;border-radius:6px}
.post-content .esp-embed{position:relative;width:100%;aspect-ratio:16/9;background:#111;border-radius:6px;overflow:hidden}
.post-content .esp-embed iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.post-content figure.esp-fig>figcaption{margin:.5em 0 0;font-size:.86em;font-weight:400;line-height:1.55;text-align:left;color:var(--secondary)}
.post-content .esp-note{font-size:.93em;padding:.8em 1em;border-left:3px solid rgba(127,127,127,.45);background:rgba(127,127,127,.08);border-radius:4px}
</style>

ESP32는 Espressif가 만든 Wi-Fi 겸 블루투스 마이크로컨트롤러다. 저장소와 제작 기록이 공개된 ESP32 프로젝트 가운데, 작동하는 모습을 사진이나 영상으로 확인할 수 있는 28개를 골랐다. 탁상 로봇부터 위성 신호 수신국까지 있다.

28개에서 ESP32가 하는 일은 대체로 같다. 센서와 버튼을 읽고, 모터와 화면과 스피커를 구동하고, 무선으로 다른 기기와 데이터를 주고받는다. 음성 인식처럼 계산량이 큰 일은 서버나 PC가 맡는다.

<div class="esp-note">

**난도.** 공개된 코드와 지정 부품으로 따라 만든다고 할 때를 기준으로 이 글에서 붙인 분류다. 낮음은 완제품 기기에 펌웨어를 올리는 수준, 중간은 부품 배선과 개발환경 설정이 필요한 수준, 높음은 PCB 주문, 기구 조립, 보정이 필요한 수준이다.

</div>

## 캐릭터와 장난감

화면에 얼굴을 그리거나, 말을 듣고 답하거나, 카드 한 장으로 조작하는 장치들이다.

### 01. Stack-chan

고개를 돌리고 표정을 바꾸는 손바닥 크기의 탁상 로봇이다.

<figure class="esp-fig">
<video controls preload="none" playsinline muted loop poster="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/01-stackchan-clip.jpg">
  <source src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/01-stackchan-clip.mp4" type="video/mp4">
  <a href="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/01-stackchan-clip.mp4">영상 파일 열기</a>
</video>
<figcaption>README에 실린 동작 GIF. 고개를 돌리며 표정이 바뀐다. 원본 길이가 6초다. 출처: <a href="https://raw.githubusercontent.com/stack-chan/stack-chan/develop/docs/images/stackchan.gif">Stack-chan 저장소</a>, Apache-2.0</figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/01-stackchan-photo.jpg" alt="검은 입체 케이스 앞면 화면에 두 눈과 입이 표시된 작은 로봇이 받침대 위에 서 있다." loading="lazy">
<figcaption>Dynamixel 서보로 조립한 Stack-chan. 저장소의 케이스 문서에 실린 사진이다. 출처: <a href="https://github.com/stack-chan/stack-chan/blob/develop/case/docs/images/dynamixel_front.jpg">Stack-chan 저장소</a>, Apache-2.0</figcaption>
</figure>

M5Stack 보드의 화면에 눈과 입을 그리고, 서보모터로 몸체를 좌우로 돌리거나 위아래로 기울인다. 저장소에는 펌웨어와 MOD라고 부르는 사용자 앱, 브라우저 개발 도구, 케이스 설계와 회로도가 함께 들어 있다. 현재 README는 조립된 완제품 M5StackChan CoreS3를 표준 구성으로 안내하며, 다른 M5Stack 보드와 자작 케이스도 지원한다.

- **ESP32의 역할**: 보드의 ESP32 계열 칩(CoreS3는 ESP32-S3)이 화면, 소리, 서보를 제어하고 MOD를 실행한다. 브라우저는 펌웨어 설치와 저전력 블루투스(BLE) 설정에 쓰인다. 얼굴 추적 MOD 일부는 브라우저가 카메라로 인식한 결과를 BLE로 받아 움직인다.
- **부품**: M5Stack 보드(CoreS3 등), 서보모터와 브래킷, 케이스.
- **재현**: 완제품은 낮음. 웹 설치기로 펌웨어만 올리면 된다. 사진 같은 자작형은 중간. 3D 프린팅 케이스와 서보 조립이 필요하다.
- **제작**: Shinya Ishikawa(meganetaaan)와 Stack-chan 커뮤니티. [GitHub](https://github.com/stack-chan/stack-chan), Apache-2.0.

### 02. Xiaozhi(小智)

말을 걸면 서버의 AI와 대화해 음성으로 답하는 음성 단말기다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://player.bilibili.com/player.html?bvid=BV1bpjgzKEhd&amp;t=6&amp;autoplay=0&amp;danmaku=0&amp;high_quality=1" title="人类：给 AI 装摄像头 vs AI：当场发现主人三天没洗头" loading="lazy" allow="fullscreen" allowfullscreen></iframe></div>
<figcaption>사용자가 말을 걸자 화면의 이모지와 문장이 바뀌며 대답한다. 중국어 음성이 나온다. 재생하면 0:06부터 시작하며, 약 10초 동안이 해당 장면이다. 영상: 虾哥(제작자), <a href="https://www.bilibili.com/video/BV1bpjgzKEhd?t=6">Bilibili 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/02-xiaozhi-photo.jpg" alt="정사각형 기기 화면에 웃는 이모지와 중국어 문장이 떠 있다." loading="lazy">
<figcaption>ESP32-S3-BOX-3에서 실행한 화면. 이모지와 대답 문장이 함께 표시된다. 출처: <a href="https://github.com/78/xiaozhi-esp32#hardware">Xiaozhi 저장소</a>, MIT</figcaption>
</figure>

마이크로 들은 말을 AI 서비스에 보내고, 돌아온 음성을 스피커로 들려준다. 화면이 달린 보드는 대화하는 동안 이모지와 문장을 함께 띄운다. 기기의 입출력 핀과 화면을 AI가 조작할 수 있도록 MCP 인터페이스도 제공한다. README가 안내하는 지원 보드는 100종이 넘는다.

- **ESP32의 역할**: 오프라인 호출어 감지(ESP-SR), 마이크 입력의 잡음 처리, Opus 압축과 전송, 받은 음성의 재생, 화면 표시를 기기가 처리한다. 음성 인식, 언어모델, 음성 합성은 서버가 맡는다. 기본 펌웨어는 xiaozhi.me 서버에 접속하고, 호환되는 자체 서버를 쓸 수도 있다.
- **부품**: 지원 보드(ESP32, C3, C5, C6, S3, P4 계열), 마이크, 스피커와 오디오 코덱, 선택 사항으로 OLED나 LCD.
- **재현**: 중간. 지원 보드에는 미리 빌드한 펌웨어를 올리면 된다. 소스 빌드에는 ESP-IDF 6.0.1 이상이 필요하고 5.x는 지원하지 않는다.
- **제작**: 78(虾哥)과 프로젝트 참여자. [GitHub](https://github.com/78/xiaozhi-esp32), MIT.

### 03. ArduinoGotchi의 ESP32 이식판

1996년 다마고치 P1의 프로그램을 에뮬레이터로 실행하는 전자펫이다.

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/03-arduinogotchi-upstream-photo.jpg" alt="초록색 3D 프린팅 케이스를 열자 ESP32 보드, 배터리, 배선, 버튼이 보인다." loading="lazy">
<figcaption>RBEGamer의 TamagotchiESP32 제작 예. 3D 프린팅 케이스 안에 ESP32 개발 보드, 배터리, 버튼 배선이 들어 있다. M5StickC Plus2 포트는 공개된 사진과 영상이 없다. 출처: <a href="https://github.com/RBEGamer/TamagotchiESP32#example-build">RBEGamer/TamagotchiESP32</a>, GPL-2.0</figcaption>
</figure>

TamaLib 에뮬레이터로 다마고치 P1을 재현한다. 원작은 아두이노 우노용 ArduinoGotchi이고, anabolyc의 포크를 거쳐 RBEGamer가 ESP32 지원과 딥슬립 기능을 더했다. RBEGamer의 제작 예는 ESP32 개발 보드에 0.96인치 128×64 OLED, 버튼 세 개, 부저, 리튬 배터리를 연결했다. Coreymillia는 이 코드를 M5StickC Plus2에 이식해 기기에 내장된 화면과 버튼, 스피커를 그대로 쓰게 했다. 상태를 주기적으로 저장해 두고, 딥슬립에서 깨어나면 이어서 실행한다.

- **ESP32의 역할**: 에뮬레이션, 화면, 버튼, 소리, 저장, 절전을 기기 혼자 처리한다.
- **부품**: RBEGamer판은 ESP32 개발 보드, SSD1306 OLED, 버튼 3개, 부저, LiPo 배터리와 충전 보드. M5StickC Plus2 포트는 기기 한 대.
- **재현**: M5StickC Plus2 포트는 낮음. PlatformIO로 빌드해 USB로 올리면 되고 납땜이 필요 없다. RBEGamer판은 배선과 케이스 조립이 필요해 중간이다. 포트 저장소에는 ROM 데이터와 빌드된 펌웨어가 들어 있지만 라이선스 표기가 없고, ROM의 배포 권리도 확인되지 않는다.
- **제작**: GaryZ88(원작), RBEGamer(ESP32 이식), Coreymillia(M5StickC Plus2 포트). [TamagotchiESP32](https://github.com/RBEGamer/TamagotchiESP32)는 GPL-2.0, [M5StickC Plus2 포트](https://github.com/Coreymillia/ArduinoGotchi-M5Stick-esp32-Tamagotchi)는 라이선스 표기 없음.

### 04. ESPuino

RFID 카드를 대면 지정한 음악이나 오디오북을 재생하는 플레이어다.

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/04-espuino-photo.jpg" alt="파란 몸체에 흰 덮개를 씌운 정육면체 상자. 윗면에 버튼 세 개와 손잡이가 있다." loading="lazy">
<figcaption>ESPuino 공식 문서에 실린 제작 예(Biobox 3d). 윗면에 버튼 세 개와 회전 다이얼, 앞면에 스피커가 있다. 출처: <a href="https://github.com/biologist79/ESPuino-Docs/blob/main/docs/assets/Biobox3d.jpg">ESPuino 공식 문서</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/04-espuino-screen.png" alt="ESPuino 웹 화면에 SD 카드 폴더 트리와 RFID 칩 번호 입력 칸이 있다." loading="lazy">
<figcaption>웹 설정 화면. SD 카드의 폴더를 고르고 RFID 칩 번호를 입력해 짝짓는다. 출처: <a href="https://github.com/biologist79/ESPuino#web-interface">ESPuino 저장소</a>, GPL-3.0</figcaption>
</figure>

웹 설정 화면에서 RFID 태그 번호와 microSD의 파일이나 폴더, 또는 인터넷 방송 주소를 짝지어 둔다. 태그를 리더에 대면 지정한 오디오가 재생된다. 버튼과 회전 다이얼로 음량과 곡을 조작한다.

- **ESP32의 역할**: RFID 판독, SD 카드 재생, 디지털 오디오(I2S) 출력, 설정용 웹 서버를 기기가 직접 처리한다. 인터넷 방송이나 MQTT(기기 사이의 메시지 전달 규약) 연동을 쓸 때만 외부 서비스가 필요하다.
- **부품**: 추가 메모리(PSRAM)가 있는 ESP32-WROVER 계열 보드, RC522 또는 PN5180 RFID 리더, microSD 카드, I2S 오디오 변환 칩(DAC)과 앰프, 스피커.
- **조건**: README는 PSRAM이 없는 ESP32에서는 안정적으로 동작하지 않고, 작동하는 microSD가 없으면 부팅하지 않는다고 적었다. 블루투스 스피커 출력(A2DP)은 기존 방식의 블루투스 Classic이 필요해서 원형 ESP32에서만 쓸 수 있다.
- **재현**: 중간. 전용 PCB(ESPuino Complete)를 쓰면 배선이 줄어든다.
- **제작**: biologist79와 ESPuino 커뮤니티. [GitHub](https://github.com/biologist79/ESPuino), GPL-3.0.

## 디스플레이와 시각 오브제

작은 화면과 LED로 정보를 보여 주는 장치와, 모래에 무늬를 그리는 장치다.

### 05. HoloCubic

투명한 큐브 안에 그림이 떠 있는 것처럼 보이는 탁상 디스플레이다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/RQGz9suElo8?start=350&amp;end=360&amp;rel=0" title="Tiny Holo Cubic Display" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>조립한 HoloCubic에서 AIO 펌웨어를 실행한 장면. 큐브를 기울이면 다음 앱으로 넘어간다. 원본 영상의 5:50–6:00 구간만 재생된다. 영상: Data Slayer(제3자), <a href="https://www.youtube.com/watch?v=RQGz9suElo8&amp;t=350s">YouTube 원본</a></figcaption>
</figure>

1.3인치 240×240 LCD 화면에 한 변 25.4mm짜리 정육면체 분광 프리즘을 붙였다. 프리즘 안쪽 면이 LCD 화면을 반사해서, 정면에서 보면 그림과 글자가 투명한 큐브 안에 떠 있는 것처럼 보인다. 입체 홀로그램이나 투명 디스플레이는 아니다. 원작자는 표시 틀과 날씨 같은 기본 예시를 공개했고, 여러 앱을 담은 펌웨어는 ClimbSnail이 따로 만든 HoloCubic AIO다.

- **ESP32의 역할**: ESP32-PICO-D4가 화면을 구동하고, MPU6050 관성 센서로 기울임 입력을 읽고, Wi-Fi로 날씨 같은 정보를 받는다. 표시할 그림은 microSD에 둘 수 있다.
- **부품**: ESP32-PICO-D4 기판, 1.3인치 ST7789 LCD, 분광 프리즘, MPU6050, microSD 슬롯, 케이스.
- **재현**: 높음. 공개 PCB를 주문해 작은 부품을 납땜하고, 프리즘을 접착하고, 케이스를 3D 출력하거나 가공해야 한다. 원작 펌웨어는 Arduino ESP32 코어 1.0.4 기준이라 SPI 설정을 손으로 고쳐야 한다.
- **제작**: 稚晖君(peng-zhihui). [GitHub](https://github.com/peng-zhihui/HoloCubic), GPL-3.0. AIO 펌웨어는 [ClimbSnail/HoloCubic_AIO](https://github.com/ClimbSnail/HoloCubic_AIO).

### 06. WLED

주소 지정 LED의 색과 효과를 스마트폰으로 제어하는 펌웨어다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/toxMDCoVebI?start=864&amp;end=876&amp;rel=0" title="I made a 32x32 WLED MATRIX that is SOUND REACTIVE" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>32×32 LED 매트릭스에서 음악 반응 효과가 돈다. 소리가 함께 나온다. 원본 영상의 14:24–14:36 구간만 재생된다. 영상: Make It Work(제3자), <a href="https://www.youtube.com/watch?v=toxMDCoVebI&amp;t=864s">YouTube 원본</a></figcaption>
</figure>

ESP32에 설치하면 WS2812B 같은 주소 지정 LED 스트립과 2D 매트릭스의 색, 효과, 프리셋을 브라우저나 모바일 앱에서 바꿀 수 있다. JSON API, HTTP, MQTT로 다른 시스템에서 제어할 수도 있다. 음악에 반응하는 AudioReactive 기능은 별도 포크(Sound Reactive)에서 시작했고, 0.15.0부터 공식 배포본에 기본으로 들어갔다.

- **ESP32의 역할**: LED 신호와 효과를 생성하고, 연결한 마이크나 라인 입력의 소리를 분석한다. 스마트폰과 브라우저는 설정과 명령을 보낸다.
- **부품**: ESP32 보드, WS2812B 등 주소 지정 LED, LED에 맞는 별도 전원, 음악 반응용 I2S 마이크(선택).
- **조건**: 오디오 입력 방식은 칩 세대마다 다르다. 원형 ESP32는 아날로그와 I2S 마이크를 모두 쓰고, S2는 I2S, S3는 I2S와 PDM 마이크를 쓴다.
- **재현**: 낮음. 공식 웹 설치기로 펌웨어를 올리고 데이터선, 전원, 공통 접지를 연결한다. LED 수에 맞는 전원 용량은 따로 계산해야 한다.
- **제작**: Christian Schwinne(Aircoookie)이 시작했고 현재 WLED 커뮤니티가 관리한다. [GitHub](https://github.com/wled/WLED), EUPL-1.2.

### 07. Dune Weaver

모래 아래 자석으로 쇠구슬을 끌어 무늬를 그리는 키네틱 테이블이다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/JthAa2iGrU8?start=581&amp;end=591&amp;rel=0" title="Introducing Dune Weaver Pro - The Ultimate DIY Kinetic Sand Table" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>위에서 찍은 모래판에서 쇠구슬이 선을 그리며 잎 무늬를 더한다. 빠르게 돌린 타임랩스다. 원본 영상의 9:41–9:51 구간만 재생된다. 영상: Dune Weaver(제작자), <a href="https://www.youtube.com/watch?v=JthAa2iGrU8&amp;t=581s">YouTube 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/07-dune-weaver-photo.jpg" alt="원형 모래판 테이블 세 대에 서로 다른 기하학 무늬가 그려져 있고 가장자리 조명이 켜져 있다." loading="lazy">
<figcaption>완성된 테이블 세 대와 모래 무늬. 출처: <a href="https://github.com/tuanchris/dune-weaver">Dune Weaver 저장소</a></figcaption>
</figure>

스테퍼 모터 두 개가 모래판 아래의 자석을 회전 방향과 반지름 방향으로 움직이고, 자석을 따라가는 쇠구슬이 모래에 선을 그린다. 패턴 파일, 재생 목록, 조명, 예약 기능이 있다. 제작자는 설계 파일과 제작 안내서를 판매하고, 무료 설계(OG, Mini)도 공개한다. 실물 부품은 만드는 사람이 직접 구한다.

- **ESP32의 역할**: 현행 Pro 계열에서는 MKS-DLC32 보드의 ESP32가 FluidNC에서 파생한 Dune Weaver 펌웨어로 패턴 재생, 재생 목록, 조명, 예약, 모터 제어를 모두 처리한다. 휴대전화나 브라우저는 HTTP로 명령을 보낸다. 이전 구성에서는 라즈베리 파이가 패턴을 G-code로 바꾸고 ESP32는 모터만 구동했으며, 라즈베리 파이용 소프트웨어는 지금도 선택 사항으로 제공된다.
- **부품**: MKS-DLC32 제어 보드, NEMA 17 스테퍼 모터 2개, 자석과 쇠구슬, 모래와 원형 상판, 3D 출력 부품과 프레임, 12V 전원, LED 링(선택).
- **재현**: 높음. 3D 출력, 기계 조립, 두 축의 모터 배선과 설정이 필요하다.
- **제작**: Tuan Nguyen(tuanchris). [GitHub](https://github.com/tuanchris/dune-weaver), [펌웨어](https://github.com/tuanchris/dune-weaver-firmware), GPL-3.0(소프트웨어는 상용 라이선스와 함께 이중 라이선스).

### 08. atomic14 ESP32 TV

작은 LCD와 스피커로 영상과 소리를 재생하는 실험용 텔레비전이다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/dWgjsJtlbpA?start=303&amp;end=313&amp;rel=0" title="Streaming Video From an SD Card on the ESP32." loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>SD 카드에 넣은 영상을 작은 LCD로 재생한다. 소리가 함께 나온다. 원본 영상의 5:03–5:13 구간만 재생된다. 영상: atomic14(제작자), <a href="https://www.youtube.com/watch?v=dWgjsJtlbpA&amp;t=303s">YouTube 원본</a></figcaption>
</figure>

ESP32가 TFT 화면에 JPEG 프레임을 차례로 그리고 스피커로 소리를 낸다. 재생 방식은 두 가지다. Wi-Fi 방식은 PC에서 도는 Python 서버가 영상을 프레임과 소리로 나눠 보내고, ESP32는 소리 재생 시각에 맞춰 다음 프레임을 요청한다. SD 카드 방식은 PC에서 미리 변환해 둔 AVI 파일을 읽는다. 두 방식 모두 ESP32가 MP4를 직접 해독하지는 않는다.

- **ESP32의 역할**: JPEG 프레임 표시와 PCM 소리 재생. Wi-Fi 방식의 영상 전처리는 PC 서버가 하고, SD 방식의 변환은 미리 PC에서 ffmpeg로 해 둔다.
- **부품**: 지원 ESP32 보드(ESP32-S3 자작 PCB, TinyS3, Cheap Yellow Display 등), TFT 화면, MAX98357A 같은 오디오 앰프와 스피커, SD 카드.
- **재현**: 중간. 보드와 화면, 스피커 핀을 PlatformIO 설정에 맞추고, 영상은 ffmpeg로 초당 15프레임 MJPEG와 16kHz 8비트 단일 채널 PCM이 든 AVI로 변환한다.
- **제작**: atomic14. [GitHub](https://github.com/atomic14/esp32-tv). 저장소에 라이선스 표기가 없다.

## 게임과 물리적 놀이

옛 게임기를 흉내 내거나, 옛 게임기에 새 컨트롤러를 연결하거나, 방 하나를 퍼즐로 만든 사례다.

### 09. RetroESP32

ODROID-GO에서 여러 게임기 에뮬레이터를 고르고 실행하는 런처다.

<figure class="esp-fig">
<video controls preload="none" playsinline muted loop poster="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/09-retroesp32-clip.jpg">
  <source src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/09-retroesp32-clip.mp4" type="video/mp4">
  <a href="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/09-retroesp32-clip.mp4">영상 파일 열기</a>
</video>
<figcaption>ODROID-GO에서 런처가 켜지고 게임 목록의 선택 항목이 바뀐다. 저장소 README의 GIF를 변환했다. 출처: <a href="https://raw.githubusercontent.com/retro-esp32/RetroESP32/master/Assets/animated.gif">RetroESP32 저장소</a>, CC BY-SA 4.0</figcaption>
</figure>

Hardkernel의 휴대용 게임기 ODROID-GO에 올리는 펌웨어다. 게임 목록, 최근 실행, 즐겨찾기, 화면 테마를 제공하고, 고른 게임을 해당 기종의 에뮬레이터로 실행한다. README는 NES, 게임보이, 아타리, PC 엔진 등 에뮬레이터 11개를 묶었다고 적었다. 에뮬레이터 코어 대부분은 다른 제작자의 프로젝트를 하위 모듈로 가져왔다.

- **ESP32의 역할**: 런처 화면, 버튼 입력, 에뮬레이션을 모두 기기가 처리한다.
- **부품**: ODROID-GO 또는 호환 휴대기, microSD 카드.
- **재현**: 중간. 펌웨어 파일을 SD 카드에 복사하고 B 버튼을 누른 채 전원을 켜서 설치한다. 게임 파일은 따로 준비해야 한다.
- **제작**: 32teeth와 retro-esp32 기여자. [GitHub](https://github.com/retro-esp32/RetroESP32), CC BY-SA 4.0.

### 10. FabGL

ESP32로 VGA 모니터와 PS/2 키보드를 다루는 그래픽 라이브러리다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/3I1U2nEoxIQ?start=135&amp;end=145&amp;rel=0" title="IBM PC on ESP32 with FabGL - Part I (FreeDOS + GWBasic + QBASIC)" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>ESP32에서 돌린 IBM PC 에뮬레이터가 VGA 모니터에 그래픽을 그린다. 원본 영상의 2:15–2:25 구간만 재생된다. 영상: Fabrizio Di Vittorio(제작자), <a href="https://www.youtube.com/watch?v=3I1U2nEoxIQ&amp;t=135s">YouTube 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/10-fabgl-classic-racer.png" alt="초록빛 CRT 모니터 화면 세 장. 레이싱 게임의 제목, 주행 장면, 기록표가 있다." loading="lazy">
<figcaption>VGA 예제 게임 ClassicRacer의 시작, 주행, 기록 화면. 출처: <a href="https://github.com/fdivitto/FabGL/tree/master/examples/VGA/ClassicRacer">FabGL 저장소</a>, GPL-3.0</figcaption>
</figure>

VGA와 PAL/NTSC 컴포지트 영상 출력, PS/2 키보드와 마우스 입력, 소리, GUI, 게임 엔진, ANSI/VT 터미널을 제공한다. 저장소 예제에는 IBM PC 에뮬레이터와 레이싱 게임 ClassicRacer가 들어 있다. VGA 신호는 ESP32 핀에 저항을 연결해 만든 DAC나 전용 보드로 출력한다.

- **ESP32의 역할**: 영상 신호 생성, 키보드와 마우스 입력 처리, 프로그램 실행을 칩 하나가 한다.
- **부품**: ESP32 보드, 저항 DAC와 VGA 커넥터(또는 ESP32-SBC-FabGL 같은 전용 보드), 모니터, PS/2 키보드와 마우스.
- **조건**: Arduino ESP32 코어 2.0.17 이하에서 동작한다. README는 그보다 새 코어에서는 쓸 수 있는 메모리가 부족하다고 경고한다.
- **재현**: 높음. 코어 버전 고정, 저항 DAC 배선, 예제별 준비물(PC 에뮬레이터의 디스크 이미지 등)이 필요하다.
- **제작**: Fabrizio Di Vittorio. [GitHub](https://github.com/fdivitto/FabGL), GPL-3.0.

### 11. BlueRetro

블루투스 게임패드를 구형 게임기에 연결하는 어댑터다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/yj_Zbjb2_ms?start=176&amp;end=186&amp;rel=0" title="BlueRetro - Multiplayer Bluetooth controllers adapter for retro consoles" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>CRT 화면 앞에서 블루투스 패드를 바꿔 들며 구형 게임기를 조작한다. 원본 영상의 2:56–3:06 구간만 재생된다. 영상: darthcloud(제작자), <a href="https://www.youtube.com/watch?v=yj_Zbjb2_ms&amp;t=176s">YouTube 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/11-blueretro-adapter.jpg" alt="작은 회로 기판과 여러 컨트롤러, 구형 게임기, CRT 화면이 책상 위에 있다." loading="lazy">
<figcaption>BlueRetro 어댑터와 연결한 구형 게임기, 패드들. 출처: <a href="https://hackaday.io/project/170365-blueretro">BlueRetro, Hackaday.io</a></figcaption>
</figure>

블루투스 패드, 키보드, 마우스의 입력을 받아 NES, SNES, N64, 플레이스테이션, 게임큐브 같은 구형 기기의 컨트롤러 신호로 변환한다. 어댑터 하나에 패드 여러 개를 연결할 수 있다. 제작자는 2025년 12월 저장소를 보관(archived) 상태로 바꾸고 기능 추가와 버그 수정을 중단했다. 코드와 문서는 그대로 공개돼 있다.

- **ESP32의 역할**: 블루투스 연결, 입력 해석, 게임기 쪽 신호 출력을 모두 처리한다. 설정은 스마트폰이나 PC 브라우저의 Web Bluetooth 페이지에서 바꾼다.
- **조건**: 원형 ESP32가 필요하다. 블루투스 Classic을 쓰는 패드까지 받으려면 Classic과 LE를 모두 지원하는 칩이어야 하는데, ESP32-S3와 C3는 Classic을 지원하지 않는다.[^bt-classic]
- **부품**: ESP32-DevKitC, 게임기별 커넥터와 케이블.
- **재현**: 중간. 게임기 바깥에 꽂는 케이블형(HW1) 기준이다. 게임기 내부에 설치하는 HW2는 높음.
- **제작**: Jacques Gagnon(darthcloud). [GitHub](https://github.com/darthcloud/BlueRetro), 소프트웨어 Apache-2.0, 하드웨어 CERN-OHL-P-2.0.

### 12. Lost in k-Space

ESP32 여섯 대가 퍼즐 상태를 서로 주고받는 MRI 물리학 방탈출이다.

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/12-mr-escape-room-figure1.jpg" alt="서랍, 타일 조립기, 저울, 스피커, 키패드, 진행자 모니터의 사진을 선으로 연결한 도판." loading="lazy">
<figcaption>논문 Figure 1. 게임방의 퍼즐 장치와 방 밖 진행자 모니터의 관계를 정리한 도판이다. 무선 기호가 붙은 장치가 ESP-NOW로 통신하는 ESP32 노드다. 출처: <a href="https://arxiv.org/abs/2608.09616">Räuber 외, arXiv:2608.09616</a>, CC BY 4.0</figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/12-mr-escape-room-sequence-composer.jpg" alt="나무 상자 위에 펄스 파형이 그려진 타일이 두 줄로 놓여 있고, 윗면에 표시등이 있다." loading="lazy">
<figcaption>시퀀스 조립기. 펄스 타일을 두 줄로 놓고, 윗면 표시등이 안전 경고와 시퀀스 로드 상태를 알린다. 출처: <a href="https://github.com/BAMMri/MRPhysics-Escape-Room">BAMMri/MRPhysics-Escape-Room 제작 문서</a></figcaption>
</figure>

바젤 대학 연구진이 2025년 유럽 자기공명학회(ESMRMB) 연례 학회에서 운영한 교육용 방탈출이다. 네 명이 한 팀이 되어 25분 안에 퍼즐 다섯 개를 푼다. 라머 주파수를 계산해 서랍을 열고, 펄스 시퀀스 타일을 맞추고, 자성 물체를 찾아 저울에 올린다. 저울이 목표 무게를 감지하면 시퀀스 조립기의 안전 경고가 꺼지고 스캔 버튼이 활성화된다. 마지막으로 MRI 시퀀스의 소리를 구별해 코드를 입력하면 타이머가 멈춘다.[^kspace]

- **ESP32의 역할**: 키패드, 저울, 시퀀스 조립기, 스피커, 타이머, 진행자용 모니터가 각각 ESP32-DevKitC 한 대씩이다. 여섯 대가 ESP-NOW로 서버 없이 상태를 직접 주고받는다. 진행자 모니터는 각 장치의 연결 상태와 퍼즐 진행을 표시하고 타이머를 초기화할 수 있다.
- **부품**: ESP32-DevKitC 6대, 자체 설계 PCB, RFID 리더 10개가 달린 시퀀스 조립기, HX711 로드셀 저울, 키패드, 전자종이 타이머, TFT 모니터, 스피커.
- **재현**: 높음. 저장소에 Arduino 코드, PCB 설계, CNC와 3D 출력 파일, 부품표, 진행 문서가 있다. 각 노드의 MAC 주소를 라이브러리에 적어 다시 플래시하고, RFID 태그와 저울 목표값을 현장에 맞게 조정해야 한다.
- **제작**: Sabine Melanie Räuber, Marta Brigid Maggioni, Francesco Santini. [논문](https://arxiv.org/abs/2608.09616)(CC BY 4.0), [GitHub](https://github.com/BAMMri/MRPhysics-Escape-Room)(GPL-3.0).

## 물리 인터페이스와 출력

손으로 조작하는 입력 장치와, 종이와 빛으로 결과를 내보내는 출력 장치다.

### 13. SmartKnob

돌리는 손맛과 멈춤 지점을 소프트웨어로 바꾸는 다이얼이다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/ip641WmY4pA?start=19&amp;end=29&amp;rel=0" title="DIY haptic input knob: BLDC motor + round LCD" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>누르기로 0에서 10 범위 모드로 바꾸자, 돌려도 숫자가 0과 10에서 멈춘다. 손에 걸리는 저항은 영상으로 보이지 않는다. 원본 영상의 0:19–0:29 구간만 재생된다. 영상: Scott Bezek(제작자), <a href="https://www.youtube.com/watch?v=ip641WmY4pA&amp;t=19s">YouTube 원본</a></figcaption>
</figure>

자기 엔코더가 회전각을 재고, BLDC 짐벌 모터가 그 값에 맞춰 토크를 내서 가상의 딸깍임과 끝 멈춤을 만든다. 모드를 바꾸면 딸깍임 간격과 회전 범위가 달라진다. 화면 일체형인 SmartKnob View는 둥근 화면에 현재 값과 모드를 표시하고 누르는 입력도 감지한다. 저장소는 현재 펌웨어를 데모 단계라고 설명한다.

- **ESP32의 역할**: View의 ESP32-PICO-V3-02가 엔코더 판독, 모터 제어, 화면 표시를 처리한다. PC나 서버는 필요 없다. 별도 모터 제어 보드인 NanoFOC는 ESP32-S3를 쓴다.
- **부품**: 중공축 BLDC 짐벌 모터, 자기 엔코더, TMC6300 모터 드라이버, 원형 LCD, 전용 PCB와 케이스.
- **재현**: 높음. 미세 SMD 납땜, 모터와 엔코더 정렬, 정밀하게 출력한 케이스 조립이 필요하다. README는 최신 자동 생성 PCB 자료 대신 검증된 릴리스 자료를 쓰라고 권한다.
- **제작**: Scott Bezek. [GitHub](https://github.com/scottbez1/smartknob), 소프트웨어와 회로 Apache-2.0, 기구 CC BY 4.0.

### 14. FreeTouchDeck

터치스크린 버튼을 누르면 컴퓨터에 단축키를 보내는 매크로 패널이다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/soIGV6BszcM?start=384&amp;end=396&amp;rel=0" title="Build This Yourself for Just $20! FreeTouchDeck." loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>버튼을 눌러 설정 페이지로 넘어간다. 이 구간에는 컴퓨터 쪽에서 단축키가 실행되는 장면이 없다. 원본 영상의 6:24–6:36 구간만 재생된다. 영상: Dustin Watts(제작자), <a href="https://www.youtube.com/watch?v=soIGV6BszcM&amp;t=384s">YouTube 원본</a></figcaption>
</figure>

3.5인치 터치 화면에 버튼 여섯 개를 한 페이지로 띄운다. 버튼을 누르면 미리 정한 키 조합이나 미디어 키를 BLE 키보드 입력으로 Windows, macOS, Linux 컴퓨터에 보낸다. 앱 실행, 스크립트 실행, 사용 중인 앱에 따른 페이지 전환은 컴퓨터에 설치하는 FreeTouchDeck Helper가 처리한다.

- **ESP32의 역할**: 화면 표시, 터치 판정, BLE 키보드 신호 송신. 버튼 설정은 Wi-Fi로 접속하는 웹 설정 화면에서 한다.
- **부품**: ESP32 DEVKIT V1과 3.5인치 480×320 ILI9488 화면, XPT2046 저항식 터치. 또는 정전식 화면이 달린 ESP32 TouchDown 보드.
- **재현**: 중간. 웹 설치 도구로 펌웨어를 올릴 수 있다. 소스 빌드는 Arduino ESP32 코어 2.0.14를 권장하며, 3.x에서는 컴파일 문제가 생길 수 있다.
- **제작**: Dustin Watts. [GitHub](https://github.com/DustinWatts/FreeTouchDeck), MIT.

### 15. AWTRIX NG

LED 매트릭스 시계에 알림, 센서 값, 그래프를 띄우는 펌웨어다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/TWmSnGEnexQ?start=5&amp;end=15&amp;rel=0" title="Alles wird besser: Awtrix NG für Pixel-Uhr (Ulanzi TC001)" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>Ulanzi TC001에 설치한 AWTRIX NG. 시각 화면이 날씨 아이콘과 정보 화면으로 바뀐다. 원본 영상의 0:05–0:15 구간만 재생된다. 영상: haus:automation(제3자), <a href="https://www.youtube.com/watch?v=TWmSnGEnexQ&amp;t=5s">YouTube 원본</a></figcaption>
</figure>

높이 8픽셀, 너비 32에서 128픽셀까지의 WS2812 계열 LED 매트릭스에 시각, 날짜, 센서 값, 텍스트, 아이콘, 그래프를 표시한다. Home Assistant나 스크립트가 HTTP 또는 MQTT로 알림을 보내면 화면에 띄운다. Berry 스크립트로 만든 앱은 기기에서 직접 실행된다. AWTRIX 3의 후속작으로 코드를 새로 작성했고, API가 바뀌어 기존 AWTRIX 3 연동은 다시 설정해야 한다.

- **ESP32의 역할**: Wi-Fi 통신, LED 렌더링, 웹 설정 화면, 기기 내 앱 실행. Home Assistant 같은 외부 서비스는 정보를 보내 줄 뿐이고, 시계와 기기 내 앱에는 필요 없다.
- **부품**: Ulanzi TC001 같은 ESP32 LED 시계, 또는 ESP32나 ESP32-S3 보드와 WS2812 매트릭스.
- **재현**: 낮음. TC001 완제품이면 브라우저 플래셔로 설치한다. 매트릭스를 직접 배선하면 중간.
- **제작**: Stephan Mühl(Blueforcer). [GitHub](https://github.com/Blueforcer/awtrix-ng). 라이선스는 PolyForm Noncommercial 1.0.0으로, 비상업 용도만 허용한다.

### 16. ESP32 감열 프린터

ESP32가 보낸 명령으로 영수증, 이미지, 바코드, QR 코드를 인쇄하는 감열 프린터다.

<figure class="esp-fig">
<video controls preload="none" playsinline muted loop poster="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/16-thermal-printer-clip.jpg">
  <source src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/16-thermal-printer-clip.mp4" type="video/mp4">
  <a href="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/16-thermal-printer-clip.mp4">영상 파일 열기</a>
</video>
<figcaption>명령을 보내자 영수증이 인쇄되고, 이어서 QR 코드와 바코드가 나온다. 원본 GIF 전체다. 출처: <a href="https://raw.githubusercontent.com/Circuit-Digest/Interfacing-Thermal-Printer-POS-ESC-with-the-ESP32/2bdd4124172e4ed2b2a2da06fbf3370f518e70d7/Images/InvoicePrintedReducedSize.gif">CircuitDigest 저장소</a>, MIT</figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/16-thermal-printer-photo.png" alt="검은 감열 프린터 옆 브레드보드에 ESP32 보드가 꽂혀 있고 배터리 팩이 연결돼 있다." loading="lazy">
<figcaption>브레드보드의 ESP32, PNP-500 프린터, 프린터용 배터리 팩. 출처: <a href="https://circuitdigest.com/microcontroller-projects/how-to-interface-thermal-printer-with-esp32">CircuitDigest</a></figcaption>
</figure>

ESP32 개발 보드가 TTL UART로 PNP-500 감열 프린터에 ESC/POS 명령을 보낸다. 공개 코드는 영수증 형식의 텍스트, 1비트 비트맵 이미지, CODE128과 UPC-A와 EAN13 바코드, QR 코드를 출력한다. 버튼 두 개나 PC 시리얼 모니터의 명령으로 인쇄를 시작한다.

- **ESP32의 역할**: 입력을 받아 인쇄 데이터를 만들고 UART로 보낸다. 열 헤드 구동과 용지 이송은 프린터 내장 회로가 한다.
- **부품**: ESP32 개발 보드, PNP-500 TTL 감열 프린터, 57mm 감열지, 프린터용 2S 리튬이온 전원, 저항과 버튼.
- **재현**: 중간. 프린터에는 ESP32와 별개로 충분한 전원을 공급해야 한다. 인쇄할 이미지는 폭 384픽셀 이하의 1비트 비트맵으로 변환해 코드에 넣는다.
- **제작**: Rithik Krisna, CircuitDigest. [기사](https://circuitdigest.com/microcontroller-projects/how-to-interface-thermal-printer-with-esp32), [GitHub](https://github.com/Circuit-Digest/Interfacing-Thermal-Printer-POS-ESC-with-the-ESP32)(MIT).

## 소리와 전자종이

소리를 합성하거나 방송을 재생하는 장치, 전자종이에 날씨와 책을 표시하는 장치다.

### 17. ML SynthTools 기본 신시사이저

MIDI 건반 신호를 받아 ESP32가 직접 소리를 합성하는 다성 신시사이저다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/WJGOIgaY-1s?start=971&amp;end=981&amp;rel=0" title="Arduino polyphonic synthesizer project (not a Moog) for ESP32 - STM32 - Teensy and more" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>건반을 두 MIDI 채널로 나눠 왼손과 오른손이 서로 다른 음색을 연주한다. 영상 설명에 따르면 소리는 모두 ESP32 Audio Kit에서 후처리 없이 녹음했다. 원본 영상의 16:11–16:21 구간만 재생된다. 영상: Marcel Licence(제작자), <a href="https://www.youtube.com/watch?v=WJGOIgaY-1s&amp;t=971s">YouTube 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/17-ml-synth-diagram.png" alt="MIDI 인터페이스, 신스 모듈, 리버브, 딜레이, 오디오 인터페이스가 차례로 연결된 블록도." loading="lazy">
<figcaption>신시사이저 구조. MIDI 입력이 오실레이터 3×8, 보이스 8개, 필터를 거쳐 리버브와 딜레이, 오디오 출력으로 이어진다. 출처: <a href="https://github.com/marcel-licence/ml_synth_basic_example">ml_synth_basic_example 저장소</a>, GPL-3.0</figcaption>
</figure>

MIDI 노트와 컨트롤 신호를 받아 ESP32가 실시간으로 파형을 만든다. 보이스 하나에 오실레이터 3개가 붙고, README는 ESP32에서 8보이스 동시 발음을 시험했다고 적었다. 필터, 엔벌로프, 아르페지에이터, 리버브와 딜레이가 들어 있고, MIDI 채널 16개마다 음색을 따로 정할 수 있다. 출력은 44.1kHz 16비트로 I2S 오디오 코덱에 보낸다.

- **ESP32의 역할**: 합성, 효과, MIDI 수신, 오디오 출력을 칩 하나가 모두 처리한다. PC는 필요 없다.
- **부품**: ESP32 Audio Kit v2.2(AC101 또는 ES8388 코덱) 같은 코덱 보드, 또는 ESP32와 I2S DAC. MIDI 건반과 MIDI 입력 회로.
- **조건**: 합성 핵심부인 ML_SynthTools_Lib는 소스 없이 컴파일된 라이브러리로 배포되며, 개인, 교육, 연구 목적만 허용한다. 예제 저장소는 GPL-3.0이다. MIDI 입력이 쓰는 Serial2가 Arduino ESP32 코어 3.x에서 동작하지 않아서, 라이브러리 문서는 2.0.17 이하를 쓰라고 한다.
- **재현**: 중간. 코덱 보드로 시작하면 하드웨어 작업은 적다. 5핀 DIN MIDI 건반을 쓰려면 MIDI 입력 회로를 따로 만들어야 한다.
- **제작**: Marcel Licence. [GitHub](https://github.com/marcel-licence/ml_synth_basic_example), GPL-3.0.

### 18. yoRadio

Wi-Fi로 인터넷 방송을 받아 재생하는 라디오다.

<figure class="esp-fig">
<video controls preload="none" playsinline poster="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/18-yoradio-clip.jpg">
  <source src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/18-yoradio-clip.mp4" type="video/mp4">
  <a href="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/18-yoradio-clip.mp4">영상 파일 열기</a>
</video>
<figcaption>ESP32-2432S028 터치 보드에서 방송국 목록을 열어 다른 방송국을 고르고 음량을 올린다. 소리가 함께 나온다. 원본 2:55–3:06 발췌. 출처: <a href="https://www.youtube.com/watch?v=qGRDy2TjY5E">Daradici Levente</a>, CC BY</figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/18-yoradio-photo.jpg" alt="노란 3D 프린팅 거치대 왼쪽에 원형 스피커, 오른쪽에 방송국 정보와 시계가 뜬 화면, 아래에 ESP32 보드가 있다." loading="lazy">
<figcaption>저장소에 실린 제작 사례. 스피커, 컬러 화면, ESP32 보드를 거치대 하나에 모았다. 출처: <a href="https://github.com/e2002/yoradio/blob/main/Images.md">yoRadio 저장소</a>, GPL-3.0</figcaption>
</figure>

웹 화면에서 인터넷 방송국 주소를 재생 목록에 넣고 고른다. 버튼, 로터리 엔코더, 적외선 리모컨으로도 조작한다. 화면을 달면 방송국 정보와 시계를 표시하고, SD 카드의 음악도 재생할 수 있다.

- **ESP32의 역할**: 스트림 수신, 재생 목록 관리, 웹 설정 화면, 화면과 입력 장치 제어. 소리는 I2S DAC나 VS1053B 모듈 중 하나를 거쳐 앰프와 스피커로 나간다.
- **부품**: ESP32 개발 보드, I2S DAC 또는 VS1053B 모듈, 앰프와 스피커. 선택 사항으로 화면, 버튼, 엔코더, 적외선 수신기, SD 카드.
- **조건**: README는 Arduino IDE 1.8.19를 권장하고 IDE 2.x는 지원하지 않는다고 적었다. PSRAM은 재생에 필수가 아니지만 일부 TFT 화면은 PSRAM이 있는 모듈에서만 동작한다.
- **재현**: 중간. 오디오 모듈과 스피커 배선, 출력 방식에 맞춘 핀 설정이 필요하다.
- **제작**: e2002. [GitHub](https://github.com/e2002/yoradio), GPL-3.0.

### 19. ESP32 Weather EPD

날씨 예보와 실내 온습도를 전자종이에 표시하고, 갱신 사이에는 잠드는 날씨판이다.

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/19-weather-epd-photo.jpg" alt="나무 받침에 꽂힌 흑백 전자종이에 기온, 날씨 아이콘, 그래프가 표시돼 있다." loading="lazy">
<figcaption>나무 받침에 세운 7.5인치 전자종이. 현재 날씨, 며칠 치 예보, 실내 온습도, 시간별 그래프가 한 화면에 있다. 출처: <a href="https://github.com/lmarzen/esp32-weather-epd">esp32-weather-epd 저장소</a>, GPL-3.0</figcaption>
</figure>

Wi-Fi로 OpenWeatherMap의 날씨 데이터를 받아 7.5인치 800×480 전자종이에 현재 날씨, 며칠 치 예보, 시간별 그래프를 그린다. BME280 센서로 실내 온도, 습도, 기압을 잰다. 갱신을 마치면 딥슬립에 들어간다. README에 따르면 절전 중에는 약 14μA, 갱신하는 약 15초 동안은 약 83mA를 쓰고, 5000mAh 배터리로 30분마다 갱신하면 6개월에서 12개월을 쓴다.

- **ESP32의 역할**: Wi-Fi 접속, API 요청, 센서 측정, 화면 구성, 전자종이 갱신, 딥슬립. 예보는 OpenWeatherMap 서버에서 받는다.
- **부품**: FireBeetle 2 ESP32-E, 7.5인치 전자종이(권장은 Waveshare v2 흑백)와 DESPI-C02 어댑터, BME280, LiPo 배터리.
- **재현**: 중간. 헤더가 납땜된 보드와 점퍼선을 쓰면 납땜 없이 만들 수 있다. OpenWeatherMap One Call 3.0 API 키가 필요하다. 받침이나 케이스는 따로 준비한다.
- **제작**: Luke Marzen. [GitHub](https://github.com/lmarzen/esp32-weather-epd), GPL-3.0.

### 20. DIY ESP32 ePub Reader

전자종이 보드에서 EPUB 파일을 읽는 전자책이다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/6-64GMObw4s?start=40&amp;end=51&amp;rel=0" title="DIY e-Reader update - ported to the M5Paper" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>M5Paper에서 책 목록의 항목을 눌러 열고, 삽화가 있는 첫 페이지에서 다음 페이지로 넘긴다. 원본 영상의 0:40–0:51 구간만 재생된다. 영상: atomic14(제작자), <a href="https://www.youtube.com/watch?v=6-64GMObw4s&amp;t=40s">YouTube 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/20-epub-reader-photo.jpg" alt="전자종이 기기 세 대에 책 표지, 영어 본문과 삽화, 스페인어 본문과 사진이 각각 표시돼 있다." loading="lazy">
<figcaption>왼쪽부터 EPDIY V6, M5Paper, LilyGo EPD47에서 책을 표시한 모습. 출처: <a href="https://github.com/atomic14/diy-esp32-epub-reader">diy-esp32-epub-reader 저장소</a>, MIT</figcaption>
</figure>

EPUB 파일의 압축을 풀어 XHTML 본문을 읽고 전자종이에 한 페이지씩 그린다. 버튼이나 일부 보드의 터치로 책 목록과 페이지를 넘긴다. 제목, 문단, 목록, 굵게, 기울임 같은 기본 태그에 따른 자체 서식만 적용하고 CSS 파일은 해석하지 않는다. JPG와 PNG 이미지는 표시한다.

- **ESP32의 역할**: 압축 해제, 본문 해석, 페이지 배치, 화면 렌더링을 모두 처리한다. 책은 SD 카드에서 읽는다.
- **부품**: PSRAM이 있는 ESP32 전자종이 보드(M5Paper, LilyGo T5-4.7, EPDIY), SD 카드.
- **조건**: PSRAM이 필수다. 기본 폰트에는 라틴 문자와 문장부호만 들어 있어서, 한글 책을 읽으려면 폰트 데이터를 새로 만들고 렌더링을 확인해야 한다. 저장소는 2022년 11월 이후 갱신되지 않았다.
- **재현**: 높음. 저장소를 하위 모듈까지 받아 보드에 맞는 PlatformIO 환경으로 빌드하고, 일부 보드는 SD 카드와 버튼 배선이 따로 필요하다.
- **제작**: atomic14. [GitHub](https://github.com/atomic14/diy-esp32-epub-reader), MIT.

## 로봇, 카메라, 센서

모터 여러 개를 동시에 제어하거나 이미지 센서를 다루는 사례다. 부품 수가 많아서 제작 난도가 높은 편이다.

### 21. OpenCat ESP32

서보모터 여러 개를 조율해 걷는 사족보행 로봇의 펌웨어다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/GTgps_H990w?start=6&amp;end=16&amp;rel=0" title="Petoi Bittle driven by BiBoard V0 | ESP32 controller board | PetoiCamp" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>BiBoard 초기 시제품(V0)을 단 Bittle이 일어나 네 발을 번갈아 딛으며 걷는다. 원본 영상의 0:06–0:16 구간만 재생된다. 영상: Petoi(제작자), <a href="https://www.youtube.com/watch?v=GTgps_H990w&amp;t=6s">YouTube 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/21-opencat-biboard-photo.jpg" alt="검은 제어 보드 윗면에 ESP32 모듈과 흰색 커넥터 여러 개가 있다." loading="lazy">
<figcaption>BiBoard V1. ESP32 모듈과 서보 커넥터들이 있다. 출처: <a href="https://docs.petoi.com/biboard/biboard-v1-guide">Petoi 문서</a></figcaption>
</figure>

Petoi의 사족보행 로봇을 ESP32 기반 제어 보드 BiBoard로 구동하는 펌웨어다. 서보 동작, 보행 패턴, 자세 센서 입력을 처리한다. 현재 BiBoard를 쓰는 로봇은 개 모양의 Bittle X와 고양이 모양의 Nybble Q다. 구형 제어 보드 NyBoard는 ATmega328P 기반이며 별도 OpenCat 저장소를 쓴다.

- **ESP32의 역할**: BiBoard의 ESP32가 서보 출력과 자세 센서 입력을 처리한다. 기본 보행에 라즈베리 파이나 서버는 필요 없다. 카메라 인식이나 ROS 연동은 별도 장치를 연결해야 한다.
- **부품**: BiBoard(서보 소켓 최대 12개), Bittle X나 Nybble Q 기체와 서보, 배터리.
- **재현**: 높음. 펌웨어는 MIT로 공개돼 있지만 보드와 기체는 판매 키트다. 조립한 뒤 서보를 보정해야 한다.
- **제작**: Petoi(OpenCat 창안자 Rongzhong Li). [GitHub](https://github.com/PetoiCamp/OpenCatEsp32-Quadruped-Robot), MIT.

### 22. ESP-Drone

ESP32-S2를 비행 제어기로 쓰는 소형 쿼드콥터다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://player.bilibili.com/player.html?bvid=BV1ba4y1a7Vo&amp;t=345&amp;autoplay=0&amp;danmaku=0&amp;high_quality=1" title="【乐鑫 Demo】| 四旋翼 Wi-Fi 无人机 ESP-Drone 安装试飞，支持定点/定高/传感器/摄像头" loading="lazy" allow="fullscreen" allowfullscreen></iframe></div>
<figcaption>바닥에서 이륙해 스마트폰 조종 화면과 함께 공중을 이동한다. 재생하면 5:45부터 시작하며, 약 10초 동안이 해당 장면이다. 영상: 乐鑫(Espressif), <a href="https://www.bilibili.com/video/BV1ba4y1a7Vo?t=345">Bilibili 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/22-espdrone-photo.jpg" alt="왼쪽에 드론 메인 보드, 오른쪽에 모터와 프로펠러, 배터리를 조립한 소형 드론이 있다." loading="lazy">
<figcaption>ESP32-S2-Drone V1.2 보드와 조립을 마친 기체. 출처: <a href="https://github.com/espressif/esp-drone">esp-drone 저장소</a>, GPL-3.0</figcaption>
</figure>

Espressif가 공개한 소형 드론 프로젝트다. ESP32-S2 보드가 자세 센서를 읽어 모터 네 개의 출력을 조정한다. 스마트폰 앱이나 게임패드로 Wi-Fi를 통해 조종한다. 고도 유지와 위치 유지는 기압, 광류, 거리 센서가 달린 확장 보드를 연결해야 쓸 수 있다. 비행 제어 코드는 Crazyflie 펌웨어에서 파생했다.

- **ESP32의 역할**: 비행 제어 전부. 스마트폰은 조종 명령만 보낸다. PC용 cfclient는 설정과 디버깅에 쓴다.
- **부품**: ESP32-S2-Drone V1.2 보드(ESP32-S2-WROVER, MPU6050), 716 브러시드 모터 4개, 46mm 프로펠러 4개, 300mAh 1셀 LiPo.
- **조건**: ESP32-S2에는 블루투스가 없어서 조종은 Wi-Fi로만 한다. 현재 문서의 지원 칩은 ESP32-S2와 S3다. Espressif는 2022년 12월부터 이 프로젝트를 제한적으로만 지원한다고 밝혔다.
- **재현**: 높음. 공개된 회로와 PCB 자료로 보드를 주문하고 모터, 프로펠러, 배터리를 조립한 뒤 ESP-IDF로 빌드한다.
- **제작**: Espressif Systems. [GitHub](https://github.com/espressif/esp-drone), [문서](https://docs.espressif.com/projects/espressif-esp-drone/en/latest/), GPL-3.0.

### 23. ESP32-CAM_MJPEG2SD

움직임을 감지하면 SD 카드에 녹화하고, 브라우저로 영상을 보내는 카메라다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/YLLGBM3i2aQ?start=230&amp;end=240&amp;rel=0" title="ESP32-CAM_MJPEG2SD InBrowser Web Flash Install on ESP32-CAM" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>브라우저의 실시간 카메라 화면 앞에서 손을 움직인다. README가 연결한 기여자의 설치 영상이다. 원본 영상의 3:50–4:00 구간만 재생된다. 영상: Luberth Dijkman(기여자), <a href="https://www.youtube.com/watch?v=YLLGBM3i2aQ&amp;t=230s">YouTube 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/23-mjpeg-motion.png" alt="회색 카메라 영상 위에 움직인 영역이 붉은 점으로 칠해져 있다." loading="lazy">
<figcaption>카메라 기반 움직임 감지 화면. 변화가 감지된 영역이 붉은 픽셀로 표시된다. 출처: <a href="https://github.com/s60sc/ESP32-CAM_MJPEG2SD#motion-detection-by-camera">ESP32-CAM_MJPEG2SD 저장소</a>, AGPL-3.0</figcaption>
</figure>

ESP32 카메라 보드가 JPEG 프레임을 SD 카드에 AVI 파일로 기록하고, 브라우저에는 MJPEG로 실시간 전송하거나 녹화 파일을 재생해 준다. 화면 변화나 PIR 센서 신호로 녹화를 시작하며, 타임랩스와 연속 녹화도 지원한다. 마이크를 달면 WAV 파일을 함께 기록한다. 팬과 틸트는 서보를 따로 달고 설정을 켜야 한다.

- **ESP32의 역할**: 움직임 판정, 녹화, 웹 서버. FTP, Telegram, Home Assistant 연동은 선택 사항이다.
- **부품**: AI Thinker ESP32-CAM 또는 ESP32-S3 카메라 보드, OV2640 등 지원 카메라, microSD 카드.
- **조건**: PSRAM이 필요하다. README는 원형 ESP32의 메모리가 부족하다며, 기능을 더 쓰려면 ESP32-S3를 권한다. Arduino ESP32 코어 3.1.1 이상이 필요하다.
- **재현**: 중간. 보드 정의, PSRAM, 파티션 설정을 README대로 맞춰야 한다.
- **제작**: s60sc. [GitHub](https://github.com/s60sc/ESP32-CAM_MJPEG2SD), AGPL-3.0.

### 24. M5StickC 열화상 카메라

32×24 적외선 센서로 온도 분포를 색으로 보여 주는 소형 열화상 카메라다.

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/24-thermal-live-photo.jpg" alt="손에 든 주황색 M5StickC 위쪽에 흰 열화상 모듈이 달려 있고, 작은 화면에 얼굴의 열 분포가 색으로 나타난다." loading="lazy">
<figcaption>M5StickC에 Thermal HAT을 끼워 사람 얼굴을 비춘 모습. 화면에 열 분포와 온도 수치가 나온다. 출처: <a href="https://docs.m5stack.com/en/hat/hat-thermal">M5Stack 제품 문서</a></figcaption>
</figure>

M5StickC에 MLX90640 열화상 HAT을 끼우면 물체 표면 온도를 가로 32, 세로 24 지점에서 읽는다. ESP32가 온도값에 색을 입혀 내장 LCD에 그린다. 공식 예제는 화면에 표시할 때 보간을 적용하므로, 화면의 색 블록 수가 센서의 측정점 수와 같지 않다.

- **ESP32의 역할**: I2C로 센서를 읽고 온도를 계산해 화면에 그린다. PC는 예제를 올릴 때만 필요하다.
- **부품**: M5StickC 계열 기기, Thermal Camera HAT(U062).
- **재현**: 낮음. 납땜 없이 HAT을 끼우고 공식 예제를 올린다. 원형 M5StickC 본체는 단종됐고 HAT은 판매 중이다(2026년 9월 29일 기준). 현행 StickC 모델과의 호환은 따로 확인해야 한다.
- **제작**: M5Stack. [제품 문서](https://docs.m5stack.com/en/hat/hat-thermal), [예제 코드](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/MLX90640)(MIT).

## 전파와 무선 네트워크

무선으로 메시지나 관측 데이터를 주고받는 장치다.

### 25. Meshtastic

휴대전화망 없이 LoRa 무선으로 짧은 메시지를 주고받는 메시 네트워크다.

<figure class="esp-fig">
<div class="esp-embed"><iframe src="https://www.youtube-nocookie.com/embed/2Ry-ck0fhfw?start=272&amp;end=282&amp;rel=0" title="This device makes Meshtastic the BEST off-grid tech" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>
<figcaption>책상 위 T-Deck(ESP32-S3와 SX1262)의 Meshtastic 화면에 이어, 휴대전화 앱의 대화 화면과 다른 노드가 나온다. 원본 영상의 4:32–4:42 구간만 재생된다. 영상: Level 2 Jeff(제3자), <a href="https://www.youtube.com/watch?v=2Ry-ck0fhfw&amp;t=272s">YouTube 원본</a></figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/25-meshtastic-photo.jpg" alt="안테나가 달린 검은 기판의 작은 OLED에 노드 이름이 표시돼 있다." loading="lazy">
<figcaption>ESP32 기반 LILYGO T-Beam에 Meshtastic을 올린 모습. OLED에 노드 이름이 떠 있다. 출처: <a href="https://commons.wikimedia.org/wiki/File:Meshtastic_T-Beam.jpg">Chiffre01, Wikimedia Commons</a>, CC0 1.0</figcaption>
</figure>

각 노드가 LoRa(적은 양의 데이터를 먼 거리까지 보내는 저전력 무선 방식)로 짧은 메시지를 보내고 받으며, 다른 노드의 메시지를 중계한다. 휴대전화 앱은 블루투스나 Wi-Fi로 노드에 연결해 메시지를 쓰고 읽는다. 셀룰러망이나 인터넷 없이 가까운 노드끼리 통신할 수 있고, 도달 거리는 안테나, 지형, 출력, 지역 전파 규정에 따라 달라진다.

- **ESP32의 역할**: ESP32 보드의 펌웨어가 LoRa 무선칩, 화면, 휴대전화와의 BLE 연결을 제어한다. LoRa 송수신은 보드에 따로 달린 SX1262나 SX127x 칩이 담당한다.
- **조건**: 지원 기기에는 RAK4631, T-Echo처럼 nRF52840을 쓰는 기기도 섞여 있다. ESP32 계열로는 구형 T-Beam(ESP32), T-Beam S3와 Heltec LoRa32 V3(ESP32-S3) 등이 있다.
- **부품**: 지원 LoRa 보드 두 대 이상, 주파수에 맞는 안테나, 배터리.
- **재현**: 낮음. 완성 보드에 공식 웹 플래셔로 펌웨어를 올리고, 지역 주파수와 채널 설정을 맞춘다.
- **제작**: Meshtastic 커뮤니티. [문서](https://meshtastic.org/docs/introduction/), [펌웨어](https://github.com/meshtastic/firmware), GPL-3.0.

### 26. TinyGS

소형 위성과 고고도 기구의 전파를 받는 개인 지상국 네트워크다.

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/26-tinygs-dashboard.png" alt="수신국 상세 화면에 위성 패킷의 날짜, 시각, 수신 정보, 텔레메트리 행이 표로 나열돼 있다." loading="lazy">
<figcaption>TinyGS 웹 대시보드의 수신국 화면. 한 수신국이 받은 Norbi 위성 패킷이 시각, 수신 정보와 함께 나열된다. 출처: <a href="https://github.com/tinygs/tinyGS/wiki/Web-application">TinyGS 위키</a></figcaption>
</figure>

개인이 설치한 수신국이 호환되는 LoRa와 FSK 계열 신호를 받아 패킷을 TinyGS 네트워크에 올린다. README는 소형 위성, 기상 기구, 비행체를 수신 대상으로 적었다. 웹 대시보드에서 수신국별, 위성별 패킷 목록과 해독된 값을 볼 수 있다. 실제로 받을 수 있는지는 위성의 주파수와 변조 방식, 안테나, 설치 장소, 위성 통과 시각에 달려 있다.

- **ESP32의 역할**: SX126x나 SX127x 무선칩을 설정하고, 들어온 패킷을 Wi-Fi와 MQTT로 TinyGS 서버에 보낸다. 패킷 집계와 대시보드는 서버가 맡는다.
- **부품**: 지원 ESP32 LoRa 보드(Heltec WiFi LoRa32, TTGO LoRa32, T-Beam 등. Heltec V3는 ESP32-S3), 주파수에 맞는 안테나, Wi-Fi, TinyGS 계정.
- **재현**: 중간. 완성 보드를 쓰면 납땜은 필요 없지만, 위성별 무선 설정과 안테나 선택, 통과 시각에 맞춘 관측이 필요하다.
- **제작**: TinyGS 커뮤니티. [GitHub](https://github.com/tinygs/tinyGS), GPL-3.0.

### 27. ESP-CSI

Wi-Fi 신호의 채널 상태 변화로 사람의 움직임을 감지하는 Espressif 예제 모음이다.

<figure class="esp-fig">
<video controls preload="none" playsinline muted loop poster="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/27-esp-csi-clip.jpg">
  <source src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/27-esp-csi-clip.mp4" type="video/mp4">
  <a href="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/27-esp-csi-clip.mp4">영상 파일 열기</a>
</video>
<figcaption>ESP-Crab 기기에 손을 가까이 대자 원형 화면의 CSI 진폭 곡선이 바뀐다. 원본은 약 1초짜리 GIF이고 반복 재생된다. 출처: <a href="https://raw.githubusercontent.com/espressif/esp-csi/master/examples/esp-crab/doc/img/Self-Transmission%20and%20Reception%20Amplitude.gif">esp-csi 저장소</a>, Apache-2.0</figcaption>
</figure>

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/27-esp-csi-screen.png" alt="초록색 진폭 곡선 그래프와 상태 표시가 있는 GUI 화면." loading="lazy">
<figcaption>console_test의 PC 화면. CSI 진폭 곡선과 움직임 판정 상태가 표시된다. 캡처 시점의 판정은 움직임 없음이다. 출처: <a href="https://github.com/espressif/esp-csi/blob/master/examples/esp-radar/console_test/README.md">esp-csi 저장소</a>, Apache-2.0</figcaption>
</figure>

Wi-Fi 신호가 전달되는 동안 세기와 위상이 어떻게 변했는지 나타내는 채널 상태 정보(CSI)를 분석한다. 사람이 움직이면 전파가 반사되는 경로가 달라져 CSI도 바뀐다. console_test 예제는 방 안의 움직임과 재실 상태를 PC 화면에 표시하며, 설치 환경마다 보정이 필요하다. esp-crab 예제는 손을 기기에 가까이 댈 때 CSI 진폭 곡선이 바뀌는 모습을 기기 화면에 그린다.

- **ESP32의 역할**: Wi-Fi 패킷을 보내거나 받으며 CSI를 추출한다. console_test에서는 ESP32 한 대나 공유기가 신호를 보내고 다른 ESP32가 받으며, 시각화는 PC의 Python GUI가 한다.
- **조건**: 저장소의 지원 칩은 ESP32, S2, C3, S3, C5, C6, C61이다. 예제마다 요구하는 보드가 다르고, esp-crab은 ESP32-C5 기반 전용 PCB를 쓴다. console_test는 ESP-IDF 5.0 이상을 권한다.
- **재현**: 높음. 송수신 장치 배치와 방마다 다른 보정이 필요한 실험이다.
- **제작**: Espressif Systems. [GitHub](https://github.com/espressif/esp-csi), Apache-2.0.

### 28. OpenEPaperLink

전자가격표의 펌웨어를 바꿔, ESP32 허브에서 화면 내용을 무선으로 갱신하는 시스템이다.

<figure class="esp-fig">
<img src="https://img.seosoyoung.eiaserinnys.me/images/esp32-28-devices/28-openepaperlink-ap.jpg" alt="선으로 연결된 두 보드와 작은 OLED 화면에 AP 정보가 표시돼 있다." loading="lazy">
<figcaption>OpenEPaperLink AP. 두 보드를 연결했고, 작은 OLED에 IP 주소, 채널, 등록된 태그 수가 표시된다. 출처: <a href="https://openepaperlink.org/aps">openepaperlink.org</a></figcaption>
</figure>

호환 전자가격표에 새 펌웨어를 올린 뒤, 액세스 포인트(AP)의 웹 화면에서 이미지, 텍스트, QR 코드 같은 표시 내용을 정한다. AP가 무선으로 데이터를 보내면 태그가 전자종이 화면을 갱신한다. 지원 태그는 모델명 단위로 정해져 있어서 아무 전자가격표나 쓸 수는 없다. 공식 위키가 든 예는 ZBS 칩 기반 ST-GR16000과 ST-GR29000, nRF 칩 기반 EL029H3WRA 등이다.

- **ESP32의 역할**: AP의 ESP32-S3가 Wi-Fi 연결, 웹 화면, 태그 데이터 처리를 맡고, 함께 달린 ESP32-C6가 IEEE 802.15.4 무선으로 태그와 통신한다. 태그 안에는 ZBS243, nRF52811 같은 다른 칩이 들어 있다. 외부 클라우드는 필요 없다.
- **부품**: 지원 AP(ESP32-S3와 ESP32-C6 조합 등), 지원 모델 태그, 태그 플래싱용 지그와 프로그래머.
- **재현**: 높음. 태그를 분해해 지그로 펌웨어를 올려야 하고, AP 무선칩 조합을 태그 종류에 맞춰야 한다.
- **제작**: OpenEPaperLink 커뮤니티. [GitHub](https://github.com/OpenEPaperLink/OpenEPaperLink), CC BY-NC-SA 4.0(비상업 이용만 허용).

## 공통된 설계 패턴

**입출력은 ESP32가, 큰 계산은 다른 컴퓨터가 맡는다.** 대부분의 사례에서 ESP32는 센서와 버튼을 읽고 모터, LED, 화면, 스피커를 직접 구동한다. 음성 인식과 언어모델(Xiaozhi), 영상 변환(ESP32 TV)처럼 계산량이 큰 일은 서버나 PC가 처리한다. 신시사이저, 드론, SmartKnob처럼 칩 하나로 기능이 끝나는 장치도 많다.

**무선 연결을 입출력 장치처럼 쓴다.** 방탈출 소품은 ESP-NOW로 서로 상태를 주고받고, FreeTouchDeck은 BLE 키보드로 컴퓨터에 입력하고, AWTRIX NG와 ESPuino는 MQTT로 다른 시스템과 연결된다. LoRa 통신에는 별도 무선칩이 필요하다(Meshtastic, TinyGS).

**보드와 라이선스를 먼저 확인해야 한다.** 블루투스 Classic은 원형 ESP32에만 있어서 BlueRetro의 Classic 패드 연결과 ESPuino의 블루투스 스피커 출력은 ESP32-S3에서 쓸 수 없고, ESP32-S2에는 블루투스가 없다. PSRAM이 필수인 프로젝트(ESPuino, 카메라, 전자책)와 개발환경 버전을 고정한 프로젝트(FabGL, FreeTouchDeck, Xiaozhi)도 있다. 완제품(Stack-chan CoreS3, Ulanzi TC001, M5StickC와 열화상 HAT)으로 시작하면 난도가 낮아진다. AWTRIX NG, OpenEPaperLink, 신시사이저의 합성 라이브러리는 비상업 용도만 허용한다.

[^bt-classic]: Espressif, "Bluetooth Architecture Overview", ESP-IDF Programming Guide. ESP32는 Classic(BR/EDR)과 LE를 모두 지원하고, ESP32-S3와 C3 계열은 LE만 지원한다. https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/bt-architecture/overview.html
[^kspace]: Sabine Melanie Räuber, Marta Brigid Maggioni, Francesco Santini, "Lost in k-Space: An Open-Source MR-Physics Escape Room", arXiv:2608.09616, CC BY 4.0. https://arxiv.org/abs/2608.09616
