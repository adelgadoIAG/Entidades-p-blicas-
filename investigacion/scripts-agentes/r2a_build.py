import json, sys

HEAD = json.load(open('investigacion/headers.json'))
BATCH = {int(r['ID']): r for r in json.load(open('investigacion/lotes/R2A_estatal.json'))}
OUT = 'datos/resultados/R2A_estatal.json'

POA = "https://sett.gob.es/wp-content/uploads/2026/09/20260325-POA-SETT-vf.pdf"
PAP = "https://sett.gob.es/wp-content/uploads/2026/09/MEMORIA-PAP-SETT-2026-2028-vdef.pdf"
SETT_TR = "https://sett.gob.es/transparencia/"
SETT_EMP = "https://sett.gob.es/empleo/"
SETT_OPE = "https://sett.gob.es/wp-content/uploads/2025/12/20251229_OPE-SETT.pdf"
SETT_RES = "https://sett.gob.es/wp-content/uploads/2026/09/Resolucion-Plazas-OPE.pdf"
SETT_RD = "https://sett.gob.es/wp-content/uploads/2025/08/RD_676_creacion_SETT.pdf"

FPYC_CA25 = "https://www.pluralismoyconvivencia.es/wp-content/uploads/2026/07/802EDU-PLURALISMO-Y-CONVIVENCIA-F.S.-CUENTAS-CA-2025.pdf"
FPYC_PLAN25 = "https://www.pluralismoyconvivencia.es/wp-content/uploads/2025/03/Plan-Actuacion-2025.pdf"
FPYC_INFO = "https://www.pluralismoyconvivencia.es/informacion-economica-presupuestaria-y-estadistica/"
FPYC_INFO2 = "https://www.pluralismoyconvivencia.es/fundacion/informacion-economica/"

PGE23_S30 = "https://www.sepg.pap.hacienda.gob.es/Presup/PGE2023Ley/MaestroTomos/PGE-ROM/doc/L_23_E_G30.PDF"
HAC_NP = "https://www.hacienda.gob.es/es-ES/Prensa/Noticias/Paginas/2026/20260519-NP-CM-INVERSIONES-IGUALDAD.aspx"

OIR = "https://www.hacienda.gob.es/rsc/oirescon/informe-anual-actuaciones/informe-anual-actuaciones-2025.pdf"

RD606 = "https://www.boe.es/boe/dias/2026/07/25/pdfs/BOE-A-2026-16172.pdf"
MAIN_AAI = "https://www.igualdad.gob.es/wp-content/uploads/2025/11/MAIN_ESTATUTO_AAI_Audiencia.pdf"
RD65 = "https://boe.es/boe/dias/2026/02/04/pdfs/BOE-A-2026-2553.pdf"
AESAP1 = "https://boe.es/boe/dias/2026/02/18/pdfs/BOE-A-2026-3787.pdf"
AESAP2 = "https://www.boe.es/boe/dias/2026/07/29/pdfs/BOE-A-2026-16527.pdf"
CNF_INAP = "https://laadministracionaldia.inap.es/noticia.asp?id=1235579"
CNF_CONG = "https://www.congreso.es/l15p/e11/e_0114946_n_000.pdf"
IGAE1225 = "https://www.igae.pap.hacienda.gob.es/sitios/igae/es-ES/Contabilidad/ContabilidadPublica/CPE/EjecucionPresupuestaria/Documents/ORGANISMOS%2012.%202025.pdf"

ST_PERS = "Cifra de personal publicada en fuente primaria; fecha indicada, no inferir vigencia posterior"

res = []

