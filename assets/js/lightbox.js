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
        var viewportWidth = window.innerWidth * 0.96;
        var width = Math.min(Math.max(renderedWidth, Math.min(big.naturalWidth, viewportWidth)), viewportWidth);
        big.style.width = width + 'px';
        var captionHeight = capEl ? capEl.offsetHeight + parseFloat(getComputedStyle(capEl).marginTop) : 0;
        var availableHeight = Math.min(window.innerHeight * 0.88, window.innerHeight * 0.94 - captionHeight);
        overlay.classList.toggle('ssy-lightbox--scroll', width * big.naturalHeight / big.naturalWidth > availableHeight);
      }
      var previousOverflow = document.documentElement.style.overflow;
      function close() {
        overlay.remove();
        window.removeEventListener('resize', fitImage);
        document.removeEventListener('keydown', onKey, true);
        document.documentElement.style.overflow = previousOverflow;
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
      overlay.addEventListener('click', close);
      document.addEventListener('keydown', onKey, true);
      window.addEventListener('resize', fitImage);
      big.addEventListener('load', fitImage);
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
