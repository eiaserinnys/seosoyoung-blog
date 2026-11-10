---
title: "Roguelike"
date: 2026-11-10T22:10:00+09:00
tags: ["게임 개발", "인디 게임", "Steam", "로그라이크"]
categories: ["게임"]
subjects: ["게임 개발과 디자인"]
summary: "1980년작 Rogue에서 이름을 딴 로그라이크 장르의 유즈넷 어원, 2008년 베를린 해석의 14개 기준, Moria와 Hack 양대 계보, 이상한 던전과 인디 로그라이트로의 확장을 정리한 위키백과 문서 요약."
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/01-rogue-screenshot.png"
  alt: "1980년 비디오 게임 Rogue의 절차적 생성 던전 화면. ASCII 기호로 방과 복도, 캐릭터(@)와 아이템이 표시되어 있다."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/01-rogue-screenshot.png"
---

## 3줄 요약

1. 위키백과의 「Roguelike」 항목은 1980년작 텍스트 롤플레잉 게임 *Rogue*에서 출발한 로그라이크 장르의 어원과 핵심 설계 규칙, 그리고 1975년부터 오늘날까지 이어진 개발 역사를 종합해 다룬다.
2. 2008년 국제 로그라이크 개발 콘퍼런스가 발표한 '베를린 해석'은 절차적 던전 생성, 영구적 죽음(permadeath), 턴제와 타일 기반 진행을 비롯한 고가치 요소 9개와 저가치 요소 5개로 전통적 로그라이크의 요건을 정리했다.
3. 고전 로그라이크는 *Angband*로 이어지는 *Moria* 계열과 *NetHack*으로 이어지는 *Hack* 계열을 중심으로 소스코드를 공개하며 발전했다. 이후 일본 콘솔 시장에서는 *이상한 던전* 시리즈가 나왔고, 서구 인디 게임계에서는 2008년 *Spelunky*를 계기로 로그라이트(roguelite)가 크게 유행했다.

## 명칭의 기원과 기본 개념

전통적인 로그라이크(roguelike)는 절차적으로 생성되는 던전을 탐험하는(dungeon crawl) 롤플레잉 비디오 게임으로, 격자(grid) 타일 위에서 턴제로 이동하며 캐릭터가 한 번 사망하면 영구히 소멸하는(permadeath) 규칙을 따른다. 대다수 작품은 테이블탑 롤플레잉 게임(TRPG) *Dungeons & Dragons*의 영향을 받아 하이 판타지 서사를 택한다.

1978년작 *Beneath Apple Manor*가 먼저 나왔지만, 장르의 이름과 표준 형식을 확립한 작품은 1980년 터미널에서 ASCII 문자 화면으로 실행된 *Rogue*다. 1980년대와 1990년대에 *Rogue*는 대학생과 프로그래머들 사이에서 큰 인기를 얻었고, 수백 종의 파생작이 뒤를 이었다. 대표적인 고전 파생작으로는 *Hack*, *NetHack*, *Ancient Domains of Mystery*(ADOM), *Moria*, *Angband*, *Tales of Maj'Eyal*(ToME), *Dungeon Crawl Stone Soup*(DCSS)가 있다. 일본 춘소프트(Chunsoft)가 제작한 *이상한 던전(Mystery Dungeon)* 시리즈도 로그라이크로 분류된다.

오늘날 널리 쓰이는 '로그라이크'라는 명칭은 1993년경 유즈넷(Usenet) 뉴스그룹 이용자들의 토론 과정에서 탄생했다. 당시 플레이어와 개발자들은 각 게임의 개별 뉴스그룹에서 소식을 알리고 소스코드를 공유했다. *Rogue*, *Hack*, *Moria*, *Angband*의 인기가 높아지자 공통 요소를 가진 게임들의 토론 창구를 하나의 상위 그룹으로 통합하자는 제안이 나왔다. 처음에는 `rec.games.dungeon.*`라는 이름이 거론되었다. 그러나 3주간의 토론 끝에 `rec.games.roguelike.*`가 "선택 가능한 대안 중 가장 나은 명칭(the least of all available evils)"으로 채택되었다.[^1] 당시 가장 오래된 작품으로 여겨진 *Rogue*의 이름을 딴 결정이었다. 이후 1998년 개발 전용 뉴스그룹 신설이 논의될 무렵에는 로그라이크라는 용어가 커뮤니티 전반에 완전히 정착했다.

| 시기 | 유즈넷 뉴스그룹 및 용어 정착 경과 |
|---|---|
| 1993년 이전 | *Rogue*, *Hack*, *Moria*, *Angband* 등 게임마다 별도 유즈넷 뉴스그룹에서 논의 및 소스코드 공유 진행 |
| 1993년경 | `rec.games.dungeon.*` 제안을 거쳐 3주간의 토론 끝에 상위 통합 그룹명 `rec.games.roguelike.*` 채택 |
| 1998년 | 로그라이크 개발 논의 그룹 신설 시점에 장르 일반 명사로 완전히 정착 |

[^1]: 이 과정은 1990년대 초반의 1인칭 슈팅 게임들이 한동안 '둠 클론(Doom clone)'으로 불리다가 점차 장르를 가리키는 일반 용어로 쓰이게 된 경로와 비슷하다.

