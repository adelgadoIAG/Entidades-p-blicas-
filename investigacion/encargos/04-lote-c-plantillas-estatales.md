# Lote C: plantillas estatales

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de empleo público español. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json (fíjate en ID36, que tiene plantilla ocupada y RPT bien documentadas).

Tu lote: investigacion/lotes/C_estatal_plantillas.json (IDs 2, 3, 4, 5, 6, 7, 28, 30, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43). Escribe el resultado en datos/resultados/C_estatal_plantillas.json.

Estas entidades estatales ya tienen presupuesto y capítulo 1 verificados con IGAE. Tu trabajo es SOLO la plantilla: 
- "Personal: personas (ocupadas)" (AG), "Año del personal" (AH, año o fecha AAAA-MM-DD), "Base del personal" (AI: qué se cuenta y desglose funcionarios/laborales/otros si lo hay), "Estado de verificación del personal" (AJ), "Fuente del personal" (AK).
- "Puestos aprobados / presupuestados" (AX: RPT o plantilla presupuestaria), "Fecha puestos aprobados" (AY), "Base de puestos aprobados" (AZ), "Fuente puestos aprobados" (BA).
- "Notas de personal y apoyo ministerial" (BB) si aporta (p. ej. cobertura % = ocupados/RPT, solo si ambas cifras son de la misma fecha y fuente).
- "Cobertura presupuesto / personal / salarios" (AW): actualízala si añades plantilla (p. ej. "Crédito y gasto de personal individual verificados; plantilla ocupada verificada a <fecha>").

Fuentes preferentes: portal de transparencia de cada agencia (sección "información organizativa / plantilla / RPT / número de efectivos"), memorias anuales oficiales (CSIC, AEMET, AEMPS, BOE, AIReF, CTBG, AESA, AESF, ITSS — informe anual de la ITSS da efectivos de inspectores y subinspectores, pero el organismo OEITSS incluye más personal: precisa la base), cuentas anuales en BOE (memoria con número medio de empleados), Plan de actuación/contrato de gestión, Portal de Transparencia de la AGE (RPT), y el Boletín Estadístico del Personal al Servicio de las Administraciones Públicas (BEP) si desglosa por organismo. Prioriza el dato más reciente (2025–2026); fecha exacta obligatoria. No mezcles "número medio" con "efectivos a fecha": indícalo en la base.

Respeta todo el método del brief (sin estimaciones; si una fuente da solo personal de una parte del organismo, dilo en la base). Eficiencia: 2–4 búsquedas por entidad. Tu respuesta final: resumen breve (≤15 líneas).
