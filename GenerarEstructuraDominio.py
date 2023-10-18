import json
from py_markdown_table.markdown_table import markdown_table

# Load data from the JSON file
file_path = r"D:\My Docs\Downloads\Datos Metaforas\Dominios.json"

with open(file_path, "r") as file:
    dominios_data = json.load(file)


URL_PROYECTO = 'https://github.com/MariBetancur/Metaforas_conceptuales/wiki/'

dominios = dominios_data.get("InfoDominios", [])
resultado_dominio_actual = []
resultado_dominio_fuente = []
resultado_dominio_meta = []


for dato in dominios:
    dominio = dato.get("Dominios", "")
    origen = dato.get("Origen", "")
    
    expresion_metaforica = dato.get("Expresion linguistica", "")

    nombre_archivo = dominio.replace(' ','-')

    dominio_fuente = dato.get("Como dominio fuente", "")
    como_dominio_fuente_values = dominio_fuente[0]

    tabla_dominio_actual = {
        "Dominio actual": dominio,
        "Dominio relacionado": "",
        "Tipo de relación": ""
    }
    resultado_dominio_actual.append(tabla_dominio_actual)
    
    tabla_dominio_actual_estructurada = markdown_table(resultado_dominio_actual).set_params(row_sep='markdown', quote=False).get_markdown()

    # Loop through the values
    for key, value in como_dominio_fuente_values.items():
        metafora_relacionada = value
        dominio_fuente_link = f"[{metafora_relacionada}](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/{metafora_relacionada.replace(' ','-')})"

        tabla_dominio_fuente = {
            "Como dominio fuente": dominio_fuente_link
        }
        resultado_dominio_fuente.append(tabla_dominio_fuente)

    if not resultado_dominio_fuente:
        tabla_dominio_fuente = {
            "Como dominio fuente": ""
        }
        resultado_dominio_fuente.append(tabla_dominio_fuente)    

    # Convert the list of dictionaries into a Markdown table
    tabla_dominio_fuente_estructurada = markdown_table(resultado_dominio_fuente).set_params(row_sep='markdown', quote=False).get_markdown()

    dominio_meta = dato.get("Como dominio meta", "")
    como_dominio_meta_values = dominio_meta[0]

    for key, value in como_dominio_meta_values.items():
        dato_meta = value
        dominio_meta_link = f"[{dato_meta}](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/{dato_meta.replace(' ','-')})"

        tabla_dominio_meta = {
            "Como dominio meta": dominio_meta_link
        }
        resultado_dominio_meta.append(tabla_dominio_meta)

    if not resultado_dominio_meta:
        tabla_dominio_meta = {
            "Como dominio meta": ""
        }
        resultado_dominio_meta.append(tabla_dominio_meta)    

    # Convert the list of dictionaries into a Markdown table
    tabla_dominio_meta_estructurada = markdown_table(resultado_dominio_meta).set_params(row_sep='markdown', quote=False).get_markdown()

    datos_archivo_md = f"[Dominio:](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/Dominio) {dominio}\n\n"
    datos_archivo_md += "## Dominios relacionados\n\n"
    datos_archivo_md += f"{tabla_dominio_actual_estructurada}\n\n"
    datos_archivo_md += "## Metáforas que usan este dominio\n\n"
    datos_archivo_md += f"{tabla_dominio_fuente_estructurada}\n\n"
    datos_archivo_md += f"{tabla_dominio_meta_estructurada}\n\n"

    with open(f"D:\My Docs\Desktop\Bel\Metaforas_conceptuales.wiki\Dominios\{nombre_archivo}.md", 'w+',encoding='utf8') as archivo_metafora:
        archivo_metafora.write(datos_archivo_md)

    resultado_dominio_actual = []
    resultado_dominio_fuente = []
    resultado_dominio_meta = []
    datos_archivo_md = ""