## 게임플레이와 핵심 설계: 베를린 해석 (2008)

전통적인 로그라이크에서 플레이어는 직업(class)을 고르고 능력치와 기술을 배분해 캐릭터를 생성한 뒤, 기본적인 무기와 갑옷, 횃불, 식량만 가진 상태로 던전 첫 구역에서 출발한다. 플레이어는 전장의 안개(fog of war)로 가려진 미지의 던전을 탐험하며 몬스터와 싸우고 무기, 방어구, 마법 도구, 물약, 두루마리, 식량, 금화를 수집한다. 대부분의 근접 전투는 플레이어가 몬스터가 서 있는 인접 타일로 걸어 들어가면 즉시 공방 판정이 이루어지는 방식으로 진행된다. 활을 쏘거나 마법 주문을 쓸 수도 있다. 몬스터를 처치해 경험치를 얻으면 레벨이 오르지만, 체력(HP)을 모두 잃어 사망하면 캐릭터가 영구히 삭제되고 플레이어는 새 캐릭터로 처음부터 다시 시작해야 한다.

![](https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/02-nethack-vulture.jpg)
*로그라이크 게임 NetHack에 아이소메트릭 스프라이트 인터페이스 Vulture를 적용한 화면 (출처: Wikimedia Commons, GPL)*

2000년대 들어 *Rogue*의 변주작들이 새로운 규칙을 도입하거나 기존 원칙을 생략했고, 무엇을 진정한 로그라이크로 볼 것인가를 둘러싼 정의 논쟁이 벌어졌다. 이에 2008년 독일 베를린에서 국제 로그라이크 개발 콘퍼런스(International Roguelike Development Conference)가 개최되었다. 참가자들은 *ADOM*, *Angband*, *Linley's Dungeon Crawl*, *NetHack*, *Rogue*를 다섯 기준작(canon)으로 삼아 장르의 핵심 요소를 규정했고, 그 결과를 <strong>베를린 해석(Berlin Interpretation)</strong>으로 발표했다.[^2] 베를린 해석은 9개의 고가치(high-value) 요소와 5개의 저가치(low-value) 요소를 제시한다.

[^2]: 베를린 해석은 특정 요소가 하나라도 빠지면 로그라이크 자격을 박탈하거나, 조건을 갖췄다고 무조건 로그라이크로 판정하는 배타적 규칙이 아니었다. '얼마나 로그라이크다운가'를 가늠하는 척도로 고안된 기준이었다. *Game Set Watch*의 존 해리스(John Harris)가 이 기준으로 60점 만점 채점을 시도했을 때 *Linley's Dungeon Crawl*과 *NetHack*은 57.5점을 받았다. 흔히 비교 대상으로 꼽히던 *Diablo*와 *ToeJam & Earl*은 절반 정도의 점수에 그쳤다.

| 분류 | 평가 항목 | 세부 설계 내용 |
|---|---|---|
| 고가치 요소 (9개) | 무작위 환경 생성 | 재플레이 가치를 높이기 위해 개발자가 정한 절차적 생성 규칙으로 던전 구조와 아이템 외형을 매번 새로 생성한다. |
| 고가치 요소 | 영구적 죽음 (Permadeath) | 캐릭터가 사망하면 저장 파일이 삭제되어 새 판(run)을 시작해야 한다. 저장 기능은 플레이 일시 중단 용도로만 제공된다. |
| 고가치 요소 | 턴제 진행 (Turn-based) | 플레이어가 행동을 입력할 때만 게임 내 시간이 흐르고 몬스터나 독, 허기 상태가 반응한다. 판단에 시간 제한이 없다. |
| 고가치 요소 | 격자 기반 (Grid-based) | 모든 이동과 상호작용이 균일한 타일 격자 위에서 이루어지며, 전통적으로 ASCII 문자로 표현된다. |
| 고가치 요소 | 비모드성 (Non-modal) | 별도의 전투 화면이나 전용 창으로 전환되지 않고, 게임 내 어디서든 모든 행동을 동일한 화면에서 수행할 수 있다. |
| 고가치 요소 | 시스템 복잡도 | 다양한 시스템이 맞물려 창발적 플레이(emergent gameplay)를 만든다. 잠긴 문을 따거나, 부수거나, 태우거나, 벽을 파서 우회할 수 있다. |
| 고가치 요소 | 자원 관리 | 식량과 회복 수단이 제한되어 있다. 허기 시스템(stamina decay)이 '시계' 역할을 하여 한 구역에서 무한정 턴을 넘기며 체력을 회복하는 행위를 막는다. |
| 고가치 요소 | 핵 앤 슬래시 전투 | 평화적 해결책 없이 다수의 몬스터를 처치하는 전투가 진행의 중심이 된다. |
| 고가치 요소 | 탐험과 미식별 아이템 발견 | 판마다 던전 지도를 새로 밝히고, 효과가 무작위로 배정된 미식별 물약이나 두루마리의 용도를 직접 찾아내야 한다. |
| 저가치 요소 (5개) | 단일 캐릭터 조작 | 한 판이 끝날 때까지 플레이어 캐릭터 한 명만 조작한다. |
| 저가치 요소 | 몬스터의 대칭적 행동 | 몬스터도 플레이어와 마찬가지로 바닥의 아이템을 주워 장비하거나 마법 주문을 사용한다. |
| 저가치 요소 | 전술적 난관 | 여러 번 반복해서 플레이하며 생존 전술을 익혀야 하는 난관을 제공한다. |
| 저가치 요소 | 방과 복도 구조의 던전 | 자연 지형이나 야외 대신 방과 연결 복도로 구성된 던전을 탐험한다. |
| 저가치 요소 | 숫자 기반 상태 표시 | 캐릭터와 게임의 상태를 화면 인터페이스의 숫자로 표시한다. |

