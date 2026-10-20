#!/usr/bin/env python3
"""Exercise the deployment bundle under a GitHub Pages project prefix."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import hashlib
import json
import os
import threading
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'output/site'
PREFIX = '/EDPilot0001/'


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if not self.path.startswith(PREFIX):
            self.send_error(404)
            return
        self.path = '/' + self.path[len(PREFIX) :]
        super().do_GET()

    def log_message(self, *args):
        pass


server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Handler, directory=str(SITE)))
threading.Thread(target=server.serve_forever, daemon=True).start()
BASE = os.environ.get('EDPILOT_TEST_URL', f'http://127.0.0.1:{server.server_port}{PREFIX}')
errors = []
failures = []
pages = [str(p.relative_to(SITE)) for p in SITE.rglob('*.html')]
assert len(pages) == 17
checks = 0
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for width in [1440, 390, 320]:
            context = browser.new_context(viewport={'width': width, 'height': 900})
            page = context.new_page()
            page.on('pageerror', lambda e: errors.append(str(e)))
            page.on('response', lambda r: failures.append(r.url) if r.status >= 400 else None)
            for path in pages:
                page.goto(BASE + path)
                expect(page.locator('h1')).to_have_count(1)
                assert page.locator('html').get_attribute('lang') == 'ko'
                assert page.locator('[data-language], .language-switch').count() == 0
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'), (
                    width,
                    path,
                )
                expect(page.locator('.hq-link')).to_have_attribute(
                    'href', 'https://hyangdan2.github.io/'
                )
                if path.startswith('labs/'):
                    expect(page.locator('#mode')).to_contain_text('실시간')
                    assert page.locator('#primary-plot svg').count() == 1
                    assert page.locator('#secondary-plot svg').count() == 1
                    assert 'NaN' not in page.locator('#metrics').inner_text()
                    before = page.locator('#metrics').inner_text()
                    slider = page.locator('input[type=range]').first
                    slider.focus()
                    page.keyboard.press('End')
                    expect(page.locator('#metrics')).not_to_have_text(before, use_inner_text=True)
                    page.get_by_role('button', name='기본 설정으로 초기화').click()
                    expect(page.locator('#metrics')).to_have_text(before, use_inner_text=True)
                checks += 1
            page.goto(BASE + 'main.html')
            initial = page.locator('html').get_attribute('data-theme')
            page.locator('[data-theme-toggle]').click()
            changed = page.locator('html').get_attribute('data-theme')
            assert changed != initial
            page.reload()
            expect(page.locator('html')).to_have_attribute('data-theme', changed)
            if width in [1440, 390]:
                page.screenshot(path=str(ROOT / 'output' / f'preview-{width}.png'), full_page=True)
            context.close()
        context = browser.new_context(java_script_enabled=False)
        page = context.new_page()
        page.goto(BASE + 'chapters/01-data-and-models.html')
        expect(page.locator('h1')).to_have_count(1)
        assert page.locator('.advanced-figure').count() == 4
        for name, digest in json.loads((SITE / 'manifest.json').read_text())[
            'files_sha256'
        ].items():
            response = context.request.get(BASE + name)
            assert response.status == 200, name
            assert hashlib.sha256(response.body()).hexdigest() == digest, name
        browser.close()
finally:
    server.shutdown()
assert not errors and not failures, (errors, failures)
report = {
    'status': 'passed',
    'page_viewports': checks,
    'languages': ['ko'],
    'widths': [1440, 390, 320],
    'labs': 5,
    'theme_persistence': True,
    'javascript_disabled': True,
    'manifest_http_hashes': True,
    'url': BASE,
}
(ROOT / 'output/browser-check.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report))
