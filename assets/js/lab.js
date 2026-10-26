const tabs = [...document.querySelectorAll('[role="tab"]')];
const panels = [...document.querySelectorAll('[role="tabpanel"]')];

function selectTab(tab, replaceHash) {
  const selectedId = tab.getAttribute("aria-controls");

  for (const item of tabs) {
    const selected = item === tab;
    item.setAttribute("aria-selected", String(selected));
    item.tabIndex = selected ? 0 : -1;
  }

  for (const panel of panels) {
    panel.hidden = panel.id !== selectedId;
  }

  if (replaceHash) {
    history.replaceState(null, "", `${location.pathname}${location.search}#${selectedId}`);
  }
}

const initialId = window.location.hash.slice(1);
const initialTab = tabs.find((tab) => tab.getAttribute("aria-controls") === initialId) || tabs[0];
selectTab(initialTab, false);

for (const [index, tab] of tabs.entries()) {
  tab.addEventListener("click", () => selectTab(tab, true));
  tab.addEventListener("keydown", (event) => {
    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
    event.preventDefault();
    const direction = event.key === "ArrowRight" ? 1 : -1;
    const nextIndex = (index + direction + tabs.length) % tabs.length;
    tabs[nextIndex].focus();
    selectTab(tabs[nextIndex], true);
  });
}
