from typing import Optional

from .redis_client import redis_client

def save_session_by_token(session_id: str, token: str, expire_seconds: int = 3600):
    redis_client.setex(session_id, expire_seconds, token)

def save_session_by_ip(ip: str, token: str, expire_seconds: int = 3600):
    key = f"IP:{ip}"
    redis_client.setex(key, expire_seconds, token)

def get_session_token(session_id: str) -> Optional[str]:
    result = redis_client.get(session_id)
    return str(result) if result else None

def get_session_by_ip(ip: str) -> Optional[str]:
    key = f"IP:{ip}"
    result = redis_client.get(key)
    return str(result) if result else None