# main.py
from fastapi import FastAPI
import uvicorn
from api.v1.api import api_router
from config import API_KEY, SECRET_KEY # Import keys to print (optional)

app = FastAPI(
    title="Green Careers API (Hackathon Mock)",
    description="API for user profiles and green career recommendations with mock AI.",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def read_root():
    return {"message": "Green Careers API is running!", "version": app.version}

if __name__ == "__main__":
    print(f"Using API Key: {API_KEY}")
    print(f"Using JWT SECRET KEY (first 8 chars): {SECRET_KEY[:8]}...")
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)