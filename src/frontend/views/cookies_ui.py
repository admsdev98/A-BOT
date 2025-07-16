import streamlit as st

def show_cookies_info():
    st.set_page_config(
        page_title="Política de Cookies - A-BOT",
        page_icon="🍪",
        layout="centered"
    )

    st.title("Política de Cookies")

    st.markdown("""
    <style>
    .cookies-container {
        max-width: 700px;
        margin: 2rem auto;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        color: #333333;
    }
    h2 {
        color: #0057b8;
        margin-top: 1.5rem;
    }
    a {
        color: #0057b8;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cookies-container">

    ## Uso de Cookies en A-BOT

    En A-BOT utilizamos únicamente una cookie de sesión necesaria para gestionar la autenticación segura de los usuarios mediante Auth0.

    No utilizamos cookies para fines de seguimiento, análisis, publicidad o almacenamiento de datos personales adicionales.

    Esta cookie permite mantener tu sesión iniciada y garantizar una experiencia segura y privada.

    Si deseas más información sobre cómo gestionar las cookies, puedes visitar [AboutCookies.org](https://www.aboutcookies.org).

    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅️ Volver a A-BOT"):
        st.query_params.clear()
        st.rerun()

    st.stop()

def show_cookies_info_into_chat():
    return st.markdown(
    """
    <style>
    .cookie-link-bottom-right {
        position: fixed;
        bottom: 10px;
        right: 10px;
        background: rgba(255, 255, 255, 0.9);
        padding: 6px 12px;
        border-radius: 5px;
        font-size: 13px;
        color: #555;
        box-shadow: 0 0 5px rgba(0,0,0,0.1);
        z-index: 9999;
    }
    .cookie-link-bottom-right a {
        color: #0057b8;
        text-decoration: none;
    }
    .cookie-link-bottom-right a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="cookie-link-bottom-right">
        ¿Dudas sobre nuestra <a href='?section=cookies'>Política de Cookies</a>?
    </div>
    """,
    unsafe_allow_html=True,
)

