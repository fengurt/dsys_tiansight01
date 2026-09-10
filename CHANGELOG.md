# Changelog

Versions follow the published brand guide. The system version is in `brand/VERSION`.

## v0.7 · 2026-09-10 · Connected product distribution

- Deterministic, namespaced product foundation with per-asset hashes, reusable application patterns, safe DOM runtime and chart theme access.
- Self-hosted WOFF2 subsets with provenance and OFL licenses.
- Separate caption color/size tokens; token export rejects duplicate declarations and preserves typography types.
- Gold focus/control borders and functional chart marks. Existing versioned CSS pins remain frozen; new content-addressed outputs are generated.
- Product unit tests and reviewed specimen layout baselines. See `docs/product-distribution.md` for consumer ownership and upgrades.

## v0.7 · 2026-09-09 · Rulings

- Open questions 1, 2, 3, 10 and 11 closed by the brand owner (`docs/foundation-review.md`): primary button stays the ink field with gold hairline; tagline 智慧领航者 sets in deep gold at every size; `--gold-deep` keeps its own token at the same hex; 增长 stays verbatim in the promise line; deck opener and closer return to pale manuscript with the compass watermark, charcoal limited to the fourth tier card.
- Mark lockup: the mark already reads 侍天, so the CN name is no longer set beside it — header lockups and footers pair the mark with "Tiansight" only (website, team page, specimen, hub, deck, report, people templates and builder).
- Published into `brand/tokens.css`: gold ramp 100–700 with `--gold-hover` / `--gold-press`; four shadow steps for dialogs; interface type steps `--type-ui/table/badge/tick`; semantic chart set for reports; inverse-surface tokens for the single charcoal card. Guide §1, §2, §3, §5, §7 amended.
- `components.css`: secondary, quiet and nav hovers darken along the gold ramp instead of swapping tokens; open dialogs carry `--shadow-3`; `.ts-wordmark b` deprecated.
- `deck.css`: `.slide.charcoal` and `.mark-tile` rules removed.
- `check.py` 8g: charcoal never a page ground, one charcoal card per section, tagline never bright gold on pale, semantic chart colours report-only, no CN name beside the mark, ramp values.

## v0.6 · 2026-09-07 · Distribution

- `dist/`: one-file bundle `tiansight.css` (latest channel) and `tiansight-v0.6.css` (pinned), plus `tokens.json`, `icons.svg` and a working `example.html`, built by `scripts/build_dist.py` and verified by the gate.
- Long code lines wrap instead of overflowing on narrow screens (`pre { overflow-wrap: anywhere }`).

## v0.6 · 2026-09-07 · Solidity pass

- Tokens exported to `brand/tokens.json` (Design Tokens Community Group format, mobile mode as an extension); `scripts/export_tokens.py --check` keeps it in step.
- New components: skip link, visually-hidden helper, tag, notice (default, key, warn), disclosure, tabs (line and pill), tooltip, breadcrumb, pagination, progress, dialog, sortable header affordance. Explicit focus, pressed, disabled, read-only and selected states for buttons, fields and cards.
- Specimen section 05b: interaction, states and motion, with live tabs, dialog and the three motion durations.
- Accessibility lint `scripts/lint_html.py` over every page; pages fixed to one `h1`, a `<main>` landmark, no skipped heading levels, skip links on the website, team page and specimen.
- Layout regression harness `scripts/snapshot.mjs` with the committed baseline `snapshots/layout.json`; `python3 scripts/check.py --render` runs it.
- Hatch pattern for design values emitted once per report page instead of once per chart (no duplicate ids).
- Documentation: `docs/principles.md`, `docs/quickstart.md`, `docs/contributing.md`.

## v0.6 · 2026-09-06 · HTML report system

- `html-system/`: manifest-driven report and deck builder, eleven chart families, data roles, provenance appendix, evidence grades E1 to E4, quality checks, version diff.
- `skills/`: six skills for agents producing reports on this system.
- `reference/`: inventory of the three reviewed decks.

## v0.6 · 2026-09-05 · People layer and refinement

- Co-founder profiles across website, deck, blocks, name cards and social sizes from `people/people.json`.
- Self-hosted font declarations, inline icon sprite, charcoal ground scope, hub page.

## v0.6 · 2026-09-04 · Foundation and consumers

- `brand/tokens.css`, `base.css`, `components.css`, specimen, check script.
- Sales deck, website and A4 diagnostic report on the foundation.
