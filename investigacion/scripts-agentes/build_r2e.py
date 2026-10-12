import json

OUT = "datos/resultados/R2E_varias.json"

CLM_JUL = "https://intervencion.castillalamancha.es/sites/default/files/Ejecucion%20Presupuestaria%20Julio_2026.pdf"
CLM_MAY = "https://intervencion.castillalamancha.es/sites/default/files/Ejecuci%C3%B3n%20Mayo%202026.pdf"
CLM_PROY = "https://www.castillalamancha.es/sites/default/files/documentos/archivosnoticias/20251021/proyecto_ley_presupuestos_clm_2026.pdf"
CYL_D52 = "https://sirdoc.ccyl.es/Biblioteca/Dosieres/DL203AtencionViolenciaGenero/pdfs/CyL-Decreto-52-2014-Observatorio.pdf"
CYL_INAP = "https://laadministracionaldia.inap.es/noticia.asp?id=1132927"
EXT_ORD26 = "https://doe.juntaex.es/pdfs/doe/2026/1040o/26050065.pdf"
EXT_D190 = "https://doe.juntaex.es/pdfs/doe/2007/840o/07040203.pdf"
AGENEX_LEY = "https://www.boe.es/boe/dias/2026/07/11/pdfs/BOE-A-2026-15131.pdf"
AGENEX_ENC = "https://doe.juntaex.es/pdfs/doe/2026/380o/26060465.pdf"
AUK_CC24 = "https://www.euskadi.eus/contenidos/informacion/cuentas_anuales_ee_sspp_2024/es_def/adjuntos/2024/3_6_19_AUKERAK.pdf"
AUK_FICHA23 = "https://www.euskadi.eus/contenidos/entidad/soc_publica_245/es_def/adjuntos/2023425.pdf"
CIB_FICHA24 = "https://www.euskadi.eus/contenidos/entidad/soc_publica_422/eu_def/adjuntos/2024422.pdf"
EKP_CC24 = "https://ekp.euskadi.eus/contenidos/informacion/ekp_transparencia/eu_def/adjuntos/CCAA24-EKP_signed.pdf"
EKP_FICHA24 = "https://www.euskadi.eus/contenidos/entidad/soc_publica_53/eu_def/adjuntos/2024495.pdf"
PV_SEC07 = "https://www.euskadi.eus/contenidos/informacion/presupuestos_cae/es_def/adjuntos/pdfs/2026A/07_Segurtasuna_Seguridad.pdf"
PV_RES = "https://www.euskadi.eus/contenidos/informacion/presupuestos_cae/es_def/adjuntos/pdfs/2026A/Laburpenak_Resumenes.pdf"

PV_TRUNC = ("Los PDF de Presupuestos 2026 de euskadi.eus (secciones 07, 15 y 16 y 'Resúmenes', cuyo índice sitúa los "
            "entes públicos de derecho privado en pp. 227-233) solo son extraíbles hasta ~p. 24 con la herramienta "
            "(el texto convertido acaba ahí aunque se use offset); los presupuestos de explotación por entidad no se alcanzan. "
            "Cuentas anuales 2025 (serie cuentas_anuales_ee_sspp_2025) no localizadas en buscadores.")

rows = []

