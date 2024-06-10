'''Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
'''

archivo = open('Dia_6\mi_archivo.txt', 'w')
archivo.write('Nuevo texto')
archivo.close()

archivo_abierto = open('Dia_6\mi_archivo.txt','r')
print(archivo_abierto.read())
archivo_abierto.close()