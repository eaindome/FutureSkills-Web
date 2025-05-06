# api/v1/endpoints/risk.py - Use API Key and userId
from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID
from models import AutomationRiskResponse, ErrorResponse
from services import user_service, recommendation_service
from dependencies import get_api_key # Use API Key dependency

# Apply API Key dependency to this router
router = APIRouter(dependencies=[Depends(get_api_key)])

@router.get(
    "/risk/{userId}", # userId path parameter is back
    response_model=AutomationRiskResponse,
    responses={404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}} # Add 401 for API key
)
# Accept userId path parameter
async def get_automation_risk(userId: UUID): # userId is back here
    """
    Calculates the automation risk score for a user's job identified by userId.
    Requires API Key in X-API-Key header.
    """
    # Get user data using the provided userId
    user_data = user_service.get_user(userId)
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Check if jobTitle exists for this profile entry
    if not user_data.jobTitle:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User profile incomplete. Job title not found for this user ID."
        )

    risk_score, explanation = recommendation_service.mock_get_risk_score(user_data.jobTitle)

    return AutomationRiskResponse(
        userId=user_data.id,
        jobTitle=user_data.jobTitle,
        riskScore=risk_score,
        explanation=explanation
    )