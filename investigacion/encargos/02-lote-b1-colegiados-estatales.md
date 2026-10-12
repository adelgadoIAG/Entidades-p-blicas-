# Lote B1: colegiados estatales

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos públicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Tu lote: investigacion/lotes/B1_estatal_colegiados.json (IDs 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 29). Escribe el resultado en datos/resultados/B1_estatal_colegiados.json.

Son observatorios y consejos estatales (órganos colegiados o unidades sin personalidad jurídica). Para cada uno:
1. Lee la norma de creación/regulación vigente (BOE; consolidada si existe) y localiza los artículos/disposiciones sobre gasto ("no supondrá incremento del gasto público", "medios personales y materiales del Ministerio X", "los miembros no percibirán retribución / indemnizaciones por razón del servicio", secretaría a cargo de una DG concreta). Cita artículo y URL. Si se verifica, usa Estado de cuantificación = "Sin presupuesto propio: órgano sin dotación diferenciada (verificado en norma)" y rellena coherentemente "Presupuesto: texto completo", "Cobertura presupuesto / personal / salarios", "Notas de personal y apoyo ministerial", "Estado de verificación del personal", "Estado de verificación del coste", "Estado de verificación de ejecución" (indicando que el coste lo absorbe la unidad X y que no se prorratea).
2. Busca si existe financiación específica e identificable a su nombre (convenio publicado en BOE, encargo a medio propio, contrato en la Plataforma de Contratación del Sector Público, subvención nominativa en PGE, línea presupuestaria con su nombre). Ejemplos plausibles: Observatorio Estatal de la Discapacidad (convenio Real Patronato sobre Discapacidad), Observatorio de la Lectura y el Libro, Observatorio de la Nutrición (AESAN), Observatorio Estatal de Violencia sobre la Mujer, Observatorio de la Cadena Alimentaria. Si hay importe, ponlo en las columnas contextuales AA–AD (importe en millones EUR, periodo, base tipo "Convenio 2025; NO presupuesto del órgano", titular), con fuente.
3. Si el órgano tiene personal asignado publicado (p. ej. una subdirección o unidad de apoyo con nº de efectivos en una memoria oficial), rellena AG–AK o BB; los vocales nunca son plantilla.
4. Si el órgano ha sido suprimido, integrado o está inactivo (sin reuniones/informes recientes), indícalo en "Presupuesto: texto completo" o BB con fuente, sin tocar las columnas de mandato.

Respeta todo el método del brief (sin estimaciones, sin ceros, millones de EUR, fuente para cada cifra). Eficiencia: 2–4 búsquedas por órgano. Tu respuesta final: resumen breve (≤15 líneas).
