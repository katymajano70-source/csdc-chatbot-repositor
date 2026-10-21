# Bitácora de Trabajo Semanal (Semanas 1 a 10)
**Proyecto:** Chatbot Asistente en la Nube para Atención Ciudadana (CSDC)  

---

## Control Semanal de Actividades (Plan de 10 Semanas)

### Semana 1 - Fase 0: Onboarding y Planificación
* **Actividades:** Lectura del requerimiento institucional del CSDC, constitución de la célula conversacional, asignación de roles y elaboración del Plan de Recursos Tecnológicos.
* **Entregables:** `Plan_de_Recursos_Tecnologicos.md` y estructura de repositorio GitHub creada.

### Semanas 2 y 3 - Fase 1: Análisis y Definición de Contenido
* **Actividades:** Levantamiento de casos de uso prioritarios (Simple.sv, Identidad Digital, SAC, ESIT). Redacción de las frases de entrenamiento y respuestas institucionales.
* **Entregables:** `Documento_de_Analisis_Casos_de_Uso.md` y `Catalogo_de_Intenciones_y_Respuestas.md`.

### Semanas 4 y 5 - Fase 2: Diseño y Configuración Base
* **Actividades:** Elaboración de diagramas de flujo conversacional y diseño de arquitectura cloud. Configuración inicial del agente en Dialogflow CX y exportación del borrador JSON.
* **Entregables:** `Documento_de_Diseno_y_Arquitectura.md` y `flows/dialogflow_cx_agent.json`.

### Semanas 6, 7 y 8 - Fase 3: Implementación, Webhooks y Pruebas
* **Actividades:** Desarrollo del webhook backend en Python (`src/main.py`), conexión con Google Sheets API y ejecución de la matriz de pruebas conversacionales (QA).
* **Entregables:** `src/main.py`, `flows/n8n_workflow_csdc.json` y `Matriz_de_Pruebas_Conversacionales.md`.

### Semanas 9 y 10 - Fase 4: Cierre Técnico y Entrega Profesional
* **Actividades:** Redacción del informe final, revisión de limitaciones y empaquetado del repositorio completo para entrega institucional y publicación en GitHub.
* **Entregables:** `Informe_Profesional_Final.md` y `README.md` principal.
