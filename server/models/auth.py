# models/auth.py
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

# Model for user creation (POST /signup)
class UserCreate(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    full_name: Optional[str] = None

# Model for user login (used internally by OAuth2PasswordRequestForm)
# No need for a specific Pydantic model here if using OAuth2PasswordRequestForm

# Model for JWT token response (POST /login)
class Token(BaseModel):
    access_token: str
    token_type: str # Typically "bearer"

# Model for data stored inside the JWT token
class TokenData(BaseModel):
    id: Optional[UUID] = None # User ID stored in token
    email: Optional[EmailStr] = None # Or email, depending on what you store