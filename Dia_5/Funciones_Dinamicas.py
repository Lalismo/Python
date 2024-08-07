

def checar_3_cifras(num):
    return num in range (100,1000)

resultado = checar_3_cifras(658)
print(resultado)
print('************')

def checar_3_cifras(lista):
    for num in lista:
        if num in range(100,1000):
            return True
        else:
            pass

resultado = checar_3_cifras([55,99,6000])
print(resultado)
print('************')


def checar_3_cifras(lista):

    lista_3_cifras = []
    for num in lista:
        if num in range(100,1000):
            lista_3_cifras.append(num)
        else:
            pass
    return lista_3_cifras

resultado = checar_3_cifras([55,999,6000])
print(resultado)