(() => {
  const rows = document.querySelector(".x-rows");

  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), 5000);

  fetch("/twitter/api/tweets?order=desc&limit=10", { signal: controller.signal })
    .then(async (response) => {
      if (!response.ok) {
        throw new Error("X API request failed");
      }

      const tweetsPayload = await response.json();

      for (const tweet of tweetsPayload.tweets.filter(({ kind }) => kind === "original").slice(0, 2)) {
        const link = document.createElement("a");
        link.className = "tw";
        link.href = tweet.x_url;

        const date = document.createElement("span");
        date.className = "mono";
        date.textContent = tweet.date_kst.slice(5).replace("-", ".");

        const text = document.createElement("div");
        text.className = "t clamp3";
        text.textContent = tweet.article?.title || tweet.text;

        link.append(date, text);
        rows.append(link);
      }
    })
    .catch((error) => {
      controller.abort();
      console.warn("홈 X 데이터를 표시하지 못했습니다.", error);
    })
    .finally(() => window.clearTimeout(timeout));
})();
