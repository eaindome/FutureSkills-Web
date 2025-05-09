# models/__init__.py
from .user import UserDB, UserProfileRequest, UserProfileResponse, ErrorResponse
from .recommendation import AutomationRiskResponse, GreenJob, ReskillingCourse, SideHustle
from .chat import ChatRequest, ChatResponse # Import updated ChatRequest
from .auth import UserCreate, Token, TokenData