# R2E: CLM, CyL, Cat, Ext, Gal, Mad, Mur, PV, Val

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos autonómicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Segunda ronda. Tu lote: investigacion/lotes/R2E_clm_cyl_cat_ext_gal_mad_mur_pv_val.json (CLM 117, 118; CyL 85; Extremadura 88, 122; Cataluña 86, 87, 110; Galicia 89, 121; Madrid 96; Murcia 91, 120; Comunitat Valenciana 95, 103, 104, 105, 106; País Vasco 107, 108, 109). Cada fila trae su estado actual (ya incluye ronda 1) y en '_pendiente_ronda1' lo que faltó. Las rondas 1 están en datos/resultados/F_clm_cyl_cat_ext_gal.json y G_mad_mur_nav_pv_rio_val.json (URLs que funcionaron). Escribe el resultado en datos/resultados/R2E_varias.json.

Presupuesto de búsquedas: máximo ~40 WebSearch (cupo compartido con otros 4 agentes). WebFetch solo abre URLs que hayan salido en resultados de WebSearch. Si un PDF se trunca, usa el parámetro offset de WebFetch.

Prioridades (capítulo 1 / gastos de personal y presupuesto propio son lo más valioso):
1. CLM 117 (Agencia de Investigación e Innovación) y 118 (Agencia de Transformación Digital, sección 77): crédito 2026 total y cap.1 (presupuestos JCCM 2026: "resumen por secciones/organismos", "estado de gastos", tomos en castillalamancha.es/hacienda).
2. País Vasco 107, 108, 109: gastos de personal 2026 de sus presupuestos de explotación (documentos de presupuestos 2026 de euskadi.eus por sección; usa offset para llegar a las páginas del ente).
3. Comunitat Valenciana 103, 104 (cap.1 OOAA, libros de presupuestos 2026 en hisenda.gva.es), 106 À Punt (gastos de personal y plantilla en presupuesto/cuentas), 95 AVAF (memoria 2025: plantilla y ejecución).
4. Madrid 96 AMAPAD y Murcia 91 ITREM: gastos de personal 2026 en presupuesto de explotación / contrato-programa.
5. Cataluña 86 ATC y 87 Antifrau: plantilla ocupada (memorias 2025); Galicia 89 GAIN y 121 AGACAL: prazas orzamentadas (anexo de persoal 2026).
6. Regla 6 para 85 (CyL, Decreto 8/2006 / 52/2014) y 88 (Extremadura, Decreto 28/2007); 122 AGENEX: naturaleza y titularidad (¿Diputación de Badajoz?) y presupuesto/PyG.

Respeta el método del brief (sin estimaciones, millones de EUR, fuente+página). Tu respuesta final: resumen breve (≤12 líneas).
