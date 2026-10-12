# Lote G: Madrid, Murcia, Navarra, PV, Rioja, Valencia

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos autonómicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Tu lote: investigacion/lotes/G_mad_mur_nav_pv_rio_val.json (Madrid 90, 96; Murcia 91, 120; Navarra 92; País Vasco 93, 107, 108, 109; La Rioja 94, 119; Comunitat Valenciana 95, 103, 104, 105, 106). Escribe el resultado en datos/resultados/G_mad_mur_nav_pv_rio_val.json.

Objetivo por entidad: presupuesto propio 2026 (K–R), capítulo 1 crédito 2026 (AL–AP), ejecución de capítulo 1 en 2026 (AQ–AV, corte más reciente publicado), liquidación 2025 de cap.1 (BO–BU) si está publicada, plantilla ocupada (AG–AK) y puestos presupuestados/RPT (AX–BA).

Pistas:
- Confirma primero el estado del presupuesto 2026 de cada CCAA (ley aprobada y número, o prórroga). Si hay prórroga, la cifra es "crédito inicial de prórroga": dilo en N y R.
- 90 Consejo de la Juventud de Madrid y 94 Instituto Riojano de la Juventud están marcados como suprimidos/extinguidos: solo confirma la extinción con fuente; no cuantifiques sustitutos.
- 96 Agencia Madrileña para el Apoyo a las Personas Adultas con Discapacidad (organismo autónomo, gran presupuesto y plantilla): presupuesto CAM 2026 por organismo, cap.1, plantilla presupuestaria.
- 91 ITREM y 120 Agencia Digital de la Región de Murcia: presupuestos CARM 2026 por organismo/ente.
- 92 Oficina de Buenas Prácticas y Anticorrupción de Navarra: la hoja tiene un importe de PROYECTO 2026 en contextual; si la Ley Foral de Presupuestos 2026 se aprobó, sustituye por la cifra aprobada (si la Oficina tiene partida/programa propio claramente suyo) y documéntalo.
- País Vasco: Autoridad Vasca de la Competencia (93, ya tiene presupuesto; falta cap.1/plantilla), Aukerak (107), Agencia Vasca de Ciberseguridad (108, Ciberseguridad Euskadi / sociedad o ente), Euskadiko Kirol Portuak (109, sociedad pública: presupuesto de explotación y capital; gastos de personal de PyG, no cap.1). Presupuestos Generales de la CAE 2026 (euskadi.eus) por entidad.
- 119 ARTE La Rioja.
- Comunitat Valenciana: AVAF (95, depende de Les Corts: su presupuesto propio figura en la sección de Les Corts / aprobado por su órgano; memoria anual con plantilla), AVPT (103), AVSF (104), Agència Valenciana de Residus i Economia Circular (105), Corporación Audiovisual (106, À Punt: sociedad/ente — presupuesto y gastos de personal; plantilla). Presupuestos de la Generalitat 2026 (hisenda.gva.es) y sector público instrumental.

Respeta todo el método del brief (sin estimaciones, sin ceros, millones de EUR, fuente+página para cada cifra). Tu respuesta final: resumen breve (≤15 líneas).
