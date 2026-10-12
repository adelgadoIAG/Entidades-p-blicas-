# Lote A: entes estatales

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos públicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Tu lote: investigacion/lotes/A_estatal_entes.json (IDs 14, 22, 23, 27, 44, 45, 46, 65, 66, 41, 42, 43). Escribe el resultado en datos/resultados/A_estatal_entes.json.

Objetivo: rellenar presupuesto propio, capítulo 1 (crédito, obligaciones, pagos), plantilla ocupada y puestos para estos entes estatales, con fuentes primarias. Pistas por ID:
- 14 Delegación del Gobierno contra la Violencia de Género: es un centro directivo sin personalidad. Busca el crédito del programa que gestiona (232C, Ministerio de Igualdad) en los PGE vigentes en 2026 (aprobados o prorrogados; verifica cuál) y, si la IGAE/Ministerio de Hacienda publica ejecución por programas, la ejecución. Va en columnas CONTEXTUALES (AA–AD) con base "Programa gestionado por la Delegación; no presupuesto de entidad con personalidad", nunca en K. Personal/RPT de la Delegación si se publica.
- 22 Fundación Pluralismo y Convivencia F.S.P.: busca su presupuesto (PAIF en PGE / presupuestos de fundaciones del sector público estatal), cuentas anuales 2024/2025 (resumen publicado en BOE; "gastos de personal" de la cuenta de resultados — no es cap.1: indícalo en la base), plantilla y retribuciones en su portal de transparencia.
- 23 OIReScon: ya tiene personal 30 y RPT 47 (informe anual 2025). Busca si algún documento oficial (informe anual, PGE servicio/programa del Ministerio de Hacienda, transparencia) da su coste o crédito de personal propio. Si no, documenta.
- 27 AECOSAN (denominación sustituida por AESAN): solo comprueba que la cifra contextual de AESAN (20,371 M) sea coherente con la IGAE 08.2026 y añade, si existe, el cap.1 de AESAN como contexto en BN/BB (NO en AL, que es de la entidad propia).
- 44 Autoridad Independiente para la Igualdad de Trato y la No Discriminación, 45 Agencia Estatal de Evaluación de Políticas Públicas, 46 Agencia Estatal de Salud Pública (AESAP): entes de constitución reciente (estatutos 2026). Comprueba si aparecen con presupuesto propio en la IGAE (ORGANISMOS 07.2026 / 08.2026, bloque "resto de entidades"), en una modificación presupuestaria o en BOE (transferencias de crédito, presupuesto de constitución). Si no, documenta la financiación transitoria del ministerio con el artículo de la norma.
- 65 Centro Nacional de Fotografía: averigua su naturaleza jurídica actual (¿unidad del Ministerio de Cultura, consorcio, fundación?) y si tiene presupuesto/convenio específico identificable.
- 66 SETT (Sociedad Española para la Transformación Tecnológica): sociedad mercantil estatal. Busca presupuestos de explotación y capital en PGE, cuentas anuales 2024/2025 (gastos de personal, plantilla media), y portal de transparencia (plantilla, retribuciones de directivos). Base: "gastos de personal de cuenta de pérdidas y ganancias, no cap.1".
- 41 AESIA, 42 AEAD, 43 A.A.I. Protección del Informante: SOLO las columnas anuales 2025 (BO, BP, BQ, BR, BS, BT, BU) a partir de la IGAE edición 12.2025 (ORGANISMOS 12. 2025) si estas entidades aparecen ahí; las filas existentes (p. ej. ID3 en ejemplos.json) muestran el estilo exacto. Si no aparecen en 2025, documéntalo en BU/BN. No toques plantilla de 41–43 (lo hace otro lote).

Respeta todo el método del brief (sin estimaciones, sin ceros, millones de EUR, fuente+página para cada cifra). Tu respuesta final: resumen breve (≤15 líneas).