# ---------------- CLM 117 ----------------
rows.append({
    "ID": 117,
    "updates": {
        "Notas de conciliación de crédito y ejecución": (
            "Fuente de crédito y ejecución identificada pero NO extraída: la Intervención General de la JCCM publica la ejecución "
            "mensual por organismo (informe 'Ejecución presupuestaria' julio 2026, índice: 'Agencia de Investigación e Innovación', "
            "gastos por secciones y subconcepto p. 321, ingresos p. 327; informe de mayo 2026: pp. 316/322), con columnas C.Inicial, "
            "Definitivo, Autorizado, Comprometido, Obligado y Pagado, en euros. La extracción automática del PDF se corta en la sección 11 "
            "(Presidencia), antes de los organismos autónomos, por lo que no se rellena ninguna cifra. Para completar: abrir manualmente "
            "p. 321 del informe de julio 2026 (crédito inicial y obligaciones cap.1 a 31/07/2026)."
        ),
    },
    "fuentes_nuevas": [CLM_JUL, CLM_MAY],
    "verificacion": (
        "Informes de ejecución de la Intervención General JCCM (mayo y julio 2026): el índice confirma que el organismo tiene tablas propias "
        "de gastos e ingresos (julio: pp. 321 y 327; mayo: pp. 316 y 322), unidad euros, columnas C.Inicial/Definitivo/Autorizado/"
        "Comprometido/Obligado/Pagado. El texto extraíble termina (~60.000 caracteres) en la sección 11; con offset no hay más texto. "
        "Ninguna cifra individual verificada; no se añade importe."
    ),
    "no_encontrado": (
        "Crédito inicial 2026, cap.1 y ejecución del OA: el estado de gastos por organismos de la Ley 5/2025 (tomos de presupuestos) no "
        "aparece en buscadores; el resumen del Proyecto 2026 de la Consejería (21/10/2025, tabla 'Gasto por secciones') no tiene fila de la "
        "Agencia de Investigación e Innovación; los informes mensuales de la Intervención (que sí la incluyen) no son extraíbles más allá de la "
        "sección 11. El Decreto 5/2026 (DOCM 3/03/2026, modifica estatutos, vía INAP) no contiene cifras de presupuesto ni plantilla. "
        "Plantilla/RPT y liquidación 2025 no localizadas."
    ),
})

# ---------------- CLM 118 ----------------
rows.append({
    "ID": 118,
    "updates": {
        "Presupuesto: texto completo": (
            "Organismo autónomo con presupuesto propio (sección 77 'Agencia de Transformación Digital de Castilla-La Mancha') en la Ley 5/2025, "
            "de 19 de diciembre, de Presupuestos Generales JCCM 2026 (DOCM 29/12/2025), art. 1.1.c.6º; el art. 9.2.c.2º cita créditos de capítulo 1 "
            "de la sección 77. Importe aprobado individual no verificado: el articulado no lo da; no significa cero. Pista oficial NO utilizable "
            "como cifra aprobada: el resumen del Proyecto de Ley de Presupuestos 2026 publicado por la JCCM (castillalamancha.es, 21/10/2025, tabla "
            "'Gasto por secciones', millones EUR) recoge 'Agencia Transformación Digital 142,3 [2025] 182,5 [2026] 40,2 28,2 [%]'; es proyecto (no "
            "estado de gastos de la Ley 5/2025) y cifra redondeada a 0,1 M, por lo que no se rellena el presupuesto propio. No atribuir presupuesto "
            "del departamento."
        ),
        "Notas de conciliación de crédito y ejecución": (
            "Fuente de ejecución identificada pero NO extraída: los informes mensuales de ejecución de la Intervención General JCCM (mayo y julio "
            "2026) incluyen en el índice 'Agencia de Transformación Digital' dentro de 'Organismos Autónomos y Entidades Públicas' (sin número de "
            "página en el texto extraído), con columnas C.Inicial/Definitivo/Autorizado/Comprometido/Obligado/Pagado en euros; la extracción del "
            "PDF se corta en la sección 11. Proyecto 2026 (no aprobado): 182,5 M frente a 142,3 M en 2025 (resumen de la Consejería). Sin cifra de "
            "cap.1 ni ejecución verificada."
        ),
    },
    "fuentes_nuevas": [CLM_PROY, CLM_JUL],
    "verificacion": (
        "Resumen del Proyecto de Ley de Presupuestos CLM 2026 (PDF de castillalamancha.es, archivosnoticias 20251021), tabla 'GASTO POR "
        "SECCIONES': fila literal 'Agencia Transformación Digital 142,3 182,5 40,2 28,2' (columnas 2025, 2026, variación absoluta, variación %; "
        "unidad millones EUR según los totales de la tabla; 182,5-142,3=40,2 y 40,2/142,3=28,2 % cuadran). Documento sin numeración de página. "
        "Solo se usa en texto: es proyecto, no ley aprobada. Informe de ejecución julio 2026: el índice lista la Agencia, sin datos extraíbles."
    ),
    "no_encontrado": (
        "Crédito inicial aprobado 2026 de la sección 77 (estado de gastos de la Ley 5/2025), cap.1, ejecución 2026 (informes mensuales de la "
        "Intervención no extraíbles más allá de la sección 11), liquidación 2025 y plantilla/RPT: no localizados en documento extraíble."
    ),
})

