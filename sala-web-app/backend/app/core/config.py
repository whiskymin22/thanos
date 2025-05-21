import os

class Settings:
    PROJECT_NAME: str = "Sala Web App"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:root@db:5432/mydatabase")  # Update with your database details
    UPLOAD_FOLDER: str = os.getenv("UPLOAD_FOLDER", "./uploads")
    ALLOWED_EXTENSIONS: set = {"xlsx", "xls"}

settings = Settings()