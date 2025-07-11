from fastapi import APIRouter
from fastapi.responses import RedirectResponse
import os

from interfaces.chatbot import ChatRequest
from interfaces.auth import AuthRequest
from controllers.api_controller import handle_chat_message, handle_auth_message, handle_validate_openai_api_key
from controllers.callback_controller import handle_google_auth_callback

router = APIRouter()

@router.post("/chatbot")
async def handle_chat_endpoint(chat_request: ChatRequest):
    return handle_chat_message(chat_request)

@router.post("/auth")
async def handle_auth_endpoint(auth_method: AuthRequest):
    return handle_auth_message(auth_method)

@router.post("/validate-openai-key")
async def handle_validate_openai_api_key_endpoint():
    return handle_validate_openai_api_key()

@router.get("/auth/google/callback")
async def handle_google_auth_endpoint(code):
    response = await handle_google_auth_callback(code) 
    return RedirectResponse(url=str(response.get("redirect_url")))