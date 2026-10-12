import json
NR = None
R = []
def add(ID, unidad, puestos, vocales, retrib, gasto, fuente, nota):
    R.append({"ID": ID, "unidad_apoyo": unidad, "puestos_asignados": puestos, "vocales": vocales,
              "retribucion_miembros": retrib, "gasto_identificable": gasto, "fuente": fuente, "nota": nota})

add(8, "Secretaría: titular de la SG del Centro Nacional de Innovación e Investigación Educativa (art. 3.1.d RD 275/2007, redacción RD 3/2018); personal por redistribución de efectivos del Ministerio de Educación.",
    None, 27, None, None, "https://www.boe.es/eli/es/rd/2007/02/23/275/con",
    "27 vocales fijos (art. 3.1.c) más un vocal por cada comunidad autónoma que se adhiera voluntariamente; la norma no regula retribuciones ni indemnizaciones. La dotación de personal procede de redistribuir efectivos del Ministerio, sin nuevos puestos, y no se publica el número de efectivos.")

add(9, "Ministerio de Defensa: sede, apoyo administrativo y «órgano de trabajo permanente» (art. 53.2 LO 9/2011).",
    7, 9, "no retribuidos (art. 55.1 LO 9/2011: «La pertenencia al Observatorio no será retribuida»)",
    "2014: 5.212 EUR abonados por la Subsecretaría de Defensa (RED n.º 319, 2015, https://working.mde.es/Galerias/gabinete/red/2015/red-319-observatorio-vida-militar.pdf) | 2015: autorización de gasto de 55.000 EUR para dietas en la Sección 14-Defensa (Ley 36/2014 de PGE) y presupuesto 2016 del OVM de 55.979,10 EUR sin partida en la Ley 48/2015 (Memoria-Informe 2015 del OVM, https://www.prevencionintegral.com/sites/default/files/noticia/36030/field_adjuntos/pdft076-16observatoriovidamilitar20151.pdf)",
    "https://www.boe.es/eli/es/lo/2011/07/27/9/con",
    "Según la Memoria-Informe 2015 del propio Observatorio (copia alojada en un sitio de terceros), el órgano de trabajo permanente lo formaban 7 personas: un general secretario jefe, cinco oficiales y una funcionaria (en 2014 eran un general y cuatro oficiales en la reserva). Los miembros no son retribuidos, pero cobran dietas. En la Comisión de Defensa del 24/02/2026 (DSCD-15-CO-492) un diputado citó «aproximadamente 29 000 euros anuales asignados», y el presidente pidió «incrementar la plantilla» del órgano de trabajo.")

add(10, "Unidad Técnica y Secretaría Permanente atendidas por personal de la SG de Análisis, Estudios y Prospectiva Universitaria (art. 7.2 y DA única RD 1220/2010).",
    None, 18, None, None, "https://www.boe.es/eli/es/rd/2010/10/01/1220/con",
    "18 vocales: 3 del Consejo de Universidades, 3 de la CGPU, 3 estudiantes, 6 de sindicatos, patronal y consejos sociales y 3 de la SG de Universidades; con presidencia, vicepresidencia y secretaría suman 21 miembros. La norma no regula retribuciones; la DA única excluye incremento de puestos y de retribuciones, y no fija número de efectivos.")

add(11, "Secretariado: titular de una SG de la DG de la Función Pública (art. 4.1.e); medios técnicos, personales y materiales de la SE de Función Pública a través de la DG de la Función Pública (DA 2.ª.1 RD 868/2010).",
    None, 21, None, None, "https://www.boe.es/eli/es/rd/2010/07/02/868",
    "21 vocales: 6 de la AGE, 9 de CCAA y Ceuta y Melilla, 1 de la FEMP y 5 sindicales; con presidencia, dos vicepresidencias y secretario suman 25. La norma no regula retribuciones ni indemnizaciones y no fija puestos.")

