import json
P1281 = "https://www.parcan.es/files/transparencia/ofi_presupuestaria/2026/1281.pdf"
P1210 = "https://www.parcan.es/files/transparencia/ofi_presupuestaria/2026/1210.pdf"
P1202 = "https://www.parcan.es/files/transparencia/ofi_presupuestaria/2026/1202.pdf"

cant_common = ("Ronda 2: el PDF del BOC Ext. 12/2026 copiado en BOE (boe.es/ccaa/boct/2026/012/c00001-01406.pdf) solo devuelve ~77.000 caracteres "
  "(articulado hasta el art. 23, p. 2225); con offset no hay más texto: los anexos del estado de gastos no son extraíbles. "
  "transparencia.cantabria.es bloquea robots (ROBOTS_DISALLOWED). Búsquedas sin resultado: documentos de presupuestos 2026 en cantabria.es "
  "(resumen por capítulos/organismos), tomos del proyecto en parlamento-cantabria.es (solo aparece un proyecto de 2017), ejecución mensual de la "
  "Intervención General de Cantabria, CVE-2026-3601 en boc.cantabria.es, importe exacto 18.273.639 y web 112.cantabria.es.")

out = []
def add(ID, updates=None, fuentes=None, verif="", no=""):
    out.append({"ID": ID, "updates": updates or {}, "fuentes_nuevas": fuentes or [], "verificacion": verif, "no_encontrado": no})

# Asturias
ast_common = ("Ronda 2: el BOPA Suplemento de 31/12/2025 (Ley 5/2025) en copia BOE (boe.es/ccaa/bopa/2025/251/a00001-00699.pdf, 699 pp.) solo devuelve "
  "~74.000 caracteres (hasta p. 30/699, art. 22): no se alcanzan anexos con desglose por capítulos. El Tomo 8 'Informe de personal' del proyecto 2026 "
  "sí salió en buscador (transparencia.asturias.es/documents/2213862/3949486/proyecto_2026_T8_informe_personal.pdf) pero devuelve ROBOTS_DISALLOWED. "
  "Copia del Tomo 7 (informe económico-financiero) en asturiasliberal.es: solo se extraen pp. 5-48 (contexto económico); la estructura orgánica (pp. 193-204) queda fuera, "
  "y además es proyecto y web no oficial. BOPA 2026: solo convocatorias del SEPA (p. ej. BOPA 14/07/2026, 2026-05856), sin ejecución por capítulos.")
add(79, no=ast_common + " Sin capítulo 1, ejecución 2026, liquidación 2025 ni plantilla del SEPA (sección 87).")
add(112, no=ast_common + " Búsqueda de cuentas anuales 2025/plantilla de Sekuens: solo plan de contratación 2025 (miprincipado.asturias.es) y convocatorias; sin gastos de personal de su presupuesto de explotación.")
add(113, no=ast_common + " Sin desglose por capítulos de la sección 88 (Consejo de Transparencia) ni personal adscrito.")

# Cantabria
add(82, no=cant_common + " Total y capítulo 1 de la Sección 16 (ICASS) siguen sin verificar; plantilla, ejecución y liquidación 2025 no localizadas.")
add(83, no=cant_common + " Capítulo 1 2026 del ICASST, ejecución y plantilla no localizados.")
add(114, no=cant_common + " Capítulo 1 2026 del SEMCA, ejecución, liquidación 2025 y plantilla no localizados.")
add(116, no=cant_common + " Búsqueda específica en transparencia del ICAP 'Rafael de la Sierra': sin resultados. El capítulo 1 de la ley aprobada sigue sin verificar (el 1.153.998 EUR del anteproyecto queda solo como contexto ya anotado).")
add(115, no=cant_common + " Búsqueda de subvención nominativa/transferencia al 'Consejo de la Juventud de Cantabria' (2025-2026): solo aparecen en jovenmania.com (portal de juventud del Gobierno) una convocatoria a entidades locales (Resolución 18/03/2025, BOC 58, aplicación 07.08.232A.463, 100.000 EUR) y una concesión a asociaciones juveniles (02/10/2024); ninguna nombra al Consejo. Sin importe contextual verificable.")

