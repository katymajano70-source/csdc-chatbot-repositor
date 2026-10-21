# Documento de Diseño y Arquitectura (Fase 2)
**Proyecto:** Chatbot Asistente en la Nube para Atención Ciudadana (CSDC)  

---

## 1. Arquitectura General del Sistema
El prototipo conversacional se estructura en cuatro capas desacopladas:

```
[ Ciudadano / Usuario ] 
        │
        ▼ (Mensajes / Telegram / Webchat)
[ Canal de Mensajería ]
        │
        ▼ (Webhook HTTP / JSON API)
[ Dialogflow CX / n8n NLP Engine ] ──(Fulfillment Request)──► [ Webhook Backend / Cloud Function ]
                                                                       │
                                                                       ▼
                                                             [ Google Sheets API ]
```

---

## 2. Diagrama de Flujo Conversacional (Árbol de Diálogo)

```
                       [ Inicio / Welcome ]
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
[ Simple.sv ]          [ Identidad Digital ]        [ SAC / Denuncias ]
   │                       │                           │
   ├── Antecedentes        └── Paso a paso DUI         ├── Captura Sector/Institución
   ├── Pasaportes              SMS & Email             ├── Captura Datos Contacto
   └── Apostillas                                      └── Webhook -> Google Sheets
```

---

## 3. Especificación de Interfaces e Integraciones
* **Interfaz de Entrada:** Payload de Dialogflow CX en formato JSON conteniendo `sessionInfo.parameters`.
* **Procesamiento Middleware:** Servicio en Python (GCP Cloud Functions / Cloud Run) que valida la firma del request y procesa la lógica.
* **Interfaz de Salida (Almacenamiento):** Inserción mediante API OAuth2 en la hoja de cálculo `Registro_Solicitudes_CSDC` con columnas: `[Fecha, Nombre, Correo, Teléfono, Sector, Detalle, Estado]`.
