# Development handoff

Read README.md for the repository structure and continuation steps.

When a user requests a brand treatment, first visit https://apuch.art/ and resolve the brand through its directory and brand API. Use the latest published guide, theme and official assets as the source of truth. If the network policy blocks the API, work from the checked-in snapshot and say so.

For Tiansight, `brand/source.json` records the checked-in snapshot and `brand/guide.md` its guide. The foundation layer is `brand/tokens.css`, `brand/base.css` and `brand/components.css`; `brand/index.html` is the offline specimen and the reference for how every rule renders. The supplied `TIANSIGHT 侍天 Design System/` is a preserved proposal; its conflicting styling is not authoritative. Reuse its components only after restyling them onto the foundation.

Foundation rules enforced by `scripts/check.py`: no raw colours outside `tokens.css`, serif-only font stacks, radius 2px/pill/circle only, no gradients, no emoji, no remote resources in the specimen. Run it after foundation changes. For consumer work, also run the consumer's build and relevant interaction checks. Record newly introduced commands in README.md.