*Rogue* 개발자 마이클 토이(Michael Toy)는 플레이어를 괴롭히려는 의도라기보다, 선택마다 신중함을 요구해 몰입감을 높이려는 목적으로 영구적 죽음을 설계했다고 밝혔다. 초기 *Rogue*에 저장 기능을 넣자 플레이어들은 최상의 결과가 나올 때까지 저장 파일을 거듭 불러오는 이른바 '세이브 스커밍(save scumming)'을 되풀이했다. 개발진은 이를 막으려고 불러오는 즉시 저장 파일을 지우는 영구적 죽음 규칙을 확립했다. 또한 *NetHack* 커뮤니티에서 유명한 "개발팀은 모든 경우의 수를 생각한다(The Dev Team Thinks of Everything)"라는 격언은 시스템 복잡도를 잘 보여준다. 예를 들어 코카트리스(cockatrice)는 만지면 상대를 돌로 만든다. 그 시체를 무기처럼 휘둘러 적을 석화시키려면 플레이어는 자신이 돌로 변하지 않도록 반드시 장갑을 끼고 있어야 한다.

## 초기 텍스트 인터페이스와 로그라이트의 분화

대학 내 유닉스(UNIX) 메인프레임과 텍스트 터미널 환경에서 태동한 초기 로그라이크들은 별도의 그래픽 없이 ASCII나 ANSI 문자만으로 던전 지형과 생물을 화면에 그렸다. 플레이어 캐릭터는 "당신이 있는 곳(where you're at)"을 뜻하는 `@`로, 금화는 `$`로, 용(dragon)은 `D`로 표시하는 관례가 정착했다. 이후 컬러 텍스트가 도입되자 용의 종류도 색으로 구분했다. 불을 뿜는 적색 용은 빨간색 `D`로, 산성액을 뱉는 녹색 용은 초록색 `D`로 표시하는 식이다. 사회학자 마크 존슨(Mark R. Johnson)은 여러 로그라이크가 공유한 이 기호 체계를 두고, 텍스트 기호 자체를 미학적 형태로 삼아 향수를 불러일으키는 '기호학적 코드(semiotic codes)'라고 해석했다.

![](https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/03-nethack-ascii.png)
*ASCII 모드로 구동된 NetHack의 던전 화면. 방과 복도, 캐릭터(@)와 아이템이 텍스트 기호로 표현된다 (출처: Wikimedia Commons, NetHack GPL)*

개인용 컴퓨터와 콘솔의 그래픽 성능이 향상되면서, 고전 로그라이크에서 절차적 생성과 영구적 죽음만 빌려오고 타일 이동이나 턴제 전투는 실시간 액션과 플랫포머 등으로 바꾼 게임들이 활발히 제작되었다. 고전 로그라이크는 학습 곡선이 가파르고 플레이 시간이 끝없이 이어져 대중에게 팔기에는 불리했다. 이 때문에 새로운 작품들은 난이도를 완화하고 한 판의 길이를 줄여 입문 부담을 줄였다. 베를린 해석을 지지하는 기존 팬들은 실시간 액션이 전술적 깊이를 줄인다며, 로그라이크라는 용어가 희석되는 것을 경계했다. 이들은 이런 파생작을 구분하려고 **로그라이트(roguelite)**, **로그라이크-라이크(roguelike-like)**, 혹은 <strong>절차적 죽음의 미궁(procedural death labyrinth)</strong>이라는 명칭을 쓰기 시작했다.

| 비교 항목 | 전통적 로그라이크 (베를린 해석 기준) | 현대 로그라이트 (Roguelite) |
|---|---|---|
| 진행 및 이동 방식 | 턴제(step-based) 진행, 격자 타일 단위 이동 | 실시간 액션, 플랫포머, 슈팅, 덱빌딩 등 타 장르 결합 |
| 한 판(run)의 호흡 | 수십 시간에서 무기한까지 이어지는 긴 호흡 | 명확한 승리 조건을 갖춘 짧은 플레이 시간 |
| 사건의 예측 가능성 | 전 구간이 절차적 생성에 의존해 고정 이벤트가 적음 | 정해진 수의 바이옴(biome)과 구간별 고정 보스전 배치 |
| 영구 성장 (Metagame) | 죽음 시 모든 진행 초기화 (다음 판에 능력치 이월 없음) | 판마다 모은 자원으로 새 캐릭터나 아이템 해금 및 영구 강화 |
| 시드(Seed) 활용 | 판마다 무작위 시드 배정이 기본 | 고정 난수 시드를 공유하는 일일 챌린지 및 온라인 리더보드 활성화 |

