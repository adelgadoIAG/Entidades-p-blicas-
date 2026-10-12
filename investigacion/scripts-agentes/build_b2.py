import json

EC = "Sin presupuesto propio: órgano sin dotación diferenciada (verificado en norma)"
NOCERO = " Coste absorbido no cuantificado ni prorrateado; no significa 0 EUR."
VOC = " Vocales/miembros no son plantilla. No repartir gasto ministerial."

def std(unidad, art, extra_pers=""):
    """Campos coherentes para un órgano verificado sin dotación propia."""
    return {
        "Estado de cuantificación": EC,
        "Estado de verificación del personal": (
            "Sin plantilla propia según norma (" + art + "): apoyo con medios de " + unidad +
            "; no hay cifra publicada de personal de apoyo asignado" + extra_pers + "; vocales no son plantilla"),
        "Estado de verificación del coste": (
            "Sin crédito de personal propio (verificado en norma, " + art + "): coste absorbido por créditos de " +
            unidad + "; no desglosado ni prorrateado"),
        "Estado de verificación de ejecución": (
            "Sin ejecución propia: el gasto que genere se imputa a " + unidad +
            " sin desglose publicado; no prorrateado"),
        "Cobertura presupuesto / personal / salarios": (
            "Sin presupuesto propio (verificado en norma, " + art + "); personal y salarios absorbidos por " +
            unidad + ", sin desglose ni plantilla propia publicada. No significa 0 EUR."),
    }

out = []

# ---------------- 47 ----------------
u47 = "la Secretaría de Estado de Comercio (DG de Política Comercial)"
d = std(u47, "apdo. noveno del Acuerdo CM 11/10/2018")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: Acuerdo CM 11/10/2018 publicado por Resolución de 25/10/2018 de la "
        "Secretaría de Estado de Comercio (BOE-A-2018-15776), apartado noveno 'No incremento de gasto público': el departamento "
        "'atenderá con sus medios personales y materiales la constitución y funcionamiento del Observatorio' 'sin que pueda suponer "
        "un aumento del gasto público'. Coste absorbido por la Secretaría de Estado de Comercio (secretaría del Pleno: Subdirección "
        "General de Apoyo a la Competitividad del Pequeño Comercio, apdo. cuarto)." + NOCERO +
        " El apartado undécimo suprime el Observatorio de Pagos con Tarjeta Electrónica (2006-2018). Página oficial (comercio.gob.es, "
        "consulta 11/10/2026): de los cuatro grupos de trabajo, el de Información 'es el único que ha iniciado sus trabajos'; sin datos "
        "de presupuesto o contrato propios."),
    "Notas de personal y apoyo ministerial": (
        "Secretaría del Pleno: titular de la Subdirección General de Apoyo a la Competitividad del Pequeño Comercio (DG de Política "
        "Comercial y Competitividad, denominación 2018), con voz y voto; gestiona los grupos de trabajo (apdos. cuarto y sexto). "
        "Medios personales y materiales del departamento (apdo. noveno; en 2018 Ministerio de Industria, Comercio y Turismo; la web "
        "del Observatorio figura hoy bajo el Ministerio de Economía, Comercio y Empresa, Secretaría de Estado de Comercio). La norma no "
        "prevé retribuciones ni indemnizaciones de vocales." + VOC),
})
out.append({
    "ID": 47,
    "updates": d,
    "fuentes_nuevas": [
        "https://boe.es/diario_boe/txt.php?id=BOE-A-2018-15776",
        "https://comercio.gob.es/ComercioInterior/Observatorio/Paginas/GTAnalisisMetricasyVariables.aspx",
    ],
    "verificacion": (
        "Sin cifras. Norma leída en BOE (BOE-A-2018-15776, BOE núm. 279 de 19/11/2018 según cabecera de la página): apdo. noveno (no "
        "incremento de gasto, medios personales y materiales del departamento), apdo. cuarto (secretaría), apdo. undécimo (supresión "
        "del Observatorio de Pagos con Tarjeta Electrónica). Corrección de matiz: la nota previa decía 'Medios del Ministerio de "
        "Industria y Turismo'; la norma remite al departamento de 2018 (Industria, Comercio y Turismo) y la web oficial actual del "
        "Observatorio está en comercio.gob.es con cabecera del Ministerio de Economía, Comercio y Empresa (un metadato aún indica "
        "'Ministerio de Industria y Turismo'). Posible discrepancia de fecha: la columna 'Norma fundacional' dice 'publicado 25/10/2018', "
        "pero 25/10/2018 es la fecha de la Resolución; la página BOE indica publicación en BOE núm. 279 de 19/11/2018 (no se ha tocado la columna)."),
    "no_encontrado": (
        "No se ha encontrado contrato, convenio ni línea presupuestaria a nombre del Observatorio del Comercio 4.0 (la web muestra "
        "logotipos NextGeneration/PRTR sin vincular importes al Observatorio). Búsqueda adicional en PLACSP no posible: cupo de búsquedas web agotado."),
})

