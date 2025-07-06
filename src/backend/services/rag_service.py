import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
from sentence_transformers import SentenceTransformer, util
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv(find_dotenv())
PERSONAL_DATA_PATH = Path(__file__).parents[1] / "config" / "personal_data.md"

def load_md_file(file_path):
    path = Path(file_path)
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def get_model_context():
    return """
        Eres A-BOT, un asistente virtual que responde solo sobre la experiencia laboral y datos profesionales de Adam.

        Solo utiliza la información que existe en el fichero personal_data.md. No inventes ni supongas nada que no esté allí.

        Responde con precisión y de forma concisa.

        Contrasta la informacion y trata de buscar similitudes con la informacion que tienes, y si ves que algo no existe al 100%, 
        di claramente "Actualmente, no dispongo de esa información.".

        Si dudas de algun dato, di, "Puede que si, puede que no, no se"

        Tu tono es profesional y amigable, sin dar datos innecesarios.
    """


    
def retrieve_best_similarities(message):
    # Dependiendo del modelo utilizado, el tamaño del chunk puede necesitar diferentes valores (OpenAI 500, phi4-mini 100-150 para PCs de gama baja)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    vectorizer = SentenceTransformer("all-MiniLM-L6-v2")

    # Vectorizamos el archivo MD
    md_file = load_md_file(PERSONAL_DATA_PATH)
    md_chunks = text_splitter.split_text(md_file)
    md_embeddings = vectorizer.encode(md_chunks, convert_to_tensor=True, normalize_embeddings=True)

    # Vectorizamos el prompt
    prompt_embedding = vectorizer.encode(message, convert_to_tensor=True, normalize_embeddings=True)

    # Obtenemos los 'hits' y los chunks más relevantes
    hits = util.semantic_search(prompt_embedding, md_embeddings, top_k=3)
    relevant_chunks = [md_chunks[int(hit['corpus_id'])] for hit in hits[0]]

    return "\n".join(relevant_chunks)