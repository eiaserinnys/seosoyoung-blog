const root = document.documentElement;
const themeButton = document.querySelector(".theme-control");

function updateThemePressed() {
  const dark = root.dataset.theme
    ? root.dataset.theme === "dark"
    : window.matchMedia("(prefers-color-scheme: dark)").matches;
  themeButton.setAttribute("aria-pressed", String(dark));
}

if (themeButton) {
  updateThemePressed();
  themeButton.addEventListener("click", () => {
    const current = root.dataset.theme || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    root.dataset.theme = current === "dark" ? "light" : "dark";
    localStorage.setItem("pref-theme", root.dataset.theme);
    updateThemePressed();
  });
}

document.querySelectorAll(".pk[aria-controls]").forEach(button => {
  const row = button.closest(".row, .lrow");
  const panel = row.nextElementSibling;
  button.addEventListener("click", async () => {
    const expanded = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!expanded));
    panel.hidden = expanded;

    if (expanded || panel.dataset.loaded || panel.dataset.loading) return;

    const loading = document.createElement("span");
    loading.className = "lbl";
    loading.textContent = "불러오는 중";
    panel.replaceChildren(loading);
    panel.dataset.loading = "true";
    panel.setAttribute("aria-busy", "true");

    try {
      if (!button.dataset.peek) throw new Error("Missing peek URL");
      const response = await fetch(button.dataset.peek);
      if (!response.ok) throw new Error(`Peek request failed: ${response.status}`);
      const payload = await response.json();
      panel.innerHTML = payload.html;
      panel.dataset.loaded = "true";
    } catch {
      const link = document.createElement("a");
      link.className = "go";
      link.href = row.querySelector(".t a").href;
      link.textContent = "전문 읽기";
      panel.replaceChildren(link);
    } finally {
      delete panel.dataset.loading;
      panel.removeAttribute("aria-busy");
    }
  });
});
