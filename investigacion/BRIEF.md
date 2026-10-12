# Brief común: completar huecos de "Entidades públicas: poder y presupuesto" (Hoja 1)

## Contexto
Hoja de cálculo de 125 entidades públicas españolas (estatales y autonómicas) creadas desde 2006: mandato, poder real, presupuesto, personal y gasto de personal. El usuario quiere rellenar los campos vacíos, en particular **el coste (presupuesto propio)** y **los salarios que se están pagando** (gasto de personal: capítulo 1 — crédito, obligaciones reconocidas y pagos — y plantilla ocupada). Fecha de revisión: 11/10/2026. La hoja ya tiene un método muy estricto; hay que respetarlo al pie de la letra.

Ficheros (léelos con Read):
- `investigacion/headers.json`: las 73 cabeceras exactas de la Hoja 1.
- `investigacion/ejemplos.json`: tres filas bien rellenas (estatal IGAE ID3, autonómica ID99, personal ID36). Copia su estilo, vocabulario y nivel de detalle.
- Tu fichero de lote (indicado en tu encargo): las filas que te tocan, con los campos ya rellenos (lo vacío no aparece).

## Reglas de método (obligatorias)
1. **Solo fuentes primarias u oficiales**: BOE y boletines autonómicos, leyes de presupuestos y sus anexos/estados (presupuestos por secciones, programas, organismos), IGAE (ejecución mensual de organismos, cuentas anuales del sector público en BOE), intervenciones generales y portales de presupuestos de las CCAA, portales de transparencia de la propia entidad o del gobierno, cuentas anuales auditadas, memorias anuales oficiales, RPT publicadas. Prensa solo como pista para localizar el documento oficial, nunca como fuente de la cifra.
2. **Cada número con URL y localización** (página/tabla/fila/columna) y unidad original (euros, miles de euros). Convierte a **millones de EUR** (p. ej. 4.288 miles EUR = 4.288; 20.513.203 EUR = 20.513203). Hasta 6 decimales, sin redondear más de lo que permite la fuente.
3. **Nunca estimar, nunca prorratear** presupuestos ministeriales/de consejería entre órganos, **nunca poner 0** para "no encontrado". Si no hay cifra, se deja vacío y se explica en el texto.
4. Distingue siempre: crédito inicial vs crédito total/definitivo/actualizado vs obligaciones reconocidas vs pagos; presupuesto aprobado vs proyecto vs prórroga; año y fecha de corte. Capítulo 1 = "gastos de personal": no equivale a salarios puros (incluye cotizaciones sociales, etc.); dilo en la base.
5. Plantilla: distinguir **personas ocupadas** (efectivos reales, columna "Personal: personas (ocupadas)") de **puestos RPT/plantilla presupuestaria** (columna "Puestos aprobados / presupuestados"). Los vocales/miembros de un órgano colegiado NO son plantilla.
6. Órganos colegiados/observatorios sin personalidad: verifica en su norma de creación si dice algo como "no supondrá incremento del gasto público", "se atenderá con los medios personales y materiales del Ministerio/Consejería", "los miembros no percibirán retribución / sí indemnizaciones por asistencia". Si es así, déjalo documentado (artículo y URL) en "Presupuesto: texto completo", "Notas de personal y apoyo ministerial", "Cobertura..." y estados, y usa **Estado de cuantificación = "Sin presupuesto propio: órgano sin dotación diferenciada (verificado en norma)"**. Si existe un importe específico e identificable que lo financia (convenio, encargo, contrato, subvención nominativa, línea de programa con su nombre), ponlo en las columnas **contextuales** (AA–AD: "Importe contextual (EUR millones; NO sumar)", "Año / periodo contextual", "Base contextual", "Nombre del titular del importe"), nunca como presupuesto propio.
7. No borres ni contradigas información existente salvo que tengas una fuente primaria que lo corrija; si corriges, explícalo en "verificacion".
8. Trabaja con eficiencia: prioriza los huecos de mayor valor (presupuesto propio, cap.1 crédito/ejecución, plantilla). Si tras 3–4 búsquedas razonables no aparece una cifra, documenta qué buscaste y pasa a la siguiente.

