import streamlit as st

from views.auth_ui import show_auth_dialog
from views.chat_ui import render_chat_interface
from services.session_manager import initialize_session_state, validate_session, check_authentication

initialize_session_state()

validate_session()

if not check_authentication():
    show_auth_dialog()
else:
    render_chat_interface()
