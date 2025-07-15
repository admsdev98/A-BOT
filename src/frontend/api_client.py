import httpx
import streamlit as st
import streamlit.components.v1 as components

def get_chat_response(user_query):
    try:
        response = httpx.post("http://localhost:8000/api/v1/chatbot", json={"user_query": user_query}, timeout=120.0)
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


def check_if_user_is_authenticated():
    if not st.session_state.get("user_token"):
        return False
    
    st.markdown(f"User token: {st.session_state.get('user_token')}")
    is_alive = validate_if_user_token_is_alive(st.session_state.get("user_token"))

    if is_alive:
        return True
    else:
        return False

def set_user_auth_token(auth_method):
    try:
        response = httpx.post("http://localhost:8000/api/v1/auth", json={"auth_method": auth_method}, timeout=120.0)
        return response.json()
    except Exception as e:
        raise ConnectionError(f"Error al conectar con el servidor: {e}")

def validate_if_user_token_is_alive(session_cookie):
    try:
        response = httpx.get("http://localhost:8000/api/v1/auth-validate-session", params={"cookie_session": session_cookie}, timeout=120.0)
        return response.json()
    except Exception as e:
        raise ConnectionError(f"Error al conectar con el servidor: {e}")

def validate_auth_url_parameters():
    params = st.query_params
    
    if "token" in params and params["token"]:
        st.toast("¡Genial! Ya puedes chatear con A-BOT.")
        st.session_state["user_token"] = params["token"]
        st.query_params.clear()
        return True
    elif "error" in params and params["error"]:
        error_msg = params["error"][0]
        if error_msg == "auth_failed":
            st.error("Error en la autenticación. Por favor, intentalo de nuevo.")
        elif error_msg == "unknown_error":
            st.error("Error desconocido. Por favor, intenta de nuevo mas tarde.")
        else:
            st.error(f"Error: {error_msg}")
        st.query_params.clear()
        return False
    
    return None