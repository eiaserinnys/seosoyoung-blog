---
title: "Far Far West, 세 번의 프로토타입에서 얼리 액세스까지"
date: 2026-09-12T12:30:00+09:00
tags: ["Steam", "인디 게임", "게임 개발", "Unreal Engine"]
categories: ["게임"]
summary: "프랑스 리옹의 8인 스튜디오 Evil Raptor는 3D 플랫포머 두 편을 만든 뒤 처음으로 협동 FPS 「Far Far West」를 만들었다. 개발자 인터뷰, Steam 공지 50건, 공식 Bluesky 게시물, Epic의 Inside Unreal 방송을 바탕으로 그 개발 과정을 다시 이었다. 타워 디펜스와 선형 미션을 거쳐 지금의 반복 플레이 구조에 이른 경위, 로봇과 떠 있는 손을 택한 이유, 세 차례의 공개 테스트, 출시 첫 주의 네트워크 문제, 이후 넉 달의 정비를 날짜순으로 정리했다."
ShowToc: true
TocOpen: false
sidenotes: true
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/01-robot-cowboy-concepts.jpg"
  alt: "Far Far West 로봇 카우보이의 초기 콘셉트 스케치 모음. 모자를 쓴 로봇의 머리, 몸통, 손 모양을 여러 갈래로 그려 두었다. 2025년 7월 4일 공식 Bluesky 게시물."
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/01-robot-cowboy-concepts.jpg"
---

## 3줄 요약

1. 프랑스 리옹에 있는 여덟 명의 스튜디오 Evil Raptor가 「Far Far West」라는 협동 FPS를 만들었다. 혼자서도, 최대 네 명이서도 플레이할 수 있다. 이 팀은 그 전까지 「Pumpkin Jack」(2020)과 「Akimbot」(2024)이라는 3D 플랫포머만 만들어 왔고, 2026년 4월 28일에 이 게임을 Steam 얼리 액세스로 내놓았다.
2. 지금의 반복 플레이 구조는 세 번째 시도였다. 그 앞에는 타워 디펜스 프로토타입과 Left 4 Dead와 비슷한 선형 미션 구조가 있었다. 애니메이션 제작 부담을 줄이기 위해 로봇 카우보이와 몸통에서 분리된 채 떠 있는 손을 택했다. 초기 테스트에서 총격만으로는 부족하다고 판단한 뒤에 마법을 더했다.
3. 2025년 6월에 처음 공개한 뒤 출시 전까지 공개 플레이테스트 두 번과 데모 한 번을 진행했다. 출시 뒤에는 네트워크 제공사의 DDoS(디도스) 방어 오작동과 세이브 손상, 수천 건의 버그 보고를 처리했다. 그 과정에서 팀을 늘리고 작업 방식도 고쳤으며, 8월 27일의 첫 대형 업데이트와 함께 공개 로드맵을 내놓았다.

## 플랫포머를 만들던 여덟 사람

Evil Raptor의 출발점은 Nicolas Meyssonnier가 혼자 만든 「Pumpkin Jack」이었다. 그는 PC Gamer 인터뷰에서 게임을 만들게 된 계기를 "구글에 '게임 만드는 법'이라고 쳤다"고 설명했고, Screen Rant에는 그 게임을 만들던 때가 스무 살 무렵이었다고 말했다.[^pcg-apr][^sr] 「Pumpkin Jack」은 2020년 10월 23일 Headup Games를 통해 나왔고, 스튜디오는 그 성과를 발판으로 2020년 리옹에 법인을 세웠다.[^afjv] 이어서 만든 「Akimbot」은 PLAION이 퍼블리싱해 2024년 8월 29일에 출시됐다.[^moby]

「Far Far West」의 팀이 어떻게 구성됐는지는 개발자 Arnaud Petit가 GamesRadar+에 설명했다. 그는 "지금 팀의 대부분은 이미 「Akimbot」에서 함께 일했고, 「Far Far West」로 넘어온 것은 그룹으로서 하던 일의 자연스러운 연장이었으며, 게임을 최대한 좋게 만들기 위해 몇 사람을 새로 더했다"고 말했다.[^gr] 팀 규모는 여러 곳에서 "8명"으로 소개된다. Steam 상점의 얼리 액세스 안내문, 퍼블리셔 보도자료의 스튜디오 소개문, 그리고 Meyssonnier 본인의 인터뷰가 모두 같은 숫자를 쓰는데, 시점은 모두 2026년 4월과 5월의 출시 전후다.[^steam-store][^sr] 그 뒤 팀은 더 커졌다. 7월 개발일지는 두 사람의 합류를, 9월 개발일지는 한 사람의 합류를 더 알렸고, 8월 21일 공지는 "팀을 확장하고 있다"고 적었다.[^devlog-jul][^devlog-sep][^frost-coming] 출시 시점의 8명이 정직원만을 뜻하는지, 외주 인력을 포함하는지는 공개된 자료에 나오지 않는다.

역할은 개발일지에 닉네임으로만 드문드문 나온다. Meyssonnier는 스튜디오 대표이면서 기술 디렉터를 겸한다고 스스로 밝혔다.[^sr] 5월 개발일지에서는 "Captain Spinker"라는 필자가 Mylan을 "두 번째 개발자"라고 불렀다. 그는 두 사람이 출시 직후의 치명적인 버그를 며칠 만에 고쳤다고 썼다. 문맥상 이 필자는 기술 디렉터 Meyssonnier로 보이지만, 개발일지에는 실명이 나오지 않는다.[^devlog-may] Petit는 PC Gamer에서 "handyman"으로 소개됐다. 5월 개발일지는 "Arno가 하루 종일 피드백을 읽고 메모하고 균형을 찾는 일로 바쁘다"고 적었고, 9월 개발일지는 그가 "Arno"라는 이름으로 직접 쓰면서 다음 업데이트의 게임 디자인을 맡고 있다고 밝혔다.[^pcg-apr][^devlog-may][^devlog-sep] 공식 사이트에는 Meyssonnier와 함께 공동 아트 디렉터 Adrian Long의 이름이 올라 있다.[^site] 개발일지의 크레디트에 따르면 콘셉트와 3D 모델은 Capp과 MashArt가, 레벨 디자인은 Promium이, 레벨 아트는 Erton과 Borealis가, 애니메이션은 Calu가 맡았다.[^devlog-jul][^devlog-sep] 작곡가는 「Akimbot」의 OST를 만든 같은 사람이라고 Petit가 말했지만, 어느 인터뷰에도 이름은 나오지 않았다.[^gr]

## 연표

