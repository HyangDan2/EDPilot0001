# 교육과정 구성

한국어 단일 사이트로, 진입 페이지와 메인 목차, 7개 장, 5개 실험실,
3개 부록을 합쳐 총 17개 HTML 페이지입니다.

| 순서 | 학습 주제 | 연결 실험실 |
| --- | --- | --- |
| 1 | 데이터에서 학습으로: 생성 과정, 평가와 데이터 누출 | — |
| 2 | 예측의 수학: 선형 회귀, 기저, 정규화 | 회귀 곡선 |
| 3 | 모델 개선: 최적화와 경사하강 | 경사하강 경로 |
| 4 | 불확실성: 확률, 추론과 의사결정 | — |
| 5 | 정보 압축: PCA와 SVD | PCA 압축 |
| 6 | 숨은 집단: GMM과 EM | GMM 군집 |
| 7 | 분류 경계: SVM, 마진과 최적성 | SVM 분류 경계 |

각 장은 기초 설명 6개, 심화 사례 3개와 비교 그림 4개로 구성됩니다.
전체 심화 사례는 21개, SVG 비교 그림은 28개입니다.
부록은 수학, 용어·기호, 참고자료·제작 및 재현 정보입니다.

기본 Python 예제와 Notebook, 심화 계산 Python과 실행 출력이 저장된
Notebook을 다운로드할 수 있습니다. 모든 데이터는 합성 데이터입니다.

`python3 tools/render_site.py`는 한국어 원본에서 HTML과 기본 예제를 생성합니다.
`python3 tools/enrich_site.py`는 심화 결과, 그림과 Notebook을 갱신합니다.
전체 작성·검증·배포 절차는 Web-HQ의
[교육자료 작성 Harness Guide](https://github.com/HyangDan2/hyangdan2.github.io/blob/main/docs/education-harness-guide.md)를 따릅니다.
