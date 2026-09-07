# Changelog

Versions follow the published brand guide. The system version is in `brand/VERSION`.

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
