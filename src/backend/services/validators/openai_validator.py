from services.chat.providers.openai_provider import init_client, send_message

def validate_openai_api_key():
    try:
        client = init_client()
        return send_message(client, "My API key is valid?")
    except Exception as e:
        return {"error": f"Failed to validate OpenAI key: {str(e)}"}