#Metodo para transformar una cadena de texto en mayusculas
texto = "Este es un texto de prueba"
resultado = texto.upper()
print(resultado)
print('.....')

#Metodo para transformar una cadena de texto a minuscula
texto = "Este es un texto de prueba"
resultado = texto.lower()
print(resultado)
print('.....')

#Metodo para separar elementos y los convierte a una lista
texto = "Este es un texto de prueba"
resultado = texto.split()
print(resultado)
print('.....')

#Por defecto toma como separador a los espacios,
#Pero se puede agregar un separador diferente
texto = "Este es un texto de prueba"
resultado = texto.split("t")
print(resultado)
print('.....')

#Metodo para unir elementos
#La unión de estos elementos se hace mediante una lista
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e)
print('.....')

#Metodo para buscar un determinado caracter o una palabra
#La diferencia entre index y find
#Es que al buscar un caracter que no exista en la cadena
#Este devolvera -1 para find
texto = "Este es un texto de prueba"
resultado = texto.find("e")
print(resultado)
print('.....')

#Metodo para reemplazar fragmentos de texto
#Donde el primer parametro es el texto que se quiere remplazar
#Y el segundo el que será su remplazo
texto = "Este es un texto de prueba"
resultado = texto.replace("e", "i")
print(resultado)
print('.....')