import os
from pathlib import Path

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM


#PERSONAL_DATA_PATH = load_env_file()
PERSONAL_DATA_PATH = Path(__file__).parents[1] / "config" / "personal_data.md"

def get_chat_response(prompt):
    template = """
    Eres el asistente virtual de un desarrollador backend con experiencia en Python y PHP(Yii2).
    
    Responde ÚNICAMENTE basándote en la siguiente información personal:
    {context}
    
    Pregunta: 
    {question}
    
    Instrucciones:
    - Responde en español de manera simpatica y amigable
    - Responde en tercera persona, ya que tu no eres la persona especificada en el contexto.
    - Solo menciona información que esté en el contexto proporcionado
    - Si la información no está en el contexto, di que no tienes esa información por el momento.
    - Si te preguntan por ti, di que eres A-BOT, un asistente virtual personalizado.
    
    Respuesta:
    """
    model = OllamaLLM(model="phi4-mini")
    prompt_template = PromptTemplate.from_template(template)
    chain = prompt_template | model
    return chain.invoke({"context": retrieve_best_similarities(prompt), "question": prompt.prompt}) 

def load_md_file(file_path):
    path = Path(file_path)
    with open(path, "r") as file:
        return file.read()

def retrieve_best_similarities(prompt):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    vectorizer = SentenceTransformer("all-MiniLM-L6-v2")

    # Vectorizamos el archivo MD
    md_file = load_md_file(PERSONAL_DATA_PATH)
    md_chunks = text_splitter.split_text(md_file)
    md_embeddings = vectorizer.encode(md_chunks, convert_to_tensor=True)

    # Vectorizamos el prompt
    prompt_embedding = vectorizer.encode(prompt.prompt, convert_to_tensor=True)

    # Obtenemos los 'hits' y los chunks más relevantes
    hits = util.semantic_search(prompt_embedding, md_embeddings, top_k=3)
    relevant_chunks = [md_chunks[int(hit['corpus_id'])] for hit in hits[0]]

    return "\n".join(relevant_chunks)