## Columnas y vocabulario controlado
- K "Presupuesto propio (EUR millones)", L "Año del presupuesto" (número, p. ej. 2026), M "Base del presupuesto numérico" → **exactamente uno de**: `Crédito total actualizado` | `Crédito inicial aprobado` | `Presupuesto propio aprobado` (el resumen hace SUMIFS sobre estos literales). N "Corte del presupuesto numérico" (p. ej. `31/08/2026`, `2026, crédito aprobado`, `2026, prórroga del presupuesto 2025`). P "Crédito inicial (EUR millones)", Q "Modificación neta (EUR millones)" (solo si hay crédito actualizado).
- O "Estado de cuantificación": `Cifra propia verificada` | `Cifra propia2025 verificada; actual2026 pendiente` (cambia el año si procede) | `Sin presupuesto propio: órgano sin dotación diferenciada (verificado en norma)` | `Sin cifra propia actual verificada` (si sigue sin encontrarse) | los de extinción ya existentes.
- R "Presupuesto: texto completo": reescribe con la cifra, base, corte, documento y página, y advertencias (p. ej. "incluye transferencias/ayudas, no solo administración").
- AG "Personal: personas (ocupadas)" (número), AH "Año del personal" (año o fecha AAAA-MM-DD), AI "Base del personal" (texto: qué se cuenta), AJ "Estado de verificación del personal" (`Cifra de personal publicada en fuente primaria; fecha indicada, no inferir vigencia posterior` si se rellena), AK "Fuente del personal" (URL).
- AL "Crédito de personal (EUR millones)" (cap.1), AM año, AN base (p. ej. `Capítulo 1: crédito inicial 2026, sección X programa Y`), AO estado (p. ej. `Crédito autorizado, no gasto realizado ni solo salarios`), AP fuente.
- AQ "Gasto de personal ejecutado (EUR millones)" (obligaciones reconocidas cap.1), AR año, AS "Corte de ejecución de personal" (p. ej. `Hasta 30/06/2026: 6 meses, NO año completo`), AT base, AU fuente, AV estado (`Fuente primaria cotejada contra fila y unidad; no estimación`).
- AW "Cobertura presupuesto / personal / salarios": resumen de una línea de qué hay verificado y qué no.
- AX "Puestos aprobados / presupuestados" (número), AY fecha, AZ base, BA fuente.
- BB "Notas de personal y apoyo ministerial": texto.
- BI "Pagos de personal 2026 hasta 31/08 (EUR millones)": solo si la fuente da pagos cap.1 con corte 31/08/2026; si el corte es otro, ponlo en BN.
- BJ / BK: crédito y obligaciones cap.1 comparativos 2025 a 31/08 (edición IGAE 08.2026) — solo estatales IGAE.
- BN "Notas de conciliación de crédito y ejecución": texto libre para cifras con otro corte o matices.
- BO "Crédito personal 2025 cierre", BP "Gasto personal 2025 reconocido anual", BQ "Pagos personal 2025 anual" (EUR millones), BR "Año y corte anual personal", BS "Base anual de personal", BT "Fuente anual de personal" (URL), BU "Verificación anual / conciliación". **Solo año 2025 completo** (liquidación/cuenta general/cuentas anuales 2025). Si solo hay 2024, ponlo como texto en BN con fuente.
- "Fuentes de la ficha": no la reescribas; devuelve las URLs nuevas en `fuentes_nuevas` y yo las añado.

## Acceso web
- Usa WebSearch (mode "standard"; "extended" si lo estándar sale pobre o desactualizado) y WebFetch. **WebFetch solo funciona con URLs que hayan aparecido en resultados de WebSearch** (si da PROVENANCE_REQUIRED, busca el documento para que su URL salga en resultados y vuelve a intentarlo). El shell no tiene acceso a internet.
- PDFs largos: WebFetch trunca; usa el parámetro `offset` para seguir leyendo, y pide en el prompt que cite literalmente la fila, cifras, unidad y página. Desconfía de resúmenes: pide la cita literal.
- Para la IGAE: los PDFs "ORGANISMOS MM. AAAA" (ejecución mensual de organismos autónomos y "resto de entidades"); gastos por capítulos en el bloque de gastos (págs. ~42-72 OOAA y ~99-119 resto de entidades). La cifra de ejecución por capítulos está en miles de EUR.

## Salida
Escribe un JSON en la ruta indicada en tu encargo con esta forma (lista, una entrada por ID de tu lote, aunque no hayas podido rellenar nada):
```json
[
  {
    "ID": 23,
    "updates": {"<cabecera exacta>": <valor: número en EUR millones o texto>, "...": "..."},
    "fuentes_nuevas": ["https://..."],
    "verificacion": "Para cada número: documento, página/tabla/fila, unidad original y conversión.",
    "no_encontrado": "Qué buscaste y no apareció."
  }
]
```
Usa las cabeceras **exactas** de headers.json como claves en `updates`. Incluye solo campos que cambian o se rellenan. Escribe el JSON con la herramienta Write y valida que es JSON correcto (python3 -c "import json; json.load(open(...))"). Tu respuesta final: un resumen breve (máx. 15 líneas) de qué rellenaste, qué no, y cualquier duda o contradicción con la hoja.