# ---------------- 48 ----------------
u48 = "el Ministerio competente en ciencia (Gabinete del Ministro; Unidad de Mujeres y Ciencia)"
d = std(u48, "RD 938/2020, disposición adicional única")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: RD 938/2020 (BOE-A-2020-13026), disposición adicional única 'No incremento del "
        "gasto público': la creación y el funcionamiento del Observatorio 'no supondrá incremento del gasto público' y se atenderá 'con "
        "los medios personales, técnicos y presupuestarios asignados al Ministerio de Ciencia e Innovación'. Coste absorbido por el "
        "Gabinete del Ministerio (secretaría, art. 4.2; Unidad de Mujeres y Ciencia/Unidad de Igualdad, art. 4.1.i)." + NOCERO +
        " El RD 938/2020 deroga el RD 1401/2018 sin extinguir el Observatorio."),
    "Notas de personal y apoyo ministerial": (
        "Secretaría: un/a funcionario/a de carrera de nivel 28 o superior del Gabinete de la persona titular del Ministerio, con voz y "
        "sin voto (art. 4.2). Vocalía de la Unidad de Mujeres y Ciencia/Unidad de Igualdad del Gabinete (art. 4.1.i). Medios "
        "personales, técnicos y presupuestarios del Ministerio (DA única; denominación 2020 'Ciencia e Innovación'). La norma no regula "
        "retribuciones ni indemnizaciones de miembros." + VOC),
})
out.append({
    "ID": 48,
    "updates": d,
    "fuentes_nuevas": ["https://www.boe.es/eli/es/rd/2020/10/27/938"],
    "verificacion": "Sin cifras. RD 938/2020 leído en BOE (ELI): DA única (no incremento de gasto; medios del Ministerio), art. 4.1.i y 4.2 (unidad de apoyo y secretaría). La página no muestra modificaciones posteriores.",
    "no_encontrado": "Sin financiación específica identificable (convenio/contrato/línea) a nombre del Observatorio; búsqueda adicional limitada por cupo de búsquedas web agotado. Sin cifra publicada de personal de la Unidad de Mujeres y Ciencia.",
})

# ---------------- 49 ----------------
u49 = "la Tesorería General de la Seguridad Social (SG de Recaudación en Periodo Voluntario y subdirecciones provinciales)"
d = std(u49, "Orden TMS/667/2019, disposición adicional única")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: Orden TMS/667/2019 (BOE-A-2019-9215; modificada por Orden TMS/1066/2019, sin "
        "derogación), disposición adicional única 'Medios personales y materiales': constitución y funcionamiento atendidos 'con cargo "
        "a sus actuales medios personales y materiales', 'sin que se pueda generar, en ningún caso, aumento de las dotaciones "
        "presupuestarias'. Coste absorbido por la TGSS (secretaría del Pleno: titular de la Subdirección General de Recaudación en "
        "Periodo Voluntario, art. 6.1; comisiones provinciales: subdirecciones provinciales de recaudación, art. 7.1)." + NOCERO),
    "Notas de personal y apoyo ministerial": (
        "Secretaría del Pleno: titular de la Subdirección General de Recaudación en Periodo Voluntario de la TGSS (art. 6.1.2.º); "
        "comisiones provinciales: titular de la subdirección provincial competente en recaudación en periodo voluntario (art. 7.1.2.º). "
        "Medios personales y materiales existentes, sin aumento de dotaciones (DA única). La norma no regula retribuciones ni "
        "indemnizaciones de miembros." + VOC),
})
out.append({
    "ID": 49,
    "updates": d,
    "fuentes_nuevas": ["https://www.boe.es/eli/es/o/2019/06/05/tms667"],
    "verificacion": "Sin cifras. Orden TMS/667/2019 leída en BOE (ELI): DA única (medios actuales, sin aumento de dotaciones), arts. 6.1 y 7.1 (secretarías). Consta modificada por Orden TMS/1066/2019 (arts. 2.2, 3.b, 6.2, 7.1 y 7.2), no derogada.",
    "no_encontrado": "Sin financiación específica identificable ni personal asignado publicado; búsqueda adicional limitada por cupo de búsquedas web agotado.",
})

