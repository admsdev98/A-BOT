import os

from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from interfaces.chatbot import ChatRequest

from services.chatbot_service import get_chat_response as get_custom_chat_response
from services.openai_service import validate_key, get_chat_response as get_openai_chat_response

load_dotenv(find_dotenv())

app = FastAPI()

@app.post("/chat")
async def chat(request: ChatRequest):
    user_message = request.user_message

    #Modifiy .env parameter to use the API model or the custom model
    if os.getenv("USE_API_MODEL") == "True":
        response = get_openai_chat_response(user_message)
    else:
        response = get_custom_chat_response(user_message)
    
    return {"response": response}

@app.post("/validate-openai-key")
async def validate_openai_key():
    response = validate_key()
    return {"response": response}