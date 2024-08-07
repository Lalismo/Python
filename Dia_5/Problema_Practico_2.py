'''
Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro,
y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.

Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver ['d','e','i','n','o','r','t']
'''

def ordenar(palabra):
    '''
    Creación de 2 listas vacias
    La primera para almacenar 1 por 1
    con el ciclo for y la otra para
    eliminar los items duplicados con set y
    ordenarlos en orden alfabetico
    '''
    lista = []
    nuevalista = []
    
    for n in palabra:
        lista.append(n)
    nuevalista = list(set(lista))
    nuevalista.sort()
        
    return nuevalista
    
print(ordenar('cascarrabias'))