# ---------------- 50 ----------------
u50 = "el Ministerio de Cultura (Dirección General de Derechos Culturales)"
d = std(u50, "Orden reguladora de 2024, apdo. quinto")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: Orden del Ministerio de Cultura por la que se regula el Observatorio de Igualdad de "
        "Género en el ámbito de la Cultura (firma electrónica 16/09/2024, Ministro Ernest Urtasun), apartado quinto: el funcionamiento "
        "'se atenderá con los recursos humanos y medios técnicos y materiales del Ministerio de Cultura'. No contiene cláusula expresa "
        "de 'no incremento del gasto'. Coste absorbido por el Ministerio de Cultura (DG de Derechos Culturales)." + NOCERO +
        " No equivale al presupuesto de igualdad cultural."),
    "Notas de personal y apoyo ministerial": (
        "Secretaría: 'una persona funcionaria del Ministerio de Cultura, con voz pero sin voto', designada por la persona titular de la "
        "Dirección General de Derechos Culturales (apdo. tercero.1.d). Recursos humanos y medios técnicos y materiales del Ministerio "
        "(apdo. quinto). La orden no regula retribuciones ni indemnizaciones de miembros." + VOC),
})
out.append({
    "ID": 50,
    "updates": d,
    "fuentes_nuevas": ["https://culturaygenero.com/wp-content/uploads/2024/12/orden-reguladora-observatorio-igualdad.pdf"],
    "verificacion": (
        "Sin cifras. Texto de la orden reguladora leído en copia íntegra alojada en culturaygenero.com (mismo título que el PDF oficial "
        "ya listado en la ficha, cultura.gob.es/dam/.../report-orden-reguladora-observatorio-igualdad.pdf, que no pudo abrirse en esta "
        "sesión): apdo. quinto (medios del Ministerio), apdo. tercero.1.d (secretaría). No consta publicación en BOE en el texto. "
        "Conviene cotejar contra el PDF oficial de cultura.gob.es; la copia de tercero se da solo como pista de lectura."),
    "no_encontrado": "No se ha localizado publicación en BOE de la orden de 2024 ni financiación específica a nombre del Observatorio; búsqueda adicional limitada por cupo de búsquedas web agotado.",
})

# ---------------- 51 ----------------
u51 = "el Instituto Cervantes (plantilla y presupuesto del Instituto)"
d = std(u51, "RD 431/2022, art. 5.7")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: RD 431/2022 (BOE-A-2022-9382), art. 5.7: 'La creación y funcionamiento del "
        "Observatorio Global del Español no supondrá incremento del gasto público'; para sus funciones 'se podrán asignar puestos de "
        "trabajo incluidos en la plantilla del Instituto Cervantes'. Secretaría del Pleno: Secretaría General del Instituto Cervantes "
        "(art. 4.3); Comisión ejecutiva presidida por la Dirección del Instituto Cervantes (art. 5.2). Coste absorbido por el Instituto "
        "Cervantes." + NOCERO + " No asignar al observatorio los 1.100 M EUR del PERTE de lengua."),
    "Notas de personal y apoyo ministerial": (
        "RD 431/2022 art. 5.7 permite asignar puestos de la plantilla del Instituto Cervantes (personal del Cervantes, no plantilla "
        "propia del observatorio); no se ha localizado cifra publicada de puestos asignados. Pleno presidido por el titular de "
        "Exteriores (art. 4.1); secretaría del Pleno: Secretaría General del Instituto Cervantes (art. 4.3). La norma no regula "
        "retribuciones ni indemnizaciones de miembros. Vocales y director no equivalen a plantilla propia. No repartir el presupuesto "
        "del Instituto Cervantes."),
})
out.append({
    "ID": 51,
    "updates": d,
    "fuentes_nuevas": ["https://www.boe.es/eli/es/rd/2022/06/07/431/con"],
    "verificacion": "Sin cifras. RD 431/2022 leído en texto consolidado BOE (sin modificaciones; en vigor desde 09/06/2022): art. 5.7 (no incremento de gasto; puestos de plantilla del Instituto Cervantes), arts. 4.1, 4.3 y 5.2.",
    "no_encontrado": "No se ha localizado línea presupuestaria, convenio o transferencia identificable a nombre del Observatorio en el presupuesto del Instituto Cervantes ni en el PERTE; búsqueda adicional limitada por cupo de búsquedas web agotado. Sin cifra publicada de puestos asignados.",
})

