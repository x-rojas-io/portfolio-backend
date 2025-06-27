from fastapi import APIRouter, HTTPException
from app.models.case_study import CaseStudy
import json

router = APIRouter()
with open("app/data/case_study_index.json") as f:
    CASE_STUDIES = [CaseStudy(**item) for item in json.load(f)]

@router.get("/case-studies", response_model=list[CaseStudy])
def get_all_studies():
    return CASE_STUDIES

@router.get("/case-studies/{slug}", response_model=CaseStudy)
def get_case_study(slug: str):
    for cs in CASE_STUDIES:
        if cs.slug == slug:
            return cs
    raise HTTPException(status_code=404, detail="Case study not found")

@router.get("/case-studies/search/")
def search_case_studies(q: str):
    results = [cs for cs in CASE_STUDIES if q.lower() in cs.title.lower()]
    return results