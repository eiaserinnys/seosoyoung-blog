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
  const panel = document.getElementById(button.getAttribute("aria-controls"));
  button.addEventListener("click", () => {
    const expanded = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!expanded));
    panel.hidden = expanded;
  });
});
