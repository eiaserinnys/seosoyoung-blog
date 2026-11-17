  (function () {
    var lightboxSelector = '.post-content img, article.post-single .entry-cover img';

    function openLightbox(img) {
      var renderedWidth = img.getBoundingClientRect().width;
      var overlay = document.createElement('div');
      overlay.className = 'ssy-lightbox';
      overlay.setAttribute('role', 'dialog');
      overlay.setAttribute('aria-modal', 'true');
      overlay.tabIndex = -1;
      var big = document.createElement('img');
      var cover = img.closest('figure.entry-cover');
      big.src = cover ? (cover.dataset.lightboxSrc || img.currentSrc || img.src) : (img.currentSrc || img.src);
      big.alt = img.alt || '';
      big.tabIndex = 0;
      overlay.appendChild(big);
      var fig = img.closest('figure');
      var cap = fig && fig.querySelector('figcaption');
      var text = cap && cap.textContent.trim();
      var capEl = null;
      if (text) {
        capEl = document.createElement('div');
        capEl.className = 'ssy-lightbox-caption';
        capEl.textContent = text;
        capEl.id = 'ssy-lightbox-caption';
        overlay.setAttribute('aria-labelledby', capEl.id);
        overlay.appendChild(capEl);
      } else {
        overlay.setAttribute('aria-label', img.alt || '이미지 확대');
      }
      function fitImage() {
        if (!big.naturalWidth) return;
        // 폭의 정본은 바탕의 실제 안쪽 폭이다. 데스크톱에서 바탕은 scrollbar-gutter로 스크롤바 자리를
        // 미리 두므로, 세로 스크롤바가 생겨도 이 값이 바뀌지 않는다. CSS 그림 최대 폭(max-width: 100%)도
        // 같은 안쪽 폭을 따른다.
        var overlayStyle = getComputedStyle(overlay);
        var boxWidth = overlay.clientWidth
          - parseFloat(overlayStyle.paddingLeft) - parseFloat(overlayStyle.paddingRight);
        var boxHeight = overlay.clientHeight
          - parseFloat(overlayStyle.paddingTop) - parseFloat(overlayStyle.paddingBottom);
        if (!boxWidth || !boxHeight) return;
        var ratio = big.naturalHeight / big.naturalWidth;
        var captionHeight = capEl ? capEl.offsetHeight + parseFloat(getComputedStyle(capEl).marginTop) : 0;
        var availableHeight = Math.min(boxHeight * 0.88, boxHeight * 0.94 - captionHeight);
        // 화면에 통째로 맞춘 폭이 본문에서 보이던 폭의 1.5배보다 작고, 높이에 맞춘 폭이 안쪽 폭의
        // 1.5배 이상인 그림이면 높이를 화면에 맞춰 연다. 화면보다 조금만 넓게 열려 일부만 잘리는
        // 상태는 만들지 않는다. 화면보다 넓으면 왼쪽 끝에서 시작해 가로로 밀어 본다.
        // 화면에 통째로 맞춘 폭이 본문 폭 이상인 그림은 지금처럼 통째로 보인다.
        var fitWidth = Math.min(big.naturalWidth, boxWidth, availableHeight / ratio);
        var heightFitWidth = Math.min(big.naturalWidth, availableHeight / ratio);
        var width = fitWidth;
        var scroll = false;
        var wide = false;
        if (fitWidth < renderedWidth * 1.5 && heightFitWidth >= boxWidth * 1.5) {
          width = heightFitWidth;
          wide = width > boxWidth + 1;
        } else if (fitWidth < renderedWidth - 1) {
          width = Math.min(Math.max(renderedWidth, Math.min(big.naturalWidth, boxWidth)), boxWidth);
          scroll = width * ratio > availableHeight;
        }
        big.style.width = width + 'px';
        overlay.classList.toggle('ssy-lightbox--scroll', scroll);
        overlay.classList.toggle('ssy-lightbox--wide', wide);
      }
      var previousOverflow = document.documentElement.style.overflow;
      function close() {
        overlay.remove();
        window.removeEventListener('resize', fitImage);
        document.removeEventListener('keydown', onKey, true);
        document.documentElement.style.overflow = previousOverflow;
        document.documentElement.classList.remove('ssy-lightbox-open');
        img.focus({ preventScroll: true });
      }
      function onKey(e) {
        if (e.key === 'Escape') {
          e.preventDefault();
          close();
        } else if (e.key === 'Tab') {
          e.preventDefault();
          big.focus({ preventScroll: true });
        }
      }
      // 가로로 민 동작(포인터가 8px 넘게 움직인 뒤의 click)은 닫기로 삼지 않는다.
      var downX = 0;
      var downY = 0;
      var dragged = false;
      overlay.addEventListener('pointerdown', function (e) {
        downX = e.clientX;
        downY = e.clientY;
        dragged = false;
      });
      overlay.addEventListener('pointermove', function (e) {
        if (Math.abs(e.clientX - downX) > 8 || Math.abs(e.clientY - downY) > 8) dragged = true;
      });
      overlay.addEventListener('click', function () {
        if (dragged) {
          dragged = false;
          return;
        }
        close();
      });
      document.addEventListener('keydown', onKey, true);
      window.addEventListener('resize', fitImage);
      big.addEventListener('load', fitImage);
      document.documentElement.classList.add('ssy-lightbox-open');
      document.documentElement.style.overflow = 'hidden';
      document.body.appendChild(overlay);
      fitImage();
      big.focus({ preventScroll: true });
    }

    function isLightboxImage(img) {
      return img && img.matches(lightboxSelector) && !img.closest('a');
    }

    function prepareLightboxImages() {
      document.querySelectorAll(lightboxSelector).forEach(function (img) {
        if (!isLightboxImage(img)) return;
        img.tabIndex = 0;
        img.setAttribute('role', 'button');
        img.setAttribute('aria-haspopup', 'dialog');
        img.setAttribute('aria-label', img.alt || '이미지 확대');
      });
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', prepareLightboxImages, { once: true });
    } else {
      prepareLightboxImages();
    }

    document.addEventListener('click', function (e) {
      if (!(e.target instanceof Element)) return;
      var img = e.target.closest(lightboxSelector);
      if (!isLightboxImage(img)) return;
      openLightbox(img);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter' && e.key !== ' ') return;
      if (!(e.target instanceof Element)) return;
      var img = e.target.closest(lightboxSelector);
      if (!isLightboxImage(img)) return;
      e.preventDefault();
      openLightbox(img);
    });
  })();
