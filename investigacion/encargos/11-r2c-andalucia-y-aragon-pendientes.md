# R2C: Andalucía y Aragón pendientes

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de presupuestos autonómicos españoles. Lee primero investigacion/BRIEF.md (método obligatorio, columnas, vocabulario y formato de salida), luego investigacion/headers.json y investigacion/ejemplos.json.

Segunda ronda. Tu lote: investigacion/lotes/R2C_andalucia_aragon.json (Andalucía 73, 74, 75, 76, 77, 97, 98, 99, 100, 101; Aragón 78). Cada fila trae su estado actual (ya incluye lo hecho en ronda 1) y en '_pendiente_ronda1' lo que faltó. La ronda 1 completa está en datos/resultados/D_andalucia_aragon.json (léela: ahí están las URLs de la Intervención General de la Junta, IGJA, que funcionaron). Escribe el resultado en datos/resultados/R2C_andalucia_aragon.json.

Presupuesto de búsquedas: máximo ~35 WebSearch (cupo compartido con otros 4 agentes). WebFetch solo abre URLs que hayan salido en resultados de WebSearch.

Prioridades:
1. Actualizar la ejecución de capítulo 1 de 2026 al corte MÁS RECIENTE publicado por la IGJA (resúmenes mensuales "rendicion/mensuales2026/<mes>/descargas/agencias/<agencia>/2_<AGENCIA>-3.pdf"; julio o el último disponible) para 73, 75, 97, 98, 99, 100, 101. Busca esas URLs para que aparezcan en resultados (p. ej. "mensuales2026 julio descargas agencias aacid 2_AACID-3"). Si consigues un corte posterior al 31/03/2026, sustituye AQ/AR/AS/AT/AU/AV y actualiza BN y Cobertura. Si es exactamente 31/08/2026 con pagos, rellena también BI.
2. 74 y 76 (secciones 08.00 y 07.00 de la Junta): ejecución cap.1 2026 y liquidación 2025 desde el resumen "Junta de Andalucía" (2_JUNTA-3) — usa offset en WebFetch para llegar a la sección; y plantilla ocupada si su memoria la da.
3. 101: cap.1 2025 anual completo (el PDF de diciembre 2025 se truncó; usa offset).
4. 77 Observatorio Territorial de Andalucía: regla 6 (Orden de 13/03/2007, BOJA 2007/70/4).
5. 78 ACPUA (Aragón): estado del presupuesto 2026 de Aragón (ley o prórroga), presupuesto propio de ACPUA (entidad de derecho público), cap.1 y plantilla (memoria anual ACPUA). Si aragon.es bloquea, busca copias en BOA/BOE o en acpua.aragon.es.

Respeta el método del brief (sin estimaciones, millones de EUR, fuente+página; "plazas presupuestadas" ≠ ocupadas). Tu respuesta final: resumen breve (≤12 líneas).
