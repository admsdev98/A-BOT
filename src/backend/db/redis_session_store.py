from .redis_client import redis_client
from typing import Optional

def save_session_token(session_id: str, token: str, expire_seconds: int = 3600):
    redis_client.setex(session_id, expire_seconds, token)

def save_session_ip(session_id: str, ip: str, expire_seconds: int = 3600):
    redis_client.setex(session_id, expire_seconds, ip)

def get_session_token(session_id: str) -> Optional[str]:
    result = redis_client.get(session_id)
    return str(result) if result else None

def get_session_ip(session_id: str) -> Optional[str]:
    result = redis_client.get(session_id)
    return str(result) if result else None

def delete_session_token(session_id: str):
    redis_client.delete(session_id)
