  (function () {
    var lightboxSelector = '.post-content img, article.post-single .entry-cover img';

    function openLightbox(img) {
      var overlay = document.createElement('div');
      overlay.className = 'ssy-lightbox';
      overlay.setAttribute('role', 'dialog');
      overlay.setAttribute('aria-modal', 'true');
      overlay.tabIndex = -1;
      var big = document.createElement('img');
      big.src = img.closest('article.post-single .entry-cover') ? img.src : (img.currentSrc || img.src);
      big.alt = img.alt || '';
      big.tabIndex = 0;
      overlay.appendChild(big);
      var nw = img.naturalWidth, nh = img.naturalHeight;
      if (nw && nh) {
        var fitW = Math.min(nw, window.innerWidth * 0.96, window.innerHeight * 0.88 * nw / nh);
        if (fitW < img.getBoundingClientRect().width) overlay.classList.add('ssy-lightbox--scroll');
      }
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
      function fitImageHeight() {
        if (!capEl || overlay.classList.contains('ssy-lightbox--scroll')) return;
        big.style.maxHeight = 'calc(94vh - ' + (capEl.offsetHeight + 14) + 'px)';
      }
      var previousOverflow = document.documentElement.style.overflow;
      function close() {
        overlay.remove();
        window.removeEventListener('resize', fitImageHeight);
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
      if (capEl) window.addEventListener('resize', fitImageHeight);
      document.documentElement.style.overflow = 'hidden';
      document.body.appendChild(overlay);
      fitImageHeight();
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