# ---------------- CyL 85 ----------------
rows.append({
    "ID": 85,
    "updates": {
        "Estado de cuantificación": "Sin presupuesto propio: órgano sin dotación diferenciada (verificado en norma)",
        "Presupuesto: texto completo": (
            "Sin presupuesto propio (verificado en norma). El Decreto 8/2006, de 16 de febrero, que creó el Observatorio para la Convivencia "
            "Escolar de Castilla y León, fue derogado por el Decreto 52/2014, de 16 de octubre, por el que se crea y regula el Observatorio de la "
            "Comunidad de Castilla y León (BOCyL núm. 201, 20/10/2014), disposición derogatoria c), p. 71664. Sus funciones pasan a la 'sección de "
            "convivencia escolar' del nuevo Observatorio (art. 4.1.c y art. 7), órgano colegiado adscrito a la Consejería de la Presidencia (art. 2.1). "
            "Art. 12 (p. 71663): 'La Consejería de la Presidencia atenderá, con cargo a sus medios personales y materiales, las necesidades derivadas "
            "del funcionamiento del observatorio'. Disposición adicional primera (p. 71663): la condición de vocal y la asistencia a las sesiones 'no "
            "generarán en ningún caso derecho a la percepción de ninguna cuantía económica'. No se atribuye presupuesto de la Consejería. Vigencia "
            "posterior del Decreto 52/2014 no auditada."
        ),
        "Estado legal y operativo": (
            "Decreto 8/2006 derogado por el Decreto 52/2014 (disp. derogatoria c); desde 2014 es la sección de convivencia escolar del Observatorio "
            "de la Comunidad de Castilla y León (art. 4.1.c, art. 7), órgano colegiado adscrito a la Consejería de la Presidencia; no contar como "
            "órgano original intacto. Actividad 2026 no auditada."
        ),
        "Estado de verificación del personal": "Sin plantilla propia: medios personales de la Consejería de la Presidencia (verificado en norma, Decreto 52/2014, art. 12)",
        "Estado de verificación del coste": "Sin crédito de personal propio: órgano sin dotación diferenciada (verificado en norma)",
        "Estado de verificación de ejecución": "Sin ejecución propia: órgano sin dotación diferenciada (verificado en norma)",
        "Cobertura presupuesto / personal / salarios": (
            "Sin presupuesto ni plantilla propios (verificado en norma: Decreto 52/2014, art. 12 y DA 1ª); funcionamiento con medios de la "
            "Consejería de la Presidencia, sin importe identificable; vocales sin retribución ni asistencias"
        ),
        "Notas de personal y apoyo ministerial": (
            "Sin plantilla propia: la Consejería de la Presidencia atiende el funcionamiento 'con cargo a sus medios personales y materiales' "
            "(Decreto 52/2014, art. 12); el secretario de la sección de convivencia escolar es el del Comité permanente (art. 7.3); vicepresidencia "
            "de la consejería de educación (art. 7.2). Vocales sin derecho a 'ninguna cuantía económica' (DA 1ª). Los vocales no son plantilla."
        ),
    },
    "fuentes_nuevas": [CYL_D52, CYL_INAP],
    "verificacion": (
        "Decreto 52/2014, de 16 de octubre (BOCyL núm. 201, 20/10/2014, pp. 71658-71664), copia en el dossier de las Cortes de CyL (sirdoc.ccyl.es) "
        "y texto reproducido por INAP: art. 2.1 órgano colegiado adscrito a la Consejería de la Presidencia (p. 71658); art. 4.1.c y art. 7.1-7.4 "
        "sección de convivencia escolar (pp. 71661-71662); art. 12 medios personales y materiales de la Consejería (p. 71663); DA 1ª sin percepción "
        "económica (p. 71663); disp. derogatoria c) deroga el Decreto 8/2006 (p. 71664). No contiene cláusula literal 'no supondrá incremento del "
        "gasto', pero sí atribución expresa a medios de la Consejería y gratuidad de vocales: se aplica la regla 6. Sin importe contextual identificable."
    ),
    "no_encontrado": "Texto del Decreto 8/2006 original no leído (derogado). Modificaciones posteriores del Decreto 52/2014 no auditadas.",
})

