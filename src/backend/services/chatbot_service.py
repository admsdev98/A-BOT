from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from config.personal_data import user_context

def get_chat_response(prompt):
    template = """
    Answer in Spanish and briefly, unless otherwise indicated.

    Here is the context:
    {context}

    Question:
    {question}

    Answer:

    """
    model = OllamaLLM(model="phi4-mini")
    prompt_template = PromptTemplate.from_template(template)
    chain = prompt_template | model
    return chain.invoke({"context": user_context, "question": prompt.prompt}) 
