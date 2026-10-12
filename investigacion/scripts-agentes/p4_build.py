import json
PB="https://www.juntadeandalucia.es/export/presup2026/personal/"
PROXY=("Proxy por subgrupo, no por función (parte de los A1/A2 hacen gestión): funcionarios A1 + A1/A2 + A2 -> núcleo técnico; C1 + C1/C2 + C2 -> administración y apoyo; "
       "puestos de adscripción mixta A2/C1 -> otro/no clasificable; laborales del convenio de la Junta: grupos 1-2 (titulados) -> núcleo, grupos 3-5 -> administración y apoyo. "
       "Altos cargos fuera del total (columna propia)")
NOLD="Puestos de libre designación: la RPT completa de la Junta en datos abiertos (dataset-jda_rpt.csv vía datos.juntadeandalucia.es/api/v0/rpt/all) no es legible con las herramientas disponibles (devuelve binario) y no hay fichero RPT propio de la entidad; no se estima."
out=[]
def add(ID, u, ver, nf=""):
    t=u.get("Desglose: total de referencia")
    a,b,c=(u.get(k) for k in ("Desglose: personal técnico/científico/inspector","Desglose: personal de administración y apoyo","Desglose: otro / no clasificable"))
    if t is not None: assert a+b+c==t,(ID,a,b,c,t)
    out.append({"ID":ID,"updates":u,"verificacion":ver,"no_encontrado":nf})

# 73 AACID
add(73,{
 "Desglose: personal técnico/científico/inspector":26,
 "Desglose: personal de administración y apoyo":18,
 "Desglose: otro / no clasificable":12,
 "Desglose: total de referencia":56,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026, plantilla de efectivos de 'otro personal' de AACID, agencia pública empresarial); no ocupación",
 "Desglose: criterio de clasificación":"Por función, a partir de la unidad y la categoría de la plantilla: unidades de cooperación y gestión de ayudas (Gestión de Ayudas, Unidad Técnica, Planificación/Evaluación y Coherencia, Cooperación con Iberoamérica, Cooperación con África y Mediterráneo): T.S., T.M. y jefaturas (J. Departamento/Unidad/Área) -> núcleo; unidades horizontales (Tecnología y Estrategia Digital; Buen Gobierno, Transparencia y Contratación; Personas y Desarrollo Profesional; Económico Financiero) completas + secretaria de dirección -> administración y apoyo; categoría 'Unidad de gestión' en unidades finalistas y en Dirección (función no indicada) y resto de Dirección (director, 5 coordinadores/as, 1 T.S.) -> otro",
 "Desglose: fuente":PB+"personalI-con-4-9.pdf",
 "Desglose: verificación":"Anexo de Personal 2026, personalI-con-4-9.pdf, pp. 867-869, tabla 'CLASIFICACIÓN DE PERSONAL / PLAZAS', Sevilla, TOTAL 56. Unidades: Gestión de Ayudas 4 (Unidad de gestión 1, T.S. 1.2 2, J. Departamento 1); Tecnología y Estrategia Digital 4 (T.M. 2.3 1, J. Dpto 1, Auxiliar de informática 2); Buen Gobierno, Transparencia y Contratación 6 (U. gestión 1, T.S. 1.4 1, T.S. 1.2 2, J. Dpto 1, Conserje 1); Personas y Desarrollo Profesional 4 (U. gestión 1, T.S. 1.2 1, J. Dpto 1, Conductor/a 1); Unidad Técnica 5 (T.S. 1.2 3, J. Unidad 1, J. Área 1); Económico Financiero 3 (U. gestión 1, T.S. 1.4 1, T.S. 1.2 1); Planificación, Evaluación y Coherencia 6 (U. gestión 1, T.S. 1.4 1, T.S. 1.2 1, J. Unidad 1, J. Dpto 1, J. Área 1); Iberoamérica 7 (U. gestión 1, T.S. 1.4 2, T.S. 1.2 3, J. Unidad 1); África y Mediterráneo 8 (U. gestión 1, T.S. 1.2 4, T.M. 2.3 1, J. Unidad 1, J. Dpto 1); Dirección 9 (Director 1, Secretaria de dirección 1, U. gestión 1, T.S. 1.2 1, Coordinador/a 5). Núcleo = 3+5+5+6+7 = 26; administración = 4+6+4+3 (unidades horizontales) + 1 secretaria = 18; otro = 4 'Unidad de gestión' en unidades finalistas + 8 de Dirección (director 1, U. gestión 1, T.S. 1, coordinadores 5) = 12. 26+18+12 = 56. Las abreviaturas T.S./T.M. (técnico superior/medio) no se desarrollan en el documento."
},"Plantilla AACID 2026 por unidad y categoría (personalI-con-4-9, pp. 867-869): 26 núcleo / 18 apoyo / 12 otro = 56 plazas.",
 "Altos cargos y eventuales: AACID no tiene sección en el Anexo I (solo plantilla de 'otro personal'); el Director figura como 1 plaza de la plantilla. "+NOLD)

