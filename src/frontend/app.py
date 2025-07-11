import streamlit as st
from auth import show_auth_dialog
from api_client import get_chat_response, handle_url_params

def set_first_message():
    first_message = "Hola, soy A-BOT, el asistente virtual de Adam. ¿En qué puedo ayudarte hoy?"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if not st.session_state.get("first_message", False):
        st.session_state.messages.append({"role": "assistant", "content": first_message})
        st.session_state.first_message = True

def main_chat():
    user_query = st.chat_input("Escribe tu mensaje aquí...", key="input_text")

    if user_query:
        st.session_state["input_text_saved"] = user_query

        if not st.session_state["user_token"]:
            st.session_state["tried_send"] = True
            st.rerun()
        else:
            user_query = st.session_state.pop("input_text_saved", user_query)

            with st.chat_message("user"):
                st.markdown(user_query)
            st.session_state.messages.append({"role": "user", "content": user_query})

            with st.spinner("A-BOT está pensando..."):
                response = None
                try:
                    response = get_chat_response(user_query)
                except Exception as e:
                    st.error(f"Error: {e}")

            if response:
                with st.chat_message("assistant"):
                    st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

handle_url_params()

if "user_token" not in st.session_state:
    st.session_state["user_token"] = None

if "tried_send" not in st.session_state:
    st.session_state["tried_send"] = False

if "input_text_saved" not in st.session_state:
    st.session_state["input_text_saved"] = ""

st.title("🤖 A-BOT - El asistente virtual de Adam")
st.markdown("---")
st.markdown("### 👋 ¡Bienvenido!")
st.markdown("Este bot ha sido diseñado para responder todas tus preguntas sobre **Adam** y su experiencia profesional.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "first_message" not in st.session_state:
    set_first_message()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if not st.session_state["user_token"]:
    show_auth_dialog()

main_chat()

# Mantener el modal si el usuario intenta enviar sin autenticarse
if not st.session_state["user_token"] and st.session_state["tried_send"]:
    show_auth_dialog()
