from interfaces.chatbot import ChatRequest
from interfaces.auth import AuthRequest

from services.chat.chat_service import generate_chat_response
from services.auth.auth_service import generate_auth_response
from services.validators.openai_validator import validate_openai_api_key


def handle_chat_message(chat_request: ChatRequest):
    return generate_chat_response(chat_request)

def handle_auth_message(auth_method: AuthRequest):
    return generate_auth_response(auth_method)

def handle_validate_openai_api_key():
    return validate_openai_api_key()