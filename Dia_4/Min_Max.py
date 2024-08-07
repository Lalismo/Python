menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor, mayor)
print('********')

lista  = [58,96,72,64,35]
print(f'el menor es {min(lista)} y el mayor es {max(lista)}')
print('********')


nombres = ['juan', 'carlos', 'alicia', 'carlos']
print(min(nombres))
print('********')

#Aqui resulta que primero busca por numeros en mayuscula, asi que el minimo es C
nombre = 'Carlos'
print(min(nombre))

#Pero si hacemos que todas las letras sin importar que en la cadena de string sea mayuscula nos dira que a es la minima
nombre = 'Carlos'
print(min(nombre.lower()))