add(12, "Secretaría General Permanente: titular de la SG de Análisis, Estrategia y Evaluación de la SE de Comercio (art. 4.3); medios técnicos, personales y materiales de la SE de Comercio (DA única RD 430/2009).",
    None, 24, "no retribuidos (DA única RD 430/2009: el funcionamiento «no supondrá incremento de gasto, ya sea por indemnizaciones, asistencias»)",
    None, "https://www.boe.es/eli/es/rd/2009/03/27/430",
    "Hasta 24 vocales (art. 4.1), entre ellos un máximo de 8 del sector privado, 2 sindicales y 2 universitarios; con presidencia y dos vicepresidencias suman hasta 27. La norma no prevé un régimen retributivo: excluye expresamente gasto por indemnizaciones y asistencias.")

add(13, "Secretaría: titular de la SG de Sensibilización, Prevención y Estudios de la Violencia contra las Mujeres, en la DGVG (art. 4.4 RD 752/2022); gastos personales y materiales con cargo al ministerio del que depende la DGVG (DA única). Esa SG elabora el informe anual.",
    None, 45, None,
    "Becas de formación en el Observatorio: 6 becas en 2022-2023, de 1.050 EUR brutos/mes más 600 EUR/año cada una (extracto BOE 22/03/2022) (https://violenciagenero.igualdad.gob.es/wp-content/uploads/DGVGInforma_becas.pdf) | Borrador de bases de 2026: entre 14.400 y 22.200 EUR brutos anuales por beca, sin número fijado (https://www.igualdad.gob.es/wp-content/uploads/2026/06/Orden-de-Bases-becas_BORRADOR.pdf)",
    "https://www.boe.es/eli/es/rd/2022/09/13/752/con",
    "45 vocalías: 18 de administraciones públicas, 6 institucionales (FEMP, Fiscalía, CGPJ, RTVE, Abogacía y Psicología), 19 de agentes sociales y sociedad civil y 2 expertas; con presidencia y dos vicepresidencias suman 48. La norma no regula retribuciones. Las becas tuteladas por personal de la DGVG son gasto con nombre propio, pero no son puestos de plantilla.")

add(15, "Secretario del Consejo y del Observatorio: un funcionario del ministerio designado por la SE competente en familias (arts. 7.1 y 11); medios personales y materiales del ministerio (DA única RD 613/2007).",
    None, 36, None, None, "https://www.boe.es/eli/es/rd/2007/05/11/613",
    "El Consejo tiene 36 consejeros (art. 6: 9 ministeriales, 8 del ministerio de asuntos sociales y 19 del movimiento asociativo); con los cargos suman 40. El Observatorio tiene 16 consejeros elegidos entre ellos (art. 10). La norma no regula retribuciones ni indemnizaciones.")

add(16, "Dirección pública: DG competente en discapacidad (art. 73.1 RDLeg 1/2013). La gestión técnica la presta el CERMI con la subvención, con personal propio que no es empleo público.",
    None, None, None,
    "100.000 EUR: subvención directa al CERMI «para el Observatorio Estatal de la Discapacidad» (RD 904/2025, art. 3.3.e), ejecutable en 2025-2026 (https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-20078) | 2023: 80.000 EUR de subvención nominativa (aplicación 29.102.231F.485), de los que 15.000 EUR eran para «Secretaría técnica» según el anexo 2 del convenio RPD-CERMI (https://www.boe.es/diario_boe/txt.php?id=BOE-A-2023-11877)",
    "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-20078",
    "No es un órgano colegiado con pleno. El convenio de 2023 solo crea una comisión de seguimiento de 4 miembros (cláusula 6.ª) y exige que el 100 % del personal técnico del CERMI asignado sean personas con discapacidad, sin fijar cuántas.")

