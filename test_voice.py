import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

# 1. Cargar configuración desde el .env
load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("VOICE_ID")

# 2. Inicializar el cliente (Sintaxis moderna v1+)
client = ElevenLabs(api_key=api_key)

def test_speech():
    print("🤖 Generando audio de prueba con el nuevo cliente...")
    try:
        # Generar el audio
        audio = client.generate(
            text="Configuración exitosa. Soy el agente de voz de Miguel Ángel Arboleda.",
            voice=voice_id if voice_id else "Rachel",
            model="eleven_multilingual_v2"
        )
        
        # Guardar el archivo
        save(audio, "test_output.mp3")
        print("✅ Archivo 'test_output.mp3' generado con éxito.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_speech()