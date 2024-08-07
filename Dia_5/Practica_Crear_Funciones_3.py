'''
Práctica Crear Funciones 3
Declara una función llamada cuadrado, que tome como argumento un número cualquiera,
y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.

Solo debes definir la función y crear la variable, no debes invocar la función luego.
'''
un_numero = 2
def cuadrado(num):
    print(f'La potencia del numero es: {num**2}')

cuadrado(un_numero)