# ---------------- 52 / 53 ----------------
u52 = "el MAPA (presupuesto ordinario de la DG de Desarrollo Rural, Innovación y Formación Agroalimentaria; SG de Regadíos, Caminos Naturales e Infraestructuras Rurales)"
for _id, nombre in ((52, "Observatorio"), (53, "Mesa")):
    d = std(u52, "RD 854/2022, disposición adicional primera")
    base = (
        "Sin presupuesto propio, verificado en norma: RD 854/2022 (BOE-A-2022-16583; consolidado a 02/10/2025), disposición adicional "
        "primera: la creación y el funcionamiento de la Mesa y del Observatorio 'no supondrán, en ningún caso, incremento del gasto "
        "público'; el preámbulo precisa que los gastos 'provendrán del presupuesto ordinario de la Dirección General de Desarrollo "
        "Rural, Innovación y Formación Agroalimentaria' y no del Mecanismo de Recuperación." + NOCERO)
    if _id == 52:
        base += (" La plataforma la gestiona el Ministerio 'a través de la unidad competente en materia de regadíos' (art. 6.3). "
                 "No sumar con la Mesa (ID 53): mismo soporte departamental.")
        notas = ("Gestión de la plataforma: unidad competente en regadíos del MAPA (art. 6.3). Sin personal propio previsto. "
                 "La norma no regula retribuciones ni indemnizaciones." + VOC)
    else:
        base += (" No sumar con el Observatorio (ID 52): mismo soporte departamental.")
        notas = ("Secretaría de la Mesa (y de su Comisión Institucional): persona funcionaria A1 de la Subdirección General de "
                 "Regadíos, Caminos Naturales e Infraestructuras Rurales del MAPA (art. 4.2.19.º y 4.3); puede asistir acompañada de "
                 "funcionarios de su Subdirección (art. 5.3). La norma no regula retribuciones ni indemnizaciones de miembros." + VOC)
    d.update({"Presupuesto: texto completo": base, "Notas de personal y apoyo ministerial": notas})
    out.append({
        "ID": _id,
        "updates": d,
        "fuentes_nuevas": ["https://www.boe.es/eli/es/rd/2022/10/11/854/con"],
        "verificacion": "Sin cifras. RD 854/2022 leído en texto consolidado BOE (última actualización 02/10/2025): DA primera (no incremento de gasto), preámbulo (presupuesto ordinario de la DG de Desarrollo Rural, Innovación y Formación Agroalimentaria), arts. 4.2.19.º, 4.3, 5.3 y 6.3.",
        "no_encontrado": "No se ha localizado encargo a medio propio ni contrato identificable a nombre de la plataforma/Mesa; búsqueda en PLACSP no posible por cupo de búsquedas web agotado.",
    })

