# Development handoff

Read README.md for the repository structure and continuation steps.

When a user requests a brand treatment, first visit https://apuch.art/ and resolve the brand through its directory and brand API. Use the latest published guide, theme and official assets as the source of truth.

For Tiansight, `brand/source.json` records the checked-in snapshot and `brand/guide.md` its guide. The supplied `TIANSIGHT 侍天 Design System/` is a preserved proposal; its conflicting styling is not authoritative. Reuse its components after checking the published guide.

Run `python3 scripts/check.py` after foundation changes. For consumer work, also run the consumer's build and relevant interaction checks. Record newly introduced commands in README.md.
