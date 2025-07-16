import streamlit as st
from services.api_client import validate_user_auth_by_session_id, get_remaining_chat_attempts

def initialize_session_state():
    st.session_state["session_id"] = st.context.cookies.get("session_id")
    st.session_state["tried_send"] = st.session_state.get("tried_send", False)
    st.session_state["input_text_saved"] = st.session_state.get("input_text_saved", False)
    st.session_state["auth_failure_reason"] = st.session_state.get("auth_failure_reason", None)

    if "cookies_section" not in st.session_state:
        st.session_state["cookies_section"] = False

    if "cookies_accepted" not in st.session_state:
        st.session_state["cookies_accepted"] = False

def validate_if_user_need_to_authenticate():
    if not validate_user_session_id():
        return False
    
    if not validate_message_attempts():
        return False

    return True
    
 
def validate_user_session_id():
    if "session_id" not in st.session_state:
        return False

    try:
        session_id = st.session_state["session_id"]
        validation_result = validate_user_auth_by_session_id(session_id)
        return validation_result.get("exists", False)

    except Exception as e:
        return False


def validate_message_attempts():
        user_attempts = get_remaining_chat_attempts(st.session_state["session_id"]) 
        
        if user_attempts.get("attempts") == False:
            st.session_state["auth_failure_reason"] = "attempts_exceeded"
            return False
        
        return True

