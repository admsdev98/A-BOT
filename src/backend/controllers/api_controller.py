from interfaces.chatbot import ChatRequest
from interfaces.auth import AuthRequest

from services.chat.chat_service import get_chat_response
from services.auth.auth_service import generate_auth_response
from services.validators.openai_validator import validate_openai_api_key


def process_chat_request(chat_request: ChatRequest):
    return get_chat_response(chat_request)

def process_auth_request(auth_method: AuthRequest):
    return generate_auth_response(auth_method)

def process_validate_openai_api_key():
    return validate_openai_api_key()