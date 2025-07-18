import streamlit as st
from services.api_client import get_chat_response, reduce_chat_attempts
from views.cookies_ui import show_cookies_info_into_chat

def set_first_message():
    first_message = "Hola! ¿En qué puedo ayudarte hoy?"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if not st.session_state.get("first_message", False):
        st.session_state.messages.append({"role": "assistant", "content": first_message})
        st.session_state.first_message = True

def main_chat():
    user_query = st.chat_input("Escribe tu mensaje aquí...", key="input_text")
    show_cookies_info_into_chat()

    if user_query:
        st.session_state["input_text_saved"] = user_query
        user_query = st.session_state.pop("input_text_saved", user_query)

        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})

        with st.spinner("Dejame pensar..."):
            response = None
            try:
                response = get_chat_response(user_query)
            except Exception as e:
                st.error(f"Error: {e}")

        if response:
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

        try:
            reduce_chat_attempts(st.session_state["session_id"])
        except Exception as e:
            print(f"Error reducing attempts: {e}")


def render_chat_interface():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "first_message" not in st.session_state:
        set_first_message()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    main_chat() 