import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

APP_ENV = os.getenv("DATABASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

result = urlparse(DATABASE_URL)

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": result.hostname,
        "database": result.path[1:],
        "user": result.username,
        "password": result.password,
        "port": result.port,
        "prefix": "",
        "log_queries": APP_ENV == "dev",
    }
}

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
DO_SPACES_KEY = os.getenv("DO_SPACES_KEY")
DO_SPACES_SECRET = os.getenv("DO_SPACES_SECRET")
DO_SPACES_BUCKET = os.getenv("DO_SPACES_BUCKET")
DO_SPACES_REGION = os.getenv("DO_SPACES_REGION")
DO_SPACES_ENDPOINT_URL = os.getenv("DO_SPACES_ENDPOINT_URL")