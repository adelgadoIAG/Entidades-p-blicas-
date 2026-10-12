# Brief: desglose del personal por tipo de puesto

## Qué quiere el usuario
Para cada entidad con presupuesto propio, saber **cuánta gente hace el trabajo propio de la entidad** (científicos, técnicos, inspectores, meteorólogos, evaluadores, etc.) **y cuánta es de administración y apoyo**. También cuántos puestos son de **libre designación**, cuántos **altos cargos** y cuánto **personal eventual (de confianza)**. Ejemplo literal del usuario: "cuántos científicos hay en el CSIC y cuántos son administrativos".

## Columnas nuevas que debes rellenar (claves exactas en `updates`)
- `Desglose: personal técnico/científico/inspector` (número): el núcleo funcional de la entidad.
- `Desglose: personal de administración y apoyo` (número): gestión, administración general, auxiliares, secretaría, servicios generales.
- `Desglose: otro / no clasificable` (número): lo que la fuente no permite asignar (p. ej. personal laboral de oficios sin función indicada, militares en INVIED, personal "otro").
- `Desglose: total de referencia` (número): el total al que suman las tres anteriores. Debe cuadrar (núcleo + administración + otro = total). Si no cuadra, explica por qué.
- `Desglose: unidad y fecha` (texto): qué se cuenta (personas ocupadas / puestos RPT / plazas presupuestadas) y a qué fecha. Ejemplo: "Plazas presupuestadas 2026 (Anexo de Personal)" o "Personas a 31/12/2025 (Memoria 2025)".
- `Desglose: criterio de clasificación` (texto): cómo has repartido. Dos tipos:
  - **Por función**, cuando la entidad publica categorías propias (p. ej. CSIC: personal investigador / personal técnico de apoyo / personal de gestión). Indica qué categorías van a cada columna.
  - **Por grupo o subgrupo profesional como aproximación** (A1+A2 = titulados superiores y medios → núcleo técnico; C1+C2+E/AP = administrativos y auxiliares → administración y apoyo). Dilo explícitamente: "proxy por subgrupo, no por función; parte de los A1/A2 hacen gestión". En Cataluña los grupos son A/B/C/D/E (A+B → núcleo; C+D+E → administración, como proxy).
- `Puestos de libre designación` (número): puestos de la RPT con forma de provisión "LD" (o equivalente autonómico). Fecha de la RPT en la columna de unidad y fecha o en el texto.
- `Altos cargos` (número) y `Personal eventual (confianza)` (número): de la RPT, el anexo de personal del presupuesto o el portal de transparencia.
- `Desglose: fuente` (URL principal) y `Desglose: verificación` (texto: documento, página, fila/tabla, y las cifras literales que has sumado).

Rellena lo que encuentres; no hace falta tenerlo todo. Si solo encuentras altos cargos y eventuales, pon esos. Si solo hay subgrupos de plazas presupuestadas, usa el proxy y dilo.

## Fuentes útiles
- **Anexos de personal de los presupuestos** (dan plazas por grupo/subgrupo, altos cargos, eventuales): Andalucía `juntadeandalucia.es/export/presup2026/personal/personalI-*.pdf` (ya usados en la ronda anterior; mira "Fuente puestos aprobados" de cada fila), Cataluña `aplicacions.economia.gencat.cat/wpres/2026/pdf/AP_<código>.pdf`, País Vasco "Anexo de personal 2026" de euskadi.eus, Galicia "anexo de persoal".
- **Estadística/Boletín del Personal al Servicio de las AAPP (EPSAP enero 2026)**: solo da funcionarios/laborales/otro, no función. Úsala solo como total de referencia si no hay nada mejor.
- **Memorias anuales y planes de acción** de cada agencia (suelen tener un apartado de recursos humanos con distribución por grupos o categorías): CSIC ("CSIC en cifras", memoria), AEMET, AEMPS, ITSS (inspectores y subinspectores frente a personal de apoyo), AESA, CNMC, BOE (Plan de acción 2026), CTBG (Memoria 2025), AIPI (Plan de actuación 2026), AECID, SEPIE.
- **RPT publicadas** en portales de transparencia (Portal de Transparencia de la AGE: RPT por ministerio/organismo; portales autonómicos; datos abiertos de la Junta de Andalucía). Las RPT dan forma de provisión (LD / CM / C) y subgrupo por puesto. Si el PDF es largo y WebFetch lo trunca, cuenta solo si puedes leer la tabla entera; si no, no estimes.

## Reglas
- Solo fuentes oficiales; cada número con documento, página/tabla y cifras literales.
- No estimar, no extrapolar porcentajes de otra entidad, no poner 0 por "no encontrado" (sí 0 si la fuente dice literalmente 0).
- Distingue personas, puestos RPT y plazas presupuestadas; no mezcles fechas distintas en un mismo desglose.
- WebFetch solo abre URLs que hayan salido en resultados de WebSearch. El cupo de WebSearch es compartido entre 6 agentes: **máximo ~30 búsquedas por agente**. Si una URL del BOE con "?id=" devuelve un documento de otro título, descártala (caché contaminada entre agentes).
- PDFs largos: usa el parámetro `offset` de WebFetch; pide en el prompt la cita literal de la tabla.

## Salida
JSON (lista, una entrada por ID de tu lote, aunque no hayas encontrado nada):
```json
[{"ID": 33, "updates": {"Desglose: personal técnico/científico/inspector": 0, "...": "..."}, "verificacion": "...", "no_encontrado": "..."}]
```
Valida que es JSON correcto. Respuesta final: resumen breve (≤12 líneas).
