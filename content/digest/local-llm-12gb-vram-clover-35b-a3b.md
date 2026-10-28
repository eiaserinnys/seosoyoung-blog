---
title: "12GB VRAM 게이밍 PC의 로컬 LLM 실측: 확산 언어 모델 Clover-35B-A3B"
date: 2026-10-29T01:15:00+09:00
draft: false
summary: "10월 28일 공개된 확산 언어 모델 Clover-35B-A3B-Preview를 RTX 3080 Ti(12GB VRAM) PC에서 4비트로 실행했다. 일반 디코딩은 초당 42.72토큰으로 이 PC에서 돌린 모델 가운데 가장 빨랐고, 확산 방식의 자기 추측 생성은 초당 6.7에서 24.6토큰으로 일반 디코딩보다 느렸다."
categories: ["모델과 연구"]
subjects: ["추론 효율과 로컬 실행"]
tags: ["로컬 LLM", "확산 모델", "MoE", "양자화", "벤치마크"]
author: "서소영"
sidenotes: true
ShowToc: true
TocOpen: false
cover:
  image: "https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-clover-35b-a3b/01-cover.png"
  alt: "게이밍 PC 본체 옆에 앉아 그래픽카드에서 돋아난 하늘색 세잎클로버를 바라보는 치비 서소영과, 본체 앞에서 빠르게 흘러나오는 종이 토큰 띠"
  og_focus: "40%"
  relative: false
images:
  - "https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-clover-35b-a3b/01-cover.png"
---

<style>
.clv-viz { margin: 1.75rem 0; padding: 1.1rem 1.2rem; background: var(--bg-2); border: 1px solid var(--rule); box-sizing: border-box; font-family: var(--sans); }
.clv-viz-title { font-size: 0.95rem; font-weight: 700; color: var(--ink); margin: 0 0 0.7rem 0; }
.clv-legend { display: flex; flex-wrap: wrap; gap: 0.5rem 1rem; font-size: 0.8rem; color: var(--ink-2); margin-bottom: 0.95rem; }
.clv-key { display: inline-flex; align-items: center; gap: 0.35rem; }
.clv-sw { width: 12px; height: 12px; display: inline-block; flex-shrink: 0; box-sizing: border-box; }
.clv-sw-acc { background: var(--accent); }
.clv-sw-ink { background: var(--ink-2); }
.clv-sw-muted { background: var(--ink-3); }
.clv-sw-ram { background: repeating-linear-gradient(135deg, var(--ink-3) 0 2px, transparent 2px 5px); border: 1px solid var(--ink-3); }
.clv-rows { display: flex; flex-direction: column; gap: 1.05rem; }
.clv-head { display: flex; justify-content: space-between; align-items: baseline; gap: 0.25rem 0.6rem; flex-wrap: wrap; margin-bottom: 0.35rem; }
.clv-name { font-size: 0.88rem; font-weight: 600; color: var(--ink); }
.clv-val { font-family: var(--sans); font-variant-numeric: tabular-nums; font-size: 0.8rem; color: var(--ink-2); white-space: nowrap; }
.clv-val strong { font-family: var(--mono); color: var(--ink); font-size: 0.95rem; }
.clv-best .clv-val strong { color: var(--accent); }
.clv-tag { display: inline-block; font-family: var(--sans); font-size: 0.72rem; font-weight: 600; padding: 0 0.35rem; margin-left: 0.35rem; border: 1px solid var(--ink-2); color: var(--ink-2); line-height: 1.5; }
.clv-layers { display: flex; height: 10px; border: 1px solid var(--rule); margin-bottom: 0.3rem; }
.clv-l-ram { background: repeating-linear-gradient(135deg, var(--ink-3) 0 2px, transparent 2px 5px); }
.clv-l-gpu { background: var(--accent); }
.clv-track { position: relative; height: 14px; background: var(--bg); border: 1px solid var(--rule); box-sizing: border-box; }
.clv-fill { height: 100%; background: var(--ink-2); min-width: 3px; }
.clv-fill-acc { background: var(--accent); }
.clv-fill-muted { background: var(--ink-3); }
.clv-range { position: absolute; top: 0; bottom: 0; background: var(--ink-3); min-width: 4px; }
.clv-range-acc { background: var(--accent); }
.clv-sub { font-size: 0.78rem; color: var(--ink-2); margin-top: 0.3rem; font-family: var(--sans); font-variant-numeric: tabular-nums; }
.clv-axis { display: flex; justify-content: space-between; font-family: var(--sans); font-variant-numeric: tabular-nums; font-size: 0.74rem; color: var(--ink-2); margin-top: 0.4rem; }
.clv-pair { display: flex; flex-direction: column; gap: 0.3rem; }
.clv-line { display: grid; grid-template-columns: 4.4rem 1fr 3.4rem; align-items: center; gap: 0.5rem; }
.clv-env { font-size: 0.78rem; color: var(--ink-2); }
.clv-num { font-family: var(--mono); font-size: 0.82rem; color: var(--ink); text-align: right; white-space: nowrap; }
.clv-na { font-family: var(--sans); font-size: 0.74rem; color: var(--ink-2); }
.clv-axis-pair { display: grid; grid-template-columns: 4.4rem 1fr 3.4rem; gap: 0.5rem; margin-top: 0.4rem; }
.clv-axis-pair .clv-axis { margin-top: 0; }
.clv-resp { margin: 1.2rem 0; border: 1px solid var(--rule); background: var(--bg); }
.clv-resp-head { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 0.3rem 0.6rem; padding: 0.65rem 0.9rem; background: var(--bg-2); border-bottom: 1px solid var(--rule); }
.clv-resp-title { font-size: 0.88rem; font-weight: 700; color: var(--ink); }
.clv-resp-meta { font-family: var(--mono); font-size: 0.76rem; color: var(--ink-2); }
.clv-resp-body { padding: 0.85rem 1rem; font-size: 0.92rem; line-height: 1.75; color: var(--ink); word-break: keep-all; overflow-wrap: anywhere; }
.clv-resp-body p { margin: 0 0 0.55rem 0; }
.clv-resp-body p:last-child { margin-bottom: 0; }
mark.clv-quirk { background: var(--bg-2); color: inherit; font-weight: 700; padding: 0 0.15rem; text-decoration: underline wavy var(--ink-2); text-underline-offset: 4px; }
details.clv-resp > summary.clv-resp-head { cursor: pointer; list-style: none; border-bottom: none; }
details.clv-resp[open] > summary.clv-resp-head { border-bottom: 1px solid var(--rule); }
details.clv-resp > summary.clv-resp-head::-webkit-details-marker { display: none; }
.clv-fold::after { content: "펼치기 ▼"; font-size: 0.76rem; color: var(--ink-2); font-weight: 600; }
details.clv-resp[open] .clv-fold::after { content: "접기 ▲"; }
@media (max-width: 640px) {
  .clv-viz { padding: 0.95rem 0.85rem; }
  .clv-line, .clv-axis-pair { grid-template-columns: 3.9rem 1fr 3rem; gap: 0.4rem; }
  .clv-resp-head { padding: 0.6rem 0.75rem; }
  .clv-resp-body { padding: 0.75rem 0.8rem; font-size: 0.9rem; }
}
</style>

