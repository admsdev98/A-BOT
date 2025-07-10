# 🤖 A-BOT - Asistente Virtual de Adam

## Descripción

A-BOT es un asistente virtual diseñado por y para el usuario, orientado a responder consultas sobre la información que este defina. 

Se caracteriza por una configuración sencilla, uso intuitivo y rendimiento ágil.

## Características

- **Chat interactivo**, porque leer ficheros a veces es aburrido.
- **Información personal**, permite responder en base a la información definida por el usuario.
- **IA como agente**, compatible con modelos locales a través de Ollama o integrable mediante API con cualquier otro modelo.
- **Simple y rápido**, backend en FastAPI y frontend en Streamlit.
- **Dockerizado**, despliegue fácil y sencillo para cualquier desarrollador en su equipo.

## Tecnologías Utilizadas

### Backend
Python / FastAPI / Uvicorn / LangChain / Ollama / Pydantic

### Frontend
Streamlit / HTTPX (cliente HTTP asíncrono)

### IA
Ollama / GPT-3.5 

### Otros
Docker / Docker Compose

## Importante

> **Primera ejecución lenta**: Si utilizas el modelo local configurado por defecto (`phi4-mini`) u otro compatible, la primera vez que ejecutes el proyecto tardará varios minutos en descargar el modelo de IA (~3GB).

## Instalación y Configuración


### Prerrequisitos

- **Docker** y **Docker Compose** instalados
- **4GB+ de RAM** para ejecutar el modelo LLM preconfigurado

   **Obligatorio**: A-BOT requiere Ollama instalado en tu sistema para funcionar con modelos locales.

   1. **Instalar Ollama:**
   [Descargar desde la página oficial][ollama-download]

   [ollama-download]: https://ollama.ai/download

   2. **Descargar el modelo requerido:**
      ```bash
      ollama pull phi4-mini
      ```
   [ollama-models]: https://github.com/ollama/ollama?tab=readme-ov-file#model-library

   3. **Verificar la instalación:**
      ```bash
      ollama list
      ```


### Instalación con Docker (Recomendado)

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd A-BOT
   ```

2. **Ejecutar con Docker Compose:**
   ```bash
   cd docker
   docker-compose up --build
   ```

3. **Acceder a la aplicación:**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Acceso a contenedores

```bash
# Frontend (Streamlit)
docker-compose exec frontend streamlit run app.py --server.port 8501

# Backend (FastAPI) - Modelo local
docker-compose exec backend uvicorn main:app --reload --port 8000

# Backend (FastAPI) - Modelo OpenAI
docker-compose exec backend bash -c "ABOT_MODEL=openai uvicorn main:app --reload --port 8000"