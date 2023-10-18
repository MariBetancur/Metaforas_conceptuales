import json
from py_markdown_table.markdown_table import markdown_table

# Load data from the JSON file
file_path = r"D:\My Docs\Downloads\Datos Metaforas\ExpresionesMetaforicas.json"

with open(file_path, "r") as file:
    dominios_data = json.load(file)


URL_PROYECTO = 'https://github.com/MariBetancur/Metaforas_conceptuales/wiki/'

exp_metaforicas = dominios_data.get("InfoExpMetaforicas", [])
resultado_tabla_exp_metaforica = []
resultado_metafora_conceptual = []
resultado_unidad_lexica = []

for dato in exp_metaforicas:
    exp_linguistica = dato.get("Expresion linguistica", "")
    origen = dato.get("Origen", "")
    codigo = dato.get("Codigo", "")
    numero = dato.get("Numero", "")

    nombre_archivo = exp_linguistica.replace(' ','-').replace('"','')

    tabla_exp_metaforica = {
        "Origen": origen,
        "Código": codigo,
        "Número": numero
    }
    resultado_tabla_exp_metaforica.append(tabla_exp_metaforica)
    
    tabla_exp_metaforica_estructurada = markdown_table(resultado_tabla_exp_metaforica).set_params(row_sep='markdown', quote=False).get_markdown()
    
    metafora_conceptual = dato.get("Metafora conceptual", "")
    metafora_conceptual_values = metafora_conceptual[0]
    # Loop through the values
    for key, value in metafora_conceptual_values.items():
        metafora_relacionada = value
        metafora_link = f"[{metafora_relacionada}](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/{metafora_relacionada.replace(' ','-')})"

        tabla_metafora = {
            "Metáfora conceptual": metafora_link
        }
        resultado_metafora_conceptual.append(tabla_metafora)

    if not resultado_metafora_conceptual:
        tabla_metafora = {
            "Metáfora conceptual": ""
        }
        resultado_metafora_conceptual.append(tabla_metafora)

    # Convert the list of dictionaries into a Markdown table
    tabla_metafora_estructurada = markdown_table(resultado_metafora_conceptual).set_params(row_sep='markdown', quote=False).get_markdown()

  
    for i, meta_concept in enumerate(dato["Metafora conceptual"][0].values()):
        unidad_lexica = dato["Unidad lexica metaforizada"][0][str(i + 1)]
        categoria_gramatical = dato["Categoria gramatical"][0][str(i + 1)]
        significado_literal = dato["Significado literal"][0][str(i + 1)]
        significado_contextual = dato["Significado contextual"][0][str(i + 1)]
        
        tabla_unidad_lexica = {
            "Unidad léxica metaforizada": unidad_lexica,
            "Categoría gramatical" : categoria_gramatical,
            "Significado literal" : significado_literal,
            "Significado contextual" : significado_contextual
        }
        resultado_unidad_lexica.append(tabla_unidad_lexica)

    if not resultado_unidad_lexica:
        tabla_unidad_lexica = {
            "Unidad léxica metaforizada": "",
            "Categoría gramatical" : "",
            "Significado literal" : "",
            "Significado contextual" : ""
        }        
        resultado_unidad_lexica.append(tabla_unidad_lexica)
        
    # Convert the list of dictionaries into a Markdown table
    tabla_unidad_lexica_estructurada = markdown_table(resultado_unidad_lexica).set_params(row_sep='markdown', quote=False).get_markdown()

    datos_archivo_md = f"[Expresión lingüístca metafórica:](https://github.com/MariBetancur/Metaforas_conceptuales/wiki/Expresiones-lingüísticas-metafóricas) {exp_linguistica}\n\n"
    
    datos_archivo_md += f"{tabla_exp_metaforica_estructurada}\n\n"
    datos_archivo_md += f"{tabla_metafora_estructurada}\n\n"
    datos_archivo_md += f"{tabla_unidad_lexica_estructurada}\n\n"

    with open(f"D:\My Docs\Desktop\Bel\Metaforas_conceptuales.wiki\Expresiones-Linguisticas\{nombre_archivo}.md", 'w+',encoding='utf8') as archivo_metafora:
        archivo_metafora.write(datos_archivo_md)

    resultado_tabla_exp_metaforica = []
    resultado_metafora_conceptual = []
    resultado_unidad_lexica = []
    datos_archivo_md = ""