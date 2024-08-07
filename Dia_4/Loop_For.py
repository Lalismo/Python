lista = ['a', 'b', 'c']

#La diferencia entre estos 2 ciclos es
#Que el conteno del indice inicial en la ultima
#Inicia desde 1 y en la primera inicia desde 0
#Ya que en la ultima al conteo de indice se suma un 1
for letra in lista:
    numeroLetra = lista.index(letra)
    print(f'Letra {numeroLetra}: {letra}' )

for letra in lista:
    numeroLetra = lista.index(letra) + 1
    print(f'Letra {numeroLetra}: {letra}' )

print('*******************')
#Dentro de los ciclos for puedes crear condicionales
#Para decidir que se mostrara en la pantalla con cada iteración
lista = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('El nombre no comienza con L')

print('*******************')
#De igual forma en los cilcos puedes hacer expresiones matematicas
#Con los valores que estes iterando, siempre y cuando sean numeros
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor+=numero
    print(mi_valor)

print('*******************')

palabra = 'Python'

for letra in palabra:
    print(letra)

print('*******************')

for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)

print('*******************')
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

print('*******************')