# database/database.py
from typing import Dict, Optional
from uuid import UUID
from models import UserDB # Import the UserDB model

# Mock Database (In-Memory Dictionary) - UPDATED
# Key is now user ID (UUID)
fake_db: Dict[UUID, UserDB] = {}

# Added an index for quick lookup by email
fake_users_by_email: Dict[str, UserDB] = {}


def get_user_from_db(user_id: str) -> Optional[UserDB]:
    """Retrieves a user by ID from the mock database."""
    try:
        # Convert string to UUID and use .get() for safe access
        user_uuid = UUID(user_id)
        return fake_db.get(user_uuid)
    except ValueError:
        # Handle cases where user_id is not a valid UUID string
        return None
    

def get_user_by_email_from_db(email: str) -> Optional[UserDB]:
    """Retrieves a user by email from the mock database index."""
    return fake_users_by_email.get(email.lower()) # Store/lookup lowercase email

def create_user_in_db(user_data: UserDB) -> UserDB:
    """Adds a new user to the mock database and updates index."""
    fake_db[user_data.id] = user_data
    fake_users_by_email[user_data.email.lower()] = user_data # Add to email index
    return user_data

def update_user_in_db(user_id: UUID, user_data: UserDB) -> Optional[UserDB]:
    """Updates an existing user in the mock database and index."""
    if user_id in fake_db:
        # Ensure the ID in user_data matches the user_id being updated
        # (or handle potential mismatches if necessary)
        user_data.id = user_id 
        
        # Update the main database entry
        fake_db[user_id] = user_data

        return user_data
    return None

# Add other database interaction functions here as needed