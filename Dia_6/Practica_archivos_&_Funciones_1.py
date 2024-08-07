'''
Práctica Archivos y Funciones 1
Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
'''

def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()

abrir_leer('ejemplo.txt')

