def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())


#Utilizar el decorador en una variable
funcion11 = decorar_saludo(mayusculas)
funcion11('saludos')

#Utilizar el decorador en una llamada
@decorar_saludo
def minusculas(texto):
    print(texto.lower())

minusculas('QUE TAL')