## 3줄 요약

1. 10월 28일 공개된 확산 언어 모델 `Clover-35B-A3B-Preview`를 4비트(`Q4_K_M`, 20.2GB)로 양자화했다. 그리고 [앞 글](https://seosoyoung.eiaserinnys.me/digest/local-llm-12gb-vram-deepseek-qwen38-27b/)과 같은 PC(RTX 3080 Ti 12GB VRAM, 32GB RAM)에서 llama.cpp 포크로 실행했다.
2. Windows에서 24개 층의 전문가 가중치를 시스템 RAM에 두고 일반 디코딩으로 실행하자 초당 42.72토큰이 나왔고, 이 PC에서 돌린 모델 가운데 가장 빨랐다. 확산 모델의 자기 추측 생성(`draft-self`)은 수락률이 100%로 표시됐는데도 초당 6.7에서 24.6토큰으로 일반 디코딩보다 느렸다.
3. 코딩과 확률 계산은 두 환경 모두 정답을 냈고, 한국어 단편에는 `으shy`, `다른話야`처럼 영어와 한자가 섞였다. Clover는 토큰마다 약 3B만 계산하는 MoE 구조 덕분에 이 PC에서 빨랐고, 확산 생성 기능은 속도에 보탬이 되지 않았다.

## Clover-35B-A3B는 어떤 모델인가

지금 널리 쓰는 언어 모델은 대부분 자기회귀 방식이다. 앞에 나온 토큰을 모두 보고 다음 토큰 하나를 고르는 계산을 응답이 끝날 때까지 되풀이한다. 확산 언어 모델은 응답을 마스크 토큰(아직 정하지 않은 빈 토큰)으로 채워 두고, 여러 단계 동안 확신이 높은 토큰부터 동시에 확정한다. 한 번의 계산으로 토큰 여러 개를 정할 수 있어 생성이 빠르다는 것이 이 방식의 장점이다.

DiffuSpace가 10월 28일 Apache-2.0 라이선스로 공개한 `Clover-35B-A3B-Preview`는 블록 확산 방식을 쓴다. 응답을 32토큰 블록 단위로 생성하고, 같은 블록의 토큰끼리는 양방향 어텐션으로 서로를 참조한다. 확신도가 0.95보다 높은 토큰은 한꺼번에 확정하고, 그런 토큰이 없으면 확신도가 가장 높은 토큰 하나를 확정한다. 완성된 블록은 다음 블록의 앞 문맥이 된다.

기반 모델은 알리바바의 `Qwen3.6-35B-A3B`다. 전체 파라미터는 350억 개(35B)지만, 전문가 혼합(MoE) 구조라서 토큰 하나를 계산할 때 쓰는 파라미터는 약 30억 개(3B)다. 40개 층마다 라우팅 전문가 256개 가운데 8개와 공유 전문가 1개가 계산에 참여한다. 앞 문맥을 순환 상태로 압축하는 Gated DeltaNet 층과 일반 어텐션 층을 섞은 구조이고, 문맥 길이는 128K 토큰이다.

공식 권장 서빙 엔진은 SGLang이고, 블록 확산 생성과 자기 추측 디코딩을 모두 지원한다. 개인 PC에서 흔히 쓰는 llama.cpp는 아직 정식 지원 전이다. 10월 28일 제출된 llama.cpp PR #31306이 Clover의 변환과 실행을 지원하지만, 블록 확산 생성은 구현하지 않았고 자기 추측 디코딩 모드 `draft-self`만 지원한다.

추측 디코딩은 작은 초안 모델이 토큰 여러 개를 먼저 제안하고, 큰 모델이 한 번의 계산으로 그 후보를 검증해 맞은 앞부분을 한꺼번에 확정하는 기법이다. `draft-self`는 초안 모델을 따로 두지 않는다. Clover가 마스크 블록을 채워 후보를 제안하고, 같은 Clover가 그 후보를 자기회귀 순서로 검증한다.

<figure class="blog-diagram" style="margin: 2rem 0;">
<style>.blog-diagram .diagram-svg-desktop { display: block; width: 100%; height: auto; background: var(--bg-2); border: 1px solid var(--rule); } .blog-diagram .diagram-svg-mobile { display: none; width: 100%; height: auto; background: var(--bg-2); border: 1px solid var(--rule); } @media (max-width: 640px) { .blog-diagram .diagram-svg-desktop { display: none; } .blog-diagram .diagram-svg-mobile { display: block; } }</style>
<svg class="diagram-svg-desktop" viewBox="0 0 720 236" role="img" aria-label="draft-self 생성 흐름. 1 마스크 블록, 2 Clover가 블록을 한 번에 채워 후보 제안, 3 같은 Clover가 앞에서부터 검증, 4 맞은 토큰만 확정하고 다음 블록에서 반복" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="clv-arr-ink" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="clv-arr-acc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="720" height="236" fill="var(--bg-2)"/>
  <rect x="20" y="24" width="150" height="140" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="34" y="50" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 마스크 블록</text>
  <rect x="34" y="70" width="18" height="18" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="56" y="70" width="18" height="18" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="78" y="70" width="18" height="18" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="100" y="70" width="18" height="18" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="122" y="70" width="18" height="18" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="34" y="122" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">빈 토큰 최대 15개</text>
  <text x="34" y="140" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">(이번 실측 기본값)</text>
  <rect x="196" y="24" width="150" height="140" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="210" y="50" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">2. 한 번에 채움</text>
  <rect x="210" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="232" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="254" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="276" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="298" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <text x="210" y="122" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">Clover가 후보 제안</text>
  <text x="210" y="140" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">(계산 한 번)</text>
  <rect x="372" y="24" width="150" height="140" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="386" y="50" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">3. 앞에서부터 검증</text>
  <rect x="386" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="408" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="430" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="452" y="70" width="18" height="18" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="474" y="70" width="18" height="18" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1"/>
  <path d="M 390 79 l 4 4 l 7 -8 M 412 79 l 4 4 l 7 -8 M 434 79 l 4 4 l 7 -8 M 456 79 l 4 4 l 7 -8" fill="none" stroke="var(--accent)" stroke-width="1.6"/>
  <path d="M 478 74 l 10 10 M 488 74 l -10 10" fill="none" stroke="var(--ink-2)" stroke-width="1.6"/>
  <text x="386" y="122" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">같은 Clover가 검증</text>
  <text x="386" y="140" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">(틀린 토큰부터 버림)</text>
  <rect x="548" y="24" width="152" height="140" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="562" y="50" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent)">4. 맞은 토큰 확정</text>
  <rect x="562" y="70" width="18" height="18" fill="var(--accent)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="584" y="70" width="18" height="18" fill="var(--accent)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="606" y="70" width="18" height="18" fill="var(--accent)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="628" y="70" width="18" height="18" fill="var(--accent)" stroke="var(--accent)" stroke-width="1"/>
  <text x="562" y="122" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">확정한 토큰이</text>
  <text x="562" y="140" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">다음 블록의 앞 문맥</text>
  <line x1="170" y1="94" x2="192" y2="94" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#clv-arr-ink)"/>
  <line x1="346" y1="94" x2="368" y2="94" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#clv-arr-ink)"/>
  <line x1="522" y1="94" x2="544" y2="94" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#clv-arr-acc)"/>
  <path d="M 624 164 L 624 196 L 95 196 L 95 168" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#clv-arr-acc)"/>
  <text x="360" y="220" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">다음 블록에서 1부터 반복</text>
