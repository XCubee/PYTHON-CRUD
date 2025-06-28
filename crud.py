from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import User
import logging

logger = logging.getLogger(__name__)

class UserCRUD:
    def __init__(self, db_session: Session):
        self.db = db_session
    
    def create_user(self, name: str, email: str, phone: str = None, address: str = None):
        """Create a new user"""
        try:
            user = User(
                name=name,
                email=email,
                phone=phone,
                address=address
            )
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            logger.info(f"User created successfully: {user.id}")
            return user
        except IntegrityError as e:
            self.db.rollback()
            logger.error(f"User creation failed - duplicate email: {e}")
            raise ValueError("Email already exists")
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"User creation failed: {e}")
            raise Exception("Failed to create user")
    
    def get_user_by_id(self, user_id: int):
        """Get user by ID"""
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if user:
                logger.info(f"User retrieved: {user.id}")
                return user
            else:
                logger.warning(f"User not found: {user_id}")
                return None
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving user: {e}")
            raise Exception("Failed to retrieve user")
    
    def get_user_by_email(self, email: str):
        """Get user by email"""
        try:
            user = self.db.query(User).filter(User.email == email).first()
            if user:
                logger.info(f"User retrieved by email: {email}")
                return user
            else:
                logger.warning(f"User not found with email: {email}")
                return None
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving user by email: {e}")
            raise Exception("Failed to retrieve user")
    
    def get_all_users(self, skip: int = 0, limit: int = 100):
        """Get all users with pagination"""
        try:
            users = self.db.query(User).offset(skip).limit(limit).all()
            logger.info(f"Retrieved {len(users)} users")
            return users
        except SQLAlchemyError as e:
            logger.error(f"Error retrieving users: {e}")
            raise Exception("Failed to retrieve users")
    
    def update_user(self, user_id: int, name: str = None, email: str = None, 
                   phone: str = None, address: str = None):
        """Update user information"""
        try:
            user = self.get_user_by_id(user_id)
            if not user:
                raise ValueError("User not found")
            
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            if phone is not None:
                user.phone = phone
            if address is not None:
                user.address = address
            
            self.db.commit()
            self.db.refresh(user)
            logger.info(f"User updated successfully: {user_id}")
            return user
        except IntegrityError as e:
            self.db.rollback()
            logger.error(f"User update failed - duplicate email: {e}")
            raise ValueError("Email already exists")
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"User update failed: {e}")
            raise Exception("Failed to update user")
    
    def delete_user(self, user_id: int):
        """Delete a user"""
        try:
            user = self.get_user_by_id(user_id)
            if not user:
                raise ValueError("User not found")
            
            self.db.delete(user)
            self.db.commit()
            logger.info(f"User deleted successfully: {user_id}")
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            logger.error(f"User deletion failed: {e}")
            raise Exception("Failed to delete user")
    
    def search_users(self, search_term: str):
        """Search users by name or email"""
        try:
            users = self.db.query(User).filter(
                (User.name.ilike(f"%{search_term}%")) |
                (User.email.ilike(f"%{search_term}%"))
            ).all()
            logger.info(f"Found {len(users)} users matching '{search_term}'")
            return users
        except SQLAlchemyError as e:
            logger.error(f"Error searching users: {e}")
            raise Exception("Failed to search users") 