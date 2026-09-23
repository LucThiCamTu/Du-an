import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def summarize_project_progress(tasks_data: list) -> str:
    """Hàm AI tóm tắt tiến độ dự án"""
    if not settings.GEMINI_API_KEY:
        return "Chưa cấu hình GEMINI_API_KEY trong .env"
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = f"Hãy tóm tắt ngắn gọn tiến độ dự án và đưa ra lời khuyên dựa trên danh sách công việc sau: {tasks_data}"
    
    response = model.generate_content(prompt)
    return response.text
