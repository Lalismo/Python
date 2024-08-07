'''
Práctica Funciones Dinámicas 1
Crea una función (todos_positivos) que reciba una lista de números como parámetro,
y devuelva True si todos los valores de una lista son positivos,
y False si al menos uno de los valores es negativo.
Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
'''

lista_numeros = [3,6,324,45,34,-3,-32,-45]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else:
            pass
    return True
        
resultado = todos_positivos(lista_numeros)
print(resultado)