# ---------------- ID 66 SETT ----------------
res.append({
 "ID": 66,
 "updates": {
  "Presupuesto propio (EUR millones)": 11.1445,
  "Año del presupuesto": 2026,
  "Base del presupuesto numérico": "Presupuesto propio aprobado",
  "Corte del presupuesto numérico": "2026, presupuesto operativo de gastos del Plan Operativo Anual 2026 (versión final; fichero fechado 25/03/2026)",
  "Estado de cuantificación": "Cifra propia verificada",
  "Presupuesto: texto completo": "Presupuesto operativo de gastos 2026 de la SETT: 11.144,5 miles EUR = 11,1445 M EUR (Plan Operativo Anual 2026, Tabla 2 'Gastos operativos SETT 2024-2026 (ppto)', p.25; texto p.24: 'El presupuesto operativo de gastos para el año 2026 ascenderá a 11,1 millones de euros'). Incluye gastos de personal 4,000 M, evaluación de operaciones (Comisión de Evaluación y Consejo Rector; notarías e informes), gastos corrientes y servicios especializados (encargos a Ineco/Tragsatec y otros: 5,1717 M). Serie: 2024 real 3,5378 M; 2025 provisional 7,1036 M; 2026 ppto 11,1445 M. NO incluye las dotaciones de los instrumentos (RD 676/2024: Chip 10.750 M, Next Tech 4.000 M, Audiovisual 1.712 M) ni lo formalizado en 2025 (POA p.9: PERTE Chip 864,4 M; Next Tech 100,2 M directas + 217,0 M vehículos; Audiovisual 49,4 M): son operaciones financieras de los fondos, no gasto anual de funcionamiento. El POA no indica fecha ni órgano de aprobación; el Estatuto (RD 676/2024, art.11.1.e) atribuye al Consejo Rector aprobar el plan anual de actuación y los presupuestos anuales de explotación y de capital. Advertencia: en la extracción las partidas de la Tabla 2 no suman exactamente el total impreso; el total 2026 coincide con el texto de p.24. Presupuesto de explotación y capital en PGE (prórroga 2026): no localizado.",
  "Crédito de personal (EUR millones)": 4.0,
  "Año del coste de personal": 2026,
  "Base del coste de personal": "Gastos de personal presupuestados 2026 (POA 2026, Tabla 2 p.25 y cuenta de pérdidas y ganancias presupuestada p.27): sueldos y salarios 2.934,1 + Seguridad Social y otros 1.065,9 = 4.000,0 miles EUR. Base cuenta de PyG de EPE, NO capítulo 1 presupuestario",
  "Estado de verificación del coste": "Previsión presupuestaria propia de la entidad (POA 2026); no gasto realizado ni solo salarios",
  "Fuente del coste": POA,
  "Gasto de personal ejecutado (EUR millones)": 1.5708,
  "Año del gasto de personal": 2025,
  "Corte de ejecución de personal": "2025 año completo; cifra PROVISIONAL ('Prov.') del POA 2026, no cuentas anuales auditadas",
  "Base de ejecución de personal": "Gastos de personal 2025 de la cuenta de PyG provisional (POA 2026, Tabla 2 p.25; PyG p.27): sueldos y salarios 1.410,4 + Seguridad Social y otros 160,4 = 1.570,8 miles EUR; base PyG, no capítulo 1",
  "Fuente de ejecución de personal": POA,
  "Estado de verificación de ejecución": "Fuente primaria cotejada contra fila y unidad milesEUR; no estimación; cifra provisional",
  "Cobertura presupuesto / personal / salarios": "Presupuesto operativo 2026 y gastos de personal 2026 (presupuestados) y 2025 (provisionales) verificados en el POA 2026; plantilla ocupada no publicada; efectivos autorizados previstos (63 a cierre de 2026) según PAP; cuentas anuales 2024/2025 no localizadas",
  "Puestos aprobados / presupuestados": 63,
  "Fecha puestos aprobados": "2026 (previsión a cierre del ejercicio)",
  "Base de puestos aprobados": "Efectivos autorizados por la DG de Función Pública con los que se prevé cerrar 2026 (Memoria PAP 2026-2028, p.26: '63 efectivos al final del ejercicio'; p.57: incorporación en 2026 de las 50 personas autorizadas en su oferta de empleo). Previsión/autorización, NO ocupación real. El PAP cita 130 plazas previstas en la constitución (p.57) y 83 empleados en 2028",
  "Fuente puestos aprobados": PAP,
  "Notas de personal y apoyo ministerial": "EPE con personal laboral propio (Estatuto RD 676/2024: art.18.1 Estatuto de los Trabajadores; art.18.3 retribuciones fijadas por el Director General según criterios del Consejo Rector, art.11.1.h; art.17.3 directivos sujetos al RD 451/2012). Plantilla actual no publicada (ni POA ni web de empleo). OPE publicada 29/12/2025: 49 plazas indefinidas (4 administrativas, 41 técnicas, 4 jefaturas; bases pp.1-2). La resolución de adjudicación (publicada sept. 2026) marca 38 filas 'ADJUDICADA', 6 'DESIERTA' y 5 'NO ADJUDICADA' (recuento de filas de la tabla, sin total oficial; no se usa como plantilla). Retribuciones de convocatoria (Anexo I de las bases OPE): administrativo E-4 parte fija 31.100 EUR + incentivo variable 2.000; técnico/a de Asesoría Jurídica E-4 45.000 EUR con incentivo variable 6.500; jefatura de departamento 70.000 EUR + incentivo variable 10.000. Previsión PAP 2026-2028 (p.57) de gastos de personal (incl. acción social y SS): 4,0 M (2026), 6,1 M (2027), 6,8 M (2028).",
  "Notas de conciliación de crédito y ejecución": "Serie de gastos de personal (PyG, miles EUR; POA 2026 Tabla 2 p.25 y PyG p.27): 2024 real 612,1 (sueldos 536,7; SS 75,4); 2025 provisional 1.570,8 (sueldos 1.410,4; SS y otros 160,4); 2026 presupuesto 4.000,0 (sueldos 2.934,1; SS y otros 1.065,9; en la PyG: SS a cargo de la empresa 821 + otros 244). No consta si 2024 incluye meses como SEMYS S.A. (la EPE inició su funcionamiento el 31/07/2024, PAP p.4). Cuentas anuales 2024/2025 auditadas no localizadas: el portal de transparencia remite al buscador de Rendición de Cuentas de Hacienda (no legible automáticamente). Por eso BO-BU quedan vacías: la cifra 2025 es provisional.",
  "Verificación anual / conciliación": "Sin cifra anual 2025 de cuentas anuales: solo la provisional de 1,5708 M (POA 2026), que no se lleva a BP. Nulo, NO cero."
 },
 "fuentes_nuevas": [POA, PAP, SETT_TR, SETT_EMP, SETT_OPE, SETT_RES, SETT_RD],
 "verificacion": "POA 2026 SETT (portal de transparencia, 'Plan Operativo Anual'): Tabla 2 'Gastos operativos SETT 2024-2026 (ppto)', p.25, miles EUR: fila 'Gastos de personal' 612,1 / 1.570,8 / 4.000,0 (2024 / 2025 / 2026 ppto); subfilas sueldos y salarios 536,7 / 1.410,4 / 2.934,1 y Seguridad Social y otros 75,4 / 160,4 / 1.065,9; 'Total gastos' 3.537,8 / 7.103,6 / 11.144,5. Cuenta de PyG p.27 (Real 2024 / Prov. 2025 / Ppto. 2026), miles EUR: 'Gastos de personal' -612 / -1.571 / -4.000, coherente con la Tabla 2. Texto p.24: 'El presupuesto operativo de gastos para el año 2026 ascenderá a 11,1 millones de euros'. Conversión: 11.144,5 miles = 11,1445 M; 4.000,0 miles = 4,0 M; 1.570,8 miles = 1,5708 M. Memoria PAP 2026-2028: p.26 '63 efectivos al final del ejercicio' (2026) y coste estimado de personal 2026 de 4,0 M€; p.57 '50 personas autorizadas en su oferta de empleo', 83 empleados en 2028, 130 plazas previstas en la constitución. Estatuto (RD 676/2024, copia en sett.gob.es): art.11.1.e) el Consejo Rector aprueba 'el plan anual de actuación, el programa de actuación plurianual, los presupuestos anuales de explotación y de capital'. Bases OPE (29/12/2025): 49 plazas; importes retributivos citados en el Anexo I. Criterio: se usa como presupuesto propio el 'presupuesto operativo de gastos' del POA por ser el presupuesto de funcionamiento publicado por la entidad; el POA no recoge la fecha de aprobación, lo que se advierte en el texto.",
 "no_encontrado": "Cuentas anuales 2024 y 2025 de la SETT (plantilla media y gastos de personal auditados): no publicadas en BOE según las búsquedas; el portal remite al buscador de Rendición de Cuentas (dinámico). Presupuestos de explotación y capital de la SETT en PGE/prórroga 2026: no localizados. Plantilla ocupada a una fecha: no publicada en POA, PAP ni en la web de empleo. Retribuciones de directivos: no publicadas en la página de transparencia (solo la descripción de la sección)."
})

