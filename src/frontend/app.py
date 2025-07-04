import streamlit as st
import httpx

def set_first_message():
    first_message = "Hola, soy A-BOT, el asistente virtual de Adam. ¿En qué puedo ayudarte hoy?"
    st.session_state.messages.append({"role": "assistant", "content": first_message})
    st.session_state.first_message = True

def get_response(prompt):
    try:
        # Agregar timeout y manejo de errores
        response = httpx.post("http://localhost:8000/chat", json={"prompt": prompt}, timeout=120.0)
        return response
    except httpx.ReadTimeout:
        st.error("La respuesta está tardando más de lo esperado. Por favor, intenta de nuevo.")
        st.session_state.messages.append({"role": "assistant", "content": "La respuesta está tardando más de lo esperado. Por favor, intenta de nuevo."})
        return None
    except Exception as e:
        st.error(f"Error al conectar con el servidor: {e}")
        return None

st.title("A-BOT")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "first_message" not in st.session_state:
    set_first_message()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Mostrar indicador de carga
    with st.spinner("A-BOT está pensando..."):
        response = get_response(prompt)
    
    if response and response.status_code == 200:
        with st.chat_message("assistant"):
            st.markdown(response.json()["response"])
        st.session_state.messages.append({"role": "assistant", "content": response.json()["response"]})