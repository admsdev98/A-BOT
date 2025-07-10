import os

from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from services.rag_service import retrieve_relevant_context, get_system_prompt

load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def init_client():
    return OpenAI(api_key=OPENAI_API_KEY)

def send_message(client, messages):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}

def get_openai_response(user_query):
    client = init_client()
    retrieved_context = retrieve_relevant_context(user_query)

    messages = [
        {"role": "system", "content": get_system_prompt()},
        {"role": "assistant", "content": f"Contexto relevante:\n{retrieved_context}"},
        {"role": "user", "content": user_query}
    ]

    return send_message(client, messages)

def validate_openai_api_key():
    try:
        client = init_client()
        return send_message(client, "My API key is valid?")
    except Exception as e:
        return {"error": f"Failed to validate OpenAI key: {str(e)}"}
    