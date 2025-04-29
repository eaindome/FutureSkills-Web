# api/v1/endpoints/hustles.py
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from uuid import UUID
from models import SideHustle, ErrorResponse
from services import user_service, recommendation_service
from dependencies import get_api_key

router = APIRouter(dependencies=[Depends(get_api_key)])

@router.get(
    "/hustles/{userId}",
    response_model=List[SideHustle],
    responses={404: {"model": ErrorResponse}}
)
async def get_side_hustle_ideas(userId: UUID):
    """
    Returns side hustle suggestions based on user profile.
    Returns up to 2 recommendations.
    Requires API Key in X-API-Key header.
    """
    user_data = user_service.get_user(userId)
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    hustles = recommendation_service.mock_get_side_hustles(user_data.jobTitle, user_data.interests)

    return hustles