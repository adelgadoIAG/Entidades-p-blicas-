# Lote D: Andalucía y Aragón

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos autonómicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json (ID99 es una fila autonómica andaluza bien hecha).

Tu lote: investigacion/lotes/D_andalucia_aragon.json (IDs 73, 74, 75, 76, 77, 97, 98, 99, 100, 101 de Andalucía y 78 de Aragón). Escribe el resultado en datos/resultados/D_andalucia_aragon.json.

Objetivo por entidad: presupuesto propio 2026 (K–R), capítulo 1 crédito 2026 (AL–AP), ejecución de capítulo 1 en 2026 (AQ–AV, con el corte más reciente publicado), liquidación 2025 de cap.1 (BO–BU) si está publicada, plantilla ocupada (AG–AK) y puestos presupuestados (AX–BA).

Pistas:
- Andalucía: Presupuesto 2026 = Ley 8/2025 (ya citada). Los documentos por sección/programa están en juntadeandalucia.es/export/presup2026/... (estados III-a, III-b, etc. con "personas presupuestadas" y capítulo 1 por sección de agencia). Las agencias administrativas y de régimen especial tienen sección propia (p. ej. 10.39 ATA, 15.31 ACCUA, 13.32 ISA, 01.39 Emergencias). La Intervención General de la Junta publica ejecución presupuestaria mensual/trimestral (informes de ejecución, "Cuenta General", "Información económico-financiera"), a veces por sección: busca el capítulo 1 ejecutado de cada sección de agencia en 2026 y la liquidación 2025 (Cuenta General 2025 o liquidación del presupuesto 2025).
- 73 AACID y 97 ADA tienen presupuesto pero no cap.1: búscalo en sus estados de gastos/PAIF. 74 Agencia de Defensa de la Competencia de Andalucía y 76 Consejo de Transparencia y Protección de Datos de Andalucía: verifica si tienen sección/servicio propio en la Ley 8/2025 (el Consejo de Transparencia suele tener sección propia). 77 Observatorio Territorial: órgano colegiado (aplica regla 6 del brief). 98 TRADE (agencia pública empresarial): presupuesto de explotación y capital (PEC/PAIF) en la Ley 8/2025 o documentación anexa; "gastos de personal" del PEC (indica base: no cap.1). 101 Agencia de Emergencias de Andalucía: hoy solo hay cap.1 de un programa; busca el total de la agencia.
- 78 ACPUA (Aragón): verifica la situación presupuestaria de Aragón en 2026 (ley aprobada o prórroga) y localiza la sección/organismo de ACPUA (entidad de derecho público) en el presupuesto, con cap.1 y plantilla; memoria anual de ACPUA para personal.

Respeta todo el método del brief (sin estimaciones, sin ceros, millones de EUR, fuente+página para cada cifra; "personas presupuestadas" ≠ ocupadas). Tu respuesta final: resumen breve (≤15 líneas).
