# database/database.py
from typing import Dict, Optional
from uuid import UUID
from models import UserDB # Import the UserDB model

# Mock Database (In-Memory Dictionary)
# In a real application, this would connect to PostgreSQL, MongoDB, etc.
fake_db: Dict[UUID, UserDB] = {}

def get_user_from_db(user_id: UUID) -> Optional[UserDB]:
    """Retrieves a user by ID from the mock database."""
    return fake_db.get(user_id)

def create_user_in_db(user_data: UserDB) -> UserDB:
    """Adds a new user to the mock database."""
    fake_db[user_data.id] = user_data
    return user_data

# Add other database interaction functions here as needed