import os
import json
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

# Cargamos variables de entorno
load_dotenv()

class IsabelSurveyEngine:
    """
    Engine para la automatización de encuestas de voz.
    Inspirado en el modelo de atención empática de Sistecrédito.
    """
    def __init__(self, kb_path='knowledge_base.json'):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.client = ElevenLabs(api_key=self.api_key)
        self.assets_dir = "audio_assets"
        
        # Cargar Base de Conocimiento
        with open(kb_path, 'r', encoding='utf-8') as f:
            self.kb = json.load(f)
            
        self.voice_id = os.getenv("VOICE_ID", "Rachel") # Fallback a Rachel
        
        if not os.path.exists(self.assets_dir):
            os.makedirs(self.assets_dir)

    def _get_audio(self, text, file_id):
        """Gestiona el caché para optimizar latencia y consumo de créditos."""
        file_path = os.path.join(self.assets_dir, f"{file_id}.mp3")
        
        if os.path.exists(file_path):
            print(f"✔️ [CACHE] Audio listo: {file_id}")
            return file_path
            
        print(f"🌐 [API] Generando voz para: {file_id}...")
        try:
            audio = self.client.generate(
                text=text,
                voice=self.voice_id,
                model="eleven_multilingual_v2"
            )
            save(audio, file_path)
            return file_path
        except Exception as e:
            print(f"❌ Error en ElevenLabs: {e}")
            return None

    def build_survey_assets(self):
        """Genera todos los archivos de la encuesta basados en el KB."""
        print(f"\n--- Iniciando construcción de assets para {self.kb['empresa']} ---")
        
        # 1. Bienvenida personalizada
        intro_text = f"Hola, soy Isabel de {self.kb['empresa']}. Qué alegría saludarte. Como eres un aliado de {self.kb['aliado_principal']}, queremos escucharte."
        self._get_audio(intro_text, "0_bienvenida")

        # 2. Procesar preguntas del JSON
        for q in self.kb['preguntas']:
            self._get_audio(q['texto'], q['file_id'])

        # 3. Despedida
        despedida = "Muchas gracias por tu tiempo. Tus respuestas nos ayudan a mejorar cada día. ¡Feliz día!"
        self._get_audio(despedida, "z_despedida")
        
        print("\n✅ Proceso finalizado. Carpeta 'audio_assets' actualizada.")

if __name__ == "__main__":
    engine = IsabelSurveyEngine()
    engine.build_survey_assets()