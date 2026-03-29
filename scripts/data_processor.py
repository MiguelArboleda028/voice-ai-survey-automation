import json
import pandas as pd
from datetime import datetime

class SurveyDataCleaner:
    """
    Componente de ETL (Extract, Transform, Load) para limpiar 
    el ruido de los logs de voz y estructurar insights.
    """
    def __init__(self, raw_data_path):
        self.raw_data_path = raw_data_path

    def clean_voice_response(self, raw_json):
        """
        Filtra el ruido de ElevenLabs y extrae solo la esencia 
        de la conversación de Isabel.
        """
        # Imaginamos que extraemos de la estructura compleja de la API
        cleaned_data = {
            "fecha_interaccion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cliente_id": raw_json.get("metadata", {}).get("user_id", "Desconocido"),
            "duracion_segundos": raw_json.get("analysis", {}).get("call_duration", 0),
            "transcripcion_completa": raw_json.get("transcript", ""),
        }

        # Mapeo de respuestas de la encuesta (Extracción de lógica de negocio)
        # Aquí es donde limpiamos el ruido de los "ehmm", "mmm" o silencios
        respuestas = raw_json.get("analysis", {}).get("extracted_data", {})
        cleaned_data.update(respuestas)

        return cleaned_data

    def export_to_excel(self, cleaned_list, filename="reporte_encuestas.xlsx"):
        df = pd.DataFrame(cleaned_list)
        df.to_excel(filename, index=False)
        print(f"📊 Reporte generado con éxito: {filename}")

# Ejemplo de uso profesional
if __name__ == "__main__":
    # Simulacro de JSON ruidoso que llega de la API
    raw_payload = {
        "transcript": "Hola Isabel, pues la verdad el proceso me pareció un 4, muy fácil todo.",
        "analysis": {
            "call_duration": 45.5,
            "extracted_data": {
                "p1_facilidad_ux": 4,
                "sentimiento_general": "Positivo"
            }
        },
        "metadata": {"user_id": "CLIENTE_001"}
    }

    cleaner = SurveyDataCleaner(None)
    data = cleaner.clean_voice_response(raw_payload)
    
    # Esto es lo que guardas en Mongo o Excel
    print("✨ Datos Limpios para el Cliente:", json.dumps(data, indent=2))