# config.py
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

API_KEY: str = os.getenv("API_KEY", "your-secret-hackathon-key")
API_KEY_NAME: str = "X-API-Key"

# You can add other configuration here later (e.g., database URL)