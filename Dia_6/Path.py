from pathlib import Path

#Nos proporciona la ruta de acceso al directorio principal
base = Path.home()
print(base)
print('----------')

#Construir objetos que responden a una ruta de acceso
guia = Path('Barcelona', 'Sagradafamilia.txt')
print(guia)
print('----------')

#Creación de ruta absolita con el directorio principal y una ruta relativa
ruta_absoluta = Path(base,guia)
print(ruta_absoluta)
print('----------')

#Copiar un path creado para apuntar a un objeto distinto
guia2= ruta_absoluta.with_name('La_pedrera.txt')
print(guia2)
print('----------')

#Acceder a directorios intermedios con parent para devolver los antecesores de una ruta
print(ruta_absoluta.parent)
print(ruta_absoluta.parent.parent)
print(ruta_absoluta.parent.parent.parent)

#Enumerar archivos en un arbol de carpeta
guia = Path(Path.home(), 'Europa')
for txt in Path(guia).glob('**/*.txt'):
    print(txt)
#Construir rutas desde carpetas especificas
guia = Path('Europa', 'España','Barcelona','Sagrada_Familia.txt')
en_europa = guia.relative_to('Europa')
en_españa = guia.relative_to('Europa','España')