add(17, "Secretaría del Pleno y del Comité Técnico: un funcionario de la DG competente en libro (art. 5.2 y art. 6.f RD 1574/2007); dotación de personal mediante modificación de la RPT del Ministerio de Cultura (DA 2.ª).",
    None, 32, None, None, "https://www.boe.es/eli/es/rd/2007/11/30/1574/con",
    "23 vocalías numeradas que suman hasta 32 personas: 9 de la AGE, 6 de CCAA, 1 de la FEMP, 11 del sector y hasta 5 expertos; con presidencia y vicepresidencia suman 34. La norma no regula retribuciones. Prevé puestos en la RPT, pero no publica cuántos.")

add(18, "Unidad técnica de la Estrategia NAOS (AESAN), con sus recursos humanos y materiales (apdo. Cuarto.1). Secretaría: un representante de AESAN responsable del seguimiento de NAOS (apdo. Tercero.1.D).",
    None, 14, "no retribuidos (apdo. Quinto del Acuerdo CM 18/01/2013: «no percibirán remuneración alguna en el ejercicio de sus funciones»)",
    None, "https://boe.es/boe/dias/2013/02/23/pdfs/BOE-A-2013-2074.pdf",
    "14 vocalías (AESAN, 4 ministeriales/CSD, CCAA, FEMP, FESNAD, sociedades científicas, colegios, FIAB, hostelería, distribución y consumidores) más presidencia y vicepresidencia. No se publica el número de efectivos de la Unidad NAOS dedicados al Observatorio.")

add(19, "DG competente en RSE (Economía Social y RSE): preparación, apoyo técnico y gestión (art. 2.2); su titular asume la secretaría y «podrá disponer de la asistencia de personal de apoyo» (art. 5.3, redacción RD 301/2026); medios de la SE de Economía Social (DA 4.ª).",
    None, 56, None, None, "https://www.boe.es/eli/es/rd/2008/02/15/221/con",
    "56 vocalías en cuatro grupos de 14 (empresariales, sindicales, otras organizaciones y AAPP; art. 5.1, versión del 11/04/2026). La norma no regula retribuciones ni indemnizaciones y no fija cuánto personal de apoyo hay.")

add(20, "Secretaría: titular de la SG de Programas Sociales, que «podrá ser asistido por el personal de apoyo necesario» (art. 8.1 RD 891/2005); la web ministerial la sitúa hoy en la SG de Servicios Sociales. Coste con cargo a créditos del ministerio (DA 2.ª).",
    None, 42, None, None, "https://www.boe.es/buscar/pdf/2005/BOE-A-2005-14549-consolidado.pdf",
    "Según el texto consolidado hay 42 vocalías (art. 4 y 7.1): 20 de la AGE, 20 del movimiento asociativo gitano, 1 de la Autoridad Independiente para la Igualdad de Trato y 1 del Instituto de las Mujeres. Esto corrige las «40 vocalías» de la ficha. La norma no regula retribuciones. La Oficina Técnica acordada en 2024 «con medios propios» no tiene cifra publicada.")

add(21, "Secretaría: Presidencia del Instituto de las Mujeres, O.A. (art. 7.1, redacción RD 634/2026); asistencia técnica a las vocalías «por medio de los servicios correspondientes» (art. 7.2.d); créditos del Ministerio de Igualdad (DA 4.ª).",
    None, 40, None, None, "https://www.boe.es/eli/es/rd/2009/11/20/1791/con",
    "40 vocalías (art. 4.1): 13 de AAPP, 20 de organizaciones de mujeres, 4 empresariales y sindicales y 3 expertas; con presidencia, dos vicepresidencias y secretaría suman 44. La norma no regula retribuciones ni indemnizaciones.")

add(29, "Según la norma, la secretaría es de la SG de Estructura de la Cadena Alimentaria (art. 11.1.d RD 64/2015); según la Memoria 2024, de la SG de Promoción de los Alimentos de España (DG de Alimentación, MAPA). Se financia con el presupuesto del MAPA (art. 13).",
    None, 26, "no retribuidos (art. 13 RD 64/2015: «ni sus miembros percibirán dietas por el ejercicio de sus funciones»)",
    None, "https://www.boe.es/eli/es/rd/2015/02/06/64/con",
    "26 vocales fijos más uno por cada organización profesional agraria más representativa (art. 11.1), con hasta 6 invitados. La Memoria 2024 cita 35 estudios de cadena de valor, pero no publica contrato, encargo, importe ni personal.")

