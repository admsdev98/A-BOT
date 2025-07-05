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

### Instalación Local (sin Docker)

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd A-BOT
   ```

2. **Crear entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # o
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instalar Ollama:**
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

5. **Descargar el modelo predefinido:**
   ```bash
   ollama pull phi4-mini
   ```

6. **Ejecutar el backend:**
   ```bash
   cd src/backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

7. **Ejecutar el frontend (nueva terminal):**
   ```bash
   cd src/frontend
   streamlit run app.py
   ```