# Canarias ATC
upd81 = {
 "Presupuesto propio (EUR millones)": 85.087141,
 "Año del presupuesto": 2026,
 "Base del presupuesto numérico": "Crédito total actualizado",
 "Corte del presupuesto numérico": "31/07/2026",
 "Estado de cuantificación": "Cifra propia verificada",
 "Crédito inicial (EUR millones)": 64.227709,
 "Modificación neta (EUR millones)": 20.859432,
 "Presupuesto: texto completo": ("Sección 72 'Agencia Tributaria Canaria', ejercicio 2026: crédito inicial 64.227.709,00 EUR; modificaciones netas +20.859.432,21; crédito definitivo "
   "85.087.141,21 EUR (85,087141 M) a 31/07/2026. Fuente: 'Estado de ejecución de gastos de corriente :: detalle por sección / capítulo', Ejercicio 2026, Período enero (1) / julio (7), "
   "Fecha de edición 20.08.2026, publicado por la Oficina Presupuestaria del Parlamento de Canarias (parcan.es, fichero 2026/1281), fila '* 72 AGENCIA TRIBUTARIA CANARIA', en euros. "
   "Las modificaciones son casi todas cap.4 transferencias corrientes (+19.730.222,18), cap.7 (+1.018.710,03) y cap.8 (+110.500); el crédito inicial (cap.1 29.745.009 + cap.2 17.842.980 + cap.6 16.639.720) "
   "coincide con el Plan de Acción 2026 (BOC 2026/065); no usar 64.277.709. Obligaciones reconocidas totales a 31/07/2026: 40.755.728,95; pagos 37.371.723,72. "
   "Crédito, no gasto ejecutado; incluye transferencias e inversiones, no solo administración."),
 "Corte: texto completo": "Crédito definitivo y ejecución a 31/07/2026 (enero-julio, edición 20/08/2026); crédito inicial 2026 de la Ley 9/2025; revisión 11/10/2026",
 "Crédito de personal (EUR millones)": 29.744903,
 "Año del coste de personal": 2026,
 "Base del coste de personal": "Capítulo 1: crédito definitivo (total actualizado) 2026, sección 72 ATC, corte 31/07/2026 (estado de ejecución enero-julio, edición 20/08/2026)",
 "Estado de verificación del coste": "Crédito autorizado, no gasto realizado ni solo salarios",
 "Fuente del coste": P1281,
 "Gasto de personal ejecutado (EUR millones)": 17.279615,
 "Año del gasto de personal": 2026,
 "Corte de ejecución de personal": "Hasta 31/07/2026: 7 meses, NO año completo",
 "Base de ejecución de personal": "Capítulo 1: obligaciones reconocidas; incluye costes de personal (cotizaciones sociales, etc.), no desglose salarial puro",
 "Fuente de ejecución de personal": P1281,
 "Estado de verificación de ejecución": "Fuente primaria cotejada contra fila y unidad EUR; no estimación",
 "Cobertura presupuesto / personal / salarios": "Presupuesto 2026 (crédito total a 31/07) y capítulo 1 2026 (crédito y obligaciones a 31/07) verificados; ocupación RPT a cierre 2025 del Plan 2026; liquidación 2025 del cap.1 no verificada",
 "Crédito personal inicial / otra base (EUR millones; NO sumar)": 29.745009,
 "Base / fecha del crédito alternativo": "Capítulo 1: crédito inicial 2026 (Ley 9/2025 de PG de Canarias), sección 72 ATC, según estado de ejecución enero-julio 2026 (y enero 2026, fichero 1202)",
 "Notas de conciliación de crédito y ejecución": ("Oficina Presupuestaria del Parlamento de Canarias, ejecución enero-julio 2026 (ed. 20/08/2026), fila '1 GASTOS DE PERSONAL' de la sección 72, EUR: crédito inicial 29.745.009,00; "
   "mod. -106,37 (pasa a cap.3); definitivo 29.744.902,63; saldo disponible 926.063,34; retenciones 154.336,99; autorizaciones 28.664.502,30; compromisos 28.664.502,30; "
   "obligaciones reconocidas 17.279.615,19; pagos 17.279.615,19; pendiente de pago 0,00. Corte 31/07/2026, no 31/08: por eso no se rellena 'Pagos de personal 2026 hasta 31/08'. "
   "Pagos cap.1 a 31/07/2026: 17,279615 M. Enero-febrero 2026 (ed. 19/03/2026, fichero 1210): obligaciones cap.1 4.144.466,42. "
   "Liquidación 2025: no localizada (la web de transparencia de la ATC solo enlaza ejecución trimestral 1T-3T 2025; no apareció el cierre de diciembre 2025). "
   "Capítulo 1 no equivale solo a sueldos. No comparar 7 meses con año completo.")
}
add(81, upd81, [P1281, P1210, P1202],
  verif=("(1) parcan.es 2026/1281.pdf: 'ESTADO DE EJECUCIÓN DE GASTOS DE CORRIENTE :: DETALLE POR SECCIÓN / CAPÍTULO', Ejercicio 2026, Período Enero(1)/Julio(7), Fecha de edición 20.08.2026; "
   "columnas: crédito inicial | mod. crédito | crédito definitivo | saldo c.disponible | retenciones | autorizaciones | compromisos | oblig. reconoc. | pagos realizados | oblig. pdte pago. "
   "Fila literal '1 GASTOS DE PERSONAL 29.745.009,00 -106,37 29.744.902,63 926.063,34 154.336,99 28.664.502,30 28.664.502,30 17.279.615,19 17.279.615,19 0,00' (EUR) -> crédito definitivo 29,744903 M; obligaciones 17,279615 M; crédito inicial 29,745009 M. "
   "Coherencia: 29.744.902,63 - 926.063,34 - 154.336,99 = 28.664.502,30. Fila '* 72 AGENCIA TRIBUTARIA CANARIA 64.227.709,00 20.859.432,21 85.087.141,21 ... 40.755.728,95 37.371.723,72 3.384.005,23' -> 85,087141 M; mod. 20,859432 M. "
   "Cotejo: suma de capítulos iniciales 29.745.009+17.842.980+16.639.720 = 64.227.709; suma de modificaciones por capítulo = 20.859.432,21; suma de obligaciones por capítulo = 40.755.728,95. "
   "El PDF no muestra número de página. (2) 1210.pdf: período enero-febrero, ed. 19.03.2026, cap.1 crédito 29.745.009,00 y obligaciones 4.144.466,42. (3) 1202.pdf: enero 2026, fecha de carga <=05/02/2026, cap.1 crédito 29.745.009,00 y total ATC 64.227.709,00. "
   "Se cambia la base de 'Presupuesto propio' de crédito inicial a crédito total actualizado a 31/07/2026 (método de la hoja); el crédito inicial 64,227709 M se conserva en 'Crédito inicial'. Fuente: repositorio de transparencia del Parlamento de Canarias con el estado contable del Gobierno (Status C, operaciones contables), no prensa."),
  no=("No hay edición de agosto 2026 en resultados de búsqueda (se usa julio). Liquidación/cierre 2025 del cap.1 de la ATC: no localizada en parcan.es (ofi_presupuestaria/2025) ni en la web de la ATC (solo 1T-3T 2025). "
      "El PDF de la Ley 9/2025 (BOE ccaa boc/2025/256) solo devuelve el articulado hasta el art. 1; sus anexos no son legibles. El Plan de Acción 2026 (URL de la ficha) devolvió PROVENANCE_REQUIRED, así que no se recotejó su página."))

