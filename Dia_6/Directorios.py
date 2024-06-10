import os
#Para obtener la ruta actual en la que nos encontramos
ruta = os.getcwd()

print(ruta)

#Cambiar de directorio para acceder a cualquier carpeta que queramos
ruta = os.chdir(r'C:\Users\PC\OneDrive\Documentos')

archivo = open('otro_archivo.txt')

print(archivo.read())
print('----------')

#Crear carpeta en cualquier directorio
ruta = os.makedirs('C:\\Users\\PC\\OneDrive\\Documentos\\Dia_6')

#Separar elementos de una ruta
ruta = 'C:\\Users\\PC\\Python\\Dia_6\\prueba.txt'

#Para obtener la base o el nombre del archivo de la ruta
elemento = os.path.basename(ruta)
print(elemento)
print('----------')

#Para obtener el nombre del directorio
directorio = os.path.dirname(ruta)
print(directorio)
print('----------')

#Obtener ambos elementos en una tupla
elementos = os.path.split(ruta)
print(elementos)
print('----------')

#Eliminar carpetas
