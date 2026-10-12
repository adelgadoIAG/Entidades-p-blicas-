# Verificar muestra de cifras nuevas

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un verificador independiente. No has participado en la investigación. Tu tarea: comprobar contra la fuente primaria una muestra de 20 cifras que se han añadido a una hoja de cálculo de presupuestos de entidades públicas españolas.

Lee investigacion/verificar.json. Cada entrada tiene: ID, Nombre de la entidad, campo, valor_hoja (en millones de EUR salvo los campos de personas), el texto explicativo de la ficha y las URLs de fuentes (columnas 'fuentes', 'fuente_coste', 'fuente_ejec', 'fuente_personal', 'fuente_anual').

Para cada entrada: abre con WebFetch la URL más directa de la cifra (pide en el prompt de WebFetch la cita literal de la fila/importe y la unidad), y comprueba que el valor de la hoja coincide tras convertir unidades (euros → /1.000.000; miles de euros → /1.000). Si un PDF es largo, usa el parámetro offset. Si WebFetch rechaza la URL por procedencia (PROVENANCE_REQUIRED), haz UNA WebSearch con el título del documento para que la URL aparezca en resultados y reintenta; tienes un máximo de 12 WebSearch en total, así que priorízalas. Si una consulta al BOE con "?id=" devuelve un documento con otro título, descártala (caché contaminada) y dilo.

Escribe datos/resultados/verificacion.json: lista de {"ID", "campo", "valor_hoja", "valor_fuente_literal", "unidad", "url", "resultado": "COINCIDE" | "NO COINCIDE" | "NO VERIFICABLE", "nota"}. Tu respuesta final: tabla breve con el resultado por ID y cualquier discrepancia explicada (≤15 líneas).
