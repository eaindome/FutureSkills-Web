# models/chat.py
from pydantic import BaseModel, Field
from uuid import UUID

# Model for API Request (POST /chat)
class ChatRequest(BaseModel):
    userId: UUID
    message: str = Field(..., min_length=1, description="User's chat message")

# Model for API Response (POST /chat)
class ChatResponse(BaseModel):
    response: str