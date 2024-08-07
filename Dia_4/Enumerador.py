#Enumerate se puede utilizar para sacar el indice de los objetos como una lista
#Dentro de un ciclo

lista = ['a', 'b', 'c']
for indice,item in enumerate(range(50,56)):
    print(indice,item)

mis_tuples = list(enumerate(lista))

print(mis_tuples[1][1])
    