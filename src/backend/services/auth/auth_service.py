import os

from fastapi.responses import RedirectResponse
from interfaces.auth import AuthRequest

from services.auth.providers.linkedin_service import generate_linkedin_token
from services.auth.providers.github_service import generate_github_auth_url
from services.auth.providers.google_service import generate_google_auth_url


def generate_auth_response(auth_method: AuthRequest):
    method = auth_method.auth_method

    if method == "linkedin":
        return generate_linkedin_token()
    elif method == "github":
        return generate_github_auth_url()
    elif method == "google":
        return generate_google_auth_url()

def generate_auth_redirect_uri(auth_data):
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