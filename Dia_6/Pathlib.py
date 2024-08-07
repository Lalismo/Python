from pathlib import Path,PureWindowsPath

#Leer con path

carpeta = Path('C:/Users/PC/Python/Dia_6/prueba.txt')
print(carpeta.read_text())
print('---------')

#Devolver nombre del archivo

print(carpeta.name)

print('---------')
#Devolver la extension del archivo
print(carpeta.suffix)

print('---------')
#Devuelve el nombre del archivo sin la extension
print(carpeta.stem)
print('---------')

#Verificar si existe un archivo
if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial, existe')
    
print('---------')
#Transformar cualquier ruta a una ruta de windows
ruta_windows =  PureWindowsPath(carpeta)
print(ruta_windows)