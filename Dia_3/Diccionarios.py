diccionario = {
    'c1':'valor1',
    'c2':'valor1'
}
print(type(diccionario))
print(diccionario)
print('.....')

#Extraer el contenido de una llave
resultado = diccionario['c1']
print(resultado)
print('.....')

#Los diccionarios pueden tener diferentes tipos de datos
cliente ={
    'nombre':'Eduardo',
    'apellido': 'Luna',
    'peso': 83,
    'talla':1.67
}
consulta1 = cliente['nombre']
consulta2 = cliente['peso']
print(f'El nombre del cliente es {consulta1} y tienen un peso de {consulta2}')
print('.....')

#Hasta pueden tener listas y más diccionarios dentro del mismo diccionario
dic = {
    'c1':55,
    'c2':[10,20,30],
    'c3':{
        's1':100,
        's2':200
    }
}

#Podemos ser especificos al querer imprimir o mandar a traer
#Desde que llave hasta cual indice traer si es que hay una lista o otro diccionario

#Para imprimir un indice especifico en lista se hace mediante numero
print(dic['c2'][1])

#Para imprimir un indice de diccionario se hace mediante su key
print(dic['c3']['s2'])
print('.....')

#De las siguientes 2 listas has que la letra e se imprima en mayuscula
dic = {'c1':['a','b','c'], 'c2':['d','e','f']}

print(dic['c2'][1].upper())
print('.....')

#Agregar elementos a un diccionario ya creado
dic = {1:'a',2:'b'}
print(dic)

dic[3] = 'c'
print(dic)
print('.....')
#Actualizar valor a un diccionario
dic[2] = 'B'
print(dic)
print('.....')

#Imprimir todas las keys
print(dic.keys())
print('.....')

#Imprimir todos los valores
print(dic.values())

#Imprimir todos los elementos de un diccionario
print(dic.items())
print(len(dic))

