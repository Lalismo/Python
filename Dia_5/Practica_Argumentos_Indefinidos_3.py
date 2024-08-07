'''
Práctica sobre Argumentos Indefinidos (*args) 3
Crea una función llamada numeros_persona que reciba,
como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
'''
#Solucion corta

def numeros_personas(nombre,*args):
    return f'{nombre}, la suma de tus números es {sum(args)}'

print(numeros_personas('Eduardo',1,5,4))

#Solucion larga con ciclo For
def numeros_personas(nombre,*args):
    suma_numero = 0
    for arg in args:
        suma_numero += arg
    return f'{nombre}, la suma de tus números es {suma_numero}'

print(numeros_personas('Omar',1,5,4))