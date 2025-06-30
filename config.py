import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Use PostgreSQL by default
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:saksham@localhost:8080/list')
    
    # PostgreSQL configuration (if you want to use it later)
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '8080')
    DB_NAME = os.getenv('DB_NAME', 'list')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'saksham')
    
    @classmethod
    def get_database_url(cls):
        return cls.DATABASE_URL 