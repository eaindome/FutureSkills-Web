# services/chat_service.py
from typing import Optional
from .recommendation_service import mock_get_risk_score # Import needed mock logic

def mock_chat_response(message: str, job_title: str, interests: Optional[str]) -> str:
    """Mocks AI chat responses based on message and user context."""
    message_lower = message.lower()
    job_title_lower = job_title.lower()
    interests_lower = interests.lower() if interests else ""

    default_response = "I'm a demo AI mentor. I can tell you about automation risk, green job ideas, reskilling courses, or side hustles based on your profile."

    if any(keyword in message_lower for keyword in ["next", "future", "path", "transition"]):
        if "cashier" in job_title_lower or "retail" in job_title_lower:
             return f"Considering your {job_title} background and potential interest in green fields, a good next step could be exploring roles like Solar Sales Support or Eco-Retail Coordinator. Look into courses like 'Sustainable Business Practices'."
        elif "teacher" in job_title_lower or "educator" in job_title_lower:
             return f"For an {job_title}, you could transition into environmental education or sustainability training. Courses on climate change education or urban sustainability could be beneficial."
        else:
             return f"Based on your {job_title} role, exploring green jobs in areas like green building or renewable energy project administration could be a good direction. Consider introductory courses in environmental science."

    elif any(keyword in message_lower for keyword in ["green job", "eco job", "sustainable career"]):
        if "cashier" in job_title_lower or "retail" in job_title_lower:
            return "Green jobs like Solar Sales Support Specialist or Eco-Retail Coordinator are good fits for someone with your skills, especially if you have interests in the environment."
        elif "teacher" in job_title_lower or "educator" in job_title_lower:
            return "You could leverage your skills in roles like Environmental Education Program Manager or Sustainability Training Coordinator."
        else:
            return "Many industries need green skills now. Roles in renewable energy, sustainable consulting, or environmental program management are growing."

    elif any(keyword in message_lower for keyword in ["reskilling", "courses", "learn", "train"]):
        if "cashier" in job_title_lower or "retail" in job_title_lower:
            return "Consider online courses such as 'Sustainable Business Practices' (Coursera) or 'Solar Energy Fundamentals' (edX) to build new skills."
        elif "teacher" in job_title_lower or "educator" in job_title_lower:
            return "Courses like 'Climate Change Education' (Coursera) or 'Urban Sustainability' (edX) can enhance your profile for green roles."
        else:
            return "Look into courses related to your specific interests within the green sector, such as circular economy or environmental science basics."

    elif any(keyword in message_lower for keyword in ["side hustle", "extra income", "part-time"]):
         if "cashier" in job_title_lower or "retail" in job_title_lower:
            return "Ideas include selling eco-friendly crafts on Etsy or starting a green-themed blog, especially if you have related interests."
         elif "teacher" in job_title_lower or "educator" in job_title_lower:
            return "You could offer online tutoring in environmental subjects or lead workshops on sustainable living."
         else:
            return "Consider freelance green copywriting or sustainable product affiliate marketing."

    elif any(keyword in message_lower for keyword in ["risk", "automate", "obsolete"]):
         risk, explanation = mock_get_risk_score(job_title) # Use imported mock function
         return f"Based on your role as a {job_title}, the automation risk score is {risk}%. {explanation}"

    return default_response