add(47, "Secretaría: titular de la SG de Apoyo a la Competitividad del Pequeño Comercio (DG de Política Comercial), que gestiona los grupos de trabajo (apdos. Cuarto y Sexto); medios personales y materiales del departamento (apdo. Noveno).",
    None, 20, None, None, "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2018-15776",
    "20 vocales (12 de la AGE y sector público, 7 de organizaciones y 1 de medios de pago); con presidente, vicepresidente y secretario suman 23. El Acuerdo no regula retribuciones ni indemnizaciones. Título de BOE-A-2018-15776 verificado.")

add(48, "Gabinete de la persona titular del Ministerio: secretaría a cargo de un funcionario de carrera de nivel 28 o superior (art. 4.2) y vocalía de la Unidad de Mujeres y Ciencia (art. 4.1.i); medios del Ministerio (DA única RD 938/2020).",
    None, 18, None, None, "https://www.boe.es/eli/es/rd/2020/10/27/938",
    "18 vocalías (10 ministeriales y 8 de la Subsecretaría, las SSGG, el SECTI, los OPI, la UMyC y el Instituto de la Mujer); con presidencia y tres vicepresidencias suman 22. La norma no regula retribuciones.")

add(49, "TGSS: secretaría del Pleno a cargo del titular de la SG de Recaudación en Periodo Voluntario (art. 6.1.2.º) y, en las comisiones provinciales, de las subdirecciones provinciales de recaudación (art. 7.1.2.º); medios actuales sin aumento de dotaciones (DA única).",
    None, 14, None, None, "https://www.boe.es/eli/es/o/2019/06/05/tms667/con",
    "14 vocales en el Pleno (dos por TGSS, INSS, ISM, ITSS, Servicio Jurídico, sindicatos y patronal); con presidente y secretario suman 16. Hay además comisiones provinciales con unos 12-14 vocales cada una. La norma no regula retribuciones.")

add(50, "DG de Derechos Culturales: secretaría a cargo de una persona funcionaria designada por su titular (apdo. Tercero.1.d); recursos humanos y medios del Ministerio de Cultura (apdo. Quinto).",
    None, 9, None, None, "https://www.cultura.gob.es/dam/jcr:85ee66d9-d300-4e8a-9903-07653ae01b27/report-orden-reguladora-observatorio-igualdad.pdf",
    "Al menos 9 vocalías fijas (4 de la AGE y 5 asociaciones), ampliables por designación de la Presidencia (apdo. Tercero). La orden, firmada el 16/09/2024, no regula retribuciones ni indemnizaciones.")

add(51, "Instituto Cervantes: la Secretaría General ejerce la secretaría del Pleno (art. 4.3); la Dirección del IC preside la Comisión ejecutiva (art. 5.2); pueden asignarse puestos de la plantilla del IC (art. 5.7 RD 431/2022).",
    1, 10, None,
    "73.693,05 EUR: retribución anual del puesto «Dirección del Observatorio Global del Español», sin antigüedad, en la tabla de directivos fuera de convenio a junio de 2025 (Memoria IC 2024-2025, Organización, https://cervantes.org/sites/public/produccion/files/2025-12/memoria-2024-2025-instituto-cervantes-11-organizacion.pdf)",
    "https://www.boe.es/eli/es/rd/2022/06/07/431/con",
    "El Pleno tiene 10 vocales más la presidencia del ministro de Exteriores, y la Comisión ejecutiva 4 miembros. La memoria del Cervantes acredita al menos un puesto directivo propio (Dirección del OGE), sin publicar el resto del equipo. La norma no regula retribuciones de los miembros.")

