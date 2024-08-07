import Proyecto_Dia_8_Numeros

print('Bienvenido a farmacia python')

def preguntar():
    while True:

        print('''[P] - Perfumeria
[F] - Farmacia
[C] - Cosmetica''')
        try:
            area = input('Eliga una area: ').upper()
            ['P','F','C'].index(area)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            break
    Proyecto_Dia_8_Numeros.decorar_ticket(area)

def inicio():
    while True:
        preguntar()
        try:
            nuevoTurno = input('Desea Continuar [S] [N]').upper()
            ['S', 'N'].index(nuevoTurno)
        except ValueError:
            print('Esa no es una opcon valida')
        else:
            if nuevoTurno == 'N':
                print('Hasta luego')
                break

inicio()