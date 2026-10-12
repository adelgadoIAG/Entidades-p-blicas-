import json

OUT = "datos/resultados/C_estatal_plantillas.json"

REV = "https://digital.gob.es/content/dam/portal-mtdfp/funcion-publica/rcp/boletin/2026_01/revision-agosto-2026/EPSAP_Enero_2026%20.pdf"
ORIG = "https://digital.gob.es/content/dam/portal-mtdfp/funcion-publica/rcp/boletin/2026_01/EPSAP_Enero_2026.pdf"
NOTA = "https://digital.gob.es/content/dam/portal-mtdfp/funcion-publica/rcp/notaepsap/Noticia_EPSAP_Enero_26.pdf"

AJ_OK = "Cifra de personal publicada en fuente primaria; fecha indicada, no inferir vigencia posterior"
AW_BEP = "Crédito y gasto de personal individual verificados; plantilla ocupada verificada a enero de 2026 (EPSAP, efectivos); puestos RPT no verificados"

# (ID, fila literal, tabla, pagina, F, L, O, total, no_encontrado)
T41 = ("Tabla 4.1 'Efectivos de agencias estatales por ministerio de adscripción y tipología de personal'", "p.37")
T31 = ("Tabla 3.1 'Efectivos de OO.AA. por ministerio de adscripción y tipología de personal'", None)