# ---------------- 54 ----------------
u54 = "el Ministerio de Industria y Turismo (Secretaría de Estado de Industria; SG de Emprendimiento y PYME)"
d = std(u54, "RD 439/2024, disposición adicional única")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: RD 439/2024 (BOE-A-2024-8711), disposición adicional única 'No incremento del "
        "gasto público': 'no supondrá gastos adicionales a los previstos en las dotaciones presupuestarias del Ministerio de Industria y "
        "Turismo' y 'el funcionamiento de ambos órganos [Consejo Estatal de la PYME y Observatorio] será atendido con los medios "
        "personales, técnicos y presupuestarios del departamento'. Adscrito a la Secretaría de Estado de Industria (art. 9); secretaría: "
        "titular de la Subdirección General de Emprendimiento y PYME (art. 14.5)." + NOCERO),
    "Notas de personal y apoyo ministerial": (
        "Secretaría: titular de la Subdirección General de Emprendimiento y PYME (art. 14.5). Medios personales, técnicos y "
        "presupuestarios del Ministerio de Industria y Turismo (DA única). Art. 14.8: los miembros 'no percibirán ninguna retribución o "
        "compensación económica'. Datos aportados gratuitamente por miembros y participantes (art. 13.2)." + VOC),
})
out.append({
    "ID": 54,
    "updates": d,
    "fuentes_nuevas": ["https://www.boe.es/eli/es/rd/2024/04/30/439", "https://www.boe.es/boe/dias/2024/05/01/pdfs/BOE-A-2024-8711.pdf"],
    "verificacion": "Sin cifras. RD 439/2024 leído en BOE (ELI): DA única (sin gastos adicionales; medios del departamento), arts. 9, 13.2, 14.5 y 14.8.",
    "no_encontrado": "Sin financiación específica identificable a nombre del Observatorio; búsqueda adicional limitada por cupo de búsquedas web agotado.",
})

# ---------------- 55 ----------------
out.append({
    "ID": 55,
    "updates": {},
    "fuentes_nuevas": [],
    "verificacion": "Sin cambios. No hay norma de creación con cláusula de gasto que verificar: la ficha lo describe como proyecto estadístico conjunto (Economía/Hacienda, Banco de España, AEAT) lanzado por nota de 2023.",
    "no_encontrado": "No se ha podido localizar convenio o acuerdo publicado que regule su financiación ni personal asignado: el cupo de búsquedas web de la sesión se agotó antes de revisar este órgano. Se mantiene 'Sin cifra propia actual verificada'.",
})

# ---------------- 56 ----------------
out.append({
    "ID": 56,
    "updates": {},
    "fuentes_nuevas": [],
    "verificacion": "Sin cambios.",
    "no_encontrado": "No se pudo leer la Orden ministerial de 26/04/2024 (PDF de sanidad.gob.es listado en la ficha): la URL no estaba disponible para lectura en esta sesión y el cupo de búsquedas web se agotó. Pendiente verificar su cláusula de gasto/medios antes de cambiar a 'verificado en norma'.",
})

# ---------------- 57 ----------------
u57 = "la Dirección General de la Guardia Civil (Ministerio del Interior)"
d = std(u57, "Orden PJC/849/2024, disposición adicional única", extra_pers=" (la norma remite el nivel orgánico a la RPT)")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: Orden PJC/849/2024 (BOE-A-2024-16600), disposición adicional única 'No incremento "
        "del gasto': 'La creación y funcionamiento del COMGECET y del Observatorio no supondrán gastos adicionales' 'ni incremento de "
        "gasto público, siendo atendidos, en su caso, con los medios personales, técnicos y presupuestarios de la Dirección General de "
        "la Guardia Civil'. Coste absorbido por la DGGC." + NOCERO),
    "Estado de verificación del personal": (
        "Pendiente: unidad interna con nivel orgánico 'que se determine en la relación de puestos de trabajo' (DF primera, nuevo art. "
        "23 bis Orden PRE/422/2013); la norma no fija número de puestos y no se ha localizado cifra publicada de efectivos"),
    "Notas de personal y apoyo ministerial": (
        "Unidad organizativa de la DGGC (art. 8), no órgano con plantilla propia: nivel orgánico según RPT (DF primera, art. 23 bis "
        "Orden PRE/422/2013) e inclusión en régimen de destinos (DF segunda, art. 9.3 Orden INT/26/2021). Se apoya en el resto de "
        "jefaturas y unidades de la DGGC (art. 8.2). La persona que dirige el Observatorio es vocal permanente del COMGECET y su "
        "secretaría la ejerce personal del Observatorio de la escala de oficiales (art. 7.2). Medios personales, técnicos y "
        "presupuestarios de la DGGC (DA única). Número de puestos/efectivos no publicado en las fuentes revisadas. No repartir gasto "
        "de la DGGC."),
})
out.append({
    "ID": 57,
    "updates": d,
    "fuentes_nuevas": ["https://www.boe.es/boe/dias/2024/08/10/pdfs/BOE-A-2024-16600.pdf"],
    "verificacion": "Sin cifras. Orden PJC/849/2024 leída en PDF BOE (núm. 193, 10/08/2024): art. 7.2, art. 8, DA única (no incremento de gasto; medios de la DGGC), DF primera y segunda (RPT y destinos).",
    "no_encontrado": "No se ha localizado RPT o memoria con número de puestos/efectivos del Observatorio; búsqueda adicional limitada por cupo de búsquedas web agotado.",
})

