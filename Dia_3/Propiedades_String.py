#Ya que los string son inmutables no
#Se podría hacer lo siguiente:
'''
nombre = "Carina"
nombre[0] ="K"
print(nombre) 
'''

#Los strings se pueden multiplicar
saludo = "Hola"
print(saludo*5)
print('.....')
#Puedes hacer salto de linea con 3 comillas al inicio y al final
poema = """ Mil pequeños peces blancos
como si hirivera
el color del agua
"""
print(poema)
print('.....')
#De igual forma se puede consultar
#Si es que existe una determinada palabra o
#Caracter en la cadena de string.
print("agua" in poema)
print("sol" not in poema)
print('.....')
#También podemos saber el largo de la cadena
poema = "hola mundo!"
print(len(poema))