bep = [
    (2, "AGENCIA ESTATAL DE SEGURIDAD AÉREA 340 6 - 346", T41[0], "p.37", 340, 6, 0, 346,
     "Puestos RPT: no localizado total publicado. Revisado: página de transparencia de AESA (sin plantilla/RPT); Cuentas anuales e informe de gestión 2025 (texto extraíble sin cifras de plantilla); Informe General de Actividad 2024, sección 'Profesionales de AESA' (p.79) no extraíble (texto cortado en p.58)."),
    (3, "AGENCIA ESTATAL COMISIÓN ESPAÑOLA PARA LA LUCHA ANTIDOPAJE EN EL DEPORTE 17 7 - 24", T41[0], "p.37", 17, 7, 0, 24,
     "Puestos RPT: no localizado total publicado; no se encontró memoria/plan con plantilla propia en esta revisión."),
    (4, "AGENCIA ESTATAL DE INVESTIGACIÓN 200 20 - 220", T41[0], "p.37", 200, 20, 0, 220,
     "Puestos RPT: el Plan de Actuación Anual 2025 (aprobado 26/12/2024) tiene sección 4.2 Recursos Humanos y anexos RPT (pp.38, 46, 54), pero el texto extraíble se corta en p.36; no verificados. No se localizó plan 2026."),
    (7, "AGENCIA ESTATAL DE SEGURIDAD FERROVIARIA 115 11 - 126", T41[0], "p.37", 115, 11, 0, 126,
     "Puestos RPT: Plan de acción 2025 de la AESF (aprobado por el Consejo Rector el 18/12/2024) sin cifras de plantilla ni RPT; no se localizó memoria con RPT."),
    (28, "AGENCIA DE INFORMACIÓN Y CONTROL ALIMENTARIOS, O.A. 80 1 - 81", T31[0], "p.23", 80, 1, 0, 81,
     "Puestos RPT: página 'Información institucional, organizativa y de planificación' de AICA no accesible (error de lectura); memorias anuales no revisadas para RPT."),
    (30, "ORGANISMO ESTATAL INSPECCIÓN DE TRABAJO Y SEGURIDAD SOCIAL O.A. 3.339 74 183 3.596", T31[0], "p.24", 3339, 74, 183, 3596,
     "Puestos RPT totales del O.A.: no localizados. El Informe Anual ITSS 2024 (cap. Recursos humanos) no da RPT ni dotaciones. Respuesta parlamentaria del Gobierno 184/27631 (8/10/2025) cita '346 puestos de estructura del OEITSS' para inspectores/subinspectores, sin fecha ni total: no usada. Informe Anual ITSS 2025 no localizado."),
    (32, None, None, None, 92, 178, 0, 270,
     "Puestos RPT: no localizados (el Plan de acción 2026 no da puestos RPT; la página de transparencia de la AEBOE no publica RPT con totales)."),
    (33, "CONSEJO SUPERIOR DE INVESTIGACIONES CIENTÍFICAS - CSIC 7.136 9.767 227 17.130", T41[0], "p.37", 7136, 9767, 227, 17130,
     "Puestos RPT: no buscados en profundidad (organismo con >17.000 efectivos; contrato de gestión 2023-2026, Orden PCM/829/2023, no revisado para plantilla)."),
    (34, "AGENCIA ESTATAL DE METEOROLOGÍA 941 44 73 1.058", T41[0], "p.37", 941, 44, 73, 1058,
     "Puestos RPT totales: no verificados. Plan de acción anual AEMET 2026 (fecha 4-jun-26) sin cifras de plantilla ni RPT; página de planificación/transparencia sin enlaces a RPT con totales."),
    (35, "AGENCIA ESPAÑOLA DE MEDICAMENTOS Y PRODUCTOS SANITARIOS 525 68 36 629", T41[0], "p.37", 525, 68, 36, 629,
     "Puestos RPT: no publicados en cifras; la Memoria de actividades 2025 (p.22) solo menciona la necesidad de un 'refuerzo de la relación de puestos de trabajo (RPT)'."),
    (37, "CONFEDERACIÓN HIDROGRÁFICA DEL MIÑO-SIL, O.A. 158 52 - 210", T31[0], "p.24", 158, 52, 0, 210,
     "Puestos RPT: búsquedas de memoria/transparencia de la CH Miño-Sil sin resultado con plantilla o RPT."),
    (38, "CONFEDERACIÓN HIDROGRÁFICA DEL CANTÁBRICO, O.A. 185 74 1 260", T31[0], "p.24", 185, 74, 1, 260,
     "Puestos RPT: búsquedas de memoria/transparencia de la CH Cantábrico sin resultado con plantilla o RPT."),
    (39, "SERVICIO ESPAÑOL PARA LA INTERNACIONALIZACIÓN DE LA EDUCACIÓN (SEPIE) 116 4 - 120", T31[0], "p.23", 116, 4, 0, 120,
     "Puestos RPT: no localizados en sepie.es (memoria/transparencia)."),
    (40, "AGENCIA ESTATAL AGENCIA ESPACIAL ESPAÑOLA 53 12 - 65", T41[0], "p.37", 53, 12, 0, 65,
     "Puestos RPT: no localizados (aee.gob.es solo publica convocatorias de provisión; sin plan de acción ni memoria con plantilla)."),
    (41, "AGENCIA ESPAÑOLA DE SUPERVISIÓN DE INTELIGENCIA ARTIFICIAL 26 9 - 35", T41[0], "p.37", 26, 9, 0, 35,
     "Puestos RPT aprobados: no localizados; solo la previsión del Plan Inicial de Actuación (41 puestos), que no es RPT aprobada."),
    (42, "AGENCIA ESTATAL DE ADMINISTRACIÓN DIGITAL 416 6 16 438", T41[0], "p.37", 416, 6, 16, 438,
     "Puestos RPT: no localizados; no se encontró plan de acción anual de la AEAD con plantilla."),
]

def fmt(n):
    return f"{n:,}".replace(",", ".")

