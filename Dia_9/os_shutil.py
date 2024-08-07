import os
import shutil
print(os.getcwd())

#Crear y escribir dentro de un archivo
# archivo = open('curso.txt', 'w')
# archivo.write('texto de prueba')
# archivo.close()

#Mover archivos
#shutil.move('curso.txt', 'C:\\Users\\PC\\Python\\Dia_8')

# metodo Walk para recorrer carpetas
ruta = 'C:\\Users\\PC\\Python'

for carpeta,subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for ar in archivo:
        print(f'\t{ar}')
    print('\n')