# Lote F: CLM, CyL, Cataluña, Extremadura, Galicia

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos autonómicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Tu lote: investigacion/lotes/F_clm_cyl_cat_ext_gal.json (Castilla-La Mancha 84, 117, 118; Castilla y León 85; Cataluña 86, 87, 102, 110; Extremadura 88, 122; Galicia 89, 121). Escribe el resultado en datos/resultados/F_clm_cyl_cat_ext_gal.json.

Objetivo por entidad: presupuesto propio 2026 (K–R), capítulo 1 crédito 2026 (AL–AP), ejecución de capítulo 1 en 2026 (AQ–AV, corte más reciente publicado), liquidación 2025 de cap.1 (BO–BU) si está publicada, plantilla ocupada (AG–AK) y puestos presupuestados/RPT (AX–BA).

Pistas:
- Confirma primero el estado del presupuesto 2026 de cada CCAA (ley aprobada y número, o prórroga del anterior: Cataluña lleva varios ejercicios con prórrogas/ley tardía; compruébalo). Si hay prórroga, la cifra es "crédito inicial de prórroga": dilo en N y R.
- Cataluña: Agència Tributària de Catalunya (86, ya tiene presupuesto; falta cap.1, ejecución y plantilla), Agència de la Natura de Catalunya (102), Agència de Ciberseguretat de Catalunya (110, entidad de derecho público con presupuesto propio en los pressupostos de la Generalitat / sector públic), Oficina Antifrau de Catalunya (87: depende del Parlament; su presupuesto figura en la sección del Parlament o en su propio presupuesto aprobado; tiene memoria anual con plantilla). Fuentes: economia.gencat.cat (pressupostos, execució pressupostària, Compte General), portals de transparència.
- Castilla-La Mancha: Agencia del Agua (84), Agencia de Investigación e Innovación (117, OA), Agencia de Transformación Digital (118). Presupuestos JCCM 2026 por organismo/sección y anexo de personal.
- Castilla y León 85 y Extremadura 88 (Observatorios para la Convivencia Escolar): órganos colegiados — aplica la regla 6 del brief.
- Extremadura 122 AGENEX: ¿es realmente EPE de la Junta o agencia de la Diputación de Badajoz / asociación? Verifica naturaleza y titularidad antes de cuantificar; presupuesto y cuentas (gastos de personal de PyG; no cap.1).
- Galicia: GAIN (89, ya tiene presupuesto; falta cap.1/ejecución/plantilla) y AGACAL (121). Presupuestos Xunta 2026 por organismo/entidad, anexo de persoal, Conta Xeral 2025.

Respeta todo el método del brief (sin estimaciones, sin ceros, millones de EUR, fuente+página para cada cifra). Tu respuesta final: resumen breve (≤15 líneas).
