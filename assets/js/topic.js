const sectionButtons = [...document.querySelectorAll("[data-filter-section]")];
const chipButtons = [...document.querySelectorAll(".chip[data-chip-kind]")];
const rows = [...document.querySelectorAll(".lrow")];
const months = [...document.querySelectorAll(".mon")];
const filter = document.querySelector(".filt");
const filterOrigin = document.querySelector(".filt-origin");
const siteTop = document.querySelector(".site-top");

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
    button.setAttribute("aria-pressed", String(section === activeSection));
  }

  for (const button of chipButtons) {
    const chip = { kind: button.dataset.chipKind, value: button.dataset.chip };
    const count = rows.filter((row) => matchesSection(row, activeSection) && matchesChip(row, chip)).length;
    const disabled = count === 0;
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
  }
}

function updateAfterSelection() {
  const originY = filterOrigin.getBoundingClientRect().top + window.scrollY;
  const stickyTop = filter ? parseFloat(getComputedStyle(filter).top) || 0 : 0;
  const wasStuck = filter
    && window.scrollY > originY - stickyTop
    && filter.getBoundingClientRect().top <= stickyTop + 1;
  update();
  if (wasStuck) window.scrollTo({ top: originY - stickyTop, behavior: "instant" });
}

if (filter && siteTop) {
  function updateSubbarStuckState() {
    const stickyTop = parseFloat(getComputedStyle(filter).top) || 0;
    const isStuck = window.scrollY > 0
      && filter.getBoundingClientRect().top <= stickyTop + 1;
    if (isStuck) {
      siteTop.dataset.subbarStuck = "true";
    } else {
      delete siteTop.dataset.subbarStuck;
    }
  }

  window.addEventListener("scroll", () => requestAnimationFrame(updateSubbarStuckState), { passive: true });
  updateSubbarStuckState();
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
