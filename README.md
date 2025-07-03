# A-BOT: Chatbot Local con Llama

Un chatbot inteligente y conversacional basado en modelos Llama que funciona completamente de forma local, sin necesidad de conexión a internet para el procesamiento de lenguaje natural.

## 🚀 Características

- **Procesamiento 100% local**: No requiere conexión a internet para funcionar
- **Modelos Llama**: Utiliza modelos Llama 2/3 para respuestas inteligentes
- **Interfaz conversacional**: Chat interactivo y fácil de usar
- **Configuración flexible**: Soporte para diferentes tamaños de modelo
- **Memoria de conversación**: Mantiene contexto de la conversación
- **Múltiples formatos**: Soporte para texto, código y respuestas estructuradas

## 📋 Requisitos Previos

- **Python 3.8+**
- **Git**
- **Al menos 8GB de RAM** (recomendado 16GB+)
- **GPU compatible con CUDA** (opcional, para aceleración)

## 🛠️ Instalación

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd A-BOT
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate     # En Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Descargar modelo Llama
```bash
# Opción 1: Usando Hugging Face Hub
python scripts/download_model.py --model "meta-llama/Llama-2-7b-chat-hf"

# Opción 2: Descarga manual desde Hugging Face
# Visita: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
```

## 🎯 Uso Rápido

### Iniciar el chatbot
```bash
python main.py
```

### Uso desde Python
```python
from chatbot import LlamaChatbot

# Inicializar chatbot
bot = LlamaChatbot(model_path="models/llama-2-7b-chat")

# Hacer una pregunta
response = bot.chat("¿Cuál es la capital de España?")
print(response)
```

### Interfaz web (opcional)
```bash
python web_interface.py
# Abrir http://localhost:8000 en tu navegador
```

## 📁 Estructura del Proyecto

```
A-BOT/
├── README.md                 # Este archivo
├── requirements.txt          # Dependencias de Python
├── main.py                  # Punto de entrada principal
├── chatbot.py               # Clase principal del chatbot
├── models/                  # Directorio para modelos descargados
├── config/                  # Archivos de configuración
│   ├── model_config.yaml
│   └── chat_config.yaml
├── scripts/                 # Scripts de utilidad
│   ├── download_model.py
│   └── benchmark.py
├── web/                     # Interfaz web (opcional)
│   ├── templates/
│   ├── static/
│   └── web_interface.py
├── tests/                   # Tests unitarios
└── examples/                # Ejemplos de uso
```

## ⚙️ Configuración

### Configuración del modelo
Edita `config/model_config.yaml`:

```yaml
model:
  name: "llama-2-7b-chat"
  path: "models/llama-2-7b-chat"
  max_length: 2048
  temperature: 0.7
  top_p: 0.9
  device: "auto"  # "cpu", "cuda", o "auto"
```

### Configuración del chat
Edita `config/chat_config.yaml`:

```yaml
chat:
  max_history: 10
  system_prompt: "Eres un asistente útil y amigable."
  enable_memory: true
  save_conversations: true
```

## 🔧 Opciones Avanzadas

### Usar GPU para aceleración
```bash
# Instalar PyTorch con soporte CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Cambiar modelo
```bash
# Descargar modelo diferente
python scripts/download_model.py --model "meta-llama/Llama-2-13b-chat-hf"

# O usar modelo local
python main.py --model-path /ruta/a/tu/modelo
```

### Benchmark de rendimiento
```bash
python scripts/benchmark.py --model llama-2-7b-chat
```

## 📊 Modelos Soportados

| Modelo | Tamaño | RAM Mínima | Calidad |
|--------|--------|------------|---------|
| Llama-2-7b-chat | 7B | 8GB | Buena |
| Llama-2-13b-chat | 13B | 16GB | Mejor |
| Llama-2-70b-chat | 70B | 64GB | Excelente |
| Llama-3-8b-instruct | 8B | 12GB | Muy buena |

## 🐛 Solución de Problemas

### Error: "CUDA out of memory"
- Reduce el tamaño del modelo
- Usa `device: "cpu"` en la configuración
- Cierra otras aplicaciones que usen GPU

### Error: "Model not found"
- Verifica que el modelo esté descargado en `models/`
- Ejecuta `python scripts/download_model.py`

### Rendimiento lento
- Usa GPU si está disponible
- Reduce `max_length` en la configuración
- Usa un modelo más pequeño

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- [Meta AI](https://ai.meta.com/) por los modelos Llama
- [Hugging Face](https://huggingface.co/) por la infraestructura de modelos
- [Transformers](https://github.com/huggingface/transformers) por la biblioteca de procesamiento

## 📞 Soporte

Si tienes problemas o preguntas:

- Abre un [Issue](https://github.com/tu-usuario/A-BOT/issues)
- Consulta la [documentación](docs/)
- Únete a nuestro [Discord](https://discord.gg/tu-servidor)

---

**¡Disfruta conversando con tu chatbot local! 🤖✨** 