# api/v1/endpoints/profile.py
from fastapi import APIRouter, HTTPException, status
from models import UserProfileRequest, UserProfileResponse, ErrorResponse
from services import user_service # Import the user service

router = APIRouter()

@router.post(
    "/profile",
    response_model=UserProfileResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": ErrorResponse}}
)
async def submit_user_profile(profile: UserProfileRequest):
    """
    Stores user input (job title, experience, interests, resume).
    Returns a unique user ID.
    """
    if not profile.jobTitle.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="jobTitle cannot be empty"
        )

    user_db_data = user_service.create_user_profile(profile)

    return UserProfileResponse(userId=user_db_data.id, message="Profile submitted successfully")