# 4. Duplicidades entre el Estado y las comunidades

Pregunta: para cada tema, ¿cuántos organismos hacen lo mismo entre el Estado y las 17 comunidades? El máximo posible es 18.

## Cómo se cuenta

Cada celda (tema × territorio) tiene un tipo y una fuente oficial: una lista de una red de coordinación o la norma de creación.

| Tipo | Significado | ¿Cuenta como organismo? |
|---|---|---|
| `estatal` | El organismo del Estado | Sí |
| `ente` | Organismo autonómico con personalidad jurídica (agencia, organismo autónomo, ente, fundación…) | Sí |
| `organo` | Órgano autonómico específico sin personalidad (consejo, observatorio, oficina con nombre propio) | Sí |
| `consejeria` | Lo hace una dirección general de la consejería | No |
| `estado` | La comunidad no tiene organismo propio y la cubre el estatal (por convenio, ley o defecto) | No |
| `no` | No existe nada específico | No |
| `no_verificado` | No se pudo comprobar | No: queda pendiente |

Las instrucciones y las fuentes preferentes están en [`investigacion/BRIEF_DUP.md`](../investigacion/BRIEF_DUP.md). Los resultados por tema están en `datos/resultados/DUP1.json` a `DUP5.json`. En el Excel, la hoja «Duplicidades por tema» tiene una celda por territorio y la fuente de cada una.

## Resultado

| Tema | Estatal | Organismos verificados | Sin verificar |
|---|---|---|---|
| Observatorios de convivencia escolar | Observatorio Estatal | 15 | 3 |
| Consejos de transparencia | CTBG | 13 | 0 |
| Formación de empleados públicos | INAP | 13 | 4 |
| Seguridad y salud laboral | INSST | 13 | 0 |
| Agencias tributarias | AEAT | 12 | 0 |
| Consejos de la juventud | Consejo de la Juventud de España | 12 | 6 |
| Calidad universitaria | ANECA | 11 | 0 |
| Agencias de la energía | IDAE | 11 | 2 |
| Igualdad y violencia de género | Observatorio Estatal | 11 | 7 |
| Administración digital y TIC | AEAD | 10 | 7 |
| Defensa de la competencia | CNMC | 10 | 0 |
| Antifraude y protección del informante | AIPI | 10 | 0 |
| Investigación e innovación | AEI y CDTI | 9 | 8 |
| Emergencias 112 | — (el Estado no presta el 112) | 9 | 6 |
| Ciberseguridad | INCIBE y CCN-CERT | 8 | 10 |
| Cooperación al desarrollo | AECID | 6 | 12 |
| Salud pública | AESAP | 5 | 0 |
| Protección de datos | AEPD | 4 | 0 |
| Consejos audiovisuales | CNMC | 4 | 12 |
| Evaluación de políticas públicas | Agencia Estatal de Evaluación | 3 | 13 |
| Seguridad ferroviaria | AESF | 2 | 3 |

En cinco temas **el Estado ya cubre o puede cubrir** los territorios sin organismo propio:
- **Transparencia:** el CTBG, por convenio.
- **Protección de datos:** la AEPD, por defecto.
- **Competencia:** la CNMC, por defecto.
- **Calidad universitaria:** ANECA, en 7 comunidades.
- **Ciberseguridad pública:** el CCN-CERT, de referencia por ley.

Esto sostiene buena parte de los veredictos «Integrar».

## Pendiente

Hay 93 celdas sin verificar, concentradas en cooperación, audiovisual, evaluación, ciberseguridad e I+D+i. Hasta que se verifiquen, los recuentos de esos temas son un mínimo.
