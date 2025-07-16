from services.auth.providers.google_service import get_google_auth_data
from services.auth.providers.github_service import get_github_auth_data
from services.auth.providers.linkedin_service import get_linkedin_auth_data
from services.auth.auth_service import generate_auth_redirect_uri
from services.auth.auth_utils import validate_if_user_token_is_alive, validate_user_remaining_attempts, reduce_chat_attempts

async def get_google_auth_response(code):
    try:
        auth_data = await get_google_auth_data(code)        
        return generate_auth_redirect_uri(auth_data)
    except Exception:
        return generate_auth_redirect_uri(None)

async def get_github_auth_response(code):
    try:
        auth_data = await get_github_auth_data(code)
        return generate_auth_redirect_uri(auth_data)
    except Exception:
        return generate_auth_redirect_uri(None)

async def get_linkedin_auth_response(code):
    try:
        auth_data = await get_linkedin_auth_data(code)
        return generate_auth_redirect_uri(auth_data)
    except Exception:
        return generate_auth_redirect_uri(None)

def process_auth_validate_session_request(cookie_session):
    return validate_if_user_token_is_alive(cookie_session)

def process_auth_validate_remaining_attempts_request(cookie_session):
    return validate_user_remaining_attempts(cookie_session)

def process_reduce_chat_attempts_request(cookie_session):
    return reduce_chat_attempts(cookie_session)