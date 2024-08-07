#Para que un loop while pare es necesario tener una variable
#que haga que el valor de la condicion decremente o incremente
#Dependiendo de la condición que tenga el while para que este se pare
monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else: print('Ya no tienes monedas')
print('**********')

respuesta = 's'
while respuesta == 's':
    respuesta = input('quieres seguir? (s/n)')
else: 
    print('Gracias')