# Documento de Análisis y Casos de Uso (Fase 1)
**Proyecto:** Chatbot Asistente en la Nube para Atención Ciudadana (CSDC)  

---

## 1. Contexto Institucional y Problemática Detectada
El **Centro de Servicios Digitales Ciudadanos (CSDC)** opera como primer punto de contacto entre la población y las instituciones públicas de El Salvador. 
Actualmente, la atención se realiza de forma manual mediante agentes humanos, generando:
1. **Tiempos de respuesta elevados:** Colas de mensajes en horas pico.
2. **Sobrecarga del personal:** Redundancia al responder preguntas frecuentes (FAQ) repetitivas sobre trámites en **Simple.sv**, **Identidad Digital** o **SAC**.
3. **Falta de trazabilidad:** Dificultad para construir estadísticas consolidadas sobre las inquietudes ciudadanas.

---

## 2. Definición de Usuarios Finales
* **Ciudadano General:** Requiere información rápida 24/7 sobre trámites en Simple.sv (costos, requisitos, tiempos).
* **Diáspora Salvadoreña:** Consulta sobre pasaportes en el exterior y apostillado de partidas de nacimiento.
* **Estudiante / Profesional:** Interesado en capacitaciones continuas gratuitas de la ESIT.
* **Usuario Interno CSDC:** Recibe solicitudes estandarizadas y registradas en Google Sheets.

---

## 3. Matriz de Casos de Uso Prioritarios

| ID Caso de Uso | Nombre del Caso de Uso | Actor Principal | Descripción Breve | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **CU-01** | Consultar Requisitos y Costos de Trámites | Ciudadano / Diáspora | Obtener información inmediata de antecedentes penales, policiales, pasaporte y apostilla. | Respuesta clara con montos en USD y enlace a Simple.sv. |
| **CU-02** | Guía de Registro de Identidad Digital | Ciudadano | Recibir la guía paso a paso para crear cuenta en `login.gob.sv` / Simple.sv. | Instrucciones de los 6 pasos con verificación DUI/SMS. |
| **CU-03** | Registro de Incidencia / Denuncia SAC | Ciudadano | Capturar datos del sector (Salud/Educación), departamento, institución y descripción. | Fila agregada en Google Sheets y confirmación al usuario. |
| **CU-04** | Consulta de Oferta Académica ESIT | Estudiante / Servidor | Informar sobre diplomados y cursos asincrónicos gratuitos de la ESIT. | Catálogo de cursos (Scrum, MySQL, Gobernanza) y link. |
| **CU-05** | Canal de Soporte Humano | Ciudadano | Proporcionar correos y números telefónicos de atención oficial. | Directorio de contacto (`contacto@simple.sv`, WhatsApp SAC). |
