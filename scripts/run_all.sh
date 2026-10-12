#!/usr/bin/env bash
# Reproduce todo el proceso a partir de la hoja original y los resultados de la investigación.
# Uso (desde cualquier sitio):  bash scripts/run_all.sh
set -euo pipefail
cd "$(dirname "$0")/.."
R=datos/resultados
OUT=salida/Entidades_publicas_poder_y_presupuesto_v5.xlsx

# 1. Clasificación (tres versiones encadenadas; la que cuenta es la tercera, alineada con el P100)
python3 scripts/clasificacion.py    # v1: niveles A-D (histórica)
python3 scripts/clasificacion2.py   # v2: función, tema, duplicidad, UE, actividad + datos de duplicidades del dashboard
python3 scripts/clasificacion3.py   # v3: veredicto P100 (Mantener, Reformar, Integrar, Suprimir, Pendiente, Extinguida)

# 2. Volcar todo en el Excel. El orden importa: cada fichero pisa a los anteriores en los mismos campos.
python3 scripts/apply.py "$OUT" \
  $R/A_estatal_entes.json $R/B1_estatal_colegiados.json $R/B2_estatal_colegiados.json $R/C_estatal_plantillas.json \
  $R/D_andalucia_aragon.json $R/E_ast_bal_can_cant.json $R/F_clm_cyl_cat_ext_gal.json $R/G_mad_mur_nav_pv_rio_val.json \
  $R/R2A_estatal.json $R/R2B_colegiados.json $R/R2C_andalucia_aragon.json $R/R2D_ast_bal_can_cant.json $R/R2E_varias.json \
  $R/P1_investigacion.json $R/P2_reguladores.json $R/P3_estatal_otros.json $R/P4_andalucia_aragon.json \
  $R/P5_ast_bal_can_cant_cat.json $R/P6_gal_mad_mur_nav_pv_val.json \
  $R/Z_clasificacion.json

# 3. Datos y página del dashboard
python3 scripts/build_dash_data.py "$OUT"
python3 scripts/build_dashboard.py
python3 scripts/export_csv.py "$OUT"

echo "Hecho: $OUT y dashboard/index.html, dashboard/preview.html"
echo "Las fórmulas del Excel se calculan al abrirlo en Excel, LibreOffice o Google Sheets."
