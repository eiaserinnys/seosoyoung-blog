const sectionButtons = [...document.querySelectorAll("[data-filter-section]")];
const chipButtons = [...document.querySelectorAll(".chip[data-chip-kind]")];
const rows = [...document.querySelectorAll(".lrow")];
const months = [...document.querySelectorAll(".mon")];

let activeSection = "all";
let activeChip = null;

function matches(row) {
  if (activeSection !== "all" && row.dataset.type !== activeSection) return false;
  if (!activeChip) return true;
  if (activeChip.kind === "subject") return row.dataset.subject === activeChip.value;
  return row.dataset.tags.split("|").includes(activeChip.value);
}

function update() {
  for (const row of rows) {
    const visible = matches(row);
    row.hidden = !visible;
    const panel = row.nextElementSibling;
    if (panel?.matches(".peek")) {
      const expanded = row.querySelector(".pk").getAttribute("aria-expanded") === "true";
      panel.hidden = !visible || !expanded;
    }
  }

  for (const month of months) {
    let count = 0;
    for (let node = month.nextElementSibling; node && !node.matches(".mon"); node = node.nextElementSibling) {
      if (node.matches(".lrow") && !node.hidden) count += 1;
    }
    month.hidden = count === 0;
    month.querySelectorAll(".mono")[1].textContent = String(count);
  }
}

for (const button of sectionButtons) {
  button.addEventListener("click", () => {
    activeSection = button.dataset.filterSection;
    for (const item of sectionButtons) {
      item.setAttribute("aria-pressed", String(item === button));
    }
    update();
  });
}

for (const button of chipButtons) {
  button.addEventListener("click", () => {
    const isActive = activeChip?.kind === button.dataset.chipKind
      && activeChip.value === button.dataset.chip;
    activeChip = isActive
      ? null
      : { kind: button.dataset.chipKind, value: button.dataset.chip };
    for (const item of chipButtons) {
      const pressed = item === button && !isActive;
      item.setAttribute("aria-pressed", String(pressed));
    }
    update();
  });
}
