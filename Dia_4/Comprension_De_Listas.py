lista = [letra for letra in 'python']
print(lista)
print('*********')

lista = [numero for numero in range(0,21,2)]
print(lista)
print('*********')

lista = [numero / 2 for numero in range(0,21,2)]
print(lista)
print('*********')

lista = [numero if numero * 2 > 10  else 'no' for numero in range(0,21,2) ]
print(lista)
print('*********')

pies = [10,20,30,40,50]

metros = [p * 3.281 for p in pies]

print(metros)