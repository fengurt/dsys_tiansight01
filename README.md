# Tiansight 侍天 design system

Development baseline for Tiansight. The published brand foundation lives in `brand/`; the supplied design-system export is preserved unchanged in `TIANSIGHT 侍天 Design System/`.

## Start here

```sh
python3 scripts/check.py            # guide conformance, build freshness, tokens.json, a11y lint, contrast
python3 scripts/check.py --render   # plus layout regression in headless Chromium
python3 -m http.server 8000 --bind 127.0.0.1
```

Docs: [principles](docs/principles.md) · [quickstart](docs/quickstart.md) · [contributing](docs/contributing.md) · [changelog](CHANGELOG.md) · [distribution](dist/README.md). System version: `brand/VERSION`.

## Sharing the system with other sites

`dist/tiansight.css` is the whole foundation in one file. Another team adds one line and gets the fonts, tokens, element defaults and every component:

```html
<link rel="stylesheet" href="https://fengurt.github.io/dsys_tiansight01/dist/tiansight.css">
```

That URL is the **latest channel**: every push updates every site linking it. `dist/tiansight-v0.6.css` is the same content pinned to a version for sites that want to move deliberately. `dist/tokens.json` carries the tokens as data, `dist/icons.svg` the sprite, and `dist/example.html` is a working page to copy. Serving needs GitHub Pages switched on (settings → Pages → deploy from `main`, root); see [dist/README.md](dist/README.md). Rebuild with `python3 scripts/build_dist.py`.