</svg>
<svg class="diagram-svg-mobile" viewBox="0 0 350 448" role="img" aria-label="draft-self 생성 흐름(모바일). 마스크 블록, 한 번에 채움, 앞에서부터 검증, 맞은 토큰 확정 순서로 내려가고 다음 블록에서 반복" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="clv-arr-ink-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--ink-2)"/></marker>
    <marker id="clv-arr-acc-m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--accent)"/></marker>
  </defs>
  <rect width="350" height="448" fill="var(--bg-2)"/>
  <rect x="16" y="16" width="318" height="76" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="44" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">1. 마스크 블록</text>
  <text x="30" y="66" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">빈 토큰 최대 15개</text>
  <rect x="214" y="40" width="16" height="16" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="234" y="40" width="16" height="16" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="254" y="40" width="16" height="16" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="274" y="40" width="16" height="16" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <rect x="294" y="40" width="16" height="16" fill="var(--bg)" stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="175" y1="92" x2="175" y2="114" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#clv-arr-ink-m)"/>
  <rect x="16" y="118" width="318" height="76" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="146" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">2. 한 번에 채움</text>
  <text x="30" y="168" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">Clover가 후보 제안</text>
  <rect x="214" y="142" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="234" y="142" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="254" y="142" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="274" y="142" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="294" y="142" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <line x1="175" y1="194" x2="175" y2="216" stroke="var(--ink-2)" stroke-width="1.5" marker-end="url(#clv-arr-ink-m)"/>
  <rect x="16" y="220" width="318" height="76" fill="var(--bg)" stroke="var(--rule-strong)" stroke-width="1.5"/>
  <text x="30" y="248" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--ink)">3. 앞에서부터 검증</text>
  <text x="30" y="270" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">같은 Clover가 검증</text>
  <rect x="214" y="244" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="234" y="244" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="254" y="244" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="274" y="244" width="16" height="16" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="294" y="244" width="16" height="16" fill="var(--bg)" stroke="var(--ink-2)" stroke-width="1"/>
  <path d="M 217 252 l 4 4 l 6 -7 M 237 252 l 4 4 l 6 -7 M 257 252 l 4 4 l 6 -7 M 277 252 l 4 4 l 6 -7" fill="none" stroke="var(--accent)" stroke-width="1.5"/>
  <path d="M 298 248 l 8 8 M 306 248 l -8 8" fill="none" stroke="var(--ink-2)" stroke-width="1.5"/>
  <line x1="175" y1="296" x2="175" y2="318" stroke="var(--accent)" stroke-width="1.5" marker-end="url(#clv-arr-acc-m)"/>
  <rect x="16" y="322" width="318" height="76" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.5"/>
  <text x="30" y="350" font-family="var(--sans)" font-size="13" font-weight="700" fill="var(--accent)">4. 맞은 토큰 확정</text>
  <text x="30" y="372" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">다음 블록의 앞 문맥</text>
  <rect x="214" y="346" width="16" height="16" fill="var(--accent)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="234" y="346" width="16" height="16" fill="var(--accent)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="254" y="346" width="16" height="16" fill="var(--accent)" stroke="var(--accent)" stroke-width="1"/>
  <rect x="274" y="346" width="16" height="16" fill="var(--accent)" stroke="var(--accent)" stroke-width="1"/>
  <text x="175" y="428" text-anchor="middle" font-family="var(--sans)" font-size="11" fill="var(--ink-2)">다음 블록에서 1부터 반복</text>
</svg>
<figcaption style="margin-top: 0.65rem; font-size: 0.85rem; color: var(--ink-2); text-align: center; line-height: 1.5;">llama.cpp <code>draft-self</code>의 생성 흐름. 제안과 검증을 같은 모델이 모두 맡는다.</figcaption>
</figure>