# ---------------- Extremadura 88 ----------------
rows.append({
    "ID": 88,
    "updates": {
        "Estado legal y operativo": (
            "Vigente y con actividad formal en 2026: Orden de 27 de mayo de 2026 de la Consejería de Educación y FP (DOE núm. 104, 2/06/2026, "
            "pp. 23357-23358) cesa y nombra vocales del Observatorio para la Convivencia Escolar en Extremadura, citando el art. 7 del Decreto 28/2007 "
            "(DOE núm. 24, 27/02/2007) como norma de creación, sin modificarlo; mandato de cuatro años. Naturaleza: 'órgano colegiado, de carácter "
            "consultivo' que se relaciona administrativamente con la Consejería a través de la Dirección General de Política Educativa (Decreto "
            "190/2007, estructura orgánica de la Consejería de Educación, arts. 1.6 y 3.3, DOE núm. 84, 21/07/2007; estructura de 2007). Dotación "
            "propia y régimen de indemnizaciones no verificados."
        ),
        "Notas de personal y apoyo ministerial": (
            "Vocales nombrados y cesados por orden de la Consejería (Orden 27/05/2026, DOE 104); los vocales no son plantilla. La Orden no regula "
            "indemnizaciones ni medios. Cláusulas del Decreto 28/2007 sobre secretaría, medios de la Consejería, gasto e indemnizaciones no "
            "verificadas (texto del decreto no accesible en esta revisión)."
        ),
    },
    "fuentes_nuevas": [EXT_ORD26, EXT_D190],
    "verificacion": (
        "Orden de 27/05/2026 (DOE núm. 104, 2/06/2026, pp. 23357-23358, código 2026050065): apartados Primero (cese) y Segundo (nombramiento) de "
        "vocales; cita Decreto 28/2007 de 20 de febrero (DOE núm. 24, 27/02/2007) como norma de creación y su art. 7; sin derogatoria ni cláusulas de "
        "gasto. Decreto 190/2007 (DOE núm. 84, 21/07/2007, pp. 12669-12672): art. 1.6 naturaleza consultiva y art. 3.3 relación vía DG de Política "
        "Educativa. Estado de cuantificación NO cambiado: la regla 6 exige leer el Decreto 28/2007."
    ),
    "no_encontrado": (
        "Texto del Decreto 28/2007: el PDF de educarex de la ficha da PROVENANCE_REQUIRED; las búsquedas devolvieron el Decreto 50/2007, el "
        "Compromiso Social por la Convivencia (2006), un informe sindical y el Decreto 190/2007, ninguno con el articulado del 28/2007. Sin cláusula "
        "de gasto/medios/indemnizaciones verificada."
    ),
})

