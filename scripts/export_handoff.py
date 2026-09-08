"""Package the co-founder profile content for a human designer: python3 scripts/export_handoff.py

Writes people/export/tiansight-profiles-handoff.zip containing the copy as Markdown, the portraits,
the brand mark, a one-page brand spec, the structured data and the founders' original PDFs. Nothing
in the zip depends on this repository's HTML or CSS — it is the content, not a layout.
"""
from pathlib import Path
import json
import shutil
import sys
import zipfile

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'people' / 'profiles.json').read_text(encoding='utf-8'))
out = root / 'people' / 'export'
stage = out / 'handoff'
UPLOADS = Path('/root/.claude/uploads/0a17cf55-b0d3-5df0-83b8-b63fc3055f4c')
ORIGINALS = {'bian-jiang': 'd4052037-bianjianga4profile_21.pdf', 'guo-feng': 'ea835bdb-guofenga4profile.pdf'}


def md_profile(profile):
    """The whole profile as Markdown: one heading per block, tables where the layout is a table."""
    src = data['sources'][profile['source']]
    aux_on = [t for t in profile['titles_aux'] if t['show']]
    aux_off = [t for t in profile['titles_aux'] if not t['show']]
    L = [f'# {profile["name"]} {profile["en"]}', '',
         f'> {profile["domain"]}　·　{profile["domain_zh"]}', '',
         '## 职务 Titles', '',
         f'**主职务（固定）**：{profile["title_main"]}', '',
         '**辅助职务（最多显示三个）**：']
    L += [f'{i}. {t["zh"]}' + (f'　*{t["en"]}*' if t.get('en') else '') for i, t in enumerate(aux_on, 1)]
    if aux_off:
        L += ['', '备选，当前不显示：'] + [f'- {t["zh"]}' for t in aux_off]
    L += ['', '## 一句话简介 Lede', '', profile['lede'], '',
          '## 关键数字 Key figures', '',
          '| 数值 | 英文标签 | 中文说明 | 口径 | 等级 |', '|---|---|---|---|---|']
    L += [f'| **{f["value"]}{f.get("unit", "")}** | {f["label"]} | {f["zh"]} | {f.get("note", "")} | {f["grade"]} |'
          for f in profile['figures']]
    L += ['', '## 个人简介 Profile', ''] + [p + '\n' for p in profile['summary']]
    L += ['## 全案经验 Operating principles', '']
    for p in profile['principles']:
        L += [f'### {p["title"]}', '', p['body'], '']
    L += ['## 履历 Roles, education and training', '',
          '| 时间 | 职务 | 机构 | 备注 |', '|---|---|---|---|']
    for r in profile.get('roles', []) + profile.get('education', []):
        L.append(f'| {r.get("period", "")} | {r["title"]} | {r.get("org", "")} | {r.get("note", "")} |')
    for t in profile.get('trainings', []):
        detail = ' · '.join(t[k] for k in ('role', 'scale', 'region') if t.get(k))
        L.append(f'| {t.get("period", "")} | {t["title"]} | {t.get("org", "")} | {detail} |')
    L += ['', f'## 服务覆盖 {"Brand portfolio" if profile.get("brands") else "Service portfolio"}', '',
          profile['portfolio_lede'], '']
    if profile.get('brands'):
        L += ['| 品类 | 品牌 |', '|---|---|']
        L += [f'| **{g["group"]}** | {"、".join(g["items"])} |' for g in profile['brands']]
    else:
        L += ['| 方向 | 内容 |', '|---|---|']
        L += [f'| **{s["group"]}** | {s["body"]} |' for s in profile['services']]
    L += ['', '## 核心能力 Capability model', '']
    L += [f'{i}. **{c["title"]}**' for i, c in enumerate(profile['capabilities'], 1)]
    L += ['', '## 选摘案例 Selected cases', '']
    names = {c['id']: c['title'] for c in profile['capabilities']}
    for n, case in enumerate(profile['cases'], 1):
        L += [f'### 案例 {n}：{case["title"]}', '', '| 字段 | 内容 |', '|---|---|']
        L += [f'| {f["k"]} | {f["v"]} |' for f in case['facts']]
        L += ['', '**产品策略 Product strategy**', '', case['strategy'], '',
              '**经营结果 Business result**', '', '| 指标 | 数值 | 口径 | 等级 |', '|---|---|---|---|']
        L += [f'| {r["metric"]} | **{r["value"]}** | {r["window"]} | {r["grade"]} |' for r in case['results']]
        caps = '、'.join(names[c] for c in case.get('capabilities', []))
        L += ['', f'*本案涉及能力：{caps}*', '']
    L += ['## 数据出处与口径 Sources', '',
          f'本文档全部数字来源：**{src["label"]}**（{src["kind"]}，{src["date"]}），证据等级 **{src["grade"]}**。', '',
          '| 等级 | 含义 |', '|---|---|']
    L += [f'| {k} | {v} |' for k, v in data['grades'].items()]
    items = [i['text'] for i in data['open_items'] if i['profile'] in ('*', profile['id'])]
    L += ['', '**待核 Open items**', ''] + [f'- {t}' for t in items]
    edits = [e for e in data['lexicon_edits'] if e['profile'] == profile['id']]
    if edits:
        L += ['', '**语汇调整 Lexicon edits**（依品牌指南语汇表，原稿用词已替换）', '']
        L += [f'- 「{e["from"]}」→「{e["to"]}」：{e["why"]}' for e in edits]
    L += ['', '---', '', f'*侍天 Tiansight · A Member of the Table AI Alliance · {data["version"]} · {data["issued"]}*', '']
    return '\n'.join(L)


