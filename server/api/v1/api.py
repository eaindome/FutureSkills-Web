# api/v1/api.py
from fastapi import APIRouter
from .endpoints import (
    chat_router,
    hustles_router,
    jobs_router,
    profile_router,
    reskilling_router,
    risk_router,
)

api_router = APIRouter()

# Include individual endpoint routers
api_router.include_router(profile_router, tags=["profile"])
api_router.include_router(risk_router, tags=["risk"])
api_router.include_router(jobs_router, tags=["jobs"])
api_router.include_router(reskilling_router, tags=["reskilling"])
api_router.include_router(hustles_router, tags=["hustles"])
api_router.include_router(chat_router, tags=["chat"])

# Add more routers here as you add functionality