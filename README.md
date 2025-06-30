# Basic CRUD Application with Python and PostgreSQL

A simple command-line CRUD (Create, Read, Update, Delete) application built with Python and PostgreSQL using SQLAlchemy ORM.

## Features

- ✅ Create new users with name, email, phone, and address
- ✅ Read/View all users or specific users by ID/email
- ✅ Update existing user information
- ✅ Delete users with confirmation
- ✅ Search users by name or email
- ✅ PostgreSQL database integration
- ✅ SQLAlchemy ORM for database operations
- ✅ Error handling and logging
- ✅ User-friendly command-line interface

## Prerequisites

Before running this application, make sure you have:

1. **Python 3.7+** installed on your system
2. **PostgreSQL** database server installed and running
3. **pip** (Python package installer)

## Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd CRUD
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL database**
   - Create a new database named `crud_db` (or any name you prefer)
   - Note down your database credentials (username, password, host, port)

4. **Configure database connection**
   - Copy `env_example.txt` to `.env`
   - Update the `.env` file with your actual database credentials:
   ```env
   DATABASE_URL=postgresql://your_username:your_password@localhost:5432/crud_db
   ```
   
   Or use individual parameters:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=crud_db
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```

## Usage

Run the application:
```bash
python main.py
```

The application will:
1. Connect to your PostgreSQL database
2. Create the necessary tables automatically
3. Display a menu with all available operations

### Available Operations

1. **Create a new user** - Add a new user with name, email, phone, and address
2. **View all users** - Display all users in the database
3. **View user by ID** - Find and display a specific user by their ID
4. **View user by email** - Find and display a specific user by their email
5. **Update user** - Modify existing user information
6. **Delete user** - Remove a user from the database (with confirmation)
7. **Search users** - Search for users by name or email
8. **Exit** - Close the application

## Project Structure

```
CRUD/
├── main.py              # Main application file with CLI interface
├── crud.py              # CRUD operations implementation
├── models.py            # SQLAlchemy models (User table)
├── database.py          # Database connection and session management
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── env_example.txt      # Example environment configuration
└── README.md           # This file
```

## Database Schema

The application creates a `users` table with the following structure:

| Column     | Type      | Description                    |
|------------|-----------|--------------------------------|
| id         | INTEGER   | Primary key, auto-increment    |
| name       | VARCHAR   | User's full name (required)    |
| email      | VARCHAR   | User's email (unique, required)|
| phone      | VARCHAR   | User's phone number (optional) |
| address    | TEXT      | User's address (optional)      |
| created_at | TIMESTAMP | Record creation timestamp      |
| updated_at | TIMESTAMP | Record last update timestamp   |

## Error Handling

The application includes comprehensive error handling for:
- Database connection failures
- Duplicate email addresses
- Invalid user IDs
- Missing required fields
- Database operation failures

## Logging

The application logs all operations to help with debugging:
- Database connections
- CRUD operations
- Errors and exceptions
- User actions

## Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Verify PostgreSQL is running
   - Check your database credentials in `.env`
   - Ensure the database exists

2. **Module Not Found Errors**
   - Run `pip install -r requirements.txt`
   - Make sure you're in the correct directory

3. **Permission Denied**
   - Check PostgreSQL user permissions
   - Verify database user has CREATE, SELECT, UPDATE, DELETE privileges

### Getting Help

If you encounter issues:
1. Check the error messages in the console
2. Verify your database configuration
3. Ensure all dependencies are installed
4. Check that PostgreSQL is running and accessible

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

