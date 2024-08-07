'''Crea un generador (almacenado en la variable generador)
que sea capaz de devolver una secuencia infinita de números,
iniciando desde el 1, y 
entregando un número consecutivo superior cada vez que sea llamada mediante next.
'''
def generador():
    num = 0
    while(num >= 0):
        num += 1
        yield num

g = generador()
print(next(g))
print(next(g))