![](https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/04-abyss-odyssey.jpg)
*로그라이크 요소와 벨트스크롤 액션(beat 'em up)을 결합한 Abyss Odyssey (출처: Wikimedia Commons, CC BY-SA 3.0)*

로그라이트의 확산과 함께 뚜렷한 하위 장르들도 형성되었다. 플랫포머와 결합한 *Spelunky*나 슈팅과 결합한 *The Binding of Isaac*, *Enter the Gungeon* 같은 **액션 로그라이크**가 대표적이다. 액션 로그라이크 중에서는 *Vampire Survivors* 계열의 미니멀리스트 슈팅 하위 장르도 생겨났다. 이 하위 장르에서 플레이어는 이동만 조작하고, 무작위 파워업을 조합해 몰려오는 적의 파도를 버텨낸다. 또 다른 주요 하위 장르로는 <strong>로그라이크 덱빌더(roguelike deck-builder)</strong>가 있다. 실물 카드 게임에서 영감을 받아 던전을 진행하는 동안 즉석에서 덱을 구성해 가는 방식이며, 2014년작 *Dream Quest*가 처음 선보였고 2017년작 *Slay the Spire*가 대중적 인기를 확립했다.

## 역사적 기원과 양대 계보 (1975–1995)

로그라이크는 1970년대 후반에 시작되었다. 취미 프로그래머와 해커들이 1975년작 텍스트 어드벤처 *Colossal Cave Adventure*와 TRPG *Dungeons & Dragons*를 메모리가 제한된 메인프레임과 초기 개인용 컴퓨터로 구현하려 한 것이 계기였다.[^3] 당시 컴퓨터에는 던전 전체를 담아 둘 메모리가 없었다. 이 한계를 우회하려고 절차적 생성이 도입되었고, 그것이 높은 재플레이 가치로 이어졌다.

[^3]: 초기 로그라이크 창작자들은 서로의 존재를 모른 채 독립적으로 게임을 개발했으며, 장르가 본격적으로 형성된 지 수년이 지나서야 다른 프로젝트들을 알게 된 경우가 많았다. 1975년 PLATO 시스템용으로 제작된 최초의 던전 크롤러 *pedit5*와 그 후속작들(*dnd*, *orthanc*, PLATO판 *Moria*(1978), *avatar*)도 무작위 몬스터 조우 등 일부 요소를 갖추고 있었다. 그러나 *Rogue* 개발진이 PLATO 시스템을 접했다는 증거는 확인되지 않았다.

| 연도 | 작품명 | 개발자 (플랫폼) | 역사적 의의와 주요 특징 |
|---|---|---|---|
| 1975 | *pedit5* | Rusty Rutherford (PLATO) | 최초의 던전 크롤러로 꼽히며 단일 고정 층에서 무작위 몬스터 조우를 구현했다. |
| 1978 | *Beneath Apple Manor* | Don Worth (Apple II) | 핵심 로그라이크 요소를 모두 갖춘 최초의 작품이자 최초의 상업용 로그라이크다. 수제 포장과 우편 주문으로 판매되어 대학 네트워크를 탄 *Rogue*만큼 널리 퍼지지는 못했다. |
| 1980 | *Rogue* | Michael Toy, Glenn Wichman (VAX-11/780) | 켄 아널드(Ken Arnold)의 `curses` 라이브러리를 활용해 터미널 화면에 텍스트 기반 무작위 모험을 구현했다. ARPANET 전파와 1984년 BSD UNIX v4.2 탑재를 통해 대학가에 폭발적으로 확산되었다. |
| 1982 | *Sword of Fargoal* | Jeff McCord (Commodore VIC-20, C64) | 1979년 *GammaQuest*로 개발을 시작해 Epyx를 통해 출시되었다. 1983년 PC 이식 당시 그래픽과 사운드 덕분에 *Rogue*의 상업용 PC판보다 높은 평가를 받았다. |

UC 산타크루즈 학생이던 글렌 위크먼(Glenn Wichman)과 마이클 토이는 텍스트 게임 *Star Trek*(1971)과 *Adventure*(1975)의 경험을 판마다 무작위로 달라지게 하려고 1980년 *Rogue*를 제작했다. 제작진은 던전을 만든 가상의 마법사 로드니(Rodney)의 철자를 거꾸로 뒤집어 '옌더(Yendor)'라 이름 붙이고, 플레이어가 던전 최하층에서 이 '옌더의 부적(Amulet of Yendor)'을 회수해 오는 이야기를 부여했다. 토이는 UC 버클리 컴퓨터 연구소에 취업해 `curses` 라이브러리 제작자인 켄 아널드를 만났고, 이때 코드 최적화와 기능 확장이 이루어졌다. *Rogue*는 유닉스의 창시자 켄 톰프슨(Ken Thompson)까지 즐겨 플레이할 만큼 인기를 끌었다. 데니스 리치(Dennis Ritchie)는 당시 *Rogue*를 두고 "역사상 가장 거대한 CPU 사이클 낭비"라고 농담을 남겼다.

<figure class="blog-diagram" style="margin: 2.2rem 0;">
<style>.blog-diagram .diagram-svg-desktop { display: block; width: 100%; height: auto; background: var(--bg-2); border: 1px solid var(--rule); } .blog-diagram .diagram-svg-mobile { display: none; width: 100%; height: auto; background: var(--bg-2); border: 1px solid var(--rule); } @media (max-width: 640px) { .blog-diagram .diagram-svg-desktop { display: none; } .blog-diagram .diagram-svg-mobile { display: block; } }</style>
<svg class="diagram-svg-desktop" viewBox="0 0 720 340" role="img" aria-label="Rogue(1980)에서 분기한 Hack 계열과 Moria 계열의 로그라이크 역사 계보도" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="340" fill="var(--bg-2)"/>
  <rect x="260" y="18" width="200" height="48" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="360" y="38" text-anchor="middle" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent)">Rogue (1980)</text>
  <text x="360" y="55" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">1986년 BSD v4.3까지 소스코드 미공개</text>
  <line x1="310" y1="66" x2="180" y2="96" stroke="var(--ink-2)" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#arr-ink)"/>
  <line x1="410" y1="66" x2="540" y2="96" stroke="var(--ink-2)" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#arr-ink)"/>
  <rect x="40" y="100" width="280" height="220" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="56" y="122" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">1. Hack 계열 (D&amp;D 규칙과 상호작용 확장)</text>
  <rect x="60" y="134" width="240" height="40" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="74" y="152" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">Hack (1982)</text>
  <text x="74" y="167" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">층 구조 보존, USENIX 테이프로 소스 배포</text>
  <line x1="180" y1="174" x2="180" y2="192" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="60" y="196" width="240" height="44" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="74" y="214" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">NetHack (1987)</text>
  <text x="74" y="230" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">유즈넷 DevTeam 협업, 분기 던전과 다중 신화</text>
  <line x1="180" y1="240" x2="180" y2="258" stroke="var(--ink-2)" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#arr-ink)"/>
  <rect x="60" y="262" width="240" height="42" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="74" y="280" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">ADOM (1994)</text>
  <text x="74" y="295" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">영감 기반 자체 개발, 오버월드와 퀘스트 중심</text>
  <rect x="400" y="100" width="280" height="220" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="416" y="122" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2. Moria 계열 (톨킨 세계관, 고정 마을과 보스)</text>
  <rect x="420" y="134" width="240" height="40" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="434" y="152" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">Moria (1983) → UMoria (1988)</text>
  <text x="434" y="167" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">고정 상점 마을, 발로그 보스전, UNIX 이식</text>
  <line x1="540" y1="174" x2="540" y2="192" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="420" y="196" width="240" height="44" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="434" y="214" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">Angband (1990)</text>
  <text x="434" y="230" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">모르고스 최종 보스, 60종 이상의 소스 포크 파생</text>
  <line x1="540" y1="240" x2="540" y2="258" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc)"/>
  <rect x="420" y="262" width="240" height="42" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="434" y="280" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">ZAngband (1994) → ToME (2009)</text>
  <text x="434" y="295" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">앰버 연대기 테마 변주 후 독자 판타지 세계관</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 510" role="img" aria-label="Rogue(1980)에서 분기한 Hack 계열과 Moria 계열의 로그라이크 역사 계보도 (모바일)" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arr-ink-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="arr-acc-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="510" fill="var(--bg-2)"/>
  <rect x="16" y="14" width="318" height="44" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="175" y="33" text-anchor="middle" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent)">Rogue (1980)</text>
  <text x="175" y="49" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">1986년 BSD v4.3까지 소스코드 미공개</text>
  <rect x="16" y="72" width="318" height="204" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="28" y="92" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">1. Hack 계열 (D&amp;D 규칙과 상호작용 확장)</text>
  <rect x="28" y="102" width="294" height="40" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="40" y="120" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">Hack (1982)</text>
  <text x="40" y="135" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">층 구조 보존, USENIX 테이프로 소스 배포</text>
  <line x1="175" y1="142" x2="175" y2="158" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="28" y="162" width="294" height="42" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="40" y="180" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">NetHack (1987)</text>
  <text x="40" y="195" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">유즈넷 DevTeam 협업, 분기 던전과 다중 신화</text>
  <line x1="175" y1="204" x2="175" y2="220" stroke="var(--ink-2)" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#arr-ink-m)"/>
  <rect x="28" y="224" width="294" height="40" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="40" y="242" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">ADOM (1994)</text>
  <text x="40" y="257" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">영감 기반 자체 개발, 오버월드와 퀘스트 중심</text>
  <rect x="16" y="290" width="318" height="204" fill="var(--bg-2)" stroke="var(--rule)" stroke-width="1"/>
  <text x="28" y="310" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">2. Moria 계열 (톨킨 세계관, 고정 마을과 보스)</text>
  <rect x="28" y="320" width="294" height="40" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="40" y="338" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">Moria (1983) → UMoria (1988)</text>
  <text x="40" y="353" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">고정 상점 마을, 발로그 보스전, UNIX 이식</text>
  <line x1="175" y1="360" x2="175" y2="376" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="28" y="380" width="294" height="42" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="40" y="398" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">Angband (1990)</text>
  <text x="40" y="413" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">모르고스 최종 보스, 60종 이상의 소스 포크 파생</text>
  <line x1="175" y1="422" x2="175" y2="438" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#arr-acc-m)"/>
  <rect x="28" y="442" width="294" height="40" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="40" y="460" font-family="var(--sans)" font-size="12" font-weight="700" fill="var(--ink)">ZAngband (1994) → ToME (2009)</text>
  <text x="40" y="475" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">앰버 연대기 테마 변주 후 독자 판타지 세계관</text>
