
from random import choice

def listaPalabras():
    lista = ['Payday', 'Minecraft', 'Super Mario Bros', 'Mario Galaxy']
    return choice(lista).lower()  # Convertir a minúsculas para facilitar las comparaciones

def pedirLetra():
    letra = input('Introduce una letra: ').lower()  # Convertir a minúsculas para facilitar las comparaciones
    return letra

def mostrarPalabraOculta(palabraOculta):
    print('Palabra: ' + ' '.join(palabraOculta))

def validarLetra(palabra, letra, palabraOculta):
    indices = [i for i, l in enumerate(palabra) if l == letra]
    for i in indices:
        palabraOculta[i] = letra
    return palabraOculta

def jugarAhorcado(palabra):
    palabraOculta = ['-' if letra != ' ' else ' ' for letra in palabra]
    letrasIncorrectas = []
    vidas = 6

    while vidas > 0 and '-' in palabraOculta:
        mostrarPalabraOculta(palabraOculta)
        letra = pedirLetra()
        
        if letra in palabra:
            palabraOculta = validarLetra(palabra, letra, palabraOculta)
        else:
            if letra not in letrasIncorrectas:
                letrasIncorrectas.append(letra)
                vidas -= 1
            print(f'La letra no se encuentra en la palabra, te quedan {vidas} vidas')
            print(f'Letras incorrectas: {", ".join(letrasIncorrectas)}')

    if '-' not in palabraOculta:
        print('¡Felicidades! Has adivinado la palabra:', ''.join(palabraOculta))
    else:
        print('Lo siento, has perdido. La palabra era:', palabra)

# Juego principal
palabra = listaPalabras()
jugarAhorcado(palabra)

    



