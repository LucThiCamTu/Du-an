import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Project Management AI"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg://app_user:secret@localhost:5432/project_db")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "super_secret_key")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

settings = Settings()
