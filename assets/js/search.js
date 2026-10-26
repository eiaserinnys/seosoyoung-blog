// Search flow adapted from PaperMod fastsearch.js (MIT); see third_party/PaperMod-LICENSE.
const input = document.getElementById("searchInput");
const resultsList = document.getElementById("searchResults");
const sectionLabels = {
  posts: "쓴 글",
  digest: "읽은 글",
  gallery: "그림",
};
const shelfLabels = {
  experiment: "실험",
  atlas: "아틀라스",
  report: "리포트",
};

const fuseOptions = {
  distance: 100,
  threshold: 0.4,
  ignoreLocation: true,
  keys: ["title", "summary", "content"],
};

let fuse;
let searchTimer;
// 마지막으로 그린 검색어. 같은 검색어로 다시 그리면 포커스를 가진 행이 지워진다
// (한글 조합이 ↓나 Tab으로 끝날 때 compositionend와 input이 같은 검색을 한 번 더 예약한다).
let renderedQuery = null;

function clearResults() {
  resultsList.replaceChildren();
}

function renderResults() {
  const query = input.value.trim();
  if (fuse && query === renderedQuery) return;
  clearResults();
  if (!fuse) return;
  renderedQuery = query;
  if (!query) return;

  const matches = fuse.search(query, { limit: 30 });
  if (matches.length === 0) {
    const empty = document.createElement("li");
    empty.className = "search-empty";
    empty.textContent = "결과 없음";
    resultsList.append(empty);
    return;
  }

  for (const { item } of matches) {
    const row = document.createElement("li");
    const link = document.createElement("a");
    link.className = `lrow search-result${item.section === "posts" ? " ins" : ""}`;
    link.href = item.permalink;

    const date = document.createElement("span");
    date.className = "date mono";
    date.textContent = item.date;

    const badge = document.createElement("span");
    badge.className = `badge${item.section === "posts" ? " w" : ""}`;
    badge.textContent = item.section === "lab"
      ? (shelfLabels[item.shelf] ?? "실험실")
      : sectionLabels[item.section];

    const copy = document.createElement("span");
    copy.className = "search-copy";

    const title = document.createElement("span");
    title.className = "t clamp1";
    title.textContent = item.title;

    const summary = document.createElement("span");
    summary.className = "search-summary clamp1";
    summary.textContent = new DOMParser()
      .parseFromString(String(item.summary ?? ""), "text/html")
      .body.textContent.trim();

    copy.append(title, summary);
    link.append(date, badge, copy);
    row.append(link);
    resultsList.append(row);
  }
}

function scheduleSearch() {
  window.clearTimeout(searchTimer);
  searchTimer = window.setTimeout(renderResults, 150);
}

input.addEventListener("compositionend", () => {
  scheduleSearch();
});
input.addEventListener("input", () => {
  scheduleSearch();
});
input.addEventListener("search", () => {
  if (!input.value) {
    window.clearTimeout(searchTimer);
    renderResults();
  }
});

document.addEventListener("keydown", (event) => {
  const links = resultsList.querySelectorAll("a.search-result");
  const activeIndex = Array.from(links).indexOf(document.activeElement);

  if (event.key === "Escape") {
    input.value = "";
    window.clearTimeout(searchTimer);
    renderResults();
    input.focus();
    return;
  }

  if (event.key === "ArrowDown" && links.length > 0 && document.activeElement === input) {
    event.preventDefault();
    links[0].focus();
  } else if (event.key === "ArrowDown" && activeIndex >= 0 && activeIndex < links.length - 1) {
    event.preventDefault();
    links[activeIndex + 1].focus();
  } else if (event.key === "ArrowUp" && activeIndex === 0) {
    event.preventDefault();
    input.focus();
  } else if (event.key === "ArrowUp" && activeIndex > 0) {
    event.preventDefault();
    links[activeIndex - 1].focus();
  } else if (event.key === "ArrowRight" && activeIndex >= 0) {
    links[activeIndex].click();
  }
});

fetch("../index.json")
  .then((response) => response.json())
  .then((index) => {
    fuse = new Fuse(index, fuseOptions);
    renderResults();
  })
  .catch((error) => console.error("Search index could not be loaded", error));