# ---------------- ID 22 FPyC ----------------
res.append({
 "ID": 22,
 "updates": {
  "Presupuesto propio (EUR millones)": 2.027433,
  "Año del presupuesto": 2025,
  "Base del presupuesto numérico": "Presupuesto propio aprobado",
  "Corte del presupuesto numérico": "2025, plan de actuación aprobado por el Patronato el 28/02/2025",
  "Estado de cuantificación": "Cifra propia2025 verificada; actual2026 pendiente",
  "Presupuesto: texto completo": "Presupuesto 2025 del Plan de Actuación 2025 (apartado 5 'Presupuesto 2025', pp.17-18): total gastos 2.027.432,75 EUR = 2,027433 M EUR, igual al total de ingresos (transferencia a favor de la Fundación (PGE) 1.980.000; reintegro de ayudas 26.077,75; Comisión Europea, proyecto RE-TO, 21.355). Incluye ayudas monetarias (1.200.000 de concesión directa a federaciones + 146.077,75 de subvenciones contra la intolerancia) y gastos de personal 480.000. Plan aprobado el 28/02/2025 (cuentas anuales 2025, p.20). Ejecución 2025 (cuentas anuales 2025, documento fechado 24/06/2026): total gastos 2.084.510,21 EUR (Nota 3.1, p.7), de ellos ayudas monetarias 1.399.058,44 y gastos de personal 452.388,46 (cuenta de resultados, p.4); transferencia de la AGE 2025 por 1.980.000 EUR para gastos corrientes (aplicación 13.08.912O.441), imputada al ejercicio 1.860.000 (Nota 4.14 p.13; Nota 14.2 p.25). Plan de actuación o presupuesto 2026 no publicado en el portal (consulta 12/10/2026). La convocatoria 2026 de 130.000 EUR (columnas contextuales) es una línea parcial: no sumar.",
  "Personal: personas (ocupadas)": 8,
  "Año del personal": "2025",
  "Base del personal": "Personal de la Fundación en 2025 según Nota 13.3 de las cuentas anuales 2025 (p.21): 'en 2025 es de 8 personas a la espera de la incorporación de un nuevo efectivo aprobado por Tasa de reposición ordinaria'. La memoria no precisa si es media anual o plantilla a 31/12. Cumplimiento del plan: 5 asalariados en la actividad A1 y 3 en la A2 (pp.26-29)",
  "Estado de verificación del personal": ST_PERS,
  "Fuente del personal": FPYC_CA25,
  "Crédito de personal (EUR millones)": 0.48,
  "Año del coste de personal": 2025,
  "Base del coste de personal": "Gastos de personal presupuestados en el Plan de Actuación 2025 (apartado 5, pp.17-18): 480.000,00 EUR; base PyG de fundación, NO capítulo 1",
  "Estado de verificación del coste": "Presupuesto aprobado de la entidad; no gasto realizado ni solo salarios",
  "Fuente del coste": FPYC_PLAN25,
  "Gasto de personal ejecutado (EUR millones)": 0.452388,
  "Año del gasto de personal": 2025,
  "Corte de ejecución de personal": "2025 año completo (cuentas anuales 2025)",
  "Base de ejecución de personal": "Partida (64) 8. Gastos de personal de la cuenta de resultados 2025 (p.4): sueldos y salarios 345.249,20 + Seguridad Social a cargo de la entidad 105.326,86 + otros gastos sociales 1.812,40 (Nota 13.3, p.21) = 452.388,46 EUR; base PyG, no capítulo 1",
  "Fuente de ejecución de personal": FPYC_CA25,
  "Estado de verificación de ejecución": "Fuente primaria cotejada contra fila y unidad EUR; no estimación",
  "Cobertura presupuesto / personal / salarios": "Presupuesto propio 2025 aprobado (plan de actuación), gasto de personal 2025 ejecutado (cuentas anuales) y personal 2025 (8 personas) verificados; presupuesto 2026 no publicado",
  "Notas de personal y apoyo ministerial": "Fundación del sector público estatal con personal propio (no ministerial). Retribución de la Dirección General publicada en el portal de transparencia: 'Retribución básica: 50.000,00 euros' y 'Retribución complementaria: 23.917,14 euros' (página 'Información económica, presupuestaria y estadística', consulta 12/10/2026). Gastos de personal 2024: 479.883,05 EUR (comparativo de la cuenta de resultados 2025, p.4).",
  "Gasto personal 2025 reconocido anual (EUR millones)": 0.452388,
  "Año y corte anual personal": "2025: hasta31/12/2025, año completo",
  "Base anual de personal": "Gastos de personal de la cuenta de resultados (cuentas anuales 2025): sueldos, Seguridad Social y otros gastos sociales; base PyG, no obligaciones reconocidas de capítulo 1",
  "Fuente anual de personal": FPYC_CA25,
  "Verificación anual / conciliación": "Cuentas anuales 2025 (portal de transparencia; informe de auditoría 2025 publicado junto a ellas): fila '(64) 8. Gastos de personal' -452.388,46 EUR (2025) y -479.883,05 (2024), p.4. Fundación con contabilidad PGC-ESFL: no hay crédito de cierre ni pagos de capítulo 1 (BO y BQ vacías, NO cero)."
 },
 "fuentes_nuevas": [FPYC_CA25, FPYC_PLAN25, FPYC_INFO, FPYC_INFO2],
 "verificacion": "Cuentas anuales 2025 FPyC (PDF del portal, 77.335 caracteres, llega a la p.31): cuenta de resultados p.4, '(64) 8. Gastos de personal' -452.388,46 (2025) / -479.883,05 (2024) EUR; ayudas monetarias -1.399.058,44; Nota 3.1 p.7 total gastos -2.084.510,21; Nota 13.3 p.21 desglose 640/642/649 = 345.249,20 / 105.326,86 / 1.812,40 y texto '8 personas'; Nota 4.14 p.13 transferencia 1.980.000,00 (13.08.912O.441); Nota 14.2 p.25 concedido 1.980.000 / imputado 1.860.000 / pendiente 120.000; p.20 'Plan de Actuación aprobado el 28 de febrero de 2025'. Plan de Actuación 2025, apartado 5 pp.17-18: total ingresos = total gastos 2.027.432,75 EUR; gastos de personal 480.000,00. Conversión EUR→M: 2.027.432,75 = 2,027433 (6 decimales); 452.388,46 = 0,452388; 480.000 = 0,48. Advertencia: la suma de los cuadros por objetivo del plan (2.025.185,76) difiere en 2.246,99 EUR del total del apartado 5; se usa el total del apartado 5. Retribución de la Dirección General: texto literal de la página de transparencia.",
 "no_encontrado": "Plan de actuación o presupuesto 2026 (no enlazado en 'Planes de actuación'); PAIF en PGE/prórroga 2026; tabla global de cumplimiento del plan 2025 (el texto extraído de las cuentas termina en la actividad A2, p.31); número medio de empleados por categoría y plantilla a 31/12; resumen de cuentas en BOE (no buscado: las cuentas completas están en el portal)."
})