공식 블로그에 따르면 Clover는 SWE-bench Verified 73.6점을 비롯해 에이전트 평가 여섯 개에서 같은 크기의 자기회귀 모델 Qwen3.6-35B-A3B보다 높은 점수를 받았다. NVIDIA GB300 한 장에서 BF16, 배치 크기 1로 내부 에이전트 과제를 처리할 때 초당 680토큰, H200 한 장에서는 초당 515토큰을 생성했다. 16GB VRAM의 RTX 5070 Ti에서는 INT4 양자화로 MATH-500 문제를 초당 101.8토큰으로 풀었다고 한다.[^official-speed]

[^official-speed]: 공식 속도 수치는 블록 확산 생성 기준이다. RTX 5070 Ti 사례에는 어떤 추론 엔진을 썼는지 적혀 있지 않다.

PR 작성자는 모든 가중치를 VRAM에 적재한 H200에서 `draft-self` 구현이 초당 약 32토큰을 낸다고 적었고, 성능 최적화는 이후 PR로 미뤘다.

## 실험 환경과 준비 과정

측정에 쓴 PC는 앞 글과 같다. CPU는 16코어 24스레드인 Intel Core i9-12900K이고, 메모리는 DDR5-4800 16GB 두 개로 총 32GB다. 그래픽카드는 VRAM이 12GB인 RTX 3080 Ti이며, 저장 장치는 Samsung 990 PRO 4TB NVMe다. WSL2(Ubuntu, RAM 15.5GiB 할당)와 Windows 네이티브에서 같은 포크를 각각 빌드해 실행했다.

모든 측정은 4비트 `Q4_K_M` 모델로 했다. 매번 확률이 가장 높은 토큰만 고르는 탐욕 디코딩(greedy)을 썼고, 문맥 길이는 8,192토큰이며 사고 모드는 껐다(채팅 틀에 빈 `<think>` 블록을 넣었다). 프롬프트는 한국어 단편, 파이썬 코딩, 확률 계산 세 가지이고 각각 한 번씩 실행했다.[^not-measured]

[^not-measured]: 측정하지 않은 항목은 사고 모드, 8K 토큰보다 긴 문맥, SGLang의 블록 확산 생성, 다른 양자화 수준이다. 프롬프트마다 한 번씩만 실행했으므로 응답 품질 평가는 인상 수준이다.

공개 당일이라 미리 양자화된 GGUF 파일이 없었다. 69GB인 BF16 원본은 초당 55MB로 약 45분 동안 내려받았다. 이어서 `Maphist0/llama.cpp-pub` 포크의 `dev-clover` 브랜치(커밋 `4838ffb`)를 CUDA로 빌드하고, 원본을 BF16 GGUF로 변환했다. 변환한 파일은 65GiB였다. 이 파일을 `Q4_K_M`(20.2GB, 가중치당 평균 4.88비트)으로 양자화하는 데 575초가 걸렸다. 그 과정에서 다섯 가지 문제가 생겼다.

| 증상 | 원인 | 해결 |
|---|---|---|
| 변환이 10분 실행 제한을 초과 | 명령당 실행 시간 상한 | 출력을 13조각으로 분할해 병렬 변환 |
| WSL에서 D 드라이브 쓰기 실패 | 9p가 512MB 초과 텐서를 잘라 씀 | WSL 내부 디스크에 쓴 뒤 복사 |
| draft-self 실행 거부 | GGUF에 든 반복 억제 기본값 | 반복 억제를 끔 |
| Strata로 실행 불가 | Clover 구조 미지원 | 포크를 Windows에서 직접 빌드 |
| nvcc가 오류 문구 없이 종료 | TEMP 경로의 한글 | TEMP를 영문 경로로 변경 |

조각별 변환은 4조각에 92초가 걸렸다. WSL에서 D 드라이브는 9p 파일 시스템으로 연결되는데, 읽기 속도는 단일 스트림 초당 165MB, 4개 병렬 초당 545MB였다. 앞 글에서 쓴 Strata의 엔진과, 함께 설치된 llama.cpp b11871은 모두 Clover 모델 구조(`clover_moe`)를 지원하지 않았다. 그래서 Windows에서 네이티브로 실행하려고 같은 포크를 Visual Studio 2022 빌드 도구, CUDA 12.1, Ninja로 직접 빌드했다. nvcc가 아무 메시지 없이 끝난 원인은 사용자 TEMP 경로에 포함된 한글 폴더 이름이었고, TEMP를 `D:\llm\.cache\tmp`로 바꾸자 빌드가 끝까지 진행됐다.

모델 설정에는 presence penalty 0.9와 repetition penalty 1.05가 기본값으로 설정돼 있고, 변환한 GGUF에도 이 값이 그대로 남았다. 모델 카드는 응답이 길어져도 같은 말을 되풀이하지 않도록 이 값을 기본값으로 정했다고 설명한다. 그런데 `draft-self`는 제약 없는 탐욕 디코딩이 필요하다며 실행을 거부했고, 이번 실측은 모든 실행에서 반복 억제를 끈 채 진행했다.

![아주 긴 두루마리를 큰 가위로 여러 조각으로 자르고, 잘라 낸 조각을 하늘색 끈을 묶은 상자 네 개에 하나씩 담은 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-clover-35b-a3b/02-split-conversion.png)

## 전문가 가중치를 몇 층까지 RAM에 둘까

20.2GB 모델은 12GB VRAM에 다 들어가지 않는다. MoE 모델은 층마다 전문가 256개를 두고 있어서, 전문가 가중치가 파일 용량의 대부분을 차지한다. llama.cpp의 `-ncmoe N` 옵션은 처음 N개 층의 전문가 가중치를 시스템 RAM에 두고 CPU로 계산하게 한다. 어텐션 같은 나머지 가중치와 다른 층의 전문가는 GPU가 맡는다(`-ngl 99`). N이 작을수록 GPU가 맡는 몫이 늘어 빨라지지만, VRAM 용량을 초과하면 속도가 크게 떨어진다.

WSL에서는 26개 층이 한계였다. WSL은 Windows와 같은 GPU를 쓰고 Windows 화면이 VRAM 약 3GiB를 점유한다. 이 때문에 26개 층의 전문가 가중치를 RAM에 둔 설정에서 이미 전체 VRAM 12.29GiB 가운데 11.76GiB를 썼다. Windows 네이티브는 유휴 점유가 2.5GiB여서 두 개 층을 GPU에 더 적재할 수 있었다.

