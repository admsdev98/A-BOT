from interfaces.auth import AuthRequest

from services.auth.providers.linkedin_service import generate_linkedin_token
from services.auth.providers.captcha_service import generate_captcha_token
from services.auth.providers.google_service import generate_google_token

def generate_auth_response(auth_method: AuthRequest):
    method = auth_method.auth_method
    if method == "linkedin":
        return generate_linkedin_token()
    elif method == "captcha":
        return generate_captcha_token()
    elif method == "google":
        return generate_google_token()