add(52, "Unidad competente en regadíos del MAPA, la SG de Regadíos, Caminos Naturales e Infraestructuras Rurales (DGDRIFA), que gestiona la plataforma (art. 6.3 RD 854/2022).",
    None, None, None, None, "https://www.boe.es/eli/es/rd/2022/10/11/854/con",
    "No es un órgano colegiado: es una «plataforma en línea» sin miembros (arts. 6-7), así que no hay vocales ni retribuciones. Los gastos salen del presupuesto ordinario de la DGDRIFA (DA 1.ª y preámbulo), igual que los de la Mesa (ID 53).")

add(53, "Secretaría: una persona funcionaria A1 de la SG de Regadíos, Caminos Naturales e Infraestructuras Rurales del MAPA, que puede asistir con funcionarios de su Subdirección (art. 4.2.19.º y art. 5.3-5.4 RD 854/2022).",
    None, None, None, None, "https://www.boe.es/eli/es/rd/2022/10/11/854/con",
    "La norma no fija un total: hay 19 vocalías numeradas (1.º-18.º y 11.º bis) y varias agrupan a varias personas (CCAA, confederaciones hidrográficas, Fenacore, OPA). No regula retribuciones ni indemnizaciones.")

add(54, "Secretaría: titular de la SG de Emprendimiento y PYME (art. 14.5 RD 439/2024); medios personales, técnicos y presupuestarios del Ministerio de Industria y Turismo (DA única).",
    None, 20, "no retribuidos (art. 14.8 RD 439/2024: «no percibirán ninguna retribución o compensación económica»)",
    None, "https://www.boe.es/eli/es/rd/2024/04/30/439",
    "20 vocalías más la presidencia (art. 14.1); otros 9 organismos participan sin ser miembros (art. 14.6). La norma no fija puestos.")

add(55, "Proyecto conjunto del Ministerio de Economía, Comercio y Empresa, el Banco de España y la AEAT; la AEAT elabora los datos cada trimestre (página OME de Hacienda; análisis AEAT).",
    None, None, None, None, "https://www.hacienda.gob.es/es-ES/CDI/Paginas/Impuestos/OME/Observatorio-de-margenes-empresariales.aspx",
    "No se ha localizado norma, acuerdo ni convenio que fije composición, miembros, retribuciones o medios. El coste se reparte entre los participantes sin desglose.")

add(56, "Secretaría General Técnica del Ministerio de Sanidad: secretaría (apdo. Tercero.1.c) y coordinación de la Comisión Permanente (apdo. Noveno); medios materiales y personales del Departamento (apdo. Décimo).",
    None, 6, None, None, "https://www.sanidad.gob.es/organizacion/transparenciaGobierno/OCFCS/docs/ORDEN_MINISTERIAL.OBSERVATORIO_ANTIFRAUDE._FIRMA.pdf",
    "6 vocales (SE de Sanidad, Subsecretaría, AEMPS, INGESA, DG de Cartera Común y SG de Cohesión y Alta Inspección); con presidencia y secretaría suman 8. La Orden no regula retribuciones ni indemnizaciones.")

add(57, "Es una unidad organizativa de los Servicios Centrales de la DGGC (art. 8; DF 1.ª, nivel orgánico según RPT) y se apoya en las demás jefaturas (art. 8.2); medios de la DGGC (DA única).",
    None, None, None, None, "https://www.boe.es/boe/dias/2024/08/10/pdfs/BOE-A-2024-16600.pdf",
    "No es colegiado y no tiene vocales: su director es vocal permanente del COMGECET, un órgano distinto con presidencia y 9 vocales permanentes. Su personal es plantilla de la Guardia Civil por RPT, pero la Orden no publica el número de puestos ni el empleo del director.")

