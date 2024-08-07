
#Las listas pueden contener diferentes tipos de datos
mi_lista = [34,True,"hola",123.33]
print(mi_lista)
print('.....')

#Podemos obtener el largo de nuestra lista
mi_lista = ['a', 'b', 'c']
resultado = len(mi_lista)
print(resultado)
print('.....')

#Extracción de elemento por su indice
resultado= mi_lista[0]
print(resultado)
print('.....')

resultado= mi_lista[0:2]
print(resultado)
print('.....')

#Se puede hacer concatenación de listas
mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
print(mi_lista+mi_lista2)

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista+mi_lista2
print(mi_lista3)

#Reemplazar por indice
mi_lista3[0]= "alfa"
print(mi_lista3)

#Metodo para agregar elementos, los cuales se agregan al final
mi_lista3.append("g")
print(mi_lista3)

#Metodo para eliminar elementos, el cual se elimina el ultimo si no se especifica dentro del metodo
mi_lista3.pop()
print(mi_lista3)

#Metodo para ordenar una lista
#El ordenar una lista no hace que se pueda almacenar
#En una misma linea, si se quiere almacenar se tendra que hacer por separado
lista = ['g','o','b','m','c']
lista.sort()
print(lista)

#Metodo para poner al reves la lista
lista.reverse()
print(lista)