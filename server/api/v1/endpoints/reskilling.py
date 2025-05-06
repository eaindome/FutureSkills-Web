# api/v1/endpoints/reskilling.py
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from uuid import UUID
from models import ReskillingCourse, ErrorResponse
from services import user_service, recommendation_service
from dependencies import get_api_key

router = APIRouter(dependencies=[Depends(get_api_key)])

@router.get(
    "/reskilling/{userId}",
    response_model=List[ReskillingCourse],
    responses={404: {"model": ErrorResponse}}
)
async def get_reskilling_recommendations(userId: UUID):
    """
    Returns reskilling course suggestions based on user profile.
    Returns up to 2 recommendations.
    Requires API Key in X-API-Key header.
    """
    user_data = user_service.get_user(userId)
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    courses = recommendation_service.mock_get_reskilling_courses(user_data.jobTitle, user_data.interests)

    return courses