# ---------------- ID 14 Delegación VG ----------------
res.append({
 "ID": 14,
 "updates": {
  "Presupuesto: texto completo": "Sin presupuesto propio de entidad: centro directivo del Ministerio de Igualdad sin personalidad. Crédito identificable (columnas contextuales): servicio 30.03 'Delegación del Gobierno contra la Violencia de Género', PGE 2023 (Ley 31/2022), tomo Sección 30, pp.16-17, miles EUR: cap.1 2.556,06; cap.2 6.742,27; cap.4 53.618,00 (a CCAA 19.800; a familias e ISFL 33.768; al exterior 50); cap.6 16.623,54; total 79.539,87 = 79,53987 M EUR, todo en el programa 232C. El programa 232C suma 259.741,89 miles (259,74189 M), de los que 180.202,02 miles corresponden al servicio 30.02 Secretaría de Estado de Igualdad y contra la Violencia de Género (p.18): no imputables a la Delegación. 2026: presupuesto 2023 prorrogado (Ministerio de Hacienda, nota de 19/05/2026: crédito del cap.6 del programa 'dotada en el presupuesto para el año 2023, prorrogado para el año 2026', crédito inicial 16.623.540 EUR, idéntico al PGE 2023). El tomo de la prórroga 2026 no se ha podido cotejar, y la ejecución 2026 del servicio/programa no se ha localizado. No equivale al coste de la Delegación como organización: incluye transferencias e inversiones.",
  "Importe contextual (EUR millones; NO sumar)": 79.53987,
  "Año / periodo contextual": "2026 (prórroga del presupuesto 2023; importe del PGE 2023 Ley)",
  "Base contextual": "Crédito inicial del servicio 30.03 Delegación del Gobierno contra la Violencia de Género (programa 232C), PGE 2023 prorrogado a 2026; centro directivo sin personalidad, NO presupuesto propio de entidad; incluye transferencias (cap.4 53,618 M) e inversiones (cap.6 16,624 M)",
  "Nombre del titular del importe": "Delegación del Gobierno contra la Violencia de Género (servicio 30.03, Ministerio de Igualdad)",
  "Crédito de personal (EUR millones)": 2.55606,
  "Año del coste de personal": 2026,
  "Base del coste de personal": "Capítulo 1: crédito inicial del servicio 30.03 Delegación (programa 232C), PGE 2023 (Ley 31/2022) prorrogado a 2026: altos cargos 61,04 + funcionarios 2.138,89 + cuotas, prestaciones y gastos sociales 356,13 = 2.556,06 miles EUR. Importe del tomo PGE 2023; tomo de prórroga 2026 no cotejado",
  "Estado de verificación del coste": "Crédito autorizado, no gasto realizado ni solo salarios",
  "Fuente del coste": PGE23_S30,
  "Cobertura presupuesto / personal / salarios": "Crédito del servicio 30.03 (PGE 2023 prorrogado a 2026) en columnas contextuales y su capítulo 1 verificados; personal ocupado y ejecución 2026 no verificados",
  "Notas de conciliación de crédito y ejecución": "Prórroga: nota del Ministerio de Hacienda de 19/05/2026 (Consejo de Ministros, límites de compromisos del cap.6 del programa 'Actuaciones para la prevención integral de la violencia de género', solicitados por la Delegación): presupuesto 2023 'prorrogado para el año 2026'. El cap.6 de 2026 (16.623.540 EUR) coincide con el PGE 2023 (16.623,54 miles), lo que es coherente con la prórroga automática de los créditos iniciales; los demás capítulos de 2026 no se han cotejado en el tomo de prórroga. Ejecución (obligaciones) 2025 y 2026 del servicio 30.03: no localizada.",
  "Límites del juicio": "El programa 232C está compartido con la Secretaría de Estado (servicio 30.02); solo el servicio 30.03 es de la Delegación. Falta la ejecución 2026 del servicio y el tomo de prórroga 2026; personal ocupado no publicado."
 },
 "fuentes_nuevas": [PGE23_S30, HAC_NP],
 "verificacion": "Tomo PGE 2023 Ley, Sección 30 (L_23_E_G30.PDF): estado de gastos del servicio 30.03, pp.16-17, miles EUR, filas literales '10 Altos cargos 61,04', '12 Funcionarios 2.138,89', '16 Cuotas, prestaciones y gastos sociales a cargo del empleador 356,13', '45 A Comunidades Autónomas 19.800,00', '48 A familias e instituciones sin fines de lucro 33.768,00', '49 Al exterior 50,00', '6 INVERSIONES REALES 16.623,54', 'TOTAL DELEGACIÓN DEL GOBIERNO CONTRA LA VIOLENCIA DE GÉNERO 79.539,87'. Comprobación: 2.556,06+6.742,27+53.618,00+16.623,54 = 79.539,87. Resumen orgánico p.18: programa 232C = 180.202,02 (30.02) + 79.539,87 (30.03) = 259.741,89. Conversión: 79.539,87 miles = 79,53987 M; 2.556,06 miles = 2,55606 M. Nota de Hacienda 19/05/2026: 'dotada en el presupuesto para el año 2023, prorrogado para el año 2026'; 'con un crédito inicial de 16.623.540 euros' (cap.6), idéntico al PGE 2023.",
 "no_encontrado": "Tomo de la prórroga 2026 de la SEPG (PGE2026Prorroga, sección 30): no aparece en búsquedas y WebFetch exige procedencia. Ejecución 2025/2026 del programa 232C o del servicio 30.03: no localizada (la nota de Igualdad de 23/01/2026 solo da la ejecución agregada del ministerio, 95,97% en obligaciones). Personal de la Delegación: la RPT de personal laboral del Ministerio de Igualdad (vigencia 01/12/2024) solo recoge puestos laborales y su extracción es desordenada; la RPT de funcionarios no se ha localizado."
})

