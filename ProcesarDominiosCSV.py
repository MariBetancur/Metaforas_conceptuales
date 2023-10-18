import csv
import json


with open("D:\My Docs\Downloads\Datos Metaforas\Dominios.csv", 'r') as f:
    reader = csv.reader(f)
    data = list(reader)


json_data = {"InfoDominios": []}
dominio_actual = None
URL_PROYECTO = 'https://github.com/MariBetancur/Metaforas_conceptuales/wiki/'

for row in data[1:]:
    dominio = row[0]
    dominio_relacionado = row[1]
    dominio_fuente = row[2]
    dominio_meta = row[3]    
    linkeable = URL_PROYECTO + dominio.replace(' ','-')

    if dominio:
        if dominio_actual:
            json_data["InfoDominios"].append(dominio_actual)
        dominio_actual = {
                            "Dominios": dominio,
                            "Dominios relacionados": [{}],
                            "Como dominio fuente": [{}],
                            "Como dominio meta": [{}],
                            "linkeable" : linkeable
                         }

    if dominio_relacionado:
        dominio_actual["Dominios relacionados"][0][str(len(dominio_actual["Dominios relacionados"][0]) + 1)] = dominio_relacionado
    
    if dominio_fuente:
        dominio_actual["Como dominio fuente"][0][str(len(dominio_actual["Como dominio fuente"][0]) + 1)] = dominio_fuente

    if dominio_meta:
        dominio_actual["Como dominio meta"][0][str(len(dominio_actual["Como dominio meta"][0]) + 1)] = dominio_meta


if dominio_actual:
    json_data["InfoDominios"].append(dominio_actual)


with open("D:\My Docs\Downloads\Datos Metaforas\Dominios.json", 'w+') as json_file:
    json_file.write(json.dumps(json_data, indent=4, ensure_ascii=False)) 