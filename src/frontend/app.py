import streamlit as st

from services.session_manager import initialize_session_state, validate_if_user_need_to_authenticate
from views.auth_ui import show_auth_dialog
from views.chat_ui import render_chat_interface
from views.cookies_ui import show_cookies_info

st.set_page_config(
    page_title="Who Is, A-BOT?",
    layout="centered"
)

initialize_session_state()

query_params = st.query_params
if query_params.get("section") == "cookies":
    show_cookies_info()
else:
    if not validate_if_user_need_to_authenticate():
        show_auth_dialog()
    else:
        pages = [
            st.Page("pages/chat.py", title="Chat"),
            st.Page("pages/cookies.py", title="Como usamos las cookies")
        ]
        
        pg = st.navigation(pages)
        pg.run()