</svg>
<figcaption style="margin-top: 0.65rem; font-size: 0.85rem; color: var(--ink-2); text-align: center; line-height: 1.5;">Rogue(1980) 이후 주요 고전 로그라이크 계보. 점선은 영감을 받아 새로 작성한 작품, 실선은 부모 게임의 소스코드를 직접 포크해 발전시킨 작품을 뜻한다.</figcaption>
</figure>

*Rogue*의 제작진은 상업화를 염두에 두고 1986년 BSD v4.3 배포 전까지 소스코드를 공개하지 않았다. 이 때문에 초기 추종자들은 *Rogue*를 본뜬 게임을 처음부터 직접 코딩했고, 그 소스코드는 공개했다. 이후 고전 로그라이크는 크게 *Moria* 계열과 *Hack* 계열이라는 두 갈래로 발전했다.

첫째, **Moria 계열**은 1983년 오클라호마 대학교 학생 로버트 앨런 코네키(Robert Alan Koeneke)가 VAX-11/780에서 파스칼(Pascal) 언어로 작성한 *Moria*에서 시작되었다. 톨킨(J. R. R. Tolkien)의 중간계 소설 속 미궁 모리아를 배경으로 삼아 지하 깊은 곳의 발로그(Balrog)를 물리치는 보스전 개념을 도입했고, 던전 맨 위 구역에 장비를 사고팔 수 있는 고정된 마을을 두었다. 이전 구역으로 되돌아가면 던전이 새로 생성되는 구조는 *Rogue*와 같았다. 이후 짐 윌슨(Jim E. Wilson)이 유닉스로 이식한 *UMoria*가 나왔고, 1990년에는 워릭 대학교의 알렉스 커틀러(Alex Cutler)와 앤디 애스트랜드(Andy Astrand)가 모르고스(Morgoth)의 요새를 배경으로 설정한 *Angband*를 개발했다. *Angband*는 유즈넷에 공개된 뒤 관리 주체가 여러 차례 바뀌는 동안 60종 이상의 포크(fork) 변종을 낳았다. 대표적 포크인 *ZAngband*(1994)는 로저 젤라즈니의 『앰버 연대기』를 테마로 삼은 작품이다. 이 코드베이스는 *Troubles of Middle Earth*(2002)를 거쳐 독자적인 세계관을 갖춘 *Tales of Maj'Eyal*(2009)로 이어졌다.

