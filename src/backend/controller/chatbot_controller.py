import os

from dotenv import load_dotenv, find_dotenv
from interfaces.chatbot import ChatRequest

from services.chatbot_service import generate_local_chat_response
from services.openai_service import validate_openai_api_key, get_openai_response

load_dotenv(find_dotenv())
ABOT_MODEL = os.getenv("ABOT_MODEL")

def handle_chat_message(chat_request: ChatRequest):
    user_query = chat_request.user_query

    if ABOT_MODEL == "openai":
        chat_response = get_openai_response(user_query)
    else:
        chat_response = generate_local_chat_response(user_query)
    
    return {"response": chat_response}

def validate_openai_api_key():
    return validate_openai_api_key()