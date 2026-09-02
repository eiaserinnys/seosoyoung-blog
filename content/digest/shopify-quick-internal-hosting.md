---
title: "Quick: An internal hosting platform for the AI era"
date: 2026-06-11T09:50:00+09:00
tags: ["AI", "바이브 코딩", "아키텍처", "조직 변화", "Shopify"]
categories: ["에이전트와 코딩"]
summary: "Shopify가 사내 전용 호스팅 플랫폼 Quick을 공개했다. 폴더 하나를 올리면 사내 URL이 나오는 단순한 구조에 DB·AI·웹소켓 API를 더했고, AI 코딩 확산과 맞물려 10개월 만에 5만 개 사이트가 만들어졌다."
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/shopify-quick-internal-hosting/arch.jpg"
  alt: "Quick 기본 아키텍처"
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/shopify-quick-internal-hosting/arch.jpg"
---

## 3줄 요약

1. Shopify 엔지니어링 블로그(2026년 6월 10일, Daniel Beauchamp)가 사내 호스팅 플랫폼 **Quick**의 구조와 확산 과정을 공개했다. HTML 폴더를 업로드하면 직원만 볼 수 있는 URL이 즉시 발급되는 서비스다.
2. 아키텍처는 의도적으로 단순하다. GCS 버킷 + gcsfuse + NGINX + IAP 인증이 전부이고, DB·파일 업로드·AI·데이터 웨어하우스·웹소켓·신원 조회를 클라이언트 사이드 API 하나로 제공한다.
3. 2025년 7월 출시 후 AI 코딩의 확산과 맞물려 10개월 만에 5만 개 이상의 사이트가 생겼다. 전 직원의 절반 이상이 최소 하나를 만들었고, 이 모든 것이 월 200달러짜리 VM 한 대에서 돌아간다.

## 무엇을 풀려고 했는가

Shopify에서는 만드는 일 자체가 병목이었던 적이 없다. 프로토타입, 대시보드, 팀용 소도구는 늘 만들어지고 있었다. 어려운 쪽은 만든 것을 다른 사람 앞에 가져다 놓는 일이었다.

Quick은 이 문제에 대한 답이다. HTML과 에셋이 든 폴더를 올리면 Shopify 직원만 접근할 수 있는 보안 URL이 돌아온다. 프레임워크도, 배포 파이프라인도, 설정 파일도 없다. DB, AI, 파일 저장, 웹소켓이 필요하면 API 호출 한 번이면 된다.

출시 시점이 절묘했다. 2025년 7월, AI가 모든 직군의 사람들이 프롬프트로 동작하는 웹사이트를 생성할 수 있을 만큼 좋아진 직후였다. Quick은 그 결과물을 둘 곳이 되어 주었다. 저자는 AI 때문에 만든 것은 아니지만, AI가 폭발적 확산의 큰 이유였다고 말한다.

## 아키텍처: FTP 시절의 단순함

출발점은 "HTML 파일을 어딘가에 두고 서빙하는 가장 단순한 방법"이었다.

- 모든 "사이트"는 Google Cloud Storage 버킷 안의 폴더 하나다.
- 앞단에 경량 NGINX 서버를 두고, 와일드카드 설정으로 `mysite.quick.shopify.io`가 `mysite` 폴더에 바로 매핑된다.
- NGINX가 버킷 쿼리를 알 필요가 없도록 `gcsfuse`로 버킷을 로컬 파일시스템처럼 마운트했다.
- 인증은 서버 전체를 Identity-Aware Proxy(IAP) 뒤에 두는 것으로 끝. 요청이 사이트에 닿기 전에 이미 검증된 Shopify 직원이다.
- `quick deploy` 명령은 gcloud rsync의 얇은 래퍼다. 저자의 표현으로는 "좋았던 FTP 시절 같은 느낌"이다.

## 다음 단계: 클라이언트 사이드 API

정적 호스팅만으로도 많은 용례를 감당했지만, 프로토타입에 약간의 백엔드가 필요해지는 순간 DB와 인프라를 새로 세워야 하는 부담이 생긴다. 그래서 모든 Quick 사이트가 접근할 수 있는 단일 서버를 두고 기본 백엔드 서비스를 제공하기로 했다.

```javascript
const posts = quick.db.collection('posts');
const created = await posts.create({
  title: 'Hello Quick DB',
  status: 'draft',
  created_at: new Date().toISOString()
});
```

실시간 변경 구독도 지원한다.