# ---------------- ID 23 OIReScon ----------------
res.append({
 "ID": 23,
 "updates": {
  "Notas de personal y apoyo ministerial": "Informe anual de actuaciones 2025 (aprobado el 06/03/2026): a efectos organizativos la Oficina está adscrita al MINHAC a través de su Subsecretaría (nota 7, p.21) y usa el Portal y la Sede Electrónica del MINHAC (pp.24 y 29). A 01/01/2025: RPT efectiva de 47 puestos y 30 ocupados (p.17), 63,83% (p.18); a 31/12/2025, ocupación de la RPT del 66,67% (p.18), sin número de puestos a esa fecha (no se infiere). El informe no da presupuesto, crédito ni coste de personal propio; el encargo a ISDEFE (3 años desde el 15/02/2026) figura sin importe. No se reparte crédito del Ministerio de Hacienda.",
  "Notas de conciliación de crédito y ejecución": "Sin crédito ni ejecución propios: el informe anual 2025 no los publica y la Oficina está adscrita a la Subsecretaría del MINHAC. Ocupación de la RPT: 63,83% a 01/01/2025 y 66,67% a 31/12/2025 (p.18)."
 },
 "fuentes_nuevas": [OIR],
 "verificacion": "Informe anual de actuaciones 2025 de la OIReScon: p.17 'la RPT efectiva de la Oficina la integraban 47 puestos', '30 se encontraban efectivamente ocupados a 1 de enero'; p.18 '63,83%' y 'a 31 de diciembre de 2025, el porcentaje de ocupación de la RPT era del 66,67%'; nota 7 p.21 'a efectos organizativos la Oficina está adscrita al MINHAC a través de su Subsecretaría'. No se modifican las cifras existentes (30 ocupadas; 47 puestos). No se añade ningún importe.",
 "no_encontrado": "Coste, crédito o gasto de personal propio de la OIReScon: el informe anual 2025 no los publica ni cita programa presupuestario. No se ha consultado el programa del MINHAC en la prórroga 2026 porque no hay servicio presupuestario propio identificado; tampoco se reparte."
})

