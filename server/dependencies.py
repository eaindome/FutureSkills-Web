# dependencies.py
from fastapi import Header, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError # Import JWTError
from typing import Optional # Import Optional

from models import UserDB, TokenData, ErrorResponse
from database import get_user_from_db # get_user_from_db gets user by ID
from database import get_user_by_email_from_db # Need this for get_current_user as well
from services.auth_service import verify_token # Import verify_token function # Note: auth_service imports this, consider moving verify_token *into* dependencies? Let's keep it in auth_service for now.
from config import API_KEY, API_KEY_NAME

# Define the OAuth2 scheme for Bearer tokens (for JWT)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")

# Dependency to check API Key (For original endpoints)
def get_api_key(api_key_header: str = Header(None, name=API_KEY_NAME)):
    """Dependency to check for the API key in the header."""
    if api_key_header is None or api_key_header != API_KEY:
         raise HTTPException(
             status_code=status.HTTP_401_UNAUTHORIZED,
             detail="API Key header missing or invalid",
             headers={"WWW-Authenticate": f"Header name=\"{API_KEY_NAME}\""},
         )
    return api_key_header

# Dependency to get the current authenticated user from the JWT token (For /me)
def get_current_user(token: str = Depends(oauth2_scheme)) -> UserDB:
    """
    Dependency to get the current authenticated user from the JWT token.
    Requires 'Authorization: Bearer <token>' header.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_data: TokenData = verify_token(token) # Use verify_token from auth_service

        if token_data.id is None:
             raise credentials_exception

        # Fetch the user from the database using the ID from the token
        # This assumes users created via signup ARE stored in fake_db keyed by ID
        user = get_user_from_db(token_data.id)

        if user is None:
            raise credentials_exception # User not found in DB (maybe deleted?)

        # Ensure user object has enough data to be useful (e.g., not just an ID placeholder)
        # If the user was only created via /signup, they might only have auth data
        # If the user was only created via /profile, they won't have auth data but will have profile data
        # The UserDB model must handle optional fields correctly.

        return user # Return the full UserDB object

    except JWTError:
        raise credentials_exception # Token is malformed or invalid signature
    except Exception:
         # Catch any other unexpected errors
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail="Internal server error during authentication"
         )