# CSIC y CNMC: en qué se gasta

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos públicos españoles. El usuario pregunta, para el CSIC y la CNMC: "¿en qué se usa ese dinero? ¿cuánto es personal y cuánto actividades?". Necesito el desglose de su presupuesto 2026 por capítulos económicos y, para las partidas grandes, a qué se destinan.

Datos ya conocidos (IGAE, ejecución a 31/08/2026, crédito total actualizado):
- CNMC: crédito total 4.846,353 M€ (inicial 3.686,434 + modificaciones 1.159,919). Capítulo 1 personal 47,618 M; capítulo 2 bienes y servicios 25,567 M; transferencias de capital 4.656,642 M. Hay que averiguar **a quién van esas transferencias de capital** (hipótesis a comprobar, no a dar por buena: fondos que la CNMC canaliza hacia el sistema eléctrico o gasista por mandato legal, p. ej. por la Ley 15/2012 o la Ley 24/2013, y que no son coste de funcionamiento de la CNMC). Busca la norma o el documento presupuestario que lo explique (memoria de programas de los PGE, presupuesto de la CNMC en su portal de transparencia, informe de ejecución trimestral de la CNMC, cuentas anuales).
- CSIC: crédito total 1.543,754 M€ (inicial 1.213,105); capítulo 1 personal 614,97 M. Falta el resto: capítulo 2 (bienes y servicios), 4 y 7 (transferencias), 6 (inversiones reales, que en el CSIC suelen ser proyectos de investigación e infraestructuras), 8 y 9. Fuentes: tomos de los PGE (sepg.pap.hacienda.gob.es, presupuesto de agencias estatales, por capítulos; recuerda que 2026 funciona con los PGE 2023 prorrogados), el presupuesto del CSIC en su portal de transparencia, sus cuentas anuales o la IGAE.

Devuelve en datos/resultados/gasto_csic_cnmc.json una lista con una entrada por entidad: {"ID": 33 o 24, "entidad", "anio", "base" (crédito inicial / actualizado / obligaciones, y fecha), "capitulos": [{"capitulo": "1 Gastos de personal", "importe_m": ..., "destino": "frase corta"}, ...], "total_m", "fuente", "verificacion" (documento, página, cifras literales, unidad), "explicacion_transferencias" (para la CNMC)}. Solo fuentes oficiales; no estimes; millones de EUR.

Presupuesto de búsquedas MUY limitado: máximo 12 WebSearch. WebFetch solo abre URLs que hayan salido en resultados de búsqueda (las URL del BOE en formato ELI, boe.es/eli/..., suelen abrirse directamente). PDFs largos: usa el parámetro offset. Respuesta final: resumen breve (≤10 líneas) con el reparto de cada una.