add(58, "MTDFP a través de la SE de Función Pública, que diseña y mantiene el Observatorio (art. 19.2 RD 371/2026); DG de Gobernanza Pública, para los cauces de buenas prácticas (art. 19.6); SG de Gobierno Abierto, secretaría del Foro (art. 13.1).",
    None, None, None, None, "https://www.boe.es/eli/es/rd/2026/05/06/371",
    "Es un «espacio virtual» dentro del Portal de la Transparencia, sin miembros propios. La gratuidad de la DA única.2 («no dará derecho a remuneración») se refiere al Foro de Gobierno Abierto, no al Observatorio.")

add(59, "Por el MAPA, medios humanos de la SG de Innovación y Digitalización (DGDRIFA); Cajamar ejecuta con medios propios (Plan Director y oficina técnica; adenda 2023, cláusula 4.ª).",
    None, None, None,
    "1.570.000 EUR: presupuesto total del convenio MAPA-Cajamar 2021-2026, con anualidad 2026 de 200.000 EUR (segunda adenda, cláusula 6.ª, BOE 22/12/2025, https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-26325)",
    "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-26325",
    "Se crea por convenio, no es un órgano colegiado con pleno. El personal ejecutor de Cajamar no es empleo público y no hay cifra publicada de efectivos del MAPA dedicados. El importe es de convenio, no gasto ejecutado.")

add(60, "Red.es (EPE del MTDFP) financia y supervisa; ejecuta el grupo de entidades coordinado por la Fundación Instituto Hermes, con medios propios (convenio BOE-A-2024-14138).",
    None, None, None,
    "Hasta 4.781.250 EUR: Red.es aporta hasta 3.825.000 EUR (80 %, PRTR) y las entidades al menos 956.250 EUR en especie; anualidad 2026 de 1.434.375 EUR (cláusula 4.ª, https://www.boe.es/diario_boe/txt.php?id=BOE-A-2024-14138)",
    "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2024-14138",
    "Es un espacio creado por convenio, sin pleno ni vocales en norma. El personal es de las entidades, no empleo público. No se ha leído la adenda de 07/05/2026.")

add(61, "DG de Políticas Palanca para el Cumplimiento de la Agenda 2030 (secretaría, apdo. Tercero.4); el Ministerio facilita los medios personales y materiales (apdo. Octavo.3), y además hay asistencia técnica contratada.",
    None, 61, "no retribuidos (apdo. Octavo.1 Orden DSA/819/2020: «no percibirán remuneración alguna por el ejercicio de sus funciones»)",
    "153.620,64 EUR (valor estimado, sin IVA): licitación de 2024 del «Servicio de asesoramiento y asistencia técnica al Consejo de Desarrollo Sostenible y a sus grupos de trabajo técnicos», exp. 242907PA0001, DOUE S 180/2024 de 16/09/2024 (https://ted.europa.eu/es/notice/554472-2024/pdf)",
    "https://www.boe.es/eli/es/o/2020/09/03/dsa819/con",
    "61 vocalías: 60 de la sociedad civil y 1 de la SE Agenda 2030; con presidencia, vicepresidencia y secretaría suman 64. Además del apoyo de la DG, hay un contrato externo de asistencia técnica a su nombre. Solo consta el anuncio de licitación: falta comprobar la adjudicación.")

add(62, "Secretaría: titular de la SG de Derechos LGTBI, con suplente funcionario A1 de esa SG (apdo. 3.2 y 5.5); dotaciones ordinarias del Ministerio de Igualdad, sin aumento de gastos de personal (DA única).",
    None, 31, None, None, "https://www.boe.es/eli/es/o/2020/06/24/igd577/con",
    "31 vocalías (apdo. 3.1): 10 de la AGE, 2 de CCAA, 1 local, 1 universitaria, 2 empresariales, 2 sindicales, 12 de entidades LGTBI y 1 de la Autoridad Independiente. Ni la Orden ni el Reglamento interno de 2021 regulan dietas o indemnizaciones.")

