# api/v1/endpoints/risk.py
from fastapi import APIRouter, HTTPException, status, Depends
from uuid import UUID
from models import AutomationRiskResponse, ErrorResponse
from services import user_service, recommendation_service # Import services
from dependencies import get_api_key # Import dependency

router = APIRouter(dependencies=[Depends(get_api_key)]) # Apply API key dependency to all routes in this router

@router.get(
    "/risk/{userId}",
    response_model=AutomationRiskResponse,
    responses={404: {"model": ErrorResponse}}
)
async def get_automation_risk(userId: UUID):
    """
    Calculates the automation risk score for a user's job.
    Requires API Key in X-API-Key header (applied at router level).
    """
    user_data = user_service.get_user(userId)
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    risk_score, explanation = recommendation_service.mock_get_risk_score(user_data.jobTitle)

    return AutomationRiskResponse(
        userId=user_data.id,
        jobTitle=user_data.jobTitle,
        riskScore=risk_score,
        explanation=explanation
    )