BRAND_SPEC = """# 侍天 Tiansight — 品牌速查 Brand spec

给排版设计师的一页速查。完整指南见 `brand/guide.md`（仓库内）。

## 一句话

素墨为纸、玄墨为字、土金为骨；沉稳敢言、有据可依。
*Ink is the paper, charcoal is the voice, gold is the structure — composed, forthright, evidence-based.*

## 色彩 Palette

| 名称 | Hex | 用途 | 画面占比 |
|---|---|---|---|
| 淡墨纸 Pale Manuscript | `#F4F0E7` | 页面底色，避免纯白 | ≈ 78% |
| 宣纸 Paper | `#FFFDF8` | 内容层、卡片、图片衬底 | — |
| 素墨 Ink（主色） | `#EFE6D2` | 色块、关键操作；不作文字色 | ≈ 7% |
| 玄墨 Charcoal | `#17130D` | 标题与正文 | ≈ 12% |
| 土金 Earth Gold | `#76551F` | 描边、分隔线、题注 | ≈ 3% |
| 明金 Bright Gold | `#D4A862` | 关键数字、激活态；浅底上仅用于大字号 | 少量 |
| 素墨灰 Ink Muted | `#706758` | 辅助文字 | — |
| 朱红 Vermillion | `#8C3228` | 印章、否定、警示；从不作为色块 | ≤ 5% |

发丝线 `rgba(23,19,13,0.18)`　卡片描边 `rgba(118,85,31,0.34)`

## 字体 Typography

- **中文**：Noto Serif SC 思源宋体 — 600 标题 / 400 正文 / 300 辅助。回退：Source Han Serif SC → Songti SC → STSong，**永不落到无衬线**。
- **英文**：Noto Serif — 全大写，字距 0.30–0.34em，仅作题注与标签。
- **数字与代码**：IBM Plex Mono — 仅用于数字、价格、日期、令牌。

## 规矩 Rules

- 圆角 2px；只有状态徽章用胶囊形。
- 无渐变、无表情符号、无 Inter / Roboto、无「圆角＋左侧色条」卡片。
- 手绘图形不超过圆与线（罗盘、印章）。
- 玄墨底只用于开篇、收尾或单张卡片，不铺满整份文件。
- 避免用词：赋能、抓手、闭环、包治百病、颠覆、爆款、裂变、解决方案、打法。以「增利」代「增长」（产品承诺句除外）。

## 版面 Format

- A4 纵向 210 × 297mm，页边距 14–16mm。
- 完整版七页：封面 / 个人简介 / 服务覆盖与核心能力 / 案例 ×3 / 数据出处。
- 一页版：单页 A4，同样的主张压缩。
- 每页保留侍天标志位与一个合作方 LOGO 位。
"""

