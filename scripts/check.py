"""Offline baseline check: python3 scripts/check.py."""
from pathlib import Path
import hashlib
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
brand = root / 'brand'
source = json.loads((brand / 'source.json').read_text())
guide = (brand / 'guide.md').read_text()
tokens = (brand / 'tokens.css').read_text()
base = (brand / 'base.css').read_text()
components = (brand / 'components.css').read_text()
specimen = (brand / 'index.html').read_text()
problems = []


def token_value(name):
    match = re.search(r'--' + re.escape(name) + r':\s*([^;]+);', tokens)
    return match[1].strip() if match else None


# 1. Published theme → tokens.css
mapping = {'surface': 'surface', 'paper': 'paper', 'ink-primary': 'primary',
           'charcoal': 'ink', 'gold': 'accent', 'ink-muted': 'muted', 'seal': 'secondary'}
for token, key in mapping.items():
    value = token_value(token)
    if not value or value.lower() != source['theme'][key].lower():
        problems.append(f'tokens.css --{token} != theme.{key}')
line = token_value('line')
if not line or re.sub(r'\s', '', line) != re.sub(r'\s', '', source['theme']['line']):
    problems.append('tokens.css --line != theme.line')

# 2. Guide colour table → tokens.css (every row of §1)
guide_rows = re.findall(r'^\| `--([a-z-]+)` \|[^|]*\| `(#[0-9A-Fa-f]{6})` \|', guide, re.M)
if len(guide_rows) < 9:
    problems.append('guide colour table not found')
for token, hexval in guide_rows:
    if (token_value(token) or '').lower() != hexval.lower():
        problems.append(f'tokens.css --{token} != guide {hexval}')

# 3. Official logo
if hashlib.sha256((brand / 'logo.png').read_bytes()).hexdigest() != source['logo']['sha256']:
    problems.append('logo.png hash mismatch')
if 'Serif everywhere' not in guide:
    problems.append('guide.md missing "Serif everywhere"')

# 4. Foundation policy: serif fallbacks only, no banned families, no raw colour outside tokens.css
for name, css in (('tokens.css', tokens), ('base.css', base), ('components.css', components)):
    for family in re.findall(r'--font-[a-z]+:\s*([^;]+);', css):
        if 'sans-serif' in family:
            problems.append(f'{name}: sans-serif fallback in font stack')
    if re.search(r'\b(Inter|Roboto|Arial|Helvetica)\b', css):
        problems.append(f'{name}: banned font family')
    if name != 'tokens.css' and re.search(r'#[0-9A-Fa-f]{3,8}\b|rgba?\(', css):
        problems.append(f'{name}: raw colour value, use a token')
    for radius in re.findall(r'border-radius:\s*([^;]+);', css):
        if radius not in ('var(--radius)', 'var(--radius-pill)', '50%'):
            problems.append(f'{name}: border-radius {radius} (only 2px, pill, 50%)')
    if 'linear-gradient' in css or 'radial-gradient' in css:
        problems.append(f'{name}: gradient')

# 5. Every var(--x) used in base/components/specimen is declared in tokens.css
declared = set(re.findall(r'--([a-z0-9-]+):', tokens + base + components + specimen))
declared |= {'span', 'span-md', 'swatch-color', 'mark-size', 'stamp-size', 'compass-size'}
used = set(re.findall(r'var\(--([a-z0-9-]+)', base + components + specimen))
for missing in sorted(used - declared):
    problems.append(f'undeclared token --{missing}')

# 6. Specimen is offline: no remote scripts, styles, fonts, or images
for url in re.findall(r'(?:src|href)="(https?://[^"]+)"', specimen):
    problems.append(f'index.html loads remote resource {url}')
if '<script' in specimen:
    problems.append('index.html contains script')
for ref in re.findall(r'(?:src|href)="([^"#:]+)"', specimen):
    if not (brand / ref).is_file():
        problems.append(f'index.html references missing file {ref}')
