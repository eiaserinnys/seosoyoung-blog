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
      var codeStyle = window.getComputedStyle(pre);
      toolbar.style.backgroundColor = codeStyle.backgroundColor;
      button.style.backgroundColor = codeStyle.backgroundColor;
      button.style.color = codeStyle.color;
      frame.style.backgroundColor = codeStyle.backgroundColor;

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
      wrappers.push({ table: table, wrapper: wrapper });
    });

    function updateOverflow() {
      wrappers.forEach(function (item) {
        var overflows = item.wrapper.scrollWidth > item.wrapper.clientWidth + 1
          || item.table.scrollWidth > item.wrapper.clientWidth + 1;
        item.wrapper.classList.toggle("is-overflowing", overflows);
      });
    }

    updateOverflow();
    window.addEventListener("resize", updateOverflow);
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
