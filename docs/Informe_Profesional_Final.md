# Informe Profesional Final (Fase 4)
**Proyecto:** Chatbot Asistente en la Nube para Atención Ciudadana (Prototipo Lite)  
**Cliente:** Centro de Servicios Digitales Ciudadanos (CSDC)  
**Institución:** Escuela Superior de Innovación y Tecnología (ESIT)  

---

## 1. Resumen Ejecutivo
El presente informe documenta el desarrollo, pruebas y despliegue del prototipo de **Chatbot Asistente en la Nube** orientado a la atención automatizada de la ciudadanía salvadoreña. En el marco de la Estancia Profesional de 10 semanas de la ESIT, se construyó una solución conversacional basada en **Dialogflow CX / * e integrada con **Google Sheets** mediante un backend webhook en Python.

---

## 2. Objetivos Alcanzados
1. **Automatización de FAQ (24/7):** Resolución inmediata sobre costos y requisitos de más de 90 trámites en Simple.sv, pasaportes y certificados.
2. **Estandarización de Registros:** Captura estructurada de solicitudes para el Sistema de Atención Ciudadana (SAC).
3. **Despliegue Multi-Canal:** Soporte para interacción vía Bot de Telegram y widget web.
4. **Documentación Completa:** Publicación de especificaciones de arquitectura, flujos JSON y bitácoras de trabajo en GitHub.

---

## 3. Demostración del Flujo Operativo
* **Paso 1:** El ciudadano inicia conversación en Telegram/Web y recibe menú principal.
* **Paso 2:** Selecciona la consulta de un trámite o el registro de una incidencia SAC.
* **Paso 3:** En caso de denuncia SAC, la plataforma recopila parámetros (nombre, correo, teléfono, sector).
* **Paso 4:** El webhook procesa los parámetros en milisegundos y almacena la información en la hoja de cálculo institucional de Google Sheets.

---

## 4. Limitaciones Actuales y Recomendaciones Futuras
* **Limitación:** El prototipo no consulta directamente APIs de bases de datos gubernamentales en tiempo real para verificar el estado interno de expedientes institucionales.
* **Recomendación Futura:** Integrar autenticación OAuth2 directa con la plataforma de Identidad Digital (`login.gob.sv`) para autenticación avanzada y habilitar módulos de inteligencia artificial generativa (Vertex AI / Gemini) para manejar consultas complejas no estructuradas.
