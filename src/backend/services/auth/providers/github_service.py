import os
import httpx
from dotenv import load_dotenv, find_dotenv

from services.auth.auth_utils import generate_session_token
from db.redis_session_store import save_session_by_token, save_session_by_ip

load_dotenv(find_dotenv())


def generate_github_auth_url():
    return (
        "https://github.com/login/oauth/authorize"
        f"?client_id={os.getenv('GITHUB_AUTH_CLIENT_ID')}"
        f"&redirect_uri={os.getenv('GITHUB_REDIRECT_PATH')}"
        "&response_type=code"
        "&scope=read:user%20user:email"
        "&state=random_state_string"
    )


async def get_github_auth_data(code, request):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://github.com/login/oauth/access_token",
                data={
                    "code": code,
                    "client_id": os.getenv("GITHUB_AUTH_CLIENT_ID"),
                    "client_secret": os.getenv("GITHUB_AUTH_CLIENT_SECRET"),
                    "redirect_uri": os.getenv("GITHUB_REDIRECT_PATH"),
                },
                headers={
                    "Accept": "application/json"
                }
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