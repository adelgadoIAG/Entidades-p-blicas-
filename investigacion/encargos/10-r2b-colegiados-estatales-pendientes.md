# R2B: colegiados estatales pendientes

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos públicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Segunda ronda. Tu lote: investigacion/lotes/R2B_colegiados.json (IDs 55, 56, 59, 60, 64, 67, 68, 69). Cada fila trae su estado actual y en '_pendiente_ronda1' lo que faltó. Escribe el resultado en datos/resultados/R2B_colegiados.json.

Presupuesto de búsquedas: máximo ~30 WebSearch (cupo compartido con otros 4 agentes). WebFetch solo abre URLs que hayan salido en resultados de WebSearch; si una consulta al BOE con "?id=" devuelve un documento con otro título, descártalo (contaminación de caché entre agentes): comprueba siempre el título. Prefiere URLs ELI (boe.es/eli/...) o PDF (boe.es/boe/dias/...).

Para cada órgano (regla 6 del brief): localiza en su norma de creación vigente la cláusula de gasto ("no supondrá incremento del gasto público", "medios personales y materiales del Ministerio X", retribución/indemnizaciones de miembros), cita artículo y URL, y si se verifica usa Estado de cuantificación = "Sin presupuesto propio: órgano sin dotación diferenciada (verificado en norma)" y rellena coherentemente "Presupuesto: texto completo", "Cobertura presupuesto / personal / salarios", "Notas de personal y apoyo ministerial", "Estado de verificación del personal", "Estado de verificación del coste", "Estado de verificación de ejecución" (qué unidad absorbe el coste, sin prorratear). Usa como modelo el estilo de la ronda 1 ya aplicado a órganos similares (p. ej. lee datos/resultados/B2_estatal_colegiados.json, entrada ID 54, para copiar el formato).
Además, busca financiación específica identificable: 68 Comisión Interministerial del Trío de Eclipses (¿acontecimiento de excepcional interés público con beneficios fiscales? ¿crédito o programa?), 59 y 60 (revisar contextuales existentes: convenio del Observatorio de Digitalización Agroalimentaria y programa de Red.es — mejorar solo con fuente primaria), 67 Oficina Técnica de Desertificación, 69 Plataforma Nacional para la Reducción del Riesgo de Desastres, 55 Observatorio de Márgenes Empresariales, 56 Observatorio contra el Fraude y la Corrupción Sanitaria, 64 Consejo Nacional de Seguridad Aeroespacial. Importes en columnas contextuales AA–AD, nunca en K.

Tu respuesta final: resumen breve (≤12 líneas).
