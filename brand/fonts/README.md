# Webfonts

`brand/fonts.css` expects these files here. None are bundled; all three families are
published under the SIL Open Font License and may be self-hosted.

| File | Family · weight | Source |
|---|---|---|
| `NotoSerifSC-Light.woff2` | Noto Serif SC 300 | github.com/notofonts/noto-cjk (Serif, SC) |
| `NotoSerifSC-Regular.woff2` | Noto Serif SC 400 | same |
| `NotoSerifSC-Medium.woff2` | Noto Serif SC 500 | same |
| `NotoSerifSC-SemiBold.woff2` | Noto Serif SC 600 | same |
| `NotoSerifSC-Bold.woff2` | Noto Serif SC 700 | same |
| `NotoSerif-Regular.woff2` | Noto Serif 400 | github.com/notofonts/latin-greek-cyrillic |
| `NotoSerif-Italic.woff2` | Noto Serif 400 italic | same |
| `NotoSerif-Bold.woff2` | Noto Serif 700 | same |
| `IBMPlexMono-Regular.woff2` | IBM Plex Mono 400 | github.com/IBM/plex |
| `IBMPlexMono-Medium.woff2` | IBM Plex Mono 500 | same |

Noto Serif SC is large (several MB per weight). For the web, subset to the characters the
consumers use (GB 2312 level 1 plus the brand's copy is a reasonable floor) with
`pyftsubset` from fonttools, keeping `--flavor=woff2`. Print and deck exports can use the
full fonts. Until the files exist, browsers fall back to the local serifs listed in
`brand/tokens.css`; `scripts/check.py` reports which files are still missing.
