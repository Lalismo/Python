'''Práctica Enumerador 2
Crea una lista formada por las tuplas (indice, elemento),
formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices .
'''
#Un string puede pasar directamente a formar una lista de tuplas 
#Con solo utilizar enumerate y dentro de el mandar a llamar al string
nombre = 'Python'
lista_indices = list(enumerate(nombre))
print(lista_indices)

