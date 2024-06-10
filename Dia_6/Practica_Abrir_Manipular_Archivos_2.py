'''
Práctica Abrir y Manipular Archivos 2
Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
'''

mi_archivo = open('Dia_6\prueba.txt')
print(mi_archivo.readline())
mi_archivo.close()