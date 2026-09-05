# Tiansight 侍天 design system

Development baseline for Tiansight. The published brand foundation lives in `brand/`; the supplied design-system export is preserved unchanged in `TIANSIGHT 侍天 Design System/`.

## Start here

```sh
python3 scripts/check.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Open the [foundation specimen](http://127.0.0.1:8000/brand/index.html). It is fully offline: no CDN scripts, fonts or images, and it renders the published tokens, type scale, mark, CSS components, chart palette, layout rules, voice, and the open questions listed below.

The supplied export previews still work as references: [website kit](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/ui_kits/website/index.html), [report kit](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/ui_kits/report/index.html), [slides](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/slides/index.html). They use CDN scripts and fonts and a prebuilt bundle, need internet access, and are not a build pipeline.

## Source of truth

The [brand directory](https://apuch.art/) resolves Tiansight to the [published brand API](https://apuch.art/api/brands/tiansight.json). `brand/source.json` records the version, theme, retrieval date and official logo hash. `brand/guide.md` is the published primary guide (v0.6).

The export is a separate proposal: parchment `#EFE6D2` page background, sans-serif body, Spectral Latin, a four-colour chart semantics, and its own token scales. The published guide requires the `#F4F0E7` canvas, `#17130D` text, serif end-to-end, `#EFE6D2` as the primary field and action colour, and the official mark in `brand/logo.png`. Follow the published guide; reuse export components only after restyling them onto `brand/`.

## Foundation layer (`brand/`)

| File | Role |
|---|---|
| `tokens.css` | Published palette plus derived surfaces, text roles, chart series, type scale, spacing, layout, radius, motion. Load first. |
| `base.css` | Element defaults on the foundation: serif everywhere, body 18/1.7, headings 600, captions uppercase in deep gold, mono only for data, reduced motion, print. |
| `components.css` | CSS-only components with the `.ts-` prefix: container/grid/section, heading pair, display lockup, rules and frames, compass watermark, card (with 天干 index), token row, badges, ✓/✕ list, buttons, form fields, stat, quote, step marker, seal stamp, mark lockup, nav/header, ledger table, chart chrome, reveal. No raw colour values. |
| `index.html` | Offline specimen of everything above, in brand voice, bilingual. |
| `guide.md`, `source.json`, `logo.png` | Published guide, provenance snapshot, official mark. |

A new consumer imports the three CSS files in order and uses the `.ts-` classes or the tokens directly. The foundation does not restyle the export.

`scripts/check.py` verifies: tokens match the published theme and every row of the guide's colour table; the logo hash; serif-only font stacks with no Inter/Roboto; no raw colours or gradients outside `tokens.css`; radius limited to 2px, pill or circle; every `var(--x)` is declared; the specimen loads no remote resource, script or emoji; and the export manifest is intact. Run it before committing.

## Decisions taken in the foundation

- **Primary button** is the ink field (`#EFE6D2`) with charcoal text and a gold hairline border, because ink against the canvas is only 1.09:1 and needs an edge. Press moves it down 1px, like a stamp.
- **Bright gold `#D4A862`** is 1.9:1 on the canvas, so the foundation uses it only at 28px and above, for active states, and on charcoal (8.4:1). Small captions use deep gold; token-row hex values use deep gold for the same reason.
- **`--gold` and `--gold-deep`** are both `#76551F` in v0.6. Both tokens are kept so they can diverge later.
- **Mark.** The guide describes a compass ring with 侍; the published asset is the circular 侍天 seal. The foundation uses the published asset and draws the compass only as a watermark.
- **Charts** follow guide §5: one series bright gold, two adds charcoal, three adds vermillion; ticks in ink muted. The export's growth/loss/caution/datum colours are not in the guide and are not in the foundation.
- **Fonts** are not bundled. Stacks fall back to local serifs, never sans-serif. Noto Serif SC, Noto Serif and IBM Plex Mono are OFL and can be self-hosted once the target and subset strategy are chosen.
- **Vermillion seal stamp** is a CSS placeholder. The real 朱印 needs calligraphy artwork.

## Open questions for the brand owner

1. Accept the gold hairline on the primary button, or make the charcoal solid button the primary action?
2. Keep bright gold for the 智慧领航者 tagline at body size, or move it to deep gold?
3. Should deep gold get its own value so captions differ from structural rules?
4. Compass mark or seal: which is the primary 标志 going forward?
5. Does the report need semantic chart colours beyond the three-series rule?
6. Font hosting target and subsetting.
7. Which consumer migrates first? Recommendation: the website, as the entry surface with the widest component coverage.
8. All prices, customer quotes and partner names in the specimen come from the guide or the export and need verification before publication.

## Continue development

1. Settle the open questions above, then bump `brand/guide.md` and `source.json` when the published guide changes.
2. Choose the first consumer (recommendation: website). Rebuild its sections on `brand/` using the `.ts-` classes; port export components one at a time, replacing their token names with foundation tokens.
3. Add a build pipeline for that consumer. The supplied `_ds_bundle.js` is generated output with no rebuild command; editing JSX alone does not update the bundled previews.
4. Validate interactions, keyboard navigation and mobile layouts in the consumer, then run `python3 scripts/check.py` before committing.

No product backend, application framework or deployment target is configured by this baseline. Demo copy, prices and customer claims require verification before publication.
