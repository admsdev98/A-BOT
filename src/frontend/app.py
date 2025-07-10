import streamlit as st
import httpx

with open("styles/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def set_first_message():
    first_message = "Hola, soy A-BOT, el asistente virtual de Adam. ¿En qué puedo ayudarte hoy?"
    st.session_state.messages.append({"role": "assistant", "content": first_message})
    st.session_state.first_message = True

def get_response(user_query):
    try:
        response = httpx.post("http://localhost:8000/api/v1/chatbot", json={"user_query": user_query}, timeout=120.0)
        data = response.json()
        return data["response"]
    except httpx.ReadTimeout:
        st.error("La respuesta está tardando más de lo esperado. Por favor, intenta de nuevo.")
        st.session_state.messages.append({"role": "assistant", "content": "La respuesta está tardando más de lo esperado. Por favor, intenta de nuevo."})
        return None
    except Exception as e:
        st.error(f"Error al conectar con el servidor: {e}")
        return None

st.title("🤖 A-BOT - El asistente virtual de Adam")
st.markdown("---")
st.markdown("### 👋 ¡Bienvenido!")
st.markdown("Este bot ha sido diseñado para responder todas tus preguntas sobre **Adam** y su experiencia profesional.")
st.markdown("")
st.markdown("**Puedes preguntarle sobre:** Experiencia laboral, habilidades técnicas, proyectos, educación y más información relacionada.")
st.markdown("")
st.markdown("*¡Adelante, pregunta lo que quieras!* 🚀")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "first_message" not in st.session_state:
    set_first_message()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Escribe tu mensaje aquí..."):
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.spinner("A-BOT está pensando..."):
        response = get_response(user_query)
    
    if response:
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})