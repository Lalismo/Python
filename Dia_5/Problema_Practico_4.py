'''
Escribe una función llamada contar_primos() que requiera un solo argumento numérico.

Esta función va a mostrar en pantalla todos los números primos existentes en el rango que va desde cero hasta ese número incluido,
y va a devolver la cantidad de números primos que encontró.

Aclaración, por convención el 0 y el 1 no se consideran primos
'''


def contar_primos(numero):
    '''
    Esta función muestra en pantalla todos los números primos existentes en el rango que va desde 2 hasta el número
    dado (incluido) y devuelve la cantidad de números primos que encontró.

    Parámetro:
    numero (int): El número hasta el cual se deben contar los números primos.

    Retorna:
    int: La cantidad de números primos encontrados.
    '''
    numeros_primos = []
    
    for n in range(2, numero + 1):
        es_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(n)
    
    print(numeros_primos)
    return len(numeros_primos)

print(contar_primos(12))