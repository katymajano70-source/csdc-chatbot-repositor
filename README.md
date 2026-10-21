# Chatbot Asistente en la Nube para Atención Ciudadana (CSDC)

Repositorio profesional para el proyecto de asistente digital del Centro de Servicios Digitales Ciudadanos (CSDC), desarrollado para apoyar la atención automatizada de trámites, consultas y solicitudes ciudadanas a través de canales digitales.

## 📌 Descripción general

El objetivo del proyecto es reducir la carga operativa del personal institucional y mejorar la experiencia del ciudadano mediante un chatbot que:

- responde preguntas frecuentes sobre trámites, servicios y procedimientos institucionales;
- orienta a la ciudadanía en procesos de Simple.sv, Identidad Digital y servicios de la ESIT;
- captura solicitudes, denuncias o requerimientos en formato estructurado;
- integra canales como Telegram, webchat o nodos automatizados mediante Dialogflow CX y n8n;
- registra la información en Google Sheets a través de un webhook middleware en Python.

Este repositorio corresponde a una versión Lite / MVP orientada a demostrar la viabilidad técnica y funcional del caso de uso para atención ciudadana digital.

---

## 🎯 Objetivos del proyecto

1. Automatizar atención de consultas recurrentes de la ciudadanía.
2. Simplificar el registro de incidentes, solicitudes y denuncias.
3. Centralizar la información capturada en una hoja de cálculo para revisión y seguimiento.
4. Integrar la experiencia de atención con herramientas de automatización y flujo conversacional.
5. Crear una base reutilizable para extensiones futuras hacia canales adicionales y procesos más complejos.

---

## 🧩 Componentes principales

- Dialogflow CX: orquestación del flujo conversacional e intención del usuario.
- n8n: automatización de procesos y conectividad con servicios externos.
- Python: procesamiento del webhook y manejo de la lógica de registro.
- Google Sheets: almacenamiento y trazabilidad de solicitudes.
- Telegram / webchat: canales de interacción con la ciudadanía.

---

## 📁 Estructura del repositorio

```text
csdc-chatbot-repo/
├── .env.example                     # Variables de entorno de ejemplo
├── .gitignore                       # Exclusiones de Git
├── README.md                        # Documentación principal
├── docs/                            # Documentación del proyecto
│   ├── Bitacora_de_Trabajo_Semanal.md
│   ├── Catalogo_de_Intenciones_y_Respuestas.md
│   ├── Documento_de_Analisis_Casos_de_Uso.md
│   ├── Documento_de_Diseno_y_Arquitectura.md
│   ├── Informe_Profesional_Final.md
│   ├── Matriz_de_Pruebas_Conversacionales.md
│   └── Plan_de_Recursos_Tecnologicos.md
├── flows/                           # Definiciones de flujos e intenciones
│   ├── dialogflow_cx_agent.json
│   └── n8n_workflow_csdc.json
├── src/                             # Código fuente del backend webhook
│   ├── main.py
│   ├── requirements.txt
│   └── service_account.json.example
├── tests/                           # Casos de prueba y payloads
│   ├── test_webhook.sh
│   └── test_webhook_payload.json
└── .venv/                           # Entorno virtual local (no versionado)
```

---

## ✅ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de contar con:

- Python 3.10 o superior
- pip y entorno virtual
- acceso a una cuenta de Google Cloud con Sheets habilitado
- archivo JSON de credenciales de servicio de Google
- token de bot de Telegram si se habilita ese canal
- variables de entorno configuradas para el entorno local o de despliegue

---

## ⚙️ Configuración del entorno

1. Clona el repositorio:

```bash
git clone <url-del-repositorio>
cd csdc-chatbot-repo
```

2. Crea un entorno virtual:

```bash
python -m venv .venv
```

En Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

En Linux/macOS:

```bash
source .venv/bin/activate
```

3. Instala dependencias:

```bash
pip install -r src/requirements.txt
```

4. Configura las variables de entorno copiando el archivo de ejemplo:

```bash
copy .env.example .env
```

o en Linux/macOS:

```bash
cp .env.example .env
```

Contenido sugerido del archivo `.env`:

```env
GOOGLE_APPLICATION_CREDENTIALS=service_account.json
SPREADSHEET_NAME=Registro_Solicitudes_CSDC
TELEGRAM_BOT_TOKEN=tu_telegram_bot_token_aqui
GMAIL_SENDER_USER=notificaciones@csdc.gob.sv
PORT=8080
```

5. Configura la credencial de Google Sheets:

- Descarga el archivo JSON del servicio de Google Cloud.
- Renómbralo como `service_account.json` y colócalo en la carpeta `src/` o ajusta la variable `GOOGLE_APPLICATION_CREDENTIALS` según el path real.

---

## 🚀 Ejecución local

Desde la raíz del proyecto:

```bash
python src/main.py
```

El script actual incluye un ejemplo de prueba de webhook con datos de sesión y genera una respuesta JSON de ejemplo. Esto permite validar la estructura del payload y la lógica de procesamiento antes de integrarlo con Dialogflow CX, n8n o Telegram.

---

## 🧪 Pruebas

El repositorio incluye un payload de prueba y un script de validación para enviar una solicitud al webhook.

Ejecuta la prueba:

```bash
bash tests/test_webhook.sh
```

También puedes revisar el archivo `tests/test_webhook_payload.json` para adaptar los datos de prueba a nuevos casos de uso.

---

## 🔄 Flujo de operación

1. El usuario interactúa con el chatbot por Telegram o Webchat.
2. El flujo conversacional se define en Dialogflow CX.
3. Se ejecutan automatizaciones mediante n8n.
4. El webhook recibe la información y valida la solicitud.
5. La información se registra en Google Sheets para seguimiento administrativo.

---

## 📚 Documentación complementaria

La carpeta `docs/` contiene la documentación completa del proyecto, incluyendo:

- análisis de casos de uso;
- catálogo de intenciones y respuestas;
- diseño y arquitectura;
- planificación de recursos;
- pruebas conversacionales;
- informe final del proyecto;
- bitácora semanal de trabajo.

---

## 🛡️ Consideraciones de seguridad

- No subas credenciales ni archivos de servicio JSON al repositorio.
- Usa variables de entorno o secretos del entorno de despliegue.
- Agrega a `.gitignore` cualquier archivo sensible como `.env`, `service_account.json` y otros secretos.

---

## 📌 Estado del proyecto

Este repositorio representa una solución base funcional en formato MVP/Lite para la atención ciudadana digital. Puede ampliarse con:

- autenticación y validación de usuarios;
- integración con más servicios públicos;
- lógica avanzada de routing y escalamiento;
- dashboards para monitoreo y analítica;
- despliegue en nube con automatización continua.

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Para proponer mejoras:

1. realiza un fork del repositorio;
2. crea una rama con tu cambio;
3. valida la funcionalidad con pruebas;
4. abre un pull request describiendo el objetivo y los resultados.

---

## 📎 Licencia

El contenido de este repositorio está orientado a uso académico y profesional dentro del marco del proyecto de atención ciudadana digital. Se recomienda revisar la política institucional correspondiente antes de uso comercial o despliegue en producción.

---

## Contacto

Proyecto: Chatbot Asistente en la Nube para Atención Ciudadana (CSDC)
Institución: Secretaría de Innovación de El Salvador (ESIT)