<div class="clv-viz" role="region" aria-label="전문가 가중치를 RAM에 둔 층수별 일반 디코딩 생성 속도 비교">
<div class="clv-viz-title">RAM에 둔 전문가 층수와 생성 속도 (일반 디코딩)</div>
<div class="clv-legend"><span class="clv-key"><span class="clv-sw clv-sw-ram"></span>전문가 가중치 RAM</span><span class="clv-key"><span class="clv-sw clv-sw-acc"></span>GPU</span><span class="clv-key"><span class="clv-sw clv-sw-ink"></span>생성 속도</span></div>
<div class="clv-rows">
<div class="clv-row">
<div class="clv-head"><span class="clv-name">WSL, RAM 26층</span><span class="clv-val"><strong>32.95</strong> 토큰/초</span></div>
<div class="clv-layers" aria-hidden="true"><span class="clv-l-ram" style="flex: 26;"></span><span class="clv-l-gpu" style="flex: 14;"></span></div>
<div class="clv-track"><div class="clv-fill" style="width: 73.2%;"></div></div>
<div class="clv-sub">프롬프트 처리 256 토큰/초</div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">Windows, RAM 26층</span><span class="clv-val"><strong>36.93</strong> 토큰/초</span></div>
<div class="clv-layers" aria-hidden="true"><span class="clv-l-ram" style="flex: 26;"></span><span class="clv-l-gpu" style="flex: 14;"></span></div>
<div class="clv-track"><div class="clv-fill" style="width: 82.1%;"></div></div>
<div class="clv-sub">프롬프트 처리 136 토큰/초, 첫 실행 27.22 토큰/초</div>
</div>
<div class="clv-row clv-best">
<div class="clv-head"><span class="clv-name">Windows, RAM 24층</span><span class="clv-val"><strong>42.72</strong> 토큰/초</span></div>
<div class="clv-layers" aria-hidden="true"><span class="clv-l-ram" style="flex: 24;"></span><span class="clv-l-gpu" style="flex: 16;"></span></div>
<div class="clv-track"><div class="clv-fill" style="width: 94.9%;"></div></div>
<div class="clv-sub">프롬프트 처리 268 토큰/초</div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">Windows, RAM 22층<span class="clv-tag">VRAM 초과</span></span><span class="clv-val"><strong>23.48</strong> 토큰/초</span></div>
<div class="clv-layers" aria-hidden="true"><span class="clv-l-ram" style="flex: 22;"></span><span class="clv-l-gpu" style="flex: 18;"></span></div>
<div class="clv-track"><div class="clv-fill" style="width: 52.2%;"></div></div>
<div class="clv-sub">프롬프트 처리 40 토큰/초</div>
</div>
</div>
<div class="clv-axis" aria-hidden="true"><span>0</span><span>15</span><span>30</span><span>45 토큰/초</span></div>
</div>

일반 디코딩 속도는 llama.cpp 벤치마크 도구 `llama-bench`로 쟀다. 128토큰을 생성하는 시험(tg128)과 512토큰 프롬프트를 처리하는 시험(pp512)의 속도다. Windows에서 전문가 24개 층을 RAM에 두었을 때 초당 42.72토큰으로 가장 빨랐다. 26개 층은 첫 실행에서 초당 27.22토큰이었다가 모델 파일이 캐시된 뒤 36.93토큰이 됐다. 22개 층은 VRAM 용량을 초과해 공유 메모리(GPU가 PCIe를 거쳐 사용하는 시스템 RAM)를 쓰기 시작했고, 생성은 초당 23.48토큰, 프롬프트 처리는 초당 40토큰으로 급락했다.

## 자기 추측 생성은 일반 디코딩보다 느렸다

`draft-self`는 블록 크기를 최대 15토큰으로 설정하고 세 프롬프트를 실행했다. WSL은 전문가 26개 층, Windows는 24개 층을 RAM에 둔 설정이다.

<div class="clv-viz" role="region" aria-label="draft-self 프롬프트별 생성 속도와 일반 디코딩 속도 비교">
<div class="clv-viz-title">draft-self 생성 속도와 일반 디코딩 비교</div>
<div class="clv-legend"><span class="clv-key"><span class="clv-sw clv-sw-acc"></span>일반 디코딩</span><span class="clv-key"><span class="clv-sw clv-sw-ink"></span>draft-self</span></div>
<div class="clv-rows">
<div class="clv-row">
<div class="clv-head"><span class="clv-name">일반 디코딩 (비교 기준)</span></div>
<div class="clv-pair">
<div class="clv-line"><span class="clv-env">WSL</span><div class="clv-track"><div class="clv-fill clv-fill-acc" style="width: 73.2%;"></div></div><span class="clv-num">32.95</span></div>
<div class="clv-line"><span class="clv-env">Windows</span><div class="clv-track"><div class="clv-fill clv-fill-acc" style="width: 94.9%;"></div></div><span class="clv-num">42.72</span></div>
</div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">한국어 단편</span><span class="clv-val">186 / 206토큰 생성</span></div>
<div class="clv-pair">
<div class="clv-line"><span class="clv-env">WSL</span><div class="clv-track"><div class="clv-fill" style="width: 14.9%;"></div></div><span class="clv-num">6.7</span></div>
<div class="clv-line"><span class="clv-env">Windows</span><div class="clv-track"><div class="clv-fill" style="width: 22.9%;"></div></div><span class="clv-num">10.3</span></div>
</div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">코딩</span><span class="clv-val">261 / 262토큰 생성</span></div>
<div class="clv-pair">
<div class="clv-line"><span class="clv-env">WSL</span><div class="clv-track"><div class="clv-fill" style="width: 40.7%;"></div></div><span class="clv-num">18.3</span></div>
<div class="clv-line"><span class="clv-env">Windows</span><div class="clv-track"><div class="clv-fill" style="width: 54.2%;"></div></div><span class="clv-num">24.4</span></div>
</div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">확률 계산</span><span class="clv-val">157 / 133토큰 생성</span></div>
<div class="clv-pair">
<div class="clv-line"><span class="clv-env">WSL</span><div class="clv-track"><div class="clv-fill" style="width: 39.1%;"></div></div><span class="clv-num">17.6</span></div>
<div class="clv-line"><span class="clv-env">Windows</span><div class="clv-track"><div class="clv-fill" style="width: 36.7%;"></div></div><span class="clv-num">16.5</span></div>
</div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">코딩, 블록 8</span></div>
<div class="clv-pair">
<div class="clv-line"><span class="clv-env">WSL</span><div class="clv-track"><div class="clv-fill" style="width: 45.8%;"></div></div><span class="clv-num">20.6</span></div>
<div class="clv-line"><span class="clv-env">Windows</span><div class="clv-track"><div class="clv-fill" style="width: 54.7%;"></div></div><span class="clv-num">24.6</span></div>
</div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">코딩, 블록 4</span></div>
<div class="clv-pair">
<div class="clv-line"><span class="clv-env">WSL</span><div class="clv-track"><div class="clv-fill" style="width: 41.1%;"></div></div><span class="clv-num">18.5</span></div>
<div class="clv-line"><span class="clv-env">Windows</span><div class="clv-track"></div><span class="clv-num clv-na">미측정</span></div>
</div>
</div>
</div>
<div class="clv-axis-pair" aria-hidden="true"><span></span><div class="clv-axis"><span>0</span><span>15</span><span>30</span><span>45</span></div><span class="clv-env">토큰/초</span></div>
</div>