# ---------------- ID 44 AAI Igualdad de Trato ----------------
r44 = BATCH[44]
res.append({
 "ID": 44,
 "updates": {
  "Presupuesto: texto completo": "No se ha identificado crédito propio separado. RD 606/2026, de 22 de julio (BOE-A-2026-16172), disposición transitoria única, apdo.1 (p.104854): 'Hasta que la Autoridad cuente con un presupuesto propio' ... 'su actividad se financiará con cargo a los créditos presupuestarios del Ministerio de Igualdad' ... 'que no afecten a los créditos del Instituto de las Mujeres, O.A.'; apdo.2 (p.104855): el Ministerio de Igualdad presta los servicios y el apoyo administrativo necesario hasta su puesta en funcionamiento en la fecha que determine una orden de la persona titular del Ministerio. Régimen futuro: anteproyecto de presupuesto aprobado por su órgano de gobierno y remitido a Hacienda (art.10.f, p.104864). Importe individual no verificado. IGAE 08.2026, bloque 'resto de entidades': no comprobado (extracción del PDF truncada en la p.27). La MAIN del proyecto de Estatuto (audiencia pública, nov. 2025, p.23) cita un presupuesto provisional 2025 de 112.447,76 EUR con cargo a las aplicaciones 30.01.232M.620, 22002 y 22706 del presupuesto prorrogado de Igualdad, y un coste 2026 con unidades internamente inconsistentes: es una previsión de proyecto, no crédito ni ejecución, y no se usa como cifra.",
  "Notas de personal y apoyo ministerial": r44["Notas de personal y apoyo ministerial"] + " Precisión con fuente: RD 606/2026, DT única apdo.1 (p.104854, financiación con créditos de Igualdad sin afectar al Instituto de las Mujeres), apdo.2 (p.104855, apoyo administrativo del Ministerio hasta la puesta en funcionamiento) y apdo.3 (cobertura inicial de los puestos de su RPT, posible por comisión de servicios). Personal propio: funcionario de carrera o laboral (art.19.1). La MAIN (nov. 2025, p.20) preveía una RPT provisional de 19 puestos: previsión de proyecto, no RPT aprobada ni ocupación."
 },
 "fuentes_nuevas": [RD606, MAIN_AAI],
 "verificacion": "BOE-A-2026-16172 (PDF, BOE núm. 180 de 25/07/2026; título comprobado: 'Real Decreto 606/2026, de 22 de julio, por el que se aprueba el Estatuto de la Autoridad Independiente para la Igualdad de Trato y la No Discriminación, A.A.I.'): DT única apdos.1-3 (pp.104854-104855), art.10.f-h (p.104864), art.19.1 (p.104870). MAIN del Estatuto (igualdad.gob.es, audiencia nov. 2025): p.23 presupuesto provisional 2025 de 112.447,76 EUR y aplicaciones 30.01.232M; p.20 RPT provisional de 19 puestos. No se añaden importes a columnas numéricas.",
 "no_encontrado": "IGAE ORGANISMOS 08.2026: la URL no aparece en los resultados de búsqueda (procedencia denegada) y, en las ediciones accesibles (12.2025), el texto extraído termina en la p.27, así que el bloque de pp.99-119 no es legible. Orden de puesta en funcionamiento de la Autoridad: no localizada (BOE-A-2026-19049 de la ficha no aparece en búsquedas). Transferencias de crédito a su favor: no localizadas. Texto del RD a partir del art.20.2: truncado en la extracción."
})

