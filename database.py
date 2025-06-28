from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from config import Config
from models import Base
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.engine = None
        self.SessionLocal = None
        
    def connect(self):
        """Create database connection"""
        try:
            database_url = Config.get_database_url()
            self.engine = create_engine(database_url, echo=True)
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            logger.info("Database connection established successfully")
            return True
        except SQLAlchemyError as e:
            logger.error(f"Database connection failed: {e}")
            return False
    
    def create_tables(self):
        """Create all tables"""
        try:
            Base.metadata.create_all(bind=self.engine)
            logger.info("Tables created successfully")
            return True
        except SQLAlchemyError as e:
            logger.error(f"Table creation failed: {e}")
            return False
    
    def get_session(self):
        """Get database session"""
        if not self.SessionLocal:
            raise Exception("Database not connected. Call connect() first.")
        return self.SessionLocal()
    
    def close(self):
        """Close database connection"""
        if self.engine:
            self.engine.dispose()
            logger.info("Database connection closed")

# Global database instance
db = Database() 