from fastapi import FastAPI
from interfaces.chatbot import ChatRequest
from services.chatbot_service import get_chat_response

app = FastAPI()

@app.post("/chat")
async def chat(prompt: ChatRequest):
    response = get_chat_response(prompt)
    return {"response": response}