import os
from dotenv import load_dotenv, find_dotenv
from interfaces.chatbot import ChatRequest

from services.chat.providers.openai_provider import get_openai_response
from services.chat.providers.local_provider import generate_local_chat_response

load_dotenv(find_dotenv())
ABOT_MODEL = os.getenv("ABOT_MODEL")

def generate_chat_response(chat_request: ChatRequest):
    user_query = chat_request.user_query
    try:
        if ABOT_MODEL == "openai":
            chat_response = get_openai_response(user_query)
        else:
            chat_response = generate_local_chat_response(user_query)
        return {"success": True, "response": chat_response}
    except Exception as e:
        return {"success": False, "error": str(e)}