if re.search(r'[\U0001F300-\U0001FAFF☀-➿]', specimen.replace('✓', '').replace('✕', '')):
    problems.append('index.html contains emoji')

# 7. Consumers (deck, website) follow the same policy and stay offline
PHOTO = re.compile(r'photos/(founder-0[1-5]|missing)\.png$')
missing_photos = set()
for consumer in ('deck', 'website', 'report', 'people'):
    folder = root / consumer
    pages = sorted(folder.glob('*.html'))
    html = ''.join(p.read_text() for p in pages)
    css = ''.join(f.read_text() for f in folder.glob('*.css'))
    if re.search(r'#[0-9A-Fa-f]{3,8}\b|rgba?\(', css):
        problems.append(f'{consumer}: raw colour value in CSS, use a token')
    for style in re.findall(r'style="([^"]*)"', html):
        if re.search(r'#[0-9A-Fa-f]{3,8}\b|rgba?\(', style):
            problems.append(f'{consumer}: raw colour value in inline style')
            break
    for radius in re.findall(r'border-radius:\s*([^;]+);', css):
        if radius not in ('var(--radius)', 'var(--radius-pill)', '50%', '0'):
            problems.append(f'{consumer}: border-radius {radius}')
    if re.search(r'\b(Inter|Roboto|Arial|Helvetica)\b', css) or 'sans-serif' in css:
        problems.append(f'{consumer}: banned or sans-serif font family')
    for url in re.findall(r'(?:src|href)="(https?://[^"]+)"', html):
        problems.append(f'{consumer}: loads remote resource {url}')
    for ref in set(re.findall(r'(?:src|href)="([^"#:]+)"', html)):
        if (folder / ref).is_file():
            continue
        if PHOTO.search(ref):
            missing_photos.add(ref.split('/')[-1])
        else:
            problems.append(f'{consumer}: references missing file {ref}')
    if re.search(r'[\U0001F300-\U0001FAFF☀-➿]', html.replace('✓', '').replace('✕', '')):
        problems.append(f'{consumer}: contains emoji')
    used = set(re.findall(r'var\(--([a-z0-9-]+)', css + html))
    local = set(re.findall(r'--([a-z0-9-]+):', css + html))
    for missing in sorted(used - declared - local - {'h'}):
        problems.append(f'{consumer}: undeclared token --{missing}')
    if consumer == 'website':
        for word in ('赋能', '抓手', '闭环', '包治百病', '颠覆', '爆款', '裂变', '解决方案', '打法'):
            if word in html:
                problems.append(f'website: avoided lexicon "{word}"')

# 8. Generated outputs must match their builders
sys.path.insert(0, str(root / 'scripts'))
import build_report  # noqa: E402
import build_people  # noqa: E402
if build_report.render() != (root / 'report' / 'index.html').read_text():
    problems.append('report/index.html is stale: run python3 scripts/build_report.py')
for path, out in build_people.render_all().items():
    if not path.exists() or path.read_text() != out:
        problems.append(f'{path.relative_to(root)} is stale: run python3 scripts/build_people.py')

# 9. Supplied export is intact
export = root / 'TIANSIGHT 侍天 Design System'
manifest = json.loads((export / '_ds_manifest.json').read_text())
for entry in manifest['components']:
    if not (export / entry['sourcePath']).is_file():
        problems.append(f'export missing {entry["sourcePath"]}')
for entry in manifest['cards']:
    if not (export / entry['path']).is_file():
        problems.append(f'export missing {entry["path"]}')

if problems:
    print('FAIL')
    for problem in problems:
        print(' -', problem)
    sys.exit(1)
if missing_photos:
    print('note: portraits not yet supplied: ' + ', '.join(sorted(missing_photos)))
print(f"PASS: official palette, {len(guide_rows)} guide tokens, logo hash, foundation policy, "
      f"offline specimen, deck, website, report and people, {len(manifest['components'])} component exports and {len(manifest['cards'])} cards")