# ---------------- Extremadura 122 AGENEX ----------------
rows.append({
    "ID": 122,
    "updates": {
        "Presupuesto: texto completo": (
            "Sin cifra propia 2026 verificada; no significa cero. Ley 1/2026, de 2 de julio (BOE-A-2026-15131, BOE 11/07/2026): art. 12.2, el "
            "presupuesto de AGENEX, de carácter estimativo, 'se integrará en los Presupuestos Generales de la Comunidad Autónoma de Extremadura' "
            "(p. 96709); recursos del art. 7 (dotaciones anuales de la Ley de Presupuestos, encargos/convenios, subvenciones, patrimonio; p. 96708); "
            "actividad en mercado libre limitada al 20 % (art. 5.5). A 18/02/2026 seguía operando como consorcio: Resolución de 18/02/2026 (DOE núm. "
            "38, 25/02/2026) le encomienda trabajos técnicos de gestión de ayudas de la DG de Industria, Energía y Minas, sin obligaciones ni compromisos "
            "económicos para las partes. Presupuesto 2026 del consorcio o de la EPE no localizado. No atribuir presupuesto de la consejería."
        ),
        "Estado legal y operativo": (
            "EPE de la Junta de Extremadura (no de la Diputación), con personalidad jurídica, patrimonio y tesorería propios, adscrita a la "
            "Consejería competente en energía (Ley 1/2026, art. 1, p. 96704). Antecedente: Consorcio AGENEX constituido por convenio de 23/12/2021 "
            "entre la Junta y las Diputaciones de Cáceres y Badajoz; Cáceres se separó (pleno 31/10/2024); la Asamblea General de 13/12/2024 acordó la "
            "disolución con cesión global de activos y pasivos a la nueva entidad (exposición de motivos, pp. 96701-96702). DA 1ª: integración global "
            "y sucesión universal; DA 2ª: subrogación del personal; DF 2ª: efectos solo con la extinción efectiva del consorcio, previa aprobación del "
            "proyecto de cesión global (p. 96712). DT única: hasta aprobar estatutos rige la normativa del consorcio. Extinción efectiva no verificada "
            "(en febrero de 2026 seguía como consorcio)."
        ),
        "Notas de personal y apoyo ministerial": (
            "Personal laboral (Ley 1/2026, art. 8.1), selección por convocatoria pública (art. 8.2); posible incorporación de empleados públicos de la "
            "Junta (art. 8.3). DA 2ª: el personal del consorcio se incorpora a AGENEX con subrogación y reconocimiento de antigüedad, con efectos a la "
            "extinción efectiva del consorcio (DF 2ª). La ley no fija número de efectivos ni memoria económica."
        ),
        "Cobertura presupuesto / personal / salarios": (
            "Naturaleza y régimen verificados (EPE de la Junta, Ley 1/2026); presupuesto 2026, personal y gastos de personal no verificados; vacío no "
            "significa cero"
        ),
    },
    "fuentes_nuevas": [AGENEX_LEY, AGENEX_ENC],
    "verificacion": (
        "Ley 1/2026 de Extremadura (PDF BOE-A-2026-15131): art. 1 (p. 96704) naturaleza EPE de la Junta y adscripción; art. 2.1 régimen; art. 6.5.b "
        "anteproyecto de presupuesto (p. 96707); art. 7 recursos y art. 8 personal (p. 96708); art. 12 régimen presupuestario y art. 13 control de la "
        "Intervención General (p. 96709); DA 1ª y 2ª (p. 96709); DT única (p. 96711); DF 2ª (p. 96712); exposición de motivos pp. 96701-96703 "
        "(socios del consorcio y disolución). Resolución de 18/02/2026 (DOE 38, 25/02/2026): AGENEX descrita como consorcio; sin cifras."
    ),
    "no_encontrado": (
        "Presupuesto 2026 (ley de presupuestos de Extremadura 2026 o prórroga) con dotación del consorcio/EPE, PyG/gastos de personal, plantilla y "
        "acto de extinción efectiva del consorcio/proyecto de cesión aprobado: no localizados (cupo de búsquedas agotado)."
    ),
})

# ---------------- Cataluña ----------------
rows.append({"ID": 86, "updates": {}, "fuentes_nuevas": [],
    "verificacion": "Sin cambios.",
    "no_encontrado": ("Plantilla ocupada (memòria 2025 ATC), ejecución cap.1 2026 y liquidación 2025: la búsqueda solo devolvió prensa (no fuente de "
                      "cifra) y el Annex de personal ya usado (AP_7910). Memoria/portal de transparencia de la ATC no localizados.")})
rows.append({"ID": 87, "updates": {}, "fuentes_nuevas": [],
    "verificacion": "Sin cambios.",
    "no_encontrado": ("Dotaciones 2026 (Annex de personal, servei OA01): el fichero wpres/2026/pdf/AP_OA01.pdf no aparece en buscadores (solo versiones "
                      "2016 y 2022) y WebFetch lo rechaza (PROVENANCE_REQUIRED). Memòria 2025 de la Oficina (plantilla) no localizada; solo prensa y "
                      "memorias de otros entes.")})
rows.append({"ID": 110, "updates": {}, "fuentes_nuevas": [],
    "verificacion": "Sin cambios.",
    "no_encontrado": "No priorizado en esta ronda (cupo de búsquedas); ejecución cap.1 2026, cuentas 2025 y plantilla ocupada siguen pendientes."})

