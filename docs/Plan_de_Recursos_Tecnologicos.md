# Plan de Recursos Tecnológicos (Fase 0)
**Proyecto:** Chatbot Asistente en la Nube para Atención Ciudadana (CSDC)  
**Cliente:** Centro de Servicios Digitales Ciudadanos (CSDC) - Secretaría de Innovación  
**Unidad Ejecutora:** Unidad de Proyectos ESIT (Célula Conversacional Cloud)  

---

## 1. Asignación de Roles del Equipo
* **Líder de Proyecto Jr.:** Coordinación de backlog, cumplimiento de fases y enlace con tutoría.
* **Diseñador/a de Conversaciones Jr. (CX/UX):** Definición de intenciones, árbol de diálogo, tono y mensajes.
* **Ingeniero/a de Integración Cloud Jr.:** Configuración de Dialogflow CX, n8n y canales (Telegram/Web).
* **Desarrollador/a de Automatización Jr.:** Implementación de webhooks, almacenamiento en Google Sheets y notificaciones.
* **QA / Documentador Técnico Jr.:** Matriz de pruebas conversacionales, bitácora semanal e informe final.

---

## 2. Inventario de Recursos Cloud y Herramientas

| Recurso | Plataforma / Proveedor | Responsable | Uso Previsto | Límites y Observaciones |
| :--- | :--- | :--- | :--- | :--- |
| **Plataforma Conversacional** | Dialogflow CX / GCP | Ing. Integración Cloud Jr. | Motor NLP, manejo de intenciones, entidades y rutas de páginas. | Free Tier de GCP / Créditos educativos. |
| **Plataforma Automatización** | n8n Cloud / Self-hosted | Dev Automatización Jr. | Orquestación de flujos, webhook middleware y conexiones HTTP. | Instancia de prueba controlada. |
| **Canal de Mensajería** | Bot Father / Telegram API | Diseñador CX / Ing. Integración | Interfaz conversacional con el ciudadano. | Sandbox con datos simulados. |
| **Almacenamiento Backend** | Google Sheets API | Dev Automatización Jr. | Registro estandarizado de solicitudes e incidencias. | Sin datos personales reales. |
| **Control de Versiones** | GitHub | Líder de Proyecto Jr. | Repositorio centralizado de código, flujos JSON y documentación `/docs`. | Repositorio público/privado con `.gitignore`. |
| **Herramientas de Testing** | cURL / Postman | QA / Documentador Jr. | Validación de payloads JSON y endpoints de fulfillment. | Pruebas de integración asincrónicas. |

---

## 3. Acuerdos de Trabajo Asincrónico
* **Canales de Comunicación:** Discord / WhatsApp para avisos rápidos; GitHub Issues para asignación de tareas.
* **Control de Commits:** Commits descriptivos con prefijos (`feat:`, `docs:`, `fix:`, `test:`).
* **Protección de Datos:** Estrictamente prohibido incluir tokens, llaves privadas o claves API en el código fuente (uso de `.env.example`).
