# api/v1/api.py
from fastapi import APIRouter
from .endpoints import (
    auth_router,
    chat_router,
    hustles_router,
    jobs_router,
    profile_router,
    reskilling_router,
    risk_router,
)

api_router = APIRouter() # No global dependency here

# Include routers with their respective dependencies applied internally
api_router.include_router(auth_router, prefix="", tags=["auth"]) # Auth routes
api_router.include_router(profile_router, prefix="", tags=["profile"]) # Profile requires API Key
api_router.include_router(risk_router, prefix="", tags=["risk"]) # Risk requires API Key
api_router.include_router(jobs_router, prefix="", tags=["jobs"]) # Jobs requires API Key
api_router.include_router(reskilling_router, prefix="", tags=["reskilling"]) # Reskilling requires API Key
api_router.include_router(hustles_router, prefix="", tags=["hustles"]) # Hustles requires API Key
api_router.include_router(chat_router, prefix="", tags=["chat"]) # Chat requires API Key

# Paths will be:
# /api/v1/signup
# /api/v1/token
# /api/v1/me (Requires JWT)
# /api/v1/profile (Requires API Key)
# /api/v1/risk/{userId} (Requires API Key)
# /api/v1/jobs/{userId} (Requires API Key)
# /api/v1/reskilling/{userId} (Requires API Key)
# /api/v1/hustles/{userId} (Requires API Key)
# /api/v1/chat (Requires API Key and userId in body)