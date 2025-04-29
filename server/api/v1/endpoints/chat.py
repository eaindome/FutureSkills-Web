# api/v1/endpoints/chat.py
from fastapi import APIRouter, HTTPException, status
from models import ChatRequest, ChatResponse, ErrorResponse
from services import user_service, chat_service # Import services

router = APIRouter()

@router.post(
    "/chat",
    response_model=ChatResponse,
    responses={400: {"model": ErrorResponse}, 404: {"model": ErrorResponse}}
)
async def chat_with_ai_mentor(chat_request: ChatRequest):
    """
    Handles conversational queries with the AI mentor.
    """
    if not chat_request.message.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="message cannot be empty"
        )

    user_data = user_service.get_user(chat_request.userId)
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    response_text = chat_service.mock_chat_response(
        chat_request.message.strip(),
        user_data.jobTitle,
        user_data.interests
    )

    return ChatResponse(response=response_text)