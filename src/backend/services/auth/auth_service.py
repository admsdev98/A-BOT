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