# ---------------- 58 ----------------
u58 = "el Ministerio para la Transformación Digital y de la Función Pública (Secretaría de Estado de Función Pública; DG de Gobernanza Pública)"
d = std(u58, "RD 371/2026, art. 19.2 y disposición adicional única")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: RD 371/2026 (BOE-A-2026-9880, BOE núm. 111 de 07/05/2026), art. 19.1-2: el "
        "Observatorio es 'un espacio virtual' con 'un entorno propio dentro del Portal de la Transparencia'; 'Su diseño y mantenimiento "
        "corresponderán al Ministerio para la Transformación Digital y de la Función Pública' 'a través de la Secretaría de Estado de "
        "Función Pública'. La disposición adicional única.1 ('no supondrá un incremento del gasto público'; 'dotaciones presupuestarias "
        "ordinarias' de los departamentos) se refiere literalmente al Foro de Gobierno Abierto, no al Observatorio; la norma no asigna "
        "dotación propia al Observatorio. Coste absorbido por el MTDFP (Portal de la Transparencia)." + NOCERO),
    "Notas de personal y apoyo ministerial": (
        "Diseño y mantenimiento: MTDFP a través de la Secretaría de Estado de Función Pública (art. 19.2); cauces de propuesta de "
        "buenas prácticas habilitados por la Dirección General de Gobernanza Pública (art. 19.6). Secretaría del Foro: titular de la "
        "Subdirección General de Gobierno Abierto (art. 13.1). DA única.2: la participación en el Foro 'no exigirá dedicación exclusiva "
        "ni dará derecho a remuneración'. Sin personal propio previsto." + VOC),
})
out.append({
    "ID": 58,
    "updates": d,
    "fuentes_nuevas": ["https://www.boe.es/eli/es/rd/2026/05/06/371/con", "https://www.boe.es/eli/es/rd/2026/05/06/371"],
    "verificacion": "Sin cifras. RD 371/2026 leído en BOE (ELI y consolidado): art. 19 (Observatorio), art. 13.1, art. 17, DA única apdos. 1 y 2. Identificador BOE-A-2026-9880. Matiz: la cláusula de no incremento de gasto nombra al Foro; para el Observatorio la norma solo atribuye diseño y mantenimiento al MTDFP, sin dotación propia.",
    "no_encontrado": "No se ha localizado contrato o encargo identificable para el desarrollo del entorno del Observatorio en el Portal de la Transparencia, ni la MAIN del proyecto (la página de información pública no mostraba enlaces); cupo de búsquedas web agotado.",
})

# ---------------- 59 ----------------
out.append({
    "ID": 59,
    "updates": {},
    "fuentes_nuevas": [],
    "verificacion": "Sin cambios: se mantienen las cifras contextuales existentes (convenio 2021-2025, 1,370 M EUR; 185.000 EUR en 2024 y 2025), que ya citan los PDF del BOE.",
    "no_encontrado": "No se pudo comprobar si existe prórroga o nuevo convenio MAPA-Cajamar para 2026: los PDF del BOE de la ficha no estaban disponibles para lectura en esta sesión y el cupo de búsquedas web se agotó.",
})

# ---------------- 60 ----------------
out.append({
    "ID": 60,
    "updates": {},
    "fuentes_nuevas": [],
    "verificacion": "Sin cambios: se mantiene la cifra contextual de 10,83 M EUR (programa completo de Red.es, no presupuesto del Observatorio).",
    "no_encontrado": "No se pudo releer la cláusula económica del convenio BOE-A-2024-14138 ni localizar fuente primaria con el periodo del programa: PDF no disponible para lectura en esta sesión y cupo de búsquedas web agotado.",
})

