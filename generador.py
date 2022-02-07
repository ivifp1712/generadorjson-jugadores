import json, csv
from random import randint
import string
def listAlphabet():
  return list(string.ascii_uppercase)

clientes = int(input("¿Cuantos usuarios quieres crear?"))

d1 = open("generadorjson/datos/hombres.csv", "r", encoding="UTF-8")
nombres = []
for x in d1.readlines():
    if "nombre" in x:
        continue
    else:
        nombres.append("")
        for y in x:
            if y != ",":
                nombres[len(nombres)-1] += y
            else:
                temp = nombres[len(nombres)-1] 
                nombres[len(nombres)-1] = temp.title()
                break
d2 = open("generadorjson/datos/mujeres.csv", "r", encoding="UTF-8")
for x in d2.readlines():
    if "nombre" in x:
        continue
    else:
        nombres.append("")
        for y in x:
            if y != ",":
                nombres[len(nombres)-1] += y
            else:
                temp = nombres[len(nombres)-1] 
                nombres[len(nombres)-1] = temp.title()
                break
d3 = open("generadorjson/datos/apellidos.csv", "r", encoding="UTF-8")
apellidos = []
for x in d3.readlines():
    if "apellido" in x:
        continue
    else:
        apellidos.append("")
        for y in x:
            if y != ",":
                apellidos[len(apellidos)-1] += y
            else:
                temp = apellidos[len(apellidos)-1] 
                apellidos[len(apellidos)-1] = temp.title()
                break


calles = []
d4 = open('generadorjson/datos/calles.csv', "r", newline='') 
reader = csv.reader(d4, delimiter=';')

for row in reader:
    if row[1] == "CALLE":
        calles.append(f"Calle {row[2].title()} {row[3].title()}")
    if row[1] == "AVENIDA":
        calles.append(f"Avenida {row[2].title()} {row[3].title()}")

data = []
i = 1
posiciones = ["Portero", "Defensa", "Centrocampista", "Delantero"]
while i < (clientes+1):
    data.append({
        'dorsal': f'{i}',
        'nombre': f'{nombres[randint(0,len(nombres))]}',
        'apellidos': f'{apellidos[randint(0,len(apellidos))]}',
        'telefono' : f'6{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}',
        'direccion': {
            'calle': f'{calles[randint(0,len(calles))]}',
            'numero': f'{randint(1,999)}',
            'piso': f'{randint(1,5)}',
            'letra':f'{listAlphabet()[randint(0,6)]}'
        },
        'posicion_principal': f'{posiciones[randint(0,3)]}',
        'posicion_alternativa': f'{posiciones[randint(0,3)]}'
    })
    i += 1

with open('generadorjson/datos/data.json', 'w') as file:
    json.dump(data, file, indent=5, ensure_ascii=False)

print("--JSON CREADO CON ÉXITO--")

