from services.auth.providers.google_service import get_google_auth_data
from services.auth.providers.github_service import get_github_auth_data
from services.auth.auth_service import generate_auth_redirect_uri
from services.auth.auth_utils import validate_if_user_token_is_alive, validate_if_user_token_is_alive_by_ip

async def get_google_auth_response(code, request):
    try:
        auth_data = await get_google_auth_data(code, request)        
        return generate_auth_redirect_uri(auth_data)
    except Exception:
        return generate_auth_redirect_uri(None)

async def get_github_auth_response(code, request):
    try:
        auth_data = await get_github_auth_data(code, request)
        return generate_auth_redirect_uri(auth_data)
    except Exception:
        return generate_auth_redirect_uri(None)

def process_auth_validate_session_request(cookie_session):
    return validate_if_user_token_is_alive(cookie_session)

def process_auth_validate_session_ip_request(request):
    return validate_if_user_token_is_alive_by_ip(request.client.host)


