# Coste de apoyo de órganos consultivos

Encargo literal enviado a un agente de investigación (Claude, tipo `general-purpose`), con las rutas adaptadas a esta carpeta.

---

Eres un investigador de organización administrativa española. Contexto: en una hoja de 125 entidades públicas, 40 órganos (observatorios, consejos, mesas, comisiones) se han clasificado como "consultivos sin medios propios": no tienen presupuesto propio y su coste lo absorbe un ministerio o consejería. El usuario quiere dejar claro que **sí tienen coste de personal**, aunque no se publique por separado.

Lee investigacion/lotes/C_apoyo.json (los 40 órganos, con su norma y lo que ya se sabe de su apoyo). Para cada uno, busca en fuentes oficiales (su norma de creación en BOE o boletín autonómico, órdenes de nombramiento, memorias, RPT, convenios, contratos en la Plataforma de Contratación) y devuelve:
- `unidad_apoyo`: qué unidad le presta secretaría y apoyo (DG, subdirección, unidad técnica), según la norma.
- `puestos_asignados`: número de puestos o personas asignados expresamente, SOLO si una fuente oficial lo dice (si no, null).
- `vocales`: número de miembros del pleno según la norma (número, o null si la norma no lo fija).
- `retribucion_miembros`: "no retribuidos", "dietas/indemnizaciones por asistencia", "asistencias retribuidas" o null, según la norma (cita el artículo).
- `gasto_identificable`: cualquier importe específico a su nombre (convenio, contrato, subvención) con año y URL; null si no hay.
- `fuente`: URL principal; `nota`: una o dos frases.
No estimes ni inventes. Muchos ya traen en "Notas de personal y apoyo ministerial" la unidad de apoyo: reutilízalo y céntrate en vocales, dietas y puestos asignados.

WebFetch solo abre URLs que hayan salido en resultados de WebSearch; máximo ~25 WebSearch (cupo compartido con otros agentes). Si una URL del BOE con "?id=" devuelve un documento con otro título, descártala.

Escribe datos/resultados/C_apoyo.json como lista de {"ID", "unidad_apoyo", "puestos_asignados", "vocales", "retribucion_miembros", "gasto_identificable", "fuente", "nota"} (las 40 entradas). Valida el JSON. Respuesta final: resumen breve (≤10 líneas).