# ---------------- Galicia ----------------
GAL_NF = ("Prazas orzamentadas 2026: el anexo de persoal de OOAA/axencias existe en la serie del Parlamento como PERS_OOAA_<año>.PDF "
          "(aparecen 2024 y 2025 en buscadores), pero PERS_OOAA_2026.PDF no aparece y WebFetch lo rechaza (PROVENANCE_REQUIRED). Ejecución cap. I 2026 "
          "y Conta Xeral 2025 no localizadas.")
rows.append({"ID": 89, "updates": {}, "fuentes_nuevas": [], "verificacion": "Sin cambios.", "no_encontrado": GAL_NF})
rows.append({"ID": 121, "updates": {}, "fuentes_nuevas": [], "verificacion": "Sin cambios.", "no_encontrado": GAL_NF})

# ---------------- Madrid 96 ----------------
rows.append({"ID": 96, "updates": {}, "fuentes_nuevas": [],
    "verificacion": "Sin cambios.",
    "no_encontrado": ("Gastos de personal 2026 (presupuesto de explotación) y cuentas 2025 de AMAPAD: el resumen del Proyecto 2026 de la CAM "
                      "(comunidad.madrid/file/497589) no menciona la agencia; libro de empresas/entes 2026 no aparece en buscadores; la página "
                      "institucional de AMAPAD no enlaza cuentas ni presupuesto 2025-2026. Solo constan cuentas 2024 (ya en notas).")})

# ---------------- Murcia ----------------
rows.append({"ID": 91, "updates": {}, "fuentes_nuevas": [],
    "verificacion": "Sin cambios.",
    "no_encontrado": ("Contrato-programa 2026 (BORM 168, 23/07/2026, anuncio 844337): el texto extraíble termina en p. 17992 (apdo. A02 Comunicación) "
                      "también con offset; no contiene gastos de personal, plantilla ni presupuesto administrativo/explotación (p. 17976 solo dice que "
                      "los presupuestos 2026 del ITREM se configuran según el Plan; p. 17978: aportación 2025 de 250.000 EUR al consorcio Vías Verdes, "
                      "no es personal). Anexo económico y cuentas 2025 no localizados.")})
rows.append({"ID": 120, "updates": {}, "fuentes_nuevas": [],
    "verificacion": "Sin cambios.",
    "no_encontrado": "No priorizado en esta ronda (cupo de búsquedas); crédito propio 2026 y personal siguen pendientes."})

# ---------------- C. Valenciana ----------------
rows.append({"ID": 95, "updates": {}, "fuentes_nuevas": [],
    "verificacion": "Sin cambios.",
    "no_encontrado": ("Memoria AVAF 2025: el PDF antifraucv.es/wp-content/uploads/2026/03/Memoria_Avaf_2025_es.pdf no aparece en buscadores (dos "
                      "búsquedas, una 'extended') y WebFetch lo rechaza (PROVENANCE_REQUIRED). Plantilla y ejecución 2025 siguen pendientes.")})
CV_FP1 = ("Desglose por capítulos 2026: los presupuestos de la Generalitat publican fichas F.P.1 'Resumen de recursos financieros' por entidad y "
          "programa (fila 'G1 - Gastos de personal', miles EUR) con URL hisenda.gva.es/auto/presupuestos/<año>/T4/EUR/FP1_<entidad>_<programa>.pdf "
          "(p. ej. AVPT 00149, programa 431.11, visto para 2022); las versiones 2026 no aparecen en buscadores y WebFetch las rechaza "
          "(PROVENANCE_REQUIRED). Ejecución 2026 y liquidación 2025 no localizadas.")
rows.append({"ID": 103, "updates": {}, "fuentes_nuevas": [], "verificacion": "Sin cambios.", "no_encontrado": CV_FP1})
rows.append({"ID": 104, "updates": {}, "fuentes_nuevas": [], "verificacion": "Sin cambios.", "no_encontrado": CV_FP1})
rows.append({"ID": 105, "updates": {}, "fuentes_nuevas": [], "verificacion": "Sin cambios.",
    "no_encontrado": "No priorizado en esta ronda (cupo de búsquedas); constitución efectiva de la agencia sigue sin verificar."})
