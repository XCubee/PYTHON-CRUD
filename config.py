import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Use SQLite by default for easier setup
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///crud_app.db')
    
    # PostgreSQL configuration (if you want to use it later)
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '8080')
    DB_NAME = os.getenv('DB_NAME', 'crud_db')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
    
    @classmethod
    def get_database_url(cls):
        if cls.DATABASE_URL != 'sqlite:///crud_app.db':
            return cls.DATABASE_URL
        return cls.DATABASE_URL 