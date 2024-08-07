'''Práctica sobre Interacción entre Funciones 3
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar).
Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos:
el primero, debe ser el resultado del lanzamiento de la moneda.
El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
'''
from random import choice

def lanzar_moneda():
    moneda = ['Cara','Cruz']
    return choice(moneda)

lista_numeros = [1,32,34,53,2,3]
def probar_suerte(resultado,lista):
    if resultado == 'Cara':
        return f'La lista se autodestruira {lista.clear()}'
    else:
        return f'La lista fue salvada {lista}'
    

print(probar_suerte(lanzar_moneda(),lista_numeros))
    
    