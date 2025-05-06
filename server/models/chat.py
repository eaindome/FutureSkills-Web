# models/chat.py - Revert ChatRequest to include userId
from pydantic import BaseModel, Field
from uuid import UUID # userId is back in the request body

# Model for API Request (POST /chat) - REVERTED
class ChatRequest(BaseModel):
    userId: UUID # Back in the request body
    message: str = Field(..., min_length=1, description="User's chat message")

# Model for API Response (POST /chat)
class ChatResponse(BaseModel):
    response: str