extra_bb = {
    30: ("EPSAP enero 2026 cuenta 3.596 efectivos del O.A. (todo su personal). Contexto, otra fecha y fuente (no sumar ni mezclar): Informe Anual ITSS 2024, cap. Recursos humanos, Tabla 1 p.31: a 31/12/2024 la ITSS-AGE tenía 913 inspectores + 1.298 subinspectores (964 Empleo y SS + 334 SSL) = 2.211; p.33: personal de estructura y apoyo 1.150 efectivos (1.074 funcionarios + 76 laborales; la misma página y el Gráfico 11 dan 1.073/1.149, incoherencia interna). El total del sistema (2.439 inspectores/subinspectores) incluye Inspección de Cataluña (174) y del Gobierno Vasco (54), que no forman parte del O.A. No hay RPT verificada: no se calcula cobertura."),
    34: ("RPT laboral transparencia.gob.es parcialmente contada (62, PDF posiblemente truncado); RPT funcionario no contada. EPSAP enero 2026 (Tabla 4.1 p.37): 1.058 efectivos ocupados (941 funcionarios de carrera + 44 laborales + 73 otro personal). Sin total RPT verificado: no se calcula cobertura."),
    35: ("Memoria de actividades AEMPS 2025, p.6 (organigrama): '525 Personal científico-técnico', '108 Funciones administrativas', '22 Becas de formación', '12 Red de expertos', sin fecha ni definición de cómputo: no usadas como plantilla (becarios y red de expertos no son plantilla). La plantilla ocupada se toma de EPSAP enero 2026."),
    41: ("Memoria y Plan Inicial de Actuación de AESIA (revisión agosto 2024): preveía 23 personas el primer año y 41 puestos para 2024 y siguientes (Tabla 10, p.30, 'PUESTOS CREADOS'/'EFECTIVOS'); es previsión de planificación, no RPT aprobada ni ocupación. Ocupación real EPSAP enero 2026: 35."),
    4: ("Plan de Actuación Anual 2025 de la AEI (aprobado 26/12/2024) alude a la 'baja cobertura de la RPT' (p.12) y a puestos RPT que 'permanecen vacantes' (p.20), sin cifras legibles; RPT no verificada."),
    32: ("Plan de acción anual 2026 (ap. 3, p.5) prevé 17 bajas por jubilación y 11 nuevas incorporaciones (6 de OEP) durante 2026: previsión, no dato de plantilla. RPT no verificada."),
}

fuentes_extra = {
    30: ["https://oeitss.gob.es/content/dam/oeitss/documentos/2-0-sobre-la-itss/2-3-b-nuestra-actividad/02-recursos%20humanos.pdf"],
    35: ["https://memoria.aemps.gob.es/docs/memoria-2025.pdf"],
    41: ["https://aesia.digital.gob.es/storage/media/0545dbdb-0d27-4f51-90be-b847e13e7659.pdf"],
    4: ["https://www.aei.gob.es/sites/default/files/page/field_file/2025-01/PLAN%20DE%20ACTUACION%20ANUAL%202025%20APROBADO.pdf"],
}

results = []

