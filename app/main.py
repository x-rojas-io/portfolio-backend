from fastapi import FastAPI
from app.routes import case_studies

app = FastAPI(
    title="Portfolio API",
    description="API to serve Data Science case studies",
    version="1.0"
)

app.include_router(case_studies.router)