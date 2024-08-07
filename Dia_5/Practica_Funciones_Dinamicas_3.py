'''Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen
en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
'''

lista_numeros = list(range(2,101,2))
def cantidad_pares(lista_numeros):
    cuenta = 0
    for n in (lista_numeros):
        if  n % 2 == 0:
            cuenta += 1
    return cuenta
            
    
resultado = cantidad_pares(lista_numeros)
print(resultado)


