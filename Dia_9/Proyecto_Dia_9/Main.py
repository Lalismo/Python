import datetime
import os
import math
import re
from pathlib import Path
import time

ruta = 'C:\\Users\\PC\\Python\\Dia_9\\Proyecto_Dia_9\\Mi_Gran_Directorio'
patron = r'N\D{3}-\d{5}'
fecha = datetime.datetime.now()
fecha = fecha.strftime("%x")
archivo_serie = {}
inicio = time.time()


def buscar_numero(archivo, patron):
    abrir_archivo = open(archivo, 'r')
    texto = abrir_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ''
    

def crear_diccionario():
    for carpeta,subcarpeta, archivo in os.walk(ruta):
        for ar in archivo:
                serie =  buscar_numero(Path(carpeta, ar), patron)
                if serie != '':
                     archivo_serie[ar.title()] = serie.group()
    return archivo_serie
                   
             



def mostrar():
    print('-'*50) 
    print(f'Fecha de busqueda: {fecha}')
    print('''ARCHIVO \t NRO.SERIE
------- \t ----------''')
    for key, value in diccionario.items():
     print(key +'\t'+ value)
    print(f'\nNumeros encontrados {len(diccionario)}')
    fin = time.time()
    duracion =  fin-inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')

diccionario = crear_diccionario() 
mostrar()



