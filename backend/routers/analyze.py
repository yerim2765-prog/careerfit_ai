# backend/routers/analyze.py
from services.llm_service import get_llm_response

from fastapi import APIRouter

from pydantic import BaseModel

from typing import List

router = APIRouter()

# 요청 본문(Request Body) 모델

# 손님이 제출하는 주문서 양식

class AnalyzeRequest(BaseModel):

    major: str

    skills: List[str]

    job_type: str

    experience_years: int = 0

    preferred_company_size: str = "무관"

# 응답 본문(Response Body) 모델

# 주방에서 손님에게 돌려주는 영수증 양식

class AnalyzeResponse(BaseModel):

    answer: str         # AI 분석 결과 텍스트

    sources: List[dict]     # 답변 근거 데이터 목록



@router.post("/analyze", response_model=AnalyzeResponse, tags=["Analyze"])

def analyze_career(request: AnalyzeRequest):

    """

    사용자의 전공·스킬·관심 직무를 기반으로 취업·공모전 맞춤 분석을 제공한다.

    현재는 목업 응답을 반환하며, 실습 8에서 Gemini API와 연결한다.

    """

    # 임시 목업 응답: 실습 8에서 실제 Gemini + RAG 응답으로 교체한다

    query = f"""
전공: {request.major}
보유 스킬: {", ".join(request.skills)}
관심 직무: {request.job_type}
경력: {request.experience_years}년
희망 기업 규모: {request.preferred_company_size}
"""

    result = get_llm_response(
        query=query,
        context_docs=[]
    )

    return AnalyzeResponse(
        answer=result["answer"],
        sources=result["sources"]
    )