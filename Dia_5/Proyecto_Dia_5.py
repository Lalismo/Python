'''
En el juego real del ahorcado, cada vez que perdemos una vida, se va completando el dibujo
del ahorcado miembro por miembro. Pero en nuestro caso, como aún no tenemos elementos
gráficos, simplemente le vamos a decir que tiene seis vidas y se las iremos descontando de una
en una, cada vez que el jugador elija una letra incorrecta.

Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra
completa antes de perder todas las vidas, el jugador gana.

Parece sencillo, pero ¿cómo diseñamos todo este código? Bueno, aquí van algunas ayudas:
* Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
también vas a crear al comienzo.

* Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario
ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la
palabra o no, para verificar si ha ganado o no, etc.

Recuerda escribir primero las funciones y luego el código que las implementa
ordenadamente. 

'''
from random import choice

def listaPalabras():
    '''
    Selecciona aleatoriamente una palabra o frase de una lista predefinida.
    Retorna la palabra o frase en minúsculas.
    '''
    lista = ['Payday', 'Minecraft', 'Super Mario Bros', 'Mario Galaxy']
    return choice(lista).lower()

def pedirLetra():
    '''
    Solicita al usuario que introduzca una letra.
    Convierte la letra a minúsculas y la retorna.
    '''
    letra = input('Introduce una letra: ').lower()
    return letra

def mostrarPalabraOculta(palabraOculta):
    '''
    Muestra la palabra oculta al usuario,
    con letras no adivinadas representadas por guiones.
    '''
    print('Palabra: ' + ' '.join(palabraOculta))

def validarLetra(palabra, letra, palabraOculta):
    '''
    Valida si la letra introducida por el usuario está en la palabra.
    Si la letra está en la palabra, actualiza la palabra oculta en las posiciones correctas.
    Retorna la palabra oculta actualizada.
    '''
    indices = []
    for i, l in enumerate(palabra):
        if l == letra:
            indices.append(i)
    for i in indices:
        palabraOculta[i] = letra
    return palabraOculta

def jugarAhorcado(palabra):
    '''
    Valida si la letra introducida por el usuario está en la palabra.
    Si la letra está en la palabra, actualiza la palabra oculta en las posiciones correctas.
    Retorna la palabra oculta actualizada.
    '''
    palabraOculta = []
    for letra in palabra:
        if letra != ' ':
            palabraOculta.append('-')
        else:
            palabraOculta.append(' ')
    
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
