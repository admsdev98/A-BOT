import os
from dotenv import load_dotenv, find_dotenv

from interfaces.chatbot import ChatRequest
from services.chat.providers.openai_provider import get_openai_response
from services.chat.providers.local_provider import get_local_chat_response

env_file = ".env.local" if os.getenv("ENVIRONMENT") == "local" else ".env"
load_dotenv(find_dotenv(env_file))

ABOT_MODEL = os.getenv("ABOT_MODEL")

def get_chat_response(chat_request: ChatRequest):
    user_query = chat_request.user_query
    try:
        if ABOT_MODEL == "openai":
            chat_response = get_openai_response(user_query)
        else:
            chat_response = get_local_chat_response(user_query)
        return {"success": True, "response": chat_response}
    except Exception as e:
        return {"success": False, "error": str(e)}