# 74 Competencia
add(74,{
 "Desglose: personal técnico/científico/inspector":23,
 "Desglose: personal de administración y apoyo":13,
 "Desglose: otro / no clasificable":4,
 "Desglose: total de referencia":40,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026, sección 08.00), sin el alto cargo; no ocupación",
 "Desglose: criterio de clasificación":PROXY,
 "Altos cargos":1,
 "Desglose: fuente":PB+"personalI-b-5.pdf",
 "Desglose: verificación":"personalI-b-5.pdf, p. 37 'Resumen de anexo de personal', sección 08.00 Agencia de la Competencia y de la Regulación Económica de Andalucía: 'DIRECTORES GENERALES Y ASIMILADOS 1'; funcionarios 'GRUPO A1 20', 'GRUPO A1/A2 2', 'GRUPO A2 1', 'GRUPO A2/C1 4', 'GRUPO C1 1', 'GRUPO C1/C2 9', 'TOTAL FUNCIONARIOS 37'; laborales 'GRUPO 4 1', 'GRUPO 5 2', 'TOTAL LABORALES 3'; 'TOTAL 41'. Núcleo 20+2+1 = 23; administración 1+9 (C1, C1/C2) + 3 laborales = 13; otro 4 (A2/C1). 23+13+4 = 40 = 41 - 1 alto cargo. (La agrupación 'A1 22 / A2 5 / C1 10' de la ficha anterior funde los grupos mixtos.)"
},"Anexo de Personal 2026 sección 08.00 p. 37: 23/13/4 (+1 alto cargo).",
 "Personal eventual: el resumen del Anexo no tiene fila de eventuales (no se pone 0 por no ser literal). "+NOLD)

# 75 ATRIAN
add(75,{
 "Desglose: personal técnico/científico/inspector":446,
 "Desglose: personal de administración y apoyo":333,
 "Desglose: otro / no clasificable":52,
 "Desglose: total de referencia":831,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026, sección 10.39), sin el alto cargo; no ocupación",
 "Desglose: criterio de clasificación":PROXY,
 "Altos cargos":1,
 "Desglose: fuente":PB+"personalI-d-2.pdf",
 "Desglose: verificación":"personalI-d-2.pdf, p. 605 'Resumen de anexo de personal', sección 10.39 Agencia Tributaria de Andalucía: 'DIRECTORES GENERALES Y ASIMILADOS 1'; funcionarios 'GRUPO A1 251', 'GRUPO A1/A2 129', 'GRUPO A2 66', 'GRUPO A2/C1 52', 'GRUPO C1 50', 'GRUPO C1/C2 266', 'GRUPO C2 15', 'TOTAL FUNCIONARIOS 829'; laborales 'GRUPO 3 1', 'GRUPO 5 1'; 'TOTAL 832'. Núcleo 251+129+66 = 446; administración 50+266+15+1+1 = 333; otro 52 (A2/C1). 446+333+52 = 831 = 832 - 1 alto cargo. Alternativa en personas (no mezclada): Memoria Cuentas Anuales 2024 ATRIAN, nota 1, efectivos a 31/12/2024: A1 311, A2 102, C1 240, C2 48, G.III 1, G.V 1 = 703 (A1+A2 = 413; C1+C2+laborales = 290; incluye 1 alto cargo y 11 directivos)."
},"Anexo de Personal 2026 sección 10.39 p. 605: 446/333/52 (+1 alto cargo). Alternativa personas 2024 en verificación.",
 "Personal eventual: el resumen del Anexo no tiene fila de eventuales. "+NOLD)