add(63, "Dirección General competente en participación infantil y apoyo al CEPIA (Ministerio de Juventud e Infancia): secretaría a cargo de una persona funcionaria designada por la DG, que puede actuar «a través de la asistencia técnica de profesionales especializados» (apdo. Duodécimo.1.d); la DG atiende los gastos con cargo a su presupuesto (apdo. Decimosexto.3).",
    None, 34, None, None, "https://www.boe.es/eli/es/o/2026/01/29/jui80",
    "34 consejeros de entre 8 y 17 años (apdo. Tercero.1), que participan «a título voluntario» (Tercero.3). La orden no regula dietas ni desplazamientos. No se ha localizado contrato de asistencia técnica a su nombre.")

add(64, "Departamento de Seguridad Nacional: Secretaría Técnica y órgano de trabajo permanente, con secretario designado entre su personal (apdo. Quinto.d Orden PCM/218/2020); la presidencia (JEMAD) puede recabar apoyos de su estructura.",
    None, None, None, None, "https://www.boe.es/eli/es/o/2020/03/13/pcm218/con",
    "La norma no fija el número de vocales: uno por cada departamento u organismo con representación en el Consejo de Seguridad Nacional, más la Agencia Espacial Española (Quinto.c, redacción 2023). No regula retribuciones.")

add(67, "Es un órgano administrativo de la SG de Política Forestal y Lucha contra la Desertificación (DG de Biodiversidad, Bosques y Desertificación, MITERD), con el rango que fije la RPT (artículo único.1-2 Orden TED/873/2025).",
    None, None, None, None, "https://www.boe.es/eli/es/o/2025/08/01/ted873",
    "No es colegiado y no tiene vocales. Su personal son puestos de la RPT del MITERD, pero la Orden no fija número ni jefatura y no se ha localizado la RPT. Se financia con los presupuestos del Ministerio (DA única).")

add(68, "Secretaría: titular de la Presidencia de la Comisión Nacional de Astronomía (art. 4.6 RD 686/2025); coordinación desde la SE de Ciencia, Innovación y Universidades; medios de los departamentos que la integran (DA 2.ª).",
    None, 13, None, None, "https://www.boe.es/eli/es/rd/2025/07/29/686/con",
    "13 vocalías ministeriales de rango DG o superior; con presidencia y vicepresidencia suman 15, más 3 directores científicos con voz y sin voto. No regula retribuciones. La subvención de 100.000 EUR a la Fundación ONCE (RD 815/2026) es para los eclipses, no para la Comisión.")

add(69, "DG de Protección Civil y Emergencias: la presidencia y los medios materiales y personales (apdo. Séptimo); secretaría a cargo del titular de la SG de Formación y Relaciones Institucionales (apdo. Cuarto.4).",
    None, None, None, None, "https://www.boe.es/boe/dias/2026/04/27/pdfs/BOE-A-2026-9157.pdf",
    "El Acuerdo no fija un total: hay una vocalía por ministerio, una por CA y ciudad autónoma (hasta 19), la FEMP y 30 de la sociedad civil (17 + 13). No regula retribuciones ni indemnizaciones.")

add(77, "Secretaría General de Ordenación del Territorio, a través de la DG del Instituto de Cartografía de Andalucía: apoyo técnico y funciones de secretaría (art. 4 Orden 13/03/2007).",
    None, None, "dietas/indemnizaciones por asistencia (DA única Orden 13/03/2007: miembros ajenos a la Junta «podrán percibir indemnizaciones en concepto de dietas y gastos de desplazamientos», Decreto 54/1989)",
    None, "https://cdn.juntadeandalucia.es/boja/2007/70/d5.pdf",
    "La norma no fija un número exacto: el Consejo (art. 3.2) tiene 8 miembros natos (altos cargos) y entre 7 y 12 nombrados entre expertos. Solo los miembros externos pueden cobrar dietas y desplazamientos.")

