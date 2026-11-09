import os
import json
from flask import Flask, request, jsonify

app = Flask(_name_)

def handle_webhook_request(req_data):
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

@app.route('/webhook', methods=['POST'])
def webhook():
    req_data = request.get_json(force=True)
    response = handle_webhook_request(req_data)
    return jsonify(response)

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
                "sector": "Salud"
            }
        }
    }
    print(json.dumps(handle_webhook_request(test_req), indent=2))
