# Changelog

Versions follow the published brand guide. The system version is in `brand/VERSION`.

## v0.6 · 2026-09-07 · Co-founder profiles

- `people/profiles.json`: a classified履历 library for 边江 and 郭峰, transcribed from the A4 profiles they supplied. Ten categories, four evidence grades, every number bound to a source.
- `scripts/build_profiles.py`: builds a seven-page 完整版 and a one-page 一页版 per person plus the library index, and refuses to build on an undeclared source, an unknown category, a case naming a capability the profile does not have, or more than three auxiliary titles.
- Fixed main title 侍天联合创始人; auxiliary titles switch on the `show` flag, with a screen-only preview on the full page.
- Case pages carry a before-and-after strip drawn from the stated facts, and each names the capabilities it exercised.
- New `.ts-scroll-x` utility so a wide table scrolls in its own box instead of widening the page.
- The avoided-lexicon check now covers `people/` as well as `website/`; the block that documents a substitution is exempt.

## v0.6 · 2026-09-07 · Contrast audit

- `scripts/check_contrast.py`: computes all thirty colour pairings the system uses against WCAG 2.1, compositing translucent tokens over their ground, and verifies the ratios printed in the specimen. Wired into the gate.
- Fixed by the audit: the focus ring is now solid gold (2.2:1 → 6.0:1), control borders use the new `--control-border` token (2.2:1 → 3.4:1), the chart benchmark line reaches 3.3:1, and the chart axis line uses the axis colour.
- Two pairings the published guide mandates are recorded as waivers with what carries the meaning instead: bright gold as key numbers and as the first data series on light grounds. Open question 2 asks the brand owner to settle the first.
- `scripts/export_tokens.py` now fails on a token that matches no group instead of filing it under "other".

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
