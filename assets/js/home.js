(() => {
  const panel = document.querySelector(".xs");
  const rows = document.querySelector(".x-rows");
  const stat = document.querySelector("#stat-x .n");
  const total = panel.querySelector(".sh .lbl");
  total.id = "x-total";

  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), 5000);

  Promise.all([
    fetch("/twitter/api/tweets?order=desc&limit=10", { signal: controller.signal }),
    fetch("/twitter/api/meta", { signal: controller.signal }),
  ])
    .then(async ([tweetsResponse, metaResponse]) => {
      if (!tweetsResponse.ok || !metaResponse.ok) {
        throw new Error("X API request failed");
      }

      const [tweetsPayload, meta] = await Promise.all([
        tweetsResponse.json(),
        metaResponse.json(),
      ]);

      if (!Number.isFinite(meta.total_tweets)) {
        throw new Error("X metadata did not include total_tweets");
      }

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

      stat.textContent = meta.total_tweets;
      total.textContent = meta.total_tweets;
      panel.hidden = false;
      document.documentElement.dataset.homeXReady = "true";
    })
    .catch((error) => {
      controller.abort();
      console.warn("홈 X 데이터를 표시하지 못했습니다.", error);
    })
    .finally(() => window.clearTimeout(timeout));
})();
