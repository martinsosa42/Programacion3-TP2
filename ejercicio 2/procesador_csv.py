import os
import re
from resultado import Resultado

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(directorio_actual, 'f1_results.csv')

patron_regex = r"([^,\n]+),([^,\n]+),([^,\n]+),([^,\n]+),([^,\n]+),([^,\n]+)"

resultados = []

if os.path.exists(ruta_archivo):
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        coincidencias = re.finditer(patron_regex, contenido)

        next(coincidencias)
        for c in coincidencias:
            res = c.groups()
            resultado = Resultado(*res)
            resultados.append(resultado)