# 76 CTPDA
add(76,{
 "Desglose: personal técnico/científico/inspector":36,
 "Desglose: personal de administración y apoyo":11,
 "Desglose: otro / no clasificable":4,
 "Desglose: total de referencia":51,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026, sección 07.00), sin el alto cargo; libre designación: puestos RPT funcionarios 2T/2026 (datos abiertos del Consejo)",
 "Desglose: criterio de clasificación":PROXY.replace("Altos cargos fuera del total (columna propia)","Las 2 plazas de personal eventual -> otro. Altos cargos fuera del total (columna propia)"),
 "Puestos de libre designación":20,
 "Altos cargos":1,
 "Personal eventual (confianza)":2,
 "Desglose: fuente":PB+"personalI-b-4.pdf",
 "Desglose: verificación":"personalI-b-4.pdf, p. 33 'Resumen de anexo de personal', sección 07.00: 'VICECONSEJEROS Y ASIMILADOS 1'; 'EVENTUALES 2'; funcionarios A1 31, A1/A2 4, A2 1, A2/C1 2, C1 3, C1/C2 7 (total 48); laborales Grupo 4 1; 'TOTAL 52'. Núcleo 31+4+1 = 36; administración 3+7+1 = 11; otro 2 (A2/C1) + 2 eventuales = 4; 36+11+4 = 51 = 52 - 1 alto cargo. Libre designación: RPT funcionarios 2T/2026 del Consejo (CSV datos abiertos, https://www.juntadeandalucia.es/datosabiertos/portal/dataset/ce12dae2-4d8c-44b6-88ea-8542803fd780/resource/d6d9db97-c3d6-4783-99ad-a1e9726c05fb/download/relacion-de-puestos-de-trabajo-funcionarios-2t.csv): 76 puestos; MODO DE ACCESO 'PLD' 20 (13 con carácter de ocupación Definitivo, 7 'Sin dotación'), PC 41, 'PC, SO' 13, 'D.2' 2. PLD incluye Secretario/a General (A1, 30), Directores/as de Área de Transparencia y de Protección de Datos (A1, 30), 6 gabinetes (A1, 29), 4 Consejerías Técnicas (A1, 28, sin dotación), Adjunto de la Dirección, Asesor/a Jurídico/a, 2 jefaturas de servicio, Coordinador Secretaría Dirección (A2-C1) y Secretario/a Alto Cargo (C1-C2)."
},"Anexo 2026 sección 07.00 p. 33 (36/11/4, 1 alto cargo, 2 eventuales) y RPT 2T/2026 del Consejo (20 PLD).")

