# services/user_service.py - UPDATED create_user_profile
from typing import Optional
from uuid import UUID
from models import UserProfileRequest, UserDB
from database import get_user_from_db, create_user_in_db, update_user_in_db

def create_user_profile(profile_data: UserProfileRequest) -> UserDB:
    """Creates a new user profile entry in the database."""
    # This creates a NEW user entry, separate from any auth users
    user_db_data = UserDB(
        id=profile_data.id,
        jobTitle=profile_data.jobTitle.strip(),
        experience=profile_data.experience.strip() if profile_data.experience else None,
        interests=profile_data.interests.strip() if profile_data.interests else None,
        resumeText=profile_data.resumeText.strip() if profile_data.resumeText else None,
        # email, hashed_password, full_name will be None
    )
    return update_user_in_db(user_db_data.id, user_db_data)

def get_user(user_id: str) -> Optional[UserDB]:
    """Retrieves a user profile by ID."""

    return get_user_from_db(user_id)