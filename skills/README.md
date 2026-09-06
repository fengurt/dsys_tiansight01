# Tiansight report skills · 报告技能集

Six skills that make every agent produce HTML slides and reports to the same standard: branded on
`brand/`, every number with a source, a 口径 and a formula, explained in a dedicated module rather
than the body, and drillable in the web build. They were written from the review of three delivered
decks (`reference/catalogue.md`) and point at the reference implementation in `html-system/`.

| Skill | Use it when | Owns |
|---|---|---|
| `ts-html-report` | building or revising any HTML slide deck or long-scroll report | the workflow, slide anatomy, writing rules, build and gate |
| `ts-dataviz-modules` | choosing or drawing a chart, table, KPI or ledger | chart families, encoding rules, `charts.py` |
| `ts-data-provenance` | declaring sources, grading evidence, writing 口径 and formulas, the appendix | manifest sources / metrics / meta, EGA, appendix |
| `ts-data-quality` | before any number enters a report | the check list, thresholds, the 质量异常 slide, `dq_checks.py` |
| `ts-report-versioning` | a report changes, data is refreshed, a caliber is fixed | versions, change log slide, source→metric→slide mapping, `version_diff.py` |
| `ts-webapp-interactive` | the report is served as a web app with drill-down | `report.js` hooks, URL state, tooltips, filters |

Load `ts-html-report` first; it tells you when to load the others. Every skill is self-contained
enough to be copied into another repository together with `html-system/` and `brand/`.

```sh
python3 html-system/build_deck.py <report-dir>          # manifest → index.html
python3 html-system/check_report.py <report-dir> --layout
python3 html-system/dq_checks.py data/table.csv --key 品项名称 --value 总销量 --rate 复购点击率 --num 复购数量 --den 总销售数量
python3 html-system/version_diff.py old/manifest.json new/manifest.json
python3 scripts/inventory_reference.py                  # catalogue new reference assets
```
