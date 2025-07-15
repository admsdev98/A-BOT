import os
from fastapi.responses import RedirectResponse
from db.redis_session_store import get_session_token


def validate_if_user_token_is_alive(cookie_session):
    return {"exists": get_session_token(cookie_session) is not None}

def set_cookie_and_redirect(auth_data):
    front_uri = os.getenv("FRONT_URI", "localhost")
    front_host = os.getenv("FRONT_HOST", "8501")

    if auth_data.get("session_id"):
        redirect_path = f"http://{front_uri}:{front_host}/?token={auth_data.get('session_id')}"
    elif auth_data.get("error"):
        redirect_path = f"http://{front_uri}:{front_host}/?error=true"
    else:
        redirect_path = f"http://{front_uri}:{front_host}/?error=something_went_wrong"

    print(f"Redirecting to: {redirect_path}")
    return RedirectResponse(url=redirect_path)