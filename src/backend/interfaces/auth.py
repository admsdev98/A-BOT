from pydantic import BaseModel

class AuthRequest(BaseModel):
    auth_method: str    