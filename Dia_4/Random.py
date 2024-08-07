from random import *

#randint para numeros enteros aleatorios
aleatorio = randint(1,50)
print(aleatorio)
print('*****')

#uniform para numeros decimales aleatorios
aleatorio = round(uniform(1,5),1)
print(aleatorio)
print('*****')

#random automaticamente escoje un numero del 0 a 1 de forma decimal
aleatorio = round(random(),3)
print(aleatorio)


#choice una seleccion aleatoria dentro de los elementos de una coleccion

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

#Mescla todos los elementos dentro de una collección
numeros = list(range(5,51, 5))
shuffle(numeros)
print(numeros)