for (ID, fila, tabla, pag, F, L, O, T, noenc) in bep:
    assert F + L + O == T, ID
    if ID == 32:
        plan = "https://www.boe.es/transparencia/documentos/plan_accion_aeboe_2026.pdf"
        upd = {
            "Personal: personas (ocupadas)": 270,
            "Año del personal": "2026-01-01",
            "Base del personal": "270 efectivos a 1/1/2026: 92 funcionarios + 178 laborales (Plan de acción anual 2026 de la AEBOE, ap. 3, p.5). Coincide con EPSAP enero 2026, Tabla 4.1 p.37 (92 funcionarios de carrera + 178 laborales + 0 otro personal = 270). Personas, no puestos RPT.",
            "Estado de verificación del personal": AJ_OK,
            "Fuente del personal": plan,
            "Cobertura presupuesto / personal / salarios": "Crédito y gasto de personal individual verificados; plantilla ocupada verificada a 01/01/2026 (Plan de acción 2026, coincide con EPSAP); puestos RPT no verificados",
            "Notas de personal y apoyo ministerial": extra_bb[32],
        }
        ver = ("Plan de acción anual 2026 de la Agencia Estatal BOE (propuesta del Consejo Rector 9/6/2026; resolución de aprobación firmada 01/07/2026), ap. 3, p.5, literal: 'la Agencia dispone de una plantilla de 270 efectivos, a 1 de enero de 2026, 178 laborales y 92 funcionarios'; repetido en Anexo 2 (HO 3) y Memoria p.10 ('270 empleados/as a 1 de enero de 2026'). Unidad: personas. Cotejo: EPSAP enero 2026 (revisión agosto 2026), Tabla 4.1 p.37, fila 'AGENCIA ESTATAL BOLETÍN OFICIAL DEL ESTADO 92 178 - 270' (idéntica en la versión original).")
        results.append({"ID": ID, "updates": upd,
                        "fuentes_nuevas": [plan, "https://www.boe.es/transparencia/informacion_institucional_organizativa_planificacion.php", REV],
                        "verificacion": ver, "no_encontrado": noenc})
        continue
    otro_txt = f"{fmt(O)} otro personal" if O else "0 otro personal ('-' en la tabla)"
    base = (f"Efectivos (personas) según Estadística del Personal al Servicio de las AA.PP. (EPSAP) enero 2026, {tabla.split(' ')[0]} {tabla.split(' ')[1]} {pag}: "
            f"{fmt(F)} funcionarios de carrera + {fmt(L)} personal laboral + {otro_txt} = {fmt(T)}. "
            "Datos a enero de 2026 (la publicación no indica día). Estadística oficial de la DGFP; no son puestos RPT ni número medio anual.")
    upd = {
        "Personal: personas (ocupadas)": T,
        "Año del personal": "2026-01",
        "Base del personal": base,
        "Estado de verificación del personal": AJ_OK,
        "Fuente del personal": REV,
        "Cobertura presupuesto / personal / salarios": AW_BEP,
    }
    if ID in extra_bb:
        upd["Notas de personal y apoyo ministerial"] = extra_bb[ID]
    ver = (f"EPSAP Enero 2026 (revisión agosto 2026), {tabla}, {pag}, fila literal '{fila}' "
           "(columnas: funcionario de carrera / personal laboral / otro personal / total; unidad: personas). "
           "Fila idéntica en la versión original EPSAP_Enero_2026.pdf. Fecha: nota EPSAP enero 2026 ('datos actualizados a enero de 2026'); la tabla no lleva nota de fecha propia. "
           "Coherencia: la misma edición da para la AEBOE 92+178=270, idéntico al Plan de acción AEBOE 2026 'a 1 de enero de 2026'.")
    if ID == 3:
        ver += " La EPSAP clasifica a la CELAD en la Tabla 4.1 (agencias estatales) con esa denominación."
    if ID == 30:
        ver += (" Contexto en notas: Informe Anual ITSS 2024, cap. 02 Recursos humanos, Tabla 1 p.31 (inspectores/subinspectores a 31/12/2024) y p.33 (estructura y apoyo 1.150).")
    results.append({"ID": ID, "updates": upd,
                    "fuentes_nuevas": [REV, NOTA] + fuentes_extra.get(ID, []),
                    "verificacion": ver, "no_encontrado": noenc})

# ID 5 AIReF
results.append({
    "ID": 5,
    "updates": {
        "Notas de personal y apoyo ministerial": "Sin cifra verificada en esta revisión: airef.es bloquea la lectura automática (robots). Documentos oficiales localizados para comprobación manual: Memoria anual de actividades 2025 (https://www.airef.es/wp-content/uploads/2026/03/Memoria/AIReF_Memoria-anual-de-actividades_2025.pdf) y RPT de funcionarios a 03/04/2025 (https://www.airef.es/wp-content/uploads/2025/04/Sobre_nosotros/RPT_funcionarios_03_04_2025.pdf). La EPSAP enero 2026 solo publica el agregado de Autoridades Administrativas Independientes (1.926 efectivos, Tabla 1.5 p.8), sin desglose por entidad.",
        "Cobertura presupuesto / personal / salarios": "Crédito y gasto de personal individual verificados; plantilla ocupada y puestos RPT no verificados (fuente propia no legible automáticamente)",
    },
    "fuentes_nuevas": [],
    "verificacion": "Ningún número nuevo. EPSAP enero 2026 (revisión agosto 2026), Tabla 1.5 p.8: 'Autoridades Administrativas Independientes 908 986 32 1.926' (agregado de todas las AAI; no imputable a la AIReF).",
    "no_encontrado": "Plantilla ocupada y RPT de la AIReF: Memoria anual 2025 y RPT funcionarios 03/04/2025 localizadas en airef.es pero WebFetch devuelve ROBOTS_DISALLOWED; búsquedas de copia oficial alternativa (BOE cuentas anuales 2025: solo referencia al Registro de cuentas; resoluciones BOE de AIReF: convocatorias, no RPT) sin resultado. No se usa prensa (El Español 2023).",
})

