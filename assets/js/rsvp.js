(function () {
  "use strict";
  var article = document.querySelector("article.post-single"),
    content = article && article.querySelector(".post-content");
  if (!content) return;

  var launchButton, dialog, wordDisplay, wordLeft, wordFocus, wordRight,
    status, progress, progressValue, playButton, wpmSlider, wpmValue;
  var tokens = [], sentenceStarts = [];
  var currentIndex = 0, wpm = 300, playTimer = 0, isPlaying = false,
    ended = false, firstAfterPlay = false;
  var sentenceHighlight;
  var wordHighlight;

  var excludedSelector = "pre,figure,table,.katex-display,.footnotes,aside,sup[id^='fnref'],.footnote-ref,[role='doc-noteref'],.anchor,script,style,noscript,svg,canvas,iframe,video,audio,model-viewer,button,input,select,textarea,[aria-hidden='true'],[hidden],.bs-interactive,.sn,.sn-body,[role='note']";
  var blockSelector = "address,blockquote,dd,div,dl,dt,h1,h2,h3,h4,h5,h6,li,ol,p,section,ul";

  function findAncestor(element, selector) {
    while (element && element !== content) {
      if (element.matches(selector)) return element;
      element = element.parentElement;
    }
    return null;
  }

  function blockFor(element) {
    return findAncestor(element, blockSelector) || content;
  }

  function createRange(fragments) {
    var range = document.createRange();
    var first = fragments[0], last = fragments[fragments.length - 1];
    range.setStart(first.node, first.start);
    range.setEnd(last.node, last.end);
    return range;
  }

  function collectTokens() {
    var collected = [];
    var walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT);
    var pending = null;
    var activeBlock = null;
    var previousMath = null;

    function flush() {
      if (!pending) return;
      collected.push({
        text: pending.text,
        range: createRange(pending.fragments),
        block: pending.block,
        isMath: false
      });
      pending = null;
    }

    function appendCharacter(node, block, character, start, end) {
      if (!pending) pending = { text: "", fragments: [], block: block };
      var last = pending.fragments[pending.fragments.length - 1];
      if (last && last.node === node && last.end === start) {
        last.end = end;
      } else {
        pending.fragments.push({ node: node, start: start, end: end });
      }
      pending.text += character;
    }

    var node;
    while ((node = walker.nextNode())) {
      var mathElement = findAncestor(node.parentElement, ".katex");
      var mathExcluded = mathElement && findAncestor(mathElement.parentElement, excludedSelector);

      if (mathElement && !mathExcluded) {
        var mathBlock = blockFor(mathElement);
        flush();
        if (mathElement !== previousMath) {
          var mathRange = document.createRange();
          mathRange.selectNodeContents(mathElement);
          collected.push({
            text: "",
            range: mathRange,
            block: mathBlock,
            isMath: true,
            mathElement: mathElement
          });
        }
        previousMath = mathElement;
        activeBlock = mathBlock;
        continue;
      }

      previousMath = null;
      if (findAncestor(node.parentElement, excludedSelector)) {
        flush();
        activeBlock = null;
        continue;
      }

      var block = blockFor(node.parentElement);
      if (activeBlock && activeBlock !== block) flush();
      activeBlock = block;

      var text = node.nodeValue;
      for (var offset = 0; offset < text.length;) {
        var character = String.fromCodePoint(text.codePointAt(offset));
        var nextOffset = offset + character.length;
        if (/\s/u.test(character)) {
          flush();
        } else {
          appendCharacter(node, block, character, offset, nextOffset);
        }
        offset = nextOffset;
      }
    }

    flush();
    assignSentences(collected);
    return collected;
  }

  function assignSentences(words) {
    var start = 0;
    sentenceStarts = [];

    for (var index = 1; index <= words.length; index += 1) {
      var boundary = index === words.length ||
        words[index].block !== words[index - 1].block ||
        sentenceEnd(words[index - 1].text);
      if (!boundary) continue;

      var range = document.createRange();
      var firstRange = words[start].range;
      var lastRange = words[index - 1].range;
      range.setStart(firstRange.startContainer, firstRange.startOffset);
      range.setEnd(lastRange.endContainer, lastRange.endOffset);
      sentenceStarts.push(start);

      for (var wordIndex = start; wordIndex < index; wordIndex += 1) {
        words[wordIndex].sentenceStart = start;
        words[wordIndex].sentenceRange = range;
      }
      start = index;
    }
  }

  function punctuationOnly(character) { return /[\p{P}\p{S}]/u.test(character); }

  function wordPosition(word) {
    var characters = Array.from(word);
    var first = 0;
    var last = characters.length;
    while (first < last && punctuationOnly(characters[first])) first += 1;
    while (last > first && punctuationOnly(characters[last - 1])) last -= 1;

    var length = last - first;
    var position = length === 0 ? 0 : length === 1 ? 0 :
      length <= 5 ? 1 : length <= 9 ? 2 : length <= 13 ? 3 : 4;
    return { characters: characters, index: Math.min(first + position, characters.length - 1), length: length };
  }

  function sentenceEnd(text) { return /[.!?…][)\]}>'"”’»]*$/u.test(text); }

  function clauseEnd(text) {
    return /[,;:][)\]}>'"”’»]*$/u.test(text);
  }

  function coreLength(token) {
    return token.isMath ? 0 : wordPosition(token.text).length;
  }

  function delayFor(index, atStart) {
    var token = tokens[index];
    var factor = 1;
    if (clauseEnd(token.text)) factor = Math.max(factor, 1.6);
    if (sentenceEnd(token.text)) factor = Math.max(factor, 2.2);
    if (index === tokens.length - 1 || tokens[index + 1].block !== token.block) {
      factor = Math.max(factor, 2.6);
    }
    if (coreLength(token) >= 7) factor *= 1.3;
    if (token.isMath) factor *= 2;
    if (atStart) factor *= 2;
    return (60000 / wpm) * factor;
  }

  function createDialog() {
    dialog = document.createElement("dialog");
    dialog.className = "rsvp-dialog";
    dialog.setAttribute("aria-labelledby", "rsvp-title");
    dialog.tabIndex = -1;
    dialog.innerHTML = [
      '<div class="rsvp-panel">',
      '  <header class="rsvp-header">',
      '    <h2 id="rsvp-title">속독 모드</h2>',
      '    <button type="button" class="rsvp-close" aria-label="속독 모드 닫기">닫기</button>',
      '  </header>',
      '  <button type="button" class="rsvp-word-display" aria-label="재생 또는 정지">',
      '    <span class="rsvp-word-left"></span>',
      '    <span class="rsvp-word-focus"></span>',
      '    <span class="rsvp-word-right"></span>',
      '  </button>',
      '  <p class="rsvp-status" aria-live="polite"></p>',
      '  <div class="rsvp-progress" role="progressbar" aria-label="읽기 진행" aria-valuemin="0" aria-valuemax="100">',
      '    <span class="rsvp-progress-value"></span>',
      '  </div>',
      '  <div class="rsvp-actions">',
      '    <button type="button" class="rsvp-play">재생</button>',
      '    <button type="button" class="rsvp-restart">처음부터</button>',
      '    <button type="button" class="rsvp-previous">이전 문장</button>',
      '    <button type="button" class="rsvp-next">다음 문장</button>',
      '  </div>',
      '  <label class="rsvp-speed-row">',
      '    <span class="rsvp-speed-label">속도 <output class="rsvp-speed-value"></output></span>',
      '    <input class="rsvp-speed-slider" type="range" min="100" max="800" step="10" aria-label="분당 어절 수">',
      '  </label>',
      '  <p class="rsvp-help">스페이스 재생/정지 · ←→ 문장 이동 · ↑↓ 속도 · Esc 닫기</p>',
      '</div>'
    ].join("");

    document.body.appendChild(dialog);
    wordDisplay = dialog.querySelector(".rsvp-word-display");
    wordLeft = dialog.querySelector(".rsvp-word-left");
    wordFocus = dialog.querySelector(".rsvp-word-focus");
    wordRight = dialog.querySelector(".rsvp-word-right");
    status = dialog.querySelector(".rsvp-status");
    progress = dialog.querySelector(".rsvp-progress");
    progressValue = dialog.querySelector(".rsvp-progress-value");
    playButton = dialog.querySelector(".rsvp-play");
    wpmSlider = dialog.querySelector(".rsvp-speed-slider");
    wpmValue = dialog.querySelector(".rsvp-speed-value");

    var storedWpm = Number.parseInt(window.localStorage.getItem("seosoyoung.rsvp.wpm"), 10);
    if (storedWpm >= 100 && storedWpm <= 800) wpm = storedWpm;
    wpmSlider.value = String(wpm);

    dialog.querySelector(".rsvp-close").addEventListener("click", function () {
      dialog.close();
    });
    dialog.addEventListener("click", function (event) {
      if (event.target !== dialog) return;
      var rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right ||
          event.clientY < rect.top || event.clientY > rect.bottom) {
        dialog.close();
      }
    });
    dialog.addEventListener("close", function () {
      stopPlayback();
      clearHighlights();
      document.documentElement.classList.remove("rsvp-active");
    });
    wordDisplay.addEventListener("click", togglePlayback);
    playButton.addEventListener("click", togglePlayback);
    dialog.querySelector(".rsvp-restart").addEventListener("click", function () {
      stopPlayback();
      currentIndex = 0;
      ended = false;
      renderWord();
    });
    dialog.querySelector(".rsvp-previous").addEventListener("click", function () {
      moveSentence(-1);
    });
    dialog.querySelector(".rsvp-next").addEventListener("click", function () {
      moveSentence(1);
    });
    wpmSlider.addEventListener("input", function () {
      setWpm(Number(wpmSlider.value));
    });
    dialog.addEventListener("close", function () {
      launchButton.focus({ preventScroll: true });
    });
    setWpm(wpm);
  }

  function setWpm(value) {
    wpm = Math.max(100, Math.min(800, value));
    wpmSlider.value = String(wpm);
    wpmValue.value = wpm + " WPM";
    window.localStorage.setItem("seosoyoung.rsvp.wpm", String(wpm));
    updateStatus();
  }

  function initHighlights() {
    if (!window.CSS || !window.CSS.highlights || typeof window.Highlight !== "function") {
      sentenceHighlight = null;
      wordHighlight = null;
      return;
    }
    sentenceHighlight = new window.Highlight();
    sentenceHighlight.priority = 1;
    wordHighlight = new window.Highlight();
    wordHighlight.priority = 2;
    window.CSS.highlights.set("rsvp-sentence", sentenceHighlight);
    window.CSS.highlights.set("rsvp-word", wordHighlight);
  }

  function updateHighlights(token) {
    if (!wordHighlight || !sentenceHighlight) return;
    wordHighlight.clear();
    wordHighlight.add(token.range);
    sentenceHighlight.clear();
    sentenceHighlight.add(token.sentenceRange);
  }

  function clearHighlights() {
    if (!window.CSS || !window.CSS.highlights) return;
    window.CSS.highlights.delete("rsvp-word");
    window.CSS.highlights.delete("rsvp-sentence");
    wordHighlight = null;
    sentenceHighlight = null;
  }

  function displayWord(token) {
    wordFocus.replaceChildren();
    if (token.isMath) {
      wordLeft.textContent = "";
      wordRight.textContent = "";
      wordFocus.classList.add("rsvp-math-focus");
      var clone = token.mathElement.cloneNode(true);
      clone.setAttribute("aria-hidden", "true");
      wordFocus.appendChild(clone);
      wordDisplay.setAttribute("aria-label", "수식. 재생 또는 정지");
    } else {
      wordFocus.classList.remove("rsvp-math-focus");
      var position = wordPosition(token.text);
      wordLeft.textContent = position.characters.slice(0, position.index).join("");
      wordFocus.textContent = position.characters[position.index] || "";
      wordRight.textContent = position.characters.slice(position.index + 1).join("");
      wordDisplay.setAttribute("aria-label", token.text + ". 재생 또는 정지");
    }
  }

  function remainingTime() {
    var total = 0;
    for (var index = currentIndex; index < tokens.length; index += 1) {
      total += delayFor(index, index === currentIndex && firstAfterPlay);
    }
    return total;
  }

  function updateStatus() {
    if (!tokens.length) return;
    var current = currentIndex + 1;
    var percent = (current / tokens.length) * 100;
    var minutes = Math.ceil(remainingTime() / 60000);
    status.textContent = current + " / " + tokens.length + " 어절 · 약 " + minutes + "분 남음";
    progress.setAttribute("aria-valuenow", String(Math.round(percent)));
    progressValue.style.width = percent + "%";
    playButton.textContent = ended ? "처음부터" : isPlaying ? "일시정지" : "재생";
    playButton.setAttribute("aria-label", ended ? "처음부터 재생" : isPlaying ? "일시정지" : "재생");
  }

  function ensureWordVisible(token) {
    if (!dialog || !dialog.open) return;
    var rect = token.range.getBoundingClientRect();
    var dialogTop = dialog.getBoundingClientRect().top;
    var margin = 12;
    var upperSpaceBottom = dialogTop - margin;
    if (rect.top >= margin && rect.bottom <= upperSpaceBottom) return;

    var targetCenter = Math.max(margin, upperSpaceBottom) / 2;
    var targetTop = window.scrollY + rect.top + rect.height / 2 - targetCenter;
    var behavior = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth";
    window.scrollTo({ top: Math.max(0, targetTop), behavior: behavior });
  }

  function renderWord() {
    if (!tokens.length) return;
    var token = tokens[currentIndex];
    displayWord(token);
    updateHighlights(token);
    updateStatus();
    ensureWordVisible(token);
  }

  function stopPlayback() {
    window.clearTimeout(playTimer);
    playTimer = 0;
    isPlaying = false;
    firstAfterPlay = false;
    updateStatus();
  }

  function scheduleNext() {
    if (!isPlaying) return;
    playTimer = window.setTimeout(function () {
      if (currentIndex >= tokens.length - 1) {
        isPlaying = false;
        ended = true;
        updateStatus();
        return;
      }
      currentIndex += 1;
      firstAfterPlay = false;
      renderWord();
      scheduleNext();
    }, delayFor(currentIndex, firstAfterPlay));
  }

  function togglePlayback() {
    if (!dialog || !dialog.open) return;
    if (isPlaying) {
      stopPlayback();
      return;
    }
    if (ended) {
      currentIndex = 0;
      ended = false;
      renderWord();
    }
    isPlaying = true;
    firstAfterPlay = true;
    updateStatus();
    scheduleNext();
  }

  function moveSentence(direction) {
    if (!tokens.length) return;
    stopPlayback();
    var currentStart = tokens[currentIndex].sentenceStart;
    var target;
    if (direction < 0 && currentIndex !== currentStart) {
      target = currentStart;
    } else {
      for (var index = 0; index < sentenceStarts.length; index += 1) {
        if (direction < 0 && sentenceStarts[index] < currentStart) target = sentenceStarts[index];
        if (direction > 0 && sentenceStarts[index] > currentStart) {
          target = sentenceStarts[index];
          break;
        }
      }
    }
    if (target !== undefined) {
      currentIndex = target;
      ended = false;
      renderWord();
    }
  }

  function firstVisibleToken(words) {
    for (var index = 0; index < words.length; index += 1) {
      var rect = words[index].range.getBoundingClientRect();
      if (rect.bottom > 0 && rect.top < window.innerHeight) return index;
    }
    return 0;
  }

  function openReader() {
    tokens = collectTokens();
    if (!tokens.length) return;
    currentIndex = firstVisibleToken(tokens);
    ended = false;
    if (!dialog) createDialog();
    initHighlights();
    document.documentElement.classList.add("rsvp-active");
    dialog.showModal();
    renderWord();
    dialog.focus();
  }

  function handleKeys(event) {
    if (!dialog || !dialog.open || event.altKey || event.ctrlKey || event.metaKey) return;
    var target = event.target;
    if (event.code === "Space") {
      event.preventDefault();
      togglePlayback();
      return;
    }
    if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
      if (target === wpmSlider) return;
      event.preventDefault();
      moveSentence(event.key === "ArrowLeft" ? -1 : 1);
      return;
    }
    if (event.key === "ArrowUp" || event.key === "ArrowDown") {
      if (target.matches && target.matches("select, textarea, [contenteditable='true']")) return;
      event.preventDefault();
      setWpm(wpm + (event.key === "ArrowUp" ? 20 : -20));
    }
  }

  function addLaunchButton() {
    launchButton = document.createElement("button");
    launchButton.type = "button";
    launchButton.className = "rsvp-launch";
    launchButton.textContent = "속독 모드";
    launchButton.addEventListener("click", openReader);

    var meta = article.querySelector(".post-meta");
    if (meta) {
      meta.appendChild(document.createTextNode("\u00a0·\u00a0"));
      meta.appendChild(launchButton);
      return;
    }
    launchButton.classList.add("rsvp-launch-header");
    var header = article.querySelector(".post-header") || article;
    header.appendChild(launchButton);
  }

  document.addEventListener("keydown", handleKeys);
  document.addEventListener("visibilitychange", function () {
    if (document.hidden && isPlaying) stopPlayback();
  });
  addLaunchButton();
})();
