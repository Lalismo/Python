'''Práctica sobre Argumentos Indefinidos (*args) 1
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos,
y que retorne la suma de sus valores al cuadrado.



Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
'''

'''
Para utilizar bien args se necesita de variables externas
que sean declaradas como vacias si es el dado de querer pasar
los argumentos de args por ellas.
'''
def suma_cuadrado(*args):
    suma = 0
    cuadrado = 0
    for arg in (args):
        cuadrado = arg ** 2
        suma += cuadrado 
        
    return suma

print(suma_cuadrado(1,2,3))