rows.append({"ID": 106, "updates": {}, "fuentes_nuevas": [], "verificacion": "Sin cambios.",
    "no_encontrado": ("Presupuesto de explotación 2026 (gastos de personal), plantilla y cuentas 2025 de la Corporació: dos búsquedas solo devolvieron "
                      "prensa (no fuente de cifra; una pieza de Valencia Plaza de 2020-2022 cita el límite legal de un tercio del presupuesto para "
                      "personal y el contrato-programa 2021-2023, sin documento oficial enlazado). Portal de transparencia de À Punt no localizado.")})

# ---------------- País Vasco ----------------
rows.append({
    "ID": 107,
    "updates": {
        "Notas de conciliación de crédito y ejecución": (
            "Ente público de derecho privado: gastos de personal 2026 del presupuesto de explotación no extraídos (sección 16 Justicia, p. 145, y "
            "Resúmenes pp. 227-233 de los Presupuestos 2026, PDF no extraíble más allá de ~p. 24). Último gasto de personal anual localizado: 2024, "
            "cuenta de pérdidas y ganancias 'Gastos de personal' = 5.312.119 EUR (5,312119 M; sueldos, salarios y asimilados 4.190.441; cargas "
            "sociales 1.121.678); 2023: 4.526.504 EUR (cuentas anuales 2024 de Aukerak, p. 5, en euros). Gasto devengado PyG, no capítulo 1 ni "
            "presupuesto 2026; no comparar con la dotación 2026. Cuentas 2025 no localizadas: no se rellenan columnas 2025."
        ),
        "Notas de personal y apoyo ministerial": (
            "Plantilla presupuestaria 2026: 74 plazas (Anexo de personal), NO ocupación. Ficha 'Sector Público CAE y entidades participadas - 2023' "
            "(p. 3/3): 'Nº medio de empleados 24.00' (plantilla media, año de referencia de los datos no explícito en la ficha; no usar como plantilla "
            "actual ni como personas ocupadas)."
        ),
        "Cobertura presupuesto / personal / salarios": (
            "Presupuesto propio 2026 y plantilla presupuestaria 2026 verificados; gasto de personal 2026 y personas ocupadas no verificados; gasto de "
            "personal PyG 2024 en notas"
        ),
    },
    "fuentes_nuevas": [AUK_CC24, AUK_FICHA23],
    "verificacion": (
        "Cuentas anuales 2024 de Aukerak (euskadi.eus, cuentas_anuales_ee_sspp_2024, 3_6_19_AUKERAK.pdf), cuenta de pérdidas y ganancias p. 5, "
        "'(Expresada en euros)': 'Gastos de personal (5.312.119) [2024] (4.526.504) [2023]'; 'Sueldos, salarios y asimilados (4.190.441) "
        "(3.550.293)'; 'Cargas sociales (1.121.678) (976.211)'; sumas cuadran. 5.312.119 EUR = 5,312119 M. Plantilla media no aparece en el extracto "
        "de la memoria. Ficha 2023 (soc_publica_245/2023425.pdf), p. 3/3: 'Nº medio de empleados 24.00'; activo total 3.339.794 EUR; cifra de "
        "negocios 8.622.121 EUR. " + PV_TRUNC
    ),
    "no_encontrado": "Gastos de personal 2026 (presupuesto de explotación), personas ocupadas a fecha, cuentas 2025 y ejecución 2026. " + PV_TRUNC,
})
rows.append({
    "ID": 108,
    "updates": {
        "Notas de personal y apoyo ministerial": (
            "Plantilla presupuestaria 2026: 12 plazas (Anexo de personal), NO ocupación. Ficha 'Sector Público CAE y entidades participadas - 2024' "
            "(p. 4/4): 'Nº medio de empleados 6.48'; activo total 2.289.391 EUR; cifra de negocios 0 EUR (plantilla media; año de referencia de los "
            "datos no explícito; no usar como personas ocupadas)."
        ),
        "Notas de conciliación de crédito y ejecución": (
            "Ente público de derecho privado: gastos de personal 2026 del presupuesto de explotación (sección 07 Seguridad, p. 141) no extraídos: el PDF "
            "solo es legible hasta ~p. 24. Cuentas anuales 2024 y 2025 de la Agencia no localizadas. Sin gasto de personal anual verificado."
        ),
    },
    "fuentes_nuevas": [CIB_FICHA24],
    "verificacion": (
        "Ficha 2024 (euskadi.eus, soc_publica_422/2024422.pdf, Euskal Zibersegurtasun Agentzia / Agencia Vasca de Ciberseguridad, CIF Q0100620D), "
        "p. 4/4: 'Nº medio de empleados 6.48'; 'Activo total 2.289.391 €'; 'Importe neto de la cifra de negocios 0 €'. Sección 07 2026 (PDF 2026A): "
        "índice sitúa el programa 2225 en p. 83 y el ente en p. 141; texto extraíble termina en p. 24 aun con offset. " + PV_TRUNC
    ),
    "no_encontrado": "Gastos de personal 2026, personas ocupadas a fecha, cuentas 2024/2025 y ejecución 2026. " + PV_TRUNC,
})
rows.append({
    "ID": 109,
    "updates": {
        "Notas de conciliación de crédito y ejecución": (
            "Ente público de derecho privado: gastos de personal 2026 del presupuesto de explotación (sección 15, p. 116) no extraídos (PDF legible "
            "solo hasta ~p. 24). Último gasto de personal anual localizado: 2024, cuenta de pérdidas y ganancias 'Gastos de personal' (nota 12.3) = "
            "1.004.022 EUR (1,004022 M; sueldos, salarios y asimilados 751.654; cargas sociales 252.368); 2023: 859.138 EUR (cuentas anuales 2024 de "
            "EKP, p. 4, euros). Gasto devengado PyG, no capítulo 1 ni presupuesto 2026. Cuentas 2025 no localizadas: no se rellenan columnas 2025."
        ),
        "Notas de personal y apoyo ministerial": (
            "Plantilla presupuestaria 2026: 19 plazas (Anexo de personal), NO ocupación. Ficha 'Sector Público CAE y entidades participadas - 2024' "
            "(p. 4/4): 'Nº medio de empleados 16.08'; cifra de negocios 6.134.013 EUR; activo total 28.519.434 EUR (plantilla media; año de referencia "
            "de los datos no explícito; no usar como personas ocupadas)."
        ),
        "Cobertura presupuesto / personal / salarios": (
            "Presupuesto propio 2026 y plantilla presupuestaria 2026 verificados; gasto de personal 2026 y personas ocupadas no verificados; gasto de "
            "personal PyG 2024 en notas"
        ),
    },
    "fuentes_nuevas": [EKP_CC24, EKP_FICHA24],
    "verificacion": (
        "Cuentas anuales 2024 de Euskadiko Kirol Portuak (portal de transparencia ekp.euskadi.eus, CCAA24-EKP_signed.pdf), PyG p. 4, euros: "
        "'Langileengatiko gastuak / Gastos de personal 12.3 -1.004.022 -859.138'; 'Sueldos, salarios y asimilados -751.654 -634.488'; 'Cargas "
        "sociales -252.368 -224.650'; sumas cuadran. 1.004.022 EUR = 1,004022 M. Nota de plantilla no incluida en el extracto. Ficha 2024 "
        "(soc_publica_53/2024495.pdf), p. 4/4: 'Nº medio de empleados 16.08'. " + PV_TRUNC
    ),
    "no_encontrado": "Gastos de personal 2026, personas ocupadas a fecha, cuentas 2025 y ejecución 2026. " + PV_TRUNC,
})

# Order as in batch
order = [117, 118, 85, 88, 122, 86, 87, 110, 89, 121, 96, 91, 120, 95, 103, 104, 105, 106, 107, 108, 109]
byid = {r["ID"]: r for r in rows}
assert set(order) == set(byid), set(order) ^ set(byid)
out = [byid[i] for i in order]

headers = set(json.load(open("investigacion/headers.json")))
for r in out:
    for k in r["updates"]:
        assert k in headers, (r["ID"], k)

json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
print("ok", len(out))
