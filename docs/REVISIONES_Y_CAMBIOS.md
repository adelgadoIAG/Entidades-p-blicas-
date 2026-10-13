# Revisiones y cambios (fork / mantenimiento)

Registro de cambios metodológicos o de datos hechos **después** de la publicación original del análisis (corte 12/10/2026). Cada entrada debe indicar qué se cambió, por qué y qué validación se hizo.

## 2026-03-12 — Dashboard: pestañas, matriz de integración y UI

| Área | Cambio | Motivo |
|------|--------|--------|
| CSS / `app.js` | Pestañas no ocultaban paneles | `.ep-page { display: grid }` anulaba `[hidden]` |
| Tabla entidades | Columna «Matriz / integración» | Mostrar `destino` sin abrir el detalle |
| Tema 112 | Nota en tabla y en Duplicidades | No hay organismo estatal que absorba el 112 |
| Docs | `AUDITORIA_DASHBOARD.md`, `serve_dashboard.ps1`, d3 local | Revisión local y publicación Claude |

**Validación:** `python scripts/build_dashboard.py`, `python scripts/validate_dashboard_data.py`, servidor local.

---

## 2026-03-12 — Clasificación, destinos y referencias (revisión metodológica)

### 1. Agencia de Emergencias de Andalucía (id 101) — sigue **Mantener**

- **Pregunta:** ¿Debería ser «Integrar» por el «mando único» (112, GREA, IESPA)?
- **Decisión:** **No.** El veredicto «Integrar» del P100 significa que la función pasa a un **organismo estatal** (o equivalente nacional) porque «con uno basta». El 112 es competencia autonómica; el Estado no presta el servicio en ninguna CCAA (`temas.json`, tema «Entes de emergencias 112»).
- **Cambio:** Se amplía el **motivo** en `clasificacion3.py` para distinguir integración operativa interna de la CA del veredicto P100.
- **Indicadores:** Sigue apareciendo «Mantener» porque el veredicto no cambia; es coherente con Asturias y Cantabria (mismo tema).

### 2. Confederaciones hidrográficas Miño-Sil (37) y Cantábrico (38) — **Mantener** (antes Reformar)

- **Pregunta:** ¿Por qué solo estas dos y «Reformar»? ¿Y Ebro, Tajo, etc.?
- **Decisión:** Son **organismos autónomos estatales** adscritos al ministerio de Medio Ambiente, no duplicidades autonómicas. El inventario de 125 solo incluye entidades **creadas o transformadas desde 2006**; otras confederaciones no tienen ficha en esta hoja.
- **P100 «Menos normas 12»:** Afecta al régimen de informes (silencio favorable), no a suprimir o integrar el organismo. Se reclasifican como **Mantener** con motivo explícito.
- **Efecto en cifras:** «Reformar» pasa de 6 a **4** (quedan CTBG, AECID, INVIED, SETT). Actualizar lectura en `docs/03-clasificacion-p100.md` al regenerar documentación.

### 3. Nombres completos en «destino / matriz»

- **Cambio:** `scripts/destino_labels.py` y aplicación en `clasificacion3.py` + `build_dash_data.py` (`destino_mostrar`).
- **Motivo:** Siglas (CDTI, AEAT, CNMC…) generan dudas en lectura no experta.

### 4. CDTI como referencia en «Todas las entidades»

- **Problema:** La AEE (id 40) integra en «CDTI», pero el CDTI no estaba en el inventario de 125.
- **Cambio:** Fila de **referencia** en `datos/referencias_matriz.json` → `dashboard/datos/referencias_matriz.json`, visible en la tabla (veredicto «Referencia»), **excluida** de KPIs y de `indicadores` en `calcs.js`.
- **Pendiente:** Volcar presupuesto y personal del CDTI desde PGE 2023 ([rom PGE 2023](https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Ley/MaestroDocumentos/PGE-ROM/N_23_E_R_5_0_0N_0_0978_0.htm), [CDTI presupuestos](https://www.cdti.es/presupuestos-generales)) con el mismo método que el resto de fichas.

### Regenerar datos tras cambios de clasificación

```powershell
cd C:\Users\Holacons\Work\extramuros
python scripts/clasificacion3.py
python scripts/apply.py salida/Entidades_publicas_poder_y_presupuesto_v5.xlsx datos/resultados/Z_clasificacion.json
python scripts/build_dash_data.py
python scripts/build_dashboard.py
python scripts/export_csv.py salida/Entidades_publicas_poder_y_presupuesto_v5.xlsx
```

---

## Plantilla para próximas entradas

```markdown
## YYYY-MM-DD — Título breve

- **Archivos:** …
- **Decisión / cambio:** …
- **Validación:** …
```
