# Catálogo de Intenciones y Respuestas (Fase 1 y 2)
**Proyecto:** Chatbot Asistente en la Nube para Atención Ciudadana (CSDC)  

---

## 1. Intent: `welcome_intent`
* **Descripción:** Saludo inicial y presentación del menú principal.
* **Frases de Entrenamiento (*Training Phrases*):**
  * "Hola", "Buenas tardes", "Inicio", "Necesito ayuda con trámites", "¿Qué consultas puedo hacer?"
* **Respuesta Base:**
  > "¡Hola! 👋 Bienvenido al Asistente Virtual del Centro de Servicios Digitales Ciudadanos (CSDC). Estoy para orientarte las 24/7.\n\nPor favor, selecciona o escribe la opción que necesitas:\n1. 📄 Consultar Trámites en Simple.sv\n2. 🆔 Crear Identidad Digital / Login.gob.sv\n3. 📝 Registrar Caso o Denuncia (SAC)\n4. 🎓 Cursos Gratuitos de la ESIT\n5. 📞 Soporte y Atención Humana"

---

## 2. Intent: `consultar_tramite_simplesv`
* **Entidades Extraídas:** `$tipo_tramite` (penales, policiales, pasaporte, apostilla, DUI).
* **Frases de Entrenamiento:**
  * "¿Cuánto valen los antecedentes penales?"
  * "Requisitos para solvencia de la policía"
  * "Precio del pasaporte en Centroamérica y Estados Unidos"
  * "¿Cómo apostillar una partida de nacimiento?"
* **Respuestas Mapeadas:**
  * **Antecedentes Penales:** Costo $3.00 USD en Simple.sv.
  * **Antecedentes Policiales:** Costo $3.50 USD en Simple.sv.
  * **Pasaporte Exterior:** $40.00 USD Centroamérica; $60.00 USD resto del mundo.
  * **Apostilla Electrónica / DUI:** Trámites 100% gratuitos en línea.

---

## 3. Intent: `crear_identidad_digital`
* **Frases de Entrenamiento:**
  * "¿Cómo creo mi perfil digital?"
  * "Pasos para registrar mi cuenta en login.gob.sv"
  * "No me llega el código SMS para mi Identidad Digital"
* **Respuesta Base:**
  > "Para crear tu Identidad Digital:\n1. Ingresa a simple.sv o login.gob.sv y haz clic en 'Crear cuenta'.\n2. Digita tu número de DUI y acepta términos.\n3. Ingresa el número de folio de tu DUI.\n4. Verifica tu correo electrónico con el código enviado.\n5. Verifica tu número telefónico vía SMS.\n6. Asigna tu contraseña segura."

---

## 4. Intent: `registrar_denuncia_sac`
* **Parámetros Requeridos:** `$nombre_ciudadano`, `$correo_contacto`, `$telefono_contacto`, `$sector`, `$detalle_caso`.
* **Frases de Entrenamiento:**
  * "Quiero poner un reclamo sobre un centro de salud"
  * "Denuncia anónima en el SAC para educación"
  * "Registrar solicitud de información pública"
* **Acción Fulfillment:** Ejecuta Webhook Backend para guardar los datos en Google Sheets.

---

## 5. Intent: `sys.no-match-default` (Fallback)
* **Respuesta Base:**
  > "Disculpa, no logré comprender tu consulta. Por favor, intenta redactar tu pregunta de forma distinta o selecciona una de nuestras opciones principales: Trámites Simple.sv, Identidad Digital, SAC o Cursos ESIT."
