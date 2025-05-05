# api/v1/endpoints/chat.py - Use API Key and userId in body
from fastapi import APIRouter, HTTPException, status, Depends
from models import ChatRequest, ChatResponse, ErrorResponse
from services import user_service, chat_service
from dependencies import get_api_key # Use API Key dependency

# Apply API Key dependency to this router
router = APIRouter(dependencies=[Depends(get_api_key)])

@router.post(
    "/chat", # Path is /chat
    response_model=ChatResponse,
    responses={400: {"model": ErrorResponse}, 404: {"model": ErrorResponse}, 401: {"model": ErrorResponse}} # Add 401 for API key
)
# Accept ChatRequest with userId
async def chat_with_ai_mentor(chat_request: ChatRequest):
    """
    Handles conversational queries with the AI mentor for a user identified by userId.
    Requires API Key in X-API-Key header.
    """
    if not chat_request.message.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="message cannot be empty"
        )

    # Get user data using the provided userId from the request body
    user_data = user_service.get_user(chat_request.userId)
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # We need jobTitle for context, handle if not set
    if not user_data.jobTitle:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User profile incomplete. Job title not found for this user ID to use chat features."
        )


    response_text = chat_service.mock_chat_response(
        chat_request.message.strip(),
        user_data.jobTitle,
        user_data.interests
    )

    return ChatResponse(response=response_text)