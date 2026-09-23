from fastapi import FastAPI
from app.services.ai_service import summarize_project_progress

app = FastAPI(title="Project Management AI API")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Hệ thống Quản lý Dự án Nhóm tích hợp AI đang hoạt động!"}

@app.post("/api/v1/ai/summarize")
def ai_summarize(tasks: list):
    summary = summarize_project_progress(tasks)
    return {"summary": summary}
