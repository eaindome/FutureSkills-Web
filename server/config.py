# config.py
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# API Key (Kept for the original endpoints)
API_KEY: str = os.getenv("API_KEY", "your-secret-hackathon-key")
API_KEY_NAME: str = "X-API-Key"

# JWT Settings (For signup, login, me)
SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "another-super-secret-random-key-replace-me") # *** IMPORTANT: CHANGE THIS ***
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))