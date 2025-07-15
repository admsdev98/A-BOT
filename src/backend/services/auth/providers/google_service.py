import os
import httpx
from dotenv import load_dotenv, find_dotenv

from services.auth.auth_utils import generate_session_token
from db.redis_session_store import save_session_by_token, save_session_by_ip

load_dotenv(find_dotenv())


def generate_google_auth_url():
    return (
        "https://accounts.google.com/o/oauth2/v2/auth"
        f"?client_id={os.getenv('GOOGLE_AUTH_CLIENT_ID')}"
        f"&redirect_uri={os.getenv('GOOGLE_REDIRECT_PATH')}"
        "&response_type=code"
        "&scope=openid%20email%20profile"
        "&access_type=offline"
    )


async def get_google_auth_data(code, request):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                str(os.getenv("GOOGLE_TOKEN_URL")),
                data={
                    "code": code,
                    "client_id": os.getenv("GOOGLE_AUTH_CLIENT_ID"),
                    "client_secret": os.getenv("GOOGLE_AUTH_CLIENT_SECRET"),
                    "redirect_uri": os.getenv("GOOGLE_REDIRECT_PATH"),
                    "grant_type": "authorization_code",
                },
            )
            auth_data = response.json()
            
            if auth_data.get("error"):
                return {"error": "No se pudo completar el login. Por favor, intenta de nuevo."}
            
            user_session_data = generate_session_token(auth_data)

            save_session_by_token(str(user_session_data.get("session_id")), str(user_session_data.get("token")))
            save_session_by_ip(request.client.host, str(user_session_data.get("token")))

            return user_session_data
            
    except Exception as e:
        return {"error": "No se pudo completar el login. Por favor, intenta de nuevo."}