const sectionButtons = [...document.querySelectorAll("[data-filter-section]")];
const chipButtons = [...document.querySelectorAll(".chip[data-chip-kind]")];
const rows = [...document.querySelectorAll(".lrow")];
const months = [...document.querySelectorAll(".mon")];
const filter = document.querySelector(".filt");
const filterOrigin = document.querySelector(".filt-origin");

let activeSection = "all";
let activeChip = null;

function matchesSection(row, section) {
  return section === "all" || row.dataset.type === section;
}

function matchesChip(row, chip) {
  if (!chip) return true;
  if (chip.kind === "subject") return row.dataset.subject === chip.value;
  return row.dataset.tags.split("|").includes(chip.value);
}

function matches(row) {
  return matchesSection(row, activeSection) && matchesChip(row, activeChip);
}

function update() {
  if (activeChip && !rows.some((row) => matchesSection(row, activeSection) && matchesChip(row, activeChip))) {
    activeChip = null;
  }

  for (const button of sectionButtons) {
    const section = button.dataset.filterSection;
    const count = rows.filter((row) => matchesSection(row, section) && matchesChip(row, activeChip)).length;
    button.querySelector(".mono").textContent = String(count);
    button.setAttribute("aria-pressed", String(section === activeSection));
  }

  for (const button of chipButtons) {
    const chip = { kind: button.dataset.chipKind, value: button.dataset.chip };
    const count = rows.filter((row) => matchesSection(row, activeSection) && matchesChip(row, chip)).length;
    const disabled = count === 0;
    button.querySelector(".mono").textContent = String(count);
    button.disabled = disabled;
    button.setAttribute("aria-disabled", String(disabled));
    button.setAttribute("aria-pressed", String(
      activeChip?.kind === chip.kind && activeChip.value === chip.value
    ));
  }

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

function updateAfterSelection() {
  const originY = filterOrigin.getBoundingClientRect().top + window.scrollY;
  const wasStuck = filter
    && window.scrollY > originY
    && filter.getBoundingClientRect().top <= 1;
  update();
  if (wasStuck) window.scrollTo({ top: originY, behavior: "instant" });
}

for (const button of sectionButtons) {
  button.addEventListener("click", () => {
    activeSection = button.dataset.filterSection;
    updateAfterSelection();
  });
}

for (const button of chipButtons) {
  button.addEventListener("click", () => {
    const isActive = activeChip?.kind === button.dataset.chipKind
      && activeChip.value === button.dataset.chip;
    activeChip = isActive
      ? null
      : { kind: button.dataset.chipKind, value: button.dataset.chip };
    updateAfterSelection();
  });
}

update();
