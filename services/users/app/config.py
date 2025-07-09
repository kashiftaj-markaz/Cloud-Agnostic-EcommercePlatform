import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

DB_USER = os.getenv("DB_USER", "serviceusers")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Usersservice")
DB_HOST = os.getenv("DB_HOST", "mysql")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "users_db")

# Construct the database URL
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def get_database_url():
    return SQLALCHEMY_DATABASE_URL
