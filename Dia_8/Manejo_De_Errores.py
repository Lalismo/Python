def suma():
    n1 = int(input('numero 1: '))
    n2 = int(input('numero 2: '))
    print(n1+n2)


try:
    # Codigo que queremos probar
    suma()
except ValueError:
    #Codigo a ejecutar si hay un error
    print('Eso no es un numero')
except TypeError:
    #Codigo a ejecutar si hay un error
    print('Estas concatenando diferentes tipos')
else:
    #Codigo a ejecutar si no hay un error
    print('Hiciste todo bien')
finally:
    #Codigo que se ejecuta de de todos modos
    print('Eso fue todo')


#Hacer mas facil el pedir un numero

def pedir_numero():
    while True:
        try:
            numero = int(input('Ingresa un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'El numero fue: {numero}')
            break
pedir_numero()