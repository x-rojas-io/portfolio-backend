from fastapi import APIRouter, HTTPException
from app.models.case_study import CaseStudy
from datetime import datetime
import json
from fastapi import HTTPException
from typing import List

router = APIRouter()
with open("app/data/case_study_index.json") as f:
    CASE_STUDIES = [CaseStudy(**item) for item in json.load(f)]

@router.get("/case-studies", response_model=list[CaseStudy])
def get_all_studies():
    try:
        sorted_studies = sorted(
            CASE_STUDIES,
            key=lambda cs: datetime.strptime(cs.date, "%Y-%m-%d"),
            reverse=True
        )
        return sorted_studies
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Sorting error: {str(e)}")

@router.get("/case-studies/search", response_model=list[CaseStudy])
def search_case_studies(q: str):
    query_tokens = q.lower().split()
    results = []

    for cs in CASE_STUDIES:
        title = cs.title.lower()
        summary = cs.summary.lower()

        # Match if ANY token appears in title or summary
        if any(token in title or token in summary for token in query_tokens):
            results.append(cs)

    return results

@router.get("/case-studies/{id}", response_model=CaseStudy)
def get_case_study(id: str):
    for cs in CASE_STUDIES:
        if cs.id == id:
            return cs
    raise HTTPException(status_code=404, detail="Case study not found")

@router.get("/case-studies/topic/{tag}", response_model=List[CaseStudy])
def get_case_studies_by_topic(tag: str):
    matches = [cs for cs in CASE_STUDIES if tag.lower() in [t.lower() for t in cs.tags]]
    if not matches:
        raise HTTPException(status_code=404, detail="No case studies found for this topic")
    return matches

@router.get("/case-studies/find/latest", response_model=CaseStudy)
def get_latest_case_study():
    if not CASE_STUDIES:
        raise HTTPException(status_code=404, detail="No case studies available")

    try:
        latest = max(
            CASE_STUDIES,
            key=lambda cs: datetime.strptime(cs.date, "%Y-%m-%d")
        )
        return latest
    except ValueError:
        raise HTTPException(status_code=500, detail="Date parsing error")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")