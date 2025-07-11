import streamlit as st
import uuid

from api_client import set_google_auth_token

def generate_token(method: str) -> str:
    st.info(f"Generando token para método: {method}")
    return str(uuid.uuid4())

@st.dialog("🔐 Validación para acceder a A-BOT", width="small")
def show_auth_dialog():
    st.markdown("### Elige un método de validación")
    option = st.radio("Método", ["Login con LinkedIn", "Login con Google", "Captcha"])

    if option == "Login con LinkedIn":
        st.write("Haz clic para iniciar sesión con LinkedIn:")
        if st.button("Iniciar login con LinkedIn"):
            token = generate_token("LinkedIn")
            st.session_state["user_token"] = token
            st.session_state["tried_send"] = False
            st.rerun()

    elif option == "Login con Google":
        if st.button("Iniciar login con Google"):
            try:
                google_auth_url = set_google_auth_token("google")
                st.markdown(f"### 🔗 Autenticación con Google")
                st.markdown(f"Haz clic en el enlace para autenticarte con Google:")
                st.markdown(f"[🔐 **Iniciar sesión con Google**]({google_auth_url})")
                st.info("Se abrirá una nueva ventana para completar la autenticación con Google")
                st.warning("Después de autenticarte, serás redirigido de vuelta a la aplicación")
            except Exception as e:
                st.error(f"Error al iniciar autenticación con Google: {e}")

    elif option == "Captcha":
        st.write("Resuelve el captcha para continuar:")
        if st.button("Simular resolución captcha"):
            token = generate_token("Captcha")
            st.session_state["user_token"] = token
            st.session_state["tried_send"] = False
            st.rerun()
