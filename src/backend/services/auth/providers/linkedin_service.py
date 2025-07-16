import os
import httpx
import secrets
from urllib.parse import urlencode
from dotenv import load_dotenv, find_dotenv

from services.auth.auth_utils import generate_session_token

load_dotenv(find_dotenv())


def generate_state():
    return secrets.token_urlsafe(16)


def generate_linkedin_auth_url():
    base_url = "https://www.linkedin.com/oauth/v2/authorization"
    state = generate_state()
    params = {
        "response_type": "code",
        "client_id": os.getenv("LINKEDIN_CLIENT_ID"),
        "redirect_uri": os.getenv("LINKEDIN_REDIRECT_URI"),
        "state": state,
        "scope": "openid profile email",
    }
    url = f"{base_url}?{urlencode(params)}"
    return url


async def get_linkedin_auth_data(code):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://www.linkedin.com/oauth/v2/accessToken",
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": os.getenv("LINKEDIN_REDIRECT_URI"),
                    "client_id": os.getenv("LINKEDIN_CLIENT_ID"),
                    "client_secret": os.getenv("LINKEDIN_CLIENT_SECRET"),
                },
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            response.raise_for_status()
            auth_data = response.json()

            if "error" in auth_data:
                return {"error": "No se pudo completar el login con LinkedIn. Por favor, intenta de nuevo."}

            return generate_session_token(auth_data)
    except Exception:
        return {"error": "No se pudo completar el login con LinkedIn. Por favor, intenta de nuevo."}
