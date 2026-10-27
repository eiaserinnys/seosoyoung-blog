  (function () {
    var desktopQuery = window.matchMedia('(min-width: 1200px)');
    var overlapGap = 12;
    var resizeTimer = 0;

    function normalizeFootnoteKey(value) {
      if (!value) return '';
      var key = String(value).trim();
      if (key.charAt(0) === '#') key = key.slice(1);
      try {
        key = decodeURIComponent(key);
      } catch (error) {
        // Keep the raw key when the browser gives an already-decoded fragment.
      }
      return key
        .replace(/^fnref[:\-]/, '')
        .replace(/^fn[:\-]/, '');
    }

    function markerKey(marker) {
      var link = marker.matches('a[href^="#fn"]')
        ? marker
        : marker.querySelector('a[href^="#fn"]');
      var hrefKey = link ? normalizeFootnoteKey(link.getAttribute('href')) : '';
      return hrefKey || normalizeFootnoteKey(marker.id);
    }

    function removeSidenotes(article, resetLayout) {
      article.querySelectorAll('aside.sidenote').forEach(function (note) {
        note.remove();
      });
      article.querySelectorAll('.footnotes > ol > li[data-footnote-id]').forEach(function (item) {
        item.id = item.dataset.footnoteId;
      });
      article.querySelectorAll('.footnotes > ol > li[id]').forEach(function (item) {
        item.tabIndex = -1;
      });
      article.querySelectorAll('.post-content sup[id^="fnref"]').forEach(function (marker) {
        marker.tabIndex = -1;
      });
      if (!resetLayout) return;
      article.classList.remove('has-sidenotes');
      article.style.removeProperty('--sidenotes-height');
      var main = article.closest('.main');
      if (main) main.classList.remove('has-sidenotes');
    }

    function collectMarkers(article) {
      var markers = Array.prototype.slice.call(
        article.querySelectorAll('.post-content sup[id^="fnref"]')
      );
      if (!markers.length) {
        markers = Array.prototype.slice.call(
          article.querySelectorAll('.post-content a.footnote-ref[href^="#fn"]')
        );
      }
      markers.forEach(function (marker) {
        if (!marker.matches('a')) marker.tabIndex = -1;
      });
      return markers;
    }

    function noteByKey(footnoteList) {
      var notes = new Map();
      Array.prototype.slice.call(footnoteList.children).forEach(function (item) {
        var footnoteId = item.dataset.footnoteId || item.id;
        if (!footnoteId) return;
        item.dataset.footnoteId = footnoteId;
        item.tabIndex = -1;
        var key = normalizeFootnoteKey(footnoteId);
        if (key) notes.set(key, item);
      });
      return notes;
    }

    function handleFootnoteNavigation(event) {
      if (!(event.target instanceof Element)) return;
      var link = event.target.closest(
        'a.footnote-ref, a.footnote-backref, a[role="doc-backlink"]'
      );
      if (!link) return;

      var article = link.closest('article.post-single');
      var href = link.getAttribute('href');
      if (!article || !href || href.charAt(0) !== '#') return;

      var targetId = href.slice(1);
      try {
        targetId = decodeURIComponent(targetId);
      } catch (error) {
        // Keep the raw fragment if it is already decoded.
      }
      var target = document.getElementById(targetId);
      if (!target || !article.contains(target)) return;

      event.preventDefault();
      event.stopImmediatePropagation();
      history.pushState(null, null, href);

      var scrollTarget = target;
      if (link.matches('.footnote-backref, [role="doc-backlink"]')) {
        scrollTarget = target.closest('.post-content p, .post-content li') || target;
      }
      if (target.tabIndex < 0) target.tabIndex = -1;
      var options = { block: 'start' };
      if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        options.behavior = 'smooth';
      }
      scrollTarget.scrollIntoView(options);
      target.focus({ preventScroll: true });

      var correctionTimeout;
      var cleanupTimeout;
      function correctFootnoteScrollPosition() {
        var targetTop = scrollTarget.getBoundingClientRect().top;
        var scrollMarginTop = parseFloat(getComputedStyle(scrollTarget).scrollMarginTop) || 0;
        var scrollPaddingTop = parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0;
        if (Math.abs(targetTop - scrollMarginTop - scrollPaddingTop) > 4) {
          scrollTarget.scrollIntoView({ block: 'start' });
        }
      }
      function finishFootnoteScrollCorrection() {
        correctFootnoteScrollPosition();
        window.removeEventListener('scrollend', finishFootnoteScrollCorrection);
        window.clearTimeout(correctionTimeout);
        window.clearTimeout(cleanupTimeout);
      }
      window.addEventListener('scrollend', finishFootnoteScrollCorrection);
      correctionTimeout = window.setTimeout(correctFootnoteScrollPosition, 1200);
      cleanupTimeout = window.setTimeout(function () {
        window.removeEventListener('scrollend', finishFootnoteScrollCorrection);
      }, 3000);
    }

    function layoutArticle(article) {
      removeSidenotes(article, !desktopQuery.matches);
      if (!desktopQuery.matches) return;

      var footnoteList = article.querySelector('.footnotes > ol');
      if (!footnoteList || !footnoteList.children.length) {
        removeSidenotes(article, true);
        return;
      }

      var markers = collectMarkers(article);
      if (!markers.length) {
        removeSidenotes(article, true);
        return;
      }

      var notes = noteByKey(footnoteList);
      if (!markers.some(function (marker) { return notes.has(markerKey(marker)); })) {
        removeSidenotes(article, true);
        return;
      }
      article.classList.add('has-sidenotes');
      var main = article.closest('.main');
      if (main) main.classList.add('has-sidenotes');
      // Reflow after widening the main column so marker coordinates use final layout.
      article.offsetWidth;

      var articleTop = article.getBoundingClientRect().top + window.scrollY;
      var lastBottom = 0;
      var created = 0;
      var positionedKeys = new Set();

      markers.forEach(function (marker) {
        var key = markerKey(marker);
        var source = notes.get(key);
        if (!source || positionedKeys.has(key)) return;
        positionedKeys.add(key);

        var sidenote = document.createElement('aside');
        sidenote.className = 'sidenote';
        sidenote.setAttribute('role', 'note');
        sidenote.id = source.dataset.footnoteId;
        sidenote.tabIndex = -1;
        sidenote.dataset.footnoteKey = key;
        sidenote.innerHTML = source.innerHTML;
        source.removeAttribute('id');
        article.appendChild(sidenote);

        var markerTop = marker.getBoundingClientRect().top + window.scrollY - articleTop;
        var top = Math.max(markerTop, lastBottom + overlapGap);
        sidenote.style.top = Math.round(top) + 'px';
        lastBottom = top + sidenote.offsetHeight;
        created += 1;
      });

      if (!created) {
        removeSidenotes(article, true);
        return;
      }

      article.style.setProperty('--sidenotes-height', Math.ceil(lastBottom) + 'px');
    }

    function layoutSidenotes() {
      document.querySelectorAll('article.post-single').forEach(layoutArticle);
    }

    function scheduleLayout(delay) {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(layoutSidenotes, delay == null ? 120 : delay);
    }

    // Lazy images load after window.load and push the text down; re-place notes when each one arrives.
    function watchImages() {
      Array.prototype.forEach.call(document.querySelectorAll('.post-content img'), function (img) {
        if (!img.complete) {
          img.addEventListener('load', function () { scheduleLayout(150); });
        }
      });
    }

    function init() {
      layoutSidenotes();
      watchImages();

      document.querySelectorAll('details.toc').forEach(function (toc) {
        toc.addEventListener('toggle', function () { scheduleLayout(0); });
      });

      window.addEventListener('load', function () {
        layoutSidenotes();
        scheduleLayout(800);
      });
      window.addEventListener('resize', function () {
        scheduleLayout(120);
      });
      if (desktopQuery.addEventListener) {
        desktopQuery.addEventListener('change', layoutSidenotes);
      } else if (desktopQuery.addListener) {
        desktopQuery.addListener(layoutSidenotes);
      }
      if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(layoutSidenotes).catch(function () {});
      }
      // 안전망: 이미지·폰트·표 등이 늦게 자리잡으며 sup 위치가 변할 때 sidenote를 다시 배치한다.
      // load+800ms 트리거만으로는 느린 이미지 응답·동적 콘텐츠를 못 따라잡는다.
      if ('ResizeObserver' in window) {
        var ro = new ResizeObserver(function () { scheduleLayout(120); });
        document.querySelectorAll('article.post-single').forEach(function (article) {
          ro.observe(article);
        });
      }
    }

    document.addEventListener('click', handleFootnoteNavigation, true);
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init, { once: true });
    } else {
      init();
    }
  })();