# 97 ADA
add(97,{
 "Desglose: personal técnico/científico/inspector":858,
 "Desglose: personal de administración y apoyo":195,
 "Desglose: otro / no clasificable":266,
 "Desglose: total de referencia":1319,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026: Anexo I sección 01.31 + plantilla de 'otro personal'), sin los 2 altos cargos; no ocupación",
 "Desglose: criterio de clasificación":"Mixto. Anexo I (1.135 plazas): "+PROXY.replace("Altos cargos fuera del total (columna propia)","")+" 'Otro personal' (184 plazas, categorías sin función literal): por unidad; unidades TIC (SAE, Alpes, Subdirección de Sistemas de Información, Tecnologías de la Información), que son la función propia de la ADA -> núcleo (incluidos 2 mandos y 14 plazas G3 de la SSI); Servicios Generales y Personal -> administración y apoyo. Altos cargos fuera del total",
 "Altos cargos":2,
 "Desglose: fuente":PB+"personalI-c-1.pdf",
 "Desglose: verificación":"(1) personalI-c-1.pdf, p. 510 'Resumen de anexo de personal' sección 01.31: Viceconsejeros y asimilados 1, Directores generales y asimilados 1; funcionarios A1 358, A1/A2 258, A2 61, A2/C1 266, C1 68, C1/C2 82, C2 14 (total 1.107); laborales Grupo 2 3, Grupo 3 14, Grupo 4 9, Grupo 5 2 (total 28); TOTAL 1.137. (2) personalI-con-1b-1.pdf, pp. 700-704, plantilla 'otro personal' ADA, TOTAL 184: SAE 34 (Técnico C-F y 'Mandos E' 1), Alpes 3 (ALP. TMED/TSUP), Subdirección de Sistemas de Información 127 (G1/G2/G3 con nivel retributivo, incl. G3 6+6+2 y 'Subdirector 03' 1), Tecnologías de la Información 14 (Grupo 1/2), Servicios Generales y Personal 6 (Córdoba 2 'Técnico 1 DEVA'; Sevilla 4: técnico informático, B-5, B-1, A-3). Núcleo = 358+258+61+3 + 178 = 858; administración = 68+82+14 + 14+9+2 + 6 = 195; otro = 266 (A2/C1). Total 1.319 = 1.321 - 2 altos cargos."
},"Anexo 2026 sección 01.31 p. 510 + plantilla otro personal pp. 700-704: 858/195/266 (+2 altos cargos). El bloque A2/C1 (266) impide asignar una quinta parte.",
 "Personal eventual: no figura en el resumen del Anexo. "+NOLD)

# 98 TRADE
add(98,{
 "Desglose: personal técnico/científico/inspector":172,
 "Desglose: personal de administración y apoyo":121,
 "Desglose: otro / no clasificable":19,
 "Desglose: total de referencia":312,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026, plantilla de efectivos de 'otro personal' de TRADE); no ocupación",
 "Desglose: criterio de clasificación":"Por función, con unidad y categoría de la plantilla: direcciones finalistas (Internacionalización de la Economía, Desarrollo de Negocio y Soporte de Valor, Financiación Empresarial, Fomento Empresarial): técnicos/as de cualquier nivel, gestor de cartera y mandos/directores de esas direcciones -> núcleo; administrativos/as, secretaria de dirección y Gerente/a de Administración y Finanzas -> administración y apoyo; Dirección de Servicios Corporativos y Secretaría General completas -> administración y apoyo; Dirección General: 1 administrativo/a -> apoyo, resto (19: Director General, jefaturas, asesor y técnicos del gabinete) -> otro",
 "Desglose: fuente":PB+"personalI-con-4-2.pdf",
 "Desglose: verificación":"personalI-con-4-2.pdf, pp. 810-820, columnas 'CLASIFICACIÓN DE PERSONAL / PLAZAS'; total 312 (Almería 7, Cádiz 15, Córdoba 13, Granada 20, Huelva 7, Jaén 12, Madrid 3, Málaga 18, Sevilla 217). Sevilla por unidad: Internacionalización 37+1+3, Desarrollo de Negocio 27, Fomento 8, Financiación 42, Servicios Corporativos 7+3+44 (+Madrid 3 = 57), Secretaría General 25, Dirección General 20. Núcleo: provincias distintas de Sevilla 73 (técnicos de Financiación, Fomento, Desarrollo e Internacionalización) + Sevilla 99 (Internacionalización 33+1+3, Desarrollo 24, Fomento 7, Financiación 31) = 172. Administración: administrativos/as en direcciones finalistas 38 (19 fuera de Sevilla + Sevilla 4+3+1+11, este último incluye 'Gerente/a de Adm. y Fin.') + Servicios Corporativos 57 + Secretaría General 25 + 1 administrativo/a de la DG = 121. Otro: Dirección General 19. Advertencia: en Desarrollo de Negocio (Sevilla) una segunda lectura de las filas sumó 26 frente al subtotal impreso 27, por lo que la asignación de 1 plaza dentro de esa unidad puede variar entre núcleo y apoyo."
},"Plantilla TRADE 2026 (pp. 810-820): 172/121/19 = 312.",
 "Altos cargos: TRADE no tiene sección en el Anexo I; el Director General es 1 plaza de la plantilla. "+NOLD)

