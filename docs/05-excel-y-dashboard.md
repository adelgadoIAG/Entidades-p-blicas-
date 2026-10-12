# 5. Excel y dashboard

## Excel

`scripts/apply.py` parte siempre de la hoja original de `datos/entrada/`, así que se puede ejecutar las veces que haga falta. Hace lo siguiente:

1. Aplica los JSON de `datos/resultados/` en el orden que recibe. En `run_all.sh`, la clasificación va la última.
2. Marca **en amarillo** cada celda cambiada y pone la fecha de revisión en la fila.
3. Añade las URL nuevas a «Fuentes de la ficha», sin borrar las anteriores.
4. Añade columnas nuevas al final de «Hoja 1»: la clasificación (útil o no, veredicto, base en el P100, destino, función, duplicidad, UE, actividad, motivo, tema), el coste de apoyo, el coste por persona y el desglose de personal.
5. Crea o rehace estas hojas:

| Hoja | Contenido |
|---|---|
| Entidades | Resumen con fórmulas: presupuesto por base, ejecución de personal a 31/08, cobertura de campos, recuentos por veredicto, por útil o no y por función, base en el P100, texto del criterio y escenario de coste de los órganos consultivos |
| Duplicidades por tema | Matriz tema × territorio con nombre y fuente de cada celda |
| Hoja 1 | La hoja original completada |
| Cambios 12-10-2026 | Cada celda cambiada: valor anterior y valor nuevo |
| Verificación y pendientes | Por ficha: cómo se verificó y qué sigue sin cifra |
| Gasto CNMC y CSIC | Capítulos y a qué se destina cada uno |

Las fórmulas se calculan al abrir el fichero. Si hace falta el fichero con los valores ya calculados (por ejemplo, para leerlo con pandas), ábrelo y guárdalo en Excel o LibreOffice.

`scripts/export_csv.py` saca un CSV plano con una fila por entidad, para leerlo en GitHub o en cualquier hoja de cálculo.

## Dashboard

El dashboard publicado es un artifact de Claude de tipo «Dashboard». El tipo pone el entorno: el objeto `dash`, los estilos (`--cds-*`, `--color-*`) y d3. Nosotros ponemos la página y los datos.

| Fichero | Qué es |
|---|---|
| `dashboard/style.css` | Estilos propios |
| `dashboard/body.html` | Marcado de las seis pestañas: Resumen, Duplicidades, Todas las entidades, Personal, Indicadores, Verificación y pendientes |
| `dashboard/calcs.js` | Todas las cifras derivadas (`dash.calc`): recuentos por veredicto, por útil o no, por base, por presidencia; destino de las integraciones; escenario de coste; indicadores… |
| `dashboard/app.js` | Dibujo de tablas y gráficos con d3, filtros y ficha de detalle |
| `dashboard/datos/*.json` | Los siete conjuntos de datos que usa la página |

Los datos salen de `scripts/build_dash_data.py` (que lee el Excel) y de `scripts/clasificacion2.py` (duplicidades y temas). `scripts/build_dashboard.py` monta dos ficheros:
- `dashboard/index.html`: la página tal como se publica en el artifact.
- `dashboard/preview.html`: una copia autónoma que se abre en cualquier navegador. Lleva los datos dentro, carga d3 desde cdnjs e incluye un sustituto mínimo de `dash` y unos estilos de reserva. Sirve para revisar el contenido sin Claude; no reproduce exactamente el aspecto publicado.

### Publicar o actualizar el dashboard en Claude

1. Sube cada `dashboard/datos/<conjunto>.json` como fichero (asset) del artifact.
2. Apunta el documento `datasets/<conjunto>` a la URL del fichero subido.
3. Sustituye el documento `files/index.html` por el contenido de `dashboard/index.html`.

Lo más sencillo es pedírselo a Claude con este README delante.

### Marcado

Para que las cifras se puedan citar y comprobar, la página no lleva números escritos a mano. Cada valor está marcado con `data-source` (el conjunto o el cálculo), `data-field` (la columna) y `data-where` o `data-row` (la fila). Las tablas llevan `data-row-key`. Si se añade una cifra, debe salir de un conjunto o de un `dash.calc`, nunca escrita en el HTML.
