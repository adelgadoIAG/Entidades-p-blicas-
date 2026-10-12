# Lote E: Asturias, Baleares, Canarias, Cantabria

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos autonómicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Tu lote: investigacion/lotes/E_ast_bal_can_cant.json (Asturias 79, 112, 113; Illes Balears 80, 111, 124, 125; Canarias 81; Cantabria 82, 83, 114, 115, 116, 123). Escribe el resultado en datos/resultados/E_ast_bal_can_cant.json.

Objetivo por entidad: presupuesto propio 2026 (K–R), capítulo 1 crédito 2026 (AL–AP), ejecución de capítulo 1 en 2026 (AQ–AV, con el corte más reciente publicado), liquidación 2025 de cap.1 (BO–BU) si está publicada, plantilla ocupada (AG–AK) y puestos presupuestados/RPT (AX–BA).

Pistas:
- Primero confirma el estado del presupuesto 2026 de cada CCAA (ley aprobada y número, o prórroga) — p. ej. Cantabria: la hoja tiene ICASS (82) y Oficina... con importes de PROYECTO 2026 en columnas contextuales; si la ley se aprobó, pasa la cifra aprobada a K y deja constancia.
- Organismos autónomos y entes con sección/servicio propio: SEPA (79), SCEI/Sekuens (112), ICASS (82), ICASST (83), SEMCA (114), ICAP (116), ATIB (80), ASPIB (111), ABDigital (124), IBE (125, hoy solo 2025), ATC (81). Busca en los presupuestos generales de cada CCAA (estados de gastos por organismo, resumen por capítulos, anexo de personal/plantilla presupuestaria). Las intervenciones generales publican ejecución mensual/trimestral y la Cuenta General 2025.
- Consejo de Transparencia de Asturias (113), Consejo de la Juventud de Cantabria (115), Observatorio de Igualdad de Género de Cantabria (123): verifica si tienen dotación propia (sección, subvención nominativa, transferencia con su nombre) o aplica la regla 6 del brief.
- Entes empresariales (si alguno es EPE o sociedad): presupuesto de explotación y capital; "gastos de personal" de PyG (indica que no es cap.1).
- Plantilla: memorias anuales, portales de transparencia (Asturias "Transparencia", CAIB "Portal de transparència", Gobierno de Canarias "Transparencia" con RPT), anexos de personal del presupuesto.

Respeta todo el método del brief (sin estimaciones, sin ceros, millones de EUR, fuente+página para cada cifra). Tu respuesta final: resumen breve (≤15 líneas).
