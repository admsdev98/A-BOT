import os
import uuid
import jwt
import datetime
from dotenv import load_dotenv, find_dotenv

from db.redis_session_store import get_session_token, get_session_attempts, save_session_by_token, initialize_session_attempts, update_session_attempts

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("SUPER_KEY")



def generate_session_token(auth_data):
    session_id = str(uuid.uuid4())
    user_token = auth_data.get("access_token")

    jwt_token = encode_session_token(session_id, user_token)

    save_session_by_token(session_id, jwt_token)
    initialize_session_attempts(session_id)

    return { "token": jwt_token }

def validate_if_user_token_is_alive(jwt_token: str) -> dict:
    try:
        payload = decode_session_token(jwt_token)
        session_id = payload.get("session_id")

        if not session_id:
            return {"exists": False}

        stored_token = get_session_token(session_id)
        if stored_token is None:
            return {"exists": False}

        if stored_token != jwt_token:
            return {"exists": False}

        return {"exists": True}

    except jwt.ExpiredSignatureError:
        return {"exists": False}
    except jwt.InvalidTokenError:
        return {"exists": False}


def validate_user_remaining_attempts(cookie_session: str):
    payload = decode_session_token(cookie_session)
    session_id = payload.get("session_id")

    if not session_id:
        return {"attempts": False}

    attempts = get_session_attempts(session_id)

    if attempts == 0 or attempts is None:
        return {"attempts": False}
    return {"attempts": True}

def reduce_chat_attempts(cookie_session):
    payload = decode_session_token(cookie_session)
    session_id = payload.get("session_id")

    if not session_id:
        return {"attempts": False}

    session_attempts = get_session_attempts(session_id)

    if session_attempts is not None:
        new_session_attempts = max(0, session_attempts - 1)
        update_session_attempts(session_id, new_session_attempts)

def encode_session_token(session_id, user_token):
    payload = {
        "session_id": session_id,
        "user_token": user_token,
        "iat": datetime.datetime.now(datetime.timezone.utc),
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
    }
    return jwt.encode(payload, str(SECRET_KEY), algorithm="HS256")

def decode_session_token(token):
    return jwt.decode(token, str(SECRET_KEY), algorithms=["HS256"])