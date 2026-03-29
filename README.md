🎙️ Voice AI Survey Automation: Engine "Isabel"
Este proyecto es una reconstrucción técnica de la solución que diseñé e implementé para Sistecrédito (Medellín, Colombia). Se trata de un motor de encuestas de voz automatizado que utiliza Inteligencia Artificial Generativa para transformar la experiencia del cliente en un diálogo natural, empático y eficiente.

🌟 El Problema y Mi Solución
En el sector financiero, las encuestas suelen ser frías y los clientes las abandonan. Mi enfoque fue crear a "Isabel", una analista virtual con acento y modismos colombianos que no suena como un robot de call center, sino como un aliado cercano.

Logros clave del proyecto:

Ingeniería de Prompt Avanzada: Diseñé un sistema de "Guardrails" y reglas de personalidad para que la IA maneje silencios, dudas y cambios de humor del cliente sin perder el hilo.

Optimización de Costos: Implementé un sistema de Caché de Audio que evita gastar créditos de API innecesarios, reutilizando respuestas comunes.

Baja Latencia: Estructura pensada para que la respuesta de voz sea casi instantánea, mejorando la retención del usuario en la llamada.

🏗️ Arquitectura del Sistema
El proyecto se divide en tres capas de ingeniería:

Cerebro (Knowledge Base): Un archivo JSON dinámico que permite cambiar la encuesta en segundos. Hoy puede ser para Sistecrédito y mañana para LuegoPago, sin tocar una sola línea de código.

Motor de Voz (Orquestador): Conexión profesional con la API de ElevenLabs (Python 3.12), gestionando la generación de audio multilingüe de alta fidelidad.

Pipeline de Datos (ETL): Un procesador que limpia el "ruido" de las respuestas de la IA (metadatos técnicos) y entrega los resultados listos para Excel o MongoDB.

🚀 Tecnologías Usadas
Lenguaje: Python 3.12 (Entorno virtual optimizado).

IA de Voz: ElevenLabs API (Modelos Multilingual v2).

LLM Orchestration: Prompt Engineering avanzado para modelos de lenguaje.

Data Science: Pandas para la limpieza y estructuración de resultados.

📂 Estructura del Repositorio
survey_engine.py: El corazón que genera y gestiona los audios.

data_processor.py: El limpiador que convierte conversaciones en datos útiles.

knowledge_base.json: La configuración de las preguntas y la marca.

PROMPT_ENGINEERING.md: Documento detallado con la lógica de "Isabel".

📈 Impacto en el Negocio
Este motor no solo hace llamadas; recolecta insights. Al mapear sentimientos y convertir respuestas habladas en números (0-10), permito que las empresas vean en tiempo real dónde están fallando en su servicio al cliente.

Notas de Instalación
Nota: Este proyecto requiere una API Key de ElevenLabs configurada en un archivo .env. El sistema está diseñado para ser Plug & Play: configuras tus preguntas en el JSON y el motor se encarga del resto.