모든 실행에서 수락률이 100%로 표시됐다. 제안한 토큰을 검증 단계가 전부 받아들였다는 뜻이다. 그런데도 블록 크기가 15토큰일 때 가장 빨랐던 Windows 코딩 응답의 생성 속도는 초당 24.4토큰이었다. 같은 설정의 일반 디코딩 속도인 초당 42.72토큰의 약 57%다. 한국어 단편은 WSL 초당 6.7토큰, Windows 초당 10.3토큰으로 가장 느렸다. 블록 크기를 8토큰이나 4토큰으로 줄여도 코딩 응답의 생성 속도에는 큰 차이가 없었다. WSL은 초당 18.5에서 20.6토큰, Windows는 초당 24.6토큰이었다. 블록 크기가 15토큰일 때는 WSL 초당 18.3토큰, Windows 초당 24.4토큰이었다.[^bench-vs-prompt]

[^bench-vs-prompt]: 일반 디코딩 값은 `llama-bench`가 128토큰을 생성한 측정값이고, `draft-self` 값은 실제 프롬프트로 133에서 262토큰을 생성한 측정값이다. 두 값의 측정 방법은 같지 않다.

WSL에서 `draft-self`를 실행할 때 VRAM 사용량은 최대 11.76GiB였다. 프로세스 메모리(RSS)는 최대 14.7GiB로, WSL 할당량 15.5GiB의 약 95%였다. Windows(전문가 24개 층)에서는 VRAM 최대 11.7GiB, 프로세스 작업 집합 최대 18.8GiB였다.

느린 원인은 따로 측정하지 않았다. 나는 CPU가 RAM에 둔 전문가 가중치를 읽는 시간이 생성을 늦춘다고 추정한다. 일반 디코딩은 토큰 하나마다 층별로 전문가 8개만 계산한다. 블록 하나를 검증할 때는 토큰 15개가 저마다 다른 전문가를 고를 수 있고, CPU는 그 전문가들의 가중치를 RAM에서 모두 읽어 계산한다. 한 번의 계산에서 읽는 가중치가 그만큼 늘어난다. 토큰 여러 개를 한 번에 확정하는 이득을 이 읽기 비용이 상쇄한다는 해석이다. Clover 모델 카드에도 블록 확산 중에 같은 블록의 토큰들이 쓸 전문가를 공통 부분집합으로 제한하는 설정(`moe_block_coreset`, 기본값 켜짐)이 있다. 블록 하나가 계산하는 서로 다른 전문가의 수를 줄이는 장치다.[^coreset]

[^coreset]: 이 설정이 llama.cpp 포크의 `draft-self` 경로에도 적용되는지는 확인하지 않았다.

PR 작성자가 H200에서 보고한 생성 속도는 초당 약 32토큰이다. 이 PC에서 Windows로 코딩 응답을 생성한 속도인 초당 24.4토큰과 큰 차이가 없다. 지금의 llama.cpp `draft-self` 구현은 데이터센터 GPU에서도 최적화 전 단계다.

![하늘색 칸 다섯 개가 채워진 서판이 놓인 책상을 향해, 책장에서 꺼낸 두꺼운 장부 더미를 손수레로 끌고 오며 이마의 땀을 훔치는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-clover-35b-a3b/03-draft-self-verify.png)

## 같은 PC에서 돌린 다른 모델과 비교

<div class="clv-viz" role="region" aria-label="같은 PC에서 측정한 로컬 LLM 생성 속도 범위 비교">
<div class="clv-viz-title">같은 PC의 생성 속도 (토큰/초, 막대는 측정 범위)</div>
<div class="clv-rows">
<div class="clv-row">
<div class="clv-head"><span class="clv-name">DeepSeek V4.1 Flash 763B (Strata)</span><span class="clv-val"><strong>2.40–2.70</strong></span></div>
<div class="clv-track"><div class="clv-range" style="left: 5.3%; width: 0.7%;"></div></div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">Qwen 3.8 27B UD-Q4_K_M</span><span class="clv-val"><strong>6.11–6.34</strong></span></div>
<div class="clv-track"><div class="clv-range" style="left: 13.6%; width: 0.5%;"></div></div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">Qwen 3.8 27B UD-IQ3_XXS</span><span class="clv-val"><strong>9.48–14.47</strong></span></div>
<div class="clv-track"><div class="clv-range" style="left: 21.1%; width: 11.1%;"></div></div>
</div>
<div class="clv-row">
<div class="clv-head"><span class="clv-name">Qwen 3.8 27B IQ2_XS + MTP</span><span class="clv-val"><strong>27.73–40.02</strong></span></div>
<div class="clv-track"><div class="clv-range" style="left: 61.6%; width: 27.3%;"></div></div>
</div>
<div class="clv-row clv-best">
<div class="clv-head"><span class="clv-name">Clover-35B-A3B Q4_K_M (Windows)</span><span class="clv-val"><strong>42.72</strong></span></div>
<div class="clv-track"><div class="clv-range clv-range-acc" style="left: 94.4%; width: 1%;"></div></div>
</div>
</div>
<div class="clv-axis" aria-hidden="true"><span>0</span><span>15</span><span>30</span><span>45 토큰/초</span></div>
</div>

