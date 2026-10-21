import os
import json

def handle_webhook_request(req_data):
    """
    Procesador de Webhook para Dialogflow CX / n8n
    """
    session_info = req_data.get("sessionInfo", {})
    parameters = session_info.get("parameters", {})

    nombre = parameters.get("nombre_ciudadano", "Anónimo")
    correo = parameters.get("correo_contacto", "N/A")
    sector = parameters.get("sector", "General")

    response_text = f"Solicitud registrada para {nombre} ({sector}). Contacto: {correo}"

    return {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [response_text]
                    }
                }
            ]
        }
    }

if __name__ == "__main__":
    test_req = {
        "sessionInfo": {
            "parameters": {
                "nombre_ciudadano": "María López",
                "correo_contacto": "maria@ejemplo.sv",
                "sector": "Salud"
            }
        }
    }
    print(json.dumps(handle_webhook_request(test_req), indent=2))
