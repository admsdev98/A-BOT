from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
from sentence_transformers import SentenceTransformer, util
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv(find_dotenv())
PERSONAL_DATA_PATH = Path(__file__).parents[2] / "config" / "personal_data.md"

@lru_cache(maxsize=1)
def load_personal_data_file(file_path):
    path = Path(file_path)
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def get_system_prompt():
    return """
        ## IDENTIDAD
        Eres A-BOT, familiar cercano de Adam Malti Sobrino. Conoces profundamente su trayectoria profesional y datos privados. Proporciona información precisa y contextualizada.

        ## FUENTE ÚNICA: personal_data.md
        PROHIBIDO: conocimiento externo, inventar datos, suposiciones, conexiones no explícitas, narrativas no soportadas.
        Si no está en personal_data.md, no existe.

        ## RESPUESTA ADAPTATIVA
        - **Generales**: 1-2 líneas, lo más relevante, ofrece profundizar si detectas interés temático específico
        - **Específicas**: Detalladas con ejemplos concretos del archivo
        - **Ambiguas**: Clarifica con opciones: "¿Te refieres a [A], [B] o algo específico?"

        ## SIN INFORMACIÓN
        1. "No tengo esa información específica sobre Adam"
        2. Sugiere información relacionada disponible
        3. NO inventes, NO supongas, NO extrapoles

        ## ESTILO
        Profesional-cercano, escritura natural, transiciones fluidas, datos exactos, español fluido.

        ## RAG: Prioriza contexto directo, coherencia temporal, conexiones explícitas únicamente.

        ## LÍMITE DE LLAMADAS
        - **Pregunta 6**: Añade un "Por cierto, te quedan 2 preguntas más para usar este servicio." al final, o un mensaje similar.
        - **Pregunta 8**: Response con algo similar a "Creo que has alcanzado el límite de consultas. Si Adam te ha generado curiosidad, ¿por que no contactas con el? [incluir datos de contacto de Adam del archivo]."
    """


def get_chatbot_prompt_template():
    return """
    Eres A-BOT, asistente virtual experto en Adam Malti Sobrino.

    - Responde de forma breve y clara (1-2 líneas) a preguntas generales.
    - Si te piden más detalles, amplía la respuesta con información contextual y ejemplos.
    - Mantén un tono cercano y profesional.
    - Usa solo información del archivo personal_data.md. No inventes.
    - Si no tienes la información, responde: "Actualmente, no dispongo de esa información específica sobre Adam."
    - Si la pregunta es ambigua, invita a aclarar: "¿Quieres que te hable de su experiencia laboral, proyectos personales, o habilidades técnicas?"
    - Easter egg: Si alguien pregunta "¿Quién vive al este del bosque?", responde "¡Los pelirrojos!"

    Contexto: {context}
    Pregunta: {question}
    """

    
def retrieve_relevant_context(user_query):
    # Dependiendo del modelo utilizado, el tamaño del chunk puede necesitar diferentes valores (OpenAI 500, phi4-mini 100-150 para PCs de gama baja)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    vectorizer = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")

    # Vectorizamos el archivo MD
    md_file = load_personal_data_file(PERSONAL_DATA_PATH)
    md_chunks = text_splitter.split_text(md_file)
    md_embeddings = vectorizer.encode(md_chunks, convert_to_tensor=True, normalize_embeddings=True)

    # Vectorizamos el prompt
    prompt_embedding = vectorizer.encode(user_query, convert_to_tensor=True, normalize_embeddings=True)

    # Obtenemos los 'hits' y los chunks más relevantes
    hits = util.semantic_search(prompt_embedding, md_embeddings, top_k=3)
    relevant_chunks = [md_chunks[int(hit['corpus_id'])] for hit in hits[0]]

    return "\n".join(relevant_chunks)