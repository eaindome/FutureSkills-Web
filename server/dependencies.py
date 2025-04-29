# dependencies.py
from fastapi import Header, HTTPException, status, Depends
from config import API_KEY, API_KEY_NAME

def get_api_key(api_key_header: str = Header(None, name=API_KEY_NAME)):
    """Dependency to check for the API key in the header."""
    # For hackathon demo, allow if header is missing, but check if present
    if api_key_header is None:
         print(f"Warning: {API_KEY_NAME} header missing. Access allowed for demo.")
         return None # Or return a default permission level

    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
            # Optionally add headers for browser support:
            # headers={"WWW-Authenticate": "Bearer"},
        )