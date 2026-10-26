// Code-copy button behavior adapted from PaperMod layouts/partials/footer.html (MIT).
(function () {
  "use strict";

  function copyButtons() {
    document.querySelectorAll("pre > code").forEach(function (codeblock) {
      var container = codeblock.parentNode.parentNode;
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

      if (container.classList.contains("highlight")) {
        container.appendChild(button);
      } else if (container.parentNode.firstChild === container) {
        // The first cell of a line-number table is not the code block.
      } else if (codeblock.parentNode.parentNode.parentNode.parentNode.parentNode.nodeName === "TABLE") {
        codeblock.parentNode.parentNode.parentNode.parentNode.parentNode.appendChild(button);
      } else {
        codeblock.parentNode.appendChild(button);
      }
    });
  }

  function formatReaderButton() {
    var button = document.querySelector("article.post-single .post-meta .rsvp-launch");
    if (!button) return;
    var separator = button.previousSibling;
    if (separator && separator.nodeType === Node.TEXT_NODE) separator.remove();
    button.textContent = "빠른 읽기";
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      copyButtons();
      formatReaderButton();
    }, { once: true });
  } else {
    copyButtons();
    if (document.readyState === "interactive") {
      document.addEventListener("DOMContentLoaded", formatReaderButton, { once: true });
    } else {
      formatReaderButton();
    }
  }
})();
