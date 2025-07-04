# PERSONAL DATA
personal_data = {
    "name": "Adam Malti Sobrino",
    "position": "Backend Developer",
    "email": "adam98ms@gmail.com",
    "phone": "684 084 411",
    "location": "Cuenca, España"
}

# PROFESSIONAL PROFILE
professional_profile = """
Desarrollador backend con más de 3 años de experiencia en Python, PHP (Yii2) y Node.js.
Especializado en integración de APIs REST, automatización de tareas y gestión de bases de datos.
Experiencia en metodologías ágiles como Kanban y Jira.
Acostumbrado a trabajar en equipo y orientado a la mejora continua y refactorización de código legacy.
"""

# WORK EXPERIENCE
work_experience = [
    {
        "company": "Funiglobal",
        "position": "Junior Developer",
        "period": "Septiembre 2021 – Marzo 2025",
        "location": "Zaragoza",
        "responsibilities": [
            "Desarrollo y mantenimiento backend con Python, PHP (Yii2) y Node.js (TypeScript)",
            "Refactorización de código legacy y automatización de tareas internas",
            "Integración y soporte de APIs REST para servicios logísticos",
            "Analítica con ElasticSearch y control de procesos con Redis",
            "Uso diario de MySQL y PostgreSQL para integraciones y informes",
            "Tecnologías: Git, Redis, ElasticSearch, RabbitMQ, Angular"
        ]
    },
    {
        "company": "Bahía Software",
        "position": "Soporte N2/N3",
        "period": "Marzo 2025 – Actualidad",
        "location": "A Coruña",
        "responsibilities": [
            "Soporte técnico en el área financiera de Inditex",
            "Resolución de incidencias de nivel N2 y N3",
            "Uso diario de SQL y MongoDB para consultas y análisis"
        ]
    }
]

# PROGRAMMING SKILLS
programming_skills = {
    "languages": ["Python", "PHP (Yii2)", "Node.js", "TypeScript", "SQL"],
    "databases": ["MySQL", "PostgreSQL", "MongoDB", "Redis"],
    "tools": ["Git", "ElasticSearch", "RabbitMQ", "Docker"],
    "frameworks": ["Yii2", "Angular"],
    "methodologies": ["Kanban", "Jira", "APIs REST"]
}

# LANGUAGES
languages = [
    {"language": "Español", "level": "Nativo"},
    {"language": "Inglés", "level": "Buena comprensión lectora y auditiva. Capacidad para escribir con apoyo"}
]

# INTERESTS
interests = [
    "Inteligencia artificial y modelos de lenguaje (LLM)",
    "Aprendizaje autodidacta constante",
    "Desarrollo de proyectos personales con IA, LangChain y Ollama"
]

# FORMATTED CONTEXT FOR THE CHATBOT
user_context = f"""
PERSONAL INFORMATION:
- Name: {personal_data['name']}
- Position: {personal_data['position']}
- Email: {personal_data['email']}
- Phone: {personal_data['phone']}
- Location: {personal_data['location']}

PROFESSIONAL PROFILE:
{professional_profile.strip()}

WORK EXPERIENCE:
"""
for exp in work_experience:
    user_context += f"""
{exp['company']} ({exp['location']})
Position: {exp['position']}
Period: {exp['period']}
Responsibilities:
"""
    for resp in exp['responsibilities']:
        user_context += f"- {resp}\n"

user_context += f"""
PROGRAMMING SKILLS:
- Languages: {', '.join(programming_skills['languages'])}
- Databases: {', '.join(programming_skills['databases'])}
- Tools: {', '.join(programming_skills['tools'])}
- Frameworks: {', '.join(programming_skills['frameworks'])}
- Methodologies: {', '.join(programming_skills['methodologies'])}

LANGUAGES:
"""
for lang in languages:
    user_context += f"- {lang['language']}: {lang['level']}\n"

user_context += f"""
INTERESTS:
"""
for interest in interests:
    user_context += f"- {interest}\n"

user_context = user_context.strip()

# For compatibility
user_data = user_context