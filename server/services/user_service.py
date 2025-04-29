# services/user_service.py
from typing import Optional
from uuid import UUID
from models import UserProfileRequest, UserDB
from database import get_user_from_db, create_user_in_db # Import DB functions

def create_user_profile(profile_data: UserProfileRequest) -> UserDB:
    """Creates a new user profile in the database."""
    # In a real app, AI parsing of resumeText might happen here
    user_db_data = UserDB(
        jobTitle=profile_data.jobTitle.strip(),
        experience=profile_data.experience.strip() if profile_data.experience else None,
        interests=profile_data.interests.strip() if profile_data.interests else None,
        resumeText=profile_data.resumeText.strip() if profile_data.resumeText else None
    )
    return create_user_in_db(user_db_data)

def get_user(user_id: UUID) -> Optional[UserDB]:
    """Retrieves a user profile by ID."""
    return get_user_from_db(user_id)