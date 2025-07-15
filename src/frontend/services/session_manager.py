import streamlit as st
from services.api_client import validate_auth_url_parameters, validate_user_auth_by_ip, validate_if_user_token_is_alive

def initialize_session_state():
    if "user_token" not in st.session_state:
        st.session_state["user_token"] = None

    if "tried_send" not in st.session_state:
        st.session_state["tried_send"] = False

    if "input_text_saved" not in st.session_state:
        st.session_state["input_text_saved"] = ""

def validate_session():
    validate_auth_url_parameters()

def check_authentication():
    if st.session_state["user_token"]:
        try:
            session_is_alive = validate_if_user_token_is_alive(st.session_state["user_token"])
            
            if session_is_alive.get("exists") == False:
                st.session_state["user_token"] = None
                st.session_state["auth_failure_reason"] = "session_expired"
                return False
                
            return True
        except Exception as e:
            print(f"Error validando token: {e}")
            st.session_state["user_token"] = None
    
    try:
        ip_validation = validate_user_auth_by_ip()

        if ip_validation.get("exists"):
            return True
        else:
            st.session_state["auth_failure_reason"] = "no_ip_session"
    except Exception as e:
        print(f"Error validando autenticación por IP: {e}")
    
    return False 