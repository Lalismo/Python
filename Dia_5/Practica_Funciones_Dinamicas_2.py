'''
Práctica Funciones Dinámicas 2
Crea una función (suma_menores) que sume los números de una lista
(almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000,
y devuelva el resultado de dicha suma.
'''
lista_numeros = [1,45,76,23,67]
def suma_menores(lista_numeros):
    resultado = 0
    for n in lista_numeros:
        if n in range(1,1000):
            resultado += n
    return resultado

resultado = suma_menores(lista_numeros)
print(resultado)