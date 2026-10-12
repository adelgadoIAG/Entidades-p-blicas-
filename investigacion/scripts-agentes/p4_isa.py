isa = {
 ("Cádiz","PITA"): {"Asesor técnico":2},
 ("Granada","Dir Área Proyectos Investigación"): {"Prof 3B":1},
 ("Granada","Dirección Gestión y Servicios"): {"Admin":4},
 ("Granada","Subd Sistemas Información y TIC"): {"Auxiliar servicios":3,"Prof 3B":1,"TCO II":4,"TCO IV":1,"TCO TIC":1,"Tit medio":2},
 ("Granada","Dirección Entidad"): {"Admin":2,"Espec II":1,"Tit sup":2},
 ("Granada","Observatorio Infancia"): {"Recepción":2},
 ("Granada","Registro de Cáncer"): {"Admin":3,"Prof 2A":1,"Prof 3B":1,"TCO II":1,"Tit medio":3},
 ("Granada","CADIME"): {"Espec I":5,"TCO III":1,"Tit medio":1,"Tit sup":5},
 ("Granada","AETSA"): {"Secretario dirección":1},
 ("Granada","Biobanco"): {"Evaluador jefe proyecto":2,"Investigador senior":4},
 ("Granada","GENYO"): {"Administrativo":2,"Evaluador jefe proyecto":4,"Investigador senior":5,"Secretario dirección":2,"Técnico científico":1},
 ("Granada","IAVANTE"): {"Auxiliar científico":1,"Investigador senior":2,"Secretario dirección":2},
 ("Granada","RADYTTA"): {"Investigador senior":1},
 ("Granada","Dir Área Proyectos Investigación b"): {"Admin":2},
 ("Granada","AC Ciudadanía y Bienestar Social"): {"Prof 1B":1,"Prof 2A":4,"Prof 3A":3,"Prof 3B":4,"TCO III":1,"TCO IV":2},
 ("Granada","AC Ética y Políticas"): {"Prof 1A":1,"Prof 2A":1,"Prof 3A":1,"Prof 3B":4},
 ("Granada","AC Salud Internacional"): {"Admin":4,"Prof 1B":3},
 ("Granada","AC Salud Pública"): {"Prof 1A":2,"Prof 1B":2,"Prof 2A":6,"Prof 2B":1,"Prof 3A":3},
 ("Granada","Dir Área Proyectos Docencia"): {"Admin":20},
 ("Granada","Dir Área Proyectos Consultoría"): {"Admin":4},
 ("Granada","Consejero Delegado"): {"Consejero delegado":1},
 ("Granada","AC Tecnologías y Gestión Info"): {"Tit sup":1},
 ("Granada","AC Gestión Servicios y Profesionales Salud"): {"TCO III":5,"TCO II":3,"Prof 3B":2,"Prof 3A":2,"Prof 2B":2,"Prof 2A":1,"Prof 1B":1,"Prof 1A":4},
 ("Granada","AC Salud Pública b"): {"TCO IV":2,"TCO III":3,"TCO II":2,"Prof 3B":3},
 ("Huelva","PITA"): {"Asesor técnico":1},
 ("Jaén","PITA"): {"Asesor técnico":1},
 ("Málaga","UC"): {"Secretario dirección":3},
 ("Málaga","STIC"): {"Evaluador jefe proyecto":1,"Auxiliar científico":1},
 ("Málaga","PITA"): {"Asesor técnico":1},
 ("Málaga","IAVANTE"): {"Secretario dirección":7,"Investigador senior":2,"Auxiliar científico":1},
 ("Málaga","GOI"): {"Secretario dirección":2,"Investigador senior":3,"Auxiliar científico":1},
 ("Málaga","BIONAND"): {"Evaluador jefe proyecto":1},
 ("Sevilla","Área Bioinformática"): {"Investigador senior":1,"Evaluador jefe proyecto":1},
 ("Sevilla","RADYTTA"): {"Investigador senior":3,"Evaluador jefe proyecto":2,"Auxiliar científico":1},
 ("Sevilla","UC"): {"Secretario dirección":3},
 ("Sevilla","STIC"): {"Evaluador jefe proyecto":1},
 ("Sevilla","PITA"): {"Secretario dirección":1,"Investigador senior":1,"Asesor técnico":2},
 ("Sevilla","IAVANTE"): {"Secretario dirección":4,"Evaluador jefe proyecto":2},
 ("Sevilla","I+D+I"): {"Secretario dirección":12,"Investigador senior":6,"Evaluador jefe proyecto":10,"Auxiliar científico":2,"Administrativo":6},
 ("Sevilla","GOI"): {"Secretario dirección":4,"Investigador senior":6,"Evaluador jefe proyecto":6,"Administrativo":6},
 ("Sevilla","CABIMER"): {"Secretario dirección":3,"Investigador senior":18,"Evaluador jefe proyecto":6,"Administrativo":2},
 ("Sevilla","Biobanco"): {"Investigador senior":1},
 ("Sevilla","AETSA"): {"Secretario dirección":3,"Evaluador jefe proyecto":1},
 ("Sevilla","ACSA"): {"Secretario dirección":15,"Investigador senior":3,"Evaluador jefe proyecto":12,"Administrativo":8},
}
expected_unit = {("Granada","Subd Sistemas Información y TIC"):12,("Granada","GENYO"):14,("Granada","AC Gestión Servicios y Profesionales Salud"):20,("Sevilla","I+D+I"):36,("Sevilla","GOI"):22,("Sevilla","CABIMER"):29,("Sevilla","ACSA"):38}
from collections import Counter
prov=Counter(); cats=Counter()
for (p,u),d in isa.items():
    s=sum(d.values()); prov[p]+=s
    for c,n in d.items(): cats[c]+=n
    if (p,u) in expected_unit and expected_unit[(p,u)]!=s: print("MISMATCH",p,u,s)
print(prov, sum(prov.values()))
print(cats)
admin_cats={"Admin","Administrativo","Secretario dirección","Auxiliar servicios","Recepción"}
otro_cats={"Consejero delegado"}
support_units={"Subd Sistemas Información y TIC","Dirección Gestión y Servicios"}
core=adm=otro=0; core_cat=Counter(); adm_cat=Counter(); tic_tech=0
for (p,u),d in isa.items():
    for c,n in d.items():
        if c in otro_cats: otro+=n
        elif c in admin_cats: adm+=n; adm_cat[c]+=n
        elif u in support_units: adm+=n; tic_tech+=n
        else: core+=n; core_cat[c]+=n
print("core",core,dict(core_cat)); print("admin",adm,dict(adm_cat),"tic tech",tic_tech); print("otro",otro, core+adm+otro)
