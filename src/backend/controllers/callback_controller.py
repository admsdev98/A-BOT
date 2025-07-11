import os
from services.auth.providers.google_service import get_google_auth_data

async def handle_google_auth_callback(code):
    try:
        auth_data = await get_google_auth_data(code)

        if auth_data.get("error"):
            redirect_url = build_redirect_url(None, auth_data.get("error"))
            return {"success": False, "redirect_url": redirect_url}
        
        redirect_url = build_redirect_url(auth_data.get("token"))
        return {"success": True, "redirect_url": redirect_url}
    except Exception as e:
        redirect_url = build_redirect_url(None, "auth_failed")
        return {"success": False, "redirect_url": redirect_url}

def build_redirect_url(token=None, error=None):
    front_uri = os.getenv("FRONT_URI", "localhost")
    front_host = os.getenv("FRONT_HOST", "8501")
    
    if token:
        return f"http://{front_uri}:{front_host}/?token={token}"
    elif error:
        return f"http://{front_uri}:{front_host}/?error={error}"
    else:
        return f"http://{front_uri}:{front_host}/?error=unknown_error"