| Surface | URL | Notes |
|---|---|---|
| Foundation specimen | [brand/index.html](http://127.0.0.1:8000/brand/index.html) | Every published rule rendered, with the open questions. |
| Sales deck | [deck/index.html](http://127.0.0.1:8000/deck/index.html) | 13 slides at 16:9. Arrow keys, space, number keys, tap halves, F for fullscreen, `#n` deep links. Print to PDF gives one slide per page. |
| Website | [website/index.html](http://127.0.0.1:8000/website/index.html) | Long-scroll marketing site. Chapter tabs, five-question stepper, contact form with a local success state. |

All three are offline: no CDN scripts, fonts or images. They share `brand/tokens.css`, `brand/base.css` and `brand/components.css`.

The supplied export previews still work as references: [website kit](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/ui_kits/website/index.html), [report kit](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/ui_kits/report/index.html), [slides](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/slides/index.html). They use CDN scripts and fonts and a prebuilt bundle, need internet access, and are not a build pipeline.

## Source of truth

The [brand directory](https://apuch.art/) resolves Tiansight to the [published brand API](https://apuch.art/api/brands/tiansight.json). `brand/source.json` records the version, theme, retrieval date and official logo hash. `brand/guide.md` is the published primary guide (v0.6).

The export is a separate proposal: parchment `#EFE6D2` page background, sans-serif body, Spectral Latin, a four-colour chart semantics, and its own token scales. The published guide requires the `#F4F0E7` canvas, `#17130D` text, serif end-to-end, `#EFE6D2` as the primary field and action colour, and the official mark in `brand/logo.png`. Follow the published guide; reuse export components only after restyling them onto `brand/`.

## Foundation layer (`brand/`)

| File | Role |
|---|---|
| `fonts.css` | `@font-face` for Noto Serif SC, Noto Serif and IBM Plex Mono: local font first, then `brand/fonts/*.woff2` (not bundled, see `brand/fonts/README.md`). Load first. |
| `icons.svg` | Seventeen line icons, circles and lines only, 1.5 stroke, `currentColor`. Pages inline the sprite between `icons:start` and `icons:end` markers so `<use href="#ts-…">` works on `file://`; `scripts/sync_icons.py` keeps the copies identical. |
| `tokens.css` | Published palette plus derived surfaces, text roles, chart series, type scale, spacing, layout, radius, motion. Load first. |
| `base.css` | Element defaults on the foundation: serif everywhere, body 18/1.7, headings 600, captions uppercase in deep gold, mono only for data, reduced motion, print. |
| `components.css` | CSS-only components with the `.ts-` prefix, plus `.ts-icon` and the `.ts-ground-charcoal` scope that inverts every component for an opener, closer or a single card: container/grid/section, heading pair, display lockup, rules and frames, compass watermark, card (with 天干 index), token row, badges, ✓/✕ list, buttons, form fields, stat, quote, step marker, seal stamp, mark lockup, nav/header, ledger table, chart chrome, reveal. No raw colour values. |
| `index.html` | Offline specimen of everything above, in brand voice, bilingual. |
| `guide.md`, `source.json`, `logo.png` | Published guide, provenance snapshot, official mark. |
| `tokens.json` | Generated Design Tokens (DTCG) export of `tokens.css` for other tools; `python3 scripts/export_tokens.py`. |
| `VERSION` | System version, must match the guide. |

A new consumer imports the three CSS files in order and uses the `.ts-` classes or the tokens directly. The foundation does not restyle the export.

## Consumers

**Sales deck (`deck/`).** `index.html` holds the slides as static sections at a 1280 by 720 design size. `deck.js` scales the canvas to the window, handles keyboard, tap and hash navigation, and shows a counter. `deck.css` carries the slide type scale (nothing under 19px) and the print layout. Slides: 封面, 承诺, 导航四件套, 经营五问, 以样张为证, 利润失于何处, 90 天行动清单, 成熟度阶梯, 信条, 服务与价格, 伙伴背书, 专家顾问团, 联系. Opener and closer sit on charcoal with the mark on an ink tile, since the mark is never recoloured.

**Website (`website/`).** `index.html` sections: hero, 导航四件套, 以样张为证 (five chapter figures and the 90-day ledger), 经营五问, 服务与价格, 成熟度, 伙伴 and 专家顾问团, 信条, 联系, footer. `site.js` provides the mobile menu, active nav, accessible tabs, the stepper, the demo form and a one-time reveal. `site.css` is layout only.

Both consumers use the published tiers and prices from guide section 6 and reuse the export's copy where it does not conflict: the promise line, 经营五问, the partner list and the three testimonials. The export's 三层+X ladder, its `TIANSIGHT / INSIGHT` two-tone wordmark and its four-colour chart semantics are not used.

Placeholders that need real assets: expert portraits and names, the WeChat QR, partner logos (names are set in type), the proposal target and date on the deck cover. All figures are sample data and are labelled as such.

`scripts/check.py` verifies the same rules for `deck/`, `website/`, `report/` and `people/`, that generated outputs match their builders, and: tokens match the published theme and every row of the guide's colour table; the logo hash; serif-only font stacks with no Inter/Roboto; no raw colours or gradients outside `tokens.css`; radius limited to 2px, pill or circle; every `var(--x)` is declared; the specimen loads no remote resource or external script and no emoji; the deck and website obey the same colour, radius, font and offline rules with no undeclared tokens; the website avoids the guide's avoided lexicon; and the export manifest is intact. It also runs `scripts/export_tokens.py --check`, `scripts/build_dist.py --check`, `scripts/check_contrast.py` (every real colour pairing against WCAG 2.1, translucent tokens composited over their ground) and `scripts/lint_html.py` (lang, title, one `h1`, `<main>`, heading order, alt text, labels, accessible names, unique ids, resolvable anchors and targets on every page). With `--render` it runs `node scripts/snapshot.mjs --check`, which renders all pages at desktop and mobile widths and compares overflow, structure and height against `snapshots/layout.json`; refresh that baseline with `--update` when a layout change is intended. Run it before committing.

## People layer (`people/`)

One data file drives every co-founder surface. `people/people.json` holds the five entries (name, English name, title, focus, one-line bio, quotable line, contact) plus company strings; every value is a placeholder until the founders confirm them. Portraits go in `people/photos/founder-01.png` to `founder-05.png` in the order supplied; the portrait tile multiplies the photo onto the ink field so a white background disappears without editing, and shows a labelled tile while a file is missing.

```sh
python3 scripts/build_people.py      # renders the surfaces below from the templates
node scripts/export_people.mjs       # people/export/: 20 social PNGs and namecards.pdf (needs playwright)
```

| Output | Surface |
|---|---|
| `website/team.html` | 团队 page: five profile cards, three quoted voices, full profiles, contact band. Linked from the site nav. |
| `deck/index.html` | Six generated slides between the `people:start` and `people:end` markers: a team slide and one spotlight per founder. |
| `people/blocks.html` | Block specimen with usage: portrait tile sizes, profile card, compact row, byline, voice, signature with seal, team grid. |
| `people/namecards.html` | 90 × 54 mm cards, three faces per founder (front, portrait, back); print gives one face per page. |
| `people/social.html` | Four artboards per founder: 1080 × 1080, 1200 × 628, 900 × 383 公众号 cover, 1080 × 1920 story. |

`people/people.css` carries the `.ts-portrait`, `.ts-identity` and block classes and is loaded after the brand stylesheets.

## HTML report system and skills (`html-system/`, `skills/`, `reference/`)

Three delivered decks were reviewed and catalogued (`reference/catalogue.md`, `reference/inventory.json`, sources under `reference/source/`). From them `html-system/` re-implements the slide system on the brand foundation: one `manifest.json` per report declares sources with evidence grades, fields, metrics with formulas, slides with their sources and explanation panel, quality results and versions; `build_deck.py` renders the deck (or a long-scroll report) with generated cover, TOC, evidence base, evidence map, change log, quality, limitations, source log, glossary and a drill-down appendix; `charts.py` draws eleven chart families as inline SVG with data roles; `report.js` adds drill-down, tooltips, keyboard and URL state; `check_report.py` is the gate (provenance links, grades, footer versions, offline, slide overflow); `dq_checks.py` and `version_diff.py` support the data-quality and versioning skills.

```sh
python3 html-system/build_deck.py html-system/sample
python3 html-system/check_report.py html-system/sample --layout
```

`skills/` holds six skills for agents: `ts-html-report` (workflow), `ts-dataviz-modules`, `ts-data-provenance`, `ts-data-quality`, `ts-report-versioning`, `ts-webapp-interactive`. Start at `skills/README.md`.

## Decisions taken in the foundation

- **Primary button** is the ink field (`#EFE6D2`) with charcoal text and a gold hairline border, because ink against the canvas is only 1.09:1 and needs an edge. Press moves it down 1px, like a stamp.
- **Bright gold `#D4A862`** is 1.9:1 on the canvas, so the foundation uses it only at 28px and above, for active states, and on charcoal (8.4:1). Small captions use deep gold; token-row hex values use deep gold for the same reason.
- **`--gold` and `--gold-deep`** are both `#76551F` in v0.6. Both tokens are kept so they can diverge later.
- **Mark.** The guide describes a compass ring with 侍; the published asset is the circular 侍天 seal. The foundation uses the published asset and draws the compass only as a watermark.
- **Charts** follow guide §5: one series bright gold, two adds charcoal, three adds vermillion; ticks in ink muted. The export's growth/loss/caution/datum colours are not in the guide and are not in the foundation.
- **Fonts** are declared in `brand/fonts.css` but not bundled. Drop the woff2 files listed in `brand/fonts/README.md` into `brand/fonts/`; until then stacks fall back to local serifs, never sans-serif, and the check script lists the missing files.
- **Vermillion seal stamp** is a CSS placeholder. The real 朱印 needs calligraphy artwork.
- **Offer.** The consumers use the guide's four priced tiers, not the export's unpriced 三层+X ladder. The export's 经营五问, promise line, partner names and testimonials are reused where they do not conflict.
- **Lexicon.** "增长在何处" stays verbatim in the promise; elsewhere 增长 becomes 增利 to follow the guide's avoided-word list.
- **Report charts** stay within the three-series rule: vermillion marks warnings and losses only, and the heatmap's negative side. The export's four semantic chart colours are not used.

## Open questions for the brand owner

1. Accept the gold hairline on the primary button, or make the charcoal solid button the primary action?
2. Keep bright gold for the 智慧领航者 tagline at body size, or move it to deep gold?
3. Should deep gold get its own value so captions differ from structural rules?
4. Compass mark or seal: which is the primary 标志 going forward?
5. Does the report need semantic chart colours beyond the three-series rule?
6. Font hosting target and subsetting.
7. Which consumer migrates first? Recommendation: the website, as the entry surface with the widest component coverage.
8. All prices, customer quotes and partner names come from the guide or the export and need verification before publication.
9. The export's 三层+X ladder (经营洞察 / 第二大脑共建 / AI 原生品牌 / 增值专项) and the guide's four priced tiers describe the offer differently. The consumers follow the guide. Confirm which is current.
10. The guide's lexicon avoids 增长, but the product promise "增长在何处、利润失于何处" uses it. It is kept verbatim in the promise and replaced by 增利 elsewhere. Confirm.
11. The deck uses charcoal grounds for its opener and closer, which the guide does not explicitly allow. Confirm or switch them to pale.

## Continue development

1. Settle the open questions above, then bump `brand/guide.md` and `source.json` when the published guide changes.
2. Build the report consumer (`report/`): 决策维度, 分析维度, 趋势与归因, 方法论地图 pages and the five insight matrices, print-first on A4, reusing the chart chrome and ledger from the website.
3. Replace placeholders in the deck and website as assets arrive; wire the contact form to a backend when one exists.
4. Add self-hosted fonts (`brand/fonts.css`) once the hosting target and subset strategy are chosen.
5. Validate interactions, keyboard navigation and mobile layouts after each change, then run `python3 scripts/check.py` before committing.

No product backend, application framework or deployment target is configured by this baseline. Demo copy, prices and customer claims require verification before publication.
