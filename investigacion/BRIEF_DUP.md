# Brief: mapa de duplicidades Estado + 17 comunidades autónomas

## Qué quiere el usuario
Saber, para cada tema funcional, **cuántos organismos públicos hacen lo mismo** entre el Estado y las 17 comunidades autónomas ("no deberían existir sobre el mismo tema 17 organismos"). Es un análisis de armonización: cuántas copias hay, de qué tipo, y si el organismo estatal podría cubrir ese territorio.

Las 17 CCAA (usa exactamente estos nombres como claves): Andalucía, Aragón, Asturias, Illes Balears, Canarias, Cantabria, Castilla-La Mancha, Castilla y León, Cataluña, Comunitat Valenciana, Extremadura, Galicia, Madrid, Murcia, Navarra, País Vasco, La Rioja.

## Qué cuenta como "organismo sobre el tema"
Un organismo **específicamente dedicado** a ese tema, vigente a octubre de 2026:
- `ente` = con personalidad jurídica propia (agencia, organismo autónomo, ente público, entidad pública empresarial, sociedad, consorcio, fundación pública, autoridad independiente).
- `organo` = órgano específico sin personalidad pero diferenciado (consejo, comisión, observatorio, comisionado, oficina con nombre propio).
- `consejeria` = la función la hace una dirección general o servicio ordinario de la consejería, sin organismo específico (no cuenta como duplicado).
- `estado` = la comunidad no tiene organismo propio y la cubre el organismo estatal (p. ej. por convenio).
- `no` = no existe nada específico.
- `no_verificado` = no has podido comprobarlo.

Si una comunidad suprimió su organismo, márcalo como `consejeria` o `no` e indícalo en la nota (con año y norma).

## Fuentes
- Preferentemente **listas oficiales de redes o coordinación** que enumeran todos los organismos autonómicos a la vez (son eficientes): p. ej. red de agencias de calidad universitaria (REACU/ANECA/ENQA), consejos de transparencia (CTBG: convenios con CCAA y red de consejos), autoridades de competencia (CNMC: Consejo de Defensa de la Competencia / red autonómica), protección de datos (AEPD y autoridades autonómicas), autoridades de protección del informante designadas por cada CCAA (Ley 2/2023), CSIRT autonómicos (INCIBE/CCN), agencias energéticas regionales (IDAE / EnerAgen), consejos de la juventud (Consejo de la Juventud de España), observatorios autonómicos de convivencia escolar, institutos de seguridad y salud laboral (INSST), etc.
- Confirma con la **norma de creación** (BOE/boletín autonómico) cuando puedas. Cada celda lleva URL de la fuente que la sostiene (lista oficial o norma).
- Prensa solo como pista, nunca como fuente.

## Por tema, además
- `estado`: el organismo estatal equivalente (nombre, tipo, si cubre a CCAA sin organismo propio y cómo).
- `competencia`: base competencial en una frase (p. ej. "tributos cedidos: gestión autonómica por LOFCA"; "transparencia: cada administración puede crear su órgano o convenir con el CTBG (Ley 19/2013, DA 4ª)"). Sin opinión política.
- `cobertura_estatal`: sí/no/parcial y cómo (convenio, ley, por defecto).
- `presupuesto`: si con poco esfuerzo encuentras el presupuesto 2026 (o último) de cada organismo autonómico, añádelo (M EUR, año, fuente). Opcional.

## Reglas
- No inventes. Si no puedes verificar, `no_verificado`. No uses tu memoria como fuente: puede orientarte para buscar, pero la celda necesita una URL oficial.
- WebFetch solo abre URLs que hayan salido en resultados de WebSearch. El cupo de WebSearch es compartido entre 6 agentes: **máximo ~32 búsquedas por agente**. Prioriza listas oficiales que cubran muchas CCAA de golpe. Si una URL del BOE con "?id=" devuelve un documento con otro título, descártala.
- PDFs largos: parámetro `offset` de WebFetch.

## Salida
Lista JSON, un objeto por tema:
```json
[{"tema": "Consejos de transparencia",
  "estado": {"nombre": "...", "tipo": "ente|organo", "url": "..."},
  "competencia": "...", "cobertura_estatal": "...",
  "ccaa": {"Andalucía": {"tipo": "ente", "nombre": "...", "norma": "...", "url": "...", "presupuesto_m": null, "anio": null, "nota": "..."}, "...": {}},
  "notas": "...", "fuentes": ["..."]}]
```
Las 17 claves de `ccaa` deben estar siempre. Valida el JSON. Respuesta final: tabla breve tema → nº de CCAA con `ente`, con `organo`, con `estado`/`consejeria`/`no`, y `no_verificado` (≤12 líneas).