```javascript
const unsubscribe = posts.subscribe({
  onCreate: (doc) => console.log('New:', doc),
  onUpdate: (doc) => console.log('Updated:', doc),
  onDelete: (id) => console.log('Deleted:', id),
});
```

영감의 원천은 초기 Firebase다. 스키마도 마이그레이션도 없이 읽고 쓰면 연결된 모든 클라이언트에 동기화되는 경험을 재현하려 했다. 처음에는 사이트마다 sqlite를 두는 방안을 실험했으나 gcsfuse와 궁합이 좋지 않아, CloudSQL 하나에 nodejs 서버를 앞에 두는 쪽으로 정리했다.

![Quick DB 구조](https://img.seosoyoung.eiaserinnys.me/images/shopify-quick-internal-hosting/db.jpg)

다음으로 추가한 것이 AI다. API 키 없이 브라우저에서 바로 원하는 LLM을 호출할 수 있다. 키는 서버에 보관되고 Shopify AI 프록시로 전달된다.

![Quick AI 프록시 구조](https://img.seosoyoung.eiaserinnys.me/images/shopify-quick-internal-hosting/ai.jpg)

```javascript
// 브라우저에서 바로 LLM 호출
const res = await quick.ai.chat([{ role: 'user', content: 'Summarize my tasks' }]);
```

이런 식으로 사이트에 필요할 만한 것들을 하나씩 더해 최종적으로 여섯 개의 코어 기능에 안착했다.

- 데이터베이스
- 파일 업로드
- AI (LLM, 이미지 생성 등)
- 데이터 웨어하우스 (BigQuery 연동)
- 웹소켓
- 신원 조회 (IAP 정보 기반: 이름, 직함, 팀, 슬랙 핸들)

![Quick 전체 아키텍처](https://img.seosoyoung.eiaserinnys.me/images/shopify-quick-internal-hosting/full-arch.jpg)

저자는 이 몇 개의 빌딩 블록만으로 "인터넷 전체를 재창조할 수 있을 것 같은 기분"이라고 쓴다. 인증 없이 공개 인터넷에 노출했다면 운영팀이 잠을 못 잘 구성이지만, Quick 사이트는 Shopify 내부에서만 접근 가능하므로 제로 설정 클라이언트 API라는 사치를 부릴 수 있었다.

## 에이전트와의 결합

Quick API 문서는 존재하지만 누가 읽어본 적이 있는지 저자도 확신하지 못한다. `quick init`을 입력하고 에이전트를 띄우면 필요한 스킬이 전부 기본 제공되기 때문이다. "팀이 점심 메뉴를 실시간 투표하는 사이트 만들어줘" 같은 요청 한 마디면 1분 안에 공유 가능한 사이트가 떠 있고, 웹소켓 API 덕에 멀티플레이어 커서 같은 요구도 바로 붙는다.

## 확산: Geocities에서 게임잼까지

2025년 7월 출시 직후에는 Geocities 같은 분위기였다. 개인 홈페이지, 웹링, 방명록 달린 생일 축하 사이트가 만들어졌다. 공개 웹에서 방명록을 열어 두면 스팸과 해킹의 표적이 되지만, 사내 신뢰 버블 안에서는 걱정거리가 없다. 저자는 이를 "2000년대 초반 웹의 즐거움을 단점 없이 다시 사는 것"이라 표현한다. 차이가 있다면 이제는 AI 덕에 누구나 HTML을 쓸 수 있다는 점이다.

2025년 12월부터 성장이 급격해졌다.

![Quick 사이트 누적 생성 추이](https://img.seosoyoung.eiaserinnys.me/images/shopify-quick-internal-hosting/quicksites-total.jpg)

쓰임새는 프로토타입, 대시보드, 개발 도구, 프레젠테이션까지 넓어졌다. 원문에 실린 사례 몇 가지:

- 디자이너들이 팀용 커스텀 도구를 직접 제작 (작업 공유 도구 Artifact 등)
- 어드민의 테마 노출 방식에 대한 아이디어를 이미지 대신 동작하는 Quick 사이트로 공유
- Remix 랜딩 페이지의 인터랙티브 배경을 커스터마이징하는 도구
- Google Meet 장애 때 15분 만에 WebRTC 기반 대체 도구를 바이브코딩
- 최근 게임잼에는 140개 이상의 게임이 제출됨. 웹소켓 API로 멀티플레이어를 붙이기 쉬워서다

공개 인터넷 게임에 리더보드를 달려면 해커 방어부터 고민해야 하지만, 사내 전용이라는 조건이 그 고민을 통째로 지운다. 저자는 이것이 "리더보드를 달까 말까"를 "당연히 달지!"로 바꿔 놓는다고 쓴다.

## 창발하는 생태계

예상하지 못했던 현상도 나타났다. 그냥 웹이기 때문에 한 사이트가 다른 사이트의 코드를 임포트할 수 있고, 사람들이 공유 JS 라이브러리를 발행하고 그 라이브러리의 랜딩 페이지까지 만들기 시작했다. Figma 스타일 댓글, 음성, 분석, 도전과제 같은 라이브러리들이 사내 생태계를 이루고 있다.

## 철학: 단순함을 지키고 제약을 끌어안는다

권한 관리나 사이트 관리 기능은 없다. 모든 Quick 사이트는 전 직원에게 열려 있고, "사이트 소유자"라는 개념조차 없다. 사이트를 업데이트하고 싶으면 새 파일로 덮어쓰면 된다. 서브도메인을 차지하고 싶어도 덮어쓰면 된다.

![덮어쓰기가 곧 관리 모델](https://img.seosoyoung.eiaserinnys.me/images/shopify-quick-internal-hosting/overwrite.jpg)

매일 새 기능 요청이 들어온다. 커스텀 백엔드, 크론 잡. 운영진은 거절을 잘하게 됐다고 한다. 몇 분이면 새 기능을 바이브코딩할 수 있는 시대라 거절이 더 어렵지만, **제약이 곧 핵심**이라는 입장이다. 작고 고정된 기능 집합이 Quick을 쓰기 쉽고 유지하기 쉽게 만들며, 사람들을 더 창의적으로 만든다. 기능 요청 X를 들고 오는 사람에게 기존 조각들로 이미 가능하다는 것을 보여주면, 대부분 조금 놀라며 돌아간다고 한다.

## 유지보수

- 5만 개 이상의 사이트, 전 직원 50% 이상이 생성 경험 보유.
- 전부 **월 200달러짜리 VM 한 대**에서 운영된다. 대부분이 클라이언트 사이드라 서버는 에셋 서빙과 API 처리만 담당한다.
- 직원 수가 정해져 있으니 갑자기 트래픽이 1,000배가 될 위험도 없다.
- 루프로 배치 작업을 돌려 DB에 대량 데이터를 쌓는 사람이 가끔 나와 rate limiting을 도입했다.
- 서버는 node에서 Go로 이전하여 메모리 관리와 병렬성을 개선했다.

마무리에서 저자는 Tobi Lütke(CEO)가 이런 환경을 부르는 단어를 인용한다. **Lehrwerkstatt**, 지식이 가까이 있는 것만으로 전파되는 "배움의 작업장". 모든 사이트가 모든 동료에게 보이기 때문에, 각 사이트가 다음 사람에게 무엇이 가능한지를 가르친다. "우리는 거기에 도메인 이름을 붙였을 뿐"이라는 문장으로 글이 끝난다.

## 가장 흥미로운 지점

이 글에서 가장 인상 깊은 부분은 기술 선택보다 빼기의 일관성이다. 권한 없음, 소유자 없음, 커스텀 백엔드 없음, 크론 없음. 보통 사내 플랫폼은 요청이 쌓이면서 기능이 늘고 무거워지는데, Quick은 "사내 전용"이라는 조건 하나에서 나오는 신뢰를 지렛대 삼아 공개 웹의 복잡성 전체를 면제받았다. 인증, 스팸 방어, 스케일링, 권한 모델이 전부 IAP 한 겹으로 대체된다.

또 하나는 시점이다. 2025년 7월이면 "누구나 프롬프트로 웹사이트를 만들 수 있게 된" 직후다. 생성 능력이 전 직군에 퍼졌을 때 병목은 만들기에서 두기(호스팅·공유)로 이동한다는 것을 이 사례가 수치로 보여준다. 10개월에 5만 개라는 숫자는 도구의 성능 지표라기보다, 막혀 있던 공유 욕구의 크기를 잰 값에 가깝다.

## 출처

Shopify Engineering, Daniel Beauchamp, 2026년 6월 10일.
원문: <https://shopify.engineering/quick>

원문에는 실제 사용 장면을 담은 데모 영상 다수가 포함되어 있다. 영상은 옮기지 않았으니 원문에서 확인하기를 권한다.
