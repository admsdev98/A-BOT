# 🤖 A-BOT - Asistente Virtual de Adam

## Descripción

A-BOT es mi asistente virtual creado por y para vosotros, que os contestará cualquier pregunta relacionada sobre mí y el mundo laboral.

**💡 Este proyecto ha sido desarrollado con la ayuda de [Cursor](https://cursor.sh).**

## ✨ Características

- **Chat interactivo**: Interfaz web amigable para conversar con el bot
- **Información completa**: Respuestas sobre experiencia laboral, habilidades, proyectos y educación
- **IA avanzada**: Utiliza el modelo `phi4-mini` a través de Ollama para respuestas inteligentes, pensando en aquellas personas que tengan PC poco potentes
- **Arquitectura moderna**: Backend en FastAPI y frontend en Streamlit
- **Dockerizado**: Fácil despliegue y ejecución con Docker

## 🏗️ Arquitectura

El proyecto está estructurado en dos componentes principales:

### Backend (FastAPI)
- **API REST**: Endpoint `/chat` para procesar consultas
- **Servicio de IA**: Integración con LangChain y Ollama
- **Gestión de contexto**: Información personal y profesional estructurada

### Frontend (Streamlit)
- **Interfaz web**: Chat interactivo y responsive
- **Gestión de sesión**: Mantiene el historial de conversación
- **UX optimizada**: Diseño moderno y fácil de usar

## 🛠️ Tecnologías Utilizadas

### Backend
- **FastAPI**: Framework web moderno y rápido
- **Uvicorn**: Servidor ASGI para FastAPI
- **LangChain**: Framework para aplicaciones de IA
- **LangChain-Ollama**: Integración con Ollama
- **Ollama**: Servidor local de modelos LLM
- **Pydantic**: Validación de datos

### Frontend
- **Streamlit**: Framework para aplicaciones web de datos
- **HTTPX**: Cliente HTTP asíncrono

### DevOps
- **Docker**: Containerización de la aplicación
- **Docker Compose**: Orquestación de servicios

## ⚠️ Importante

> **⚠️ Primera ejecución lenta**: La primera vez que ejecutes el proyecto, tardará varios minutos en descargar el modelo de IA `phi4-mini` (~3GB). Las siguientes ejecuciones serán mucho más rápidas.

## 📦 Instalación y Configuración

### Prerrequisitos

- **Docker** y **Docker Compose** instalados
- **4GB+ de RAM** para ejecutar el modelo LLM
- **Conexión a internet** para la primera descarga del modelo

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

5. **Descargar el modelo:**
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

## 🛠️ Uso

1. **Abrir el navegador** y navegar a http://localhost:8501
2. **Ver el mensaje de bienvenida** de A-BOT
3. **Escribir preguntas** sobre Adam en el chat
4. **Recibir respuestas** basadas en su información profesional

### Ejemplos de preguntas

- "¿Cuál es la experiencia laboral de Adam?"
- "¿Qué tecnologías domina?"
- "¿Dónde ha trabajado en 2022?"
- "¿Sabe programar con APIs?"
- "¿Qué metodologías utiliza?"