# ---------------- 61 ----------------
u61 = "el departamento con competencias en Agenda 2030 (Secretaría de Estado para la Agenda 2030; DG de Políticas Palanca para el Cumplimiento de la Agenda 2030)"
d = std(u61, "Orden DSA/819/2020, apdos. octavo y undécimo")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: Orden DSA/819/2020 (deroga la Orden PCI/169/2019), apartado undécimo: 'La "
        "constitución y funcionamiento del Consejo de Desarrollo Sostenible no supondrán incremento alguno del gasto público'; apartado "
        "octavo.2: funcionamiento atendido con cargo a los créditos existentes en el Ministerio de Derechos Sociales y Agenda 2030; "
        "octavo.3: el Ministerio 'facilitará los medios personales y materiales necesarios'. Coste absorbido por la Secretaría de Estado "
        "para la Agenda 2030." + NOCERO + " No atribuir todo el gasto Agenda 2030 al Consejo."),
    "Notas de personal y apoyo ministerial": (
        "Adscrito a través de la Secretaría de Estado para la Agenda 2030, cuyo titular lo preside (apdos. primero.2 y tercero.2). "
        "Secretaría: Dirección General de Políticas Palanca para el Cumplimiento de la Agenda 2030, con voz y sin voto (apdo. "
        "tercero.4). Medios personales y materiales del Ministerio (apdo. octavo.3). Apdo. octavo.1: los integrantes 'no percibirán "
        "remuneración alguna'. Corrección: la nota previa atribuía los medios al MITERD; la norma vigente los atribuye al Ministerio de "
        "Derechos Sociales y Agenda 2030 (denominación de 2020)." + VOC),
})
out.append({
    "ID": 61,
    "updates": d,
    "fuentes_nuevas": ["https://www.boe.es/eli/es/o/2020/09/03/dsa819/con"],
    "verificacion": "Sin cifras. Orden DSA/819/2020 leída en texto consolidado BOE (sin modificaciones posteriores): apdos. primero.2, tercero.2 y 4, octavo.1-3, undécimo y duodécimo.2 (deroga la Orden PCI/169/2019). Corrige la atribución previa 'Medios del MITERD (Orden PCI/169/2019)': la norma vigente remite al Ministerio de Derechos Sociales y Agenda 2030; no se ha reverificado aquí la denominación actual del departamento.",
    "no_encontrado": "Sin financiación específica identificable (contrato de secretaría técnica, etc.) a nombre del Consejo; búsqueda adicional limitada por cupo de búsquedas web agotado.",
})

# ---------------- 62 ----------------
u62 = "el Ministerio de Igualdad (DG de Diversidad Sexual y Derechos LGTBI; SG de Derechos LGTBI)"
d = std(u62, "Orden IGD/577/2020, disposición adicional única")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: Orden IGD/577/2020 (BOE-A-2020-6840), disposición adicional única: creación y "
        "funcionamiento 'no supondrán incremento de gasto público', 'serán atendidos con las dotaciones presupuestarias ordinarias del "
        "Ministerio de Igualdad' y 'En ningún caso podrán suponer aumento neto de los gastos de personal al servicio de la "
        "Administración General del Estado'. Coste absorbido por el Ministerio de Igualdad." + NOCERO),
    "Notas de personal y apoyo ministerial": (
        "Secretaría: titular de la Subdirección General de Derechos LGTBI (apdo. 3.2); vicepresidencia primera: DG de Diversidad "
        "Sexual y Derechos LGTBI (apdo. 3.1.b). Dotaciones ordinarias del Ministerio de Igualdad, sin aumento neto de gastos de "
        "personal (DA única). La orden no regula retribuciones, dietas ni indemnizaciones de miembros." + VOC),
})
out.append({
    "ID": 62,
    "updates": d,
    "fuentes_nuevas": ["https://www.igualdad.gob.es/wp-content/uploads/IGD_577_2020.pdf"],
    "verificacion": "Sin cifras. Orden IGD/577/2020 leída en la copia oficial publicada por el Ministerio de Igualdad (texto del BOE núm. 178 de 27/06/2020, págs. 45276-45280, BOE-A-2020-6840): DA única, apdos. 3.1.b y 3.2.",
    "no_encontrado": "Sin financiación específica identificable a nombre del Consejo; búsqueda adicional limitada por cupo de búsquedas web agotado.",
})

