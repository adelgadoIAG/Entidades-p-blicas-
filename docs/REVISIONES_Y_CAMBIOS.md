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

### 4. Matrices de integración en «Todas las entidades»

- **Problema:** Destinos del P100 (CDTI, AEAT, ANECA…) no tenían ficha en las 125 entidades.
- **Cambio:** Filas de **referencia** en `datos/referencias_matriz.json` → `dashboard/datos/referencias_matriz.json` (veredicto «Referencia»), **excluidas** de KPIs e `indicadores` en `calcs.js`.
- **Matrices que ya están en el inventario** (no se duplican): AEI id 4, AIReF id 5, CTBG id 6, CNMC id 24 — listado en `datos/matrices_en_inventario.json`.
- **Presupuesto PGE 2023** (miles € → M€ en el dashboard), donde hay fuente ROM u oficial:

| id ref. | Organismo | presupuesto_m (2023) | Fuente principal |
|--------|-----------|----------------------|------------------|
| 9001 | CDTI | 1.086,9 | [POA CDTI 2023](https://www.cdti.es/sites/default/files/2023-06/poa_2023_2.pdf); ROM `N_23_E_R_5_0_0N_0_0152_0` (no INNVIERTE `0978`) |
| 9002 | AEAT | 1.231,6 | [ROM Hacienda AEAT](https://www.congreso.es/docu/pge2023/pge_2023-web/PGE-ROM/doc/HTM/N_23_A_R_31_115_1_1_1_T_1.HTM) |
| 9003 | ANECA | **12,9** (total ingresos O.A.; no solo transferencia 8,9) | [ROM OO.AA. ingresos](https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Ley/MaestroDocumentos/PGE-ROM/doc/HTM/N_23_E_V_1_102_2_1_A_1.HTM) |
| 9004 | AEPD | 18,8 | [Presupuesto AEPD 2023](https://www.aepd.es/documento/presupuestos-aepd-2023.pdf) |
| 9005 | Defensor del Pueblo | 20,9 | [Ejecución 2023](https://www.defensordelpueblo.es/transparencia/informacion-economica-presupuestaria-y-contractual/presupuestos/ejecucion-2023/) |
| 9006 | IDAE | 195,8 (subv. explotación) | [PEC IDAE PGE 2023](https://www.congreso.es/docu/pge2023/pge_2023-web/PGE-ROM/doc/1/6/1/1/22/N_23_A_R_5_0_0N_0_0154_0_PECROOT1_24013.PDF) |
| 9007 | INCIBE | 23,5 (ordinario + socio) | [Cuentas INCIBE 2023](https://www.incibe.es/sites/default/files/paginas/normativa-financiera/2023_informacion_financiera.pdf) |
| 9008 | CCN-CERT | — | Solo ancla institucional (sin ROM limitativo propio) |

- **Pendiente:** Personal y cap. 1 en referencias cuando se extienda el mismo método que las 125 fichas (corte 2026 en inventario).
- **Desglose núcleo técnico/científico vs administración:** solo existe en el pipeline del inventario (`personal_desglose.json`, generado desde el Excel). Las filas `referencias_matriz` **no** tienen ese desglose; hoy `personal_desglose.json` puede ir vacío si el libro no trae columnas de desglose rellenas. No se ha replicado el trabajo de clasificación de plantilla para CDTI, AEAT, ANECA, AEPD, Defensor, IDAE ni INCIBE.

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

## Próximos pasos (documentados, sin implementar)

Ideas acordadas para una iteración posterior; **no** forman parte del comportamiento actual del dashboard.

1. **Definición única de «presupuesto» en fichas y referencias**  
   Hoy conviven criterios distintos según el tipo de ente: transferencia nominativa (ANECA cap. 4), dotación PPGGE (CDTI), presupuesto de ingresos/gastos de O.A. (ANECA total ~12,9 M€), PEC de E.P.E. (IDAE con fuerte componente UE), partidas MRR a parte (INCIBE), etc. Convendría un glosario en `docs/` (p. ej. ampliar `REVISIONES_Y_CAMBIOS` o `AUDITORIA_DASHBOARD.md`) con: qué va en `presupuesto_m`, qué en `contextual_m`, año de corte y enlace ROM obligatorio por fila.

2. **Capítulo 1 y personal en `referencias_matriz`**  
   Mismo método que las 125 fichas (IGAE 2026 o PGE según se decida en el punto 1).

3. **Desglose núcleo técnico/científico vs administración**  
   Solo el inventario alimenta `personal_desglose.json` desde el Excel; las referencias 9001–9008 no lo tienen. Opciones: ampliar el libro/plantilla o un script de extracción por organismo (memoria, RPT, transparencia).

4. **Validación automática de referencias**  
   Comprobar que `presupuesto_anio`, `presupuesto_base` y `fuente` HTTPS están rellenos en todas las filas con `referencia_matriz: true`.

---

## Plantilla para próximas entradas

```markdown
## YYYY-MM-DD — Título breve

- **Archivos:** …
- **Decisión / cambio:** …
- **Validación:** …
```
