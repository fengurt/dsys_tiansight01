# Tiansight 侍天 design system

Development baseline for Tiansight. The supplied design-system export is preserved in `TIANSIGHT 侍天 Design System/`; the current published brand foundation is in `brand/`.

## Start here

```sh
python3 scripts/check.py
python3 -m http.server 8000 --bind 127.0.0.1
```

Open [the supplied website kit](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/ui_kits/website/index.html), [report kit](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/ui_kits/report/index.html), or [slides](http://127.0.0.1:8000/TIANSIGHT%20%E4%BE%8D%E5%A4%A9%20Design%20System/slides/index.html).

These are reference previews, using CDN scripts/fonts and a prebuilt bundle. They require internet access and are not a production build pipeline.

## Source of truth

The [brand directory](https://apuch.art/) resolves Tiansight to the [published brand API](https://apuch.art/api/brands/tiansight.json). `brand/source.json` records the version, theme, retrieval date and official logo hash. `brand/guide.md` contains the published primary guide; `brand/tokens.css` exposes its foundation for new work. Import that CSS in a new consumer; it intentionally does not restyle the supplied export.

The export is a separate proposal: it uses parchment `#EFE6D2` as the page background, sans-serif body text, Spectral Latin text, and a different seal. The published guide requires `#F4F0E7` canvas, `#17130D` text, serif typography throughout, and the official mark in `brand/logo.png`. Follow the published guide when migrating components. Additional scales in the export are proposals, not published brand tokens.

Fonts are not bundled. The official CSS uses local serif fallbacks; arrange licensed/self-hosted Noto fonts when a production target is selected. Bright gold is decorative on pale surfaces; use charcoal or deep gold for readable small text.

## Continue development

1. Choose the first consumer: website, report, or sales deck.
2. Reuse the matching exported components, migrating their styles to the published foundation. Component source, declarations and prompt notes live together.
3. Add a build pipeline for that consumer. The supplied `_ds_bundle.js` is generated output with no included rebuild command; editing JSX alone does not update bundled previews.
4. Validate changed interactions, keyboard navigation and mobile layouts in the consumer, then run `python3 scripts/check.py` before committing.

No product backend, application framework, deployment target, or remote Git repository is configured by this baseline. Demo copy, prices and customer claims require verification before publication.