# ---------------- ID 45 AEval ----------------
r45 = BATCH[45]
res.append({
 "ID": 45,
 "updates": {
  "Presupuesto: texto completo": "No se ha localizado crédito propio separado. RD 65/2026, de 3 de febrero (BOE-A-2026-2553), disposición transitoria tercera (p.17526): 'Hasta que la Agencia cuente con un presupuesto propio, los gastos que conlleve su puesta en funcionamiento o su actividad' ... 'se financiarán con cargo a los créditos presupuestarios de la Secretaría de Estado' de la que dependía el Instituto; 'Hasta la aprobación de su presupuesto, la Agencia actuará de acuerdo con el régimen presupuestario' del Instituto. DT primera (p.17525): hasta la aprobación de la RPT de la Agencia, los puestos del Instituto 'subsistirán transitoriamente y serán retribuidos con cargo a los mismos créditos presupuestarios'. Recursos previstos: transferencias consignadas en los PGE e ingresos propios (art.41.1, p.17546); presupuesto de gastos limitativo por su importe global y equilibrado (art.42.2). Puesta en funcionamiento con la sesión constitutiva del Consejo Rector (DA primera, p.17524; según la ficha, 24/04/2026), que suprime el Instituto. Presencia en la IGAE 08.2026: no comprobada (extracción del PDF truncada en la p.27). No cuantificado.",
  "Notas de personal y apoyo ministerial": r45["Notas de personal y apoyo ministerial"] + " Precisión con fuente: RD 65/2026, DT tercera (p.17526, gastos con cargo a los créditos de la Secretaría de Estado hasta tener presupuesto propio); DT primera (p.17525, puestos del Instituto subsisten y se retribuyen con los mismos créditos hasta la RPT de la Agencia); DA sexta (p.17525, integración del personal funcionario del Instituto y subrogación del laboral). El RD no fija número de puestos ni plantilla; la RPT la aprueba el Consejo Rector (arts.16.i y 30.2)."
 },
 "fuentes_nuevas": [RD65],
 "verificacion": "BOE-A-2026-2553 (PDF, BOE de 04/02/2026; título comprobado: 'Real Decreto 65/2026, de 3 de febrero, por el que se aprueba el Estatuto de la Agencia Estatal de Evaluación de Políticas Públicas'): DT tercera p.17526; DT primera p.17525; DA sexta p.17525; DA primera p.17524; arts.41.1 y 42.2 p.17546; art.16.i p.17535; art.30.2 p.17542. Páginas tomadas de los pies del texto extraído. Ninguna cifra numérica.",
 "no_encontrado": "IGAE ORGANISMOS 08.2026 (bloque resto de entidades): no legible (procedencia y truncado en la p.27). Presupuesto propio 2026, plan de acción o RPT de la Agencia: no localizados. Frase 'no supondrá incremento del gasto': no aparece en el RD."
})

# ---------------- ID 46 AESAP ----------------
r46 = BATCH[46]
res.append({
 "ID": 46,
 "updates": {
  "Presupuesto: texto completo": "Sin presupuesto propio individual identificado. No se atribuye a la agencia la inversión de vigilancia sanitaria ni el presupuesto de Sanidad. Orden PJC/101/2026 (BOE-A-2026-3787, 18/02/2026, p.25284): la Agencia podría operar 'de manera inmediata desde la sede central del Ministerio de Sanidad' mientras no se fije su sede, y el real decreto de Estatuto 'se encuentra en una fase muy avanzada de tramitación'; el acuerdo de urgencia de 18/11/2025 citaba el hito CID 281 (componente 18 del PRTR), que incluye equipamiento tecnológico de la Agencia, sin importe. Orden PJC/781/2026 (BOE-A-2026-16527, 29/07/2026, p.106639): recuerda que la Ley 7/2025 fijó seis meses para aprobar el Estatuto y no indica que se haya aprobado. Las cifras de la candidatura de Zaragoza incluidas en esa orden (316 puestos de trabajo en la sede definitiva y 67 en la provisional; obras por 20.256.380,23 EUR; mantenimiento asumido por el Gobierno de Aragón durante cinco años; pp.106654-106656) son compromisos de la candidatura autonómica, NO presupuesto ni plantilla de la AESAP. Ley 7/2025 (arts.4-5, régimen económico y presupuestario): no releída en BOE.",
  "Notas de personal y apoyo ministerial": r46["Notas de personal y apoyo ministerial"] + " Precisión con fuente: Orden PJC/101/2026 (BOE-A-2026-3787, p.25284), operación provisional desde la sede central del Ministerio de Sanidad y Estatuto en tramitación (feb. 2026); Orden PJC/781/2026 (BOE-A-2026-16527), sede física en Zaragoza, sin regular plantilla ni presupuesto. Estatuto aprobado: no localizado a 12/10/2026."
 },
 "fuentes_nuevas": [AESAP1, AESAP2],
 "verificacion": "BOE-A-2026-3787 (título comprobado: 'Orden PJC/101/2026, de 17 de febrero, por la que se publica el Acuerdo del Consejo de Ministros de 17 de febrero de 2026, por el que se modifica el plazo de resolución del procedimiento para la determinación de la sede física de la Agencia Estatal de Salud Pública', pp.25284-25285). BOE-A-2026-16527 (título comprobado: 'Orden PJC/781/2026, de 28 de julio, por la que se publica el Acuerdo del Consejo de Ministros de 28 de julio de 2026, por el que se determina la sede física de la Agencia Estatal de Salud Pública', BOE núm.184, p.106638 y ss.). Ninguna cifra se lleva a columnas numéricas.",
 "no_encontrado": "Ley 7/2025 en BOE (arts.4-5 y disposiciones): la URL eli no aparece en resultados (procedencia denegada) e iberley solo da el índice. Real decreto de Estatuto de la AESAP: no localizado en búsquedas. IGAE 08.2026: no legible (procedencia y truncado en la p.27). Presupuesto de constitución o transferencias de crédito: no localizados."
})

