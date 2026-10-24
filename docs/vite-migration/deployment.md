# Git 배포자 TODO

## 저장소 및 워크플로

- [ ] Pages 공개 소스가 GitHub Actions인지 저장소 설정에서 확인합니다.
- [ ] GitHub Actions가 `npm ci`로 lockfile 기준 의존성을 설치하도록 설정합니다.
- [ ] `main` push에서 Python 콘텐츠 렌더링, Vite 빌드, 수학·링크·브라우저 검증을 순서대로 실행합니다.
- [ ] Pull Request에서는 빌드와 검증만 수행하고 운영 Pages에는 배포하지 않도록 조건을 둡니다.
- [ ] 검증을 통과한 경우에만 `dist/`를 Pages artifact로 업로드하고 배포합니다.
- [ ] `pages: write`, `id-token: write` 등 Pages 배포에 필요한 최소 권한만 부여합니다.
- [ ] 동시 배포 제어와 실패 시 로그·artifact 보존 정책을 설정합니다.
- [ ] `dist/` 밖의 파일을 Pages artifact에 포함하지 않는지 워크플로를 확인합니다.

## 경로·설정

- [ ] 저장소 Settings → Pages의 게시 소스와 `github-pages` environment 승인을 확인합니다.
- [ ] Pages 프로젝트 사이트 경로가 `/EDPilot0001/`이며 Vite `base`와 일치하는지 확인합니다.
- [ ] 환경별 비밀이 필요하지 않은지 검토합니다. 정적 클라이언트 번들에 비밀 값을 넣지 않습니다.
- [ ] README의 배포 링크, 빌드 방법, 미리보기 방법이 실제 workflow와 일치하도록 갱신합니다.

## 출시·복구

- [ ] PR에서 Actions 검증 산출물을 검토하고, 검증 통과 후 `main`에 병합합니다.
- [ ] Pages 배포 job의 성공 상태와 workflow가 출력한 공개 URL을 확인합니다.
- [ ] 공개 URL에서 홈, 하위 페이지, 자산, 다운로드, EduHub 왕복 링크를 확인합니다.
- [ ] 배포 실패 시 이전 정상 커밋을 기준으로 복구하는 절차와 담당자를 문서화합니다.
- [ ] 배포 완료 커밋, Actions 실행 링크, QA 증거 및 알려진 문제를 기록합니다.
