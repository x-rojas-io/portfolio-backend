# 🔌 AI/ML Case Study Portfolio — Backend (FastAPI)

This is the backend service for the AI/ML & Data Science Portfolio site. It serves structured metadata about real-world case studies, handles topic/category filtering, search, and dynamic retrieval of GitHub-hosted markdown content.

> ⚙️ Built with **FastAPI**, served from a structured JSON file — no database required (yet).

---

## 📦 Features

- ✅ Serve all case studies as structured JSON
- 🔍 Full-text search on titles and summaries
- 🏷️ Filter by topic/category (`Fintech`, `Economics`, etc.)
- 📌 Fetch latest published case study
- 🧩 Designed for frontend Markdown rendering (via GitHub raw URLs)
- ⚡ Fast and lightweight — deploys easily to Render or Fly.io

---

## 🗂️ Folder Structure
personal_page-backend/
├── app/
│   ├── data/
│   │   └── case_study_index.json    # JSON file with all studies
│   ├── models/
│   │   └── case_study.py            # Pydantic model
│   └── routes/
│       └── case_study_routes.py     # All route definitions
├── main.py                          # FastAPI app entrypoint
├── requirements.txt
├── README.md
└── .gitignore