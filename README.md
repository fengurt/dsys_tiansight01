# Tiansight 侍天 design system

Development baseline for Tiansight. The published brand foundation lives in `brand/`; the supplied design-system export is preserved unchanged in `TIANSIGHT 侍天 Design System/`.

## Start here

```sh
python3 scripts/check.py
python3 -m http.server 8000 --bind 127.0.0.1
```

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
| `tokens.css` | Published palette plus derived surfaces, text roles, chart series, type scale, spacing, layout, radius, motion. Load first. |
| `base.css` | Element defaults on the foundation: serif everywhere, body 18/1.7, headings 600, captions uppercase in deep gold, mono only for data, reduced motion, print. |
| `components.css` | CSS-only components with the `.ts-` prefix: container/grid/section, heading pair, display lockup, rules and frames, compass watermark, card (with 天干 index), token row, badges, ✓/✕ list, buttons, form fields, stat, quote, step marker, seal stamp, mark lockup, nav/header, ledger table, chart chrome, reveal. No raw colour values. |
| `index.html` | Offline specimen of everything above, in brand voice, bilingual. |
| `guide.md`, `source.json`, `logo.png` | Published guide, provenance snapshot, official mark. |

A new consumer imports the three CSS files in order and uses the `.ts-` classes or the tokens directly. The foundation does not restyle the export.

## Consumers

**Sales deck (`deck/`).** `index.html` holds the slides as static sections at a 1280 by 720 design size. `deck.js` scales the canvas to the window, handles keyboard, tap and hash navigation, and shows a counter. `deck.css` carries the slide type scale (nothing under 19px) and the print layout. Slides: 封面, 承诺, 导航四件套, 经营五问, 以样张为证, 利润失于何处, 90 天行动清单, 成熟度阶梯, 信条, 服务与价格, 伙伴背书, 专家顾问团, 联系. Opener and closer sit on charcoal with the mark on an ink tile, since the mark is never recoloured.

**Website (`website/`).** `index.html` sections: hero, 导航四件套, 以样张为证 (five chapter figures and the 90-day ledger), 经营五问, 服务与价格, 成熟度, 伙伴 and 专家顾问团, 信条, 联系, footer. `site.js` provides the mobile menu, active nav, accessible tabs, the stepper, the demo form and a one-time reveal. `site.css` is layout only.

Both consumers use the published tiers and prices from guide section 6 and reuse the export's copy where it does not conflict: the promise line, 经营五问, the partner list and the three testimonials. The export's 三层+X ladder, its `TIANSIGHT / INSIGHT` two-tone wordmark and its four-colour chart semantics are not used.

Placeholders that need real assets: expert portraits and names, the WeChat QR, partner logos (names are set in type), the proposal target and date on the deck cover. All figures are sample data and are labelled as such.

`scripts/check.py` verifies: tokens match the published theme and every row of the guide's colour table; the logo hash; serif-only font stacks with no Inter/Roboto; no raw colours or gradients outside `tokens.css`; radius limited to 2px, pill or circle; every `var(--x)` is declared; the specimen loads no remote resource, script or emoji; the deck and website obey the same colour, radius, font and offline rules with no undeclared tokens; the website avoids the guide's avoided lexicon; and the export manifest is intact. Run it before committing.

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
