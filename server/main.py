# main.py
from fastapi import FastAPI
import uvicorn
from api.v1.api import api_router # Import the main API router
from config import API_KEY # Optional: just to show it's loaded

app = FastAPI(
    title="Green Careers API (Hackathon Mock)",
    description="API for user profiles and green career recommendations with mock AI.",
    version="1.0.0",
    # Add OpenAPI specific configurations if needed
)

# Include the main API router, potentially with a prefix like /api/v1
app.include_router(api_router, prefix="/api/v1")

# Optional: Add a root endpoint for health check or info
@app.get("/")
async def read_root():
    return {"message": "Green Careers API is running!", "version": app.version}

# Running the App
if __name__ == "__main__":
    print(f"Using API Key: {API_KEY}") # Print the loaded API key for verification
    # To run: uvicorn main:app --reload
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)