# ---------------- 63 ----------------
u63 = "el departamento con competencias en infancia (Dirección General con competencias en participación infantil y apoyo al CEPIA)"
d = std(u63, "Orden JUI/80/2026, apdo. decimosexto.3")
d.update({
    "Presupuesto: texto completo": (
        "Sin presupuesto propio, verificado en norma: Orden JUI/80/2026 (BOE-A-2026-3001, BOE núm. 35 de 09/02/2026), apartado "
        "decimosexto.3 (pág. 20676): 'El departamento ministerial con competencias en materia de infancia proveerá al CEPIA de los "
        "medios necesarios'; la Dirección General con competencias en participación de la infancia y la adolescencia y apoyo al CEPIA "
        "'atenderá los gastos de funcionamiento del CEPIA con cargo a su presupuesto'. No contiene cláusula expresa de 'no incremento "
        "del gasto'. Coste absorbido por esa Dirección General." + NOCERO +
        " La secretaría puede actuar 'a través de la asistencia técnica de profesionales especializados' (apdo. duodécimo.1.d): posible "
        "contrato de asistencia no localizado. Deja sin efectos la Orden DSA/1009/2021 (apdo. decimonoveno) sin extinguir el Consejo."),
    "Notas de personal y apoyo ministerial": (
        "Secretaría: persona funcionaria designada por la Dirección General con competencias en participación infantil y apoyo al CEPIA "
        "(apdo. duodécimo, pág. 20675), que puede apoyarse en asistencia técnica externa (duodécimo.1.d). La DG presta 'los apoyos "
        "técnicos, administrativos y logísticos necesarios' (decimosexto.3). Los miembros lo son 'a título voluntario' (apdo. "
        "tercero.3); la orden no regula retribuciones ni indemnizaciones ni dice quién paga desplazamientos de consejeros y "
        "acompañantes. Consejeros menores no son plantilla. No repartir gasto ministerial."),
})
out.append({
    "ID": 63,
    "updates": d,
    "fuentes_nuevas": ["https://boe.es/boe/dias/2026/02/09/pdfs/BOE-A-2026-3001.pdf"],
    "verificacion": "Sin cifras. Orden JUI/80/2026 leída en PDF BOE (núm. 35, 09/02/2026): apdos. tercero.3, séptimo.2, duodécimo (págs. 20674-20675), decimosexto (pág. 20676) y decimonoveno.",
    "no_encontrado": "No se ha localizado contrato de asistencia técnica al CEPIA ni crédito a su nombre (búsqueda en PLACSP no posible: cupo de búsquedas web agotado).",
})

# ---------------- 64, 67, 68, 69 ----------------
pend = {
    64: ("Orden PCM/218/2020 (BOE-A-2020-3638)", ""),
    67: ("Orden TED/873/2025 (BOE-A-2025-16493)", ""),
    68: ("RD 686/2025 (consolidado en boe.es/eli/es/rd/2025/07/29/686/con)",
         " Tampoco se pudo comprobar si existe crédito o programa de acontecimiento de excepcional interés público vinculado a los eclipses."),
    69: ("Resolución de 23/04/2026 que publica el Acuerdo CM 21/04/2026 (BOE-A-2026-9157)", ""),
}
for _id, (norma, extra) in pend.items():
    out.append({
        "ID": _id,
        "updates": {},
        "fuentes_nuevas": [],
        "verificacion": "Sin cambios.",
        "no_encontrado": (
            "No se pudo leer en esta sesión " + norma + ": la URL del BOE no estaba disponible para lectura (requiere que aparezca en "
            "resultados de búsqueda) y el cupo de búsquedas web compartido se agotó antes de llegar a este órgano. Se mantiene 'Sin cifra "
            "propia actual verificada' hasta verificar la cláusula de gasto/medios." + extra),
    })

for r in out:
    for k, v in r["updates"].items():
        if isinstance(v, str):
            r["updates"][k] = v.replace(" de el ", " del ").replace(" a el ", " al ")
out.sort(key=lambda r: r["ID"])
path = "datos/resultados/B2_estatal_colegiados.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(len(out), "entries written")