![](https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/05-angband-town.png)
*Moria와 그 후속작인 Angband는 플레이어가 장비를 거래할 수 있는 고정된 지상 마을 구역을 도입했다 (출처: Wikimedia Commons, GPL)*

둘째, **Hack 계열**은 1982년 링컨-서드베리 고등학교 학생 제이 펜러슨(Jay Fenlason)과 친구들이 교사 브라이언 하비(Brian Harvey)의 컴퓨터 수업 프로젝트로 만든 *Hack*에서 출발했다. 이들은 UC 버클리 연구소를 방문했을 때 접한 *Rogue*를 개선하고 싶어 USENIX 콘퍼런스에서 토이와 아널드에게 소스코드를 요청했지만 거절당했다. 이에 처음부터 코드를 직접 작성했고, 플레이어가 구역을 옮겨 가도 이전 구역의 지형이 그대로 보존되는 기능 등을 담았다. 1987년에는 마이크 스티븐슨(Mike Stephenson), 펜실베이니아 대학교 철학과 교수 이츠하크 밀러(Izchak Miller), 재닛 월즈(Janet Walz)가 'DevTeam'을 결성했다. 이들은 USENIX 디지털 테이프로 배포된 *Hack*의 소스코드를 이어받아 유즈넷 협업으로 *NetHack*을 만들었다. *NetHack*은 시대착오적 유머와 다양한 신화를 결합했다. 테리 프래쳇의 『디스크월드』에서 따온, 플래시 카메라를 든 관광객(Tourist) 직업이 그 대표적인 예다. 던전 분기 경로와 캐릭터별 퀘스트도 추가했다. 1994년에는 도르트문트 공과대학교 학생 토마스 비스쿠프(Thomas Biskup)가 *ADOM*을 발표했다. *ADOM*은 *NetHack*의 산만함을 줄이고 서사적 응집력을 높이려고 처음부터 새로 코딩한 작품이며, 오버월드 지도와 카오스 오염(돌연변이) 시스템을 정립했다.[^4]

