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

# d) Mostrar los ultimos 20 resultados.
print("--- ULTIMOS 20 RESULTADOS ---")
for res in resultados[-20:]:
    print (res)
print("\n")

# e) Con diccionarios obtener los 3 pilotos mas ganadores.
pilotos_ganadores = {}
for r in resultados:
    if r.position == "1":
        pilotos_ganadores[r.driver_name] = (
            pilotos_ganadores.get(r.driver_name, 0) + 1
        )

pilotos_ganadores = sorted(
    pilotos_ganadores.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

print("--- TOP 3 PILOTOS MAS GANADORES ---")
for piloto, victorias in pilotos_ganadores:
    print(f"{piloto}: {victorias} victorias")
print("\n")

# f) Con diccionarios obtener las 3 escuderias mas ganadores.
escuderias_ganadoras = {}
for r in resultados:
    if r.position == "1":
        escuderias_ganadoras[r.constructor] = (
            escuderias_ganadoras.get(r.constructor, 0) + 1
        )

escuderias_ganadoras = sorted(
    escuderias_ganadoras.items(),
    key=lambda x: x[1],
    reverse=True
)[:3]

print("--- TOP 3 ESCUDERIAS MAS GANADORAS ---")
for escuderia, victorias in escuderias_ganadoras:
    print(f"{escuderia}: {victorias} victorias")
print("\n")