'''
Crea un función llamada devolver_distintos() que reciba 3 integers como parámetros.

Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor

Si la suma de los 3 numeros es menor a 10, va a devolver el numero menor

Si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos) va a devolver el numero de valor intermedio

Para resolver este problema de 3 numeros
se puede hacer de la manera en utilizar metodos que ayuden a sacar
el maximo, minimo y con eso sacar el valor intermedio
pero se puede hacer tambien de manera manual sin
utilizar metodos
'''


def devolver_distintos(num1,num2,num3):
    suma = 0
    suma = num1+num2+num3
    numMayor = max(num1,num2,num3)
    numMenor = min(num1,num2,num3)
    numIntermedio = (num1+num2+num3) - numMenor -numMayor
 

    if  suma > 15:
        return f'El numero mayor es: {numMayor}'
    elif suma < 10:
        return f'El numero menor es: {numMenor}'
    elif 10 < suma < 15:
        return f'El numero intermedio es {numIntermedio}'
    
print(devolver_distintos(3,2,7))
        