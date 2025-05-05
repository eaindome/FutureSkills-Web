# api/v1/endpoints/profile.py - Use API Key
from fastapi import APIRouter, HTTPException, status, Depends
from models import UserProfileRequest, UserProfileResponse, ErrorResponse, UserDB # Ensure UserDB is imported if needed elsewhere, though not directly returned
from services import user_service
from dependencies import get_api_key # Use API Key dependency

# Apply API Key dependency to this router
router = APIRouter(dependencies=[Depends(get_api_key)])

@router.post(
    "/profile",
    response_model=UserProfileResponse,
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": ErrorResponse}, 401: {"model": ErrorResponse}} # Add 401 for API key
)
# No user object parameter here, just depends on the API key being present
async def submit_user_profile(profile: UserProfileRequest):
    """
    Stores user input (job title, experience, interests, resume) in a NEW entry.
    Returns a unique user ID for this entry.
    Requires API Key in X-API-Key header.
    """
    if not profile.jobTitle.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="jobTitle cannot be empty"
        )

    # Call service to create a new profile entry
    user_db_data = user_service.create_user_profile(profile)

    # Return the ID of the newly created profile entry
    return UserProfileResponse(userId=user_db_data.id, message="Profile submitted successfully")

#get user profile
@router.get(
    "/profile/{user_id}",
    response_model=UserProfileResponse, # FastAPI expects this model
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorResponse}}
)
async def get_user_profile(user_id: str):
    """
    Retrieves user profile information by user ID.
    Requires API Key in X-API-Key header.
    """
    user_profile: Optional[UserDB] = user_service.get_user(user_id) # Returns UserDB or None
    
    if not user_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User profile not found" 
        )
    
    # *** This is the crucial part ***
    # Construct and return the UserProfileResponse object
    return UserProfileResponse(userId=user_profile, message="User profile retrieved successfully")