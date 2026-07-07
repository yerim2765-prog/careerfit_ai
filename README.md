# CareerFit AI

> 취업·공모전 데이터 기반 맞춤형 AI 포트폴리오 코치

---

## 📌 프로젝트 개요

취업 준비생은 수많은 채용 공고 속에서 자신의 역량에 맞는 직무를 찾고, 어떤 기술을 준비해야 하는지 파악하기 어렵습니다.

CareerFit AI는 취업 공고 데이터를 기반으로 사용자의 전공, 보유 기술, 희망 직무를 분석하고 RAG(Retrieval-Augmented Generation)를 활용하여 근거 기반의 맞춤형 역량 분석 결과를 제공합니다.

---

## 🛠 기술 스택

| 영역 | 기술 |
|---|---|
| 백엔드 | Python 3.11, FastAPI |
| AI API | Gemini 2.5 Flash-Lite |
| 데이터 | Pandas, SQLite, ChromaDB |
| 프론트엔드 | React, Vite |
| 실행 환경 | Docker |

---

## 🏗 아키텍처

```text
사용자 입력
      ↓
React UI
      ↓
FastAPI (/analyze)
      ↓
ChromaDB (RAG 검색)
      ↓
Gemini API
      ↓
분석 결과 + Sources 반환
```

---

## 🚀 실행 방법

### Docker로 실행 (권장)

```bash
# 1. 이미지 빌드
docker build -t careerfit-ai ./backend

# 2. 컨테이너 실행
docker run -p 8000:8000 --env-file backend/.env careerfit-ai
```

API 문서

```
http://localhost:8000/docs
```

### 로컬 실행

```bash
cd backend

# Python 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt

# FastAPI 실행
uvicorn main:app --reload --port 8000
```

---

## 📊 데이터 파이프라인

```text
CSV
 ↓
Pandas 전처리
 ↓
SQLite (구조화 데이터 저장)
 ↓
ChromaDB (벡터 검색)
 ↓
Gemini RAG 분석
```

전처리 실행

```bash
python data/preprocess.py
```

---

## ✨ 주요 기능

- RAG 기반 역량 분석: 취업 공고 데이터를 기반으로 맞춤형 분석 제공
- 출처(Sources) 제공: 분석에 활용된 공고 정보를 함께 반환
- Mock Mode 지원: Gemini API 호출 없이 테스트 가능
- Docker 지원: 컨테이너 기반으로 동일한 실행 환경 제공

---

## 📁 프로젝트 구조

```text
careerfit-ai/
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── data/
│   └── Dockerfile
├── frontend/
└── docs/
```

---

## ✅ 검증

- Docker 환경에서 FastAPI 서버 정상 실행 확인
- `/health` 엔드포인트 정상 응답 확인
- `/analyze` API 호출 및 응답 확인
- Render를 통한 웹 서비스 배포 완료

---

## 🔮 향후 개선

- [ ] 이력서 PDF 업로드 및 자동 역량 분석
- [ ] 실시간 채용 공고 데이터 연동
- [ ] RAG 검색 품질 평가(Ragas 등) 적용

---

## 📝 개발 과정

Docker를 이용해 FastAPI 애플리케이션을 컨테이너 환경에서 실행하는 과정과 Gemini API 환경변수를 설정하는 과정에서 어려움을 겪었습니다. Dockerfile과 환경변수를 수정하고 테스트를 반복하여 Docker 환경에서 서비스를 정상적으로 실행할 수 있었습니다.

---

## Demo

**Live Demo**

https://careerfit-ai-9yjr.onrender.com

**API Docs**

https://careerfit-ai-9yjr.onrender.com/docs

---

## 👨‍💻 Developer

**Name**

Yerim

**Role**

Backend / AI Service Development

**GitHub**

https://github.com/yerim2765-prog

**Email**

yerim2765@gmail.com
