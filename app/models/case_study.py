from pydantic import BaseModel
from typing import List

class CaseStudy(BaseModel):
    id: str
    slug: str
    title: str
    summary: str
    tags: List[str]
    github_url: str
    readme_url: str
    date: str