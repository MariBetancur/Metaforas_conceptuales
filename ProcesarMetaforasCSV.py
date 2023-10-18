import csv
import json

with open("D:\My Docs\Downloads\Datos Metaforas\Metaforas.csv", 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    
json_data = {"InfoMetaforas": []}
metafora_actual = None
URL_PROYECTO = 'https://github.com/MariBetancur/Metaforas_conceptuales/wiki/'

for row in data[1:]:
    metafora = row[0]
    origen = row[1]
    dominio_meta = row[2]
    dominio_fuente = row[3]
    exp_linguistica_metaforica = row[6]
    co_ontologica = row[7]
    co_epistemica = row[8]
    linkeable = URL_PROYECTO + metafora.replace(' ','-')

    if metafora:
        if metafora_actual:
            json_data["InfoMetaforas"].append(metafora_actual)
        metafora_actual = {
                            "Metafora": metafora,
                            "Origen": origen,
                            "Dominio fuente": dominio_fuente,
                            "Dominio meta": dominio_meta,
                            "Expresion linguistica": exp_linguistica_metaforica,
                            "Correspondencia ontologica" : co_ontologica,
                            "Correspondencia epistemica" : co_epistemica,
                            "linkeable" : linkeable
                          }

if metafora_actual:
    json_data["InfoMetaforas"].append(metafora_actual)

with open("D:\My Docs\Downloads\Datos Metaforas\Metaforas.json", 'w+') as json_file:
    json_file.write(json.dumps(json_data, indent=4, ensure_ascii=False))