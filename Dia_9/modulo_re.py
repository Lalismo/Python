'''
Caracteres especiales

caracter        descripcion         ejemplo
/d          digito numerico         \d.\d\d
/w          carecter alfanumerico   \w\w\w-\w\w
/s          espacio en blanco       numero\s\d\d
/D          No numerico             \D\D\D\D
/W          No alfanumerico         \W\W\W
/S          No espacio blanco       \S\S\S\S

Cuantificadores
caracter        descripcion         ejemplo
+           1 o más veces           codigo_\d-\d+
{n}         se repite n veces       \d-\d{4}
{n,m}       desde n hacia arriba    \w{3,5}
{n,}        desde n hacia infinito  -\d{4,}-
*           0 o mas veces           \w\s*\w
?           1 o 0                   casas?      
'''

import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

patron = 'ayuda'

#objeto busqueda que busca solo la primer aparicion de la palabra
busqueda = re.search(patron, texto)
print(busqueda)
print('---------')

#Obtener solo la información de la ubicación de la palabra con span()
busqueda = re.search(patron, texto)
print(busqueda.span())
print('---------')

#Obtener el indice inicial de la palabra a buscar
busqueda = re.search(patron, texto)
print(busqueda.start())
print('---------')

#Obtener el indice final de la palabra a buscar
busqueda = re.search(patron, texto)
print(busqueda.end())
print('---------')

#Obtener todas las busquedas de esa palabra en forma de lista
busqueda = re.findall(patron, texto)
print(busqueda)
print('---------')

#Obtener todas las ubicaciones de la palabra con span
for encontrar in re.finditer(patron,texto):
    print(encontrar.span())
print('---------')

#Buscar si existe un numero telefonico en el siguiente enunciado
texto = 'llama al 544-455-6895'

patron = r'\d\d\d-\d\d\d-\d\d\d\d'

resultado = re.search(patron,texto)
print(resultado)
print('---------')

#Obtener solo el patron a buscar
resultado = re.search(patron,texto)
print(resultado.group())
print('---------')

#Cuantificando el patron
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron,texto)
print(resultado.group())
print('---------')

#Obtener el rsultado del patron por grupos utilizando compile
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron,texto)
print(resultado.group(3))
print('---------')

#Controlar el ingreso de una clave de usuario mediante un patron
clave = input('clave')

patron = r'\D{1}\w{7}'

checar =  re.search(patron,clave)

print(checar)
print('---------')
#Buscar por palabras clave
texto = 'No atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes', texto)
print(buscar)
print('---------')

#Buscar por palabras comodin
buscar = re.search(r'....demos...', texto)
print(buscar)
print('---------')

#Buscar al comienzo se encuentra algun patron
buscar = re.search(r'^\D', texto)
print(buscar)
print('---------')

#Buscar al final si encuentra algun patron
buscar = re.search(r'\D$', texto)
print(buscar)
print('---------')

#Busca todo lo que no sea un espacio vacio y lo aguarda en una lista por cada caracter
buscar = re.findall(r'[^\s]', texto)
print(buscar)
print('---------')

#Lo mismo que la anterior peero ahora los agurapara en palabras
buscar = re.findall(r'[^\s]+', texto)
print(buscar)
print('---------')