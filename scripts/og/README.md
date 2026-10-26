# OG title fonts

Title fonts are selected in `layouts/partials/og/article-image.html`:

1. A title with Han characters and no Hangul or kana uses `NotoSansSC-Bold.ttf`.
2. Otherwise, a title with no Han, Hangul, or kana and a letterlike symbol (U+2100–U+214F) uses `NotoSans-Bold.ttf`.
3. All other titles use `PretendardJP-Bold.ttf`.

The two Noto static TTFs are made from the official Google Fonts variable TTFs at weight 700. With `fontTools` installed, run these commands from the repository root after downloading the source files to `/tmp/og-fonts/`:

```sh
python3 -m fontTools.varLib.instancer \
  "/tmp/og-fonts/NotoSansSC[wght].ttf" wght=700 --static \
  -o assets/fonts/NotoSansSC-Bold.ttf
python3 -m fontTools.varLib.instancer \
  "/tmp/og-fonts/NotoSans[wght].ttf" wght=700 --static \
  -o assets/fonts/NotoSans-Bold.ttf
```

The variable sources are published in [Google Fonts Noto Sans SC](https://github.com/google/fonts/tree/main/ofl/notosanssc) and [Google Fonts Noto Sans](https://github.com/google/fonts/tree/main/ofl/notosans). The corresponding OFL license files are kept beside the static TTFs in `assets/fonts/`.
