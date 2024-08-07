'''
Práctica sobre Argumentos Indefinidos (**kwargs) 2
Crea una función llamada lista_atributos que devuelva en forma
de lista los valores de los atributos entregados en forma de palabras clave (keywords).
La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
'''
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

print(lista_atributos(x=76,y=5,z=2))