# 99 ACCUA
add(99,{
 "Desglose: personal técnico/científico/inspector":21,
 "Desglose: personal de administración y apoyo":18,
 "Desglose: otro / no clasificable":0,
 "Desglose: total de referencia":39,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026: Anexo I sección 15.31 + plantilla de 'otro personal'), sin el alto cargo; no ocupación",
 "Desglose: criterio de clasificación":"Mixto. Anexo I (11 funcionarios): proxy por subgrupo, no por función (A1 y A1/A2 -> núcleo; C1/C2 -> administración). 'Otro personal' (28): por función según unidad y categoría: Dirección de Evaluación y Acreditación (DEVA): licenciados y técnicos -> núcleo, administrativos y auxiliares -> apoyo; Servicios Generales y Personal, Administración y Finanzas, Servicios Jurídicos y Contratación y Gabinete de Comunicación -> administración y apoyo. Otro = 0 por clasificación (no por falta de dato). Alto cargo fuera del total",
 "Altos cargos":1,
 "Desglose: fuente":PB+"personalI-con-1b-4.pdf",
 "Desglose: verificación":"(1) personalI-c-7.pdf, p. 564, 'Resumen de anexo de personal' sección 15.31: 'DIRECTORES GENERALES Y ASIMILADOS 1', 'GRUPO A1 7', 'GRUPO A1/A2 2', 'GRUPO C1/C2 2', 'TOTAL FUNCIONARIOS 11', 'TOTAL 12' (sin laborales). (2) personalI-con-1b-4.pdf, pp. 719-720, TOTAL 28: Córdoba 15 = Servicios Generales y Personal 1 (Conserje DEVA) + DEVA 14 (Administrativo DEVA 2, Auxiliar DEVA 3, Licenciado DEVA 4, Técnico 1 DEVA 4, Técnico 2 DEVA 1); Sevilla 13 = Administración y Finanzas 4 (Técnico 2 [cifra no legible], Técnico B-5 1, Técnico B-6 1), Gabinete de Comunicación 1, Servicios Generales y Personal 3, Servicios Jurídicos y Contratación 2, DEVA 3 (Técnico A-9 1, A-11 2). Núcleo = 7+2 + 9 + 3 = 21; administración = 2 + 5 + (1+4+1+3+2) = 18. 21+18 = 39 = 40 - 1 alto cargo."
},"Anexo 2026 sección 15.31 p. 564 + plantilla pp. 719-720: 21/18/0 (+1 alto cargo).",
 "Personal eventual: no figura en el resumen. El inventario de puestos de ACCUA (datos abiertos, XLSX 3T/2026) no es legible con las herramientas disponibles. "+NOLD)

