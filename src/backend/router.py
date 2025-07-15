from fastapi import APIRouter

from interfaces.chatbot import ChatRequest
from interfaces.auth import AuthRequest
from controllers.api_controller import process_chat_request, process_auth_request, process_validate_openai_api_key
from controllers.callback_controller import get_google_auth_response, get_github_auth_response, process_auth_validate_session_request

router = APIRouter()

@router.post("/chatbot")
async def handle_chat_endpoint(chat_request: ChatRequest):
    return process_chat_request(chat_request)

@router.post("/validate-openai-key")
async def handle_validate_openai_api_key_endpoint():
    return process_validate_openai_api_key()

@router.post("/auth")
async def handle_auth_endpoint(auth_method: AuthRequest):
    return process_auth_request(auth_method)

@router.get("/auth-validate-session")
async def handle_auth_validate_session_endpoint(cookie_session: str):
    return process_auth_validate_session_request(cookie_session)

@router.get("/auth/google/callback")
async def handle_google_auth_endpoint(code):
    return await get_google_auth_response(code) 

@router.get("/auth/github/callback")
async def handle_github_auth_endpoint(code):
    return await get_github_auth_response(code) 