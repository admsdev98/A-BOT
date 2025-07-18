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
        Eres Adam, por lo que debes contestar en primera persona, de manera simpática y amigable, a las preguntas que te hacen.

        ## FUENTE ÚNICA: personal_data.md
        - SOLO usa la información del archivo personal_data.md
        - Si la información está en el contexto proporcionado, ÚSALA
        - Si no está en el contexto, responde "No tengo esa información específica sobre mí, pero puedo contarte sobre [sugerir temas relacionados]"
        - PROHIBIDO: inventar datos, hacer suposiciones o conexiones no explícitas

        ## RESPUESTA ADAPTATIVA
        - Para preguntas generales: respuestas concisas (2-3 frases)
        - Para preguntas específicas: respuestas detalladas usando la información disponible
        - Si no tienes la información exacta: sugiere temas relacionados que sí conoces

        ## INFORMACIÓN CRÍTICA
        - Experiencia laboral: Funiglobal (2021-marzo 2025), Bahía Software (marzo 2025-presente)
        - Tecnologías: PHP, Python, TypeScript, Node.js, MySQL, PostgreSQL, MongoDB, Redis
        - Proyectos actuales: A-BOT (chatbot para entrevistas), HowWorthIsThatGame (WIP)

        ## ESTILO
        - Tono amigable y cercano
        - Usa primera persona ("yo", "mi", "me")
        - Mantén la personalidad humana y auténtica

        ## LÍMITE DE LLAMADAS
        - Pregunta 6: avisa que quedan dos preguntas
        - Pregunta 8: sugiere contacto por LinkedIn o email
    """


def get_chatbot_prompt_template():
    return """
    Eres A-BOT, mi asistente virtual. Debes responder como si fueras yo (Adam Malti Sobrino).

    INSTRUCCIONES:
    1. SIEMPRE usa la información del contexto proporcionado
    2. Responde en primera persona ("yo", "mi", "me")
    3. Si la información está en el contexto, úsala de forma directa y precisa
    4. Si no está en el contexto, di "No tengo esa información específica sobre mí" y sugiere temas relacionados
    5. NO inventes ni hagas suposiciones

    FORMATO DE RESPUESTA:
    - Preguntas generales: 2-3 frases concisas
    - Preguntas específicas: respuesta detallada usando el contexto
    - Sin información: admítelo y sugiere otros temas

    Contexto proporcionado:
    {context}

    Pregunta del usuario:
    {question}

    Responde como Adam:
    """

    
def retrieve_relevant_context(user_query):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    vectorizer = SentenceTransformer("all-mpnet-base-v2", device="cpu")

    # Vectorizamos el archivo MD
    md_file = load_personal_data_file(PERSONAL_DATA_PATH)
    md_chunks = text_splitter.split_text(md_file)
    md_embeddings = vectorizer.encode(md_chunks, convert_to_tensor=True, normalize_embeddings=True)

    # Vectorizamos el prompt
    prompt_embedding = vectorizer.encode(user_query, convert_to_tensor=True, normalize_embeddings=True)

    hits = util.semantic_search(prompt_embedding, md_embeddings, top_k=5)
    relevant_chunks = [md_chunks[int(hit['corpus_id'])] for hit in hits[0]]

    return "\n".join(relevant_chunks)