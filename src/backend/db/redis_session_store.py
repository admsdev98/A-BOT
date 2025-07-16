from typing import Optional

from .redis_client import redis_client

# Session token
def save_session_by_token(session_id: str, jwt_token: str, expire_seconds: int = 3600):
    redis_client.setex(session_id, expire_seconds, jwt_token)

def update_session_token(session_id: str, jwt_token: str, expire_seconds: int = 3600):
    redis_client.setex(session_id, expire_seconds, jwt_token)

def get_session_token(session_id: str) -> Optional[str]:
    result = redis_client.get(session_id)
    return str(result) if result else None
    
# Session attempts
def initialize_session_attempts(session_id: str, initial_attempts: int = 8, expire_seconds: int = 3600):
    key = f"ATTEMPTS:{session_id}"
    redis_client.setex(key, expire_seconds, initial_attempts)

def update_session_attempts(session_id: str, new_attempts: int, expire_seconds: int = 3600):
    key = f"ATTEMPTS:{session_id}"
    redis_client.setex(key, expire_seconds, new_attempts)

def get_session_attempts(session_id: str) -> Optional[int]:
    key = f"ATTEMPTS:{session_id}"
    result = redis_client.get(key)

    if result is None:
        return 0
    else:
        return int(str(result))