import os
import httpx
import streamlit as st
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "http://localhost:8000").rstrip("/")

def get_chat_response(user_query):
    try:
        response = httpx.post(f"{BACKEND_BASE_URL}/api/v1/chatbot", json={"user_query": user_query}, timeout=120.0)
        response_json = response.json()

        if "response" in response_json:
            return response_json.get("response")
        elif "error" in response_json:
            return response_json.get("error")
        else:
            return "Error: Respuesta inesperada del servidor"
    except httpx.ReadTimeout:
        raise TimeoutError("La respuesta está tardando más de lo esperado.")
    except Exception as e:
        raise ConnectionError(f"Error al conectar con el servidor: {e}")

def set_user_auth_token(auth_method):
    try:
        response = httpx.post(f"{BACKEND_BASE_URL}/api/v1/auth", json={"auth_method": auth_method}, timeout=120.0)
        return response.json()
    except Exception as e:
        raise ConnectionError(f"Error al conectar con el servidor: {e}")

def validate_user_auth_by_session_id(session_id):
    try:
        response = httpx.get(f"{BACKEND_BASE_URL}/api/v1/auth-validate-session", params={"cookie_session": session_id}, timeout=120.0)
        return response.json()
    except Exception as e:
        raise ConnectionError(f"Error al conectar con el servidor: {e}")

def get_remaining_chat_attempts(session_id):
    try:
        response = httpx.get(f"{BACKEND_BASE_URL}/api/v1/validate-remaining-attempts", params={"cookie_session": session_id}, timeout=120.0)
        return response.json()
    except Exception as e:
        raise ConnectionError(f"Error al conectar con el servidor: {e}")

def reduce_chat_attempts(session_id):
    try:
        response = httpx.post(f"{BACKEND_BASE_URL}/api/v1/reduce-chat-attempts", params={"cookie_session": session_id}, timeout=120.0)
        return response.json()
    except Exception as e:
        raise ConnectionError(f"Error al conectar con el servidor: {e}")