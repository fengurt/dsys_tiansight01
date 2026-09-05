"""Offline baseline check: python3 scripts/check.py."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
brand = root / 'brand'
source = json.loads((brand / 'source.json').read_text())
css = (brand / 'tokens.css').read_text()
mapping = {'surface': 'surface', 'paper': 'paper', 'ink-primary': 'primary',
           'charcoal': 'ink', 'gold': 'accent', 'ink-muted': 'muted', 'seal': 'secondary'}
for token, key in mapping.items():
    value = re.search(r'--' + token + r':\s*([^;]+);', css)
    assert value and value[1].lower() == source['theme'][key].lower(), token
assert hashlib.sha256((brand / 'logo.png').read_bytes()).hexdigest() == source['logo']['sha256']
assert 'Serif everywhere' in (brand / 'guide.md').read_text()
export = root / 'TIANSIGHT 侍天 Design System'
manifest = json.loads((export / '_ds_manifest.json').read_text())
for entry in manifest['components']:
    assert (export / entry['sourcePath']).is_file(), entry['sourcePath']
for entry in manifest['cards']:
    assert (export / entry['path']).is_file(), entry['path']
print(f"PASS: official palette, logo hash, guide, {len(manifest['components'])} component exports and {len(manifest['cards'])} cards")
