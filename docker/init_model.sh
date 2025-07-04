#!/bin/bash

# Iniciar Ollama en segundo plano
ollama serve &

# Esperar a que Ollama esté listo
sleep 5

# Descargar el modelo phi4-mini
ollama pull phi4-mini

# Ejecutar la aplicación FastAPI
exec uvicorn backend.main:app --host 0.0.0.0 --port 8000 