<style>
.post-content ol.tl{list-style:none;margin:1.5rem 0 1rem;padding:0 0 0 1.6rem;padding-inline-start:1.6rem;border-left:2px solid var(--secondary,#999);position:relative}
.post-content ol.tl li{position:relative;margin:0 0 1.5rem;padding-left:.5rem;padding-inline-start:.5rem}
.post-content ol.tl li::before{content:"";position:absolute;left:calc(-1.6rem - 8px);top:.35em;width:10px;height:10px;border-radius:50%;background:var(--primary,#333);border:2px solid var(--theme,#fff);box-sizing:content-box}
.post-content ol.tl .tl-date{font-size:.82em;color:var(--secondary,#777)}
.post-content ol.tl .tl-tag{display:inline-block;font-size:.72em;line-height:1.4;padding:0 .55em;border:1px solid var(--border,#ccc);border-radius:999px;margin-left:.45em;color:var(--secondary,#777);vertical-align:middle}
.post-content ol.tl .tl-title{font-weight:600;margin:.15em 0 .1em;line-height:1.45}
.post-content ol.tl .tl-metric{font-size:.9em;margin:0 0 .15em;line-height:1.5}
.post-content ol.tl .tl-src{font-size:.78em;color:var(--secondary,#777)}
.post-content ol.tl .tl-src a{color:inherit;text-decoration:underline;text-decoration-thickness:.5px;text-underline-offset:2px}
.post-content .tl-note{font-size:.8em;color:var(--secondary,#777);margin:0 0 2rem}
</style>
<ol class="tl">
<li><div class="tl-date">2020년 10월 23일 <span class="tl-tag">전작</span></div><div class="tl-title">「Pumpkin Jack」 출시</div><div class="tl-metric">Meyssonnier가 혼자 만든 3D 플랫포머. 퍼블리셔는 Headup Games였다. 이 성과로 2020년 리옹에 Evil Raptor를 세웠다.</div><div class="tl-src"><a href="https://www.mobygames.com/company/61705/evil-raptor/">MobyGames</a> / <a href="https://www.afjv.com/societe/1232-evil-raptor.htm">AFJV 기업 정보</a></div></li>
<li><div class="tl-date">2024년 8월 29일 <span class="tl-tag">전작</span></div><div class="tl-title">「Akimbot」 출시</div><div class="tl-metric">팀으로 만든 첫 게임. 퍼블리셔는 PLAION. 지금 팀의 대부분이 이 게임에서 함께 일했다.</div><div class="tl-src"><a href="https://www.mobygames.com/company/61705/evil-raptor/">MobyGames</a> / <a href="https://www.gamesradar.com/games/co-op/far-far-west-developer-q-and-a-like-with-pretty-much-everything-we-do-we-just-went-with-a-vibe/">GamesRadar+</a></div></li>
<li><div class="tl-date">2025년 초 <span class="tl-tag">개발</span></div><div class="tl-title">프로토타입 "Canyon"</div><div class="tl-metric">2026년 1월 소식지는 개발이 "작년 초 거친 프로토타입"에서 시작됐으며 내부에서는 Canyon이라 불렀다고 회고했다. 타워 디펜스와 선형 미션 프로토타입이 각각 언제였는지는 공개되지 않았다.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1823191198608078">Steam 소식지 2026년 1월</a></div></li>
<li><div class="tl-date">2025년 5월에서 6월 <span class="tl-tag">계약</span></div><div class="tl-title">Fireshine Games와 퍼블리싱 계약</div><div class="tl-metric">계약 시기는 같은 소식지가 밝혔다. 6월 8일 보도자료에서는 Fireshine의 수석 제품 관리자(Senior Product Manager) Rob Feather가 올해 말 첫 플레이테스트를 열겠다고 예고했다.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1823191198608078">Steam 소식지 2026년 1월</a> / <a href="https://dlh.net/en/news/giddy-up-for-a-bounty-hunting-chaotic-co-op-cowboy-shooter-in-far-far-west-coming-to-steam-early-access-in-2026/">보도자료(dlh.net 전재)</a></div></li>
<li><div class="tl-date">2025년 6월 8일 <span class="tl-tag">공개</span></div><div class="tl-title">PC Gaming Show에서 첫 공개</div><div class="tl-metric">공개 트레일러와 함께 Steam 페이지가 열렸다. 4인 협동, 로봇 카우보이, 2026년 얼리 액세스 예정이라고 알렸다.</div><div class="tl-src"><a href="https://bsky.app/profile/farfarwest.bsky.social/post/3lr4ko2djxk2a">공식 Bluesky</a></div></li>
<li><div class="tl-date">2025년 8월 <span class="tl-tag">테스트</span></div><div class="tl-title">첫 비공개 커뮤니티 플레이테스트</div><div class="tl-metric">참가 규모는 공개되지 않았다.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1823191198608078">Steam 소식지 2026년 1월</a></div></li>
<li><div class="tl-date">2025년 10월 23일에서 11월 11일 <span class="tl-tag">테스트</span></div><div class="tl-title">첫 공개 플레이테스트</div><div class="tl-metric">Galaxies Showcase의 새 트레일러와 함께 시작. 11월 6일까지 예정이었으나 11월 10일까지로 연장됐고, 종료 공지는 11일에 올라왔다. 최고 동시 접속 2,500명 이상, 참가자 13만 명 이상. 개발팀은 동시 접속 300명을 예상했다고 밝혔다.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1814309641450220">Steam 공지 10/23</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1815580768428360">11/11</a> / <a href="https://bsky.app/profile/farfarwest.bsky.social/post/3m4gfzqlbhi22">Bluesky 10/30</a></div></li>
<li><div class="tl-date">2026년 1월 8일에서 19일 <span class="tl-tag">테스트</span></div><div class="tl-title">두 번째 공개 플레이테스트</div><div class="tl-metric">New Game+ Showcase에서 개발자 미션 시연. 새 지도 Far Far North, 새 무기 둘, UI 전면 개편, 세이브 시스템 재구축. 최고 동시 접속 9,270명, 피드백 폼 11,000건 이상.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1821288646578842">Steam 공지 1/8</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1823191198608078">소식지 1월</a></div></li>
<li><div class="tl-date">2026년 2월 19일에서 3월 2일 <span class="tl-tag">데모</span></div><div class="tl-title">공개 데모와 Steam Next Fest</div><div class="tl-metric">Next Fest(2월 23일에서 3월 2일)가 시작되기 나흘 전에 데모를 열었다. 가장 많이 플레이된 데모 5위 안에 들었고, 리뷰는 6,000건을 넘었으며 그중 98%가 긍정이었다. 데모 참가자는 30만 명 이상이고, 53%는 이 게임을 처음 접한 사람이었다.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1824644522839848">Steam 공지 2/13</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1826362059921210">3/5</a></div></li>
<li><div class="tl-date">2026년 4월 9일 <span class="tl-tag">공개</span></div><div class="tl-title">얼리 액세스 출시일 발표</div><div class="tl-metric">Triple-i Initiative 쇼케이스에서 4월 28일로 확정. 이튿날 퍼블리셔 모회사 EG7은 위시리스트 58만 개 이상이라고 공시했다.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1829528821307512">Steam 공지</a> / <a href="https://www.enadglobal7.com/">EG7 보도자료(4/10)</a></div></li>
<li><div class="tl-date">2026년 4월 28일 <span class="tl-tag">출시</span></div><div class="tl-title">Steam 얼리 액세스 출시, 19.99달러</div><div class="tl-metric">첫날 동시 접속 약 2만 명, 이후 최고 4만 7천 명. 개발팀은 첫날 4천 명, 첫 주말 1만 명을 예상했다고 밝혔다.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1830797770245289">Steam 공지</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1833968530885317">5월 개발일지</a></div></li>
<li><div class="tl-date">2026년 5월 1일에서 2일 <span class="tl-tag">운영</span></div><div class="tl-title">네트워크 제공사의 DDoS 방어 오작동</div><div class="tl-metric">공개 로비 접속과 프로모션 코드 사용이 막혔다. 같은 날 복구 공지, 이튿날 핫픽스 2에서 공개 로비를 자체 네트워크와 분리. 48시간 판매 25만 장.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1831432155571987">Steam 공지 5/1</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1831432155572871">핫픽스 2</a></div></li>
<li><div class="tl-date">2026년 5월 14일 <span class="tl-tag">업데이트</span></div><div class="tl-title">Update 1</div><div class="tl-metric">성장 요구량 절반으로 축소, 조커(퍽) 아이템의 개인별 인스턴싱, 호스트와 다른 네트워크에 있을 때의 접속 끊김 수정. 5월 18일 판매 100만 장.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1832700592788508">Steam 공지</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1832700592798258">5/18</a></div></li>
<li><div class="tl-date">2026년 6월 5일 <span class="tl-tag">업데이트</span></div><div class="tl-title">패치 0.1.1.3</div><div class="tl-metric">버전 표기를 빌드 번호(v6xx)에서 0.x.y.z 체계로 변경. 상위 난이도가 쉽다는 피드백에 따라 엘리트 적 4종 추가, 아군 피해 상한 도입.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1834602721191060">Steam 공지</a></div></li>
<li><div class="tl-date">2026년 7월 10일 <span class="tl-tag">개발</span></div><div class="tl-title">7월 개발일지</div><div class="tl-metric">새 적 세력 Zurkers, 등대, 근접 무기, 방어막을 작업 중이라고 알렸다. 레벨 디자인과 프로그래밍을 맡는 PROmium, 네트워크와 내부 도구를 맡는 Teeto가 합류.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1837955055356796">Steam 공지</a></div></li>
<li><div class="tl-date">2026년 8월 13일 <span class="tl-tag">기술</span></div><div class="tl-title">Epic의 Inside Unreal 방송</div><div class="tl-metric">Epic의 Ari Arnbjörnsson과 컨설턴트 Tom Looman이 개발 빌드(UE 5.8)를 프로파일링. Evil Raptor 팀원은 출연하지 않았다.</div><div class="tl-src"><a href="https://www.youtube.com/watch?v=kJPqrvB0fdo">YouTube</a></div></li>
<li><div class="tl-date">2026년 8월 21일에서 27일 <span class="tl-tag">업데이트</span></div><div class="tl-title">Frostburn 업데이트와 공개 로드맵</div><div class="tl-metric">21일 공지가 "내부 구조를 재정비하고 팀을 확장하는 데 시간을 썼다"고 밝혔다. 26일 Gamescom에서 하루 먼저 시연, 27일 v0.2.0.2 배포와 함께 Notion 로드맵 공개.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1841579228668773">Steam 공지 8/21</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1842212951299982">8/27</a></div></li>
<li><div class="tl-date">2026년 9월 3일에서 7일 <span class="tl-tag">운영</span></div><div class="tl-title">업데이트 후 통계, 9월 개발일지, 패치 0.2.0.20</div><div class="tl-metric">새 플레이어 6만 명 이상, 동시 접속 1만 1천 명 이상, 버그 보고 500건 이상. Sentry 도입으로 주요 크래시 원인 5개 중 3개 수정. 보스 개편을 맡는 Jonathan 합류.</div><div class="tl-src"><a href="https://store.steampowered.com/news/app/3124540/view/1842846814444430">Steam 공지 9/3</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1842846814449079">9/5</a> / <a href="https://store.steampowered.com/news/app/3124540/view/1842846814454046">9/7</a></div></li>
</ol>
<p class="tl-note">개발팀과 퍼블리셔가 공개한 기록을 시간순으로 배열했다. 날짜는 공지가 게시된 날(UTC)을 기준으로 삼았고, 기사가 뒤늦게 회고한 시점은 본문에서 따로 표시했다. 판매량과 접속자 수는 개발팀과 퍼블리셔의 자기 보고 수치다.</p>

## 세 번의 프로토타입

이 게임은 처음부터 지금과 같은 모양으로 계획된 것이 아니었다. Petit는 GamesRadar+에 "「Far Far West」는 세 번의 큰 반복을 거쳤다"고 설명했다. "첫 프로토타입은 타워 디펜스를 새롭게 해석한 것이었고, 두 번째는 Left 4 Dead처럼 선형 미션으로 구성했다. 두 방향 모두 우리가 바라던 만큼 잘 맞지 않는다는 것을 깨달은 뒤, 가장 좋은 아이디어를 한데 모았다. 탄탄한 총격, 웃긴 주문, 엉뚱한 조합에 집중해 반복 플레이가 가능한 구조로 엮었고, 그제야 게임이 자기 자리를 찾았다."[^gr] 같은 이야기를 Meyssonnier도 GameDiscoverCo에 했다. 그에 따르면 지금의 판은 "실은 세 번째"였고, 그 앞의 첫 번째는 타워 디펜스, 두 번째는 "선형의 미션 기반 게임"이었다.[^gdco]

세 단계가 각각 어느 시기였는지에 대해서는 두 사람 모두 말하지 않았다. 순서만 알 수 있다. 시점에 관한 유일한 단서는 2026년 1월 말 소식지의 회고인데, "작년 초 거친 프로토타입으로 시작했고, 내부에서는 Canyon이라 불렀다"고 적었다.[^bulletin-jan] 「Akimbot」은 2024년 8월 말에 나왔다. 그 출시와 2025년 초의 Canyon 사이에 앞선 두 프로토타입이 있었는지, 「Akimbot」 개발과 겹쳐 진행됐는지, Canyon이 세 단계 가운데 어디에 해당하는지는 자료에 나오지 않는다.

지금의 구조 안에서도 한 번 더 방향이 바뀌었다. Meyssonnier는 Screen Rant에 이렇게 말했다. "우리는 어느 한 범주에 맞추려 하지 않았고, 처음부터 추출 슈터를 만들 생각도 없었다. 개발 중 어느 시점까지는 미션에서 미션으로 넘어갈 뿐 추출 요소가 없었다. 그러다 한번 시험해 보기로 했다. 미션이 끝나면 로비로 돌아가는 기차를 만들었더니 추출 슈터가 됐다. 처음부터 노린 방향은 아니었지만, 만들고 보니 그렇게 됐다."[^sr] 지금 게임의 한 판은 임무를 마친 뒤 기차역으로 가서 종을 울리고, 몰려오는 적을 버티며 기차를 기다리는 것으로 끝난다.

![Far Far North 지도를 달리는 기차 1225 Pere Marquette의 텍스처 완성본. 2026년 1월 소식지.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/06-train-pere-marquette.jpg)

지도는 절차적으로 생성되지 않는다. 출시 당일 Steam 게시판에 Fireshine 소속 담당자가 올린 답변(개발자 답변으로 표시됨)은 이렇게 설명한다. "지도는 손으로 정성껏 만든다. 그 위에 '슬롯'을 놓으면 슬롯이 여러 요소를 무작위로 불러온다. 그러니 지도는 무작위이기는 하지만 절차적으로 생성되지는 않는다. 무작위로 정해지는 것은 관심 지점이고, 지도 자체는 고정되어 있다."[^steam-qa]

## 서부, 로봇, 그리고 마법

배경을 서부로 정한 과정을 Meyssonnier는 소거법으로 설명했다. 스튜디오는 무명에서 벗어나게 해 줄 소재, 그러면서 다른 슈터와 구분되는 소재를 찾았다. SF 쪽에는 Deep Rock Galactic과 Helldivers가 이미 자리를 잡고 있었고, 해적은 Sea of Thieves의 것이었다. "Steam을 훑으면서 하나씩 제외해 나갔더니 서부가 비어 있었다. 양식화된 서부 게임이 별로 없었다. 그러면 서부를 만들지 않을 이유가 있나. 양식화할 수 있는 관습이 많고, 색깔이 풍부한 배경이다. 우리에게 아주 잘 맞았다."[^pcg-apr] 그는 GameDiscoverCo에 카우보이와 로봇을 겹치는 발상에는 Overwatch에서 조금 영감을 받았다고 덧붙였다.[^gdco]

![초기 콘셉트 단계의 환경 디오라마. 사막 바닥에 바위와 선인장, 마른 나무를 배치했다. 2025년 7월 18일 공식 Bluesky 게시물.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/02-world-concept-desert.jpg)

로봇은 취향의 문제가 아니었다. "로봇을 택한 이유는 전적으로 기술적인 제약 때문이었다"고 그는 말했다. 딱딱하고 기계적인 로봇 카우보이는 살과 뼈가 있는 카우보이보다 모델링과 애니메이션 제작이 훨씬 단순하다. 팀은 한 걸음 더 나가서 모든 로봇에게 Rayman처럼 몸에서 떠 있는 손을 주었다. 그 덕분에 대부분의 멀티플레이어 FPS가 따로 만들어야 하는 1인칭용 애니메이션과 3인칭용 애니메이션을 무기마다 한 세트만 만들 수 있었다.[^pcg-apr] 2025년 7월 4일 공식 Bluesky는 로봇 카우보이의 초기 콘셉트를 공개하면서 "1인칭 게임에서는 손을 오랫동안 쳐다보게 되므로, 손을 완벽하게 만드는 것이 우리에게 중요했다"고 적었다.[^bsky-hands] 이 원칙은 조연에게도 적용됐다. 같은 해 10월 1일 게시물은 "오래된 유기체 닭 메시를 대체할 새 닭 메시를 만들고 있다"고 알리며 깃털 달린 닭과 로봇 닭을 나란히 보여 주었다.[^bsky-chicken]

![대체되기 전의 유기체 닭 모델. 2025년 10월 1일 공식 Bluesky 게시물.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/04-old-organic-chicken.jpg)

![새로 만든 로봇 닭 모델을 Blender에서 작업하는 화면. 같은 날 게시물의 영상 한 장면.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/05-new-robot-chicken.jpg)

마법은 나중에 들어왔다. PC Gamer에 따르면, 초기 플레이테스트에서 총격만으로는 무언가 부족하다는 점이 분명해진 뒤에 로봇들이 주문을 쓰기 시작했다. Petit는 "무언가 더 필요하다고 느꼈고, 우리가 더 할 수 있다고 느꼈다. 그리고 마법은 언제나 멋지다"고 말했다. 주문끼리 효과와 상태 이상을 조합할 수 있게 하자 협동할 거리가 늘었고, 그는 이것이 "게임과 아주 잘 맞았다"고 했다.[^pcg-apr] 2025년 7월 28일 시점에 공개된 주문은 불, 전기, 산성의 세 속성 열다섯 개였다.[^bsky-spells] 두 번째 플레이테스트에서는 속성마다 고유 효과를 붙이고 몇 개를 교체했으며, 데모 직후의 소식지에는 새 속성인 선인장의 3D 메시가 실렸고, 8월 업데이트에는 근접 무기와 방어막에 맞춘 새 속성 냉기가 추가됐다.[^pt2][^bulletin-mar][^frost-out]

![권총의 콘셉트 스케치와 게임 안 모델. 2025년 7월 25일 공식 Bluesky 게시물.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/03-pistol-concept-to-model.jpg)

아트 디렉션과 분위기는 Meyssonnier에게서 나왔다고 Petit가 말했다.[^gr] Meyssonnier 자신은 색에 관한 취향을 이렇게 설명했다. "「Pumpkin Jack」을 만들 때 나는 스푸키한 게임을 만들었고, 그 톤과 검은 테마가 좋았다. 검정, 파랑, 초록을 함께 쓰면 요즘 게임에서 사라진 아주 좋은 색이 나온다. 게임에 생기를 되돌리려면 채도가 높은 무언가가 필요하다고 느꼈다. 특히 로비는 살아 있는 장소처럼 느껴져야 했다."[^sr] 음악은 「Akimbot」을 맡았던 작곡가가 그대로 맡았다. Petit는 그가 전자 음악 전문이라서 그 에너지를 이어 오되 "밴조를 그 위에 얹고 카우보이를 생각하면 '일렉트로 밴조 밥(electro banjo bop)'이 된다"고 했고, 장르 이름을 따로 정하지 않은 채 가고 있다고 말했다.[^gr] 총격의 감각에 관해서는 Overwatch의 애니메이션을 유심히 연구했다고 밝혔다.[^gr]

## 플랫포머 팀이 처음 만든 협동 FPS

Meyssonnier는 협동 FPS로 방향을 바꾼 계기를 「Pumpkin Jack」을 만든 계기와 같은 방식으로 설명했다. 「Akimbot」을 만든 뒤 팀은 함께 게임을 많이 했는데 취향에 맞는 협동 슈터를 찾지 못했다. "우리에게 완벽한 게임이 없다. 그런데 우리는 게임을 만든다. 그러면 우리가 플레이할 협동 게임을 만들자."[^pcg-apr] 싱글 플레이 플랫포머에서 멀티플레이어 FPS로 넘어오는 데는 배워야 할 것이 많았다. PC Gamer는 팀이 대역폭 관리, 새로운 종류의 레벨 디자인, 그리고 더 집요한 최적화를 벼락치기로 익혔다고 전했다. 최적화가 필요한 이유를 Meyssonnier는 "사람들은 성능이 나쁜 컴퓨터를 가진 친구와 함께 플레이하기를 기대한다"고 표현했다.[^pcg-apr]

기술적인 선택의 상당 부분은 개발팀이 직접 설명한 적이 없고, 대신 2026년 8월 13일 Epic Games의 Inside Unreal 방송에서 드러났다. 이 방송에는 Epic 개발자 관계 팀의 기술 담당자 Ari Arnbjörnsson과, 이 게임의 최적화를 돕는 외부 컨설턴트 Tom Looman이 출연했다. Evil Raptor 팀원은 나오지 않았고, Arnbjörnsson은 방송 며칠 전에 Looman이 보내 준 개발 빌드를 처음 살펴봤다고 말했다.[^iu] 따라서 아래 내용은 두 사람이 빌드를 들여다보고 관찰한 것이며, 개발팀이 설계 의도를 직접 밝힌 진술과는 구분해서 읽어야 한다.

{{< youtube kJPqrvB0fdo >}}

그 빌드는 Unreal Engine 5.8이었다. 4월 말에 Looman이 혼자 올린 영상에서는 5.7이었으므로, 그 사이에 팀이 엔진 버전을 올렸다.[^iu][^looman] 지도는 한 변의 길이가 약 1킬로미터다. World Partition 스트리밍을 쓰지 않고 지도 전체를 메모리에 한꺼번에 올린다. Arnbjörnsson은 "내가 보통 권하는 모범 사례인 World Partition과 HLOD를 쓰지 않았는데도 성능이 꽤 좋아서 놀랐다"고 했다.[^iu] Looman은 지도가 그리 크지 않은 데다, 바위와 나무 구조물에 같은 메시를 몇 가지 재질로 바꿔 반복해서 쓰기 때문에 Nanite가 재질별 인스턴싱을 효율적으로 처리한다고 설명했다.[^iu]

방송 후반의 질의응답에서는 멀티플레이어와의 관계가 나왔다. 이 게임에서는 호스트가 되는 플레이어가 서버 역할을 하고, 다른 플레이어들은 지도 반대편에 있을 수 있다. 그러니 충돌 데이터가 항상 전부 준비돼 있어야 하고, 지도를 스트리밍하지 않는 쪽이 도리어 문제를 덜 만들었다고 그는 설명했다.[^iu] Nanite를 쓴 이유에 관해 Arnbjörnsson은 "양식화된 게임이라 그렇게 많은 디테일이 필요하지는 않지만, Lumen과 가상 섀도 맵을 쓰려면 Nanite를 함께 쓰는 것이 성능에 낫다"고 설명했다.[^iu]

적을 다루는 방식도 소개됐다. 팀의 프로그래머(방송에서는 Dave라고만 불렸다)가 만든 "Enemy Optimizer"는 적마다 플레이어들에게 얼마나 중요한지를 계산한다. 멀리 있고 아무도 보지 않는 적은 틱 속도를 낮추고 애니메이션을 끈다. 물리 기반으로 걷게 하는 대신 내비게이션 메시 위를 미끄러지듯 이동시킨다. 호스트는 모든 플레이어의 위치를 함께 고려해야 한다.[^iu] Arnbjörnsson은 적이 움직여도 물리 데이터가 이전 자리에 남아 있다가 총을 맞을 때에만 현재 위치로 갱신되는 모습을 Chaos Visual Debugger로 보여 주면서, "내가 오기 전에 이미 엄청난 양의 최적화를 해 두었다"고 말했다.[^iu]

Looman의 4월 30일 영상과 글은 GPU 쪽을 다뤘다. 기준선은 RTX 3060에서 초당 약 50프레임이었고, 프레임 하나에 20밀리초가 걸렸다. 그 20밀리초 가운데 7밀리초를 Nanite VisBuffer가 쓰고 있었다. 마스크 재질의 나뭇잎에 Pixel Depth Offset이 켜져 있었던 것이 원인이었다. 이것을 끄면 프레임당 약 2밀리초가 절약됐다. 지도 전체를 덮는 데칼 두 장(모래 혼합층과 물의 빛 굴절)이 마을 밖에서 데칼 비용을 올리고 있었다는 것도 발견했다.[^looman] 9월 개발일지는 이 두 영상을 "우리가 새로운 최적화 방법을 찾도록 도와준 전문가들의 영상"이라고 소개하면서, 그것이 "Spinker 자신의 작업 위에" 더해진 것이라고 썼다. 같은 글은 "Unreal Engine 5의 최적화에 관한 비판은 우리도 다 들어 왔다. 그 비판이 우리를 더 자극한다. 「Far Far West」를 그것이 가능하다는 것을 증명하는 게임으로 만들고 싶다"고 밝혔고, Vulkan SM5 지원을 준비 중이라고 알렸다.[^devlog-sep]

낮은 사양을 향한 노력은 출시 전부터 기록에 남아 있다. 2026년 1월 소식지는 "CPU 최적화에 큰 진전"을 적었고, 2월의 데모 공지는 "DirectX 11을 지원해 더 많은 시스템과 호환된다"고 알렸다.[^bulletin-jan][^demo-coming] Steam 상점의 최소 사양은 GTX 1660 또는 RX 590, 8GB 메모리다.[^steam-store] 8월 업데이트 이후에는 "저사양과 Linux에서의 안정화"에 집중하고 있다고 했고, 9월 7일 패치는 특정 Linux Vulkan 환경의 GPU 크래시를 고쳤다.[^frost-stats][^patch-0220]

## 공개 개발: 세 번의 테스트와 한 번의 데모

Meyssonnier는 이 게임이 스튜디오가 "오픈 개발" 방식으로 만든 첫 게임이라고 했다. "솔직히 이것은 우리가 게임을 위해 낸 최고의 아이디어였다. 플레이어와 건설적이고 직설적인 관계를 갖는 것은 개발자로서 아주 즐거운 일이다."[^gdco] 로비에는 피드백을 요청하는 Discord 링크가 있고, 팀은 Steam 포럼과 Discord를 전부 읽는다고 그는 Screen Rant에 말했다.[^sr]

첫 공개 플레이테스트는 2025년 10월 23일 Galaxies Showcase의 새 트레일러와 함께 열렸다. 키 없이 Steam 페이지의 버튼으로 바로 참가할 수 있었고, 버그 보고는 Steam 게시판 대신 Discord와 게임 안 링크로 받았다.[^pt1] 개발팀은 동시 접속 300명을 예상했다. 일주일 뒤 밤에 2,424명이 동시에 접속했고, 팀은 이를 축하하며 로비를 할로윈 장식으로 바꾸고 「Pumpkin Jack」 스킨을 넣은 업데이트를 냈다.[^pt1-halloween] 11월 6일 종료 예정이던 테스트는 "한 주말 더"라는 공지와 함께 11월 10일까지 연장됐고, 종료 공지는 11일에 올라왔다. 테스트가 끝났을 때 최고 동시 접속은 2,500명을 넘었고, 참가자는 13만 명을 넘었다. 종료 공지의 피드백 폼은 Fireshine Games의 계정으로 만들어져 있었다.[^pt1-end]

테스트가 끝난 뒤의 두 달 동안 공식 Bluesky에는 작업 중인 것들이 올라왔다. 11월 13일에는 Mars Attacks!에서 영감을 받은 새 외계인 군대의 이름을 Discord 투표로 정했다며 "Zukers"와 그 지도자 Berk의 콘셉트를 공개했고, 11월 20일에는 첫 개체의 리깅을 마쳤다고 알렸다. 11월 26일에는 부메랑 무기와 미끄러운 얼음을 "200% 미완성"이라며 보여 주었다.[^bsky-zukers][^bsky-boomerang]

두 번째 공개 플레이테스트는 2026년 1월 8일에 시작해 16일까지 예정됐다가 19일까지 연장됐다. 공지는 이번 테스트에 지난 테스트의 피드백을 반영한 새 기능과 콘텐츠, 여러 개선 사항을 담았다고 소개했다. 눈과 얼음의 새 지도 Far Far North는 다른 지도에서 수상한 기차를 찾아야 열렸다. 부메랑과 셰리프 스타라는 무기 두 종을 더했고, 주문에는 속성별 고유 효과를 넣었다. UI도 접근성과 가독성을 높이도록 전면 개편해서, 계약 선택 화면은 세계 지도가 되고 멀티플레이어 탭은 필터가 있는 서버 목록이 됐다.

여기에 계약에 붙일 수 있는 수정자, 새 주요 목표 두 종(드릴과 페이로드), 살룬이 보스인 전투가 추가됐다. 세이브 시스템은 완전히 다시 만들었다. 공지는 이것이 장기 업데이트를 위한 "무한한 확장성"을 위한 것이며 "이번부터 플레이테스트 사이에 진행 상황을 유지할 수 있어야 한다"고 적었다. 무기 경험치는 처치 수 대신 피해량으로 오르게 바뀌었다.[^pt2]

![두 번째 플레이테스트에서 새로 들어간 세계 지도 형태의 계약 선택 화면. 2026년 1월 8일 Steam 공지.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/07-playtest2-world-map.jpg)

같은 날 밤 New Game+ Showcase에서 개발팀은 미션 하나를 처음부터 끝까지 시연했다. 프랑스 매체 NoFrag는 이 쇼케이스에 "Evil Raptor의 개발자 여섯 명"이 나왔다고 전했고, 당시 빌드에 대해 총격의 감각이 "대단하지 않고" 보스 패턴이 서로 비슷하다는 비판을 적었다. 이 기사에는 개발자들이 "만족스러운 버전에 이르기까지 아직 2년의 작업이 남았다고 본다"는 문장이 있다. 이 발언은 얼리 액세스 출시 세 달 반 전에 나왔다. 여기서 "만족스러운 버전"이 얼리 액세스인지 정식 출시인지는 기사가 밝히지 않는다.[^nofrag-jan]

{{< youtube s-CirtbU0mA >}}

결과는 첫 테스트를 크게 넘었다. 1월 말 소식지에 따르면 최고 동시 접속 9,270명, 참가자 30만 명 이상, Discord 회원은 7천 명 미만에서 2만 5천 명으로 늘었고, 피드백 폼 11,000건 이상이 들어왔다.[^bulletin-jan] 참가자 수에는 기록 사이에 차이가 있다. 연장을 알린 1월 15일 Bluesky 게시물은 "50만 명 이상"이라고 썼고, 2주 뒤의 소식지는 "30만 명 이상"이라고 썼다.[^bsky-extend][^bulletin-jan] 어느 쪽이 정확한지, 두 수치의 정의가 어떻게 다른지는 공개되지 않았다.

퍼블리셔가 이 테스트들을 어떻게 운영했는지는 Fireshine의 Rob Feather가 GameDiscoverCo에 설명했다. "각 '플레이 가능한 시점' 일주일 전에 VIP 커뮤니티 회원 수백 명이 먼저 들어와서 피드백을 모으고 빌드를 다졌다. 나흘 전에는 뉴스레터 구독자가 코드를 받았다. 이틀 전에는 Discord 커뮤니티 전체가 키를 받을 수 있었다. 단계마다 실제 데이터를 모아 빌드를 손볼 시간을 벌었고, 게임을 공유하려는 사람도 늘었다. 그 뒤 플레이테스트는 온라인 쇼케이스의 소개와 함께 완전히 열렸고, 그 무렵 몇몇 크리에이터를 합류시키고 유료 광고와 짧은 영상으로 그 순간을 뒷받침했다."[^gdco]

그가 함께 제공한 위시리스트 그래프는 2025년 9월 20일부터 출시 직전까지의 일별 위시리스트 추가 수를 보여 준다. 그래프를 보면 첫 플레이테스트 기간에는 하루 약 1만 개 안팎의 봉우리가 두 차례 나타난다. 두 번째 플레이테스트 기간에는 하루 약 2만 7천 개로 가장 높은 봉우리가 나타났고, 거기에는 "스트리머와 짧은 영상 활성화"라는 설명이 붙었다. Next Fest 기간에는 "Next Fest 첫 화면 노출"이라는 설명과 함께 약 2만 개의 봉우리가 있고, 출시일을 발표했을 때는 약 1만 3천 개의 봉우리가 나타났다.[^gdco] 사건별 기여도를 개발팀이나 퍼블리셔가 수치로 밝힌 것은 아니고, 이 값들은 그래프의 눈금을 눈으로 읽어 적은 근사치다.

2월 19일에 데모가 열렸다. Steam Next Fest는 그로부터 나흘 뒤인 2월 23일에 시작해 3월 2일에 끝났다. 뉴스레터 구독자는 하루 먼저 들어갈 수 있는 코드를 받았다. 공지는 이 데모가 "지난 플레이테스트의 재방송이 아니다"라고 하면서, 장비 설계도 시스템(게임 안에서 무기 설계도를 찾아 상점에서 제작), 설계도를 모을수록 오르는 Glory 레벨, 새 업그레이드와 무기와 주문, DirectX 11 지원, 접근성 옵션 추가를 나열했다.[^demo-coming] 데모가 끝난 뒤 개발팀은 리뷰 6,000건 이상에 긍정 98%(영어 리뷰는 99%), 데모 참가자 30만 명 이상, 그중 53%가 이 게임을 처음 접한 사람, 최고 난이도인 Nightmare를 시도한 사람은 9%라고 발표했다. Valve의 집계에서 가장 많이 플레이된 데모 5위 안에 들었다.[^demo-end][^bulletin-mar] 4월 28일의 출시 공지는 "40만 명 이상의 데모 플레이어"라고 썼는데, 3월 5일의 30만 명 이상과 어느 시점의 어떤 집계가 다른지는 설명되지 않았다.[^launch]

3월 소식지는 데모 피드백에 따른 수정과 함께 작업 중인 콘텐츠를 콘셉트 아트, 3D와 리그, 애니메이션으로 나누어 보여 주었다. 새 적 Deadeye는 콘셉트 스케치와 3D 모델이 나란히 실렸고, Loot Goblin이라는 중립 적, 새 속성 선인장의 주문 메시, Far Far North의 기차 완성본, 무작위로 생성되는 소원의 샘이 이때 소개됐다.[^bulletin-mar]

![새 적 Deadeye의 콘셉트 스케치. 스케치 여백의 메모에는 사거리가 아주 길고 배럴 제트팩으로 공중에 떠 있다고 적혀 있다. 2026년 3월 소식지.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/08-deadeye-concept.jpg)

![같은 소식지에 실린 Deadeye의 3D 모델.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/09-deadeye-model.jpg)

4월 9일 Triple-i Initiative 쇼케이스에서 출시일이 4월 28일로 발표됐다. 이튿날 Fireshine의 모회사 EG7은 위시리스트가 58만 개를 넘었다고 공시했고, GameDiscoverCo는 출시 시점의 위시리스트를 약 65만 개로 추정했다.[^ea-date][^eg7-apr][^gdco] 출시 전날 공식 Bluesky에 올라온 얼리 액세스 로드맵 미리보기에는 새 적 군대, 새 지도, 새 주요 목표, 장기 성장, 복제 가능한 조커, 커뮤니티 목표와 이벤트, 스킨과 무기 스킨이 적혀 있었다.[^bsky-roadmap] Petit는 출시 전의 마음을 이렇게 돌아봤다. "여러 번의 공개 플레이테스트와 공개 리뷰가 있는 데모를 돌린 것이 분명히 긴장을 덜어 주었다. 사람들이 즐기는 것을 볼 수 있었으니까. 그렇지만 데모가 무료였기 때문에 그 관심이 실제 판매로 이어질지는 알 수 없었다."[^gr]

![출시 전날 공개된 얼리 액세스 로드맵 미리보기. 2026년 4월 27일 공식 Bluesky 게시물.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/10-ea-roadmap-preview.jpg)

## 출시 첫 주

4월 28일 얼리 액세스가 시작됐다. Steam 상점의 안내문은 얼리 액세스 기간을 12개월로 계획하고 있고, 정식 출시 때 가격을 올릴 것이라고 밝혔다.[^steam-store] 5월 개발일지에서 개발자는 자신의 예상과 결과를 나란히 늘어놓았다. 개발자는 첫날 동시 접속을 4천 명, 첫 주말을 1만 명으로 잡아 두었다. 실제로는 첫날에만 2만 명이 들어왔고, 최고 동시 접속은 4만 7천 명까지 올라갔다. 판매는 첫 주에 10만 장을 예상했는데 50만 장을 넘겼다. 위시리스트는 100만 개에 이르렀고, Discord 회원은 12만 명이 됐다. 리뷰 긍정 비율은 85%에서 90% 사이를 예상했는데 97%가 나왔다.[^devlog-may] 판매량 공식 발표는 4월 30일 무렵의 48시간 25만 장, 5월 4일의 50만 장, 5월 18일의 100만 장 순서였다.[^250k][^500k][^1m]

같은 주에 문제가 잇따랐다. 5월 1일 개발팀은 "네트워크 제공사의 DDoS 방어 시스템이 오늘 일어난 플레이어 수 급증 때문에 발동했다"고 공지했다. 그 결과 공개 로비에 들어갈 수 없고 게임 안에서 프로모션 코드를 쓸 수 없었다. 프로모션 코드가 보상을 지급하지 않고도 사용된 것으로 처리될 수 있으니 복구 전에는 입력하지 말라고 안내했고, 혼자 플레이하거나 세션 코드와 Steam 초대로 친구와 플레이하는 것은 정상이라고 알렸다.[^server] PC Gamer는 Discord에서 개발팀이 "우리의 훌륭한 서비스 제공사는 지금 도와주는 대신 모히토를 마시고 있다"고 쓴 것을 전했다. 같은 기사의 후속 갱신에 따르면 팀은 베타 브랜치에서 우회 패치를 시험했는데, 그 패치가 작동하면 "모두가 온라인 세션에서 플레이하기 위해 우리 네트워크가 작동할 필요가 없어진다"고 했다.[^pcg-server] 그 변경은 이튿날 핫픽스 2에 들어갔다. "공개 로비의 작동 방식을 바꿔서 Evil Raptor 네트워크가 내려가 있어도 항상 켜져 있게 했다."[^hotfix2] 첫 핫픽스도 "네트워크 크래시를 막기 위해 내부 네트워크 시스템을 개선했다"고 적었고, Update 1은 "호스트와 같은 네트워크에 있지 않을 때 호스트에서 끊기는 버그"를 고쳤다.[^hotfix1][^update1] 네트워크 제공사의 이름과 전송 계층의 구현 방식은 어느 자료에도 나오지 않는다.

세이브 손상은 첫 주의 다른 한 축이었다. Meyssonnier는 Screen Rant에 "진행 상황 손실을 포함한 버그를 사람들이 겪고 있고, 모두에게 정말 답답한 일이다. 버그가 생길까 봐 끊임없이 모니터링하고 있어서 스트레스가 크다"고 말했다.[^sr] 첫 핫픽스는 세이브 백업 수를 10개에서 30개로 늘리고 미션을 마칠 때마다 백업을 만들게 했으며, 세 번째 핫픽스는 손상된 진행 상황을 저장하지 않게 하고 크래시 위험이 있는 작업 중에는 저장을 멈추게 했다. 자동 백업은 Steam 클라우드에서 빼서 패밀리 셰어링으로 잃지 않게 했다.[^hotfix1][^hotfix3] 5월 개발일지는 첫 주에 치명적 오류와 크래시와 서버 문제를 제외하고도 2,000건 이상의 버그 보고가 들어왔고, 두 프로그래머가 며칠 만에 치명적인 것들을 고쳐 같은 주에 핫픽스 둘을 냈다고 적었다. "핫픽스가 없애야 할 버그보다 더 많은 버그를 가져오면 어쩌나" 하는 긴장이 같이 적혀 있다.[^devlog-may]

## 출시 이후 넉 달

5월 14일의 Update 1은 버그 수정만 담은 핫픽스 셋이 나온 뒤에 처음으로 시스템 변경을 담은 업데이트였고, 두 가지 큰 변경의 이유를 설명했다. 첫째는 성장 요구량이다. "Prestige 시스템을 만들면서 한 번의 Prestige에 필요한 반복량을 과하게 잡았다. 영웅과 무기를 조금 더 얻기 위해 그렇게 많이 반복해야 하는 것은 꽤 불공평하다고 느껴서 반복량을 절반으로 줄인다. 얼리 액세스 첫 며칠이지만, 그것이 레벨 업의 재미를 전부 빼앗는 시스템의 변명이 될 수는 없다." 둘째는 조커라고 부르는 퍽 아이템이다. 멀티플레이어 로비에서 조커가 나오는 순간 달려가 독식하는 문제가 있었는데, 팀은 처음에 협력과 공유가 어려워질까 봐 바꾸기를 망설였다. 결국 조커를 플레이어별로 인스턴싱하되 미니맵에서 떨어뜨려 공유할 수 있게 했고, 핑으로 공유하는 방식은 조커가 물체 안에 스폰될 수 있고 흩어진 플레이어가 하나를 위해 되돌아가는 것이 재미없다는 이유로 택하지 않았다. 대신 인원이 많을수록 적의 조커 드롭률을 낮췄다.[^update1]

6월 5일 패치 0.1.1.3은 버전 표기를 바꿨다. 그때까지 v583, v644처럼 하나씩 올라가던 빌드 번호를 0.1.1.3 같은 체계로 바꾸고, 맨 앞의 0이 얼리 액세스를 뜻하며 정식 출시 때 1이 된다고 설명했다. 상위 난이도가 너무 단순하고 조커를 하나도 집지 않고 이기는 사람도 있다는 피드백에 따라 엘리트 적 4종을 넣었고, 세션에 들어와 아군을 한 방에 죽이고 나가는 사람들 때문에 아군 피해에 한 번에 체력 25까지라는 상한을 두었다.[^patch-0113]

5월 개발일지는 팀의 상태를 솔직하게 적었다. 두 프로그래머가 버그에 매달리는 동안 나머지가 새 동물, 지도별 보스, 부두 속성의 새 조합, 모자를 던지는 함성, Hellfire 지도를 작업하고 있었다. 커뮤니티 성우들에게서 1,200개의 음성 파일이 들어왔는데 한 사람이 전부 듣느라 두 시간에 100개밖에 듣지 못했다는 대목도 있다. 피드백에 관해서는 "모두를 만족시키고, 모든 요구에 맞는 시스템을 만들고, '깨진 빌드'를 피하는 것은 극도로 어렵다(마지막 것은 실패한 것 같다). 솔직히 모든 피드백을 관리하고 모두와 제대로 소통하는 데 어려움을 겪고 있다. Discord, YouTube, Reddit, X, Steam을 다 봐야 한다"고 썼다. 공개하는 작업물에 관해서는 "여기 보이는 것은 게임에 영영 들어오지 않을 수도 있다. 지금은 이것에 대한 피드백을 받지 않는다. 먼저 요리하게 해 달라"는 경고를 붙였다.[^devlog-may]

7월 10일 개발일지는 그 뒤의 작업을 넓게 보여 주었다. 새 외계인 세력 Zurkers가 먼저 나왔는데, Bluesky에서 처음 소개할 때는 Zukers라고 표기했던 세력이다. 지도의 특수 시설을 미니맵에 그냥 표시하는 대신, 등대에 올라 미니게임을 풀면 지도가 밝혀지는 탐험 요소도 만들고 있었다. 정글 지도의 지하 던전 세 곳을 도는 퀘스트, 거의 완성된 Hellfire 지도, 막 시작한 Redwood 숲 지도, 근접 무기, 방어막, 새 조커 30개 이상도 함께 소개됐다. 같은 글은 두 사람의 합류를 알렸다. PROmium은 퀘스트와 적을 포함한 레벨 디자인과 프로그래밍을, Teeto는 "네트워크, Discord 연동, Twitch 연동, 그리고 Evil Raptor에서의 삶을 편하게 해 줄 많은 내부 도구"를 맡는다고 했다.[^devlog-jul] 7월 말에는 「Far Far West」의 리드 애니메이터와 함께 일할 원격 3D 애니메이터 채용 공고가 프랑스 구직 사이트에 올라왔다.[^job]

![새 적 세력 Zurkers의 작업 중 화면. 얼굴은 아직 임시 처리 상태다. 2026년 7월 개발일지.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/11-zurkers-faction.jpg)

그 뒤 한 달 남짓 소식이 없었다. 8월 21일 공지는 그 사정을 설명했다. "우리는 작은 인디 팀이고, 「Far Far West」를 세상에 내놓을 때 이 정도의 사랑과 성공은 전혀 예상하지 못했다. 그것은 한 걸음 물러서서 앞으로 닥칠 일을 감당할 준비가 됐는지 확인해야 한다는 뜻이기도 했다. 지난 몇 달 동안 우리는 트레일러로 보여 주기에는 별로 신나지 않는 일을 많이 했다. 내부 구조를 재정비하고, 팀을 확장하고, 일하는 방식을 개선하고, 「Far Far West」의 미래가 실제로 어떤 모양이어야 하는지 생각했다."[^frost-coming] 8월 27일의 업데이트 공지는 여기에 한 문장을 더했다. "지난 몇 달은 우리를 완전히 휘청이게 했다. 출시는 우리 작은 팀에게 거대한 순간이었고, 그 뒤에 따라온 모든 일을 겪은 뒤에 쉬고 회복할 시간이 필요했다."[^frost-out]

Frostburn 업데이트는 8월 26일 Gamescom 부스에서 하루 먼저 시연됐고 27일에 v0.2.0.2로 배포됐다. 기존에는 무기별로 조각을 추적해 모아야 했는데, 이것을 단일 통화인 설계도로 바꿨다. 미션 안에서만 쓰는 새 통화 우라늄도 추가해 로비의 장기 성장에 쓰는 금과 분리했다. 근접 무기는 너클, 올가미, 밴조 세 종을 추가했고, 방어막과 새 속성 냉기, Hellfire 지도, 등대도 함께 넣었다. 각 변경에는 이유가 붙었다. 이를테면 우라늄은 "미션 중에 도구를 쓰는 것이 낭비처럼 느껴지지 않게" 하려는 것이고, 마음에 들지 않는 조커를 부숴 우라늄으로 바꿀 수 있게 한 것은 조커 목록이 늘수록 싫은 조커를 만날 확률도 늘기 때문이라고 했다.[^frost-out] 같은 날 Notion에 공개 로드맵이 올라왔다. 이 글을 쓰는 시점의 로드맵은 2026년 10월(할로윈 이벤트, 새 목표, 난이도 상향, 주간 조커), 12월(크리스마스 이벤트, Zurkers 군대, 보스 개편, 주간 과제), 2027년 1분기(주문 시스템 개선, 로드아웃, 무기 스킨, 주간 원정), 2분기(길드, 커뮤니티 목표, 주간 현상 사냥)를 적고 있으며, 모든 항목이 바뀔 수 있다는 단서가 붙어 있다.[^roadmap] 로드맵의 항목은 아직 구현되지 않은 계획이고, 위에 적은 Frostburn의 내용은 이미 게임에 들어가 있다.

![Frostburn 업데이트 일주일 뒤 개발팀이 공개한 통계 이미지. 새 플레이어는 6만 명 이상, 동시 접속자는 1만 1천 명 이상, 버그 보고는 500건 이상이다. 평균 플레이 시간은 11시간이며, Nightmare 난이도를 플레이한 비율은 14%, 친구와 함께 플레이한 비율은 70%다. 2026년 9월 3일 Steam 공지.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/12-frostburn-stats.jpg)

업데이트 일주일 뒤의 통계에는 버그 보고 500건 이상이 함께 적혔다.[^frost-stats] 9월 5일 개발일지는 그 처리 방식이 달라졌다고 전했다. 7월에 합류한 Teeto가 오류 추적 도구 Sentry를 설치했고, 덕분에 크래시가 일어날 때 무엇이 잘못됐는지 상세한 로그를 받을 수 있게 됐다. 개발일지에는 "며칠 만에 주요 크래시 원인 5개 중 3개를 고쳤다"고 적혀 있다. 접속 끊김도 같은 방식으로 로그를 받아 주된 원인을 고쳤다.[^devlog-sep] 9월 7일 패치는 100개 이상의 버그를 고쳤다고 했는데, 그 안에는 매우 잦은 GPU 크래시, 특정 Linux Vulkan 환경의 GPU 크래시, 잦은 접속 끊김이 포함됐다. AMD 프레임 생성 기능과의 충돌은 AMD의 패치를 기다리고 있다고 적었다.[^patch-0220]

![Sentry에 모인 크래시 로그 화면. 개발팀이 9월 개발일지에서 공개한 것으로, 한 항목에 "5개 중 3개 수정"이라는 손글씨 주석이 붙어 있다.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/13-sentry-dashboard.jpg)

같은 개발일지는 앞으로의 분위기 작업도 설명했다. "로봇도 있고 해골도 있고 마법도 있는데, 전체 분위기에 아직 빠진 것이 있다고 느낀다. 그것은 스푸키함이다." 팀은 게임을 완전히 할로윈풍으로 만들지는 않되 스푸키함을 "약 20%" 올려서 지도들이 더 살아 있게 하려 하고, 이 변화는 할로윈이 지난 뒤에도 남는다고 했다.[^devlog-sep]

![Canyon 지도의 분위기를 스푸키하게 바꾸는 방향의 페인트오버 콘셉트. 개발팀 스스로 "과하게 그린 것"이라고 표시했다. 2026년 9월 개발일지.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/14-canyon-spooky-paintover.jpg)

## 퍼블리셔가 한 일

Fireshine Games는 영국 퍼블리셔로, 법적으로는 Sold Out Sales and Marketing Ltd의 상호이며 스웨덴 상장사 EG7 그룹에 속한다.[^eg7-may] 계약은 2025년 5월과 6월 사이에 이루어졌고, 6월 8일 PC Gaming Show의 첫 공개와 함께 발표됐다.[^bulletin-jan][^pr-jun] 공개 기록에서 확인되는 Fireshine의 활동은 이렇다. 플레이테스트 종료 공지의 피드백 폼은 Fireshine 계정으로 만들어졌고, 데모의 하루 먼저 입장 코드는 Fireshine 뉴스레터 구독자에게 배포됐다.[^pt1-end][^demo-coming] 출시 당일 Steam 게시판에서 지도 생성 방식을 묻는 질문에는 Fireshine 소속 담당자가 답했다.[^steam-qa] Feather가 설명한 층별 접근 방식의 테스트 운영과 크리에이터 접촉, 유료 광고와 짧은 영상은 위에 적었다.[^gdco] 판매 이정표는 EG7의 투자자 공시로도 나갔다.[^eg7-may] GamesIndustry.biz는 5월 19일 Fireshine 경영진 인터뷰를 실었으나 본문이 유료 구독자용이라 나는 도입부만 읽었다.[^gib]

각 활동이 결과에 얼마나 기여했는지는 공개된 자료로 가릴 수 없다. Feather는 플레이테스트의 반응이 스트리머와 짧은 영상의 자발적 확산을 불렀고, 그것이 Steam의 탐색 대기열과 추천 알고리즘의 노출로 이어졌다고 설명했지만, 이것은 퍼블리셔 측의 해석이다.[^gdco]

## 공개되지 않은 것들

개발비, 자금 조달 방식, 퍼블리싱 계약의 조건은 어디에도 공개되지 않았다. 프랑스의 공적 지원(CNC 게임 지원 기금 등)이나 Epic MegaGrant를 받았는지도 찾을 수 없었다. 세 프로토타입의 각 시기, 첫 비공개 테스트의 규모, 출시 시점 8명의 구성(정직원과 외주의 구분)도 나오지 않는다. 작곡가의 이름, 네트워크 제공사의 이름, 멀티플레이어의 전송 계층 구현은 밝혀지지 않았다. 두 번째 플레이테스트의 참가자 수(30만 명과 50만 명)와 데모 참가자 수(30만 명과 40만 명)는 개발팀의 기록 사이에 차이가 있다. 개발팀이 2026년 1월과 2월의 플레이테스트 패치 노트를 올렸던 Notion 페이지는 이 글을 쓰는 시점에 삭제되어 읽을 수 없었다. 프로토타입 단계의 화면은 공개된 적이 없다. 개발팀이 공개한 가장 이른 시각 자료는 2025년 7월의 콘셉트 스케치다.

## 가장 눈여겨본 것

가장 의외였던 것은 개발팀이 스스로 적어 둔 예상치들이었다. 첫 플레이테스트에서 동시 접속 300명을 예상했고, 출시 첫날에는 4천 명을, 첫 주 판매는 10만 장을, 리뷰 긍정 비율은 85%에서 90% 사이를 예상했다고 그들은 뒤에 밝혔다. 그 숫자들은 성공을 자랑하는 자리에 나온 것이지만, 내게는 다른 쪽으로 읽혔다. 8월 21일 공지의 "한 걸음 물러서서 준비가 됐는지 확인해야 했다"는 문장과 27일의 "쉬고 회복할 시간이 필요했다"는 문장은, 첫날 4천 명을 위해 지은 조직이 2만 명을 받은 뒤 넉 달 동안 무엇을 해야 했는지를 말한다. 두 프로그래머가 2,000건의 버그 보고를 받던 5월에서 오류 추적 도구가 크래시의 원인을 가려 주는 9월까지, 가장 크게 달라진 것은 새 기능보다 팀의 모양과 일하는 방식이었다. 이 게임의 개발 기록에서 가장 큰 변경 사항은 어쩌면 패치 노트에 적히지 않은 그 부분일지도 모른다.

![얼리 액세스 현재 빌드의 전투 장면. Steam 상점 스크린샷.](https://img.seosoyoung.eiaserinnys.me/images/far-far-west-dev-history/15-steam-screenshot-current.jpg)

## 사용한 자료

개발자와 퍼블리셔의 직접 발언이 담긴 자료를 먼저 두고, 공식 기록과 2차 보도를 뒤에 두었다. 같은 인터뷰를 옮겨 실은 기사는 세지 않았다.

- PC Gamer, Lincoln Carpenter, 2026-04-24. Meyssonnier와 Petit 인터뷰. 장르 전환의 계기, 서부와 로봇을 택한 이유, 떠 있는 손, 마법이 들어온 경위. [기사](https://www.pcgamer.com/games/fps/developers-of-steam-next-fests-wildly-popular-robot-wizard-cowboy-shooter-say-its-cowboy-robots-are-also-wizards-because-magic-is-always-cool/)
- Screen Rant, Chris Carter, 2026-05-04. Meyssonnier 인터뷰. 기차와 추출 구조의 우연한 형성, 색에 관한 취향, 피드백 철학, 출시 첫 주의 스트레스. [기사](https://screenrant.com/far-far-west-developer-interview/)
- GameDiscoverCo, Simon Carless, 2026-05-08. Meyssonnier와 Fireshine의 Rob Feather 인터뷰, 출시 전 위시리스트 그래프. 유료 뉴스레터이지만 이 게임을 다룬 부분은 무료 구간에 있었다. [글](https://newsletter.gamediscover.co/p/how-far-far-west-sold-500k-in-less)
- GamesRadar+, Andrew Brown, 2026-07-22. Petit 문답. 팀의 형성, 세 번의 프로토타입, 음악, Overwatch 연구. [기사](https://www.gamesradar.com/games/co-op/far-far-west-developer-q-and-a-like-with-pretty-much-everything-we-do-we-just-went-with-a-vibe/)
- Steam 공식 공지 50건, 2025-10-23부터 2026-09-07까지. 플레이테스트와 데모 공지, 월간 소식지 2회, 개발일지 3회, 패치 노트. Steam 뉴스 API로 전문을 읽었다. [공지 목록](https://steamcommunity.com/app/3124540/announcements/)
- 공식 Bluesky 계정 @farfarwest.bsky.social, 2025-06-08부터. 콘셉트 아트, 작업 중 영상, 테스트 통계. [계정](https://bsky.app/profile/farfarwest.bsky.social)
- Steam 상점 페이지. 얼리 액세스 안내문, 최소 사양, 개발사와 퍼블리셔. [페이지](https://store.steampowered.com/app/3124540/Far_Far_West/)
- Inside Unreal, "The Optimization Journey of 'Far Far West' (so far)", 2026-08-13. Ari Arnbjörnsson과 Tom Looman. 자막 전문을 확인했고 타임코드는 각주에 적었다. [영상](https://www.youtube.com/watch?v=kJPqrvB0fdo)
- Tom Looman, "GPU Profiling in Unreal Engine 5.7 for Far Far West", 2026-04-30. 영상과 글. [글](https://tomlooman.com/unreal-engine-optimization-farfarwest/)
- PC Gamer, Andy Chalk, 2026-05-01. 네트워크 문제의 Discord 발언과 베타 브랜치 우회. [기사](https://www.pcgamer.com/games/fps/hit-cowboy-co-op-shooters-servers-are-struggling-developer-says-its-service-provider-is-currently-drinking-mojitos-instead-of-helping/)
- NoFrag, 2025-06-11, 2025-10-24, 2026-01-11, 2026-04-13, 2026-05-11. 프랑스 매체의 쇼케이스와 테스트 보도, 1월 시연 현장 기술. [1월 기사](https://nofrag.com/new-game-de-nouveaux-playtests-pour-le-shooter-cooperatif-far-far-west/)
- actualitesjeuxvideo.fr, 2026-01-12. 두 번째 플레이테스트와 "오픈 개발" 소개. [기사](https://actualitesjeuxvideo.fr/new-game-showcase-2026-new-game-plus-showcase-2026-evil-raptor-fireshine-games-far-far-west-un-second-playtest-ouvert-est-disponible/)
- Fireshine Games 보도자료 2025-06-08(dlh.net 전재), EG7 투자자 공시 2026-04-10과 2026-05-18. 계약 발표, 위시리스트 58만, 판매 100만.
- Notion 공개 로드맵, 2026-09-12 열람. [로드맵](https://farfarwest.notion.site/)
- AFJV 기업 정보, MobyGames 크레디트, Evil Raptor 공식 사이트. 설립 시기, 소재지, 전작의 출시일과 퍼블리셔.

[^pcg-apr]: Lincoln Carpenter, "Developers of Steam Next Fest's wildly popular robot wizard cowboy shooter say its cowboy robots are also wizards because 'magic is always cool'", PC Gamer, 2026-04-24. <https://www.pcgamer.com/games/fps/developers-of-steam-next-fests-wildly-popular-robot-wizard-cowboy-shooter-say-its-cowboy-robots-are-also-wizards-because-magic-is-always-cool/>
[^sr]: Chris Carter, "How Far Far West Is Reinventing The Extraction Genre", Screen Rant, 2026-05-04. <https://screenrant.com/far-far-west-developer-interview/>
[^afjv]: AFJV 기업 정보 "Evil Raptor". 설립 2020년, 리옹. <https://www.afjv.com/societe/1232-evil-raptor.htm> 「Pumpkin Jack」 출시일과 퍼블리셔는 MobyGames 크레디트 기준.
[^moby]: MobyGames, Evil Raptor 회사 페이지. 「Akimbot」 2024-08-29, PLAION. <https://www.mobygames.com/company/61705/evil-raptor/>
[^gr]: Andrew Brown, "Far Far West developer Q&A", GamesRadar+, 2026-07-22. <https://www.gamesradar.com/games/co-op/far-far-west-developer-q-and-a-like-with-pretty-much-everything-we-do-we-just-went-with-a-vibe/>
[^steam-store]: Steam 상점 페이지의 얼리 액세스 안내문("Why Early Access?" 이하 개발팀 답변)과 시스템 요구 사항. 2026-09-12 열람. <https://store.steampowered.com/app/3124540/Far_Far_West/>
[^devlog-jul]: "Devlog - July", Steam 공지, 2026-07-10. <https://store.steampowered.com/news/app/3124540/view/1837955055356796>
[^devlog-sep]: "DEVLOG - SEPTEMBER", Steam 공지, 2026-09-05. <https://store.steampowered.com/news/app/3124540/view/1842846814449079>
[^frost-coming]: "Frostburn is Coming August 27!", Steam 공지, 2026-08-21. <https://store.steampowered.com/news/app/3124540/view/1841579228668773>
[^devlog-may]: "Devlog - May", Steam 공지, 2026-05-27. <https://store.steampowered.com/news/app/3124540/view/1833968530885317>
[^site]: Evil Raptor 공식 사이트 팀 소개. <https://www.evilraptor.com/>
[^gdco]: Simon Carless, "How Far, Far West sold >500k in less than 2 weeks...", GameDiscoverCo, 2026-05-08. <https://newsletter.gamediscover.co/p/how-far-far-west-sold-500k-in-less>
[^bulletin-jan]: "The FFW Bullet-in: January 2026", Steam 공지, 2026-01-31. <https://store.steampowered.com/news/app/3124540/view/1823191198608078>
[^steam-qa]: Steam 게시판 "Procedural generation?", 2026-04-28, Fireshine Games 담당자의 답변(개발자 답변으로 표시). <https://steamcommunity.com/app/3124540/discussions/0/807975542034961720/>
[^bsky-hands]: 공식 Bluesky, 2025-07-04. <https://bsky.app/profile/farfarwest.bsky.social/post/3lt5lz4fhkh2n>
[^bsky-chicken]: 공식 Bluesky, 2025-10-01. <https://bsky.app/profile/farfarwest.bsky.social/post/3m25bphgix62f>
[^bsky-spells]: 공식 Bluesky, 2025-07-28. <https://bsky.app/profile/farfarwest.bsky.social/post/3luzzeoecw52u>
[^pt2]: "Open Playtest #2 is NOW LIVE!", Steam 공지, 2026-01-08. <https://store.steampowered.com/news/app/3124540/view/1821288646578842>
[^bulletin-mar]: "The FFW Bullet-in: Feb-March 2026", Steam 공지, 2026-03-11. <https://store.steampowered.com/news/app/3124540/view/1826992588590205>
[^frost-out]: "FROSTBURN IS OUT NOW! - v0.2.0.2", Steam 공지, 2026-08-27. <https://store.steampowered.com/news/app/3124540/view/1842212951299982>
[^iu]: "The Optimization Journey of 'Far Far West' (so far) w/ Tom Looman & Ari Arnbjörnsson", Inside Unreal, 2026-08-13. 출연자 소개 3분 38초, 개발 빌드 입수 경위 10분 4초, "꽤 놀랐다" 14분 30초, UE 5.8 14분 57초, 지도 크기와 인스턴싱 26분 7초, World Partition을 쓰지 않는 이유 29분 56초, Nanite와 Lumen 30분 57초, Chaos Visual Debugger 1시간 24분 55초, 호스트 플레이어와 충돌 데이터 1시간 46분 41초, Enemy Optimizer 1시간 47분 34초, 감사 인사 2시간 14분 14초. <https://www.youtube.com/watch?v=kJPqrvB0fdo>
[^looman]: Tom Looman, "GPU Profiling in Unreal Engine 5.7 for Far Far West", 2026-04-30. 글과 영상. <https://tomlooman.com/unreal-engine-optimization-farfarwest/> / <https://www.youtube.com/watch?v=3qgd4glfIR0>
[^demo-coming]: "Next Fest Demo Coming 19th of Feb!", Steam 공지, 2026-02-13. <https://store.steampowered.com/news/app/3124540/view/1824644522839848>
[^frost-stats]: "Stats from the FROSTBURN update!", Steam 공지, 2026-09-03. <https://store.steampowered.com/news/app/3124540/view/1842846814444430>
[^patch-0220]: "FFW Early Access - Patch 0.2.0.20", Steam 공지, 2026-09-07. <https://store.steampowered.com/news/app/3124540/view/1842846814454046>
[^pt1]: "FREE Far Far West Open Playtest LIVE NOW", Steam 공지, 2025-10-23. <https://store.steampowered.com/news/app/3124540/view/1814309641450220>
[^pt1-halloween]: "Far Far West: Spooky Halloween Update!", Steam 공지, 2025-10-30. <https://store.steampowered.com/news/app/3124540/view/1815034432876494> 예상 300명은 같은 날 공식 Bluesky 게시물. <https://bsky.app/profile/farfarwest.bsky.social/post/3m4gfzqlbhi22>
[^pt1-end]: "The Far Far West Playtest Has Ended (For Now!)", Steam 공지, 2025-11-11. <https://store.steampowered.com/news/app/3124540/view/1815580768428360>
[^bsky-zukers]: 공식 Bluesky, 2025-11-13과 2025-11-20. <https://bsky.app/profile/farfarwest.bsky.social/post/3m5jdamdcln2y> / <https://bsky.app/profile/farfarwest.bsky.social/post/3m62jxmay5s2n>
[^bsky-boomerang]: 공식 Bluesky, 2025-11-26. <https://bsky.app/profile/farfarwest.bsky.social/post/3m6jzfpuyef2m>
[^nofrag-jan]: Estyaah, "[New Game+] De nouveaux playtests pour le shooter coopératif Far Far West", NoFrag, 2026-01-11. <https://nofrag.com/new-game-de-nouveaux-playtests-pour-le-shooter-cooperatif-far-far-west/>
[^bsky-extend]: 공식 Bluesky, 2026-01-15. <https://bsky.app/profile/farfarwest.bsky.social/post/3mchvs2oyxs2l>
[^demo-end]: "THANKS FOR PLAYING THE DEMO!!", Steam 공지, 2026-03-05. <https://store.steampowered.com/news/app/3124540/view/1826362059921210>
[^launch]: "Far Far West is OUT NOW!", Steam 공지, 2026-04-28. <https://store.steampowered.com/news/app/3124540/view/1830797770245289>
[^ea-date]: "Far Far West Early Access - APRIL 28TH!!", Steam 공지, 2026-04-09. <https://store.steampowered.com/news/app/3124540/view/1829528821307512>
[^eg7-apr]: EG7 보도자료, "Far Far West scheduled for release April 28, 2026 – over 580,000 wishlists and 98 percent positive reviews", 2026-04-10. <https://www.enadglobal7.com/>
[^bsky-roadmap]: 공식 Bluesky, 2026-04-27. <https://bsky.app/profile/farfarwest.bsky.social/post/3mkianhh3xb2u>
[^250k]: "250,000 copies sold in 48 hours!", Steam 공지, 2026-05-01. <https://store.steampowered.com/news/app/3124540/view/1831432155571340>
[^500k]: "500,000 COWBOYS ARE ROAMING THE FAR FAR WEST!", Steam 공지, 2026-05-04. <https://store.steampowered.com/news/app/3124540/view/1831432155576849>
[^1m]: "1 MILLION COWBOYS", Steam 공지, 2026-05-18. <https://store.steampowered.com/news/app/3124540/view/1832700592798258>
[^server]: "Ongoing server issue (RESOLVED!)", Steam 공지, 2026-05-01. <https://store.steampowered.com/news/app/3124540/view/1831432155571987>
[^pcg-server]: Andy Chalk, "Hit cowboy co-op shooter's servers are struggling, developer says its service provider 'is currently drinking mojitos instead of helping'", PC Gamer, 2026-05-01. <https://www.pcgamer.com/games/fps/hit-cowboy-co-op-shooters-servers-are-struggling-developer-says-its-service-provider-is-currently-drinking-mojitos-instead-of-helping/>
[^hotfix2]: "FFW Early Access - Hotfix 2 - Version 593", Steam 공지, 2026-05-02. <https://store.steampowered.com/news/app/3124540/view/1831432155572871>
[^hotfix1]: "FFW Early Access - Hotfix 1 - Version 583", Steam 공지, 2026-04-30. <https://store.steampowered.com/news/app/3124540/view/1831432155568748>
[^update1]: "FFW Early Access - UPDATE 1 - V644", Steam 공지, 2026-05-14. <https://store.steampowered.com/news/app/3124540/view/1832700592788508>
[^hotfix3]: "FFW Early Access - Hotfix 3 - Version 601", Steam 공지, 2026-05-04. <https://store.steampowered.com/news/app/3124540/view/1831432155576492>
[^patch-0113]: "FFW Early Access - PATCH 0.1.1.3", Steam 공지, 2026-06-05. <https://store.steampowered.com/news/app/3124540/view/1834602721191060>
[^job]: 3D 애니메이터 채용 공고(원격, 「Far Far West」), 구직 사이트 bebee 게재 2026-07-23. 리드 애니메이터와 협업, Blender와 UE5.
[^roadmap]: Far Far West 공개 로드맵(Notion), 2026-09-12 열람. <https://farfarwest.notion.site/>
[^eg7-may]: EG7 보도자료, "Far Far West Sells More Than One Million Steam Early Access Units", 2026-05-18. Fireshine Games는 Sold Out Sales and Marketing Ltd의 상호로 Steam 법적 고지에 표기된다.
[^pr-jun]: Fireshine Games 보도자료, "Giddy Up for a Bounty-Hunting, Chaotic Co-op Cowboy Shooter in 'Far Far West', Coming to Steam Early Access in 2026", 2025-06-08. dlh.net 전재. <https://dlh.net/en/news/giddy-up-for-a-bounty-hunting-chaotic-co-op-cowboy-shooter-in-far-far-west-coming-to-steam-early-access-in-2026/>
[^gib]: Alex Forbes-Calvin, "How Fireshine Games backed a winner with Far Far West", GamesIndustry.biz, 2026-05-19. 본문은 구독자용이라 도입부만 확인했다. <https://www.gamesindustry.biz/how-fireshine-games-backed-a-winner-with-far-far-west>