[^4]: *Moria*나 *Hack* 계보에 속하지 않는 독자 변종들도 중요한 설계 유산을 남겼다. 노아 모건(Noah Morgan)의 *Larn*(1986)은 제한된 턴 수 이내에 목표를 달성해 한 번의 플레이로 끝내도록 설계되었고, 로렌스 브라더스(Laurence Brothers)의 *Omega*(1980년대 후반)는 *ADOM*보다 앞서 오버월드 개념을 처음 도입했다. 린리 헨젤(Linley Henzell)이 1995년에 발표한 *Linley's Dungeon Crawl*은 무기 숙련도나 함정 탐지 같은 능력을 하나씩 올리는 스킬 기반 성장 시스템을 선보였다. 이 작품의 포크는 현대 정통 로그라이크의 대표 주자인 *Dungeon Crawl Stone Soup*(2006)의 기반이 되었다.

![](https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/06-nethack-town.png)
*강(파란색 타일)과 건물들이 배치된 NetHack의 고정 구역에서 지니(djinni)가 소원을 들어주는 장면 (출처: Wikimedia Commons, NetHack GPL)*

## 콘솔 이식과 현대 인디 붐 (1993–현재)

1993년까지 컴퓨터 전용 장르였던 로그라이크를 가정용 콘솔 시장에 정착시킨 주역은 일본의 춘소프트였다. 나카무라 고이치(Koichi Nakamura)와 개발진은 *드래곤 퀘스트* 시리즈로 서구 컴퓨터 RPG의 문법을 일본 콘솔 이용자의 눈높이에 맞게 바꾸어 성공을 거둔 바 있다. 이들은 *Rogue*도 "더 이해하기 쉽고 콘솔에서 편하게 즐길 수 있는 버전"으로 재해석할 수 있다고 판단했다. 이렇게 탄생한 첫 작품이 1993년작 *토리네코의 대모험: 이상한 던전*이다. 춘소프트는 친숙한 *드래곤 퀘스트 4*의 상인 캐릭터 토리네코와 스토리를 도입하고, 난이도가 점진적으로 올라가는 던전과 창고에 아이템을 보관하는 시스템을 더해 영구적 죽음의 가혹함을 완화했다. 이어 1995년 독자 세계관으로 출시한 *풍래의 시렌*이 큰 호평을 받았다. 춘소프트는 이후 *초코보*, *포켓몬 불가사의 던전*, *세계수의 미궁* 크로스오버 등 25편 이상의 *이상한 던전* 시리즈를 제작하며 이 장르를 일본 게임 시장의 주류로 만들었다.

![](https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/07-dcss.png)
*미니맵과 상시 인벤토리 창 등 현대적인 사용자 인터페이스를 결합한 정통 로그라이크 Dungeon Crawl Stone Soup (출처: Wikimedia Commons, GPL)*

서구권에서도 고전 로그라이크의 영향력은 그래픽 시대의 새로운 장르들로 이어졌다. 블리자드의 데이비드 브레빅(David Brevik)은 *Rogue*, *NetHack*, *Telengard*의 무작위 던전 및 전리품 생성 구조에서 영감을 받아 액션 RPG *Diablo*(1996)를 설계했다. 타일 기반 ASCII 인터페이스는 개발 효율이 높아 다른 장르와 결합한 시도도 활발했다. 건설 및 경영 시뮬레이션에 로그라이크 인터페이스를 결합한 *Dwarf Fortress*(2006)는 후일 *Minecraft*에 큰 영감을 주었고, 생존 게임 장르의 선구자로 꼽히는 *UnReal World*(1992)도 이 흐름에 속한다. 또한 2005년 유즈넷에서 시작된 '7일 로그라이크 챌린지(7DRL)'에서 파생된, 짧은 시간에 한 판을 끝낼 수 있는 '커피브레이크 로그라이크'(*DoomRL*, *Desktop Dungeons* 등)도 꾸준히 만들어졌다.