README = f"""# 侍天联合创始人履历 — 设计交付包

给排版设计师的内容包。**这里没有版式，只有内容、图片与品牌规范**，版式由设计师决定。

## 目录

```
content/            文案（Markdown）
  bian-jiang.md       边江，完整内容
  guo-feng.md         郭峰，完整内容
  profiles.json       同样的内容，结构化数据；每条经历有分类，每个数字有出处与等级
photos/             肖像
  bian-jiang.png      388 × 488 px
  guo-feng.png        435 × 542 px
brand/              品牌
  brand-spec.md       一页速查：色彩、字体、规矩、版面
  logo.png            侍天标志
  tokens.json         全部设计令牌（Design Tokens 格式），可导入设计工具
reference/          原始材料
  bian-jiang-original.pdf
  guo-feng-original.pdf
```

## 三件需要注意的事

1. **肖像分辨率偏低。** 两张肖像是从原始 PDF 中提取的，388 × 488 与 435 × 542 px。屏幕与小尺寸印刷可用，整页大图或高精度印刷请向本人索取 1200px 以上原图。
2. **每个数字都有出处。** 全部数字来自本人提供的 A4 Profile，证据等级 E4（未验证）。客户可见版本前请逐条确认。各文档末尾的「数据出处与口径」列出了全部条目与待核事项。
3. **两处待本人确认。** 边江封面写「原海底捞高级品牌总监」，简介写「品牌高级经理」，职级表述不一致；联系方式尚未提供。

## 需要的两个版本

- **完整版**：A4 多页，封面、个人简介、服务覆盖与核心能力、三个案例、数据出处。
- **一页版**：单页 A4，同样的主张压缩到一页。

主职务统一为「侍天联合创始人」，辅助职务最多显示三个（文档中已标出当前选定的三个与备选项）。

*侍天 Tiansight · A Member of the Table AI Alliance · {data["version"]} · {data["issued"]}*
"""


def build():
    if stage.exists():
        shutil.rmtree(stage)
    for sub in ('content', 'photos', 'brand', 'reference'):
        (stage / sub).mkdir(parents=True)
    notes = []
    for profile in data['profiles']:
        (stage / 'content' / f'{profile["id"]}.md').write_text(md_profile(profile), encoding='utf-8')
        photo = root / 'people' / profile['photo']
        if photo.is_file():
            shutil.copy(photo, stage / 'photos' / f'{profile["id"]}.png')
        else:
            notes.append(f'portrait missing: {profile["photo"]}')
        original = UPLOADS / ORIGINALS.get(profile['id'], '')
        if original.is_file():
            shutil.copy(original, stage / 'reference' / f'{profile["id"]}-original.pdf')
        else:
            notes.append(f'original PDF not available for {profile["id"]}')
    (stage / 'content' / 'profiles.json').write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (stage / 'brand' / 'brand-spec.md').write_text(BRAND_SPEC, encoding='utf-8')
    shutil.copy(root / 'brand' / 'logo.png', stage / 'brand' / 'logo.png')
    shutil.copy(root / 'brand' / 'tokens.json', stage / 'brand' / 'tokens.json')
    (stage / 'README.md').write_text(README, encoding='utf-8')

    zip_path = out / 'tiansight-profiles-handoff.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(stage.rglob('*')):
            if f.is_file():
                z.write(f, Path('tiansight-profiles-handoff') / f.relative_to(stage))
    for n in notes:
        print('note:', n)
    print(f'wrote {zip_path.relative_to(root)} ({zip_path.stat().st_size:,} bytes, '
          f'{sum(1 for f in stage.rglob("*") if f.is_file())} files)')
    return 0


if __name__ == '__main__':
    sys.exit(build())