# 100 ISA
add(100,{
 "Desglose: personal técnico/científico/inspector":242,
 "Desglose: personal de administración y apoyo":147,
 "Desglose: otro / no clasificable":1,
 "Desglose: total de referencia":390,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026: Anexo I sección 13.32 + plantilla de 'otro personal'), sin el alto cargo; no ocupación",
 "Desglose: criterio de clasificación":"Mixto. Anexo I (38): proxy por subgrupo, no por función (A1, A1/A2 y laborales grupo 1 -> núcleo; C1/C2 -> administración). 'Otro personal' (352): por función según categoría: investigador/a senior, evaluador/a jefe de proyecto, técnico/a y auxiliar científico/a, asesor/a técnico/a, profesorado (Prof 1A-3B), técnicos (TCO II-IV, Tit. sup./medio, Espec. I-II) -> núcleo; Admin/Administrativo/a, Secretario/a de dirección, Auxiliar de servicios y Recepción -> administración y apoyo; los 9 técnicos de la Subdirección de Sistemas de Información y TIC -> apoyo (función de soporte); Consejero Delegado -> otro. Alto cargo fuera del total",
 "Altos cargos":1,
 "Desglose: fuente":PB+"personalI-con-1b-3.pdf",
 "Desglose: verificación":"(1) personalI-c-5.pdf, p. 556 'Resumen de anexo de personal' sección 13.32: 'VICECONSEJEROS Y ASIMILADOS 1', 'GRUPO A1 16', 'GRUPO A1/A2 7', 'GRUPO C1/C2 8', 'TOTAL FUNCIONARIOS 31', laborales 'GRUPO 1 7', 'TOTAL 39'. (2) personalI-con-1b-3.pdf, pp. 709-717, TOTAL 352 (Cádiz 2, Granada 173, Huelva 1, Jaén 1, Málaga 23, Sevilla 152). Suma por categoría: Investigador/a senior 56, Evaluador/a jefe proyecto 49, Prof (1A 7, 1B 7, 2A 13, 2B 3, 3A 9, 3B 16) 55, TCO II 10, TCO III 10, TCO IV 5, TCO TIC 1, Tit. sup 8, Tit. medio 6, Espec I 5, Espec II 1, Asesor/a técnico/a 7, Auxiliar científico/a 7, Técnico/a científico/a 1; Secretario/a de dirección 62, Admin 39, Administrativo/a 24, Auxiliar servicios 3, Recepción 2; Consejero delegado 1. Núcleo plantilla 212 (= 221 técnicos - 9 de la Subdirección SI y TIC: Prof 3B 1, TCO II 4, TCO IV 1, TCO TIC 1, Tit. medio 2); apoyo plantilla 130 + 9 = 139; otro 1. Total: núcleo 16+7+7+212 = 242; apoyo 8+139 = 147; otro 1; 390 = 391 - 1 alto cargo. Filas literales comprobadas en 2ª lectura para I+D+I (36), GOI (22), CABIMER (29), ACSA (38), Docencia (Admin 20), SI y TIC (12) y Dirección Entidad (5)."
},"Anexo 2026 sección 13.32 p. 556 + plantilla pp. 709-717: 242/147/1 (+1 alto cargo).",
 "Personal eventual: no figura en el resumen. "+NOLD)

# 101 Emergencias
add(101,{
 "Desglose: personal técnico/científico/inspector":3734,
 "Desglose: personal de administración y apoyo":115,
 "Desglose: otro / no clasificable":134,
 "Desglose: total de referencia":3983,
 "Desglose: unidad y fecha":"Plazas presupuestadas 2026 (Anexo de Personal 2026: Anexo I sección 01.39 + plantilla de 'otro personal'), sin el alto cargo; no ocupación",
 "Desglose: criterio de clasificación":"Mixto. Plantilla de 'otro personal' (3.793, categorías solo por grupo/nivel 1-4, sin denominación): por unidad. El operativo de incendios forestales (bomberos forestales y demás personal de la Subdirección de Incendios Forestales y Emergencias Ambientales, 3.609) -> núcleo funcional; subdirecciones horizontales (Recursos Humanos, Contratación y Recursos Materiales, Recursos Financieros, Tecnologías de la Información, Subdirección General, Desarrollo Corporativo Estratégico, Planificación de Calidad I+D+I) -> administración y apoyo; gerencias provinciales (función mixta no indicada), Infraestructuras/Obras Forestales y Paisajismo, Uso Público y Coord. TCA y Seguridad -> otro. Anexo I (190): proxy por subgrupo, no por función (A1, A1/A2, A2 -> núcleo; C1, C1/C2 y laborales grupos 3-5 -> apoyo; A2/C1 -> otro); parte de los laborales del grupo 3 pueden ser operadores de emergencias (no consta). Alto cargo fuera del total",
 "Altos cargos":1,
 "Desglose: fuente":PB+"personalI-con-2-1.pdf",
 "Desglose: verificación":"(1) personalI-d-1.pdf, p. 598 'Resumen de anexo de personal' sección 01.39: Directores generales y asimilados 1; funcionarios A1 32, A1/A2 92, A2 1, A2/C1 15, C1 1, C1/C2 6 (total 147); laborales Grupo 3 24, Grupo 4 6, Grupo 5 13 (total 43); TOTAL 191. (2) personalI-con-2-1.pdf, pp. 722-733, líneas 'TOTAL' literales: 'TOTAL SUBD INCEND FOREST Y EMERG AMB' 416 (Almería) + 364 (Cádiz) + 382 (Córdoba) + 424 y 84 (Granada) + 467 (Huelva) + 623 (Jaén) + 414 (Málaga) + 435 (Sevilla) = 3.609; Subdirección RRHH 4+4+1+3+5+1+16 = 34; Subdir. Contratación y R. Mat. 3+1+8+4 = 16; Subdirec. Rec. Financ. 6; Tecn. Información 1+1+1+3 = 6; Subdirección General 1; Serv. Des. Corp. Estratégico 1; Plan. Cal. I+D+I 1 (apoyo 65); Gerencias provinciales 108 (Almería 11, Cádiz 9, Córdoba 9, Granada 27 + bloques 'Gerencia de Granada' 2+2+6+3+2, Huelva 10, Jaén 11, Málaga 12, Sevilla 4); Infraest. O. Forest. y Paisajism. 2+1+1+5 = 9; Uso Público 1; Coord. TCA y Seguridad 1 (otro 119); 'TOTAL ... 3.793'. Núcleo 125 + 3.609 = 3.734; apoyo 7 + 43 + 65 = 115; otro 15 + 119 = 134; 3.983 = 3.984 - 1 alto cargo."
},"Anexo 2026 sección 01.39 p. 598 + plantilla pp. 722-733: 3.734/115/134 (+1 alto cargo); el operativo de incendios (3.609) va en núcleo.",
 "Personal eventual: no figura en el resumen. "+NOLD)