# ID 6 CTBG
mem = "https://consejodetransparencia.es/content/dam/ctransparencia/portal-ctbg/nosotros/memorias-y-plan-estrategico/memoria-2025/Memoria_2025_CTBG.pdf"
rpt = "https://consejodetransparencia.es/content/dam/ctransparencia/portal-ctbg/transparencia/informacion-institucional-organizativa-y-de-planificacion/RPT_30-06-2026.pdf"
results.append({
    "ID": 6,
    "updates": {
        "Personal: personas (ocupadas)": 31,
        "Año del personal": "2025-12-31",
        "Base del personal": "31 efectivos a 31/12/2025, incluido el Presidente; los otros 30 son funcionarios de carrera (por disposición estatutaria); sin personal laboral ni eventual. Memoria CTBG 2025, ap. 1.3.2, p.19, Tabla 1 'Efectivos del CTBG a 31 de diciembre de 2025'.",
        "Estado de verificación del personal": AJ_OK,
        "Fuente del personal": mem,
        "Puestos aprobados / presupuestados": 39,
        "Fecha puestos aprobados": "2026-06-30",
        "Base de puestos aprobados": "Puestos de la RPT del CTBG (personal funcionario), 'Total Puestos: 39', fecha de vigencia 30-06-2026; el documento no indica ocupación ni vacantes.",
        "Fuente puestos aprobados": rpt,
        "Notas de personal y apoyo ministerial": "Ocupados (31 a 31/12/2025, Memoria; incluye al Presidente, alto cargo fuera de RPT) y RPT (39 puestos a 30/06/2026) son de fechas y fuentes distintas: no se calcula cobertura. Portal de transparencia CTBG: 'Toda la plantilla ... está formada por funcionarios/as de carrera' y no hay personal eventual. Memoria 2025: cap. 1 presupuestado 2.463,70 miles EUR; obligaciones 2.201.447,49 EUR (89,36%), coherente con IGAE (2,201 M).",
        "Cobertura presupuesto / personal / salarios": "Crédito y gasto de personal individual verificados; plantilla ocupada verificada a 31/12/2025 (Memoria CTBG) y puestos RPT a 30/06/2026 (fechas distintas, sin cobertura calculada)",
    },
    "fuentes_nuevas": [mem, rpt, "https://consejodetransparencia.es/ct_Home/transparencia/portal-transparencia/informacion-institucional/mas-transparencia/documentos-personal.html"],
    "verificacion": "Memoria CTBG 2025, ap. 1.3.2 Recursos humanos, p.19, literal: 'A 31 de diciembre de 2025 el CTBG contaba con 31 efectivos, todos ellos funcionarios de carrera por expresa disposición estatutaria, con excepción del Presidente'; Tabla 1 'TOTAL DE EFECTIVOS 31'; recuadro '30 EFECTIVOS ADEMÁS DEL PRESIDENTE'. Unidad: personas. RPT CTBG 'Fecha de Vigencia: 30-06-2026', línea 'Total Puestos: 39' (subtotales por unidad 3+5+6+8+11+6 = 39). Cotejo cap.1: Memoria Tabla 3 '1: Gastos de personal 2.463.700,00 € 2.201.447,49 €' = IGAE 2025 obligaciones 2,201 M ya en la ficha.",
    "no_encontrado": "Ocupación a 30/06/2026 (misma fecha que la RPT) no publicada; por eso no se calcula cobertura.",
})

