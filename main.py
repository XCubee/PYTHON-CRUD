#!/usr/bin/env python3
"""
Basic CRUD Application with PostgreSQL
A command-line interface to manage user records
"""

import sys
import json
from database import db
from crud import UserCRUD
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def print_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("           USER MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Create a new user")
    print("2. View all users")
    print("3. View user by ID")
    print("4. View user by email")
    print("5. Update user")
    print("6. Delete user")
    print("7. Search users")
    print("8. Exit")
    print("="*50)

def get_user_input():
    """Get user input for creating/updating users"""
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone (optional): ").strip() or None
    address = input("Enter address (optional): ").strip() or None
    return name, email, phone, address

def create_user(crud):
    """Create a new user"""
    print("\n--- CREATE NEW USER ---")
    try:
        name, email, phone, address = get_user_input()
        user = crud.create_user(name, email, phone, address)
        print(f"✅ User created successfully!")
        print(f"ID: {user.id}")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

def view_all_users(crud):
    """View all users"""
    print("\n--- ALL USERS ---")
    try:
        users = crud.get_all_users()
        if not users:
            print("No users found.")
            return
        
        for user in users:
            print(f"\nID: {user.id}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print(f"Phone: {user.phone or 'N/A'}")
            print(f"Address: {user.address or 'N/A'}")
            print(f"Created: {user.created_at}")
            print("-" * 30)
    except Exception as e:
        print(f"❌ Error: {e}")

def view_user_by_id(crud):
    """View user by ID"""
    print("\n--- VIEW USER BY ID ---")
    try:
        user_id = int(input("Enter user ID: "))
        user = crud.get_user_by_id(user_id)
        if user:
            print(f"\nID: {user.id}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print(f"Phone: {user.phone or 'N/A'}")
            print(f"Address: {user.address or 'N/A'}")
            print(f"Created: {user.created_at}")
            print(f"Updated: {user.updated_at}")
        else:
            print("❌ User not found.")
    except ValueError:
        print("❌ Please enter a valid ID number.")
    except Exception as e:
        print(f"❌ Error: {e}")

def view_user_by_email(crud):
    """View user by email"""
    print("\n--- VIEW USER BY EMAIL ---")
    try:
        email = input("Enter email: ").strip()
        user = crud.get_user_by_email(email)
        if user:
            print(f"\nID: {user.id}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print(f"Phone: {user.phone or 'N/A'}")
            print(f"Address: {user.address or 'N/A'}")
            print(f"Created: {user.created_at}")
            print(f"Updated: {user.updated_at}")
        else:
            print("❌ User not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

def update_user(crud):
    """Update user information"""
    print("\n--- UPDATE USER ---")
    try:
        user_id = int(input("Enter user ID to update: "))
        user = crud.get_user_by_id(user_id)
        if not user:
            print("❌ User not found.")
            return
        
        print(f"\nCurrent user information:")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        print(f"Phone: {user.phone or 'N/A'}")
        print(f"Address: {user.address or 'N/A'}")
        
        print(f"\nEnter new information (press Enter to keep current value):")
        name = input(f"Name ({user.name}): ").strip() or user.name
        email = input(f"Email ({user.email}): ").strip() or user.email
        phone = input(f"Phone ({user.phone or 'N/A'}): ").strip() or user.phone
        address = input(f"Address ({user.address or 'N/A'}): ").strip() or user.address
        
        updated_user = crud.update_user(user_id, name, email, phone, address)
        print("✅ User updated successfully!")
        print(f"Updated Name: {updated_user.name}")
        print(f"Updated Email: {updated_user.email}")
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

def delete_user(crud):
    """Delete a user"""
    print("\n--- DELETE USER ---")
    try:
        user_id = int(input("Enter user ID to delete: "))
        user = crud.get_user_by_id(user_id)
        if not user:
            print("❌ User not found.")
            return
        
        print(f"\nUser to delete:")
        print(f"ID: {user.id}")
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")
        
        confirm = input("\nAre you sure you want to delete this user? (yes/no): ").strip().lower()
        if confirm == 'yes':
            crud.delete_user(user_id)
            print("✅ User deleted successfully!")
        else:
            print("❌ Deletion cancelled.")
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

def search_users(crud):
    """Search users"""
    print("\n--- SEARCH USERS ---")
    try:
        search_term = input("Enter search term (name or email): ").strip()
        if not search_term:
            print("❌ Please enter a search term.")
            return
        
        users = crud.search_users(search_term)
        if not users:
            print(f"No users found matching '{search_term}'.")
            return
        
        print(f"\nFound {len(users)} user(s) matching '{search_term}':")
        for user in users:
            print(f"\nID: {user.id}")
            print(f"Name: {user.name}")
            print(f"Email: {user.email}")
            print(f"Phone: {user.phone or 'N/A'}")
            print("-" * 30)
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Main application function"""
    print("🚀 Starting User Management System...")
    
    # Connect to database
    if not db.connect():
        print("❌ Failed to connect to database. Please check your configuration.")
        sys.exit(1)
    
    # Create tables
    if not db.create_tables():
        print("❌ Failed to create tables.")
        sys.exit(1)
    
    print("✅ Database connected and tables created successfully!")
    
    # Create CRUD instance
    session = db.get_session()
    crud = UserCRUD(session)
    
    try:
        while True:
            print_menu()
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                create_user(crud)
            elif choice == '2':
                view_all_users(crud)
            elif choice == '3':
                view_user_by_id(crud)
            elif choice == '4':
                view_user_by_email(crud)
            elif choice == '5':
                update_user(crud)
            elif choice == '6':
                delete_user(crud)
            elif choice == '7':
                search_users(crud)
            elif choice == '8':
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 8.")
            
            input("\nPress Enter to continue...")
    
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    finally:
        session.close()
        db.close()

if __name__ == "__main__":
    main() 