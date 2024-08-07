#Generadores
def ticket_perfumeria():
    for n in range(1,100000):
        yield f'P - {n}'

def ticket_farmacia():
    for n in range(1,100000):
        yield f'F - {n}'

def ticket_cosmetica():
    for n in range(1,100000):
        yield f'C - {n}'

P = ticket_perfumeria()
F = ticket_farmacia()
C = ticket_cosmetica()

def decorar_ticket(area):
    print('Su numero es:')
    if area == "P":
        print(next(P))
    elif area == "F":
        print(next(F))
    else:
        print(next(C))
    print('Espere y sera atendido')













