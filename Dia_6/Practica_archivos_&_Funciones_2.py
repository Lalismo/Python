'''
Práctica Archivos y Funciones 2
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro,
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
'''
def sobrescribir(archivo):
    archivo = open(archivo, 'w')
    return archivo.write('contenido eliminado')