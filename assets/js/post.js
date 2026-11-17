// Code-copy button behavior adapted from PaperMod layouts/partials/footer.html (MIT).
(function () {
  "use strict";

  function copyButtons() {
    document.querySelectorAll("pre > code").forEach(function (codeblock) {
      var pre = codeblock.parentNode;
      var block = pre.closest(".highlight") || pre;
      if (block.parentNode && block.parentNode.classList.contains("code-frame")) return;

      var frame = document.createElement("div");
      frame.className = "code-frame";
      block.parentNode.insertBefore(frame, block);
      frame.appendChild(block);

      var toolbar = document.createElement("div");
      toolbar.className = "code-copy-bar";
      var button = document.createElement("button");
      button.type = "button";
      button.className = "copy-code";
      button.textContent = "복사";

      function copied() {
        button.textContent = "복사됨";
        window.setTimeout(function () {
          button.textContent = "복사";
        }, 2000);
      }

      button.addEventListener("click", function () {
        if ("clipboard" in navigator) {
          navigator.clipboard.writeText(codeblock.textContent);
          copied();
          return;
        }

        var range = document.createRange();
        range.selectNodeContents(codeblock);
        var selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        try {
          document.execCommand("copy");
          copied();
        } catch (error) {
          // The selected code remains available for the browser's copy command.
        }
        selection.removeRange(range);
      });

      toolbar.appendChild(button);
      frame.insertBefore(toolbar, block);
    });
  }

  var MIN_COLUMN_EM = 8;
  var EXPANDED_COLUMN_EM = 20;

  function glueMathPunctuation() {
    document.querySelectorAll(".post-content .katex").forEach(function (math) {
      if (math.closest(".katex-display")) return;

      // KaTeX auto-render는 수식마다 class 없는 span을 만들어 그 안에 .katex를 그린다.
      // 앞뒤 텍스트는 그 span의 형제이므로 span을 수식 단위로 삼는다.
      var parent = math.parentElement;
      if (parent && parent.tagName === "SPAN" && !parent.className && parent.childNodes.length === 1) {
        math = parent;
      }

      var prev = math.previousSibling;
      var next = math.nextSibling;
      // 여는 따옴표(“ " ‘ ')도 수식과 묶어 줄 끝에 따옴표만 홀로 남지 않게 한다.
      var openTail = prev && prev.nodeType === Node.TEXT_NODE
        ? (prev.data.match(/[(\[{“‘\"']+$/) || [""])[0]
        : "";
      // 닫는 따옴표(” " ’ ')도 수식 뒤 글자와 함께 묶는다.
      var closeHead = next && next.nodeType === Node.TEXT_NODE
        ? (next.data.match(/^[)\]},.:;!?%”’\"'A-Za-zㄱ-ㆎ가-힣]+/) || [""])[0]
        : "";
      if (!openTail && !closeHead) return;

      var wrapper = document.createElement("span");
      wrapper.className = "math-nowrap";
      math.parentNode.insertBefore(wrapper, math);
      if (openTail) {
        wrapper.appendChild(prev.splitText(prev.data.length - openTail.length));
      }
      wrapper.appendChild(math);
      // 인라인 블록 뒤 줄바꿈은 부모 white-space를 따르므로, 수식은 nowrap으로 두고 .base 사이에만 줄바꿈 자리를 연다.
      math.querySelectorAll(".katex-html").forEach(function (html) {
        var bases = Array.from(html.children).filter(function (child) {
          return child.classList.contains("base");
        });
        bases.slice(1).forEach(function (base) {
          var breakPoint = document.createElement("span");
          breakPoint.className = "math-break";
          breakPoint.textContent = "\u200b";
          html.insertBefore(breakPoint, base);
        });
      });
      if (closeHead) {
        next.splitText(closeHead.length);
        wrapper.appendChild(next);
      }
    });
  }

  function wrapTables() {
    var wrappers = [];
    document.querySelectorAll(".post-content table").forEach(function (table) {
      if (table.closest(".highlight") || table.classList.contains("highlighttable")) return;

      var wrapper = table.parentElement;
      if (!wrapper || !wrapper.classList.contains("table-scroll")) {
        wrapper = document.createElement("div");
        wrapper.className = "table-scroll";
        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
      }
      var cols = 0;
      table.querySelectorAll("tr").forEach(function (row) {
        var count = 0;
        Array.prototype.forEach.call(row.children, function (cell) {
          count += cell.colSpan || 1;
        });
        if (count > cols) cols = count;
      });
      table.style.setProperty("--table-cols", cols);
      wrappers.push({ table: table, wrapper: wrapper, cols: cols });
    });

    function firstColumnWidth(table) {
      var rows = table.querySelectorAll("tr");
      for (var i = 0; i < rows.length; i++) {
        var cell = rows[i].children[0];
        if (cell && cell.colSpan === 1) return cell.getBoundingClientRect().width;
      }
      return null;
    }

    function updateOverflow() {
      wrappers.forEach(function (item) {
        item.wrapper.classList.remove("is-overflowing", "is-sticky-first", "is-expanded");
        item.table.style.removeProperty("--table-expanded-width");
      });
      wrappers.forEach(function (item) {
        var natural = item.wrapper.scrollWidth > item.wrapper.clientWidth + 1
          || item.table.scrollWidth > item.wrapper.clientWidth + 1;
        var squeezed = false;
        if (!natural && item.cols >= 3 && item.cols <= 5) {
          var fontSize = parseFloat(getComputedStyle(item.table).fontSize);
          if (item.wrapper.clientWidth / item.cols < fontSize * MIN_COLUMN_EM) {
            var inlineWidth = item.table.style.getPropertyValue("width");
            var inlinePriority = item.table.style.getPropertyPriority("width");
            item.table.style.setProperty("width", "max-content");
            squeezed = item.table.getBoundingClientRect().width > item.wrapper.clientWidth + 1;
            if (inlineWidth) item.table.style.setProperty("width", inlineWidth, inlinePriority);
            else item.table.style.removeProperty("width");
          }
        }
        // Measure text lines before applying a wider table, then cap the widened width.
        var expanded = false;
        if (item.cols >= 3) {
          var longCell = Array.from(item.table.querySelectorAll("th, td")).some(function (cell) {
            var range = document.createRange();
            range.selectNodeContents(cell);
            var tops = [];
            Array.from(range.getClientRects()).forEach(function (rect) {
              if (rect.width && rect.height && !tops.some(function (top) { return Math.abs(top - rect.top) < 2; })) {
                tops.push(rect.top);
              }
            });
            return tops.length >= 5;
          });
          if (longCell) {
            var oldWidth = item.table.style.getPropertyValue("width");
            var oldPriority = item.table.style.getPropertyPriority("width");
            item.table.style.setProperty("width", "max-content");
            var maxWidth = item.table.getBoundingClientRect().width;
            if (oldWidth) item.table.style.setProperty("width", oldWidth, oldPriority);
            else item.table.style.removeProperty("width");
            if (maxWidth > item.wrapper.clientWidth + 1) {
              var cap = parseFloat(getComputedStyle(item.table).fontSize) * item.cols * EXPANDED_COLUMN_EM;
              item.table.style.setProperty("--table-expanded-width", Math.min(maxWidth, cap) + "px");
              expanded = true;
            }
          }
        }
        var overflowing = natural || squeezed || expanded;
        item.wrapper.classList.toggle("is-expanded", expanded);
        item.wrapper.classList.toggle("is-overflowing", overflowing);
        var sticky = false;
        // 2칸 표는 값 열이 좁은 창으로만 보여 읽기 나빠지므로 고정하지 않는다.
        if (overflowing && item.cols >= 3 && item.wrapper.clientWidth > 0) {
          var width = firstColumnWidth(item.table);
          var fontSize = parseFloat(getComputedStyle(item.table).fontSize);
          sticky = width !== null && !isNaN(fontSize)
            && item.wrapper.clientWidth - width >= fontSize * MIN_COLUMN_EM;
        }
        item.wrapper.classList.toggle("is-sticky-first", sticky);
        syncHeader(item);
      });
    }

    function syncHeader(item) {
      var head = item.table.tHead;
      if (!head || !item.wrapper.classList.contains("is-overflowing")) {
        if (item.clone) item.clone.hidden = true;
        return;
      }
      if (!item.clone) {
        var clone = document.createElement("div");
        clone.className = "table-header-clone";
        clone.setAttribute("aria-hidden", "true");
        clone.setAttribute("inert", "");
        clone.hidden = true;
        var copy = item.table.cloneNode(false);
        copy.removeAttribute("id");
        copy.appendChild(head.cloneNode(true));
        copy.querySelectorAll("[id]").forEach(function (el) { el.removeAttribute("id"); });
        clone.appendChild(copy);
        item.wrapper.appendChild(clone);
        item.clone = clone;
      }
      var wrapperRect = item.wrapper.getBoundingClientRect();
      var headRect = head.getBoundingClientRect();
      var tableRect = item.table.getBoundingClientRect();
      var topbar = document.querySelector(".site-top");
      var top = topbar ? topbar.getBoundingClientRect().bottom : 0;
      var visible = headRect.top < top && tableRect.bottom > top + headRect.height;
      item.clone.hidden = !visible;
      if (!visible) return;
      var cloneTable = item.clone.firstElementChild;
      var originals = head.querySelectorAll("tr:first-child > *");
      var copies = cloneTable.querySelectorAll("tr:first-child > *");
      cloneTable.style.width = tableRect.width + "px";
      cloneTable.style.left = -item.wrapper.scrollLeft + "px";
      originals.forEach(function (cell, index) {
        if (copies[index]) copies[index].style.width = cell.getBoundingClientRect().width + "px";
      });
      if (copies[0]) copies[0].style.transform = item.wrapper.classList.contains("is-sticky-first")
        ? "translateX(" + item.wrapper.scrollLeft + "px)" : "";
      item.clone.style.top = top + "px";
      item.clone.style.left = wrapperRect.left + "px";
      item.clone.style.width = item.wrapper.clientWidth + "px";
    }

    wrappers.forEach(function (item) {
      item.wrapper.addEventListener("scroll", function () { syncHeader(item); }, { passive: true });
    });
    window.addEventListener("scroll", function () { wrappers.forEach(syncHeader); }, { passive: true });

    updateOverflow();
    // 모바일 주소창이 접히며 높이만 바뀌는 resize는 건너뛴다. 클래스를 뗐다 붙이면 밀어 둔 표의 scrollLeft가 0으로 돌아간다.
    var lastWidth = window.innerWidth;
    window.addEventListener("resize", function () {
      if (window.innerWidth === lastWidth) return;
      lastWidth = window.innerWidth;
      updateOverflow();
    });
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(updateOverflow).catch(function () {});
    }
  }

  function preserveImageWidths() {
    document.querySelectorAll(".post-content img[width]").forEach(function (img) {
      var width = Number(img.getAttribute("width"));
      if (Number.isFinite(width) && width > 0) img.style.width = width + "px";
    });
  }

  function formatReaderButton() {
    var button = document.querySelector("article.post-single .post-meta .rsvp-launch");
    if (!button) return;
    var separator = button.previousSibling;
    if (separator && separator.nodeType === Node.TEXT_NODE) separator.remove();
    button.textContent = "빠른 읽기";
  }

  document.addEventListener("click", function (event) {
    if (!(event.target instanceof Element) || !event.target.closest("article.post-single .rsvp-launch")) return;
    var title = document.getElementById("rsvp-title");
    if (title) title.textContent = "빠른 읽기";
    var close = document.querySelector(".rsvp-dialog .rsvp-close");
    if (close) close.setAttribute("aria-label", "빠른 읽기 닫기");
  });

  function preparePostContent() {
    glueMathPunctuation();
    copyButtons();
    wrapTables();
    preserveImageWidths();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      preparePostContent();
      formatReaderButton();
    }, { once: true });
  } else {
    preparePostContent();
    if (document.readyState === "interactive") {
      document.addEventListener("DOMContentLoaded", formatReaderButton, { once: true });
    } else {
      formatReaderButton();
    }
  }
})();