![](https://img.seosoyoung.eiaserinnys.me/images/roguelike-wikipedia/08-crawl-2014.png)
*최대 4명의 플레이어가 인간 영웅과 던전 몬스터 역할을 번갈아 맡으며 협동과 경쟁을 함께 수행하는 브롤러 로그라이트 Crawl (출처: Wikimedia Commons, CC BY-SA 3.0)*

2000년대 들어 서구 인디 게임계가 로그라이트의 폭발적 성장을 주도했다. 그 조짐은 개발사 Digital Eel(디지털 일)의 단편 우주 탐험 게임 *Strange Adventures in Infinite Space*(2002)와 후속작 *Weird Worlds*(2005)에서 먼저 나타났고, 2008년 데렉 유(Derek Yu)가 출시한 *Spelunky*를 기점으로 본격화되었다. 데렉 유는 고전 로그라이크의 깊이 있는 창발적 게임플레이에 플랫포머의 즉각적인 조작감을 결합했다. 이 접근법은 에드먼드 맥밀런(Edmund McMillen)의 *The Binding of Isaac*(2011), 리 형제의 *Rogue Legacy*(2012), 저스틴 마(Justin Ma)와 매튜 데이비스(Matthew Davis)의 *FTL: Faster Than Light*(2012)의 직접적인 설계 모델이 되었다.

| 출시 연도 | 작품명 | 결합한 장르 및 핵심 메커니즘 |
|---|---|---|
| 2008 | *Spelunky* | 플랫포머 액션에 영구적 죽음과 절차적 동굴 생성을 결합해 인디 로그라이트 붐을 촉발했다. |
| 2011 | *The Binding of Isaac* | 탑다운 슈팅 액션에 수백 종의 아이템 시너지 조합을 접목했다. |
| 2012 | *FTL: Faster Than Light* | 우주선 실시간 전술 시뮬레이션에 섹터 단위 절차적 사건 탐색을 접목했다. |
| 2012 | *Rogue Legacy* | 가문 대물림 시스템을 통해 이전 판에서 모은 금화로 성채와 후손의 능력치를 영구 강화하는 메타게임을 정착시켰다. |
| 2015 | *Crypt of the NecroDancer* | 리듬 게임의 박자 판정에 맞춰 타일 위를 이동하고 공격하는 방식을 도입했다. |
| 2017 | *Slay the Spire* | 로그라이크 경로 선택과 즉석 덱빌딩 카드 전투를 결합해 덱빌더 하위 장르를 대중화했다. |
| 2018 | *Dead Cells* | 메트로배니아 스타일의 2D 탐색형 플랫포머 액션에 로그라이트 반복 진행을 접목했다. |
| 2020 | *Hades* | 핵 앤 슬래시 액션 RPG에 사망 후 귀환할 때마다 진행되는 비선형 서사를 결합해 서사 중심 이용자층까지 흡수했다. |
| 2022 | *Vampire Survivors* | 이동만 조작하면 공격은 자동으로 나가며 무작위 무기를 조합하는 미니멀리스트 탄막 생존 슈팅을 확립했다. |
| 2024 | *Balatro* | 포커 족보 규칙과 조커 카드의 배수 시너지를 결합한 점수 어택형 덱빌딩 로그라이크다. |
| 2025 | *Blue Prince* | 날마다 방 배치가 바뀌는 저택을 설계하며 미스터리를 푸는 퍼즐 어드벤처와 로그라이크를 결합했다. |

개발자 파비앙 피셔(Fabien Fischer)는 대형(AAA) 게임사들이 양산한 표면적 볼거리와 스키너 상자(Skinner Box)식 보상 설계에 지친 이용자들이 인디 로그라이트로 눈을 돌렸다고 진단했다. 동시에 절차적 세계 생성은 현실적인 제작 해법이기도 했다. 소규모 인디 개발팀은 방대한 수작업 레벨 디자인에 자원을 쏟지 않고도 수백 시간 분량의 역동적인 플레이 경험을 만들 수 있었다. 커뮤니티의 교류도 활발하다. 매년 130편 이상의 신작이 출품되는 7DRL 챌린지와 2016년 샌프란시스코에서 시작된 연례 콘퍼런스 '로그라이크 셀러브레이션(Roguelike Celebration)'을 중심으로 고전과 현대를 아우르는 개발자 및 팬들의 교류가 이어지고 있다.

## 가장 흥미로운 지점

내가 이 문서에서 가장 흥미롭게 읽은 부분은 로그라이크의 두 핵심 요소, 곧 '절차적 생성'과 '영구적 죽음'의 유래를 다룬 기록이다. 둘 다 처음부터 거창한 장르 미학으로 기획되지는 않았다. 1970년대 말과 1980년대 초의 메인프레임과 초기 PC는 메모리가 비좁아 던전 전체를 저장해 둘 수 없었다. 개발자들은 이전 구역을 메모리에서 지우고 새 구역을 즉석에서 만들어 내는 방식으로 이 하드웨어 제약을 우회했다. 영구적 죽음 역시 사후 처방이었다. 저장 기능을 넣었더니 플레이어들이 원하는 결과가 나올 때까지 불러오기를 반복했고, 개발진은 선택 하나하나에 긴장감을 되살리려고 이 규칙을 도입했다.

또 하나 인상적인 점은 소스코드 공개 여부가 장르의 진화 경로를 좌우한 과정이다. *Rogue*의 원작자들이 상업화를 위해 1986년까지 소스코드를 잠가 두자, 이에 자극받은 대학생과 고등학생들은 오히려 처음부터 자기만의 코드를 짜서 *Moria*와 *Hack*을 만들고 유즈넷과 디지털 테이프로 소스코드를 공개했다. 만약 *Rogue*가 처음부터 소스코드를 공개했더라면 장르는 단일 코드베이스를 부분 수정하는 데 그쳤을지도 모른다. 소스 비공개라는 제약 덕분에 장르는 서로 다른 두 개의 아키텍처와 60종 이상의 포크 생태계로 확장된 셈이다. 오늘날 로그라이트는 *Balatro*나 *Blue Prince*처럼 포커와 건축 퍼즐까지 결합하며 변주를 거듭한다. 규칙과 시스템의 조합만으로 매번 새로운 플레이 경험을 만들려 한 초기 해커들의 시도가 오늘날의 신작들에서도 그대로 이어지고 있다.

## 출처

Wikipedia contributors, "Roguelike," *Wikipedia, The Free Encyclopedia*.
원문: <https://en.wikipedia.org/wiki/Roguelike>
