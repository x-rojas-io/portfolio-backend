from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import case_studies

app = FastAPI(
    title="Portfolio API",
    description="API to serve Data Science case studies",
    version="1.0"
)
origins = [
    "http://localhost:3000",
    "https://personal-page-frontend-khaki.vercel.app",
    "https://nestorojas.com",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow your frontend origin
    allow_credentials=True,
    allow_methods=["*"],          # Allow all HTTP methods
    allow_headers=["*"],          # Allow all headers
)
app.include_router(case_studies.router)