# 78 ACPUA
add(78,{
 "Desglose: personal técnico/científico/inspector":4,
 "Desglose: personal de administración y apoyo":3,
 "Desglose: otro / no clasificable":1,
 "Desglose: total de referencia":8,
 "Desglose: unidad y fecha":"Personas nominales del organigrama publicado en la web de ACPUA ('About us', sin fecha; consulta 12/10/2026). Hay además 1 puesto administrativo vacante, no incluido",
 "Desglose: criterio de clasificación":"Por función, según el área y el puesto publicados: Área técnica (coordinadora de calidad y 3 técnicos de calidad: docencia, internacional, prospectiva) -> núcleo; asistente de dirección, auxiliar administrativa del área técnica y jefa de administración -> administración y apoyo; directora -> otro (dirección)",
 "Desglose: fuente":"https://acpua.aragon.es/en/about-us",
 "Desglose: verificación":"Página 'About us' de ACPUA (https://acpua.aragon.es/en/about-us; misma página en https://acpua.aragon.es/en/node/37): Management: Director (Cristina Rodríguez Coarasa), Executive Assistant; Technical Area: Quality Assurance Coordinator, Teaching Quality Assurance Technician, International Quality Assurance Technician, Foresight Quality Assurance Technician, Administrative Assistant; Administration Area: Head of Administration, 'Administrative' vacante. 4 + 3 + 1 = 8 personas (9 puestos con la vacante). El SAR de ACPUA para ENQA (acpua_sar_es.pdf, pp. 9-10 y 16) solo dice que la plantilla 'ha cubierto ya todos los puestos' y remite a la web; el informe ENQA 2026 (p. 14) dice que en 2024 'se cubrieron todos los puestos vacantes'. La Memoria 2025 (apartado 'Organización interna y gestión de recursos humanos', p. 47) no es legible: la extracción de texto se corta en la p. 33."
},"Web 'About us' de ACPUA: 4 técnicos / 3 apoyo / 1 directora = 8 personas (+1 vacante).",
 "Libre designación, altos cargos y eventuales: no se ha encontrado RPT de ACPUA ni anexo de personal; la Memoria 2025 (pp. 47-57) no es legible con la herramienta.")

json.dump(out,open("datos/resultados/P4_andalucia_aragon.json","w"),ensure_ascii=False,indent=1)
print(len(out),[o["ID"] for o in out])
