from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from services.chat.rag_service import retrieve_relevant_context, get_chatbot_prompt_template


def get_local_chat_response(user_query: str) -> str:
    """Obtiene respuesta del chat usando el modelo local."""
    try:
        prompt_template = get_chatbot_prompt_template()
        
        model = OllamaLLM(model="phi4-mini")
        prompt_template = PromptTemplate.from_template(prompt_template)
        chain = prompt_template | model
        
        response = chain.invoke({
            "context": retrieve_relevant_context(user_query), 
            "question": user_query
        })
        
        return '(LOCAL) - ' + str(response)
        
    except Exception as e:
        return "Error interno del servidor. Por favor, intenta de nuevo." 