import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

from services.chat.rag_service import retrieve_relevant_context, get_system_prompt

env_file = ".env.local" if os.getenv("ENVIRONMENT") == "local" else ".env"
load_dotenv(find_dotenv(env_file))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

def init_client():
    return OpenAI(api_key=OPENAI_API_KEY)

def send_message(client, messages):
    try:
        completion = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}

def get_openai_response(user_query):
    try:
        client = init_client()
        retrieved_context = retrieve_relevant_context(user_query)

        messages = [
            {"role": "system", "content": get_system_prompt()},
            {"role": "user", "content": f"""
            ### Pregunta que hace el usuario:
            {user_query}

            ### Contexto que hemos obtenido:
            {retrieved_context}"""}
        ]

        try:
            response = send_message(client, messages)
            return response
        except Exception as e:
            print(f"Error en send_message: {str(e)}")
            return {
                "content": "Lo siento, ha ocurrido un error al procesar tu pregunta. Por favor, inténtalo de nuevo en unos momentos.",
                "error": str(e)
            }

    except Exception as e:
        print(f"Error en get_openai_response: {str(e)}")
        return {
            "content": "Ha ocurrido un error inesperado. Por favor, inténtalo de nuevo.",
            "error": str(e)
        }
    