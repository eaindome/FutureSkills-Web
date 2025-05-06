# models/recommendation.py
from pydantic import BaseModel, Field
from uuid import UUID

# Model for API Response (GET /risk/{userId})
class AutomationRiskResponse(BaseModel):
    userId: UUID
    jobTitle: str
    riskScore: int = Field(..., ge=0, le=100)
    explanation: str

# Model for API Response (GET /jobs/{userId})
class GreenJob(BaseModel):
    title: str
    growthRate: int
    skillMatch: str
    description: str
    salary: str

# Model for API Response (GET /reskilling/{userId})
class ReskillingCourse(BaseModel):
    title: str
    provider: str
    duration: str
    skills: str
    link: str

# Model for API Response (GET /hustles/{userId})
class SideHustle(BaseModel):
    title: str
    description: str
    skills: str
    earnings: str