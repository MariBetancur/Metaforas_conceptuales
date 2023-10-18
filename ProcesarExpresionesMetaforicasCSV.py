import csv
import json

# Read the CSV file
with open("D:\My Docs\Downloads\Datos Metaforas\Expresiones metaforicas.csv", 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Prepare the JSON structure
json_data = {"InfoExpMetaforicas": []}
metafora_actual = None
aux_exp_linguistica_metaforica = None
exp_linguistica_metaforica = None
URL_PROYECTO = 'https://github.com/MariBetancur/Metaforas_conceptuales/wiki/'

for row in data[1:]:  # Skip the header row
    aux_exp_linguistica_metaforica = exp_linguistica_metaforica
    exp_linguistica_metaforica = row[0].strip().replace('<br>','')
    metafora_conceptual = row[1]
    origen = row[2]
    codigo = row[3]
    numero = row[4]
    dominio_fuente = row[5]
    dominio_meta = row[6]
    unidad_lexica_metaf = row[7]
    categoria_gramatical = row[8]
    significado_literal = row[9]
    significado_contextual = row[10]
    linkeable = URL_PROYECTO + exp_linguistica_metaforica.strip().replace(' ','-')
    

    if exp_linguistica_metaforica and aux_exp_linguistica_metaforica and exp_linguistica_metaforica != aux_exp_linguistica_metaforica :  # Start of a new metafora_conceptual
        if metafora_actual:  # Save the previous metafora_conceptual if exists
            json_data["InfoExpMetaforicas"].append(metafora_actual)
        metafora_actual = {
                            "Expresion linguistica": exp_linguistica_metaforica, 
                            "Metafora conceptual": [{}], 
                            "Origen": origen,
                            "Codigo": codigo,
                            "Numero": numero,
                            "Dominio fuente": dominio_fuente,
                            "Dominio meta": dominio_meta,
                            "Unidad lexica metaforizada": [{}],
                            "Categoria gramatical": [{}],
                            "Significado literal": [{}],
                            "Significado contextual": [{}],
                            "linkeable" : linkeable
                          }
        
    if metafora_conceptual:
        metafora_actual["Metafora conceptual"][0][str(len(metafora_actual["Metafora conceptual"][0]) + 1)] = metafora_conceptual

    if unidad_lexica_metaf:
        metafora_actual["Unidad lexica metaforizada"][0][str(len(metafora_actual["Unidad lexica metaforizada"][0]) + 1)] = unidad_lexica_metaf
        
    if categoria_gramatical:
        metafora_actual["Categoria gramatical"][0][str(len(metafora_actual["Categoria gramatical"][0]) + 1)] = categoria_gramatical

    if significado_literal:
        metafora_actual["Significado literal"][0][str(len(metafora_actual["Significado literal"][0]) + 1)] = significado_literal

    if significado_contextual:
        metafora_actual["Significado contextual"][0][str(len(metafora_actual["Significado contextual"][0]) + 1)] = significado_contextual
        

# Don't forget to save the last metafora_conceptual
if metafora_actual:
    json_data["InfoExpMetaforicas"].append(metafora_actual)

# Save the JSON to a file
with open("D:\My Docs\Downloads\Datos Metaforas\ExpresionesMetaforicas.json", 'w+') as json_file:
    json_file.write(json.dumps(json_data, indent=4, ensure_ascii=False)) 