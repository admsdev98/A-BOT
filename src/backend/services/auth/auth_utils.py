import os
import uuid

from db.redis_session_store import get_session_token, get_session_by_ip


def validate_if_user_token_is_alive(cookie_session):
    return {"exists": get_session_token(cookie_session) is not None}

def validate_if_user_token_is_alive_by_ip(ip):
    return {"exists": get_session_by_ip(ip) is not None}

def generate_session_token(auth_data):
    return {
        "token": auth_data.get("access_token"),
        "session_id": str(uuid.uuid4())
    }