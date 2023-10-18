import json
from py_markdown_table.markdown_table import markdown_table

# Load data from the JSON file
file_path = r"D:\My Docs\Downloads\Datos Metaforas\Metaforas.json"

with open(file_path, "r") as file:
    metaforas_data = json.load(file)


URL_PROYECTO = 'https://github.com/MariBetancur/Metaforas_conceptuales/wiki/'

metaforas = metaforas_data.get("InfoMetaforas", [])
resultado_dominio = []


for dato in metaforas:
    metafora = dato.get("Metafora", "")
    origen = dato.get("Origen", "")
    dominio_fuente = dato.get("Dominio fuente", "")
    dominio_meta = dato.get("Dominio meta", "")
    expresion_metaforica = dato.get("Expresion linguistica", "")
    correspondencia_ontologica = dato.get("Correspondencia ontologica", "")
    correspondencia_epistemica = dato.get("Correspondencia epistemica", "")


    nombre_archivo = metafora.replace(' ','-').replace('/','-')
    dominio_fuente_link = f"[{dominio_fuente}](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/{dominio_fuente.replace(' ','-')})"
    dominio_meta_link = f"[{dominio_meta}](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/{dominio_meta.replace(' ','-')})"
    expresion_metaforica_link = f"[{expresion_metaforica}](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/{expresion_metaforica.replace(' ','-')})"
    
    tabla_dominio = {
        "Dominio fuente": dominio_fuente_link,
        "Dominio meta": dominio_meta_link
    }
    resultado_dominio.append(tabla_dominio)

    # Convert the list of dictionaries into a Markdown table
    tabla_dominio_estructurada = markdown_table(resultado_dominio).set_params(row_sep='markdown', quote=False).get_markdown()

    datos_archivo_md = f"[Metáfora:](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/Met%C3%A1foras-conceptuales) {metafora}\n\n"
    datos_archivo_md += f"**Origen:** {origen}\n\n"
    datos_archivo_md += f"{tabla_dominio_estructurada}\n\n"
    datos_archivo_md += "**Metáforas relacionadas:**\n\n"
    datos_archivo_md += f"**Expresiones lingüísticas metafóricas:** {expresion_metaforica_link}\n\n"
    datos_archivo_md += f"**Correspondencias ontológicas:** {correspondencia_ontologica}\n\n"
    datos_archivo_md += f"**Correspondencias epistémicas:** {correspondencia_epistemica}"

    with open(f"D:\My Docs\Desktop\Bel\Metaforas_conceptuales.wiki\Metaforas\{nombre_archivo}.md", 'w+',encoding='utf8') as archivo_metafora:
        archivo_metafora.write(datos_archivo_md)

    resultado_dominio = []
    datos_archivo_md = ""