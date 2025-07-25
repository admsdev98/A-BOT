import os

from fastapi.responses import RedirectResponse, Response
from interfaces.auth import AuthRequest

from services.auth.providers.linkedin_service import generate_linkedin_auth_url
from services.auth.providers.github_service import generate_github_auth_url
from services.auth.providers.google_service import generate_google_auth_url


def generate_auth_response(auth_method: AuthRequest):
    method = auth_method.auth_method

    if method == "linkedin":
        return generate_linkedin_auth_url()
    elif method == "github":
        return generate_github_auth_url()
    elif method == "google":
        return generate_google_auth_url()


def generate_auth_redirect_uri(auth_data):
    front_uri = os.getenv("FRONT_URI", "localhost")
    front_host = os.getenv("FRONT_HOST", "")  # vacío si puerto 443

    if front_host and front_host != "443":
        base_url = f"https://{front_uri}:{front_host}"
    else:
        base_url = f"https://{front_uri}"

    if auth_data.get("token"):
        redirect_path = f"{base_url}/?logged=true"
    elif auth_data.get("error"):
        redirect_path = f"{base_url}/?error=true"
    else:
        redirect_path = f"{base_url}/?error=something_went_wrong"

    response = RedirectResponse(url=redirect_path)

    if auth_data.get("token"):
        response.set_cookie(
            key="session_id",
            value=auth_data.get("token"),
            httponly=True,
            secure=True,
            max_age=3600,
            path="/"
        )
    return response