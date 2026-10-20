#!/usr/bin/env python3
"""Package only public Korean runtime files, with a SHA-256 manifest."""

from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output'
DEST = OUT / 'site'


def package():
    files = [ROOT / 'index.html', ROOT / 'main.html', ROOT / 'assets/favicon.svg']
    for folder, pattern in [
        ('chapters', '*.html'),
        ('labs', '*.html'),
        ('appendix', '*.html'),
        ('assets/css', '*.css'),
        ('assets/js', '*.js'),
        ('assets/images/advanced', '*.svg'),
        ('downloads', '*.py'),
        ('downloads', '*.ipynb'),
        ('downloads', '*.json'),
    ]:
        files.extend(sorted((ROOT / folder).glob(pattern)))
    expected = {str(p.relative_to(ROOT)) for p in files} | {'.nojekyll', 'manifest.json'}
    if DEST.exists():
        unexpected = {str(p.relative_to(DEST)) for p in DEST.rglob('*') if p.is_file()} - expected
        if unexpected:
            raise SystemExit('Review unexpected output files before packaging: ' + str(unexpected))
    DEST.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for source in files:
        relative = source.relative_to(ROOT)
        target = DEST / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        manifest[str(relative)] = hashlib.sha256(source.read_bytes()).hexdigest()
    (DEST / '.nojekyll').write_text('')
    (DEST / 'manifest.json').write_text(
        json.dumps({'project': 'EDPilot0001', 'language': 'ko', 'files_sha256': manifest}, indent=2)
        + '\n'
    )
    archive = OUT / 'edpilot0001-static.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in sorted(expected):
            z.write(DEST / name, name)
    with zipfile.ZipFile(archive) as z:
        assert set(z.namelist()) == expected and z.testzip() is None
    print(json.dumps({'folder': str(DEST), 'zip': str(archive), 'files': len(expected)}))


if __name__ == '__main__':
    package()
