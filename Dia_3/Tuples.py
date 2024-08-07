my_tuple = (1,2,(10,20),4)
print(type(my_tuple))
print('.....')
#Extraer contenido de una tupla
print(my_tuple[0])
print(my_tuple[2][0])
print('.....')

#Se puede hacer casting para cambiar el tipo
mi_tuple = list(my_tuple)
print(type(mi_tuple))
print('.....')
#Asignar contenido de una tupla en diferentes variables
#Esto se puede hacer ya que se tiene la misma cantidad de valoes en la tupla como el numero de variables
t = (1,2,3)

x,y,z =t

print(x,y,z)
print('.....')

#Mostrar el largo de la tupla
t = (1,2,3,24,5)
print(len(t))
print('.....')
#Metodo count para tuples
#Count permite contar la cantidad de apareciones de un valor dentro de la tupla
print(t.count(1))
print('.....')

#Metodo count para consultar un valor por su indice
print(t.index(2))

#Las tuplas pueden contener cualquier tipo de objetos
