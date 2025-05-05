# api/v1/endpoints/auth.py - Use JWT only for /me
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models import UserCreate, UserProfileResponse, Token, ErrorResponse, UserDB # Import UserDB for /me response
from services import auth_service
from database import get_user_from_db # Needed to fetch user for /me after verify_token
from dependencies import get_current_user # Import the JWT dependency
from datetime import timedelta
from config import ACCESS_TOKEN_EXPIRE_MINUTES

# No global dependency on this router
router = APIRouter(tags=["auth"])

@router.post(
    "/signup",
    response_model=UserProfileResponse, # Returning userId and message
    status_code=status.HTTP_201_CREATED,
    responses={400: {"model": ErrorResponse}}
)
async def signup(user_create: UserCreate):
    """
    Registers a new user with email, password, and full name.
    Creates a NEW user entry in the database (separate from profile entries).
    Returns the user ID (of the auth entry).
    """
    try:
        user_db_data = auth_service.create_user(user_create) # Creates UserDB with auth fields
        # Return response similar to profile submission, but for the auth user ID
        return UserProfileResponse(userId=user_db_data.id, message="User created successfully")
    except HTTPException as e:
        raise e
    except Exception as e:
         raise HTTPException(
             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
             detail=f"An error occurred during signup: {e}"
         )


@router.post(
    "/token",
    response_model=Token,
    responses={401: {"model": ErrorResponse}}
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Handles user login with email and password (form data) and returns a JWT access token.
    """
    user = auth_service.authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Store user ID (sub claim) and email in the token
    access_token = auth_service.create_access_token(
        data={"sub": str(user.id), "email": user.email},
        expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")

@router.get("/me", response_model=UserDB, responses={401: {"model": ErrorResponse}})
async def read_users_me(current_user: UserDB = Depends(get_current_user)):
    """
    Get details of the current authenticated user (from JWT token).
    Requires 'Authorization: Bearer <token>' header.
    """
    # current_user is provided by the dependency
    return current_user