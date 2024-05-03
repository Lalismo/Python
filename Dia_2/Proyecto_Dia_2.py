'''
Tu trabajas en una empresa donde los vendedores reciben comisiones del 13% por sus ventas totales,
y tu jefe quiere que ayudes a los vendedores a calcular sus comisiones creando un programa que les
pregunte su nombre y cuánto han vendido en este mes.
Tu programa le va a responder con una frase que incluya su nombre y el monto que le corresponde
por las comisiones.
'''

Nombre = input('¿Cual es tu nombre?')
MontoVendido = int(input('¿Cuanto es lo que vendiste en el mes?'))

comision = round(MontoVendido*0.13,2)
print(f'Perfecto {Nombre}. Este mes ganaste ${comision}')