# ---------------- ID 65 CNF ----------------
r65 = BATCH[65]
res.append({
 "ID": 65,
 "updates": {
  "Estado de cuantificación": "Sin presupuesto propio: órgano sin dotación diferenciada (verificado en norma)",
  "Presupuesto: texto completo": "Sin presupuesto propio. RD 670/2023, de 18 de julio (BOE-A-2023-16819): art.1.1, centro 'de titularidad y gestión estatal' que 'dependerá orgánica y funcionalmente de la Dirección General de Patrimonio Cultural y Bellas Artes', a través de la Subdirección General de Museos Estatales; art.2.1, 'La naturaleza jurídica del Centro Nacional de Fotografía es la de un museo de titularidad estatal' (Reglamento de Museos de Titularidad Estatal, RD 620/1987), sin personalidad jurídica propia; art.8.2.c, el Patronato conoce el 'anteproyecto de presupuesto que deberá presentar la Subdirección General de Museos Estatales'; disposición adicional segunda: los gastos de creación 'serán atendidos con cargo a los créditos presupuestarios del Ministerio de Cultura y Deporte' y 'Lo dispuesto en este real decreto no supondrá incremento del gasto público'. Sin importe específico identificable (la inversión en la sede de Soria no se ha verificado en fuente primaria). No se reparte el presupuesto del Ministerio de Cultura.",
  "Cobertura presupuesto / personal / salarios": "Sin presupuesto propio (verificado en norma: museo estatal sin personalidad, créditos del Ministerio de Cultura); personal y salarios no desglosados; no significa cero coste",
  "Notas de personal y apoyo ministerial": r65["Notas de personal y apoyo ministerial"] + " Precisión con fuente (RD 670/2023): museo de titularidad estatal sin personalidad (arts.1.1 y 2.1); la DA primera prevé aprobar 'la relación de puestos de trabajo necesaria' (RPT no localizada); la Secretaría del Patronato corresponde a un funcionario de carrera de subgrupo A2 como mínimo (art.5.e); la Dirección se provee conforme al TREBEP (art.11.1). Pregunta parlamentaria de 19/05/2026 (Congreso, registro 114946) sobre la constitución del Patronato, presupuesto y personal: respuesta no localizada."
 },
 "fuentes_nuevas": [CNF_INAP, CNF_CONG],
 "verificacion": "Contenido del RD 670/2023 leído a través de la reseña oficial del INAP ('La Administración al Día', noticia 1235579), que cita literalmente el art.2.1 ('La naturaleza jurídica del Centro Nacional de Fotografía es la de un museo de titularidad estatal'), el art.1.1 ('titularidad y gestión estatal'; 'dependerá orgánica y funcionalmente de la Dirección General de Patrimonio Cultural y Bellas Artes'), el art.8.2.c y la DA segunda ('Lo dispuesto en este real decreto no supondrá incremento del gasto público'; 'serán atendidos con cargo a los créditos presupuestarios del Ministerio de Cultura y Deporte'). El BOE (BOE-A-2023-16819, ya en la ficha) no se ha podido releer directamente porque no aparece en resultados de búsqueda: conviene un cotejo final en BOE. Ninguna cifra numérica.",
 "no_encontrado": "Texto del BOE-A-2023-16819 leído directamente (procedencia denegada); RPT del Centro; importe de la obra de la sede o de un convenio específico en fuente primaria (solo prensa: 'presupuesto de 85 millones', no usado); respuesta del Gobierno a la pregunta 114946."
})

# ---------------- ID 42 AEAD ----------------
r42 = BATCH[42]
res.append({
 "ID": 42,
 "updates": {
  "Verificación anual / conciliación": r42["Verificación anual / conciliación"] + " Revisión 12/10/2026 (2ª ronda): ORGANISMOS 12. 2025 es accesible por WebFetch, pero su texto extraído tiene 60.454 caracteres y termina en la p.27 (tablas de ingresos de OOAA); un offset de 200.000 no devuelve nada. El bloque de gastos por capítulos de 'resto de entidades' (pp.99-119) sigue sin poder cotejarse. La búsqueda de cuentas anuales 2025 o plan de acción de la AEAD en BOE solo devuelve convenios (p. ej. BOE-A-2026-7887, convenio AEAD-Tribunal de Cuentas, sin cifras presupuestarias). Nulo, NO cero."
 },
 "fuentes_nuevas": [],
 "verificacion": "Sin cifra nueva. Se comprobó que la edición IGAE 12.2025 se lee solo hasta la p.27: en la p.23 y la p.26 aparece la fila de ingresos del Ministerio 'PARA LA TRANSF. DIGITAL Y LA FUNCIÓN PÚBL.', no la AEAD. BOE-A-2026-7887 (título comprobado: Resolución de 24/03/2026 de la Subsecretaría de Presidencia que publica el convenio AEAD-Tribunal de Cuentas): contribución de 6.000 EUR anuales del Tribunal a la AEAD, que no es presupuesto ni gasto de personal.",
 "no_encontrado": "BO-BU (anual 2025): no legibles en IGAE 12.2025 por truncado de la extracción en la p.27. Cuentas anuales 2025 de la AEAD: no localizadas. Puestos RPT: no localizados."
})

# ---------------- ID 5 AIReF ----------------
res.append({
 "ID": 5,
 "updates": {},
 "fuentes_nuevas": [],
 "verificacion": "Sin cifra nueva; no se modifica ningún campo.",
 "no_encontrado": "Personas ocupadas y RPT de la AIReF: la Memoria anual 2025 (airef.es) sigue devolviendo ROBOTS_DISALLOWED en WebFetch. La búsqueda de una copia oficial alternativa (memoria o plantilla a 31/12/2025) solo devolvió estadísticas generales de empleo público, sin desglose de la AIReF. No se usa prensa."
})

# ---------- validation ----------
ids = sorted(e["ID"] for e in res)
assert ids == sorted(BATCH.keys()), ids
for e in res:
    for k in e["updates"]:
        if k not in HEAD:
            print("BAD KEY", e["ID"], k); sys.exit(1)
json.dump(res, open(OUT, 'w'), ensure_ascii=False, indent=1)
print("written", OUT, len(res))
