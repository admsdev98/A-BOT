import streamlit as st
import sys
from pathlib import Path

# Añadir el directorio padre al path para las importaciones
sys.path.append(str(Path(__file__).parent.parent))

from services.session_manager import initialize_session_state, validate_if_user_need_to_authenticate
from views.auth_ui import show_auth_dialog
from views.chat_ui import render_chat_interface

st.title("_:blue[A-BOT]_, el asistente virtual de Adam")
st.markdown("---")

initialize_session_state()

if not validate_if_user_need_to_authenticate():
    show_auth_dialog()
else:
    with st.container(key="chat_page_container"):
        render_chat_interface() 