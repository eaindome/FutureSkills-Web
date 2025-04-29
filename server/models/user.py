# models/user.py
import uuid
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

# Model for storing user data internally (mock DB)
class UserDB(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    jobTitle: str
    experience: Optional[str] = None
    interests: Optional[str] = None
    resumeText: Optional[str] = None
    # Add createdAt timestamp here in a real DB model

# Model for API Request (POST /profile)
class UserProfileRequest(BaseModel):
    jobTitle: str = Field(..., min_length=1, description="User's current job title")
    experience: Optional[str] = Field(None, description="User's work experience range")
    interests: Optional[str] = Field(None, description="Comma-separated user interests")
    resumeText: Optional[str] = Field(None, description="User's pasted resume text")

# Model for API Response (POST /profile)
class UserProfileResponse(BaseModel):
    userId: UUID
    message: str

# Model for Error Responses
class ErrorResponse(BaseModel):
    error: str