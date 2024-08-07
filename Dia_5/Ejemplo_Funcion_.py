'''
Ejemplo de una función para desempaquetar tuplas
'''

precios_cafe = [('capuchino',1.5), ('Expresso',1.2),('Moka',1.9)]
def cafe_caro(lista_precio):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass


    return (cafe_mas_caro,precio_mayor )