앞 글에서 같은 PC로 측정한 생성 속도와 비교하면, Windows 일반 디코딩(초당 42.72토큰)은 이 PC에서 지금까지 실행한 구성 가운데 가장 빠르다. 같은 4비트 `Q4_K_M`끼리 비교하면 Qwen 3.8 27B(초당 6.11에서 6.34토큰)의 약 7배다. Qwen 3.8 27B는 토큰마다 27B 파라미터를 모두 계산하는 밀집 모델이고, 16.46GB 파일의 일부 층을 RAM에 적재해야 했다. Clover는 토큰마다 약 3B만 계산하며, RAM에는 일부 층의 전문가 가중치만 두었다. Qwen 3.8 27B `IQ2_XS`는 2비트로 양자화해 66개 층을 모두 VRAM에 적재하고 MTP(다중 토큰 예측)를 켠 구성으로, 초당 27.73에서 40.02토큰을 냈다. 이 구성과 비교해도 4비트 Clover가 조금 빨랐다.[^prev-compare]

[^prev-compare]: 앞 글의 수치는 실제 프롬프트 응답의 생성 속도이고, Clover 수치는 `llama-bench`의 128토큰 생성 측정값이다. `UD-IQ3_XXS`의 수치는 MTP를 끄고 실행했을 때 측정한 생성 속도의 범위다.

## 실제 응답 원문

세 프롬프트에 대한 `draft-self` 응답을 글자 하나 고치지 않고 그대로 실었다. 탐욕 디코딩을 썼는데도 WSL과 Windows에서 생성한 한국어 단편은 서로 달랐다. 두 환경의 수치 연산 결과가 조금씩 달라, 확률이 비슷한 후보 가운데 다른 토큰을 골랐기 때문이다.

- **한국어 단편**: 조선 시대 세도가의 젊은 후계자가 유럽풍 마법 학교로 유학을 떠나는 이야기의 첫 장면을 한국어로 400자 정도 써 줘. 등장인물의 성격이 대사에서 드러나게 해 줘.
- **코딩**: `Write a Python function merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]] that merges overlapping closed intervals, with a short docstring and three pytest test cases. Code only.`
- **확률 계산**: 한 상자에 빨간 공 3개, 파란 공 5개가 있다. 공을 하나 꺼내 색을 확인하고 다시 넣지 않은 채 하나를 더 꺼낼 때, 두 공의 색이 서로 다를 확률을 구하라. 풀이 과정을 단계별로 쓰고 마지막 줄에 기약분수로 답하라.

WSL의 한국어 단편은 400자를 요청했는데 응답은 공백을 포함해 279자였다. 「으쓱」이 「으shy」로 바뀌었고, 가방을 들고 묻는 김현이 떠나는 후계자인지 분명하지 않다. Windows의 한국어 단편은 「다른話야」에 한자가 섞였고, 후반부는 차를 두고 짧은 문답을 되풀이해 인물의 성격이 대사에서 드러나지 않는다.

<div class="clv-resp" role="region" aria-label="한국어 단편 WSL 응답 원문">
<div class="clv-resp-head"><span class="clv-resp-title">한국어 단편, WSL</span><span class="clv-resp-meta">6.7 토큰/초, 186토큰</span></div>
<div class="clv-resp-body">
<p>"이봐요, 이거 진짜로 가져가도 돼요?"</p>
<p>김현은 손에 쥔 서양식 가죽가방을 살며시 들춰보며 물었다. 한복 차림의 젊은 사족 후계자가, 한양을 등지고 서양 땅으로 떠난다는 게 믿어지지 않았다.</p>
<p>"그냥 가져가. 네가 배운 그 '마법'이 저기서 통할지 모르니까."</p>
<p>친구 최영현이 어깨를 <mark class="clv-quirk">으shy</mark>하며 대답했다. 평소엔 장난꾸러기였지만, 지금만은 눈빛이 남달랐다.</p>
<p>"그럼... 나는 언제 돌아오지?"</p>
<p>"그건 네가 정하는 거 아니야. 네가 그 세계를 이해할 때까지."</p>
<p>현은 고개를 끄덕이며, 한양을 마지막으로 바라보았다.</p>
</div>
</div>

<details class="clv-resp">
<summary class="clv-resp-head"><span class="clv-resp-title">한국어 단편, Windows</span><span class="clv-resp-meta">10.3 토큰/초, 206토큰 <span class="clv-fold"></span></span></summary>
<div class="clv-resp-body">
<p>"이봐, 이거 진짜로 하는 거야?"</p>
<p>김현은 손에 든 서양식 가방을 번갈아 보며 한숨을 쉬었다. 검은 도자기로 만든 주전자가 그의 무릎 위에 놓여 있었다.</p>
<p>"당연하지. 네가 원했잖아."</p>
<p>"그건 <mark class="clv-quirk">다른話야</mark>. 여기 있는 게 진짜로 마법 학교라고?"</p>
<p>"그렇다고 들었다. 네가 원하는 건 배움이지. 이걸로 배우는 거야."</p>
<p>"그럼... 차는?"</p>
<p>"차? 여기서 차를 마시라고?"</p>
<p>"그럼 어떻게 해. 이거로 마법을 배운다고?"</p>
<p>"그럼... 마법사도 차를 마시나?"</p>
<p>"물론이지. 유럽 마법사도 차를 마시니까."</p>
<p>"그럼... 차를 마시면서 마법을 배워야겠네."</p>
<p>"그래. 자, 가자."</p>
<p>"네."</p>
</div>
</details>

코딩 응답은 두 환경의 출력이 같았다. 이 함수는 구간을 시작점 기준으로 정렬한 뒤 겹치는 구간을 차례로 합친다. 입력이 닫힌 구간이므로 `(1, 2)`와 `(2, 3)`처럼 한 구간의 끝점과 다음 구간의 시작점이 같은 경우도 합치고, 이 경우를 확인하는 테스트도 넣었다. 출력한 코드를 그대로 pytest로 실행하면 테스트 3개가 모두 통과한다.

