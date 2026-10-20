# EDPilot0001 — 머신러닝 공부

한국어로 읽고 브라우저에서 실험하는 독립 정적 교육 사이트입니다.
7개 장, 5개 실험실, 3개 부록과 진입 페이지로 총 17개 HTML 페이지를 제공합니다.
21개 심화 사례, 28개 비교 그림, Python 예제와 실행 결과를 포함한 Notebook이 있습니다.
모든 실험 데이터는 합성이며 방문자에게 서버 API나 외부 라이브러리가 필요하지 않습니다.

- [학습 사이트](https://hyangdan2.github.io/EDPilot0001/)
- [Web-HQ](https://hyangdan2.github.io/)
- [교육자료 작성 Harness Guide](https://github.com/HyangDan2/hyangdan2.github.io/blob/main/docs/education-harness-guide.md)
- [교육과정 구성](docs/curriculum-map.md)

## 개발 및 검증

Python 3.12 이상과 Node.js 22를 권장합니다.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt -r requirements-format.txt
npm ci
python -m playwright install chromium
npm run build
npm test
npm run test:browser
python tests/advanced_verify.py --notebook
```

`npm run build`는 한국어 원본에서 페이지와 기본 예제를 생성하고
`output/site/` 및 `output/edpilot0001-static.zip`을 만듭니다.
수치 실험 원본을 변경했다면 빌드 전에 `python tools/enrich_site.py`를 실행하세요.
HTML 생성은 번역 데이터나 Web-HQ 파일을 읽지 않습니다.

```sh
python -m http.server 8000 --directory output/site
```

`http://localhost:8000/`에서 결과물을 확인할 수 있습니다.
수정할 원본은 `tools/content*.py`, `tools/render_site.py`, `assets/js/`, `downloads/`입니다.
생성된 HTML과 기본 예제를 직접 고치지 마세요.

## 배포

`main`에 push하면 GitHub Actions가 빌드, 수학 검증, 링크 검사 및 브라우저 검증을
통과한 `output/site/`만 GitHub Pages에 게시합니다. 수동 실행도 가능합니다.
저장소 Settings → Pages의 배포 소스는 GitHub Actions입니다.
작성 도구, 테스트, 내부 문서는 공개 사이트 산출물에서 제외합니다.

기존 MLStudy를 한국어 전용으로 분리한 프로젝트입니다. 테마 전환, 인쇄,
반응형 레이아웃과 브라우저 계산 기능을 유지합니다. 언어 선택이나 번역 생성 과정은 없습니다.
