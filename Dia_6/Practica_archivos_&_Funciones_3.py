'''
Práctica Archivos y Funciones 3
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro,
y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".
Finalmente, debe cerrar el archivo abierto.
'''
def registro_error(archivo):
    archivo = open(archivo,'a')
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()
    