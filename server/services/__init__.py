# services/__init__.py
from .user_service import create_user_profile, get_user
from .recommendation_service import mock_get_risk_score, mock_get_green_jobs, mock_get_reskilling_courses, mock_get_side_hustles
from .chat_service import mock_chat_response