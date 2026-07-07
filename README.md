# careerfit\_ai

취업/공모전 데이터 기반 Ai 포트폴리오 코치
# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치



## 프로젝트 개요



[내 직무 및 전공 관련해서 어떤 취업 공고가 있는지 잘 모르겠다.]



## 기술 스택



| 영역 | 기술 |

|---|---|

| 백엔드 | Python, FastAPI |

| AI API | Gemini 2.5 Flash-Lite |

| 데이터 | Pandas, SQLite, ChromaDB |

| 프론트엔드 | React, Vite |

| 실행 환경 | Docker |

## 진행 현황
## 📌 진행 현황 (2일차)

- FastAPI 기반 `/health`, `/jobs`, `/analyze` API 엔드포인트를 구현했습니다.
- Python 가상환경 및 백엔드 개발 환경을 구축하고 필수 패키지를 설치했습니다.
- Gemini 2.5 Flash-Lite API를 연동할 수 있는 기본 구조를 구성했습니다.
- `.env`를 활용하여 API Key를 관리하고 `MOCK_MODE` 환경변수를 설정했습니다.
- Swagger(`/docs`)에서 각 API의 동작을 확인하며 백엔드 서버를 테스트했습니다.

## 📌 진행 현황 (3일차)

취업 공고 CSV 데이터를 분석하고 전처리 파이프라인을 구현했습니다.
- CSV 데이터 불러오기
- UTF-8 / CP949 인코딩 자동 처리
- 결측치(빈값) 확인
- 핵심 컬럼(title, required_skills) 결측 데이터 제거
- 나머지 텍스트 컬럼 결측치 빈 문자열로 처리
- company + title 기준 중복 데이터 제거

### 내가 추가할 관심 직무 분야

- 관심 직무 1: 데이터 분석가
- 관심 직무 2: 머신러닝 엔지니어

### 내가 추가할 공모전 분야

- AI·데이터 분석 공모전

### 강조하고 싶은 스킬 키워드

- Python
- SQL
- Pandas
- 머신러닝
- 데이터 시각화

## 📌 진행 현황 (4일차)
```bash
git add .
git commit -m "feat: RAG 기반 /analyze API 및 React UI 구현

- ChromaDB 문서 검색 (rag_service.py)
- Gemini RAG 연결 답변 생성 (llm_service.py)
- React + Vite 프로젝트 생성
- InputForm, ResultCard, SourceCard 컴포넌트
- fetch로 /analyze API 연결
- design-skill.md 작성"
git push
```markdown
## 프론트엔드 실행 방법

```bash
cd frontend
npm install
npm run dev
```

프론트엔드: http://localhost:5173
백엔드 API: http://localhost:8000/docs
-주요기능
 전공·보유 스킬·관심 직무 입력 폼
 React + Vite 기반 UI 구현
 FastAPI /analyze API 호출
 AI 분석 결과(ResultCard) 출력
 출처 공고(SourceCard) 출력
 Tailwind CSS 기반 UI 구성


- [x] 1일차: 프로젝트 기획 및 개발 환경 세팅

- [x] 2일차: FastAPI 서버 구축 및 Gemini API 연결

- [x] 3일차: 데이터 파이프라인 구축

- [x] 4일차: RAG 기반 서비스 + React UI

- [ ] 5일차: Docker + 포트폴리오 완성

