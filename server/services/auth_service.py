# services/auth_service.py
from datetime import datetime, timedelta, timezone
from typing import Optional
from uuid import UUID

from jose import JWTError, jwt
from fastapi import HTTPException, status

from models import UserCreate, UserDB, TokenData
from database import get_user_by_email_from_db, create_user_in_db
from services.auth_utils import hash_password, verify_password
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def create_user(user_data: UserCreate) -> UserDB:
    """Creates a new user with a hashed password."""
    existing_user = get_user_by_email_from_db(user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = hash_password(user_data.password)

    user_db_data = UserDB(
        email=user_data.email,
        hashed_password=hashed_password,
        full_name=user_data.full_name,
        # jobTitle, experience, interests, resumeText are optional and can be added later via /profile
        jobTitle=None, experience=None, interests=None, resumeText=None
    )
    return create_user_in_db(user_db_data)

def authenticate_user(email: str, password: str) -> Optional[UserDB]:
    """Authenticates a user by email and password."""
    user = get_user_by_email_from_db(email)
    if not user:
        return None # User not found

    if not verify_password(password, user.hashed_password):
        return None # Password does not match

    return user # Authentication successful

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Creates a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> TokenData:
    """Verifies a JWT token and returns the payload."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extract data from the payload, e.g., user ID or email
        user_id: str = payload.get("sub") # Standard claim for subject (often used for user ID)
        if user_id is None:
            raise JWTError("Invalid payload")

        # Optionally, validate the token payload further (e.g., check expiry is handled by jwt.decode)
        token_data = TokenData(id=UUID(user_id)) # Assuming user ID (UUID) is stored in 'sub' claim
        return token_data
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            # headers={"WWW-Authenticate": "Bearer"}, # Add headers for browser support
        )