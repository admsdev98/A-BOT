from fastapi import APIRouter

from interfaces.chatbot import ChatRequest
from controller.chatbot_controller import handle_chat_message, validate_openai_api_key

router = APIRouter()

@router.post("/chatbot")
async def handle_chat_endpoint(chat_request: ChatRequest):
    return handle_chat_message(chat_request)

@router.post("/validate-openai-key")
async def validate_api_key_endpoint():
    return validate_openai_api_key()