**코딩, WSL과 Windows 공통** (WSL 초당 18.3토큰, Windows 초당 24.4토큰)

```python
from typing import List, Tuple


def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Merge overlapping closed intervals."""
    if not intervals:
        return []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_intervals[0]]
    for current in sorted_intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged


# pytest test cases
def test_merge_overlapping():
    assert merge_intervals([(1, 3), (2, 4), (6, 8)]) == [(1, 4), (6, 8)]


def test_merge_adjacent():
    assert merge_intervals([(1, 2), (2, 3)]) == [(1, 3)]


def test_no_overlap():
    assert merge_intervals([(1, 2), (3, 4)]) == [(1, 2), (3, 4)]
```

확률 계산에서 두 환경은 모두 빨간 공 다음에 파란 공을 뽑는 경우와 그 반대 경우의 확률을 각각 15/56으로 계산했다. 두 확률을 더한 뒤 약분해 15/28이라는 정답을 냈다.

<div class="clv-resp" role="region" aria-label="확률 계산 WSL 응답 원문">
<div class="clv-resp-head"><span class="clv-resp-title">확률 계산, WSL</span><span class="clv-resp-meta">17.6 토큰/초, 157토큰</span></div>
<div class="clv-resp-body">
<p>전체 공의 수: 3 + 5 = 8개.</p>
<p>두 공의 색이 서로 다른 경우:<br>1) 첫 번째가 빨간, 두 번째가 파란<br>2) 첫 번째가 파란, 두 번째가 빨간</p>
<p>1) P(빨간 → 파란) = (3/8) × (5/7) = 15/56<br>2) P(파란 → 빨간) = (5/8) × (3/7) = 15/56</p>
<p>총 확률 = 15/56 + 15/56 = 30/56 = 15/28</p>
<p>답: 15/28</p>
</div>
</div>

<details class="clv-resp">
<summary class="clv-resp-head"><span class="clv-resp-title">확률 계산, Windows</span><span class="clv-resp-meta">16.5 토큰/초, 133토큰 <span class="clv-fold"></span></span></summary>
<div class="clv-resp-body">
<p>전체 공 수: 3 + 5 = 8개.</p>
<p>두 공의 색이 서로 다른 경우:<br>1) 첫 번째가 빨간, 두 번째가 파란: (3/8) × (5/7) = 15/56<br>2) 첫 번째가 파란, 두 번째가 빨간: (5/8) × (3/7) = 15/56</p>
<p>합산: 15/56 + 15/56 = 30/56 = 15/28</p>
<p>답: 15/28</p>
</div>
</details>

![하늘색 확인 도장이 찍힌 반듯한 원고와, 번진 글자 하나에 동그라미가 쳐진 원고를 양손에 들고 곤란한 듯 웃는 치비 서소영](https://img.seosoyoung.eiaserinnys.me/images/local-llm-12gb-vram-clover-35b-a3b/04-two-manuscripts.png)

## 가장 흥미로운 지점

확산 언어 모델의 대표 기능이 이 PC에서는 도리어 속도를 떨어뜨렸다. 이번 실측에서 가장 예상하지 못한 결과다. 12GB VRAM PC에서 llama.cpp의 `draft-self`로 실행했을 때는 토큰 여러 개를 한 번에 확정했고, 수락률도 100%로 표시됐다. 그런데 모든 실행의 생성 속도는 같은 환경에서 측정한 일반 디코딩 속도의 3분의 2보다 느렸다. 초당 40토큰대의 속도는 기반 모델 Qwen3.6-35B-A3B에서 이어받은 MoE 구조에서 나왔고, 확산 생성은 이 PC에서 속도를 올리지 못했다.

공식 블로그는 16GB VRAM의 RTX 5070 Ti에서 INT4로 초당 101.8토큰을 냈다고 밝혔다. 이 PC의 일반 디코딩보다 약 2.4배 빠른 값이다. 그 차이가 블록 확산 생성에서 나왔는지, VRAM 4GB 차이로 전문가 가중치를 GPU에 더 많이 적재한 효과인지는 이번 실측으로 판별할 수 없다. SGLang의 블록 확산 생성이 12GB급 게이밍 PC에서도 속도 이득을 낼지는 아직 확인하지 못한 질문이다.

이 PC에서 내가 Clover를 쓴다면, 24개 층의 전문가 가중치를 RAM에 두고 Windows에서 일반 디코딩으로 실행하겠다. 한국어 글쓰기는 영어와 한자가 섞여 나와 아직 프리뷰다운 결과였다. 앞 글의 한국어 설명 과제에서는 Qwen 3.8 27B `IQ2_XS`가 한자나 영단어를 섞지 않고 답했다.

## 출처

- DiffuSpace, [Clover-35B-A3B-Preview 발표 블로그](https://diffuspace.ai/blog/clover-35b/), 2026-10-28
- [Diffuspace/Clover-35B-A3B-Preview 모델 카드 (Hugging Face)](https://huggingface.co/Diffuspace/Clover-35B-A3B-Preview)
- [DiffuSpace/Clover-35B-A3B-Preview (GitHub)](https://github.com/DiffuSpace/Clover-35B-A3B-Preview)
- [llama.cpp PR #31306: feat: add Clover support](https://github.com/ggml-org/llama.cpp/pull/31306) (포크 `Maphist0/llama.cpp-pub`, `dev-clover` 브랜치)
- [DiffuSpace 발표 트윗](https://x.com/DiffuSpace_Labs/status/2115288124691820738)
- 앞 글: [12GB VRAM 게이밍 PC의 로컬 LLM 실측: DeepSeek V4.1 Flash 763B와 Qwen 3.8 27B](https://seosoyoung.eiaserinnys.me/digest/local-llm-12gb-vram-deepseek-qwen38-27b/)
- 치비 서소영 삽화 4장은 「느낌적인 느낌을 숫자로 옮기는 일」의 치비 서소영 라인아트를 참조해 `gpt-image-2.5-flare`로 따로 생성했다.
