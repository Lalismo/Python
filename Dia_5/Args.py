#Para definir argumentos se necesita el *
#El nombre que le pongas puede ser cualquiera

def suma(*args):
    return sum(args)


print(suma(5,3,6,32,13,31))