# Baleares
bal_common = ("Ronda 2: el índice del Compte General 2025 (caib.es/conselleries/hisenda/interven/compte_general_2025/index.html) sí lista los estados de la ATIB "
  "(archivos/atib_tom1_1_1.html 'Estat d'execució del pressupost de despeses'; atib_tom3_1_2_50.html 'detall per partides'), del IB-Salut y apartados de EPE/fundacions/consorcis, "
  "pero esas páginas solo devuelven el aviso 'sólo para navegadores de 4ª generación' (contenido cargado por script); no se localizaron PDFs equivalentes en buscador. "
  "La única otra pieza de la Intervenció hallada (sites/intervencio/f/527011) es la Instrucció 1/2025 sobre modificaciones de crédito, sin cifras.")
add(80, no=bal_common + " Ejecución 2026 y liquidación 2025 del cap.1 de la ATIB y plantilla ocupada siguen sin cifra.")
add(111, no=bal_common + " Nada nuevo sobre el personal de la ASPIB ni la ejecución de la sección 74.")
add(124, no=bal_common + " Nada nuevo sobre ejecución 2026 ni plantilla de ABDigital (cuentas 2025 estarían en el apartado EPE, no legible).")
add(125, no=bal_common + " Nada nuevo sobre plantilla ni cuentas 2025 del IBE (apartado EPE no legible).")

order = [79,112,113,82,83,114,116,115,81,80,111,124,125]
out.sort(key=lambda r: order.index(r["ID"]))
json.dump(out, open("datos/resultados/R2D_ast_bal_can_cant.json","w"), ensure_ascii=False, indent=1)
