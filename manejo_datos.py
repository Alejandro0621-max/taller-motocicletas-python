import csv
from pathlib import Path

p= Path(".")
carpeta = p/"datos"
carpeta.mkdir(exist_ok=True)




def ingresar_datos(nombre_archivo: str, datos: dict):
    archivo = carpeta/f"{nombre_archivo}.csv"
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        escritura= csv.writer(f, delimiter="|")
        escritura.writerow(datos.values())

def nueva_informacion(nombre_archivo: str, datos: dict):
    archivo = carpeta/f"{nombre_archivo}.csv"
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        escritura= csv.writer(f, delimiter="|")
        escritura.writerow(datos.keys())
        escritura.writerow(datos.values())

def registrar(nombre_archivo: str, datos: dict):
    archivo = carpeta/f"{nombre_archivo}.csv"
    if archivo.exists():
        ingresar_datos(nombre_archivo, datos)
    else:
        nueva_informacion(nombre_archivo, datos)

def buscar(nombre_archivo: str):
    archivo = carpeta/f"{nombre_archivo}.csv"
    nombre=input("Ingrese el dato a buscar: ")
    with open(archivo, "r", encoding="utf-8") as f:
        lectura = csv.reader(f, delimiter="|")
        for linea in lectura:
            if linea[0] == nombre:
                print(f"Resultado: {linea}")
                break
        else:
            print("No se encentra.")
