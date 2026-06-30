# backend/routers/jobs.py

from fastapi import APIRouter

from typing import List

router = APIRouter()



# 목업 데이터: 3일차에 실제 CSV 데이터로 교체한다

MOCK_JOBS = [

    {
    "id": 1,
    "company": "네이버",
    "title": "데이터 분석가",
    "required_skills": ["Python", "SQL", "Pandas"],
    "preferred_skills": ["Tableau", "통계", "데이터 시각화"],
    "description": "서비스 이용 데이터를 분석하여 사용자 행동을 파악하고 비즈니스 의사결정을 지원합니다. 다양한 부서와 협업하며 데이터 기반 인사이트를 제공합니다.",
    "deadline": "2026-08-31"
},
{
    "id": 2,
    "company": "삼성SDS",
    "title": "BI 데이터 분석가",
    "required_skills": ["SQL", "Python", "Power BI"],
    "preferred_skills": ["Excel", "통계", "ETL"],
    "description": "기업 데이터를 분석하여 경영 현황을 시각화하고 보고서를 작성합니다. 데이터 품질을 관리하며 의사결정에 필요한 분석 결과를 제공합니다.",
    "deadline": "2026-08-31"
},
{
    "id": 3,
    "company": "한국환경공단",
    "title": "환경 데이터 분석가",
    "required_skills": ["Python", "SQL", "통계"],
    "preferred_skills": ["R", "GIS", "데이터 시각화"],
    "description": "환경 및 기후 데이터를 수집·분석하여 정책 수립을 지원합니다. 분석 결과를 시각화하고 보고서를 작성하여 다양한 이해관계자에게 제공합니다.",
    "deadline": "2026-08-31"
}

]



@router.get("/jobs", tags=["Jobs"])

def get_jobs():

    """

    취업 공고 목록을 반환하는 엔드포인트.

    현재는 목업 데이터를 반환하며, 3일차에 실제 데이터로 교체한다.

    """

    return {

        "count": len(MOCK_JOBS),

        "jobs": MOCK_JOBS

    }



@router.get("/jobs/{job_id}", tags=["Jobs"])

def get_job_by_id(job_id: int):

    """

    특정 공고의 상세 정보를 반환한다.

    """

    for job in MOCK_JOBS:

        if job["id"] == job_id:

            return job

    # 찾지 못한 경우

    from fastapi import HTTPException

    raise HTTPException(status_code=404, detail=f"공고 ID {job_id}를 찾을 수 없습니다.")