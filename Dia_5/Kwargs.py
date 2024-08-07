def suma(**kwargs):
    total = 0

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(x=3,y=5,z=2))

print('*********')

def prueba(num1,num2,*args,**kwargs):
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')


print(prueba(15,50,100,200,300,400,x='uno',y=5,z=2))