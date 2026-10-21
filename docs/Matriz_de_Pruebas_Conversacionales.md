# Matriz de Pruebas Conversacionales (Fase 3)
**Proyecto:** Chatbot Asistente en la Nube para Atención Ciudadana (CSDC)  

---

## Resultados del Protocolo de Pruebas (QA Conversacional)

| ID Test | Categoría / Escenario | Entrada del Usuario | Intención Detectada | Resultado Esperado en Respuesta | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Camino Feliz - Antecedentes | "¿Cuánto cuestan los antecedentes penales?" | `consultar_tramite_simplesv` | Informa precio de $3.00 USD y enlace a Simple.sv. | **PASS** |
| **TC-02** | Variación Lenguaje - Policiales | "Quiero mi papel de la policía" | `consultar_tramite_simplesv` | Detecta trámite de solvencia policial ($3.50 USD). | **PASS** |
| **TC-03** | Tolerancia a Tipeo - Registro | "como ago para crear mi cuuenta en login.gob" | `crear_identidad_digital` | Muestra guía de 6 pasos de registro DUI/SMS. | **PASS** |
| **TC-04** | Consulta Gratuita - Apostilla | "¿Es gratis la apostilla de partida de nacimiento?" | `consultar_tramite_simplesv` | Confirma que el apostillado electrónico es $0.00 USD. | **PASS** |
| **TC-05** | Flujo Completo SAC - Webhook | "Quiero reportar un problema en un hospital de San Salvador" | `registrar_denuncia_sac` | Solicita datos, ejecuta webhook y guarda fila en Google Sheets. | **PASS** |
| **TC-06** | Fallback - Fuera de Ámbito | "¿A qué hora juega la selección de fútbol?" | `sys.no-match-default` | Mensaje de fallback orientando a opciones institucionales. | **PASS** |
| **TC-07** | Inyección / Basura | "asdfghjkl 12345" | `sys.no-match-default` | Mantiene estabilidad de sesión y despliega menú principal. | **PASS** |
| **TC-08** | Prueba de Carga Webhook | Petición HTTP POST simultánea (10 req/s) | `registrar_denuncia_sac` | HTTP 200 OK en <500ms; escrituras exitosas en Sheets. | **PASS** |
