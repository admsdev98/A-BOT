# A-BOT - Asistente Virtual Personal

## Descripción

A-BOT es un asistente virtual personal que responde consultas basándose en la información que definas sobre ti mismo. 

Se caracteriza por una configuración sencilla, uso intuitivo y rendimiento ágil.

## Características

- **Chat interactivo**, porque leer ficheros a veces es aburrido.  
- **Información personal**, permite responder en base a la información definida por el usuario.  
- **IA como agente**, compatible con OpenAI o modelos locales a través de Ollama.  
- **Simple y rápido**, backend en FastAPI y frontend en Streamlit.  
- **Dockerizado**, despliegue fácil y sencillo para cualquier desarrollador en su equipo. 

## IMPORTANTE.

Este bot está configurado para usar el nombre "Adam" por defecto. Cuando lo descargues, podrás personalizar fácilmente:

   - El nombre del bot

   - El nombre del usuario al que se refiere

   - O incluso adaptarlo para un negocio

Así, puedes ajustarlo a tus necesidades de forma sencilla y rápida.

## Tecnologías Utilizadas

### Backend  
Python / FastAPI / Uvicorn / LangChain / OpenAI

### Frontend  
Streamlit / HTTPX (cliente HTTP asíncrono)

### IA  
OpenAI GPT / Sentence Transformers / LangChain

### Infraestructura  
Docker / Docker Compose / Redis

## Instalación y Configuración

### Prerrequisitos

- **Docker** y **Docker Compose** instalados  
- **2GB+ de RAM** para ejecutar la aplicación
- **Cuenta de OpenAI** (opcional, para usar GPT)

### Configuración Inicial

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd A-BOT
   ```

2. **Configurar datos personales:**
   ```bash
   # Copiar el archivo de ejemplo
   cp src/backend/config/personal_data_example.md src/backend/config/personal_data.md
   
   # Editar con tu información personal
   nano src/backend/config/personal_data.md
   ```

3. **Configurar variables de entorno:**
   ```bash
   # Copiar el archivo de ejemplo
   cp env.example .env
   
   # Editar con tus credenciales
   nano .env
   ```

### Despliegue con Docker

1. **Levantar la aplicación:**
   ```bash
   cd docker
   docker-compose up --build
   ```

2. **Acceder a la aplicación:**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs


## Desarrollo Local

### Backend
```bash
cd src/backend
uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd src/frontend
streamlit run app.py --server.port 8501
```

## Configuración Opcional: Modelos Locales con Ollama

### IA (OPCIONAL, para equipos con recursos medios - altos)
Ollama / GPT-3.5 / GTP-3.5 turbo

### Prerrequisitos adicionales

- **OPCIONAL. 4GB+ de RAM** para ejecutar el modelo LLM preconfigurado  

**Obligatorio**: A-BOT requiere Ollama instalado en tu sistema para funcionar con modelos locales.

1. **Instalar Ollama:**  
   [Descargar desde la página oficial][ollama-download]

2. **Descargar el modelo requerido:**  
   ```bash
   ollama pull phi4-mini
   ```

3. **Verificar la instalación:**  
   ```bash
   ollama list
   ```

### Configuración para modelos locales

1. **Cambiar variable de entorno:**
   ```bash
   # En tu archivo .env
   ABOT_MODEL=local
   ```

2. **Levantar con Docker:**
   ```bash
   cd docker
   docker-compose up --build
   ```

> **OPCIONAL. Primera ejecución lenta**: Si utilizas el modelo local configurado por defecto (`phi4-mini`) u otro compatible, la primera vez que ejecutes el proyecto tardará varios minutos en descargar el modelo de IA (~3GB).

[ollama-download]: https://ollama.ai/download

## Licencia

Este proyecto está bajo la Licencia MIT.
