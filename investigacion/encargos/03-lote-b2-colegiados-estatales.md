# Lote B2: colegiados estatales

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos públicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Tu lote: investigacion/lotes/B2_estatal_colegiados.json (IDs 47–64, 67, 68, 69). Escribe el resultado en datos/resultados/B2_estatal_colegiados.json.

Son observatorios, consejos, mesas, oficinas técnicas, comisiones interministeriales y plataformas estatales (en su mayoría sin personalidad jurídica). Para cada uno:
1. Lee la norma de creación/regulación vigente (BOE; consolidada si existe) y localiza los artículos/disposiciones sobre gasto ("no supondrá incremento del gasto público", "medios personales y materiales del Ministerio X", "los miembros no percibirán retribución / indemnizaciones", secretaría a cargo de una DG concreta). Cita artículo y URL. Si se verifica, usa Estado de cuantificación = "Sin presupuesto propio: órgano sin dotación diferenciada (verificado en norma)" y rellena coherentemente "Presupuesto: texto completo", "Cobertura presupuesto / personal / salarios", "Notas de personal y apoyo ministerial", "Estado de verificación del personal", "Estado de verificación del coste", "Estado de verificación de ejecución" (indicando qué unidad absorbe el coste, sin prorratear).
2. Busca financiación específica e identificable a su nombre (convenio en BOE, encargo a medio propio, contrato en la Plataforma de Contratación del Sector Público, subvención nominativa, línea presupuestaria con su nombre). Ya hay contextuales en 59 (convenio 2021–2025) y 60 (programa Red.es): revísalos y mejóralos solo si encuentras fuente primaria mejor. Ejemplos plausibles: Comisión Interministerial del Trío de Eclipses (puede tener crédito/programa de acontecimiento de excepcional interés público), Observatorio Global del Español (Instituto Cervantes), Oficina Técnica de Desertificación, Observatorio de Gobierno Abierto. Importe en columnas contextuales AA–AD (millones EUR, periodo, base tipo "Convenio 2025; NO presupuesto del órgano", titular), con fuente.
3. Si el órgano tiene personal asignado publicado (nº de efectivos de una unidad de apoyo en memoria oficial), rellena AG–AK o BB; los vocales nunca son plantilla.
4. Si el órgano ha sido suprimido, integrado o está inactivo, indícalo con fuente en "Presupuesto: texto completo" o BB, sin tocar columnas de mandato.

Respeta todo el método del brief (sin estimaciones, sin ceros, millones de EUR, fuente para cada cifra). Eficiencia: 2–4 búsquedas por órgano. Tu respuesta final: resumen breve (≤15 líneas).
