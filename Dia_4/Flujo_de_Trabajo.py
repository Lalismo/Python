'''El flujo de trabajo es utilizado cuando queremos que nuestro programa tome alguna desicion
IF: Si esto es
ELIF: Si esto tambien es
ELSE: si no es

'''


mascota = 'perico'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print(f'Tu mascota no es un gato ni perro es {mascota}')