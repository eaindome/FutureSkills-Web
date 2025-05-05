# models/user.py
import uuid
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr


# Model for storing user data internally (mock DB) - UPDATED
class UserDB(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    email: Optional[EmailStr] = Field(None) # Made optional
    hashed_password: Optional[str] = Field(None) # Made optional
    full_name: Optional[str] = Field(None) # Made optional
    jobTitle: Optional[str] = Field(None) # Remains optional
    experience: Optional[str] = Field(None) # Remains optional
    interests: Optional[str] = Field(None) # Remains optional
    resumeText: Optional[str] = Field(None) # Remains optional

class UserProfileRequest(BaseModel):
    id: Optional[UUID] = Field(None, description="User ID")
    jobTitle: Optional[str] = Field(None, min_length=1, description="User's current job title")
    experience: Optional[str] = Field(None, description="User's work experience range")
    interests: Optional[str] = Field(None, description="Comma-separated user interests")
    resumeText: Optional[str] = Field(None, description="User's pasted resume text")

class UserProfileResponse(BaseModel):
    userId: UUID
    message: str

class ErrorResponse(BaseModel):
    error: str