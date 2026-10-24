# Frontend TODO

## 구성 파악

- [x] 공개 HTML 입력 목록을 정리합니다: `index.html`, `main.html`, `chapters/`, `labs/`, `appendix/`의 생성 페이지. Vite 설정이 이 경로에서 17개를 자동 검색합니다.
- [x] 각 페이지가 참조하는 CSS, JavaScript, SVG, 이미지, Notebook, Python 예제, JSON 다운로드 파일을 확인합니다. Vite가 HTML·CSS·참조 SVG를 처리하고 패키저가 기존 공개 다운로드 리소스를 그대로 복사합니다.
- [x] 현재 `tools/render_site.py`, `tools/package_site.py`, `assets/js/`의 생성·복사 책임을 확인하고 중복 작업을 표시합니다. Python은 페이지 생성, Vite는 HTML/CSS/이미지 자산 빌드, 패키저는 다운로드·manifest·ZIP을 담당합니다.
- [x] 현행 공개 URL을 기준선으로 확인했습니다. 루트 진입, 장별 페이지, 실험실, 부록의 HTML 경로와 다운로드 경로가 유지됩니다.

## Vite 적용

- [x] Vite와 필요한 플러그인만 개발 의존성으로 추가하고 lockfile을 갱신합니다.
- [x] Python 렌더링을 Vite 빌드 전에 실행하는 명령을 정합니다. 콘텐츠 생성 단계는 필요한 산출물을 Vite가 읽을 수 있도록 유지합니다.
- [x] `vite.config`에 공개 HTML 페이지를 다중 페이지 입력으로 등록하거나, 생성된 페이지를 누락 없이 찾는 재현 가능한 입력 생성 단계를 구현합니다.
- [x] GitHub Pages 프로젝트 경로 `/EDPilot0001/`에 맞춰 `base`를 설정하고, 로컬 미리보기와 Pages 하위 경로에서 자산 링크가 일치하도록 구성합니다.
- [x] 정적 리소스와 다운로드 파일의 복사 규칙을 명시합니다. 불필요한 원본 파일은 산출물에 복사하지 않습니다.
- [x] 출력 경로를 `dist/`로 정하고 빌드 시 이전 산출물을 정리합니다.
- [x] 빌드 전후 페이지별 메타데이터, favicon, stylesheet, script, 내부 링크 동작을 확인합니다. 기존 HTML에는 canonical link 태그가 없어서 추가하지 않았습니다.
- [x] `package.json`의 `build`, `preview` 명령을 추가하거나 기존 명령을 교체하고 README를 갱신합니다.

## 완료 조건

- [x] 로컬 Vite 미리보기에서 모든 페이지와 대표 리소스가 정상 로드됩니다. 브라우저 검증은 17개 페이지를 3개 화면 크기로 확인했습니다.
- [x] HTML 주소가 현행 사용자 경로와 동일합니다.
- [x] 브라우저에 전달되는 번들에 비밀 값이나 배포 전용 자격 증명이 없습니다. Vite 설정에 환경값 주입이나 Define 설정이 없습니다.
