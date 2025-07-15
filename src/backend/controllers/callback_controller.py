from services.auth.providers.google_service import get_google_auth_data
from services.auth.providers.github_service import get_github_auth_data
from services.cookie.cookie_service import set_cookie_and_redirect, validate_if_user_token_is_alive
from db.redis_session_store import save_session_token

async def get_google_auth_response(code):
    try:
        auth_data = await get_google_auth_data(code)

        save_session_token(str(auth_data.get("session_id")), str(auth_data.get("token")))
        return set_cookie_and_redirect(auth_data)
    except Exception:
        return set_cookie_and_redirect(None)

async def get_github_auth_response(code):
    try:
        auth_data = await get_github_auth_data(code)
        save_session_token(str(auth_data.get("session_id")), str(auth_data.get("token")))
        return set_cookie_and_redirect(auth_data)
    except Exception:
        return set_cookie_and_redirect(None)

def process_auth_validate_session_request(cookie_session):
    return validate_if_user_token_is_alive(cookie_session)