# ID 43 AIPI
paa = "https://www.proteccioninformante.gob.es/content/dam/aipi/documentos/PLAN_ACTUACION_ANUAL_2026_AIPI.pdf"
results.append({
    "ID": 43,
    "updates": {
        "Personal: personas (ocupadas)": 17,
        "Año del personal": "2026-07",
        "Base del personal": "17 puestos de la RPT cubiertos (personas en puesto RPT; no incluye a la Presidencia, alto cargo). Plan de Actuación Anual 2026 de la AIPI, ap. 2.4, p.19: 'RPT con 22 puestos de los que están cubiertos 17'; Ilustración 3 fechada 'Julio de 2026. Registro Central de Personal'. Sin desglose funcionarios/laborales.",
        "Estado de verificación del personal": AJ_OK,
        "Fuente del personal": paa,
        "Puestos aprobados / presupuestados": 22,
        "Fecha puestos aprobados": "2026-07",
        "Base de puestos aprobados": "Puestos RPT según el texto del PAA 2026, p.19 ('RPT con 22 puestos'). La Ilustración 3 (RCP, julio 2026), en lectura automática, lista 24 filas (17 ocupadas 'O', 7 vacantes 'V'): discrepancia interna no resuelta; se adopta la cifra literal del texto.",
        "Fuente puestos aprobados": paa,
        "Notas de personal y apoyo ministerial": "Cobertura RPT 77,3% (17/22), misma fuente y fecha (PAA 2026, julio 2026). Inicio de funcionamiento 1/9/2025 (Orden PJC/908/2025), con soporte del Ministerio de Presidencia en RRHH y otros servicios hasta 1/11/2025. Indicador de la Memoria 2025 citado en el PAA (p.9): 'Cobertura de RPT. 8 puestos 44%' (fecha 2025, no comparable). El Plan Inicial de Actuación preveía 42 efectivos (previsión, no dato). Los puestos denominados 'Vocal' en la RPT son puestos de trabajo, no miembros de órgano colegiado.",
        "Cobertura presupuesto / personal / salarios": "Crédito y gasto de personal individual verificados; plantilla ocupada (17) y puestos RPT (22) verificados a julio de 2026 (PAA 2026)",
    },
    "fuentes_nuevas": [paa, "https://www.boe.es/eli/es/o/2025/08/08/pjc908"],
    "verificacion": "Plan de Actuación Anual 2026 AIPI (sin fecha de aprobación visible; RPT fechada julio 2026), p.19 literal: 'La AIPI cuenta actualmente con una Relación de Puestos de Trabajo (RPT) con 22 puestos de los que están cubiertos 17.' Pie: 'Ilustración 3. Relación de Puestos de Trabajo de la AIPI. Julio de 2026. Registro Central de Personal.' Unidad: puestos/personas. Cobertura 17/22 = 0,7727. Cotejo: p.20 presupuesto 2026 '1 Gastos de personal 2.599,32' miles EUR = crédito cap.1 2,599 M ya en la ficha. Orden PJC/908/2025: inicio de funcionamiento 1/9/2025.",
    "no_encontrado": "Desglose funcionarios/laborales no publicado. Discrepancia 22 (texto) vs 24 filas (Ilustración 3, lectura automática) no resuelta.",
})

results.sort(key=lambda r: r["ID"])
ids = [r["ID"] for r in results]
assert ids == [2, 3, 4, 5, 6, 7, 28, 30, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43], ids

headers = json.load(open("investigacion/headers.json"))
for r in results:
    for k in r["updates"]:
        assert k in headers, (r["ID"], k)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
print("ok", len(results))
