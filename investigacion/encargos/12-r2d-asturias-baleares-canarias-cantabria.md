# R2D: Asturias, Baleares, Canarias, Cantabria

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos autonómicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Segunda ronda. Tu lote: investigacion/lotes/R2D_ast_bal_can_cant.json (Asturias 79, 112, 113; Cantabria 82, 83, 114, 116, 115; Canarias 81; Baleares 80, 111, 124, 125). Cada fila trae su estado actual (ya incluye ronda 1) y en '_pendiente_ronda1' lo que faltó. La ronda 1 completa está en datos/resultados/E_ast_bal_can_cant.json (URLs que funcionaron). Escribe el resultado en datos/resultados/R2D_ast_bal_can_cant.json.

Presupuesto de búsquedas: máximo ~35 WebSearch (cupo compartido con otros 4 agentes). WebFetch solo abre URLs que hayan salido en resultados de WebSearch. Si un PDF se trunca, usa el parámetro offset de WebFetch para leer más adelante.

Prioridades (capítulo 1 = "gastos de personal" es lo más valioso):
1. Cantabria (Ley 4/2026): capítulo 1 2026 de SEMCA (114), ICAP (116), ICASST (83), y total + cap.1 de la Sección 16 ICASS (82). Los anexos del BOC no se leían; prueba los documentos de presupuestos en la web del Gobierno de Cantabria (hacienda/presupuestos 2026: "estado de gastos por organismos", "resumen por capítulos", "anexo de personal") o el BOC con offset. Consejo de la Juventud (115): busca subvención nominativa/transferencia con su nombre.
2. Asturias (Ley 5/2025): capítulo 1 2026 de SEPA (79), Sekuens (112, gastos de personal de su presupuesto de explotación), Consejo de Transparencia (113). transparencia.asturias.es bloquea robots: busca copias (BOPA, BOE, sede asturias.es "presupuestos 2026 tomo", "informe de personal").
3. Canarias: Agencia Tributaria Canaria (81): cap.1 2026 (Ley de PG de Canarias 2026, sección/organismo ATC), ejecución y liquidación 2025.
4. Baleares (prórroga 2026): ejecución 2026 y liquidación 2025 de cap.1 de ATIB (80), y plantilla de ATIB/ABDigital/IBE si se publica en algún PDF legible.

Respeta el método del brief (sin estimaciones, millones de EUR, fuente+página). Tu respuesta final: resumen breve (≤12 líneas).
