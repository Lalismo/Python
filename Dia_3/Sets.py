mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
print('.....')

#Los sets no muestran los elementos repetidos
#No aceptan listas y diccionarios, pero a las tuplas si

otro_set = set([1,2,3,4,5,5,4,4,4,3,3,3,1,1,2,2])
print(otro_set)
print('.....')

#Saber el largo de un set
print(len(otro_set))
print('.....')

#Hacer consultas
print(2 in mi_set)
print('.....')

#Metodo union
#Esta es otra forma de declarar los sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)

print(s3)
print('.....')

#Agregar más elementos
s1 = {1,2,3}
s1.add(4)
print(s1)
print('.....')

#Eliminar elementos
s1.remove(3)
print(s1)
print('.....')
#Descartar un elemento, este metodo funciona igual
#Que remove, pero si le damos un numero que no esta en el set
#No nos genera un Error
s1.discard(6)

#Pop al no tener los set un orden pop funciona de forma aleatoria
s1.pop()
print(s1)
print('.....')

#Clear limpia todos los datos que tenga el set
s1.clear()
print(s1)