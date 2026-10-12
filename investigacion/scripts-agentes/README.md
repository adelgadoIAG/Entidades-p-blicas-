# Scripts de los agentes de investigación

Algunos agentes no escribieron el JSON de resultados a mano: escribieron un pequeño script de Python con las cifras encontradas, sus fuentes y sus notas, y el script generaba el JSON. Se guardan aquí para que se vea exactamente cómo se construyó cada resultado.

**No hace falta ejecutarlos para reproducir el análisis.** Los JSON ya están en `datos/resultados/`. Si se ejecutan desde la raíz del repositorio, regeneran su JSON, y se ha comprobado que el resultado es idéntico al guardado.

| Script | Genera | Encargo |
|---|---|---|
| `build_b2.py` | `B2_estatal_colegiados.json` | 03 |
| `build_C.py` | `C_estatal_plantillas.json` | 04 |
| `r2a_build.py` | `R2A_estatal.json` | 09 |
| `build_r2c.py` | `R2C_andalucia_aragon.json` | 11 |
| `build_r2d.py` | `R2D_ast_bal_can_cant.json` | 12 |
| `build_r2e.py` | `R2E_varias.json` | 13 |
| `p1.py` | `P1_investigacion.json` | 15 |
| `p4_build.py` (con `p4_isa.py`, recuento de la RPT del Instituto de Salud de Andalucía) | `P4_andalucia_aragon.json` | 18 |
| `mk_p5.py` | `P5_ast_bal_can_cant_cat.json` | 19 |
| `p6_build.py` | `P6_gal_mad_mur_nav_pv_val.json` | 20 |
| `build_dup1.py`, `build_dup2.py`, `dup3.py`, `build_dup4.py`, `dup5.py` | `DUP1.json` a `DUP5.json` | 21–25 |
| `build_c_apoyo.py` | `C_apoyo.json` | 26 |
| `build_gasto.py` | `gasto_csic_cnmc.json` | 27 |

Estos resultados no tienen script, porque el agente escribió el JSON directamente:
- `A`, `B1`, `D`, `E`, `F` y `G` (ronda 1);
- `R2B`;
- `P2` y `P3`;
- `verificacion.json`.

`../notas/` guarda las notas de trabajo de un agente (lote G), con las referencias de cada cifra.
