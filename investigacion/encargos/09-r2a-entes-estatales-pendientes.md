# R2A: entes estatales pendientes

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos públicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Segunda ronda. Tu lote: investigacion/lotes/R2A_estatal.json (IDs 14, 22, 23, 44, 45, 46, 65, 66, 42, 5). Cada fila incluye su estado actual y en '_pendiente_ronda1' lo que la primera ronda no logró. Escribe el resultado en datos/resultados/R2A_estatal.json.

Presupuesto de búsquedas: máximo ~35 WebSearch en total (el cupo es compartido con otros 4 agentes). Prioriza por valor. WebFetch solo abre URLs que hayan salido en resultados de WebSearch; si una consulta al BOE con "?id=" devuelve un documento con otro título, descártalo (hay contaminación de caché entre agentes): comprueba siempre el título.

Prioridades:
1. 66 SETT: cuentas anuales 2024/2025 (gastos de personal, plantilla media) — busca "SETT cuentas anuales 2025" / "Sociedad Española para la Transformación Tecnológica plantilla" / portal de transparencia SETT; base: "gastos de personal de la cuenta de pérdidas y ganancias, no cap.1".
2. 22 Fundación Pluralismo y Convivencia: portal de transparencia (presupuesto 2026, cuentas 2025, plantilla, retribuciones); BOE resumen de cuentas anuales.
3. 14 Delegación del Gobierno contra la Violencia de Género: crédito del programa 232C (columnas contextuales, nunca K) en los PGE vigentes 2026 — averigua si son prorrogados (PGE 2023 prorrogados) o aprobados. Personal de la Delegación si se publica.
4. 42 AEAD: columnas anuales 2025 (BO–BU) desde IGAE edición 12.2025 ("ORGANISMOS 12. 2025", bloque de gastos por capítulos de agencias estatales / resto de entidades). Si el PDF se trunca antes de las tablas, usa el parámetro offset de WebFetch (las tablas de gastos por capítulos de "resto de entidades" están hacia las págs. 99–119; prueba offsets grandes, p. ej. 150000, 200000, 250000).
5. 44, 45, 46 (Autoridad Igualdad de Trato, Agencia Estatal de Evaluación de Políticas Públicas, AESAP): comprueba si aparecen en IGAE ORGANISMOS 08.2026 (mismo truco de offset); si no, documenta con el artículo de su estatuto la financiación transitoria del ministerio.
6. 23 OIReScon (coste propio si algún informe lo da), 65 Centro Nacional de Fotografía (naturaleza jurídica actual y financiación identificable), 5 AIReF (personas ocupadas: memoria 2025 o RPT; la web airef.es puede bloquear lectura automática — busca el PDF de la memoria).

Respeta el método del brief (sin estimaciones, sin ceros por "no encontrado", millones de EUR, fuente+página). Tu respuesta final: resumen breve (≤12 líneas).