add(85, "Consejería de la Presidencia de Castilla y León, «con cargo a sus medios personales y materiales» (art. 12 Decreto 52/2014); la secretaría de la sección de convivencia escolar es la del Comité permanente (art. 7.3), cuyo secretario es el titular del órgano directivo central con funciones de secretariado de la Junta (art. 4.3).",
    None, None, "no retribuidos (DA 1.ª Decreto 52/2014: no generan derecho a «ninguna cuantía económica» en concepto de «remuneración, dietas o indemnizaciones»)",
    None, "https://sirdoc.ccyl.es/Biblioteca/Dosieres/DL203AtencionViolenciaGenero/pdfs/CyL-Decreto-52-2014-Observatorio.pdf",
    "El Decreto 52/2014 derogó el Decreto 8/2006 y convirtió el órgano en la sección de convivencia escolar del Observatorio de la Comunidad. La norma no fija un total de vocales, porque depende del número de organizaciones (art. 7). Vigencia posterior no auditada.")

add(88, "Según el Decreto 190/2007, art. 3.3, se relaciona con la Consejería de Educación a través de la DG de Política Educativa; no se ha verificado la unidad actual de secretaría.",
    None, None, None, None, "https://doe.juntaex.es/pdfs/doe/2024/2400o/24050192.pdf",
    "No se ha podido leer el texto del Decreto 28/2007 (enlaces bloqueados o sin texto), así que no constan vocales, retribuciones ni medios. Las órdenes de nombramiento (DOE 12/12/2024; DOE 104/2026) acreditan vocales nombrados por la Consejería con mandato de 4 años (art. 7).")

add(115, "Consejería competente en Juventud del Gobierno de Cantabria, que debe aportar medios «materiales, técnicos, económicos y humanos» (art. 19.2 Ley 1/2019) y apoyo técnico en contratación (art. 23).",
    None, None, None, None, "https://www.boe.es/buscar/act.php?id=BOE-A-2019-3488",
    "Es una corporación pública sectorial de base privada con personalidad propia (art. 1.1) y puede contratar personal laboral propio (art. 25 bis). La ley no fija los representantes de la Asamblea; la Comisión Permanente tiene 7-9 miembros (art. 12.1). El art. 22.2 admite remuneración o indemnizaciones según el reglamento interno, que no se ha verificado. No se ha localizado subvención nominativa 2025-2026.")

add(123, "La DG competente en igualdad y mujer presta el apoyo administrativo y material (art. 10 Decreto 53/2020); secretaría a cargo de un funcionario designado por esa DG.",
    None, 20, "no retribuidos (art. 8.6 Decreto 53/2020: la asistencia «no genera ningún derecho económico en concepto de remuneración o indemnización»)",
    None, "https://laadministracionaldia.inap.es/noticia.asp?id=1201913",
    "20 vocalías según el art. 6.1.c (instituciones, agentes sociales y colegios profesionales); con presidencia y vicepresidencia suman 22. La cifra procede del resumen del INAP del BOC de 21/08/2020 porque el BOC bloqueó la lectura directa, y conviene contrastarla con el texto oficial.")

ids_batch = [e['ID'] for e in json.load(open('investigacion/lotes/C_apoyo.json'))]
ids_out = [r['ID'] for r in R]
assert sorted(ids_batch) == sorted(ids_out), (set(ids_batch)-set(ids_out), set(ids_out)-set(ids_batch))
assert len(ids_out) == len(set(ids_out)) == 40
# order as batch
order = {i:k for k,i in enumerate(ids_batch)}
R.sort(key=lambda r: order[r['ID']])
json.dump(R, open('datos/resultados/C_apoyo.json','w'), ensure_ascii=False, indent=1)
d = json.load(open('datos/resultados/C_apoyo.json'))
print("OK", len(d))
print("vocales con número:", sum(1 for r in d if isinstance(r['vocales'], int)))
print("retribución definida:", sum(1 for r in d if r['retribucion_miembros']))
print("puestos:", [(r['ID'], r['puestos_asignados']) for r in d if r['puestos_asignados'] is not None])
print("gasto:", [r['ID'] for r in d if r['gasto_identificable']])
