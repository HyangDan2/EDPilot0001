#!/usr/bin/env python3
"""Add public downloads and a SHA-256 manifest to the Vite output."""

from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
DEST = OUT


def package():
    # Vite processes HTML, styles, scripts, and referenced SVG assets. Copy the
    # original downloadable files too, retaining the URLs used by page links.
    files = []
    for folder, pattern in [
        ('assets/css', '*.css'),
        ('assets/js', '*.js'),
        ('assets/images/advanced', '*.svg'),
        ('assets', '*.svg'),
        ('downloads', '*.py'),
        ('downloads', '*.ipynb'),
        ('downloads', '*.json'),
    ]:
        files.extend(sorted((ROOT / folder).glob(pattern)))
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
    archive = ROOT / 'output' / 'edpilot0001-static.zip'
    archive.parent.mkdir(parents=True, exist_ok=True)
    expected = {str(p.relative_to(DEST)) for p in DEST.rglob('*') if p.is_file()}
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in sorted(expected):
            z.write(DEST / name, name)
    with zipfile.ZipFile(archive) as z:
        assert set(z.namelist()) == expected and z.testzip() is None
    print(json.dumps({'folder': str(DEST), 'zip': str(archive), 'files': len(expected)}))


if __name__ == '__main__':
    package()
