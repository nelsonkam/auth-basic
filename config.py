import os
from dotenv import load_dotenv
load_dotenv()

APP_ENV = os.getenv("DATABASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

URL = DATABASE_URL.split("//")[1]
DB_USER = URL.split("@")[0].split(":")[0]
DB_PASSWORD = URL.split("@")[0].split(":")[1]
DB_HOST = URL.split("@")[1].split("/")[0].split(":")[0]
DB_NAME = URL.split("@")[1].split("/")[1]

DATABASES = {
    'postgres': {
        'driver': 'postgres',
        'host': DB_HOST,
        'database': DB_NAME,
        'user': DB_USER,
        'password': DB_PASSWORD,
        'prefix': '',
        'log_queries': APP_ENV == "dev"
    }
}

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
DO_SPACES_KEY = os.getenv("DO_SPACES_KEY")
DO_SPACES_SECRET = os.getenv("DO_SPACES_SECRET")
DO_SPACES_BUCKET = os.getenv("DO_SPACES_BUCKET")
DO_SPACES_REGION = os.getenv("DO_SPACES_REGION")
DO_SPACES_ENDPOINT_URL = os.getenv("DO_SPACES_ENDPOINT_URL")